import pandas as pd
import csv

def load_data():
    columns = ['id', 'url', 'region', 'region_url', 'price', 'year', 'manufacturer', 'model', 'condition', 'cylinders', 'fuel', 'odometer', 'title_status', 'transmission', 'vin', 'drive', 'size', 'type', 'paint_color', 'image_url', 'description', 'county', 'state', 'lat', 'long']
    feature_columns = ['region', 'year', 'price', 'manufacturer', 'model', 'condition', 'cylinders', 'fuel', 'odometer', 'title_status', 'transmission', 'vin', 'drive', 'size', 'type', 'paint_color', 'description', 'county', 'state']
    data = pd.read_csv("./vehicles.csv", names=columns, delimiter=',')
    data.head()

    X = data[feature_columns]
    X_clean = []
    y_clean = []
    for index, row in X.iterrows():
        print (row["price"])
        print(type(row))

# Don't implement for now, probably overspecific
def city_index(city):
    return city

def price_regularize(price):
    return price

def regularize_year(year):
    if year == "" or year == None:
        return -1
    else:
        return 2020-int(year)

def make_index(make):
    if make == "" or make == None:
        return -1
    else:
        makeUpper = make.upper()
        makes = ['ACURA', 'ALFA-ROMEO', 'ASTON-MARTIN', 'AUDI', 'BMW', 'BUICK', 'CADILLAC', 'CHEVROLET', 'CHRYSLER', 'DATSUN', 'DODGE', 'FERRARI', 'FIAT', 'FORD', 'GMC', 'HARLEY-DAVIDSON', 'HENNESSEY', 'HONDA', 'HYUNDAI', 'INFINITI', 'JAGUAR', 'JEEP', 'KIA', 'LAND ROVER', 'LEXUS', 'LINCOLN', 'MAZDA', 'MERCEDES-BENZ', 'MERCURY', 'MINI', 'MITSUBISHI', 'MORGAN', 'NISSAN', 'PONTIAC', 'PORCHE', 'RAM', 'ROVER', 'SATURN', 'SUBARU', 'TESLA', 'TOYOTA', 'VOLKSWAGEN', 'VOLVO']
        return makes.index(makeUpper)

def condition_index(condition):
    if condition == "" or condition == None:
        return -1
    else:
        conditionUpper = condition.upper()
        conditions = ['NEW', 'LIKE NEW', 'EXCELLENT', 'GOOD', 'FAIR', 'SALVAGE']
        return conditions.index(conditionUpper)

def cylinders_index(cylinder):
    if cylinder == "" or cylinder == None:
        return -1
    else:
        cylinderUpper = cylinder.upper()
        cylinders = ['3 CYLINDERS', '4 CYLINDERS', '5 CYLINDERS', '6 CYLINDERS', '8 CYLINDERS', '10 CYLINDERS', '12 CYLINDERS', 'OTHER']
        return cylinders.index(cylinderUpper)

def gas_index(gas):
    if gas == "" or gas == None:
        return -1
    else:
        gasUpper = gas.upper()
        gasTypes = ['GAS', 'DIESEL', 'OTHER', 'ELECTRIC', 'HYBRID']
        return gasTypes.index(gasUpper)

def odometer_regularize(odometer):
    return odometer

def title_index(title):
    if title == "" or title == None:
        return -1
    else:
        titleUpper = title.upper()
        titles = ['CLEAN', 'REBUILT', 'SALVAGE', 'LIEN', 'MISSING', 'PARTS ONLY']
        return titles.index(titleUpper)

def transmission_index(transmission):
    if transmission == "" or transmission == None:
        return -1
    else:
        transmissionUpper = transmission.upper()
        transmissions = ['MANUAL', 'AUTOMATIC', 'OTHER']
        return transmissions.index(transmissionUpper)

def drive_index(drive):
    if drive == "" or drive == None:
        return -1
    else:
        driveUpper = drive.upper()
        drives = ['4WD', 'FWD', 'RWD']
        return drives.index(driveUpper)

def size_index(size):
    if size == "" or size == None:
        return -1
    else:
        sizeUpper = size.upper()
        sizes = ['COMPACT', 'MID-SIZE', 'FULL-SIZE', 'SUB-COMPACT']
        return sizes.index(sizeUpper)

def type_index(typee):
    if typee == "" or typee == None:
        return -1
    else:
        typeUpper = typee.upper()
        types = ['HATCHBACK', 'PICKUP', 'SUV', 'SEDAN', 'TRUCK', 'WAGON', 'VAN', 'COUPE', 'CONVERTIBLE', 'OTHER', 'OFFROAD', 'MINI-VAN', 'BUS']
        return types.index(typeUpper)

def color_index(color):
    if color == "" or color == None:
        return -1
    else:
        colorUpper = color.upper()
        colors = ['BLACK', 'WHITE', 'SILVER', 'BROWN', 'BLUE', 'GREY', 'RED', 'CUSTOM', 'PURPLE', 'YELLOW', 'GREEN', 'ORANGE']
        return colors.index(colorUpper)

def state_index(state):
    if state == "" or state == None:
        return -1
    else:
        upper_state = state.upper()
        states = ["AL","AK","AZ","AR","CA","CO","CT","DC","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
        return states.index(upper_state)

def regularize_data(cur_row):
    cur_row[0] = city_index(cur_row[0])# City
    cur_row[1] = price_regularize(cur_row[1])# Price
    cur_row[2] = regularize_year(cur_row[2]) # Change year to number of years old
    cur_row[3] = make_index(cur_row[3]) # Change make of car to number
    cur_row[4] = model_index(cur_row[3], cur_row[4]) # Change model of car to number
    cur_row[5] = condition_index(cur_row[5])# Condition
    cur_row[6] = cylinders_index(cur_row[6])# Cylinders
    cur_row[7] = gas_index(cur_row[7])# Gas type
    cur_row[8] = odometer_regularize(cur_row[8])# Odometer
    cur_row[9] = title_index(cur_row[9])# Title Status
    cur_row[10] = transmission_index(cur_row[10])# Transmission (Manual/Auto)
    cur_row[11] = drive_index(cur_row[11])# Drive (4wd, fwd, rwd)
    cur_row[12] = size_index(cur_row[12])# Size
    cur_row[13] = type_index(cur_row[13])# Type
    cur_row[14] = color_index(cur_row[14])# Color
    cur_row[15] = state_index(cur_row[15]) # State
    return cur_row

def acura(model):
    model = model.upper()
    if "CL" in model:
        return "CL"
    if "CSX" in model:
        return "CSX"
    if "EL" in model:
        return "EL"
    if "ILX" in model:
        return "ILX"
    if "INTEGRA" in model:
        return "INTEGRA"
    if "LEGEND" in model:
        return "LEGEND"
    if "MDX" in model:
        return "MDX"
    if "NSX" in model:
        return "NSX"
    if "RDX" in model:
        return "RDX"
    if "RL" in model:
        return "RL"
    if "RLX" in model:
        return "RLX"
    if "RSX" in model:
        return "RSX"
    if "TL" in model:
        return "TL"
    if "TLX" in model:
        return "TLX"
    if "TSX" in model:
        return "TSX"
    if "ZDX" in model:
        return "ZDX"
    else:
        return "NOTVALID"

def alfa_romeo(model):
    model = model.upper()
    if "159" in model:
        return "159"
    if "164" in model:
        return "164"
    if "4C" in model:
        return "4C"
    if "GIULIA" in model and "QUADRIFOGLIO" in model:
        return "GIULIA QUADRIFOGLIO"
    if "GIULIA" in model:
        return "GIULIA"
    if "GIULIETTA" in model:
        return "GIULIETTA"
    if "GTV6" in model:
        return "GTV6"
    if "GTV" in model:
        return "GTV"
    if "SPIDER" in model or "SPYDER" in model:
        return "SPIDER"
    if "STELVIO" in model:
        return "STELVIO"
    if "SZ" in model:
        return "SZ"
    else:
        return "NOTVALID"

def aston_martin(model):
    model = model.upper()
    dictionary = ["DB11", "DB7 VANTAGE VOLANTE", "DB7 VANTAGE", "DB7", "DB9", "DBS SUPERLEGGARA", "DBS", "RAPIDE S", "RAPIDE", "VANTAGE V12" "VANTAGE V8", "VANTAGE V8 S", "VANQUISH", "VANQUISH S", "VANTAGE S", "VANTAGE"]
    for key in dictionary:
        if key in model:
            return key
    return "NOTVALID"

def audi(model):
    model = model.upper()
    dictionary =["A3 SPORTBACK", "A3 E-TRON", "A3 CABRIOLET", "A3", "A 3", "A-3", "A4 ALLROAD", "ALLROAD", "A4", "A-4", "A 4", "A5 SPORTBACK", "A5 COUPE", "A5", "A6 ALLROAD", "A-6", "A6", "A7 SPORTBACK", "A7", "A8", "A 8", "A-8", "Q8", "Q7", "Q5", "Q3", "QUATTRO", "R8", "RS 3", "RS 4", "RS 5 COUPE", "RS 5 SPORTBACK", "RS 5", "RS 6", "RS 7 SPORTBACK PERFORMANCE", "RS 7 SPORTBACK", "RS 7", "S3 SEDAN", "S3", "S4", "S5 SPORTBACK", "S5 COUPE", "S5", "S6", "S7 SPORTBACK", "S7", "S8 PLUS", "S8", "SQ5", "TTS", "TT RS", "TT"]
    for key in dictionary:
        if key in model:
            if key == "ALLROAD":
                return "A4 ALLROAD"
            if key == "A 4" or "A-4":
                return "A4"
            if key == "A 3" or "A-3":
                return "A3"
            if "A 8" or "A-8":
                return "A8"
            if "A-6":
                return "A6"
            return key
    return "NOTVALID"

def bmw(model):
    title = ""
    if model == "":
        return "NOTVALID"

    model = model.upper()
    series_dictionary = ["1", "2", "3", "4", "5", "6", "7", "8"]
    for key in series_dictionary:
        if model[0].startswith(key):
            title =  key

    other_dictionary = ["X1", "X2", "X3", "X4", "X5", "X6", "Z3", "Z4", "M2 PERFORMANCE", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "I3", "I8", "E3", "E4"]
    for key in other_dictionary:
        if key in model:
            if key == "E3":
                title = "3"
            if key == "E4":
                title = "4"
            title = key

    series_return = ["1", "2", "3", "4", "5", "6", "7", "8", "X1", "X2", "X3", "X4", "X5", "X6", "Z3", "Z4", "M2 PERFORMANCE", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "I3", "I8", "E3", "E4"]
    if title in series_return:
        return series_return.index(title)
    else:
        return "NOTVALID"

def buick(model):
    model = model.upper()
    dictionary = ["APOLLO", "ALLURE", "CASCADA", "CENTURY", "ELECTRA", "ENCLAVE", "ENCORE", "ENVISION", "GRAN SPORT", "GRAND NATIONAL", "LA CROSS", "LACROSS", "LACROSSE", "LASABRE", "LA SABRE", "LE SABRE", "LE SABER", "LESABRE", "LUCERNE", "MCLAUGHLIN", "PARK AVE", "RAINER", "RANIER", "RAINIER", "REATTA", "REGAL", "RENDEZVOUS", "RIVERA", "RIVIERA", "ROADMASTER", "SKYLARK", "SKYHAWK", "SPECIAL", "SUPER", "TERRAZA", "VERANO", "WILDCAT"]
    for key in dictionary:
        if key in model:
            if key == "LACROSSE" or "LA CROSS":
                return "LACROSSE"
            if key == "RIVERA":
                return "RIVERIA"
            if key == "RAINER" or key == "RANIER":
                return "RAINIER"
            if key == "LASABRE" or key == "LA SABRE" or key == "LE SABER" or key == "LESABRE" or key == "LE SABRE":
                return "LESABRE"
            return key

    print(model)
    return "NOTVALID"


def model_index(makeIndex, model):
    if makeIndex == 0:
        return acura(model)
    if makeIndex == 1:
        return alfa_romeo(model)
    if makeIndex == 2:
        return aston_martin(model)
    if makeIndex == 3:
        return audi(model)
    if makeIndex == 4:
        return bmw(model)
    if makeIndex == 5:
        return buick(model)
    else:
        return "Model"

def model_list():
    models = []
    trimmed_models = []
    for i in range(43):
        models.append([])
        trimmed_models.append([])

    with open('vehicles_clean.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            makeIndex = make_index(row[3].upper())
            if makeIndex != -1:
                if row[4] not in models[makeIndex]:
                    models[makeIndex].append(row[4])


def clean_clean_data():
    clean_data = []
    with open('vehicles_clean.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            regular_row = regularize_data(row)
            if regular_row[3] == 4:
                clean_data.append(regular_row)
    return clean_data

def load_data_csv():
    clean_data = []
    with open('vehicles_clean.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            if int(row[4]) > 0:
                cleanrows = cleanrows + 1
                cur_row = [row[2], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[15], row[16], row[17], row[18], row[22]]
                regular_row = regularize_data(cur_row)
                if regular_row[3] == 4:
                    clean_data.append(regular_row)
    return clean_data

def save_csv(clean_data):
    with open('vehicles_cleaner.csv','w') as cleanfile:
        csvwriter = csv.writer(cleanfile)
        for row in clean_data:
            csvwriter.writerow(row)

def main():
    #clean_data = load_data_csv()
    cleaner_data = clean_clean_data()
    save_csv(cleaner_data)
    #model_list()

main()