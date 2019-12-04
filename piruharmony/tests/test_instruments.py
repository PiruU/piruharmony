import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from instruments import *
from theory import ChordsTypes


def test_guitar_e_maj():
    tested_tablature = [0, 2, 2, 1, None, None]
    target_key_indices = [31, 38, 43, 47] # [E3, B3, E4, G#4]
    assert guitar().to_keyboard(tested_tablature) == target_key_indices

def test_guitar_d_maj():
    tested_tablature = [None, 3, 2, 0, 1, 0]
    target_key_indices = [39, 43, 46, 51, 55] # [C2, E4, G4, C5, E5]
    assert guitar().to_keyboard(tested_tablature) == target_key_indices

def test_ukulele():
    tested_tablature = [0, 2, 3, 2]
    target_key_indices = [46, 41, 46, 50]
    assert ukulele().to_keyboard(tested_tablature) == target_key_indices

def test_bass():
    tested_tablature = [None, 7, None, None]
    target_key_indices = [19]
    assert bass().to_keyboard(tested_tablature) == target_key_indices

def test_mandolin():
    tested_tablature = [None, 7, 5, None]
    target_key_indices = [60, 65]
    assert mandolin().to_keyboard(tested_tablature) == target_key_indices

def test_banjo():
    tested_tablature = [8, 7, 5, None, None]
    target_key_indices = [66, 48, 51]
    assert banjo().to_keyboard(tested_tablature) == target_key_indices

def test_open_d_guitar():
    tested_tablature = [5, 5, 5, 3, None, 0]
    target_key_indices = [34, 41, 46, 49, 53]
    open_d_guitar = strings_instrument(['D3', 'A3', 'D4', 'G4', 'A4', 'D5'])
    assert open_d_guitar.to_keyboard(tested_tablature) == target_key_indices

"""
def test_generate_patterns_major_triad_three_frets_on_bass():
    n_reacheable_frets = 3
    generator = ChordPatternsGenerator(bass(), ChordsTypes.MAJOR_TRIAD, n_reacheable_frets)
    tested_patterns = generator.build_valid_patterns()
    valid_patterns = [[0, 2, 2, 1]]  # single valid pattern over 3 frets on a bass
    assert tested_patterns == valid_patterns

def test_generate_patterns_minor_triad_three_frets_on_bass():
    n_reacheable_frets = 3
    generator = ChordPatternsGenerator(bass(), ChordsTypes.MINOR_TRIAD, n_reacheable_frets)
    tested_patterns = generator.build_valid_patterns()
    valid_patterns = [[0, 2, 2, 0]]  # single valid pattern over 3 frets on a bass
    assert tested_patterns == valid_patterns

def test_generate_patterns_major_seventh_three_frets_on_bass():
    n_reacheable_frets = 3
    generator = ChordPatternsGenerator(bass(), ChordsTypes.MAJOR_SEVENTH, n_reacheable_frets)
    tested_patterns = generator.build_valid_patterns()
    valid_patterns = [[0, 2, 1, 1]] # single valid pattern over 3 frets on a bass
    assert tested_patterns == valid_patterns

def test_generate_patterns_minor_seventh_three_frets_on_bass():
    n_reacheable_frets = 3
    generator = ChordPatternsGenerator(bass(), ChordsTypes.MINOR_SEVENTH, n_reacheable_frets)
    tested_patterns = generator.build_valid_patterns()
    valid_patterns = [[0, 2, 0, 0]] # single valid pattern over 3 frets on a bass
    assert tested_patterns == valid_patterns

def test_generate_patterns_seventh_three_frets_on_bass():
    n_reacheable_frets = 3
    generator = ChordPatternsGenerator(bass(), ChordsTypes.SEVENTH, n_reacheable_frets)
    tested_patterns = generator.build_valid_patterns()
    valid_patterns = [[0, 2, 0, 1]] # single valid pattern over 3 frets on a bass
    assert tested_patterns == valid_patterns
"""
