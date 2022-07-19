import sys, os

sys.path.append(os.path.abspath('sphinxext'))

extensions = ['extname']
extensions = ['myst_parser']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
