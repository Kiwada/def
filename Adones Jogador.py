info_jogador = dict()
gols = []  


info_jogador["Nome"] = input(" nome")
info_jogador[" Partidas"] = int(input(" Partidas jogadas"))

for partidas in range(1 , info_jogador[ "partidas"] + 1):
    gol  = int(input(f" Quantos gols feitos na {partidas} partida:"))
    gols.append(gols)  #quando o loop acabar a lista vai conter todos os gols nas partidas
info_jogador[" gols"] = gols


for key , value in info_jogador.items():
    print(f"{key.title()}: {value}")
    #if key != "gols":
        #print(f"{key.title()}: {value}")
    #else:
        #print(key.title() , end = " :")
    #for g in info_jogador["gols"]:
        #print(g , end = " ," if info_jogador["gols"].index(g)!= len(info_jogador)["gols"] else ".")

 

