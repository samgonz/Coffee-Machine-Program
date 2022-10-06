import returnChange
import inventory
import splashScreen

machine_status = 'y'
denomination_amount = [0.25, 0.10, 0.05, 0.01]
water_needed = 0
milk_needed = 0
coffee_needed = 0

water_inventory = inventory.machine_resource_dict['water']
milk_inventory = inventory.machine_resource_dict['milk']
coffee_inventory = inventory.machine_resource_dict['coffee'] 

print(splashScreen.logo)
while machine_status == 'y':
    user_drink = input('What do you want to drink? (espresso, latte, cappachino)\n').lower()
    
    #ingredients needed
    if 'water' in inventory.menu[user_drink]['ingredients']:
        water_needed = inventory.menu[user_drink]['ingredients']['water']
    if 'milk' in inventory.menu[user_drink]['ingredients']:    
        milk_needed = inventory.menu[user_drink]['ingredients']['milk'] 
    if 'coffee' in inventory.menu[user_drink]['ingredients']:    
        coffee_needed = inventory.menu[user_drink]['ingredients']['coffee']
        
        cost_needed = inventory.menu[user_drink]['cost']
    
    #Check to see if enough ingredients
    if water_inventory < water_needed:
        print('There is not enough water available.')
        machine_status == 'off'
        break
    if milk_inventory < milk_needed:
        print('There is not enough milk available.')
        machine_status == 'off'
        break
    if coffee_inventory < coffee_needed:
        print('There is not enough coffee available.')  
        machine_status == 'off'  
        break
    
    quarters_inserted = int(input('How many quarters do you want to insert into the coffee machine?\n')) 
    dimes_inserted = int(input('How many dimes do you want to insert into the coffee machine?\n')) 
    nickles_inserted = int(input('How many nickles do you want to insert into the coffee machine?\n')) 
    pennies_inserted = int(input('How many pennies do you want to insert into the coffee machine?\n')) 
    
    total_inserted = round((quarters_inserted * .25) + (dimes_inserted * .10) + (nickles_inserted * .05) + (pennies_inserted * .01), 2)
    
    if total_inserted < cost_needed:
        print('There is not enough money inserted.')
        machine_status == 'off'
        break
    
    inventory.machine_wallet['quarters'] += quarters_inserted
    inventory.machine_wallet['dimes'] += dimes_inserted
    inventory.machine_wallet['nickles'] += nickles_inserted
    inventory.machine_wallet['pennies'] += pennies_inserted
    inventory.machine_wallet['total'] += total_inserted
    
    total_overage = round(total_inserted - cost_needed, 2)
    
    # get the amount of change returned and remove it from the machine wallet
    change_returned = returnChange.calculateChange(total_overage, denomination_amount)
    returnChange.removeChangeFromMachineWallet(cost_needed, change_returned)
    
    #Remove inventory from machine
    water_inventory -= water_needed
    milk_inventory -= milk_needed
    coffee_inventory -= coffee_needed
    
    print(f'{inventory.machine_wallet}, water: {water_inventory}, milk: {milk_inventory}, coffe: {coffee_inventory}')
    machine_status = input('Would you like to make another dirnk? [y/n]:').lower()

print('Turning Off....')
