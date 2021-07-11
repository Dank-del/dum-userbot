from os import path
from pyrogram import Client
import logging
from configparser import ConfigParser

config = ConfigParser()

config.read('ub.ini')
bot_prefixes = list(map(str, config.get('ub', 'prefixes').split()))

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('[bot]')

botclient = Client("bot", config_file='ub.ini', plugins={'root': path.join(__package__, 'components')})