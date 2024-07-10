import setuptools

setuptools.setup(
    name='calculator',
    version='1.0',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'calcu = cal:main'
        ]
    }
)
