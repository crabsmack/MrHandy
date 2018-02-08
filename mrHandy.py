import time
import easygui

start = time.time()
hours = 0
while True:
    if hours != 0:
        messages = []
        if hours % 1 == 0:
            messages.append("hand poses")
            messages.append("finger stretch")
            messages.append("massage hands")
            messages.append("take a walk")
        if hours % 2 == 0:
            messages.append("shake wrists and fingers")
        if hours % 3 == 0:
            messages.append("pull wrists")
        easygui.msgbox(", ".join(messages))
        # print(str(hours) + " " + message)
    time.sleep(3600.0 - ((time.time() - start) % 3600.0))
    hours += 1
