"""Step Streaks — Starter

You are analyzing a user's daily step counts.
Implement without mutating inputs.
"""
from typing import List, Tuple


def max_window_sum(values: List[int], k: int) -> Tuple[int, int] | None:
    """Return (start_index, window_sum) of the largest sum among all length-k windows.

    If k <= 0, raise ValueError. If k > len(values), return None.
    """
    if k <= 0:
        raise ValueError("k must be > 0")
    n = len(values)
    if k > n:
        return None
    window_sum = sum(values[0:k])
    best_sum = window_sum
    best_start = 0
    for right in range(k, n):
        left = right - k
        window_sum += values[right] - values[left]
        if window_sum > best_sum:
            best_sum = window_sum
            best_start = left + 1
    return best_start, best_sum
    raise NotImplementedError


def count_goal_windows(values: List[int], k: int, target_avg: float) -> int:
    """Return how many length-k windows have average >= target_avg.

    If k <= 0, raise ValueError. If k > len(values), return 0.
    """
    if k <= 0:
        raise ValueError("k must be > 0")
    n = len(values)
    if k > n:
        return 0
    threshold = target_avg * k
    count = 0
    window_sum = sum(values[0:k])
    if window_sum >= threshold:
        count += 1
    for right in range(k, n):
        left = right - k
        window_sum += values[right] - values[left]
        if window_sum >= threshold:
            count += 1
    return count
    raise NotImplementedError


def longest_rising_streak(values: List[int]) -> int:
    """Return the length of the longest strictly increasing consecutive streak.

    Empty list -> 0. Single element -> 1.
    """
    n = len(values)
    if n == 0:
        return 0
    best = 1
    cur = 1
    for i in range(1, n):
        if values[i] > values[i - 1]:
            cur += 1
        else:
            if cur > best:
                best = cur
            cur = 1
    if cur > best:
        best = cur
    return best
    raise NotImplementedError