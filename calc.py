def calculate_discount(price, discount_percent):
    if discount_percent >= 20 :
        discount = (discount_percent / 100) * price
        return price - discount        
    else :
        return price

price_input = input("Enter the original price: ")
discount_input = input("Enter the discount percent: ") 

price = float(price_input)
discount_percent = float(discount_input)

final_price = calculate_discount(price, discount_percent)

print("Final price:", final_price)

