def _step(arr, highlights=None, description="", comparisons=0, swaps=0):
    return {
        "array": arr[:],
        "highlights": highlights or {},
        "description": description,
        "comparisons": comparisons,
        "swaps": swaps,
    }


# ─── Bubble Sort ─────────────────────────────────────────────────────────────
def bubble_sort_steps(arr):
    steps = []
    n = len(arr)
    sorted_indices = set()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            hl = {k: "#10b981" for k in sorted_indices}
            hl[j] = "#f59e0b"; hl[j+1] = "#f59e0b"
            steps.append(_step(arr, hl, f"Comparing index {j} ({arr[j]}) and {j+1} ({arr[j+1]})", comparisons=1))
            if arr[j] > arr[j+1]:
                hl2 = {k: "#10b981" for k in sorted_indices}
                hl2[j] = "#ef4444"; hl2[j+1] = "#ef4444"
                steps.append(_step(arr, hl2, f"Swapping {arr[j]} ↔ {arr[j+1]}", swaps=1))
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        sorted_indices.add(n - i - 1)
        hl_done = {k: "#10b981" for k in sorted_indices}
        steps.append(_step(arr, hl_done, f"Pass {i+1} complete — index {n-i-1} is sorted"))
        if not swapped:
            break
    hl_all = {k: "#10b981" for k in range(n)}
    steps.append(_step(arr, hl_all, "Array fully sorted! ✅"))
    return steps


# ─── Selection Sort ───────────────────────────────────────────────────────────
def selection_sort_steps(arr):
    steps = []
    n = len(arr)
    sorted_indices = set()
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            hl = {k: "#10b981" for k in sorted_indices}
            hl[i] = "#ec4899"; hl[min_idx] = "#f59e0b"; hl[j] = "#f59e0b"
            steps.append(_step(arr, hl, f"Comparing min ({arr[min_idx]}) with index {j} ({arr[j]})", comparisons=1))
            if arr[j] < arr[min_idx]:
                min_idx = j
                hl2 = {k: "#10b981" for k in sorted_indices}
                hl2[min_idx] = "#f59e0b"
                steps.append(_step(arr, hl2, f"New minimum found: {arr[min_idx]} at index {min_idx}"))
        if min_idx != i:
            hl3 = {k: "#10b981" for k in sorted_indices}
            hl3[i] = "#ef4444"; hl3[min_idx] = "#ef4444"
            steps.append(_step(arr, hl3, f"Swapping {arr[i]} ↔ {arr[min_idx]}", swaps=1))
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        sorted_indices.add(i)
        hl4 = {k: "#10b981" for k in sorted_indices}
        steps.append(_step(arr, hl4, f"Position {i} sorted — placed {arr[i]}"))
    return steps


# ─── Insertion Sort ───────────────────────────────────────────────────────────
def insertion_sort_steps(arr):
    steps = []
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        hl = {k: "#10b981" for k in range(i)}
        hl[i] = "#ec4899"
        steps.append(_step(arr, hl, f"Inserting key = {key} (index {i})"))
        while j >= 0 and arr[j] > key:
            hl2 = {k: "#10b981" for k in range(i)}
            hl2[j] = "#f59e0b"; hl2[j+1] = "#ef4444"
            steps.append(_step(arr, hl2, f"{arr[j]} > {key} — shifting right", comparisons=1, swaps=1))
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        hl3 = {k: "#10b981" for k in range(i+1)}
        hl3[j+1] = "#06b6d4"
        steps.append(_step(arr, hl3, f"Placed {key} at index {j+1}"))
    hl_all = {k: "#10b981" for k in range(n)}
    steps.append(_step(arr, hl_all, "Array fully sorted! ✅"))
    return steps


# ─── Merge Sort ───────────────────────────────────────────────────────────────
def merge_sort_steps(arr):
    steps = []

    def merge_sort(a, left, right):
        if right - left <= 1:
            return
        mid = (left + right) // 2
        merge_sort(a, left, mid)
        merge_sort(a, mid, right)
        merge(a, left, mid, right)

    def merge(a, left, mid, right):
        left_part  = a[left:mid]
        right_part = a[mid:right]
        i = j = 0
        k = left
        while i < len(left_part) and j < len(right_part):
            hl = {x: "#8b5cf6" for x in range(left, right)}
            hl[left+i] = "#f59e0b"; hl[mid+j] = "#f59e0b"
            steps.append(_step(a, hl, f"Comparing {left_part[i]} and {right_part[j]}", comparisons=1))
            if left_part[i] <= right_part[j]:
                a[k] = left_part[i]; i += 1
            else:
                a[k] = right_part[j]; j += 1
            k += 1
        while i < len(left_part):
            a[k] = left_part[i]; i += 1; k += 1
        while j < len(right_part):
            a[k] = right_part[j]; j += 1; k += 1
        hl2 = {x: "#10b981" for x in range(left, right)}
        steps.append(_step(a, hl2, f"Merged range [{left}:{right}]", swaps=right-left))

    merge_sort(arr, 0, len(arr))
    hl_all = {k: "#10b981" for k in range(len(arr))}
    steps.append(_step(arr, hl_all, "Array fully sorted! ✅"))
    return steps


# ─── Quick Sort ───────────────────────────────────────────────────────────────
def quick_sort_steps(arr):
    steps = []

    def partition(a, low, high):
        pivot = a[high]
        hl = {high: "#ec4899"}
        steps.append(_step(a, hl, f"Pivot = {pivot} (index {high})"))
        i = low - 1
        for j in range(low, high):
            hl2 = {high: "#ec4899", j: "#f59e0b"}
            if i >= low: hl2[i] = "#8b5cf6"
            steps.append(_step(a, hl2, f"Comparing {a[j]} with pivot {pivot}", comparisons=1))
            if a[j] <= pivot:
                i += 1
                if i != j:
                    hl3 = {high: "#ec4899", i: "#ef4444", j: "#ef4444"}
                    steps.append(_step(a, hl3, f"Swapping {a[i]} ↔ {a[j]}", swaps=1))
                    a[i], a[j] = a[j], a[i]
        a[i+1], a[high] = a[high], a[i+1]
        hl4 = {i+1: "#10b981"}
        steps.append(_step(a, hl4, f"Pivot {pivot} placed at index {i+1}", swaps=1))
        return i + 1

    def quick_sort(a, low, high):
        if low < high:
            pi = partition(a, low, high)
            quick_sort(a, low, pi - 1)
            quick_sort(a, pi + 1, high)

    quick_sort(arr, 0, len(arr) - 1)
    hl_all = {k: "#10b981" for k in range(len(arr))}
    steps.append(_step(arr, hl_all, "Array fully sorted! ✅"))
    return steps


# ─── Heap Sort ────────────────────────────────────────────────────────────────
def heap_sort_steps(arr):
    steps = []
    n = len(arr)

    def heapify(a, size, root):
        largest = root
        l, r = 2*root+1, 2*root+2
        hl = {root: "#ec4899"}
        if l < size:
            hl[l] = "#f59e0b"
            steps.append(_step(a, hl, f"Heapify: comparing root {a[root]} with left child {a[l]}", comparisons=1))
            if a[l] > a[largest]:
                largest = l
        if r < size:
            hl2 = {root: "#ec4899", r: "#f59e0b"}
            steps.append(_step(a, hl2, f"Heapify: comparing with right child {a[r]}", comparisons=1))
            if a[r] > a[largest]:
                largest = r
        if largest != root:
            hl3 = {root: "#ef4444", largest: "#ef4444"}
            steps.append(_step(a, hl3, f"Swapping {a[root]} ↔ {a[largest]}", swaps=1))
            a[root], a[largest] = a[largest], a[root]
            heapify(a, size, largest)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    steps.append(_step(arr, {}, "Max-heap built ✅"))

    for i in range(n-1, 0, -1):
        hl = {0: "#ef4444", i: "#ef4444"}
        steps.append(_step(arr, hl, f"Placing max ({arr[0]}) at position {i}", swaps=1))
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
        hl2 = {k: "#10b981" for k in range(i, n)}
        steps.append(_step(arr, hl2, f"Index {i} sorted — {arr[i]}"))

    hl_all = {k: "#10b981" for k in range(n)}
    steps.append(_step(arr, hl_all, "Array fully sorted! ✅"))
    return steps