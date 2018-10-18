#Settings for vm

sudo apt-get update
sudo apg-get upgrade
sudo apt-get install python-pip
sudo pip install -U Celery
sudo apt install -y python-celery-common
sudo pip install flask
sudo apt-get install -y octave
sudo pip install oct2py
sudo apt-get install -y python-scipy
sudo apt install rabbitmq-server

# Username: ACC15
# Password: pwd
# Vhost: myvhost
# User tags: mytag

sudo rabbitmqctl add_user ACC15 pwd
sudo rabbitmqctl add_vhost myvhost
sudo rabbitmqctl set_user_tags ACC15 mytag
sudo rabbitmqctl set_permissions -p myvhost ACC15 ".*" ".*" ".*"
