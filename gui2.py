import pyautogui
import time

# Show a start prompt
start_prompt = pyautogui.confirm(text='Do you want to start the script?', title='Start Prompt', buttons=['OK', 'Cancel'])

if start_prompt == 'OK':
    
    # Set the screen width and height
    screen_width, screen_height = pyautogui.size()
    # Get the start and end numbers from the user
    start_number = int(pyautogui.prompt(text='Enter the start number:', title='Start Number', default='91'))
    end_number = int(pyautogui.prompt(text='Enter the end number:', title='End Number', default='101'))

    # Set the start numbers
    start_numbers = range(start_number, end_number)  # Adjust the range as needed
    # Loop over each start number
    for start_number in start_numbers:
        # Loop over each image in the tab
        for i in range(1, 4):  # Adjust the range as needed
            # Move the mouse to the center of the screen
            pyautogui.moveTo(screen_width // 2, screen_height // 2)

            # Right click
            pyautogui.click(button='right')

            # Select 'Save As' (you may need to adjust the coordinates based on your screen resolution and the position of the 'Save As' option in the context menu)
            pyautogui.moveTo(1000, 600)  # for a 1920x1080 screen
            pyautogui.click()
            time.sleep(3)  # wait for the 'Save As' dialog to appear

            # Click on the 'File name' input field in the 'Save As' dialog (replace with the actual coordinates)
            pyautogui.moveTo(300, 450)  # Replace with the actual coordinates
            pyautogui.click()
            time.sleep(3) 

            # Type the name of the file (the start number + '-' + the index of the image)
            pyautogui.write(f'{start_number}-{i}')
            pyautogui.press('enter')

            # Wait for the image to download
            time.sleep(3)  # Adjust the sleep time as needed

            # Press the right arrow key
            pyautogui.press('right')
            time.sleep(3)

        # Switch to the next tab after every 4 images
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(3)  # wait for the tab to load