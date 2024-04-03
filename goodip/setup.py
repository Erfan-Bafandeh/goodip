from setuptools import setup, find_packages

setup(
    name = 'goodip',
    version = '0.0.4',
    author= 'Erfan Bafandeh',
    author_email = 'user.enbh@gmail.com',
    description = 'you can get your ip address and get its information.',
    keywords = ['ip', 'myip', 'goodip', 'checkip'],
    long_description = open("README.md", encoding="utf-8").read(),
    python_requires="~=3.6",
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Erfan-Bafandeh/goodip',
    packages = find_packages(),
    install_requires = ["requests", "colorama", "beautifulsoup4"],
    classifiers = [
    	"Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
    ]
)
