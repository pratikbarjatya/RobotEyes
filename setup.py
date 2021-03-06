from setuptools import setup, find_packages
import sys, os

version = '0.45'

setup(name='robotframework-eyes',
      version=version,
      description="Visual regression library and report generator for robot framework",
      long_description="""\
Visual regression library and report generator for robot framework. Capture elements, fullscreens and compare them against baseline images. Extends Selenium2Libary. Visit https://github.com/jz-jess/RobotEyes for documentation.""",
      classifiers=[
        'Framework :: Robot Framework',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
      ],
      keywords='visual-regression image-comparison robotframework robot-eyes',
      author='Jesse Zacharias Priyadharshini Chandana',
      author_email='iamjess988@gmail.com',
      url='https://github.com/jz-jess/RobotEyes',
      scripts=[os.path.join('scripts', 'reportgen')],
      license='Apache License 2.0',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'pillow',
          'robotframework',
          'robotframework-selenium2library'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
