import time
import webbrowser

i = 3
two_hours = 7200
print "This program started on " + time.ctime()
while (i > 0):
    time.sleep(two_hours)
    webbrowser.open("http://www.google.com")
    i -= 1


