import growattServerSR as growattServer
import datetime
import getpass
import pprint

"""
This is a very trivial script to show how to interface with the configuration settings of a plant and it's inverters
This has been tested against my personal system (muppet3000) which is a hybrid (aka 'mix') inverter system.

Throughout the script there are points where 'pp.pprint' has been commented out. If you wish to see all the data that is returned from those
specific library calls, just uncomment them and they will appear as part of the output.
"""
pp = pprint.PrettyPrinter(indent=4)

#Prompt user for username
username="Rankinehousehold"

#Prompt user to input password
user_pass="9P2Ip^HuIeRmnopR"

api = growattServer.GrowattApi(add_random_user_id=True, agent_identifier=username)
login_response = api.login(username, user_pass)

plant_list = api.plant_list(login_response['user']['id'])

#Simple logic to just get the first inverter from the first plant
#Expand this using a for-loop to perform for more systems (see mix_example for more detail)
plant = plant_list['data'][0] #This is an array - we just take the first - would need a for-loop for more systems
plant_id = plant['plantId']
plant_name = plant['plantName']
plant_info=api.plant_info(plant_id)
print(plant_info)

device = plant_info['storageList'][0] #This is an array - we just take the first - would need a for-loop for more systems
device_sn = device['deviceSn']
device_type = device['deviceType']


#Get plant settings - This is performed for us inside 'update_plant_settings' but you can get ALL of the settings using this
current_settings = api.plant_settings(plant_id)
#pp.pprint(current_settings)

#Get mix inverter settings
inverter_settings = api.get_mix_inverter_settings(device_sn)
pp.pprint(inverter_settings)
