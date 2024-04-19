import math
from decimal import Decimal
finalResult=""
# frequency_table = {"a": 80, "b": 2, "c": 18}
# bits=[1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
# k=6
# total_frequency = sum(list(frequency_table.values()))
# minprob=1
# probability_table = {}
# for key, value in frequency_table.items():
#      probability_table[key] = value / total_frequency
#      minprob = min(minprob, value/total_frequency)
s = input("Enter data :")
n = input("Enter number of letters : ")
frequency_table = {}
print("Enter letter and his frequency: ")
total_frequency=0
for i in range (int(n)) :
    b = input()
    l = input()
    frequency_table[str(b)] = l
    total_frequency+=int(l)
# frequency_table = {"a": 80, "b": 2, "c": 18}
msg=s
bits=[]
k=int(input("Enter smallest number of bits required to (0.5) (k) :"))
for c in s:
    bits.append(int(c))
# total_frequency = sum(list(frequency_table.values()))
length=len(bits)
minprob=1
probability_table = {}
for key, value in frequency_table.items():
     probability_table[key] = int(value) / total_frequency
     minprob = min(minprob, int(value)/total_frequency)

sum=0
m=1
i=k-1;
while(i>=0):
    if bits[i]==1:
        sum += m
    m *=2
    i-=1
code = Decimal(0.0)
code = sum/pow(2,k)

stage_min=Decimal(0.0)
stage_max=Decimal(1.0)
def process_stage(probability_table, stage_min, stage_max):
    stage_probs = {}
    stage_domain = stage_max - stage_min
    for term_idx in range(len(probability_table.items())):
        term = list(probability_table.keys())[term_idx]
        term_prob = Decimal(probability_table[term])
        cum_prob = term_prob * stage_domain + stage_min
        stage_probs[term] = [stage_min, cum_prob]
        stage_min = cum_prob
    return stage_probs

dic=process_stage(probability_table,stage_min,stage_max)
def get_symbol(code):
    res=""
    for key,value in dic.items():
        if value[0]<= code <=value[1]:
            res=key
            break
    return res

c=get_symbol(code)
stage_probs = process_stage(probability_table, stage_min, stage_max)
stage_min = stage_probs[c][0]
stage_max = stage_probs[c][1]
finalResult+=c
def scalling(stage_min,stage_max):
    if (stage_min < 0.5 and stage_max < 0.5):
        while (stage_max < 0.5):
            stage_min = stage_min * 2
            stage_max = stage_max * 2
            bits.pop(0)
    if (stage_min > 0.5 and stage_max > 0.5):
        while (stage_min > 0.5):
            stage_min = (stage_min - Decimal(0.5)) * 2
            stage_max = (stage_max - Decimal(0.5)) * 2
            bits.pop(0)
    if (stage_min < 0.5 and stage_max < 0.5):
        while (stage_max < 0.5):
            stage_min = stage_min * 2
            stage_max = stage_max * 2
            bits.pop(0)
    if (stage_min > 0.5 and stage_max > 0.5):
        while (stage_min > 0.5):
            stage_min = (stage_min - Decimal(0.5)) * 2
            stage_max = (stage_max - Decimal(0.5)) * 2
            bits.pop(0)
    return stage_min,stage_max
while(len(bits)>k):
     if length==len(bits):
         code=Decimal(Decimal(Decimal(code)-Decimal(stage_min))/Decimal(Decimal(stage_max)-Decimal(stage_min)))
     else:
         sum = 0
         m = 1
         i = k - 1
         while (i >= 0):
             if bits[i] == 1:
                 sum += m
             m *= 2
             i -= 1
         code = Decimal(0.0)
         code = sum / pow(2, k)
         code=Decimal(Decimal(Decimal(code)-Decimal(stage_min))/Decimal(Decimal(stage_max)-Decimal(stage_min)))
         length=len(bits)
     c=get_symbol(code)
     finalResult+=c
     stage_probs = process_stage(probability_table, stage_min, stage_max)
     stage_min = stage_probs[c][0]
     stage_max = stage_probs[c][1]
     stage_min,stage_max=scalling(stage_min,stage_max)

code = 0.5
code=Decimal(Decimal(Decimal(code)-Decimal(stage_min))/Decimal(Decimal(stage_max)-Decimal(stage_min)))
c=get_symbol(code)
finalResult+=c
print(finalResult)
# 110001100000