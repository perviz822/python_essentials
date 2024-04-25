

# greedy
def  maximizing_loot(dictionary_of_prices_and_weights, knapsack_capacity):
 price=0
 dpw =  dictionary_of_prices_and_weights;
 capacity=0
 sorted_dpw =  sorted(dpw.items(),key= lambda item :item[0])
 for item in sorted_dpw:
     if capacity <=knapsack_capacity:
      price +=min(knapsack_capacity-capacity,item[1])*(item[0]//item[1])
      print(price)
     capacity+=item[1]
     
  
 print('the maximum price is : {}'.format(price))








d1  = {45:3,32:4,48:12}
maximizing_loot(d1,9)
