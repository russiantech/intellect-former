CSS Course:

(Lesson-1) Introduction To CSS
(Topic-1) What Is Css?
What is CSS?
Anyone would want to make their webpage look more interactive and fancy, we’ve a solution for it in the world of programming- CSS.
CSS is a language that decides how your HTML should look.
CSS stands for Cascading Style Sheets.
Let’s see what CSS can do for us:
`<img-of-add_colors.jpg->`
Add colors to the webpage.
Providing webpage a rich and attractive look.
Change shapes, give borders to your HTML Elements.
Something like the picture given above.
Something like the picture given above.
Position your elements as you want - change the layout.
<img-of-animated_box.gif->
Animate your HTML elements.
So, basically CSS does all that to the HTML that filters do to your Instagram pictures. Make it look beautiful!

CSS stands for:
`Select the right answer`
`Cross Style Sheets`
`Cascading Style Scripts`
`Cascading Style Sheets`
`None of the above`

(Topic-2) Css Syntax

Syntax
CSS Syntax consists of Selectors and Declarations.
Selectors are simply used to select the HTML element to be styled.
Declaration consists of a set of instructions which tell the browser how to style the selected HTML element.
Selectors tell “where to do” and declarations tell the browser “what to do”. Exactly like :
Choosing a paper - Selection
Cutting it into half - Manipulation which comes from the ‘Declaration’.

<img-of-select_p_tag.jpg->
In the above image p is a Selector and the rest forms the Declaration block.
Declarations are properties and values followed by semicolons and enclosed within curly brackets.
So, by this we are selecting all the paragraph elements present in our webpage and changing their font size to 24px. (px stands for pixels).
That’s how we can select elements and write property and value pairs to manipulate them.
*If you don’t understand what font-size is doing, take a chill pill. We will be exploring it in further sections.

Which of the following do you think CSS is capable of doing?
`Select the right answer`
`Add Colors`
`Modify Layout`
`Add animations`
`All of the above`

Which of the following is NOT a part of CSS Syntax?
`Select the right answer`
`Semicolon`
`Tags`
`Curly brackets`
`Selectors`

p{
color : red ; 
}
What according to you will the above code do?
`Select the right answer`
`It will change the color of all the elements.`
`It will change the color of all the paragraph elements to Red.`
`It will set alphabet to color red.`
`I don’t understand.`


(Lesson-2) How To Add CSS
(Topic-1) How to add CSS to your HTML?

How to add CSS to your HTML?
There are numerous ways in which a task can be performed. Similarly, you can add CSS to your HTML the way you want to. Not really. ;)

There are three ways to apply CSS to your HTML elements:

1. Write your CSS within the HTML tags - Inline CSS
2. Write it inside your HTML file enclosed within the <style></style> tag - Internal CSS.
3. Write it in a separate file with a .css extension and include it in HTML using the <link> tag - External CSS.

(Topic-2) Inline CSS

Inline CSS
Writing CSS inside the HTML tags using a style attribute, is known as Inline CSS.
 <p style=”font-size: 24px; color: orange;”>
This is how you write inline CSS.
</p>
<img-of-snippet-above->
It will change the color of text inside the paragraph to orange and font-size to 24px.

(Topic-3) Internal CSS

Internal CSS
When you write CSS enclosed in the <style> tag within the <head> tag in your HTML file, it is known as Internal CSS.
 <head>
	<style>
	p{
		color: orange;
		font-size: 24px;
	}
</style>
</head>
The above snippet will change the color of the text inside the paragraph to orange and font-size to 24px.

(Topic-4) External CSS

Storing your things in different compartments is always a judicious way of managing.
When you write CSS in a separate file and include the file in the HTML using the <link> tag, it is known as External CSS.
 <head>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
“rel” attribute specifies the relationship that the linked file has with the source file.

“type” attribute specifies the internet media type and the value “text/css” conveys that it is CSS.

“href” or hypertext reference is used to provide the path of the file which we want to link.
 `//style.css
 p{
	font-size: 24px;
	color: orange
}`
The styles written inside .css file are not enclosed within any tags.

Writing CSS externally is recommended as it is easy to manage as well as it can be used at multiple places easily.

Can you include CSS using all the three ways?
High-five if this question popped up in your mind :)

If you include CSS in all the three ways having the same property and selector, then the Inline CSS will have the highest precedence and it will override all the other CSS.

If you include internal CSS as well as external CSS then the precedence depends upon the order in which you specify them inside the <head> tag.

 <head>
	<link rel="stylesheet" type="text/css" href="style.css">
	<style>
	p{
		color: red;
		font-size: 20px;
	}
	</style>
</head>

Here the CSS written internally will override the external css and the text color will change to red and its font size to 20px.

*CSS is always read by browsers from top to bottom, so the one appearing below will override the above one if the selector and property are same.

(Topic-5) Let’s Revise

When we include CSS within the HTML tags,it is known as:
`Select the right answer`
`Internal CSS`
`Inline CSS`
`External CSS`
`None of the above`

Which of these attributes are a part of the syntax while linking to the External CSS?
`Select one or more answers`
`style`
`rel`
`type`
`href`

Which among the following is the recommended way of writing CSS?
`Select the right answer`
`Inline`
`External`
`Internal`
`None of the above`

Which one among the 3 holds highest precedence, when used together?
`Select the right answer`
`Inline`
`External`
`Internal`
`None of the above`

(Lesson-3) Selecting HTML Elements
(Topic-1) Select Html Elements

Selecting HTML Elements
An HTML element can be selected using:
1. Element Selector
2. Class Selector
3. Id selector
4. Attribute Selector

Element Selector
 <p>Here is some text written inside the paragraph tag.</p>
To simply select the above text, we can use element selector which is nothing but using the element name.
So, in order to select the above text and modify its style, we can write:
`p{
	/*property value pairs*/ 
}`
The above snippet will select all the paragraph elements present on the webpage.

Note: /* */ is used to enclose comments in CSS. The things written inside /* and */ is not read by browsers.

Class Selector
 <p class=”select-me”>Here is a paragraph tag which also has a class specified inside it.</p>
If an HTML element has class associated with it, then it can be referenced using class selector in CSS.
Writing a class selector involves writing . (dot) followed by class name.
`.select-me{
	/*property value pairs*/
}`
The above snippet will select all the elements containing the select-me class.

Id Selector
 <p id=”select-me”>
	Here is a paragraph tag which also has an id specified inside it.
</p>
If an HTML element has an id associated with it, then it can be referenced using id selector in CSS.
Writing an ID selector involves writing # (hash) followed by the id name.
`#select-me{
	/*property value pairs*/
}`
The above snippet will select the element containing select-me id.

Attribute Selector
<input type="text" />
Given above is an input tag containing type attribute with value text.
If an HTML element has an attribute associated with it, then it can be referenced using attribute selector in CSS.
Writing an attribute selector involves writing element name followed by [attribute = value] as shown below:
`input[type=text]{
	/*property value pairs*/
}`
The above snippet will select all the input elements containing the type attribute with value text.

(Topic-2) Let's Revise

Which of the following is NOT a valid CSS Selector?
`Select the right answer`
`Class Selector`
`Tag Selector`
`Id Selector`
`Element Selector`

Which of the following is correct syntax of attribute selector?
`Select the right answer`
`[value=type]`
`.input[type = value]`
`#input[type = value]`
`input [type = value]`

# is used in which selector?
`Select the right answer`
`Class Selector`
`Id Selector`
`Attribute`
`None of the above`

(Lesson-4) Playing With Colors
(Topic-1) Playing With Colors

Playing with colors
Colors are integral part of any web application.
Colors in CSS can be specified in following ways:
1. Directly writing the name of colors.
2. Using hex values of colors.
3. Using RGB/RGBA values.

Using Color Names
<img-of-using_color_names.png->
Color in CSS can be specified by simply using a color name.
The total number of color names supported is 140.
Black, Blue, Red, Green, Gray, Aqua, Brown, Coral, Indigo are few to name.

Hex Values
Another way of specifying colors in CSS is by using hexadecimal aka Hex values.
Hexadecimal values are written in following format #rrggbb where rr, gg and bb are values between 00 and ff.
rr - the amount of red
gg - the amount of green
bb - the amount of blue
00 is the lowest value and ff the highest.
#000000 forms black color, whereas #FFFFFF forms white.

RGB/RGBA Values
A color can also be specified using an RGB or RGBA value.
R- Red, G- Green, B- Blue and A - Alpha, alpha is a number between 0.0 (fully transparent) and 1.0 (fully opaque).
0 depicting the lowest intensity and 255 the highest.
For writing color in RGB format follow the syntax:
rgb(R, G, B) where R, G and B can be any values between 0 and 255.

If there is a need to specify opacity: rgba(R, G, B, A) is used and for A values between 0.0 - 1.0 can be specified.

rgb(0,0,0) will form a black color and rgb(255,255,255) white.

(Topic-2) Let's revise

Which of the following is incorrect way of specifying colors?
`Select the right answer`
`Red`
`ff0000`
`#ff0000`
`rgb(255,0,0)`

Which of the following is the range of a in rgba?
`Select the right answer`
`0 - 255`
`1.0- 10`
`0.15 - 1.15`
`0.0 - 1.0
`
# is used in which of the following color formats?
`Select the right answer`
`rgba`
`hex`
`Color Names`
`None of the above`

What does A in rgba(R, G, B, A) stands for?
`Select the right answer`
`Apple`
`Alpha`
`Alpes`
`Align`

(Lesson-5) Manipulating Background
(Topic-1) Manipulating background of your web-page
Manipulate Page Background

Like the background of a room enhances the look and feel of it, similarly-
<img-of-bg.jpg->
Changing that white background becomes a necessity when it comes to building for the web.
Either you can set the background color or add an image as background.

Background Color
<img-bg_color.png->
The property used to modify background color is background-color or background and values can be specified in any format from the ones we learnt.
 body{
	background-color: red;
}
or
 body{
	background-color: #FF0000;
}
or
body{
	background-color: rgb(255,0,0);
}
or
body{
	background-color: rgb(255,0,0);
}

Will change the background color of page to red.
*Simply background can also be used instead of background-color.

Background Image
<img-of-wallpaper.png->
Imagine adding a beautiful wallpaper to one of the walls of you room, similarly you can add image to your webpage in the background.
It is as easy as learning abc.
background or background-image property is used to specify background image.
`background: url(“path to image”);`
Value consists of the url followed by the path to image in brackets. This path can be replaced by some url of image on the web or by the path of image present in your local machine.
`body{
background: url('https://intellect.techa.tech/img/logos/favicon.png');
}`
<img-of-snippet-page-above->
Will set the background image to the above.

Customizing background image
Isn’t it a beauty, to modify the image as per your convenience.

`background-size` property enables us to set/change the size of background image in css. It can take values of height followed by width, or contain or cover.

`contain` makes sure that the height and width of background image are in accordance with the height and width of content. And image fits inside the content area.

`cover` makes sure that the height and width of the image spans the entire width and height of the available area.

Valid background-size values are as follows:
`background-size: 100%;`
`background-size: cover;` 
`background-size: contain;`

*height and width can be specified in multiple ways which we will be learning ahead.

Customizing background image (continued)
`Background-repeat` property enables us to control if the image will be repeated to fill the content area or not.
It can take either of `repeat` or `no-repeat` as values. 
Repeat specifies that the image is allowed to be `repeated` to fill the content area and no-repeat specifies it `is not`.
`background-repeat: no-repeat;`
`background-repeat: repeat;`
Both these are valid declarations.

(Topic-2) Let's Revise

Which of the following can be used to set background color?
`Select one or more answers`
`backgroundColor`
`background-color`
`background`
`background-image`

What is the correct syntax to set a background image?
`Select one or more answers`
`background-image: url(“path”);`
`background: url(“path”);`
`backgroundImage: “path”`
`background: “path”`

What should be used if we want our background image to span across the height and width of the available content area?
`Select the right answer`
`background-size: cover;`
`background-size: contain;`
`backgroundSize: cover;`
`backgroundSize: contain;`

(Lesson-6) Beautifying Texts Using CSS
(Topic-1) Beautifying Texts Using CSS

Beautifying text using CSS
<img-of-beautify_text.jpg->
Font-style, color, font-size, formatting of text is inevitable whether you are writing a novel or creating a web application.

HTML cannot do these things alone. That’s where CSS comes to rescue.
Let’s see how to modify properties of text.

Changing Color
The text, when in contrast with the background, enhances the user readability.
To change color of text in CSS color property is used followed by value or name of color.
`<p>Hey! Make me purple</p>
//style.css 
p{
	color: purple;
}`

The above CSS will change color of text inside every paragraph tag to purple.

Changing Alignment
<img-align_text.png->
Justified, center, right or left? How?
Let’s see how we can change alignment of text.
`<p>Hey! I am here.</p>
//style.css 
p{
	text-align: center;
}`
The property used is text-align and values can be anyone of center, left, right and justify.
The above CSS will make the text inside paragraph tag center aligned.

Changing Font size
<img-of-font_size.png->
The size of the text plays a crucial role in writing, for prioritizing and emphasizing.
Font size in CSS can be changed using font-size property.
The value of font-size can be either set using pixels (px) or em.
1em = 16px;

`<p>Hey! Please increase my font-size.</p> 
//style.css
p{
	font-size: 32px;  /*can be specified using em as 2em*/ 
}`
The above will increase font size of text to 32px.

What according to you will change the font size of the text to 50px?
`Select the right answer`
`Font-size: 50;`
`size: 50;`
`font-size: 50px;`
`Size-font: 50px;`

Changing Font weight
Font weight is used to change the weight (boldness) of the font.
The font-weight property is used to modify font-weight.
Values can be normal, bold, bolder, lighter or any value from 100, 200, 300, 400, 500, 600, 700, 800 or 900. 100 being the lightest and 900 being the boldest.

<p>Hey! Please change my font-weight.</p>
`//style.css
p{
    font-weight: 400;  /* can be anything from above values*/
}`
The command given above will change the font-weight of the text to 400.

Changing Font family
The font family or font can be changed using font-family property.
`<p>Hey! Please change my font-family.</p>
  //style.css
p{
	font-family:'Roboto', sans-serif;
}`
The command given above will change the font-family to Roboto.
If the roboto font is not found then sans-serif font is applied. It uses a fallback system.

(Topic-2) Let's Revise _ Beautifying Text With CSS
Quiz Time!!!
Which of the following is a valid value for text-align property?
`Select one or more answers`
`center`
`justify`
`right`
`top`

Which of the following are accepted units for specifying font size?
`Select the right answer`
`em, px`
`m, cm`
`in`
`None of the above`

Which property is used to change the color of the text?
`Select the right answer`
`text-color`
`color`
`font-color`
`None of the above`

Why is font-weight property used?
`Select the right answer`
`To transform text to italic`
`To make text bold`
`To underline text`
`None of the above`

(Lesson-7) Height | Width | Margin & More
(Topic-1) Introduction _ Height & Width Html

Height, width margin and more
CSS gives freedom to modify height, width, margin, apply border and padding to elements.
These properties come handy while making any web application visually appealing.
Let’s explore how we can use these properties.

Height & Width
To change the height of any element height property is used.
Similarly, to change width, width property is used.
Height and width can take values in pixels(px) and percentage.
Let’s see how it is done.
<img-of-height.png->
<img src=”img.png” class=”panda”>Wow</div>
`//style.css
.panda{
	height: 400px;
	width: 400px;
}` 
The above CSS will change the height and width of div to 400px.
`.panda{
	height: 50%;
	width: 100%; 
}`
This will change the height to 50% of the available container height and width to 100% of the available container width.

Can height and width property take both px and percentage as values?
`Select the right answer`
`True`
`False`

Border
<img-of-border.png->
We have to admit that things do look better with borders!
To give border to any element we can use border-width, border-style and border-color properties.

border-width can take any value in pixels, border-style provides variations like dashed, solid, dotted and border-color can take any valid color value.
 <div class=”rocket”>The box has margin around it.</div>
`//style.css
.rocket{
	border-width: 2px;
	border-style: solid;
	border-color: black;
}`
The above css will apply a solid border to div with width 2px and blue color.
There is also a shorthand property to apply border which goes like:

`.rocket{
	border: 2px solid black; 
}`

Where 2px is the border-width, solid is the border-style and the border-color is black.

If we need curved edges,then border-radius property can be used.
`.rocket{
	border: 2px solid black;
	border-radius: 20px; 
}`
Making its value 50%, will transform it to a circle.

Margin
We create margins to separate the main content from the page’s edge.
For a webpage, Margin is used to create space around elements outside the border.
We use margin-top, margin-right, margin-bottom and margin-left properties which in turn applies margin to top, right, bottom and left sides respectively.

 <div class=”starlord”>Starlord, who?</div>
`.starlord{
	margin-top: 20px;
	margin-right: 30px;
	margin-bottom: 20px;
	margin-left: 30px;
}`

The above command will change the default margin around div to 20px from the top, 30px from the right, 20px from the bottom and 30px from the left.

Is there any shorthand property for margin? Hell Yeah!
`.starlord{
	margin: 20px 30px 20px 30px; /*In order top, right, bottom, left*/ 
}`

Also, we can write:
`.starlord{
 margin: 20px 30px;
}`

These values will repeat themselves for bottom and left and will end up giving the same result as the above.

Also,
`.starlord{
margin: 20px;
}`

will create a margin of 20px around all sides.

For margin: 10px 20px 10px 20px;
What is the order that is considered while drawing a margin?
`Select the right answer`
`right, left, top, bottom`
`top, right, bottom, left.`
`left, top, bottom, right`
`top, left, right, bottom`

Padding
<img-of-padding.png->
Padding is used to create space around elements, inside the border.
We use padding-top, padding-right, padding-bottom and padding-left properties which in turn applies padding to top, right, bottom and left sides respectively.
<div class=”starlord”>Starlord, who?</div>
`.starlord{
	padding-top: 20px;
	padding-right: 30px;
	padding-bottom: 20px;
	padding-left: 30px;
}`

Deja Vu!!?? No.

The above command will change the default padding around div to 20px from the top, 30px from the right, 20px from the bottom and 30px from the left.

Is there also a shorthand property for padding? ofcourse.
`.starlord{
	padding: 20px 30px 20px 30px; /*In order top, right, bottom, left*/ 
}`

Also, we can write:
 .starlord{
	padding: 20px 30px;
}

These values will repeat themselves for the bottom and left and will end up giving the same result as the above.

Also,

`.starlord{
	padding: 20px;
}`

will create a padding of 20px around all sides.
Deja Vu!!?? No.

(Topic-2) Let's revise

Which of the following is a property used to give color to border?
`Select the right answer`
`border-radius`
`border-style`
`border-color`
`borderColor`

Which of the following correctly defines padding and margin respectively?
`Select the right answer`
`Space around element - inside border, space around element - both inside and out`
`Space around element - inside border, space around element - outside border`
`Space around element - both inside and out, Space around element - inside border`
`None of the above`

What effect will following have margin: 20px 50px; on the element to which it is applied?
`Select the right answer`
`Margin of 20px and 50px from top and right respectively`
`Margin of 20px, 50px, 20px, 50px from top, right, bottom, left respectively.`
`Margin of 20px and 50px from top and left.`
`Margin of 50px from bottom and 20px from right`

What effect will height: 100%; and width: 100% will have on the element to which it is applied?
`Select the right answer`
`Element will cover entire area available within element container`
`Element will have height 100px and width 100px`
`The element will grow to fit to page`
`None of the above`

(Lesson-8) Positioning Your HTML Elements
(Topic-1) Introduction To Positioning Elements

Positioning HTML elements
Better positioning of objects in a room gives it a neat and a managed look. Similarly, Positioning of elements is an integral part of building for web.
The property used to change position of elements is position. Obviously!
Want something sticking to the screen or make an element adjust its position relative to itself or place elements exactly where you want.
Everything at your disposal. Tap! Tap!

Static Position
<img-postion_static.png->
For a room, the default position of a flower vase would be somewhere on the table, near the window.
For a webpage, an element which is positioned static is positioned according to the normal flow of the page.
By default the position of all HTML elements is set to static.
This is how you must give static position to elements, if ever required.

You can take the back seat, nothing to do here.
`<div class=”static-me”>I am not special.</div>
.static-me{
	position: static;
}`

Is static, the default position of all HTML elements?
`Select the right answer`
`True`
`False`

Relative Position
<img-postion_relative.png->
The rug we place in the room is near the door/bed/bathroom. So we keep changing its position relative to our need.
Relative positioning enables us to position the element relative to itself.
That is, the element will change position relative to its default position.
`<div class=”relative-me”>What does this even mean? Look up.</div> 
.relative-me{
	position: relative;
	top: 10px;
}`
This will move the div 10px towards bottom from where it would have been by default.
*top, left, right, bottom are used with position to specify distance from respective axes.

Fixed Position
<img-postion_fixed.png->
We tend to fix the position of a painting in a room (till the time we get another one).
Fixed positioning enables us to position the element relative to the screen.
If an element is given a fixed position it will occupy that position on the screen.
`<div class=”fixed-me”>I get attached soon.</div>
.fixed-me{
	position: fixed;
	top: 50px;
	left: 50px;
}`
This will move the div 50px towards bottom and 50px towards right from its original position and will keep it fixed there.
Fixed elements stay at the same place on screen even if user scrolls.

Select all that is correct about fixed position.
`Select one or more answers`

`Elements with position as fixed, stay at the same place on the screen.`

`Elements move relative to the screen. --  x`

`Elements are positioned relative to the screen`

`Top, left, right, etc can be used to specify exact position.`

Absolute Position
<img-postion_absolute.png->
Absolute positioning enables us to position the element exactly where we want it.
We can use top, right, bottom, let properties to place it wherever we want.
`<div class=”absolute-me”>I am the best thing you have in store.</div>
.absolute-me{
	position: absolute;
	top: 50px;
	left: 50px;
}`
This will place the div 50px towards bottom and 50px towards right from its original position.


(Topic-2) Let's Revise Positioning Elements

Which of the following will enable us to position elements relative to the screen?
`Select the right answer`
`static`
`absolute`
`fixed`
`relative`

Relative positioning will make element’s position relative to?
`Select the right answer`
`Screen`
`Itself`
`Both Screen and itself`
`None of the above`

If we want to place an element exactly where we want it then which one of the following should be used?
`Select the right answer`
`Relative`
`Absolute`
`Fixed`
`Static`


(Lesson-9) Manipulating Display Properties
(Topic-1) Let's Manipulate The Display

Manipulating display properties
<img-of-tetris.png->
Remember, the excitement we get while playing tetris to change the default shape of the objects, just to win the game.
Display property in CSS is used to control the default rendering behavior of an element.
Different elements have different default rendering behaviour.
For eg: <p> and <div> are block level elements whereas <a> and <span> are inline elements.
Puzzled? Let’s explore the display and inline values of display property.

Display block
<img-block_inline.png->
An element which has display property set to block is displayed on a new line and spans across the whole width.
To change the display behaviour of elements display property is used.
And to make an element display as block, display property is set to value `block`.
`<span class=”block-me”>I need space.</span>

//style.css
.block-me{
		display:block;
 } `
The above snippet will change the display behaviour of <span> to block.
*<span> is an inline element by default.

Does the display:block; takes the entire available width?
`Select the right answer`
`True`
`False`

Display:Inline block
<img-of-block-inline.png->
Setting display behaviour to inline-block enables us to set the height and width of the element and also occupy multiple elements in a single row.

`<div class=”inline-me”>Hey, I wish we were together.</div>
<div class=”inline-you”>What’s stopping you?</div>

//style.css
 .inline-me, inline-you{
	display: inline-block;
	height: 20px; 
	width: 50%;
}`

The above snippet will make both the divs inline where each will one take 50% of the container width and the output will be similar to the one shown in the above image.
*div is a block element by default.

How is inline-block different from block display?
`Select one or more answers`
`They both are same.`
`You can add height and width to the class.`
`You can add multiple elements in a row.`

Display : None
Display value none is used to completely remove the element.
*Whoosh, Vanish!* Just like that.
`<div class=”not-me”>I didn’t do anything.</div>
//style.css
 .not-me{
	display: none; 
}`
The above snippet will remove the div from the view.

(Topic-2) Let’s Revise

Which of the following will make an element span itself through entire row?
`Select the right answer`
`display: inline;`
`display:none;`
`display: block;`
`display: inline-block`

If I want to hide an element, what value of display property should I use?
`Select the right answer`
`block`
`none`
`inline-block`
`None of the above`

Display inline-block makes an element,
`Select the right answer`
`Cover entire row`
`Span to a given width and height and occupy other elements`
`Invisible`
`None of the above`

`Correct Answer`
Keep rolling! We learned that display set to inline-block will make an element span to the width provided and occupy multiple elements in a single row.


(Lesson-10) Overflowing Contents? No Problem
(Topic-1) Overflowing Contents? No Problem

Overflowing content? ok.
<img-of-overflow_content.png->
Wouldn’t it be helpful, if we get informed about overflowing of a water jar while we still watch the extra minutes of a football game.
The overflow property in CSS, is used to specify what happens if content goes beyond the context or content area.
Two options: Either trim the content or find a genie.

Trim overflowing content
<img-of-overflow_content_trim.png->
To trim the overflowing content hidden value is passed to the overflow property. This will make the overflowing content invisible.
`<div class=”trimmed”>I know I am going to get slashed from bottom but it’s fine. Someone will save me. Hopes intact.</div>

//style.css
 .trimmed{
	height: 20px;
	width: 400px;
	overflow: hidden;
} `

The above snippet will result in the following output below:
<make-the-above-code-display-here->
`I know I am going to get slashed from bottom but it’s fine.`

The height and width of div is set to be 20px and 400px respectively, so the content overflows and since it is assigned a value of hidden. It gets trimmed.

How can you make the overflowing content invisible?
`Select the right answer`
`overflow: trim`
`overflow : hidden`
`overflow: hide`
`None of the above`

Add scrollbars
<img-of-overflow_content_scroll.png->
The code is magical in itself, no need of a genie.
To display the overflowing content we can set the display property to scroll.
This will add a horizontal as well as a vertical scrollbar to the div.
`<div class=”scroll”>I knew you would save me. Let’s show the world what we are made of.</div>

//style.css
 .scroll{
	height: 50px;
	width: 200px;
	overflow: scroll; 
} `

The output of the above snippet:
<img-of-snippet-above->
Scrollbars appear around the div and the content can be seen upon scroll.

How can you make the overflowing content visible?
`Select the right answer`
`overflow: unhide`
`overflow : scroll`
`overflow: untrim`
`None of the above`

Overflow Auto
<img-of-overflow_content_auto.png->
Setting overflow to auto is an intelligent move.
It automatically detects if the content is trimmed and adds scrollbar if necessary, and only along the axis where it is required.
`<div class=”auto-me”>I knew you would save me. Let’s show the world what we are made of</div>

.auto-me{
	height: 40px;
	width: 200px;
	overflow: auto; 
}`
The above snippet will result in above output.

The scrollbar appears since the content is getting trimmed, also only vertical scrollbar appears.

Overflow visible
<img-of-overflow_content_visible.png->
This is not something you would want.
But setting overflow to visible will make the content render even if it goes outside the container.
Surprisingly, this is the default behaviour.
`<div class=”visible-me”>I knew you would save me. Let’s show the world what we are made of</div>

//style.css
 .visible-me{
	height: 40px;
	width: 200px;
	overflow: visible;
	border: 1px solid #000;
 }` 
The above snippet will result output above.
You can observe how the content is shown even if it goes outside the div.


(Lesson-11) What Are Pseudo Classes?
(Topic-1) Pseudo class introduction

What are Pseudo Classes?
<img-of-pseudo_class.png->
The way we can twist and turn a piece of clay and change it into the shape/state we want. Similarly in HTML-
An element can have multiple states.
These states can be anything like hovered, focused, visited, active depending upon the user’s actions.
To change the properties of elements in these states we have pseudo classes.
Pseudo classes are written in the following manner:
`selector:pseudo-class{
	  property: value; 
}`

Let’s explore the available pseudo classes.

Changing element properties on hover
<img-of-hover.png->
Have you ever noticed the text being focused when you hover over it?
For the same purpose we use pseudo class hover to target elements when they are hovered.
Whatever property and value we give to hover pseudo class will apply only when the element is hovered.
`<input class=”hover-me” type=”button” value=”Hover” />

//style.css
.hover-me:hover{
 background-color: green; 
}`
The above snippet will result in below:
<make-snippet-above-display-here->
And when the button is hovered, the background turns green like this:
<make-snippet-above-display-here-or-hover_state.png->

Pls Answer
The below will result in red color of the background when hovered?
`.hover-red.hover{
	 background:red;
}`
`Select the right answer`
`True`
`False`

Changing properties of an active element
<img-of-link.png->
To change the properties of an active link, active pseudo class is used.
A link is in active state when clicked.
`<a href=”www.anywebsiteyoulike.com”>Click me</a>

//style.css
 a:active{
	color: red; 
}`
The above snippet will result in image above

When the link is clicked
<img-of-link_active.png->

Change properties of unvisited links
<img-link_unvisited.png->
To change the properties of links which are yet unvisited, link pseudo class is used.
`<a href=”www.anywebsiteyoulike.com”>Don’t click me</a>

//style.css
 a:link{
	color: red; 
}`
The above snippet will result in:
Once the above link is visited it will lose the properties applied to it using `:link` class.

Change properties of visited links
<img-link_visited.png->
To change the properties of links which are already visited, visited pseudo class is used.
Visiting a link is nothing but clicking on it.
`<a href=”www.anywebsiteyoulike.com”>Click me</a>

//style.css
a:visited{
	color: black; 
}`
Once the link is clicked it will result in above

(Topic-2) Let's revise _ Pseudo Classes.

Which of the following pseudo classes is used to trigger the properties of element when it is hovered?
`Select the right answer`
`active`
`hover`
`link`
`visited`

Which of the following is correct the syntax to write pseudo classes?
`Select the right answer`
`selector;pseudo-class`
`selector pseudo-class`
`pseudo-class`
`selector:pseudo-class`

To select a link which is yet to be visited which pseudo class is used?
`Select the right answer`
`unvisited`
`link`
`visited`
`None of the above`

To select a link which is currently active which pseudo class is used?
`Select the right answer`
`unvisited`
`link`
`active`
`None of the above`


(Lesson-12) Writing CSS For Mobile

(Topic-1) Writing CSS for mobile

Writing CSS for mobile
<mobile.png->
We all are avid users of the mobiles and tablets.
It becomes necessary to make sure that the things developed are compatible and properly visible across all devices.

Media queries come to rescue.
Using media queries we can write styles based on screen sizes, specifically targeted to tablets, phones and desktops.

Writing media queries
To write media queries @media property is used.
It is written as follows:
`@media screen and (condition) {
	//Whatever CSS you want to write 
}`
Here condition consists of conditions involving height and width of screen.
And inside the media block we can write whatever CSS we want specifically for that screen size.

To write CSS for screen sizes wider than or equal to 720px, we can write
 @media screen and (min-width: 720px){
	p{
		font-size: 16px;
	}
}
The above CSS will change font-size of every paragraph to 16px on devices with screen size 720px or more than 720px.

Similarly,
max-width can be used to specify properties specifically for screen sizes equal to or less than specified.
On the same grounds max-height and min-height can also be used.

(Topic-2) Let’s Revise _ CSS For Mobile

Which of the following will apply CSS to devices with screen width equal to or smaller than 480px?
`Select the right answer`
`@media screen and (min-width: 480px)`
`@media screen and (max-width: 480px)`
`@media screen and (min-height: 480px)`
`@media screen and (max-height: 480px)`

Which of the following properties is used to write CSS for specific screen sizes?
`Select the right answer`
`pseudo-class`
`screen size`
`max-width`
`@media`