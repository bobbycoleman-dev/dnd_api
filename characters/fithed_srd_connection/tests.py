from __init__ import *
from pprint import pprint

# Create your tests here.

# "Good" not in the list of alignments, warning should print

pprint(get_all_classes())

assert get_alignment_by_index("Good") == {"error": "Not found"}
print("Testing get_alignment_by_index() with incorrect index: PASSED")

assert "error" not in get_alignment_by_index("lawful-good")
print("Testing get_alignment_by_index() with lawful-good index: PASSED")
