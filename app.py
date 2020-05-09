import gspread
from oauth2client.service_account import ServiceAccountCredentials

import dialogflow_handler
try:
    import requests
    import urllib
    import json
    import os
    from flask import (Flask,request, make_response)
    import smtplib

except Exception as e:

    print("Some modules are missing {}".format(e))


# Flask app should start in global layout
app = Flask(__name__)
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]         
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)                              
client = gspread.authorize(creds)
sheet = client.open("spreaddemo").sheet1


@app.route('/webhook', methods=['POST'])

def webhook():
    ihandler = dialogflow_handler.intent_handler(request.get_json())
    intent = ihandler.get_intent()
    
    
    if request.method == "POST":
        req = request.get_json(silent=True, force=True)
        query_response = req["queryResult"]
        text = query_response.get('queryText', None)
        parameters = query_response.get('parameters', None)
        result = req.get("result")
        isOnline = sheet.cell(1, 8).value
        if isOnline=="OFFLINE" and intent =='make_order':
            if intent == "make_order":                      #Name and first order
                item_list = []
                sheet.update_cell(1,8, "ONLINE")
                speech = ""
                sheet.update_cell(1,5, 2)
                name = str(parameters.get("name"))
                item = str(parameters.get("items"))
                insertRow = [name, item]
                sheet.insert_row(insertRow, 10)
                speech = item + " added " + "\nyou can add more items, \n'Checkout/Done' to place the order , \n'my cart' to check items you added"
                res = {"fulfillmentText": speech,}
        else:
            speech = "Sorry, We are taking order from other customer, please come back in 5 minutes."
            res = {"fulfillmentText": speech,}
        if intent == "make_order - repeat":           #Order repeat
            item_list = []
            item = str(parameters.get("items"))
            item_list.append(item)
            sheet_number = int(sheet.cell(1, 5).value)
            sheetplus = sheet_number + 1
            sheet.update_cell(1,5, sheetplus)
            sheet.update_cell(10,sheetplus, item)
            speech = item + " added " + "\nyou can add more items, 'Checkout/Done' to place the order , 'my cart' to check items you added"
            res = {"fulfillmentText": speech,}

        elif intent == "place the order":          #Prompt and show orders
            code = ["aloo tikki","veggie","veg supreme","heaven","hell","burgpizza",
            "salty fries","maggie dust","cheese fries","cheese burst fries",
            "plain maggie","veg maggie","cheese veg maggie","cheese burst maggie",
            "maggie sandwich","cheese aloo tikki sandwich","double cheese loaded sandwich",
            "eco meal","heaven meal","maggie meal","hell meal","family meal","supreme cheese burst"]
            row = sheet.row_values(10)
            prices = sheet.row_values(4)
            prices = list(map(int, prices))
            speech = ""
            total = 0
            for i in range(1, len(row)):
                item_price = prices[code.index(row[i])]
                total += item_price
                speech += row[i] +"\t\t"+ str(item_price) + "\n"
            res = {"fulfillmentText": speech+"\nTotal "+str(total)+"\n\nAre You Sure You Want to Place The Order",}


        elif intent == "place the order - yes":         #Confirm Order
            sheet_number = int(sheet.cell(1, 5).value)
            sheetplus = sheet_number + 1
            sheet.update_cell(1,5, 2)
            sheet.update_cell(10,sheetplus, "CONFIRMED")
            speech = "Your order has been placed and delivered in some time in your doorstep \n Have a Nice Day."
            res = {"fulfillmentText": speech,}

        elif intent == "place the order - no":          #reject order
            sheet_number = int(sheet.cell(1, 5).value)
            sheetplus = sheet_number + 1
            sheet.update_cell(1,5, 2)
            sheet.update_cell(10,sheetplus, "Rejected")
            speech = "Alright your order has been cancelled"
            res = {"fulfillmentText": speech,}

        elif intent == "check_cart":          #check order
            code = ["aloo tikki","veggie","veg supreme","heaven","hell","burgpizza",
            "salty fries","maggie dust","cheese fries","cheese burst fries",
            "plain maggie","veg maggie","cheese veg maggie","cheese burst maggie",
            "maggie sandwich","cheese aloo tikki sandwich","double cheese loaded sandwich",
            "eco meal","heaven meal","maggie meal","hell meal","family meal","supreme cheese burst"]
            row = sheet.row_values(10)
            prices = sheet.row_values(4)
            prices = list(map(int, prices))
            speech = ""
            total = 0
            for i in range(1, len(row)):
                item_price = prices[code.index(row[i])]
                total += item_price
                speech += row[i] +"\t\t"+ str(item_price) + "\n"
            res = {"fulfillmentText": speech+"\nTotal "+str(total),}
        res = json.dumps(res, indent=4)
        r = make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r
    def codes():        #saving the locations of cells where the price are stored in sheet (we can directly get from sheet but sometime there was delay in responce)
        code = {"aloo tikki":[4,1],"veggie":[4,2],"veg supreme":[4,3],"heaven":[4,4],"hell":[4,5],"burgpizza":[4,6],
        "salty fries":[5,1],"maggie dust":[5,2],"cheese fries":[5,3],"cheese burst fries":[5,4],
        "plain maggie":[6,1],"veg maggie":[6,2],"cheese veg maggie":[6,3],"cheese burst maggie":[6,4],
        "maggie sandwich":[7,1],"cheese aloo tikki sandwich":[7,2],"double cheese loaded sandwich":[7,3],
        "eco meal":[8,1],"heaven meal":[8,2],"maggie meal":[8,3],"hell meal":[8,4],"family meal":[8,5],"supreme cheese burst":[8,6]}

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    sheet.update_cell(6,8, '2')

    print ("Starting app on port %d" %(port))
    app.run(debug=True, port=port, host='0.0.0.0')