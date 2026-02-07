# test_digitalforge.py
"""
Tests for DigitalForge module.
"""

import unittest
from digitalforge import DigitalForge

class TestDigitalForge(unittest.TestCase):
    """Test cases for DigitalForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DigitalForge()
        self.assertIsInstance(instance, DigitalForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DigitalForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
