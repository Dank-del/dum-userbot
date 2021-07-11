from os import path
from pyrogram import Client
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('[bot]')

botclient = Client("bot", config_file='ub.ini', plugins={'root': path.join(__package__, 'components')})