from setuptools import setup

setup(
    name='data-augmentation',
    version='0.0.2',        
    packages=['src', 'src/processors', 'config', 'data'],
    python_requires='>=3.8.0',
    license='LICENSE',
    description='Code for Textual Feedback Detection',
    long_description=open('README.md').read(),
    install_requires=[]
)