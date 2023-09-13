class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        anagrams = []
        sorted_word = sorted(self.word.lower())
        
        for candidate in possible_anagrams:
            candidate_lower = candidate.lower()
            
            if candidate_lower != self.word.lower() and sorted(candidate_lower) == sorted_word:
                anagrams.append(candidate)

        return anagrams

# Example usage:
listen = Anagram("listen")
result = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(result)  # Output: ['inlets']
