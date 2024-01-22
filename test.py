from sarufi import Sarufi

sarufi = Sarufi(api_key='your API KEY')
chatbot = sarufi.create_bot(name="Pizza Yangu", description="Pizza Ordering Chatbot")

# We assign intents attribute a dict with intent name and intents dict {<intent name>: [list of all related keywords to trigger the intent]}

chatbot.flow = {
    'greets': {
        'message': ['Hi, How can I help you?'],
        'next_state': 'end'
    },
    'order_pizza': {
        'message': ['Sure, How many pizzas would you like to order?'],
        'next_state': 'number_of_pizzas'
    },
    'number_of_pizzas': {
        'message': ['Sure, What would you like to have on your pizza?'],
        'next_state': 'pizza_toppings'
    },
    'pizza_toppings': {
        'message': ['Cool, What\'s your address?'],
        'next_state': 'address'
    },
    'address': {
        'message': ['Sure, What is your phone number?'],
        'next_state': 'phone_number'
    },
    'phone_number': {
        'message': ['Your order has been placed.', 'Thank you for ordering with us.'],
        'next_state': 'end'
    },
    'goodbye': {
        'message': ['Bye', 'See you soon'],
        'next_state': 'end'
    }
}
