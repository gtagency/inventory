Agnecy Inventory System
=======================

Item registration &amp; check out system

I'll be developing this in python/django.

The backend will be a some form of a sqlish database containing
all the user and item data. This will be exposed via a REST API
in django. There will be a web CRUD interface as well as a 
python script for interfacing with the scanner.

If you'd like to help, please contact me. I'm sure you can find
my email somewhere, you're smart.

Also feel free to submit pull requests, etc., and please please
tell me if you see my doing anything stupid.

thanks.
-T

Setup/Prereqs:
=============

<pre>
	sudo apt-get install python python-django
	python agencyinventory/manage.py syncdb
</pre>
