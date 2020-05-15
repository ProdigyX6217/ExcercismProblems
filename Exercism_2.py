"""Problem: 
    -Manage a High Score list.

    Your task is to write methods that return the highest score from the list,
    the last added score and the three highest scores.

    In this exercise, you're going to use and manipulate lists. Python lists are very versatile,
    and you'll find yourself using them again and again in problems both simple and complex.

        Data Structures (Python 3 Documentation Tutorial)
        Lists and Tuples in Python (Real Python)
        Python Lists (Google for Education)

    Example Input:
        - highest score:            highestscore(scores)
        - three highest scores:     top_3_scores(scores)
        - last added score:         last_added(scores)
        scores = [5, 1, 3, 6, 8, 2, 4, 7]

    Example Output:
        - highest score:            Highest score: [Name]:[score]
        - three highest scores:     Top 3 high scorers: 1st: [Name]:[score], 2nd: [Name]:[score], 3rd: [Name]:[score]
        - last added score:         Latest score: [Name]:[score]

-1 Restate the problem
    -Display 3 different options for highscore calls
        highest score, three highest scores, last added score
-2 Ask clarifying questions
    -
-3 State your assumptions
    -
-4 Think out loud
  -4a Brainstorm solutions
        - make an array and do linear or binary search to find the specified functions
        - use a dictionary to do a similar search 
        - use a binary tree to sort the highschores 
  -4b Explain your rationale
        - Array method would be naive but would work
        - Not fully sure on the Dictionary method
        - Though the benifits of a binary tree would be nice the complexity of setting it up for some of the functions might be a bit complex
  -4c Discuss tradeoffs
        - 
  -4d Suggest improvements
        -
"""

"""Pseudo Approach
    - Array approach, append elements to an array keeping track of size and what element was added last, use max function for highest score then remove it and call k more times (in our case k = 3)

    Edge Cases:
        -

    Complexity Check:
        After implementing some code go back through and revaluate its time and/or space complexity -- refractor/improve/find more edge cases -- repeat
"""

class Highscore:
    def __init__(self, scores):
        self.last_added = "Latest score: "
        self.scores = []
        self.size = 0
        for score in scores:
            self.add_highscore(score)
        print(self.scores)

    def add_highscore(self, score):
        self.scores.append(score)
        self.last_added = "Latest score: " + str(score)
        self.size += 1

    def highestscore(self):
        self.scores.sort()
        return "Highest score: [NAME]:" + str(max(self.scores))

    def _find_k_largest(self, array, k):   
        # overall Runtime: being k <= n,
        # O(n+k*(n+n)) -> O(n+2nk) -> O(n+nk), -> O(nk)
        """Given an array a of n numbers and a count k find the k largest values in the array a."""
        outputs = []                    # O(1)
        array = list(array)             # O(n) n being length/size of array
        for _ in range(k):              # O(k) number of largest numbers
            largest = max(array)        # O(n) m being size of new array
            outputs.append(largest)     # O(1)* to append to the end
            array.remove(largest)       # O(n)
        return outputs                  # O(1)

    def top_3_scores(self):
        print("Top 3 high scorers: ")
        for i, score in enumerate(self._find_k_largest(self.scores, 3)):
            print(i+1,":[Name]:[",score,"],")


if __name__ == "__main__":                              # RunTime:
    hs_1 = Highscore([7, 9, 1, 4, 6, 2, 5, 10])
    highest = hs_1.highestscore()
    print(highest)

    top_3 = hs_1.top_3_scores()
    
    ladded = hs_1.last_added
    print(ladded)

    print("\n--------\n")
    hs_2 = Highscore([80, 700, 150, 30, 400, 300, 10])
    highest = hs_2.highestscore()
    print(highest)

    top_3 = hs_2.top_3_scores()

    ladded = hs_2.last_added
    print(ladded)