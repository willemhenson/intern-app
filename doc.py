import requests
from bs4 import BeautifulSoup
import json
import time

def refreshGradcrackerPage():
	
	# Gradcracker: summer tech internships in London (first 80)
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
	with open("gradcracker.html", "wt") as file:
		file.write(html_string)

def refreshRMPPage():
	
	# RMP: summer tech internships in London (first 20)
	url = "https://scrapeninja.p.rapidapi.com/scrape-js"
	payload = {
		"url": "https://www.ratemyplacement.co.uk/search-jobs/internship/technology/london",
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
	with open("rmp.html", "wt") as file:
		file.write(html_string)

def addGradcrackerPage(response_content):

	response_content = response_content.replace("\n","")
	response_content = response_content.replace("\t","")

	# Parse the HTML content with BeautifulSoup
	soup = BeautifulSoup(response_content, "html.parser")

	elements = soup.find_all(class_="tw-relative tw-mb-4 tw-border-2 tw-border-gray-200 tw-rounded")

	jobs = []
	for element in elements:
		this_job = {
			"Salary": "",
			"Location": "",
			"Duration": "",
			"Starting": "",
			"Deadline": ""
		}
		this_job["Host"] = "Gradcracker.com"
		this_job["Name"] = element.find(class_="tw-block tw-text-base tw-font-semibold").decode_contents(),
		this_job["Name"] = this_job["Name"][0]
		this_job["Link"] = element.find(class_="tw-block tw-text-base tw-font-semibold").get("href"),
		this_job["Link"] = this_job["Link"][0]
		this_job["Logo"] = element.find(class_="tw-flex tw-flex-col tw-w-2/5 tw-pl-4 tw-space-y-2 tw-border-l-2 tw-border-gray-100").contents[0].contents[0].get("src")

		metadata = element.find(class_="tw-pl-0 tw-mt-0 tw-mb-0 tw-space-y-1.5 tw-text-xs tw-font-medium tw-py-2 tw-text-gray-500 tw-list-none").contents
		for meta_pair in metadata:
			this_job[meta_pair.contents[0].decode_contents().strip(":")] = meta_pair.contents[1][1:]

		jobs.append(this_job)

	return jobs

def addRMPPage(response_content):

	response_content = response_content.replace("\n","")
	response_content = response_content.replace("\t","")

	# Parse the HTML content with BeautifulSoup
	soup = BeautifulSoup(response_content, "html.parser")

	elements = soup.find_all(class_="Search-content")

	jobs = []
	for element in elements:
		this_job = {
			"Salary": "",
			"Location": "",
			"Duration": "",
			"Starting": "",
			"Deadline": ""
		}
		this_job["Host"] = "RateMyPlacement.com"
		this_job["Name"] = element.contents[1].contents[0].contents,
		this_job["Name"] = this_job["Name"][0][0]
		this_job["Link"] = element.contents[0].contents[0].get("href")
		this_job["Logo"] = element.contents[0].contents[0].contents[0].get("src")

		jobs.append(this_job)

	return jobs

REFRESH = False

if REFRESH:

	refreshGradcrackerPage()
	refreshRMPPage()

jobs = []

with open("gradcracker.html", "rt") as file:
	response_content = file.read()
	jobs += addGradcrackerPage(response_content)

with open("rmp.html", "rt") as file:
	response_content = file.read()
	jobs += addRMPPage(response_content)







with open("jobs.json", "wt") as file:
	file.write(json.dumps(jobs))
