from sheetFiller import SheetFiller
from apartmentSearch import ApartmentSearch


searcher = ApartmentSearch()
info = searcher.get_info()
address = info[0]['address']
price = info[0]['price']
link = info[0]['link']

sheet_filler = SheetFiller()
sheet_filler.fill_form(address, price, link)
