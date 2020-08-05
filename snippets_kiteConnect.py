from kiteconnect import KiteConnect
from pprint import pprint
import pdb
from pprint import pprint
import telegram
import mysql.connector
import time


api_k = "Enter your api key"  # id
api_s = "Enter your secret key" # pass
kite = ""

#########################################################
# only if you are using cloud to store your daily request token, otherwise, just hardcode your request token
# refer Trade Hull @youtube for tutorial series and all the code snippets and explanations

mydb = mysql.connector.connect(
    host="database-restored1.cninlcvpipmk.us-east-1.rds.amazonaws.com", user="admin", passwd="password", database="stocks")
time.sleep(2)
mycursor = mydb.cursor()


def fetch_access_token():
    print("fetching access token value")
    mycursor.execute("select value from token_val")
    myresult = mycursor.fetchone()
    for row in myresult:
        a = row
    return a

#######################################################################################


def get_login(api_k, api_s):  # log in to zerodha API panel
    try:
        print("trying to login...")
        global kite
        kite = KiteConnect(api_key=api_k)
        access_token = fetch_access_token()
        kite.set_access_token(access_token)
        # login_flag = 1
        # bot.sendMessage(chat_id=984101934,
        #                 text="you are now logged in for today, level excel")
        print("you are now logged in for today")
    except Exception as e:
        # bot.sendMessage(chat_id=984101934,
        #                 text="update api key, not able to login")
        print(e)


get_login(api_k, api_s)


pprint(kite.orders())
order_id = 200624201857992
pprint(kite.order_history(order_id))
kite.cancel_order(kite.VARIETY_CO, 200624201773346)
kite.exit_order(kite.VARIETY_CO,)


def buy_order_limit_BO(name, price, quantity, target, sl):
    print("placing buy order with name quantity sl price",
          name, price, quantity, target, sl)

    kite.place_order(tradingsymbol=name, price=price, variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE,
                     transaction_type=kite.TRANSACTION_TYPE_BUY, quantity=quantity, trigger_price=price, order_type=kite.ORDER_TYPE_SL, product=kite.PRODUCT_MIS)

    kite.place_order(tradingsymbol=name, price=sl, variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE, transaction_type=kite.TRANSACTION_TYPE_SELL, quantity=quantity, trigger_price=sl, order_type=kite.ORDER_TYPE_SL,
                     product=kite.PRODUCT_MIS)

    kite.place_order(tradingsymbol=name, price=target, variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE,
                     transaction_type=kite.TRANSACTION_TYPE_SELL, quantity=quantity, order_type=kite.ORDER_TYPE_LIMIT, product=kite.PRODUCT_MIS)


def sell_order_limit_BO(name, price, quantity, target, sl):
    print("placing sell order with name quantity sl price",
          name, price, quantity, target, sl)

    kite.place_order(tradingsymbol=name, price=price, variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE,
                     transaction_type=kite.TRANSACTION_TYPE_SELL, quantity=quantity, trigger_price=price, order_type=kite.ORDER_TYPE_SL, product=kite.PRODUCT_MIS)

    kite.place_order(tradingsymbol=name, price=sl, variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE, transaction_type=kite.TRANSACTION_TYPE_BUY, quantity=quantity, trigger_price=sl, order_type=kite.ORDER_TYPE_SL,
                     product=kite.PRODUCT_MIS)

    kite.place_order(tradingsymbol=name, price=target, variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE,
                     transaction_type=kite.TRANSACTION_TYPE_BUY, quantity=quantity, order_type=kite.ORDER_TYPE_LIMIT, product=kite.PRODUCT_MIS)


def buy_order_market_CO(name, quantity, sl):
    print("placing order with name quantity sl price", name, quantity, sl)
    # trd_portfolio[inst_of_single_company]['status'] = "bought"
    kite.place_order(tradingsymbol=name, variety=kite.VARIETY_CO, exchange=kite.EXCHANGE_NSE,
                     transaction_type=kite.TRANSACTION_TYPE_BUY, quantity=quantity, trigger_price=sl, order_type=kite.ORDER_TYPE_MARKET, product=kite.PRODUCT_MIS)
    # trd_portfolio[inst_of_single_company]["order_ids"] = order_id


def sell_order_market_CO(name, quantity, sl):
    print("placing order with name quantity sl price", name, quantity, sl)
    # trd_portfolio[inst_of_single_company]['status'] = "sold"
    kite.place_order(tradingsymbol=name, variety=kite.VARIETY_CO, exchange=kite.EXCHANGE_NSE,
                     transaction_type=kite.TRANSACTION_TYPE_SELL, trigger_price=sl, quantity=quantity, order_type=kite.ORDER_TYPE_MARKET, product=kite.PRODUCT_MIS)
    # trd_portfolio[inst_of_single_company]["order_ids"] = order_id
