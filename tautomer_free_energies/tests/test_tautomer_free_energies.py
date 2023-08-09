"""
Unit and regression test for the tautomer_free_energies package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import tautomer_free_energies


def test_tautomer_free_energies_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "tautomer_free_energies" in sys.modules
