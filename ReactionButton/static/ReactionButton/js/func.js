const reaction_type_number = 3;

let reaction_counter = Array(reaction_type_number);
reaction_counter.fill(0);

//なるべく均等になるようにリアクションボタンを選ぶ．
function reactionSelecter(reactions){

}

//10回ごとにリアクションボタンを押した回数を送る．
function sendReaction(reaction_number){
  reaction_counter[reaction_number] += 1;
  if(reaction_counter[reaction_number] >= 10){
    _sendReaction(reaction_number);
    reaction_counter[reaction_number] = 0; // reset
  }
}

//リアクションボタンを押した回数を送る．
function _sendReaction(reaction_number){
  var userid = document.getElementById('userid').value;
  $.get('/ReactionButton/PushReaction/', {
    'reaction' : reaction_number,
    'userid' : userid,
    'count' : reaction_counter[reaction_number]
  });
}

//ページを離れるときにリアクションボタンを押した回数を送る．
$(window).on('beforeunload', function(e) {
  for(var i = 0; i < reaction_type_number; i++){
    if(reaction_counter[i]==0) continue;
    _sendReaction(i);
    reaction_counter[i] = 0; // reset
  }
  return true;
});