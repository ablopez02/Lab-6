def first_letter(word):
    if word[0] == 'k':
        return True
    else:
        return False
print(first_letter('kello')) 
def fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer for n."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(4))
