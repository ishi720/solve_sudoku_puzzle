/*
 * 現在入力されているパズルを9x9の配列として取得する
 * @return {Array}
 */
function pazzeleDataGet() {
    var pazzeleData = [];
    for (var i = 0; i <= 8; i++) {
        pazzeleData[i] = [];
        for (var j = 0; j <= 8; j++) {
            pazzeleData[i][j] = Number(document.getElementsByClassName('cell_'+i+j)[0].value);
        }
    }
    return pazzeleData;
}

/*
 * 特定できた箇所に数値をセットする
 * @param {Array} pazzeleData セットするデータ
 */
function pazzeleDataSet(pazzeleData,percentage,fraction) {
    for (var i = 0; i <= 8; i++) {
        for (var j = 0; j <= 8; j++) {
            document.getElementsByClassName('cell_'+i+j)[0].value = pazzeleData[i][j];
        }
    }
    document.getElementsByClassName('percentage')[0].innerText = percentage + "%";
    document.getElementsByClassName('fraction')[0].innerText = "(" + fraction + ")";
}

function puzzleSolver() {
	var puzzle = pazzeleDataGet();
    $.ajax({
        type: "POST",
        url: '/api/',
        data: {
            puzzle: JSON.stringify(puzzle)
        },
        dataType: 'json',
    }).done(function(res) {
        console.log(res);
        pazzeleDataSet(res.afterPuzzle,res.percentage,res.fraction);
    });
}