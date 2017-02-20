from setuptools import setup

setup(name='twitter',
      version='0.1',
      description='Extract, Transform and Load (ETL) Twitter Data ',
      url='http://github.com/Alan-F/USI-Impact-L-Train-Shutdown',
      author='Dongjie Fan',
      author_email='df1676@nyu.edu',
      license='MIT',
      packages=['twitter'],
      install_requires=[
          'tweepy',
      ],
      #dependency_links=[]
      zip_safe=False)