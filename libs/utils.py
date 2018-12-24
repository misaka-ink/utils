# -*- coding: UTF-8 -*-

# from .__version__ import __version__ as VERSION

import os, sys

platform = sys.platform

def check_files_exists(files):
	'Check files exists'

	pass

def get_file_content(filename):
	'Get file content'

	if check_files_exists(filename):
		with open(filename) as file:
			content = file
			return content
	else:
		return False

def which(program):
	'Get program command path'

	def is_exe(path):
		return os.path.isfile(path) and os.access(path, os.X_OK)

	filepath, filename = os.path.split(program)

	if filepath:
		if is_exe(program):
			return program
	else:
		for path in os.environ["PATH"].split(os.pathsep):
			exe_file = os.path.join(path, program)
			if is_exe(exe_file):
				return exe_file

	return None

def is_virtual():
	'Check if the current environment is a virtual machine'

	return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))