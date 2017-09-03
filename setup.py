from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='ObjectExtractor',
      version='0.1.5',
      description='Extract objects from images with OpenCV',
      url='https://github.com/ducthienbui97/ObjectExtractor',
      author='Thien Bui',
      author_email='thienbui797@gmail.com',
      license='BSD-3-Clause',
      packages=['object_extractor'],
      install_requires=['opencv-python'],
      package_data={'object_extractor': ['data/*.xml']},
      long_description=readme(),
      )
