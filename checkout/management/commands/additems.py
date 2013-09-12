from django.core.management import BaseCommand, CommandError
from checkout.models import Item, Person, Book
import json
import urllib2
import sys

class Command(BaseCommand):
	args = ''
	help = ''

	def handle(self, *args, **options):
		endpoint = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'
		while True:
			try:
				code = raw_input()
				book_data = json.loads(urllib2.urlopen(endpoint + code).read())['items'][0] 
				print book_data
				book_volume_data = book_data['volumeInfo']
				book = Book(title=book_volume_data['title'],code=code,description=book_volume_data['description'])
				book.image = book_volume_data['imageLinks']['thumbnail']
				if 'authors' in book_volume_data:
					book.author = ', '.join(book_volume_data['authors'])
				else:
					book.author = "Unknown"
				book.save()
			except Exception as e:
				print "book failed to scan: ", sys.exc_info()[0]# + e.strerror
