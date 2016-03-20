import logging

from telegram.dispatcher import run_async

from espeak_bot.reply import reply_message


log = logging.getLogger(__name__)


@run_async
def update_handler(bot, received, **kwargs):
    log.debug('Received: %s', received)

    reply_message(bot, received.message)
