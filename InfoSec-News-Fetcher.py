import os
import requests
from bs4 import BeautifulSoup
import datetime
import time
import textwrap

# URLs to fetch articles from
urls = ['https://thehackernews.com/',
        'https://cyware.com/cyber-security-news-articles',
        'https://www.bleepingcomputer.com/tag/zero-day/',
        'https://www.bleepingcomputer.com/',
        'https://www.securityweek.com/category/malware-cyber-threats/']

# dictionary to store the stories
stories = {}
TD = datetime.datetime.now()

# Get terminal width using os.get_terminal_size() if available, otherwise use fixed width
try:
    terminal_width = os.get_terminal_size().columns
except OSError:
    terminal_width = 80  # Fallback to a default fixed width

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
        
        # Adjust text wrapping based on terminal width or fallback fixed width
        wrapped_text = textwrap.fill(story, width=terminal_width)
        print(wrapped_text)
        
        print("-" * terminal_width)
        print(datetime.datetime.now())
        print('Please Account For When The Story was found, Until It Was Published And When You Are Reading It')
        print("-" * terminal_width)

    time.sleep(240)
