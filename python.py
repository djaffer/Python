import time
import webbrowser

count  = 1
while (count==1):
    print("Current Time: "+time.ctime())
    time.sleep(3600)
    webbrowser.open("https://www.youtube.com/watch?v=HZu3bXWhnX4")
