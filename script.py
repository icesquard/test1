per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print(per_cent)
money = int(input("Сумма которую планируете положить под проценты:"))
deposit = list()
TKB = float((per_cent['ТКБ']) * (money/100))
deposit.append(TKB)
SKB = float((per_cent['СКБ']) * (money/100))
deposit.append(SKB)
VTB = float((per_cent['ВТБ']) * (money/100))
deposit.append(VTB)
SBER = float((per_cent['СБЕР']) * (money/100))
deposit.append(SBER)
M = (max(deposit))
print("Максимальная сумма, которую вы можете заработать —", M)










