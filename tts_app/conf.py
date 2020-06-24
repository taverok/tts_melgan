import os


def get_weight_path(file: str) -> str:
	return os.path.sep.join( os.path.dirname(__file__).split(os.path.sep)[0:-1] + ["weight", file] )
