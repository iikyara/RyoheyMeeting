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
