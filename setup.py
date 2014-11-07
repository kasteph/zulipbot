from setuptools import setup

setup(
    name="zulipbot",
    version="0.0.1",
    author="Steph Samson",
    author_email="sdvsamson@gmail.com",
    description=("The unofficial bot API for Zulip."),
    license="MIT",
    keywords="zulip bot api zulipbot",
    url="http://github.com/stephsamson/zulipbot",
    packages=['zulipbot'],
    package_data={'zulipbot': ['LICENSE', 'README.rst']},
    long_description=open('README.rst').read(),
    install_requires=['requests>=2.0.0', 'simplejson'],
)
