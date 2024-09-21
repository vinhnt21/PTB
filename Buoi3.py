import pyautogui

# auto click mouse on x = 1057, y=87 after each 5 second
pyautogui.sleep(5)
while True:
    pyautogui.click(1057, 87)
    pyautogui.sleep(10)