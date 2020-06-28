from setuptools import setup
setup(
    name = 'Pycli',
    version = '0.1.0',
    packages = ['Pycli'],
    entry_points = {
        'console_scripts': [
            'Pycli = Pycli.__main__:main'
        ]
    })
