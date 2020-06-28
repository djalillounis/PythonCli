from setuptools import setup
setup(
    name = 'Py-cli',
    version = '0.1.0',
    packages = ['Py-cli'],
    entry_points = {
        'console_scripts': [
            'Py-cli = Py-cli.__main__:main'
        ]
    })
