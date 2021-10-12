from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import pickle
import colorama
from colorama import Fore
colorama.init(autoreset=True)

username = 'ravidubey6141'
password = 'Iknowiamawesome'        

def main():
    global driver
    driver = webdriver.Chrome(executable_path='D:\Gourav\Scripts\School_Project\chromedriver.exe')
    driver.get('https://www.instagram.com')
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    sleep(5)
    usr_inpt = driver.find_element_by_name('username')
    passd_inpt = driver.find_element_by_name('password')

    usr_inpt.send_keys(username)
    passd_inpt.send_keys(password)

    #login btn
    driver.find_element_by_xpath("//button[@type='submit']").click()

    sleep(3)
    #not now notfi
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

def like_posts():
    sleep(3)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']"))).send_keys(accnt_name)
    sleep(4)
    try:
        driver.find_element_by_xpath(f'//a[@href=\"/{accnt_name}/\"]').click()
    except:
        driver.close()
        print(Message)
        print(Message2)
        print(Options)
        print(Fore.LIGHTRED_EX + '\n[-] Provided account not found.')
        main_menu()
    
    sleep(3)
    if 'This account is private' in driver.page_source:
        driver.close()
        print(Message)
        print(Message2)
        print(Options)
        print(Fore.LIGHTRED_EX + "\n[-] Given account is private, commands can't be performed")
        main_menu()



Message = Fore.GREEN + '''                                                                                                       
            ___ _   _ ____ _____  _    ____   ___ _____ 
            |_ _| \ | / ___|_   _|/ \  | __ ) / _ |_   _|
             | ||  \| \___ \ | | / _ \ |  _ \| | | || |  
             | || |\  |___) || |/ ___ \| |_) | |_| || |  
            |___|_| \_|____/ |_/_/   \_|____/ \___/ |_|  
                                                                                        
                                             
'''

Message2 = '''


            This is just a small project of a Instagram bot,
            Please don't use this program to do illegal work,
            We will not be responsible for that..


            Note that we'll be using a demo account for the
            presentation of this program.
            
            Thank you.'''

print(Message)
print(Message2)

Options = '''

    1. Like all posts of a specific person in Instagram.
    2. Spam direct messages to someone in Instgram.
    3. commment on a person random post.

'''

print(Options)

def main_menu():
    command = input('command--> ')
    if command == '1':
        print(Fore.LIGHTYELLOW_EX + '\n[#] The account name should be correct or program will terminate itself automatically.\n')
        global accnt_name
        accnt_name = input(str('Account Name: '))
        print(Fore.LIGHTGREEN_EX + '\n [*] Let the bot do his work...\n')
        sleep(3)
        main()
        like_posts()

    else:
        print(Fore.LIGHTRED_EX + '[-] Please select from the above options.')
        main_menu()


main_menu()