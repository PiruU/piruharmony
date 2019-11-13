import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from theory import note, notes, lowest_note, interval, intervals, IntervalsTypes, chord, ChordsTypes

def test_default_note_octave():
    assert note().octave() == '4'

def test_default_note_tone():
    assert note().tone() == 'A'

def test_default_note_alteration():
    assert note().alteration() == ''

def test_custom_note_octave():
    assert note('G#5').octave() == '5'

def test_custom_note_tone():
    assert note('G#5').tone() == 'G'

def test_custom_note_alteration():
    assert note('G#5').alteration() == '#'

def test_notes_octaves():
    tested_octaves = [n.octave() for n in notes(['A4', 'Bb4', 'C#5', 'D2', 'E#3'])]
    expected_octaves = ['4', '4', '5', '2', '3']
    assert  tested_octaves == expected_octaves

def test_notes_tones():
    tested_tones = [n.tone() for n in notes(['A4', 'Bb4', 'C#5', 'D2', 'E#3'])]
    expected_tones = ['A', 'B', 'C', 'D', 'E']
    assert tested_tones == expected_tones

def test_notes_alterations():
    tested_alterations = [n.alteration() for n in notes(['A4', 'Bb4', 'C#5', 'D2', 'E#3'])]
    expected_alterations = ['', 'b', '#', '', '#']
    assert tested_alterations == expected_alterations

def test_sorted_notes():
    tested_tags = [n.tag() for n in notes(['A4', 'Bb4', 'C#5', 'D2', 'E#3'], return_sorted = True)]
    expected_tags = ['D2', 'E#3', 'A4', 'Bb4', 'C#5']
    assert tested_tags == expected_tags

def test_notes_equality():
    tested_note = note('F#5')
    assert tested_note == note("F#5")

def test_notes_inequality():
    tested_note = note('F#5')
    assert tested_note != note("F#4")

def test_lowest_note():
    tested_lowest_note = lowest_note(['D3', 'E#3', 'Ab2', 'Bb4', 'C#5'])
    assert tested_lowest_note == note('Ab2')

def test_interval_semitones():
    tested_interval = interval('C3', 'G#3')
    assert tested_interval.count_semitones() == 8

def test_interval_tones_range():
    tested_interval = interval('C3', 'Fb3')
    assert tested_interval.tones_range() == 3

def test_interval_equality():
    tested_interval = interval('C3', 'F3')
    assert tested_interval == interval('G2', 'C3')

def test_interval_inequality():
    tested_interval = interval('C3', 'F3')
    assert tested_interval != interval('G2', 'F3')

def test_raw_intervals_semitones():
    tested_intervals = intervals(['C3', 'E3', 'F#3', "B3"])
    tested_semitones = [i.count_semitones() for i in tested_intervals]
    assert tested_semitones == [4, 6, 11]

def test_raw_intervals_tones_ranges():
    tested_intervals = intervals(['C3', 'E3', 'F#3', "B3"])
    tested_tones_ranges = [i.tones_range() for i in tested_intervals]
    assert tested_tones_ranges == [2, 3, 6]

def test_flattened_intervals_semitones():
    tested_intervals = intervals(['C3', 'E3', 'F#1', "B3"], return_flattened = True)
    tested_semitones = [i.count_semitones() for i in tested_intervals]
    assert tested_semitones == [5, 6, 10]

def test_flattened_intervals_tones_ranges():
    tested_intervals = intervals(['C3', 'E3', 'F#1', "B3"], return_flattened = True)
    tested_tones_ranges = [i.tones_range() for i in tested_intervals]
    assert tested_tones_ranges == [3, 4, 6]

def test_diminished_ninth():
    tested_interval = interval('C3', 'Db3')
    assert tested_interval.has_type(IntervalsTypes.DIMINISHED_NINTH)

def test_ninth():
    tested_interval = interval('D3', 'E5')
    assert tested_interval.has_type(IntervalsTypes.NINTH)

def test_augmented_ninth():
    tested_interval = interval('F3', 'G#3')
    assert tested_interval.has_type(IntervalsTypes.AUGMENTED_NINTH)

def test_diminished_third():
    tested_interval = interval('A#2', 'C3')
    assert tested_interval.has_type(IntervalsTypes.DIMINISHED_THIRD)

def test_minor_third():
    tested_interval = interval('E5', 'G5')
    assert tested_interval.has_type(IntervalsTypes.MINOR_THIRD)

def test_major_third():
    tested_interval = interval('D6', 'F#6')
    assert tested_interval.has_type(IntervalsTypes.MAJOR_THIRD)

def test_augmented_third():
    tested_interval = interval('F6', 'A#6')
    assert tested_interval.has_type(IntervalsTypes.AUGMENTED_THIRD)

def test_diminished_fourth():
    tested_interval = interval('E1', 'Ab1')
    assert tested_interval.has_type(IntervalsTypes.DIMINISHED_FOURTH)

def test_fourth():
    tested_interval = interval('A1', 'D2')
    assert tested_interval.has_type(IntervalsTypes.FOURTH)

def test_augmented_fourth():
    tested_interval = interval('Bb3', 'E4')
    assert tested_interval.has_type(IntervalsTypes.AUGMENTED_FOURTH)

def test_diminished_fifth():
    tested_interval = interval('A#5', 'E6')
    assert tested_interval.has_type(IntervalsTypes.DIMINISHED_FIFTH)

def test_fifth():
    tested_interval = interval('Db4', 'Ab4')
    assert tested_interval.has_type(IntervalsTypes.FIFTH)

def test_augmented_fifth():
    tested_interval = interval('Db5', 'A5')
    assert tested_interval.has_type(IntervalsTypes.AUGMENTED_FIFTH)

def test_diminished_sixth():
    tested_interval = interval('C#3', 'A3')
    assert tested_interval.has_type(IntervalsTypes.DIMINISHED_SIXTH)

def test_sixth():
    tested_interval = interval('F2', 'D3')
    assert tested_interval.has_type(IntervalsTypes.SIXTH)

def test_augmented_sixth():
    tested_interval = interval('F2', 'D#3')
    assert tested_interval.has_type(IntervalsTypes.AUGMENTED_SIXTH)

def test_diminished_seventh():
    tested_interval = interval('B2', 'Ab3')
    assert tested_interval.has_type(IntervalsTypes.DIMINISHED_SEVENTH)

def test_minor_seventh():
    tested_interval = interval('E5', 'D6')
    assert tested_interval.has_type(IntervalsTypes.MINOR_SEVENTH)

def test_major_seventh():
    tested_interval = interval('C4', 'B4')
    assert tested_interval.has_type(IntervalsTypes.MAJOR_SEVENTH)

def test_major_triad():
    tested_chord = chord(['C3', 'E4', 'G5'])
    assert tested_chord.has_type(ChordsTypes.MAJOR_TRIAD)

def test_minor_triad():
    tested_chord = chord(['C3', 'Eb4', 'G5'])
    assert tested_chord.has_type(ChordsTypes.MINOR_TRIAD)

def test_diminished_triad():
    tested_chord = chord(['B3', 'D4', 'F5'])
    assert tested_chord.has_type(ChordsTypes.DIMINISHED_TRIAD)

def test_augmented_triad():
    tested_chord = chord(['C3', 'E4', 'G#5'])
    assert tested_chord.has_type(ChordsTypes.AUGMENTED_TRIAD)

def test_seventh_chord():
    tested_chord = chord(['G3', 'B4', 'D5', 'F4'])
    assert tested_chord.has_type(ChordsTypes.SEVENTH)

def test_major_seventh_chord():
    tested_chord = chord(['F3', 'E6', 'A4', 'C5'])
    assert tested_chord.has_type(ChordsTypes.MAJOR_SEVENTH)

def test_minor_seventh_chord():
    tested_chord = chord(['D3', 'F4', 'C4', 'A5'])
    assert tested_chord.has_type(ChordsTypes.MINOR_SEVENTH)

def test_half_diminished_seventh_chord():
    tested_chord = chord(['C3', 'Eb4', 'Gb5', 'Bb5'])
    assert tested_chord.has_type(ChordsTypes.HALF_DIMINISHED_SEVENTH)

def test_minor_major_seventh_chord():
    tested_chord = chord(['C3', 'Eb4', 'G5', 'B5'])
    assert tested_chord.has_type(ChordsTypes.MINOR_MAJOR_SEVENTH)

def test_augmented_major_seventh_chord():
    tested_chord = chord(['C3', 'E4', 'G#5', 'B4'])
    assert tested_chord.has_type(ChordsTypes.AUGMENTED_MAJOR_SEVENTH)

def test_diminished_seventh_chord():
    tested_chord = chord(['B3', 'D4', 'F5', 'Ab4'])
    assert tested_chord.has_type(ChordsTypes.DIMINISHED_SEVENTH)
