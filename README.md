#  SIGAA_BOT
#### An automated way to interact with my college's site.


<p align="center">
<img src="assets/sigaabot.gif" alt="Demo" title="Demo"  width="720" height="480"/>
</p>


## Problem
It's so terrible the way that we are suposed to interact with the college site. We have to click im various things just to open the homepage.
## Solution
A bot to be used as a cli application, just to open and interact with the site with commands in the terminal.

## Requirements
- Make sure to download and unpack the latest version of geckodriver in its folder. You can also use the [get-gecko-driver python package](https://pypi.org/project/get-gecko-driver/) or my other project a bash script [geckodriver_downloader](https://github.com/italopinto/geckodriver_downloader) to automate the download, the unpack and move the driver to a folder in path, this only works on linux OS.
- If you want to use chromedriver will work, as well. However you might face an annoying bug. The browser sudenly shutoff after the bot finishes. I recommend to use geckodriver, but if you know how to fix this feel free to send me a pull request.
- run: `pip install -r requirements.txt`

## How I use it
- I use the `sigaabot_shell.bash` file in my pc, inside the `/usr/bin/` to access it anywhere with the terminal. How you could see in the demo above.
### TODO:
- [X] Make the bot work locally.
- [X] Make the sigaa methods work.
- [X] Supports both webdrivers. Gecko and Chrome.
- [ ] Formating in PEP 8.
- [X] Attach the `sigaabot.sh` in the repo. I use it locally for test and for daily access of the site. 