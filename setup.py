#!/usr/bin/env python
#Copyright (c) 2008 Erik Tollerud (etolleru@uci.edu) 



from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup,find_packages

from astropysics.version import version as versionstr

setup(name='Astropysics',
      version=versionstr,
      description='Astrophysics libraries for Python',
      
      packages=find_packages(),
      package_data={'astropysics':['data/*']},
      scripts=['scripts/spylot','scripts/fitsinfo'],
      install_requires=['numpy','scipy'],
      provides=['astropysics'],
      extras_require={'plots':'matplotlib',
                      'guis':['traits','traitsGUI','chaco'],
                      'gui3d':'mayavi',
                      'fits':'pyfits',
                      'all':['matplotlib','traits','traitsGUI','chaco','pyfits','mayavi']},
      
      author='Erik Tollerud',
      author_email='etolleru@uci.edu',
      license = 'Apache License 2.0',
      url='http://www.physics.uci.edu/~etolleru/software.html#astropysics',
      
      
      long_description="""
      ``astropysics`` contains a variety of utilities and algorithms for 
      reducing, analyzing, and visualizing astronomical data.
      
      while ``astropysics`` requres only ``numpy`` and ``scipy``, other 
      packages are necessary for some of the functionality.  These include: 
      ``matplotlib``,``Traits``, ``TraitsGUI``, ``chaco``.
      """,
     )
