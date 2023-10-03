
# Import Dependencies
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
chrome_options.add_argument("webdriver.chrome.driver=C:/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://twitter.com/login")

subject = "Narendra Modi"


# Setup the log in
sleep(3)
email = driver.find_element(By.XPATH,"//input[@name='text']")
email.send_keys("desaiatharva50@gmail.com")
next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
next_button.click()

sleep(3)
username = driver.find_element(By.XPATH,"//input[@name='text']")
username.send_keys('atharva9883')
next = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
next.click()

sleep(3)
password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys("Athmanmil100#")
login = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
login.click()

# Search item and fetch it
sleep(3)
search_logo = driver.find_element(By.XPATH,"//a[@aria-label='Search and explore']")
search_logo.click()


sleep(3)
search_box = driver.find_element(By.XPATH,"//input[@aria-label='Search query']")
search_box.send_keys(subject)
search_box.send_keys(Keys.ENTER)

sleep(3)
people = driver.find_element(By.XPATH, "//span[contains(text(), 'People')]")
people.click()

sleep(3)
profile = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]")
profile.click()

sleep(3)



# UserTag = driver.find_element(By.XPATH,"//div[@data-testid='User-Names']").text
# TimeStamp = driver.find_element(By.XPATH,"//time").get_attribute('datetime')
# Tweet = driver.find_element(By.XPATH,"//div[@data-testid='tweetText']").text
# Reply = driver.find_element(By.XPATH,"//div[@data-testid='reply']").text
# reTweet = driver.find_element(By.XPATH,"//div[@data-testid='retweet']").text
# Like = driver.find_element(By.XPATH,"//div[@data-testid='like']").text


UserTags=[]
TimeStamps=[]
Tweets=[]
Replys=[]
reTweets=[]
Likes=[]

articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
while True:
    for article in articles:
        UserTag = driver.find_element(By.XPATH,".//div[@data-testid='User-Name']").text
        UserTags.append(UserTag)
        
        TimeStamp = driver.find_element(By.XPATH,".//time").get_attribute('datetime')
        TimeStamps.append(TimeStamp)
        
        Tweet = driver.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
        Tweets.append(Tweet)
        
        Reply = driver.find_element(By.XPATH,".//div[@data-testid='reply']").text
        Replys.append(Reply)
        
        reTweet = driver.find_element(By.XPATH,".//div[@data-testid='retweet']").text
        reTweets.append(reTweet)
        
        Like = driver.find_element(By.XPATH,".//div[@data-testid='like']").text
        Likes.append(Like)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(3)
    articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
    Tweets2 = list(set(Tweets))
    if len(Tweets2) > 15:
        break


print(len(UserTags),
len(TimeStamps),
len(Tweets),
len(Replys),
len(reTweets),
len(Likes))


import pandas as pd

df = pd.DataFrame(zip(UserTags,TimeStamps,Tweets,Replys,reTweets,Likes)
                  ,columns=['UserTags','TimeStamps','Tweets','Replys','reTweets','Likes'])

df.head()

df.to_excel("narendra_modi.xlsx",index=False)
print("Saved to exel sucessfully")








