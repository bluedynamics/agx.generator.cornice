# 

import os
from setuptools import (
    setup,
    find_packages,
)


version = "1.0"
shortdesc = ""
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()


setup(name="agx.generator.cornice",
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
          "",
      ],
      keywords="",
      author="",
      author_email="",
      url="",
      license="",
      packages=find_packages("src"),
      package_dir={"": "src"},
      namespace_packages=["agx", "agx.generator"],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          ##code-section dependencies
          'agx.generator.pyramid',
          ##/code-section dependencies
      ],
      extras_require=dict(
          ##code-section extras_require
          test=[
              'interlude',
          ],
          ##/code-section extras_require
      ),
      entry_points="""
      ##code-section entry_points
      [agx.generator]
        register = agx.generator.cornice:register
      ##/code-section entry_points
      """,
      ##code-section additionals
      ##/code-section additionals
      )
