'''
Version 0.1
By Chouaibcher
2024/07/09
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time
import platform

# change this 
url = "https://chouaibcher.com"


def play_alert_sound():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(500, 10000)  # Frequency and duration in milliseconds
    else:
        import os
        # Using the `afplay` command for macOS, `aplay` for Linux
        if platform.system() == "Darwin":
            os.system('afplay /System/Library/Sounds/Ping.aiff')  # Change the file path to an actual sound file if needed
        else:
            os.system('aplay /usr/share/sounds/alsa/Front_Center.wav')  # Change the file path to an actual sound file if needed


service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

while True:
    try:
        driver.get(url)
        if driver.title != "Error":
            print("Successfully connected!")
            play_alert_sound()
            break
        else:
            print("Failed to load the page, retrying...")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(5)  # Wait for 5 seconds before retrying

#driver.quit()
