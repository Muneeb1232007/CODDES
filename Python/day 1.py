a=[12,456,6,5432132,45,65,43]
for index,marks in enumerate(a):
    print(f"Your index is {index} this and value is this {marks}")
for index,marks in enumerate(a,start=3):
    print(f"Your index is {index} this and value is this {marks}")
    if index==7:
        break