from distutils.core import setup

setup(
    name='django-international',
    description='Country and currency data for Django projects',
    long_description="django-international is a set of reusable components "
    "and data that can be used in Django projects that need to handle country "
    "and currency data. It contains forms, models, fixtures, and data in "
    "form usable directly by Python programs.",
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


