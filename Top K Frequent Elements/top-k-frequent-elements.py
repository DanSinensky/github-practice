from collections import Counter

def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    result = []

    count = Counter(nums)
    sorted_counts = sorted(count.items(), key=lambda x: x[1], reverse = True)
        
    for i in range(0, k):
        result.append(sorted_counts[i][0])

    return result