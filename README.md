# Food-Divilery-chatbot
# the problem
For a food dilivery startup if the number of order in a day are upto 10, you can easily manage the orders via calls or message
but when the orders rises upto 20-30 in a single day then it harder to manage for a single person, and you have to repeat every information customer
asked.
instead of managing all of the orders yourself one can use a chatbot, the you may have in mind that the customer can simply 
leave a message to the list of orders to the food dilivery person. but the problem with this approach is that what if the customer
have asked for something like "what is plain maggie" then you need to reply the message as well.

Now there are two types of chatbot one is hard coaded chatbot
another one is AI based chatbot.

The hard coaded chatbot are now reliable they are build on if else condition only if the customer
asked for the exact phrase then only the chatbot will work so these chatbots are not customer frienly.

AI based chatbots are on the other hand are more reliable, they used to learn the intention of customer that what the customer is
tryin to ask even if the phrase was not exact the chatbot will understand and reply with the appropriate message. these type
of chatbot are more customer friendly.

this chatbot is created in dialogflow, linked with google sheets for inventory management
it will make database of customers with their orders so that you can check for dilivery status even after a months,
(like burgers tends to sold more this months)

This can be used as Chatbot for Food Delivery buisness
 # How to use the chatbot
 ## - First the chatbot greet and show you the available ordering list with Menu
 ## - then you can add items of your wish from the menu by saying "make an order"
 ## - chatbot then ask for your name so it can add it to the database
 ## - then you need to order your first order which is mandatory
 ## - you can add more items if you want by saying add ("add plain maggie"). or you can skip to the next step if you are happy  with 
 your list
 ## - you can check your cart if you want to check your shopping cart for the order list with the amount for every order with total amount.
 ## - if you wish you can add more orders or if you want to order to be placed you can simply say "place the order"
 ## - the bot will show you the order list that you have added and ask you for the confirmation (yes/no)
 ## - after whatever the response from the customer the bot will make the entry to the spreadsheet database
 like Confirmed after the order if the customer choose yes or rejected otherwise.
 
 ## the bot comes with one more smart feature which triggered when one customer is making an order and another customer cones
 with the order request, the bot will check into the system for any customer currently making an order. if so the bot will not allow
 new customer to order while the previous customer done ordering so that the new customer will not intrrupt the list of the previous
 customer. (synchronization will come in future version so that multiple customer can order at the same time.
 
 
 you can see the spreadsheet being updated with the new orders 
 https://docs.google.com/spreadsheets/d/1GPMEzuC_28VxZelBfd1c9iqO6Gocbkl5SM-QqbPwYnc/edit#gid=0
 and you can test the chatbot here
 @Foodtest2bot with the telegram APP
 or https://bot.dialogflow.com/food2bot for web based demo (But some of the features are not available currently so it is
 better to test the bot on telegram APP)
 
