import os
from setuptools import setup, find_packages
import uuid

from archive_gopro_videos import __version__ as version_string


requirements_path = os.path.join(
    os.path.dirname(__file__),
    'requirements.txt',
)
try:
    from pip.req import parse_requirements
    requirements = [
        str(req.req) for req in parse_requirements(
            requirements_path,
            session=uuid.uuid1()
        )
    ]
except ImportError:
    requirements = []
    with open(requirements_path, 'r') as in_:
        requirements = [
            req for req in in_.readlines()
            if not req.startswith('-')
            and not req.startswith('#')
        ]


setup(
    name='archive-gopro-videos',
    version=version_string,
    url='https://github.com/coddingtonbear/archive-gopro-videos',
    description=(
        'Archive gopro videos.'
    ),
    author='Adam Coddington',
    author_email='me@adamcoddington.net',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=requirements,
    tests_require=['tox'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'archive-gopro-videos = archive_gopro_videos.cmdline:main'
        ],
    },
)
