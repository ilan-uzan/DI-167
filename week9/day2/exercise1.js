// / #1
function funcOne() {
    let a = 5;
    if(a > 1) {
        a = 3;
    }
    alert(`inside the funcOne function ${a}`);
}

// #1.1 - run in the console:
funcOne()
// #1.2 What will happen if the variable is declared 
// with const instead of let ?  --IT WOULD ALWAYS PRINT 5-- ILAN U.

//#2
let a = 0;
function funcTwo() {
    a = 5;
}

function funcThree() {
    alert(`inside the funcThree function ${a}`);
}

// #2.1 - run in the console:
funcThree()     //IT WOULD ALERT AND SHOW THE STRING WITH THE a AS A VALUE OF ZERO
funcTwo()   //IT WOULD CHANGE THE VALUE OF a TO 5 BUT NOTHING WILL PRINT
funcThree() //NOW IT CHECKS WHAT THE VALUE OF a IS AND ALERT AND SHOW THE VALUE OF a AS 5.
// #2.2 What will happen if the variable is declared 
// with const instead of let ? IT WOULD ONLY ALERT 0 FOR a EVERYTIME funcThree IS CALLED


//#3
function funcFour() {
    window.a = "hello";
}


function funcFive() {
    alert(`inside the funcFive function ${a}`);
}

// #3.1 - run in the console:
funcFour()
funcFive()

//#4
let a = 1;
function funcSix() {
    let a = "test";
    alert(`inside the funcSix function ${a}`);
}


// #4.1 - run in the console:
funcSix()
// #4.2 What will happen if the variable is declared 
// with const instead of let ?

//#5
let a = 2;
if (true) {
    let a = 5;
    alert(`in the if block ${a}`);
}
alert(`outside of the if block ${a}`);

// #5.1 - run the code in the console
// #5.2 What will happen if the variable is declared 
// with const instead of let ?