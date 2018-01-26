#!/usr/bin/env python

from setuptools import find_packages, setup


install_requires = [
    'click'
]

test_require = [
    'tox',
]

extras_require = {
    'test': test_require,
}


setup(
    name='card-adv',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    extras_require=extras_require,
    entry_points={
        'console_scripts': [
            'card-adv=game.game:main',
        ],
    },
)
