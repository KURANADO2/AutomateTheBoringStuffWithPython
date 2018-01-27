import time
import threading


def takeANap():
    time.sleep(5)
    print('Wake up!')


print('Start of program!')
newThread = threading.Thread(target=takeANap())
newThread.start()
print('End of pragram!')