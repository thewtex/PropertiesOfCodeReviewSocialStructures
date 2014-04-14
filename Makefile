all: html

html: PropertiesOfCodeReviewSocialStructures.rst
	rst2html.py PropertiesOfCodeReviewSocialStructures.rst index.html
