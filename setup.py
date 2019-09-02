from setuptools import setup, find_packages

setup(name='ignore4',
      version='1.0.0',
      url='https://github.com/Smeb/ignore4',
      license='MIT',
      author='Ben Ryves',
      author_email='bryves@gmail.com',
      entry_points={
          'console_scripts': [
              'ignore4=ignore4.main:cli'
          ]
      },
      description='A wrapper script for downloading gitignore files from github/gitignore',
      packages=['ignore4'],
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      zip_safe=False,
      )
