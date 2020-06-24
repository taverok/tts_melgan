import os

from tensorflow_tts.configs import FastSpeechConfig
from tensorflow_tts.models import TFFastSpeech
import yaml

from tts_app.conf import get_weight_path


def get_model():
    with open( get_weight_path('fastspeech_config.yml') ) as f:
        config = yaml.load(f, Loader=yaml.Loader)

    config = FastSpeechConfig(**config['fastspeech_params'])
    fastspeech = TFFastSpeech(config=config, name='fastspeech')
    fastspeech._build()
    fastspeech.load_weights( get_weight_path('fastspeech-150k.h5') )

    return fastspeech