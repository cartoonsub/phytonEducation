from simplecrypt import encrypt, decrypt
passwords = []
with open('C:/phytonProjects/phytonEducation/firstStep/part2/static/passwords.txt', 'r') as file:
    for line in file:
        dataLine = line.strip().split('\t')
        passwords.append(dataLine[0])
print(passwords)

with open("C:/phytonProjects/phytonEducation/firstStep/part2/static/encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    for x in passwords:
      print(x)
      try:
        print(decrypt(x, encrypted).decode("utf-8"))
      except:
          continue
