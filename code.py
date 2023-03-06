import numpy as np


def evaluate_polynomial(coefficients, s):
    """Fungsi polinomial dengan parameter sebuah koefisien saat s"""
    result = 0
    for i in range(len(coefficients)):
        result += coefficients[i] * (s ** (len(coefficients) - i - 1))
    return result


def routh_stability(coefficients, K):
    """Fungsi komputasi dan menampilkan Routh table untuk persamaan polinomial dengan nilai koefisien dan K"""
    n = len(coefficients)
    table = np.zeros((n, (n+1)//2))
    table[0, :] = coefficients[::2]
    table[1, :] = coefficients[1::2]
    for i in range(2, n):
        for j in range((n+1)//2):
            if j == 0:
                table[i, j] = -1 / table[i-1, 1] * \
                    (table[i-2, 0] * (K if i == n-1 else 1) -
                     table[i-1, 1] * table[i-2, j+1])
            else:
                table[i, j] = -1 / table[i-1, 1] * \
                    (table[i-2, j-1] * (K if i == n-1 else 1) -
                     table[i-1, 1] * table[i-2, j])
    return table


# Contoh
coefficients = [1, 3, 3, 1]

# Polinomial saat s = 2
s = 2
value = evaluate_polynomial(coefficients, s)
print(f"Persamaan polinomial saat s = {s}, adalah {value}")

# Input nilai K dari user
K = float(input("Input nilai K: "))

# Komputasi dan menampilkan Routh table
table = routh_stability(coefficients, K)
print("Routh table:")
print(table)

# Input nilai K yang baru untuk user
K = float(input("Input nilai K: "))
table = routh_stability(coefficients, K)
print(f"Routh table dengan nilai K = {K}, adalah ")
print(table)
