from Selenium2Library import Selenium2Library

class WebAutomation(Selenium2Library):

	def __init__(self):
		super(WebAutomation,self).__init__()

	def open_browser_via_library(self):
		self.open_browser('https://www.google.com')

	def navigate_to_page(self,url):
		self.go_to(url)
