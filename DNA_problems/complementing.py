#!/usr/bin/env python3

s = 'TTTCATGATGCAAAAAGCCCGGTGTCAACCGGTGGAACCTCCAATCTCGATCGAGCAATCCTAATGGACTTAGCGCAAGCGAAGCACCCGTAAGCCTGATCACCTACACAACAGGTGGATTTGTTTGGAGAGATGTGATGTCAGGTTGGCTGATCAACTAAGAATACACCATCCTGCTCAGCTCGCAAGTTTGAACACCGCGGACAGCTCAGGAAGTTGGGTAGGTTAGTCGTCCGGGGATAGACGTTCGGTGGGATACGACTGAGAGGTGTATAGGACTGAAGCGTTCGGAAGGCGTTTGCAGCCTTAGTCCAACATCAATCGACTACAGACACGAGTTGGATTCGGAGGTCTCGTGGACTTTTTTGAAGAGACTAATAACAGTCGATCGACCTAGCATGAGCGGTCTAGGTCATGAAATACTCGTTGATCGACAGACGGACCAAATAACTTGAACGTATAGTTGGTGTCGGGAGGTTGTGCGTGACAGACGATAAGTAACGGCCGCTGGGGTACCCCGGCGCTACGAAATAGAAAAGCGGCGTGAGTTTTTGGTCAGGTGACAGGACCCATTACGAAACCCCTCACTCCTCTATATACATCTATATGCCACTGTATGTGCGACTCCCAACTTACAGACGGCTTATTCAGTCCAGCAGTGTCTTCGCTGTATTTCCATTTTGCCTAACCGGCCCTTTGCTCGGGAACACACGCGATCACCGCGTACCAGTGCATGTGCCGAGAGAATGGCAGATCTGGCGTCAGGCAATTTGACACCGGGCAAAGGTGCCATTGCAAAATCGTCTCCCCTTTTCTGCGCCCGTTTAGGATTACCAGCAGCGTAGTACTGCTAGTAACAACTACACAAGATCATGCACGCTGACGGTTGCCGGAAACTTCGTCAGAAAAGGTTCCGTGCGTCGCGACCTTGAGATTGCGCCTTGCTTGCCAGCACTACTGTGCCGGTGGGT'[::-1]

mapping_table = str.maketrans({'A':'T','T':'A','G':'C','C':'G'})

rc = s.translate(mapping_table)

print(rc)
