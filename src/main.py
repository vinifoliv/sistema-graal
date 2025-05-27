from controller.produto_controller import ProdutoController
from controller.venda_controller import VendaController
from database.database import Database
from model.produto_model import ProdutoModel
from model.venda_model import VendaModel
from view.app import App

database = Database()
produto_model = ProdutoModel(database)
venda_model = VendaModel(database)

produto_controller = ProdutoController(produto_model)
venda_controller = VendaController(produto_model, venda_model)

app = App(produto_controller, venda_controller)
app.executar()
