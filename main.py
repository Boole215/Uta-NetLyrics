import requests
from bs4 import BeautifulSoup

websiteLink = input("Please enter your uta-net URL: ")
r = requests.get(websiteLink)
soup = BeautifulSoup(r.content, 'html.parser', from_encoding="utf-8")
interest = soup.find("div", {"id" : "kashi_area"});
splitInterest = interest.prettify().split("\n");

lyrics = [x for x in splitInterest if "<" not in x]
lyrics = list(map(lambda x: x.strip(),lyrics))

fileName = input("\nWhat would you like to name the lyrics .txt? ").strip();

with open(fileName+".txt", encoding="utf-8", mode="w") as f:
	for line in lyrics:
		f.write(line+"\n");

print("\nFile created.")