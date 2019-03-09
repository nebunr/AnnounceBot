# AnnounceBot
>`git clone linkaboveidunno`

This was made in Python 3.5 so get that, you also need the following packages and files:

> `pip install DateTime`  
> `pip install discord.py`  

> bot.py  
> constants.py  

bot.py holds the source code for the bot, you shouldn't have to edit it.  

constants.py contains the following and should be changed on how many channels you are outputting to:

```python
DISCORD_TOKEN = ''                # token goes here
CHANNEL_INPUT = ''                # mod-log (use channel id)
CHANNEL_OUTPUT_DEFAULT = ''       # default
POLL_INTERVAL = int               # seconds, default: 1
def get_ident(ident):
    if ident == 'ann':
        ident = ''             # ann
    elif ident == 'owl':
        ident = ''             # owl
    elif ident == 'owc':
        ident = ''             # owc
    elif ident == 'test':
        ident = ''             # test
    else:
        print("Invalid channel alias given")
        ident = CHANNEL_OUTPUT_DEFAULT
    return ident
```
This is an example for The Collegiate Hub for Overwatch announcements.  
This is what you need to post in `constants.CHANNEL_INPUT`:  
`!read YYYY-MM-DD HH:MM:SS; alias; message`  
`!read 2019-03-08 13:59:00; test; cool message goes here :moon2SMUG:`  
The alias determines where the message goes and should correspond to a variable from constants.CHANNEL_OUTPUT_
