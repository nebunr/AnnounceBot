#!/usr/bin/python

import constants    # constants.py needed

import datetime     # pip install DateTime
import discord      # pip install discord.py

client = discord.Client()


@client.event
async def on_ready():
    print("Bot is online at:", datetime.datetime.now())


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # checks for the message prefix and if placed in proper channel
    if message.content.startswith('!read ') and message.channel.id == constants.CHANNEL_INPUT:
        read_date = [0, 0, 0, 0, 0, 0]   # year, month, day, hour, minute, second
        ident = 'test'                   # holds where msg is sent
        msg = message.content
        msg, read_date, ident = store_time(msg, read_date, ident)
        ident = constants.get_ident(ident)
        if error_time(read_date):
            ident == constants.CHANNEL_OUTPUT_DEFAULT
            msg = 'Invalid time given. Check if time has already past.'
        else:
            await check_time(read_date)
        await client.send_message(client.get_channel(ident), msg)


def store_time(msg, read_date, ident):
    msg = msg.replace("!read ", "")
    temp_msg = msg.split(";")[0]
    ident = msg.split(";")[1]
    ident = ident.replace(" ", "")
    msg = msg.split(";")[2]
    msg = msg.replace('"', '')  # .replace("'", '')

    temp_msg = temp_msg.replace(";", "").replace(msg, "")
    read_date[0] = temp_msg.split("-")[0]
    read_date[1] = temp_msg.split("-")[1]
    temp_msg = temp_msg.replace(read_date[0], "").replace(read_date[1], "").replace("-", "")
    read_date[2] = temp_msg.split(" ")[0]

    temp_msg = temp_msg.replace(read_date[2], "")
    read_date[3] = temp_msg.split(":")[0]
    read_date[4] = temp_msg.split(":")[1]
    temp_msg = temp_msg.replace(read_date[3], "").replace(read_date[4], "").replace(":", "")

    if temp_msg:
        read_date[5] = temp_msg

    read_date = [int(x) for x in read_date]
    print(read_date[0], read_date[1], read_date[2], read_date[3], read_date[4], read_date[5], ident)

    return msg, read_date, ident


def error_time(read_date):
    now = datetime.datetime.now()
    if now.year > read_date[0]:
        return True
    if now.year == read_date[0]:
        if now.month > read_date[1]:
            return True
        if now.month == read_date[1]:
            if now.day > read_date[2]:
                return True
            if now.day == read_date[2]:
                if now.hour > read_date[3]:
                    return True
                if now.hour == read_date[3]:
                    if now.minute > read_date[4]:
                        return True
    return False


async def check_time(read_date):
    while True:
        start = datetime.datetime.now() + datetime.timedelta(seconds=constants.POLL_INTERVAL)
        now = datetime.datetime.now()
        while datetime.datetime.now() < start:
            if read_date[0] == now.year and read_date[1] == now.month and read_date[2] == now.day and read_date[3] == now.hour and read_date[4] == now.minute:
                print("Printing message at:", datetime.datetime.now())
                return


if __name__ == '__main__':
    print("Starting bot at:", datetime.datetime.now())
    client.run(constants.DISCORD_TOKEN)
    print("Ending bot at:", datetime.datetime.now())
# AnnounceBot
