# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()
def counting_vowels_and_consonants(text): 
    vowels = "aeiouAEIOU"
    vowelcount = 0 
    consonantcount = 0 
    for character in text: 
        if character.isalpha(): 
            if character in vowels: 
                vowelcount += 1 
            else: 
                consonantcount += 1 
    return (vowelcount, consonantcount)


# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()
def average_vowels_and_consonants(paragraph): 
    cleanparagraph = paragraph.replace("!", ".")
    rawsentences = cleanparagraph.split(".") 
    
    sentences = []
    for s in rawsentences: 
        stripped = s.strip() 
        if stripped != "": 
            sentences.append(stripped) 
            numberofsentences = len(sentences) 

            totalvowels = 0
            totalconsonants = 0 
    for sentence in sentences: 
                vcount, ccount = counting_vowels_and_consonants(sentence) 

                totalvowels += vcount 
                totalconsonants += ccount 
                avgvowels = totalvowels / numberofsentences 
                avgconsonants = totalconsonants / numberofsentences
    return (numberofsentences, avgvowels, avgconsonants) 

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 
numberofsentences, avgvowels, avgconsonants = average_vowels_and_consonants(paragraph) 

print(f"The paragraph contains a total of {numberofsentences} sentences.")
print(f"On average, each sentence has {avgvowels:.0f} vowels.")
print(f"On average, each sentence has {avgconsonants:.0f} consonants.")
