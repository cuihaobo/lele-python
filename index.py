#String
single_quote_string ='Hello I am a single quote string,my name is %s and I am %s years'
double_quote_string="Hello I am a double quote string,my name is %s and I am %s years"
triple_quote_multi_line_string = '''
Hello I am a triple multi_line_string,my name is %s and I am %s years
'''
name = "Peppa pig"
age = "8"
#print(single_quote_string % (name,s))

found_coins=20
magic_coins=70
stolen_coins=3
coins = found_coins
for week in range(1,53):
    coins = coins + magic_coins - stolen_coins
    print('Week %s = %s' % (week,coins))