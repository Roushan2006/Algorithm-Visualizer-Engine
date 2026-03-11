_CODE = {

# ════════════════════════════════════════════════════════════════════════════
# BUBBLE SORT
# ════════════════════════════════════════════════════════════════════════════
"Bubble Sort": {

"python": '''\
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break          # already sorted — early exit
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))   # [11, 12, 22, 25, 34, 64, 90]
''',

"java": '''\
public class BubbleSort {
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp   = arr[j];
                    arr[j]     = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped    = true;
                }
            }
            if (!swapped) break;
        }
    }

    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        bubbleSort(arr);
        // arr → [11, 12, 22, 25, 34, 64, 90]
    }
}
''',

"c": '''\
#include <stdio.h>
#include <stdbool.h>

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int tmp    = arr[j];
                arr[j]     = arr[j + 1];
                arr[j + 1] = tmp;
                swapped    = true;
            }
        }
        if (!swapped) break;
    }
}

int main(void) {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof arr / sizeof arr[0];
    bubbleSort(arr, n);
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);  /* 11 12 22 25 34 64 90 */
    return 0;
}
''',

"cpp": '''\
#include <iostream>
#include <vector>
using namespace std;

void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;  // early exit if already sorted
    }
}

int main() {
    vector<int> arr = {64, 34, 25, 12, 22, 11, 90};
    bubbleSort(arr);
    for (int x : arr) cout << x << " ";
    // Output: 11 12 22 25 34 64 90
    return 0;
}
''',

"javascript": '''\
function bubbleSort(arr) {
    const n = arr.length;
    for (let i = 0; i < n - 1; i++) {
        let swapped = false;
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
                swapped = true;
            }
        }
        if (!swapped) break;
    }
    return arr;
}

const arr = [64, 34, 25, 12, 22, 11, 90];
console.log(bubbleSort(arr)); // [11, 12, 22, 25, 34, 64, 90]
''',
},

# ════════════════════════════════════════════════════════════════════════════
# SELECTION SORT
# ════════════════════════════════════════════════════════════════════════════
"Selection Sort": {

"python": '''\
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))  # [11, 12, 22, 25, 64]
''',

"java": '''\
public class SelectionSort {
    public static void selectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < n; j++)
                if (arr[j] < arr[minIdx]) minIdx = j;
            int temp    = arr[minIdx];
            arr[minIdx] = arr[i];
            arr[i]      = temp;
        }
    }
    public static void main(String[] args) {
        int[] arr = {64, 25, 12, 22, 11};
        selectionSort(arr); // [11, 12, 22, 25, 64]
    }
}
''',

"c": '''\
#include <stdio.h>

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++)
            if (arr[j] < arr[minIdx]) minIdx = j;
        int tmp     = arr[minIdx];
        arr[minIdx] = arr[i];
        arr[i]      = tmp;
    }
}

int main(void) {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof arr / sizeof arr[0];
    selectionSort(arr, n);
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    return 0;
}
''',

"cpp": '''\
#include <iostream>
#include <vector>
using namespace std;

void selectionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++)
            if (arr[j] < arr[minIdx]) minIdx = j;
        swap(arr[i], arr[minIdx]);
    }
}

int main() {
    vector<int> arr = {64, 25, 12, 22, 11};
    selectionSort(arr);
    for (int x : arr) cout << x << " ";
    // Output: 11 12 22 25 64
    return 0;
}
''',

"javascript": '''\
function selectionSort(arr) {
    const n = arr.length;
    for (let i = 0; i < n - 1; i++) {
        let minIdx = i;
        for (let j = i + 1; j < n; j++)
            if (arr[j] < arr[minIdx]) minIdx = j;
        [arr[i], arr[minIdx]] = [arr[minIdx], arr[i]];
    }
    return arr;
}
console.log(selectionSort([64, 25, 12, 22, 11])); // [11, 12, 22, 25, 64]
''',
},

# ════════════════════════════════════════════════════════════════════════════
# INSERTION SORT
# ════════════════════════════════════════════════════════════════════════════
"Insertion Sort": {

"python": '''\
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j   = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort([12, 11, 13, 5, 6]))  # [5, 6, 11, 12, 13]
''',

"java": '''\
public class InsertionSort {
    public static void insertionSort(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            int key = arr[i], j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }
    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6};
        insertionSort(arr); // [5, 6, 11, 12, 13]
    }
}
''',

"c": '''\
#include <stdio.h>

void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i], j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int main(void) {
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof arr / sizeof arr[0];
    insertionSort(arr, n);
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    return 0;
}
''',

"cpp": '''\
#include <iostream>
#include <vector>
using namespace std;

void insertionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i], j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int main() {
    vector<int> arr = {12, 11, 13, 5, 6};
    insertionSort(arr);
    for (int x : arr) cout << x << " ";
    // Output: 5 6 11 12 13
    return 0;
}
''',

"javascript": '''\
function insertionSort(arr) {
    for (let i = 1; i < arr.length; i++) {
        let key = arr[i], j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
    return arr;
}
console.log(insertionSort([12, 11, 13, 5, 6])); // [5, 6, 11, 12, 13]
''',
},

# ════════════════════════════════════════════════════════════════════════════
# MERGE SORT
# ════════════════════════════════════════════════════════════════════════════
"Merge Sort": {

"python": '''\
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid   = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)

def _merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
# [3, 9, 10, 27, 38, 43, 82]
''',

"java": '''\
public class MergeSort {
    public static void mergeSort(int[] arr, int l, int r) {
        if (l < r) {
            int m = (l + r) / 2;
            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }
    static void merge(int[] arr, int l, int m, int r) {
        int n1 = m - l + 1, n2 = r - m;
        int[] L = new int[n1], R = new int[n2];
        for (int i = 0; i < n1; i++) L[i] = arr[l + i];
        for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];
        int i = 0, j = 0, k = l;
        while (i < n1 && j < n2)
            arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
        while (i < n1) arr[k++] = L[i++];
        while (j < n2) arr[k++] = R[j++];
    }
    public static void main(String[] args) {
        int[] arr = {38, 27, 43, 3, 9, 82, 10};
        mergeSort(arr, 0, arr.length - 1);
        // arr → [3, 9, 10, 27, 38, 43, 82]
    }
}
''',

"c": '''\
#include <stdio.h>
#include <stdlib.h>

void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1, n2 = r - m;
    int *L = malloc(n1 * sizeof(int));
    int *R = malloc(n2 * sizeof(int));
    for (int i = 0; i < n1; i++) L[i] = arr[l + i];
    for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];
    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2)
        arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
    free(L); free(R);
}
void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = (l + r) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}
int main(void) {
    int arr[] = {38, 27, 43, 3, 9, 82, 10};
    int n = sizeof arr / sizeof arr[0];
    mergeSort(arr, 0, n - 1);
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    return 0;
}
''',

"cpp": '''\
#include <iostream>
#include <vector>
using namespace std;

void merge(vector<int>& arr, int l, int m, int r) {
    vector<int> L(arr.begin() + l, arr.begin() + m + 1);
    vector<int> R(arr.begin() + m + 1, arr.begin() + r + 1);
    int i = 0, j = 0, k = l;
    while (i < (int)L.size() && j < (int)R.size())
        arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
    while (i < (int)L.size()) arr[k++] = L[i++];
    while (j < (int)R.size()) arr[k++] = R[j++];
}

void mergeSort(vector<int>& arr, int l, int r) {
    if (l < r) {
        int m = (l + r) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

int main() {
    vector<int> arr = {38, 27, 43, 3, 9, 82, 10};
    mergeSort(arr, 0, arr.size() - 1);
    for (int x : arr) cout << x << " ";
    // Output: 3 9 10 27 38 43 82
    return 0;
}
''',

"javascript": '''\
function mergeSort(arr) {
    if (arr.length <= 1) return arr;
    const mid   = Math.floor(arr.length / 2);
    const left  = mergeSort(arr.slice(0, mid));
    const right = mergeSort(arr.slice(mid));
    return merge(left, right);
}
function merge(left, right) {
    const result = [];
    let i = 0, j = 0;
    while (i < left.length && j < right.length)
        result.push(left[i] <= right[j] ? left[i++] : right[j++]);
    return [...result, ...left.slice(i), ...right.slice(j)];
}
console.log(mergeSort([38, 27, 43, 3, 9, 82, 10]));
// [3, 9, 10, 27, 38, 43, 82]
''',
},

# ════════════════════════════════════════════════════════════════════════════
# QUICK SORT
# ════════════════════════════════════════════════════════════════════════════
"Quick Sort": {

"python": '''\
def quick_sort(arr, low=0, high=None):
    if high is None: high = len(arr) - 1
    if low < high:
        pi = _partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

def _partition(arr, low, high):
    pivot, i = arr[high], low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

print(quick_sort([10, 7, 8, 9, 1, 5]))  # [1, 5, 7, 8, 9, 10]
''',

"java": '''\
public class QuickSort {
    static int partition(int[] arr, int low, int high) {
        int pivot = arr[high], i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                int t = arr[++i]; arr[i] = arr[j]; arr[j] = t;
            }
        }
        int t = arr[i+1]; arr[i+1] = arr[high]; arr[high] = t;
        return i + 1;
    }
    static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }
    public static void main(String[] args) {
        int[] arr = {10, 7, 8, 9, 1, 5};
        quickSort(arr, 0, arr.length - 1);
        // arr → [1, 5, 7, 8, 9, 10]
    }
}
''',

"c": '''\
#include <stdio.h>

static void swap(int *a, int *b) { int t = *a; *a = *b; *b = t; }

int partition(int arr[], int low, int high) {
    int pivot = arr[high], i = low - 1;
    for (int j = low; j < high; j++)
        if (arr[j] <= pivot) swap(&arr[++i], &arr[j]);
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
int main(void) {
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof arr / sizeof arr[0];
    quickSort(arr, 0, n - 1);
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    return 0;
}
''',

"cpp": '''\
#include <iostream>
#include <vector>
using namespace std;

int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high], i = low - 1;
    for (int j = low; j < high; j++)
        if (arr[j] <= pivot) swap(arr[++i], arr[j]);
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    vector<int> arr = {10, 7, 8, 9, 1, 5};
    quickSort(arr, 0, arr.size() - 1);
    for (int x : arr) cout << x << " ";
    // Output: 1 5 7 8 9 10
    return 0;
}
''',

"javascript": '''\
function quickSort(arr, low = 0, high = arr.length - 1) {
    if (low < high) {
        const pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
    return arr;
}
function partition(arr, low, high) {
    const pivot = arr[high];
    let i = low - 1;
    for (let j = low; j < high; j++) {
        if (arr[j] <= pivot)
            [arr[++i], arr[j]] = [arr[j], arr[i]];
    }
    [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
    return i + 1;
}
console.log(quickSort([10, 7, 8, 9, 1, 5])); // [1, 5, 7, 8, 9, 10]
''',
},

# ════════════════════════════════════════════════════════════════════════════
# HEAP SORT
# ════════════════════════════════════════════════════════════════════════════
"Heap Sort": {

"python": '''\
def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, i, 0)
    return arr

def _heapify(arr, n, i):
    largest = i
    l, r    = 2*i + 1, 2*i + 2
    if l < n and arr[l] > arr[largest]: largest = l
    if r < n and arr[r] > arr[largest]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)

print(heap_sort([12, 11, 13, 5, 6, 7]))  # [5, 6, 7, 11, 12, 13]
''',

"java": '''\
public class HeapSort {
    static void heapify(int[] arr, int n, int i) {
        int largest = i, l = 2*i+1, r = 2*i+2;
        if (l < n && arr[l] > arr[largest]) largest = l;
        if (r < n && arr[r] > arr[largest]) largest = r;
        if (largest != i) {
            int t = arr[i]; arr[i] = arr[largest]; arr[largest] = t;
            heapify(arr, n, largest);
        }
    }
    public static void heapSort(int[] arr) {
        int n = arr.length;
        for (int i = n/2-1; i >= 0; i--) heapify(arr, n, i);
        for (int i = n-1; i > 0; i--) {
            int t = arr[0]; arr[0] = arr[i]; arr[i] = t;
            heapify(arr, i, 0);
        }
    }
    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6, 7};
        heapSort(arr); // [5, 6, 7, 11, 12, 13]
    }
}
''',

"c": '''\
#include <stdio.h>

void heapify(int arr[], int n, int i) {
    int largest = i, l = 2*i+1, r = 2*i+2, t;
    if (l < n && arr[l] > arr[largest]) largest = l;
    if (r < n && arr[r] > arr[largest]) largest = r;
    if (largest != i) {
        t = arr[i]; arr[i] = arr[largest]; arr[largest] = t;
        heapify(arr, n, largest);
    }
}
void heapSort(int arr[], int n) {
    for (int i = n/2-1; i >= 0; i--) heapify(arr, n, i);
    for (int i = n-1; i > 0; i--) {
        int t = arr[0]; arr[0] = arr[i]; arr[i] = t;
        heapify(arr, i, 0);
    }
}
int main(void) {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof arr / sizeof arr[0];
    heapSort(arr, n);
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    return 0;
}
''',

"cpp": '''\
#include <iostream>
#include <vector>
using namespace std;

void heapify(vector<int>& arr, int n, int i) {
    int largest = i, l = 2*i+1, r = 2*i+2;
    if (l < n && arr[l] > arr[largest]) largest = l;
    if (r < n && arr[r] > arr[largest]) largest = r;
    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = n/2 - 1; i >= 0; i--) heapify(arr, n, i);
    for (int i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

int main() {
    vector<int> arr = {12, 11, 13, 5, 6, 7};
    heapSort(arr);
    for (int x : arr) cout << x << " ";
    // Output: 5 6 7 11 12 13
    return 0;
}
''',

"javascript": '''\
function heapSort(arr) {
    const n = arr.length;
    for (let i = Math.floor(n/2) - 1; i >= 0; i--) heapify(arr, n, i);
    for (let i = n - 1; i > 0; i--) {
        [arr[0], arr[i]] = [arr[i], arr[0]];
        heapify(arr, i, 0);
    }
    return arr;
}
function heapify(arr, n, i) {
    let largest = i, l = 2*i+1, r = 2*i+2;
    if (l < n && arr[l] > arr[largest]) largest = l;
    if (r < n && arr[r] > arr[largest]) largest = r;
    if (largest !== i) {
        [arr[i], arr[largest]] = [arr[largest], arr[i]];
        heapify(arr, n, largest);
    }
}
console.log(heapSort([12, 11, 13, 5, 6, 7])); // [5, 6, 7, 11, 12, 13]
''',
},

# ════════════════════════════════════════════════════════════════════════════
# LINEAR SEARCH
# ════════════════════════════════════════════════════════════════════════════
"Linear Search": {

"python": '''\
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i   # found
    return -1          # not found

arr = [10, 50, 30, 70, 80, 60, 20, 90, 40]
print(linear_search(arr, 70))   # 3
print(linear_search(arr, 100))  # -1
''',

"java": '''\
public class LinearSearch {
    public static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++)
            if (arr[i] == target) return i;
        return -1;
    }
    public static void main(String[] args) {
        int[] arr = {10, 50, 30, 70, 80, 60, 20, 90, 40};
        System.out.println(linearSearch(arr, 70));   // 3
        System.out.println(linearSearch(arr, 100));  // -1
    }
}
''',

"c": '''\
#include <stdio.h>

int linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; i++)
        if (arr[i] == target) return i;
    return -1;
}
int main(void) {
    int arr[] = {10, 50, 30, 70, 80, 60, 20, 90, 40};
    int n = sizeof arr / sizeof arr[0];
    printf("%d\n", linearSearch(arr, n, 70));   /*  3 */
    printf("%d\n", linearSearch(arr, n, 100));  /* -1 */
    return 0;
}
''',

"cpp": '''\
#include <iostream>
#include <vector>
using namespace std;

int linearSearch(const vector<int>& arr, int target) {
    for (int i = 0; i < (int)arr.size(); i++)
        if (arr[i] == target) return i;
    return -1;
}

int main() {
    vector<int> arr = {10, 50, 30, 70, 80, 60, 20, 90, 40};
    cout << linearSearch(arr, 70)  << "\n";  //  3
    cout << linearSearch(arr, 100) << "\n";  // -1
    return 0;
}
''',

"javascript": '''\
function linearSearch(arr, target) {
    for (let i = 0; i < arr.length; i++)
        if (arr[i] === target) return i;
    return -1;
}
const arr = [10, 50, 30, 70, 80, 60, 20, 90, 40];
console.log(linearSearch(arr, 70));   //  3
console.log(linearSearch(arr, 100));  // -1
''',
},

# ════════════════════════════════════════════════════════════════════════════
# BINARY SEARCH
# ════════════════════════════════════════════════════════════════════════════
"Binary Search": {

"python": '''\
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if   arr[mid] == target: return mid
        elif arr[mid] <  target: low  = mid + 1
        else:                    high = mid - 1
    return -1

arr = [2, 3, 4, 10, 40, 55, 70, 88]  # must be sorted
print(binary_search(arr, 10))   #  3
print(binary_search(arr, 99))   # -1
''',

"java": '''\
public class BinarySearch {
    public static int binarySearch(int[] arr, int target) {
        int low = 0, high = arr.length - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if      (arr[mid] == target) return mid;
            else if (arr[mid] <  target) low  = mid + 1;
            else                         high = mid - 1;
        }
        return -1;
    }
    public static void main(String[] args) {
        int[] arr = {2, 3, 4, 10, 40, 55, 70, 88};
        System.out.println(binarySearch(arr, 10));  //  3
        System.out.println(binarySearch(arr, 99));  // -1
    }
}
''',

"c": '''\
#include <stdio.h>

int binarySearch(int arr[], int n, int target) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if      (arr[mid] == target) return mid;
        else if (arr[mid] <  target) low  = mid + 1;
        else                         high = mid - 1;
    }
    return -1;
}
int main(void) {
    int arr[] = {2, 3, 4, 10, 40, 55, 70, 88};
    int n = sizeof arr / sizeof arr[0];
    printf("%d\n", binarySearch(arr, n, 10));  /*  3 */
    printf("%d\n", binarySearch(arr, n, 99));  /* -1 */
    return 0;
}
''',

"cpp": '''\
#include <iostream>
#include <vector>
using namespace std;

int binarySearch(const vector<int>& arr, int target) {
    int low = 0, high = (int)arr.size() - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if      (arr[mid] == target) return mid;
        else if (arr[mid] <  target) low  = mid + 1;
        else                         high = mid - 1;
    }
    return -1;
}

int main() {
    vector<int> arr = {2, 3, 4, 10, 40, 55, 70, 88};  // sorted!
    cout << binarySearch(arr, 10) << "\n";  //  3
    cout << binarySearch(arr, 99) << "\n";  // -1
    return 0;
}
''',

"javascript": '''\
function binarySearch(arr, target) {
    let low = 0, high = arr.length - 1;
    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        if      (arr[mid] === target) return mid;
        else if (arr[mid] <  target)  low  = mid + 1;
        else                          high = mid - 1;
    }
    return -1;
}
const arr = [2, 3, 4, 10, 40, 55, 70, 88];
console.log(binarySearch(arr, 10));  //  3
console.log(binarySearch(arr, 99));  // -1
''',
},

# ════════════════════════════════════════════════════════════════════════════
# JUMP SEARCH
# ════════════════════════════════════════════════════════════════════════════
"Jump Search": {

"python": '''\
import math

def jump_search(arr, target):
    n, step, prev = len(arr), int(math.sqrt(len(arr))), 0
    while arr[min(step, n) - 1] < target:
        prev  = step
        step += int(math.sqrt(n))
        if prev >= n: return -1
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n): return -1
    return prev if arr[prev] == target else -1

arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
print(jump_search(arr, 55))   # 10
print(jump_search(arr, 100))  # -1
''',

"java": '''\
public class JumpSearch {
    public static int jumpSearch(int[] arr, int target) {
        int n = arr.length, step = (int)Math.sqrt(n), prev = 0;
        while (arr[Math.min(step, n) - 1] < target) {
            prev  = step;
            step += (int)Math.sqrt(n);
            if (prev >= n) return -1;
        }
        while (arr[prev] < target)
            if (++prev == Math.min(step, n)) return -1;
        return arr[prev] == target ? prev : -1;
    }
    public static void main(String[] args) {
        int[] arr = {0,1,1,2,3,5,8,13,21,34,55,89,144};
        System.out.println(jumpSearch(arr, 55));   // 10
        System.out.println(jumpSearch(arr, 100));  // -1
    }
}
''',

"c": '''\
#include <stdio.h>
#include <math.h>

int jumpSearch(int arr[], int n, int target) {
    int step = (int)sqrt(n), prev = 0;
    while (arr[(step<n?step:n)-1] < target) {
        prev  = step;
        step += (int)sqrt(n);
        if (prev >= n) return -1;
    }
    while (arr[prev] < target)
        if (++prev == (step<n?step:n)) return -1;
    return arr[prev] == target ? prev : -1;
}
int main(void) {
    int arr[] = {0,1,1,2,3,5,8,13,21,34,55,89,144};
    int n = sizeof arr / sizeof arr[0];
    printf("%d\n", jumpSearch(arr, n, 55));   /* 10 */
    printf("%d\n", jumpSearch(arr, n, 100));  /* -1 */
    return 0;
}
''',

"cpp": '''\
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int jumpSearch(const vector<int>& arr, int target) {
    int n = arr.size(), step = (int)sqrt(n), prev = 0;
    while (arr[min(step, n) - 1] < target) {
        prev  = step;
        step += (int)sqrt(n);
        if (prev >= n) return -1;
    }
    while (arr[prev] < target)
        if (++prev == min(step, n)) return -1;
    return arr[prev] == target ? prev : -1;
}

int main() {
    vector<int> arr = {0,1,1,2,3,5,8,13,21,34,55,89,144};
    cout << jumpSearch(arr, 55)  << "\n";  // 10
    cout << jumpSearch(arr, 100) << "\n";  // -1
    return 0;
}
''',

"javascript": '''\
function jumpSearch(arr, target) {
    const n = arr.length, step = Math.floor(Math.sqrt(n));
    let prev = 0, curr = step;
    while (arr[Math.min(curr, n) - 1] < target) {
        prev  = curr;
        curr += step;
        if (prev >= n) return -1;
    }
    while (arr[prev] < target)
        if (++prev === Math.min(curr, n)) return -1;
    return arr[prev] === target ? prev : -1;
}
const arr = [0,1,1,2,3,5,8,13,21,34,55,89,144];
console.log(jumpSearch(arr, 55));   // 10
console.log(jumpSearch(arr, 100));  // -1
''',
},

# ════════════════════════════════════════════════════════════════════════════
# EXPONENTIAL SEARCH
# ════════════════════════════════════════════════════════════════════════════
"Exponential Search": {

"python": '''\
def exponential_search(arr, target):
    if arr[0] == target: return 0
    n, i = len(arr), 1
    while i < n and arr[i] <= target:
        i *= 2
    return _binary(arr, i // 2, min(i, n - 1), target)

def _binary(arr, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if   arr[mid] == target: return mid
        elif arr[mid] <  target: low  = mid + 1
        else:                    high = mid - 1
    return -1

arr = [2, 3, 4, 10, 40, 55, 70, 88, 100, 120]
print(exponential_search(arr, 55))   # 5
print(exponential_search(arr, 99))   # -1
''',

"java": '''\
public class ExponentialSearch {
    static int binary(int[] arr, int l, int r, int x) {
        while (l <= r) {
            int m = (l + r) / 2;
            if      (arr[m] == x) return m;
            else if (arr[m] <  x) l = m + 1;
            else                  r = m - 1;
        }
        return -1;
    }
    public static int exponentialSearch(int[] arr, int x) {
        if (arr[0] == x) return 0;
        int i = 1, n = arr.length;
        while (i < n && arr[i] <= x) i *= 2;
        return binary(arr, i/2, Math.min(i, n-1), x);
    }
    public static void main(String[] args) {
        int[] arr = {2, 3, 4, 10, 40, 55, 70, 88, 100, 120};
        System.out.println(exponentialSearch(arr, 55));  // 5
        System.out.println(exponentialSearch(arr, 99));  // -1
    }
}
''',

"c": '''\
#include <stdio.h>

int binary(int arr[], int l, int r, int x) {
    while (l <= r) {
        int m = (l + r) / 2;
        if      (arr[m] == x) return m;
        else if (arr[m] <  x) l = m + 1;
        else                  r = m - 1;
    }
    return -1;
}
int expSearch(int arr[], int n, int x) {
    if (arr[0] == x) return 0;
    int i = 1;
    while (i < n && arr[i] <= x) i *= 2;
    return binary(arr, i/2, (i<n?i:n-1), x);
}
int main(void) {
    int arr[] = {2, 3, 4, 10, 40, 55, 70, 88, 100, 120};
    int n = sizeof arr / sizeof arr[0];
    printf("%d\n", expSearch(arr, n, 55));  /*  5 */
    printf("%d\n", expSearch(arr, n, 99));  /* -1 */
    return 0;
}
''',

"cpp": '''\
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int binarySearch(const vector<int>& arr, int l, int r, int x) {
    while (l <= r) {
        int m = (l + r) / 2;
        if      (arr[m] == x) return m;
        else if (arr[m] <  x) l = m + 1;
        else                  r = m - 1;
    }
    return -1;
}

int exponentialSearch(const vector<int>& arr, int x) {
    if (arr[0] == x) return 0;
    int i = 1, n = arr.size();
    while (i < n && arr[i] <= x) i *= 2;
    return binarySearch(arr, i / 2, min(i, n - 1), x);
}

int main() {
    vector<int> arr = {2, 3, 4, 10, 40, 55, 70, 88, 100, 120};
    cout << exponentialSearch(arr, 55) << "\n";  //  5
    cout << exponentialSearch(arr, 99) << "\n";  // -1
    return 0;
}
''',

"javascript": '''\
function exponentialSearch(arr, target) {
    if (arr[0] === target) return 0;
    const n = arr.length;
    let i = 1;
    while (i < n && arr[i] <= target) i *= 2;
    return binarySearch(arr, Math.floor(i/2), Math.min(i, n-1), target);
}
function binarySearch(arr, low, high, target) {
    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        if      (arr[mid] === target) return mid;
        else if (arr[mid] <  target)  low  = mid + 1;
        else                          high = mid - 1;
    }
    return -1;
}
const arr = [2, 3, 4, 10, 40, 55, 70, 88, 100, 120];
console.log(exponentialSearch(arr, 55));  //  5
console.log(exponentialSearch(arr, 99));  // -1
''',
},

}  # end _CODE


def get_code(algorithm: str, language: str) -> str:
    """Return source code for the given algorithm and language."""
    return _CODE.get(algorithm, {}).get(
        language,
        f"// Code not yet available for '{algorithm}' in '{language}'"
    )