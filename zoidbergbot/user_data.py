# 8888888888P         d8b      888 888                                    888               888
#       d88P          Y8P      888 888                                    888               888
#      d88P                    888 888                                    888               888
#     d88P    .d88b.  888  .d88888 88888b.   .d88b.  888d888 .d88b.       88888b.   .d88b.  888888
#    d88P    d88""88b 888 d88" 888 888 "88b d8P  Y8b 888P"  d88P"88b      888 "88b d88""88b 888
#   d88P     888  888 888 888  888 888  888 88888888 888    888  888      888  888 888  888 888
#  d88P      Y88..88P 888 Y88b 888 888 d88P Y8b.     888    Y88b 888      888 d88P Y88..88P Y88b.
# d8888888888 "Y88P"  888  "Y88888 88888P"   "Y8888  888     "Y88888      88888P"   "Y88P"   "Y888
# This software is provided free of charge without a warranty.   888
# This Source Code Form is subject to the terms of the      Y8b d88P
# Mozilla Public License, v. 2.0. If a copy of the MPL was   "Y88P"
# this file, You can obtain one at https://mozilla.org/MPL/2.0/.

# This is designed to be used with Zoidberg bot, however I'm sure it could be adapted to work with your own projects.
# If there is an issue that might cause issue on your own bot, feel free to pull request if it will improve something.<3

# This isn't even really a cog.
from zoidbergbot.config import *
import sqlite3


# TODO: It's probably worth adding something to remove servers when the bot has been removed or perhaps even inactive
#  servers if it gets to the point of causing an actual response time issue
if not os.path.isfile(os.getcwd() + '\\data.db'):
    print("Logging DB missing! Creating new DB. ")
    connection = sqlite3.connect(os.getcwd() + '\\data.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE logging (
                    guild INTEGER,
                    log_channel INTEGER,
                    message_log_channel INTEGER,
                    log_joins BOOLEAN,
                    log_leaves BOOLEAN,
                    log_invites BOOLEAN,
                    log_messages BOOLEAN,
                    log_message_edits BOOLEAN,
                    log_roles BOOLEAN,
                    log_profile BOOLEAN,
                    log_nickname BOOLEAN,
                    log_user_nickname BOOLEAN,
                    log_bans BOOLEAN,
                    log_kicks BOOLEAN,
                    log_vc_mute BOOLEAN,
                    log_vc_move BOOLEAN,
                    log_vc_kick BOOLEAN,
                    log_vc_user_mute BOOLEAN,        
                    log_vc_user_leave BOOLEAN  
                    )"""
                   )
else:
    # I know that sqlite3 will automatically make the db file, but I'd prefer to handle it like this.
    connection = sqlite3.connect(os.getcwd() + '\\data.db')
    cursor = connection.cursor()


def initialize_server(guild):
    # This might be worth having it back up the db every time.
    cursor.execute(f'''INSERT INTO logging({guild})''')
    connection.commit()


def update_attribute(column, value, guild):
    cursor.execute(f"""UPDATE logging 
                    SET {column} = {value} 
                    WHERE guild = {guild}; 
                    """)
    connection.commit()


def get_val(val, guild):
    data = cursor.execute(f'SELECT {val} FROM logging WHERE guild = {guild}')
    return int(''.join(map(str, data.fetchall()[0])))