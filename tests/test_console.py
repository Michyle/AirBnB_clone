#!/usr/bin/python3
"""Tests for the console"""

import unittest
import console
from console import HBNBCommand

class test_console(unittest.TestCase):
    """class to test console"""

    def create(self):
        """create the intance"""
        return HBNBCommand()

    def test_quit(self):
        """ A test for the method quit
        """
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def tests_EOF(self):
        """EOF method tests
        """
        con = self.create()
        self.asssertTrue(con.onecmd("EOF"))
