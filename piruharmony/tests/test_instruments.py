import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from instruments import guitar, ukulele, bass, mandolin, banjo, strings_instrument


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
