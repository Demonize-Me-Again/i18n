from setuptools import setup

setup(
    name='i18n',
    version='0.0.1',
    description='Translation library for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Naegin',
    author_email='discord.naegin@gmail.com',
    url='https://github.com/Demonize-Me-Again/i18n',
    download_url='https://github.com/Demonize-Me-Again/i18n/archive/master.zip',
    license='MIT',
    packages=['i18n'],
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ],
)