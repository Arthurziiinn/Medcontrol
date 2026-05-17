import unittest
import requests

from app import adicionar
from app import listar
from app import remover


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

    def test_api(self):
        url = "http://worldtimeapi.org/api/timezone/America/Sao_Paulo"

        resposta = requests.get(url)

        self.assertEqual(resposta.status_code, 200)


if __name__ == "__main__":
    unittest.main()
