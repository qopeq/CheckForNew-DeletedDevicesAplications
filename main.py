import getListFromRegistry
import time as Time
import emailTool

def difTables(tab1, tab2):
    dif = []
    for item in tab1:
        try:
            tab2.index(item)
        except:
            dif.append(item)

    return dif


def onTurnOn():

    first_list_of_software = getListFromRegistry.getFullList()
    first_list_of_devices =getListFromRegistry.getConnectedDevices()



    while 1:

        Time.sleep(5)
        second_list_of_software = getListFromRegistry.getFullList()
        second_list_of_devices = getListFromRegistry.getConnectedDevices()

        if(first_list_of_software != second_list_of_software or second_list_of_devices != first_list_of_devices):

            msg = difTables(first_list_of_software, second_list_of_software) + difTables(second_list_of_software, first_list_of_software) + difTables(first_list_of_devices, second_list_of_devices) + difTables(second_list_of_devices, first_list_of_devices)
            clock = Time.localtime()
            time = str(clock.tm_year) + "." + str(clock.tm_mon) + "." + str(clock.tm_yday) + "   " + str(clock.tm_hour) + ":" + str(clock.tm_min) + ":" + str(clock.tm_sec)
            emailTool.sendEmail(msg, time)


        first_list_of_software = second_list_of_software
        first_list_of_devices = getListFromRegistry.getConnectedDevices()

onTurnOn()


