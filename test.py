# -*- coding: utf-8 -*-
from app import app
import unittest

class ExampleTest(unittest.TestCase):
   def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_METHODS'] = []  # This is the magic
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        self.app = app.test_client()

class Test(unittest.TestCase):
    def setUp(self):
        # cria uma instância do unittest, precisa do nome "setUp"
        self.app = app.test_client()

        # envia uma requisicao GET para a URL
        self.result = self.app.get('/')

    def test_requisicao(self):
        # compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(self.result.status_code, 200)

    def test_conteudo(self):
        # verifica o retorno do conteudo da pagina
        self.assertEqual(self.result.data.decode('utf-8'), "Oi! eu sou o Leonardo Vinicius e essa é a minha mensagem customizada!")