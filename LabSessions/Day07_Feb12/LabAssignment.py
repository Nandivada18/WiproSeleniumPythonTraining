def make_it_equal(A, B):
    i = 0
    # Find longest common prefix
    while i < len(A) and i < len(B) and A[i] == B[i]:
        i += 1
    # Remaining characters to remove
    operations = (len(A) - i) + (len(B) - i)
    return str(operations)

# non editable starts here
if __name__ == "__main__":
    A = input().strip()
    B = input().strip()
    print(make_it_equal(A, B))
# non editable ends here