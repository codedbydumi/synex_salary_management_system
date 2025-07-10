import os
from hash_password import Hash


class Login(Hash):

    def __init__(self, cur):

        print('''
                         ⠀⢀⣀⣀⣀⣤⣤⣤⣤⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿  Welcome    ⣿⡿⠟⠋⠀⠀⠀⠀⠀
                      ⣄⡉⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⢉⣠⠀
                  _____                          ____          __           __
                 / ___/__  ______  ___  _  __   /  _/___  ____/ /_  _______/ /________  __
                  \__ \/ / / / __ \/ _ \| |/_/   / // __ \/ __  / / / / ___/ __/ ___/ / / /
                 ___/ / /_/ / / / /  __/>  <   _/ // / / / /_/ / /_/ (__  ) /_/ /  / /_/ /
                /____/\__, /_/ /_/\___/_/|_|  /___/_/ /_/\__,_/\__,_/____/\__/_/   \__, /
                     /____/                                                       /____/
                    ⠀⣿⣿⣿⣿⣿   - D B -   ⣿⣿⣿⣿⣿⠀⠀⠀⠀                    -> Database⠀
                ⠀⠀⠀⠀⠀⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠛⠛⠉⠉⠉⠁⠀⠀⠀⠀
        
             ''')

        user_name = input("     User_Name   ->     ")
        passwd = input("      Password   ->     ")

        if user_name.lower() == 'exit' or passwd == 'exit'.lower():
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
        
        self.passwd = passwd
        self.cur = cur
        self.success = True

        # Fixed: Use user_name instead of username
        self.get_data = f"select Password from app_user where Username = '{user_name}'"
        self.user_name_in = f"select Username from app_user"
        self.get_type = f"select user_type from app_user where Username = '{user_name}'"

        # Fixed: Use user_name instead of username
        self.u_correct(user_name, passwd)

    def u_correct(self, user_name, passwd):

        self.cur.execute(self.user_name_in)
        u = []
        usernames = self.cur.fetchall()
        for i in usernames: 
            u.append(i[0])

        if user_name not in u:
            os.system("cls")
            print("\n       Help - Please check Your user_name again !")
            self.__init__(self.cur)

        self.password_correct(passwd, user_name)

    def password_correct(self, passwd, user_name):

        self.cur.execute(self.get_data)
        decrypt_passwd = self.decrypt(self.cur.fetchone()[0])

        if passwd == decrypt_passwd:
            self.user_type(user_name)
        else:
            os.system('cls')
            print("\n       Help - Please check Your Password again !")
            self.__init__(self.cur)

    def user_type(self, user):
        self.cur.execute(self.get_type)
        self.user_t = self.cur.fetchone()[0]
        from user_menu import User
        
        if self.user_t == 'owner':
            user = User("owner", self.cur)
            user.owner()

        if self.user_t == 'admin':
            user = User("admin", self.cur)
            user.emp_manager()