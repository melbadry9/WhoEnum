from setuptools import setup, find_packages


EXTRAS = {}
REQUIRED = ["argparse", "future", "python-dateutil"]

setup(
    name="WhoEnum",
    version="0.1",
    description="Mass querying whois records using whois command line.",
    packages=find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),

    entry_points={
        'console_scripts': ['whoenum=whoisenum.whoenum:main'],
    },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    author="Mohamed Elbadry",
    author_email='me@melbadry9.xyz',
    url='https://github.com/melbadry9/WhoEnum',
)