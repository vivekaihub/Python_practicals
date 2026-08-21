print("===== ORDER TRACKING SYSTEM =====")

status = input("Enter order status (shipped/delivered/pending): ").lower()

if status == "shipped":
    print("Your order has been shipped and is on its way.")
elif status == "delivered":
    print("Your order has been delivered successfully.")
elif status == "pending":
    print("Your order is pending and will be processed soon.")
else:
    print("Invalid order status. Please enter shipped, delivered, or pending.")