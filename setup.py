import setuptools

setuptools.setup(
    name='django-dajax3',
    version='0.9.3',
    author='Naved Rangwala',
    author_email='naved@ecarone.com',
    description=('Easy to use library to create asynchronous presentation '
                 'logic with django and dajaxice'),
    url='http://dajaxproject.com',
    license='BSD',
    packages=['dajax'],
    package_data={'dajax': ['static/dajax/*']},
    long_description=('dajax is a powerful tool to easily and super-quickly '
                      'develop asynchronous presentation logic in web '
                      'applications using python and almost no JS code. It '
                      'supports up to four of the most popular JS frameworks: '
                      'jQuery, Prototype, Dojo and mootols.'),
    install_requires=[
        'django-dajaxice3>=0.63'
    ],
    classifiers=['Development Status :: 4 - Beta',
                'Environment :: Web Environment',
                'Framework :: Django',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: BSD License',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Topic :: Utilities']
)
