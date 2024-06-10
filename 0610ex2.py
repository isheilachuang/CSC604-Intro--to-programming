def day_name(num):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    if 0 <= num <= 6:
        return days[num]
    else:
        return None


print(day_name(3))
print(day_name(6))
print(day_name(42))