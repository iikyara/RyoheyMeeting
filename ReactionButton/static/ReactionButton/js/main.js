// const $audio = new Audio();
// $audio.src = "/sound-of-silence.mp3";

// $audio.play();

window.onload = () => {
    const se     = document.querySelector('#B1_Uso_audio');
    document.querySelector("#B1_Uso_img").addEventListener("click", () => {
        se.play();
    
    // const se     = document.querySelector('#R1_Sekaiichi_audio');
    // document.querySelector("#R1_Sekaiichi_img").addEventListener("click", () => {
    //     se.play();
    });
};

// window.onload = () => {
//     const se     = document.querySelector('#R1_Sekaiichi_audio');
//     document.querySelector("#R1_Sekaiichi_img").addEventListener("click", () => {
//         se.play();
//     });
// };

// window.onload = function() {
//     // ページ読み込みと同時にロード
//     wa.loadFile("./assets/sample.mp3", function(buffer) {
//       wa.play(buffer);
  
//       // ユーザーイベント
//       var event = "click";
//       document.addEventListener(event, function() {
//         wa.playSilent();
//       });
//     });
//   }