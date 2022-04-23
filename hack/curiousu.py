import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import webbrowser
#import time

url = 'https://www.utwente.nl/en/summer-school-curiousu/Win%20a%20free%20ticket/solve/'

def send_req(pw):
	myData = {
		"crypto": pw,
		"output": pw
	}
	x = requests.get(url, data = myData)
	return x

def main():
	f_out = open("curiousu.txt", 'w')
	
	pw = "abcdefg"
	x = send_req(pw)
	f_out.write(x.text)
	
	#Click
	driver = webdriver.Chrome(r"C:\Users\Lorenzo\.wdm\drivers\chromedriver\win32\100.0.4896.60\chromedriver.exe")
	#driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get(url)
	#button = driver.find_element_by_link_text("Check")
	#button = driver.find_element_by_id("checkbtn")
	button = driver.find_element("Check")
	button.click()
	
	f_out.write(requests.get(url).text)
	f_out.close()
main()
