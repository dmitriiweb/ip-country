from setuptools import setup

with open('README.md') as readme:
    r = str(readme.read())

setup(
    name='ip_country',
    version='1.0.1',
    packages=['ip_country'],
    url='https://github.com/dmitriiweb/ip-country',
    license='MIT',
    author='Dmitrii K',
    author_email='winston.smith.spb@gmail.com',
    description='An offline tool to get country by IP',
    long_description=r,
    install_requires=[
        'pandas>=0.25.0',
    ],
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ),
)
