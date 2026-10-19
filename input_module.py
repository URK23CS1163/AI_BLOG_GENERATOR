def get_customer_details():
    print("\n" + "=" * 55)
    print("          INTELLIGENT EMAIL ASSISTANT")
    print("=" * 55)

    customer_name = input("\nEnter Customer Name: ").strip()
    subject = input("Enter Email Subject: ").strip()

    print("\nEnter Customer Email:")
    customer_email = input("> ").strip()

    return customer_name, subject, customer_email


def display_customer_details(customer_name, subject, customer_email):
    print("\n" + "-" * 55)
    print("              CUSTOMER DETAILS")
    print("-" * 55)

    print(f"Customer Name  : {customer_name}")
    print(f"Subject        : {subject}")
    print(f"Customer Email : {customer_email}")

    print("-" * 55)
if __name__ == "__main__":
    name, subject, email = get_customer_details()
    display_customer_details(name, subject, email)