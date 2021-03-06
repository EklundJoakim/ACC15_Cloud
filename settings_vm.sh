sudo apt-get update
sudo apt-get install -y python3-pip
export LC_ALL=C
sudo pip3 install -U Celery
sudo apt install -y python-celery-common
sudo pip3 install flask
sudo pip3 install numpy
sudo apt-get install -y octave
sudo pip3 install oct2py
sudo pip3 install scipy

sudo apt install software-properties-common
sudo add-apt-repository cloud-archive:rocky
sudo apt-get update
sudo pip3 install python-openstackclient

sudo apt install -y docker.io
sudo apt install -y rabbitmq-server

# Username: ACC15
# Password: pwd
# Vhost: myvhost
# User tags: mytag

sudo rabbitmqctl add_user ACC15 pwd
sudo rabbitmqctl add_vhost myvhost
sudo rabbitmqctl set_user_tags ACC15 mytag
sudo rabbitmqctl set_permissions -p myvhost ACC15 .* .* .*

