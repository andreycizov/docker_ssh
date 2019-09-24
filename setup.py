from setuptools import setup, find_packages

readme = open('README.rst').read()
history = open('HISTORY.rst').read()
reqs = [x.strip() for x in open('requirements.txt').readlines()]
test_reqs = [x.strip() for x in open('requirements-tests.txt').readlines()]

setup(
    name='docker_tunnel',
    version='0.0.1',
    author='Andrey Cizov',
    author_email='acizov@gmail.com',
    packages=find_packages(include=('docker_tunnel', 'docker_tunnel.*',)),
    description='Python docker SSH tunnel',
    keywords='',
    url='https://github.com/andreycizov/python-docker_tunnel',
    include_package_data=True,
    long_description=readme,
    install_requires=reqs,
    tests_require=test_reqs,
    entry_points={
        'console_scripts': [
            'docker-tunnel = docker_tunnel.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ]
)
