import logging
import os

from espeak_bot.audio import get_text_to_speech_file


log = logging.getLogger(__name__)


def reply_message(bot, message):
    if not message.text:
        log.debug('No text in message')
        return

    audio_file_path = get_text_to_speech_file(message.text)
    try:
        bot.sendVoice(chat_id=message.chat.id, voice=open(audio_file_path, 'rb'))
    except:
        raise
    finally:
        os.remove(audio_file_path)


