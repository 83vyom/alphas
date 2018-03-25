import envars
import mysql.connector
from alpha_vantage.timeseries import TimeSeries
#alphakey= "IX9A9CNUP9DL3HOJ"
alphakey = envars.alphakey
ts = TimeSeries(key=alphakey)
# Get json object with the intraday data and another with  the call's metadata
#data, meta_data = ts.get_intraday('GOOGL')
data, meta_data = ts.get_daily_adjusted(symbol='NSE:TITAN', outputsize='full')
data, meta_data = ts.get_daily_adjusted(symbol='BSE:TITAN', outputsize='full')
print(data)

cnx = mysql.connector.connect(user=envars.dbuser, password=envars.dbpass,
                              #host='127.0.0.1',
                              database=envars.dbname)
cursor=cnx.cursor()
query = ("SELECT stk_id, stk_symbol, stk_name FROM stock_symbols")
cursor.execute(query)
datas=cursor.fetchone()
#for (stk_id, stk_symbol, stk_name) in cursor:
#  print("{}, {} {}".format(
#    stk_id,stk_symbol,stk_name))
#print(cursor)
print (datas)
cursor.close()
cnx.close()