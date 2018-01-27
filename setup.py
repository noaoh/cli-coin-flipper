#!/usr/bin/python3
from setuptools import setup, find_packages
setup(
        name='cli_coin_flipper',
        version='1.1.0',
        description='An animated coin flipper in your terminal',
        url='https://github.com/noaoh/cli-coin-flipper',
        author='Noah Holt',
        author_email='noahryanholt@gmail.com',
        license='GPL3',
        python_requires='>=3',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: End Users/Desktop',
            'Environment :: Console',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Natural Language :: English',
            ],
        package_data = {
            'assets' : ['assets.json'],
            'config' : ['config.ini']
            },
        keywords='coin fun command-line chance ascii', 
        packages=find_packages(exclude=['contrib', 'docs', 'tests']),
        install_requires=['argparse','configparser'],
        entry_points={'console_scripts': ['coin-flip =\
            coin:Main']},
)    

