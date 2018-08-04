import sys

def main():
  input_file = sys.argv[1]
  output_file = sys.argv[2]

  # key is drug name
  # value is an array, the first item is drug cost, the second is number of prescribes
  drug_list = dict()

  # dictionary of drug and prescriber
  # key is drug name, value is a set of all prescriber id
  # The purpose of set is to eliminate all duplicate prescribers
  drug_prescriber = dict() 

  with open(input_file, 'r') as f:
    title = f.readline()
    for line in f:
      arr = line.split(',')
      # print(arr)
      prescriber_id = arr[0]
      drug_name = arr[3]
      drug_cost = int(arr[4])

      if drug_name not in drug_list:
        drug_list[drug_name] = [drug_cost, 1]
        drug_prescriber[drug_name] = {prescriber_id}
      # only if the prescriber is not in the set, add cost and prescribe number
      elif prescriber_id not in drug_prescriber[drug_name]:
        drug_list[drug_name][0] += drug_cost
        drug_list[drug_name][1] += 1
        drug_prescriber[drug_name].add(prescriber_id)

  result = []
  for name in drug_list.keys():
    result.append([drug_list[name][0], name, drug_list[name][1]])
  result.sort(reverse=True)

  with open(output_file, 'w') as g:
    g.write('drug_name,num_prescriber,total_cost\n')
    for i in range(len(result)-1):
      item = result[i]
      item = [item[1], str(item[2]), str(item[0])]  
      g.write(','.join(item))
      g.write('\n')
    item = result[-1]
    item = [item[1], str(item[2]), str(item[0])]
    g.write(','.join(item))


if __name__ == '__main__':
  main()
