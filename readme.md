# spacehey-scanner

A webscraping tool for SpaceHey that helps you find profiles via keywords.

**How it works:** The scraper will go through "Online Users" pages and gather profile links. It will then parse each profile and if it contains one of your keywords, its link is written to a text file.

Note that some websites and services are opposed and/or finnicky towards webscraping, so use this tool at your own risk.

### Basic Setup (Windows)

You will need to install the Python Programming Language. You can find downloads [here.](https://www.python.org/downloads/) Be sure to check "Add to PATH" so you are able to run Python.

Download this repo. You can just download the zip file and extract it or download [git](https://git-scm.com/downloads) and clone it.

Once you have the folder ready for use, look for the 'example.env' file and change it to your liking. **Be sure to separate each keyphrase with a comma then a space.**

Now, rename the file to .env

This step may not be needed but make a file called cool.txt in the folder.

Install the needed dependencies. Open the terminal and type "pip install -r requirements.txt"

Finally, in the folder, open the terminal and type "python main.py" and run it. If the file is empty for awhile, this is normal. Try adding more keywords or just wait. Note that you must restart the script if you make a change to the .env file.

### Basic Setup (Linux)

The steps here are near identical to Windows, except you may not need to install Python depending on your distribution.

The command to run may also be different, i.e "python3 main.py"

### Conclusion

Thanks for reading! Star the repo if you found it helpful, and for support or questions, open an issue or contact me on [spacehey](https://spacehey.com/rainyboyo), Discord @ rainy.boyo or on Matrix @ rainy:chat.rainys.pet