from selenium import webdriver
import time, pyfirmata, getpass
from keyboard import press
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import PySimpleGUI as sg


img = Image.open(r'./simp.jpg')


try:
    from twitchInfo import username, password

except:
    layout = [ [sg.Text('Simp', font="Helvetica 18")],
            [sg.Text('Twitch Username:'), sg.InputText(key = "username") ],
            [sg.Text('Twitch Password:'), sg.InputText(key = "password", password_char="*") ],
            [sg.Checkbox('Remember Me', key="remember")],
            [sg.Button('ok'), sg.Button('cancel')]
            ]

    window = sg.Window('Testing',layout)

    while True:
        event, values = window.read()

        username = values["username"]
        password = values["password"]
        remember = values["remember"]

        if remember == True:
            with open('./twitchInfo.py', 'w+') as h:
                h.write(f"username = '{username}'\n")
            with open('./twitchInfo.py', 'a+') as i:
                i.write(f"password = '{password}'")

        if event in (None, "ok", "cancel"):
            break

    window.close()




def simpbot():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://pokimane.tv/tip')
    driver.maximize_window()

    time.sleep(1)

    id_box = driver.find_element_by_name('username')
    id_box.send_keys('simpboy\t2\tI want to lick your beautiful feet, you sexy gazelle\t\t\t')
    press('enter')

    driver.get("https://streamlabs.com/login?r=%2Fglobal%2Fidentity%3Fpopup%3D1%26r%3Dhttps%3A%2F%2Fpokimane.tv%2Ftip&amp;popup=1&amp;domain=pokimane.tv&amp;dto=c38fcfc1248dd829ae6c9d0d911e3a9d&amp;limited=1")
    login = driver.find_element_by_id('connect-with-twitch')
    login.click()
    twitchUN = driver.find_element_by_id('login-username')
    twitchUN.send_keys(f"{username}\t{password}\t\t")
    press('enter')
    img.show()

board = pyfirmata.Arduino('/dev/cu.usbmodem14101')

it = pyfirmata.util.Iterator(board)
it.start()

digital_input = board.get_pin('d:10:i')

while True:
    sw = digital_input.read()
    if sw is True:
        simpbot()
        
    time.sleep(0.1)
