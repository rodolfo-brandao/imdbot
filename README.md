# IMDbot - The Internet Movie Database discord bot

![MIT License](https://img.shields.io/github/license/rodolfo-brandao/imdbot)
![Python version](https://img.shields.io/badge/python-3.10.2-blue)

## 1. Overview
This is a [Discord](https://discord.com/) bot to explore movies and series straight from the [IMDb-API](https://imdb-api.com/).

## 2. Dependencies
- [discord.py](https://pypi.org/project/discord.py/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://pypi.org/project/requests/)

These packages can be installed through `requirements.txt` file by simply running the following [pip](https://pip.pypa.io/en/stable/) command:

```bash
$ pip install -r requirements.txt
```

## 3. Avaliable commands
- `imdbot help`<br>Lists all bot commands.<br><br>
- `imdbot help <command>`<br>Details the specified command.<br><br>
- `imdbot ping`<br>Shows the bot latency in milliseconds.<br><br>
- `imdbot [movies|series] <args>`<br>Lists all movies or series whose title/description matches the given arguments.<br><br>
- `imdbot details <id>`<br>Lists all movie/series details by the given id.

Once you search for movies or series through the `imdbot [movies|series] <args>` command, simply use the **id** of the desired title in the `imdbot details <id>` command.
