class Personel:

    def __init__(self, adi, departman, yil, maas):
        self.adi = adi
        self.departman = departman
        self.yil = yil
        self.maas = maas


class Firma:
    personellistesi = []


    def personel_ekle(self, personel):

        self.personellistesi.append(personel)

    def personel_listele(self):
        for personel in self.personellistesi:
            print("ad:",personel.adi,"departman:",personel.departman,"yil:",personel.yil,"maas:",personel.maas)

    def maas_zammi(self,personel,maas_oranı):
        personel.maas*=maas_oranı


    def personel_cikart(self,personel):
        self.personellistesi.remove(personel)

ödev3
