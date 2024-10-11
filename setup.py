from setuptools import setup, find_packages

setup(
    name='SafeGuard_AI_Banking_Transaction',
    version='1.0.0',
    author='BERRAHAL Malek',
    author_email='berrahalmalek@gmail.com',
    description='Banking transaction fraud detection application using machine learning',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'sqlalchemy',
        'psycopg2-binary',
        'PyYAML',
        'scikit-learn',
        'imbalanced-learn',
        'fpdf',
        'pymysql',
    ],
)
