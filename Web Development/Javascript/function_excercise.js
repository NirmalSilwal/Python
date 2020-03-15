function monkeyTrouble(aSmile, bSmile){
 return (aSmile && bSmile) || (!aSmile && !bSmile)
}

function stringTimes(str, n){
    var i = 0;
    var output = "";
    while (i<n){
        output += str
        i += 1
    }
    return output
}