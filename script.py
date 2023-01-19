
# анализтор доходности вклада

myDepo =int(input("введите сумму вклада:"))

print("Ваш вклад",myDepo)

per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}

deposit_TKB=int(myDepo*(per_cent['TKB']/100))

deposit_SKB= int(myDepo*(per_cent['SKB']/100))

deposit_VTB= int(myDepo*(per_cent['VTB']/100))


deposit_SBER = int(myDepo*(per_cent['SBER']/100))

myMoney = []


myMoney.append(deposit_TKB)

myMoney.append(deposit_SKB)

myMoney.append(deposit_VTB)

myMoney.append(deposit_SBER)

print('депозит', myMoney)

# Вторая часть задания
max_deposit=max(myMoney)

print("максимальная сумма которую Вы можете заработать", max_deposit)

