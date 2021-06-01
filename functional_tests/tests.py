from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase



class NewVisitorTest(StaticLiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox(executable_path=r"C:\Users\ajurc\PycharmProjects\geockdriver\geckodriver.exe")
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_home_page_visit(self):
		# Użytkownik wchodzi na stronę główną
		self.browser.get('http://127.0.0.1:8000')
		header_text = self.browser.find_element_by_tag_name('h1').text

		# Tytuł i nagłówek strony głównej zawierają nazwę "Backend Library Project"
		self.assertIn('Backend Library Project', self.browser.title)
		self.assertIn('Backend Library Project', header_text)


		# Użytkownik wchodząc na stronę główną otrzymuje komunikat o możliwości przeglądania serwisu bez rejestracji oraz okienko do 
		# rejestracji/logowania na stronę biblioteki, w celu korzystania z innych możliwości serwisu.
		
		link = self.browser.find_element_by_partial_link_text('wo signing in')
		print(link)
		self.assertIn('View library collection wo signing in', link.text)

		"""

		"""
		self.fail('Zakończenie testu!')





# Niezainteresowany rejestracją postanawia kliknąć na link pod okienkiem rejestracji/logowania
# "Przeglądaj księgozbiór biblioteki bez logowania"


# 
