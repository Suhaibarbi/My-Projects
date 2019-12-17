#Loading Screen
from IPython.display import clear_output
import time
seconds = 10
for progress in range(0,seconds+1):
    percent = (progress * 100) // seconds
    clear_output()
    print("\n")
    print("Loading...")
    print("<" + ("=" * progress) + (" " * (seconds-progress)) + "> " + str(percent) + "%")
    print("\n")
    time.sleep(1)
print ("Loaded Successful")
time.sleep(2)
clear_output()
