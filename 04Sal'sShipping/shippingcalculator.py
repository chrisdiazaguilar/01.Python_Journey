
"""First things first, define a weight variable and set it equal to any number."""
weight = 4.8

"""
Next, we need to know how much it costs to ship a package of given weight by normal ground shipping based on the 
“Ground shipping” table above.

Write a comment that says “Ground Shipping”.

Create an if/elif/else statement for the cost of ground shipping. It should check for weight, and print the cost of 
shipping a package of that weight.
"""
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20


"""
A package that weighs 8.4 pounds should cost $53.60 to ship with normal ground shipping:

8.4 lb×$4.00+$20.00=$53.60

Test that your ground shipping calculation gets the same value.
"""

print("Ground Shipping $", cost_ground)

"""
We’ll also need to make sure we include the price of premium ground shipping in our code.

Create a variable for the cost of premium ground shipping.

Note: This does not need to be an if statement because the price of premium ground shipping does not change 
with the weight of the package.
"""

ground_shipping_premium = cost_ground + 125

total_with_premium_shipping = print("Ground Shipping Premium $", ground_shipping_premium)

"""

Write a comment for this section of the code, “Drone Shipping”.

Create an if/elif/else statement for the cost of drone shipping. This statement should check against weight 
and print the cost of shipping a package of that weight.
"""

if weight <= 2:
  cost_drone = weight * 4.50
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25

print("Drone shopping $", cost_drone)

"""
A package that weighs 1.5 pounds should cost $6.75 to ship by drone:
1.5 lb×$4.50+$0.00=$6.75
"""