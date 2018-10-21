# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 21:08:12 2018

@author: Daniel
"""

import collections

cipher_location = 'path to file'
eng_freq = 'path to file'

# load the files
cipher = open(cipher_location, 'r').read()
english = open(eng_freq, 'r').read()

# change the fequencies into a dictionary
eng_dict = {}
total = 0
listy = english.split()
characters = listy[0::2]
counts = listy[1::2]
for i in range(len(characters)):
    eng_dict[characters[i].lower()] = int(counts[i])
    total+=int(counts[i])
    
# get the %
for i in eng_dict:
    eng_dict[i] = (float(eng_dict[i])/float(total))*100
    

# clean the cipher text of numbers, new lines and spaces
cipher_clean = ''
for i in cipher:
    if i==' ' or i=='\n' or i.isnumeric():
        pass
    else:
        cipher_clean+=i

# get the character frequencies of the cipher text
cipher_count = collections.Counter(cipher_clean)

# check the characters present
for i in cipher_count:
    print('|' + str(i) + '|', cipher_count[i])

# get the frequencies of the values
cipher_tot = sum(cipher_count.values())
for i in cipher_count:
    print(i + str(':'), (float(cipher_count[i])/float(cipher_tot))*100)
    
# character replacement
translated_cipher = cipher_clean

# switch characters
j=0
common = cipher_count.most_common()
log = {}
for i in eng_dict.keys():
    print(common[j][0], i)
    translated_cipher = translated_cipher.replace(common[j][0], i)
    log[i] = translated_cipher
    j+=1
 
##############################################################################
    # do this looking at bigrams - might be more helpful
bigrams = open('path to file', 'r').read()
# change the fequencies into a dictionary
eng_bigrams = {}
total = 0
listy = bigrams.split()
characters = listy[0::2]
counts = listy[1::2]
for i in range(len(characters)):
    eng_bigrams[characters[i].lower()] = int(counts[i])
    total+=int(counts[i])
    
# all combinations of two characters in order
entire_set = {}

for i in range(len(translated_cipher)):
    # if not at end
    if not (i+1==len(translated_cipher)):
        sample = translated_cipher[i] + translated_cipher[i+1]
        # if not found previously, set
        if sample not in entire_set:
            entire_set[sample] = 1
        else:
            # increment pressence
            entire_set[sample] = entire_set[sample]+1
    else:
        break

# listy sum
the_sum = 0
listy_sum = listy[1::2]
for i in listy_sum:
    the_sum += int(i)

# listy bigram freq
for i in eng_bigrams:
    eng_bigrams[i] = (float(eng_bigrams[i])/float(the_sum)) * 100

# turn numbers into %
trans_c_tot = len(translated_cipher)
for i in entire_set:
    entire_set[i] = (float(entire_set[i])/float(trans_c_tot)) * 100
    
    
# character replacement
translated_cipher = cipher_clean

translated_cipher = translated_cipher.replace(']M', 'in')

translated_cipher = translated_cipher.replace('<T', 'er')

translated_cipher = translated_cipher.replace('in', ']M')

translated_cipher = translated_cipher.replace('er', '<T')

translated_cipher = translated_cipher.replace(']', 'e')

translated_cipher = translated_cipher.replace('(', 'h')

translated_cipher = translated_cipher.replace('O', 't')

translated_cipher = translated_cipher.replace('M', 'n')

translated_cipher = translated_cipher.replace('T', 's')

translated_cipher = translated_cipher.replace('S', 'x')

translated_cipher = translated_cipher.replace('S', 'x')

translated_cipher = translated_cipher.replace('x', 'S')

translated_cipher = translated_cipher.replace('S', 'a')

translated_cipher = translated_cipher.replace('n', 'r')

translated_cipher = translated_cipher.replace('a', 'S')

translated_cipher = translated_cipher.replace('a', 'S')

translated_cipher = translated_cipher.replace('~', 'a')

translated_cipher = translated_cipher.replace('~', 'a')

translated_cipher = translated_cipher.replace('L', 'p')

translated_cipher = translated_cipher.replace('H', 'o')

translated_cipher = translated_cipher.replace('{', 'j')

translated_cipher = translated_cipher.replace('£', 'c')

translated_cipher = translated_cipher.replace('X', 'y')

translated_cipher = translated_cipher.replace('<', 'i')

translated_cipher = translated_cipher.replace('%', 'g')

translated_cipher = translated_cipher.replace('C', 'l')

translated_cipher = translated_cipher.replace('R', 'u')

translated_cipher = translated_cipher.replace('s', 'n')

translated_cipher = translated_cipher.replace('*', 'd')

translated_cipher = translated_cipher.replace('U', 'w')

translated_cipher = translated_cipher.replace('A', 'm')

translated_cipher = translated_cipher.replace('|', 'b')

translated_cipher = translated_cipher.replace('S', 's')

translated_cipher = translated_cipher.replace('E', 'c')

translated_cipher = translated_cipher.replace('?', 'f')

translated_cipher = translated_cipher.replace('{', 'z')

translated_cipher = translated_cipher.replace('[', 'z')

translated_cipher = translated_cipher.replace('>', 'k')

translated_cipher = translated_cipher.replace('Z', 'x')

translated_cipher = translated_cipher.replace('I', 'xq')

translated_cipher = translated_cipher.replace('xq', 'q')
