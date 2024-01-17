def calculate_discount(cart_total, quantities, wrapped_gifts):
    total_quantity = sum(quantities)
    discount = 0
    if cart_total > 200:
        discount = 10
    elif any(q > 10 for q in quantities):
        discount = 5
    elif total_quantity > 20:
        discount = 10
    elif total_quantity > 30 and any(q > 15 for q in quantities):
        discount = 50
    
    return discount

def calculate_cost(product_prices, quantities, wrapped_gifts):
    cart_total = sum(price * quantity for price, quantity in zip(product_prices, quantities))
    discount = calculate_discount(cart_total, quantities, wrapped_gifts)
    gift_wrap_fee = sum(wrapped_gifts) * 1
    shipping_fee = sum(quantities) // 10 * 5
    total_cost = cart_total - (cart_total * discount / 100) + shipping_fee + gift_wrap_fee
    return cart_total, discount, gift_wrap_fee, shipping_fee, total_cost
def main():
    num_products = int(input("Enter the number of products: ")) 
    product_prices = []
    quantities = []
    wrapped_gifts = []
    for i in range(num_products):
        product_name = input(f"Enter the name of product {i + 1}: ")
        price = float(input(f"Enter the price of {product_name}: "))
        quantity = int(input(f"Enter the quantity of {product_name}: "))
        wrapped_gift = input(f"Is {product_name} wrapped as a gift? (yes/no): ").lower() == "yes"
        product_prices.append(price)
        quantities.append(quantity)
        wrapped_gifts.append(wrapped_gift)
    cart_total, discount, gift_wrap_fee, shipping_fee, total_cost = calculate_cost(product_prices, quantities, wrapped_gifts)
    for i in range(len(product_prices)):
        print(f"Product {chr(65 + i)}: Quantity - {quantities[i]}, Total - {product_prices[i] * quantities[i]}")
    print(f"\nSubtotal: {cart_total}")
    print(f"Discount Applied: {discount}%")
    print(f"Gift Wrap Fee: {gift_wrap_fee}")
    print(f"Shipping Fee: {shipping_fee}")
    print(f"\nTotal: {total_cost}")
if __name__ == "__main__":
    main()