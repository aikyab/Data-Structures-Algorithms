class MyString:
    def __init__(self, word):
        self.word = word

    def __lt__(self, other):
        return self.word > other.word

count = {}
k=3
words_1 = ["i","love","leetcode","i","love","coding"]
for word in words_1:
    count[word] = count.get(word, 0) + 1

heap = []
for word, ct in count.items():
    heapq.heappush(heap, (ct, MyString(word)))
    if len(heap) > k:
        heapq.heappop(heap)

results = []
for i in range(k):
    word_tuple = heapq.heappop(heap)
    results.append(word_tuple[1].word)
results.reverse()
print(results)
