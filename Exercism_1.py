"""Problem: 
    - Given a phrase, count the occurrences of each word in that phrase.

    Example Input:
        - For example, for the phrase:
            "That's the password: 'PASSWORD 123'!", cried the Special Agent.\nSo I fled. 

    Example Output:
        - The count would be:
            that's: 1, the: 2, password: 2, 123: 1, cried: 1, special: 1, agent: 1, so: 1, i: 1, fled: 1

-1 Restate the problem
    - make a histogram of the occurrences of each word in a phrase
-2 Ask clarifying questions
    -
-3 State your assumptions
    - For the purposes of this exercise you can expect that a word will always be one of:
        A number composed of one or more ASCII digits (ie "0" or "1234") OR
        A simple word composed of one or more ASCII letters (ie "a" or "they") OR
        A contraction of two simple words joined by a single apostrophe (ie "it's" or "they're")
        When counting words you can assume the following rules:

        The count is case insensitive (ie "You", "you", and "YOU" are 3 uses of the same word)
        The count is unordered; the tests will ignore how words and counts are ordered
        Other than the apostrophe in a contraction all forms of punctuation are ignored
        The words can be separated by any form of whitespace (ie "\t", "\n", " ")

-4 Think out loud
  -4a Brainstorm solutions
        - make a dictionary/histogram table of each elements occurrence
        first we will need to parse the string provided so that it fits all the requirements/assumptions
  -4b Explain your rationale
        - with out it parsed properly it may find weird word differences do to computers being super specific
  -4c Discuss tradeoffs
        -
  -4d Suggest improvements
        -
"""

"""Pseudo Approach
    - first we will need to parse the string provided so that it fits all the requirements/assumptions
      then make a dictionary/histogram table of each elements occurrence

    Edge Cases:
        -

    Complexity Check:
        After implementing some code go back through and revaluate its time and/or space complexity -- refractor/improve/find more edge cases -- repeat
"""
import re

def parse(phrase):
    words = []
    for word in phrase.lower().split():
        word = re.sub('[,()]!?', '', word)
        word = re.sub('--', ' ', word)
        word = re.sub('\'', '', word)
        word = re.sub('\"', '', word)
        word = re.sub('\\n', '', word)
        words.append(word)
    return words


def histo(array):
    # Runtime: O(n+n)
    hist = {}
    for element in array:
        hist[element] = hist.get(element, 0) + 1
    return hist


if __name__ == "__main__":                              # RunTime:
    phrase = "That\'s the password: 'PASSWORD 123\'!\", cried the Special Agent.\\nSo I fled."
    print(phrase)
    
    parsed_phrase = parse(phrase)
    print(parsed_phrase)
    
    counts = histo(parsed_phrase)
    print(counts)

    print("\n------\n")

    phrase = "Read command--line arguments and test string searching algorithms."
    print(phrase)

    parsed_phrase = parse(phrase)
    print(parsed_phrase)

    counts = histo(parsed_phrase)
    print(counts)
