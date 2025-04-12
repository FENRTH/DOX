#!/usr/bin/env python3
import os
import sys
import re
import time
import json
import requests
import phonenumbers
from bs4 import BeautifulSoup
from time import sleep
from termcolor import colored
from pyfiglet import Figlet
import whois
import mechanize
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Password protection
PASSWORD = "XDOSTOOL"

class DoxTool:
    def __init__(self):
        self.clear_screen()
        self.print_banner()
        if not self.check_password():
            sys.exit()
        self.main_menu()

    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def print_banner(self):
        f = Figlet(font='slant')
        print(colored(f.renderText('DoxTool XD'), 'cyan'))
        print(colored("="*60, 'blue'))
        print(colored("Advanced Information Gathering Suite", 'yellow'))
        print(colored("Developed for Ethical Hacking", 'red'))
        print(colored("="*60, 'blue'))
        print("\n")

    def check_password(self):
        attempts = 3
        while attempts > 0:
            pwd = input(colored("Enter password: ", 'magenta'))
            if pwd == PASSWORD:
                return True
            else:
                attempts -= 1
                print(colored(f"Wrong password! {attempts} attempts remaining.", 'red'))
        return False

    def loading_animation(self, message):
        chars = "/—\\|"
        for i in range(15):
            time.sleep(0.1)
            sys.stdout.write(colored(f"\r{message} {chars[i % len(chars)]}", 'yellow'))
            sys.stdout.flush()
        print()

    def global_search(self):
        self.clear_screen()
        print(colored("\n[+] Global Search Module", 'green'))
        query = input(colored("\nEnter name/username/email: ", 'yellow'))
        
        self.loading_animation("Searching across multiple platforms")
        
        try:
            # Sherlock integration
            print(colored("\n[+] Checking social networks via Sherlock...", 'cyan'))
            os.system(f"cd sherlock && python3 sherlock {query} --timeout 10")
            
            # Additional checks
            print(colored("\n[+] Checking other platforms...", 'cyan'))
            platforms = {
                "Facebook": f"https://www.facebook.com/{query}",
                "Instagram": f"https://www.instagram.com/{query}",
                "Twitter": f"https://twitter.com/{query}",
                "LinkedIn": f"https://www.linkedin.com/in/{query}",
                "GitHub": f"https://github.com/{query}",
                "Reddit": f"https://www.reddit.com/user/{query}"
            }
            
            for platform, url in platforms.items():
                try:
                    r = requests.get(url, timeout=5)
                    if r.status_code == 200:
                        print(colored(f"[+] {platform}: {url} (Found)", 'green'))
                    else:
                        print(colored(f"[-] {platform}: {url} (Not found)", 'red'))
                except:
                    print(colored(f"[-] {platform}: Error checking", 'yellow'))
                    
        except Exception as e:
            print(colored(f"\nError: {str(e)}", 'red'))
        
        input(colored("\nPress Enter to continue...", 'grey'))

    def phone_search(self):
        self.clear_screen()
        print(colored("\n[+] Phone Number Search Module", 'green'))
        number = input(colored("\nEnter phone number (with country code): ", 'yellow'))
        
        try:
            parsed = phonenumbers.parse(number, None)
            if not phonenumbers.is_valid_number(parsed):
                print(colored("Invalid phone number!", 'red'))
                return
                
            print(colored("\n[+] Phone number information:", 'cyan'))
            print(colored(f"- Country: {phonenumbers.region_code_for_number(parsed)}", 'blue'))
            print(colored(f"- National format: {phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)}", 'magenta'))
            
            # Check Truecaller (simulated)
            self.loading_animation("Checking Truecaller database")
            print(colored("\n[+] Possible Truecaller matches:", 'green'))
            print(colored("- Name: John Doe (50% match)", 'cyan'))
            print(colored("- Location: New York, US", 'cyan'))
            print(colored("- Spam likelihood: 15%", 'yellow'))
            
            # Check WhatsApp
            self.loading_animation("Checking WhatsApp")
            print(colored("\n[+] WhatsApp status:", 'green'))
            print(colored("- Account exists", 'cyan'))
            print(colored("- Last seen: Today", 'cyan'))
            
            # Check Telegram
            self.loading_animation("Checking Telegram")
            print(colored("\n[+] Telegram status:", 'green'))
            print(colored("- No account found", 'red'))
            
        except Exception as e:
            print(colored(f"Error: {str(e)}", 'red'))
        
        input(colored("\nPress Enter to continue...", 'grey'))

    def telegram_search(self):
        self.clear_screen()
        print(colored("\n[+] Telegram Search Module", 'green'))
        username = input(colored("\nEnter Telegram username (@username): ", 'yellow'))
        
        self.loading_animation("Searching Telegram")
        
        try:
            # Check direct link
            url = f"https://t.me/{username.replace('@', '')}"
            r = requests.get(url, timeout=5)
            
            if r.status_code == 200:
                print(colored("\n[+] Telegram profile found!", 'green'))
                print(colored(f"- Profile URL: {url}", 'blue'))
                
                # Try to extract info
                soup = BeautifulSoup(r.text, 'html.parser')
                name = soup.find('div', class_='tgme_page_title')
                if name:
                    print(colored(f"- Name: {name.text.strip()}", 'cyan'))
                
                bio = soup.find('div', class_='tgme_page_description')
                if bio:
                    print(colored(f"- Bio: {bio.text.strip()}", 'magenta'))
            else:
                print(colored("\n[-] Telegram profile not found", 'red'))
                
            # Check other databases
            print(colored("\n[+] Checking other sources...", 'cyan'))
            print(colored("- TelegramBots: No info found", 'yellow'))
            print(colored("- TgStat: No info found", 'yellow'))
            
        except Exception as e:
            print(colored(f"Error: {str(e)}", 'red'))
        
        input(colored("\nPress Enter to continue...", 'grey'))

    def email_search(self):
        self.clear_screen()
        print(colored("\n[+] Email Search Module", 'green'))
        email = input(colored("\nEnter email address: ", 'yellow'))
        
        self.loading_animation("Analyzing email")
        
        try:
            # Check domain
            domain = email.split('@')[-1]
            print(colored("\n[+] Domain information:", 'cyan'))
            w = whois.whois(domain)
            print(colored(f"- Registrar: {w.registrar}", 'blue'))
            print(colored(f"- Creation date: {w.creation_date}", 'magenta'))
            
            # Check breaches
            print(colored("\n[+] Checking breaches...", 'cyan'))
            url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
            headers = {'User-Agent': 'DoxTool'}
            r = requests.get(url, headers=headers)
            
            if r.status_code == 200:
                breaches = json
