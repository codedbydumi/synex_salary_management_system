import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import font
import os

class SynexIndustriesGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Synex Industries - Salary Management System")
        self.root.geometry("1200x800")
        self.root.configure(bg='#2c3e50')
        
        # Center the window
        self.center_window()
        
        # Configure styles
        self.setup_styles()
        
        # Database connection
        self.setup_database()
        
        # Current user info
        self.current_user = None
        self.user_type = None
        
        # Start with login screen
        self.show_login_screen()
        
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def setup_styles(self):
        """Configure custom styles"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Colors
        self.primary_color = "#2c3e50"
        self.secondary_color = "#3498db"
        self.success_color = "#27ae60"
        self.danger_color = "#e74c3c"
        self.warning_color = "#f39c12"
        
        # Custom fonts
        self.title_font = font.Font(family="Arial", size=24, weight="bold")
        self.heading_font = font.Font(family="Arial", size=14, weight="bold")
        self.normal_font = font.Font(family="Arial", size=10)
        
        # Button styles
        self.style.configure('Primary.TButton',
                           background=self.primary_color,
                           foreground='white',
                           padding=(15, 8),
                           font=('Arial', 11, 'bold'))
        
        self.style.configure('Success.TButton',
                           background=self.success_color,
                           foreground='white',
                           padding=(12, 6),
                           font=('Arial', 10, 'bold'))
        
        self.style.configure('Danger.TButton',
                           background=self.danger_color,
                           foreground='white',
                           padding=(12, 6),
                           font=('Arial', 10, 'bold'))
    
    def setup_database(self):
        """Setup database connection"""
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="synex_industries"
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error connecting to database: {err}")
            self.root.quit()
    
    def clear_window(self):
        """Clear all widgets from window"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_login_screen(self):
        """Display the login screen"""
        self.clear_window()
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill='both', expand=True)
        
        # Create two panels
        left_panel = tk.Frame(main_frame, bg='#34495e', width=600)
        left_panel.pack(side='left', fill='both', expand=True)
        left_panel.pack_propagate(False)
        
        right_panel = tk.Frame(main_frame, bg='white', width=600)
        right_panel.pack(side='right', fill='both', expand=True)
        right_panel.pack_propagate(False)
        
        # Left panel - Company branding
        self.create_branding_panel(left_panel)
        
        # Right panel - Login form
        self.create_login_form(right_panel)
    
    def create_branding_panel(self, parent):
        """Create the left branding panel"""
        brand_frame = tk.Frame(parent, bg='#34495e')
        brand_frame.pack(expand=True)
        
        # Company logo/title
        title_label = tk.Label(brand_frame, 
                              text="SYNEX\nINDUSTRIES", 
                              font=self.title_font,
                              fg='white',
                              bg='#34495e',
                              justify='center')
        title_label.pack(pady=50)
        
        # Subtitle
        subtitle_label = tk.Label(brand_frame,
                                 text="SALARY MANAGEMENT SYSTEM",
                                 font=('Arial', 14, 'bold'),
                                 fg='#3498db',
                                 bg='#34495e')
        subtitle_label.pack(pady=(0, 30))
        
        # ASCII Art
        ascii_art = '''
    ⣿⣿⣿⣿⣿   - D B -   ⣿⣿⣿⣿⣿
        -> Database Management
        '''
        
        art_label = tk.Label(brand_frame,
                            text=ascii_art,
                            font=('Courier', 10),
                            fg='#bdc3c7',
                            bg='#34495e',
                            justify='center')
        art_label.pack(pady=20)
        
        # Version info
        version_label = tk.Label(brand_frame,
                                text="Version 2.0 - Professional Edition",
                                font=('Arial', 9),
                                fg='#95a5a6',
                                bg='#34495e')
        version_label.pack(side='bottom', pady=20)
    
    def create_login_form(self, parent):
        """Create the login form"""
        form_frame = tk.Frame(parent, bg='white')
        form_frame.pack(expand=True)
        
        # Welcome message
        welcome_label = tk.Label(form_frame,
                                text="Welcome Back!",
                                font=('Arial', 22, 'bold'),
                                fg='#2c3e50',
                                bg='white')
        welcome_label.pack(pady=(50, 10))
        
        subtitle_label = tk.Label(form_frame,
                                 text="Please sign in to your account",
                                 font=('Arial', 12),
                                 fg='#7f8c8d',
                                 bg='white')
        subtitle_label.pack(pady=(0, 40))
        
        # Username field
        username_label = tk.Label(form_frame,
                                 text="Username",
                                 font=('Arial', 11, 'bold'),
                                 fg='#2c3e50',
                                 bg='white')
        username_label.pack(anchor='w', padx=60, pady=(0, 5))
        
        self.username_entry = tk.Entry(form_frame,
                                      font=('Arial', 12),
                                      width=30,
                                      relief='solid',
                                      borderwidth=1)
        self.username_entry.pack(pady=(0, 20), padx=60, ipady=8)
        
        # Password field
        password_label = tk.Label(form_frame,
                                 text="Password",
                                 font=('Arial', 11, 'bold'),
                                 fg='#2c3e50',
                                 bg='white')
        password_label.pack(anchor='w', padx=60, pady=(0, 5))
        
        self.password_entry = tk.Entry(form_frame,
                                      font=('Arial', 12),
                                      width=30,
                                      show='*',
                                      relief='solid',
                                      borderwidth=1)
        self.password_entry.pack(pady=(0, 30), padx=60, ipady=8)
        
        # Login button
        login_btn = tk.Button(form_frame,
                             text="LOGIN",
                             font=('Arial', 12, 'bold'),
                             bg='#3498db',
                             fg='white',
                             width=25,
                             height=2,
                             relief='flat',
                             cursor='hand2',
                             command=self.handle_login)
        login_btn.pack(pady=(0, 20))
        
        # Exit button
        exit_btn = tk.Button(form_frame,
                            text="EXIT",
                            font=('Arial', 10),
                            bg='#e74c3c',
                            fg='white',
                            width=25,
                            height=1,
                            relief='flat',
                            cursor='hand2',
                            command=self.handle_exit)
        exit_btn.pack()
        
        # Bind Enter key to login
        self.username_entry.bind('<Return>', lambda e: self.handle_login())
        self.password_entry.bind('<Return>', lambda e: self.handle_login())
        
        # Focus on username field
        self.username_entry.focus()
    
    def handle_login(self):
        """Handle login attempt"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not username or not password:
            messagebox.showwarning("Input Error", "Please enter both username and password!")
            return
        
        if username.lower() == 'exit' or password.lower() == 'exit':
            self.handle_exit()
            return
        
        # Verify credentials
        if self.verify_login(username, password):
            self.current_user = username
            self.show_main_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")
            self.password_entry.delete(0, tk.END)
    
    def verify_login(self, username, password):
        """Verify user credentials with plain text password"""
        try:
            # Check if user exists and get password and user type
            self.cursor.execute("SELECT Password, user_type FROM app_user WHERE Username = %s", (username,))
            result = self.cursor.fetchone()
            
            if not result:
                return False
            
            stored_password, user_type = result
            
            # Compare plain text passwords directly
            if password == stored_password:
                self.user_type = user_type
                return True
            
            return False
            
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error verifying login: {err}")
            return False
    
    def show_main_dashboard(self):
        """Show the main dashboard based on user type"""
        self.clear_window()
        
        # Create main dashboard
        main_frame = tk.Frame(self.root, bg='#ecf0f1')
        main_frame.pack(fill='both', expand=True)
        
        # Header
        self.create_header(main_frame)
        
        # Sidebar
        self.create_sidebar(main_frame)
        
        # Content area
        self.content_frame = tk.Frame(main_frame, bg='white')
        self.content_frame.pack(side='right', fill='both', expand=True, padx=10, pady=10)
        
        # Show welcome message
        self.show_welcome_content()
    
    def create_header(self, parent):
        """Create the header bar"""
        header_frame = tk.Frame(parent, bg='#2c3e50', height=60)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        # Company title
        title_label = tk.Label(header_frame,
                              text="SYNEX INDUSTRIES - SALARY MANAGEMENT",
                              font=('Arial', 16, 'bold'),
                              fg='white',
                              bg='#2c3e50')
        title_label.pack(side='left', padx=20, pady=15)
        
        # User info
        user_info = tk.Label(header_frame,
                            text=f"Welcome, {self.current_user} ({self.user_type.upper()})",
                            font=('Arial', 11),
                            fg='#bdc3c7',
                            bg='#2c3e50')
        user_info.pack(side='right', padx=20, pady=15)
    
    def create_sidebar(self, parent):
        """Create the sidebar navigation"""
        sidebar_frame = tk.Frame(parent, bg='#34495e', width=250)
        sidebar_frame.pack(side='left', fill='y')
        sidebar_frame.pack_propagate(False)
        
        # Navigation title
        nav_title = tk.Label(sidebar_frame,
                            text="NAVIGATION",
                            font=('Arial', 12, 'bold'),
                            fg='white',
                            bg='#34495e')
        nav_title.pack(pady=(20, 10))
        
        # Menu buttons based on user type
        if self.user_type == 'owner':
            self.create_owner_menu(sidebar_frame)
        elif self.user_type == 'admin':
            self.create_admin_menu(sidebar_frame)
        else:
            self.create_user_menu(sidebar_frame)
        
        # Logout button at bottom
        logout_btn = tk.Button(sidebar_frame,
                              text="LOGOUT",
                              font=('Arial', 10, 'bold'),
                              bg='#e74c3c',
                              fg='white',
                              width=20,
                              relief='flat',
                              cursor='hand2',
                              command=self.handle_logout)
        logout_btn.pack(side='bottom', pady=20)
    
    def create_owner_menu(self, parent):
        """Create menu for owner"""
        menu_items = [
            ("🏠 Dashboard", self.show_welcome_content),
            ("⚙️ App Manager", self.show_app_manager),
            ("👥 Employee Manager", self.show_emp_manager),
            ("📊 Reports", self.show_reports)
        ]
        
        for text, command in menu_items:
            btn = tk.Button(parent,
                           text=text,
                           font=('Arial', 11),
                           bg='#34495e',
                           fg='white',
                           width=25,
                           height=2,
                           relief='flat',
                           cursor='hand2',
                           command=command,
                           anchor='w')
            btn.pack(pady=2, padx=10, fill='x')
    
    def create_admin_menu(self, parent):
        """Create menu for admin"""
        menu_items = [
            ("🏠 Dashboard", self.show_welcome_content),
            ("👥 Employee Manager", self.show_emp_manager),
            ("📊 Reports", self.show_reports)
        ]
        
        for text, command in menu_items:
            btn = tk.Button(parent,
                           text=text,
                           font=('Arial', 11),
                           bg='#34495e',
                           fg='white',
                           width=25,
                           height=2,
                           relief='flat',
                           cursor='hand2',
                           command=command,
                           anchor='w')
            btn.pack(pady=2, padx=10, fill='x')
    
    def create_user_menu(self, parent):
        """Create menu for regular user"""
        menu_items = [
            ("🏠 Dashboard", self.show_welcome_content),
            ("👤 My Profile", self.show_profile),
            ("💰 My Salary", self.show_my_salary)
        ]
        
        for text, command in menu_items:
            btn = tk.Button(parent,
                           text=text,
                           font=('Arial', 11),
                           bg='#34495e',
                           fg='white',
                           width=25,
                           height=2,
                           relief='flat',
                           cursor='hand2',
                           command=command,
                           anchor='w')
            btn.pack(pady=2, padx=10, fill='x')
    
    def show_welcome_content(self):
        """Show welcome dashboard content"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        welcome_label = tk.Label(self.content_frame,
                                text=f"Welcome to Synex Industries\nSalary Management System",
                                font=('Arial', 18, 'bold'),
                                fg='#2c3e50',
                                bg='white',
                                justify='center')
        welcome_label.pack(expand=True)
    
    def show_app_manager(self):
        """Show app manager interface (owner only)"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Header
        header_frame = tk.Frame(self.content_frame, bg='white')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(header_frame,
                              text="🔧 System Administrator",
                              font=('Arial', 18, 'bold'),
                              fg='#2c3e50',
                              bg='white')
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(header_frame,
                                 text="Manage application users and system settings",
                                 font=('Arial', 12),
                                 fg='#7f8c8d',
                                 bg='white')
        subtitle_label.pack()
        
        # Menu options
        options_frame = tk.Frame(self.content_frame, bg='white')
        options_frame.pack(expand=True, fill='both', padx=50, pady=20)
        
        # Create grid of buttons
        buttons = [
            ("👤 Add New App User", "Add a new user to the system", self.add_app_user),
            ("🗑️ Remove App User", "Remove an existing user", self.remove_app_user),
            ("💼 Add New Profession", "Add a new job profession", self.add_profession),
            ("✏️ Change Profession Details", "Modify existing profession", self.change_profession),
            ("🗂️ Delete Profession", "Remove a profession", self.delete_profession),
            ("📁 Load Data File", "Import data from file", self.load_data_file),
            ("🗑️ Delete Employee Data", "Remove employee records", self.delete_employee_data)
        ]
        
        row = 0
        col = 0
        for title, desc, command in buttons:
            btn_frame = tk.Frame(options_frame, bg='white', relief='raised', bd=1)
            btn_frame.grid(row=row, column=col, padx=10, pady=10, sticky='ew', ipadx=10, ipady=10)
            
            btn = tk.Button(btn_frame,
                           text=title,
                           font=('Arial', 12, 'bold'),
                           bg='#3498db',
                           fg='white',
                           relief='flat',
                           cursor='hand2',
                           command=command)
            btn.pack(fill='x', pady=(0, 5))
            
            desc_label = tk.Label(btn_frame,
                                 text=desc,
                                 font=('Arial', 9),
                                 fg='#7f8c8d',
                                 bg='white',
                                 wraplength=150)
            desc_label.pack()
            
            col += 1
            if col > 1:  # 2 columns
                col = 0
                row += 1
        
        # Configure grid weights
        for i in range(2):
            options_frame.columnconfigure(i, weight=1)
    
    def show_emp_manager(self):
        """Show employee manager interface"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Header with ASCII art
        header_frame = tk.Frame(self.content_frame, bg='white')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(header_frame,
                              text="👥 Employee Manager",
                              font=('Arial', 18, 'bold'),
                              fg='#2c3e50',
                              bg='white')
        title_label.pack(pady=10)
        
        # ASCII Art
        ascii_art = '''
     ,---.     ,--.          ,--.            ,--.   ,--.                        
    /  O  \\  ,-|  |,--,--,--.`--',--,--,     |   `.'   | ,---. ,--,--, ,--.,--. 
   |  .-.  |' .-. ||        |,--.|      \\    |  |'.'|  || .-. :|      \\|  ||  | 
   |  | |  |\\ `-' ||  |  |  ||  ||  ||  |    |  |   |  |\\   --.|  ||  |'  ''  ' 
   `--' `--' `---' `--`--`--'`--'`--''--'    `--'   `--' `----'`--''--' `----'  
        '''
        
        art_label = tk.Label(header_frame,
                            text=ascii_art,
                            font=('Courier', 8),
                            fg='#3498db',
                            bg='white',
                            justify='center')
        art_label.pack(pady=10)
        
        subtitle_label = tk.Label(header_frame,
                                 text="Synex Salary Calculating System",
                                 font=('Arial', 12, 'italic'),
                                 fg='#7f8c8d',
                                 bg='white')
        subtitle_label.pack()
        
        # Menu options
        options_frame = tk.Frame(self.content_frame, bg='white')
        options_frame.pack(expand=True, fill='both', padx=50, pady=20)
        
        buttons = [
            ("📊 Create Employee Salary Sheet", "Generate salary sheets for all employees", self.create_salary_sheet),
            ("💰 Calculate Monthly Taxes", "Calculate total taxes from all employees", self.calculate_taxes),
            ("📈 Calculate Company Profit", "Calculate monthly company profit", self.calculate_profit),
            ("📋 Create Year Salary Report", "Generate annual salary report for employee", self.create_year_report),
            ("📄 Monthly Salary Report", "Create salary report for specific month", self.create_month_report)
        ]
        
        for i, (title, desc, command) in enumerate(buttons):
            btn_frame = tk.Frame(options_frame, bg='white', relief='raised', bd=1)
            btn_frame.pack(fill='x', pady=5, padx=20)
            
            btn = tk.Button(btn_frame,
                           text=f"{i+1}. {title}",
                           font=('Arial', 12, 'bold'),
                           bg='#27ae60',
                           fg='white',
                           relief='flat',
                           cursor='hand2',
                           command=command,
                           height=2)
            btn.pack(fill='x', pady=5, padx=10)
            
            desc_label = tk.Label(btn_frame,
                                 text=desc,
                                 font=('Arial', 10),
                                 fg='#7f8c8d',
                                 bg='white')
            desc_label.pack(pady=(0, 5))
    
    def add_app_user(self):
        """Add new app user interface"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Header
        header_frame = tk.Frame(self.content_frame, bg='white')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(header_frame,
                            text="👤 Add New App User",
                            font=('Arial', 18, 'bold'),
                            fg='#2c3e50',
                            bg='white')
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(header_frame,
                                text="Create a new user account for the system",
                                font=('Arial', 12),
                                fg='#7f8c8d',
                                bg='white')
        subtitle_label.pack()
        
        # Form frame
        form_frame = tk.Frame(self.content_frame, bg='white')
        form_frame.pack(expand=True, fill='both', padx=50, pady=20)
        
        # Username field
        username_label = tk.Label(form_frame,
                                text="Username:",
                                font=('Arial', 12, 'bold'),
                                fg='#2c3e50',
                                bg='white')
        username_label.grid(row=0, column=0, sticky='w', pady=(10, 5), padx=(0, 10))
        
        username_entry = tk.Entry(form_frame,
                                font=('Arial', 12),
                                width=30,
                                relief='solid',
                                borderwidth=1)
        username_entry.grid(row=0, column=1, pady=(10, 5), padx=(0, 10), ipady=5)
        
        # Password field
        password_label = tk.Label(form_frame,
                                text="Password:",
                                font=('Arial', 12, 'bold'),
                                fg='#2c3e50',
                                bg='white')
        password_label.grid(row=1, column=0, sticky='w', pady=(10, 5), padx=(0, 10))
        
        password_entry = tk.Entry(form_frame,
                                font=('Arial', 12),
                                width=30,
                                relief='solid',
                                borderwidth=1)
        password_entry.grid(row=1, column=1, pady=(10, 5), padx=(0, 10), ipady=5)
        
        # Confirm Password field
        confirm_password_label = tk.Label(form_frame,
                                        text="Confirm Password:",
                                        font=('Arial', 12, 'bold'),
                                        fg='#2c3e50',
                                        bg='white')
        confirm_password_label.grid(row=2, column=0, sticky='w', pady=(10, 5), padx=(0, 10))
        
        confirm_password_entry = tk.Entry(form_frame,
                                        font=('Arial', 12),
                                        width=30,
                                        relief='solid',
                                        borderwidth=1)
        confirm_password_entry.grid(row=2, column=1, pady=(10, 5), padx=(0, 10), ipady=5)
        
        # User Type field
        user_type_label = tk.Label(form_frame,
                                text="User Type:",
                                font=('Arial', 12, 'bold'),
                                fg='#2c3e50',
                                bg='white')
        user_type_label.grid(row=3, column=0, sticky='w', pady=(10, 5), padx=(0, 10))
        
        user_type_var = tk.StringVar(value="admin")
        user_type_combo = ttk.Combobox(form_frame,
                                    textvariable=user_type_var,
                                    values=["owner", "admin", "user"],
                                    font=('Arial', 12),
                                    width=28,
                                    state="readonly")
        user_type_combo.grid(row=3, column=1, pady=(10, 5), padx=(0, 10), ipady=5)
        
        # Buttons frame
        buttons_frame = tk.Frame(form_frame, bg='white')
        buttons_frame.grid(row=4, column=0, columnspan=2, pady=30)
        
        def validate_and_add_user():
            """Validate form data and add user to database"""
            username = username_entry.get().strip()
            password = password_entry.get().strip()
            confirm_password = confirm_password_entry.get().strip()
            user_type = user_type_var.get()
            
            # Validation
            if not username:
                messagebox.showerror("Validation Error", "Username is required!")
                username_entry.focus()
                return
            
            if len(username) < 3:
                messagebox.showerror("Validation Error", "Username must be at least 3 characters!")
                username_entry.focus()
                return
            
            if not password:
                messagebox.showerror("Validation Error", "Password is required!")
                password_entry.focus()
                return
            
            if len(password) < 6:
                messagebox.showerror("Validation Error", "Password must be at least 6 characters!")
                password_entry.focus()
                return
            
            if password != confirm_password:
                messagebox.showerror("Validation Error", "Passwords do not match!")
                confirm_password_entry.focus()
                return
            
            # Check if username already exists
            try:
                self.cursor.execute("SELECT Username FROM app_user WHERE Username = %s", (username,))
                if self.cursor.fetchone():
                    messagebox.showerror("Error", "Username already exists! Please choose a different username.")
                    username_entry.focus()
                    return
                
                # Insert new user with plain text password (NO ENCRYPTION)
                insert_query = "INSERT INTO app_user (Username, Password, user_type) VALUES (%s, %s, %s)"
                self.cursor.execute(insert_query, (username, password, user_type))
                self.connection.commit()
                
                messagebox.showinfo("Success", f"User '{username}' has been created successfully!")
                
                # Clear form
                username_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                confirm_password_entry.delete(0, tk.END)
                user_type_var.set("admin")
                username_entry.focus()
                
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error adding user: {err}")
                self.connection.rollback()
        
        def clear_form():
            """Clear all form fields"""
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            confirm_password_entry.delete(0, tk.END)
            user_type_var.set("admin")
            username_entry.focus()
       
        
        # Add User button
        add_btn = tk.Button(buttons_frame,
                           text="ADD USER",
                           font=('Arial', 12, 'bold'),
                           bg='#27ae60',
                           fg='white',
                           width=15,
                           height=2,
                           relief='flat',
                           cursor='hand2',
                           command=validate_and_add_user)
        add_btn.pack(side='left', padx=(0, 10))
        
        # Clear button
        clear_btn = tk.Button(buttons_frame,
                             text="CLEAR",
                             font=('Arial', 12, 'bold'),
                             bg='#f39c12',
                             fg='white',
                             width=15,
                             height=2,
                             relief='flat',
                             cursor='hand2',
                             command=clear_form)
        clear_btn.pack(side='left', padx=(0, 10))
        
        # Back button
        back_btn = tk.Button(buttons_frame,
                            text="BACK",
                            font=('Arial', 12, 'bold'),
                            bg='#95a5a6',
                            fg='white',
                            width=15,
                            height=2,
                            relief='flat',
                            cursor='hand2',
                            command=self.show_app_manager)
        back_btn.pack(side='left')
        
        # Configure grid weights
        form_frame.columnconfigure(1, weight=1)
        
        # Focus on username field
        username_entry.focus()

    def remove_app_user(self):
        """Remove app user interface"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Header
        header_frame = tk.Frame(self.content_frame, bg='white')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(header_frame,
                              text="🗑️ Remove App User",
                              font=('Arial', 18, 'bold'),
                              fg='#2c3e50',
                              bg='white')
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(header_frame,
                                 text="Remove an existing user from the system",
                                 font=('Arial', 12),
                                 fg='#7f8c8d',
                                 bg='white')
        subtitle_label.pack()
        
        # Warning message
        warning_frame = tk.Frame(self.content_frame, bg='#ffe6e6', relief='solid', bd=1)
        warning_frame.pack(fill='x', padx=50, pady=10)
        
        warning_label = tk.Label(warning_frame,
                                text="⚠️ WARNING: This action cannot be undone! Please be careful when removing users.",
                                font=('Arial', 11, 'bold'),
                                fg='#e74c3c',
                                bg='#ffe6e6')
        warning_label.pack(pady=10)
        
        # Main content frame
        main_frame = tk.Frame(self.content_frame, bg='white')
        main_frame.pack(expand=True, fill='both', padx=50, pady=20)
        
        # Users list frame
        list_frame = tk.Frame(main_frame, bg='white')
        list_frame.pack(fill='both', expand=True, pady=(0, 20))
        
        # List header
        list_header = tk.Label(list_frame,
                              text="Select User to Remove:",
                              font=('Arial', 14, 'bold'),
                              fg='#2c3e50',
                              bg='white')
        list_header.pack(pady=(0, 10))
        
        # Create treeview for users list
        columns = ('Username', 'User Type', 'Status')
        tree_frame = tk.Frame(list_frame, bg='white')
        tree_frame.pack(fill='both', expand=True)
        
        users_tree = ttk.Treeview(tree_frame, columns=columns, show='headings', height=10)
        
        # Configure columns
        users_tree.heading('Username', text='Username')
        users_tree.heading('User Type', text='User Type')
        users_tree.heading('Status', text='Status')
        
        users_tree.column('Username', width=200, anchor='center')
        users_tree.column('User Type', width=150, anchor='center')
        users_tree.column('Status', width=150, anchor='center')
        
        # Scrollbar for treeview
        scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=users_tree.yview)
        users_tree.configure(yscrollcommand=scrollbar.set)
        
        users_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        def load_users():
            """Load users from database into treeview"""
            # Clear existing items
            for item in users_tree.get_children():
                users_tree.delete(item)
            
            try:
                # Get all users except the current logged-in user (can't delete yourself)
                self.cursor.execute("""
                    SELECT Username, user_type 
                    FROM app_user 
                    WHERE Username != %s 
                    ORDER BY Username
                """, (self.current_user,))
                
                users = self.cursor.fetchall()
                
                if not users:
                    # Insert a message if no users found
                    users_tree.insert('', tk.END, values=('No other users found', '', ''))
                    return
                
                for username, user_type in users:
                    status = "Active"  # You can modify this based on your needs
                    users_tree.insert('', tk.END, values=(username, user_type.title(), status))
                    
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error loading users: {err}")
        
        def refresh_users():
            """Refresh the users list"""
            load_users()
            messagebox.showinfo("Refreshed", "Users list has been refreshed!")
        
        def validate_and_remove_user():
            """Validate selection and remove user"""
            selected_item = users_tree.selection()
            
            if not selected_item:
                messagebox.showwarning("No Selection", "Please select a user to remove!")
                return
            
            # Get selected user details
            selected_user_data = users_tree.item(selected_item[0])['values']
            
            if not selected_user_data or selected_user_data[0] == 'No other users found':
                messagebox.showwarning("Invalid Selection", "Please select a valid user!")
                return
            
            username_to_remove = selected_user_data[0]
            user_type_to_remove = selected_user_data[1]
            
            # Prevent removing yourself (additional check)
            if username_to_remove == self.current_user:
                messagebox.showerror("Error", "You cannot remove your own account!")
                return
            
            # Show confirmation dialog with user details
            confirm_message = f"""Are you sure you want to remove the following user?

    Username: {username_to_remove}
    User Type: {user_type_to_remove}

    This action cannot be undone!"""
            
            result = messagebox.askyesno("Confirm Removal", confirm_message, icon='warning')
            
            if result:
                try:
                    # Delete user from database
                    delete_query = "DELETE FROM app_user WHERE Username = %s"
                    self.cursor.execute(delete_query, (username_to_remove,))
                    
                    if self.cursor.rowcount > 0:
                        self.connection.commit()
                        messagebox.showinfo("Success", f"User '{username_to_remove}' has been removed successfully!")
                        
                        # Refresh the users list
                        load_users()
                    else:
                        messagebox.showerror("Error", "User not found or could not be removed!")
                        
                except mysql.connector.Error as err:
                    messagebox.showerror("Database Error", f"Error removing user: {err}")
                    self.connection.rollback()
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg='white')
        buttons_frame.pack(pady=20)
        
        # Remove User button
        remove_btn = tk.Button(buttons_frame,
                              text="REMOVE USER",
                              font=('Arial', 12, 'bold'),
                              bg='#e74c3c',
                              fg='white',
                              width=15,
                              height=2,
                              relief='flat',
                              cursor='hand2',
                              command=validate_and_remove_user)
        remove_btn.pack(side='left', padx=(0, 10))
        
        # Refresh button
        refresh_btn = tk.Button(buttons_frame,
                               text="REFRESH",
                               font=('Arial', 12, 'bold'),
                               bg='#3498db',
                               fg='white',
                               width=15,
                               height=2,
                               relief='flat',
                               cursor='hand2',
                               command=refresh_users)
        refresh_btn.pack(side='left', padx=(0, 10))
        
        # Back button
        back_btn = tk.Button(buttons_frame,
                            text="BACK",
                            font=('Arial', 12, 'bold'),
                            bg='#95a5a6',
                            fg='white',
                            width=15,
                            height=2,
                            relief='flat',
                            cursor='hand2',
                            command=self.show_app_manager)
        back_btn.pack(side='left')
        
        # Load users initially
        load_users()
    
    def add_profession(self):
        messagebox.showinfo("Feature", "Add Profession functionality will be implemented here")
    
    def change_profession(self):
        messagebox.showinfo("Feature", "Change Profession functionality will be implemented here")
    
    def delete_profession(self):
        messagebox.showinfo("Feature", "Delete Profession functionality will be implemented here")
    
    def load_data_file(self):
        messagebox.showinfo("Feature", "Load Data File functionality will be implemented here")
    
    def delete_employee_data(self):
        messagebox.showinfo("Feature", "Delete Employee Data functionality will be implemented here")
    
    # Placeholder methods for Employee Manager functions
    def create_salary_sheet(self):
        messagebox.showinfo("Feature", "Create Salary Sheet functionality will be implemented here")
    
    def calculate_taxes(self):
        messagebox.showinfo("Feature", "Calculate Taxes functionality will be implemented here")
    
    def calculate_profit(self):
        messagebox.showinfo("Feature", "Calculate Profit functionality will be implemented here")
    
    def create_year_report(self):
        messagebox.showinfo("Feature", "Create Year Report functionality will be implemented here")
    
    def create_month_report(self):
        messagebox.showinfo("Feature", "Create Month Report functionality will be implemented here")
    
    def show_reports(self):
        """Show reports interface"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        title_label = tk.Label(self.content_frame,
                              text="Reports",
                              font=('Arial', 16, 'bold'),
                              fg='#2c3e50',
                              bg='white')
        title_label.pack(pady=20)
        
        placeholder = tk.Label(self.content_frame,
                              text="Reports and analytics will be displayed here.\nThis will include salary reports, employee statistics, etc.",
                              font=('Arial', 12),
                              fg='#7f8c8d',
                              bg='white',
                              justify='center')
        placeholder.pack(expand=True)
    
    def show_settings(self):
        """Show settings interface"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        title_label = tk.Label(self.content_frame,
                              text="Settings",
                              font=('Arial', 16, 'bold'),
                              fg='#2c3e50',
                              bg='white')
        title_label.pack(pady=20)
        
        placeholder = tk.Label(self.content_frame,
                              text="System settings and configuration options will be available here.",
                              font=('Arial', 12),
                              fg='#7f8c8d',
                              bg='white',
                              justify='center')
        placeholder.pack(expand=True)
    
    def show_profile(self):
        """Show user profile"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        title_label = tk.Label(self.content_frame,
                              text="My Profile",
                              font=('Arial', 16, 'bold'),
                              fg='#2c3e50',
                              bg='white')
        title_label.pack(pady=20)
        
        placeholder = tk.Label(self.content_frame,
                              text="User profile information will be displayed here.",
                              font=('Arial', 12),
                              fg='#7f8c8d',
                              bg='white',
                              justify='center')
        placeholder.pack(expand=True)
    
    def show_my_salary(self):
        """Show user's salary information"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        title_label = tk.Label(self.content_frame,
                              text="My Salary Information",
                              font=('Arial', 16, 'bold'),
                              fg='#2c3e50',
                              bg='white')
        title_label.pack(pady=20)
        
        placeholder = tk.Label(self.content_frame,
                              text="Your salary information and pay slips will be displayed here.",
                              font=('Arial', 12),
                              fg='#7f8c8d',
                              bg='white',
                              justify='center')
        placeholder.pack(expand=True)
    
    def handle_logout(self):
        """Handle user logout"""
        result = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if result:
            self.current_user = None
            self.user_type = None
            self.show_login_screen()
    
    def handle_exit(self):
        """Handle application exit"""
        result = messagebox.askyesno("Exit", "Are you sure you want to exit the application?")
        if result:
            try:
                self.connection.close()
            except:
                pass
            self.root.quit()
    
    def run(self):
        """Start the application"""
        self.root.protocol("WM_DELETE_WINDOW", self.handle_exit)
        self.root.mainloop()

if __name__ == "__main__":
    app = SynexIndustriesGUI()
    app.run()