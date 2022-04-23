import threading
import time
import requests

def run_req():
	headers = {
		'authority': 'www.utwente.nl',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
		'cache-control': 'max-age=0',
		'cookie': 'ut-sess=%7B%22referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22start%22%3A1650661302121%7D; monsido=A7E1650661303590; _gid=GA1.2.646142715.1650661304; ut-settings=%7B%22firstreferrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22firstrefertime%22%3A1650661302121%2C%22country%22%3A%22HU%22%2C%22countryname%22%3A%22Hungary%22%2C%22clientid%22%3A%22208153306.1650661304%22%7D; _gcl_au=1.1.1621285438.1650661305; _fbp=fb.1.1650661305408.1537172726; utwente__avgconsent=%7B%22a%22%3Atrue%2C%22c%22%3Atrue%2C%22v%22%3A1%2C%22lc%22%3A%22Fri%2C%2022%20Apr%202022%2021%3A01%3A44%20GMT%22%2C%22isset%22%3Atrue%7D; _fbc=fb.1.1650661390721.IwAR1sgFxV22KBgphzNPX4-mWtP4NSJ5HeUO5D2WmATD5p-61bAVpBfe7klUw; _hjSessionUser_85186=eyJpZCI6Ijg5MTliYTkwLTNlOTMtNTkwNi04NmQ3LTMxNDY2ZDUxZTBmNCIsImNyZWF0ZWQiOjE2NTA2NjEzMDM4ODUsImV4aXN0aW5nIjp0cnVlfQ==; %7B%22v%22%3A2%2C%22c%22%3A%5B%22analytics%22%2C%22marketing%22%5D%2C%22lc%22%3A%222022-04-22T22%3A45%3A00.512Z%22%7D; _ga_DHY20KGR51=GS1.1.1650667489.2.1.1650667504.0; _ga=GA1.2.208153306.1650661304',
		'if-modified-since': 'Fri, 22 Apr 2022 16:31:06 GMT',
		'referer': 'https://www.utwente.nl/en/summer-school-curiousu/Win%20a%20free%20ticket/instructions/?utm_source=hack_fb_organic+&amp;utm_medium=fb_organic&amp;utm_campaign=hack_code&amp;utm_id=competition+&fbclid=IwAR1sgFxV22KBgphzNPX4-mWtP4NSJ5HeUO5D2WmATD5p-61bAVpBfe7klUw',
		'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
	}
	payload = {
		"crypto": "abcefsd",
		"output": "abcefsd",
		"checkbtn": "Verify();"
	}

	response = requests.get('https://www.utwente.nl/en/summer-school-curiousu/Win%20a%20free%20ticket/solve/', headers=headers, json=payload)

	print(response.text)

run_req()
