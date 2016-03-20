import os

try:
    CERTIFICATE_PATH = os.environ['CERTIFICATE_PATH']
    BOT_URL = os.environ['BOT_URL']
    PORT = int(os.environ['PORT'])
except KeyError:
    CERTIFICATE_PATH = None
    BOT_URL = None
    PORT = None