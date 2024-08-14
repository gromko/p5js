# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['p5']

package_data = \
{'': ['*']}

install_requires = \
['pygame>=2.1.2,<3.0.0','pycairo>=1.20.0']

setup_kwargs = {
    'name': 'p5-python',
    'version': '0.6.29',
    'description': 'A package wrapping pygame functionality in p5.js calling conventions.',
    'long_description': '#p5 is a friendly tool for learning to code and make art. It is a free and open-source Python library built by an inclusive, nurturing community. p5 is a Python library that provides high level drawing functionality to help you quickly create simulations and interactive art using Python.',
    'author': 'Grygoriy Gromko',
    'author_email': 'gr.gromko@gmail.com',
    'maintainer':  'Grygoriy Gromko',
    'maintainer_email': 'gr.gromko@gmail.com',
    'url': 'https://github.com/gromko/p5-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.0',
}


setup(**setup_kwargs)
