
import requests
from bs4 import BeautifulSoup

URL="https://www.amazon.in/s?k=mobile+under+40000&crid=174Z2A2F540FK&sprefix=mobile+under+40000%2Caps%2C234&ref=nb_sb_noss_2"

page=requests.get(URL)
soup=BeautifulSoup(page.content,"html.parser")

results = soup.find(id="11")
result_element=results.find_all("div",class_="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col s-widget-spacing-small sg-col-12-of-16")

for result in result_element:
    title=result.find("div",class_="a-section a-spacing-none puis-padding-right-small s-title-instructions-style")
    print(title.text.strip())
