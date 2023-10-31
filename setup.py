from setuptools import setup, find_packages

setup(
    name="bot-assistant",
    version="0.1.0",
    description="cli bot assistant",
    packages=find_packages(),
    install_requires=[
        "prompt_toolkit==3.0.39",
        "python-dateutil==2.8.2",
    ],
    author="Data Fusion Team",
    author_email="romanslipchenko@gmail.com, Spogoretskyi@gmail.com, eadors@gmail.com, e.churylov@gmail.com",
    license="MIT",
    entry_points={
        "console_scripts": ["bot-assistant = modules.bot_assistant.main:main"]
    },
)
