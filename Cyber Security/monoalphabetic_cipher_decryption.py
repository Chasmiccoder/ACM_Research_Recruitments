"""
Cyber Security Task - 
We need to decrypt the following string:
ndgzixzgvtnozvydgtvbvdinooczrjjyviynojizjacdggcjpnzviyrcvozqzmrvgfzyoczmzrvgfzyvgjiz 

Decrypted Text:
_llenfelau_teadlluagaln_t the wood and _toneophlllhoy_e and whatever walked there walked alone

Given More time, we could have completely cracked it...
Key Cracked so far:
potential_key =  {'z': 'e', 'v': 'a', 'y': 'd', 'o': 't', 'g':'l',
'j': 'o', 'i': 'n', 'c': 'h', 'r': 'w', 'd': 'l', 't': 'u', 'm': 'r', 
'f': 'k', 'x': 'f', 'q': 'v', 'p': 'y', 'b': 'g', 'a': 'p'} 

"""

"""
---Solving the Problem ---
Given Information:
Cipher used = Monoalphabetic Cipher

In Caesar Cipher, the number of possible keys is = 26. (Easy to use brute force)
But in monoalphabetic cipher, we have 26! possible keys to the cipher ( 4 * 10^26 appx )
Therefore, we cannot use brute force attack to crack this encryption efficiently.

How monoalphabetic cipher works:
Letters: A B C D, ..., Z
Cipher : D F P Q, ..., K
No letter gets repeated.

Therefore, to break this code, we can use letter frequency analysis, based on
the most common letters and words used in English.
I am using the letter frequency statistics from this website:
https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html

Goto line 221 for Second Approach (which resulted in the answer)
"""

def find_frequency( cipher ):
    """
    Function takes a string (cipher) and then returns a dictionary such that the key corresponds 
    to the letter in the cipher, and its respective value corresponds to the letter's frequency.
    The dictionary returned is sorted in such a way that the letters are in descending order.
    """
    freq   = { }
    
    for i in cipher:
        if i not in freq.keys():
            freq[ i ] = 1
        else:
            freq[ i ] += 1

    count = list( freq.values( ) )
    letters = list( freq.keys( ) )

    letters = [ x for _,x in sorted( zip( count, letters ), reverse=True ) ]
    count.sort( reverse=True )

    freq = dict( zip( letters, count ) )
    
    return freq


def print_neighbourhood( cipher, letter ):
    """
    This function prints the neighbourhood of each occurrence of 'letter' in 'cipher'
    """
    for i in range( len(cipher) ):
        if cipher[ i ] == letter:
            print( cipher[i-3:i+4] )
    print( )

def good_guess( letters, freq ):
    """
    Creates a potential key in which most frequent letters in English are matched to 
    most frequent latters in cipher.
    """
    potential_key = { }
    cipher_letters = list( freq.keys( ) ) # Already in decreasing order of frequency
    
    for i in range( len( cipher_letters ) ):
        potential_key[ cipher_letters[ i ] ] = letters[ i ]
    
    return potential_key
        

def test_run_blank( cipher, key ):
    plain_text = ""
    for i in cipher:
        if i in key.keys( ):
            plain_text += key[ i ]
        else:
            plain_text += "_"
    
    return plain_text

cipher = "ndgzixzgvtnozvydgtvbvdinooczrjjyviynojizjacdggcjpnzviyrcvozqzmrvgfzyoczmzrvgfzyvgjiz"

print( "Cipher:\n", cipher )
print( )

# List of letters arranged in decreasing order of occurence in English
letters = [ 'e', 't', 'a', 'i', 'n', 'o', 's', 'h', 'r', 'd', 'l', 'u', 'c', 
            'm', 'f', 'w', 'y', 'g', 'p', 'b', 'v', 'k', 'q', 'j', 'x', 'z' ]

# Cipher letters that have been decrypted
letters_found = [ ]

# 'frequency' is a dictionary with frequency of each letter in the given cipher
#cipher = "ttestmessage"
frequency = find_frequency( cipher )
#print( "Frequency of each letter: " )
#print( frequency )
#print( )

"""
Output: 
{'z': 13, 'v': 10, 'g': 8, 'y': 6, 'o': 6, 'j': 6, 'i': 6, 'n': 5, 'c': 5, 
'r': 4, 'd': 4, 't': 2, 'm': 2, 'f': 2, 'x': 1, 'q': 1, 'p': 1, 'b': 1, 'a': 1}

Therefore, 'z' is the most common letter. 'z' could be 'e'.
The most letter at the end of a word is 'e'. 
Cipher ends with 'z' Therefore, 'z' has to be 'e' (most probably)

'v' could be 't'.
"""
potential_key = { } # Where our main guess will be happening
potential_key[ 'z' ] = 'e'
potential_key[ 'v' ] = 't'
letters_found.append( 'z' )
letters_found.append( 'v' )


"""
We need to analyse a sequence of letters for better understanding.

Trying to see if 'v' (potentially 't') is followed by similar letters
This is because the most occuring doublet in English is "th"
"""
#print( "Neighbourhood of 'v': " )
print_neighbourhood( cipher, 'v' )

"""
'v' is followed by t,y,b,d,i,i,o,g,g,g.

An instance of 'voz' is seen. Since 'v' is 't', and 'z' is 'e', 'o' has to be 'h'.
This is because 'the' is the most frequent triplet in English.

'vgf' is seen twice

'viy' is also seen twice. 
"""
potential_key[ 'o' ] = 'h'
letters_found.append( 'o' )

message = test_run_blank( cipher, potential_key ) # At this point we have 3 letters.
#print( "Test Run:\n", message )

"""
Frequency of 'g' is 8. Could be the letter 'a'.
"""

# Now, we will use function good_guess( ) to match frequencies
# new_potential_key is a temporary key for reference
new_potential_key = good_guess( letters, frequency )
#print( "Key generated by basic frequency match: " )
#print( new_potential_key )
#print( )

# Applying new_potential_key to cipher
plain_text = test_run_blank( cipher, new_potential_key )
#print( "Is this answer correct?\n" )
#print( plain_text )
#print( )

"""
hlaesfeatuhnetilautgtlshnnredooitsihnoseoprlaaroyhetsidrtnewecdtameinrecedtameitaose
       *                        *                          *         * *
What stands out here are the following words:
featu = feature
its = its
new = new
in = in
rece = recent

Now, we will attempt to incorporate these estimations
"""
word = cipher[5:15]
word_plain = plain_text[5:15]
#print( "In cipher          :", word )
#print( "Possible Plain Text:", word_plain )
#print( )

potential_key[ 'x' ] = 'f'
potential_key[ 'z' ] = 'e'
potential_key[ 'g' ] = 'a'
potential_key[ 'v' ] = 't'
potential_key[ 't' ] = 'u'

word = cipher[31:36]
word_plain = plain_text[31:36]
#print( "In cipher          :", word )
#print( "Possible Plain Text:", word_plain )
#print( )

potential_key[ 'y' ] = 'i'
potential_key[ 'i' ] = 's'

word = cipher[56:61]
word_plain = plain_text[56:61]
#print( "In cipher          :", word )
#print( "Possible Plain Text:", word_plain )
#print( )

potential_key[ 'o' ] = 'n'
potential_key[ 'q' ] = 'w' # This makes sense since 'q' come only once in cipher, and 'w' also rare.

word = cipher[67:77]
word_plain = plain_text[67:77]
#print( "In cipher          :", word )
#print( "Possible Plain Text:", word_plain )
#print( ) # The word is similar to 'recent' in which case 'r' is 'n'.

potential_key[ 'c' ] = 'r'
potential_key[ 'm' ] = 'c'
#potential_key[ 'r' ] = 'n'

# Conducting another trial run:
message = test_run_blank( cipher, potential_key )
#print( "Test Run 2: ", message )


"""
Approach 2
"""
potential_key = { }
cipher = "ndgzixzgvtnozvydgtvbvdinooczrjjyviynojizjacdggcjpnzviyrcvozqzmrvgfzyoczmzrvgfzyvgjiz"

letters = [ 'e', 't', 'a', 'i', 'n', 'o', 's', 'h', 'r', 'd', 'l', 'u', 'c', 
            'm', 'f', 'w', 'y', 'g', 'p', 'b', 'v', 'k', 'q', 'j', 'x', 'z' ]
        
cipher_frequency = find_frequency( cipher )

print( "Cipher Frequency:\n", cipher_frequency )
print( "\nLetter Frequency in English:\n", letters )

potential_key['z'] = 'e' 

"""
'v' is 't' did not give us any grouped words like 'th'.
Trying the next most frequent letter.
Taking 'v' as 'a'.
"""
potential_key[ 'v' ] = 'a'

doublets = { }
# Finding doublet frequency (to find "th")
for i in range( 0, len(cipher) ):
    if cipher[ i:i+2 ] not in doublets:
        doublets[ cipher[i:i+2] ] = 1
    else:
        doublets[ cipher[i:i+2] ] += 1
count = list( doublets.values( ) )
letters_ = list( doublets.keys( ) )

letters_ = [ x for _,x in sorted( zip( count, letters_ ), reverse=True ) ]
count.sort( reverse=True )

doublets = dict( zip( letters_, count ) )

# Finding triplet frequency (to find "th")
triplets = { }
for i in range( 0, len(cipher) ):
    if cipher[ i:i+3 ] not in triplets:
        triplets[ cipher[i:i+3] ] = 1
    else:
        triplets[ cipher[i:i+3] ] += 1
count = list( triplets.values( ) )
letters_ = list( triplets.keys( ) )

letters_ = [ x for _,x in sorted( zip( count, letters_ ), reverse=True ) ]
count.sort( reverse=True )

triplets = dict( zip( letters_, count ) )

print( )
print( "Doublets in cipher:\n", doublets )
print( )
print( "Triplets in cipher:\n", triplets )
print( )

"""
'v' cannot be 't' (as found in approach 1)

The following words can be 'the' ('z' is 'e')
ocz, jiz, gfz, pnz, voz, ixz, dgz ( with decreasing order of priority )
"""

# Taking 'ocz' as 'the':
potential_key[ 'o' ] = 't' 
potential_key[ 'c' ] = 'h'

"""
From doublets, 'gg' and 'oo' are repeating.
The most common double letters in English are: SS, EE, TT, FF, LL, MM, OO
This confirms that 'o' is 't'.
"""

frequency_based_key = good_guess( letters, cipher_frequency )
print( "Frequency Based Key: ", frequency_based_key )
print( )
print( "Potential Key: ", potential_key )

# Now we need to fuse these two:
"""
Frequency Based Key:  {'z': 'e', 'v': 't', 'g': 'a', 'y': 'i', 'o': 'n', 
'j': 'o', 'i': 's', 'n': 'h', 'c': 'r', 'r': 'd', 'd': 'l', 't': 'u', 'm': 'c', 
'f': 'm', 'x': 'f', 'q': 'w', 'p': 'y', 'b': 'g', 'a': 'p'}

Potential Key:  {'z': 'e', 'v': 'a', 'o': 't', 'c': 'h'}

"""
new_potential_key =  {'z': 'e', 'v': 'a', 'y': 'i', 'o': 't', 
'j': 'o', 'i': 's', 'n': 'h', 'c': 'h', 'r': 'd', 'd': 'l', 't': 'u', 'm': 'c', 
'f': 'm', 'x': 'f', 'q': 'w', 'p': 'y', 'b': 'g', 'a': 'p'} # new_potential_key[ 'g' ] = ??

print( )
plain_text = test_run_blank( cipher, new_potential_key )
print( "Plain Text using New Potential Key: \n", plain_text )

"""
Plain Text Generated:
hl_esfe_auhteail_uagalshtthedooiasihtoseophl__hoyheasidhatewecda_meitheceda_meia_ose
                          *                               *           *
Noted Words:
hate = hate
thece = there

Therefore, what gave us 'c' should have given us 'r'.
"""

new_potential_key =  {'z': 'e', 'v': 'a', 'y': 'i', 'o': 't', 
'j': 'o', 'i': 's', 'n': 'h', 'c': 'h', 'r': 'd', 'd': 'l', 't': 'u', 'm': 'r', 
'f': 'm', 'x': 'f', 'q': 'w', 'p': 'y', 'b': 'g', 'a': 'p'} # new_potential_key[ 'g' ] = ??

print( )
plain_text = test_run_blank( cipher, new_potential_key )
print( "Plain Text using New Potential Key: \n", plain_text )

"""
Plain Text Generated:
hl_esfe_auhteail_uagalshtthedooiasihtoseophl__hoyheasidhatewerda_meithereda_meia_ose
                                                      *******
Noted Word:
After changing 'c' to 'r', we get -
dhatewer = whatever

change 'd' to 'w'
change 'w' to 'v'
"""
new_potential_key =  {'z': 'e', 'v': 'a', 'y': 'i', 'o': 't', 
'j': 'o', 'i': 's', 'n': 'h', 'c': 'h', 'r': 'w', 'd': 'l', 't': 'u', 'm': 'r', 
'f': 'm', 'x': 'f', 'q': 'v', 'p': 'y', 'b': 'g', 'a': 'p'} # new_potential_key[ 'g' ] = ??

print( )
plain_text = test_run_blank( cipher, new_potential_key )
print( "Plain Text using New Potential Key: \n", plain_text )

"""
Plain Text: 
hl_esfe_auhteail_uagalshtthewooiasihtoseophl__hoyheasiwhateverwa_meitherewa_meia_ose
                             *
wooi = wood
also realised that both 'c' and 'n' are giving 'h'
"""
new_potential_key =  {'z': 'e', 'v': 'a', 'y': 'd', 'o': 't', 
'j': 'o', 'i': 's', 'c': 'h', 'r': 'w', 'd': 'l', 't': 'u', 'm': 'r', 
'f': 'm', 'x': 'f', 'q': 'v', 'p': 'y', 'b': 'g', 'a': 'p'} # new_potential_key[ 'g' ] = ??
                                                            # new_potential_key[ 'n' ] = ??

print( )
plain_text = test_run_blank( cipher, new_potential_key )
print( "Plain Text using New Potential Key: \n", plain_text )

"""
Plain Text:
hl_esfe_auhteadl_uagalsht the wood asdhtoseophl__hoyheasd whatever wa_med there wa_meda_ose
                                    *                                         
Trying 'asd' as 'and'
replacing 's' with 'n'
"""
new_potential_key =  {'z': 'e', 'v': 'a', 'y': 'd', 'o': 't', 
'j': 'o', 'i': 'n', 'c': 'h', 'r': 'w', 'd': 'l', 't': 'u', 'm': 'r', 
'f': 'm', 'x': 'f', 'q': 'v', 'p': 'y', 'b': 'g', 'a': 'p'} # new_potential_key[ 'g' ] = ??
                                                            # new_potential_key[ 'n' ] = ??


print( )
plain_text = test_run_blank( cipher, new_potential_key )
print( "Plain Text using New Potential Key: \n", plain_text )

"""
Plain Text:
_l_enfe_au_teadl_uagaln_t the wood and _toneophl__hoy_e and whatever wa_med there wa_meda_one

wa_med = walked
replacing '_' with 'l' and 'm' with 'k'
"""
new_potential_key =  {'z': 'e', 'v': 'a', 'y': 'd', 'o': 't', 'g':'l',
'j': 'o', 'i': 'n', 'c': 'h', 'r': 'w', 'd': 'l', 't': 'u', 'm': 'r', 
'f': 'k', 'x': 'f', 'q': 'v', 'p': 'y', 'b': 'g', 'a': 'p'} # new_potential_key[ 'n' ] = ??

print( )
plain_text = test_run_blank( cipher, new_potential_key )
print( "Plain Text using New Potential Key: \n", plain_text )

"""
Plain Text:
_llenfelau_teadlluagaln_t the wood and _toneophlllhoy_e and whatever walked there walked alone
"""