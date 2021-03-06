from setuptools import setup, find_packages

name = 'onegov.ballot'
version = '3.10.1'


def get_long_description():
    readme = open('README.rst').read()
    history = open('HISTORY.rst').read()
    return '\n'.join((readme, history))


setup(
    name=name,
    version=version,
    description='Votes and elections for OneGov.',
    long_description=get_long_description(),
    url='http://github.com/onegov/onegov.ballot',
    author='Seantis GmbH',
    author_email='info@seantis.ch',
    license='GPLv2',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=name.split('.')[:-1],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    python_requires='>=3.6',
    install_requires=[
        'onegov.core>=0.4.0',
        'sqlalchemy',
        'sqlalchemy_utils'
    ],
    extras_require=dict(
        test=[
            'coverage',
            'freezegun',
            'onegov_testing',
            'pytest'
        ],
    ),
    entry_points={
        'onegov': [
            'upgrade = onegov.ballot.upgrade'
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    ]
)
