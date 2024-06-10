def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

word = input()
vowel_count = count_vowels(word)
print(f"{word} - {vowel_count} has vowels")
