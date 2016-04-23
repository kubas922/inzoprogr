def ciag_fibonacciego(n):
    if n > 1:
        return ciag_fibonacciego(n-1) + ciag_fibonacciego(n-2)
    else:
        return n

fibonacci = []
ilosc = int(input())

for i in range(ilosc):
    fibonacci.append(ciag_fibonacciego(i))

print (fibonacci)
