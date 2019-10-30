from collections import Counter
import re
def retrieveMostFrequentlyUsedWords(literatureText, wordsToExclude):
    literatureText = literatureText.lower()
    expected = []
    for value in wordsToExclude:
        expected.append(value.lower())
    literatureText = re.sub("[^\w\s]", " ", literatureText)
    reducedText = filter(lambda x: x not in expected, literatureText.split())
    counter = Counter(list(reducedText))
    sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse= True)
    ans = []
    if len(sorted_counter) > 0:
        prev_freq = sorted_counter[0][1]
        for value, freq in sorted_counter:
            if freq == prev_freq:
                ans.append(value)
    return ans

print(retrieveMostFrequentlyUsedWords(",;'    ", [" ", "jill"]))