### script to download manually each image
import pyautogui
import time

# Wait for all actions to complete
time.sleep(2)

# Iterate over the tabs
for i in range(10):
    # Use hotkey to switch to the next tab
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(1)  # wait for the tab to load

    # Move the mouse to the center of the screen (you may need to adjust the coordinates based on your screen resolution)
    pyautogui.moveTo(960, 540)  # for a 1920x1080 screen
    time.sleep(0.5)

    # Right click
    pyautogui.click(button='right')
    time.sleep(0.5)  # wait for the context menu to appear

    # Select 'Save As' (you may need to adjust the coordinates based on your screen resolution and the position of the 'Save As' option in the context menu)
    pyautogui.moveTo(1000, 600)  # for a 1920x1080 screen
    pyautogui.click()
    time.sleep(1)  # wait for the 'Save As' dialog to appear

    # Type the name of the file (the index of the tab + 1)
    pyautogui.write(str(i + 1))
    time.sleep(1.5)

    # Press 'Enter' to save the file
    pyautogui.press('enter')
    time.sleep(0.6)  # wait for the file to be saved