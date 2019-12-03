
from keyboard import notes_references
from theory import keyboard_to_chord_properties

REGULAR_GUITAR_TUNING = ['E3', 'A3', 'D4', 'G4', 'B4', 'E5']
REGULAR_MANDOLIN_TUNING = ['G4', 'D5', 'A5', 'E6']
REGULAR_UKULELE_TUNING = ['G4', 'C4', 'E4', 'A4']
REGULAR_BANJO_TUNING = ['G5', 'D4', 'G4', 'B4', 'D5']
REGULAR_BASS_TUNING = ['E1', 'A1', 'D2', 'G2']

def guitar():
    """
    Returns a StringsInstrument tuned as an guitar.

    Parameters
    ----------
    None

    Returns
    -------
    out : StringsInstrument
        An instance of class StringsInstrument tuned as a regular
        guitar.

    See Also
    --------
    ukulele : Returns a StringsInstrument tuned as a ukulele
    bass : Returns a StringsInstrument tuned as a bass
    mandolin : Returns a StringsInstrument tuned as a mandolin
    banjo : Returns a StringsInstrument tuned as a banjo

    Examples
    --------
    >>> my_guitar = guitar()
    >>> my_guitar.count_strings()
    6
    >>> i_frets = [None, 3, 2, 0, 1, 0]
    >>> my_guitar.to_keyboard(i_frets)
    [None, 39, 43, 46, 51, 55]
    """
    return strings_instrument(tuning = REGULAR_GUITAR_TUNING)


def bass():
    """
    Returns a StringsInstrument tuned as a bass.

    Parameters
    ----------
    None

    Returns
    -------
    out : StringsInstrument
        An instance of class StringsInstrument tuned as a regular
        bass guitar.

    See Also
    --------
    ukulele : Returns a StringsInstrument tuned as a ukulele
    guitar : Returns a StringsInstrument tuned as a guitar
    mandolin : Returns a StringsInstrument tuned as a mandolin
    banjo : Returns a StringsInstrument tuned as a banjo

    Examples
    --------
    >>> my_bass = bass()
    >>> my_bass.count_strings()
    4
    >>> my_bass.to_keyboard([None, 5, None, None])
    [None, 17, None, None]
    """
    return strings_instrument(tuning = REGULAR_BASS_TUNING)


def mandolin():
    """
    Returns a StringsInstrument tuned as a mandolin.

    Parameters
    ----------
    None

    Returns
    -------
    out : StringsInstrument
        An instance of class StringsInstrument tuned as a regular
        mandolin (superimposed fourths).

    See Also
    --------
    ukulele : Returns a StringsInstrument tuned as a ukulele
    guitar : Returns a StringsInstrument tuned as a guitar
    bass : Returns a StringsInstrument tuned as a bass
    banjo : Returns a StringsInstrument tuned as a banjo

    Examples
    --------
    >>> my_mandolin = mandolin()
    >>> my_mandolin.count_strings()
    4
    >>> my_mandolin.to_keyboard([None, 5, 3, None])
    [None, 58, 63, None]
    """
    return strings_instrument(tuning = REGULAR_MANDOLIN_TUNING)


def banjo():
    """
    Returns a StringsInstrument tuned as a banjo.

    Parameters
    ----------
    None

    Returns
    -------
    out : StringsInstrument
        An instance of class StringsInstrument tuned as a regular
        banjo (reversed open G).

    See Also
    --------
    ukulele : Returns a StringsInstrument tuned as a ukulele
    guitar : Returns a StringsInstrument tuned as a guitar
    bass : Returns a StringsInstrument tuned as a bass
    mandolin : Returns a StringsInstrument tuned as a mandolin

    Examples
    --------
    >>> my_banjo = banjo()
    >>> my_banjo.count_strings()
    5
    >>> my_banjo.to_keyboard([5, 5, 5, None, 3])
    [63, 46, 51, None, 56]
    """
    return strings_instrument(tuning = REGULAR_BANJO_TUNING)


def ukulele():
    """
    Returns a StringsInstrument tuned as an ukulele.

    Parameters
    ----------
    None

    Returns
    -------
    out : StringsInstrument
        An instance of class StringsInstrument tuned as a regular
        ukulele (reversed open Am).

    See Also
    --------
    guitar : Returns a StringsInstrument tuned as a guitar
    bass : Returns a StringsInstrument tuned as a bass
    mandolin : Returns a StringsInstrument tuned as a mandolin
    banjo : Returns a StringsInstrument tuned as a banjo

    Examples
    --------
    >>> my_ukulele = ukulele()
    >>> my_ukulele.count_strings()
    4
    >>> i_frets = [2] * my_ukulele.count_strings()
    >>> my_ukulele.to_keyboard(i_frets)
    [48, 41, 45, 50]
    """
    return strings_instrument(tuning = REGULAR_UKULELE_TUNING)


def strings_instrument(tuning):
    """
    Returns a StringsInstrument with custom tuning.

    Parameters
    ----------
    None

    Returns
    -------
    out : StringsInstrument
        An instance of class StringsInstrument with user defined
        tuning.

    See Also
    --------
    ukulele : Returns a StringsInstrument tuned as a ukulele
    bass : Returns a StringsInstrument tuned as a bass
    mandolin : Returns a StringsInstrument tuned as a mandolin
    banjo : Returns a StringsInstrument tuned as a banjo
    guitar : Returns a StringsInstrument tuned as a guitar

    Examples
    --------
    >>> my_metal_guitar = strings_instrument(tuning = ['D3', 'A3', 'D4', 'G4', 'B4', 'E5'])
    >>> my_metal_guitar.count_strings()
    6
    >>> my_metal_guitar.to_keyboard([3, 3, 3, None, 0, 0])
    [32, 39, 44, None, 50, 55]
    """
    return StringsInstrument(tuning)


class StringsInstrument:
    """
    A class that describes strings instruments.

    A properties class, used to describe strings instruments with any
    tuning and to transform tablatures into notes.

    Parameters
    ----------
    tuning : list of two to three characters, optional.
        Overrides the default tuning. The tuning contains the name
        of notes corresponding to strings. Notes names are given in
        english notation. Tags in the list are ordered as the strings
        are, that is from left to right.

    Examples
    --------

    Build an open-D guitar (DADGAD):
    >>> open_d_guitar = StringsInstrument(['D3', 'A3', 'D4', 'G4', 'A4', 'D5'])

    Count strings
    >>> open_d_guitar.count_strings()
    6

    Translate chords to piano keys ids
    >>> open_d_guitar.to_keyboard([2, 2, 2, None, None, None])
    [31, 38, 43, None, None, None]
    >>> open_d_guitar.to_keyboard([2, 2, 2, 0, None, None])
    [31, 38, 43, 46, None, None]
    """
    def __init__(self, tuning = REGULAR_GUITAR_TUNING):
        """ Constructor of class StringsIntrument's instances """
        self._tuning = tuning

    def _single_string_to_keyboard(self, i_string, i_fret):
        """ Returns piano's key id corresponding to (i_string, i_fret) """
        return notes_references[self._tuning[i_string]] + i_fret if i_fret != None else None

    def count_strings(self):
        """ Returns instrument's number of strings """
        return len(self._tuning)

    def to_keyboard(self, i_frets):
        """ Returns piano's keys ids corresponding to i_frets """
        i_strings = range(self.count_strings())
        return list(filter(None, [self._single_string_to_keyboard(i_string, i_fret) for (i_string, i_fret) in zip(i_strings, i_frets)]))

    def to_chord_properties(self, i_frets):
        """ Returns most likely ChordHarmonicProperties corresponding to i_frets """
        i_notes_on_keyboard = self.to_keyboard(i_frets)
        return keyboard_to_chord_properties(i_notes_on_keyboard)




from itertools import product
from theory import keyboard_to_chord_properties

class ChordPatternsGenerator:
    """
    """
    def __init__(self, strings_instrument, chord_type, n_reacheable_frets):
        self._instrument = strings_instrument
        self._chord_type = chord_type
        self._n_reacheable_frets = n_reacheable_frets

    def _frets_values(self):
        """  """
        mute_fret_value = None
        return [mute_fret_value] + list(range(self._n_reacheable_frets))

    def _all_patterns(self):
        """  """
        return list(product(*[self._frets_values()] * self._instrument.count_strings()))

    def _compliant_patterns(self):
        min_notes_in_chord = 3
        max_mute_frets = self._instrument.count_strings() - min_notes_in_chord
        return list(filter(lambda pattern: pattern.count(None) < max_mute_frets, self._all_patterns()))

    def _compliant_keyboard_notes(self):
        return [self._instrument.to_keyboard(pattern) for pattern in self._compliant_patterns()]

    def _compliant_chords_properties(self):
        return [keyboard_to_chord_properties(i_notes) for i_notes in self._compliant_keyboard_notes()]

    def _compliant_patterns_zip_properties(self):
        return zip(self._compliant_patterns(), self._compliant_chords_properties())

    def _filtered_unknonwn_properties(self):
        return filter(lambda pattern_properties : pattern_properties[1] != None, self._compliant_patterns_zip_properties())

    def _filtered_non_empty_enrichments(self):
        return filter(lambda pattern_properties : pattern_properties[1].enrichments() == [], self._filtered_unknonwn_properties())

    def _filtered_valid_base_type(self):
        return filter(lambda pattern_properties : pattern_properties[1].base_type() == self._chord_type, self._filtered_non_empty_enrichments())

    def build_valid_patterns(self):
        return [list(pattern_properties[0]) for pattern_properties in self._filtered_valid_base_type()]
