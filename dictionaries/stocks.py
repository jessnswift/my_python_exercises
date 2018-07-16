stock_dict = { 'GM': 'General Moters', 'MSFT': 'Microsoft',
    'CAT': 'Caterpillar', 'EK': 'Eastman Kodak',
    'AAPL': 'Apple' }

purchases = [ ('GM', 100, '10-sep-2018', 48 ),
    ('MSFT', 100, '01-april-2016', 97 ),
    ('CAT', 900, '8-may-2014', 56 ),
    ('EK', 300, '6-may-2014', 32 ),
    ('AAPL', 700, '4-dec-2017', 53 ) ]

# create a purchase history report
purchase_history = []

# Create a purchase history report that computes the full purchase price
# (shares x dollars) for each block of stock and uses the `stockDict` to look up the full company name.

# get number of shares and the price
# calculate purchase price and add to list
# look up company name
# add company name to list