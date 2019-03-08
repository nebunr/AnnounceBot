#   from secrets import *  # not in use

DISCORD_TOKEN = ''
CHANNEL_INPUT = ''                # mod-log
CHANNEL_OUTPUT_1 = ''             # ann
CHANNEL_OUTPUT_2 = ''             # owl
CHANNEL_OUTPUT_3 = ''             # owc
CHANNEL_OUTPUT_4 = ''             # test
CHANNEL_OUTPUT_DEFAULT = ''       # default
POLL_INTERVAL = 1


def get_ident(ident):
    if ident == 'ann':
        ident = CHANNEL_OUTPUT_1
    elif ident == 'owl':
        ident = CHANNEL_OUTPUT_2
    elif ident == 'owc':
        ident = CHANNEL_OUTPUT_3
    elif ident == 'test':
        ident = CHANNEL_OUTPUT_4
    else:
        print("Invalid channel alias given")
        ident = CHANNEL_OUTPUT_DEFAULT
    return ident
# AnnounceBot
