input = input("Enter the price: ")
input = discount_percent = input("Enter the discount percent: ")
price = float(input)


calculate_discount(price, discount_percent){
    if price < 0 {
        discount = discount_percent / 100 * price
        discounted_price = price - discount
        print("Discounted price: ", discounted_price)
    }else {
        print("Price : ", price)
    }
}