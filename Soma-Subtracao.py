p = str(
    input(
        "Se deseja\033[1;31m SOMAR\033[m digite \033[1;31mS\033[m e se deseja\033[1;34m SUBTRAIR\033[m digite\033[1;34m SB\033[m: "
    ))
if p != 'S' and p != 'SB':
  print("Só posso subtrair e somar")

if p == 'S':
  n1 = int(input("Digite o primeiro número: "))
  n2 = int(input("Digite o segundo número: "))
  s = n1 + n2
  print(f"\033[1;31m A soma entre {n1} e {n2} é igual a {s} \033[m")
if p == "SB":
  n1 = int(input("Digite o primeiro número: "))
  n2 = int(input("Digite o segundo número: "))
  s = n1 - n2
  print(f"\033[1;34m A subtração entre {n1} e {n2} é igual a {s} \033[m")
