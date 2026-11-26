from collections import deque


# Обчислює найкращу суму до кожного індексу, беручи максимум із черги.
def constrainedSubsetSum(nums, k) -> int:
    candidates = deque()
    best = nums[0]
    for index, value in enumerate(nums):
        if candidates and candidates[0][0] < index - k:
            candidates.popleft()

        score = value
        if candidates:
            score += candidates[0][1]
        best = max(best, score)

        # Недодатну суму вигідніше замінити початком нової підпослідовності.
        if score > 0:
            while candidates and candidates[-1][1] <= score:
                candidates.pop()
            candidates.append((index, score))
    return best


if __name__ == "__main__":
    assert constrainedSubsetSum([10, 2, -10, 5, 20], 2) == 37
    assert constrainedSubsetSum([-1, -2, -3], 1) == -1
    assert constrainedSubsetSum([10, -2, -10, -5, 20], 2) == 23
    assert constrainedSubsetSum([-5], 1) == -5
    assert constrainedSubsetSum([0, 0, 0], 2) == 0
    assert constrainedSubsetSum([4, -10, 4], 1) == 4
    assert constrainedSubsetSum([4, -10, 4], 2) == 8
    print("OK")
