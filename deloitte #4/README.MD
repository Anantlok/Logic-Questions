# 💨 Total Momentum from a Linked List

## 📜 Problem Statement

Ratul made a **linked list** containing `n` nodes.  
Each node stores two values:

- **Velocity (v)**
- **Mass (m)**

Since all the particles move in the **same direction**,  
find the **total momentum** of the system formed by these particles.

---

## 📏 Constraints

- \( 1 \leq n \leq 10,000 \)  
- \( 1 \leq m, v \leq 100 \)

---

## 📥 Input Format

1. First line: integer `n` — the number of nodes  
2. Next `n` lines: two integers separated by a space — `m` (mass) and `v` (velocity)  

---

## 📤 Output Format

A single integer representing the **total momentum**.

---

## 🧮 Sample Input

4
1 3
2 4
2 3
4 5

yaml
Copy
Edit

---

## 📊 Sample Output

37

python
Copy
Edit

---

## 📖 Explanation

For each node, momentum is calculated as:

\[
p = m \times v
\]

| Node | Mass (m) | Velocity (v) | Momentum (m × v) |
|------|----------|--------------|------------------|
| 1    | 1        | 3            | 3                |
| 2    | 2        | 4            | 8                |
| 3    | 2        | 3            | 6                |
| 4    | 4        | 5            | 20               |

**Total Momentum** = 3 + 8 + 6 + 20 = **37**

---
