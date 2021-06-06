from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from urllib.parse import urljoin
from main_library.models import Bookshelf
import main_library.admin

from main_library.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		# response = home_page(request)
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'main_library/base.html')

class Adding_n_deleting_books_admin_view(TestCase):

	def test_admin_view_displays_table_of_books_with_it_properties(self):
		pass




