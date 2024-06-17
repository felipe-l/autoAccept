import pyautogui
import cv2
import time


def main():
    click_image_found("accept.png")
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
    
    #Change this for picks and bans
    click_image_found("BanAChamp.png", "move", 0.5)
    select_champion("Yasuo")
    select_champion("Camille")

    click_image_found("PickAChampion.png", "move", 0.7)
    select_champion("Poppy")

    
    

def click_image_found(imageName, interaction="click", conf=0.7):

    accept_button_location = None
    print(f"Looking for {imageName}!")
    while accept_button_location is None:
        try:
            accept_button_location = pyautogui.locateOnScreen(imageName, confidence=conf)
        except:
            print("NOT FOUND")
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