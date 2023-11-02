# Euclidean algorithm for GCD 
Let's say you want to find the GCD of two numbers, A and B. Here are the steps:

Start with your two numbers, A and B.

Divide the larger number by the smaller number. If A is greater than B, then calculate A divided by B. If B is greater than A, then calculate B divided by A.

Take the remainder of the division.

Replace the larger number with the smaller number and the smaller number with the remainder from step 3.

Repeat steps 2-4 until the remainder is 0. When the remainder becomes 0, the last non-zero remainder is the GCD of A and B.

## Example
Step 1: A = 48, B = 18

Step 2: Divide 48 by 18, and you get a quotient of 2 and a remainder of 12.

Step 3: Replace A with 18 and B with 12.

Step 4: A = 18, B = 12

Step 2: Divide 18 by 12, and you get a quotient of 1 and a remainder of 6.

Step 3: Replace A with 12 and B with 6.

Step 4: A = 12, B = 6

Step 2: Divide 12 by 6, and you get a quotient of 2 and a remainder of 0.

Since the remainder is now 0, the GCD of 48 and 18 is the last non-zero remainder, which is 6.
