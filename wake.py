import pvporcupine
import pyaudio
import struct


def get_next_audio_frame():
  pass

def startlistening(callback):
  porcupine = pvporcupine.create(
  access_key='20vA5YzEyZWRvNdwuQDMQfmGZtZ97fva7nzU4hviTRHmfbIWzo+hTQ==',
  keyword=['Hey-Friday_en_windows_v3_0_0.ppn']
  )
  
  while True:
    audio_frame = get_next_audio_frame()
    keyword_index = porcupine.process(audio_frame)
    if keyword_index>=0:
      callback()