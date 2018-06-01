import urllib
import re
import time

url = "https://www.currys.co.uk/gbuk/panasonic-lumix-dmc-g7eb-k-mirrorless-camera-with-14-42-mm-f-3-5-5-6-lens-10132843-pdt.html"
string = "Add to basket" # presence of this string indicates that the item is in stock
timer = 60 # time between checks, in seconds

while True:
    page = urllib.urlopen(url).read()
    results = re.findall(string,page)
    if results:
        print('ITEM IN STOCK')
    if not results:
        print('ITEM OUT OF STOCK')
    time.sleep(timer)
