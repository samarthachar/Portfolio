from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time


driver = webdriver.Chrome()
driver.get('https://www.chromedino.com')

driver.implicitly_wait(10)

button = driver.find_element(By.CSS_SELECTOR, ".fc-button.fc-cta-consent.fc-primary-button")
button.click()

dino_location = pyautogui.locateOnScreen('dino.png', confidence=0.8)



if dino_location:
    dino_x = dino_location.left
    dino_y = dino_location.top
    print(f"Dino found at ({dino_x}, {dino_y})")
else:
    print("Dino not found. Make sure the game is visible and dino.png is accurate.")

def is_obstacle():
    for x_offset in range(30, 80, 10):
        for y_offset in range(-10, 10, 5):
            pixel = pyautogui.pixel(dino_x + x_offset, dino_y + y_offset)
            print(f"Pixel at ({dino_x + x_offset}, {dino_y + y_offset}): {pixel}")
            if pixel[0] < 100:
                pyautogui.press('space')
                return True
    return False

pyautogui.click(dino_x + 20, dino_y + 20)
time.sleep(0.5)
pyautogui.press('space')
time.sleep(0.5)


while True:
    if is_obstacle():
        print('works')
        pyautogui.press('space')
        time.sleep(0.1)
