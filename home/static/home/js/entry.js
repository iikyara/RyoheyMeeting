let elem_participate = document.getElementById('participate');
let elem_not_participate = document.getElementById('not_participate');
let conference_id = document.getElementById('conference_id').value;

let activateClass = "active_section";

function participate(is_participate){
  var p_str = (is_participate) ? 1 : 0;
  $.getJSON('/setpresenter/' + getConferenceId() + "/" + p_str + "/", function(data){
    console.log("participate", data);
    updateButtons();
  });

}

function updateButtons(){
  $.getJSON('/getispresenter/' + getConferenceId() + "/", function(data){
    console.log(data);
    if(data['success']){
      var is_presenter = data['data']['is_presenter']
      var state = (is_presenter) ? 1 : 0;
      console.log("updatebutton", is_presenter);
      setState(state);
    }
    else{
      console.log(data);
    }
  });
}

function setState(state){
  switch(state){
    case 0:
      elem_participate.classList.add(activateClass);
      elem_not_participate.classList.remove(activateClass);
      break;
    case 1:
      elem_participate.classList.remove(activateClass);
      elem_not_participate.classList.add(activateClass);
      break;
    default:
  }
}

function getConferenceId(){
  return conference_id;
}

$(function(){
  updateButtons();
});
