from collections import deque


# Зберігає індекси кандидатів на максимум у порядку спадання значень.
def maxSlidingWindow(nums, k) -> list:
    if not 1 <= k <= len(nums):
        return []

    candidates = deque()
    maxima = []
    for index, value in enumerate(nums):
        if candidates and candidates[0] <= index - k:
            candidates.popleft()
        while candidates and nums[candidates[-1]] <= value:
            candidates.pop()
        candidates.append(index)

        if index >= k - 1:
            maxima.append(nums[candidates[0]])
    return maxima


if __name__ == "__main__":
    assert maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert maxSlidingWindow([1], 1) == [1]
    assert maxSlidingWindow([-3, -2, -5], 1) == [-3, -2, -5]
    assert maxSlidingWindow([-3, -2, -5], 3) == [-2]
    assert maxSlidingWindow([7, 7, 7, 1], 2) == [7, 7, 7]
    assert maxSlidingWindow([4, 3, 2, 1], 2) == [4, 3, 2]
    print("OK")
