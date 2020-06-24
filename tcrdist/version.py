
from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 2
_version_minor = 0
_version_micro = 0  # use '' for first of series, number for 1 and above
_version_extra = 'dev'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "tcrdist2: a package for analyzing TCR repertoire datasets"
# Long description will go up on the pypi page
long_description = """
tcrdist2
========
tcrdist2 is a package for analyzing T-cell receptor repertoire datasets.
Some of the functionality and code is adapted from the original tcr-dist
package which was released with the publication of  Dash et al.
Nature (2017) doi:10.1038/nature22383. This package contains a new API
for accessing the features of tcr-dist, as well as many new features.

The original code replicating analysis in the manuscript can be found at
https://github.com/phbradley/tcr-dist

To get started using these components in your own software, please go to the
repository README.
.. _README: https://github.com/kmayerb/tcrdist2/blob/API2/README.md

License
=======
``tcrdist2`` is licensed under the terms of the MIT license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.
All trademarks referenced herein are property of their respective holders.
Copyright (c) 2020, Phillip Harlan Bradley, Jeremy Chase Crawford, Andrew Fiore-Gartland, and Koshlan Mayer-Blackwell.
Fred Hutchinson Cancer Research Center.
"""

NAME = "tcrdist2"
MAINTAINER = "Koshlan Mayer-Blackwell"
MAINTAINER_EMAIL = "kmayerbl@fredhutch.org"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://github.com/kmayerb/tcrdist2"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "Phillip Harlan Bradley, Jeremy Chase Crawford, Andrew Fiore-Gartland, Koshlan Mayer-Blackwell"
AUTHOR_EMAIL = "kmayerbl@fredhutch.org"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {'tcrdist': ['datasets/test_human_pairseqs.tsv',
                            'datasets/test_mouse_pairseqs.tsv',
                            'db/*',
                            'db/alphabeta_db.tsv_files/*',
                            'db/alphabeta_db.tsv_files/probs_files_human_A/*',
                            'db/alphabeta_db.tsv_files/probs_files_human_B/*',
                            'db/alphabeta_db.tsv_files/probs_files_mouse_A/*',
                            'db/alphabeta_db.tsv_files/probs_files_mouse_B/*',
                            'db/blast_dbs/*',
                            'db/fasta/*',
                            'external/blargs/*',
                            'external/blast-2.2.16/bin/*',
                            'external/tablesorter/*']}
                            #]}#[pjoin('datasets', 'test_human_pairseqs.tsv'),pjoin('datasets', 'test_mouse_pairseqs.tsv'), pjoin('db', '*'), pjoin('external', '*')]}
REQUIRES = ["numpy", "pandas", "pytest", "scipy", "matplotlib", "parasail","seaborn", "statsmodels", "sklearn", "tables"]
