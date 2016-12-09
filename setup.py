"""Setup file for the snowday/ code kata assignment."""


from setuptools import setup

setup(
    name="snowday",
    description="A series of code kata solutions.",
    version=0.1,
    author="Rachael Wisecarver",
    author_email="rachael.wisecarver@gmail.com",
    license="MIT",
    py_modules=[""],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']}
    )
