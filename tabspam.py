import webbrowser
import time
import random

while True:
    sites = random.choice(['https://www.youtube.com/watch?v=6GxWmSVv-cY','https://www.youtube.com/watch?v=8UFIYGkROII'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(1, 1)
    time.sleep(seconds)
