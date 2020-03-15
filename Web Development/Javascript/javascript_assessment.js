var employee = {
    name : "nirmal silwal",
    age : 24,
    job : "programmer"
}

console.log(employee["name"])
console.log(employee["age"])
console.log(employee["job"])

console.log(employee["name"].length)

//employee["nameLength"] = function(){
//    nameLength = this.name.length
//}
//TASK 1
function nameLength(employee){
    console.log("length of employee name is: "+ employee["name"].length)
}

nameLength(employee)

//TASK 2
var lenOfObject = Object.keys(employee).length

//for (var i=0; i<lenOfObject;i++){
//    console.log(i)
//}

// note: iterating object in javascript is tricky

//Object.entries(employee).forEach((item) =>{
//    console.log(item[0],item[1])
//}
//)


var output = ""
Object.entries(employee).forEach((item) =>{
    output = output + ( ", "+item[0]+" is "+item[1])
//    alert(item[0]+" is "+item[1])
}
)
alert(output)

console.log('task 2 done' )



// TASK 3

function lastName(x){
    fullName = x["name"];
    console.log(fullName.split(' ')[1])
}
lastName(employee)
