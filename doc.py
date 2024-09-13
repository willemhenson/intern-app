import requests
from bs4 import BeautifulSoup
import json

REFRESH = True

# Gradcracker: summer internships in London (first 80)
if REFRESH:
	url = "https://scrapeninja.p.rapidapi.com/scrape-js"
	payload = {
		"url": "https://www.gradcracker.com/search/computing-technology/work-placements-internships-in-london-and-south-east?duration=Summer&page=1",
		"geo": "eu",
		"retryNum": 1
	}
	headers = {
		"x-rapidapi-key": "367c6adf02mshb1234a763c706f1p179830jsna154653f7562",
		"x-rapidapi-host": "scrapeninja.p.rapidapi.com",
		"Content-Type": "application/json"
	}
	response = requests.post(url, json=payload, headers=headers)
	html_string = response.json()["body"]
	html_string = html_string.replace("\n","")
	html_string = html_string.replace("\t","")
	with open("eg.html", "wt") as file:
		file.write(html_string)
with open("eg.html", "rt") as file:
	response_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response_content, "html.parser")

# Find all elements with the class "poopy class"
elements = soup.find_all(class_="tw-relative tw-mb-4 tw-border-2 tw-border-gray-200 tw-rounded")

jobs = []
for element in elements:
	jobs += [{
		"job-hosted-on": "gradcracker",
		"job-name": element.find(class_="tw-block tw-text-base tw-font-semibold").decode_contents(),
		"job-apply-link":element.find(class_="tw-block tw-text-base tw-font-semibold").get("href")
	}]

print(json.dumps(jobs, indent=4))

