from distutils.core import setup

setup(
    name='django-international',
    description='Country and currency data for Django projects',
    long_description='Models, forms, and data for use with projects that '
    'require country- and currency-related functionality.',
    version='0.0.1',
    packages=['international'],
    author='Monwara LLC',
    author_email='branko@monwara.com',
    url='https://bitbucket.org/monwara/django-international',
    download_url='https://bitbucket.org/monwara/django-international/downloads',
    license='BSD',
    classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
    ],
)


