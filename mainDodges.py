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
    if getattr(sys, 'frozen', False):
        os.chdir(sys._MEIPASS)

    sys.stderr = open(os.path.join(base_dir, 'errors.txt'), 'w')
    monitor_accept()

def task(bans, picks):
    ban1, ban2, ban3 = bans
    prio_pick1, prio_pick2, prio_pick3 = picks
    
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
    select_champion(ban1)
    select_champion(ban2)
    select_champion(ban3)

    click_image_found("PickAChampion.png", "move", 0.7)
    select_champion(prio_pick1)
    select_champion(prio_pick2)
    select_champion(prio_pick3)
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
    def close_auto_fill():
        while True:
            click_image_found("autoFillJgl.png", "move")
            click_image_found("close1.png", "once")
            time.sleep(10)  # Adjust sleep time as necessary for the function's purpose
    
    def decline_swap():
        while True:
            click_image_found("decline.png", "once")
            time.sleep(2)  # Adjust sleep time as necessary for the function's purpose
    
    autofill_thread = threading.Thread(target=close_auto_fill)
    autofill_thread.daemon = True
    autofill_thread.start()

    
    decline_thread = threading.Thread(target=decline_swap)
    decline_thread.daemon = True
    decline_thread.start()

    current_thread = None
    while True:
        accept_button_location = click_image_found("accept.png")
        if current_thread is not None:
            current_thread.cancel()
            current_thread.join()  # Ensure the old thread has finished
        current_thread = threading.Timer(0, task, args=([ban1, ban2, ban3], [prio_pick1, prio_pick2, prio_pick3]))
        current_thread.start() 
        time.sleep(13.5)  # 13 second buffer before looking for accept.png again, (time it takes for full accept dodge)

def click_image_found(imageName, interaction="click", conf=0.7):
    accept_button_location = None
    print(f"Looking for {imageName}!")
    while accept_button_location is None:
        try:
            accept_button_location = pyautogui.locateOnScreen(f"./assets/{imageName}", confidence=conf)
        except:
            print(f"{imageName} NOT FOUND")
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
    time.sleep(0.5)  
    return accept_button_center

if __name__ == "__main__":
    main()