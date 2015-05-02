from setuptools import setup

setup(
    name='docker-update',
    version='0.1.0',
    description='Generate commands you need to upgrade your docker containers',
    url='https://github.com/iamfat/docker-update',
    author="Jia Huang",
    author_email="iamfat@gmail.com",
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='docker update parse upgrade',
    packages=['docker_update'],
    install_requires=["docker-parse"],
    entry_points={
        'console_scripts': [
            'docker-update=docker_update:main',
        ],
    },
)
