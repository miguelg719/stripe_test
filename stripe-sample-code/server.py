#! /usr/bin/env python3.6
"""
Python 3.6 or newer required.
"""
import json
import os
import stripe
import random 
import time

# This is your test secret API key.
stripe.api_key = 'sk_test_51OlQPEHKGh8YsfR4LE9iPTTmJsL1L8RoHNMMGTS5PSlGuyxu4sHlwWQBdFOrNZJuaEQBRmb9U90rYv2j44lY9sfw00KfQDZPbF'

from flask import Flask, render_template, jsonify, request

card = 4000000000000077

app = Flask(__name__, static_folder='public',
            static_url_path='', template_folder='public')

def calculate_order_amount(items):
    # Replace this constant with a calculation of the order's amount
    # Calculate the order total on the server to prevent
    # people from directly manipulating the amount on the client
    return 1400

def rand_buy_sell():
    number = random.uniform(-20, 20)
    number = round(number, 2)
    print(number)
    if number < 0:
        return refund_payment(number, customer)
    else:
        return make_payment(number, customer)
    
customer = stripe.Customer.retrieve("cus_PawNoOnz5rYYpm")

def make_payment(amount, customer):
  intent = stripe.PaymentIntent.create(
    amount = round(amount * 100),
    currency = "usd",
    customer = customer.id,
    payment_method = "pm_card_bypassPending",
  )
  confirm = stripe.PaymentIntent.confirm(intent.id, return_url="https://www.example.com")
  return "successful payment"

def refund_payment(amount, customer):
  refund = stripe.Refund.create(
    payment_intent = "pi_3OlpfVHKGh8YsfR40juRNNR7",
    amount = round(amount * 100 * -1),
  )
  return "successful refund"


@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    try:
        data = json.loads(request.data)
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=calculate_order_amount(data['items']),
            currency='usd',
            # In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
            automatic_payment_methods={
                'enabled': True,
            },
        )
        return jsonify({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify(error=str(e)), 403
    
@app.route('/demo', methods=['POST', 'GET'])
def demo():
    while True:
        rand_buy_sell()
        time.sleep(5)


if __name__ == '__main__':
    app.run(debug=True, port=4242)