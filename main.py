from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from sys import platform
import string    
import random
from time import sleep
import os
import time

tab_number = 0

link = "http://s0urce.io/"
    
print("source rocks $$")

JS_ADD_TEXT_TO_INPUT = """
  var elm = arguments[0], txt = arguments[1];
  elm.value += txt;
  elm.dispatchEvent(new Event('change'));
  """

chrome_options = Options()
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument("--no-sandbox")
wd = wd.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

def create_bot(tab):
    if tab != 0:
        wd.execute_script("window.open('');")
        wd.switch_to.window(wd.window_handles[tab])
    
    wd.get(link)
        
    loginInput = wd.find_element_by_id('login-input')
    if tab == 0:
        wd.execute_script(JS_ADD_TEXT_TO_INPUT, loginInput, "👌︎ rockstar")
    loginInput.send_keys(Keys.ENTER)

for i in range(30):
    create_bot(tab_number)
    tab_number += 1