try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


setup(
    name='pythonTask',
    version='0.1.0',
    author='Walter P. Kuhn',
    author_email='wkuhn@ymail.com',
    packages=find_packages(),
    include_package_data=True,
    license='LICENSE.txt',
    description='Python tasks is a nice test provided by AGT.',
    long_description=open('README.txt').read(),
    install_requires=[
        "unittest2 >= 1.1.0",
    ],
)

