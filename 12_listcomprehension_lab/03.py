"""
Find and print all possible sequences
of 3 lowercase characters: aaa, aab, aac, ..., zzz
"""

english_letters = [chr(letter) for letter in range(ord("a"),ord("z") + 1)]
combinations = [x + y + z for x in english_letters for y in english_letters for z in english_letters]

print combinations
