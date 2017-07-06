from setuptools import setup

setup(
    name = 'Contactgious',
    version = '1.0',
    description = 'Flask back-end for contact form POST requests',
    author = 'Lim Jia Yee',
    author_email = 'jiayeerawr@gmail.com',
    install_requires = [
        'Flask == 0.12.2',
        'Flask-Mail == 0.9.1',
        'Flask-WTF == 0.14.2',
        'itsdangerous == 0.24',
        'Jinja2 == 2.9.6',
        'MarkupSafe == 1.0',
        'six == 1.10.0',
        'Werkzeug == 0.12.2',
        'WTForms == 2.1'
    ]
)