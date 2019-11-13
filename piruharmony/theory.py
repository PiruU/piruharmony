from keyboard import notes_references
from enum import Enum

DEFAULT_NOTE_TAG = 'A4'
VALID_TONES = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def note(note_tag = DEFAULT_NOTE_TAG):
    """
    Returns an instance of class Note.

    Parameters
    ----------
    note_tag : list of two to three characters, optional.
        Overrides the default note tag. The name of the note is given
        in standard english notation. The list concatenates the tone,
        alteration and octave.

    Returns
    -------
    out : Note
        The instance of class Note corresponding to note_tag.

    See Also
    --------
    notes : Returns a list of instance of class Note.

    Examples
    --------
    >>> my_note = note() # default Note is natural 'A' (440Hz)
    >>> my_note.tag()
    'A4'
    >>> my_note = note('G#4')
    >>> my_note.octave()
    '4'
    """
    return Note(note_tag)


def notes(notes_tags, return_sorted = False):
    """
    Returns a list containing instances of class Note.

    Parameters
    ----------
    notes_tags : list of list of two or three characters.
        The name of the notes are given in english notation. The list
        concatenates the tone, alteration and octave.
    return_sorted : boolean, optional
        If True, then the notes in the newly created list of notes
        will be sorted from the lowest to the highest.

    Return
    ------
    out : list containing instances of class Note.
        The instances of class Note corresponding to each element of
        list notes_tags.

    See also
    --------
    note : Returns a instance of class Note from its english notation.

    Examples
    --------
    >>> my_notes = notes(['C3', 'E3', 'D2', 'F2'])
    >>> [n.tag() for n in my_notes]
    ['C3', 'E3', 'D2', 'F2']
    >>> my_notes = notes(['C3', 'E3', 'D2', 'F2'], return_sorted = True)
    >>> [n.tag() for n in my_notes]
    ['D2', 'F2', 'C3', 'E3']
    """
    unsorted_notes = [note(note_tag) for note_tag in notes_tags]
    if return_sorted:
        return sorted(unsorted_notes, key = lambda note: note.keyboard_index())
    else:
        return unsorted_notes


def lowest_note(notes_tags):
    """
    Returns the lowest note among a list of notes names.

    Parameters
    ----------
    notes_tags : list of list of two or three characters.
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
    >>> lowest_note(['Eb2', 'Bb4', 'G3', 'C1']).tag()
    'C1'
    """
    return notes(notes_tags, return_sorted = True)[0]


class Note:
    """
    A class that describes notes.

    A properties class, used to encapsulate characteristics and to
    connect symbols with indices of piano's keys.

    Parameters
    ----------
    note_tag : list of two to three characters, optional.
        Overrides the default note tag. The name of the note is given
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
    >>> my_note.tag()
    'F#4'

    Compare notes
    >>> my_note == Note('G5')
    False
    >>> print(my_note == Note('F#4'))
    True
    """
    def __init__(self, note_tag = DEFAULT_NOTE_TAG):
        """ Builds a Note instance. """
        self._tag = note_tag

    def __eq__(self, other):
        """ Comparison operator overloading. """
        return self.octave() == other.octave() and self.tone() == other.tone() and self.alteration() == other.alteration()

    def octave(self):
        """ Returns the octave of which the note belongs. """
        i_octave = -1
        return self._tag[i_octave]

    def tone(self):
        """ Returns the tone of the note. """
        i_tone = 0
        return self._tag[i_tone]

    def alteration(self):
        """ Returns the alteration; sharp, flat, none. """
        if len(self._tag) == 3:
            i_alteration = 1
            return self._tag[i_alteration]
        else:
            return ''

    def tag(self):
        """ Returns the name of the note in english notation. """
        return self._tag

    def keyboard_index(self):
        """ Returns the piano's key index corresponding to the note. """
        return notes_references[self.tag()]


def interval(root_note_tag, slave_note_tag):
    """
    Returns an instance of class Interval.

    Parameters
    ----------
    root_note_tag : list of two to three characters, optional.
        Reference (bass) note of the interval. root_note_tag is given
        in english notation.
    slave_note_tag : list of two to three characters, optional.
        Slave (high) note of the interval. slave_note_tag is given in
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
    n_semitones = _count_semitones(root_note_tag, slave_note_tag)
    tones_range = _get_tones_range(root_note_tag, slave_note_tag)
    return Interval(n_semitones, tones_range)


def intervals(notes_tags, return_flattened = False):
    """
    Returns a list containing instances of class Interval.

    Parameters
    ----------
    notes_tags : list of list of two or three characters.
        The name of the notes are given in english notation. The list
        concatenates the tone, alteration and octave.
    return_flattened : boolean, optional
        If True, then the intervals in the newly created list of
        intervals will be changed so that they all fit within one
        octave.

    Return
    ------
    out : list containing instances of class Note.
        The instances of class Interval describing intervals between
        the lowest note corresponding to notes_tags and all others.

    See also
    --------
    interval : Returns a instance of class Interval.

    Examples
    --------
    >>> my_intervals = intervals(['C3', 'E3', 'G3', 'Bb3'])
    >>> [i.count_semitones() for i in my_intervals]
    [4, 7, 10]  # ['C3-E3', 'C3-G3', 'C3-Bb3']
    >>> my_intervals = intervals(['C3', 'Eb3', 'Gb2', 'Bb3'], return_flattened = True)
    >>> [i.count_semitones() for i in my_intervals]
    [6, 9, 4]  # ['Gb-C', 'Gb-Eb', 'Gb-Bb']
    >>> [i.tones_range() for i in my_intervals]
    [3, 5, 2]  # ['G to C', 'G to E', 'G to B']
    """
    sorted_notes = notes(notes_tags, return_sorted = True)
    unflattened_intervals = [interval(sorted_notes[0].tag(), note.tag()) for note in sorted_notes[1:]]
    if return_flattened:
        flattened_intervals = [interval.flattened() for interval in unflattened_intervals]
        return sorted(flattened_intervals, key = lambda interval: interval.count_semitones())
    else:
        return unflattened_intervals


def _count_semitones(root_note_tag, slave_note_tag):
    """
    Returns the number of semitones between to notes.

    Parameters
    ----------
    root_note_tag : list of two to three characters, optional.
        Reference (bass) note of the interval. root_note_tag is given
        in english notation.
    slave_note_tag : list of two to three characters, optional.
        Slave (high) note of the interval. slave_note_tag is given in
        english notation.

    Returns
    -------
    out : int
        The number of semitones between notes with tags given as
        input.

    See Also
    --------
    _get_tones_range : Returns the number of tones between two notes.

    Examples
    --------
    >>> _count_semitones('C#3', 'A3')
    8
    """
    root_note, slave_note = notes([root_note_tag, slave_note_tag], return_sorted = True)
    return slave_note.keyboard_index() - root_note.keyboard_index()


def _get_tones_range(root_note_tag, slave_note_tag):
    """
    Returns the number of tones between two notes.

    Parameters
    ----------
    root_note_tag : list of two to three characters, optional.
        Reference (bass) note of the interval. root_note_tag is given
        in english notation.
    slave_note_tag : list of two to three characters, optional.
        Slave (high) note of the interval. slave_note_tag is given in
        english notation.

    Returns
    -------
    out : int
        The difference of tones between notes with tags given as
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
    root_note, slave_note = notes([root_note_tag, slave_note_tag], return_sorted = True)
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


def chord(notes_tags):
    """
    Returns an instance of class Chord.

    Parameters
    ----------
    notes_tags : list of two or three characters.
        Name of notes composing the chord. Tags in notes_tags are
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
    --------
    """
    return Chord(root_note = lowest_note(notes_tags), chord_intervals = intervals(notes_tags, return_flattened = True))


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

    def has_type(self, chord_type):
        """ Returns true if the chords has """
        return self.intervals() == chord_type.value


class ChordsTypes(Enum):
    """
    Gathers all regular chords types existing in major/minor scales
    """
    MAJOR_TRIAD             = [IntervalsTypes.MAJOR_THIRD.value, IntervalsTypes.FIFTH.value]
    MINOR_TRIAD             = [IntervalsTypes.MINOR_THIRD.value, IntervalsTypes.FIFTH.value]
    AUGMENTED_TRIAD         = [IntervalsTypes.MAJOR_THIRD.value, IntervalsTypes.AUGMENTED_FIFTH.value]
    DIMINISHED_TRIAD        = [IntervalsTypes.MINOR_THIRD.value, IntervalsTypes.DIMINISHED_FIFTH.value]
    SEVENTH                 = [IntervalsTypes.MAJOR_THIRD.value, IntervalsTypes.FIFTH.value, IntervalsTypes.MINOR_SEVENTH.value]
    MAJOR_SEVENTH           = [IntervalsTypes.MAJOR_THIRD.value, IntervalsTypes.FIFTH.value, IntervalsTypes.MAJOR_SEVENTH.value]
    MINOR_SEVENTH           = [IntervalsTypes.MINOR_THIRD.value, IntervalsTypes.FIFTH.value, IntervalsTypes.MINOR_SEVENTH.value]
    HALF_DIMINISHED_SEVENTH = [IntervalsTypes.MINOR_THIRD.value, IntervalsTypes.DIMINISHED_FIFTH.value, IntervalsTypes.MINOR_SEVENTH.value]
    MINOR_MAJOR_SEVENTH     = [IntervalsTypes.MINOR_THIRD.value, IntervalsTypes.FIFTH.value, IntervalsTypes.MAJOR_SEVENTH.value]
    AUGMENTED_MAJOR_SEVENTH = [IntervalsTypes.MAJOR_THIRD.value, IntervalsTypes.AUGMENTED_FIFTH.value, IntervalsTypes.MAJOR_SEVENTH.value]
    DIMINISHED_SEVENTH      = [IntervalsTypes.MINOR_THIRD.value, IntervalsTypes.DIMINISHED_FIFTH.value, IntervalsTypes.DIMINISHED_SEVENTH.value]
