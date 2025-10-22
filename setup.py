from setuptools import setup, find_packages

setup(
    name='econcli',
    version='1.0.0',
        package_dir={'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'econ = econcli.main:main',
        ],
    },
    author='Gemini',
    author_email='gemini@google.com',
    description='A CLI tool to track GDP, inflation, and other economic data for countries.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gemini/econcli',
)
