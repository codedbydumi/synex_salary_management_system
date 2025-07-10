import os
import sys
from hash_password import Hash


class Login(Hash):

    def __init__(self, cur):
        self.cur = cur
        self.success = False
        self.max_attempts = 3
        self.current_attempts = 0
        
        # Display welcome screen and handle login
        self.display_welcome()
        self.handle_login()

    def display_welcome(self):
        """Display the welcome screen with proper encoding handling"""
        try:
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
        except UnicodeEncodeError:
            print('''
                 _____                          ____          __           __
                / ___/__  ______  ___  _  __   /  _/___  ____/ /_  _______/ /________  __
                 \__ \/ / / / __ \/ _ \| |/_/   / // __ \/ __  / / / / ___/ __/ ___/ / / /
                ___/ / /_/ / / / /  __/>  <   _/ // / / / /_/ / /_/ (__  ) /_/ /  / /_/ /
               /____/\__, /_/ /_/\___/_/|_|  /___/_/ /_/\__,_/\__,_/____/\__/_/   \__, /
                    /____/                                                       /____/
                                    Welcome to Synex Industry Database
            ''')

    def handle_login(self):
        """Handle the login process with attempt limiting"""
        while self.current_attempts < self.max_attempts:
            try:
                user_name = input("     User_Name   ->     ").strip()
                passwd = input("      Password   ->     ").strip()

                # Check for exit command
                if user_name.lower() == 'exit' or passwd.lower() == 'exit':
                    self.display_exit_message()
                    sys.exit(0)

                # Validate input
                if not user_name or not passwd:
                    print("\n       Please enter both username and password!")
                    self.current_attempts += 1
                    continue

                # Attempt login
                if self.authenticate_user(user_name, passwd):
                    self.success = True
                    self.handle_user_type(user_name)
                    break
                else:
                    self.current_attempts += 1
                    remaining = self.max_attempts - self.current_attempts
                    if remaining > 0:
                        print(f"\n       Invalid credentials! {remaining} attempts remaining.")
                    else:
                        print("\n       Maximum login attempts exceeded. Access denied.")
                        sys.exit(1)

            except KeyboardInterrupt:
                print("\n\nLogin cancelled by user.")
                sys.exit(0)
            except Exception as e:
                print(f"\n       Login error: {e}")
                self.current_attempts += 1

    def display_exit_message(self):
        """Display exit message with proper encoding handling"""
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
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
                       Thank you for visiting!
                       ->>   
                        """)
        except UnicodeEncodeError:
            print("\n       Thank you for visiting Synex Industry!\n       Goodbye!")

    def authenticate_user(self, user_name, passwd):
        """Authenticate user with proper error handling and SQL injection prevention"""
        try:
            # Use parameterized queries to prevent SQL injection
            self.cur.execute("SELECT Username FROM app_user WHERE Username = %s", (user_name,))
            user_result = self.cur.fetchone()
            
            if not user_result:
                print("\n       User not found!")
                return False

            # Get encrypted password
            self.cur.execute("SELECT Password FROM app_user WHERE Username = %s", (user_name,))
            password_result = self.cur.fetchone()
            
            if not password_result:
                print("\n       Password retrieval failed!")
                return False

            # Decrypt and compare password
            try:
                decrypted_passwd = self.decrypt(password_result[0])
                return passwd == decrypted_passwd
            except Exception as e:
                print(f"\n       Password decryption error: {e}")
                return False

        except Exception as e:
            print(f"\n       Database error during authentication: {e}")
            return False

    def handle_user_type(self, user_name):
        """Handle user type determination and menu loading"""
        try:
            # Get user type with parameterized query
            self.cur.execute("SELECT user_type FROM app_user WHERE Username = %s", (user_name,))
            user_type_result = self.cur.fetchone()
            
            if not user_type_result:
                print("\n       User type not found!")
                return

            user_type = user_type_result[0]
            
            # Import here to avoid circular imports
            from user_menu import User
            
            # Create user object and load appropriate menu
            user_obj = User(user_type, self.cur)
            
            if user_type == 'owner':
                user_obj.owner()
            elif user_type == 'admin':
                user_obj.emp_manager()
            else:
                print(f"\n       Unknown user type: {user_type}")
                
        except ImportError:
            print("\n       Error: Could not load user menu module!")
        except Exception as e:
            print(f"\n       Error determining user type: {e}")

    def restart_login(self):
        """Restart the login process"""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.current_attempts = 0
        self.display_welcome()
        self.handle_login()