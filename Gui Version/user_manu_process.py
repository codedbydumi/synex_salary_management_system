import os
from hash_password import Hash
from start import Login


class User_changes(Hash):

    def __init__(self, cur):
        os.system('cls')
        self.cur = cur
        if self.user_choice == 00:
            os.system('cls')
            self.owner()
        elif self.user_choice == 1:
            self.add_user()
        elif self.user_choice == 2:
            self.remove_user()
        elif self.user_choice == 3:
            self.profession()
        elif self.user_choice == 4:
            self.change_profession_data()
        elif self.user_choice == 5:
            self.drop_profession()
        elif self.user_choice == 6:
            self.load_data()
        elif self.user_choice == 7:
            self.drop_emp_data()

        from prettytable import PrettyTable
        x = PrettyTable()

    def add_user(self):
        print('''
                  ____  ___    ___        ____     ___ __    __      __ __  _____   ___  ____  
                 /    T|   \  |   \      |    \   /  _]  T__T  T    |  T  T/ ___/  /  _]|    \ 
                Y  o  ||    \ |    \     |  _  Y /  [_|  |  |  |    |  |  (   \_  /  [_ |  D  )
                |     ||  D  Y|  D  Y    |  |  |Y    _]  |  |  |    |  |  |\__  TY    _]|    / 
                |  _  ||     ||     |    |  |  ||   [_l  `  '  !    |  :  |/  \ ||   [_ |    \ 
                |  |  ||     ||     |    |  |  ||     T\      /     l     |\    ||     T|  .  Y
                l__j__jl_____jl_____j    l__j__jl_____j \_/\_/       \__,_j \___jl_____jl__j\_j



                                                                            ''')
        print("Go Back - 00")
        username = input("      Enter !new User name -> ")
        if username == '00': self.app_manager()

        passwd = input("        Enter !new Passwd -> ")
        if passwd == '00': self.app_manager()

        c_passwd = input("       ~Confirm !new Passwd -> ")
        if passwd != c_passwd:
            os.system('cls')
            print('\n\n__Password Not Match__\n\n')
            self.add_user()
        user_type = input("        ~Pick User-Type : (owner| admin) ->")

        c_passwd = self.encrypt(c_passwd)
        if username == '00' or passwd == '00' or user_type == '00':
            self.app_manager()

        add = f"insert into app_user values ('{username}','{c_passwd}','{user_type}')"
        self.cur.execute(add)

        os.system('cls')
        print('''

                 ________      ______    _____  ___    _______  
                |"      "\    /    " \  (\"   \|"  \  /"     "| 
                (.  ___  :)  // ____  \ |.\\   \    |(: ______) 
                |: \   ) || /  /    ) :)|: \.   \\  | \/    |   
                (| (___\ ||(: (____/ // |.  \    \. | // ___)_  
                |:       :) \        /  |    \    \ |(:      "| 
                (________/   \"_____/    \___|\____\) \_______) 
                                                                

        ''')
        again = int(input('''\n
                          .Add Another User press 1
                          .Back TO Menu     press 2
                          .!Exit            press 0 ->  '''))

        if again == 1:self.add_user()
        elif again == 2:self.app_manager()
        elif again == 0:
            os.system('cls')
            print("""
                    ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                    ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                    ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                    ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                    ─╔╗──╔╗▄██▄──▄██▄
                    ─║╚╗╔╝║█░████████▌
                    ─╚╗╚╝╔╩═╦╗╔╗█████
                    ──╚╗╔╣╔╗║║║║███▀
                    ───║║║╚╝║╚╝║█▀
                    ───╚╝╚══╩══╝
                     --
                       For Visited 
                       ->>   

                        """)
            exit()
        else:
            os.system('cls')
            print("         Invaild Synatx      "*50)
            print("""
                    ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                    ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                    ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                    ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                    ─╔╗──╔╗▄██▄──▄██▄
                    ─║╚╗╔╝║█░████████▌
                    ─╚╗╚╝╔╩═╦╗╔╗█████
                    ──╚╗╔╣╔╗║║║║███▀
                    ───║║║╚╝║╚╝║█▀
                    ───╚╝╚══╩══╝
                     --
                       For Visited 
                       ->>   

                        """)

    def remove_user(self):
        print('''
                 __      ____     ___  ___ ___   ___   __ __    ___      __ __  _____   ___  ____  
                |  T    |    \   /  _]|   T   T /   \ |  T  |  /  _]    |  T  T/ ___/  /  _]|    \ 
                |  |    |  D  ) /  [_ | _   _ |Y     Y|  |  | /  [_     |  |  (   \_  /  [_ |  D  )
                |__j    |    / Y    _]|  \_/  ||  O  ||  |  |Y    _]    |  |  |\__  TY    _]|    / 
                 __     |    \ |   [_ |   |   ||     |l  :  !|   [_     |  :  |/  \ ||   [_ |    \ 
                |  T    |  .  Y|     T|   |   |l     ! \   / |     T    l     |\    ||     T|  .  Y
                l__j    l__j\_jl_____jl___j___j \___/   \_/  l_____j     \__,_j \___jl_____jl__j\_

                 ''')
        print("Go Back - 00")

        r_user = input("\n       Enter !removing Section Username -> ")
        if r_user == '00': self.app_manager()

        user_confirm = input(f"       Are You Sure? , you want to Remove {r_user} (y/n)    ")

        if user_confirm.lower() != 'y':
            os.system('cls')
            self.remove_user()

        remove_command = f"Delete from app_user where Username = '{r_user}'"

        self.cur.execute("select Username from app_user")
        val = self.cur.fetchall()
        lst = []
        for i in val: lst.append(i[0])

        '''get all users in mysql db and check if remove user in that'''
        if r_user not in lst:
            os.system('cls')
            print("! user name Incorrect !" * 5)
            self.remove_user()

        self.cur.execute(remove_command)

        os.system('cls')
        print('''

                         ________      ______    _____  ___    _______  
                        |"      "\    /    " \  (\"   \|"  \  /"     "| 
                        (.  ___  :)  // ____  \ |.\\   \    |(: ______) 
                        |: \   ) || /  /    ) :)|: \.   \\  | \/    |   
                        (| (___\ ||(: (____/ // |.  \    \. | // ___)_  
                        |:       :) \        /  |    \    \ |(:      "| 
                        (________/   \"_____/    \___|\____\) \_______) 


                ''')
        again = int(input('''\n
                                  .Remove Another User press 1
                                  .Back TO Menu        press 2
                                  .!Exit               press 0 ->  '''))

        if again == 1:
            self.remove_user()
        elif again == 2:
            self.app_manager()
        elif again == 0:
            os.system('cls')
            print("""
                            ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                            ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                            ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                            ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                            ─╔╗──╔╗▄██▄──▄██▄
                            ─║╚╗╔╝║█░████████▌
                            ─╚╗╚╝╔╩═╦╗╔╗█████
                            ──╚╗╔╣╔╗║║║║███▀
                            ───║║║╚╝║╚╝║█▀
                            ───╚╝╚══╩══╝
                             --
                               For Visited 
                               ->>   

                                """)
            exit()
        else:
            os.system('cls')
            print("         Invaild Synatx      " * 50)
            print("""
                            ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                            ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                            ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                            ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                            ─╔╗──╔╗▄██▄──▄██▄
                            ─║╚╗╔╝║█░████████▌
                            ─╚╗╚╝╔╩═╦╗╔╗█████
                            ──╚╗╔╣╔╗║║║║███▀
                            ───║║║╚╝║╚╝║█▀
                            ───╚╝╚══╩══╝
                             --
                               For Visited 
                               ->>   

                                """)






    def profession(self):

        print(''' 
                              _     _   _____            __              _             
                     /\      | |   | | |  __ \          / _|            (_)            
                    /  \   __| | __| | | |__) | __ ___ | |_ ___  ___ ___ _  ___  _ __  
                   / /\ \ / _` |/ _` | |  ___/ '__/ _ \|  _/ _ \/ __/ __| |/ _ \| '_ \ 
                  / ____ \ (_| | (_| | | |   | | | (_) | ||  __/\__ \__ \ | (_) | | | |
                 /_/    \_\__,_|\__,_| |_|   |_|  \___/|_| \___||___/___/_|\___/|_| |_|

               ''')
        print("Go Back - 00")

        pro_code = input("       > Enter ~New profession code -> ")
        if pro_code == '00': self.app_manager()
        profession = input("       > Enter ~New Profession      ->  ")
        rate = input("       > Enter ~New Daily Rate      ->  ")

        add_profession = f"insert into profession values('{pro_code}','{profession}','{rate}')"
        self.cur.execute(add_profession)

        os.system('cls')
        print('''

                              ________      ______    _____  ___    _______  
                             |"      "\    /    " \  (\"   \|"  \  /"     "| 
                             (.  ___  :)  // ____  \ |.\\   \    |(: ______) 
                             |: \   ) || /  /    ) :)|: \.   \\  | \/    |   
                             (| (___\ ||(: (____/ // |.  \    \. | // ___)_  
                             |:       :) \        /  |    \    \ |(:      "| 
                             (________/   \"_____/    \___|\____\) \_______) 


                     ''')
        again = int(input('''\n
                                        .Add Another Profession press 1
                                        .Back TO Menu        press 2
                                        .!Exit               press 0 ->  '''))

        if again == 1:
            self.profession()
        elif again == 2:
            self.app_manager()
        elif again == 0:
            os.system('cls')
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)
            exit()
        else:
            os.system('cls')
            print("         Invaild Synatx      " * 50)
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)

        # self.profession()

    def change_profession_data(self):
        print('''
                 __          _        _         _                      _          
                /  |_  _ __ (_| _    |_) __ _ _|_ _  _  _  o  _ __    | \ _ _|_ _ 
                \__| |(_|| |__|(/_   |   | (_) | (/__> _>  | (_)| |   |_/(_| |_(_|

        ''')
        print("Go Back - 00")

        pro_code = input("          Enter Profession Code (changing_data) - ")
        if pro_code == "00": self.app_manager()

        print("__" * 50)

        ''' get profession details and display it to user '''

        get_data = f"select * from profession where profession_code = {pro_code}"
        self.cur.execute(get_data)
        fetch = self.cur.fetchall()
        print(f"\n        Profession code ->    {fetch[0][0]}")
        print(f"        Profession      ->    {fetch[0][1]}")
        print(f"        Daily Rate      ->    {fetch[0][2]}\n")

        print("__" * 50)

        user_req = input(
            "\n-!What do you wanna Change?\n       profession Name(n)\n        Daily Rate(d)\n          Both(b)      ->   ")
        if user_req == "00": self.app_manager()

        if user_req.lower() == 'n':
            new_name = input("      \nEnter New Profession Name ->  ")
            update = f"update profession set  profession_name = '{new_name}' where profession_code = {pro_code}"

        elif user_req.lower() == 'd':
            new_rate = input("      \nEnter New Daily Rate  ->  ")
            update = f"update profession set daily_salary = '{new_rate}' where profession_code = {pro_code}"

        elif user_req.lower() == 'b':
            new_name = input("      \nEnter New Profession Name ->  ")
            new_rate = input("      \nEnter New Daily Rate  ->  ")
            update = f"update profession set daily_salary = '{new_rate}', profession_name = '{new_name}' where profession_code = '{pro_code}'"

        self.cur.execute(update)


        os.system('cls')
        print('''

                              ________      ______    _____  ___    _______  
                             |"      "\    /    " \  (\"   \|"  \  /"     "| 
                             (.  ___  :)  // ____  \ |.\\   \    |(: ______) 
                             |: \   ) || /  /    ) :)|: \.   \\  | \/    |   
                             (| (___\ ||(: (____/ // |.  \    \. | // ___)_  
                             |:       :) \        /  |    \    \ |(:      "| 
                             (________/   \"_____/    \___|\____\) \_______) 


                     ''')
        again = int(input('''\n
                                        .Change Another Profession Detail press 1
                                        .Back TO Menu                     press 2
                                        .!Exit                            press 0 ->  '''))

        if again == 1:
            self.change_profession_data()
        elif again == 2:
            self.app_manager()
        elif again == 0:
            os.system('cls')
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)
            exit()
        else:
            os.system('cls')
            print("         Invaild Synatx      " * 50)
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)

    def drop_profession(self):
        print('''
              ___      _     _                       __           _          
             |   \ ___| |___| |_ ___   _ __ _ _ ___ / _|___ _____(_)___ _ _  
             | |) / -_) / -_)  _/ -_) | '_ \ '_/ _ \  _/ -_|_-<_-< / _ \ ' \ 
             |___/\___|_\___|\__\___| | .__/_| \___/_| \___/__/__/_\___/_||_|
                                      |_|                                    


               ''')
        print("Go Back - 00")

        r_profession = input("\n       Enter !removing Section Profession_code -> ")
        if r_profession == '00': self.app_manager()

        user_confirm = input(f"       Are You Sure? , you want to Remove {r_profession} (y/n)   ")

        if user_confirm.lower() != 'y':
            os.system('cls')
            self.drop_profession()

        remove_command = f"Delete from profession where profession_code = '{r_profession}'"

        self.cur.execute("select profession_code from profession")
        val = self.cur.fetchall()
        lst = []
        for i in val: lst.append(i[0])

        '''get all users in mysql db and check if remove user in that'''
        if r_profession not in lst:
            os.system('cls')
            print("! Invalid Profession code !" * 5)
            self.drop_profession()

        self.cur.execute(remove_command)


        os.system('cls')
        print('''

                              ________      ______    _____  ___    _______  
                             |"      "\    /    " \  (\"   \|"  \  /"     "| 
                             (.  ___  :)  // ____  \ |.\\   \    |(: ______) 
                             |: \   ) || /  /    ) :)|: \.   \\  | \/    |   
                             (| (___\ ||(: (____/ // |.  \    \. | // ___)_  
                             |:       :) \        /  |    \    \ |(:      "| 
                             (________/   \"_____/    \___|\____\) \_______) 


                     ''')
        again = int(input('''\n
                                        .Delete Another Profession Detail press 1
                                        .Back TO Menu                     press 2
                                        .!Exit                            press 0 ->  '''))

        if again == 1:
            self.drop_profession()
        elif again == 2:
            self.app_manager()
        elif again == 0:
            os.system('cls')
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)
            exit()
        else:
            os.system('cls')
            print("         Invaild Synatx      " * 50)
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)




    def load_data(self):
        self.month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                      'November', 'December']

        print('''
                __    _____    __    ____     ____    __   ____   __   
               (  )  (  _  )  /__\  (  _ \   (  _ \  /__\ (_  _) /__\  
                 )(__  )(_)(  /(__)\  )(_) )   )(_) )/(__)\  )(  /(__)\ 
                (____)(_____)(__)(__)(____/   (____/(__)(__)(__)(__)(__)





                ''')
        print("Go Back - 00")

        d_file = input("     Enter Data_file With Location - ")
        if d_file == '00':self.app_manager()

        with open(d_file, 'r') as File:

            employer_details = {}
            for datas in File.readlines():
                row = datas.split("   ")

                employer_details[row[0]] = {'profession_code': row[1]}, {'Work_days': row[2:]}

        """Upload TO Employer Table """

        user_c = input('Confirm data input to Database -> (yes,no)  ')
        if user_c.lower() != 'yes':
            os.system('cls')
            self.load_data()
        num = 0
        for emplo in employer_details:
            emp_name = emplo
            profession_code = employer_details[emp_name][0]['profession_code']
            emp_code = 'synex' + str(num)
            num += 1

            add_employer_db = f"insert into Employee values('{emp_code}','{emp_name}','{profession_code}')"
            self.cur.execute(add_employer_db)

            work_days = employer_details[emp_name][1]['Work_days']
            ind = 0
            for month in self.month:
                date = work_days[ind]
                ind += 1
                add_work_data_db = f"insert into work_data values ('{emp_code}','{month}','{date}')"
                self.cur.execute(add_work_data_db)


        os.system('cls')
        print('''

                              ________      ______    _____  ___    _______  
                             |"      "\    /    " \  (\"   \|"  \  /"     "| 
                             (.  ___  :)  // ____  \ |.\\   \    |(: ______) 
                             |: \   ) || /  /    ) :)|: \.   \\  | \/    |   
                             (| (___\ ||(: (____/ // |.  \    \. | // ___)_  
                             |:       :) \        /  |    \    \ |(:      "| 
                             (________/   \"_____/    \___|\____\) \_______) 


                     ''')
        again = int(input('''\n
                                        .Load Another File  Data   press 1
                                        .Back TO Menu              press 2
                                        .!Exit                     press 0 ->  '''))

        if again == 1:
            self.load_data()
        elif again == 2:
            self.app_manager()
        elif again == 0:
            os.system('cls')
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)
            exit()
        else:
            os.system('cls')
            print("         Invaild Synatx      " * 50)
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)


    def drop_emp_data(self):
        print('''
               ____                                     _       _        
             |  __ \                                   | |     | |       
             | |__) |___ _ __ ___   _____   _____    __| | __ _| |_ __ _ 
             |  _  // _ \ '_ ` _ \ / _ \ \ / / _ \  / _` |/ _` | __/ _` |
             | | \ \  __/ | | | | | (_) \ V /  __/ | (_| | (_| | || (_| |
             |_|  \_\___|_| |_| |_|\___/ \_/ \___|  \__,_|\__,_|\__\__,_|


             ''')

        print("Go Back - 00")

        get_password = "select Password from app_user where user_type = 'owner'"
        self.cur.execute(get_password)
        p_lst = []
        for passwd in self.cur.fetchall():
            p_lst.append(self.decrypt(passwd[0]))

        ad_passwd = input('      !Enter Administrator passwd   ->  ')
        if ad_passwd == '00': self.app_manager()

        if ad_passwd not in p_lst:
            os.system('cls')
            print('!check passwd again!' * 20)
            self.drop_emp_data()

        u_confirm = input('~ Are You Sure! Reset All_employee Details (yes/no)  -> ')

        if u_confirm.lower() != 'yes':
            os.system('cls')
            self.drop_emp_data()

        self.cur.execute("TRUNCATE table work_data")
        self.cur.execute("TRUNCATE table employee")

        os.system('cls')
        print('''

                              ________      ______    _____  ___    _______  
                             |"      "\    /    " \  (\"   \|"  \  /"     "| 
                             (.  ___  :)  // ____  \ |.\\   \    |(: ______) 
                             |: \   ) || /  /    ) :)|: \.   \\  | \/    |   
                             (| (___\ ||(: (____/ // |.  \    \. | // ___)_  
                             |:       :) \        /  |    \    \ |(:      "| 
                             (________/   \"_____/    \___|\____\) \_______) 


                     ''')
        again = int(input('''\n          
                                        .Back TO Menu              press 1
                                        .!Exit                     press 0 ->  '''))

        if again == 1:
            self.app_manager()

        elif again == 0:
            os.system('cls')
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)
            exit()
        else:
            os.system('cls')
            print("         Invaild Synatx      " * 50)
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)


class Emp_data_calculataion:

    def __init__(self, cur):
        os.system('cls')
        self.cur = cur
        if self.user_choice == 00:
            login =Login(self.cur)

        elif self.user_choice == 1:
            self.emp_salary_sheet()

        elif self.user_choice == 2:
            self.taxes_each_month()

        elif self.user_choice == 3:
            self.synex_profit()

        elif self.user_choice == 4:
            self.emp_year_salary()

        elif self.user_choice == 5:
            self.emp_Month_salary()






    def emp_salary_sheet(self):

        print('''
                            
                 __       _                    __ _               _   
                / _\ __ _| | __ _ _ __ _   _  / _\ |__   ___  ___| |_ 
                \ \ / _` | |/ _` | '__| | | | \ \| '_ \ / _ \/ _ \ __|
                _\ \ (_| | | (_| | |  | |_| | _\ \ | | |  __/  __/ |_ 
                \__/\__,_|_|\__,_|_|   \__, | \__/_| |_|\___|\___|\__|
                                       |___/                          

        
        ''')
        print("Go Back - 00")
        file = input('       Enter file name with location To add data -     ')
        if file == '00':self.emp_manager()

        get_employee_data = 'select * from employee'
        self.cur.execute(get_employee_data)
        fetch = self.cur.fetchall()
        emp_data ={}

        for data in fetch:
            emp_data[data[0]] = {'emp_name':data[1],'profession_code':data[2]}


        with open(file, 'w') as File:
            for names in emp_data:
                emp_name = emp_data[names]['emp_name']
                profession_code = emp_data[names]['profession_code']

                get_daly_rate = f"select daily_salary, profession_name from profession where profession_code = '{profession_code}'"
                self.cur.execute(get_daly_rate)
                fetch = self.cur.fetchall()
                File.write('______________'*50)




                for data in fetch:
                    emp_rate = int(data[0])
                    profession_name = data[1]



                File.write(f"\nEmployee Name -> {emp_name}     Profession -> {profession_name}\n\n")
                print(f"\nEmployee Name -> {emp_name}     Profession -> {profession_name}\n\n")

                '''Get  Work  Days'''

                work_data = f"select * from work_data where emp_code ='{names}'"
                self.cur.execute(work_data)
                fetch = self.cur.fetchall()
                for data in fetch:
                    month = data[1]
                    days = int(data[2])

                    '''Calculate Net Salary'''
                    gross_salary = emp_rate * days
                    epf = gross_salary / 100 * 8
                    tax = gross_salary / 100 * 10
                    safety_items = 500


                    net_salary = gross_salary - epf - tax - safety_items
                    net_salary = net_salary.__round__(2)

                    File.write(f"{month}  |     {net_salary} \n")
                    print(f"{month}  |     {net_salary} ")


        os.system('cls')
        print(f'! Succefully Created {file}')

        print('''

                              ________      ______    _____  ___    _______  
                             |"      "\    /    " \  (\"   \|"  \  /"     "| 
                             (.  ___  :)  // ____  \ |.\\   \    |(: ______) 
                             |: \   ) || /  /    ) :)|: \.   \\  | \/    |   
                             (| (___\ ||(: (____/ // |.  \    \. | // ___)_  
                             |:       :) \        /  |    \    \ |(:      "| 
                             (________/   \"_____/    \___|\____\) \_______) 


                     ''')
        again = int(input('''\n
                                        .Load Data To Another File press 1
                                        .Back TO Menu              press 2
                                        .!Exit                     press 0 ->  '''))

        if again == 1:
            self.emp_salary_sheet()
        elif again == 2:
            self.emp_manager()
        elif again == 0:
            os.system('cls')
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)
            exit()
        else:
            os.system('cls')
            print("         Invaild Synatx      " * 50)
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)



    def taxes_each_month(self):
        print(''' 

                    ___________                            
                    \__    ___/____  ___  ___ ____   ______
                      |    |  \__  \ \  \/  // __ \ /  ___/
                      |    |   / __ \_>    <\  ___/ \___ \ 
                      |____|  (____  /__/\_ \\___  >____  >
                                   \/      \/    \/     \/ 
                                   
                                   
                                   
                                   
                                       ''')
        print("Go Back - 00")

        u_confirmation = input("     Press enter To calculate Tax -")
        if u_confirmation == '00':self.emp_manager()


        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                      'November', 'December']

        get_employee_data = 'select * from employee'
        self.cur.execute(get_employee_data)
        fetch = self.cur.fetchall()
        emp_data = {}

        for data in fetch:
            emp_data[data[0]] = {'emp_name': data[1], 'profession_code': data[2]}

        month_dic = {'January':0, 'February':0, 'March':0, 'April':0, 'May':0, 'June':0, 'July':0, 'August':0, 'September':0, 'October':0,
                      'November':0, 'December':0}


        for key in emp_data:



            for month in months:
                '''Employer Work Days about Month'''


                work_days = f"select days from work_data where emp_code = '{key}' and months ='{month}' "

                self.cur.execute(work_days)
                for fetch in self.cur.fetchall(): work_days = fetch[0]

                profession_code = emp_data[key]['profession_code']

                daily_salary = f"select daily_salary from profession where profession_code = '{profession_code}'"

                self.cur.execute(daily_salary)
                for fetch in self.cur.fetchall(): daily_salary = fetch[0]

                gross_salary = int(work_days) * int(daily_salary)

                tax = gross_salary / 100 * 10

                month_dic[month] +=tax



        print('           __________ ________ --->>Total Tax All Employees Each Month <<--- _________ _________')
        print("\n\n")
        for tax in month_dic:

            print(f"*{tax}   :   {month_dic[tax].__round__(2)}")



        print('''

                              ________      ______    _____  ___    _______  
                             |"      "\    /    " \  (\"   \|"  \  /"     "| 
                             (.  ___  :)  // ____  \ |.\\   \    |(: ______) 
                             |: \   ) || /  /    ) :)|: \.   \\  | \/    |   
                             (| (___\ ||(: (____/ // |.  \    \. | // ___)_  
                             |:       :) \        /  |    \    \ |(:      "| 
                             (________/   \"_____/    \___|\____\) \_______) 


                     ''')
        again = int(input('''\n
                                        .Back TO Menu              press 1
                                        .!Exit                     press 0 ->  '''))

        if again == 1:
            self.emp_manager()
        elif again == 0:
            os.system('cls')
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)
            exit()
        else:
            os.system('cls')
            print("         Invaild Synatx      " * 50)
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)

    def synex_profit(self):


        print('''
                    
                 _______  ______    _______  _______  ___   _______ 
                |       ||    _ |  |       ||       ||   | |       |
                |    _  ||   | ||  |   _   ||    ___||   | |_     _|
                |   |_| ||   |_||_ |  | |  ||   |___ |   |   |   |  
                |    ___||    __  ||  |_|  ||    ___||   |   |   |  
                |   |    |   |  | ||       ||   |    |   |   |   |  
                |___|    |___|  |_||_______||___|    |___|   |___|  

        
        ''')

        print("Go Back - 00")

        u_confirmation = input("     Press enter To calculate Profit -")
        if u_confirmation == '00':self.emp_manager()


        get_employee_data = 'select * from employee'
        self.cur.execute(get_employee_data)
        fetch = self.cur.fetchall()
        emp_data = {}

        for data in fetch:
            emp_data[data[0]] = {'emp_name': data[1], 'profession_code': data[2]}

        employers_netcost= {'January':0, 'February':0, 'March':0, 'April':0, 'May':0, 'June':0, 'July':0, 'August':0, 'September':0, 'October':0,
                      'November':0, 'December':0}

        for names in emp_data:
            emp_name = emp_data[names]['emp_name']
            profession_code = emp_data[names]['profession_code']

            get_daly_rate = f"select daily_salary from profession where profession_code = '{profession_code}'"
            self.cur.execute(get_daly_rate)
            fetch = self.cur.fetchall()


            for data in fetch:
                    emp_rate = int(data[0])





            work_data = f"select * from work_data where emp_code ='{names}'"
            self.cur.execute(work_data)
            fetch = self.cur.fetchall()
            for data in fetch:
                month = data[1]
                days = int(data[2])

                gross_salary =  emp_rate * days
                epf          = gross_salary/100 *8
                tax = gross_salary/100 * 10
                safety_item = 500

                net_cost = gross_salary - epf -tax -safety_item

                employers_netcost[month] += net_cost

        company_profit = 8000000*200
        print('           __________ ________ --->>Company Profit Each Month <<--- _________ _________')
        print("\n\n")
        for month in employers_netcost:

            print(f" *  {month}   ->  {company_profit - employers_netcost[month]} ")


        print('''

                              ________      ______    _____  ___    _______  
                             |"      "\    /    " \  (\"   \|"  \  /"     "| 
                             (.  ___  :)  // ____  \ |.\\   \    |(: ______) 
                             |: \   ) || /  /    ) :)|: \.   \\  | \/    |   
                             (| (___\ ||(: (____/ // |.  \    \. | // ___)_  
                             |:       :) \        /  |    \    \ |(:      "| 
                             (________/   \"_____/    \___|\____\) \_______) 


                     ''')
        again = int(input('''\n
                                        .Back TO Menu              press 1
                                        .!Exit                     press 0 ->  '''))

        if again == 1:
            self.emp_manager()
        elif again == 0:
            os.system('cls')
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)
            exit()
        else:
            os.system('cls')
            print("         Invaild Synatx      " * 50)
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)

    def emp_year_salary(self):

        print('''
                            
                    .-.  .-..----.  .--.  .----.    .----. .----..----.  .----. .----.  .---. 
                     \ \/ / | {_   / {} \ | {}  }   | {}  }| {_  | {}  }/  {}  \| {}  }{_   _}
                      }  {  | {__ /  /\  \| .-. \   | .-. \| {__ | .--' \      /| .-. \  | |  
                      `--'  `----'`-'  `-'`-' `-'   `-' `-'`----'`-'     `----' `-' `-'  `-'  

        
           ''')


        emp_code = input('      Enter Employer_code Calculate Year Salary Report -> ')

        get_employee_data = f"select * from employee where Emp_code = '{emp_code}'"
        self.cur.execute(get_employee_data)
        fetch = self.cur.fetchall()
        emp_data = {}

        for data in fetch:
            emp_data[data[0]] = {'emp_name': data[1], 'profession_code': data[2]}

        employers_netcost = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0,
                             'August': 0, 'September': 0, 'October': 0,
                             'November': 0, 'December': 0}

        open_file = emp_data[emp_code]['emp_name']+'.txt'
        from prettytable import PrettyTable
        x = PrettyTable()
        x.field_names = ["Month","Gross Salary" , "Total Deduction" , "Net Salary"]

        with open(open_file , 'w') as File:

            File.write(f"Salary Sheet Of {emp_data[emp_code]['emp_name']} \n")
            File.write("_"* 100)
            File.write("\n")

            for names in emp_data:
                emp_name = emp_data[names]['emp_name']
                profession_code = emp_data[names]['profession_code']

                get_daly_rate = f"select daily_salary from profession where profession_code = '{profession_code}'"
                self.cur.execute(get_daly_rate)
                fetch = self.cur.fetchall()

                for data in fetch:
                    emp_rate = int(data[0])

                work_data = f"select * from work_data where emp_code ='{names}'"
                self.cur.execute(work_data)
                fetch = self.cur.fetchall()
                for data in fetch:
                    month = data[1]
                    days = int(data[2])

                    gross_salary = emp_rate * days
                    epf = gross_salary / 100 * 8
                    tax = gross_salary / 100 * 10
                    safety_item = 500

                    total_deduction = epf + tax + safety_item

                    net_cost = gross_salary - total_deduction
                    x.add_row([month,gross_salary,total_deduction,net_cost])

            File.write(str(x))

        print(x)

        print(f'! Succefully Created {open_file}')

        print('''

                              ________      ______    _____  ___    _______  
                             |"      "\    /    " \  (\"   \|"  \  /"     "| 
                             (.  ___  :)  // ____  \ |.\\   \    |(: ______) 
                             |: \   ) || /  /    ) :)|: \.   \\  | \/    |   
                             (| (___\ ||(: (____/ // |.  \    \. | // ___)_  
                             |:       :) \        /  |    \    \ |(:      "| 
                             (________/   \"_____/    \___|\____\) \_______) 


                     ''')
        again = int(input('''\n
                                        .Get And CreateFile Other Employer Month Sheet  Press 1
                                        .Back TO Menu                                   press 2
                                        .!Exit                                          press 0 ->  '''))
        if again== 1:
            self.emp_year_salary()
        if again == 2:
            self.emp_manager()
        elif again == 0:
            os.system('cls')
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)
            exit()
        else:
            os.system('cls')
            print("         Invaild Synatx      " * 50)
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)


    def emp_Month_salary(self):
        emp_code = input('      Enter Employer_code Calculate Year Salary Report -> ')
        emp_month = input('      Enter Month In Numbers  -> ')
        emp_month = int(emp_month) - 1

        get_employee_data = f"select * from employee where Emp_code = '{emp_code}'"
        self.cur.execute(get_employee_data)
        fetch = self.cur.fetchall()
        emp_data = {}

        for data in fetch:
            emp_data[data[0]] = {'emp_name': data[1], 'profession_code': data[2]}


        open_file = emp_data[emp_code]['emp_name'] + '.txt'
        from prettytable import PrettyTable
        x = PrettyTable()
        x.field_names = ["Month", "Gross Salary", "Total Deduction", "Net Salary"]
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']

        with open(open_file, 'w') as File:

            File.write(f"Salary Sheet Of {emp_data[emp_code]['emp_name']} \n")
            File.write("_" * 100)
            File.write("\n")

            for names in emp_data:
                emp_name = emp_data[names]['emp_name']
                profession_code = emp_data[names]['profession_code']

                get_daly_rate = f"select daily_salary from profession where profession_code = '{profession_code}'"
                self.cur.execute(get_daly_rate)
                fetch = self.cur.fetchall()

                for data in fetch:
                    emp_rate = int(data[0])

                work_data = f"select * from work_data where emp_code ='{names}' and months = '{months[emp_month]}'"
                self.cur.execute(work_data)
                fetch = self.cur.fetchall()
                for data in fetch:
                    month = data[1]
                    days = int(data[2])

                    gross_salary = emp_rate * days
                    epf = gross_salary / 100 * 8
                    tax = gross_salary / 100 * 10
                    safety_item = 500

                    total_deduction = epf + tax + safety_item

                    net_cost = gross_salary - total_deduction
                    x.add_row([month, gross_salary, total_deduction, net_cost])

            File.write(str(x))
            print(x)

        print(f'! Succefully Created {open_file}')

        print('''

                              ________      ______    _____  ___    _______  
                             |"      "\    /    " \  (\"   \|"  \  /"     "| 
                             (.  ___  :)  // ____  \ |.\\   \    |(: ______) 
                             |: \   ) || /  /    ) :)|: \.   \\  | \/    |   
                             (| (___\ ||(: (____/ // |.  \    \. | // ___)_  
                             |:       :) \        /  |    \    \ |(:      "| 
                             (________/   \"_____/    \___|\____\) \_______) 


                     ''')
        again = int(input('''\n
                                        .Get And CreateFile Other Employer Month Sheet  Press 1
                                        .Back TO Menu                                   press 2
                                        .!Exit                                          press 0 ->  '''))
        if again==1:
            os.system('cls')
            self.emp_Month_salary()
        if again == 2:
            self.emp_manager()
        elif again == 0:
            os.system('cls')
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)
            exit()
        else:
            os.system('cls')
            print("         Invaild Synatx      " * 50)
            print("""
                                 ╔══╗╔╗╔╗╔══╗────────╔╗╔╗
                                 ╚╗╔╝║╚╝║║╚╝║▀██▄─▀█▀║═╔╝
                                 ─║║─║╔╗║║╔╗║─██▀▄─█─║═╚╗
                                 ─╚╝─╚╝╚╝╚╝╚╝─██─▀▄█─╚╝╚╝
                                 ─╔╗──╔╗▄██▄──▄██▄
                                 ─║╚╗╔╝║█░████████▌
                                 ─╚╗╚╝╔╩═╦╗╔╗█████
                                 ──╚╗╔╣╔╗║║║║███▀
                                 ───║║║╚╝║╚╝║█▀
                                 ───╚╝╚══╩══╝
                                  --
                                    For Visited 
                                    ->>   

                                     """)









