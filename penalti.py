Nome1= input()
Nome2= input()
gols_nome1=0
gols_nome2=0

Entrada1= str(input())
if (Entrada1=='Gol'):
    gols_nome1=1

Entrada2= str(input())
if (Entrada2=='Gol'):
    gols_nome2=1

Entrada3= str(input())
if (Entrada3=='Gol'):
    gols_nome1=gols_nome1+1

Entrada4= str(input())
if (Entrada4=='Gol'):
    gols_nome2=gols_nome2+1

Entrada5= str(input())
if (Entrada5=='Gol'):
    gols_nome1=gols_nome1+1

Entrada6= str(input())
if (Entrada6=='Gol'):
    gols_nome2=gols_nome2+1

if ((gols_nome1-gols_nome2)==3):
    print(f'{Nome1} vence a disputa de pênaltis por {gols_nome1} a {gols_nome2} e avança de fase!')
elif ((gols_nome2-gols_nome1)==3):
    print(f'{Nome2} vence a disputa de pênaltis por {gols_nome2} a {gols_nome1} e avança de fase!')
else:
    Entrada7 = str(input())
    if (Entrada7 == 'Gol'):
        gols_nome1 = gols_nome1 + 1

    if ((gols_nome1-gols_nome2)==3):
        print(f'{Nome1} vence a disputa de pênaltis por {gols_nome1} a {gols_nome2} e avança de fase!')
    elif ((gols_nome2-gols_nome1)==2):
        print(f'{Nome2} vence a disputa de pênaltis por {gols_nome2} a {gols_nome1} e avança de fase!')
    else:
        Entrada8 = str(input())
        if (Entrada8 == 'Gol'):
            gols_nome2 = gols_nome2 + 1

        if ((gols_nome1-gols_nome2)==2):
            print(f'{Nome1} vence a disputa de pênaltis por {gols_nome1} a {gols_nome2} e avança de fase!')
        elif ((gols_nome2-gols_nome1)==2):
            print(f'{Nome2} vence a disputa de pênaltis por {gols_nome2} a {gols_nome1} e avança de fase!')
        else:
            Entrada9=str(input())
            if (Entrada9=='Gol'):
                gols_nome1=gols_nome1+1

            if ((gols_nome1-gols_nome2)==2):
                print(f'{Nome1} vence a disputa de pênaltis por {gols_nome1} a {gols_nome2} e avança de fase!')
            elif ((gols_nome2-gols_nome1)==1):
                print(f'{Nome2} vence a disputa de pênaltis por {gols_nome2} a {gols_nome1} e avança de fase!')

            else:
                Entrada10=str(input())
                if (Entrada10=='Gol'):
                    gols_nome2=gols_nome2+1

                if ((gols_nome1-gols_nome2)==1):
                    print(f'{Nome1} vence a disputa de pênaltis por {gols_nome1} a {gols_nome2} e avança de fase!')
                elif ((gols_nome2-gols_nome1)==1):
                    print(f'{Nome2} vence a disputa de pênaltis por {gols_nome2} a {gols_nome1} e avança de fase!')
                else:
                    print(f'Ambas as seleções terminaram com {gols_nome1} gols, mas o desempate vai ficar para outro dia.')
