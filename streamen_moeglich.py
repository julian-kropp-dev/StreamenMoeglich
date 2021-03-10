# Eine Idee nach Algorithmen verstehen, umgesetzt von Algorithmen verstehen bzw. Julian Kropp
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
options = Options()
options.add_argument("user-data-dir=C:\\Users\\Julian\\AppData\\Local\\Google\\Chrome\\User Data")

def quality(mbit):
    bitrate = mbit * 1000 * 0.8
    if bitrate < 3000:
        return "Kein Streaming möglich. Willkommen im #IchhabeeineBambusleitungClub !"
    elif bitrate >= 3000 and bitrate <4500:
        return "Streaming in 720p,30fps möglich!"
    elif bitrate >= 4500 and bitrate <6000:
        return "Streaming in 1080p,30fps oder 720p,60fps möglich!"
    else:
        return "Streaming in 1080, 60fps möglich. Glückwunsch!"

def checkinternetspeed():
    speedtest = webdriver.Chrome("C:\\Selenium\\chromedriver.exe", options=options)
    speedtest.get("https://www.speedtest.net/")
    time.sleep(3)
    start= speedtest.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
    start.click()
    time.sleep (60)
    upload= start.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span").text
    return float(upload)
mbit= checkinternetspeed()
print(quality(mbit))
time.sleep(10)