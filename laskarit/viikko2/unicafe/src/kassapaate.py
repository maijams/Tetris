class Kassapaate:
    def __init__(self):
        self.kassassa_rahaa = 100000
        self.edulliset = 0
        self.maukkaat = 0
        self.hinta_edullinen = 240
        self.hinta_maukas = 400

    def syo_edullisesti_kateisella(self, maksu):
        if maksu >= self.hinta_edullinen:
            self.kassassa_rahaa += self.hinta_edullinen
            self.edulliset += 1
            return maksu - self.hinta_edullinen
        else:
            return maksu

    def syo_maukkaasti_kateisella(self, maksu):
        if maksu >= self.hinta_maukas:
            self.kassassa_rahaa += self.hinta_maukas
            self.maukkaat += 1
            return maksu - self.hinta_maukas
        else:
            return maksu

    def syo_edullisesti_kortilla(self, kortti):
        if kortti.saldo >= self.hinta_edullinen:
            kortti.ota_rahaa(self.hinta_edullinen)
            self.edulliset += 1
            return True
        else:
            return False

    def syo_maukkaasti_kortilla(self, kortti):
        if kortti.saldo >= self.hinta_maukas:
            kortti.ota_rahaa(self.hinta_maukas)
            self.maukkaat += 1
            return True
        else:
            return False

    def lataa_rahaa_kortille(self, kortti, summa):
        if summa >= 0:
            kortti.lataa_rahaa(summa)
            self.kassassa_rahaa += summa
        else:
            return
