from setuptools import setup


extra_packages = {
    'testing': ['pytest', 'pytest-watch', 'pytest-cov']
}


setup(
    name="echo_server",
    description="Implements the echo server assignment",
    version=0.1,
    author="Casey O'Kane" "Anna Shelby",
    author_email="okanecasey@gmail.com",
    license="MIT",
    py_modules=["server, client"],
    package_dir={'': 'src'},
    install_requires=["ipython", "pytest"],
    extras_require=extra_packages,
)
