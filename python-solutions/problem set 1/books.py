'''
name:books.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:Suppose the cover price of a book is Rs.24.95, but bookstores get a 40% discount. Shipping costs
Rs.3 for the first copy and 0.75p for each additional copy. What is the total wholesale cost for
60 copies?
'''
def calculate_sp(n):
    sell_price=(24.95-(0.40*24.95))*n
    shipping_cost=3+(0.75*(n-1))
    total_price=sell_price+shipping_cost
    print total_price

num=int(raw_input("enter the no.of books:"))
calculate_sp(num)