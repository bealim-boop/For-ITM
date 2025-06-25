#!/usr/bin/env python
# coding: utf-8

# In[2]:


def shift_letter(letter, shift):
    if letter == " ":
        return " "
   
    else:
        orig = ord(letter)- ord("A")
        shifted = (orig + shift)%26
        return chr(shifted+ord("A"))


# In[49]:


print(shift_letter("Z", 5))


# In[53]:


# 2 For every letter, add the shift number to its ordinal value, then convert it back to a letter.
def caesar_cipher(message, shift):
    changed = ""

    for letter in message:
        if letter == " ":
            changed += " "
        else:
            changed += chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
    return(changed)
print(caesar_cipher("BEA", 1))


# In[48]:


def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
   
    else:
        main = ord(letter)- ord("A")
        oks = (main + (ord(letter_shift)- ord("A")))%26
        return chr(oks+ord("A"))
print (shift_by_letter("Z", "C"))


# In[60]:


def vigenere_cipher(message, key):
    encrypted = []
    key_index = 0
    key_length = len(key)
    
    for char in message:
        if char == ' ':
            encrypted.append(char)
            key_index += 1
        else:
            # Calculate shift
            key_char = key[key_index % key_length]
            shift = ord(key_char) - ord('A')
            
            # Shifting
            original_pos = ord(char) - ord('A')
            new_pos = (original_pos + shift) % 26
            new_char = chr(new_pos + ord('A'))
            encrypted.append(new_char)
            
            key_index += 1
    
    return ''.join(encrypted)


# In[61]:


print(vigenere_cipher("A C", "KEY"))


# In[64]:


def scytale_cipher(message, shift):
    # Adjust the message length to be a multiple of shift
    original_length = len(message)
    if original_length % shift != 0:
        padding_length = shift - (original_length % shift)
        message += '_' * padding_length
    
    # Cipher the message
    encoded_message = []
    n = len(message)
    group_size = n // shift
    for i in range(n):
        pos = (i // shift) + group_size * (i % shift)
        encoded_message.append(message[pos])
    
    return ''.join(encoded_message)

print(scytale_cipher("INFORMATION_AGE", 3))


# In[66]:


def scytale_decipher(message, shift):
    n = len(message)
    group_size = n // shift
    
    decoded_message = [''] * n
    
    for i in range(n):
        # Calculate the position in the encrypted message
        pos = (i % group_size) * shift + (i // group_size)
        decoded_message[i] = message[pos]
    
    return ''.join(decoded_message)
    
print(scytale_decipher("IMNNA_FTAOIGROE", 3))


# In[ ]:




