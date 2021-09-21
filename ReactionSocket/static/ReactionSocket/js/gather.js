const confId = JSON.parse(document.getElementById('conf_id').textContent);
var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
const chatSocket = new WebSocket(
    ws_scheme + '://'
    + window.location.host
    + '/ws/ReactionSocket/'
    + confId
    + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log(data);

    //ここで音を鳴らす
    playAudio(data.message.reaction);
    moveImage(data.message.reaction_img);
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

//ロードしたやつを溜めておきたい
var audio_dict = {};
var img_dict = {};
var currentSound = null;

function playAudio(filename){
  stopCurrentSound();
  //ロード済み
  if(audio_dict[filename]){
    currentSound = audio_dict[filename];
  }
  //初回ロード
  else{
    var audio = document.createElement('audio');
    audio.src = filename;
    document.body.appendChild(audio);
    audio_dict[filename] = audio;
    currentSound = audio;
  }
  //console.log(document.getElementById('customRange1').value);
  currentSound.volume = document.getElementById('customRange1').value;
  currentSound.play();
}

function stopCurrentSound()
{
	if( currentSound != null )
	{
		currentSound.pause();
    currentSound.currentTime = 0;
	}
}

function moveImage(filename){
  console.log(filename);
  target = null;
  if(img_dict[filename]){
    target = img_dict[filename].cloneNode(true);
  }
  else{
    var image = document.createElement('img');
    image.src = filename;
    img_dict[filename] = image;
    $(image).addClass("reaction_img");
    $(image).addClass("standby");

    target = image.cloneNode(true);
  }

  //毎回一番下に追加（元の要素は自動で消える）
  document.body.appendChild(target);

  $(target).removeClass("standby");
  window.setTimeout(function(target){
    console.log(target);
    $(target).addClass("standby");
    target.remove();
  }.bind(undefined, target), 2990);
}

function Volume(flag) {
  if (0 < flag) {
    if (0.9 < audioElem.volume) {
      audioElem.volume = 1;
    } else {
      audioElem.volume += 0.1;
    }
  } else {
    if (audioElem.volume < 0.1) {
      audioElem.volume = 0;
    }
    else {
      audioElem.volume -= 0.1;
    }
  }
}
