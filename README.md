# WolframAlpha Scraper

## Overview

The Wolfram Scraper allows you to create a simple and comprehensive image to answer all your questions.

It allows you to enter a search term, and it combines all the answers it can find on WolframAlpha ito a single image.

<br />

## Prerequisites

-   You will need a working installation of python.
-   The following packages will need to be installed, preferably in a venv(see [Creating a venv](./README.md#creating-a-venvoptional)):
    -   PyQt5 &nbsp;&nbsp;&nbsp;&nbsp;(`pip install PyQt5`)
    -   requests&nbsp;(`pip install requests`)
    -   selenium (`pip install selenium`)
    -   PIL&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(`pip install Pillow`)

<br />

## Creating a venv(Optional)

-   A venv or virtual environment is a tool that can be used to manage all your installed packages.
-   You can create a venv in the _terminal_. The following screenshots are for Windows users, but macOS users can follow more or less the same instructions with a few slight changes that have been clearly mentioned.
- Start off by moving to the directory where the project folder is located and using the command `python -m venv give-your-venv-a-name-here`
    -   Note that on macOS, you have to replace `python` with `python3`.
    -   Also note that the name you give the venv should not contain any spaces.
-   Then, activate it using the command `your-venv-name\Scripts\activate.bat`
    -   On macOS, the command should be `source your-venv-name/bin/activate`
-   Now you can run the program using the command `python Interface.py` - On macOS, it is `python3 Interface.py`
-   After you are done, you can close the program window and type in the command `deactivate` in the terminal.
    <br />

## How To Use

Simply start up the program and enter your search query in the text box and press search.
<img src="README-assets/pic1.png" /><br />
<img src="README-assets/pic2.png" /><br />

<p>You will notice that the logo starts spinning, indicating that it is waiting for the data to be fetched.</p><br />
<img src="README-assets/pic4.png" /><br />
<p>CLick on Results to view the compiled image.</p><br />
<img src="README-assets/pic5.png" /><br />
<p>You can also click save to save the image to disk.</p><br />
<img src="README-assets/pic6.png" />
