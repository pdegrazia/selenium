from Selenium2Library import Selenium2Library

class WebAutomation(Selenium2Library):

	def __init__(self):
		super(WebAutomation,self).__init__()

	def open_browser_via_library(self):
		super(WebAutomation,self).open_browser('https://www.google.com')

	def navigate_to_page(self,url):
		super(WebAutomation,self).go_to(url)