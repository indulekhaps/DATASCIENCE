# Input the list of numbers from the user
elements = []
num_elements = int(input("Enter the number of elements: "))

print("Enter the elements:")
for i in range(num_elements):
    elements.append(int(input()))

print("Original array:", elements)

n = len(elements)

# Bubble sort algorithm
for i in range(n):
    # Last i elements are already in place
    for j in range(0, n-i-1):
        # Swap if the element found is greater than the next element
        if elements[j] > elements[j+1]:
            elements[j], elements[j+1] = elements[j+1], elements[j]

print("Sorted array:", elements)