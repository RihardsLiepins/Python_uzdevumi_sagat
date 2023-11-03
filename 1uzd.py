"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

1) Kādus ciparus Jūs ziniet? 0,1,2,3,4,5,6,7,8,9
2) Kādus romiešu ciparus jūs ziniet? I,V,C,M,X,L,D
3) kas ir klase? Programmēšanas struktūra kas var definēt datu uzvedību un metodes.
4) Klase sastāv no konstruktora/destruktora un metodēm (iekšējām funkcijām).
5) kādas datu struktūras ziniet? -list(saraksts) -arry(masīvs) -dict(vārdnīca)
"""
class AAA:
    # jādefinē kosntruktors
    def __init__(self):
        self.roma_sk={ 
            1: 'I',
            4: 'IV',
            5: 'V', 
            9: 'IX', 
            10: 'X', 
            40: 'XL', 
            50: 'L', 
            90: 'XC', 
            100: 'C', 
            400: 'CD', 
            500: 'D', 
            900: 'CM', 
            1000: 'M'
        }
    def to_roman(self, num): 
        result = "" 
        for value, numeral in sorted(self.roma_sk.items(), key=lambda x: x[0], reverse=True): 
            while num >= value: 
                result += numeral 
                num -= value  #num=num-value
        return result

# piemērs
skaitlis=2023
#definējam objektu
kk=AAA()
# jaunajam objekta jāizsauc klases metode
romieshu=kk.to_roman(skaitlis)

#noformēt izdruku
print(f"{skaitlis} ar romiešu cipariem ir {romieshu}")