import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from theory import *

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
    tested_names = [n.name() for n in sorted_notes(['A4', 'Bb4', 'C#5', 'D2', 'E#3'])]
    expected_names = ['D2', 'E#3', 'A4', 'Bb4', 'C#5']
    assert tested_names == expected_names

def test_notes_equality():
    tested_note = note('F#5')
    assert tested_note == note("F#5")

def test_notes_inequality():
    tested_note = note('F#5')
    assert tested_note != note("F#4")

def test_lowest_note():
    tested_lowest_note = lowest_note(['D3', 'E#3', 'Ab2', 'Bb4', 'C#5'])
    assert tested_lowest_note == note('Ab2')

def test_removed_tonality_duplicates():
    tested_notes = removed_tonality_duplicates(['A5', 'C3', 'E3', 'G3', 'C4', 'E4', 'G4'])
    expected_notes = notes(['A5', 'C3', 'E3', 'G3'])
    assert tested_notes == expected_notes

def test_cleared_notes():
    tested_notes = cleared_notes(['A5', 'C3', 'E3', 'G3', 'C4', 'E4', 'G4'])
    expected_notes = notes(['C3', 'E3', 'G3', 'A5'])
    assert tested_notes == expected_notes

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

def test_cleared_intervals_tones_ranges():
    tested_intervals = cleared_intervals(['C3', 'E3', 'F#1', "B3"])
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

def test_major_triad_contains_rock_fifth():
    assert chord(['C3', 'E3', 'G3']).contains_type(ChordsTypes.ROCK_FIFTH) == True

def test_major_seventh_contains_rock_fifth():
    assert chord(['C3', 'E3', 'G3', 'B3']).contains_type(ChordsTypes.ROCK_FIFTH) == True

def test_major_seventh_contains_major_seventh():
    assert chord(['C3', 'E3', 'G3', 'B3']).contains_type(ChordsTypes.MAJOR_SEVENTH) == True

def test_major_seventh_contains_major_seventh_triad():
    assert chord(['C3', 'E3', 'G3', 'B3']).contains_type(ChordsTypes.MAJOR_SEVENTH_TRIAD) == True

def test_major_seventh_doesnt_contain_minor_triad():
    assert chord(['C3', 'E3', 'G3', 'B3']).contains_type(ChordsTypes.MINOR_TRIAD) == False

def test_major_seventh_doesnt_contain_minor_seventh_triad():
    assert chord(['C3', 'E3', 'G3', 'B3']).contains_type(ChordsTypes.MINOR_SEVENTH_TRIAD) == False

def test_major_seventh_doesnt_contain_minor_seventh():
    assert chord(['C3', 'E3', 'G3', 'B3']).contains_type(ChordsTypes.MINOR_SEVENTH) == False

def test_minor_seventh_contains_rock_fifth():
    assert chord(['C3', 'Eb3', 'G3', 'Bb3']).contains_type(ChordsTypes.ROCK_FIFTH) == True

def test_minor_seventh_contains_minor_triad():
    assert chord(['C3', 'Eb3', 'G3', 'Bb3']).contains_type(ChordsTypes.MINOR_TRIAD) == True

def test_minor_seventh_contains_minor_seventh():
    assert chord(['C3', 'Eb3', 'G3', 'Bb3']).contains_type(ChordsTypes.MINOR_SEVENTH) == True

def test_minor_seventh_contains_minor_seventh_triad():
    assert chord(['C3', 'Eb3', 'G3', 'Bb3']).contains_type(ChordsTypes.MINOR_SEVENTH_TRIAD) == True

def test_minor_seventh_doesnt_contain_major_seventh_triad():
    assert chord(['C3', 'Eb3', 'G3', 'Bb3']).contains_type(ChordsTypes.MAJOR_SEVENTH_TRIAD) == False

def test_minor_seventh_doesnt_contain_major_triad():
    assert chord(['C3', 'Eb3', 'G3', 'Bb3']).contains_type(ChordsTypes.MAJOR_TRIAD) == False

def test_minor_seventh_doesnt_contain_major_seventh():
    assert chord(['C3', 'Eb3', 'G3', 'Bb3']).contains_type(ChordsTypes.MAJOR_SEVENTH) == False

def test_seventh_contains_rock_fifth():
    assert chord(['C3', 'E3', 'G3', 'Bb3']).contains_type(ChordsTypes.ROCK_FIFTH) == True

def test_seventh_doesnt_contain_minor_triad():
    assert chord(['C3', 'E3', 'G3', 'Bb3']).contains_type(ChordsTypes.MINOR_TRIAD) == False

def test_seventh_doesnt_contain_minor_seventh():
    assert chord(['C3', 'E3', 'G3', 'Bb3']).contains_type(ChordsTypes.MINOR_SEVENTH) == False

def test_seventh_doesnt_contain_minor_seventh_triad():
    assert chord(['C3', 'E3', 'G3', 'Bb3']).contains_type(ChordsTypes.MINOR_SEVENTH_TRIAD) == False

def test_seventh_doesnt_contain_major_seventh_triad():
    assert chord(['C3', 'E3', 'G3', 'Bb3']).contains_type(ChordsTypes.MAJOR_SEVENTH_TRIAD) == False

def test_seventh_contains_major_triad():
    assert chord(['C3', 'E3', 'G3', 'Bb3']).contains_type(ChordsTypes.MAJOR_TRIAD) == True

def test_seventh_doesnt_contain_major_seventh():
    assert chord(['C3', 'E3', 'G3', 'Bb3']).contains_type(ChordsTypes.MAJOR_SEVENTH) == False

def test_seventh_contains_seventh_triad():
    assert chord(['C3', 'E3', 'G3', 'Bb3']).contains_type(ChordsTypes.SEVENTH_TRIAD) == True

def test_tonality_chord_harmonic_properties_Fsus4():
    tested_properties = ChordHarmonicProperties('F', ChordsTypes.MAJOR_TRIAD, [IntervalsTypes.FOURTH])
    expected_tonality = 'F'
    assert tested_properties.tonality() == expected_tonality

def test_base_type_name_chord_harmonic_properties_Fsus4():
    tested_properties = ChordHarmonicProperties('F', ChordsTypes.MAJOR_TRIAD, [IntervalsTypes.FOURTH])
    expected_base_type_name = 'MAJOR_TRIAD'
    assert tested_properties.base_type().name == expected_base_type_name

def test_enrichments_semitones_count_chord_harmonic_properties_Fsus4():
    tested_properties = ChordHarmonicProperties('F', ChordsTypes.MAJOR_TRIAD, [IntervalsTypes.FOURTH])
    expected_n_semitones = 5
    assert tested_properties.enrichments()[0].value.count_semitones() == expected_n_semitones

def test_count_enrichments_chord_harmonic_properties_Fsus4():
    tested_properties = ChordHarmonicProperties('F', ChordsTypes.MAJOR_TRIAD, [IntervalsTypes.FOURTH])
    expected_n_enrichments = 1
    assert tested_properties.count_enrichments() == expected_n_enrichments

def test_count_enrichments_chord_harmonic_properties_Fsus2sus4():
    tested_properties = ChordHarmonicProperties('F', ChordsTypes.MAJOR_TRIAD, [IntervalsTypes.NINTH, IntervalsTypes.FOURTH])
    expected_n_enrichments = 2
    assert tested_properties.count_enrichments() == expected_n_enrichments

def test_chord_explorer_eb_tonality():
    tested_tonality = chord_explorer(['Eb3', 'G4', 'Bb5']).tonality()
    expected_tonality = 'Eb'
    assert tested_tonality == expected_tonality

def test_chord_explorer_g_tonality():
    tested_tonality = chord_explorer(['G4', 'Eb5', 'Bb5']).tonality()
    expected_tonality = 'G'
    assert tested_tonality == expected_tonality

def test_chord_explorer_major_triad():
    tested_base_types = chord_explorer(['C3', 'E4', 'G5']).possible_base_types()
    expected_base_type = ChordsTypes.MAJOR_TRIAD
    assert expected_base_type in tested_base_types

def test_chord_explorer_minor_triad():
    tested_base_types = chord_explorer(['C3', 'Eb4', 'G5']).possible_base_types()
    expected_base_type = ChordsTypes.MINOR_TRIAD
    assert expected_base_type in tested_base_types

def test_chord_explorer_major_seventh_triad():
    tested_base_types = chord_explorer(['C3', 'E4', 'B5']).possible_base_types()
    expected_base_type = ChordsTypes.MAJOR_SEVENTH_TRIAD
    assert expected_base_type in tested_base_types

def test_chord_explorer_minor_seventh_triad():
    tested_base_types = chord_explorer(['C3', 'Eb4', 'Bb5']).possible_base_types()
    expected_base_type = ChordsTypes.MINOR_SEVENTH_TRIAD
    assert expected_base_type in tested_base_types

def test_chord_explorer_minor_major_seventh_triad():
    tested_base_types = chord_explorer(['C3', 'Eb4', 'B5']).possible_base_types()
    expected_base_type = ChordsTypes.MINOR_MAJOR_SEVENTH_TRIAD
    assert expected_base_type in tested_base_types

def test_chord_explorer_seventh_triad():
    tested_base_types = chord_explorer(['C3', 'E4', 'Bb5']).possible_base_types()
    expected_base_type = ChordsTypes.SEVENTH_TRIAD
    assert expected_base_type in tested_base_types

def test_chord_explorer_diminished_triad():
    tested_base_types = chord_explorer(['C3', 'Eb4', 'Gb5']).possible_base_types()
    expected_base_type = ChordsTypes.DIMINISHED_TRIAD
    assert expected_base_type in tested_base_types

def test_chord_explorer_major_seventh():
    tested_base_types = chord_explorer(['C3', 'E4', 'G5', 'B4']).possible_base_types()
    expected_base_type = ChordsTypes.MAJOR_SEVENTH
    assert expected_base_type in tested_base_types

def test_chord_explorer_minor_seventh():
    tested_base_types = chord_explorer(['C3', 'Eb4', 'G5', 'Bb5']).possible_base_types()
    expected_base_type = ChordsTypes.MINOR_SEVENTH
    assert expected_base_type in tested_base_types

def test_chord_explorer_minor_major_seventh():
    tested_base_types = chord_explorer(['C3', 'Eb4', 'G5', 'B5']).possible_base_types()
    expected_base_type = ChordsTypes.MINOR_MAJOR_SEVENTH
    assert expected_base_type in tested_base_types

def test_chord_explorer_seventh():
    tested_base_types = chord_explorer(['G3', 'B3', 'D4', 'F4']).possible_base_types()
    expected_base_type = ChordsTypes.SEVENTH
    assert expected_base_type in tested_base_types

def test_keyboard_to_harmonic_properties_translator_base_type_major_triad_in_Csus4():
    tested_properties = KeyboardToHarmonicPropertiesTranslator([27, 31, 32, 34]).possible_harmonic_properties()
    assert ChordsTypes.MAJOR_TRIAD in [p.base_type() for p in tested_properties]

def test_keyboard_to_harmonic_properties_translator_base_type_major_seventh_triad_in_C7sus4():
    tested_properties = KeyboardToHarmonicPropertiesTranslator([27, 31, 32, 38]).possible_harmonic_properties()
    assert ChordsTypes.MAJOR_SEVENTH_TRIAD in [p.base_type() for p in tested_properties]

def test_keyboard_to_harmonic_properties_translator_enrichments_fourth_in_Csus4():
    tested_properties = KeyboardToHarmonicPropertiesTranslator([27, 31, 32, 34]).possible_harmonic_properties()
    assert [IntervalsTypes.FOURTH] in [p.enrichments() for p in tested_properties]

def test_has_known_base_type_false():
    tested_properties = ChordHarmonicProperties('C', ChordsTypes.UNKNOWN, [])
    assert has_known_base_type(tested_properties) == False

def test_has_known_base_type_true():
    tested_properties = ChordHarmonicProperties('C', ChordsTypes.MAJOR_TRIAD, [])
    assert has_known_base_type(tested_properties) == True

def test_predicate_is_zero_true():
    def is_zero(value):
        return value == 0
    assert Predicate(is_zero, True).test(0) == True

def test_predicate_is_zero_false():
    def is_zero(value):
        return value == 0
    assert Predicate(is_zero, True).test(1) == False

def test_predicate_is_not_zero_true():
    def is_zero(value):
        return value == 0
    assert Predicate(is_zero, False).test(1) == True

def test_predicate_is_not_zero_false():
    def is_zero(value):
        return value == 0
    assert Predicate(is_zero, False).test(0) == False

def test_harmonic_properties_filter_remove_unknown_base_type():
    all_properties = chord_explorer(['C3', 'Eb3', 'G3', 'B3']).possible_harmonic_properties()
    filtered_properties = HarmonicPropertiesFilter(all_properties).add_predicate(Predicate(has_known_base_type)).filtered()
    unknown_in_all_properties = ChordsTypes.UNKNOWN in [p.base_type() for p in all_properties]
    unknown_not_in_filtered_properties = ChordsTypes.UNKNOWN not in [p.base_type() for p in filtered_properties]
    assert unknown_in_all_properties and unknown_not_in_filtered_properties

def test_count_minimum_enrichments_is_zero():
    all_properties = [
    ChordHarmonicProperties('C', ChordsTypes.MAJOR_TRIAD, [IntervalsTypes.MAJOR_SEVENTH]),
    ChordHarmonicProperties('C', ChordsTypes.MAJOR_SEVENTH, []),
    ]
    expected_return = 0
    assert count_minimum_enrichments(all_properties) == expected_return

def test_enrichments_is_one():
    chord_properties = ChordHarmonicProperties('C', ChordsTypes.MAJOR_TRIAD, [IntervalsTypes.MAJOR_SEVENTH])
    expected_return = 1
    assert count_enrichments(chord_properties) == expected_return

def test_has_valid_enrichments_true():
    chord_properties = ChordHarmonicProperties('C', ChordsTypes.MAJOR_TRIAD, [IntervalsTypes.FOURTH])
    assert has_valid_enrichments(chord_properties) == True

def test_has_valid_enrichments_false():
    chord_properties = ChordHarmonicProperties('C', ChordsTypes.ROCK_FIFTH, [IntervalsTypes.MAJOR_THIRD])
    assert has_valid_enrichments(chord_properties) == False

def test_guess_most_likely_harmonic_properties_Csus4():
    all_possible = chord_explorer(['C3', 'E3', 'F4', 'G5']).possible_harmonic_properties()
    most_likely = guess_most_likely_harmonic_properties(all_possible)
    expected = ChordHarmonicProperties('C', ChordsTypes.MAJOR_TRIAD, [IntervalsTypes.FOURTH])
    assert expected == most_likely[0]

def test_guess_most_likely_harmonic_properties_C5sus4():
    all_possible = chord_explorer(['C3', 'F4', 'G5']).possible_harmonic_properties()
    most_likely = guess_most_likely_harmonic_properties(all_possible)
    expected = ChordHarmonicProperties('C', ChordsTypes.ROCK_FIFTH, [IntervalsTypes.FOURTH])
    assert expected == most_likely[0]

def test_guess_most_likely_harmonic_properties_Cmaj7():
    all_possible = chord_explorer(['C3', 'E4', 'G5', 'B5']).possible_harmonic_properties()
    most_likely = guess_most_likely_harmonic_properties(all_possible)
    expected = ChordHarmonicProperties('C', ChordsTypes.MAJOR_SEVENTH, [])
    assert expected == most_likely[0]

def test_guess_most_likely_harmonic_properties_Cmin7():
    all_possible = chord_explorer(['C3', 'Eb4', 'G5', 'Bb5']).possible_harmonic_properties()
    most_likely = guess_most_likely_harmonic_properties(all_possible)
    expected = ChordHarmonicProperties('C', ChordsTypes.MINOR_SEVENTH, [])
    assert expected == most_likely[0]

def test_guess_most_likely_harmonic_properties_C7():
    all_possible = chord_explorer(['C3', 'Eb4', 'Bb5']).possible_harmonic_properties()
    most_likely = guess_most_likely_harmonic_properties(all_possible)
    expected = ChordHarmonicProperties('C', ChordsTypes.MINOR_SEVENTH_TRIAD, [])
    assert expected == most_likely[0]

def test_guess_most_likely_harmonic_properties_C7sus4():
    all_possible = chord_explorer(['C3', 'Eb4', 'F3', 'Bb5']).possible_harmonic_properties()
    most_likely = guess_most_likely_harmonic_properties(all_possible)
    expected = ChordHarmonicProperties('C', ChordsTypes.MINOR_SEVENTH_TRIAD, [IntervalsTypes.FOURTH])
    assert expected == most_likely[0]

def test_keyboard_to_chord_properties_Cmaj():
    tested = keyboard_to_chord_properties([27, 31, 34])
    expected = ChordHarmonicProperties('C', ChordsTypes.MAJOR_TRIAD, [])
    assert tested == expected

def test_keyboard_to_chord_properties_Csus2():
    tested = keyboard_to_chord_properties([27, 31, 34, 53])
    expected = ChordHarmonicProperties('C', ChordsTypes.MAJOR_TRIAD, [IntervalsTypes.NINTH])
    assert tested == expected

def test_keyboard_to_chord_properties_Csus4():
    tested = keyboard_to_chord_properties([27, 31, 34, 44])
    expected = ChordHarmonicProperties('C', ChordsTypes.MAJOR_TRIAD, [IntervalsTypes.FOURTH])
    assert tested == expected

