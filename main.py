from database.database import Database
from model.funcionario_model import FuncionarioModel
from model.item_model import ItemModel
from model.produto_model import ProdutoModel
from model.venda_model import VendaModel
from view.app import App

db = Database()
# funcionario_model = FuncionarioModel(db)
# produto_model = ProdutoModel(db)
# item_model = ItemModel(db)
# venda_model = VendaModel(db)

app = App()
app.executar()