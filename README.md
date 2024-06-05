# Documentation for LeafMachine2

This is the documentation repository for [leafmachine2](https://github.com/Gene-Weaver/LeafMachine2), a suite of computer vision and machine learning algorithms that enables efficient identification, location, and measurement of vegetative, reproductive, and archival components from digital plant datasets.

## Installation

This documentation uses the [pydata sphinx theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/). To download the repository and run locally, follow the instructions below.

### Clone the GitHub repository

```shell
git clone "https://github.com/Gene-Weaver/docs-LM2"
cd docs-LM2
```
### Install Sphinx

To avoid duplication and to ensure that the installation details are accurate, please refer to the [sphinx documentation for installing sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html). There is a comprehensive list of operating systems and package managers supported.

## Structure

The documentation is written according to the [reStructured text format](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html). These files are contained within `/source`. The directories are the top level categories to which the individual documents belong, enabling easier navigation of the site.

## Building the site

If you make a change to one of the source files and would like to see what it will look like, run the following from the root of the `docs-LM2` respository 

```shell
sphinx-build -M html .\source\ .\build -a
```

This will create a directory called `build` which will contain html files that can be served through the web browser. Navigate to this folder (either through the command line or through your file explorer) and open `index.html`. You should now be able to navigate a copy of the documentation site in your browser. This build directory is ignored by git.

## Contributing

Coming soon!