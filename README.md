# WolframAlpha Scraper

## Overview

The Wolfram Scraper allows you to create a simple and comprehensive image to answer all your questions.

It allows you to enter a search term, and it combines all the answers it can find on WolframAlpha ito a single image.

<br />

## Prerequisites

-   You will need a working installation of python.
-   You will also need to download the zip of this repo from the top of this page and extract it into a separate folder.
-   The following packages will need to be installed, preferably in a venv (see [Creating a venv](./README.md#creating-a-venvoptional)):
    -   PyQt5
    -   requests
    -   selenium
    -   PIL
-   They can be easily installed by using the command `pip install -r requirements.txt` in the terminal after opening it up in the same folder as the project files.

<br />

## Creating a venv(Optional)

-   A venv or virtual environment is a tool that can be used to manage all your installed packages.
-   You can create a venv in the _terminal_. The following screenshots are for Windows users, but macOS users can follow more or less the same instructions with a few slight changes that have been clearly mentioned.
-   Start off by moving to the directory where the project folder is located and using the command `python -m venv give-your-venv-a-name-here`
    -   Note that on macOS, you have to replace `python` with `python3`.
    -   Also note that the name you give the venv should not contain any spaces.
-   Then, activate it using the command `your-venv-name\Scripts\activate.bat`
    -   On macOS, the command should be `source your-venv-name/bin/activate`
-   Next, follow the third step of [Prerequisites](./README.md#prerequisites) to install all required packages in the
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

<br /><br />

#### Note: We are in no way affiliated with Wolfram Research, Inc., or its product, WolframAlpha. This is an experimental project purely for academic purposes. 