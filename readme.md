# spacehey-scanner

A webscraping tool for SpaceHey that helps you find profiles via keywords.

**How it works:** The scraper will go through "Online Users" pages and gather profile links. It will then parse each profile and if it contains one of your keywords, its link is written to a text file.

Note that some websites and services are opposed and/or finnicky towards webscraping, so use this tool at your own risk.

### Basic Setup (Windows)

You will need to install the Python Programming Language. You can find downloads [here.](https://www.python.org/downloads/) Be sure to check the "Add to PATH" option in the setup program so you are able to run Python.

Download this repo. You can just download the zip file [here](https://github.com/rainydevzz/spacehey-scanner/archive/refs/heads/main.zip) and extract it or download [git](https://git-scm.com/downloads) and clone it, which can be done by running `git clone https://github.com/rainydevzz/spacehey-scanner.git` in the command line.

Once you have the folder ready for use, look for the 'example.env' file and change it to your liking. **Be sure to separate each keyphrase with a comma then a space.**

Now, rename the file to .env

This step may not be needed but make a file called cool.txt in the folder.

Install the needed dependencies. Open the terminal and type "pip install -r requirements.txt"

Finally, in the folder, open the terminal and type "python main.py" and run it, which can be done by navigating to the folder in File Explorer, right clicking and selecting "Open In Terminal". If the file is empty for awhile, this is normal. Try adding more keywords or just wait. Note that you must restart the script if you make a change to the .env file.

If you'd like to quickly check the contents of the text file in the terminal, type `type cool.txt`.

If these steps fail, be sure you followed them exactly, and if issues persist, feel free to contact me. Depending on installation "pip" may not be a recognized program, so you can alternatively try `python -m pip install -r requirements.txt`. As mentioned the "Add to PATH" option in the Python installer is *extremely* important as it tells Windows where to find Python.

### Basic Setup (Linux)

The steps here are near identical to Windows, except you may not need to install Python depending on your distribution.

The command to run may also be different, i.e "python3 main.py"

To quickly check the file content in the terminal, type `cat cool.txt`.

### Other OSs (Mac, ChromeOS etc.)

I am unable to test the program on these OSs, however if you can verify they work on other OSs feel free to tell me. My best judgement however is that just about any OS that you can install and run Python on should be able to run this program.

### Conclusion

Thanks for reading! Star the repo if you found it helpful, and for support or questions, open an issue or contact me on [spacehey](https://spacehey.com/rainyboyo), Discord @ rainy.boyo or on Matrix @ rainy:chat.rainys.pet

If you'd like to improve this program, feel free to fork and/or open a PR, or just make changes locally. Suggestions are also welcome via issue or contacting me directly.