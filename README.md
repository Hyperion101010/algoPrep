# algoPrep

## DS Algo
- 450 [list](https://drive.google.com/file/d/1FMdN_OCfOI0iAeDlqswCiC2DZzD4nPsb/view)

# List of solved problems.


## Resource
  - #### [Leetcode patterns](https://seanprashad.com/leetcode-patterns/)
  - #### [Errichto Binary Search](https://www.youtube.com/watch?v=GU7DpgHINWQ)
  - #### [Leetcode problem solving pattern](https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed)

## 1. Sliding window
  
  The Sliding Window pattern is used to perform a required operation on a specific window size of a given array or linked list. Sliding Windows start from the 1st element and keep shifting right by one element and adjust the length of the window according to the problem that you are solving. In some cases, the window size remains constant and in other cases the sizes grows or shrinks.
  
  Used when:
  The problem input is a linear data structure such as a linked list, array, or string
  You’re asked to find the longest/shortest substring, subarray, or a desired value
  Common problems you use the sliding window pattern with:
  
  1. Maximum sum subarray of size ‘K’ (easy)
  2. Longest substring with ‘K’ distinct characters (medium)
  3. String anagrams (hard)

  - #### How to solve sliding window blog [link](https://medium.com/outco/how-to-solve-sliding-window-problems-28d67601a66).
  - #### Sliding Window course [link](https://usaco.guide/gold/sliding-window/#sliding-window)

  - #### Problems solved
    - ##### [1876 Substring of size three](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/)
    - ##### [643 Maxsubarray](https://leetcode.com/problems/maximum-average-subarray-i/)
    - ##### [239 Sliding window max](https://leetcode.com/problems/sliding-window-maximum/)
    - ##### [219 Contains duplicate](https://leetcode.com/problems/contains-duplicate-ii/)
    - ##### [209 Min size subarray sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
    - ##### [1423 Max Points](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)
    - ##### [break][#]
    - ##### [1984 Minimum Difference Between Highest and Lowest of K Scores](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/?envType=problem-list-v2&envId=sliding-window)
    - ##### [594 Longest Harmonious Subsequence](https://leetcode.com/problems/longest-harmonious-subsequence/description/?envType=problem-list-v2&envId=sliding-window)
    - ##### [1652 Diffuse the Bomb](https://leetcode.com/problems/defuse-the-bomb/description/?envType=problem-list-v2&envId=sliding-window)

## 2. Two pointer

  Two Pointers is a pattern where two pointers iterate through the data structure in tandem until one or both of the pointers hit a certain condition.Two Pointers is often useful when searching pairs in a sorted array or linked list

  Used when:
  It will feature problems where you deal with sorted arrays (or Linked Lists) and need to find a set of elements that fulfill certain constraints
  The set of elements in the array is a pair, a triplet, or even a subarray
  Here are some problems that feature the Two Pointer pattern:
  1. Squaring a sorted array (easy)
  2. Triplets that sum to zero (medium)
  3. Comparing strings that contain backspaces (medium)
  
  - #### Problems solved
    - ##### [200 Reverse prefix of word](https://leetcode.com/problems/reverse-prefix-of-word/)
    - ##### [1877 Minmax pair sum](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/)
    - ##### [287 Find the duplicate](https://leetcode.com/problems/find-the-duplicate-number/)
    - ##### [763 Partition labels](https://leetcode.com/problems/partition-labels/)
    - ##### [15 Sum](https://leetcode.com/problems/3sum/)
    - ##### [16 3Sum closest](https://leetcode.com/problems/3sum-closest/)
    - ##### [75 sort colours](https://leetcode.com/problems/sort-colors/)
    - ##### [11 Container with most water](https://leetcode.com/problems/container-with-most-water/)
    - ##### [break - neetcode problems now]()
    - ##### [125 Valid Palindrome](https://leetcode.com/problems/valid-palindrome/submissions/1501204884/)
    - ##### [167 Two sum - Input is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

## 3. Modified Binary Search
  
  Whenever you are given a sorted array, linked list, or matrix, and are asked to find a certain element, the best algorithm you can use is the Binary Search. This pattern describes an efficient way to handle all problems involving Binary Search.
  
  - #### [Errichto Binary Search](https://www.youtube.com/watch?v=GU7DpgHINWQ)
  
  Used when:
  

  - #### Problems solved
    - ##### [704 Binary Search](https://leetcode.com/problems/binary-search)
    - ##### [378 Kth Smallest element in sorted matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix)
    - ##### [153 Find minimum in sorted array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array)
    - ##### [162 Find peak elements](https://leetcode.com/problems/find-peak-element/)
    - ##### [A Rank list codeforces](https://codeforces.com/contest/166/problem/A)

## 4. Dynamic Programming
  
  About 25% of all SRM problems have the "Dynamic Programming" category tag. The DP problems are popular among problemsetters because each DP problem is original in some sense and you have to think hard to invent the solution for it. Since dynamic programming is so popular, it is perhaps the most important method to master in algorithm competitions.
  
  Goal is to fix the overlapping problem of not recalculating states.
  
  1. Memoization (Top Down): The memoized program for a problem is similar to the recursive version with a small modification that looks into a lookup table before computing solutions. We initialize a lookup array with all initial values as NIL. Whenever we need the solution to a subproblem, we first look into the lookup table. If the precomputed value is there then we return that value, otherwise, we calculate the value and put the result in the lookup table so that it can be reused later.
  2. Tabulation (Bottom Up): The tabulated program for a given problem builds a table in bottom-up fashion and returns the last entry from the table. For example, for the same Fibonacci number, we first calculate fib(0) then fib(1) then fib(2) then fib(3), and so on. So literally, we are building the solutions of subproblems bottom-up.

  Optimal Substructure: A given problems has Optimal Substructure Property if optimal solution of the given problem can be obtained by using optimal solutions of its subproblems. 

  - #### DP from Novice to Advanced [link](https://www.topcoder.com/thrive/articles/Dynamic%20Programming:%20From%20Novice%20to%20Advanced)
  - #### Everything DP [link](https://codeforces.com/blog/entry/43256)
  - #### Top 20 DP [link](https://www.geeksforgeeks.org/top-20-dynamic-programming-interview-questions/)

  - #### Problems solved
    - ##### [70 Climbing stairs](https://leetcode.com/problems/climbing-stairs) 
    - ##### [121 Best time to buy and sell](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
    - ##### [53 Max subarray](https://leetcode.com/problems/maximum-subarray/) Complete this also
    - ##### [494 Target Sum](https://leetcode.com/problems/target-sum/) Try other DP approaches
    - ##### [198 House Robber](https://leetcode.com/problems/house-robber) Try simple iterative approach
    - ##### [5 Longest Pal substring](https://leetcode.com/problems/longest-palindromic-substring)

    DP set gfg
    
    - ##### [300 LIS](https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326552/Optimization-From-Brute-Force-to-Dynamic-Programming-Explained!) Need to try binary search approach and also understand dp[ind][previ] reason
    - ##### [1143 LCS](https://leetcode.com/problems/longest-common-subsequence/discuss/590781/From-Brute-Force-To-DP) Solved it.
    - ##### [72 Edit distance](https://leetcode.com/problems/edit-distance) solved it.
    - ##### [64 Minimum path sum](https://leetcode.com/problems/minimum-path-sum) understand it.

## 5. Uses of DS.

    - ## Map
      - To count occurences of elements
      - To count if element is repeated in given length string. mp.size and string length compare

## 6. Code snippet of implementations


  - #### LinkedList [replt](https://replit.com/@ShivamBalikondw/linkedlistclass#main.cpp)
