# Sorted alphabetically by VIN
TEST_DATA = [
    # http://www.vindecoder.net/?vin=19XFB4F24DE547421&submit=Decode says unknown
    # http://www.civicx.com/threads/2016-civic-vin-translator-decoder-guide.889/
    {'VIN': '19XFB4F24DE547421', 'WMI': '19X', 'VDS': 'FB4F24', 'VIS': 'DE547421',
     'MODEL': 'Civic Hybrid', 'MAKE':  'Honda', 'YEAR': 2013, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '547421', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=1FAHP3FN8AW139719&submit=Decode
    {'VIN': '1FAHP3FN8AW139719', 'WMI': '1FA', 'VDS': 'HP3FN8', 'VIS': 'AW139719',
     'MODEL': 'Focus', 'MAKE':  'Ford', 'YEAR': 2010, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '139719', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=1GKEV13728J123735&submit=Decode
    {'VIN': '1GKEV13728J123735', 'WMI': '1GK', 'VDS': 'EV1372', 'VIS': '8J123735',
     'MODEL': 'Acadia', 'MAKE':  'GMC', 'YEAR': 2008, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '123735', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=1GYFC56299R410242&submit=Decode didn't have model
    # http://www.vindecoderz.com/EN/check-lookup/1GYFC56299R410242
    # http://www.fueleconomy.gov/ws/rest/vehicle/menu/model?year=2009&make=Cadillac confirms Escalade ESV
    {'VIN': '1GYFC56299R410242', 'WMI': '1GY', 'VDS': 'FC5629', 'VIS': '9R410242',
     'MODEL': 'Escalade ESV', 'MAKE':  'Cadillac', 'YEAR': 2009, 'COUNTRY': 'United States',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '410242', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=2A4GM684X6R632476&submit=Decode
    {'VIN': '2A4GM684X6R632476', 'WMI': '2A4', 'VDS': 'GM684X', 'VIS': '6R632476',
     'MODEL': 'Pacifica', 'MAKE':  'Chrysler', 'YEAR': 2006, 'COUNTRY': 'Canada',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '632476', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=2B3KA43G27H825762&submit=Decode
    {'VIN': '2B3KA43G27H825762', 'WMI': '2B3', 'VDS': 'KA43G2', 'VIS': '7H825762',
     'MODEL': 'Charger', 'MAKE':  'Dodge', 'YEAR': 2007, 'COUNTRY': 'Canada',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '825762', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=2C3CDYAGXDH825982&submit=Decode doesn't have good info
    # http://dodgeforum.com/forum/vindecoder.php?vin=2C3CDYAGXDH825982
    {'VIN': '2C3CDYAGXDH825982', 'WMI': '2C3', 'VDS': 'CDYAGX', 'VIS': 'DH825982',
     'MODEL': 'Challenger', 'MAKE':  'Dodge', 'YEAR': 2013, 'COUNTRY': 'Canada',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': '825982', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=2FTCF15F2ECA55516&submit=Decode
    {'VIN': '2FTCF15F2ECA55516', 'WMI': '2FT', 'VDS': 'CF15F2', 'VIS': 'ECA55516',
     'MODEL': 'F-150', 'MAKE':  'Ford', 'YEAR': 1984, 'COUNTRY': 'Canada',
     'REGION': 'north_america', 'SEQUENTIAL_NUMBER': 'A55516', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=JA4AD2A3XEZ426420&submit=Decode didn't have model
    # https://www.mitsubishicars.com/owners/support/vin-information
    {'VIN': 'JA4AD2A3XEZ426420', 'WMI': 'JA4', 'VDS': 'AD2A3X', 'VIS': 'EZ426420',
     'MODEL': 'Outlander ES', 'MAKE':  'Mitsubishi', 'YEAR': 2014, 'COUNTRY': 'Japan',
     'REGION': 'asia', 'SEQUENTIAL_NUMBER': '426420', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=JM1BL1SF3A1267720&submit=Decode
    {'VIN': 'JM1BL1SF3A1267720', 'WMI': 'JM1', 'VDS': 'BL1SF3', 'VIS': 'A1267720',
     'MODEL': 'MAZDA3', 'MAKE':  'Mazda', 'YEAR': 2010, 'COUNTRY': 'Japan',
     'REGION': 'asia', 'SEQUENTIAL_NUMBER': '267720', 'FEWER_THAN_500_PER_YEAR': False},

    # http://www.vindecoder.net/?vin=YV1902FH5D1796335&submit=Decode doesn't have model
    # http://www.vindecoderz.com/EN/check-lookup/YV1902FH5D1796335
    # http://www.fueleconomy.gov/ws/rest/vehicle/menu/model?year=2013&make=Volvo confirms XC60
    {'VIN': 'YV1902FH5D1796335', 'WMI': 'YV1', 'VDS': '902FH5', 'VIS': 'D1796335',
     'MODEL': 'XC60', 'MAKE':  'Volvo', 'YEAR': 2013, 'COUNTRY': 'Norway',
     'REGION': 'europe', 'SEQUENTIAL_NUMBER': '796335', 'FEWER_THAN_500_PER_YEAR': False},

]
