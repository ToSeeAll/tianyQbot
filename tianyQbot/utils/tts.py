import os
import shutil

from azure.cognitiveservices.speech.audio import AudioOutputConfig
from azure.cognitiveservices.speech import ResultReason

from aspeak import SpeechServiceProvider, text_to_speech, AudioFormat, FileFormat, AspeakError


# output = AudioOutputConfig(use_default_speaker=True)


def text2mp3(_text):
    output = AudioOutputConfig(filename='output.mp3')
    try:
        provider = SpeechServiceProvider()
        result = text_to_speech(provider, output, _text,
                                voice="zh-CN-XiaoxiaoNeural", rate="-10%", pitch="0%", style="general",
                                audio_format=AudioFormat(FileFormat.MP3, 0))
        if result.reason != ResultReason.SynthesizingAudioCompleted:
            #
            return False
        else:
            # print(os.listdir('.'))
            shutil.move('output.mp3', 'tianyQbot/src/output.mp3')
            return True
    except AspeakError:
        # print("Error occurred while synthesizing speech.")
        return False
