import re
import requests
from bs4 import BeautifulSoup

# fetch all urls to process
home_url = "http://www.boardofstudies.nsw.edu.au/ebos/static/DSACH_2015_12.html"
home_html = requests.get(home_url)
home_soup = BeautifulSoup(home_html.content)

hrefs = []
for a in home_soup.find("table").find_all("a", href=True):
    hrefs.append(a['href'])
hrefs.sort()

# process each url
base_url = "http://www.boardofstudies.nsw.edu.au/ebos/static/"
for href in hrefs:
    url = base_url + href
    html = requests.get(url)
    soup = BeautifulSoup(html.content)

    for table_row in soup.find_all("tr"):
        for data in table_row.find_all("td"):
            if data.text.encode('utf-8')[1].isdigit():
                # print results in a nice format
                print re.sub(r'\s(\d{5}) - ',r'\n',data.text.encode('utf-8')[9:]) + "\n"
            else:
                # print name and school
                print data.text