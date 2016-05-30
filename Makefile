run:
	python django/./manage.py runserver --settings=poc_django_rest.settings.development

test:
	coverage run --branch --source=django/poc_django_rest  django/./manage.py test django/poc_django_rest/ -v 2 --failfast --settings=poc_django_rest.settings.test
	coverage report --omit=django/poc_django_rest/*/migrations*,django/poc_django_rest/settings/*,django/poc_django_rest/urls.py,django/poc_django_rest/wsgi.py,django/manage.py,django/poc_django_rest/*/tests/*,django/poc/__init__.py

html:
	coverage html --omit=django/poc_django_rest/*/migrations*,django/poc_django_rest/settings/*,django/poc_django_rest/urls.py,django/poc_django_rest/wsgi.py,django/manage.py,django/poc_django_rest/*/tests/*,django/poc/__init__.py
	open htmlcov/index.html

doc:
	$(MAKE) -C docs/ html
	open docs/build/html/index.html

clean:
	rm -f .coverage
	rm -rf htmlcov/
	rm -rf docs/build/