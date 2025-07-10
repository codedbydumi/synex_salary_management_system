letter_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
              'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class Hash:

    def __init__(self):
        pass

    def encrypt(self, passwd):
        a = 6
        self.h_passwd = ""
        for letter in passwd:

            if letter in letter_lst:  # shift by 6

                h_index = letter_lst.index(letter)+ a
                a += 2

                self.h_passwd += letter_lst[h_index]
            else:
                self.h_passwd += letter

        return self.h_passwd

    def decrypt(self, password):
        a = 6
        self.h_passwd = ""

        for letter in password:
            if letter in letter_lst:  # shift by 6

                self.h_index = letter_lst.index(letter) - a
                a +=2
                self.h_passwd += letter_lst[self.h_index]
            else:
                self.h_passwd += letter

        return self.h_passwd
