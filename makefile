SETTINGS=sanbot.settings
PYTHON_ENV := DJANGO_SETTINGS_MODULE=$(SETTINGS) ./env/bin/python
PIP_ENV := DJANGO_SETTINGS_MODULE=$(SETTINGS) ./env/bin/pip
COVERAGE_ENV := DJANGO_SETTINGS_MODULE=$(SETTINGS) ./env/bin/coverage
DEPS := grep -vE '^\s*\#' $(CURDIR)/requirements/system.txt  | tr '\n' ' '


run:
	python manage.py runserver

install:
	./env/bin/pip install -r prueba.txt

help:
	@echo
	@echo ----------------------------------------------------------------------
	@echo "   >>>>>                 DevZone               <<<<<   "
	@echo ----------------------------------------------------------------------
	@echo
	@echo "   - install     SETTINGS=[settings]    Install App and their dependencies"
	@echo "   - superuser   SETTINGS=[settings]    Create a super user in production"
	@echo "   - server      SETTINGS=[settings]    Serve project for development"
	@echo "   - mail_server SETTINGS=[settings]    Open the Development Mail Server"
	@echo "   - shell       SETTINGS=[settings]    Run Django in shell mode for development"
	@echo "   - test        SETTINGS=[settings]    Run Django test cases"
	@echo
	@echo ----------------------------------------------------------------------
