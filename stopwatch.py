import time


print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-c to quic.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1
# Start tracking the times
try:
    while True:
        input()
        lapTime = time.time() - lastTime
        totalTime = time.time() - startTime
        lastTime = time.time()
        print('lap # %s:  laptime: %s    totalTime: %s' %(str(lapNum).rjust(2), str(round(lapTime, 2)).rjust(6),
                                                          str(round(totalTime, 2)).rjust(6)), end='')
        lapNum += 1
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone')
