$(function(){
    // 最初にゲージを0にして、音声ファイルを読み込み
    $("#renge").addClass("hee0");
    var audio = $("#heeAudio")[0];
    // へぇボタンクリックごとの処理
    $("label").click(function () {
      // 押す度に range の value を 1ずつ増加させる
      num = parseInt($("#hee").val());
      add = 1;
      $("#hee").val(num + add);
      // 音声の再生
      audio.load();
      audio.play();
      // class の付与
      numC = $("#hee").val();
      cls = "hee" + numC;
      $("#renge").removeClass().addClass(cls);
    });
  });