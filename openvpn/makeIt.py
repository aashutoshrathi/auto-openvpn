from datetime import timedelta
import datetime
import sys
import re
import os
import selenium
from selenium import webdriver
import random
import string
import pyperclip


def update():
    os.system("pip install --upgrade auto-openvpn")

def show_help():
    print("Usage: aovpn [OPTIONS] username [USERNAME]")
    print("If you don't enter any username, it randomly assignes you one.")
    print("Options:\n  General Options:")
    print("    -h, --help                       Print this help text and exit")
    # print("    --version                        Print program version and exit")
    print("    -U, --update                     Update this program to latest version. Make sure that you have sufficient permissions (run with sudo if needed)")


def login(un=None, arg=None):
    print("This might take time, just sit back and relax....")
    options = webdriver.ChromeOptions()

    prefs = {'profile.managed_default_content_settings.images':2}
    options.add_experimental_option("prefs", prefs)

    options.set_headless(True)
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('log-level=3')

    if un == None:
        un = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))

    driver = webdriver.Chrome(chrome_options=options)
    # driver = webdriver.PhantomJS('C:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
    driver.get('https://www.tcpvpn.com/home')

    print("Creating OpenVPN account for " + un + ".\nThis may take upto 20 seconds....")

    asia = driver.find_element_by_xpath('//*[@id="plans"]/div/div/div[1]/div/a')
    asia.click()

    india = driver.find_element_by_xpath('//*[@id="blockblockB"]/div[3]/div/div[2]/div/div[2]/a')
    india.click()

    create = driver.find_element_by_xpath('//*[@id="udp"]/div[2]/div/form/button')
    create.submit()

    ed = datetime.date.today() + timedelta(days=5)
    ed_formatted = ed.strftime('%d/%m/%Y')

    try:
        input = driver.find_element_by_name("username")
        input.send_keys(un)
        input = driver.find_element_by_name("password")
        input.send_keys('test')

        makeIt = driver.find_element_by_xpath('//*[@id="edit-profile"]/button')
        makeIt.click()
        finalUsername = "udpvpn.com-" + un
        password = "test"
        print("Username: " + finalUsername + " (Copied to your clipboard)")
        print("Password: " + password)
        print("Valid till " + ed_formatted)
        pyperclip.copy(finalUsername)        

    except selenium.common.exceptions.NoSuchElementException:
        print('Something went horribly wrong :(')
    
    return password



def run():
    if len(sys.argv) > 1:
        if(sys.argv[1] == "--help" or sys.argv[1] == "-h"):
            show_help()
        elif(sys.argv[1] == "--update" or sys.argv[1] == "-U"):
            update()
        elif len(sys.argv) == 2:
            login(sys.argv[1])
    if len(sys.argv) == 1:
        login()
    else:
        print("Incorrect call, you can type aovpn --help for help")

if __name__ == '__main__':
	run()