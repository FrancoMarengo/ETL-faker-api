from setuptools import setup

setup(name='tap-fake-api',
      version='0.0.1',
      description="Singer tap para obtener data de fake API",
      author='Franco Marengo',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_fake_api'],
      install_requires=[
          'requests>=2.21.0',
          'singer-python>=2.1.4',
      ],
      entry_points='''
          [console_scripts]
          tap-fake-api=tap_fake_api:main
      ''',
      )
