dic1 = {'Ant':'Semut',
            'Bee':'Lebah',
            'Mosquito':'Nyamuk',
            'Butterfly':'Kupu-kupu',
            'Spider':'Laba-laba',
            'Fly':'Lalat',
            'Hedgehog':'Landak',
            'Snail':'Siput',
            'Cat':'Kucing',
            'Dog':'Anjing'}


start = True
while start:
    score = 0
    for str in dic1:
        print(str+"\n")
        nanya = input("apa jawaban anda: ")
        if nanya == dic1[str]:
            print('BENAR'+'\n')
            score+=1
        else:
            print('SALAH'+'\n')
        
    print(f"score anda adalah , {score}\n")
    ulang = input("ingin mengulang?: ('y/t') ")
    if ulang == 'y':
        continue
    else:
        start = False
