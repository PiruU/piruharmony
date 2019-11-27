from keyboard import notes_references
from enum import Enum
from itertools import product
from functools import reduce
from operator import add


DEFAULT_NOTE_TAG = 'A4'
VALID_TONES = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


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
    --------
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
    ROCK_FIFTH                = [IntervalsTypes.FIFTH]
    UNKNOWN                   = []


class ChordExplorer:
    """
    """
    def __init__(self, explored_chord):
        """  """
        self._chord = explored_chord

    def tonality(self):
        """  """
        return self._chord.root_note().tonality()

    def possible_base_types(self):
        """  """
        return [type for type in ChordsTypes if self._chord.contains_type(type)]

    def possible_enrichments_lists(self):
        """  """
        base_types, enrichments = self.possible_base_types(), []
        for base_type in base_types:
            enrichments.append([interval.type() for interval in self._chord.intervals() if interval.type() not in base_type.value])
        return enrichments

    def possible_harmonic_properties(self):
        """  """
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
    >>> chord_properties.tonality()
    'F#'
    >>> chord_properties.base_type().name
    'MAJOR_TRIAD'
    >>> [interval.type().name for interval in chord_properties.base_type().value]
    ['MAJOR_THIRD', 'FIFTH']
    >>> [interval.name for interval in chord_properties.enrichments()]
    ['FOURTH']
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


def _keyboard_to_possible_notes_names(i_note):
    """
    """
    return [key for key in notes_references.keys() if notes_references[key] == i_note]


class KeyboardToHarmonyTranslator:
    """
    """
    def __init__(self, i_notes_on_keyboard):
        self._i_notes = i_notes_on_keyboard

    def possible_notes_names_lists(self):
        """  """
        return [_keyboard_to_possible_notes_names(i_note) for i_note in self._i_notes]

    def possible_chords(self):
        """  """
        notes_names_lists = self.possible_notes_names_lists()
        return [chord(notes_names) for notes_names in list(product(*notes_names_lists))]

    def possible_harmonic_properties(self):
        possible_chords = self.possible_chords()
        return reduce(add, [ChordExplorer(chord).possible_harmonic_properties() for chord in possible_chords])


def have_known_base_type(chord_properties):
    return chord_properties.base_type().name != 'UNKNOWN'


class Predicate:
    """
    """
    def __init__(self, function, expected_return = True):
        self._function = function
        self._return = expected_return

    def test(self, arguments):
        return self._function(arguments) == self._return


class HarmonicPropertiesFilter:
    """
    """
    def __init__(self, chords_properties):
        self._chords_properties = chords_properties
        self._predicates = []

    def add_predicate(self, predicate):
        self._predicates.append(predicate)
        return self

    def filtered(self):
        for predicate in self._predicates:
            self._chords_properties = list(filter(lambda properties: predicate.test(properties), self._chords_properties))
        return self._chords_properties


def count_minimum_enrichments(chords_properties):
    """
    """
    return min([properties.count_enrichments() for properties in chords_properties])


def count_enrichments(chord_properties):
    """
    """
    return chord_properties.count_enrichments()



"""
"""
VALID_ENRICHMENTS = [
IntervalsTypes.DIMINISHED_NINTH , IntervalsTypes.NINTH          , IntervalsTypes.AUGMENTED_NINTH ,
IntervalsTypes.DIMINISHED_FOURTH, IntervalsTypes.FOURTH         ,IntervalsTypes.AUGMENTED_FOURTH ,
IntervalsTypes.DIMINISHED_FIFTH , IntervalsTypes.AUGMENTED_FIFTH, IntervalsTypes.DIMINISHED_SIXTH,
IntervalsTypes.SIXTH            , IntervalsTypes.AUGMENTED_SIXTH
]


def _is_valid_enrichment(enrichment):
    """
    """
    return enrichment in VALID_ENRICHMENTS


def have_valid_enrichments(chord_properties):
    """
    """
    return False not in [_is_valid_enrichment(enrichment) for enrichment in chord_properties.enrichments()]


def guess_most_likely_properties(chords_properties):
    """
    """
    properties_filter = HarmonicPropertiesFilter(chords_properties)
    properties_filter.add_predicate(Predicate(have_known_base_type))
    properties_filter.add_predicate(Predicate(have_valid_enrichments))
    #properties_filter.add_predicate(Predicate(count_enrichments, count_minimum_enrichments(chords_properties)))
    return properties_filter.filtered()


def keyboard_to_chord_properties(i_notes_on_keyboard):
    """
    """
    all_possible = KeyboardToHarmonyTranslator(i_notes_on_keyboard).possible_harmonic_properties()
    most_likely = guess_most_likely_properties(all_possible)
    if len(most_likely) > 0:
        return most_likely[0]
    else:
        return None

