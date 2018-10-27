# http://docs.openstack.org/developer/python-novaclient/ref/v2/servers.html
import time, os, sys
import inspect
from os import environ as env

from  novaclient import client
import keystoneclient.v3.client as ksclient
from keystoneauth1 import loading
from keystoneauth1 import session

flavor = "ACCHT18.large"
private_net = "SNIC 2018/10-30 Internal IPv4 Network"
floating_ip_pool_name = "Public External IPv4 network"
image_name = "Ubuntu 16.04 LTS (Xenial Xerus) - latest"

def init_instance():
    #loader = loading.get_plugin_loader('password')

    auth = loader.load_from_options(auth_url= 'https://uppmax.cloud.snic.se:5000/v3',
                                    username='s11798',
                                    password='password1',
                                    project_name= 'SNIC 2018/10-30',
                                    project_domain_name='snic',
                                    project_id= '2344cddf33a1412b846290a9fb90b762',
                                    user_domain_name='snic')

    sess = session.Session(auth=auth)
    nova = client.Client('2.1', session=sess)
    print ("user authorization completed.")

    image = nova.glance.find_image(image_name)

    flavor = nova.flavors.find(name=flavor)

    try:
        nova.floating_ip_pools.list()
        floating_ip = nova.floating_ips.create(nova.floating_ip_pools.list()[0].name)
    except Exception as e:
        return json.dumps({"success": False, 'message': e.message})

    if private_net != None:
        net = nova.neutron.find_network(private_net)
        nics = [{'net-id': net.id}]
    else:
        sys.exit("private-net not defined.")

    #print("Path at terminal when executing this file")
    #print(os.getcwd() + "\n")
    cfg_file_path =  os.getcwd()+'/cloud-cfg.txt'
    if os.path.isfile(cfg_file_path):
        userdata = open(cfg_file_path)
    else:
        sys.exit("cloud-cfg.txt is not in current working directory")

    secgroups = ['default', 'hungphan_security_c1']

    print ("Creating instance ... ")
    instance = nova.servers.create(name="acc-15-new-vm", image=image, flavor=flavor, userdata=userdata, nics=nics,security_groups=secgroups)
    inst_status = instance.status
    print ("waiting for 10 seconds.. ")
    time.sleep(10)
    while inst_status == 'BUILD':
        print ("Instance: "+instance.name+" is in "+inst_status+" state, sleeping for 5 seconds more...")
        time.sleep(5)
        instance = nova.servers.get(instance.id)
        inst_status = instance.status

    instance.add_floating_ip(floating_ip)
    print ("Instance: "+ instance.name +" is in " + inst_status + "state")
    return json.dumps({'success': True,
						'id': instance.id,
						'name': instance.name,
						'floating_ip': floating_ip.ip,
						'private_ip': instance.networks[private_net][0],
						'status': inst_status})
