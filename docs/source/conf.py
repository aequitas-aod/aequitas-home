# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'AEQUITAS'
copyright = '2024, Roberta Calegari'
author = 'Roberta Calegari, Andrea Borghesi'

release = '0.1'
version = '0.1.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx.ext.autosectionlabel',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ["_static"]
html_css_files = ["aequitas_style.css"]

#html_logo = "_static/logo_AEQUITAS_without_claim_Colors_RGB.svg"
html_logo = "_static/logo_AEQUITAS_without_claim_for_Dark_Background_RGB.svg"

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_allow_huge_pages = True
