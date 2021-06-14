from random import shuffle
from datetime import datetime
import matplotlib.pyplot as plt
from statistics import stdev

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time)

CMCs = [18,26,8,1,0,4,0,3]

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
while TotalRuns < 1000000:
    shuffle(deckTemplate)
    maxNewDeck = len(deckTemplate) + 1 - 10
    NewDeck = deckTemplate[0:maxNewDeck]
    TotalExiled = 0
    while TotalExiled < 20:
        TotalExiled += NewDeck.pop()
    CardsExiled = maxNewDeck - len(NewDeck)
    MilledCards.append(CardsExiled)
    TotalRuns +=1

print(max(MilledCards))
MilledCount = []
RawMilledCount = []
Mode = 0
ModeCount = 0
for each in range(0,max(MilledCards)+1):
    MilledCount.append(MilledCards.count(each) / TotalRuns)
    RawMilledCount.append(MilledCards.count(each))
    if MilledCards.count(each) > ModeCount:
        Mode = each
        ModeCount = MilledCards.count(each)
print('Modal cards milled: ' + str(Mode))

plt.plot(MilledCount, color='black')
Mean = sum(MilledCards) / len(MilledCards)
print('Average cards milled: ' + str(Mean))
plt.axvline(Mean, color='g')

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time)
