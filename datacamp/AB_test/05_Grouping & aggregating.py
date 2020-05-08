# 05_Grouping & aggregating.py
# Instructions
# 100 XP
# - Group the purchase_data DataFrame by 'device' and 'gender' in that order.
# - Aggregate grouped_purchase_data, finding the 'mean', 'median', and the standard deviation ('std') of the purchase price, in that order, across these groups.
# - Examine the results. Does the mean differ drastically from the median? How much variability is in each group?

# Group the data 
grouped_purchase_data = purchase_data.groupby(by= ['device', 'gender'])

# Aggregate the data
purchase_summary = grouped_purchase_data.agg({'price': ['mean', 'median', 'std']})

# Examine the results
print(purchase_summary)

>> <script.py> output:
                        price                   
                         mean median         std
    device gender                               
    and    F       400.747504    299  179.984378
           M       416.237308    499  195.001520
    iOS    F       404.435330    299  181.524952
           M       405.272401    299  196.843197