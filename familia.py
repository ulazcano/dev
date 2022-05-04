import webbrowser

class familia:
    

    #Constructor
    def __init__(self,mama,papa,hijos,casa=""):
        self.mama = mama
        self.papa = papa
        self.hijos=hijos
        self.casa=casa

    def getnuevohijo(self,nombre,edad):
        self.hijos.append((nombre,edad))

    def getnuevacasa(self,comuna,barrio="",calle="",numero=""):
        self.casa=[comuna,barrio,calle,numero]
        new=2
        url = "https://www.google.cl/maps/place/"+comuna+"+"+numero+"+"+calle+"+"+"chile"
        webbrowser.open(url,new=new)

    def 



monos = familia("Ale","Uli",[("Mateo",10),("Seba",7),("Santi",4)])

print(monos.hijos)
monos.getnuevohijo("Nohemoselegidoaun",5)
print(monos.hijos)
monos.getnuevacasa("ñuñoa","ñuñoa norte","pedro torres","123")
print(monos.casa)







