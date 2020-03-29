project := grow-prod

install:
	pip install -r requirements.txt

deploy:
	gcloud app deploy \
	  -q \
	  --project=$(project) \
	  --no-promote \
	  --version=auto \
	  --verbosity=error \
	  app.yaml

develop:
	pipenv shell
	pipenv install
	pip install -r requirements.txt

run:
	pipenv shell
	make run
