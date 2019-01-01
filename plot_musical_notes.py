#!/usr/bin/env python

# script to plot musical scale
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.ticker

# different methods of musical pitch notation:
# 1) scientific pitch notation (ISO 16, A440 hz, using concert pitch of 440hz for A above middle C)
# 2) scientific pitch (verdi tuning or philosophical pitch) - all Cs are integer powers of 2, C4 = 256 hz
#			scientific pitch is based on C-4 = 1 hz, creating C octaves of 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536 hz
#			C4 = 256 hz instead of 261.62 is ~37.6 cents lower than common A440 pitch standard
#			cent = logarithmic unit of measure used for musical intervals
#			twelve-tone equal temperament divides the octave into 12 semitones of 100 cents each -> cent = 1/1200 of chromatic scale
#			octave = 1200 cents = two notes that span a frequency ratio of 2:1
#			semitones = half-step = smallest musical interval used in western music, considered the most disonnant when sounded harmonically
#			like decibel's relation to intensity, a cent is a ratio between two close frequencies
#			therefore, the frequency range encompassed by a cent must be proportional to the two frequencies
#			ratio of frequencies one cent apart = 2 ^ (1/1200) ~ 1.000 577 7895
#			n = 1200 * log2 (b/a) given frequencies of notes a and b of two notes
#			the threshold of what is perceptible is known as the "just noticeable difference", which varies as a function
#			of frequency, amplituden and timbre, but some authors state 5-6 cents as a heuristic JND
#			side notes: one study of modern performances of schubert's ave maria found that vibrato span typically ranged
#			between +/- 34 cents and +/- 123 cents, with a mean of +/- 71 cents
#			Normal adults are able to distingush pitch differences as small as 25 cents reliably.
# 3) helmholtz notation (same as scientific pitch notation except primes and sub primes are replaced with integers)

# minor seconds are 1 semitone wide (100 cents, or 1 interval)
# whole tones or major seconds are 2 semitones wide
#	minor thirds are 3 semitones wide (6:5 freq ratio)
# major thirds are 4 semitones wide (5:4 freq ratio)
# perfect fourths are 5 semitones wide	(4:3 freq ratio)
# augmented fourth / diminished fifth 6 semitones wide
# perfect fifths are 7 semitones wide (called a fifth because they span 5 adjacent notes in the major / minor scale)
#		a fifth defines an interval or mathematical ratio which is the closest and most consonant non-octave interval
#		3:2 freq ratio
#		(diminished sixth)
# minor sixth 8 semitones (augmented fifth)
# major sixth 9 semitones 
# minor seventh 10 semitones
# major seventh 11 semitones
# perfect octave 12 semitones

# diatonic semitone (minor second), chromatic semitone are enharmonically equivalent when twelve tone equal temperament is sued
# but are not the same thing in meantone temperament, where the diatonic semitone is distinguished from and larger than
# the chromatic semitone

# SCALES
# chromatic (dodecatonic) scale - 12 notes per octave C, C#, D, D#, E, F, F#, G, G#, A, A#, B
# octatonic - 8 notes per octave
# heptatonic (diatonic) scale - 7 notes per octave - most common modern western scale
# hexatonic - 6 notes per octave
# pentatonic - 5 notes per octave
# tetratonic, tritonic, ditonic, monotonic

# CHROMATIC SCALE
# in twelve-tone equal temperament all semitones are equal in size (100 cents)
# the condition of having semitones is called hemitonia, that of having no semitones is anhemitonia
# a musical scale or chord containing semitones is called hemitonic; one without semitones is anhemitonic
# the chromatic scale is a musical scale with 12 pitches, each a semitone above or below its adjecent pitch.  
# as a result, in 12 tone equal temperament (the most common temperament in western music) the chromatic scale
# covers all 12 of the available pitches.  Thus, there is only one chromatic scale.  Moreover,
# in equal temperament, all the semitones have the same size (100 cents).  This makes the chromatic scale
# nondiatonic, with no tonic because of the symmetry of its equally-spaced notes.

# the equal tempered chromatic scale divides the octave (which has a ratio of 2:1) into 12 equal parts
# the chromatic scale can then be found by multiplying a starting frequency by 2^ (x/12)
# A				= A(2^(0/12))
# A#			= A(2^(1/12))
# B				= A(2^(2/12))
# C					2^(3/12)
# C#				2^(4/12)
# D					2^(5/12)
# D#				2^(6/12)
# E					2^*7/12)
# F					2^(8/12)
# F#				2^(9/12)
# G					2^(10/12)
# G#				2^(11/12)
# A					2^(12/12)


# DIATONIC SCALE
# in western music theory, a diatonic scale is a heptatonic scale that includes 5 whole steps and two half steps 
# in each octave, in which the two half steps are separated from each other by either two or three whole steps,
# depending on their position in the scale.  This pattern ensures that, in a diatonic scale spanning more than one
# octave, all the half steps are maximally separated from each other.

# A tonic is the first scale degree of a diatonic scale.  A tonic is the reference note of a scale. A root is the reference note of a chord
# A diatonic scale then has two tonics, one an octave higher than the key note tonic.
# diatonic scales are made up of 8 degrees:
# 1 Tonic (key note)			
# 2 supertonic						
# 3 mediant								
# 4 subdominant
# 5 Dominant
# 6 Submediant
# 7 subtonic (leading tone) - note that resolves (moves from dissonance, an unstable sound, to consonance, a stable sound) to a note one semitone higher or lower
# 8 tonic (octave)

# the 7th scale degree (leading tone) has a strong affinity for and leads melodically to the tonic.
# disconnance is said to haveits resolution when it moves to a consonance.  When a resolution is delayed
# or is accomplished in surprising ways, when the composer plays with our sense of expectation, a feeling of
# drama or suspense is created.

# The 7 pitches of any diatonic scale can also be obtained by using a chain of 6 perfect fifths.
# The 7 natural pitches that form the c-major scale can be obtained from a stack of perfect fifths starting from F:
#	F-C-G-D-A-E-B
# any sequence of successive natural notes, such as C-D-E-F-G-A-B, and any transposition thereof, is a diatonic scale
# any sequence of 7 successive white keys plays a diatonic scale. The modern keyboard originated as a diatonic keyboard with only white keys.
# black keys were added for improving the consonances, mainly the thirds, by providing a major third on each degree,
# allowing all twelve transpositions, and helping musicians to find their bearings.

# KEY: the key usually identifies the tonic note and/or chord: the note and/or major or minor triad that represents
# 		the final point of rest for a piece, or the focal point of a section.
#			A key is differentiated from a scale in that a scale is an ordered set of notes typically used in a key,
#			whereas the key is the "center of gravity" established by particular chord progressions

# MAJOR SCALE (IONIAN) T-T-S-T-T-T-S
# 7 distince notes, plus and 8th that duplicates the first and octave higher
# using T for tone (whole step) and S for semitone (half step) we can write the scale:
# T-T-S-T-T-T-S
# This gives us C major:
# C--D--E--F--G--A--B--C
#	 T--T--S--T--T--T--S

# MINOR SCALE
# for each major scale there is a corresponding natural minor scale.  It uses the same sequence of notes,
# but starts from a different note.  That is, it begins on the 6th degree of the major scale and proceeds 
# to the first octave of the 6th degree.
# Notes in A minor:
# A--B--C--D--E--F--G--A
#	 T--T--S--T--T--T--S

# from any major scale, a new scale is obtainedby taking a different degree as the tonic.  With this method,
# it is possible to generate 6 other scales or modes from each major scale.

# of Glarean's six natural scales, three are major scales (those with a major third / triad (4 semitones)):
# 	ionian, lydian, mixolydian
# and three are minor (those with a minor third / triad (3 semitones)):
#		dorian. phrygian, aolian

# triad: set of 3 notes that can be stacked vertically in thirds.  When stacked in thirds notes produce triads.
# Triads are composed of: the 
	#	1 root 
	# 2 the third (major (4 semitones) or minor (3 semitones) above the root)
	# 3 the fifth, whos interval is a minor or major third above the third.  related to the root this gives:
		#	DIMINISHED FIFTH: 	6 semitones above the root
		# PERFECT FIFTH:			7 semitones above the root - most common
		# AUGMENTED FIFTH:		8 semitones above the root
# The first inversion of a triad uses the third as the root, second inversion uses the fifth as the root

# IONIAN MODE (major scale) starts on the 1st degree of the major scale
#	C--D--E--F--G--A--B--C
#	 T--T--S--T--T--T--S
		
# DORIAN MODE starts on the 2nd degree of the major scale
#	D--E--F--G--A--B--C--D
#	 T--S--T--T--T--S--T

# PHRYGIAN MODE starts on the 3rd degree
# E--F--G--A--B--C--D--E
#	 S--T--T--T--S--T--T

# LYDIAN MODE starts on the 4th degree
#	F--G--A--B--C--D--E--F
#	 T--T--T--S--T--T--S

# MIXOLYDIAN MODE starts on the 5th degree
#	G--A--B--C--D--E--F--G
#	 T--T--S--T--T--S--T

# AEOLIAN MODE (natural minor scale) starts on the 6th degree
#	A--B--C--D--E--F--G--A
#	 T--S--T--T--S--T--T

# LOCRIAN MODE starts on the 7th degree
# B--C--D--E--F--G--A--B
#	 S--T--T--S--T--T--T

# diatonic scales can also be described as two diatonic tetrachords separated by a whole tone.
# E.G.: 

# is pythagorean tuning worth mentioning?

def chords(range):

	# note: standard 88 key piano range is A0 - C8
	note_name_prefixes = ['C','Cs','D','Ds','E','F','Fs','G','Gs','A','As','B']
	note_name_suffixes = ['-1','0','1','2','3','4','5','6','7','8','9']								

	note_names = combine_prefix_suffix(note_name_prefixes, note_name_suffixes, 'prefixes_first')

	# 0 C,, 		sub-contra octave C0		marks the low end of human hearing, only A0, B0 keys on piano
	# 1 C, 			contra octave C1
	#	2 C 			great octave	C2
	# 3 c 			small octave	C3
	# 4 c' 			1-line octave (middle c)						C4
	# 5 c" 			2-line octave (tenor c)							C5
	# 6 c"' 		3-line octave (soprano c (high c))	C6
	# 7 c"" 		4-line octave (double high c)				C7
	# 8 c""' 		5-line octave (eighth octave)				C8
		
	# Fundamental frequencies for -1 octave:
	#				C				Cs				D				Ds			E				F				Fs			G				Gs			A				As			B	
	cf_1 = [8.1758, 8.6620, 9.1770, 9.7227, 10.301, 10.914, 11.563, 12.250, 12.979, 13.750, 14.568, 15.434]
	
	# calculate all possible notes of chromatic scale given -1 octave frequencies
	all_notes = calc_all_notes(cf_1)

	notes_dict = dict(zip(note_names, all_notes))
	chord_name_prefixes = ['C','Cs','D','Ds','E','F','Fs','G','Gs','A','As','B']
	chord_name_suffixes = [' ','m','7','m7','maj7','6','m6','6/9','5','9','m9','maj9',
													'11','m11','13','m13','add9','add2','7-5','7+5','sus4','sus2',
													'dim','m7b5','aug'] 
	c_chord_name_prefixes = ['C']

	chord_names = combine_prefix_suffix(chord_name_prefixes, chord_name_suffixes, 'suffixes_first')	
	
	c_chord_names = combine_prefix_suffix(c_chord_name_prefixes, chord_name_suffixes, 'suffixes_first')
	print("Generated chord names for all possible chords of structure:\n")
	print(c_chord_names)

	# intervals in number of semitones
	# interval        semitones
	root 							= 0
	minor_second 			= 1
	major_second 			= 2
	minor_third 			= 3
	major_third 			= 4
	perfect_fourth 		= 5
	diminished_fifth 	= 6
	perfect_fifth 		= 7
	minor_sixth 			= 8
	major_sixth 			= 9
	minor_seventh 		= 10
	major_seventh 		= 11
	perfect_octave 		= 12
	minor_ninth 			= 13
	major_ninth 			= 14
	minor_tenth 			= 15
	major_tenth 			= 16
	eleventh 					= 17
	thirteenth 				= 21

	# chords
	i0 = [root, major_third, perfect_fifth]																											# C
	i1 = [root, minor_third, perfect_fifth]																											# Cm
	i2 = [root, major_third, perfect_fifth, minor_seventh]																			# C7
	i3 = [root, minor_third, perfect_fifth, minor_seventh]																			# Cm7
	i4 = [root, major_third, perfect_fifth, major_seventh]																			# Cmaj7
	i5 = [root, major_third, perfect_fifth, major_sixth]																				# C6
	i6 = [root, minor_third, perfect_fifth, major_sixth]																				# Cm6
	i7 = [root, major_third, perfect_fifth, major_sixth, major_ninth]														# C6/9 / C6add9
	i8 = [root, perfect_fifth]																																	# C5
	i9 = [root, major_third, perfect_fifth, minor_seventh, major_ninth]													# C9
	i10 = [root, minor_third, perfect_fifth, minor_seventh, major_ninth]												# Cm9
	i11 = [root, major_third, perfect_fifth, major_seventh, major_ninth]												# Cmaj9
	i12 = [root, major_third, perfect_fifth, minor_seventh, major_ninth, eleventh]							# C11
	i13 = [root, minor_third, perfect_fifth, minor_seventh, major_ninth, eleventh]							# Cm11
	i14 = [root, major_third, perfect_fifth, minor_seventh, major_ninth, eleventh, thirteenth]	# C13
	i15 = [root, minor_third, perfect_fifth, minor_seventh, major_ninth, eleventh, thirteenth]	# Cm13
	i16 = [root, major_third, perfect_fifth, major_ninth]																				# Cadd9
	i17 = [root, major_second, major_third, perfect_fifth]																			# Cadd2
	i18 = [root, major_third, diminished_fifth, minor_seventh]																	# C7-5
	i19 = [root, major_third, minor_sixth, minor_seventh]																				# C7+5
	i20 = [root, perfect_fourth, perfect_fifth]																									# Csus4
	i21 = [root, major_second, perfect_fifth]																										# Csus2
	i22 = [root, minor_third, diminished_fifth]																									# Cdim
	i23 = [root, minor_third, diminished_fifth, minor_seventh]																	# Cm7b5
	i24 = [root, major_third, minor_sixth]																											# Caug
	
	chord_intervals = [i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24]
	
	middle_c_chromatic = ['C4','Cs4','D4','Ds4','E4','F4','Fs4','G4','Gs4','A5','As5','B5']
	
	temp_chord_frequencies = []
	chord_frequencies= []
	root_note_c4 = 'C4'
	c_chord_frequencies = calc_chord_freqs(chord_names, chord_intervals, root_note_c4, notes_dict, all_notes)

	# populate chord_frequencies list with all frequencies for all notes from the first to seventh scale degree of middle c major
	
	# it looks like the issue may be here
	# will return a list: list[[c_chords], [cs_chords],.., [b_chords]]
	# where c_chords is a list, and each entry in c_chords is a list.  list of lists of lists
	for root_note in middle_c_chromatic:
		temp_chord_frequencies.append(calc_chord_freqs(chord_names, chord_intervals, root_note, notes_dict, all_notes))

	# need to flatten this list of lists of lists to a list of lists
	# for chords in list	(c_chords)
	for outer in temp_chord_frequencies:
		# for item in c_chords	(chord) in c_chords
		for inner in outer:
			chord_frequencies.append(inner)
	
	# scale degrees
	#root_note = 'C4'	# I
	#root_note = 'D4'	# II
	#root_note = 'E4'	# III
	#root_note = 'F4'	# IV
	#root_note = 'G4'	# V
	#root_note = 'A5'	# VI
	#root_note = 'B5' # VII
	#root_note = 'C5' # VIII

	c_chord_dict = dict(zip(c_chord_names, c_chord_frequencies))
	chord_dict = dict(zip(chord_names, chord_frequencies))
	if range == 'c': 
		return c_chord_dict
	if range == 'all':
		return chord_dict 

# pass in all chord names, intervals, the name of the root note, and the notes - freq dictionary
# return chord frequencies
def calc_chord_freqs(chord_names, chord_intervals, root_note, notes_dict, all_notes):
	chord_frequencies = []
	
	# determine the frequency of the root note
	root_note_freq = notes_dict[root_note]

	# find this frequency's position in the all_notes list
	pos = 0
	for i in all_notes: 
		if i == root_note_freq:
			break
		pos = pos + 1

	# take the position of the frequency in the all_notes list and calculate what frequencies
	# are present in the chord given the intervals present in the chord

	for chord in chord_intervals:
		# empty list for each chord
		chord_freq = []
		# for each note in each chord, determine the interval above the tonic note
		for interval in chord:	
			chord_freq.append(all_notes[pos + interval])
		chord_frequencies.append(chord_freq)

	# the chord_frequencies list should now contain a list of all frequencies present for each chord
	return chord_frequencies
 

def combine_prefix_suffix(prefixes, suffixes, order):
	combined = [];
	if order == 'prefixes_first':
		# iterate over all suffixes
		for suff in suffixes:
			# iterate over all prefixes
				for pre in prefixes:
					combined.append(pre+suff)
	
	if order == 'suffixes_first':
		for pre in prefixes:
			for suff in suffixes:
				combined.append(pre+suff)

	return combined


def calc_octave(input_pitch, num_octaves):
	freq = input_pitch * np.power(2,num_octaves)
	return freq

def calc_all_notes(input_scale):
	freq_arr=[]
	for i in range(0,len(input_scale)):
		for note in input_scale:
			freq_arr.append(calc_octave(note, float(i)))	
	return freq_arr

def main():
	# =============== DIATONIC==================

	# notes below piano sub-contra octave 
	# negative 1 octave (should be inaudible to humans)
	#do_1 = ['C-1', 'D-1', 'E-1', 'F-1', 'G-1', 'A-1', 'B-1']				# C-1
	
	# note: standard 88 key piano range is A0 - C8
																						# helmholtz name
	#do0 = ['C0','D0','E0','F0','G0','A0','B0']	# C,, 		sub-contra octave C0		marks the low end of human hearing, only A0, B0 keys on piano
	#do1 = ['C1','D1','E1','F1','G1','A1','B1']	# C, 			contra octave C1
	#do2 = ['C2','D2','E2','F2','G2','A2','B2']	#	C 			great octave	C2
	#do3 = ['C3','D3','E3','F3','G3','A3','B3']	# c 			small octave	C3
	#do4 = ['C4','D4','E4','F4','G4','A4','B4']	# c' 			1-line octave (middle c)						C4
	#do5 = ['C5','D5','E5','F5','G5','A5','B5']	# c" 			2-line octave (tenor c)							C5
	#do6 = ['C6','D6','E6','F6','G6','A6','B6']	# c"' 		3-line octave (soprano c (high c))	C6
	#do7 = ['C7','D7','E7','F7','G7','A7','B7']	# c"" 		4-line octave (double high c)				C7
	#do8 = ['C8','D8','E8','F8','G8','A8','B8']	# c""' 		5-line octave (eighth octave)				C8
	
	# notes above piano eighth octive
	#do9 = ['C9','D9','E9','F9','G9','A9','B9']												# C9
	#do10 = ['C10','D10','E10','F10','G10','A10','B10']								# C10
 	
	# Fundamental Frequencies
	# notes below piano sub-contra octave
	
	#				C					D				E				F				G				A				B
	df_1 = [8.1758, 9.1770, 10.301, 10.914, 12.250, 13.750, 15.434]
	all_diatonic_notes = calc_all_notes(df_1)
	
	diatonic_prefixes = ['C','D','E','F','G','A','B']
	diatonic_suffixes = ['-1','0','1','2','3','4','5','6','7','8','9','10']
	diatonic_note_names = combine_prefix_suffix(diatonic_prefixes, diatonic_suffixes, 'prefixes_first')

	# notes in the fourth octave
	diatonic_middle_c = all_diatonic_notes[34:44]
	diatonic_middle_c_names = diatonic_note_names[34:44]

	plt.plot(np.arange(len(diatonic_middle_c)), diatonic_middle_c,'-o')
	ax = plt.gca()
	ax.xaxis.set_ticks(np.arange(len(diatonic_middle_c_names)))
	ax.xaxis.set_ticklabels(diatonic_middle_c_names, rotation=90)

	plt.text(1.5, diatonic_middle_c[1], "T", fontsize=12)
	plt.text(2.5, diatonic_middle_c[2], "T", fontsize=12)
	plt.text(3.5, diatonic_middle_c[3], "S", fontsize=12)
	plt.text(4.5, diatonic_middle_c[4], "T", fontsize=12)
	plt.text(5.5, diatonic_middle_c[5], "T", fontsize=12)
	plt.text(6.5, diatonic_middle_c[6], "T", fontsize=12)
	plt.text(7.5, diatonic_middle_c[7], "S", fontsize=12)
	plt.xlabel("Notes")
	plt.ylabel("Frequency (hz)")	
	plt.title("Diatonic C Major Scale (Ionian Mode)")
	plt.grid()
	plt.show()

	plt.semilogy(np.arange(len(diatonic_middle_c)), diatonic_middle_c,'-o')
	ax = plt.gca()
	ax.xaxis.set_ticks(np.arange(len(diatonic_middle_c_names)))
	ax.xaxis.set_ticklabels(diatonic_middle_c_names, rotation=90)
	plt.xlabel("Notes")
	plt.ylabel("Frequency (logarithmic hz)")	
	plt.title("Diatonic C Major Scale")
	plt.grid()
	plt.show()


	#============= CHROMATIC ================
	
	# note: standard 88 key piano range is A0 - C8
	# for reference, notes will be structured:																																									# helmholtz name
	#co_1 =  ['C-1', 'Cs-1','D-1', 'Ds-1', 'E-1', 'F-1', 'Fs-1', 'G-1','Gs-1', 'A-1', 'As-1', 'B-1']
	#co0 = ['C0', 'Cs0','D0', 'Ds0', 'E0', 'F0', 'Fs0', 'G0','Gs0', 'A0', 'As0', 'B0']	# C,, 		sub-contra octave C0		marks the low end of human hearing, only A0, B0 keys on piano
	#co1 = ['C1', 'Cs1','D1', 'Ds1', 'E1', 'F1', 'Fs1', 'G1','Gs1', 'A1', 'As1', 'B1']	# C, 			contra octave C1
	#co2 = ['C2', 'Cs2','D2', 'Ds2', 'E2', 'F2', 'Fs2', 'G2','Gs2', 'A2', 'As2', 'B2']	#	C 			great octave	C2
	#co3 = ['C3', 'Cs3','D3', 'Ds3', 'E3', 'F3', 'Fs3', 'G3','Gs3', 'A3', 'As3', 'B3']	# c 			small octave	C3
	#co4 = ['C4', 'Cs4','D4', 'Ds4', 'E4', 'F4', 'Fs4', 'G4','Gs4', 'A4', 'As4', 'B4']	# c' 			1-line octave (middle c)						C4
	#co5 = ['C5', 'Cs5','D5', 'Ds5', 'E5', 'F5', 'Fs5', 'G5','Gs5', 'A5', 'As5', 'B5']	# c" 			2-line octave (tenor c)							C5
	#co6 = ['C6', 'Cs6','D6', 'Ds6', 'E6', 'F6', 'Fs6', 'G6','Gs6', 'A6', 'As6', 'B6']	# c"' 		3-line octave (soprano c (high c))	C6
	#co7 = ['C7', 'Cs7','D7', 'Ds7', 'E7', 'F7', 'Fs7', 'G7','Gs7', 'A7', 'As7', 'B7']	# c"" 		4-line octave (double high c)				C7
	#co8 = ['C8', 'Cs8','D8', 'Ds8', 'E8', 'F8', 'Fs8', 'G8','Gs8', 'A8', 'As8', 'B8']	# c""' 		5-line octave (eighth octave)				C8
	#co9=  ['C9', 'Cs9','D9', 'Ds9', 'E9', 'F9', 'Fs9', 'G9','Gs9', 'A9', 'As9', 'B9']

	#note_names = co_1 + co0 + co1 + co2 + co3 + co4 + co5 + co6 + co7 + co8 + co9 + c10		
	
	# Fundamental frequencies:
	#				C				Cs				D				Ds			E				F				Fs			G				Gs			A				As			B	
	cf_1 = [8.1758, 8.6620, 9.1770, 9.7227, 10.301, 10.914, 11.563, 12.250, 12.979, 13.750, 14.568, 15.434];
	
	all_notes = calc_all_notes(cf_1)

	
	chromatic_prefixes = ['C','Cs','D','Ds','E','F','Fs','G','Gs','A','As','B']
	chromatic_suffixes = ['-1','0','1','2','3','4','5','6','7','8','9','10']
	note_names = combine_prefix_suffix(chromatic_prefixes, chromatic_suffixes, 'prefixes_first')

	notes_dict = dict(zip(note_names, all_notes))
	middle_c = all_notes[59:73]
	middle_c_names = note_names[59:73]
	root = middle_c[0]	
	x = np.linspace(0,13,14)
	y = root*(np.power(2,x/12))

	plt.plot(np.arange(len(middle_c)), middle_c,'-o', markersize = 12)
	plt.plot(x,y,'go--')
	ax = plt.gca()
	ax.xaxis.set_ticks(np.arange(len(middle_c_names)))
	ax.xaxis.set_ticklabels(middle_c_names, rotation=90)
	plt.text(5, middle_c[11], "y = C4(2^(n/12))", fontsize=12)
	plt.xlabel("Notes")
	plt.ylabel("Frequency (hz)")	
	plt.title("Chromatic C4 Scale")
	plt.text(1.5, middle_c[1], "S", fontsize=12)
	plt.text(2.5, middle_c[2], "S", fontsize=12)
	plt.text(3.5, middle_c[3], "S", fontsize=12)
	plt.text(4.5, middle_c[4], "S", fontsize=12)
	plt.text(5.5, middle_c[5], "S", fontsize=12)
	plt.text(6.5, middle_c[6], "S", fontsize=12)
	plt.text(7.5, middle_c[7], "S", fontsize=12)
	plt.text(8.5, middle_c[8], "S", fontsize=12)
	plt.text(9.5, middle_c[9], "S", fontsize=12)
	plt.text(10.5, middle_c[10], "S", fontsize=12)
	plt.text(11.5, middle_c[11], "S", fontsize=12)
	plt.grid()
	plt.show()

	plt.figure()
	plt.plot(np.arange(len(middle_c)), middle_c,'-o')
	ax = plt.gca()
	ax.set_yscale('log')
	ax.set_yticks([200,300,400,500,600])
	ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
	ax.set_xticks(np.arange(len(middle_c_names)))
	ax.set_xticklabels(middle_c_names, rotation=90)
	plt.text(5, middle_c[11], "y = C4(2^(n/12))", fontsize=12)
	plt.xlabel("Notes")
	plt.ylabel("Frequency (logarithmic hz)")	
	plt.title("Chromatic C4 Scale (semi-log)")
	#plt.ylim([middle_c[0]*0.9, middle_c[len(middle_c)-1]*1.1])
	plt.ylim([200,600])

	plt.text(1.5, middle_c[0], "S", fontsize=12)
	plt.text(2.5, middle_c[1], "S", fontsize=12)
	plt.text(3.5, middle_c[2], "S", fontsize=12)
	plt.text(4.5, middle_c[3], "S", fontsize=12)
	plt.text(5.5, middle_c[4], "S", fontsize=12)
	plt.text(6.5, middle_c[5], "S", fontsize=12)
	plt.text(7.5, middle_c[6], "S", fontsize=12)
	plt.text(8.5, middle_c[7], "S", fontsize=12)
	plt.text(9.5, middle_c[8], "S", fontsize=12)
	plt.text(10.5, middle_c[9], "S", fontsize=12)
	plt.text(11.5, middle_c[10], "S", fontsize=12)
	plt.grid(True, which='both')
	plt.show()

	# to convert to wavelength 
	c = 34300 # (cm/s)
	#wavelength = c / all_notes; 

# formulaic representation of frequency of the nth key
#ff = 2^((n-49)/12) * 440 # (hz), key 49 being A4 (middle A))
	



	###### plot C major chords #######
	chords_dict = chords('c')

	plt.figure
	plt.hold(True)
	idx = 0
	for key, value in chords_dict.iteritems():
		for pitch in value:
			plt.scatter(idx, pitch)
		idx = idx + 1

	ax = plt.gca()
	ax.set_xticks(np.arange(len(chords_dict.keys())))
	ax.set_xticklabels(chords_dict.keys(), rotation=90)
	ax.set_yticks([250,300,350,400,450,500,550,600,650,700,750,800,850,900])
	plt.xlim([-1,(len(chords_dict.keys())+1)])
	ax.grid(True)
	plt.title('C Chord Frequencies')
	plt.ylabel('Frequency (hz)')
	plt.show()

	# plot with y ticks at every half step
	plt.figure
	plt.hold(True)
	idx = 0
	for key, value in chords_dict.iteritems():
		for pitch in value:
			plt.scatter(idx, pitch)
		idx = idx + 1

	c_chord_pitches = all_notes[60:82]
	ax = plt.gca()
	ax.set_xticks(np.arange(len(chords_dict.keys())))
	ax.set_xticklabels(chords_dict.keys(), rotation=90)
	ax.set_yticks(c_chord_pitches)
	plt.xlim([-1,(len(chords_dict.keys())+1)])
	ax.grid(True)
	plt.title('C Chord Frequencies')
	plt.ylabel('Frequency (hz)')
	plt.show()

	# plot with y ticks being interval numbers in semitones
	plt.figure
	plt.hold(True)
	idx = 0
	for key, value in chords_dict.iteritems():
		for pitch in value:
			plt.scatter(idx, pitch)
		idx = idx + 1

	c_chord_pitches = all_notes[60:82]
	ax = plt.gca()
	ax.set_xticks(np.arange(len(chords_dict.keys())))
	ax.set_xticklabels(chords_dict.keys(), rotation=90)
	ax.set_yticks(c_chord_pitches)
	ax.set_yticklabels(['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21'])
	plt.xlim([-1,(len(chords_dict.keys())+1)])
	ax.grid(True)
	plt.title('C Chord Intervals')
	plt.ylabel('Intervals (semitones)')
	plt.show()
	
	#c_chord_note_names = note_names[60:82]
	# finally, plot in terms of note name
	plt.figure
	plt.hold(True)
	idx = 0
	for key, value in chords_dict.iteritems():
		for pitch in value:
			plt.scatter(idx, pitch)
		idx = idx + 1

	chord_pitches = all_notes[60:83]
	chord_note_names = note_names[60:83]
	ax = plt.gca()
	ax.set_xticks(np.arange(len(chords_dict.keys())))
	ax.set_xticklabels(chords_dict.keys(), rotation=90)
	ax.set_yticks(chord_pitches)
	ax.set_yticklabels(chord_note_names)
	plt.xlim([-1,(len(chords_dict.keys())+1)])
	ax.grid(True)
	plt.title('C Chord Note Contents')
	plt.ylabel('Note Name')
	plt.show()

	# quick little plot to show frequency content of the i-v-vi-iv chord progression

	all_chords_dict = chords('all')
	four_chord_prog = ['C ','G ','Am','F ']

	plt.figure()
	plt.hold(True)
	idx = 0

	chord_pitches = all_notes[60:90]
	chord_note_names = note_names[60:90]

	for chord in four_chord_prog:
		tones = all_chords_dict[chord]
		for tone in tones:
			plt.scatter(idx, tone)
		idx = idx + 1
	ax = plt.gca()
	ax.set_xticks(np.arange(len(four_chord_prog)))
	ax.set_xticklabels(four_chord_prog, rotation=90)
	ax.set_yticks(chord_pitches)
  #ax.set_yticklabels(c_chord_note_names)
  #plt.xlim([-1,(len(chords_dict.keys())+1)])
	ax.grid(True)
	plt.title('I-V-VI-IV C major Chord Progression')
	plt.ylabel('Frequency (hz)')
	plt.show()


	plt.figure()
	plt.hold(True)
	idx = 0
	for chord in four_chord_prog:
		tones = all_chords_dict[chord]
		for tone in tones:
			plt.scatter(idx, tone)
		idx = idx + 1

	ax = plt.gca()
	ax.set_xticks(np.arange(len(four_chord_prog)))
	ax.set_xticklabels(four_chord_prog, rotation=90)
	ax.set_yticks(chord_pitches)
	ax.set_yticklabels(chord_note_names)
  #plt.xlim([-1,(len(chords_dict.keys())+1)])
	ax.grid(True)
	plt.title('I-V-VI-IV C major Chord Progression')
	plt.ylabel('Note Name')
	plt.show()




if __name__ == '__main__':
	main()
