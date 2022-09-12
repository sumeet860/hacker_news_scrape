# Web Scrapping


import requests  # allow us to Download the raw html
from bs4 import BeautifulSoup  # Use html and grab the data
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

# Using the select (i.e) css selectors
# . is used for class
# css selector for id # is used for ids
# print(soup.select('#score_24849452'))

links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')
combined_links = links + links2
combined_subtext = subtext + subtext2
# print(votes[0])

# Votes are grabbed in list so we have to use list to access the votes data
# print(votes[1].get('id'))

# Function to sort the information using votes
# The lambda takes the key as their element to sort in the dictionary


def sort_stories(hnlist):
    # Using sorted, lambda and reverse parameter to sort the news based on the count
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        # Checking the number of votes of the news
        # if the votes count is 0 or nil ignore the news and go to next news and check their votes count
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                # Using dictionary to access title and href

                hn.append({'title': title, 'links': href, 'votes': points})
    return sort_stories(hn)


pprint.pprint(create_custom_hn(combined_links, combined_subtext))
