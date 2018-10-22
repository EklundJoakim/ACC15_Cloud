#Settings for vm

sudo apt-get update
sudo apt-get install -y python3-pip
sudo pip3 install -U Celery
sudo apt install -y python-celery-common
sudo pip3 install flask
sudo pip3 install numpy
sudo apt-get install -y octave
sudo pip3 install oct2py
sudo pip3 install scipy
sudo apt get install -y pyhton3-opestackclient
sudo apt install -y rabbitmq-server

# Username: ACC15
# Password: pwd
# Vhost: myvhost
# User tags: mytag

sudo rabbitmqctl add_user ACC15 pwd
sudo rabbitmqctl add_vhost myvhost
sudo rabbitmqctl set_user_tags ACC15 mytag
sudo rabbitmqctl set_permissions -p myvhost ACC15 ".*" ".*" ".*"
