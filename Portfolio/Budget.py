# -*- coding: utf-8 -*-
"""
Created on Wed Feb    9 14:24:20 2022

@author: jindo
"""

class Category:
    # initialise the object and parameters that are locally persistant
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.Total = 0
        self.Spend = 0
        self.Deposit = 0
        title = len(name)
        no_of_stars = 30 - title
        first_half_stars = int(no_of_stars/2)
        second_half_stars = 30 - title - first_half_stars
        self.Title = first_half_stars*'*'+name+second_half_stars*'*'+'\n'
        
    # Calls the object without using parenthesis
    def __repr__(self):
        ''' 
        Returns out the ledgertable in a pretty format
        
        Args:
            self (str): Defined by the intialisation.

        Returns:
            str : formatted ledgertable
        '''
        return self.ledgertable()

    def get_balance(self):
        ''' 
        Returns out the current balance
        
        Args:
            self (str): Defined by the intialisation.

        Returns:
            str : formatted balance
        '''
        return self.Total

    def check_funds(self, amount):
        ''' 
        Checks whether the Total is high enough to be reduced by amount and 
        remain positive/ in credit        
        
        Args:
            self (str): Defined by the intialisation.

            amount (float): Value which is requested to be transferred
            or withdrawn.
        
        Returns:
            bool : bool
        '''
        if amount > self.Total:
            return False
        else:
            return True

    def none_desc(self, description=None):
        ''' 
        Returns a string to avoid an error 
        
        Args:
            self (str): Defined by the intialisation.

            description (str, optional): The string related to the transaction.
        
        Returns:
            str : either '' or the description
        '''
        if description is None:
            return ''
        else:
            return description

    def amountclip(self, amount):
        ''' 
        Formats the value to be displayed in the ledgertable
        
        Args:
            self (str): Defined by the intialisation.

            amount (float): Value which is requested to be transferred.
        
        Returns:
            str : formatted value to presented to the ledgertable
        '''
        # Convert the amount to a string and format for uniformity
        string = str(int(amount * 100))
        len_amount = len(string)
        monetise = string[:(len_amount-2)]+"."+string[(len_amount-2):]

        # Restricts the value (in str format) to be less than 7 charecters
        if len(monetise) >= 7:
            monetise = monetise[(len(string)-6):]
        else:
            monetise = (6-len_amount)*' ' + monetise
        return monetise

    def deposit(self, amount, description = None):
        ''' 
        Adds the value and amount and the desription to the reledent ledger 
        after formatting 
        
        Args:
            self (str): Defined by the intialisation.

            amount (float): Value which is requested to be transferred.
            
            description (str, optional): The string related to the transaction.
            
        Returns:
            None
        '''
        newdescription = self.none_desc(description)
        instance = {'amount' : amount, 'description' : newdescription}
        self.ledger.append(instance)
        self.Total += amount
        self.Deposit += amount

    def withdraw(self, amount, description=None):
        ''' 
        Reduces the ledger total by the amount provided there are suffient 
        funds.
        
        Args:
            self (str): Defined by the intialisation.

            amount (float): Value which is requested to be withdrawn.
            
            description (str, optional): The string related to the transaction.
        
        Returns:
            bool : bool
        '''
        if self.check_funds(amount):
            newdescription = self.none_desc(description)
            instance = {'amount' : -amount, 'description' : newdescription}
            self.ledger.append(instance)
            self.Total -= amount
            self.Spend -= amount
            return True
        else:
            return False

    def transfer(self, amount, other):
        ''' 
        Reduces the current ledger total by the amount provided there are 
        suffient funds, if sucessful, deposits the amount in the 'other' ledger.
        
        Args:
            self (str): Defined by the intialisation.

            amount (float): Value which is requested to be transferred.

            other (str): Ledger that the amount is requested to be tranferred 
            to.
        
        Returns:
            bool : bool
        '''
        if self.check_funds(amount):
            description_in_ledger1 = "Transfer to " + str(other.name)
            description_in_ledger2 = "Transfer from " + str(self.name)
            self.withdraw(amount, description_in_ledger1)
            other.deposit(amount, description_in_ledger2)
            return True
        else:
            return False

    def ledgertable(self):
        ''' 
        Prints out the ledger in a pretty format
        
        Args:
            self (str): Defined by the intialisation.

            Answer (bool, optional): Affects whether answers are displayed.
        
        Returns:
            str : formatted ledgertable
        '''
        ledger_table = self.Title
        instance = 0
        # Cycle through the ledger
        while instance < len(self.ledger):
            # Collect and pair the amount and description 
            amount = self.ledger[instance].get('amount')
            amount = self.amountclip(amount)
            desc = self.ledger[instance].get('description')
            len_desc = len(desc)
            # Clip the description for formatting
            if len_desc > 23:
                desc = desc[:23]
            else:
                desc = desc + (23-len_desc)*' '
                ledger_table += desc + amount + '\n'
                instance += 1
            ledger_table += ('Total:' + self.amountclip(self.Total))
            return ledger_table


def create_spend_chart(categories):
    
    ''' 
    Prints out the ledger chart. The categories are printed vertically and the 
    spends are printed via circles to represent as a percentage of the total 
    spend of all the categories.
    
    Args:
        categories (list, str): Must be a str equal to a pre made budget using
        the Catagory class.

    Returns:
        str : formatted budget chart
    '''
    
    if len(categories) < 1:
        quit()

    list_of_cat = []
    # Cycle through categories and make a list of the titles 
    for category in categories:
        list_of_cat.append(category.name)

    # Intialise the chart and add a title 
    chart = "Percentage spent by category\n"
    # Intialise the max value of the chart 
    percentage = 100
    totalspend = 0
    longest_name = 0
    letter = 0
    percentages_list = []
    
    # Store the category with the longest name as longest_name
    for cat_name in list_of_cat:
        if len(cat_name) > longest_name:
            longest_name = len(cat_name)

    # Calculate the culmulative total of the ledgers' spend
    for category in categories:
        totalspend += category.Spend
    
    # Calculate the the amount spent of each category out of the entire spend.
    for category in categories:
        # Restrict the accuracy to the nearest 10
        cat_perc = 10 * int(10 * (category.Spend/totalspend))
        percentages_list.append(cat_perc)

    # Cycle from the max 100% to 0% in steps of 10% and create strings to 
    # signify the percentage spends
    while percentage >= 0:
        num = str(percentage)
        # Adds the percentage line and some formatting to the chart
        chart += (3 - len(num)) * ' ' + num + '| '
        
        for cat_percentage in percentages_list:
            if cat_percentage >= percentage:
                chart += 'o  '
            else:
                chart += '   '
        chart += '\n'
        percentage -= 10
    # Create a spacer to enable pretty printing
    chart += '    -' + (len(list_of_cat) * 3) * '-' + '\n'

    # Work through the letters of the category names by stepping through the 
    # names until it reaches the last letter of the longest name 
    while letter < longest_name:
        # Create a spacer to enable pretty printing at the start of the line
        chart += '     '
        # Add the letter of the name and a space or a larger space to maintain
        # formatting
        for catagory in list_of_cat:
            try:
                chart += catagory[letter] + '  '
            except:
                chart += '   '
        if letter != longest_name - 1:
            chart += '\n'
        letter += 1
    return chart



food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
food.deposit(10, "second deposit")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(create_spend_chart([food, clothing, auto]))
