'''
Real scenarios where tuples are essential:

Using composite keys in dictionaries or sets.

Returning multiple fixed values from a function.

Representing fixed records (coordinates, RGB).

Sorting or ordering by multiple criteria.

Efficiently handling fixed-length data that should be immutable.




Your job is to:

Read the CSV file.

Identify users who have submitted more than one review for the same product.

Return a dictionary where the keys are tuples (product_id, user_id) and the values are the count of reviews that user made for that product.

'''






import pandas as pd
import csv

user_review_counts ={}

with open('tuples/product_reviews.csv','r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
      key = (row[0],row[1])
      if  key in user_review_counts:
         user_review_counts[key]  +=1
      else:
         user_review_counts[key]  = 1  

print(user_review_counts)

         



