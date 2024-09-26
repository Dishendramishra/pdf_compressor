#!/bin/bash
cd ~
sudo apt update
sudo apt install -y git ghostscript
sudo apt install -y imagemagick

# Installing and enabling apache
sudo apt install -y apache2 libapache2-mod-wsgi-py3
sudo systemctl start apache2
sudo systemctl enable apache2
# add the apache2 user (usually www-data for Ubuntu) to the personal group 
# of the current user (the group with the same name as the user name):
sudo adduser www-data $(whoami)

# installing pip and pipenv module for python https://pypi.org/project/pipenv/
sudo apt install -y python3-pip
sudo pip install pipenv

# cloning project repo
git clone https://github.com/Dishendramishra/pdf_compressor
cd ./pdf_compressor
# making essentials directories
mkdir logs
mkdir data

pipenv install 
pipenv --venv > env_path.txt
sed -i "s/\${username}/$USER/" pdf_compressor.conf
sed -i "s/\${username}/$USER/" app.wsgi
sudo cp pdf_compressor.conf /etc/apache2/sites-available/
sudo a2dissite '*'
sudo a2ensite pdf_compressor.conf
sudo chmod -R 750 ~/.local/share/

# increasing timeout on apache 
sudo sed -i 's@Timeout 300@TimeOut 600@g' /etc/apache2/apache2.conf

sudo systemctl reload apache2 && sudo systemctl restart apache2