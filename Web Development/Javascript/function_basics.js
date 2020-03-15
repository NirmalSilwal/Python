function hello(){
    console.log("i am executing now: hello world")
}
hello()

//note: in web page/ browser, left click, inspect and go to Console to see this output

function greeting(name){
    console.log('hello '+name)
}

/*FROM Console
greeting("nirmal")
function_basics.js:9 hello nirmal
*/

function welcome(name='default_name'){
    console.log('hello '+name)
}
welcome()
welcome('babu')

function restore(name="nirmal", title="sir"){
    return title+' '+name
}

/*
var message = restore()
undefined
message
"sir nirmal"
console.log('hey '+message)
VM375:1 hey sir nirmal
*/


// FUNCTION SCOPE

var greet = "global welcome"
var farewell = "global bye"

function tataBye(farewell){
    console.log('inside function: '+greet)
    farewell = "local bye bye"
    console.log('inside function: '+farewell)
}

tataBye()
console.log('outside function: '+greet)
console.log('outside function: '+farewell)
