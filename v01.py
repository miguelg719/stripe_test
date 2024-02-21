import random
import stripe
import time

stripe.api_key = "sk_test_51OlQPEHKGh8YsfR4LE9iPTTmJsL1L8RoHNMMGTS5PSlGuyxu4sHlwWQBdFOrNZJuaEQBRmb9U90rYv2j44lY9sfw00KfQDZPbF"

def rand_buy_sell():
    number = random.uniform(-20, 20)
    number = round(number, 2)
    print(number)
    if number < 0:
        return refund_payment(number, customer)
    else:
        return make_payment(number, customer)

# Create a customer
# customer = stripe.Customer.create(
#     name="Jack Sparrow",
#     email="jack@blackpearl.com"
# )

customer = stripe.Customer.retrieve("cus_PawNoOnz5rYYpm")
print(customer, "\n\n")

# Attach a payment method
# payment_method = stripe.PaymentMethod.attach(
#   "pm_card_visa",
#   customer=customer.id,
# )

payment_method = stripe.PaymentMethod.retrieve("pm_1OlksBHKGh8YsfR4MBiVOng3")
# payment_method = stripe.PaymentMethod.modify(
#     "pm_1OlksBHKGh8YsfR4MBiVOng3",
#     billing_details={"email": "jack@blackpearl.com", "name": "Jack Sparrow", "phone": "1234567890"}
#     )

print(payment_method, "\n\n")

def make_payment(amount, customer):
  intent = stripe.PaymentIntent.create(
    amount = round(amount * 100),
    currency = "usd",
    customer = customer.id,
    payment_method = "pm_card_bypassPending",
  )
  confirm = stripe.PaymentIntent.confirm(intent.id, return_url="https://www.example.com")
  return "successful payment"

# refund payment intent = pi_3OlnunHKGh8YsfR41pOJ4YM2
def refund_payment(amount, customer):
  refund = stripe.Refund.create(
    payment_intent = "pi_3OlnunHKGh8YsfR41pOJ4YM2",
    amount = round(amount * 100 * -1),
  )
  return "successful refund"

# Create a payment intent
# stripe.PaymentIntent.create(
#   amount=20000,
#   currency="usd",
#   payment_method="pm_card_bypassPending",
# )
i = 1
payment_intents = stripe.PaymentIntent.list()

# Print non-canceled payment intents
# for p in payment_intents.data:
#     if p.canceled_at is None:
#         print(p, "\n", i, "\n")
#         i += 1

# Print all payment intents
# print(payment_intents)

# Confirm a payment intent
# stripe.PaymentIntent.confirm("pi_3OllCgHKGh8YsfR40JdX0yXr", return_url="https://www.example.com")


if __name__ == "__main__": 
  while True:
    time.sleep(3)
    print(rand_buy_sell())