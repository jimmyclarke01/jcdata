from setuptools import setup

setup(
   name='jcdata',
   version='1.0',
   description='A useful module',
   author='James Clarke',
   author_email='james.clarke42@gmail.com',
   packages=['jcdatadata'],  #same as name
   install_requires=['pandas'], #external packages as dependencies
)