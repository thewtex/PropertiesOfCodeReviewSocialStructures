all: html

html: PropertiesOfCodeReviewSocialStructures.rst style.css json_graphs
	rst2html PropertiesOfCodeReviewSocialStructures.rst --stylesheet=style.css index.html

json_graphs: src/create_graphs.py
	python src/create_graphs.py
