import classes.*;

// A aplicação pode configurar proxies de forma fácil e rápida.
class Main {
    public void init() {
        ThirdPartyYouTubeLib aYouTubeService = new ThirdPartyYouTubeClass();
        ThirdPartyYouTubeLib aYouTubeProxy = new CachedYouTubeClass(aYouTubeService);
        YouTubeManager manager = new YouTubeManager(aYouTubeProxy);
        manager.reactOnUserInput();
    }

    public static void main(String[] args) {
        Main app = new Main();
        app.init();
    }
}
