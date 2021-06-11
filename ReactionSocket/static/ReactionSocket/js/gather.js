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
    //document.querySelector('#chat-log').value += ("destuser : " + data.user_id + "reaction_number" + data.reaction_number + '\n');
    document.querySelector('#chat-log').value += (data.message + '\n');

    //ここで音を鳴らす
    playAudio(data.message.reaction);
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message,
        // 'user_id': 0,
        // 'reaction_number': 0
    }));
    messageInputDom.value = '';
};

//ロードしたやつを溜めておきたい
var audio_dict = {};
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
