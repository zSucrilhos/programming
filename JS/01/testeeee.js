function abc(msg) {
    var lowerCaseStr = msg.toLowerCase();
    var newStr = "";
    
    for (var i = 0; i < lowerCaseStr.lenght; i++) {
        var currentLetter = lowerCaseStr[i];
        if (currentLetter === " ") {
            currentLetter += newStr;
        }
    }
    console.log(currentLetter)
}

abc("teste erick")

