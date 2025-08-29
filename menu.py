Peach_tea = ['Peach tea', 7.65]

ordered_items = []

def menu():
    print('Please select an option below to place an order!')
    print('')
    print(f'1.{Peach_tea[0]} for {Peach_tea[1]} ')
    print('2. Finish Order.')

def customer_order():
   order = input('What would you like to order?')
   order = int(order)

   if order == 1:
       sugar = input('How much sugar %: 30, 50, 100?')
       ice = input('How much ice %: 30, 50, 100.')
    
print('Welcome to Boba Brothers!')
menu()
customer_order()
