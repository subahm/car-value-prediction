from sklearn.model_selection import train_test_split
import random
import numpy as np  # linear algebra
import pandas as pd  # data processing / input output file operations
import os


def get_splits(csv_path, split):

    col_data = "dunno,price,year,odometer,manufacturer_acura,manufacturer_alfa-romeo,manufacturer_aston-martin,manufacturer_audi,manufacturer_bmw,manufacturer_buick,manufacturer_cadillac,manufacturer_chevrolet,manufacturer_chrysler,manufacturer_datsun,manufacturer_dodge,manufacturer_ferrari,manufacturer_fiat,manufacturer_ford,manufacturer_gmc,manufacturer_honda,manufacturer_hyundai,manufacturer_infiniti,manufacturer_jaguar,manufacturer_jeep,manufacturer_kia,manufacturer_land rover,manufacturer_lexus,manufacturer_lincoln,manufacturer_mazda,manufacturer_mercedes-benz,manufacturer_mercury,manufacturer_mini,manufacturer_mitsubishi,manufacturer_nissan,manufacturer_pontiac,manufacturer_porche,manufacturer_ram,manufacturer_saturn,manufacturer_subaru,manufacturer_tesla,manufacturer_toyota,manufacturer_volkswagen,manufacturer_volvo,model_1 Ton,model_100,model_150,model_1500,model_1500 CLASSIC,model_164,model_20,model_200,model_200S,model_210,model_240Z,model_250,model_2500,model_2500 HD,model_280Z,model_300,model_300SRT8,model_308,model_3100,model_348,model_350,model_3500,model_350Z,model_360,model_370Z,model_370Z ROADSTER,model_4500,model_456,model_458 Italia,model_458 Spider,model_488,model_4C,model_4RUNNER,model_500,model_500 Abarth,model_500E,model_500L,model_500X,model_512,model_550,model_5500,model_600,model_626,model_86,model_911,model_A-CLASS,model_A3,model_A4,model_A5,model_A6,model_A7,model_A8,model_ALLANTE,model_ALLURE,model_ALTIMA,model_AMG GT,model_APOLLO,model_ARMADA,model_ASCENT,model_ASTRA,model_ATS,model_AURA,model_AVALON,model_Acadia,model_Acadia Denali,model_Accent,model_Accord,model_Accord Coupe,model_Accord Crosstour,model_Accord Hybrid,model_Accord Sedan,model_Accord Wagon,model_Amanti,model_Apache,model_Arteon,model_Aspen,model_Astro,model_Atlas,model_Avalanche,model_Avenger,model_Aveo,model_Aviator,model_Azera,model_B-CLASS,model_B-SERIES,model_B2300,model_B9 TRIBECA,model_BAJA,model_BONNEVILLE,model_BRZ,model_Beetle,model_Bel Air,model_Biscayne,model_Blazer,model_Bolt EV,model_Borrego,model_Bronco,model_Brougham,model_C-CLASS,model_C-HR,model_C-Max,model_C/K 2500,model_C10,model_C30,model_C70,model_CAMRY,model_CAMRY HYBRID,model_CAMRY SOLORA,model_CARGO VAN,model_CASCADA,model_CAYENNE,model_CC,model_CELICA,model_CENTURY,model_CJ,model_CJ-5,model_CJ-7,model_CL,model_CL-CLASS,model_CLA-CLASS,model_CLK-CLASS,model_CLS-CLASS,model_CLUBMAN,model_CONVERTIBLE,model_COOPER,model_COROLLA,model_COROLLA HATCHBACK,model_COROLLA IM,model_COUGAR,model_COUNTRYMAN,model_COUPE,model_CR-V,model_CR-Z,model_CROSS,model_CROSSTREK,model_CT,model_CT6,model_CTS,model_CUBE,model_CX-3,model_CX-5,model_CX-7,model_CX-9,model_Cabrio,model_Cadenza,model_Caliber,model_California,model_Camaro,model_Canyon,model_Caprice,model_Captiva,model_Caravan,model_Cavalier,model_Challenger,model_Charger,model_Chateau,model_Cherokee,model_Chevelle,model_Chevette,model_Cheyenne,model_Cirrus,model_City Express,model_Civic,model_Civic Coupe,model_Civic Hatchback,model_Civic Sedan,model_Civic Type R,model_Civic del Sol,model_Clarity Plug-In Hybrid,model_Club Wagon,model_Cobalt,model_Cobra,model_Colorado,model_Commander,model_Compass,model_Concorde,model_Continental,model_Contour,model_Cordoba,model_Coronet,model_Corsica,model_Corvair,model_Corvette,model_Coupe DeVille,model_Crossfire,model_Crosstour,model_Crown Victoria,model_Cruze,model_DAKOTA,model_DB7,model_DB9,model_DIAMANTE,model_DTS,model_Dakota,model_Dart,model_Daytona,model_DeVille,model_Delray,model_Deluxe,model_Denali,model_Discovery,model_Discovery Sport,model_Durango,model_E-450,model_E-CLASS,model_E-Golf,model_E-Series,model_E3,model_E4,model_ECHO,model_ECLIPSE,model_ECLIPSE CROSS,model_EL,model_ELECTRA,model_ELR,model_ENCLAVE,model_ENCORE,model_ENDEAVOR,model_ENVISION,model_ES,model_EX,model_EcoSport,model_Econoline/Club Wagon,model_Edge,model_El Camino,model_Elantra,model_Elantra Coupe,model_Elantra GT,model_Elantra Touring,model_Eldorado,model_Element,model_Entourage,model_Envoy,model_Eos,model_Equinox,model_Equus,model_Escalade,model_Escalade ESV,model_Escalade EXT,model_Escape,model_Escort,model_Eurovan,model_Excursion,model_Expedition,model_Explorer,model_F-100,model_F-150,model_F-250,model_F-250 HD,model_F-350,model_F-Pace,model_F-Type,model_F430,model_F430 Spider,model_FF,model_FIREBIRD,model_FJ CRUISER,model_FORESTER,model_FRONTIER,model_FX,model_Fairlane,model_Falcon,model_Fiesta,model_Fit,model_Five Hundred,model_Fleetwood,model_Flex,model_Focus,model_Forte,model_Forte 5-Door,model_Forte Koup,model_Forte5,model_Freestar,model_Freestyle,model_Fusion,model_G,model_G-CLASS,model_G3,model_G3 WAVE,model_G5,model_G6,model_G8,model_GALANT,model_GIULIA,model_GL-CLASS,model_GLA-CLASS,model_GLC,model_GLC-CLASS,model_GLE-CLASS,model_GLI,model_GLK-CLASS,model_GLS,model_GR SUPRA,model_GRAND AM,model_GRAND MARQUIS,model_GRAND NATIONAL,model_GRAND PRIX,model_GS,model_GS F,model_GT,model_GT-R,model_GTI,model_GTV,model_GX,model_Galaxie,model_Genesis,model_Genesis Coupe,model_Gladiator,model_Golf,model_Golf Alltrack,model_Golf R,model_Golf SportWagen,model_Golf Wagon,model_Grand Caravan,model_Grand Cherokee,model_Grand Marquis,model_HARDTOP,model_HHR,model_HIGHLANDER,model_HIGHLANDER HYBRID,model_HR-V,model_HS,model_I,model_I-MIEV,model_I3,model_I8,model_ILX,model_IMPREZA,model_IMPREZA WRX,model_INTEGRA,model_ION,model_IS,model_IS 200t,model_IS C,model_IS F,model_Impala,model_Imperial,model_Insight,model_Intrepid,model_Ioniq,model_Ioniq Electric,model_Ioniq Hybrid,model_JUKE,model_JX35,model_Jetta,model_Jimmy,model_Journey,model_K10 Blazer,model_K900,model_KICKS,model_Kona,model_Kona Electric,model_L SERIES SEDAN,model_L SERIES WAGON,model_LANCER,model_LANCER EVOLUTION,model_LANCER SPORTBACK,model_LC,model_LCF,model_LEAF,model_LEGACY,model_LEGEND,model_LR2,model_LR3,model_LS,model_LTD,model_LUCERNE,model_LW,model_LX,model_LeBaron,model_Liberty,model_Limousine,model_Lumina,model_M,model_M-CLASS,model_M2,model_M3,model_M35h,model_M4,model_M5,model_M56x,model_M6,model_M7,model_MARAUDER,model_MATRIX,model_MAXIMA,model_MAZDA2,model_MAZDA3,model_MAZDA3 SPORT,model_MAZDA5,model_MAZDA6,model_MDX,model_METRIS CARGO VAN,model_METRIS PASSENGER VAN,model_MILLENIA,model_MIRAGE,model_MIRAI,model_MKC,model_MKS,model_MKT,model_MKX,model_MKZ,model_MODEL 3,model_MODEL S,model_MODEL X,model_MONTANA,model_MONTANA SV6,model_MONTERO,model_MONTERO SPORT,model_MPV,model_MURANO,model_MX-5,model_MX-5 RF,model_Magentis,model_Magnum,model_Malibu,model_Mark IV,model_Mark LT,model_Mark V,model_Mark VI,model_Mark VIII,model_Master,model_Model A,model_Model T,model_Mondial,model_Monte Carlo,model_Mustang,model_NSX,model_NV,model_NV CARGO,model_NV200,model_NX,model_NX 300,model_Nautilus,model_Navigator,model_Neon,model_New Yorker,model_Newport,model_Niro,model_Niro Plug-In Hybrid,model_Nitro,model_Nova,model_OUTBACK,model_OUTLANDER,model_OUTLANDER PHEV,model_OUTLOOK,model_Odyssey,model_Optima,model_Optima Hybrid,model_PACEMAN,model_PARK AVE,model_PATHFINDER,model_PATHFINDER ARMADA,model_PRIUS,model_PRIUS C,model_PRIUS PLUG-IN,model_PRIUS PRIME,model_PRIUS V,model_PROMASTER,model_PROMASTER CARGO VAN,model_PROMASTER CITY,model_PROMASTER CITY WAGON,model_PROTEGE,model_PROTEGE5,model_PT Cruiser,model_PURSUIT,model_Pacifica,model_Passat,model_Passport,model_Patriot,model_Phaeton,model_Pilot,model_Polara,model_Police Interceptor,model_Prelude,model_Prowler,model_Q3,model_Q5,model_Q50,model_Q60,model_Q7,model_Q70,model_Q70L,model_Q8,model_QUATTRO,model_QUEST,model_QX,model_QX30,model_QX50,model_QX56,model_QX60,model_QX70,model_QX80,model_R-CLASS,model_R8,model_RAINER,model_RAINIER,model_RANIER,model_RAPIDE,model_RAPIDE S,model_RAV4,model_RAV4 HYBRID,model_RC,model_RC 350,model_RC F,model_RDX,model_REATTA,model_REGAL,model_RELAY,model_RENDEZVOUS,model_RIVERA,model_RIVIERA,model_RL,model_RLX,model_ROADMASTER,model_ROADSTER,model_ROGUE,model_RS 3,model_RS 4,model_RS 5,model_RS 6,model_RS 7,model_RSX,model_RX,model_RX 350L,model_RX-8,model_Rabbit,model_Ranchero,model_Ranger,model_Renegade,model_Ridgeline,model_Rio,model_Rio5,model_Rondo,model_Routan,model_S-CLASS,model_S-Type,model_S10,model_S2000,model_S3,model_S4,model_S40,model_S5,model_S6,model_S60,model_S60 Cross"
    
    
    columns = col_data.split(",")

    # drop these columns
    features = columns[:]
    features.remove("dunno")
    features.remove("price")

    if not os.path.isfile(csv_path):
        print("csv {} not found.".format(csv_path))
        return None
    
    print("starting to read csv...")
    data = pd.read_csv(csv_path, names=columns, delimiter=',', error_bad_lines=False, dtype='unicode')
    print("finished reading csv.")

    Z = data[columns]
    # print(Z)

    X = Z[features]
    Y = Z.price

    data_dict = {}
    print("splitting data into training and testing sets.")
    data_dict['X_train'], data_dict['X_test'], data_dict['Y_train'],  data_dict['Y_test'] = train_test_split(X, Y, test_size=split)
    return data_dict