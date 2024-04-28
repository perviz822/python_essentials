from sys import stdin


def optimal_value(knapsack_capacity, weights, values):
    # Initialize total value to 0
    price = 0
    # Create a list of items with (value, weight) and sort by value-to-weight ratio
    items = [(values[i], weights[i]) for i in range(len(weights))]
    sorted_items = sorted(items, key=lambda item: item[0] / item[1], reverse=True)
    
    # Remaining capacity of the knapsack
    capacity = knapsack_capacity
    
    # Process each item in descending order of value-to-weight ratio
    for value, weight in sorted_items:
        if capacity == 0:
            break
        
        # Determine the amount of this item to take
        actual_weight = min(weight, capacity)
        price += actual_weight * (value / weight)
        capacity -= actual_weight
    
    return price




if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
