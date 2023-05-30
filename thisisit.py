import requests
from bs4 import BeautifulSoup
import datetime
import time

# URLs to fetch articles from
urls = ['https://thehackernews.com/',
        'https://cyware.com/cyber-security-news-articles',
        'https://www.bleepingcomputer.com/tag/zero-day/',
        'https://www.bleepingcomputer.com/'
        'https://www.securityweek.com/category/malware-cyber-threats/']

# -------------------------------------------------------------

# dictionary to store the stories
stories = {}
TD = (datetime.datetime.now())


while True:
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # find all the posts on the page
        posts = soup.find_all("div", class_="body-post clear")

        # loop through each post and add to the dictionary
        for post in posts:
            title = post.find("h2", class_="home-title").text
            story = post.find("div", class_="home-desc").text.strip()

            # if the title already exists, add to its story
            if title in stories:
                stories[title] = story + "\n\n" + stories[title]
            else:
                stories[title] = story
    # print the stories with their corresponding titles

    for title, story in stories.items():
        print(title)
        print(story)
        time.sleep(240)
        print("--------------"), print(datetime.datetime.now())

print('We Update Every OneHour, In Case You Were Busy and to Deliver Up-To-Date Information')
'''wait 1 hours before fetching new stories'''
time.sleep(60 * 60)

subject = "Frequent Daily Reports"
body = []
while True:
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # find all the posts on the page
        posts = soup.find_all("div", class_="body-post clear")

        # loop through each post and add to the dictionary
        for post in posts:
            title = post.find("h2", class_="home-title").text
            story = post.find("div", class_="home-desc").text.strip()

            # if the title already exists, add to its story
            if title in stories:
                stories[title] = story + "\n\n" + stories[title]
            else:
                stories[title] = story
    # print the stories with their corresponding titles

    for title, story in stories.items():
        print(title)
        print(story)
        time.sleep(240)
        print("--------------"), print(datetime.datetime.now())
        body = [title, story]


print('We Update Every Two Hours, In Case You Were Busy and to Deliver Up-To-Date Information')
'''wait 2 hours before fetching new stories'''
time.sleep(7200)

