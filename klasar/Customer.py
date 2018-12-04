class Customer(object):
    def __init__(self, first_name, last_name, Passport_num, credit_card_number):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + last_name
        self.Passport_num = Passport_num
        self.credit_card_number = credit_card_number
    
