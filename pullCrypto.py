from datetime import datetime
import coinbasepro as cbp
import time
import datetime

cbKey = ''
# secretKey = ""

client = cbp.PublicClient()
# auth_client = cbp.AuthenticatedClient(cbKey, )

# print(auth_client.get_accounts())


currentLast = 0
currentLastEth = 0

origTime = datetime.datetime.now().replace(microsecond=2)
latestTime = origTime.strftime("%Y-%m-%d %H:%M:%S")


while currentLast != -1:
    ankr = client.get_product_24hr_stats('ANKR-USD')

    if currentLast != ankr['last']:
        print(currentLast)
        lastValue = currentLast
        currentLast = ankr['last']
        
        print("ANKR latest price now: ", currentLast)
        print('time : ' + latestTime)

        newOrigTime = datetime.datetime.now().replace(microsecond=2)
        print('time between: ' + str(newOrigTime - origTime))

        percent_diff = (((currentLast - lastValue)/ currentLast)* 100)
        print(str(percent_diff) + '% change')
            

        print('------------------------------------------------')

while currentLastEth != -1:
    eth = client.get_product_24hr_stats('ETH-USD')

    if currentLastEth != eth['last']:
        print(currentLast)
        lastValue = currentLast
        currentLastEth = eth['last']
        
        print("ETH latest price now: ", currentLastEth)
        print('time : ' + latestTime)

        newOrigTime = datetime.datetime.now().replace(microsecond=2)
        print('time between: ' + str(newOrigTime - origTime))

        percent_diff = (((currentLast - lastValue)/ currentLast)* 100)
        print(str(percent_diff) + '% change')
            

        print('------------------------------------------------')
