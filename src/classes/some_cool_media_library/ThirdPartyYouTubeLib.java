package classes.some_cool_media_library;

// A interface de um serviço remoto.
import java.util.HashMap;

public interface ThirdPartyYouTubeLib {
    HashMap<String, Video> popularVideos();

    Video getVideo(String videoId);
}