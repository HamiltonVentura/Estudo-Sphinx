import os
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = 'Suporte Senior'
copyright = '2025, Coopavel'
author = 'Coopavel'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = ['sphinxcontrib.plantuml','sphinx.ext.graphviz']

templates_path = ['_templates']
exclude_patterns = []
language = 'Pt_Br'




# Caminho para o PlantUML (ajuste conforme necessário)
plantuml = f'java -jar {os.path.expanduser("~/plantuml/plantuml.jar")}'


latex_engine = 'xelatex'  # ou 'pdflatex'

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '12pt',
    'preamble': r'''
        \usepackage{fontspec}
        \setmainfont{Times New Roman}
    ''',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#bizstyle
#alabaster
#sphinx_rtd_theme
html_theme = 'alabaster'
html_static_path = ['_static']

