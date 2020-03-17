$('h1').click(function(){
console.log('there was a click event on heading1')
})

$('li').click(function(){
    console.log('any li was clicked')
})

$('h1').click(function(){
    $(this).text("I am changed form old heading text")
})

$('h2').click(function(){
    $(this).text('I am brand new text for heading 2')
})

$('h2').click(function(){
    console.log('there was click event')
})

