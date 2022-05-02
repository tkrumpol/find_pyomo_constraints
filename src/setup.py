from setuptools import setup

setup(
    name="find_pyomo_constraints",
    version="0.0.1",
    description="package to find all constraints where a pyomo variable occurs",
    maintainer="tom krumpolc",
    maintainer_email="tkrumpol@andrew.cmu.edu",
    license="GPL",
    packages=[],
    scripts=[],
    setup_requires=[],
    data_files=["LICENSE"],
    install_requires=[
        "pyomo",
    ],
    long_description="""\
package utilities
==============
given an instance of a pyomo concrete model and a pyomo variable (scalar or indexed),
return a list of all of the constraints where this variable occurs within the model.
Looking to add capabilities for parameters and expressions but these are not working
at this time. 
      """,
)
