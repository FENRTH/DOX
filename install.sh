#!/bin/bash
clear
echo -e "\e[1;36mInstalling Advanced DoxTool...\e[0m"
sleep 2

# Update and upgrade packages
echo -e "\e[1;33mUpdating packages...\e[0m"
pkg update -y && pkg upgrade -y

# Install essential dependencies
echo -e "\e[1;33mInstalling dependencies...\e[0m"
pkg install -y python git wget curl php ruby nmap openssh

# Install Python modules
echo -e "\e[1;33mInstalling Python modules...\e[0m"
pip install --upgrade pip
pip install requests bs4 phonenumbers python-whois pyfiglet termcolor mechanize selenium

# Install additional tools
echo -e "\e[1;33mInstalling additional tools...\e[0m"
gem install lolcat
pkg install -y libxml2 libxslt
pip install lxml

# Clone repositories for additional functionality
echo -e "\e[1;33mSetting up additional resources...\e[0m"
git clone https://github.com/sherlock-project/sherlock.git
cd sherlock && python -m pip install -r requirements.txt && cd ..

git clone https://github.com/htr-tech/zphisher.git

# Set permissions
chmod +x doxtool.py

echo -e "\e[1;32mInstallation complete!\e[0m"
echo -e "\e[1;34mRun: python doxtool.py\e[0m"
echo -e "\e[1;35mPassword: XDOSTOOL\e[0m"
