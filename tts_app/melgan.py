import yaml
from tensorflow_tts.models import TFMelGANGenerator
from tensorflow_tts.configs import MelGANGeneratorConfig

from tts_app.conf import get_weight_path


def get_model():
	with open( get_weight_path('melgan_config.yml') ) as f:
		config = yaml.load(f, Loader=yaml.Loader)

	config = MelGANGeneratorConfig(**config["generator_params"])
	melgan = TFMelGANGenerator(config=config, name="melgan_generator")
	melgan._build()
	melgan.load_weights( get_weight_path('melgan-1M6.h5') )

	return melgan
