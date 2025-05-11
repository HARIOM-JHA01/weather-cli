from setuptools import setup, find_packages

setup(
    name="weather_cli",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'requests',
        'typer',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'weather=weather_cli.weather:app',
        ],
    },
)
