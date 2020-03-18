//CONSOLE EXPERIMENT

$
ƒ ( selector, context ) {

		// The jQuery object is actually just the init constructor 'enhanced'
		// Need init if jQuery is called (just allow error to be thrown if not included)
		return new jQuery…
$('h1')
jQuery.fn.init [h1, prevObject: jQuery.fn.init(1)]
$('li')
jQuery.fn.init(4) [li, li, li, li, prevObject: jQuery.fn.init(1)]
var x = $('h1')
undefined
x.css('color','red')
jQuery.fn.init [h1, prevObject: jQuery.fn.init(1)]
x.css('background','blue')
jQuery.fn.init [h1, prevObject: jQuery.fn.init(1)]
var newcss = {'color':'white', 'background':'green',border:'20px solid red'}
undefined
x.css(newcss)
jQuery.fn.init [h1, prevObject: jQuery.fn.init(1)]
var listitems = $('li')
undefined
listitems
jQuery.fn.init(4) [li, li, li, li, prevObject: jQuery.fn.init(1)]
listitems[0]
listitems[-1]
undefined
listitems.css('color','blue')
jQuery.fn.init(4) [li, li, li, li, prevObject: jQuery.fn.init(1)]


listitems.eq(0).css('color','maroon')
jQuery.fn.init [li, prevObject: jQuery.fn.init(4)]
listitems.eq(-1).css('color','orange')
jQuery.fn.init [li, prevObject: jQuery.fn.init(4)]
$('h1').text
ƒ ( value ) {
		return access( this, function( value ) {
			return value === undefined ?
				jQuery.text( this ) :
				this.empty().each( function() {
					if ( this.nodeType === 1 || this.nodeType ===…
$('h1').text()
"Selecting with JQuery"
$('h1').text('I am new text')
jQuery.fn.init [h1, prevObject: jQuery.fn.init(1)]
$('h1').text()
"I am new text"
$('h1').html()
"I am new text"
$('h1').text('<em>I am emphasised</em>')
jQuery.fn.init [h1, prevObject: jQuery.fn.init(1)]
$('h1').html('<em>I am emphasised</em>')
jQuery.fn.init [h1, prevObject: jQuery.fn.init(1)]
$('input')
jQuery.fn.init(2) [input, input, prevObject: jQuery.fn.init(1)]
$('input').eq(0)
jQuery.fn.init [input, prevObject: jQuery.fn.init(2)]
$('input').eq(0).text()
""
$('input').eq(1).text()
""
$('input').eq(1).attr('type','checkbox')
jQuery.fn.init [input, prevObject: jQuery.fn.init(2)]
$('input').eq(0).val('new value')
jQuery.fn.init [input, prevObject: jQuery.fn.init(2)]




