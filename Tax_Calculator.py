'''
Tax Calculator
'''
def tax_calc():
    input_price = input('Input the price: ')
    input_tax = input('Input the tax in %: ')

    tax_price = (int(input_price) * float(input_tax)/100)
    total_price = int(input_price) + int(tax_price)

    print('\n')
    print(f'Price: P{input_price}')
    print(f'Tax: {input_tax}%')
    print(f'\nTax cost: P{tax_price}')
    print(f'Total price (with tax): P{total_price}')

tax_calc()
