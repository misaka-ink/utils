# -*- coding: UTF-8 -*-

import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import utils

class UtilsTest(unittest.TestCase):
	def test_which(self):
		self.assertEqual(utils.which('sh'), '/bin/sh')

	def test_is_virtual(self):
		self.assertTrue(utils.is_virtual())

	def test_parents(self):
		self.assertEqual(utils.parents('utils', __file__), os.getcwd())

	def test_root_path(self):
		utils.root_path('utils')
		self.assertIn(utils.parents('utils', __file__), sys.path)

	def test_existed(self):
		self.assertTrue('./utils.py')
		self.assertTrue('../utils/utils.py')

	def test_write_read(self):
		filename = './write_demo.txt'
		test_filename = os.path.join(os.getcwd(), 'test', filename)
		content = 'test'
		utils.write(filename, content)
		self.assertTrue(os.path.exists(test_filename))
		self.assertEqual(utils.read(filename), content)
		os.remove(test_filename)

if __name__ == '__main__':
	unittest.main()
