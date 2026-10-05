print("TASK 9: For Loop (Multiplication Table)")
print("=" * 50)

table_num = int(input("Enter a number for multiplication table: "))

for i in range(1, 11):
    print(f"{table_num} × {i} = {table_num * i}")
    