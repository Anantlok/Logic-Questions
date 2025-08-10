# Question 2 : Corona for Computer

## Problem Statement
Every decimal number can be changed into its binary form. Suppose your computer has its own **CoronaVirus**,  
that eats binary digits from the right side of a number.  

If the virus has `n` spikes, it will eat up `n` **LSB** (least significant binary) digits of the number.  

You will be given:
- A bunch of numbers
- The number of spikes in the virus

You have to calculate the **final values** after the virus eats the binary digits.

---

## Input Format
1. First line: A single integer `N` — the number of elements.  
2. Second line: `N` space-separated integers representing the array `V`.  
3. Third line: A single integer `n` — the number of spikes.

---

## Output Format
- `N` space-separated integers denoting the transformed array after removing binary digits.

---

## Constraints
- `1 ≤ N ≤ 10^5`
- `0 ≤ V[i] ≤ 10^9`
- `0 ≤ n ≤ 31`

---

## Sample Input
