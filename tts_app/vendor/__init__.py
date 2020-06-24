import os
import sys


def load_vendors():
	# Add vendor directory to module search path
	print("loading vendors")
	parent_dir = os.path.abspath(os.path.dirname(__file__))
	vendor_dir = os.path.join(parent_dir, 'vendor', 'TensorflowTTS')
	sys.path.append(parent_dir)
	sys.path.append(vendor_dir)
