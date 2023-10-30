from setuptools import setup, find_packages

setup(
    name="bot-assistant",
    version="0.1.0",
    description="cli bot assistant",
    packages=find_packages(),
    author="Data Fusion Team",
    author_email="romanslipchenko@gmail.com, Spogoretskyi@gmail.com, eadors@gmail.com, e.churylov@gmail.com",
    license="MIT",
    entry_points={
        "console_scripts": ["bot-assistant = modules.bot_assistant.main:main"]
    },
)
