#!/bin/bash
clear
echo -e "\e[1;36mInstalling DoxSoft...\e[0m"
sleep 2

# Update packages
echo -e "\e[1;33mUpdating packages...\e[0m"
pkg update -y

# Install dependencies
echo -e "\e[1;33mInstalling dependencies...\e[0m"
pkg install -y python git python-pip

# Install Python modules
echo -e "\e[1;33mInstalling Python modules...\e[0m"
pip install termcolor pyfiglet phonenumbers requests

# Set permissions
chmod +x doxsoft.py

echo -e "\e[1;32mInstallation complete!\e[0m"
echo -e "\e[1;34mRun: python doxsoft.py\e[0m"
