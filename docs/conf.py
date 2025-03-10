# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..")))

import aioca  # noqa

# -- General configuration ------------------------------------------------

# General information about the project.
project = "aioca"
copyright = "2019, Diamond Light Source"
author = "Tom Cobb"


# The full version, including alpha/beta/rc tags.
release = aioca.__version__

# The short X.Y version.
if "+" in release:
    # Not on a tag
    version = "master"
else:
    version = release

extensions = [
    # Use this for generating API docs
    "sphinx.ext.autodoc",
    # This can parse google style docstrings
    "sphinx.ext.napoleon",
    # For linking to external sphinx documentation
    "sphinx.ext.intersphinx",
    # Add links to source code in API docs
    "sphinx.ext.viewcode",
    # Adds the inheritance-diagram generation directive
    "sphinx.ext.inheritance_diagram",
    # Adds embedded graphviz support
    "sphinx.ext.graphviz",
    # Add multiple versions of documentation on CI
    "sphinx_multiversion",
]

# If true, Sphinx will warn about all references where the target cannot
# be found.
nitpicky = True

# Both the class’ and the __init__ method’s docstring are concatenated and
# inserted into the main body of the autoclass directive
autoclass_content = "both"

# Order the members by the order they appear in the source code
autodoc_member_order = "bysource"

# A dictionary for users defined type aliases that maps a type name to the
# full-qualified object name. It is used to keep type aliases not evaluated in
# the document. Defaults to empty ({}).
# TODO: drop when https://github.com/sphinx-doc/sphinx/issues/8934 works
autodoc_type_aliases = dict(
    Count="aioca.types.Count",
    Datatype="aioca.types.Datatype",
    Dbe="aioca.types.Dbe",
    Dbr="aioca.types.Dbr",
    Format="aioca.types.Format",
    Timeout="aioca.types.Timeout",
    # Explicitly tell sphinx to use the right namespace for these, otherwise
    # we get aioca._catools.CANothing that it can't find
    CANothing="aioca.CANothing",
    CAInfo="aioca.CAInfo",
    Subscription="aioca.Subscription",
)
# Output graphviz directive produced images in a scalable format
graphviz_output_format = "svg"

# The name of a reST role (builtin or Sphinx extension) to use as the default
# role, that is, for text marked up `like this`
default_role = "any"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "contents"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# These patterns also affect html_static_path and html_extra_path
exclude_patterns = ["_build"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

intersphinx_mapping = dict(
    python=("https://docs.python.org/3/", None),
    numpy=("https://docs.scipy.org/doc/numpy/", None),
)

# A dictionary of graphviz graph attributes for inheritance diagrams.
inheritance_graph_attrs = dict(rankdir="TB")

# Common links that should be available on every page
rst_epilog = """
.. _Diamond Light Source:
    http://www.diamond.ac.uk
"""

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# Override the colour in a custom css file
html_css_files = ["theme_overrides.css"]

# sphinx-multiversion config
smv_rebuild_tags = False
smv_tag_whitelist = r"^\d+\.\d+.*$"  # only document tags with form 0.9*
smv_branch_whitelist = r"^master$"  # only branch to document is master
smv_outputdir_format = "{ref.name}"
smv_prefer_remote_refs = False
smv_remote_whitelist = "origin|github"
