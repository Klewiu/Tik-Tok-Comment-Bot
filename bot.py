import pyautogui
import time
import random

repeat_counter=0
while True:
    #pause the video
    pyautogui.click(612,610)
    time.sleep(2)

    #open the comments
    pyautogui.click(822,683)
    time.sleep(3)

    #inputbox
    pyautogui.click(426,972)
    comment = ['This is super!','Cool video','I like it','Nice...','OMG']
    pyautogui.write(f'{random.choice(comment)}', interval=0.2)
    time.sleep(2)

    #upload comment
    pyautogui.click(833,971)
    time.sleep(3)

    #close comment
    pyautogui.click(831,456)
    time.sleep(2)

    #scrolling
    pyautogui.moveTo(605,791)
    pyautogui.dragTo(611,284, 1, button='left')
    time.sleep(4)
    if repeat_counter == 4:
        break
    repeat_counter+=1