# -*- coding: UTF-8 -*-

import os, sys, inspect, platform, subprocess

def is_windows():
	'''is unix os'''
	return 'Windows' in platform.system()


def is_unix():
	'''is unix os'''
	return 'Linux' in platform.system() or 'Darwin' in platform.system()


def is_virtual():
	'''Check current environment is a virtual environment'''
	return hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)


def which(program):
	'''Check program command-line path'''
	filepath, filename = os.path.split(program)

	def is_exe(file):
		return os.path.isfile(file) and os.access(path, os.X_OK)

	if filepath:
		if is_exe(program):
			return program
	else:
		for path in os.environ['PATH'].split(os.pathsep):
			exe_file = os.path.join(path, program)
			if is_exe(exe_file):
				return exe_file

	return None


def parents(name, path=None):
	'''Get parents name path'''
	parent_name = os.path.dirname(path or os.path.abspath(sys.modules['__main__'].__file__))

	paths = parent_name.split(os.sep)
	targetPaths = []
	for path in paths:
		targetPaths.append(path)
		if path == name:
			break
	return os.sep.join(targetPaths)


def root_path(root_name):
	'''Append root path'''
	path = parents(root_name)
	if path not in sys.path:
		sys.path.append(path)


def abs_path_wrapper(file, deep=1):
	frame = inspect.stack()[deep]
	caller_dir = os.path.dirname(frame.filename)
	return os.path.normpath(os.path.join(caller_dir, file))


def existed(files, deep=2):
	'''Files existed'''
	is_existed = True
	if type(files) != list:
		files = [files]
	for file in files:
		path = abs_path_wrapper(file, deep)
		is_existed = is_existed and os.path.exists(path)
	return is_existed


def read(filename):
	'''Get file content'''
	if existed(filename, 3):
		try:
			with open(abs_path_wrapper(filename, 2), 'rt') as file:
				return file.read()
		except OSError as err_msg:
			return err_msg
	else:
		return False


def write(filename, content):
	'''Write file content'''
	try:
		with open(abs_path_wrapper(filename, 2), 'wt') as file:
			file.write(content)
			file.close()
	except OSError as err_msg:
		return err_msg


def exec_cmd(cmd):
	'''execute command'''
	return not os.system(cmd)


def exec_sub_cmd(cmd):
	'''execute command in subprocess'''
	return subprocess.Popen(cmd, shell=True).wait()


class Property(object):
	'''
	Class property
	--------------------------
	Usage:

	class Status(enum.Enum):
		WAITING = 0,
		RUNNING = 1
	'''

	def __init__(self, getter):
		self.getter = getter

	def __get__(self, instance, owner):
		return self.getter(owner)