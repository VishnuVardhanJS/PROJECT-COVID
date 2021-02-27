# Start of the code

"""Importing prerequisites """
import requests # Module to open url
from bs4 import BeautifulSoup as bs # Module to extract data from the url
from time import sleep # To add delay to the code
import os # To access files in the computer
from art import * # To add ascii art to the code
from prettytable import PrettyTable # To print table from an dictionary
import lxml #To read lxml files

def Global_info():

    """Function to Get global information """

    def live_data():

        """ To get the live data from https://api.covid19api.com/summary """

        global c_data
        global con_data

        try:
            #To Check the internet connection
            print('Trying to connect to network...'); sleep(2)
            api = 'https://api.covid19api.com/summary'
            req = requests.get(api).text
            raw_data = bs(req, 'lxml').text
            text = open("global_data.txt","w")
            text.write(raw_data)
            text.close()
            c_data = eval(open('global_data.txt').read())
            con_data = c_data['Countries']
            print('Connection... Successful...Proceeding...'); sleep(2)

        except:
            #When device is not connected to the internt
            print('Network Error...Trying with old data...'); sleep(3)

            try:
                #Trying to read data from the backup
                c_data = eval(open('global_data.txt').read())
                con_data = c_data['Countries']

            except:
                # When the data cannot retrived from the backup
                print('Cannot retrive the data...Connect to a Network and try again...'); sleep(1)
                tprint('\nTHANK YOU \n', font='Bold-small'); sleep(3) # Thank you text in ascii art
                os.remove('global_data.txt')#Deleting the unusable data
                exit()
            
    def quick_stats():

        """Function to Get quick stats from global information """

        gbl_val = c_data['Global']
        pt = PrettyTable()#Creating a table
        pt.field_names = gbl_val.keys()#Adding field names of the table
        pt.add_row(gbl_val.values())#Adding the values to the table
        print(pt)
      
    def data_by_code():

        """Function to Get the data by entering country code from global information """

        usr_code = input('Enter the Country code which you want the details: ').upper()

        try:
            for i in range(len(con_data)):
                if con_data[i]['CountryCode'] == usr_code:
                    del con_data[i]['Slug']
                    del con_data[i]['ID']
                    del con_data[i]['Premium']
                    for key, value in con_data[i].items():
                        pt = PrettyTable()#Creating a table
                        pt.field_names = con_data[i].keys()#Adding field names of the table
                        pt.add_row(con_data[i].values())#Adding the values to the table
                        print(pt)
                        break
                    break

        except:
            print('Country code does not exist or check the code...Try Again...')
            data_by_code()

    def data_by_con():

        """Function to Get data by enter an country from global information """

        con = input('Enter the Country which you want the details: ').capitalize()

        try:
            for i in range(len(con_data)):
                if con_data[i]['Country'] == con:
                    del con_data[i]['Slug']
                    del con_data[i]['ID']
                    del con_data[i]['Premium']
                    for key, value in con_data[i].items():
                        pt = PrettyTable()#Creating a table
                        pt.field_names = con_data[i].keys()#Adding field names of the table
                        pt.add_row(con_data[i].values())#Adding the values to the table
                        print(pt)
                        break
                    break

        except:
            print('Country  does not exist or check the Spelling...Try Again...')
            data_by_con()
 
    def sub_Category():

        """Function to access sub category from global information """

        print('\nSelect sub_Category...\n')
        print('1. Quick Stats')
        print('2. Data by country code')
        print('3. Data by country')

        usr_global_option = int(input('\nEnter the option: '))

        #Calling the functions according to user entered option

        while True:
            #When user selects option 1
            if usr_global_option == 1:
                quick_stats()
                break
            #When user selects option 2
            if usr_global_option == 2:
                data_by_code()
                break
            #When user selects option 3
            if usr_global_option == 3:
                data_by_con()
                break

            else:
                print('Select the correct option...Try Again...')

    #Calling nested functions of Global_Info()

    live_data()
    sub_Category() 

def State_info():

    """Function to get State information"""

    states = {'Andaman and Nicobar Islands': 'an', 'Andhra Pradesh': 'ap',
              'Arunachal Pradesh': 'ar', 'Assam': 'as', 'Bihar': 'br',
              'Chandigarh': 'ch', 'Chhattisgarh': 'ct', 'Dadar and Nagar Haveli': 'dn',
              'Daman and Diu': 'dd', 'Delhi': 'dl', 'Goa': 'ga', 'Gujarat': 'gj', 'Haryana': 'hr',
              'Himachal Pradesh': 'hp', 'Jammu and Kashmir': 'jk', 'Jharkhand': 'jh', 'Karnataka': 'ka',
              'Kerala': 'kl', 'Lakshadweep': 'la', 'Madhya Pradesh': 'mp', 'Maharashtra': 'mh', 'Manipur': 'mn',
              'Meghalaya': 'ml', 'Mizoram': 'mz', 'Nagaland': 'nl', 'Odisha': 'or', 'Puducherry': 'py', 'Punjab': 'pb',
              'Rajasthan': 'rj', 'Sikkim': 'sk', 'Tamil Nadu': 'tn', 'Telangana': 'tg', 'Tripura': 'tr',
              'Uttar Pradesh': 'up', 'Uttarakhand': 'ut', 'West Bengal': 'wb'}

    def live_data():

        """ To get the live data from https://api.covid19india.org/states_daily.json """

        global s_data
        global state_data

        try:
            #To Check the internet connection
            print('Trying to connect to network...'); sleep(2)
            api = 'https://api.covid19india.org/states_daily.json'
            req = requests.get(api).text
            raw_data = bs(req, 'lxml').text
            text = open("state_data.txt","w")
            text.write(raw_data)
            text.close()
            s_data = eval(open('state_data.txt').read())
            state_data = s_data['states_daily'][-1]
            print('Connection... Successful...Proceeding...'); sleep(2)

        except:
            #When device is not connected to the internt
            print('Network Error...Trying with old data...'); sleep(3)

            try:
                #Trying to read data from the backup
                s_data = eval(open('state_data.txt').read())
                state_data = s_data['states_daily'][-1]

            except:
                # When the data cannot retrived from the backup
                print('Cannot retrive the data...Connect to a Network and try again...'); sleep(1)
                tprint('\nTHANK YOU \n', font='Bold-small'); sleep(3) # Thank you text in ascii art
                os.remove('state_data.txt')#Deleting the unusable data
                exit()

    def data_by_state():

        """To get data by entering state from state information"""

        try:
            usr_state = input('Enter the state In India: ').title()
            try:
                print('\nThere are {} cases in {}\n'.format(state_data[usr_state.lower()], usr_state))
            except:
                state_val = states[usr_state]
                print('\nThere are {} cases in {}\n'.format(state_data[state_val], usr_state))

        except:
            print('State Does Not Exist or check the spelling ...Try Again...')
            data_by_state()

    #Calling nested functions of State_Info()
            
    live_data()
    data_by_state()
    
def District_info():

    """Function to get District information"""

    def live_data():

        """ To get the live data from https://api.covid19india.org/districts_daily.json """

        global d_data
        global district_data

        try:
            #To Check the internet connection
            print('Trying to connect to network...'); sleep(2)
            api = 'https://api.covid19india.org/districts_daily.json'
            req = requests.get(api).text
            raw_data = bs(req, 'lxml').text
            text = open("district_data.txt","w")
            text.write(raw_data)
            text.close()
            d_data = eval(open('district_data.txt').read())
            district_data = d_data['districtsDaily']
            print('Connection... Successful...Proceeding...'); sleep(2)

        except:
            #When device is not connected to the internt
            print('Network Error...Trying with old data...'); sleep(3)

            try:
                #Trying to read data from the backup
                d_data = eval(open('district_data.txt').read())
                district_data = d_data['districtsDaily']

            except:
                # When the data cannot retrived from the backup
                print('Cannot retrive the data...Connect to a Network and try again...'); sleep(1)
                tprint('\nTHANK YOU \n', font='Bold-small'); sleep(3) # Thank you text in ascii art
                os.remove('district_data.txt')#Deleting the unusable data
                exit() 

    def data_by_district():

        """Function to Get data by entering state and district from district information """

        try:
            usr_state = input('Enter the state of the district: ').title()
            usr_district = input('Enter the district: ').title()
            district_val = district_data[usr_state][usr_district][-1]
            del district_val['notes']

            pt = PrettyTable()#Creating a table
            pt.field_names = district_val.keys()#Adding field names to the table
            pt.add_row(district_val.values())#Adding values to the table
            print(pt)
    
        except:
            print('State or District Does Not Exist...Try Again...')
            data_by_district()

    #Calling nested functions of District_Info()

    live_data()
    data_by_district()
    
def mainloop():

    """Function to control the flow of the code"""

    # To print the header of the project in ascii
    tprint('\nPROJECT-COVID \n', font='Bold-small')

    print('1. Global Information')
    print('2. Indian State Information')
    print('3. Indian District Information')
    
    while True:
        usr_option = int(input('Enter the option: '))

        #To check wether the options are entered correctly
        if usr_option in (1, 2, 3):
            break
        else:
            print('Select correct option...Try Again...\n')
    
    #Calling the functions according to user entered option

    #When user selects option 1
    if usr_option == 1:
        tprint('GLOBAL INFORMATION \n', font='small')# GLOBAL INFORMATION text in ascii art
        Global_info()
    #When user selects option 2
    if usr_option == 2:
        tprint('STATE INFORMATION \n', font='small')# STATE INFORMATION text in ascii art
        State_info()
    #When user selects option 3
    if usr_option == 3:
        tprint('DISTRICT INFORMATION \n', font='small')# DISTRICT INFORMATION text in ascii art
        District_info()
    
    # To ask the user to run the code again

    while True: 
        loop = input('Do you want to run the program again (y/n)?')

        #When user wants to run the code again
        if loop == 'yes' or loop == 'y':
            #Calling the mainloop function to run again
            mainloop() 

        #When user wants Quit the code
        elif loop == 'no' or loop == 'n':
            # Thank you text in ascii art
            tprint('\nTHANK YOU \n', font='Bold-small'); sleep(3)
            exit()

#Calling mainloop function            
mainloop()

# End of the code
