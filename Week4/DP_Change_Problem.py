def DPChange(money, coins):
    minimumNumberCoins=dict()
    minimumNumberCoins[0]=0
    for m in range (1,money+1):
        minimumNumberCoins[m]=float('inf')
        for i in range (len(coins)):
            if (m>= coins[i]):
                if (minimumNumberCoins[m-coins[i]]+1)<minimumNumberCoins[m]:
                    minimumNumberCoins[m]=minimumNumberCoins[m-coins[i]]+1
    return minimumNumberCoins[money]

print(DPChange(18,[1,4,5]))