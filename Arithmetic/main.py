import math
from decimal import Decimal
s = input("Enter data :")
n = input("Enter number of letters :")
frequency_table = {}
print("Enter letter and his code: ")
total_frequency=0
for i in range (int(n)) :
     b = input()
     l = input()
     frequency_table[str(b)] = l
     total_frequency+=int(l)
# frequency_table = {"a": 80, "b": 2, "c": 18}
msg=s
bits=[]

# total_frequency = sum(list(frequency_table.values()))
minprob=1
probability_table = {}
for key, value in frequency_table.items():
     probability_table[key] = int(value) / total_frequency
     minprob = min(minprob, int(value)/total_frequency)

# print(probability_table)
# print(minprob)
smallestRequiredBits=math.ceil(math.log2(1/minprob))
print(smallestRequiredBits)
def scalling(stage_min,stage_max):
    if (stage_min < 0.5 and stage_max < 0.5):
        while (stage_max < 0.5):
            stage_min = stage_min * 2
            stage_max = stage_max * 2
            bits.append(0)
    if (stage_min > 0.5 and stage_max > 0.5):
        while (stage_min > 0.5):
            stage_min = (stage_min - Decimal(0.5)) * 2
            stage_max = (stage_max - Decimal(0.5)) * 2
            bits.append(1)
    if (stage_min < 0.5 and stage_max < 0.5):
        while (stage_max < 0.5):
            stage_min = stage_min * 2
            stage_max = stage_max * 2
            bits.append(0)
    if (stage_min > 0.5 and stage_max > 0.5):
        while (stage_min > 0.5):
            stage_min = (stage_min - Decimal(0.5)) * 2
            stage_max = (stage_max - Decimal(0.5)) * 2
            bits.append(1)
    return stage_min,stage_max

def get_encoded_value( encoder):

     last_stage = list(encoder[-1].values())
     last_stage_values = []
     for sublist in last_stage:
          for element in sublist:
               last_stage_values.append(element)

     last_stage_min = min(last_stage_values)
     last_stage_max = max(last_stage_values)

     return (last_stage_min + last_stage_max) / 2
def process_stage( probability_table, stage_min, stage_max):

     stage_probs = {}
     stage_domain = stage_max - stage_min
     for term_idx in range(len(probability_table.items())):
          term = list(probability_table.keys())[term_idx]
          term_prob = Decimal(probability_table[term])
          cum_prob = term_prob * stage_domain + stage_min
          stage_probs[term] = [stage_min, cum_prob]
          stage_min = cum_prob
     return stage_probs


def encode( msg, probability_table):


     encoder = []

     stage_min = Decimal(0.0)
     stage_max = Decimal(1.0)

     for msg_term_idx in range(len(msg)):
          stage_probs = process_stage(probability_table, stage_min, stage_max)

          msg_term = msg[msg_term_idx]
          stage_min = stage_probs[msg_term][0]
          stage_max = stage_probs[msg_term][1]
          stage_min,stage_max=scalling(stage_min,stage_max)
          encoder.append(stage_probs)

     stage_probs = process_stage(probability_table, stage_min, stage_max)
     encoder.append(stage_probs)

     encoded_msg = get_encoded_value(encoder)

     return encoder, encoded_msg


l,m=encode(msg,probability_table)
print(m)
bits.append(1)
for i in range (smallestRequiredBits-1):
     bits.append(0)

print(bits)


