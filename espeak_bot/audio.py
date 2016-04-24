import os
import subprocess

from gtts import gTTS
from espeak_bot.utils import generate_random_string


def get_text_to_speech_file(text):
    tmp_file_path = '/tmp/{path}.mp3'.format( path = generate_random_string(20))
    tts = gTTS(text=text, lang='es')

    tts.save(tmp_file_path)

    return tmp_file_path
