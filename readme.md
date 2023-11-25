# JALT2023 Introduction to Data Analysis with Python

*Prepared by [Chris Pirotto](https://chrispirotto.com) and Daniel Cook*

This repository contains the files used for preparation of distributed materials.

---

If you want to read through the material, it's recommended to read the HTML page [here](https://1dancook.github.io/JALT2023-Intro-to-Data-Analysis-with-Python/).

### Download the Material

You can download all of the material as a zip file directly from this website (github). At the time this was created, pressing the green `<> Code` button has the option to download all of the files as a zip file.

For those familiar with git and github, you can clone this repository.


### Opening the Notebook

If you want to use the notebook, you must install python, jupyter notebook (or jupyter lab), and any python dependencies (pandas, wordcloud).

Read instructions from [Jupyter documentation](https://docs.jupyter.org/en/latest/) for how to open the notebook and use it.


### Building the material for Distribution (macos/linux)

Requirements are python, jupyterlab, and any python dependencies.

Included is a `makefile`. Run `make` and it will generate a build directory.

See the `makefile` for any other targets.

Run `make gh-pages` to build `index.html` which is used for github pages.


### Versions of things

The materials / build tools were used with these versions:

```
Python 3.11.0
jupyter-lab 3.6.1
jupyter-nbconvert 7.2.9
pandas 1.5.3       # python library
```
