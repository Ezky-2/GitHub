
from sys import path

path.append('..')

from client import Client
from library import convertpe , convertep
from atoken import token



















bot_token = token ()

bot1 = Client(bot_token)
bot1.RETRY_DELAY = 1



 
 
def esend (text ,id):
   
   send_message ({"to":id,"type":"TEXT","body": str(text)})




def send_message0 (data0):

   pass




def send_message (data0):

   data = {'to':data0['to'] , 'type' : 'TEXT' , 'body' : convertep(data0.get('body','')) , 'keyboard':data0.get ('keyboard',[]) }

   print ('(send)      : %s '% (data['body']) )

   bot1.send_message ( data )












#url = "https://bot.sapp.ir/XayO8FeO8PDjV1Xq0unWmLxsUf6MjFMnG5DFk7EVwRTsSD4PVc8lMX-d3AlBqu6e4zbLWIioqyMb_nwr1vmVMeUy3c3x_ZWZBoBjKQF6H3QcHUdkKfe2LDUTwcvl8ZDBI8NYkOGD8dTUdBqm/getMessage"

