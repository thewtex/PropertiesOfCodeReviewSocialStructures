all: html

html: PropertiesOfCodeReviewSocialStructures.rst style.css json_graphs itk_graph
	rst2html.py PropertiesOfCodeReviewSocialStructures.rst --stylesheet=style.css index.html

json_graphs: src/create_graphs.py
	python src/create_graphs.py

itk_graph: src/itk_graph.py
	python src/itk_graph.py
