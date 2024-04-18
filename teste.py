def stringnumerica2(text):
  if text != "" and text != "0":
    try:
      float(text)
    except ValueError:
      return 2
    if float(text) > 10 or float(text) < -10:
      print("AAAAAA", text)
      return 3
    return 1 #se a string for numerica
  else:
    return 3 #string vazia ou zero
  

stringnumerica2("0")
stringnumerica2("-20")
stringnumerica2("10")
stringnumerica2("12")
stringnumerica2("-2")
stringnumerica2("1.32")
stringnumerica2("1,32")
