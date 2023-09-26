# A interface de um serviço remoto.
class ThirdPartyYouTubeLib:
    def list_videos(self):
        pass

    def get_video_info(self, id):
        pass

    def download_video(self, id):
        pass

# A implementação concreta de um serviço conector. Métodos
# dessa classe podem pedir informações do YouTube. A velocidade
# do pedido depende da conexão do usuário com a internet, bem
# como do YouTube. A aplicação irá ficar lenta se muitos
# pedidos forem feitos ao mesmo tempo, mesmo que todos peçam a
# mesma informação.
class ThirdPartyYouTubeClass(ThirdPartyYouTubeLib):
    def list_videos(self):
        # Envia um pedido API para o YouTube.
        pass

    def get_video_info(self, id):
        # Obtém metadados sobre algum vídeo.
        pass

    def download_video(self, id):
        # Baixa um arquivo de vídeo do YouTube.
        pass

# Para salvar largura de banda, nós podemos colocar os
# resultados do pedido em cache e mantê-los por determinado
# tempo. Mas pode ser impossível colocar tal código diretamente
# na classe de serviço. Por exemplo, ele pode ter sido
# fornecido como parte de uma biblioteca de terceiros e/ou
# definida como `final`. É por isso que nós colocamos o código
# do cache em uma nova classe proxy que implementa a mesma
# interface que a classe de serviço. Ela delega ao objeto do
# serviço somente quando os pedidos reais foram enviados.
class CachedYouTubeClass(ThirdPartyYouTubeLib):
    def __init__(self, service: ThirdPartyYouTubeLib):
        self.service = service
        self.list_cache = None
        self.video_cache = None
        self.need_reset = False

    def list_videos(self):
        if self.list_cache is None or self.need_reset:
            self.list_cache = self.service.list_videos()
        return self.list_cache

    def get_video_info(self, id):
        if self.video_cache is None or self.need_reset:
            self.video_cache = self.service.get_video_info(id)
        return self.video_cache

    def download_video(self, id):
        if not self.download_exists(id) or self.need_reset:
            return self.service.download_video(id)

    def download_exists(self, id):
        return True

# A classe GUI, que é usada para trabalhar diretamente com um
# objeto de serviço, permanece imutável desde que trabalhe com
# o objeto de serviço através de uma interface. Nós podemos
# passar um objeto proxy com segurança ao invés de um objeto
# real de serviço uma vez que ambos implementam a mesma
# interface.
class YouTubeManager:
    def __init__(self, service: ThirdPartyYouTubeLib):
        self.service = service

    def render_video_page(self, id):
        info = self.service.get_video_info(id)
        # Renderiza a página do vídeo.

    def render_list_panel(self):
        video_list = self.service.list_videos()
        # Renderiza a lista de miniaturas do vídeo.

    def react_on_user_input(self):
        self.render_video_page()
        self.render_list_panel()

# A aplicação pode configurar proxies de forma fácil e rápida.
class Application:
    def init(self):
        a_youtube_service = ThirdPartyYouTubeClass()
        a_youtube_proxy = CachedYouTubeClass(a_youtube_service)
        manager = YouTubeManager(a_youtube_proxy)
        manager.react_on_user_input()
