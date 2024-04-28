

# greedy
def  maximizing_loot(dictionary_of_prices_and_weights, knapsack_capacity):
 price=0
 dpw =  dictionary_of_prices_and_weights;
 capacity=0
 sorted_dpw =  sorted(dpw.items(),key= lambda item :item[0]/item[1],reverse=True)
 print(sorted_dpw)
 for item in sorted_dpw:
     if capacity == knapsack_capacity:
      quit()
     price +=min(knapsack_capacity-capacity,item[1])*(item[0]/item[1])
     print(price)
     capacity+=item[1]
     
  
 print('the maximum price is : {}'.format(price))






d1  = {5:45,32:2,48:1}
maximizing_loot(d1,10)
