KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti
            self.kasvatuskoko = kasvatuskoko

        self.luku_jono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        
        for i in range(self.alkioiden_lkm):
            if n == self.luku_jono[i]:
                return True
        

        return False

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.luku_jono[0] = n
            self.alkioiden_lkm += 1

        elif not self.kuuluu(n):
            self.luku_jono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            #if self.alkioiden_lkm % len(self.luku_jono) == 0:
            if self.alkioiden_lkm >= len(self.luku_jono):
                
                taulukko_old = self.luku_jono
                self.kopioi_lista(self.luku_jono, self.luku_jono)
                self.luku_jono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.luku_jono)

        else:
            return False

        return True

    def poista(self, n):

        for i in range(self.alkioiden_lkm):

            if n == self.luku_jono[i]:
                self.luku_jono[i] = 0

                for j in range(i, self.alkioiden_lkm - 1):
                    apu = self.luku_jono[j]
                    self.luku_jono[j] = self.luku_jono[j + 1]
                    self.luku_jono[j + 1] = apu

                self.alkioiden_lkm -= 1
                return True

        return False

    def kopioi_lista(self, a, b):
        for i in range(len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(len(taulu)):
            taulu[i] = self.luku_jono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(len(a_taulu)):
            yhdiste.lisaa(a_taulu[i])

        for i in range(len(b_taulu)):
            yhdiste.lisaa(b_taulu[i])

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(len(a_taulu)):
            for j in range(len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkaus.lisaa(b_taulu[j])

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(len(a_taulu)):
            erotus.lisaa(a_taulu[i])

        for i in range(len(b_taulu)):
            erotus.poista(b_taulu[i])

        return erotus

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"

        else:
            tuotos = "{"
            for i in range(self.alkioiden_lkm - 1):
                tuotos += str(self.luku_jono[i])
                tuotos += ", "
            tuotos += str(self.luku_jono[self.alkioiden_lkm - 1])
            tuotos += "}"
            return tuotos
