import pyautogui
import numpy as np
import time

x, y, width, height = 300, 500, 100, 70


def capture_the_screen():
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    frame = np.array(screenshot)
    return frame


def evaluate_obstacle(frame):
    detected_high = False
    detected_low = False

    frame_high = frame[5:10, 0:100]
    frame_low = frame[55:57, 0:100]

    for row in frame_low:
        for pixel in row:
            if np.array_equal(pixel, [83, 83, 83]) or np.array_equal(pixel, [172, 172, 172]):
                detected_low = True
                break
        if detected_low:
            break

    for row in frame_high:
        for pixel in row:
            if np.array_equal(pixel, [83, 83, 83]) or np.array_equal(pixel, [172, 172, 172]):
                detected_high = True
                break
        if detected_high:
            break

    return detected_high, detected_low


while True:
    situation = capture_the_screen()
    high_obstacle, low_obstacle = evaluate_obstacle(situation)
    if low_obstacle:
        pyautogui.press('space')
    elif high_obstacle:
        pyautogui.keyDown('down')
        time.sleep(0.6)
        pyautogui.keyUp('down')
