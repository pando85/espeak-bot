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

        languages = ['es-es', 'en-us', 'es-mx', 'ca-es', 'it-it', 'pt-pt', 'ru-ru', 'fr-fr', 'de-de', 'ja-jp']
        results = [get_inline_query_result(query, language) for language in languages]
        
        bot.answerInlineQuery(update.inline_query.id, results=results)


def get_inline_query_result(text, lang):
    url_text = urllib.parse.quote(text)
    url_audio = 'http://www.voicerss.org/controls/speech.ashx?src={text}&hl={lang}'.format(text=url_text, lang=lang)

    return InlineQueryResultVoice(
                id=hex(getrandbits(64))[2:],
                voice_url=url_audio,
                mime_type='video/mp4',
                title=lang.upper(),
                message_text=url_audio)

def error_handler(bot, update, error):
    log.warn('Update "%s" caused error "%s"' % (update, error))