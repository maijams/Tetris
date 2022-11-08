import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        
    # Alustus kunnossa
    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)
            
    def test_kassan_saldo_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_edulliset_myydyt_lounaat_alussa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_maukkaat_myydyt_lounaat_alussa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    
    # Käteisosto edulliset lounaat    
    def test_kateisosto_edullinen_kun_maksu_riittaa_niin_kassan_saldo_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        
    def test_kateisosto_edullinen_kun_maksu_riittaa_niin_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)
        
    def test_kateisosto_edullinen_kun_maksu_riittaa_niin_myydyt_edulliset_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_kateisosto_edullinen_kun_maksu_ei_riita_niin_kassan_saldo_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_kateisosto_edullinen_kun_maksu_ei_riita_niin_palauta_maksu(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)
        
    def test_kateisosto_edullinen_kun_maksu_ei_riita_niin_myydyt_edulliset_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    
    # Käteisosto maukkaat lounaat    
    def test_kateisosto_maukas_kun_maksu_riittaa_niin_kassan_saldo_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        
    def test_kateisosto_maukas_kun_maksu_riittaa_niin_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        
    def test_kateisosto_maukas_kun_maksu_riittaa_niin_myydyt_maukkaat_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kateisosto_maukas_kun_maksu_ei_riita_niin_kassan_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_kateisosto_maukas_kun_maksu_ei_riita_niin_palauta_maksu(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)
        
    def test_kateisosto_maukas_kun_maksu_ei_riita_niin_myydyt_maukkaat_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    
    # Korttiosto edulliset lounaat    
    def test_korttisosto_edullinen_kun_maksu_riittaa_niin_kortin_saldo_oikein(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 260)
        
    def test_korttisosto_edullinen_maksu_riittaa_palauttaa_true(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(Maksukortti(500)))
              
    def test_korttisosto_edullinen_kun_maksu_riittaa_niin_myydyt_edulliset_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(500))
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_korttisosto_edullinen_kun_maksu_riittaa_niin_kassan_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(500))
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_korttisosto_edullinen_kun_maksu_ei_riita_niin_kortin_saldo_ei_muutu(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)
        
    def test_korttisosto_edullinen_maksu_ei_riita_palauttaa_false(self):
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(Maksukortti(100)))
        
    def test_korttisosto_edullinen_kun_maksu_ei_riita_niin_myydyt_edulliset_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(100))
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    
    # Korttiosto maukkaat lounaat    
    def test_korttisosto_maukas_kun_maksu_riittaa_niin_kortin_saldo_oikein(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)
        
    def test_korttisosto_maukas_maksu_riittaa_palauttaa_true(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(500)))
              
    def test_korttisosto_maukas_kun_maksu_riittaa_niin_myydyt_edulliset_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(500))
        self.assertEqual(self.kassapaate.maukkaat, 1)
        
    def test_korttisosto_maukas_kun_maksu_riittaa_niin_kassan_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(500))
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_korttisosto_maukas_kun_maksu_ei_riita_niin_kortin_saldo_ei_muutu(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)
        
    def test_korttisosto_maukas_maksu_ei_riita_palauttaa_false(self):
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(100)))
        
    def test_korttisosto_maukas_kun_maksu_ei_riita_niin_myydyt_edulliset_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(100))
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    
    # Rahan lataus kortille
    def test_rahan_lataus_kortille_ei_toimi_jos_lataussumma_negatiivinen(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(kortti, -1000), None)
    
    def test_kortille_rahaa_ladattaessa_kortin_saldo_kasvaa(self):
        kortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(kortti, 1000)
        self.assertEqual(kortti.saldo, 1500)
        
    def test_kortille_rahaa_ladattaessa_kassan_saldo_kasvaa(self):
        kortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(kortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)