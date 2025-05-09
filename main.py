from controller.produto_controller import ProdutoController
from database.database import Database
from model.funcionario_model import FuncionarioModel
from model.item_model import ItemModel
from model.produto_model import ProdutoModel
from model.venda_model import VendaModel
from view.app import App

database = Database()
produto_model = ProdutoModel(database)
# funcionario_model = FuncionarioModel(db)
# item_model = ItemModel(db)
# venda_model = VendaModel(db)

produto_controller = ProdutoController(produto_model)

app = App(produto_controller)
app.executar()
