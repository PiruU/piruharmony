from keyboard import notes_references
from enum import Enum
from itertools import product, chain
from functools import reduce
from operator import add


DEFAULT_NOTE_TAG = 'A4'
VALID_TONES = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
VALID_ALTERATIONS = ['#', '', 'b']


def note(note_name = DEFAULT_NOTE_TAG):
    """
    Returns an instance of class Note.

    Parameters
    ----------
    note_name : list of two to three characters, optional.
        Overrides the default note name. The name of the note is
        given in standard english notation. The list concatenates the
        tone, alteration and octave.

    Returns
    -------
    out : Note
        The instance of class Note corresponding to note_name.

    See Also
    --------
    notes : Returns a list of instance of class Note.

    Examples
    --------
    >>> my_note = note() # default Note is natural 'A' (440Hz)
    >>> my_note.name()
    'A4'
    >>> my_note = note('G#4')
    >>> my_note.octave()
    '4'
    """
    return Note(note_name)


def notes(notes_names):
    """
    Returns a list containing instances of class Note.

    Parameters
    ----------
    notes_names : list of list of two or three characters.
        The name of the notes are given in english notation. The list
        concatenates the tone, alteration and octave.

    Return
    ------
    out : list containing instances of class Note.
        The instances of class Note corresponding to each element of
        list notes_names.

    See also
    --------
    note : Returns a instance of class Note from its english notation.

    Examples
    --------
    >>> my_notes = notes(['C3', 'E3', 'D2', 'F2'])
    >>> [n.name() for n in my_notes]
    ['C3', 'E3', 'D2', 'F2']
    """
    return [note(note_name) for note_name in notes_names]


def sorted_notes(notes_names):
    """
    Returns list of Note instance sorted by 'height'

    Parameters
    ----------
    notes_names : list of list of two or three characters.
        The name of the notes are given in english notation. The list
        concatenates the tone, alteration and octave.

    Return
    ------
    out : list containing instances of class Note.
        The instances of class Note corresponding to each element of
        list notes_names.

    Examples
    --------
    >>> my_notes = sorted_notes(['C3', 'E3', 'D2', 'F2'])
    >>> [n.name() for n in my_notes]
    ['D2', 'F2', 'C3', 'E3']
    """
    return sorted(notes(notes_names), key = lambda note: note.keyboard_index())


def removed_tonality_duplicates(notes_names):
    """
    Returns list of Note and keeps notes with first tonalities
    occurences

    Parameters
    ----------
    notes_names : list of list of two or three characters.
        The name of the notes are given in english notation. The list
        concatenates the tone, alteration and octave.

    Return
    ------
    out : list containing instances of class Note.
        The instances of class Note corresponding to each element of
        list notes_names.

    Example
    -------
    >>> notes_names = ['A5', 'C3', 'E3', 'G3', 'C4', 'E4', 'G4']
    >>> unique_notes = removed_tonality_duplicates(notes_names)
    >>> [my_note.name() for my_note in unique_notes]
    ['A5', 'C3', 'E3', 'G3']
    """
    notes_list, no_duped_notes = notes(notes_names), []
    for my_note in notes_list:
        if my_note.tonality() not in [no_duped_note.tonality() for no_duped_note in no_duped_notes]:
            no_duped_notes.append(my_note)
    return no_duped_notes


def cleared_notes(notes_names):
    """
    Returns list of Note instance sorted by 'height' and removes
    highest duplicates tonalities

    Parameters
    ----------
    notes_names : list of list of two or three characters.
        The name of the notes are given in english notation. The list
        concatenates the tone, alteration and octave.

    Return
    ------
    out : list containing instances of class Note.
        The instances of class Note corresponding to each element of
        list notes_names.

    Examples
    --------
    >>> notes_names = ['A5', 'C3', 'E3', 'G3', 'C4', 'E4', 'G4']
    >>> notes_cleared = cleared_notes(notes_names)
    >>> [my_note.name() for my_note in cleared_notes]
    ['C3', 'E3', 'G3', 'A5']
    """
    sorted_notes_names = [note.name() for note in sorted_notes(notes_names)]
    return removed_tonality_duplicates(sorted_notes_names)


def lowest_note(notes_names):
    """
    Returns the lowest note among a list of notes names.

    Parameters
    ----------
    notes_names : list of list of two or three characters.
        The name of the notes are given in english notation. The list
        concatenates the tone, alteration and octave.

    Return
    ------
    out : instance of class Note.
        The resulting instance of class Note is the lowest one (the
        one with lowest frequency).

    See also
    --------
    notes : Returns a list of instance of class Note.

    Examples
    --------
    >>> lowest_note(['Eb2', 'Bb4', 'G3', 'C1']).name()
    'C1'
    """
    return sorted_notes(notes_names)[0]


class Note:
    """
    A class that describes notes.

    A properties class, used to encapsulate characteristics and to
    connect symbols with indices of piano's keys.

    Parameters
    ----------
    note_name : list of two to three characters, optional.
        Overrides the default note name. The name of the note is given
        in standard english notation. The list concatenates the tone,
        alteration and octave.

    Examples
    --------

    Build an F sharp note (4th octave on piano):
    >>> my_note = Note('F#4')

    Return Note properties
    >>> my_note.tone()
    F
    >>> my_note.alteration()
    #
    >>> my_note.octave()
    4
    >>> my_note.name()
    'F#4'

    Compare notes
    >>> my_note == Note('G5')
    False
    >>> print(my_note == Note('F#4'))
    True
    """
    def __init__(self, note_name):
        """ Builds a Note instance. """
        self._name = note_name

    def __eq__(self, other):
        """ Comparison operator overloading. """
        return self.octave() == other.octave() and self.tone() == other.tone() and self.alteration() == other.alteration()

    def octave(self):
        """ Returns the octave of which the note belongs. """
        i_octave = -1
        return self._name[i_octave]

    def tone(self):
        """ Returns the tone of the note. """
        i_tone = 0
        return self._name[i_tone]

    def alteration(self):
        """ Returns the alteration; sharp, flat, none. """
        if len(self._name) == 3:
            i_alteration = 1
            return self._name[i_alteration]
        else:
            return ''

    def tonality(self):
        """ Returns the note tonality """
        return self.tone() + self.alteration()

    def name(self):
        """ Returns the name of the note in english notation. """
        return self._name

    def keyboard_index(self):
        """ Returns the piano's key index corresponding to the note. """
        return notes_references[self.name()]


def transposed_note(base_note, transposition_interval, orientation = 'increase'):
    """
    Returns the transposed of a note.

    Parameters
    ----------
    base_note : instance of Note.
        The note of which the transposed is requested.
    transposition_interval : instance of Interval.
        The interval that defines the transpose.
    orientation : list of chars.
        Overrides the default 'increase' orientation. Describes the
        transpose orientation.

    Returns
    -------
    out : instance of Note
        The instance of class Note resulting from the transpose of
        base_note.

    See Also
    --------
    NoteTranspose : a class that describes a note transpose.

    Examples
    --------
    >>> base_note = note('C3')
    >>> major_third = IntervalsTypes.MAJOR_THIRD.value
    >>> transposed_note(base_note, major_third).name()
    'E3'
    >>> transposed_note(base_note, major_third, orientation = 'decrease').name()
    'Ab2'
    """
    return NoteTranspose(base_note, transposition_interval, orientation).transposed()


class NoteTranspose:
    """
    A class that describes a note transpose.

    A class the permits the tranpose of a given note.

    Parameters
    ----------
    base_note : instance of Note.
        The note of which the transposed is requested.
    transposition_interval : instance of Interval.
        The interval that defines the transpose.
    orientation : list of chars.
        Overrides the default 'increase' orientation. Describes the
        transpose orientation.

    See Also
    --------
    transposed_note : returns the transposed of a note.

    Examples
    --------

    Build increasing sixth-transposed of C3
    >>> my_note = Note('C3')
    >>> my_interval = IntervalsTypes.SIXTH.value
    >>> my_transpose = NoteTranspose(my_note, my_interval, orientation = 'increase')
    >>> my_transpose.transposed().name()
    >>> 'A3'

    Build decreasing minor third-transposed of C3
    >>> my_note = Note('C3')
    >>> my_interval = IntervalsTypes.MINOR_THIRD.value
    >>> my_transpose = NoteTranspose(my_note, my_interval, orientation = 'decrease')
    >>> my_transpose.transposed().name()
    >>> 'A2'
    """
    def __init__(self, base_note, transposition_interval, orientation = 'increase'):
        """ Builds an instance of NoteTranspose """
        if orientation == 'increase':
            self._transposition = TransposeToUpperNote(base_note, transposition_interval)
        else:
            self._transposition = TransposeToLowerNote(base_note, transposition_interval)

    def tone(self):
        """ Returns the tone of the transposed note """
        return VALID_TONES[self._transposition.i_tone()]

    def transposed(self):
        """ Returns the transposed of input root_note """
        possible_notes_names = _keyboard_to_possible_notes_names(self._transposition.i_keyboard())
        return [note(name) for name in possible_notes_names if self.tone() in name][0]


class TransposeToUpperNote:
    """
    A class that describes an increasing note transpose.

    A class the permits the tranpose to a given upper note.

    Parameters
    ----------
    base_note : instance of Note.
        The note of which the transposed is requested.
    transposition_interval : instance of Interval.
        The interval that defines the transpose.

    See Also
    --------
    transposed_note : returns the transposed of a note.

    Examples
    --------
    Build increasing fifth-transposed of C3
    >>> my_note = Note('C3')
    >>> my_interval = IntervalsTypes.FIFTH.value
    >>> my_transpose = TransposeToUpperNote(my_note, my_interval)
    >>> my_transpose.transposed().name()
    >>> 'G3'
    """
    def __init__(self, base_note, transposition_interval):
        """ Builds an instance of TransposeToUpperNote """
        self._note     = base_note
        self._interval = transposition_interval

    def i_keyboard(self):
        """ Returns the keyboard note index of the transposed note """
        return self._note.keyboard_index() + self._interval.count_semitones()

    def i_tone(self):
        """ Returns tone index of the transposed note as refered to in VALID_TONES """
        n_tones_in_scale = 7
        n_tones_in_transpose = self._interval.tones_range()
        return (VALID_TONES.index(self._note.tone()) + n_tones_in_transpose) % n_tones_in_scale


class TransposeToLowerNote:
    """
    A class that describes a decreasing note transpose.

    A class the permits the tranpose to a given lower note.

    Parameters
    ----------
    base_note : instance of Note.
        The note of which the transposed is requested.
    transposition_interval : instance of Interval.
        The interval that defines the transpose.

    See Also
    --------
    transposed_note : returns the transposed of a note.

    Examples
    --------
    Build decreasing fourth-transposed of C3
    >>> my_note = Note('C3')
    >>> my_interval = IntervalsTypes.FOURTH.value
    >>> my_transpose = TransposeToLowerNote(my_note, my_interval)
    >>> my_transpose.transposed().name()
    >>> 'G2'
    """
    def __init__(self, base_note, transposition_interval):
        """ Builds an instance of TransposeToLowerNote """
        self._note     = base_note
        self._interval = transposition_interval

    def i_keyboard(self):
        """ Returns the keyboard note index of the transposed note """
        return self._note.keyboard_index() - self._interval.count_semitones()

    def i_tone(self):
        """ Returns tone index of the transposed note as refered to in VALID_TONES """
        n_tones_in_scale = 7
        n_tones_in_transpose = self._interval.tones_range()
        return (VALID_TONES.index(self._note.tone()) + n_tones_in_scale - n_tones_in_transpose) % n_tones_in_scale


def interval(root_note_name, slave_note_name):
    """
    Returns an instance of class Interval.

    Parameters
    ----------
    root_note_name : list of two to three characters, optional.
        Reference (bass) note of the interval. root_note_name is given
        in english notation.
    slave_note_name : list of two to three characters, optional.
        Slave (high) note of the interval. slave_note_name is given in
        english notation.

    Returns
    -------
    out : Interval
        The instance of class Interval corresponding to the input
        parameters.

    See Also
    --------
    intervals : Returns a list of instance of class Interval.

    Examples
    --------
    >>> my_interval = interval('C3', 'F#3')
    >>> my_interval.count_semitones()
    6
    >>> my_interval.tones_range()
    3
    """
    n_semitones = _count_semitones(root_note_name, slave_note_name)
    tones_range = _get_tones_range(root_note_name, slave_note_name)
    return Interval(n_semitones, tones_range)


def intervals(notes_names, return_flattened = False):
    """
    Returns a list containing instances of class Interval.

    Parameters
    ----------
    notes_names : list of list of two or three characters.
        The name of the notes are given in english notation. The list
        concatenates the tone, alteration and octave.

    Return
    ------
    out : list containing instances of class Note.
        The instances of class Interval describing intervals between
        the lowest note corresponding to notes_names and all others.

    See also
    --------
    interval : Returns a instance of class Interval.

    Examples
    --------
    >>> my_intervals = intervals(['C3', 'E3', 'G3', 'Bb3'])
    >>> [i.count_semitones() for i in my_intervals]
    [4, 7, 10]  # ['C3-E3', 'C3-G3', 'C3-Bb3']
    """
    bass_note = lowest_note(notes_names)
    return [interval(bass_note.name(), note.name()) for note in sorted_notes(notes_names) if note != bass_note]


def _flattened_intervals(these_intervals):
    """
    Returns a list of Interval within a single octave.

    Parameters
    ----------
    these_intervals : list of Interval instances.
        List of instances of class Interval to be processed.

    Return
    ------
    out : list containing instances of class Note.
        The instances of class Interval flattened, that is contained
        within a singla octave.

    See also
    --------
    interval : Returns a instance of class Interval.

    Examples
    --------
    >>> my_intervals = intervals(['C2', 'E3', 'G5', 'Bb6'])
    >>> [interval.tones_range() for interval in my_intervals]
    [2, 4, 6]
    >>> [interval.count_semitones() for interval in my_intervals]
    [16, 43, 58]
    >>> my_flattened_intervals = _flattened_intervals(my_intervals)
    >>> [interval.tones_range() for interval in my_flattened_intervals]
    [2, 4, 6]
    >>> [interval.count_semitones() for interval in my_flattened_intervals]
    [4, 7, 10]
    """
    return [interval.flattened() for interval in these_intervals]


def cleared_intervals(notes_names):
    """
    Returns a list of Interval cleaned and sorted.

    Parameters
    ----------
    notes_names : list of list of two or three characters.
        The name of the notes are given in english notation. The list
        concatenates the tone, alteration and octave.

    Return
    ------
    out : list containing instances of class Note.
        A list of Interval instances where all octave dupplicates
        have been cleared and where intervals have been sorted by
        their ranges.

    See also
    --------
    interval : Returns a instance of class Interval.

    Examples
    --------
    >>> my_notes = ['E5', 'G3', 'C2', 'E2', 'G2', 'Bb4', 'C4']
    >>> my_intervals = intervals(my_notes)
    >>> [intervals.count_semitones() for intervals in my_intervals]
    [4, 7, 19, 24, 34, 40]
    >>> my_clear_intervals = cleared_intervals(my_notes)
    >>> [intervals.count_semitones() for intervals in my_clear_intervals]
    [4, 7, 10]
    """
    clear_intervals = intervals([note.name() for note in cleared_notes(notes_names)])
    return sorted(_flattened_intervals(clear_intervals))


def _count_semitones(root_note_name, slave_note_name):
    """
    Returns the number of semitones between to notes.

    Parameters
    ----------
    root_note_name : list of two to three characters, optional.
        Reference (bass) note of the interval. root_note_name is given
        in english notation.
    slave_note_name : list of two to three characters, optional.
        Slave (high) note of the interval. slave_note_name is given in
        english notation.

    Returns
    -------
    out : int
        The number of semitones between notes with names given as
        input.

    See Also
    --------
    _get_tones_range : Returns the number of tones between two notes.

    Examples
    --------
    >>> _count_semitones('C#3', 'A3')
    8
    """
    root_note, slave_note = sorted_notes([root_note_name, slave_note_name])
    return slave_note.keyboard_index() - root_note.keyboard_index()


def _get_tones_range(root_note_name, slave_note_name):
    """
    Returns the number of tones between two notes.

    Parameters
    ----------
    root_note_name : list of two to three characters, optional.
        Reference (bass) note of the interval. root_note_name is given
        in english notation.
    slave_note_name : list of two to three characters, optional.
        Slave (high) note of the interval. slave_note_name is given in
        english notation.

    Returns
    -------
    out : int
        The difference of tones between notes with names given as
        input.

    See Also
    --------
    _count_semitones : Returns the number of semitones between two
        notes.

    Examples
    --------
    >>> _get_tones_range('C#3', 'A3')
    5
    >>> _get_tones_range('C#3', 'A5')
    5
    >>> _get_tones_range('C#3', 'F#5')
    3
    >>> _get_tones_range('C#3', 'F#2')
    4
    """
    n_notes_in_scale = 7
    root_note, slave_note = sorted_notes([root_note_name, slave_note_name])
    delta_tones = VALID_TONES.index(slave_note.tone()) - VALID_TONES.index(root_note.tone())
    return delta_tones if delta_tones > 0 else n_notes_in_scale + delta_tones


DEFAULT_N_SEMITONES = 4
DEFAULT_TONES_RANGE = 2
class Interval:
    """
    A class that describes an interval.

    A properties class, used to encapsulate characteristics and to
    perform operations on intervals.

    Parameters
    ----------
    n_semitones : positive integer, optional
        Overrides the default n_semitones value. Number of semitones
        composing the interval.
    tones_range : positive integer, optional.
        Overrides the default tones_range value. Number of tones
        between interval's notes This property corresponds to a range
        between notes in VALID_TONES.

    Examples
    --------

    Build an octave aumented major third interval:
    >>> my_interval = Interval(n_semitones = 16, tones_range = 2)

    Return interval properties
    >>> my_interval.count_semitones()
    16
    >>> my_interval.tones_range()
    2

    Flatten to regular major third interval
    >>> my_flattened_interval = my_interval.flattened()
    >>> my_flattened_interval.count_semitones()
    4
    >>> my_flattened_interval.tones_range()
    2

    Compare intervals
    >>> my_interval == IntervalsTypes.MAJOR_THIRD.value
    False
    >>> interval('C4', 'E5') == my_interval
    True
    >>> my_flattened_interval == IntervalsTypes.MAJOR_THIRD.value
    True
    """
    def __init__(self, n_semitones = DEFAULT_N_SEMITONES, tones_range = DEFAULT_TONES_RANGE):
        """ Builds an instance of class Interval """
        self._n_semitones = n_semitones
        self._tones_range = tones_range

    def __eq__(self, other):
        """ Comparison operator overloading. """
        return self.count_semitones() == other.count_semitones() and self.tones_range() == other.tones_range()

    def __lt__(self, other):
        """ Lower than operator overloading (makes this class sortable) """
        if self.count_semitones() < other.count_semitones():
            return True
        elif self.count_semitones() == other.count_semitones():
            return self.tones_range() < other.tones_range()
        else:
            return False

    def has_type(self, interval_type):
        return self.flattened() == interval_type.value

    def count_semitones(self):
        """ Returns the number of semitone composing the interval """
        return self._n_semitones

    def tones_range(self):
        """ Returns the interval's tones range """
        return self._tones_range

    def flattened(self):
        """ Return an Interval with cancelled octaves """
        n_semitones_in_scale = 12
        return Interval(self.count_semitones() % n_semitones_in_scale, self.tones_range())

    def type(self):
        """ Returns interval type as defined in enum IntervalsTypes """
        interval_type = IntervalsTypes.UNKNOWN
        for tested_interval in IntervalsTypes:
            if self.has_type(tested_interval):
                interval_type = tested_interval
        return interval_type


class IntervalsTypes(Enum):
    """
    Gathers all regular intervals types existing withing an octave
    """
    DIMINISHED_NINTH   = Interval(n_semitones =  1, tones_range = 1)
    NINTH              = Interval(n_semitones =  2, tones_range = 1)
    AUGMENTED_NINTH    = Interval(n_semitones =  3, tones_range = 1)
    DIMINISHED_THIRD   = Interval(n_semitones =  2, tones_range = 2)
    MINOR_THIRD        = Interval(n_semitones =  3, tones_range = 2)
    MAJOR_THIRD        = Interval(n_semitones =  4, tones_range = 2)
    AUGMENTED_THIRD    = Interval(n_semitones =  5, tones_range = 2)
    DIMINISHED_FOURTH  = Interval(n_semitones =  4, tones_range = 3)
    FOURTH             = Interval(n_semitones =  5, tones_range = 3)
    AUGMENTED_FOURTH   = Interval(n_semitones =  6, tones_range = 3)
    DIMINISHED_FIFTH   = Interval(n_semitones =  6, tones_range = 4)
    FIFTH              = Interval(n_semitones =  7, tones_range = 4)
    AUGMENTED_FIFTH    = Interval(n_semitones =  8, tones_range = 4)
    DIMINISHED_SIXTH   = Interval(n_semitones =  8, tones_range = 5)
    SIXTH              = Interval(n_semitones =  9, tones_range = 5)
    AUGMENTED_SIXTH    = Interval(n_semitones = 10, tones_range = 5)
    DIMINISHED_SEVENTH = Interval(n_semitones =  9, tones_range = 6)
    MINOR_SEVENTH      = Interval(n_semitones = 10, tones_range = 6)
    MAJOR_SEVENTH      = Interval(n_semitones = 11, tones_range = 6)
    DIMINISHED_OCTAVE  = Interval(n_semitones = 11, tones_range = 7)
    UNKNOWN            = Interval(n_semitones = -1, tones_range = -1)


def chord(notes_names):
    """
    Returns an instance of class Chord.

    Parameters
    ----------
    notes_names : list of two or three characters.
        Name of notes composing the chord. Tags in notes_names are
        given in english notation.

    Returns
    -------
    out : Chord
        The instance of class Chord corresponding to the input
        parameters.

    See Also
    --------
    Chord : a class that describes a chord.

    Examples
    >>> my_chord = chord(['G3', 'B5', 'D4', 'F4'])
    >>> my_chord.has_type(ChordsTypes.SEVENTH)
    True
    >>> my_chord.has_type(ChordsTypes.DIMINISHED_TRIAD)
    False
    """
    intervals_list = cleared_intervals(notes_names)
    bass_note = lowest_note(notes_names)
    return Chord(root_note = bass_note, chord_intervals = intervals_list)


class Chord:
    """
    A class that describes a chord.

    A properties class, used to encapsulate characteristics of
    chords.

    Parameters
    ----------
    root_note : Note
        lowest note of the chord, bass note.
    chord_intervals : list of Interval
        intervals superimposed over the root note so as to build the
        chord.

    Examples
    --------

    Build a major triad chord with root note C3
    >>> my_root_note = note('C3')
    >>> my_intervals = [IntervalsTypes.MAJOR_THIRD.value, IntervalsTypes.FIFTH.value]
    >>> my_chord = Chord(root_note = my_root_note, chord_intervals = my_intervals)

    Compare chords intervals
    >>> my_chord.has_type(ChordsTypes.MAJOR_TRIAD)
    True
    >>> my_chord.has_type(ChordsTypes.MINOR_TRIAD)
    False
    """
    def __init__(self, root_note, chord_intervals):
        """ Builds an instance of class Chord """
        self._root_note = root_note
        self._intervals = chord_intervals

    def intervals(self):
        """ Returns a list containing the chord's intervals """
        return self._intervals

    def root_note(self):
        """ Returns the chord's root (bass) note """
        return self._root_note

    def contains_type(self, chord_type):
        """ Returns true if chord_type is a subset of self._intervals """
        return all(interval.value in self._intervals for interval in chord_type.value)

    def notes(self):
        """  """
        chord_notes = [self._root_note]
        for interval in self._intervals:
            chord_notes.append(transposed_note(self._root_note, interval))
        return chord_notes


class ChordsTypes(Enum):
    """
    Gathers all regular chords types existing in major/minor scales
    """
    MAJOR_TRIAD               = [IntervalsTypes.MAJOR_THIRD, IntervalsTypes.FIFTH]
    MINOR_TRIAD               = [IntervalsTypes.MINOR_THIRD, IntervalsTypes.FIFTH]
    AUGMENTED_TRIAD           = [IntervalsTypes.MAJOR_THIRD, IntervalsTypes.AUGMENTED_FIFTH]
    DIMINISHED_TRIAD          = [IntervalsTypes.MINOR_THIRD, IntervalsTypes.DIMINISHED_FIFTH]
    SEVENTH                   = [IntervalsTypes.MAJOR_THIRD, IntervalsTypes.FIFTH, IntervalsTypes.MINOR_SEVENTH]
    MAJOR_SEVENTH             = [IntervalsTypes.MAJOR_THIRD, IntervalsTypes.FIFTH, IntervalsTypes.MAJOR_SEVENTH]
    MINOR_SEVENTH             = [IntervalsTypes.MINOR_THIRD, IntervalsTypes.FIFTH, IntervalsTypes.MINOR_SEVENTH]
    MINOR_MAJOR_SEVENTH       = [IntervalsTypes.MINOR_THIRD, IntervalsTypes.FIFTH, IntervalsTypes.MAJOR_SEVENTH]
    SEVENTH_TRIAD             = [IntervalsTypes.MAJOR_THIRD, IntervalsTypes.MINOR_SEVENTH]
    MAJOR_SEVENTH_TRIAD       = [IntervalsTypes.MAJOR_THIRD, IntervalsTypes.MAJOR_SEVENTH]
    MINOR_SEVENTH_TRIAD       = [IntervalsTypes.MINOR_THIRD, IntervalsTypes.MINOR_SEVENTH]
    MINOR_MAJOR_SEVENTH_TRIAD = [IntervalsTypes.MINOR_THIRD, IntervalsTypes.MAJOR_SEVENTH]
    HALF_DIMINISHED_SEVENTH   = [IntervalsTypes.MINOR_THIRD, IntervalsTypes.DIMINISHED_FIFTH, IntervalsTypes.MINOR_SEVENTH]
    AUGMENTED_MAJOR_SEVENTH   = [IntervalsTypes.MAJOR_THIRD, IntervalsTypes.AUGMENTED_FIFTH, IntervalsTypes.MAJOR_SEVENTH]
    DIMINISHED_SEVENTH        = [IntervalsTypes.MINOR_THIRD, IntervalsTypes.DIMINISHED_FIFTH, IntervalsTypes.DIMINISHED_SEVENTH]
    POWER_CHORD               = [IntervalsTypes.FIFTH]
    MAJOR_THIRD_ALONE         = [IntervalsTypes.MAJOR_THIRD]
    MINOR_THIRD_ALONE         = [IntervalsTypes.MINOR_THIRD]
    UNKNOWN                   = []

def chord_explorer(notes_names):
    """
    Returns an instance of class ChordExplorer.

    Parameters
    ----------
    notes_names : list of two or three characters.
        Name of notes composing the chord. Tags in notes_names are
        given in english notation.

    Returns
    -------
    out : ChordExplorer
        The instance of class ChordExplorer corresponding to the
        input parameters.

    See Also
    --------
    ChordExplorer : a class used so as to explore chords properties.

    Examples
    --------
    >>> explorer = chord_explorer(['C3', 'Eb3', 'G3', 'B3'])
    >>> for harmonic_properties in explorer.possible_harmonic_properties():
    ...     print('Tonality    :', harmonic_properties.tonality())
    ...     print('Base type   :', harmonic_properties.base_type().name)
    ...     print('Enrichments :', [e.name for e in harmonic_properties.enrichments()])
    ...     print('')
    Tonality    : C
    Base type   : MINOR_TRIAD
    Enrichments : ['MAJOR_SEVENTH']

    Tonality    : C
    Base type   : MINOR_MAJOR_SEVENTH
    Enrichments : []

    Tonality    : C
    Base type   : MINOR_MAJOR_SEVENTH_TRIAD
    Enrichments : ['FIFTH']

    Tonality    : C
    Base type   : ROCK_FIFTH
    Enrich      : ['MINOR_THIRD', 'MAJOR_SEVENTH']

    Tonality    : C
    Base type   : UNKNOWN
    Enrichments : ['MINOR_THIRD', 'FIFTH', 'MAJOR_SEVENTH']
    """
    return ChordExplorer(chord(notes_names))


class ChordExplorer:
    """
    A class that can be used so as to explore chords properties.
    Chord inversions are analyzed.

    Parameters
    ----------
    explored_chord : Chord
        chord the properties of which will be analyzed.

    Examples
    --------
    >>> chord_explorer = ChordExplorer(chord(['C3', 'E3', 'G3']))
    >>> ChordsTypes.MAJOR_TRIAD in [p.base_type() for p in chord_explorer.possible_harmonic_properties()]
    True
    >>> chord_explorer = ChordExplorer(chord(['G2', 'C3', 'E3']))
    >>> ChordsTypes.MAJOR_TRIAD in [p.base_type() for p in chord_explorer.possible_harmonic_properties()]
    True
    """
    def __init__(self, explored_chord):
        """  """
        self._chords = [explored_chord] + inversed_chords(explored_chord)

    def possible_harmonic_properties(self):
        """  """
        return list(chain(*[StaticChordExplorer(chord).possible_harmonic_properties() for chord in self._chords]))


class StaticChordExplorer:
    """
    A class that can be used so as to explore chords properties.
    Chord inversions are ignored.

    Parameters
    ----------
    explored_chord : Chord
        chord the properties of which will be analyzed.

    Examples
    --------
    >>> chord_explorer = StaticChordExplorer(chord(['C3', 'E3', 'G3']))
    >>> ChordsTypes.MAJOR_TRIAD in [p.base_type() for p in chord_explorer.possible_harmonic_properties()]
    True
    >>> chord_explorer = StaticChordExplorer(chord(['G2', 'C3', 'E3']))
    >>> ChordsTypes.MAJOR_TRIAD in [p.base_type() for p in chord_explorer.possible_harmonic_properties()]
    False
    """
    def __init__(self, explored_chord):
        """ Builds an instance of ChordExplorer """
        self._chord = explored_chord

    def tonality(self):
        """ Returns the chord's root note tonality """
        return self._chord.root_note().tonality()

    def possible_base_types(self):
        """ Returns chord's all possible base types refered to as in enum ChordsTypes """
        return [type for type in ChordsTypes if self._chord.contains_type(type)]

    def possible_enrichments_lists(self):
        """ Returns chord's all possible listes of enrichments intervals refered to as in enum IntervalsTypes """
        base_types, enrichments = self.possible_base_types(), []
        for base_type in base_types:
            enrichments.append([interval.type() for interval in self._chord.intervals() if interval.type() not in base_type.value])
        return enrichments

    def possible_harmonic_properties(self):
        """ Returns the list of all possible harmonic properties as instances of ChordHarmonicProperties """
        tonality = self.tonality()
        types_zip_enrichments = zip(self.possible_base_types(), self.possible_enrichments_lists())
        return [ChordHarmonicProperties(tonality, type, enrichments) for (type, enrichments) in types_zip_enrichments]


class ChordHarmonicProperties:
    """
    A container class that describes harmonic properties of chords.

    Parameters
    ----------
    tonality : list of one or two chars
        Tonality or root note of the char, not related to an octave.
    base_type : one field among enum ChordsTypes
        Base type of the chord as refered in enum ChordsTypes
    enrichments : List of fields in enum Intervals Types
        Enrichments of the chord, that is intervals that appear in
        the chord bu that cannot be considered as base intervals.
        Valid enrichments are listed in enum IntervalsTypes.

    Examples
    --------

    Build the properties of an F#sus4
    >>> chord_properties = ChordHarmonicProperties('F#', ChordsTypes.MAJOR_TRIAD, [IntervalsTypes.FOURTH])

    Show chord's tonality
    >>> chord_properties.tonality()
    'F#'

    Show chord's base type
    >>> chord_properties.base_type().name
    'MAJOR_TRIAD'

    Show chord's enrichments
    >>> [interval.name for interval in chord_properties.enrichments()]
    ['FOURTH']

    Count the number of enrichments
    >>> chord_properties.count_enrichments()
    1
    """
    def __init__(self, tonality, base_type, enrichments):
        """ Builds and instance of ChordHarmonicProperties """
        self._tonality    = tonality
        self._base_type   = base_type
        self._enrichments = enrichments

    def tonality(self):
        """ Returns the tonality of the chord """
        return self._tonality

    def base_type(self):
        """ Returns chord's base type as refered in ChordsTypes """
        return self._base_type

    def enrichments(self):
        """ Returns the chord's list of enrichments """
        return self._enrichments

    def count_enrichments(self):
        """ Returns the number of enrichments in the chord """
        return len(self._enrichments)

    def __eq__(self, other):
        """ Comparison operator overloading """
        if other != None:
            same_tonality    = self.tonality()    == other.tonality()
            same_base_type   = self.base_type()   == other.base_type()
            same_enrichments = self.enrichments() == other.enrichments()
            return same_tonality and same_base_type and same_enrichments
        else:
            return False


def _keyboard_to_possible_notes_names(i_note):
    """
    Returns all notes names corresponding to a keyboard note index.

    Parameters
    ----------
    i_note : int in [0 - 88]
        note index on keyboard.

    Returns
    -------
    out : List of two or three chars
        The name of the note correponding to i_note. The returned
        name is given in english notation.

    Examples
    --------
    >>> _keyboard_to_possible_notes_names(22)
    ['G2']
    >>> _keyboard_to_possible_notes_names(38)
    ['B3', 'Cb3']
    >>> _keyboard_to_possible_notes_names(43)
    ['E4', 'Fb4']
    """
    return [key for key in notes_references.keys() if notes_references[key] == i_note]


class KeyboardToHarmonicPropertiesTranslator:
    """
    A class that converts notes indices on keyboard into harmonic
    properties.

    Parameters
    ----------
    i_notes_on_keyborad : list of intergers in range(0, 88)
        List of notes indices on kyboard composing a chord.

    Examples
    --------
    >>> translator = KeyboardToHarmonicPropertiesTranslator([27, 31, 34])
    >>> harmonic_properties = translator.possible_harmonic_properties()
    >>> for p in harmonic_properties:
    ...     print('Tonality   :', p.tonality())
    ...     print('Base type  :', p.base_type().name)
    ...     print('Enrichments:', [e.name for e in p.enrichments()])
    ...     print('')
    Tonality   : B#
    Base type  : UNKNOWN
    Enrichments: ['DIMINISHED_FOURTH', 'UNKNOWN']

    Tonality   : B#
    Base type  : UNKNOWN
    Enrichments: ['UNKNOWN', 'UNKNOWN']

    Tonality   : C
    Base type  : MAJOR_TRIAD
    Enrichments: []

    Tonality   : C
    Base type  : ROCK_FIFTH
    Enrichments: ['MAJOR_THIRD']

    Tonality   : C
    Base type  : UNKNOWN
    Enrichments: ['MAJOR_THIRD', 'FIFTH']

    Tonality   : C
    Base type  : ROCK_FIFTH
    Enrichments: ['DIMINISHED_FOURTH']

    Tonality   : C
    Base type  : UNKNOWN
    Enrichments: ['DIMINISHED_FOURTH', 'FIFTH']
    """
    def __init__(self, i_notes_on_keyboard):
        """ Builds an instance of KeyboardToHarmonicPropertiesTranslator """
        self._i_notes = i_notes_on_keyboard

    def possible_notes_names_lists(self):
        """ Returns all possible notes names corresponding to each note index """
        return [_keyboard_to_possible_notes_names(i_note) for i_note in self._i_notes]

    def possible_chords(self):
        """ Returns all possible instances af Chord corresponding to notes indices """
        notes_names_lists = self.possible_notes_names_lists()
        return [chord(notes_names) for notes_names in list(product(*notes_names_lists))]

    def possible_harmonic_properties(self):
        """ Returns all possible ChordHarmonicProperties corresponding to notes indices """
        possible_chords = self.possible_chords()
        return reduce(add, [ChordExplorer(chord).possible_harmonic_properties() for chord in possible_chords])


def has_known_base_type(chord_properties):
    """
    Returns True if chord_properties has a known base type.

    Parameters
    ----------
    chord_properties : ChordHarmonicProperties
        The instance of the above class that will be tested.

    Returns
    -------
    out : bool
        True if chord_properties has a valid base type, False
        otherwise.

    Examples
    --------
    >>> tested_properties = ChordHarmonicProperties('C', ChordsTypes.UNKNOWN, [])
    >>> has_known_base_type(tested_properties)
    False
    >>> tested_properties = ChordHarmonicProperties('C', ChordsTypes.MAJOR_TRIAD, [])
    >>> has_known_base_type(tested_properties)
    True
    """
    return chord_properties.base_type().name != 'UNKNOWN'


class Predicate:
    """
    A class that encapsulates test function and expected return

    Parameters
    ----------
    function : Function reference
        The function that will be evaluated to test the predicate.
        This function must take a single argument and must return a
        boolean.
    expected_return : bool
        Overights True. Expected return of the test function.

    Examples
    --------
    >>> def is_zero(value):
    ...     return value == 0
    >>> predicate = Predicate(is_zero, True)
    >>> predicate.test(1)
    False
    >>> predicate.test(0)
    True
    """
    def __init__(self, function, expected_return = True):
        """ Builds an instance of Predicate """
        self._function = function
        self._return = expected_return

    def test(self, arguments):
        """ Tests the validity of the predicate """
        return self._function(arguments) == self._return


class HarmonicPropertiesFilter:
    """
    A class that filters a list of ChordHarmonicProperties

    Parameters
    ----------
    chords_properties : list of ChordHarmonicProperties
        The list of ChordHarmonicProperties instances that will be
        filtered.

    Examples
    --------
    >>> all_properties = chord_explorer(['C3', 'Eb3', 'G3', 'B3']).possible_harmonic_properties()
    >>> filtered_properties = HarmonicPropertiesFilter(all_properties).add_predicate(Predicate(has_known_base_type)).filtered()
    >>> [p.base_type().name for p in filtered_properties]
    ['MINOR_TRIAD', 'MINOR_MAJOR_SEVENTH', 'MINOR_MAJOR_SEVENTH_TRIAD', 'ROCK_FIFTH'] # no 'UNKONWN' in that list
    """
    def __init__(self, chords_properties):
        """ Builds an instance of HarmonicPropertiesFilter """
        self._chords_properties = chords_properties
        self._predicates = []

    def add_predicate(self, predicate):
        """ Adds a predicate filter that applies to each element of self._chords_properties """
        self._predicates.append(predicate)
        return self

    def filtered(self):
        """ Returns the elements after filtering """
        for predicate in self._predicates:
            self._chords_properties = list(filter(lambda properties: predicate.test(properties), self._chords_properties))
        return self._chords_properties


def count_minimum_enrichments(chords_properties):
    """
    Returns the minimum number of enrichments among a list of
    ChordHarmonicProperties

    Parameters
    ----------
    chords_properties : list of ChordHarmonicProperties
        The list of ChordHarmonicProperties of which the number of
        enrichments of each element will be counted.

    Returns
    -------
    out : int
        The minimum number of enrichments among chords_properties.

    Examples
    --------
    >>> all_properties = chord_explorer(['C3', 'Eb3', 'G3', 'B3']).possible_harmonic_properties()
    >>> count_minimum_enrichments(all_properties)
    0
    """
    return min([properties.count_enrichments() for properties in chords_properties])


def count_enrichments(chord_properties):
    """
    Returns the number of enrichments in a ChordHarmonicProperties

    Parameters
    ----------
    chords_properties : list of ChordHarmonicProperties
        The tested ChordHarmonicProperties instance.

    Returns
    -------
    out : int
        The number of enrichments in chord_properties.

    Examples
    --------
    >>> chord_properties = ChordHarmonicProperties('C', ChordsTypes.MAJOR_TRIAD, [IntervalsTypes.MAJOR_SEVENTH])
    >>> count_enrichments(chord_properties)
    1
    """
    return chord_properties.count_enrichments()


"""
Gathers all intervals that can be recognized as valid enrichments.
For instance, a MAJOR_THIRD is not a valid enrichment.
"""
VALID_ENRICHMENTS = [
IntervalsTypes.DIMINISHED_NINTH , IntervalsTypes.NINTH          , IntervalsTypes.AUGMENTED_NINTH ,
IntervalsTypes.DIMINISHED_FOURTH, IntervalsTypes.FOURTH         , IntervalsTypes.AUGMENTED_FOURTH,
IntervalsTypes.DIMINISHED_FIFTH , IntervalsTypes.AUGMENTED_FIFTH, IntervalsTypes.DIMINISHED_SIXTH,
IntervalsTypes.SIXTH            , IntervalsTypes.AUGMENTED_SIXTH
]


def _is_valid_enrichment(tested_interval):
    """
    Returns True if tested_interval is a valid enrichment

    Parameters
    ----------
    tested_interval : One field in enum IntervalsTypes
        The tested interval refered to as in enum class
        IntervalsTypes.

    Returns
    -------
    out : bool
        True if tested_interval is a valid enrichment.

    Examples
    --------
    >>> _is_valid_enrichment(IntervalsTypes.MAJOR_THIRD)
    False
    >>> _is_valid_enrichment(IntervalsTypes.DIMINISHED_FIFTH)
    True
    """
    return tested_interval in VALID_ENRICHMENTS


def has_valid_enrichments(chord_properties):
    """
    Tests the validity of a ChordHarmonicPropertie's enrichments

    Parameters
    ----------
    chord_properties : ChordHarmonicProperties
        The instance of ChordHarmonicProperties that's being tested.

    Returns
    -------
    out : bool
        True if all enrichments of chord_properties are intervals
        that can be considered has harmonicaly valid, False
        otherwise.

    Examples
    --------
    >>> chord_properties = ChordHarmonicProperties('C', ChordsTypes.MAJOR_TRIAD, [IntervalsTypes.FOURTH])
    >>> has_valid_enrichments(chord_properties)
    True
    >>> chord_properties = ChordHarmonicProperties('C', ChordsTypes.ROCK_FIFTH, [IntervalsTypes.MAJOR_THIRD])
    >>> assert has_valid_enrichments(chord_properties)
    FALSE # MAJOR_THRID is not considered as an enrichment
    """
    return False not in [_is_valid_enrichment(enrichment) for enrichment in chord_properties.enrichments()]


def guess_most_likely_harmonic_properties(chords_properties):
    """
    Returns the most harmonic valid properties in a list
 
    Parameters
    ----------
    chords_properties : list of ChordHarmonicProperties
        Contains the instances of ChordHarmonicProperties that are
        being tested.

    Returns
    -------
    out : list of ChordHarmonicProperties
        Contains the selected most valid elements from the harmonic
        point of view.

    Examples
    --------
    all_possible = chord_explorer(['C3', 'Eb4', 'F3', 'Bb5']).possible_harmonic_properties()
    most_likely = guess_most_likely_harmonic_properties(all_possible)
    >>> for p in most_likely:
    ...     print('Tonality    :', p.tonality())
    ...     print('Base type   :', p.base_type().name)
    ...     print('Enrichments :', [i.name for i in p.enrichments()])
    ...     print('')
    Tonality    : C
    Base type   : MINOR_SEVENTH_TRIAD
    Enrichments : ['FOURTH']
    """
    properties_filter = HarmonicPropertiesFilter(chords_properties)
    properties_filter.add_predicate(Predicate(has_known_base_type))
    properties_filter.add_predicate(Predicate(has_valid_enrichments))
    properties_filter.add_predicate(Predicate(count_enrichments, count_minimum_enrichments(chords_properties)))
    return properties_filter.filtered()


def keyboard_to_chord_properties(i_notes_on_keyboard):
    """
    Transforms a list of keyboard notes indices into the most likely
    ChordHarmonicProperties if it exists.

    Parameters
    ----------
    i_notes_on_keyboard : list of int
        Keyboard notes indices

    Returns
    -------
    out : ChordHarmonicProperties or None
        An instance of ChordHarmonicProperties if likely properties
        can be found, None otherwise.

    Examples
    --------
    >>> chord_properties = keyboard_to_chord_properties([27, 31, 34, 44])
    >>> chord_properties.tonality()
    C
    >>> chord_properties.base_type().name
    MAJOR_TRIAD
    >>> [i.name for i in chord_properties.enrichments()]
    ['FOURTH']
    """
    all_possible = KeyboardToHarmonicPropertiesTranslator(i_notes_on_keyboard).possible_harmonic_properties()
    most_likely = guess_most_likely_harmonic_properties(all_possible)
    bass_tonalities = [n.tone() for n in notes(_keyboard_to_possible_notes_names(min(i_notes_on_keyboard)))]
    fundamentals = list(filter(lambda properties: properties.tonality() in bass_tonalities, most_likely))
    inversions = list(filter(lambda properties: properties.tonality() not in bass_tonalities, most_likely))
    if len(fundamentals) > 0:
        return fundamentals[0]
    elif len(inversions) > 0:
        return inversions[0]
    else:
        return None


def count_inversions(base_chord):
    """
    Returns the number of possible inversions of base_chord.

    Parameters
    ----------
    base_chord : instance of Chord
        Analyzed chord.

    Returns
    -------
    out : int
        The number of possible inversions of base_chord.

    Examples
    --------
    >>> analyzed_chord = chord(['C3', 'E3', 'G3', 'E4'])
    >>> count_inversions(analyzed_chord)
    2
    """
    return len(base_chord.intervals())


def inversed_chord(base_chord, i_inversion):
    """
    Returns the i_inversion-th inversed chord of base_chord.

    Parameters
    ----------
    base_chord : instance of Chord
        Chord the inversion of which is requested.
    i_inversion : int
        Index of chord inversion. Inversion indices are sorted by
        diminished interval ranges. That is, the first inversion is
        obtained by inverting the greatest interval in base_chord,
        and so on.

    Returns
    -------
    out : instance of Chord
        The instance of Chord corresponding to the inversion.

    Examples
    --------
    >>> my_chord = chord(['E2', 'C3', 'G3'])
    >>> [i.type().name for i in inversed_chord(my_chord, 0).intervals()]
    ['MAJOR_THIRD', 'FIFTH']
    """
    return ChordInversion(base_chord, i_inversion).inversed()


def inversed_chords(base_chord):
    """
    Returns all possible inversions of base_chord.

    Parameters
    ----------
    base_chord : instance of Chord
        Chord the inversion of which is requested.

    Returns
    -------
    out : list of instances of Chord
        Possible inversions of base_chord.

    Examples
    --------
    >>> my_chord = chord(['C3', 'E3', 'G3'])
    >>> inversions = inversed_chords(my_chord)
    >>> for c in inversions:
    ...     [i.type().name for i in c.intervals()]
    ['FOURTH', 'SIXTH']
    ['MINOR_THIRD', 'DIMINISHED_SIXTH']
    """
    n_inversions = count_inversions(base_chord)
    return [inversed_chord(base_chord, i_inversion) for i_inversion in range(n_inversions)]


class ChordInversion:
    """
    A class that permits the inversion of chords.

    Parameters
    ----------
    base_chord : instance of Chord
        Chord the inversion of which is requested.
    i_inversion : int
        Index of chord inversion. Inversion indices are sorted by
        diminished interval ranges. That is, the first inversion is
        obtained by inverting the greatest interval in base_chord,
        and so on.

    Examples
    --------
    >>> my_chord = chord(['E2', 'C3', 'G3'])
    >>> my_inversion = ChordInversion(my_chord, 0)
    >>> [i.type().name for i in my_inversion.inversed().intervals()]
    ['MAJOR_THIRD', 'FIFTH']
    """
    def __init__(self, base_chord, i_inversion):
        """ Buidls an instance of ChordInversion """
        self._chord      = base_chord
        self._i_inversion = i_inversion

    def root_note_index(self):
        """ Returns the index of the root note of the inversion """
        return -(1 + self._i_inversion)

    def root_note(self):
        """ Returns the root note of the inversion """
        i_root_note, octave = self.root_note_index(), Interval(n_semitones = 12, tones_range = 0)
        return transposed_note(
        base_note              = self._chord.notes()[self.root_note_index()],
        transposition_interval = octave,
        orientation            = 'decrease'
        )

    def inversed_notes(self):
        """ Returns the notes of the inversed chord """
        chord_notes = self._chord.notes()
        chord_notes[self.root_note_index()] = self.root_note()
        return chord_notes

    def inversed(self):
        """ Returns the inversed chord corresponding to input parameters """
        return chord([note.name() for note in self.inversed_notes()])

