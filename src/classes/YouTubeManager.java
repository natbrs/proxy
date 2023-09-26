package classes;

// A classe GUI, que é usada para trabalhar diretamente com um
// objeto de serviço, permanece imutável desde que trabalhe com
// o objeto de serviço através de uma interface. Nós podemos
// passar um objeto proxy com segurança ao invés de um objeto
// real de serviço uma vez que ambos implementam a mesma
// interface.
public class YouTubeManager {
    protected ThirdPartyYouTubeLib service;

    public YouTubeManager(ThirdPartyYouTubeLib service) {
        this.service = service;
    }

    public void renderVideoPage(String id) {
        service.getVideoInfo(id);
        // Renderiza a página do vídeo.
    }

    public void renderListPanel() {
        service.listVideos();
        // Renderiza a lista de miniaturas do vídeo.
    }

    public void reactOnUserInput() {
        renderVideoPage("video_id_here");
        renderListPanel();
    }
}