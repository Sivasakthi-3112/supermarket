import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
print("-------------------------")
print("Date:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("-------------------------")
items = []
gst_rate = 0.18  # Assuming 18% GST
discount_rate = 0.1  # 10% discount
def send_email(receiver_email, bill_amount):
    sender_email = "sathyagayu1976@gmail.com"  # Replace with your email address
    sender_password = "siva"  # Replace with your email password
    
    # Create the email content
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Your Supermarket Purchase Bill"
    body = f"Thank you for your purchase. The total amount of your bill is ${bill_amount}."
    message.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server and send the email
        server = smtplib.SMTP('gmail')  # Replace with your SMTP server and port
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

while True:
    display = input('Press enter to continue.')
    print('------------------Welcome to the supermarket------------------')
    print('1. View items\n2. Add items for sale\n3. Purchase items\n4. Search items \n5. Edit items\n6. Exit')
    choice = input('Enter the number of your choice : ')

    if choice == '1' :
        print('------------------View Items------------------')
        print('The number of items in the inventory are : ',len(items))
        while len(items) != 0:
            print('Here are all the items available in the supermarket.')
            for item in items:
                for key, value in item.items():
                    print(key, ':', value)
            break

    elif choice == '2' :
        print('------------------Add items------------------')
        print('To add an item fill in the form')
        item = {}
        item['name'] = input('Item name : ')
        while True:
            try:
                quantity= int(input('Item quantity : '))
                break
            except ValueError:
                print('Quantity should only be in digits')
        while True:
            try:
                price = int(input('Price $ : '))
                break
            except ValueError:
                print('Price should only be in digits')
        print('Item has been successfully added.')
        items.append(item)

    elif choice == '3' :
        print('------------------Purchase Items------------------')
        purchased_items = []
        total_amount = 0
        while True:
            print(items)
            purchase_item = input('Which item do you want to purchase? Enter name (or type "done" to finish): ')
            if purchase_item.lower() == 'done':
                break
            for item in items:
                if purchase_item.lower() == item['name'].lower():
                    if quantity != 0:
                        print('Pay $', price, 'at checkout counter.')
                        quantity -= 1
                        purchased_items.append(item)
                        total_amount += price
                    else: 
                        print('Item out of stock.')
                    break
            else:
                print('Item not found.')
        
        if total_amount > 0:
            print(f'The total amount of your bill is ${total_amount}.')
            gst_amount = total_amount* gst_rate
            discount_amount = total_amount * discount_rate
            total = total_amount + gst_amount - discount_amount
            print(f"GST (18%): Rs. {gst_amount:.2f}")
            print(f"Discount (10%): Rs. {discount_amount:.2f}")
            print("-------------------------")
            print(f"TOTAL: Rs. {total:.2f}")
            print("-------------------------")
            customer_email = input('Enter your email address to receive the bill: ')
            send_email(customer_email, total_amount)

    elif choice == '4' :
        print('------------------Search Items------------------')
        find_item = input('Enter the item\'s name to search in inventory: ')
        for item in items:
            if item['name'].lower() == find_item.lower():
                print('The item named ' + find_item + ' is displayed below with its details:')
                print(item)
                break
        else:
            print('Item not found.')

    elif choice == '5' :
        print('------------------Edit Items------------------')
        item_name = input('Enter the name of the item that you want to edit: ')
        for item in items:
            if item_name.lower() == item['name'].lower():
                print('Here are the current details of ' + item_name)
                print(item)
                item['name'] = input('Item name: ')
                while True:
                    try:
                        item['quantity'] = int(input('Item quantity: '))
                        break
                    except ValueError:
                        print('Quantity should only be in digits')
                while True:
                    try:
                        item['price'] = int(input('Price $: '))
                        break
                    except ValueError:
                        print('Price should only be in digits')
                print('Item has been successfully updated.')
                print(item)
                break
        else:
            print('Item not found.')

    elif choice == '6' :
        print('------------------Exited------------------')
        break

    else: 
         print('You entered an invalid option')
