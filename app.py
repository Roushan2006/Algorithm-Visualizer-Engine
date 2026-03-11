import streamlit as st
import time
import random
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from sorting import (
    bubble_sort_steps, selection_sort_steps, insertion_sort_steps,
    merge_sort_steps, quick_sort_steps, heap_sort_steps
)
from searching import (
    linear_search_steps, binary_search_steps, jump_search_steps,
    exponential_search_steps
)
from code_snippets import get_code

st.set_page_config(
    page_title="Algorithm Visualizer Engine",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&family=Inter:wght@300;400;500;600;700;800;900&display=swap');

*, html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    box-sizing: border-box;
}

/* ── Base ── */
.stApp {
    background: #05050f;
    color: #e2e4f0;
}

/* subtle dot-grid bg */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: radial-gradient(circle, rgba(139,92,246,0.07) 1px, transparent 1px);
    background-size: 28px 28px;
    pointer-events: none;
    z-index: 0;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #09091a 0%, #060612 100%) !important;
    border-right: 1px solid rgba(139,92,246,0.18) !important;
}
[data-testid="stSidebar"] * { color: #b8bcd8 !important; }
[data-testid="stSidebar"] label {
    font-size: 0.72rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    color: #5a5e80 !important;
    font-weight: 600 !important;
}

/* ── Headings ── */
h1 {
    font-family: 'Inter', sans-serif !important;
    font-weight: 900 !important;
    font-size: 2.8rem !important;
    letter-spacing: -1.5px !important;
    line-height: 1.05 !important;
    background: linear-gradient(130deg, #ffffff 0%, #c4b5fd 45%, #67e8f9 100%);
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    margin: 0 0 4px 0 !important;
}
h2, h3 {
    font-family: 'Inter', sans-serif !important;
    font-weight: 700 !important;
    color: #c4c8e8 !important;
    letter-spacing: -0.4px !important;
}

/* ── Hero Card ── */
.ave-hero {
    background: linear-gradient(140deg, #0d0d22 0%, #100d28 55%, #0a1520 100%);
    border: 1px solid rgba(139,92,246,0.28);
    border-radius: 22px;
    padding: 38px 48px 34px;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
}
.ave-hero::before {
    content: '';
    position: absolute;
    top: -80px; right: -80px;
    width: 340px; height: 340px;
    background: radial-gradient(circle, rgba(139,92,246,0.13) 0%, transparent 65%);
    pointer-events: none;
}
.ave-hero::after {
    content: '';
    position: absolute;
    bottom: -60px; left: 120px;
    width: 260px; height: 260px;
    background: radial-gradient(circle, rgba(6,182,212,0.08) 0%, transparent 65%);
    pointer-events: none;
}
.hero-tag {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    color: #8b5cf6;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    background: rgba(139,92,246,0.1);
    border: 1px solid rgba(139,92,246,0.22);
    padding: 3px 12px;
    border-radius: 100px;
    margin-bottom: 14px;
    font-weight: 500;
}
.hero-sub {
    color: #555878;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    margin-top: 10px;
    letter-spacing: 0.02em;
    line-height: 1.7;
}
.hero-badges {
    display: flex;
    gap: 10px;
    margin-top: 20px;
    flex-wrap: wrap;
}
.hero-badge {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    color: #8892b4;
    padding: 5px 14px;
    border-radius: 8px;
    font-size: 0.72rem;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.04em;
}

/* ── Metric Cards ── */
.metric-card {
    background: linear-gradient(145deg, #0d0d20, #111128);
    border: 1px solid rgba(139,92,246,0.18);
    border-radius: 16px;
    padding: 20px 18px 16px;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.metric-card::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #8b5cf6, #06b6d4);
    border-radius: 2px 2px 0 0;
}
.metric-value {
    font-size: 2.1rem;
    font-weight: 800;
    font-family: 'JetBrains Mono', monospace;
    background: linear-gradient(135deg, #c4b5fd, #67e8f9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1.1;
}
.metric-label {
    font-size: 0.65rem;
    color: #3e4265;
    text-transform: uppercase;
    letter-spacing: 0.16em;
    margin-top: 5px;
    font-weight: 600;
}

/* ── Step Info ── */
.step-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(139,92,246,0.12);
    border: 1px solid rgba(139,92,246,0.3);
    color: #c4b5fd;
    padding: 6px 16px;
    border-radius: 100px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.76rem;
    font-weight: 500;
}
.step-desc-text {
    color: #555878;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    margin-left: 10px;
}

/* ── Legend ── */
.legend {
    display: flex;
    gap: 18px;
    flex-wrap: wrap;
    margin: 12px 0 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: #454868;
    align-items: center;
}
.dot {
    width: 9px; height: 9px;
    border-radius: 3px;
    display: inline-block;
    margin-right: 5px;
    vertical-align: middle;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #6d28d9, #8b5cf6) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 700 !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.1em !important;
    padding: 0.7rem 2rem !important;
    transition: all 0.22s ease !important;
    box-shadow: 0 4px 22px rgba(109,40,217,0.35) !important;
}
.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 12px 36px rgba(139,92,246,0.48) !important;
    background: linear-gradient(135deg, #7c3aed, #a78bfa) !important;
}

/* ── Selectbox ── */
.stSelectbox > div > div {
    background: #0d0d20 !important;
    border: 1px solid rgba(139,92,246,0.22) !important;
    color: #dde0f5 !important;
    border-radius: 10px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.82rem !important;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(13,13,32,0.9);
    border-radius: 14px;
    padding: 5px;
    gap: 4px;
    border: 1px solid rgba(139,92,246,0.14);
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: #3e4265 !important;
    border-radius: 10px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.76rem !important;
    letter-spacing: 0.06em !important;
    padding: 9px 22px !important;
    transition: all 0.2s !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #6d28d9, #8b5cf6) !important;
    color: #fff !important;
    box-shadow: 0 4px 18px rgba(109,40,217,0.38) !important;
}

/* ── Code blocks ── */
.stCodeBlock {
    border: 1px solid rgba(139,92,246,0.18) !important;
    border-radius: 12px !important;
}

/* ── Alerts ── */
.stAlert {
    background: rgba(13,13,32,0.9) !important;
    border: 1px solid rgba(139,92,246,0.18) !important;
    border-radius: 12px !important;
}

/* ── Complexity table ── */
.complexity-table {
    width: 100%;
    border-collapse: collapse;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.76rem;
    border: 1px solid rgba(139,92,246,0.14);
    border-radius: 14px;
    overflow: hidden;
}
.complexity-table th {
    background: rgba(139,92,246,0.1);
    color: #a78bfa;
    padding: 13px 18px;
    text-align: left;
    border-bottom: 1px solid rgba(139,92,246,0.18);
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-size: 0.68rem;
}
.complexity-table td {
    padding: 12px 18px;
    border-bottom: 1px solid rgba(139,92,246,0.07);
    color: #8892b4;
}
.complexity-table tr:last-child td { border-bottom: none; }
.complexity-table tr:hover td {
    background: rgba(139,92,246,0.05);
    color: #c4c8e8;
}

/* ── Sidebar brand ── */
.sb-logo {
    font-family: 'Inter', sans-serif;
    font-weight: 900;
    font-size: 1.15rem;
    letter-spacing: -0.5px;
    background: linear-gradient(130deg, #fff, #c4b5fd 60%, #67e8f9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1.2;
    margin-bottom: 2px;
}
.sb-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.58rem;
    color: #2e3050;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 18px;
}
.sb-divider {
    height: 1px;
    background: linear-gradient(90deg, rgba(139,92,246,0.25), transparent);
    margin: 14px 0;
}
.sb-complexity {
    background: rgba(139,92,246,0.06);
    border: 1px solid rgba(139,92,246,0.13);
    border-radius: 12px;
    padding: 14px 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
}
.sb-complexity-title {
    color: #6d28d9;
    font-size: 0.62rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 10px;
    font-weight: 600;
}
.sb-row {
    display: flex;
    justify-content: space-between;
    padding: 3px 0;
}
.sb-key { color: #3e4265; }
.sb-val-best  { color: #34d399; font-weight: 600; }
.sb-val-avg   { color: #a78bfa; font-weight: 600; }
.sb-val-worst { color: #f87171; font-weight: 600; }
.sb-val-space { color: #67e8f9; font-weight: 600; }

div[data-testid="stHorizontalBlock"] > div { background: transparent; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class='sb-logo'>⚙ Algorithm Visualizer Engine</div>
    <div class='sb-sub'>Interactive · Step-by-Step · Multi-Language</div>
    <div class='sb-divider'></div>
    """, unsafe_allow_html=True)

    algo_category = st.selectbox("📂  Category", ["🔀 Sorting", "🔍 Searching"])

    if algo_category == "🔀 Sorting":
        algo_name = st.selectbox("🧮  Algorithm", [
            "Bubble Sort", "Selection Sort", "Insertion Sort",
            "Merge Sort", "Quick Sort", "Heap Sort"
        ])
    else:
        algo_name = st.selectbox("🧮  Algorithm", [
            "Linear Search", "Binary Search", "Jump Search", "Exponential Search"
        ])

    st.markdown("<div class='sb-divider'></div>", unsafe_allow_html=True)

    array_size = st.slider("📐  Array Size", min_value=6, max_value=30, value=14)
    speed = st.select_slider("⚡  Speed", options=["Slow", "Medium", "Fast", "Turbo"], value="Medium")
    speed_map = {"Slow": 0.85, "Medium": 0.40, "Fast": 0.14, "Turbo": 0.03}
    delay = speed_map[speed]

    st.markdown("<div class='sb-divider'></div>", unsafe_allow_html=True)

    search_target = 42
    if algo_category == "🔍 Searching":
        if "array" not in st.session_state or len(st.session_state.get("array", [])) != array_size:
            st.session_state["array"] = sorted(random.sample(range(1, 101), array_size))
        default_target = st.session_state["array"][len(st.session_state["array"]) // 2]
        search_target = st.number_input("🎯  Target Value", min_value=1, max_value=100, value=int(default_target))

    if st.button("🎲  New Random Array", use_container_width=True):
        if algo_category == "🔍 Searching":
            st.session_state["array"] = sorted(random.sample(range(1, 101), array_size))
        else:
            st.session_state["array"] = random.sample(range(1, 101), array_size)

    if "array" not in st.session_state:
        if algo_category == "🔍 Searching":
            st.session_state["array"] = sorted(random.sample(range(1, 101), array_size))
        else:
            st.session_state["array"] = random.sample(range(1, 101), array_size)

    # Complexity quick-ref card
    st.markdown("<div class='sb-divider'></div>", unsafe_allow_html=True)
    complexity_info = {
        "Bubble Sort":        ("O(n)",      "O(n²)",     "O(n²)",     "O(1)"),
        "Selection Sort":     ("O(n²)",     "O(n²)",     "O(n²)",     "O(1)"),
        "Insertion Sort":     ("O(n)",      "O(n²)",     "O(n²)",     "O(1)"),
        "Merge Sort":         ("O(n log n)","O(n log n)","O(n log n)","O(n)"),
        "Quick Sort":         ("O(n log n)","O(n log n)","O(n²)",     "O(log n)"),
        "Heap Sort":          ("O(n log n)","O(n log n)","O(n log n)","O(1)"),
        "Linear Search":      ("O(1)",      "O(n)",      "O(n)",      "O(1)"),
        "Binary Search":      ("O(1)",      "O(log n)",  "O(log n)",  "O(1)"),
        "Jump Search":        ("O(1)",      "O(√n)",     "O(√n)",     "O(1)"),
        "Exponential Search": ("O(1)",      "O(log n)",  "O(log n)",  "O(log n)"),
    }
    b, av, w, sp = complexity_info.get(algo_name, ("–","–","–","–"))
    st.markdown(f"""
    <div class='sb-complexity'>
        <div class='sb-complexity-title'>⏱ Complexity — {algo_name}</div>
        <div class='sb-row'><span class='sb-key'>Best</span><span class='sb-val-best'>{b}</span></div>
        <div class='sb-row'><span class='sb-key'>Average</span><span class='sb-val-avg'>{av}</span></div>
        <div class='sb-row'><span class='sb-key'>Worst</span><span class='sb-val-worst'>{w}</span></div>
        <div class='sb-row'><span class='sb-key'>Space</span><span class='sb-val-space'>{sp}</span></div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# HERO BANNER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class='ave-hero'>
  <div class='hero-tag'>⚙️ &nbsp;v2.0 · Interactive Engine</div>
  <h1>Algorithm Visualizer Engine</h1>
  <p class='hero-sub'>
    Watch sorting &amp; searching algorithms come alive — step-by-step animation,<br>
    live statistics, and source code in 5 languages side by side.
  </p>
  <div class='hero-badges'>
    <span class='hero-badge'>🔀 6 Sorting Algorithms</span>
    <span class='hero-badge'>🔍 4 Search Algorithms</span>
    <span class='hero-badge'>💻 Python · Java · C · C++ · JS</span>
    <span class='hero-badge'>📊 Complexity Charts</span>
    <span class='hero-badge'>⚡ Live Step Metrics</span>
  </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────────────────────────────────────
tab_viz, tab_code, tab_compare = st.tabs(["🎬  Visualizer", "📄  Source Code", "📊  Complexity"])

# ── Colour palette ────────────────────────────────────────────────────────────
CLR = {
    "default":   "#5b21b6",
    "comparing": "#f59e0b",
    "swapping":  "#ef4444",
    "sorted":    "#10b981",
    "found":     "#06b6d4",
    "pivot":     "#ec4899",
    "range":     "#8b5cf6",
}

def draw_array(arr, highlights: dict = None, title="", step_info=""):
    highlights = highlights or {}
    n = len(arr)
    fig, ax = plt.subplots(figsize=(max(9, n * 0.58), 4.0))
    fig.patch.set_facecolor("#05050f")
    ax.set_facecolor("#09091a")

    colors = [highlights.get(i, CLR["default"]) for i in range(n)]

    for idx, (val, color) in enumerate(zip(arr, colors)):
        # Glow layer
        ax.bar(idx, val, color=color, width=0.78, alpha=0.15, edgecolor="none")
        # Main bar
        bar = ax.bar(idx, val, color=color, width=0.65, edgecolor=color,
                     linewidth=0.6, alpha=0.92)
        # Value label
        ax.text(idx, val + max(arr) * 0.02, str(val),
                ha="center", va="bottom", fontsize=7.5, color=color,
                fontfamily="monospace", fontweight="bold")

    ax.set_xlim(-0.75, n - 0.25)
    ax.set_ylim(0, max(arr) * 1.24)
    ax.set_xticks(range(n))
    ax.set_xticklabels([str(i) for i in range(n)],
                       fontsize=6.5, color="#252844", fontfamily="monospace")
    ax.tick_params(axis="y", colors="#252844", labelsize=6.5)
    for spine in ax.spines.values():
        spine.set_color("#0f0f24")
        spine.set_linewidth(0.7)
    ax.yaxis.grid(True, color="#0f0f24", linewidth=0.6, linestyle="--", alpha=0.6)
    ax.set_axisbelow(True)
    ax.set_title(title, color="#6b6e98", fontsize=10,
                 fontfamily="monospace", pad=10, fontweight="normal")
    if step_info:
        ax.text(0.5, -0.20, step_info, transform=ax.transAxes,
                ha="center", fontsize=7.5, color="#3e4265", fontfamily="monospace")
    plt.tight_layout()
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# VISUALIZER TAB
# ─────────────────────────────────────────────────────────────────────────────
with tab_viz:
    arr = st.session_state["array"]
    if len(arr) != array_size:
        arr = (sorted(random.sample(range(1, 101), array_size))
               if algo_category == "🔍 Searching"
               else random.sample(range(1, 101), array_size))
        st.session_state["array"] = arr

    _, col_btn, _ = st.columns([3, 1, 3])
    with col_btn:
        run_btn = st.button("▶  RUN", use_container_width=True)

    # Legend
    if algo_category == "🔀 Sorting":
        st.markdown("""<div class='legend'>
            <span><span class='dot' style='background:#5b21b6'></span>Default</span>
            <span><span class='dot' style='background:#f59e0b'></span>Comparing</span>
            <span><span class='dot' style='background:#ef4444'></span>Swapping</span>
            <span><span class='dot' style='background:#10b981'></span>Sorted</span>
            <span><span class='dot' style='background:#ec4899'></span>Pivot</span>
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class='legend'>
            <span><span class='dot' style='background:#5b21b6'></span>Default</span>
            <span><span class='dot' style='background:#f59e0b'></span>Checking</span>
            <span><span class='dot' style='background:#06b6d4'></span>Found</span>
            <span><span class='dot' style='background:#8b5cf6'></span>Range</span>
        </div>""", unsafe_allow_html=True)

    chart_slot = st.empty()
    info_slot  = st.empty()
    st.markdown("<br>", unsafe_allow_html=True)
    stat_c1, stat_c2, stat_c3 = st.columns(3)
    comp_slot = stat_c1.empty()
    swap_slot = stat_c2.empty()
    step_slot = stat_c3.empty()

    # Initial state
    chart_slot.pyplot(draw_array(arr, title=f"{algo_name}  ·  Initial Array"))
    comp_slot.markdown("<div class='metric-card'><div class='metric-label'>Comparisons</div><div class='metric-value'>0</div></div>", unsafe_allow_html=True)
    swap_slot.markdown("<div class='metric-card'><div class='metric-label'>Swaps / Ops</div><div class='metric-value'>0</div></div>", unsafe_allow_html=True)
    step_slot.markdown("<div class='metric-card'><div class='metric-label'>Steps</div><div class='metric-value'>0</div></div>", unsafe_allow_html=True)

    if run_btn:
        arr_copy    = arr.copy()
        comparisons = 0
        swaps       = 0

        if algo_category == "🔀 Sorting":
            fn_map = {
                "Bubble Sort":    bubble_sort_steps,
                "Selection Sort": selection_sort_steps,
                "Insertion Sort": insertion_sort_steps,
                "Merge Sort":     merge_sort_steps,
                "Quick Sort":     quick_sort_steps,
                "Heap Sort":      heap_sort_steps,
            }
            steps = fn_map[algo_name](arr_copy.copy())
        else:
            target = int(search_target)
            fn_map = {
                "Linear Search":      linear_search_steps,
                "Binary Search":      binary_search_steps,
                "Jump Search":        jump_search_steps,
                "Exponential Search": exponential_search_steps,
            }
            steps = fn_map[algo_name](arr_copy.copy(), target)

        for i, step in enumerate(steps):
            current_arr  = step.get("array", arr_copy)
            highlights   = step.get("highlights", {})
            description  = step.get("description", "")
            comparisons += step.get("comparisons", 0)
            swaps       += step.get("swaps", 0)

            chart_slot.pyplot(draw_array(
                current_arr, highlights,
                title=f"{algo_name}  ·  Step {i+1} / {len(steps)}",
                step_info=description
            ))
            info_slot.markdown(
                f"<div style='margin:10px 0'>"
                f"<span class='step-pill'>Step {i+1} / {len(steps)}</span>"
                f"<span class='step-desc-text'>{description}</span>"
                f"</div>",
                unsafe_allow_html=True
            )
            comp_slot.markdown(f"<div class='metric-card'><div class='metric-label'>Comparisons</div><div class='metric-value'>{comparisons}</div></div>", unsafe_allow_html=True)
            swap_slot.markdown(f"<div class='metric-card'><div class='metric-label'>Swaps / Ops</div><div class='metric-value'>{swaps}</div></div>", unsafe_allow_html=True)
            step_slot.markdown(f"<div class='metric-card'><div class='metric-label'>Steps</div><div class='metric-value'>{i+1}</div></div>", unsafe_allow_html=True)

            plt.close("all")
            time.sleep(delay)

        info_slot.success(f"✅  {algo_name} complete!   Comparisons: {comparisons}  |  Swaps / Ops: {swaps}")


# ─────────────────────────────────────────────────────────────────────────────
# SOURCE CODE TAB
# ─────────────────────────────────────────────────────────────────────────────
with tab_code:
    st.markdown(f"### 📄  {algo_name} — Source Code")
    st.markdown("<br>", unsafe_allow_html=True)
    lang_tabs = st.tabs(["🐍  Python", "☕  Java", "⚙️  C", "🔷  C++", "🌐  JavaScript"])
    for lang, lt in zip(["python", "java", "c", "cpp", "javascript"], lang_tabs):
        with lt:
            code = get_code(algo_name, lang)
            st.code(code, language="cpp" if lang in ("c", "cpp") else lang)


# ─────────────────────────────────────────────────────────────────────────────
# COMPLEXITY TAB
# ─────────────────────────────────────────────────────────────────────────────
with tab_compare:
    st.markdown("### 📊  Algorithm Complexity Comparison")
    st.markdown("<br>", unsafe_allow_html=True)

    if algo_category == "🔀 Sorting":
        data = {
            "Algorithm":["Bubble","Selection","Insertion","Merge","Quick","Heap"],
            "Best":     ["O(n)","O(n²)","O(n)","O(n log n)","O(n log n)","O(n log n)"],
            "Average":  ["O(n²)","O(n²)","O(n²)","O(n log n)","O(n log n)","O(n log n)"],
            "Worst":    ["O(n²)","O(n²)","O(n²)","O(n log n)","O(n²)","O(n log n)"],
            "Space":    ["O(1)","O(1)","O(1)","O(n)","O(log n)","O(1)"],
            "Stable":   ["✅","❌","✅","✅","❌","❌"],
        }
    else:
        data = {
            "Algorithm":     ["Linear","Binary","Jump","Exponential"],
            "Best":          ["O(1)","O(1)","O(1)","O(1)"],
            "Average":       ["O(n)","O(log n)","O(√n)","O(log n)"],
            "Worst":         ["O(n)","O(log n)","O(√n)","O(log n)"],
            "Space":         ["O(1)","O(1)","O(1)","O(log n)"],
            "Needs Sorted":  ["❌","✅","✅","✅"],
        }

    rows    = list(zip(*data.values()))
    headers = list(data.keys())
    header_html = "".join(f"<th>{h}</th>" for h in headers)
    rows_html   = "".join(
        "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
        for row in rows
    )
    st.markdown(f"""
    <table class='complexity-table'>
      <thead><tr>{header_html}</tr></thead>
      <tbody>{rows_html}</tbody>
    </table>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("### 📈  Time Complexity Growth Curve")
    st.markdown("<br>", unsafe_allow_html=True)

    ns  = np.array([10, 50, 100, 200, 500, 1000])
    fig2, ax2 = plt.subplots(figsize=(10, 4.5))
    fig2.patch.set_facecolor("#05050f")
    ax2.set_facecolor("#09091a")

    if algo_category == "🔀 Sorting":
        ax2.plot(ns, ns**2,          color="#ef4444", label="O(n²) — Bubble / Selection / Insertion",
                 linewidth=2.2, marker="o", markersize=4)
        ax2.plot(ns, ns*np.log2(ns), color="#10b981", label="O(n log n) — Merge / Quick / Heap",
                 linewidth=2.2, marker="o", markersize=4)
    else:
        ax2.plot(ns, ns,           color="#ef4444", label="O(n) — Linear Search",    linewidth=2.2, marker="o", markersize=4)
        ax2.plot(ns, np.sqrt(ns),  color="#f59e0b", label="O(√n) — Jump Search",     linewidth=2.2, marker="o", markersize=4)
        ax2.plot(ns, np.log2(ns),  color="#10b981", label="O(log n) — Binary / Exp", linewidth=2.2, marker="o", markersize=4)

    ax2.legend(fontsize=8.5, facecolor="#09091a", edgecolor="#1a1a35",
               labelcolor="#8892b4", loc="upper left", framealpha=0.9)
    ax2.set_xlabel("Input Size  n", color="#3e4265", fontsize=9, labelpad=8)
    ax2.set_ylabel("Operations",    color="#3e4265", fontsize=9, labelpad=8)
    ax2.tick_params(colors="#252844", labelsize=7.5)
    for spine in ax2.spines.values():
        spine.set_color("#0f0f24")
    ax2.yaxis.grid(True, color="#0f0f24", linewidth=0.7, linestyle="--", alpha=0.7)
    ax2.set_axisbelow(True)
    ax2.set_title("Operations vs Input Size", color="#5a5e80", fontsize=11,
                  fontfamily="monospace", pad=12)
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)