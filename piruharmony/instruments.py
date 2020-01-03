from keyboard import notes_references
from theory import keyboard_to_chord_properties


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
    regular_guitar_tuning = ['E3', 'A3', 'D4', 'G4', 'B4', 'E5']
    return strings_instrument(tuning = regular_guitar_tuning)


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
    regular_bass_tuning = ['E1', 'A1', 'D2', 'G2']
    return strings_instrument(tuning = regular_bass_tuning)


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
    regular_mandolin_tuning = ['G4', 'D5', 'A5', 'E6']
    return strings_instrument(tuning = regular_mandolin_tuning)


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
    regular_banjo_tuning = ['G5', 'D4', 'G4', 'B4', 'D5']
    return strings_instrument(tuning = regular_banjo_tuning)


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
    regular_ukulele_tuning = ['G4', 'C4', 'E4', 'A4']
    return strings_instrument(tuning = regular_ukulele_tuning)


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
        The tuning contains the name of notes corresponding to
        strings. Notes names are given in english notation. Tags in
        the list are ordered as the strings are, that is from left to
        right.

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
    def __init__(self, tuning):
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
