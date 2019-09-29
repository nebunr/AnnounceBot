#   from secrets import *  # not in use

DISCORD_TOKEN = 'NTI2NTk1MTc4MDQ0MDYzNzQ1.XTosKA.MYIEBgRegziUeoqI4krVBW-n4Rc'
CHANNEL_INPUT = '528657263683043328'                # mod-log
CHANNEL_OUTPUT_DEFAULT = '363897513431793676'       # default
POLL_INTERVAL = 10


def get_ident(ident):
    if ident == 'ann':
        ident = '393326371411329024'             # ann
    elif ident == 'owl':
        ident = '393326427883307018'             # owl
    elif ident == 'owc':
        ident = '459293400730959872'             # owc
    elif ident == 'test':
        ident = '363897513431793676'             # test
    else:
        print("Invalid channel alias given")
        ident = CHANNEL_OUTPUT_DEFAULT
    return ident
# AnnounceBot
