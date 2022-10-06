import inventory 
def calculateChange(total_overage, denomination_amount):
    change_out = []
    for change_denomination in denomination_amount:
        coin_change = int(total_overage / change_denomination)
        total_overage = round(total_overage - coin_change * change_denomination, 2)
        change_out.append(coin_change)
    return change_out    


def removeChangeFromMachineWallet(cost_needed, change_returned):
    inventory.machine_wallet['quarters']  -= change_returned[0]
    inventory.machine_wallet['dimes'] -= change_returned[1]
    inventory.machine_wallet['nickles'] -= change_returned[2]
    inventory.machine_wallet['pennies'] -= change_returned[3]
    inventory.machine_wallet['total'] += cost_needed