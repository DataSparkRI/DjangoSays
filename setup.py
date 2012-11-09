from setuptools import setup, find_packages

setup(
    name='django-says',
    version='0.9',
    license="BSD",

    install_requires = [],

    description = 'App wide messages for Django',

    author='Angel Medrano',
    author_email='asmedrano@gmail.com',
    url='https://github.com/ProvidencePlan/DjangoSays',
    download_url='https://github.com/ProvidencePlan/DjangoSays/downloads',
    include_package_data = True,
    packages=['says'],
    classifiers=[
        'Development Status::4- Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Django Developers',
        'License :: BSD License',
        'Operating System :: OS independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
