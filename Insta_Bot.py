from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
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

def account_locate():
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


def spam_messages():
    try:
        driver.find_element_by_css_selector("span[class='vBF20 _1OSdk']").click()
        sleep(3)
        driver.find_element_by_css_selector("button[class='sqdOP  L3NKy    _8A5w5    ']").click()
        sleep(3)
        msg_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        for i in range(0, n_times):
            msg_box.send_keys(spam_msg)
            msg_box.send_keys(Keys.ENTER)
            sleep(0.1)

    except Exception as E:
        driver.close()
        print(Message)
        print(Message2)
        print(Options)
        print(Fore.LIGHTRED_EX + '\n\n[-] Some error occured, sorry for the inconvenience')
        print(E)
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

            Note that we are using a demo account for the
            presentation of this program.
            
            Thank you.'''

print(Message)
print(Message2)

Options = '''
    OPTIONS:-

    1. Like random post of a sepcific person.
    2. Spam direct messages to someone.
    3. commment on a person's random post.

    options - to show the options.

'''

print(Options)

def main_menu():
    command = input('command--> ')
    if command == 'options'.lower():
        print(Options)
        main_menu()
    elif command == '1':
        print(Fore.LIGHTYELLOW_EX + '\n[#] The account name should be correct or program will terminate itself automatically.\n')
        global accnt_name
        accnt_name = input(str('Account Name: '))
        print(Fore.LIGHTGREEN_EX + '\n [*] Let the bot do his work...\n')
        sleep(3)
        main()
        account_locate()

    elif command == '2':
        print('\n can only spam public accounts\n')
        accnt_name = input(str('Account Name: '))

        try:
            global n_times
            n_times = int(input('\nHow many messages you want to send: '))
        except Exception as E:
            print(E)
            main_menu()

        global spam_msg
        spam_msg = input('\nMessage you want to spam: ')
        print(Fore.LIGHTGREEN_EX + '\n [*] Spamming messages...\n')
        main()
        account_locate()
        spam_messages()


    else:
        print(Fore.LIGHTRED_EX + '[-] Please select from the above options.')
        main_menu()


main_menu()