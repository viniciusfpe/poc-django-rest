run:
	python django/./manage.py runserver --settings=poc-django-rest.settings.development

test:
	coverage run --branch --source=django/poc-django-rest  django/./manage.py test django/poc-django-rest/ -v 2 --failfast --settings=poc.settings.test
	coverage report --omit=django/poc-django-rest/*/migrations*,django/poc-django-rest/settings/*,django/poc-django-rest/urls.py,django/poc-django-rest/wsgi.py,django/manage.py,django/poc-django-rest/*/tests/*,django/poc/__init__.py

html:
	coverage html --omit=django/poc-django-rest/*/migrations*,django/poc-django-rest/settings/*,django/poc-django-rest/urls.py,django/poc-django-rest/wsgi.py,django/manage.py,django/poc-django-rest/*/tests/*,django/poc/__init__.py
	open htmlcov/index.html

doc:
	$(MAKE) -C docs/ html
	open docs/build/html/index.html

clean:
	rm -f .coverage
	rm -rf htmlcov/
	rm -rf docs/build/