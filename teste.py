def stringnumerica(text):
  if text != "" and text != "0":
    try:
      float(text)
    except ValueError:
      return 2 #tem letra nessa porra
    return 1 #se a string for numerica
  else:
    return 3 #string vazia ou zero
  

print(stringnumerica("0"))
print(stringnumerica(""))
print(stringnumerica("2313"))
print(stringnumerica("aaa0"))