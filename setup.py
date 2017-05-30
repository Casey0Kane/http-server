from setuptools import setup


extra_packages = {
    'testing': ['pytest', 'pytest-watch', 'pytest-cov']
}


setup(
    name="echo_server",
    description="Implements the HTTP server assignment",
    version=0.1,
    author="Casey O'Kane" "Anna Shelby",
    author_email="okanecasey@gmail.com",
    license="MIT",
    py_modules=["server, client, concurrency"],
    package_dir={'': 'src'},
    install_requires=["ipython", "pytest", "gevent"],
    extras_require=extra_packages,
    entry_points={
        'console_scripts': [
            'client = client:client',
            'server = server:server',
            'concurrency = concurrency:concurrency'
        ]
    }
)
