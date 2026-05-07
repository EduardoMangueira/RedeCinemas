from controller.Public_controller import UserController
from view.Menu_view import UserView

class CinemaApp:
    def __init__(self):
        # O App conecta a View ao Controller
        self.view = UserView()
        self.controller = UserController()

    def executar(self):
        while True:
            opcao = self.view.exibir_menu()

            if opcao == "1":
                id_s, qtd = self.view.obter_dados_registro()
                # O App pede ao controller para processar
                resultado = self.controller.cadastrar_publico_sessao(id_s, qtd)
                self.view.mostrar_mensagem(resultado)
            
            elif opcao == "2":
                print("Encerrando o sistema...")
                break
            else:
                print("Opção inválida!")