sellingPrice = float(input('Enter selling price: '))
buyingPrice = float(input('Enter buying price: '))

if sellingPrice > buyingPrice:
    print('You have profit in trading of this item.')
else:
    print('You don\'t have profit in trading of this item.')