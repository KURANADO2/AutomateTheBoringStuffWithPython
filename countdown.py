import time
import subprocess


timeLeft = 3
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft -= 1
# subprocess.Popen(['D:\Program Files\PotPlayer\PotPlayerMini.exe', 'D:\\Python\\alarm.wav'], shell=True)
subprocess.Popen(['start', 'D:\\Python\\alarm.wav'], shell=True)
