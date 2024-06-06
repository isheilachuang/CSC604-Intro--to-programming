def paint_cost(length, breadth, cost_per_sq_unit=20):
    area = length * breadth
    total_cost = cost_per_sq_unit * area
    return total_cost

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
cost_per_sq_unit = float(input("Enter the cost per square unit (default is 20): ") or 20)

total_cost = paint_cost(length, breadth, cost_per_sq_unit)

print(f"The total cost to paint the rectangle is: ${total_cost:.2f}")
