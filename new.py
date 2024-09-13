import requests

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