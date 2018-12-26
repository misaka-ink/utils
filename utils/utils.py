# -*- coding: UTF-8 -*-

import os, sys
import yaml

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

def parents(parents_name, current_path = None):
	'Get parents name path'

	parent_name = os.path.dirname(current_path or os.path.abspath(__file__))
	dict_name = parent_name.split('/')[-1]
	if parents_name == dict_name:
		return parent_name
	elif dict_name == '/':
		return None
	else:
		return parents(parents_name, parent_name)

def root_path(root_name):
	'''
	Append root path
	:param root_name: append target folder name
	:return:
	'''

	rootpath = parents(root_name)
	sys.path.append(rootpath)

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

class classproperty(object):
	'Class property'

	'''
	Usage: 
	
	class Status(enum.Enum):
		WAITING = 0,
		RUNNING = 1
	'''

	def __init__(self, getter):
		self.getter= getter
	def __get__(self, instance, owner):
		return self.getter(owner)

def write_yaml(file, data):
	'''
	Write yaml file
	:param file: (path) filename
	:param data: write data
	:return: None is ok or error message
	'''
	try:
		with open(file, 'wb') as yaml_file:
			yaml.dump(data, yaml_file, default_flow_style=False)
			yaml_file.close()
			return None
	except OSError as err_msg:
		print err_msg

def read_yaml(file):
	'''
	Read yaml file
	:param file: (path) filename
	:return: file data or error message
	'''
	try:
		with open(file) as yaml_file:
			data = yaml.load(yaml_file)
			yaml_file.close()
			return data
	except OSError as err_msg:
		return err_msg