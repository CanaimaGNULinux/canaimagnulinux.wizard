from setuptools import setup, find_packages
import os

version = '0.1'
long_description = open("README.rst").read() + "\n" + \
                   open(os.path.join("docs", "INSTALL.txt")).read() + "\n" + \
                   open(os.path.join("docs", "HISTORY.txt")).read()

setup(name='canaimagnulinux.wizard',
      version=version,
      description="Wizard para llenar el perfil de usuario del portal Canaima GNU/Linux",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='wizard, profile, user, data, canaimagnulinux, plone',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='https://github.com/CanaimaGNULinux/canaimagnulinux.wizard',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['canaimagnulinux'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'five.grok',
          'plone.api',
          # -*- Extra requirements: -*-
          'canaimagnulinux.userdata',
          'collective.beaker',
          'collective.z3cform.wizard',
          'plone.namedfile',
          'plone.app.z3cform',
          'plone.formwidget.namedfile',
      ],
      extras_require={
          'test': [
              'plone.app.robotframework',
              'plone.app.testing [robot] >=4.2.2',
              'plone.browserlayer',
              'plone.testing',
              'robotsuite',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
