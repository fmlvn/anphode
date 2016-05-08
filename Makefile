all:
	flake8 anphode pcrawler/pcrawler/spiders/

req:
	pip install -r requirements.txt -r requirements-test.txt

dep:
	apt-get install -y libxslt1-dev libxml2-dev python-dev libffi-dev libssl-dev

init: dep req
