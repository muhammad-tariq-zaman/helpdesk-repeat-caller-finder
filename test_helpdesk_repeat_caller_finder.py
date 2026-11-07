import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import find

def row(t, c):
    return {"ticket": t, "caller": c}

class TestRepeatCaller(unittest.TestCase):
    def test_repeat_found(self):
        self.assertEqual(find([row("T1", "Ali"), row("T2", "Ali"), row("T3", "Ali")], 3), [("Ali", 3)])
    def test_below_threshold_excluded(self):
        self.assertEqual(find([row("T1", "Ali"), row("T2", "Ali")], 3), [])
    def test_most_first(self):
        r = find([row("T1", "A"), row("T2", "A"), row("T3", "A"), row("T4", "B"), row("T5", "B"), row("T6", "B"), row("T7", "B")], 3)
        self.assertEqual(r[0][0], "B")
    def test_custom_threshold(self):
        self.assertEqual(len(find([row("T1", "Ali"), row("T2", "Ali")], 2)), 1)
