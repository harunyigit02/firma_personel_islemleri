from firma import Personel
from firma import Firma
a=Personel("harun","muhendis",211,20000)
b=Personel("asd","sdfsdf",222,500000)
firma=Firma()
firma.personel_ekle(a)
firma.personel_ekle(b)
firma.personel_listele()
firma.maas_zammi(a,2)
firma.personel_cikart(b)
firma.personel_listele()
