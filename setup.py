from distutils.core import setup

setup(
    name='seedbox',
    version='0.4',
    packages=['seedbox'],
    url='',
    license='MIT',
    author='anthonyfox',
    author_email='anthonyfox1988@gmail.com',
    description='',
    py_modules=['seedbox'],
    install_requires=[
        'Click',
        'paramiko',
        'colorama',
    ],
    entry_points='''
        [console_scripts]
        seedbox=seedbox:cli
    ''',
)