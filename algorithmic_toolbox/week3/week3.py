

# greedy algorithm of maximizing
def maximizing_loot(dictionary_of_prices_and_weights, knapsack_capacity):
    capacity = 0
    price = 0
    # Creating a sorted list of items based on the value-to-weight ratio (value per unit weight)
    sorted_dpw = sorted(dictionary_of_prices_and_weights.items(),
                        key=lambda item: item[1][0] / item[1][1],
                        reverse=True)

    # Iterating through the sorted list
    for item, (value, weight) in sorted_dpw:
        if capacity == knapsack_capacity:
            break
        # Calculate the amount of weight we can still add
        can_add = min(weight, knapsack_capacity - capacity)
        # Increase the capacity used in the knapsack
        capacity += can_add
        # Increase the price by the proportionate value of the amount we can add
        price += value * (can_add / weight)

    print(f'the maximum price is : {price}')
    print(f'the capacity is : {capacity}')

# Example usage
dictionary_of_prices_and_weights = {
    'item1': (100, 20),  # (price, weight)
    'item2': (60, 10),
    'item3': (120, 30)
}
knapsack_capacity = 40
maximizing_loot(dictionary_of_prices_and_weights, knapsack_capacity)


  







