from setuptools import setup, find_packages

setup(name='treeds', 
      version='0.1', 
      url='https://github.com/harip/python-data-structures', 
      license='MIT', 
      author='harip', 
      author_email='harip', 
      description='Tree data structure', 
      packages=find_packages(exclude=['tests']), 
      long_description=open('README.md').read(), 
      zip_safe=False)