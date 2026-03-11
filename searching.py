import math


def _step(arr, highlights=None, description="", comparisons=0, swaps=0):
    return {
        "array": arr[:],
        "highlights": highlights or {},
        "description": description,
        "comparisons": comparisons,
        "swaps": swaps,
    }


# ─── Linear Search ───────────────────────────────────────────────────────────
def linear_search_steps(arr, target):
    steps = []
    n = len(arr)
    steps.append(_step(arr, {}, f"Starting linear search for target = {target}"))
    for i in range(n):
        hl = {i: "#f59e0b"}
        steps.append(_step(arr, hl, f"Checking index {i}: arr[{i}] = {arr[i]}", comparisons=1))
        if arr[i] == target:
            hl2 = {i: "#06b6d4"}
            steps.append(_step(arr, hl2, f"🎯 Found {target} at index {i}!"))
            return steps
        else:
            hl3 = {j: "#2d2d4a" for j in range(i+1)}
            steps.append(_step(arr, hl3, f"{arr[i]} ≠ {target} — moving on"))
    steps.append(_step(arr, {}, f"❌ {target} not found in array"))
    return steps


# ─── Binary Search ────────────────────────────────────────────────────────────
def binary_search_steps(arr, target):
    steps = []
    low, high = 0, len(arr) - 1
    steps.append(_step(arr, {i: "#8b5cf6" for i in range(len(arr))},
                        f"Starting binary search for {target} — array must be sorted"))
    while low <= high:
        mid = (low + high) // 2
        hl = {i: "#8b5cf6" for i in range(low, high+1)}
        hl[mid] = "#f59e0b"
        steps.append(_step(arr, hl, f"Range [{low},{high}] — checking mid = {mid} (value {arr[mid]})", comparisons=1))
        if arr[mid] == target:
            hl2 = {mid: "#06b6d4"}
            steps.append(_step(arr, hl2, f"🎯 Found {target} at index {mid}!"))
            return steps
        elif arr[mid] < target:
            hl3 = {i: "#2d2d4a" for i in range(low, mid+1)}
            hl3.update({i: "#8b5cf6" for i in range(mid+1, high+1)})
            steps.append(_step(arr, hl3, f"{arr[mid]} < {target} — searching right half [{mid+1},{high}]"))
            low = mid + 1
        else:
            hl3 = {i: "#2d2d4a" for i in range(mid, high+1)}
            hl3.update({i: "#8b5cf6" for i in range(low, mid)})
            steps.append(_step(arr, hl3, f"{arr[mid]} > {target} — searching left half [{low},{mid-1}]"))
            high = mid - 1
    steps.append(_step(arr, {}, f"❌ {target} not found in array"))
    return steps


# ─── Jump Search ──────────────────────────────────────────────────────────────
def jump_search_steps(arr, target):
    steps = []
    n = len(arr)
    step = int(math.sqrt(n))
    steps.append(_step(arr, {}, f"Jump search for {target} — jump step = √{n} ≈ {step}"))
    prev = 0
    while prev < n and arr[min(step, n)-1] < target:
        block_end = min(step, n) - 1
        hl = {i: "#8b5cf6" for i in range(prev, min(step, n))}
        hl[block_end] = "#f59e0b"
        steps.append(_step(arr, hl, f"Block [{prev},{block_end}]: arr[{block_end}]={arr[block_end]} < {target} — jump!", comparisons=1))
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            steps.append(_step(arr, {}, f"❌ {target} not found"))
            return steps
    hl2 = {i: "#8b5cf6" for i in range(prev, min(step, n))}
    steps.append(_step(arr, hl2, f"Found block [{prev},{min(step,n)-1}] — doing linear search"))
    for i in range(prev, min(step, n)):
        hl3 = {j: "#8b5cf6" for j in range(prev, min(step, n))}
        hl3[i] = "#f59e0b"
        steps.append(_step(arr, hl3, f"Checking index {i}: arr[{i}] = {arr[i]}", comparisons=1))
        if arr[i] == target:
            hl4 = {i: "#06b6d4"}
            steps.append(_step(arr, hl4, f"🎯 Found {target} at index {i}!"))
            return steps
    steps.append(_step(arr, {}, f"❌ {target} not found"))
    return steps


# ─── Exponential Search ───────────────────────────────────────────────────────
def exponential_search_steps(arr, target):
    steps = []
    n = len(arr)
    if arr[0] == target:
        steps.append(_step(arr, {0: "#06b6d4"}, f"🎯 Found {target} at index 0!"))
        return steps
    i = 1
    steps.append(_step(arr, {}, f"Exponential search for {target} — doubling bound"))
    while i < n and arr[i] <= target:
        hl = {j: "#8b5cf6" for j in range(i//2, i+1)}
        hl[i] = "#f59e0b"
        steps.append(_step(arr, hl, f"arr[{i}] = {arr[i]} ≤ {target} — doubling i to {i*2}", comparisons=1))
        i *= 2
    low  = i // 2
    high = min(i, n-1)
    hl2 = {j: "#8b5cf6" for j in range(low, high+1)}
    steps.append(_step(arr, hl2, f"Binary search in range [{low},{high}]"))
    while low <= high:
        mid = (low + high) // 2
        hl3 = {j: "#8b5cf6" for j in range(low, high+1)}
        hl3[mid] = "#f59e0b"
        steps.append(_step(arr, hl3, f"Mid = {mid}, arr[{mid}] = {arr[mid]}", comparisons=1))
        if arr[mid] == target:
            hl4 = {mid: "#06b6d4"}
            steps.append(_step(arr, hl4, f"🎯 Found {target} at index {mid}!"))
            return steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    steps.append(_step(arr, {}, f"❌ {target} not found"))
    return steps