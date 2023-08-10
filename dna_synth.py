#!/usr/bin/env python3

import tomita.legacy.pysynth as ps

# nucleotides assigned to notes
C = ('c', 4)
T = ('d', 4)
G = ('g', 4)
A = ('a', 4)

# genetic code dictionaries
codon_aa_dict = {    
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A', 
    'TGC': 'C', 'TGT': 'C', 
    'GAC': 'D', 'GAT': 'D', 
    'GAA': 'E', 'GAG': 'E', 
    'TTC': 'F', 'TTT': 'F', 
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G', 
    'CAC': 'H', 'CAT': 'H', 
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 
    'AAA': 'K', 'AAG': 'K', 
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L', 'TTA': 'L', 'TTG': 'L', 
    'ATG': 'M', 
    'AAC': 'N', 'AAT': 'N', 
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P', 
    'CAA': 'Q', 'CAG': 'Q', 
    'AGA': 'R', 'AGG': 'R', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R', 
    'AGC': 'S', 'AGT': 'S', 'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S', 
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T', 
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V', 
    'TGG': 'W', 
    'TAC': 'Y', 'TAT': 'Y', 
    'TAA': '*', 'TAG': '*', 'TGA': '*'
    }

aa_codon_dict = {
    'A': ['GCT', 'GCC', 'GCA', 'GCG'], 
    'C': ['TGT', 'TGC'], 
    'D': ['GAT', 'GAC'], 
    'E': ['GAA', 'GAG'], 
    'F': ['TTT', 'TTC'], 
    'G': ['GGT', 'GGC', 'GGA', 'GGG'], 
    'H': ['CAT', 'CAC'], 
    'I': ['ATA', 'ATC', 'ATT'], 
    'K': ['AAA', 'AAG'], 
    'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'], 
    'M': ['ATG'], 
    'N': ['AAT', 'AAC'],
    'P': ['CCC', 'CCG', 'CCT', 'CCA'], 
    'Q': ['CAA', 'CAG'], 
    'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 
    'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'], 
    'T': ['ACT', 'ACC', 'ACA', 'ACG'], 
    'V': ['GTT', 'GTC', 'GTA', 'GTG'], 
    'W': ['TGG'], 'P': ['CCT', 'CCC', 'CCA', 'CCG'], 
    'Y': ['TAT', 'TAC'], 'I': ['ATT', 'ATC', 'ATA'], 
    '*': ['TAA', 'TAG', 'TGA']
    }

aa_codes_dict = {'Ala':'A', 'Cys':'C', 'Asp':'D', 'Glu':'E', 'Phe':'F', 'Gly':'G', 'His':'H', 'Ile':'I', 'Lys':'K', 'Leu':'L', 'Met':'M', 'Asn':'N', 'Pro':'P', 'Gln':'Q', 'Arg':'R', 'Ser':'S', 'Thr':'T', 'Val':'V', 'Trp':'W', 'Tyr':'Y'}

# codons assigned to notes
##TAG = ('c', 4)

# amino acids assigned to notes

''' (note, duration)
Note name (a to g), then optionally a '#' for sharp or
'b' for flat, then optionally the octave (defaults to 4).
An asterisk at the end means to play the note a little 
louder.  Duration: 4 is a quarter note, -4 is a dotted 
quarter note, etc.'''

aa_dict = {
    'A': ('a', 4), 
    'C': ('c', 4), 
    'D': ('d', 4), 
    'E': ('e', 4), 
    'F': ('f', 4), 
    'G': ('g', 4), 
    'H': ('b', 4),
    'I': ('c5', 4),  
    'K': ('d5', 4), 
    'L': ('e5', 4), 
    'M': ('f5', 4), 
    'N': ('g5', 4),
    'P': ('a5', 4),  
    'Q': ('b5', 4), 
    'R': ('c3', 4), 
    'S': ('d3', 4), 
    'T': ('e3', 4), 
    'V': ('f3', 4), 
    'W': ('g3', 4), 
    'Y': ('a3', 4), 
    '*': ('c6*', 1)
    }

# input string
nt_string = (A, C, G, A, C, T, T)
codon_string = ()
aa_string = 'DIIVDRLGVDADKVTEDASFKDDLGADSLDIAELVMELEDEFGTEIPDEEAEKINTVGDAVKFIN*'

# convert string to music
song = []
for aa in list(aa_string):
    note = aa_dict[aa]
    song.append(note)

# create .wav audio file from string
ps.make_wav(song, fn = "song.wav", bpm = 350)