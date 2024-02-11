import cv2
import numpy as np
import pyautogui
import time

# Recognize and click the star button
def star_and_name_click():
    
    # Uploading image to recognize in a variable
    template = cv2.imread('bet_button_star_off.png', 0)

    # Take a screenshot and modify colors and more...
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Find the correspondence with the template uploaded
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    _, matching_coefficient, _, max_loc = cv2.minMaxLoc(result)

    # Check if the matching coefficient is high enough
    if matching_coefficient < 0.95:
        return False, 0

    # Template dimensions
    h, w = template.shape

    # Coordinates computation for the clicking
    click_x = max_loc[0] + w // 2
    click_y = max_loc[1] + h // 2

    # Click the star button
    pyautogui.click(x=click_x, y=click_y)

    time.sleep(2)

    # Click the name of the bet button
    pyautogui.click(click_x - 200, click_y)

    return True, (click_x,click_y)

# Click the button that appeared after the star
def second_bet_button():

    # We need to recognize if the bet can't be clicked
    # Uploading image to recognize in a variable
    template = cv2.imread('but_button_betdisabled.png', 0)

    # Take a screenshot and modify colors and more...
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Find the correspondence with the template uploaded
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    _, matching_coefficient, _, max_loc = cv2.minMaxLoc(result)

    # Check if the matching coefficient is high enough
    if matching_coefficient > 0.9:
        
        # If there is the button of bet disabled we refresh the page and start from the beginning
        pyautogui.press("f5")

        time.sleep(15)

        return 3


    # Uploading image to recognize in a variable
    template = cv2.imread('bet_button_trophy_reference.png', 0)

    # Take a screenshot and modify colors and more...
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Find the correspondence with the template uploaded
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    _, matching_coefficient, _, max_loc = cv2.minMaxLoc(result)

    # Check if the matching coefficient is high enough
    if matching_coefficient < 0.9:
        return False

    # Template dimensions
    h, w = template.shape

    # Coordinates computation for the clicking
    click_x = max_loc[0] + w // 2
    click_y = max_loc[1] + h // 2 - 80

    # Click the star button
    pyautogui.click(x=click_x, y=click_y)

    return True

# Function to set the amount to bet
def amount_setting():

    # Uploading image to recognize in a variable
    template = cv2.imread('bet_button_quotes_to_buy.png', 0)

    # Take a screenshot and modify colors and more...
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Find the correspondence with the template uploaded
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    _, matching_coefficient, _, max_loc = cv2.minMaxLoc(result)

    # Check if the matching coefficient is high enough
    if matching_coefficient < 0.5:
        return False

    # Template dimensions
    h, w = template.shape

    # Coordinates computation for the clicking
    click_x = max_loc[0] + w // 2
    click_y = max_loc[1] + h // 2

    # Click the star button
    pyautogui.doubleClick(x=click_x, y=click_y)

    # Wait half second
    time.sleep(0.5)

    # Write the amount to bet, always 100, then check if the limit is lower
    pyautogui.write('1')

    # Check if there is a lower limit
    
    # Uploading image to recognize in a variable
    template = cv2.imread('bet_button_limit_smaller.png', 0)

    # Take a screenshot and modify colors and more...
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Find the correspondence with the template uploaded
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    _, matching_coefficient, _, max_loc = cv2.minMaxLoc(result)

    # Check if the coefficient is enough
    if matching_coefficient > 0.9:

        # Template dimensions
        h, w = template.shape

        # Coordinates computation for the clicking
        click_x = max_loc[0] + w // 2
        click_y = max_loc[1] + h // 2

        # Click the button that corrects the amount
        pyautogui.click(click_x,click_y)

    return True


# Function to click the bet button
def final_bet_button_click():

    # Uploading image to recognize in a variable
    template = cv2.imread('bet_button_profit_check.png', 0)

    # Take a screenshot and modify colors and more...
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Find the correspondence with the template uploaded
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    _, matching_coefficient, _, max_loc = cv2.minMaxLoc(result)

    # Check if the matching coefficient is high enough
    if matching_coefficient < 0.85:
        
        pyautogui.press("f5")

        time.sleep(15)

        return True

    # Template dimensions
    h, w = template.shape

    # Coordinates computation for the clicking
    click_x = max_loc[0] + w // 2
    click_y = max_loc[1] + h // 2

    # Click the star button
    pyautogui.click(x=click_x, y=click_y)

    return False

# Ozel Oran function in order to reset the page as the start
def ozelclick():
    
    # Uploading image to recognize in a variable
    template = cv2.imread('bet_button_ozel_oran.png', 0)

    # Take a screenshot and modify colors and more...
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Find the correspondence with the template uploaded
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    _, matching_coefficient, _, max_loc = cv2.minMaxLoc(result)

    # Check if the matching coefficient is high enough
    if matching_coefficient > 0.95:
        
        # Template dimensions
        h, w = template.shape

        # Coordinates computation for the clicking
        click_x = max_loc[0] + w // 2
        click_y = max_loc[1] + h // 2

        # Click the star button
        pyautogui.click(x=click_x, y=click_y)

        time.sleep(2)

        return True
    return False

# Function to make a cicle of betting (star, click, amount, final button)
def cicle_bet():

    # Star click
    star_and_name = star_and_name_click()
    if star_and_name[0]:

        time.sleep(2.3)

        # Click the bet we want to operate
        second_button = second_bet_button()

        # Check if there is the block of the bet and trying to refresh if it is like this
        for _ in range(20):
            if second_button == 3:
                second_button = second_bet_button()
            else:
                break

        if second_button:

            time.sleep(5)

            for _ in range(20):

                # Amount setting
                if amount_setting():

                    time.sleep(5)

                    # Button bet click
                    profit_check = final_bet_button_click()
                
                    # Check if there is the block on the final bet
                    if not profit_check:
                        break

                time.sleep(2.5)
    
    # Ozel Oran click for the reset of the initial conditions
    ozel = ozelclick()
    if not ozel:
        raise ValueError("Ozel Oran has to be found. Update the image or adjust the coefficient! (call Mattia!)")

#---------------------------------------------------------------------------

# FROM HERE THE BOT START TO WORK

time.sleep(5)

chrome_windows = int(input("How many chrome windows: ")) # set the amount of Chrome windows that are open on pc

# Take the time to refresh every 25 minutes
before = time.time()


# Starting the loop
while True:

    # Repeat the star clicking 5 times for every Chrome window
    for _ in range(5):
        cicle_bet()
    
    # Change the window
    pyautogui.hotkey("alt","shift","tab")

    time.sleep(2)

    # Refresh if 25 minutes have passed
    after = time.time()

    if (after - before) > 1500:

        for _ in range(chrome_windows + 1):
            pyautogui.hotkey("alt","shift","tab")
            pyautogui.press("f5")
        
        before = after