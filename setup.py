from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='ctc-migration',
    version='0.1.0',
    description='Useful tool to migrate database with different schemas',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Hasan Aliyev',
    author_email='hasan.aliyev.555@gmail.com',
    keywords=['mysql', 'sqlalchemy', 'migration'],
    url='https://github.com/AliyevH/ctc_migration',
    download_url='https://pypi.org/project/ctc_migration/'
)

install_requires = [
    'mysqlclient>=2.0.1',
    'PyYAML==5.3.1',
    'SQLAlchemy==1.3.18'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)