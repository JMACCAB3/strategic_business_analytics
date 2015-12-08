PACKAGE=strategic_business_analytics

setup:
	@if [ -z $$VIRTUAL_ENV ]; then \
		echo "================================================================="; \
		echo "You should probably be running this from a virtual environment..."; \
		echo "================================================================="; \
		exit 1; \
	fi

	@echo "Installing dependencies..."; \
	pip install --quiet -r requirements.txt; \
	echo "Install complete!";
	
clean:
	@echo "Removing garbage..."
	@find . -name '*.pyc' -delete