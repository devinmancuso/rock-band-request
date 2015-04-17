#!/usr/bin/python

import time
from selenium import webdriver
from selenium.webdriver import PhantomJS
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from sys import argv
import click

@click.command()
@click.option('--votes', type=int, prompt='Number of times you want to vote for this song', help='Number of votes to submit')
@click.option('--song', prompt='Song name', help='The name of the song you want to vote for, it can include spaces')
@click.option('--artist', prompt='Artist name', help='The name of the artist you want to vote for, it can include spaces')
def voter(votes, song, artist):
	"""Simple python program that votes for your favourite song for the next Rock Band game"""
	votestring =str(votes)
	print(' ')
	print(' ')
	print("### VOTE REQUESTER STARTING ###")
	print(' ')
	print("Voting for song: " + song)
	print("As performed by: " + artist)
	print("Submitting the form " + votestring + " times")

	chrome_options = webdriver.ChromeOptions()
	driver = webdriver.Chrome(executable_path='/Library/Python/2.7/site-packages/selenium/webdriver/chrome/chromedriver', chrome_options=chrome_options)
	driver.set_window_size(1920, 1080)
	driver.maximize_window()

	driver.get('http://www.harmonixmusic.com/games/rock-band/request/')

	votecount = 1

	for x in range(0, votes):
		
		driver.find_element_by_id('id_title').send_keys(song)	
		driver.find_element_by_id('id_artist').send_keys(artist)
		time.sleep(1)
		driver.find_element_by_class_name('req_submit').click()
		time.sleep(4)
		print("Vote: "),
		print(votecount)	
		votecount += 1
		#driver.find_element_by_class_name('thanks').click()
		#driver.find_element_by_link_text('Submit another request')
		#driver.find_element_by_link_text('SUBMIT ANOTHER REQUEST')
		driver.find_element_by_xpath("//a[@href='/games/rock-band/request/']").click()
		time.sleep(4)

	driver.quit()

if __name__ == '__main__':
	voter()