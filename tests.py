#! /usr/bin/env python
import unittest
import sys
from xmlrunner import XMLTestRunner
from colour_runner.runner import ColourTextTestRunner
from os import path


def thisDir():
    return path.dirname(path.realpath(__file__))

loader = unittest.TestLoader()
tests = loader.discover('.', pattern="test_*.py")

runner = ColourTextTestRunner()

if '--xml' in sys.argv:
    runner = XMLTestRunner(output='test-reports')

runner.run(tests)
