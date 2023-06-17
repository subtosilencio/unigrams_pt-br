#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""teste.py:

Unit tests for npl_word_segment.py.
"""

import unittest
import npl_word_segment


class Teste(unittest.TestCase):
    """Unit tests for npl_word_segment.py."""

    def test_create_unigrams(self):
        """Test create_unigrams function."""
        self.assertEqual(npl_word_segment.create_unigrams('the quick brown fox jumps over the lazy dog'),
                         {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1})

    def test_convert_accents_regex(self):
        """Test convert_accents_regex function."""
        self.assertEqual(npl_word_segment.convert_accents_regex('áéíóúàèìòùâêîôûãõäëïöüç'),
                         'aeiouaeiouaeiouaoaeiouc')

    def test_clean_text(self):
        """Test clean_text function."""
        self.assertEqual(npl_word_segment.clean_text(r'á+éíó-úàè"ìò\ùâ|êîôû/ã--õäë=ïöüç'),
                         'aeiouaeiouaeiouaoaeiouc')
