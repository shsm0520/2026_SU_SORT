import tracemalloc
import random
from unicodedata import digit

# Import all sorting algorithms from your separate files
from merge_sort import merge_sort
from radix_sort import radix_sort
from max_min_heap_sort import maxheap_sort, minheap_sort
from insrtion_sort import insertion_sort
from compairson_sort_unit_digit import first_digit_counting_sort

# -------------------------------------------------------------
# Step Counter and Tracked Object Infrastructure
# -------------------------------------------------------------
class StepCounter:
    def __init__(self):
        self.count = 0
    def reset(self):
        self.count = 0
    def increment(self):
        self.count += 1

counter = StepCounter()

class TrackedNumber:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        counter.increment()
        return str(self.value)
    def __lt__(self, other):
        counter.increment()
        return self.value < other.value
    def __le__(self, other):
        counter.increment()
        return self.value <= other.value
    def __gt__(self, other):
        counter.increment()
        return self.value > other.value
    def __ge__(self, other):
        counter.increment()
        return self.value >= other.value
    def __index__(self):
        return self.value

# -------------------------------------------------------------
# Performance Measurement Engine
# -------------------------------------------------------------
def measure_algorithm(sort_function, raw_data):
    tracked_data = [TrackedNumber(x) for x in raw_data]
    counter.reset()
    
    tracemalloc.start()
    try:
        sort_function(tracked_data)
    except Exception as e:
        tracemalloc.stop()
        return "ERROR", "ERROR"
        
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return counter.count, peak / 1024

# -------------------------------------------------------------
# Main Execution Control (Ensemble Average Benchmark)
# -------------------------------------------------------------
if __name__ == "__main__":
    execution_sizes = [10, 100, 1000, 10000, 100000, 1000000]
    RUN_COUNT = 1

    algorithms = {
        "Merge Sort": merge_sort,
        "Radix Sort": radix_sort,
        "Max Heap": maxheap_sort,
        "Min Heap": minheap_sort,
        # "Insertion": insertion_sort,
        "1st Digit CS": first_digit_counting_sort
    }

    results_sum = {size: {name: [0.0, 0.0] for name in algorithms} for size in execution_sizes}

    print(f"🚀 벤치마크 엔진 가동 (크기별 {RUN_COUNT}회 독립 반복 평균 계산)...", flush=True)

    for run in range(1, RUN_COUNT + 1):
        print(f" -> Running Iteration Round [{run}/{RUN_COUNT}]...")
        for size in execution_sizes:
            raw_test_data = [random.randint(1, 99999) for _ in range(size)]
            
            for name, sort_fn in algorithms.items():
                steps, memory = measure_algorithm(sort_fn, raw_test_data.copy())
                results_sum[size][name][0] += steps
                results_sum[size][name][1] += memory

    # Calculate final averages
    results_avg = {}
    for size in execution_sizes:
        results_avg[size] = {}
        for name in algorithms.keys():
            avg_steps = results_sum[size][name][0] / RUN_COUNT
            avg_memory = results_sum[size][name][1] / RUN_COUNT
            results_avg[size][name] = (avg_steps, avg_memory)

    # -------------------------------------------------------------
    # Calculate Slopes, Area Growth & Weighted Area Growth
    # -------------------------------------------------------------
    prev_size = execution_sizes[-2]
    last_size = execution_sizes[-1]
    delta_size = last_size - prev_size
    
    derivative_trends = {}
    for name in algorithms.keys():
        prev_steps, prev_mem = results_avg[prev_size][name]
        last_steps, last_mem = results_avg[last_size][name]
        
        # 1. Base Slopes
        step_slope = (last_steps - prev_steps) / delta_size
        mem_slope = (last_mem - prev_mem) / delta_size
        
        # 2. Pure Area Growth (Area = Ops * (Mem + 1))
        prev_area = prev_steps * (prev_mem + 1)
        last_area = last_steps * (last_mem + 1)
        area_slope = (last_area - prev_area) / delta_size
        
        # 3. Weighted Area Growth (W_Area = Ops * (Mem * 0.01 + 1))
        prev_w_area = prev_steps * (prev_mem * 0.01 + 1)
        last_w_area = last_steps * (last_mem * 0.01 + 1)
        w_area_slope = (last_w_area - prev_w_area) / delta_size
        
        # Combined dynamic text injection for the right column
        derivative_trends[name] = f"d(Ops)/dx: {step_slope:.2f} | d(Mem)/dx: {mem_slope:.4f} || d(Area)/dx: {area_slope:.2f} || d(W_Area)/dx: {w_area_slope:.2f}"

    # -------------------------------------------------------------
    # Dynamic Table Size Calculation ( 칼각 정렬 세팅 )
    # -------------------------------------------------------------
    algo_col_width = max(max(len(name) for name in algorithms.keys()), len("Algorithm"))
    trend_header_title = "Slopes & Area Growth & Weighted Area Growth (d/dx)"
    trend_col_width = max(max(len(trend) for trend in derivative_trends.values()), len(trend_header_title))
    
    size_col_widths = {}
    for size in execution_sizes:
        header_len = len(f"Size {size}")
        max_cell_len = header_len
        for name in algorithms.keys():
            steps, memory = results_avg[size][name]
            cell_data = f"{steps:.1f} ({memory:.2f}K)"
            if len(cell_data) > max_cell_len:
                max_cell_len = len(cell_data)
        size_col_widths[size] = max_cell_len + 2

    total_line_width = (algo_col_width + 3 + 
                        sum(size_col_widths[size] for size in execution_sizes) + 
                        (len(execution_sizes) * 3) + 
                        trend_col_width)

    # -------------------------------------------------------------
    # Render Master Table
    # -------------------------------------------------------------
    print("\n" + "=" * total_line_width)
    title = "FINAL SORTING BENCHMARK ENSEMBLE REPORT (AVERAGED DATA)"
    print(f"{title:^{total_line_width}}")
    print("=" * total_line_width)
    
    # Print Header
    header_str = f"{'Algorithm':<{algo_col_width}} | "
    for size in execution_sizes:
        header_str += f"{f'Size {size}':<{size_col_widths[size]}} | "
    header_str += f"{trend_header_title:<{trend_col_width}}"
    print(header_str)
    print("-" * total_line_width)

    # Print Rows
    for name in algorithms.keys():
        row_str = f"{name:<{algo_col_width}} | "
        for size in execution_sizes:
            steps, memory = results_avg[size][name]
            cell_data = f"{steps:.1f} ({memory:.2f}K)"
            row_str += f"{cell_data:<{size_col_widths[size]}} | "
        row_str += f"{derivative_trends[name]:<{trend_col_width}}"
        print(row_str)

    print("=" * total_line_width)
    note = f"Note: Area = Ops * (Mem + 1) | Weighted Area (W_Area) = Ops * (Mem * 0.01 + 1)"
    print(f"{note:^{total_line_width}}")
    print("=" * total_line_width)

    # -------------------------------------------------------------
    # 🌟 요청 반영 하단 분리 리포트 영역
    # -------------------------------------------------------------
    # Section 1: 데이터 스케일 스윗스팟 (Pure Area)
    print(f"{'  DATA SCALE SWEET SPOT (PURE AREA COST)  ':^{total_line_width}}")
    print("-" * total_line_width)
    for size in execution_sizes:
        best_algo_pure = None
        min_area_pure = float('inf')
        for name in algorithms.keys():
            if name == "1st Digit CS": continue
            steps, memory = results_avg[size][name]
            area_pure = steps * (memory + 1)
            if area_pure < min_area_pure:
                min_area_pure = area_pure
                best_algo_pure = name
        print(f" * Size {size:<5} Optimal Choice: >>> {best_algo_pure:<15} <<< (Pure Area Score: {min_area_pure:.2f})")
    
    print("-" * total_line_width)
    
    # Section 2: 가중치 데이터 스케일 스윗스팟 (Weighted Area)
    print(f"{'  WEIGHTED DATA SCALE SWEET SPOT (HARDWARE-AWARE COST)  ':^{total_line_width}}")
    print("-" * total_line_width)
    for size in execution_sizes:
        best_algo_weighted = None
        min_area_weighted = float('inf')
        for name in algorithms.keys():
            if name == "1st Digit CS": continue
            steps, memory = results_avg[size][name]
            area_weighted = steps * (memory * 0.01 + 1)
            if area_weighted < min_area_weighted:
                min_area_weighted = area_weighted
                best_algo_weighted = name
        print(f" * Size {size:<5} Optimal Choice: >>> {best_algo_weighted:<15} <<< (Weighted Area Score: {min_area_weighted:.2f})")
        
    print("=" * total_line_width)