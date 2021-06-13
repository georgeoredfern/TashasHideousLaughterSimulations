from random import shuffle
from datetime import datetime
import matplotlib.pyplot as plt
from statistics import stdev

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time)

CMCs = [19,25,11,0,0,4,0,0,1]

deckTemplate = []
cmc = 0
for each in CMCs:
    i = 0
    while i < each:
        deckTemplate.append(cmc)
        i+=1
    cmc+=1

MilledCards = []
TotalRuns = 0
while TotalRuns < 100000:
    shuffle(deckTemplate)
    maxNewDeck = len(deckTemplate) + 1 - 10
    NewDeck = deckTemplate[0:maxNewDeck]
    TotalExiled = 0
    while TotalExiled < 20:
        TotalExiled += NewDeck.pop()
    CardsExiled = maxNewDeck - 1 - len(NewDeck)
    MilledCards.append(CardsExiled)
    TotalRuns +=1

print(max(MilledCards))
MilledCount = []
RawMilledCount = []
for each in range(0,max(MilledCards)):
    MilledCount.append(MilledCards.count(each) / TotalRuns)
    RawMilledCount.append(MilledCards.count(each))

plt.plot(RawMilledCount, color='black')
Mean = sum(MilledCards) / len(MilledCards)
stdv = stdev(MilledCards)
twostdvMin = Mean - (2 * stdv)
twostdvMax = Mean + (2 * stdv)
onestvMin = Mean - stdv
onestvMax = Mean + stdv
plt.axvline(Mean, color='g')
#plt.axvline(twostdvMin, color='r')
#plt.axvline(twostdvMax, color='r')
#plt.axvline(onestvMax, color='b')
#plt.axvline(onestvMin, color='b')
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time)
