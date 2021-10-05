import sys, os,shutil
from distutils.core import setup

if os.path.exists('build') == True:
	print("build exists")
	shutil.rmtree('./build')

try:
    import numpy
except ImportError:
    sys.stderr.write('numpy is not installed, you can find it at: http://numpy.scipy.org \n')
    sys.exit()

#control version
if [int(dgt) for dgt in numpy.__version__.split('.')[:2]] < [1, 6]:
    sys.stderr.write('JWalk requires numpy v1.6 or later, you can find it at: http://numpy.scipy.org \n')
    sys.exit()

#biopython>=1.51/1.4?
try:
    import Bio
except ImportError:
    sys.stderr.write('Biopython is not installed, you can find it at: http://biopython.org/wiki/Main_Page \n')
    sys.exit()

if [int(dgt) for dgt in Bio.__version__.split('.')[:2]] < [1, 5]:
    sys.stderr.write('JWalk requires Biopython v1.5 or later, you can find it at: http://biopython.org/wiki/Main_Page \n')
    sys.exit()

# Make sure I have the right Python version.
if sys.version_info[:2] < (3, 5):
    print("JWalk requires Python 3.5 or better. Python {}.{} detected".format(*sys.version_info[:2]))
    print("Please upgrade your version of Python.")
    sys.exit(-1)



setup(
    name = "Jwalk",
    version = "2.0.0",
    author = "Josh Bullock",
    author_email = "j.bullock@cryst.bbk.ac.uk",
    maintainer = "Edgar Manriquez-Sandoval",
    maintainer_email = "emanriq1@jhu.edu",
    description = ("A tool to calculate SASDs between crosslinked residues "),
    packages=['Jwalk'],
    package_dir = {'':'src'},
    requires=['NumPy (>=1.6)',
        "Biopython (>= 1.5)",
    ],
    scripts=['src/Jwalk/jwalk'],

)

