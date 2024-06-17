import pyautogui
import cv2
import time
import threading
import os
import sys

# Determine the directory of the executable
if getattr(sys, 'frozen', False):
    base_dir = os.path.dirname(sys.executable)
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

# Load the config.py file
config_path = os.path.join(base_dir, 'config.py')
if os.path.exists(config_path):
    exec(open(config_path).read())
else:
    raise FileNotFoundError(f"Configuration file not found: {config_path}")

def main():
    def task():
        searchCoordsFinal = click_image_found("search.png")
        pickCoords = click_image_found("None.png", "move")
        lockInCoords = click_image_found("bangrey.png")
        def select_champion(champion):
            nonlocal searchCoordsFinal
            nonlocal pickCoords
            nonlocal lockInCoords
            pyautogui.click(searchCoordsFinal)
            pyautogui.press('backspace', presses=15)
            pyautogui.typewrite(champion)
            time.sleep(1)
            pyautogui.click(pickCoords)
            time.sleep(1)
            pyautogui.click(lockInCoords)
            time.sleep(1)
        
        #Change this for picks and bans
        click_image_found("BanAChamp.png", "move", 0.5)
        select_champion("Yasuo")
        select_champion("Camille")

        click_image_found("PickAChampion.png", "move", 0.7)
        select_champion("Poppy")
        time.sleep(1)
        click_image_found("rune.png", 0.9)
        center_y = (searchCoordsFinal.y + lockInCoords.y) / 2
        center_position = (lockInCoords.x, center_y)
        time.sleep(2)
        pyautogui.click(center_position)
        pyautogui.click(center_position)
        time.sleep(2)
        click_image_found("close.png", "once")

    def monitor_accept():
        current_thread = None
        while True:
            accept_button_location = click_image_found("accept.png")
            if current_thread is not None:
                current_thread.cancel()
                current_thread.join()  # Ensure the old thread has finished
            current_thread = threading.Timer(0, task)
            current_thread.start() 
            time.sleep(13.5)  # 13 second buffer before looking for accept.png again, (time it takes for full accept dodge)

    monitor_accept()

def click_image_found(imageName, interaction="click", conf=0.7):
    accept_button_location = None
    print(f"Looking for {imageName}!")
    while accept_button_location is None:
        try:
            accept_button_location = pyautogui.locateOnScreen(imageName, confidence=conf)
        except:
            print("NOT FOUND")
            if interaction == "once":
                return None
            pass
        time.sleep(1)

    print(f"{imageName} found !")
    accept_button_center = pyautogui.center(accept_button_location)

    if interaction == "move":
        pyautogui.moveTo(accept_button_center)
    else:
        pyautogui.click(accept_button_center)
 
    print(f"{imageName} clicked !")
    
    return accept_button_center

if __name__ == "__main__":
    main()