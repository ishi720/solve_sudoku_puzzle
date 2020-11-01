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
function pazzeleDataSet(pazzeleData) {
    for (var i = 0; i <= 8; i++) {
        for (var j = 0; j <= 8; j++) {
            document.getElementsByClassName('cell_'+i+j)[0].value = pazzeleData[i][j];
        }
    }
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
        pazzeleDataSet(res.afterPuzzle);
    });
}