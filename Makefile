all: html

html: PropertiesOfCodeReviewSocialStructures.rst
	rst2html.py PropertiesOfCodeReviewSocialStructures.rst index.html

json_graphs: src/create_graphs.py
	python src/create_graphs.py
