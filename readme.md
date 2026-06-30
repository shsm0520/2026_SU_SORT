# UC Summer 2026 - Sorting Algorithms

This repository contains various sorting algorithms implemented in Python during the 2026 UC Summer semester. The goal of this project was to understand the underlying mechanics, time complexities, and structures of both comparison-based and non-comparison-based sorting techniques.

## Implemented Algorithms

* **Insertion Sorts**
  - Implementations of Insertion sort

* **Merge Sort**
  - A divide-and-conquer implementation achieving stable $O(N \log N)$ time complexity.

* **Binary Heap Sort (Max / Min Heap)**
  - Array-based complete binary tree structures implementing both Max-Heap and Min-Heap properties for efficient priority-based sorting.

* **Comparison Sort by Unit Digit (1s Place)**
  - A specialized comparison sort focusing strictly on the ones-place digit, serving as a stepping stone for digit-by-digit sorting logic.

* **Radix Sort**
  - A non-comparison-based sorting algorithm that processes numbers digit by digit, achieving $O(dN)$ time complexity.

## How to Run / Test
You can run the sorting scripts using Python 3:

```bash
# Run a specific sorting script (e.g., merge sort)
python merge_sort.py
```


```bash
# calculate the resource check the batch number and repeat#
python calculate.py
```



observation of experiment

```bash
===========================================================================================================================================================
                                                  FINAL SORTING BENCHMARK ENSEMBLE REPORT (AVERAGED DATA)                                                  
===========================================================================================================================================================
Algorithm    | Size 10        | Size 100         | Size 1000          | Size 10000           | Instantaneous Slopes & Area Growth (d/dx)                   
-----------------------------------------------------------------------------------------------------------------------------------------------------------
Merge Sort   | 22.6 (1.83K)   | 543.3 (2.95K)    | 8701.3 (16.88K)    | 120446.2 (159.01K)   | d(Ops)/dx: 12.42 | d(Mem)/dx: 0.0158 | d(Area)/dx: 2124.12  
Radix Sort   | 10.0 (2.66K)   | 100.0 (23.37K)   | 1000.0 (232.44K)   | 10000.0 (2424.41K)   | d(Ops)/dx: 1.00 | d(Mem)/dx: 0.2436 | d(Area)/dx: 2668.96   
Max Heap     | 38.3 (1.07K)   | 1029.2 (2.52K)   | 16847.7 (9.30K)    | 235370.4 (84.90K)    | d(Ops)/dx: 24.28 | d(Mem)/dx: 0.0084 | d(Area)/dx: 2227.25  
Min Heap     | 37.8 (0.44K)   | 1026.8 (1.03K)   | 16857.6 (8.69K)    | 235376.4 (80.03K)    | d(Ops)/dx: 24.28 | d(Mem)/dx: 0.0079 | d(Area)/dx: 2100.93  
Insertion    | 28.9 (0.09K)   | 2425.1 (0.10K)   | 250882.3 (0.18K)   | 25016494.5 (0.18K)   | d(Ops)/dx: 2751.73 | d(Mem)/dx: 0.0000 | d(Area)/dx: 3256.94
1st Digit CS | 10.0 (1.83K)   | 100.0 (13.62K)   | 1000.0 (134.15K)   | 10000.0 (1333.92K)   | d(Ops)/dx: 1.00 | d(Mem)/dx: 0.1333 | d(Area)/dx: 1468.23   
===========================================================================================================================================================
                      Note: All cell values and slopes are averages calculated over 10 independent executions. Area = Ops * (Mem + 1)                      
===========================================================================================================================================================
                                                  SWEET SPOT ANALYSIS BY DATA SCALE (EXCLUDING 1st Digit)                                                  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
 * Size 10    Winner: >>> Insertion       <<< (Averaged Area Score: 31.61)
 * Size 100   Winner: >>> Min Heap        <<< (Averaged Area Score: 2087.59)
 * Size 1000  Winner: >>> Merge Sort      <<< (Averaged Area Score: 155565.48)
 * Size 10000 Winner: >>> Min Heap        <<< (Averaged Area Score: 19071740.59)
===========================================================================================================================================================


=========================================================================================================================================================================================================================================
                                                                                         FINAL SORTING BENCHMARK ENSEMBLE REPORT (AVERAGED DATA)                                                                                         
=========================================================================================================================================================================================================================================
Algorithm    | Size 10        | Size 100         | Size 1000          | Size 10000           | Size 100000            | Size 1000000             | Slopes & Area Growth & Weighted Area Growth (d/dx)                                    
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Merge Sort   | 25.0 (4.30K)   | 540.0 (5.02K)    | 8718.0 (17.58K)    | 120451.0 (158.49K)   | 1536492.0 (1572.68K)   | 18674518.0 (15636.98K)   | d(Ops)/dx: 19.04 | d(Mem)/dx: 0.0156 || d(Area)/dx: 321793.11 || d(W_Area)/dx: 3236.78
Radix Sort   | 10.0 (3.98K)   | 100.0 (23.37K)   | 1000.0 (232.68K)   | 10000.0 (2422.34K)   | 100000.0 (24220.02K)   | 1000000.0 (242623.39K)   | d(Ops)/dx: 1.00 | d(Mem)/dx: 0.2427 || d(Area)/dx: 266891.43 || d(W_Area)/dx: 2669.90 
Max Heap     | 40.0 (3.45K)   | 1033.0 (3.87K)   | 16821.0 (10.14K)   | 235515.0 (84.89K)    | 3019753.0 (789.64K)    | 36794557.0 (7822.46K)    | d(Ops)/dx: 37.53 | d(Mem)/dx: 0.0078 || d(Area)/dx: 317192.49 || d(W_Area)/dx: 3209.08
Min Heap     | 38.0 (1.24K)   | 1028.0 (1.19K)   | 16869.0 (8.27K)    | 235303.0 (78.80K)    | 3020115.0 (789.64K)    | 36794303.0 (7822.46K)    | d(Ops)/dx: 37.53 | d(Mem)/dx: 0.0078 || d(Area)/dx: 317189.96 || d(W_Area)/dx: 3209.05
1st Digit CS | 10.0 (2.17K)   | 100.0 (13.62K)   | 1000.0 (134.26K)   | 10000.0 (1333.93K)   | 100000.0 (13282.80K)   | 1000000.0 (133248.68K)   | d(Ops)/dx: 1.00 | d(Mem)/dx: 0.1333 || d(Area)/dx: 146579.22 || d(W_Area)/dx: 1466.78 
=========================================================================================================================================================================================================================================
                                                                             Note: Area = Ops * (Mem + 1) | Weighted Area (W_Area) = Ops * (Mem * 0.01 + 1)                                                                              
=========================================================================================================================================================================================================================================
                                                                                                 DATA SCALE SWEET SPOT (PURE AREA COST)                                                                                                  
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 * Size 10    Optimal Choice: >>> Radix Sort      <<< (Pure Area Score: 49.84)
 * Size 100   Optimal Choice: >>> Min Heap        <<< (Pure Area Score: 2251.76)
 * Size 1000  Optimal Choice: >>> Min Heap        <<< (Pure Area Score: 156301.83)
 * Size 10000 Optimal Choice: >>> Min Heap        <<< (Pure Area Score: 18776444.08)
 * Size 100000 Optimal Choice: >>> Max Heap        <<< (Pure Area Score: 2387539399.27)
 * Size 1000000 Optimal Choice: >>> Radix Sort      <<< (Pure Area Score: 242624390625.00)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                          WEIGHTED DATA SCALE SWEET SPOT (HARDWARE-AWARE COST)                                                                                           
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 * Size 10    Optimal Choice: >>> Radix Sort      <<< (Weighted Area Score: 10.40)
 * Size 100   Optimal Choice: >>> Radix Sort      <<< (Weighted Area Score: 123.37)
 * Size 1000  Optimal Choice: >>> Radix Sort      <<< (Weighted Area Score: 3326.77)
 * Size 10000 Optimal Choice: >>> Radix Sort      <<< (Weighted Area Score: 252234.38)
 * Size 100000 Optimal Choice: >>> Radix Sort      <<< (Weighted Area Score: 24320015.62)
 * Size 1000000 Optimal Choice: >>> Radix Sort      <<< (Weighted Area Score: 2427233906.25)
=========================================================================================================================================================================================================================================
