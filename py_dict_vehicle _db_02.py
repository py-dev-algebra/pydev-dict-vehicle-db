

# DEKLARACIJA / INICIJALIZACIJA
vehicle_db = {
    1: ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45_000.00], # 45.000,00
    2: ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47_000.00],
    3: ['Tegljac', 'MAN', 'RI 001 ZZ', 2018, 78_000.00],
    4: ['Tegljac', 'MAN', 'RI 002 ZZ', 2020, 97_000.00],
    5: ['Kombi', 'Mercedes Benz', 'ST 001 ZZ', 2013, 12_000.00],
    6: ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35_000.00],
    7: ['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9_000.00],
    8: ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9_300.00]
}

# GAVNI DIO PROGRAMA -> MAIN
header_top_line = f'{"ID":<5}{"Tip":<25}{"Proizvodac":<25}{"Registarska":<15}{"Godina":<18}{"Cijena":>15}'
# header_bottom_line = f'{"":<5}{"":<25}{"":<25}{"oznaka":<15}{"prve registracije":<18}{"(EUR)":<15}'
header_bottom_line = f'{"":<5}{"":<25}{"":<25}{"oznaka":<15}{"prve registracije":<18}{"(EUR)":>15}'


print(header_top_line)
print(header_bottom_line)

print('-' * 110)

for key, value in vehicle_db.items():
    print(f'{key:<5}', end='')
    # for item in value:
    #     print(item, end='\t\t')
    print(f'{value[0]:<25}', end='')
    print(f'{value[1]:<25}', end='')
    print(f'{value[2]:<15}', end='')
    print(f'{value[3]:<18}', end='')
    print(f'{value[4]:>15.2f} EUR', end='')
    print()