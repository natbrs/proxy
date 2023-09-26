package classes;

// A implementação concreta de um serviço conector. Métodos
// dessa classe podem pedir informações do YouTube. A velocidade
// do pedido depende da conexão do usuário com a internet, bem
// como do YouTube. A aplicação irá ficar lenta se muitos
// pedidos forem feitos ao mesmo tempo, mesmo que todos peçam a
// mesma informação.
public class ThirdPartyYouTubeClass implements ThirdPartyYouTubeLib {
    public void listVideos() {}

    public void getVideoInfo(String id) {}

    public void downloadVideo(String id) {}
}