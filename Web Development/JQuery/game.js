var player1 = prompt('Player One: Enter your name, you will be Blue');
var player1Color = 'rgb(86,151,255)';

var player2 = prompt('Player Two: Enter your name, you will be Red');
var player2Color = 'rgb(237,45,73)';

var game_on = true;
var table = $('table tr');

function reportWin(rowNum, colNum){
    console.log("You won starting at this row and column");
    console.log(rowNum);
    console.log(colNum);
}

function changeColor(rowIndex, colIndex, color) {
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color':color);
}

function returnColor(rowIndex,colIndex){
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}

function checkBottom(colIndex){
    var colorReport = returnColor(5, colIndex);
    for (var row=5; row>-1; row--){
        colorReport = returnColor(row,colIndex);
//        checks if grey color is present i.e no red or blue color is selected by user then return that cell
        if (colorReport === 'rgb(128,128,128)') {
            return row
        }
    }
}


function colorMatchCheck(one, two, three, four){
    return (one === two && one==three && one===four && one!='rgb(128,128,128)' && one!=undefined);
}



