from setuptools import setup, find_packages

version = '0.1'

setup(name='octopress-in-docker',
      version=version,
      description="A wrapper for using octopress in docker",
      long_description='',
      classifiers=[
          'Environment :: Console',
          'Operating System :: MacOS',
          'Operating System :: POSIX :: Linux',
          'Operating System :: POSIX :: BSD',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Topic :: Utilities',
      ],
      keywords='docker octopress',
      author='Xupeng Yun',
      author_email='xupeng@xupeng.me',
      url='https://github.com/xupeng/octopress-in-docker',
      license='BSD',
      packages=['octopress_in_docker'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points={
          'console_scripts': [
              'oid = octopress_in_docker:main',
          ]
      },
      )
