import unittest
from src.app import adicionar, listar, remover

class TestApp(unittest.TestCase):

    def test_adicionar(self):
        adicionar("Teste", "10:00")
        meds = listar()
        self.assertTrue(any(m["nome"] == "Teste" for m in meds))

    def test_remover(self):
        adicionar("Remover", "12:00")
        remover("Remover")
        meds = listar()
        self.assertFalse(any(m["nome"] == "Remover" for m in meds))

    def test_lista_nao_vazia(self):
        adicionar("X", "08:00")
        meds = listar()
        self.assertGreater(len(meds), 0)

if __name__ == "__main__":
    unittest.main()
