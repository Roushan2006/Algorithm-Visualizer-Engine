#  ⚙️ Algorithm Visualizer Engine

A stunning Streamlit web application to **visualize**, **understand**, and **compare** Sorting & Searching algorithms — with downloadable source code in **5 languages**.

## 🚀 Getting Started

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the App
```bash
streamlit run app.py
```

Open your browser at **http://localhost:8501**

---

## 📦 Project Structure
```
algo_visualizer/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── code_snippets.py        # All algorithm code in 4 languages
└── algorithms/
    ├── __init__.py
    ├── sorting.py          # Sorting step generators
    └── searching.py        # Searching step generators
```

---

## 🔀 Sorting Algorithms
| Algorithm | Best | Average | Worst | Space | Stable |
|---|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ |

## 🔍 Searching Algorithms
| Algorithm | Best | Average | Worst | Requires Sorted |
|---|---|---|---|---|
| Linear Search | O(1) | O(n) | O(n) | ❌ |
| Binary Search | O(1) | O(log n) | O(log n) | ✅ |
| Jump Search | O(1) | O(√n) | O(√n) | ✅ |
| Exponential Search | O(1) | O(log n) | O(log n) | ✅ |

---

## 🌟 Features
- 🎬 **Step-by-step animation** with color-coded highlights
- 📊 **Live stats** — comparisons, swaps, steps
- 📄 **Source code** in Python, Java, C, C++, JavaScript
- 📈 **Complexity comparison** charts
- 🎛️ **Controls** — array size, animation speed, random arrays
- 🎨 **Dark theme** with neon accents

---

## 💡 How to Use
1. Choose **Sorting** or **Searching** from the sidebar
2. Pick an algorithm
3. Adjust array size and speed
4. Click **▶ RUN** to start the animation
5. Switch to the **Source Code** tab to see implementations
6. Use the **Comparison** tab to compare complexities
