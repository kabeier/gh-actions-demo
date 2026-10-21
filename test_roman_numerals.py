from roman_numerals import to_roman

def test_01_a_single_number():
    assert to_roman(1) == "I"

def test_04_all_edge_cases():
    assert to_roman(944) == "CMXLIV"
