import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="auto-openvpn",
    version="0.0.2",
    author="Aashutosh Rathi",
    author_email="aashutoshrathi@gmail.com",
    description="One command OpenVPN free account",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aashutoshrathi/auto-openvpn",
    packages=setuptools.find_packages(),
    install_requires=['selenium', 'pyperclip'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
		'console_scripts': [
			'aovpn = openvpn.makeIt:run',
		],
	}
)