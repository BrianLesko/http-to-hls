
if (Hls.isSupported()) {
    var video = document.getElementById('video');
    var hls = new Hls();
    // Bind them together
    hls.attachMedia(video);
    hls.on(Hls.Events.MEDIA_ATTACHED, function () {
      console.log("video and hls.js are now bound together!");
      hls.loadSource("http://localhost:8080/hls/index.m3u8");
      hls.on(Hls.Events.MANIFEST_PARSED, function (event, data) {
        console.log("manifest loaded, found " + data.levels.length + " quality level");
        video.currentTime = video.duration;
      });
    });
  }
  