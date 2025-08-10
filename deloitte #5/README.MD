# 💤 Lazy String

## 📜 Problem Statement

Anish is the **laziest person** you can ever meet.  
He is tasked with writing the **name of the winner** in a game where two people take part.  

Instead of typing the entire name, he writes the **Longest Common Subsequence (LCS)** between the two names.  
This way, with minimal changes or no backspacing, he can edit it to match the winner's name.

For two given names, your task is to **predict what Anish will write** before the game's result is known.

If there are **multiple** LCS sequences of the **same maximum length**, choose the **lexicographically smallest** one.

---

## 📥 Input Format

- Two lines, each containing a name (all uppercase letters `A–Z`).

---

## 📤 Output Format

- A single line containing the **lexicographically smallest LCS**.

---

## 📏 Constraints

- \( 1 \leq \text{length of each string} \leq 1000 \)
- Only uppercase English letters (`A–Z`).

---

## 🧮 Example

### **Sample Input**
ABCD
BACD

markdown
Copy
Edit

### **Sample Output**
ACD
