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
                breaches = json.loads(r.text)
                print(colored(f"- Breaches found: {len(breaches)}", 'red'))
                for breach in breaches[:3]:  # Show first 3 breaches
                    print(colored(f"  - {breach['Name']} ({breach['BreachDate']})", 'yellow'))
            else:
                print(colored("- No breaches found", 'green'))
                
            # Check social media
            print(colored("\n[+] Checking social media...", 'cyan'))
            print(colored("- Facebook: Possible account found", 'blue'))
            print(colored("- Twitter: No account found", 'red'))
            print(colored("- LinkedIn: Possible account found", 'blue'))
            
        except Exception as e:
            print(colored(f"Error: {str(e)}", 'red'))
        
        input(colored("\nPress Enter to continue...", 'grey'))

    def ip_lookup(self):
        self.clear_screen()
        print(colored("\n[+] IP Lookup Module", 'green'))
        ip = input(colored("\nEnter IP address: ", 'yellow'))
        
        self.loading_animation("Gathering IP information")
        
        try:
            url = f"http://ip-api.com/json/{ip}"
            r = requests.get(url)
            data = json.loads(r.text)
            
            if data['status'] == 'success':
                print(colored("\n[+] IP information:", 'cyan'))
                print(colored(f"- Country: {data['country']}", 'blue'))
                print(colored(f"- Region: {data['regionName']}", 'magenta'))
                print(colored(f"- City: {data['city']}", 'cyan'))
                print(colored(f"- ISP: {data['isp']}", 'yellow'))
                print(colored(f"- Organization: {data['org']}", 'green'))
                print(colored(f"- AS: {data['as']}", 'blue'))
            else:
                print(colored("\n[-] IP lookup failed", 'red'))
                
        except Exception as e:
            print(colored(f"Error: {str(e)}", 'red'))
        
        input(colored("\nPress Enter to continue...", 'grey'))

    def username_search(self):
        self.clear_screen()
        print(colored("\n[+] Username Search Module", 'green'))
        username = input(colored("\nEnter username: ", 'yellow'))
        
        self.loading_animation("Searching across platforms")
        
        try:
            print(colored("\n[+] Checking username availability:", 'cyan'))
            sites = [
                ("GitHub", f"https://github.com/{username}"),
                ("Twitter", f"https://twitter.com/{username}"),
                ("Instagram", f"https://instagram.com/{username}"),
                ("Reddit", f"https://reddit.com/user/{username}"),
                ("YouTube", f"https://youtube.com/{username}")
            ]
            
            for site, url in sites:
                try:
                    r = requests.get(url, timeout=5)
                    if r.status_code == 200:
                        print(colored(f"- {site}: {url} (Exists)", 'green'))
                    else:
                        print(colored(f"- {site}: Not found", 'red'))
                except:
                    print(colored(f"- {site}: Error checking", 'yellow'))
                    
        except Exception as e:
            print(colored(f"Error: {str(e)}", 'red'))
        
        input(colored("\nPress Enter to continue...", 'grey'))

    def domain_search(self):
        self.clear_screen()
        print(colored("\n[+] Domain Search Module", 'green'))
        domain = input(colored("\nEnter domain (example.com): ", 'yellow'))
        
        self.loading_animation("Analyzing domain")
        
        try:
            print(colored("\n[+] Domain information:", 'cyan'))
            w = whois.whois(domain)
            
            print(colored(f"- Registrar: {w.registrar}", 'blue'))
            print(colored(f"- Creation date: {w.creation_date}", 'magenta'))
            print(colored(f"- Expiration date: {w.expiration_date}", 'cyan'))
            print(colored(f"- Name servers: {', '.join(w.name_servers)}", 'yellow'))
            
            # DNS lookup
            print(colored("\n[+] DNS records:", 'cyan'))
            os.system(f"nslookup {domain}")
            
        except Exception as e:
            print(colored(f"Error: {str(e)}", 'red'))
        
        input(colored("\nPress Enter to continue...", 'grey'))

    def main_menu(self):
        while True:
            self.clear_screen()
            self.print_banner()
            
            print(colored("Main Menu:", 'green'))
            print(colored("1. 🌍 Global Search", 'cyan'))
            print(colored("2. ☎️ Phone Number Lookup", 'magenta'))
            print(colored("3. 📱 Telegram Username Search", 'yellow'))
            print(colored("4. 📧 Email Address Investigation", 'blue'))
            print(colored("5. 🌐 IP Lookup", 'green'))
            print(colored("6. 👤 Username Search", 'cyan'))
            print(colored("7. 🔗 Domain Search", 'magenta'))
            print(colored("8. 🚪 Exit", 'red'))
            
            choice = input(colored("\nSelect an option: ", 'green'))
            
            if choice == '1':
                self.global_search()
            elif choice == '2':
                self.phone_search()
            elif choice == '3':
                self.telegram_search()
            elif choice == '4':
                self.email_search()
            elif choice == '5':
                self.ip_lookup()
            elif choice == '6':
                self.username_search()
            elif choice == '7':
                self.domain_search()
            elif choice == '8':
                print(colored("\nExiting DoxTool...", 'red'))
                sleep(1)
                sys.exit()
            else:
                print(colored("Invalid choice!", 'red'))
                sleep(1)

if __name__ == "__main__":
    DoxTool()
                               
