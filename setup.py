from setuptools import setup

def read( path ):
	with open(path, 'r') as f:
		return f.read()

setup(
	name = 'AnimateGraphViz',
	version = '1.1.1',
	description = 'A tool to create animated graph visualizations, based on graphviz, based on legacy source code of gvanim - Massimo Santini',
	long_description = read('README.md'),
	long_description_content_type='text/markdown',
	author = 'Tran Duy Thanh',
	author_email = 'coachtranduythanh@gmail.com',
	url = 'https://github.com/tranduythanh/GraphvizAnim',
	license = 'GNU/GPLv3',
	packages = ['animategv'],
	keywords = 'drawing graph animation',
	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
		'Operating System :: Unix',
		'Topic :: Software Development :: Libraries :: Python Modules'
	]
)
