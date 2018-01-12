"""CherryPy sphinx doc configuration module."""
# -*- coding: utf-8 -*-
#
# CherryPy documentation build configuration file, created by
# sphinx-quickstart on Sat Feb 20 09:18:03 2010.
#
# This file is execfile()d with the current directory set to its containing
# dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

from email import message_from_string
import importlib
import pkg_resources
import sys

assert sys.version_info > (3,), 'Python 3 required to build docs'


def try_import(mod_name):
    """Attempt importing module and suppress failure of doing this."""
    try:
        return importlib.import_module(mod_name)
    except ImportError:
        pass


custom_sphinx_theme = try_import('alabaster')

prj_dist = pkg_resources.get_distribution('cherrypy')
prj_pkg_info = prj_dist.get_metadata(prj_dist.PKG_INFO)
prj_meta = message_from_string(prj_pkg_info)
prj_author = prj_meta['Author']
prj_license = prj_meta['License']
prj_description = prj_meta['Description']

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'rst.linker',
    'jaraco.packaging.sphinx',
]

intersphinx_mapping = {
    'https://docs.python.org/3/': None,
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

project = prj_dist.project_name

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output ---------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = getattr(custom_sphinx_theme, '__name__', 'default')

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {
# "relbarbgcolor": "#880000",
#     "relbartextcolor": "white",
# "relbarlinkcolor": "#FFEEEE",
# "sidebarbgcolor": "#880000",
#     "sidebartextcolor": "white",
# "sidebarlinkcolor": "#FFEEEE",
# "headbgcolor": "#FFF8FB",
#     "headtextcolor": "black",
# "headlinkcolor": "#660000",
# "footerbgcolor": "#880000",
#     "footertextcolor": "white",
# "codebgcolor": "#FFEEEE",
# }
html_theme_options = {
    'logo': 'images/cherrypy_logo_big.png',
    'github_user': project.lower(),
    'github_repo': project.lower(),
    'github_button': True,
    'github_banner': True,
    'github_type': 'watch',
    'github_count': True,
    'travis_button': True,
    'codecov_button': True,
    # 'analytics_id': ...,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# html_style = 'cpdocmain.css'

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    'index': [
        'about.html', 'searchbox.html', 'navigation.html', 'python_2_eol.html',
    ],
    '**': [
        'about.html', 'searchbox.html', 'navigation.html', 'python_2_eol.html',
    ],
}

# Output file base name for HTML help builder.
htmlhelp_basename = 'CherryPydoc'


# -- Options for LaTeX output --------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author,
# documentclass [howto/manual]).
latex_documents = [
    (
        'index',
        'CherryPy.tex',
        'CherryPy Documentation',
        'CherryPy Team',
        'manual',
    ),
]


def mock_pywin32():
    """Mock pywin32 module.

    Resulting in Linux hosts, including ReadTheDocs,
    and other environments that don't have pywin32 can generate the docs
    properly including the PDF version.
    See:
    http://read-the-docs.readthedocs.org/en/latest/faq.html#i-get-import-errors-on-libraries-that-depend-on-c-modules
    """
    if try_import('win32api'):
        return

    from unittest import mock

    MOCK_MODULES = [
        'win32api', 'win32con', 'win32event', 'win32service',
        'win32serviceutil',
    ]
    for mod_name in MOCK_MODULES:
        sys.modules[mod_name] = mock.MagicMock()


mock_pywin32()

link_files = {
    '../CHANGES.rst': dict(
        using=dict(
            GH='https://github.com',
        ),
        replace=[
            dict(
                pattern=r'((Issue|PR)\s?)?#(?P<issue_or_pr>\d+)',
                url='{GH}/cherrypy/{project}/issues/{issue_or_pr}',
            ),
            dict(
                pattern=r'^(?m)((?P<scm_version>v?\d+(\.\d+){1,2}))\n[-=]+\n',
                with_scm='{text}\n{rev[timestamp]:%d %b %Y}\n',
            ),
            dict(
                pattern=r'PEP[- ](?P<pep_number>\d+)',
                url='https://www.python.org/dev/peps/pep-{pep_number:0>4}/',
            ),
            dict(
                # FIXME: currently this puts #v1.2.3 style version
                # into URL, but it should be v1-2-3
                pattern=r'cheroot v?(?P<cheroot_version>\d+(\.\d+){1,2})',
                url='https://cheroot.readthedocs.io'
                    '/en/latest/history.html#v{cheroot_version}',
            ),
        ],
    ),
}
