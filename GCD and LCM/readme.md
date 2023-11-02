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


# LCM of Two Numbers

Based upon a very simple approach

 a x b = LCM(a, b) * GCD (a, b)

 LCM(a, b) = (a x b) / GCD(a, b)

# Euler's Totient Function
The Euler's Totient Function (φ) counts the number of positive integers less than or equal to a given number (n) that are relatively prime to n, meaning they do not share any common factors other than 1.

So, in the case of φ(10):

1 is relatively prime to 10 because they share no common factors other than 1.

2 is not relatively prime to 10 because they share a common factor of 2.

3 is relatively prime to 10.

4 is not relatively prime to 10 because they share a common factor of 2.

5 is not relatively prime to 10 because they share a common factor of 5.

6 is not relatively prime to 10 because they share a common factor of 2.


7 is relatively prime to 10.

8 is not relatively prime to 10 because they share a common factor of 2.

9 is relatively prime to 10.

So, φ(10) is the count of numbers that are relatively prime to 10, which is 4: 1, 3, 7, and 9.
