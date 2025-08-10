🏫 Class Monitor Selection Problem
📜 Problem Statement
After JEE Mains, some students got admission into an engineering college.
In one class of such n students, the HOD needs to select a class monitor.

However, the HOD never meets all the students at once. He keeps a register to note their names and ranks:

Every time he meets a student with a rank lower than the last recorded rank,
he cuts the previous name and writes down the new student's name and rank.

Your task is:
Given the sequence of ranks the HOD gets each time, predict how many names are cut in the list.

📌 Constraints
Number of Visits ≤ 10<sup>9</sup>

Rank ≤ 10000

📥 Input Format
First line → Number of Visits N

Second line → N space-separated integers representing the ranks received in order

📤 Output Format
Single integer → Number of ranks cut in the list

💡 Example
Input

Copy
Edit
6
4 3 7 2 6 1
Output

Copy
Edit
3
🧠 Explanation
The ranks received are: 4 3 7 2 6 1

Start with rank 4 → nothing cut yet

3 is less than 4 → cut previous, count = 1

7 is greater → no cut

2 is less than 7 → cut previous, count = 2

6 is greater → no cut

1 is less than 6 → cut previous, count = 3

✅ Final Answer: 3
