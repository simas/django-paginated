# coding: utf-8
from setuptools import setup

setup(
    name='django-paginated',
    version='0.1.2',
    description='Simple django digg-style pagiantion.',
    long_description=open('README.md').read(),
    url='http://github.com/simas/django-paginated',
    author=u'Simas Skrebiškis',
    author_email='simas.skrebiskis@gmail.com',
    license='MIT',
    packages=['paginated'],
    include_package_data=True,
    zip_safe=False
)
