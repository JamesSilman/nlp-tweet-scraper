import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('/Users/james/Downloads/chromedriver')

def get_user_tweets(twitter_username, page_downs, wing_type):
	
	browser.get("https://twitter.com/" + twitter_username)

	time.sleep(1)

	elem = browser.find_element_by_tag_name("body")

	no_of_pagedowns = page_downs
	while no_of_pagedowns:
		elem.send_keys(Keys.PAGE_DOWN)
		time.sleep(0.3)
		no_of_pagedowns -= 1

	twitter_elm = browser.find_elements_by_class_name("tweet")

	count = 0
	for post in twitter_elm:
		username = post.find_element_by_class_name("username")
		if username.text.lower() == "@" + twitter_username.lower():
			tweet = post.find_element_by_class_name("tweet-text")
			print(tweet.text)
			file = open(wing_type + "/" + twitter_username + "_" + str(count) + ".txt", "w")
			file.write(tweet.text)
			file.close()
			count += 1

def quit_browser():
	browser.quit()

wings = {"right_wing_tweets":"right_wing", "left_wing_tweets":"left_wing"}

for key, value in wings.items():
	print("STARTING " + key)
	with open(str(value), 'r') as f:
		accounts = f.read().splitlines() 
		for a in accounts:
			print(a)
			get_user_tweets(a, 50, key)

quit_browser()
