import pandas as pd
from bs4 import BeautifulSoup

with open('Narendra_Modi_tweets.html', 'r',encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

tweets = []

divf = soup.find_all('span', class_="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")

for divs in divf:
    # ele = divs.find_all('div', class_='css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu')
    # for tweetts in ele:
    #     contain = tweetts.find('div', class_='css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')
    #     for div in contain:
    #         tweet_element = div.find('span', class_='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0')
    #         tweet_content = tweet_element.text.strip() if tweet_element else ''

    #         tweets.append(tweet_content)
    print(divs)

# data = {
#     'Tweets': tweets
# }

# df = pd.DataFrame(data)
# df.to_excel('Narendra_Modi_Tweets.xlsx',index=False)
# print('Data scrapped sucessfully')