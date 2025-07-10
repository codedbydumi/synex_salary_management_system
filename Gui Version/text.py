

# letter_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
#
# passwd = input("\n  Password - ")
#
# h_passwd = ""
# for letter in passwd:
#     if letter in letter_lst:#shift by 6
#
#         h_index = letter_lst.index(letter) - 6
#         h_passwd += letter_lst[h_index]
#     else:
#         h_passwd += letter
#
#
# print(h_passwd)

user_choice = int(input("""\n\n    Press 1 for add new App User
    Press 2 for Remove  App User
    Press 3 for Add New Profession
    Press 4 for Change The Profession Details
    Press 5 For delete profession
    Press 6 for Load Data File
    Press 7 Delete Employer Data
Enter Your Choice - """))


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
    if file == '00': self.emp_manager()

    get_employee_data = 'select * from employee'
    self.cur.execute(get_employee_data)
    fetch = self.cur.fetchall()
    emp_data = {}

    for data in fetch:
        emp_data[data[0]] = {'emp_name': data[1], 'profession_code': data[2]}

    with open(file, 'w') as File:
        for names in emp_data:
            emp_name = emp_data[names]['emp_name']
            profession_code = emp_data[names]['profession_code']

            get_daly_rate = f"select daily_salary, profession_name from profession where profession_code = '{profession_code}'"
            self.cur.execute(get_daly_rate)
            fetch = self.cur.fetchall()
            File.write('______________' * 50)

            for data in fetch:
                emp_rate = int(data[0])
                profession_name = data[1]

            File.write(f"\nEmployee Name -> {emp_name}     Profession -> {profession_name}\n\n")

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
