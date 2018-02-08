import time
import easygui

start = time.time()
hours = 0
while True:
    if hours != 0:
        message = ''
        if hours % 1 == 0:
            message += "hand poses"
            message += ", finger stretch"
            message += ", massage hands"
            message += ", take a walk"
        if hours % 2 == 0:
            message += ", shake wrists and fingers"
        if hours % 3 == 0:
            message += ", pull wrists"
        easygui.msgbox(message)
        # print(str(hours) + " " + message)
    time.sleep(600.0 - ((time.time() - start) % 600.0))
    hours += 1
