from setuptools import setup

setup(
    name='django-international',
    description='Country and currency data for Django projects',
    long_description=open('README.rst').read(),
    version='0.0.3',
    packages=['international'],
    author='Monwara LLC',
    author_email='branko@monwara.com',
    url='https://bitbucket.org/monwara/django-international',
    download_url='https://bitbucket.org/monwara/django-international/downloads',
    license='BSD',
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
    ],
    include_package_data=True
)


