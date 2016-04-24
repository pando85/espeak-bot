import logging
from random import getrandbits
import urllib

from telegram import InlineQueryResultVoice

from espeak_bot.reply import reply_message


log = logging.getLogger(__name__)


def update_handler(bot, received, **kwargs):
    log.debug('Received: %s', received)

    reply_message(bot, received.message)


def inline_query(bot, update):
    if update.inline_query is not None and update.inline_query.query:
        query = update.inline_query.query

        results = list()
        results.append(get_inline_query_result(query, 'es'))
        results.append(get_inline_query_result(query, 'en'))

        bot.answerInlineQuery(update.inline_query.id, results=results)


def get_inline_query_result(text, lang):
    url_text = urllib.parse.quote(text)
    url_audio = 'http://espeak.rors.org/tts?text={text}&voice={lang}&pitch=40&speed=140'.format(text=url_text, lang=lang)

    return InlineQueryResultVoice(
                id=hex(getrandbits(64))[2:],
                voice_url=url_audio,
                mime_type='video/mp4',
                title=lang.upper(),
                message_text=url_audio,
                thumb_url='http://www.cem.itesm.mx/cms/ecsh/images/Frecuencia_CEM/Escucha/Audio_Icono.jpg')

def error_handler(bot, update, error):
    log.warn('Update "%s" caused error "%s"' % (update, error))