def majority_vote(arr):
    results = {i : arr.count(i) for i in set(arr)}
    return max(results, key=results.get)

print(majority_vote(["A", "A", "A", "B", "C", "A"]))