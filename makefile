# Makefile for cleaning, building, and copying files

BUILD_DIR = build

JUPYTER_NOTEBOOK = jalt-intro-to-data-analysis.ipynb

OUTPUT_NAME = $(BUILD_DIR)/jalt2023-intro-to-data-analysis

# Define targets
.PHONY: all clean copy zip

all: clean $(BUILD_DIR) copy html

clean:
	rm -rf $(BUILD_DIR)
	rm _temp.ipynb

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

copy: $(BUILD_DIR)
	cp -r assets $(BUILD_DIR)/assets
	cp $(JUPYTER_NOTEBOOK) $(BUILD_DIR)/$(JUPYTER_NOTEBOOK)
	cp post_pizza_material.xlsx $(BUILD_DIR)/post_pizza_material.xlsx
	cp pre_pizza_material.xlsx $(BUILD_DIR)/pre_pizza_material.xlsx
	cp pckg-readme.txt $(BUILD_DIR)/readme.txt

slides:
	jupyter-nbconvert slides_version_freeze.ipynb --execute --to slides --embed-images --output slide_presentation --SlidesExporter.reveal_scroll=True

html: $(BUILD_DIR)
	python gen-toc.py $(JUPYTER_NOTEBOOK)
	jupyter-nbconvert _temp.ipynb --execute --to html --embed-images --output $(OUTPUT_NAME)

gh-pages: html
	cp $(OUTPUT_NAME).html ./index.html

zip: all
	rm -rf $(BUILD_DIR)/jalt-intro-to-data-analysis.zip
	cd $(BUILD_DIR); zip -r jalt-intro-to-data-analysis.zip ./* -x "*.DS_Store" -x "*.svn" -x "*__MACOSX" -x "*.git"
