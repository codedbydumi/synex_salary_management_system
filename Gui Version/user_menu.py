import os

from start import Login
from user_manu_process import User_changes,Emp_data_calculataion

class User(User_changes,Emp_data_calculataion):

    def __init__(self, type, cur):
        print(f'\n\n**  You are Logged as {type} **')
        self.cur = cur

    def owner(self):
        os.system('''cls''')
        print('''
        
                ___       __          _       _      __             __            
               /   | ____/ /___ ___  (_)___  (_)____/ /__________ _/ /_____  _____
              / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ __/ __ \/ ___/
             / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /_/ /_/ / /    
            /_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/\__/\____/_/     
                                                                                  
            
                    
              ''')
        print(" Type 00 To logout    ")
        app_m = input("     >press 1 for App Manager\n     >press 2 for emp Manager ")
        if app_m == "1": self.app_manager()
        if app_m == '2':self.emp_manager()
        else:
            os.system('cls')
            login =Login(self.cur)


    '''Emp  Manager  Menu '''
    def emp_manager(self):
        os.system('cls')
        print('\n                                       -------------------~ Synex Salary Calculating System ~---------------------')


        print('''
        
                                
                                                                             
                  ,---.     ,--.          ,--.            ,--.   ,--.                        
                 /  O  \  ,-|  |,--,--,--.`--',--,--,     |   `.'   | ,---. ,--,--, ,--.,--. 
                |  .-.  |' .-. ||        |,--.|      \    |  |'.'|  || .-. :|      \|  ||  | 
                |  | |  |\ `-' ||  |  |  ||  ||  ||  |    |  |   |  |\   --.|  ||  |'  ''  ' 
                `--' `--' `---' `--`--`--'`--'`--''--'    `--'   `--' `----'`--''--' `----'  
                                                                                             
  
        
            ''')
        print("GoBack   :-  '00'")

        self.user_choice = int(input("""    
                    Press 1 -> Create Employee Salary Sheet For Company
                    Press 2 -> Calculate total taxes from All employees in each Month
                    Press 3 -> Calculate company Profit In each Month
                    Press 4 -> Create Year Salary Report For Employee
                    Press 5 -> Create Salary report of an employee specific Month
          
                Enter Your Choice - """))

        Emp_data_calculataion.__init__(self,self.cur)




    def app_manager(self):
        os.system('cls')
        print('\n                                       -------------------~ System Administrator ~---------------------                        \n')
        print("GoBack   :-  '00'")

        print('''  
                   ____                                            __  ___                      
                  / __ \ _      __   ____   ___    _____          /  |/  /  ___    ____   __  __
                 / / / /| | /| / /  / __ \ / _ \  / ___/         / /|_/ /  / _ \  / __ \ / / / /
                / /_/ / | |/ |/ /  / / / //  __/ / /            / /  / /  /  __/ / / / // /_/ / 
                \____/  |__/|__/  /_/ /_/ \___/ /_/            /_/  /_/   \___/ /_/ /_/ \__,_/                   

                                                                                                     ''')

        self.user_choice = int(input("""    
            Press 1 for add new App User
            Press 2 for Remove  App User
            Press 3 for Add New Profession
            Press 4 for Change The Profession Details
            Press 5 For delete profession
            Press 6 for Load Data File
            Press 7 Delete Employer Data
        Enter Your Choice - """))

        super(User, self).__init__(self.cur)
