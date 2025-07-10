import tkinter as tk
from tkinter import ttk, messagebox
import datetime  
import mysql.connector
from tkinter import font
import os
import sys


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
        """Show modern employee manager interface with card-based layout"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Header
        header_frame = tk.Frame(self.content_frame, bg='white')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(header_frame,
                            text="👥 Employee Manager",
                            font=('Arial', 18, 'bold'),
                            fg='#2c3e50',
                            bg='white')
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(header_frame,
                                text="Comprehensive salary management and reporting system",
                                font=('Arial', 12),
                                fg='#7f8c8d',
                                bg='white')
        subtitle_label.pack()
        
        # Menu options
        options_frame = tk.Frame(self.content_frame, bg='white')
        options_frame.pack(expand=True, fill='both', padx=50, pady=20)
        
        # Create grid of buttons
        buttons = [
            ("📊 Create Employee Salary Sheet", "Generate comprehensive salary sheets for all employees", self.create_salary_sheet),
            ("💰 Calculate Monthly Taxes", "Calculate and summarize total taxes from all employees", self.calculate_taxes),
            ("📈 Calculate Company Profit", "Analyze and calculate monthly company profit margins", self.calculate_profit),
            ("📋 Create Year Salary Report", "Generate detailed annual salary report for employees", self.create_year_report),
            ("📄 Monthly Salary Report", "Create comprehensive salary report for specific month", self.create_month_report)
        ]
        
        row = 0
        col = 0
        for title, desc, command in buttons:
            btn_frame = tk.Frame(options_frame, bg='white', relief='raised', bd=1)
            btn_frame.grid(row=row, column=col, padx=10, pady=10, sticky='ew', ipadx=10, ipady=10)
            
            btn = tk.Button(btn_frame,
                        text=title,
                        font=('Arial', 12, 'bold'),
                        bg='#27ae60',
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

    #
    def darken_color(self, color):
        """Helper function to darken a color for hover effect"""
        color_map = {
            "#27ae60": "#229954",
            "#e74c3c": "#c0392b",
            "#3498db": "#2980b9",
            "#f39c12": "#e67e22",
            "#9b59b6": "#8e44ad"
        }
        return color_map.get(color, color)
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
        """Add new profession interface"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Header
        header_frame = tk.Frame(self.content_frame, bg='white')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(header_frame,
                            text="💼 Add New Profession",
                            font=('Arial', 18, 'bold'),
                            fg='#2c3e50',
                            bg='white')
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(header_frame,
                                text="Create a new profession with salary details",
                                font=('Arial', 12),
                                fg='#7f8c8d',
                                bg='white')
        subtitle_label.pack()
        
        # Form frame
        form_frame = tk.Frame(self.content_frame, bg='white')
        form_frame.pack(expand=True, fill='both', padx=50, pady=20)
        
        # Profession Code field
        profession_code_label = tk.Label(form_frame,
                                    text="Profession Code:",
                                    font=('Arial', 12, 'bold'),
                                    fg='#2c3e50',
                                    bg='white')
        profession_code_label.grid(row=0, column=0, sticky='w', pady=(10, 5), padx=(0, 10))
        
        profession_code_entry = tk.Entry(form_frame,
                                    font=('Arial', 12),
                                    width=30,
                                    relief='solid',
                                    borderwidth=1)
        profession_code_entry.grid(row=0, column=1, pady=(10, 5), padx=(0, 10), ipady=5)
        
        # Profession Name field
        profession_name_label = tk.Label(form_frame,
                                    text="Profession Name:",
                                    font=('Arial', 12, 'bold'),
                                    fg='#2c3e50',
                                    bg='white')
        profession_name_label.grid(row=1, column=0, sticky='w', pady=(10, 5), padx=(0, 10))
        
        profession_name_entry = tk.Entry(form_frame,
                                    font=('Arial', 12),
                                    width=30,
                                    relief='solid',
                                    borderwidth=1)
        profession_name_entry.grid(row=1, column=1, pady=(10, 5), padx=(0, 10), ipady=5)
        
        # Daily Salary field
        daily_salary_label = tk.Label(form_frame,
                                    text="Daily Salary:",
                                    font=('Arial', 12, 'bold'),
                                    fg='#2c3e50',
                                    bg='white')
        daily_salary_label.grid(row=2, column=0, sticky='w', pady=(10, 5), padx=(0, 10))
        
        daily_salary_entry = tk.Entry(form_frame,
                                    font=('Arial', 12),
                                    width=30,
                                    relief='solid',
                                    borderwidth=1)
        daily_salary_entry.grid(row=2, column=1, pady=(10, 5), padx=(0, 10), ipady=5)
        
        # Buttons frame
        buttons_frame = tk.Frame(form_frame, bg='white')
        buttons_frame.grid(row=3, column=0, columnspan=2, pady=30)
        
        def validate_and_add_profession():
            """Validate form data and add profession to database"""
            profession_code = profession_code_entry.get().strip()
            profession_name = profession_name_entry.get().strip()
            daily_salary = daily_salary_entry.get().strip()
            
            # Validation
            if not profession_code:
                messagebox.showerror("Validation Error", "Profession Code is required!")
                profession_code_entry.focus()
                return
            
            if not profession_name:
                messagebox.showerror("Validation Error", "Profession Name is required!")
                profession_name_entry.focus()
                return
            
            if not daily_salary:
                messagebox.showerror("Validation Error", "Daily Salary is required!")
                daily_salary_entry.focus()
                return
            
            # Validate daily salary is a number
            try:
                daily_salary_float = float(daily_salary)
                if daily_salary_float < 0:
                    messagebox.showerror("Validation Error", "Daily Salary must be a positive number!")
                    daily_salary_entry.focus()
                    return
            except ValueError:
                messagebox.showerror("Validation Error", "Daily Salary must be a valid number!")
                daily_salary_entry.focus()
                return
            
            # Check if profession code already exists
            try:
                self.cursor.execute("SELECT profession_code FROM profession WHERE profession_code = %s", (profession_code,))
                if self.cursor.fetchone():
                    messagebox.showerror("Error", "Profession Code already exists! Please choose a different code.")
                    profession_code_entry.focus()
                    return
                
                # Insert new profession
                insert_query = "INSERT INTO profession (profession_code, profession_name, daily_salary) VALUES (%s, %s, %s)"
                self.cursor.execute(insert_query, (profession_code, profession_name, daily_salary_float))
                self.connection.commit()
                
                messagebox.showinfo("Success", f"Profession '{profession_name}' has been added successfully!")
                
                # Clear form
                profession_code_entry.delete(0, tk.END)
                profession_name_entry.delete(0, tk.END)
                daily_salary_entry.delete(0, tk.END)
                profession_code_entry.focus()
                
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error adding profession: {err}")
                self.connection.rollback()
        
        def clear_form():
            """Clear all form fields"""
            profession_code_entry.delete(0, tk.END)
            profession_name_entry.delete(0, tk.END)
            daily_salary_entry.delete(0, tk.END)
            profession_code_entry.focus()
        
        # Add Profession button
        add_btn = tk.Button(buttons_frame,
                        text="ADD PROFESSION",
                        font=('Arial', 12, 'bold'),
                        bg='#27ae60',
                        fg='white',
                        width=15,
                        height=2,
                        relief='flat',
                        cursor='hand2',
                        command=validate_and_add_profession)
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
        
        # Focus on profession code field
        profession_code_entry.focus()

    def change_profession(self):
        """Change profession details interface"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Header
        header_frame = tk.Frame(self.content_frame, bg='white')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(header_frame,
                            text="✏️ Change Profession Details",
                            font=('Arial', 18, 'bold'),
                            fg='#2c3e50',
                            bg='white')
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(header_frame,
                                text="Select a profession from the list below to modify its details",
                                font=('Arial', 12),
                                fg='#7f8c8d',
                                bg='white')
        subtitle_label.pack()
        
        # Main content frame with scrollable area
        main_frame = tk.Frame(self.content_frame, bg='white')
        main_frame.pack(expand=True, fill='both', padx=20, pady=10)
        
        # Create a canvas and scrollbar for scrollable content
        canvas = tk.Canvas(main_frame, bg='white')
        scrollbar_main = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar_main.set)
        
        # Edit form frame (at the top, initially hidden)
        edit_container = tk.Frame(scrollable_frame, bg='white')
        edit_container.pack(fill='x', pady=(0, 20))
        
        edit_frame = tk.Frame(edit_container, bg='#f0f8ff', relief='solid', bd=2)
        edit_frame.pack(fill='x', padx=20, pady=10)
        edit_frame.pack_forget()  # Hide initially
        
        # Form title with prominent styling
        form_title = tk.Label(edit_frame,
                            text="📝 Edit Selected Profession",
                            font=('Arial', 16, 'bold'),
                            fg='#2c3e50',
                            bg='#f0f8ff')
        form_title.pack(pady=(15, 10))
        
        # Form fields container
        fields_container = tk.Frame(edit_frame, bg='#f0f8ff')
        fields_container.pack(padx=30, pady=(0, 15))
        
        # Create a grid layout for form fields
        fields_frame = tk.Frame(fields_container, bg='#f0f8ff')
        fields_frame.pack()
        
        # Profession Code field (read-only)
        code_label = tk.Label(fields_frame,
                            text="Profession Code:",
                            font=('Arial', 12, 'bold'),
                            fg='#2c3e50',
                            bg='#f0f8ff')
        code_label.grid(row=0, column=0, sticky='w', pady=(10, 5), padx=(0, 15))
        
        code_entry = tk.Entry(fields_frame,
                            font=('Arial', 12),
                            width=30,
                            relief='solid',
                            borderwidth=1,
                            state='readonly',
                            bg='#e8e8e8',
                            fg='#666666')
        code_entry.grid(row=0, column=1, pady=(10, 5), ipady=5)
        
        # Profession Name field
        name_label = tk.Label(fields_frame,
                            text="Profession Name:",
                            font=('Arial', 12, 'bold'),
                            fg='#2c3e50',
                            bg='#f0f8ff')
        name_label.grid(row=1, column=0, sticky='w', pady=(5, 5), padx=(0, 15))
        
        name_entry = tk.Entry(fields_frame,
                            font=('Arial', 12),
                            width=30,
                            relief='solid',
                            borderwidth=1,
                            bg='white')
        name_entry.grid(row=1, column=1, pady=(5, 5), ipady=5)
        
        # Daily Salary field
        salary_label = tk.Label(fields_frame,
                            text="Daily Salary (Rs.):",
                            font=('Arial', 12, 'bold'),
                            fg='#2c3e50',
                            bg='#f0f8ff')
        salary_label.grid(row=2, column=0, sticky='w', pady=(5, 10), padx=(0, 15))
        
        salary_entry = tk.Entry(fields_frame,
                            font=('Arial', 12),
                            width=30,
                            relief='solid',
                            borderwidth=1,
                            bg='white')
        salary_entry.grid(row=2, column=1, pady=(5, 10), ipady=5)
        
        # Form buttons
        form_buttons_frame = tk.Frame(edit_frame, bg='#f0f8ff')
        form_buttons_frame.pack(pady=(0, 15))
        
        # Professions list section
        list_section = tk.Frame(scrollable_frame, bg='white')
        list_section.pack(fill='both', expand=True, padx=20)
        
        # List header
        list_header_frame = tk.Frame(list_section, bg='white')
        list_header_frame.pack(fill='x', pady=(0, 10))
        
        list_header = tk.Label(list_header_frame,
                            text="📋 Select Profession to Modify:",
                            font=('Arial', 14, 'bold'),
                            fg='#2c3e50',
                            bg='white')
        list_header.pack()
        
        # Create treeview for professions list
        columns = ('Code', 'Name', 'Daily Salary')
        tree_frame = tk.Frame(list_section, bg='white')
        tree_frame.pack(fill='both', expand=True)
        
        professions_tree = ttk.Treeview(tree_frame, columns=columns, show='headings', height=10)
        
        # Configure columns
        professions_tree.heading('Code', text='Profession Code')
        professions_tree.heading('Name', text='Profession Name')
        professions_tree.heading('Daily Salary', text='Daily Salary (Rs.)')
        
        professions_tree.column('Code', width=150, anchor='center')
        professions_tree.column('Name', width=300, anchor='w')
        professions_tree.column('Daily Salary', width=150, anchor='center')
        
        # Scrollbar for treeview
        tree_scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=professions_tree.yview)
        professions_tree.configure(yscrollcommand=tree_scrollbar.set)
        
        professions_tree.pack(side='left', fill='both', expand=True)
        tree_scrollbar.pack(side='right', fill='y')
        
        # Main buttons frame
        buttons_frame = tk.Frame(scrollable_frame, bg='white')
        buttons_frame.pack(pady=20)
        
        def load_professions():
            """Load professions from database into treeview"""
            # Clear existing items
            for item in professions_tree.get_children():
                professions_tree.delete(item)
            
            try:
                self.cursor.execute("SELECT profession_code, profession_name, daily_salary FROM profession ORDER BY profession_code")
                professions = self.cursor.fetchall()
                
                if not professions:
                    professions_tree.insert('', tk.END, values=('No professions found', '', ''))
                    return
                
                for profession in professions:
                    code, name, salary = profession
                    professions_tree.insert('', tk.END, values=(code, name, f"Rs. {float(salary):.2f}"))
                    
            except Exception as err:
                messagebox.showerror("Database Error", f"Error loading professions: {str(err)}")
                print(f"Debug - Error loading professions: {err}")
        
        def on_profession_select(event):
            """Handle profession selection from treeview"""
            selected_item = professions_tree.selection()
            
            if not selected_item:
                return
            
            # Get selected profession data
            profession_data = professions_tree.item(selected_item[0])['values']
            
            if not profession_data or profession_data[0] == 'No professions found':
                return
            
            # Show edit form at the top
            edit_frame.pack(fill='x', padx=20, pady=10)
            
            # Scroll to top to show the edit form
            canvas.yview_moveto(0)
            
            # Populate form fields
            code_entry.config(state='normal')
            code_entry.delete(0, tk.END)
            code_entry.insert(0, profession_data[0])
            code_entry.config(state='readonly')
            
            name_entry.delete(0, tk.END)
            name_entry.insert(0, profession_data[1])
            
            salary_entry.delete(0, tk.END)
            salary_str = str(profession_data[2]).replace('Rs. ', '').replace(',', '')
            salary_entry.insert(0, salary_str)
            
            name_entry.focus()
        
        def update_profession():
            """Update profession in database"""
            profession_code = code_entry.get().strip()
            profession_name = name_entry.get().strip()
            daily_salary = salary_entry.get().strip()
            
            # Validation
            if not profession_name:
                messagebox.showerror("Validation Error", "Profession Name is required!")
                name_entry.focus()
                return
            
            if not daily_salary:
                messagebox.showerror("Validation Error", "Daily Salary is required!")
                salary_entry.focus()
                return
            
            # Validate daily salary is a number
            try:
                daily_salary_float = float(daily_salary)
                if daily_salary_float < 0:
                    messagebox.showerror("Validation Error", "Daily Salary must be a positive number!")
                    salary_entry.focus()
                    return
            except ValueError:
                messagebox.showerror("Validation Error", "Daily Salary must be a valid number!")
                salary_entry.focus()
                return
            
            # Check if profession name already exists (excluding current profession)
            try:
                check_query = "SELECT profession_code FROM profession WHERE profession_name = %s AND profession_code != %s"
                self.cursor.execute(check_query, (profession_name, profession_code))
                existing = self.cursor.fetchone()
                
                if existing:
                    messagebox.showerror("Validation Error", f"Profession name '{profession_name}' already exists!")
                    name_entry.focus()
                    return
            except Exception as err:
                messagebox.showerror("Database Error", f"Error checking profession name: {str(err)}")
                return
            
            # Confirm update
            result = messagebox.askyesno("Confirm Update", 
                                    f"Are you sure you want to update profession '{profession_code}'?\n\n"
                                    f"New Name: {profession_name}\n"
                                    f"New Daily Salary: Rs. {daily_salary_float:.2f}")
            
            if result:
                try:
                    # Update profession in database
                    update_query = "UPDATE profession SET profession_name = %s, daily_salary = %s WHERE profession_code = %s"
                    self.cursor.execute(update_query, (profession_name, daily_salary_float, profession_code))
                    
                    if self.cursor.rowcount > 0:
                        self.connection.commit()
                        messagebox.showinfo("Success", f"Profession '{profession_code}' has been updated successfully!")
                        
                        # Refresh the professions list
                        load_professions()
                        
                        # Hide edit form
                        edit_frame.pack_forget()
                        
                        # Clear selection
                        professions_tree.selection_remove(professions_tree.selection())
                    else:
                        messagebox.showerror("Error", "Profession not found or could not be updated!")
                        
                except Exception as err:
                    messagebox.showerror("Database Error", f"Error updating profession: {str(err)}")
                    print(f"Debug - Update error: {err}")
                    try:
                        self.connection.rollback()
                    except:
                        pass
        
        def cancel_edit():
            """Cancel editing and hide form"""
            edit_frame.pack_forget()
            # Clear selection
            for item in professions_tree.selection():
                professions_tree.selection_remove(item)
            
            # Clear form fields
            code_entry.config(state='normal')
            code_entry.delete(0, tk.END)
            code_entry.config(state='readonly')
            name_entry.delete(0, tk.END)
            salary_entry.delete(0, tk.END)
        
        # Update Profession button
        update_btn = tk.Button(form_buttons_frame,
                            text="✅ UPDATE",
                            font=('Arial', 12, 'bold'),
                            bg='#27ae60',
                            fg='white',
                            width=18,
                            height=1,
                            relief='flat',
                            cursor='hand2',
                            command=update_profession)
        update_btn.pack(side='left', padx=(0, 15))
        
        # Cancel button
        cancel_btn = tk.Button(form_buttons_frame,
                            text="❌ CANCEL",
                            font=('Arial', 12, 'bold'),
                            bg='#e74c3c',
                            fg='white',
                            width=15,
                            height=1,
                            relief='flat',
                            cursor='hand2',
                            command=cancel_edit)
        cancel_btn.pack(side='left')
        
        # Refresh button
        refresh_btn = tk.Button(buttons_frame,
                            text="🔄 REFRESH LIST",
                            font=('Arial', 12, 'bold'),
                            bg='#3498db',
                            fg='white',
                            width=18,
                            height=2,
                            relief='flat',
                            cursor='hand2',
                            command=load_professions)
        refresh_btn.pack(side='left', padx=(0, 15))
        
        # Back button
        back_btn = tk.Button(buttons_frame,
                            text="⬅️ BACK",
                            font=('Arial', 12, 'bold'),
                            bg='#95a5a6',
                            fg='white',
                            width=15,
                            height=2,
                            relief='flat',
                            cursor='hand2',
                            command=self.show_app_manager)
        back_btn.pack(side='left')
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar_main.pack(side="right", fill="y")
        
        # Bind treeview selection event
        professions_tree.bind('<<TreeviewSelect>>', on_profession_select)
        
        # Bind mouse wheel to canvas
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Load professions initially
        load_professions()

    def delete_profession(self):
        """Delete profession interface"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Header
        header_frame = tk.Frame(self.content_frame, bg='white')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(header_frame,
                            text="🗂️ Delete Profession",
                            font=('Arial', 18, 'bold'),
                            fg='#2c3e50',
                            bg='white')
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(header_frame,
                                text="Remove an existing profession from the system",
                                font=('Arial', 12),
                                fg='#7f8c8d',
                                bg='white')
        subtitle_label.pack()
        
        # Warning message
        warning_frame = tk.Frame(self.content_frame, bg='#ffe6e6', relief='solid', bd=1)
        warning_frame.pack(fill='x', padx=50, pady=10)
        
        warning_label = tk.Label(warning_frame,
                                text="⚠️ WARNING: Deleting a profession cannot be undone!",
                                font=('Arial', 11, 'bold'),
                                fg='#e74c3c',
                                bg='#ffe6e6')
        warning_label.pack(pady=10)
        
        # Main content frame
        main_frame = tk.Frame(self.content_frame, bg='white')
        main_frame.pack(expand=True, fill='both', padx=50, pady=20)
        
        # Professions list frame
        list_frame = tk.Frame(main_frame, bg='white')
        list_frame.pack(fill='both', expand=True, pady=(0, 20))
        
        # List header
        list_header = tk.Label(list_frame,
                            text="Select Profession to Delete:",
                            font=('Arial', 14, 'bold'),
                            fg='#2c3e50',
                            bg='white')
        list_header.pack(pady=(0, 10))
        
        # Create treeview for professions list
        columns = ('Code', 'Name', 'Daily Salary')
        tree_frame = tk.Frame(list_frame, bg='white')
        tree_frame.pack(fill='both', expand=True)
        
        professions_tree = ttk.Treeview(tree_frame, columns=columns, show='headings', height=10)
        
        # Configure columns
        professions_tree.heading('Code', text='Code')
        professions_tree.heading('Name', text='Profession Name')
        professions_tree.heading('Daily Salary', text='Daily Salary')
        
        professions_tree.column('Code', width=100, anchor='center')
        professions_tree.column('Name', width=200, anchor='w')
        professions_tree.column('Daily Salary', width=150, anchor='center')
        
        # Scrollbar for treeview
        scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=professions_tree.yview)
        professions_tree.configure(yscrollcommand=scrollbar.set)
        
        professions_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        def load_professions():
            """Load professions from database"""
            # Clear existing items
            for item in professions_tree.get_children():
                professions_tree.delete(item)
            
            try:
                # Get all professions
                query = "SELECT profession_code, profession_name, daily_salary FROM profession ORDER BY profession_code"
                
                self.cursor.execute(query)
                professions = self.cursor.fetchall()
                
                print(f"Debug - Found {len(professions)} professions")  # Debug line
                
                if not professions:
                    professions_tree.insert('', tk.END, values=('No professions found', '', ''))
                    return
                
                for profession in professions:
                    code, name, salary = profession
                    print(f"Debug - Adding profession: {code}, {name}, {salary}")  # Debug line
                    professions_tree.insert('', tk.END, values=(
                        code, name, f"Rs. {float(salary):.2f}"
                    ))
                        
            except Exception as err:
                print(f"Debug - Database error: {err}")  # Debug line
                messagebox.showerror("Database Error", f"Error loading professions: {str(err)}")
        
        def delete_selected_profession():
            """Delete selected profession"""
            selected_item = professions_tree.selection()
            
            if not selected_item:
                messagebox.showwarning("No Selection", "Please select a profession to delete!")
                return
            
            # Get selected profession data
            profession_data = professions_tree.item(selected_item[0])['values']
            
            if not profession_data or profession_data[0] == 'No professions found':
                messagebox.showwarning("Invalid Selection", "Please select a valid profession!")
                return
            
            profession_code = profession_data[0]
            profession_name = profession_data[1]
            daily_salary = profession_data[2]
            
            # Confirmation dialog
            confirm_message = f"""Are you sure you want to delete the following profession?

    Profession Code: {profession_code}
    Profession Name: {profession_name}
    Daily Salary: {daily_salary}

    This action cannot be undone!"""
            
            result = messagebox.askyesno("Confirm Deletion", confirm_message, icon='warning')
            
            if result:
                try:
                    # Delete profession from database
                    delete_query = "DELETE FROM profession WHERE profession_code = %s"
                    self.cursor.execute(delete_query, (profession_code,))
                    
                    if self.cursor.rowcount > 0:
                        self.connection.commit()
                        messagebox.showinfo("Success", f"Profession '{profession_code} - {profession_name}' has been deleted successfully!")
                        
                        # Refresh the professions list
                        load_professions()
                    else:
                        messagebox.showerror("Error", "Profession not found or could not be deleted!")
                        
                except Exception as err:
                    try:
                        self.connection.rollback()
                    except:
                        pass
                    
                    # Check if it's an integrity constraint error
                    error_msg = str(err).lower()
                    if 'foreign key' in error_msg or 'constraint' in error_msg or 'referenced' in error_msg:
                        messagebox.showerror("Cannot Delete", 
                                        f"Cannot delete this profession because it is being used by other records in the system.\n\n"
                                        f"Please remove all references to this profession first.")
                    else:
                        messagebox.showerror("Database Error", f"Error deleting profession: {str(err)}")
                        
                    print(f"Debug - Delete error: {err}")
        
        def refresh_professions():
            """Refresh the professions list"""
            load_professions()
            messagebox.showinfo("Refreshed", "Professions list has been refreshed!")
        
        def handle_profession_selection(event):
            """Handle profession selection to enable delete button"""
            selected_item = professions_tree.selection()
            if selected_item:
                profession_data = professions_tree.item(selected_item[0])['values']
                if profession_data and profession_data[0] != 'No professions found':
                    # Enable delete button when a valid profession is selected
                    delete_btn.configure(bg='#e74c3c', state='normal')
                else:
                    delete_btn.configure(bg='#95a5a6', state='disabled')
            else:
                delete_btn.configure(bg='#95a5a6', state='disabled')
        
        # Bind selection event
        professions_tree.bind('<<TreeviewSelect>>', handle_profession_selection)
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg='white')
        buttons_frame.pack(pady=20)
        
        # Delete Profession button
        delete_btn = tk.Button(buttons_frame,
                            text="🗑️ DELETE",
                            font=('Arial', 12, 'bold'),
                            bg='#95a5a6',  # Start disabled
                            fg='white',
                            width=20,
                            height=2,
                            relief='flat',
                            cursor='hand2',
                            command=delete_selected_profession,
                            state='disabled')
        delete_btn.pack(side='left', padx=(0, 10))
        
        # Refresh button
        refresh_btn = tk.Button(buttons_frame,
                            text="🔄 REFRESH",
                            font=('Arial', 12, 'bold'),
                            bg='#3498db',
                            fg='white',
                            width=15,
                            height=2,
                            relief='flat',
                            cursor='hand2',
                            command=refresh_professions)
        refresh_btn.pack(side='left', padx=(0, 10))
        
        # Back button
        back_btn = tk.Button(buttons_frame,
                            text="⬅️ BACK",
                            font=('Arial', 12, 'bold'),
                            bg='#95a5a6',
                            fg='white',
                            width=15,
                            height=2,
                            relief='flat',
                            cursor='hand2',
                            command=self.show_app_manager)
        back_btn.pack(side='left')
        
        # Load professions initially
        load_professions() 

    def load_data_file(self):
            """Load employee data from file interface"""
            for widget in self.content_frame.winfo_children():
                widget.destroy()
            
            # Header
            header_frame = tk.Frame(self.content_frame, bg='white')
            header_frame.pack(fill='x', pady=(0, 20))
            
            title_label = tk.Label(header_frame,
                                text="📁 Load Data File",
                                font=('Arial', 18, 'bold'),
                                fg='#2c3e50',
                                bg='white')
            title_label.pack(pady=10)
            
            subtitle_label = tk.Label(header_frame,
                                    text="Import employee data from a formatted text file",
                                    font=('Arial', 12),
                                    fg='#7f8c8d',
                                    bg='white')
            subtitle_label.pack()
            
            # Instructions frame
            instructions_frame = tk.Frame(self.content_frame, bg='#e8f4fd', relief='solid', bd=1)
            instructions_frame.pack(fill='x', padx=50, pady=10)
            
            instructions_title = tk.Label(instructions_frame,
                                        text="📋 File Format Instructions:",
                                        font=('Arial', 12, 'bold'),
                                        fg='#2c3e50',
                                        bg='#e8f4fd')
            instructions_title.pack(pady=(10, 5))
            
            instructions_text = tk.Label(instructions_frame,
                                        text="• Each line should contain: employee_name   profession_code   12_work_days_values\n" +
                                            "• Separate values with 3 spaces (   )\n" +
                                            "• Work days should be 12 numeric values for each month\n" +
                                            "• Example: John_Smith   ENG001   22   20   24   21   23   22   20   25   21   22   20   23",
                                        font=('Arial', 10),
                                        fg='#34495e',
                                        bg='#e8f4fd',
                                        justify='left')
            instructions_text.pack(pady=(0, 10), padx=20)
            
            # Main content frame
            main_frame = tk.Frame(self.content_frame, bg='white')
            main_frame.pack(expand=True, fill='both', padx=50, pady=20)
            
            # File path frame
            file_frame = tk.Frame(main_frame, bg='white')
            file_frame.pack(fill='x', pady=(0, 20))
            
            file_label = tk.Label(file_frame,
                                text="File Path:",
                                font=('Arial', 12, 'bold'),
                                fg='#2c3e50',
                                bg='white')
            file_label.pack(anchor='w', pady=(0, 5))
            
            file_path_frame = tk.Frame(file_frame, bg='white')
            file_path_frame.pack(fill='x')
            
            file_path_entry = tk.Entry(file_path_frame,
                                    font=('Arial', 12),
                                    relief='solid',
                                    borderwidth=1)
            file_path_entry.pack(side='left', fill='x', expand=True, ipady=5)
            
            def browse_file():
                """Open file browser dialog"""
                from tkinter import filedialog
                file_path = filedialog.askopenfilename(
                    title="Select Data File",
                    filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
                )
                if file_path:
                    file_path_entry.delete(0, tk.END)
                    file_path_entry.insert(0, file_path)
            
            browse_btn = tk.Button(file_path_frame,
                                text="BROWSE",
                                font=('Arial', 10, 'bold'),
                                bg='#3498db',
                                fg='white',
                                relief='flat',
                                cursor='hand2',
                                command=browse_file)
            browse_btn.pack(side='right', padx=(10, 0), ipady=5, ipadx=10)
            
            # Status frame for showing progress
            status_frame = tk.Frame(main_frame, bg='white')
            status_frame.pack(fill='x', pady=10)
            
            status_label = tk.Label(status_frame,
                                text="Ready to load data...",
                                font=('Arial', 11),
                                fg='#7f8c8d',
                                bg='white')
            status_label.pack()
            
            def validate_and_load_data():
                """Validate file path and load data"""
                file_path = file_path_entry.get().strip()
                
                if not file_path:
                    messagebox.showerror("Error", "Please enter or browse for a file path!")
                    return
                
                if not os.path.exists(file_path):
                    messagebox.showerror("Error", f"File not found: {file_path}")
                    return
                
                # Confirm data loading
                result = messagebox.askyesno("Confirm Load", 
                                        f"Are you sure you want to load data from:\n{file_path}\n\n" +
                                        "This will add new employee records to the database.")
                
                if not result:
                    return
                
                try:
                    status_label.config(text="Reading file...", fg='#f39c12')
                    self.root.update()
                    
                    # Read and parse file
                    employer_details = {}
                    line_count = 0
                    
                    with open(file_path, 'r') as file:
                        for line in file.readlines():
                            line = line.strip()
                            if not line:  # Skip empty lines
                                continue
                            
                            line_count += 1
                            row = line.split("   ")  # Split by 3 spaces
                            
                            if len(row) < 14:  # employee_name + profession_code + 12 work_days
                                messagebox.showerror("Format Error", 
                                                f"Invalid format on line {line_count}!\n" +
                                                f"Expected: name   profession_code   12_work_days\n" +
                                                f"Found: {len(row)} parts")
                                return
                            
                            employee_name = row[0]
                            profession_code = row[1]
                            work_days = row[2:14]  # Take exactly 12 values
                            
                            # Validate work days are numeric
                            try:
                                work_days = [int(day) for day in work_days]
                            except ValueError:
                                messagebox.showerror("Data Error", 
                                                f"Non-numeric work days found on line {line_count}!\n" +
                                                f"Work days must be numbers.")
                                return
                            
                            employer_details[employee_name] = {
                                'profession_code': profession_code,
                                'work_days': work_days
                            }
                    
                    if not employer_details:
                        messagebox.showwarning("No Data", "No valid employee data found in the file!")
                        return
                    
                    status_label.config(text=f"Processing {len(employer_details)} employees...", fg='#f39c12')
                    self.root.update()
                    
                    # Month names for database
                    months = ['January', 'February', 'March', 'April', 'May', 'June',
                            'July', 'August', 'September', 'October', 'November', 'December']
                    
                    # Insert data into database
                    num = 0
                    successful_adds = 0
                    
                    for emp_name in employer_details:
                        try:
                            profession_code = employer_details[emp_name]['profession_code']
                            emp_code = f'synex{num}'
                            num += 1
                            
                            print(f"Processing employee: {emp_name} with code: {emp_code}")  # Debug print
                            
                            # Check if employee already exists
                            self.cursor.execute("SELECT Emp_code FROM Employee WHERE Emp_name = %s", (emp_name,))
                            existing = self.cursor.fetchone()
                            if existing:
                                print(f"Employee {emp_name} already exists, skipping...")  # Debug print
                                continue  # Skip if employee already exists
                            
                            # Insert employee with correct column names
                            add_employer_db = "INSERT INTO Employee (Emp_code, Emp_name, emp_professon_code) VALUES (%s, %s, %s)"
                            print(f"Executing: {add_employer_db} with values: {emp_code}, {emp_name}, {profession_code}")  # Debug print
                            self.cursor.execute(add_employer_db, (emp_code, emp_name, profession_code))
                            print(f"Employee {emp_name} inserted successfully")  # Debug print
                            
                            # Insert work data for each month - FIXED: Using 'days' instead of 'work_days'
                            work_days_data = employer_details[emp_name]['work_days']
                            for i, month in enumerate(months):
                                if i < len(work_days_data):
                                    add_work_data_db = "INSERT INTO work_data (emp_code, months, days) VALUES (%s, %s, %s)"
                                    print(f"Inserting work data: {emp_code}, {month}, {work_days_data[i]}")  # Debug print
                                    self.cursor.execute(add_work_data_db, (emp_code, month, work_days_data[i]))
                            
                            successful_adds += 1
                            self.connection.commit()  # Commit after each successful employee
                            print(f"Successfully processed employee {emp_name}")  # Debug print
                            
                        except mysql.connector.Error as err:
                            print(f"MySQL Error adding employee {emp_name}: {err}")
                            print(f"Error details: {err.errno}, {err.sqlstate}, {err.msg}")  # More detailed error info
                            self.connection.rollback()  # Rollback on error
                            continue
                        except Exception as e:
                            print(f"General error adding employee {emp_name}: {str(e)}")
                            continue
                    
                    # Commit all changes
                    self.connection.commit()
                    
                    status_label.config(text="Data loaded successfully!", fg='#27ae60')
                    
                    # Show success message
                    messagebox.showinfo("Success", 
                                    f"Data loading completed!\n\n" +
                                    f"• Total employees processed: {len(employer_details)}\n" +
                                    f"• Successfully added: {successful_adds}\n" +
                                    f"• Skipped (already exists): {len(employer_details) - successful_adds}")
                    
                    # Clear the file path
                    file_path_entry.delete(0, tk.END)
                    
                except FileNotFoundError:
                    messagebox.showerror("File Error", f"Could not find file: {file_path}")
                    status_label.config(text="File not found!", fg='#e74c3c')
                except PermissionError:
                    messagebox.showerror("Permission Error", f"Permission denied accessing file: {file_path}")
                    status_label.config(text="Permission denied!", fg='#e74c3c')
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred while loading data:\n{str(e)}")
                    status_label.config(text="Error occurred!", fg='#e74c3c')
                    self.connection.rollback()
            
            # Buttons frame
            buttons_frame = tk.Frame(main_frame, bg='white')
            buttons_frame.pack(pady=30)
            
            # Load Data button
            load_btn = tk.Button(buttons_frame,
                                text="LOAD DATA",
                                font=('Arial', 12, 'bold'),
                                bg='#27ae60',
                                fg='white',
                                width=15,
                                height=2,
                                relief='flat',
                                cursor='hand2',
                                command=validate_and_load_data)
            load_btn.pack(side='left', padx=(0, 10))
            
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
                                command=lambda: file_path_entry.delete(0, tk.END))
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

    def delete_employee_data(self):
        """Delete all employee data interface with improved layout and scrolling"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Create main scrollable frame
        canvas = tk.Canvas(self.content_frame, bg='white')
        scrollbar = tk.Scrollbar(self.content_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel to canvas
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Header
        header_frame = tk.Frame(scrollable_frame, bg='white')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(header_frame,
                            text="🗑️ Delete All Employee Data",
                            font=('Arial', 18, 'bold'),
                            fg='#2c3e50',
                            bg='white')
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(header_frame,
                                text="Remove all employee records and work data from the system",
                                font=('Arial', 12),
                                fg='#7f8c8d',
                                bg='white')
        subtitle_label.pack()
        
        # Danger warning frame
        warning_frame = tk.Frame(scrollable_frame, bg='#ffe6e6', relief='solid', bd=2)
        warning_frame.pack(fill='x', padx=50, pady=20)
        
        warning_title = tk.Label(warning_frame,
                                text="⚠️ DANGER ZONE ⚠️",
                                font=('Arial', 16, 'bold'),
                                fg='#e74c3c',
                                bg='#ffe6e6')
        warning_title.pack(pady=(15, 5))
        
        warning_text = tk.Label(warning_frame,
                            text="This action will permanently delete ALL employee data including:\n" +
                                    "• All employee records\n" +
                                    "• All work day data\n" +
                                    "• All salary information\n\n" +
                                    "THIS ACTION CANNOT BE UNDONE!",
                            font=('Arial', 12, 'bold'),
                            fg='#c0392b',
                            bg='#ffe6e6',
                            justify='center')
        warning_text.pack(pady=(0, 15))
        
        # Main content frame
        main_frame = tk.Frame(scrollable_frame, bg='white')
        main_frame.pack(fill='x', padx=50, pady=20)
        
        # Current data status frame
        status_frame = tk.Frame(main_frame, bg='#f8f9fa', relief='solid', bd=1)
        status_frame.pack(fill='x', pady=(0, 20))
        
        status_title = tk.Label(status_frame,
                            text="📊 Current Database Status:",
                            font=('Arial', 14, 'bold'),
                            fg='#2c3e50',
                            bg='#f8f9fa')
        status_title.pack(pady=(10, 5))
        
        # Labels for showing current counts
        emp_count_label = tk.Label(status_frame,
                                text="Loading...",
                                font=('Arial', 12),
                                fg='#34495e',
                                bg='#f8f9fa')
        emp_count_label.pack()
        
        work_count_label = tk.Label(status_frame,
                                text="Loading...",
                                font=('Arial', 12),
                                fg='#34495e',
                                bg='#f8f9fa')
        work_count_label.pack(pady=(0, 10))
        
        def load_current_status():
            """Load and display current database status"""
            try:
                # Get employee count
                self.cursor.execute("SELECT COUNT(*) FROM Employee")
                emp_count = self.cursor.fetchone()[0]
                
                # Get work data count
                self.cursor.execute("SELECT COUNT(*) FROM work_data")
                work_count = self.cursor.fetchone()[0]
                
                emp_count_label.config(text=f"👥 Total Employees: {emp_count}")
                work_count_label.config(text=f"📅 Total Work Records: {work_count}")
                
                return emp_count, work_count
                
            except mysql.connector.Error as err:
                emp_count_label.config(text="❌ Error loading employee count")
                work_count_label.config(text="❌ Error loading work data count")
                return 0, 0
        
        # Load initial status
        load_current_status()
        
        # Administrator password frame
        password_frame = tk.Frame(main_frame, bg='white')
        password_frame.pack(pady=20)
        
        password_label = tk.Label(password_frame,
                                text="🔐 Administrator Password:",
                                font=('Arial', 12, 'bold'),
                                fg='#2c3e50',
                                bg='white')
        password_label.pack(pady=(0, 5))
        
        password_entry = tk.Entry(password_frame,
                                font=('Arial', 12),
                                width=30,
                                show='*',
                                relief='solid',
                                borderwidth=1)
        password_entry.pack(ipady=5)
        
        password_hint = tk.Label(password_frame,
                                text="Enter your administrator password to confirm deletion",
                                font=('Arial', 10),
                                fg='#7f8c8d',
                                bg='white')
        password_hint.pack(pady=(5, 0))
        
        # Status label for operations
        operation_status = tk.Label(main_frame,
                                text="",
                                font=('Arial', 11, 'bold'),
                                bg='white')
        operation_status.pack(pady=10)
        
        def validate_and_delete_data():
            """Validate password and delete all employee data"""
            admin_password = password_entry.get().strip()
            
            if not admin_password:
                messagebox.showerror("Error", "Please enter the administrator password!")
                password_entry.focus()
                return
            
            # Verify administrator password
            try:
                # Get owner/admin passwords
                self.cursor.execute("SELECT Password FROM app_user WHERE user_type IN ('owner', 'admin')")
                valid_passwords = [row[0] for row in self.cursor.fetchall()]
                
                if admin_password not in valid_passwords:
                    messagebox.showerror("Access Denied", "Invalid administrator password!")
                    password_entry.delete(0, tk.END)
                    password_entry.focus()
                    return
                
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error verifying password: {err}")
                return
            
            # Get current counts for confirmation
            emp_count, work_count = load_current_status()
            
            if emp_count == 0 and work_count == 0:
                messagebox.showinfo("No Data", "There is no employee data to delete!")
                return
            
            # Final confirmation dialog
            confirm_message = f"""⚠️ FINAL CONFIRMATION ⚠️

    You are about to permanently delete:
    • {emp_count} employee records
    • {work_count} work data records

    This action CANNOT be undone!

    Are you absolutely sure you want to proceed?"""
            
            result = messagebox.askyesno("Final Confirmation", confirm_message, icon='warning')
            
            if not result:
                operation_status.config(text="Operation cancelled by user", fg='#f39c12')
                return
            
            try:
                operation_status.config(text="🗑️ Deleting work data...", fg='#e74c3c')
                self.root.update()
                
                # Delete work data first (foreign key constraint)
                self.cursor.execute("DELETE FROM work_data")
                deleted_work = self.cursor.rowcount
                
                operation_status.config(text="🗑️ Deleting employee records...", fg='#e74c3c')
                self.root.update()
                
                # Delete employee records
                self.cursor.execute("DELETE FROM Employee")
                deleted_emp = self.cursor.rowcount
                
                # Commit the changes
                self.connection.commit()
                
                operation_status.config(text="✅ All employee data deleted successfully!", fg='#27ae60')
                
                # Update status display
                load_current_status()
                
                # Clear password field
                password_entry.delete(0, tk.END)
                
                # Show success message with ASCII art
                success_message = f"""✅ DELETION COMPLETED SUCCESSFULLY! ✅

    Data Removed:
    • Employee Records: {deleted_emp}
    • Work Data Records: {deleted_work}

    ╔══════════════════════════════╗
    ║     ALL DATA CLEARED!        ║
    ║                              ║
    ║    Database is now empty     ║
    ║      and ready for new       ║
    ║         employee data        ║
    ╚══════════════════════════════╝

    The system has been reset successfully."""
                
                messagebox.showinfo("Success", success_message)
                
            except mysql.connector.Error as err:
                operation_status.config(text="❌ Error occurred during deletion!", fg='#e74c3c')
                messagebox.showerror("Database Error", f"Error deleting data: {err}")
                self.connection.rollback()
        
        def refresh_status():
            """Refresh the current status display"""
            load_current_status()
            operation_status.config(text="Status refreshed", fg='#3498db')
        
        # Action buttons frame (organized in rows for better layout)
        buttons_container = tk.Frame(main_frame, bg='white')
        buttons_container.pack(pady=30)
        
        # First row of buttons - Main actions
        main_buttons_frame = tk.Frame(buttons_container, bg='white')
        main_buttons_frame.pack(pady=(0, 15))
        
        # Delete All Data button
        delete_btn = tk.Button(main_buttons_frame,
                            text="🗑️ DELETE ALL DATA",
                            font=('Arial', 12, 'bold'),
                            bg='#e74c3c',
                            fg='white',
                            width=20,
                            height=2,
                            relief='flat',
                            cursor='hand2',
                            command=validate_and_delete_data)
        delete_btn.pack(side='left', padx=(0, 15))
        
        # Refresh Status button
        refresh_btn = tk.Button(main_buttons_frame,
                            text="🔄 REFRESH STATUS",
                            font=('Arial', 12, 'bold'),
                            bg='#3498db',
                            fg='white',
                            width=20,
                            height=2,
                            relief='flat',
                            cursor='hand2',
                            command=refresh_status)
        refresh_btn.pack(side='left')
        
        # Second row - Navigation button
        nav_buttons_frame = tk.Frame(buttons_container, bg='white')
        nav_buttons_frame.pack()
        
        # Back button (centered in second row)
        back_btn = tk.Button(nav_buttons_frame,
                            text="⬅️ BACK TO APP MANAGER",
                            font=('Arial', 12, 'bold'),
                            bg='#95a5a6',
                            fg='white',
                            width=25,
                            height=2,
                            relief='flat',
                            cursor='hand2',
                            command=self.show_app_manager)
        back_btn.pack()
        
        # Add some extra space at the bottom for better scrolling
        bottom_spacer = tk.Frame(scrollable_frame, bg='white', height=50)
        bottom_spacer.pack(fill='x')
        
        # Focus on password field
        password_entry.focus()
        
        # Ensure canvas updates its scroll region
        scrollable_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

    #nowwww
    # Placeholder methods for Employee Manager functions


    import datetime  # Add this import at the top of your file

    def create_salary_sheet(self):
        """Create employee salary sheet interface"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Header
        header_frame = tk.Frame(self.content_frame, bg='white')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(header_frame,
                            text="📊 Create Employee Salary Sheet",
                            font=('Arial', 18, 'bold'),
                            fg='#2c3e50',
                            bg='white')
        title_label.pack(pady=10)

        
        # Main form frame
        form_frame = tk.Frame(self.content_frame, bg='white')
        form_frame.pack(expand=True, fill='both', padx=50, pady=20)
        
        # File location input
        file_frame = tk.Frame(form_frame, bg='white')
        file_frame.pack(fill='x', pady=(0, 20))
        
        file_label = tk.Label(file_frame,
                            text="Output File Location:",
                            font=('Arial', 12, 'bold'),
                            fg='#2c3e50',
                            bg='white')
        file_label.pack(anchor='w', pady=(0, 5))
        
        file_entry_frame = tk.Frame(file_frame, bg='white')
        file_entry_frame.pack(fill='x')
        
        file_entry = tk.Entry(file_entry_frame,
                            font=('Arial', 12),
                            relief='solid',
                            borderwidth=1)
        file_entry.pack(side='left', fill='x', expand=True, ipady=8)
        file_entry.insert(0, "salary_sheet.txt")  # Default filename
        
        def browse_file():
            """Browse for file location"""
            from tkinter import filedialog
            filename = filedialog.asksaveasfilename(
                title="Save Salary Sheet As",
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            if filename:
                file_entry.delete(0, tk.END)
                file_entry.insert(0, filename)
        
        browse_btn = tk.Button(file_entry_frame,
                            text="BROWSE",
                            font=('Arial', 10, 'bold'),
                            bg='#3498db',
                            fg='white',
                            relief='flat',
                            cursor='hand2',
                            command=browse_file)
        browse_btn.pack(side='right', padx=(10, 0), ipady=8, ipadx=10)
        
        # Preview frame
        preview_frame = tk.Frame(form_frame, bg='white', relief='solid', bd=1)
        preview_frame.pack(fill='both', expand=True, pady=(0, 20))
        
        preview_label = tk.Label(preview_frame,
                                text="Employee Data Preview:",
                                font=('Arial', 12, 'bold'),
                                fg='#2c3e50',
                                bg='white')
        preview_label.pack(anchor='w', padx=10, pady=(10, 5))
        
        # Text widget for preview
        preview_text = tk.Text(preview_frame,
                            font=('Courier', 9),
                            bg='#f8f9fa',
                            fg='#2c3e50',
                            height=15,
                            wrap='none')
        
        # Scrollbars for preview
        v_scrollbar = tk.Scrollbar(preview_frame, orient='vertical', command=preview_text.yview)
        h_scrollbar = tk.Scrollbar(preview_frame, orient='horizontal', command=preview_text.xview)
        preview_text.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        preview_text.pack(side='left', fill='both', expand=True, padx=(10, 0), pady=(0, 10))
        v_scrollbar.pack(side='right', fill='y', pady=(0, 10))
        h_scrollbar.pack(side='bottom', fill='x', padx=(10, 0), pady=(0, 10))
        
        def load_preview():
            """Load and display employee data preview"""
            preview_text.delete(1.0, tk.END)
            
            try:
                # Get employee data
                get_employee_data = 'SELECT * FROM employee'
                self.cursor.execute(get_employee_data)
                employees = self.cursor.fetchall()
                
                if not employees:
                    preview_text.insert(tk.END, "No employee data found in the database.\n")
                    return
                
                preview_text.insert(tk.END, "Employee Data Preview:\n")
                preview_text.insert(tk.END, "=" * 80 + "\n\n")
                
                employee_count = 0
                for emp_data in employees:
                    employee_count += 1
                    emp_code = emp_data[0]
                    emp_name = emp_data[1]
                    profession_code = emp_data[2]
                    
                    # Get profession details
                    get_profession = f"SELECT daily_salary, profession_name FROM profession WHERE profession_code = '{profession_code}'"
                    self.cursor.execute(get_profession)
                    profession_data = self.cursor.fetchone()
                    
                    if profession_data:
                        # FIX: Convert to float first, then to int to handle decimal values
                        daily_rate = int(float(profession_data[0]))
                        profession_name = profession_data[1]
                        
                        preview_text.insert(tk.END, f"Employee #{employee_count}\n")
                        preview_text.insert(tk.END, f"Name: {emp_name}\n")
                        preview_text.insert(tk.END, f"Profession: {profession_name}\n")
                        preview_text.insert(tk.END, f"Daily Rate: ${daily_rate}\n")
                        
                        # Get work data
                        work_query = f"SELECT * FROM work_data WHERE emp_code = '{emp_code}'"
                        self.cursor.execute(work_query)
                        work_data = self.cursor.fetchall()
                        
                        if work_data:
                            preview_text.insert(tk.END, "Work Record:\n")
                            total_salary = 0
                            for work_record in work_data:
                                month = work_record[1]
                                days = int(work_record[2])
                                
                                # Calculate salary
                                gross_salary = daily_rate * days
                                epf = gross_salary * 0.08  # 8% EPF
                                tax = gross_salary * 0.10  # 10% Tax
                                safety_items = 500
                                
                                net_salary = gross_salary - epf - tax - safety_items
                                net_salary = round(net_salary, 2)
                                total_salary += net_salary
                                
                                preview_text.insert(tk.END, f"  {month}: {days} days worked → Net Salary: ${net_salary}\n")
                            
                            preview_text.insert(tk.END, f"Total Earnings: ${round(total_salary, 2)}\n")
                        else:
                            preview_text.insert(tk.END, "No work data found for this employee.\n")
                    else:
                        preview_text.insert(tk.END, f"Employee: {emp_name} (Profession data not found)\n")
                    
                    preview_text.insert(tk.END, "-" * 80 + "\n\n")
                
                preview_text.insert(tk.END, f"Total Employees: {employee_count}\n")
                
            except Exception as e:
                preview_text.insert(tk.END, f"Error loading preview: {str(e)}\n")
        
        def generate_salary_sheet():
            """Generate the complete salary sheet"""
            file_path = file_entry.get().strip()
            
            if not file_path:
                messagebox.showerror("Error", "Please specify an output file location!")
                return
            
            try:
                # Get employee data
                get_employee_data = 'SELECT * FROM employee'
                self.cursor.execute(get_employee_data)
                employees = self.cursor.fetchall()
                
                if not employees:
                    messagebox.showwarning("No Data", "No employee data found in the database!")
                    return
                
                emp_data = {}
                for data in employees:
                    emp_data[data[0]] = {
                        'emp_name': data[1],
                        'profession_code': data[2]
                    }
                
                # Generate salary sheet file
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write("SYNEX INDUSTRIES - EMPLOYEE SALARY SHEET\n")
                    file.write("=" * 80 + "\n")
                    # Fixed line - use datetime.datetime instead of tk.datetime.datetime
                    file.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    file.write("=" * 80 + "\n\n")
                    
                    employee_count = 0
                    total_company_payout = 0
                    
                    for emp_code in emp_data:
                        employee_count += 1
                        emp_name = emp_data[emp_code]['emp_name']
                        profession_code = emp_data[emp_code]['profession_code']
                        
                        # Get profession details
                        get_daily_rate = f"SELECT daily_salary, profession_name FROM profession WHERE profession_code = '{profession_code}'"
                        self.cursor.execute(get_daily_rate)
                        profession_data = self.cursor.fetchone()
                        
                        if profession_data:
                            # FIX: Convert to float first, then to int to handle decimal values
                            emp_rate = int(float(profession_data[0]))
                            profession_name = profession_data[1]
                            
                            file.write('_' * 80 + "\n")
                            file.write(f"EMPLOYEE #{employee_count}\n")
                            file.write(f"Name: {emp_name}\n")
                            file.write(f"Profession: {profession_name}\n")
                            file.write(f"Daily Rate: ${emp_rate}\n")
                            file.write('-' * 80 + "\n")
                            
                            # Get work data
                            work_data_query = f"SELECT * FROM work_data WHERE emp_code = '{emp_code}'"
                            self.cursor.execute(work_data_query)
                            work_records = self.cursor.fetchall()
                            
                            employee_total = 0
                            if work_records:
                                file.write("MONTHLY SALARY BREAKDOWN:\n")
                                file.write("Month".ljust(15) + "Days".ljust(10) + "Gross".ljust(12) + "EPF".ljust(10) + "Tax".ljust(10) + "Safety".ljust(10) + "Net Salary\n")
                                file.write("-" * 80 + "\n")
                                
                                for work_record in work_records:
                                    month = work_record[1]
                                    days = int(work_record[2])
                                    
                                    # Calculate salary components
                                    gross_salary = emp_rate * days
                                    epf = gross_salary * 0.08  # 8% EPF
                                    tax = gross_salary * 0.10  # 10% Tax
                                    safety_items = 500
                                    
                                    net_salary = gross_salary - epf - tax - safety_items
                                    net_salary = round(net_salary, 2)
                                    employee_total += net_salary
                                    
                                    file.write(f"{month[:14].ljust(15)}{str(days).ljust(10)}${str(gross_salary).ljust(11)}${str(round(epf, 2)).ljust(9)}${str(round(tax, 2)).ljust(9)}${str(safety_items).ljust(9)}${net_salary}\n")
                                
                                file.write("-" * 80 + "\n")
                                file.write(f"TOTAL EMPLOYEE EARNINGS: ${round(employee_total, 2)}\n")
                                total_company_payout += employee_total
                            else:
                                file.write("No work data found for this employee.\n")
                            
                            file.write("\n")
                    
                    # Summary
                    file.write("=" * 80 + "\n")
                    file.write("COMPANY SUMMARY\n")
                    file.write("=" * 80 + "\n")
                    file.write(f"Total Employees: {employee_count}\n")
                    file.write(f"Total Company Salary Payout: ${round(total_company_payout, 2)}\n")
                    file.write("=" * 80 + "\n")
                
                # Success message
                success_message = f"""
    Salary sheet generated successfully!

    File Location: {file_path}
    Total Employees: {employee_count}
    Total Payout: ${round(total_company_payout, 2)}

    The salary sheet has been saved and is ready for review.
                """
                
                messagebox.showinfo("Success", success_message)
                
                # Ask if user wants to open the file
                if messagebox.askyesno("Open File", "Would you like to open the generated salary sheet?"):
                    try:
                        import subprocess
                        import sys
                        if sys.platform.startswith('win'):
                            os.startfile(file_path)
                        elif sys.platform.startswith('darwin'):
                            subprocess.call(['open', file_path])
                        else:
                            subprocess.call(['xdg-open', file_path])
                    except Exception as e:
                        messagebox.showwarning("Open File", f"Could not open file automatically: {str(e)}")
                
                # Refresh preview
                load_preview()
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to generate salary sheet: {str(e)}")
        
        # Buttons frame
        buttons_frame = tk.Frame(form_frame, bg='white')
        buttons_frame.pack(pady=20)
        
        # Generate button
        generate_btn = tk.Button(buttons_frame,
                                text="GENERATE SALARY SHEET",
                                font=('Arial', 12, 'bold'),
                                bg='#27ae60',
                                fg='white',
                                width=20,
                                height=2,
                                relief='flat',
                                cursor='hand2',
                                command=generate_salary_sheet)
        generate_btn.pack(side='left', padx=(0, 10))
        
        # Preview button
        preview_btn = tk.Button(buttons_frame,
                            text="LOAD PREVIEW",
                            font=('Arial', 12, 'bold'),
                            bg='#3498db',
                            fg='white',
                            width=15,
                            height=2,
                            relief='flat',
                            cursor='hand2',
                            command=load_preview)
        preview_btn.pack(side='left', padx=(0, 10))
        
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
                            command=self.show_emp_manager)
        back_btn.pack(side='left')
        
        # Load initial preview
        load_preview()
    
    # Focus on file entry
        file_entry.focus()

    def calculate_taxes(self):
        """Calculate monthly taxes from all employees"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Header
        header_frame = tk.Frame(self.content_frame, bg='white')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(header_frame,
                            text="💰 Monthly Tax Calculator",
                            font=('Arial', 18, 'bold'),
                            fg='#2c3e50',
                            bg='white')
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(header_frame,
                                text="Calculate total taxes from all employees for each month",
                                font=('Arial', 12),
                                fg='#7f8c8d',
                                bg='white')
        subtitle_label.pack()
        
        # Main content frame
        main_frame = tk.Frame(self.content_frame, bg='white')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Calculate button frame
        calc_frame = tk.Frame(main_frame, bg='white')
        calc_frame.pack(pady=20)
        
        calc_btn = tk.Button(calc_frame,
                            text="CALCULATE TAXES",
                            font=('Arial', 14, 'bold'),
                            bg='#e74c3c',
                            fg='white',
                            width=20,
                            height=2,
                            relief='flat',
                            cursor='hand2',
                            command=self.perform_tax_calculation)
        calc_btn.pack()
        
        # Results frame
        self.tax_results_frame = tk.Frame(main_frame, bg='white')
        self.tax_results_frame.pack(fill='both', expand=True, pady=20)
        
        # Back button
        back_btn = tk.Button(main_frame,
                            text="BACK TO EMPLOYEE MANAGER",
                            font=('Arial', 12, 'bold'),
                            bg='#95a5a6',
                            fg='white',
                            width=25,
                            height=2,
                            relief='flat',
                            cursor='hand2',
                            command=self.show_emp_manager)
        back_btn.pack(side='bottom', pady=20)

    def perform_tax_calculation(self):
        """Perform the actual tax calculation using the provided logic"""
        try:
            # Clear previous results
            for widget in self.tax_results_frame.winfo_children():
                widget.destroy()
            
            # Show loading message
            loading_label = tk.Label(self.tax_results_frame,
                                text="Calculating taxes... Please wait...",
                                font=('Arial', 12),
                                fg='#3498db',
                                bg='white')
            loading_label.pack(pady=20)
            
            # Update GUI
            self.root.update()
            
            # Define months
            months = ['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']
            
            # Get employee data
            get_employee_data = 'SELECT * FROM employee'
            self.cursor.execute(get_employee_data)
            fetch = self.cursor.fetchall()
            
            if not fetch:
                loading_label.destroy()
                no_data_label = tk.Label(self.tax_results_frame,
                                    text="No employee data found!",
                                    font=('Arial', 14, 'bold'),
                                    fg='#e74c3c',
                                    bg='white')
                no_data_label.pack(pady=20)
                return
            
            emp_data = {}
            for data in fetch:
                emp_data[data[0]] = {'emp_name': data[1], 'profession_code': data[2]}
            
            # Initialize month dictionary
            month_dic = {month: 0 for month in months}
            
            # Calculate taxes for each employee and month
            for emp_code in emp_data:
                for month in months:
                    try:
                        # Get work days for employee in specific month
                        work_days_query = f"SELECT days FROM work_data WHERE emp_code = '{emp_code}' AND months = '{month}'"
                        self.cursor.execute(work_days_query)
                        work_days_result = self.cursor.fetchone()
                        
                        if work_days_result:
                            work_days = work_days_result[0]
                            
                            # Get profession code for employee
                            profession_code = emp_data[emp_code]['profession_code']
                            
                            # Get daily salary for profession
                            daily_salary_query = f"SELECT daily_salary FROM profession WHERE profession_code = '{profession_code}'"
                            self.cursor.execute(daily_salary_query)
                            daily_salary_result = self.cursor.fetchone()
                            
                            if daily_salary_result:
                                daily_salary = daily_salary_result[0]
                                
                                # Calculate gross salary
                                gross_salary = int(work_days) * int(daily_salary)
                                
                                # Calculate tax (10% of gross salary)
                                tax = gross_salary / 100 * 10
                                
                                # Add to month total
                                month_dic[month] += tax
                    
                    except Exception as e:
                        continue  # Skip if any error occurs for this employee/month
            
            # Clear loading message
            loading_label.destroy()
            
            # Display results
            self.display_tax_results(month_dic)
            
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error calculating taxes: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def display_tax_results(self, month_dic):
        """Display the tax calculation results"""
        # Create scrollable canvas for the entire results section
        canvas = tk.Canvas(self.tax_results_frame, bg='white')
        scrollbar = ttk.Scrollbar(self.tax_results_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Results title
        results_title = tk.Label(scrollable_frame,
                            text="Total Tax All Employees Each Month",
                            font=('Arial', 16, 'bold'),
                            fg='#2c3e50',
                            bg='white')
        results_title.pack(pady=(0, 20))
        
        # Results table
        table_frame = tk.Frame(scrollable_frame, bg='white', relief='raised', bd=1)
        table_frame.pack(fill='x', padx=20, pady=10)
        
        # Table headers
        header_frame = tk.Frame(table_frame, bg='#34495e')
        header_frame.pack(fill='x')
        
        month_header = tk.Label(header_frame,
                            text="Month",
                            font=('Arial', 12, 'bold'),
                            fg='white',
                            bg='#34495e',
                            width=15,
                            pady=10)
        month_header.pack(side='left')
        
        tax_header = tk.Label(header_frame,
                            text="Total Tax Amount",
                            font=('Arial', 12, 'bold'),
                            fg='white',
                            bg='#34495e',
                            width=20,
                            pady=10)
        tax_header.pack(side='left')
        
        # Table rows
        total_tax = 0
        for i, (month, tax_amount) in enumerate(month_dic.items()):
            row_color = '#ecf0f1' if i % 2 == 0 else 'white'
            
            row_frame = tk.Frame(table_frame, bg=row_color)
            row_frame.pack(fill='x')
            
            month_label = tk.Label(row_frame,
                                text=month,
                                font=('Arial', 11),
                                fg='#2c3e50',
                                bg=row_color,
                                width=15,
                                pady=8)
            month_label.pack(side='left')
            
            tax_label = tk.Label(row_frame,
                            text=f"Rs. {tax_amount:.2f}",
                            font=('Arial', 11, 'bold'),
                            fg='#e74c3c',
                            bg=row_color,
                            width=20,
                            pady=8)
            tax_label.pack(side='left')
            
            total_tax += tax_amount
        
        # Total row
        total_frame = tk.Frame(table_frame, bg='#2c3e50')
        total_frame.pack(fill='x')
        
        total_month_label = tk.Label(total_frame,
                                text="TOTAL ANNUAL TAX",
                                font=('Arial', 12, 'bold'),
                                fg='white',
                                bg='#2c3e50',
                                width=15,
                                pady=10)
        total_month_label.pack(side='left')
        
        total_tax_label = tk.Label(total_frame,
                                text=f"Rs. {total_tax:.2f}",
                                font=('Arial', 12, 'bold'),
                                fg='#f1c40f',
                                bg='#2c3e50',
                                width=20,
                                pady=10)
        total_tax_label.pack(side='left')
        
        # Export button frame
        export_frame = tk.Frame(scrollable_frame, bg='white')
        export_frame.pack(pady=20)
        
        # Export button
        export_btn = tk.Button(export_frame,
                            text="EXPORT TO FILE",
                            font=('Arial', 12, 'bold'),
                            bg='#27ae60',
                            fg='white',
                            width=20,
                            height=2,
                            relief='flat',
                            cursor='hand2',
                            command=lambda: self.export_tax_data(month_dic, total_tax))
        export_btn.pack()
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Enable mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        def _bind_mousewheel(event):
            canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        def _unbind_mousewheel(event):
            canvas.unbind_all("<MouseWheel>")
        
        canvas.bind('<Enter>', _bind_mousewheel)
        canvas.bind('<Leave>', _unbind_mousewheel)

    def export_tax_data(self, month_dic, total_tax):
        """Export tax calculation data to a file"""
        try:
            from tkinter import filedialog
            import datetime
            
            # Ask user for file location
            file_path = filedialog.asksaveasfilename(
                title="Save Tax Report As",
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv"), ("All files", "*.*")]
            )
            
            if not file_path:
                return  # User cancelled
            
            # Generate report content
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write("SYNEX INDUSTRIES - MONTHLY TAX REPORT\n")
                file.write("=" * 60 + "\n")
                file.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write("=" * 60 + "\n\n")
                
                file.write("MONTHLY TAX BREAKDOWN:\n")
                file.write("-" * 60 + "\n")
                file.write(f"{'Month':<15} {'Tax Amount':<20}\n")
                file.write("-" * 60 + "\n")
                
                for month, tax_amount in month_dic.items():
                    file.write(f"{month:<15} Rs. {tax_amount:<18.2f}\n")
                
                file.write("-" * 60 + "\n")
                file.write(f"{'TOTAL ANNUAL TAX':<15} Rs. {total_tax:<18.2f}\n")
                file.write("=" * 60 + "\n")
                
                # Additional statistics
                file.write("\nSTATISTICS:\n")
                file.write("-" * 60 + "\n")
                months_with_tax = sum(1 for tax in month_dic.values() if tax > 0)
                avg_monthly_tax = total_tax / 12 if total_tax > 0 else 0
                
                file.write(f"Months with tax collection: {months_with_tax}\n")
                file.write(f"Average monthly tax: Rs. {avg_monthly_tax:.2f}\n")
                file.write(f"Highest month tax: Rs. {max(month_dic.values()):.2f}\n")
                file.write(f"Lowest month tax: Rs. {min(month_dic.values()):.2f}\n")
            
            # Success message
            messagebox.showinfo("Export Successful", 
                            f"Tax report has been successfully exported to:\n{file_path}")
            
            # Ask if user wants to open the file
            if messagebox.askyesno("Open File", "Would you like to open the exported file?"):
                try:
                    import subprocess
                    import sys
                    if sys.platform.startswith('win'):
                        os.startfile(file_path)
                    elif sys.platform.startswith('darwin'):
                        subprocess.call(['open', file_path])
                    else:
                        subprocess.call(['xdg-open', file_path])
                except Exception as e:
                    messagebox.showwarning("Open File", f"Could not open file automatically: {str(e)}")
                    
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export tax data: {str(e)}")  


    def calculate_profit(self):
        """Calculate company profit interface"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Header
        header_frame = tk.Frame(self.content_frame, bg='white')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(header_frame,
                            text="💰 Company Profit Calculator",
                            font=('Arial', 18, 'bold'),
                            fg='#2c3e50',
                            bg='white')
        title_label.pack(pady=10)
        
        # Create scrollable frame for results
        canvas_frame = tk.Frame(self.content_frame, bg='white')
        canvas_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        canvas = tk.Canvas(canvas_frame, bg='white')
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Variables to store data for export
        profit_data = {}
        
        # Calculate button
        def calculate_company_profit():
            """Calculate and display company profit"""
            nonlocal profit_data
            try:
                # Clear previous results
                for widget in scrollable_frame.winfo_children():
                    widget.destroy()
                
                # Get employee data
                get_employee_data = 'SELECT * FROM employee'
                self.cursor.execute(get_employee_data)
                employee_fetch = self.cursor.fetchall()
                
                if not employee_fetch:
                    no_data_label = tk.Label(scrollable_frame,
                                        text="❌ No employee data found!",
                                        font=('Arial', 14, 'bold'),
                                        fg='#e74c3c',
                                        bg='white')
                    no_data_label.pack(pady=20)
                    return
                
                emp_data = {}
                for data in employee_fetch:
                    emp_data[data[0]] = {'emp_name': data[1], 'profession_code': data[2]}
                
                # Initialize monthly net costs
                employers_netcost = {
                    'January': 0, 'February': 0, 'March': 0, 'April': 0,
                    'May': 0, 'June': 0, 'July': 0, 'August': 0,
                    'September': 0, 'October': 0, 'November': 0, 'December': 0
                }
                
                # Calculate net costs for each employee
                for emp_code in emp_data:
                    emp_name = emp_data[emp_code]['emp_name']
                    profession_code = emp_data[emp_code]['profession_code']
                    
                    # Get daily rate - FIXED to handle decimal values
                    get_daily_rate = f"SELECT daily_salary FROM profession WHERE profession_code = '{profession_code}'"
                    self.cursor.execute(get_daily_rate)
                    rate_fetch = self.cursor.fetchall()
                    
                    if not rate_fetch:
                        continue
                    
                    emp_rate = float(rate_fetch[0][0])  # FIXED: Changed from int() to float()
                    
                    # Get work data
                    work_data = f"SELECT * FROM work_data WHERE emp_code = '{emp_code}'"
                    self.cursor.execute(work_data)
                    work_fetch = self.cursor.fetchall()
                    
                    for work_record in work_fetch:
                        month = work_record[1]
                        days = int(float(work_record[2]))  # FIXED: Handle decimal strings
                        
                        # Calculate salary components
                        gross_salary = emp_rate * days
                        epf = gross_salary / 100 * 8
                        tax = gross_salary / 100 * 10
                        safety_item = 500
                        
                        net_cost = gross_salary - epf - tax - safety_item
                        
                        if month in employers_netcost:
                            employers_netcost[month] += net_cost
                
                # Company profit calculation (8000000 * 200)
                company_revenue = 8000000 * 200
                
                # Display results header
                results_header = tk.Label(scrollable_frame,
                                        text="🏢 Company Profit Analysis - Monthly Report",
                                        font=('Arial', 16, 'bold'),
                                        fg='#2c3e50',
                                        bg='white')
                results_header.pack(pady=(20, 10))
                
                revenue_label = tk.Label(scrollable_frame,
                                    text=f"📊 Total Company Revenue: Rs. {company_revenue:,}",
                                    font=('Arial', 12, 'bold'),
                                    fg='#27ae60',
                                    bg='white')
                revenue_label.pack(pady=5)
                
                separator = tk.Label(scrollable_frame,
                                text="═" * 80 + " Monthly Profit Breakdown " + "═" * 80,
                                font=('Courier', 10),
                                fg='#3498db',
                                bg='white')
                separator.pack(pady=10)
                
                # Create table-like display for each month
                total_annual_cost = 0
                total_annual_profit = 0
                
                # Store data for export
                profit_data = {
                    'monthly_costs': employers_netcost.copy(),
                    'monthly_profits': {},
                    'company_revenue': company_revenue,
                    'total_annual_cost': 0,
                    'total_annual_profit': 0
                }
                
                for month in employers_netcost:
                    monthly_cost = employers_netcost[month]
                    monthly_profit = company_revenue - monthly_cost
                    
                    total_annual_cost += monthly_cost
                    total_annual_profit += monthly_profit
                    
                    # Store for export
                    profit_data['monthly_profits'][month] = monthly_profit
                    
                    # Month frame
                    month_frame = tk.Frame(scrollable_frame, bg='#f8f9fa', relief='solid', bd=1)
                    month_frame.pack(fill='x', padx=20, pady=2)
                    
                    # Month info
                    month_info = tk.Label(month_frame,
                                        text=f"📅 {month:12s}",
                                        font=('Arial', 11, 'bold'),
                                        fg='#2c3e50',
                                        bg='#f8f9fa',
                                        width=15,
                                        anchor='w')
                    month_info.pack(side='left', padx=10, pady=5)
                    
                    cost_info = tk.Label(month_frame,
                                    text=f"💸 Cost: Rs. {monthly_cost:,}",
                                    font=('Arial', 10),
                                    fg='#e74c3c',
                                    bg='#f8f9fa',
                                    width=25,
                                    anchor='w')
                    cost_info.pack(side='left', padx=10, pady=5)
                    
                    profit_info = tk.Label(month_frame,
                                        text=f"💰 Profit: Rs. {monthly_profit:,}",
                                        font=('Arial', 10, 'bold'),
                                        fg='#27ae60',
                                        bg='#f8f9fa',
                                        anchor='w')
                    profit_info.pack(side='left', padx=10, pady=5)
                
                # Store totals for export
                profit_data['total_annual_cost'] = total_annual_cost
                profit_data['total_annual_profit'] = total_annual_profit
                
                # Annual summary
                summary_frame = tk.Frame(scrollable_frame, bg='#e8f5e8', relief='solid', bd=2)
                summary_frame.pack(fill='x', padx=20, pady=20)
                
                summary_title = tk.Label(summary_frame,
                                    text="📈 ANNUAL SUMMARY",
                                    font=('Arial', 14, 'bold'),
                                    fg='#2c3e50',
                                    bg='#e8f5e8')
                summary_title.pack(pady=10)
                
                annual_revenue = tk.Label(summary_frame,
                                        text=f"Total Annual Revenue: Rs. {company_revenue * 12:,}",
                                        font=('Arial', 12, 'bold'),
                                        fg='#27ae60',
                                        bg='#e8f5e8')
                annual_revenue.pack(pady=2)
                
                annual_cost = tk.Label(summary_frame,
                                    text=f"Total Annual Cost: Rs. {total_annual_cost:,}",
                                    font=('Arial', 12, 'bold'),
                                    fg='#e74c3c',
                                    bg='#e8f5e8')
                annual_cost.pack(pady=2)
                
                annual_profit = tk.Label(summary_frame,
                                    text=f"Total Annual Profit: Rs. {total_annual_profit:,}",
                                    font=('Arial', 12, 'bold'),
                                    fg='#27ae60',
                                    bg='#e8f5e8')
                annual_profit.pack(pady=2)
                
                # Profit margin
                profit_margin = (total_annual_profit / (company_revenue * 12)) * 100
                margin_label = tk.Label(summary_frame,
                                    text=f"Profit Margin: {profit_margin:.2f}%",
                                    font=('Arial', 12, 'bold'),
                                    fg='#3498db',
                                    bg='#e8f5e8')
                margin_label.pack(pady=(2, 10))
                
                # Enable export button
                export_btn.config(state='normal')
                
            except mysql.connector.Error as err:
                error_label = tk.Label(scrollable_frame,
                                    text=f"❌ Database Error: {err}",
                                    font=('Arial', 12, 'bold'),
                                    fg='#e74c3c',
                                    bg='white')
                error_label.pack(pady=20)
            except Exception as e:
                error_label = tk.Label(scrollable_frame,
                                    text=f"❌ Error: {str(e)}",
                                    font=('Arial', 12, 'bold'),
                                    fg='#e74c3c',
                                    bg='white')
                error_label.pack(pady=20)
        
        def export_profit_data(self):
            """Export profit calculation data to a file"""
            try:
                from tkinter import filedialog, messagebox
                import datetime
                import os
                import subprocess
                import sys
                
                # Check if data exists
                if not profit_data or not profit_data.get('monthly_profits'):
                    messagebox.showwarning("No Data", "Please calculate profit data first before exporting.")
                    return
                
                # Ask user for file location
                file_path = filedialog.asksaveasfilename(
                    title="Save Profit Report As",
                    defaultextension=".txt",
                    filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv"), ("All files", "*.*")]
                )
                
                if not file_path:
                    return  # User cancelled
                
                # Generate report content
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write("SYNEX INDUSTRIES - MONTHLY PROFIT REPORT\n")
                    file.write("=" * 60 + "\n")
                    file.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    file.write("=" * 60 + "\n\n")
                    
                    file.write("MONTHLY PROFIT BREAKDOWN:\n")
                    file.write("-" * 60 + "\n")
                    file.write(f"{'Month':<15} {'Cost':<20} {'Profit':<20}\n")
                    file.write("-" * 60 + "\n")
                    
                    for month in profit_data['monthly_costs']:
                        cost = profit_data['monthly_costs'][month]
                        profit = profit_data['monthly_profits'][month]
                        file.write(f"{month:<15} Rs. {cost:<18.2f} Rs. {profit:<18.2f}\n")
                    
                    file.write("-" * 60 + "\n")
                    file.write(f"{'TOTAL ANNUAL':<15} Rs. {profit_data['total_annual_cost']:<18.2f} Rs. {profit_data['total_annual_profit']:<18.2f}\n")
                    file.write("=" * 60 + "\n")
                    
                    # Additional statistics
                    file.write("\nSTATISTICS:\n")
                    file.write("-" * 60 + "\n")
                    file.write(f"Monthly Revenue: Rs. {profit_data['company_revenue']:,.2f}\n")
                    file.write(f"Annual Revenue: Rs. {profit_data['company_revenue'] * 12:,.2f}\n")
                    file.write(f"Total Annual Cost: Rs. {profit_data['total_annual_cost']:,.2f}\n")
                    file.write(f"Total Annual Profit: Rs. {profit_data['total_annual_profit']:,.2f}\n")
                    
                    profit_margin = (profit_data['total_annual_profit'] / (profit_data['company_revenue'] * 12)) * 100
                    file.write(f"Profit Margin: {profit_margin:.2f}%\n")
                    
                    months_with_cost = sum(1 for cost in profit_data['monthly_costs'].values() if cost > 0)
                    avg_monthly_cost = profit_data['total_annual_cost'] / 12
                    avg_monthly_profit = profit_data['total_annual_profit'] / 12
                    
                    file.write(f"Months with operational costs: {months_with_cost}\n")
                    file.write(f"Average monthly cost: Rs. {avg_monthly_cost:.2f}\n")
                    file.write(f"Average monthly profit: Rs. {avg_monthly_profit:.2f}\n")
                    file.write(f"Highest monthly cost: Rs. {max(profit_data['monthly_costs'].values()):,.2f}\n")
                    file.write(f"Lowest monthly cost: Rs. {min(profit_data['monthly_costs'].values()):,.2f}\n")
                
                # Success message
                messagebox.showinfo("Export Successful",
                                f"Profit report has been successfully exported to:\n{file_path}")
                
                # Ask if user wants to open the file
                if messagebox.askyesno("Open File", "Would you like to open the exported file?"):
                    try:
                        if sys.platform.startswith('win'):
                            os.startfile(file_path)
                        elif sys.platform.startswith('darwin'):
                            subprocess.call(['open', file_path])
                        else:
                            subprocess.call(['xdg-open', file_path])
                    except Exception as e:
                        messagebox.showwarning("Open File", f"Could not open file automatically: {str(e)}")
                
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export profit data: {str(e)}")
        
        # Initial instruction
        instruction_label = tk.Label(scrollable_frame,
                                text="Click 'CALCULATE PROFIT' to generate company profit analysis",
                                font=('Arial', 14),
                                fg='#7f8c8d',
                                bg='white')
        instruction_label.pack(expand=True, pady=50)
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Buttons frame
        buttons_frame = tk.Frame(self.content_frame, bg='white')
        buttons_frame.pack(pady=20)
        
        # Calculate button
        calculate_btn = tk.Button(buttons_frame,
                                text="📊 CALCULATE PROFIT",
                                font=('Arial', 12, 'bold'),
                                bg='#27ae60',
                                fg='white',
                                width=20,
                                height=2,
                                relief='flat',
                                cursor='hand2',
                                command=calculate_company_profit)
        calculate_btn.pack(side='left', padx=(0, 10))
        
        # Export button
        export_btn = tk.Button(buttons_frame,
                            text="📄 EXPORT REPORT",
                            font=('Arial', 12, 'bold'),
                            bg='#3498db',
                            fg='white',
                            width=20,
                            height=2,
                            relief='flat',
                            cursor='hand2',
                            state='disabled',
                            command=lambda: export_profit_data(self))
        export_btn.pack(side='left', padx=(0, 10))
        
        # Back button
        back_btn = tk.Button(buttons_frame,
                        text="⬅️ BACK",
                        font=('Arial', 12, 'bold'),
                        bg='#95a5a6',
                        fg='white',
                        width=15,
                        height=2,
                        relief='flat',
                        cursor='hand2',
                        command=self.show_emp_manager)
        back_btn.pack(side='left')
        
        # Enable mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        canvas.bind("<MouseWheel>", _on_mousewheel)  
    
    def create_year_report(self):
        """Create yearly salary report interface"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Header
        header_frame = tk.Frame(self.content_frame, bg='white')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(header_frame,
                            text="📅 Employee Year Salary Report",
                            font=('Arial', 18, 'bold'),
                            fg='#2c3e50',
                            bg='white')
        title_label.pack(pady=10)
        
        # Input frame
        input_frame = tk.Frame(self.content_frame, bg='white')
        input_frame.pack(fill='x', padx=20, pady=10)
        
        # Employee code input
        emp_label = tk.Label(input_frame,
                            text="Employee Code:",
                            font=('Arial', 12, 'bold'),
                            fg='#2c3e50',
                            bg='white')
        emp_label.pack(side='left', padx=(0, 10))
        
        emp_code_entry = tk.Entry(input_frame,
                                font=('Arial', 12),
                                width=15,
                                relief='solid',
                                bd=1)
        emp_code_entry.pack(side='left', padx=(0, 20))
        
        # Create scrollable frame for results
        canvas_frame = tk.Frame(self.content_frame, bg='white')
        canvas_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        canvas = tk.Canvas(canvas_frame, bg='white')
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Variables to store data for export
        report_data = {}
        
        def generate_year_report():
            """Generate and display yearly salary report"""
            nonlocal report_data
            emp_code = emp_code_entry.get().strip()
            
            if not emp_code:
                messagebox.showwarning("Input Error", "Please enter an employee code.")
                return
            
            try:
                # Clear previous results
                for widget in scrollable_frame.winfo_children():
                    widget.destroy()
                
                # Get employee data
                get_employee_data = f"SELECT * FROM employee WHERE Emp_code = '{emp_code}'"
                self.cursor.execute(get_employee_data)
                fetch = self.cursor.fetchall()
                
                if not fetch:
                    no_data_label = tk.Label(scrollable_frame,
                                        text=f"❌ No employee found with code: {emp_code}",
                                        font=('Arial', 14, 'bold'),
                                        fg='#e74c3c',
                                        bg='white')
                    no_data_label.pack(pady=20)
                    return
                
                emp_data = {}
                for data in fetch:
                    emp_data[data[0]] = {'emp_name': data[1], 'profession_code': data[2]}
                
                # Display employee info
                emp_info_frame = tk.Frame(scrollable_frame, bg='#f8f9fa', relief='solid', bd=1)
                emp_info_frame.pack(fill='x', padx=20, pady=10)
                
                emp_name = emp_data[emp_code]['emp_name']
                info_label = tk.Label(emp_info_frame,
                                    text=f"👤 Employee: {emp_name} | Code: {emp_code}",
                                    font=('Arial', 14, 'bold'),
                                    fg='#2c3e50',
                                    bg='#f8f9fa')
                info_label.pack(pady=10)
                
                # Table header
                header_frame = tk.Frame(scrollable_frame, bg='#3498db')
                header_frame.pack(fill='x', padx=20, pady=(10, 0))
                
                headers = ["Month", "Gross Salary", "Total Deduction", "Net Salary"]
                header_widths = [15, 20, 20, 20]
                
                for i, (header, width) in enumerate(zip(headers, header_widths)):
                    header_label = tk.Label(header_frame,
                                        text=header,
                                        font=('Arial', 11, 'bold'),
                                        fg='white',
                                        bg='#3498db',
                                        width=width,
                                        relief='solid',
                                        bd=1)
                    header_label.pack(side='left')
                
                # Get employee rate
                profession_code = emp_data[emp_code]['profession_code']
                get_daily_rate = f"SELECT daily_salary FROM profession WHERE profession_code = '{profession_code}'"
                self.cursor.execute(get_daily_rate)
                rate_fetch = self.cursor.fetchall()
                
                if not rate_fetch:
                    error_label = tk.Label(scrollable_frame,
                                        text="❌ No daily rate found for this employee's profession",
                                        font=('Arial', 12, 'bold'),
                                        fg='#e74c3c',
                                        bg='white')
                    error_label.pack(pady=20)
                    return
                
                emp_rate = float(rate_fetch[0][0])
                
                # Get work data
                work_data_query = f"SELECT * FROM work_data WHERE emp_code = '{emp_code}'"
                self.cursor.execute(work_data_query)
                work_fetch = self.cursor.fetchall()
                
                if not work_fetch:
                    no_work_label = tk.Label(scrollable_frame,
                                        text="❌ No work data found for this employee",
                                        font=('Arial', 12, 'bold'),
                                        fg='#e74c3c',
                                        bg='white')
                    no_work_label.pack(pady=20)
                    return
                
                # Process and display data
                total_gross = 0
                total_deduction = 0
                total_net = 0
                monthly_data = []
                
                for data in work_fetch:
                    month = data[1]
                    days = int(float(data[2]))
                    
                    gross_salary = emp_rate * days
                    epf = gross_salary / 100 * 8
                    tax = gross_salary / 100 * 10
                    safety_item = 500
                    
                    total_deduction_month = epf + tax + safety_item
                    net_salary = gross_salary - total_deduction_month
                    
                    total_gross += gross_salary
                    total_deduction += total_deduction_month
                    total_net += net_salary
                    
                    monthly_data.append({
                        'month': month,
                        'gross': gross_salary,
                        'deduction': total_deduction_month,
                        'net': net_salary
                    })
                    
                    # Display row
                    row_frame = tk.Frame(scrollable_frame, bg='white')
                    row_frame.pack(fill='x', padx=20)
                    
                    row_data = [month, f"Rs. {gross_salary:,.2f}", 
                            f"Rs. {total_deduction_month:,.2f}", f"Rs. {net_salary:,.2f}"]
                    
                    for i, (value, width) in enumerate(zip(row_data, header_widths)):
                        cell_label = tk.Label(row_frame,
                                            text=value,
                                            font=('Arial', 10),
                                            fg='#2c3e50',
                                            bg='white',
                                            width=width,
                                            relief='solid',
                                            bd=1,
                                            anchor='w' if i == 0 else 'e')
                        cell_label.pack(side='left')
                
                # Total row
                total_frame = tk.Frame(scrollable_frame, bg='#27ae60')
                total_frame.pack(fill='x', padx=20, pady=(5, 10))
                
                total_data = ["TOTAL", f"Rs. {total_gross:,.2f}", 
                            f"Rs. {total_deduction:,.2f}", f"Rs. {total_net:,.2f}"]
                
                for i, (value, width) in enumerate(zip(total_data, header_widths)):
                    total_label = tk.Label(total_frame,
                                        text=value,
                                        font=('Arial', 11, 'bold'),
                                        fg='white',
                                        bg='#27ae60',
                                        width=width,
                                        relief='solid',
                                        bd=1,
                                        anchor='w' if i == 0 else 'e')
                    total_label.pack(side='left')
                
                # Store data for export
                report_data = {
                    'emp_code': emp_code,
                    'emp_name': emp_name,
                    'monthly_data': monthly_data,
                    'totals': {
                        'gross': total_gross,
                        'deduction': total_deduction,
                        'net': total_net
                    }
                }
                
                # Enable export button
                export_btn.config(state='normal')
                
            except mysql.connector.Error as err:
                error_label = tk.Label(scrollable_frame,
                                    text=f"❌ Database Error: {err}",
                                    font=('Arial', 12, 'bold'),
                                    fg='#e74c3c',
                                    bg='white')
                error_label.pack(pady=20)
            except Exception as e:
                error_label = tk.Label(scrollable_frame,
                                    text=f"❌ Error: {str(e)}",
                                    font=('Arial', 12, 'bold'),
                                    fg='#e74c3c',
                                    bg='white')
                error_label.pack(pady=20)
        
        def export_year_report():
            """Export yearly report to file"""
            try:
                from tkinter import filedialog, messagebox
                import datetime
                
                if not report_data:
                    messagebox.showwarning("No Data", "Please generate report first.")
                    return
                
                file_path = filedialog.asksaveasfilename(
                    title="Save Year Report As",
                    defaultextension=".txt",
                    filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
                )
                
                if not file_path:
                    return
                
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(f"YEARLY SALARY REPORT - {report_data['emp_name']}\n")
                    file.write("=" * 80 + "\n")
                    file.write(f"Employee Code: {report_data['emp_code']}\n")
                    file.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    file.write("=" * 80 + "\n\n")
                    
                    file.write(f"{'Month':<15} {'Gross Salary':<20} {'Deduction':<20} {'Net Salary':<20}\n")
                    file.write("-" * 80 + "\n")
                    
                    for data in report_data['monthly_data']:
                        file.write(f"{data['month']:<15} Rs. {data['gross']:<18.2f} "
                                f"Rs. {data['deduction']:<18.2f} Rs. {data['net']:<18.2f}\n")
                    
                    file.write("-" * 80 + "\n")
                    file.write(f"{'TOTAL':<15} Rs. {report_data['totals']['gross']:<18.2f} "
                            f"Rs. {report_data['totals']['deduction']:<18.2f} "
                            f"Rs. {report_data['totals']['net']:<18.2f}\n")
                
                messagebox.showinfo("Export Successful", f"Report exported to:\n{file_path}")
                
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export: {str(e)}")
        
        # Initial instruction
        instruction_label = tk.Label(scrollable_frame,
                                text="Enter employee code and click 'GENERATE REPORT' to create yearly salary report",
                                font=('Arial', 14),
                                fg='#7f8c8d',
                                bg='white')
        instruction_label.pack(expand=True, pady=50)
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Buttons frame
        buttons_frame = tk.Frame(self.content_frame, bg='white')
        buttons_frame.pack(pady=20)
        
        # Generate button
        generate_btn = tk.Button(buttons_frame,
                            text="📊 GENERATE REPORT",
                            font=('Arial', 12, 'bold'),
                            bg='#27ae60',
                            fg='white',
                            width=20,
                            height=2,
                            relief='flat',
                            cursor='hand2',
                            command=generate_year_report)
        generate_btn.pack(side='left', padx=(0, 10))
        
        # Export button
        export_btn = tk.Button(buttons_frame,
                            text="📄 EXPORT REPORT",
                            font=('Arial', 12, 'bold'),
                            bg='#3498db',
                            fg='white',
                            width=20,
                            height=2,
                            relief='flat',
                            cursor='hand2',
                            state='disabled',
                            command=export_year_report)
        export_btn.pack(side='left', padx=(0, 10))
        
        # Back button
        back_btn = tk.Button(buttons_frame,
                        text="⬅️ BACK",
                        font=('Arial', 12, 'bold'),
                        bg='#95a5a6',
                        fg='white',
                        width=15,
                        height=2,
                        relief='flat',
                        cursor='hand2',
                        command=self.show_emp_manager)
        back_btn.pack(side='left')
        
        # Enable mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        canvas.bind("<MouseWheel>", _on_mousewheel)






    def create_month_report(self):
        """Create monthly salary report interface"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Header
        header_frame = tk.Frame(self.content_frame, bg='white')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(header_frame,
                            text="📅 Employee Monthly Salary Report",
                            font=('Arial', 18, 'bold'),
                            fg='#2c3e50',
                            bg='white')
        title_label.pack(pady=10)
        
        # Input frame
        input_frame = tk.Frame(self.content_frame, bg='white')
        input_frame.pack(fill='x', padx=20, pady=10)
        
        # Employee code input
        emp_label = tk.Label(input_frame,
                            text="Employee Code:",
                            font=('Arial', 12, 'bold'),
                            fg='#2c3e50',
                            bg='white')
        emp_label.pack(side='left', padx=(0, 10))
        
        emp_code_entry = tk.Entry(input_frame,
                                font=('Arial', 12),
                                width=15,
                                relief='solid',
                                bd=1)
        emp_code_entry.pack(side='left', padx=(0, 20))
        
        # Month selection
        month_label = tk.Label(input_frame,
                            text="Month:",
                            font=('Arial', 12, 'bold'),
                            fg='#2c3e50',
                            bg='white')
        month_label.pack(side='left', padx=(0, 10))
        
        # Month dropdown
        months = ['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December']
        
        month_var = tk.StringVar()
        month_dropdown = ttk.Combobox(input_frame,
                                    textvariable=month_var,
                                    values=months,
                                    state="readonly",
                                    font=('Arial', 12),
                                    width=12)
        month_dropdown.pack(side='left', padx=(0, 20))
        month_dropdown.current(0)  # Default to January
        
        # Create scrollable frame for results with both horizontal and vertical scrolling
        canvas_frame = tk.Frame(self.content_frame, bg='white')
        canvas_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        canvas = tk.Canvas(canvas_frame, bg='white')
        
        # Create both vertical and horizontal scrollbars
        v_scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        h_scrollbar = ttk.Scrollbar(canvas_frame, orient="horizontal", command=canvas.xview)
        
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Variables to store data for export
        report_data = {}
        
        def generate_month_report():
            """Generate and display monthly salary report"""
            nonlocal report_data
            emp_code = emp_code_entry.get().strip()
            selected_month = month_var.get()
            
            if not emp_code:
                messagebox.showwarning("Input Error", "Please enter an employee code.")
                return
            
            if not selected_month:
                messagebox.showwarning("Input Error", "Please select a month.")
                return
            
            try:
                # Clear previous results
                for widget in scrollable_frame.winfo_children():
                    widget.destroy()
                
                # Get employee data
                get_employee_data = f"SELECT * FROM employee WHERE Emp_code = '{emp_code}'"
                self.cursor.execute(get_employee_data)
                fetch = self.cursor.fetchall()
                
                if not fetch:
                    no_data_label = tk.Label(scrollable_frame,
                                        text=f"❌ No employee found with code: {emp_code}",
                                        font=('Arial', 14, 'bold'),
                                        fg='#e74c3c',
                                        bg='white')
                    no_data_label.pack(pady=20)
                    return
                
                emp_data = {}
                for data in fetch:
                    emp_data[data[0]] = {'emp_name': data[1], 'profession_code': data[2]}
                
                # Display employee info
                emp_info_frame = tk.Frame(scrollable_frame, bg='#f8f9fa', relief='solid', bd=1)
                emp_info_frame.pack(fill='x', padx=20, pady=10)
                
                emp_name = emp_data[emp_code]['emp_name']
                info_label = tk.Label(emp_info_frame,
                                    text=f"👤 Employee: {emp_name} | Code: {emp_code} | Month: {selected_month}",
                                    font=('Arial', 14, 'bold'),
                                    fg='#2c3e50',
                                    bg='#f8f9fa')
                info_label.pack(pady=10)
                
                # Get employee rate
                profession_code = emp_data[emp_code]['profession_code']
                get_daily_rate = f"SELECT daily_salary FROM profession WHERE profession_code = '{profession_code}'"
                self.cursor.execute(get_daily_rate)
                rate_fetch = self.cursor.fetchall()
                
                if not rate_fetch:
                    error_label = tk.Label(scrollable_frame,
                                        text="❌ No daily rate found for this employee's profession",
                                        font=('Arial', 12, 'bold'),
                                        fg='#e74c3c',
                                        bg='white')
                    error_label.pack(pady=20)
                    return
                
                emp_rate = float(rate_fetch[0][0])
                
                # Get work data for specific month
                work_data_query = f"SELECT * FROM work_data WHERE emp_code = '{emp_code}' AND months = '{selected_month}'"
                self.cursor.execute(work_data_query)
                work_fetch = self.cursor.fetchall()
                
                if not work_fetch:
                    no_work_label = tk.Label(scrollable_frame,
                                        text=f"❌ No work data found for {emp_name} in {selected_month}",
                                        font=('Arial', 12, 'bold'),
                                        fg='#e74c3c',
                                        bg='white')
                    no_work_label.pack(pady=20)
                    return
                
                # Table header
                header_frame = tk.Frame(scrollable_frame, bg='#3498db')
                header_frame.pack(fill='x', padx=20, pady=(10, 0))
                
                headers = ["Month", "Days Worked", "Daily Rate", "Gross Salary", "EPF (8%)", "Tax (10%)", "Safety Item", "Total Deduction", "Net Salary"]
                header_widths = [12, 12, 12, 15, 12, 12, 12, 15, 15]
                
                for i, (header, width) in enumerate(zip(headers, header_widths)):
                    header_label = tk.Label(header_frame,
                                        text=header,
                                        font=('Arial', 10, 'bold'),
                                        fg='white',
                                        bg='#3498db',
                                        width=width,
                                        relief='solid',
                                        bd=1)
                    header_label.pack(side='left')
                
                # Process and display data
                for data in work_fetch:
                    month = data[1]
                    days = int(float(data[2]))
                    
                    gross_salary = emp_rate * days
                    epf = gross_salary / 100 * 8
                    tax = gross_salary / 100 * 10
                    safety_item = 500
                    
                    total_deduction = epf + tax + safety_item
                    net_salary = gross_salary - total_deduction
                    
                    # Display row
                    row_frame = tk.Frame(scrollable_frame, bg='white')
                    row_frame.pack(fill='x', padx=20)
                    
                    row_data = [
                        month,
                        str(days),
                        f"Rs. {emp_rate:,.2f}",
                        f"Rs. {gross_salary:,.2f}",
                        f"Rs. {epf:,.2f}",
                        f"Rs. {tax:,.2f}",
                        f"Rs. {safety_item:,.2f}",
                        f"Rs. {total_deduction:,.2f}",
                        f"Rs. {net_salary:,.2f}"
                    ]
                    
                    for i, (value, width) in enumerate(zip(row_data, header_widths)):
                        cell_label = tk.Label(row_frame,
                                            text=value,
                                            font=('Arial', 10),
                                            fg='#2c3e50',
                                            bg='white',
                                            width=width,
                                            relief='solid',
                                            bd=1,
                                            anchor='w' if i in [0] else 'e')
                        cell_label.pack(side='left')
                    
                    # Store data for export
                    report_data = {
                        'emp_code': emp_code,
                        'emp_name': emp_name,
                        'month': selected_month,
                        'days': days,
                        'daily_rate': emp_rate,
                        'gross_salary': gross_salary,
                        'epf': epf,
                        'tax': tax,
                        'safety_item': safety_item,
                        'total_deduction': total_deduction,
                        'net_salary': net_salary
                    }
                    
                    # Enable export button
                    export_btn.config(state='normal')
                
            except mysql.connector.Error as err:
                error_label = tk.Label(scrollable_frame,
                                    text=f"❌ Database Error: {err}",
                                    font=('Arial', 12, 'bold'),
                                    fg='#e74c3c',
                                    bg='white')
                error_label.pack(pady=20)
            except Exception as e:
                error_label = tk.Label(scrollable_frame,
                                    text=f"❌ Error: {str(e)}",
                                    font=('Arial', 12, 'bold'),
                                    fg='#e74c3c',
                                    bg='white')
                error_label.pack(pady=20)
        
        def export_month_report():
            """Export monthly report to file"""
            try:
                from tkinter import filedialog, messagebox
                import datetime
                
                if not report_data:
                    messagebox.showwarning("No Data", "Please generate report first.")
                    return
                
                file_path = filedialog.asksaveasfilename(
                    title="Save Monthly Report As",
                    defaultextension=".txt",
                    filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
                )
                
                if not file_path:
                    return
                
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(f"MONTHLY SALARY REPORT - {report_data['emp_name']}\n")
                    file.write("=" * 100 + "\n")
                    file.write(f"Employee Code: {report_data['emp_code']}\n")
                    file.write(f"Employee Name: {report_data['emp_name']}\n")
                    file.write(f"Month: {report_data['month']}\n")
                    file.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    file.write("=" * 100 + "\n\n")
                    
                    file.write("SALARY BREAKDOWN:\n")
                    file.write("-" * 50 + "\n")
                    file.write(f"Days Worked:      {report_data['days']} days\n")
                    file.write(f"Daily Rate:       Rs. {report_data['daily_rate']:,.2f}\n")
                    file.write(f"Gross Salary:     Rs. {report_data['gross_salary']:,.2f}\n")
                    file.write("\n")
                    file.write("DEDUCTIONS:\n")
                    file.write(f"EPF (8%):         Rs. {report_data['epf']:,.2f}\n")
                    file.write(f"Tax (10%):        Rs. {report_data['tax']:,.2f}\n")
                    file.write(f"Safety Item:      Rs. {report_data['safety_item']:,.2f}\n")
                    file.write(f"Total Deduction:  Rs. {report_data['total_deduction']:,.2f}\n")
                    file.write("\n")
                    file.write("-" * 50 + "\n")
                    file.write(f"NET SALARY:       Rs. {report_data['net_salary']:,.2f}\n")
                    file.write("=" * 100 + "\n")
                
                messagebox.showinfo("Export Successful", f"Report exported to:\n{file_path}")
                
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export: {str(e)}")
        
        # Initial instruction
        instruction_label = tk.Label(scrollable_frame,
                                text="Enter employee code, select month, and click 'GENERATE REPORT' to create monthly salary report",
                                font=('Arial', 14),
                                fg='#7f8c8d',
                                bg='white')
        instruction_label.pack(expand=True, pady=50)
        
        # Pack canvas and scrollbars
        canvas.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")
        
        # Configure grid weights for proper resizing
        canvas_frame.grid_rowconfigure(0, weight=1)
        canvas_frame.grid_columnconfigure(0, weight=1)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.content_frame, bg='white')
        buttons_frame.pack(pady=20)
        
        # Generate button
        generate_btn = tk.Button(buttons_frame,
                            text="📊 GENERATE REPORT",
                            font=('Arial', 12, 'bold'),
                            bg='#27ae60',
                            fg='white',
                            width=20,
                            height=2,
                            relief='flat',
                            cursor='hand2',
                            command=generate_month_report)
        generate_btn.pack(side='left', padx=(0, 10))
        
        # Export button
        export_btn = tk.Button(buttons_frame,
                            text="📄 EXPORT REPORT",
                            font=('Arial', 12, 'bold'),
                            bg='#3498db',
                            fg='white',
                            width=20,
                            height=2,
                            relief='flat',
                            cursor='hand2',
                            state='disabled',
                            command=export_month_report)
        export_btn.pack(side='left', padx=(0, 10))
        
        # Back button
        back_btn = tk.Button(buttons_frame,
                        text="⬅️ BACK",
                        font=('Arial', 12, 'bold'),
                        bg='#95a5a6',
                        fg='white',
                        width=15,
                        height=2,
                        relief='flat',
                        cursor='hand2',
                        command=self.show_emp_manager)
        back_btn.pack(side='left')
        
        # Enable mouse wheel scrolling for both directions
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        def _on_shift_mousewheel(event):
            canvas.xview_scroll(int(-1*(event.delta/120)), "units")
        
        # Bind mouse wheel events
        canvas.bind("<MouseWheel>", _on_mousewheel)
        canvas.bind("<Shift-MouseWheel>", _on_shift_mousewheel)
        
        # Also bind to the scrollable frame
        scrollable_frame.bind("<MouseWheel>", _on_mousewheel)
        scrollable_frame.bind("<Shift-MouseWheel>", _on_shift_mousewheel)
        
        # Make sure the canvas can receive focus for keyboard scrolling
        canvas.focus_set()
        
        # Add keyboard scrolling support
        def _on_key_press(event):
            if event.keysym == 'Left':
                canvas.xview_scroll(-1, "units")
            elif event.keysym == 'Right':
                canvas.xview_scroll(1, "units")
            elif event.keysym == 'Up':
                canvas.yview_scroll(-1, "units")
            elif event.keysym == 'Down':
                canvas.yview_scroll(1, "units")
        
        canvas.bind("<Key>", _on_key_press)
    


    def show_reports(self):
        """Show reports interface with file listing and viewer"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Header
        header_frame = tk.Frame(self.content_frame, bg='white')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(header_frame,
                            text="📊 Reports Center",
                            font=('Arial', 18, 'bold'),
                            fg='#2c3e50',
                            bg='white')
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(header_frame,
                                text="View and manage files from any folder",
                                font=('Arial', 12),
                                fg='#7f8c8d',
                                bg='white')
        subtitle_label.pack()
        
        # Main content frame
        main_frame = tk.Frame(self.content_frame, bg='white')
        main_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Create left and right panels
        left_panel = tk.Frame(main_frame, bg='white', width=300)
        left_panel.pack(side='left', fill='y', padx=(0, 10))
        left_panel.pack_propagate(False)
        
        right_panel = tk.Frame(main_frame, bg='white')
        right_panel.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        # Left panel - File list
        file_list_frame = tk.Frame(left_panel, bg='white', relief='solid', bd=1)
        file_list_frame.pack(fill='both', expand=True)
        
        # File list header with current folder display
        file_header_frame = tk.Frame(file_list_frame, bg='#ecf0f1')
        file_header_frame.pack(fill='x')
        
        file_header = tk.Label(file_header_frame,
                            text="📁 File Browser",
                            font=('Arial', 14, 'bold'),
                            fg='#2c3e50',
                            bg='#ecf0f1')
        file_header.pack(side='left', pady=5, padx=10)
        
        # Current folder label
        current_folder_label = tk.Label(file_header_frame,
                                    text="No folder selected",
                                    font=('Arial', 9),
                                    fg='#7f8c8d',
                                    bg='#ecf0f1',
                                    wraplength=200)
        current_folder_label.pack(side='right', pady=5, padx=5)
        
        # Default folder path (start with reports folder)
        current_folder = {"path": "reports"}
        
        # Create default reports folder if it doesn't exist
        if not os.path.exists(current_folder["path"]):
            os.makedirs(current_folder["path"])
        
        # Listbox for files
        files_listbox = tk.Listbox(file_list_frame,
                                font=('Arial', 10),
                                bg='white',
                                selectbackground='#3498db',
                                selectforeground='white',
                                relief='flat')
        files_listbox.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Scrollbar for listbox
        listbox_scrollbar = tk.Scrollbar(file_list_frame, orient='vertical', command=files_listbox.yview)
        files_listbox.configure(yscrollcommand=listbox_scrollbar.set)
        listbox_scrollbar.pack(side='right', fill='y')
        files_listbox.pack(side='left', fill='both', expand=True, padx=(5, 0), pady=5)
        
        # Right panel - File viewer
        viewer_frame = tk.Frame(right_panel, bg='white', relief='solid', bd=1)
        viewer_frame.pack(fill='both', expand=True)
        
        # Viewer header
        viewer_header_frame = tk.Frame(viewer_frame, bg='#ecf0f1')
        viewer_header_frame.pack(fill='x')
        
        viewer_title = tk.Label(viewer_header_frame,
                            text="📄 File Viewer",
                            font=('Arial', 14, 'bold'),
                            fg='#2c3e50',
                            bg='#ecf0f1')
        viewer_title.pack(side='left', pady=5, padx=10)
        
        # Current file label
        current_file_label = tk.Label(viewer_header_frame,
                                    text="No file selected",
                                    font=('Arial', 10, 'italic'),
                                    fg='#7f8c8d',
                                    bg='#ecf0f1')
        current_file_label.pack(side='right', pady=5, padx=10)
        
        # Text widget for file content
        text_frame = tk.Frame(viewer_frame, bg='white')
        text_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        text_widget = tk.Text(text_frame,
                            font=('Consolas', 10),
                            bg='white',
                            fg='#2c3e50',
                            relief='flat',
                            wrap='word',
                            state='disabled')
        
        # Scrollbars for text widget
        text_v_scrollbar = tk.Scrollbar(text_frame, orient='vertical', command=text_widget.yview)
        text_h_scrollbar = tk.Scrollbar(text_frame, orient='horizontal', command=text_widget.xview)
        text_widget.configure(yscrollcommand=text_v_scrollbar.set, xscrollcommand=text_h_scrollbar.set)
        
        text_widget.pack(side='left', fill='both', expand=True)
        text_v_scrollbar.pack(side='right', fill='y')
        text_h_scrollbar.pack(side='bottom', fill='x')
        
        # Buttons frame
        buttons_frame = tk.Frame(left_panel, bg='white')
        buttons_frame.pack(fill='x', pady=(10, 0))
        
        def load_file_list():
            """Load txt files from current folder"""
            files_listbox.delete(0, tk.END)
            
            try:
                if os.path.exists(current_folder["path"]):
                    # Get all files (not just .txt)
                    all_files = []
                    for file in os.listdir(current_folder["path"]):
                        file_path = os.path.join(current_folder["path"], file)
                        if os.path.isfile(file_path):
                            all_files.append(file)
                    
                    if all_files:
                        all_files.sort()  # Sort files alphabetically
                        for file in all_files:
                            files_listbox.insert(tk.END, file)
                    else:
                        files_listbox.insert(tk.END, "No files found")
                        
                    # Update current folder display
                    folder_name = os.path.basename(current_folder["path"]) or current_folder["path"]
                    current_folder_label.config(text=f"📂 {folder_name}")
                else:
                    files_listbox.insert(tk.END, "Folder not found")
                    current_folder_label.config(text="❌ Invalid folder")
                    
            except Exception as e:
                files_listbox.insert(tk.END, f"Error loading files: {str(e)}")
        
        def select_folder():
            """Open folder selection dialog"""
            from tkinter import filedialog
            
            folder_path = filedialog.askdirectory(
                title="Select Folder to Browse",
                initialdir=current_folder["path"] if os.path.exists(current_folder["path"]) else os.getcwd()
            )
            
            if folder_path:
                current_folder["path"] = folder_path
                load_file_list()
                # Clear text widget when changing folders
                text_widget.config(state='normal')
                text_widget.delete(1.0, tk.END)
                text_widget.config(state='disabled')
                current_file_label.config(text="No file selected")
        
        def view_selected_file():
            """View the selected file in the text widget"""
            selection = files_listbox.curselection()
            
            if not selection:
                messagebox.showwarning("No Selection", "Please select a file to view!")
                return
            
            selected_file = files_listbox.get(selection[0])
            
            if selected_file in ["No files found", "Folder not found"] or selected_file.startswith("Error"):
                messagebox.showwarning("Invalid Selection", "Please select a valid file!")
                return
            
            file_path = os.path.join(current_folder["path"], selected_file)
            
            try:
                # Try to read as text file with different encodings
                content = ""
                encodings = ['utf-8', 'latin-1', 'cp1252', 'ascii']
                
                for encoding in encodings:
                    try:
                        with open(file_path, 'r', encoding=encoding) as file:
                            content = file.read()
                        break
                    except UnicodeDecodeError:
                        continue
                
                if not content:
                    # If all text encodings fail, try to read as binary and show hex
                    with open(file_path, 'rb') as file:
                        binary_content = file.read(1024)  # Read first 1KB
                        content = f"Binary file detected. First 1024 bytes in hex:\n\n"
                        content += ' '.join(f'{b:02x}' for b in binary_content)
                        if len(binary_content) == 1024:
                            content += "\n\n... (file truncated)"
                
                # Update text widget
                text_widget.config(state='normal')
                text_widget.delete(1.0, tk.END)
                text_widget.insert(1.0, content)
                text_widget.config(state='disabled')
                
                # Update current file label
                current_file_label.config(text=f"Viewing: {selected_file}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Error reading file: {str(e)}")
                text_widget.config(state='normal')
                text_widget.delete(1.0, tk.END)
                text_widget.insert(1.0, f"Error reading file: {str(e)}")
                text_widget.config(state='disabled')
        
        def refresh_file_list():
            """Refresh the file list"""
            load_file_list()
            # Clear text widget
            text_widget.config(state='normal')
            text_widget.delete(1.0, tk.END)
            text_widget.config(state='disabled')
            current_file_label.config(text="No file selected")
            messagebox.showinfo("Refreshed", "File list has been refreshed!")
        
        def open_current_folder():
            """Open the current folder in file explorer"""
            try:
                if os.path.exists(current_folder["path"]):
                    if os.name == 'nt':  # Windows
                        os.startfile(current_folder["path"])
                    elif os.name == 'posix':  # macOS and Linux
                        os.system(f'open "{current_folder["path"]}"' if sys.platform == 'darwin' else f'xdg-open "{current_folder["path"]}"')
                else:
                    messagebox.showwarning("Folder Not Found", f"Folder '{current_folder['path']}' does not exist!")
            except Exception as e:
                messagebox.showerror("Error", f"Error opening folder: {str(e)}")
        
        def delete_selected_file():
            """Delete the selected file"""
            selection = files_listbox.curselection()
            
            if not selection:
                messagebox.showwarning("No Selection", "Please select a file to delete!")
                return
            
            selected_file = files_listbox.get(selection[0])
            
            if selected_file in ["No files found", "Folder not found"] or selected_file.startswith("Error"):
                messagebox.showwarning("Invalid Selection", "Please select a valid file!")
                return
            
            # Confirm deletion
            result = messagebox.askyesno(
                "Confirm Deletion", 
                f"Are you sure you want to delete '{selected_file}'?\n\nThis action cannot be undone!",
                icon='warning'
            )
            
            if not result:
                return
            
            file_path = os.path.join(current_folder["path"], selected_file)
            
            try:
                # Check if file exists and is not a directory
                if os.path.exists(file_path):
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        messagebox.showinfo("Success", f"File '{selected_file}' has been deleted successfully!")
                        
                        # Clear text widget if deleted file was being viewed
                        if current_file_label.cget("text") == f"Viewing: {selected_file}":
                            text_widget.config(state='normal')
                            text_widget.delete(1.0, tk.END)
                            text_widget.config(state='disabled')
                            current_file_label.config(text="No file selected")
                        
                        # Refresh file list
                        load_file_list()
                    else:
                        messagebox.showerror("Error", f"'{selected_file}' is not a file!")
                else:
                    messagebox.showerror("Error", f"File '{selected_file}' does not exist!")
                    
            except PermissionError:
                messagebox.showerror("Permission Error", f"Permission denied! Cannot delete '{selected_file}'.\nThe file might be in use or you don't have sufficient permissions.")
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting file: {str(e)}")

        def create_sample_report():
            """Create a sample report file for testing"""
            import datetime
            
            sample_content = f"""SYNEX INDUSTRIES - SAMPLE REPORT
    Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    =====================================

    This is a sample report file for testing the file viewer functionality.

    EMPLOYEE SUMMARY:
    - Total Employees: 50
    - Active Employees: 45
    - On Leave: 5

    SALARY SUMMARY:
    - Total Payroll: $125,000
    - Average Salary: $2,500
    - Highest Salary: $5,000
    - Lowest Salary: $1,200

    DEPARTMENT BREAKDOWN:
    - IT Department: 15 employees
    - Sales Department: 20 employees
    - HR Department: 5 employees
    - Finance Department: 10 employees

    =====================================
    End of Report
    """
            
            try:
                if not os.path.exists(current_folder["path"]):
                    os.makedirs(current_folder["path"])
                
                sample_file = os.path.join(current_folder["path"], f"sample_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
                
                with open(sample_file, 'w', encoding='utf-8') as file:
                    file.write(sample_content)
                
                messagebox.showinfo("Success", f"Sample report created: {os.path.basename(sample_file)}")
                load_file_list()
                
            except Exception as e:
                messagebox.showerror("Error", f"Error creating sample report: {str(e)}")
        
        # Buttons
        select_folder_btn = tk.Button(buttons_frame,
                                    text="SELECT FOLDER",
                                    font=('Arial', 10, 'bold'),
                                    bg='#e74c3c',
                                    fg='white',
                                    width=18,
                                    relief='flat',
                                    cursor='hand2',
                                    command=select_folder)
        select_folder_btn.pack(pady=2, fill='x')
        
        view_btn = tk.Button(buttons_frame,
                            text="VIEW FILE",
                            font=('Arial', 10, 'bold'),
                            bg='#3498db',
                            fg='white',
                            width=18,
                            relief='flat',
                            cursor='hand2',
                            command=view_selected_file)
        view_btn.pack(pady=2, fill='x')
        
        refresh_btn = tk.Button(buttons_frame,
                            text="REFRESH LIST",
                            font=('Arial', 10, 'bold'),
                            bg='#27ae60',
                            fg='white',
                            width=18,
                            relief='flat',
                            cursor='hand2',
                            command=refresh_file_list)
        refresh_btn.pack(pady=2, fill='x')
        
        folder_btn = tk.Button(buttons_frame,
                            text="OPEN FOLDER",
                            font=('Arial', 10, 'bold'),
                            bg='#f39c12',
                            fg='white',
                            width=18,
                            relief='flat',
                            cursor='hand2',
                            command=open_current_folder)
        folder_btn.pack(pady=2, fill='x')
        
        delete_btn = tk.Button(buttons_frame,
                            text="DELETE FILE",
                            font=('Arial', 10, 'bold'),
                            bg='#e74c3c',
                            fg='white',
                            width=18,
                            relief='flat',
                            cursor='hand2',
                            command=delete_selected_file)
        delete_btn.pack(pady=2, fill='x')
        
        sample_btn = tk.Button(buttons_frame,
                            text="CREATE SAMPLE",
                            font=('Arial', 10, 'bold'),
                            bg='#9b59b6',
                            fg='white',
                            width=18,
                            relief='flat',
                            cursor='hand2',
                            command=create_sample_report)
        sample_btn.pack(pady=2, fill='x')
        
        # Double-click to view file
        files_listbox.bind('<Double-Button-1>', lambda e: view_selected_file())
        
        # Load files initially
        load_file_list()
        
        # Status bar
        status_frame = tk.Frame(self.content_frame, bg='#ecf0f1', relief='solid', bd=1)
        status_frame.pack(fill='x', side='bottom', pady=(10, 0))
        
        status_label = tk.Label(status_frame,
                            text=f"Current Folder: {os.path.abspath(current_folder['path'])}",
                            font=('Arial', 9),
                            fg='#7f8c8d',
                            bg='#ecf0f1')
        status_label.pack(side='left', padx=10, pady=2)
        
        # Update status label when folder changes
        def update_status():
            status_label.config(text=f"Current Folder: {os.path.abspath(current_folder['path'])}")
        
        # Store reference to update function for potential future use
        current_folder["update_status"] = update_status
    
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