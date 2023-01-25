# PingMe - A simple Telegram notifier

Simple functions / classes for Matlab (GNU Octave), Python and Bash to send
markdown-formatted, optionally silent, messages via a telegram bot.  
Intended to inform you about program or system states / crashes, etc.

## Telegram Setup

Instructions on how to create a Telegram Bot and get your API key, as well as a message ID
can be found e.g. [here](https://core.telegram.org/bots#how-do-i-create-a-bot).

## Installation

The scripts are small with minimal dependencies.

Python requires the [`requests`](https://pypi.org/project/requests/) package,
Matlab (GNU Octave) and Bash require `curl`.

To intall, just drop the file into the program's PATH, or copy the function into
your script

## Usage

### Python

```python
pm = PingMe('apikey', 'chatid')
pm.ping('Hello from __Python__!', silent=True)
```

### Matlab / GNU Octave

```octave
pingme('Hello from __GNU Octave__!', 'api_key','chatid', 0)
```

### Bash

Note: Telegram API keys seem to contain a `:`, replace with `%`

```bash
pingme "Hello from __BASH__!" secretkey chatid false
```
