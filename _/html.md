HTML

(Lesson-1) Html Introduction

(Topic-1) Basic Structure of HTML
Ready to learn some basics about HTML?
An HTML document consists of 2 important parts:
Document Creation (what the users will see)
Tags (and how they see it)
Tag <html> is considered to be the head of the family.
It’s from this tag that the browser recognizes, it’s an HTML document.
PS- For every opening tag there is a closing tag like this: </html>.
The tag <html> is followed by the <head> tag.
This is a special one, and the content written inside is not displayed on the webpage.
It comprises of the title (of the browser window) or any other instructions, which you want to provide to the web browser.
For example:
 <head>
	<title> Welcome to the jungle!! </title>
</head>

The <head> tag is followed by the <body> tag, where the actual content that is visible on the webpage is written
i.e. all the visual elements such as headings, paragraphs, images etc.
Brilliant! You have unlocked the basic ingredients of an HTML document.
Time for some brain tease.

Question
Drag & rearrange in the appropriate order
`<head>`
`<body>`
`<html>`
`</body>`
`</head>`
`</html>`

(Topic-2) Something to Ponder

Before we move any further along this learning path, several questions may have popped into your head.
Do not worry, we can help you solve at least a few of them.

Question : How do Web Browsers interact with HTML?
Answer: Browsers are too proud, they just do not / cannot read the content directly from the place where it is stored.
To settle this conflict, web servers are used.
A Web Server acts like an intermediator, it patiently listens to the browser’s request and executes it for us.
The document delivered to the browser contains the HTML text, which is displayed just by identifying the tag <html> from the document.

Question: What makes HTML so powerful?
Answer: As it turns out, HTML is a very friendly language and is on good terms with almost all of the web browsers.
It isn’t needy and works out well using a simple text editor.
It is the least complicated when it comes to search engines.
So, are you interested in making a simple, stable, well-structured website? Then learn HTML :D

Question: Why isn't HTML a programming language?
Answer: Trust me or not, HTML is a fashion diva. It controls the presentation, structure and layout of the data on a webpage.
It just does not contain any functional or programming logic.
Manipulating data is not in its nature, neither does it perform tasks like, event handling, taking input and displaying output.
This is what makes it different from a programming language.
PS: There are no if-else conditions. :)

(Topic-3) Let’s Revisit

What is the first tag of an HTML document?
``Select the right answer``
`<body>`
`<head>`
`<html>`

Tags? Sorry I didn’t get you

Tags and text that are not displayed on the page are written under which of these tags?
`Select one or more answers`
`<title>`
`<html>`
`<head>`
`<body>`

To create a basic HTML document what are all of the things required?
``Select the right answer``
`Text Editor`
`Common Sense`
`Web Browser`
`All of the above`

(Lesson-2) Your First Web Page

(Topic-1) What is a Web page?

Web Page ?
Hey Browser! Here is some advice for you.
You should never stop listening to the Web server.
It always has some exciting content for you.

Team Work makes the Dream Work!
A webpage is the result of a team working together.
A Web Server can be hardware / software that lets you deliver the webpage to your browser.
Browsers just have to read and decode the instructions, displaying exciting content on the screen.
And we just realised, that’s what a web page is. :D

A web browser is a medium used to access and view ______ ?
``Select the right answer``
`website`
`webpages`
`google`
`all of the above`

(Topic-2) Your First Web Page

It’s time to put your learning to some good use.
We can start by opening a simple text editor like Notepad, TextEdit etc.
Try revisiting your mind palace and refer to the memory of the basic html structure that you have learnt.
The code uses the same structure.

 <html>
	<head>
	</head>
	<body>
		Yayeye!! This my first webpage.
	</body>
</html>

Now save the text file as .html or .htm file.
You can call it hey.html
Try opening the file in your web browser.
<img-of-webpage-above->
Ta-da! Here is your first webpage.
Isn’t it a beauty :D

Question
Did you notice which tag is responsible for displaying content on the screen?
``Select the right answer``
`<body>`
`<head>`

Did you notice anything in the previous code?
Indentation made it easy to understand.
The tags were written using lower case.
So, correct capitalization should be used throughout the code.
All tags were closed in the proper order.
If they weren’t closed properly the code won’t work.
PS: Indentation, is an art of providing space from the margin, to provide structure to the code.

The tags are written using what?
``Select the right answer``
`Only Numbers`
`Upper case`
`Lower case`
`Symbols`

(Topic-3) Brain Streak

You know what? We actually like you. With some basic knowledge you just built your first web page. Impressive!
Before moving ahead, we would like to tickle your mind :D

Try and display your name on the web page
<html>
	<head>
	</head>
	<body>
		Hey! This is Russian Developers.
	</body>
</html>

`Output:`
`Hey! This is Russian Developers.`
`Continue`

After writing the code, the text file should be saved with which extension?
`Select one or more answers`
`Let it be as .txt`
`.html`
`.htm`
`.png`

____ helps the browser by providing / delivering it web page.
``Select the right answer``
`The Mail Man`
`Web Server`
`HTML`
`God Knows`

(Lesson-3) HTML Tags

(Topic-1) The paragraph tag

Let’s make this learning roadmap of HTML more exciting as we move on.
Next on our way is the backbone of the HTML language.
Yes, you are correct, we are talking about HTML Tags.

Backbone of English Language!!
As coffee is to morning, a paragraph is to the <body> in a webpage.
Denotation: <p> & </p>
Location: It’s placed inside the body tag.
Usage: It lets you make new paragraphs.
Visibility: The text placed inside this tag will be visible on the main webpage.

Here is an example to take you through:
 <body>
	We are the jungle family
		<p>I’m the one denoted as a rabbit</p>
</body>
FYI: Putting one tag inside another is termed as Nesting.

When we open this code in our web browser it looks like this:
<img-of-above-snippet->

Can you place the <p> in the correct place?
``Select the right answer``
<head>___</head>
<body>___</body>


(Topic-2) The break tag

Let’s move to the next line.
Writing sentences in a new line provides symmetry to the writing.
The break tag lets you start a sentence from a new line in HTML.
Denotation: <br>
Location: It’s placed inside the body tag.
Usage: Lets you start from a new line.
Special Characteristic: It’s a self-closing HTML Tag.

We have been waiting for you to ask this question: What is a self-closing HTML tag?
The opening and closing are both included under same tag.
Not all tags can be used in such a manner.
Identified by the forward slash towards the end.

Here is an example
 <body>
	<p>I'm just here to help the break tag.<br> 
	These people are mean. I don't wanna be a porcupine.
	</p>
</body>
<img-of-above-snippet->
This is how the text will be displayed:
For better understanding try displaying the above without using <br>
Hint: It would all be in the same line.
The route map has started to take some interesting turns, let’s continue to travel down it.

<br> is a ___?
`Select the right answer`
Self-Closing tag
Closing Tag
Opening Tag

(Topic-3) Headings in HTML

Helps Prioritize!
We tend to prioritize the important stuff. In HTML we make use of headings.
Denotation: <h1></h1>, <h2></h2>, <h3></h3>, <h4></h4>, <h5></h5>, <h6></h6>
Location: It’s placed inside the body tag.
Usage: <h1> to <h6>-arranged on basis of priority (<h1>- highest)
Visibility: The text placed inside this tag will be visible on the main webpage.

Still not clear? Don’t you worry, this example will resolve any confusion.
<body>
	<h1>Hey There! I'm Heading 1</h1>
	<h2>Hey There! I'm Heading 2</h2>
	<h3>Hey There! I'm Heading 3</h3>
	<h4>Hey There! I'm Heading 4</h4>
	<h5>Hey There! I'm Heading 5</h5>
	<h6>Hey There! I'm Heading 6</h6>
</body>
<img-of-snipet-above->
Isn’t it amazing how you can sort the important stuff from the content, just by providing a suitable heading structure.
We just wanted to check if we are on the same page (It was a pun intended [same page :D]).
Here is a question to be sure.
In accordance with the output we got on the last screen.

`Select one or more answers`
`Heading 3 had more priority over Heading 1 & Heading 2`
`Heading 4 had more priority over Heading 5 & Heading 6`
`Heading 3 is a guy with moderate priority`
`I don’t know what you are talking about.`


(Topic-4) Bold, Italics Underline

Bold, Italics, Underline
There are different tags present to format the content on a web page. Let’s learn about them.

The bold tag
Denotation: <b> </b>
Location: It’s placed inside the body tag.
Usage: Lets you mark the text bold to showcase importance.

The italic tag
Denotation: <i> </i>
Location: It’s placed inside the body tag.
Usage: Lets you mark the text in italic font.

The underline tag
Denotation: <u> </u>
Location: It’s placed inside the body tag.
Usage: Just in case you want to underline a text.

Now it’s time to make use of these tags:
 <body>
	<p><b>Hey, What's up? See I am BOLD</b></p>
	<p><i>Everything looks tilted from this angle</i></p>
	<p><u>Now, that's a straight line</u></p>
</body>
PS: We have included everything in a separate paragraph.

Once you try running the code, The content will automatically change, see below:
<img-of-snippet-above->
Time for a little pat on you back. You just crossed the most difficult hurdle.
Bravo, Let’s Continue.

Match the respective pairs-
`Click to match the appropriate answers`
<b>     <---> `A line generally follows me`
<i>     <---> `I’m the strongest`
<u>     <---> `This is how I write`

(Topic-5) Quizzing Up!

Correct HTML tag for the largest heading is?
`Select the right answer`
`<heading>`
`<head>`
`<h1>`
`<text>`

What is the correct HTML tag for inserting a line break?
`Select the right answer`
`<break>`
`<br>`
`<new>`
`<lb>`

Which of the following tags have pair tags?
`Select the right answer`
`<body>`
`<head>`
`<b>`
`All of them`

(Lesson-4) Some Special Tags

(Topic-1) The image tag

Picture time :D
Have you ever made a picture collage? It does look good, right?
We can also make our webpages more interactive by adding images to it using <img> tag.
Denotation: <img/>
Location: It’s placed inside the body tag.
Usage: Let’s help you add an image to the page.

The tag is used like this:
<img src=”image’s path”/>
src is an attribute to include the image’s path
An attribute Provides additional information about your html tag.

The page would look like this
FYI: The image’s path can also be an image URL.
 <body>
	<img src="www.google.com/images/KungFuPanda.png"/>
</body>
<img-of-snippet-with-displayed-image-above->
Let’s move on to learn another special tag.

Don’t get confused, attributes are explained in detail in a later section.
Let’s try this.
 <body>
	<img src="GrumpyPanda.png"/>
	<p>I ain't angry :/ </p>
</body>
FYI: For simplicity we’ve saved all our images and files in the same folder. Hence just the image name was included.

(Topic-2) The division tag

Into the sections!!
A simple straight webpage, will it look good and be appealing? Of course not.
Hence, the div tag comes into the picture
Denotation: <div> </div>
Location: It’s placed inside the body tag.
Usage: Let’s get you to divide the page into sections.

Let’s give this a try:
 <body>
	Can I meet my other half? Please. 
	<div>
	<p>Don't worry, I'll meet you soon</p>
	</div>
</body>
Isn’t it amazing to learn how this language works.

Do you remember which of these were self-closing tags?
`Select one or more answers`
`<img>`
`<html>`
`<br>`
`I’m too proud to answer.`

(Topic-3) The title tag

What’s there in the title?

Just like the title of Mr. or Ms. adds meaning to your name, similarly you might have noticed the text in your browser window?
That’s the use of a title tag.
Denotation: <title> </title>
Location: It’s placed inside the head tag.
Visibility: Not on the main page
Usage: Lets you provide special instructions to the browser.

Want to see how it works? Try doing this:
<head>
<title>Can you see me?</title>
</head>
<img-of-snippet-above->
Check your browser window, you’ll be able to see the text written inside <title> tag
FYI: <title> tag is very helpful for search engines.

Can you place the <title> in the correct place?
`Select the right answer`
`<head>__</head>`
`<body>__</body>`

(Topic-4) The anchor tag

Foodies, if we had a connecting door to the kitchen, directly from our room, wouldn’t that be fun?
Similarly, to embed other web pages’ links to your web page, an anchor tag is used.
<img-of-connect.png-->
Denotation: <a> </a>
Location: It’s placed inside the body tag.
Usage: Linking between web pages.

Here is, how you can use it:
 <body>
	<a href=”https://intellect.techa.tech/>I think you should try clicking this</a>
</body>
href- is another attribute used to define the link.
The link gets displayed like this.
<img-of-link-snippet-above->
`I Think you should try clicking this`
That's quite a pace you have achieved.

(Topic-5) Let’s Revise!

Let’s revise
Write your name inside the tag to display it on browser window
`Select the right answer`
`<title>Rashika</title>`
`<p>__</p>`
`<a>__</a>`
Hey Browser, please display it for me.

There is a tag that helps to create sections in your web page. What is that?
`Select the right answer`
`Subtraction`
`Addition`
`Division`
`Break`

Try filling the correct attribute name
<a _____ = "https:/intellect.techa.tech/welcome">The next webpage</a>
<img _____ = “SomeImageName.png”/>
`Tap the correct answer to fill in the blanks`
`href` 
`src`

(Lesson-5) HTML Attributes

(Topic-1) What is an Attribute?

What is an attribute?
Do you people mind having some extra money in your pockets?
Neither does the browser.
So, an attribute just gives some extra information about the HTML element to the browser.
It can be a property related to width, height, or color of an object.
The attribute is made up of 2 parts:
`Attribute Name`
`Attribute Value`
`‘=’ is used to set the value`
`“ ” the value is placed inside the double quotes.`
`It’s like attribute=”value”`

Choose the correct numbers that represent tags with attributes-
`Select one or more answers`
`<p style="color:red">I am an attribute</p>`

`<a href="https://www.intellet.techa.tech">This is an attribute</a>`

`<p>I am an attribute</p>`

`<body>I am an attribute</body>`

(Topic-2) The Basic Attributes

The Basic Amenities
Can you recall, what was the attribute used with the <a> tag?
`Select the right answer`
`src`
`alt`
`href`
`title`

A secret passage to the hidden treasure, how exciting!
href forms the same passage between the two web pages/documents.
In layman terms, it lets you provide the link of the web page to allow the user to connect to other webpages.
 <a href="https://www.intellect.techa.tech/welcome">Check out the link to complete awesomeness</a>

Can you please fill this for us, we are too tired?
 <img _____ = ”image.jpg”/>
`Tap the correct answer to fill in the blanks`
`src`
`href`

Ever noticed the arrows on a subway that mark our path to the exit?
The src attribute lets you provide the path for the image in a webpage. It instructs the browser where to look for the image.
 <img src="image.png”/>

You can define a width, height etc. for an image using these attributes:
alt: Defines text/name for an image. Just in case it can't be displayed.
width: An optional attribute to set the width of the image.
height: An optional attribute to set the height of the image.

All being put to use.
<img src="image.png" width="200" height="400"/>
<img-of-displayed-image-above->

Try removing src to see how alt works.
 <img width="200" height="400" alt="Hey People, Good Day"/>
 <img-of-<img-tag-above-without-src->
This might have provided you with a clearer picture.

Can you help us fix this statement?
<img src=image.jpg, width=”10 height =17 alt="Hey People"/>
`Select one or more answers`
`Incorrect usage of quotes`
`Tag itself should not exist`
`Incorrect use of a comma`
`There is nothing wrong`

(Topic-3) The style attribute

Let’s stylize the page.
<img-of-attr.png->
The style attribute does the final touch up of the HTML elements. It lets you change, or add different styles to it. It can be in the form of background color, size, etc.
FYI: This is just a basic description, this will be explained in detail in our CSS course.
There is a simple syntax:
style=”property:value”
The property implies basic color, the font-size gives the property of an element
 <h4 style="color:green">Can we change this to red please?</h4>
<p style="font-size:200%">No Green looks better</p>
<img-of-snippet-above->
This is how the changed text look.
PS: It’s a generic attribute and can be used with any of the html tags. Don’t get confused, it’s similar to changing colors and size in a Word document, but by using HTML.
Try doing it for yourself.
Ready to change the background color?
Hint: property: background-color changes the background color of the text
 <h1 style="background-color:orange">Try typing your name here</h1>
And the output for the user can be displayed, like this:
<img-of-<h1>-tag-above->
`Awesome, let’s continue`

(Topic-4) A short revisit

Can you match the attributes with the respective tags they are used with ?
`Click to match the appropriate answers`
`<img>`  <-----> `href`
`<a>`  <-----> `style`
`<p>`  <-----> `src`

Which of the attributes can be used with all the html tags?
`Select the right answer`
`src`
`alt`
`title`
`style`

The way the browser displays an object can be modified by ____
`Select the right answer`
`containers`
`attributes`
`parameters`
`None of the above`

(Lesson-6) The Final Webpage
(Topic-1) Our Journey So Far

It’s been an interesting one.
<img-of-journey_so_far.jpg->
Let’s quickly take you through all that we have learned so far.
HTML- Hyper Text Markup Language.
The special connection it shares with the browser.
How easily the browser understands and responds to it.

We came across the lifeline of the HTML language,
Yes we are talking about tags.

Some turned out to be the roots- <html>, <head>, <body>.

Some turned to be the branches- <p>,<h1>..<h6>, <br>

Some turned out to be the special fruits- <div>, <a>, <image>, <title>

Now these make use of some special seeds to enhance the usability.
We are those special seeds that provide the so powerful special tags -- href, src, style.

The style attribute, carries more features with it- font-size, color, background-color.

(Topic-2) Your own webpage

Don’t worry, we’ll do it step-by-step.
It’s time to open your text-editing documents.
Save it as Mywebpage.html (or any other name).
For Simplicity, we save our files and images in the same folder.
1. It’s time to open your text-editing documents.
2. Save it as Mywebpage.html (or any other name).
3. For Simplicity, we save our files and images in the same folder.
4. Now I think it is time to start writing the code.

<html>
<head>
	<title>Now you know me</title>
</head>
<body>
	<div>
		<h1>The Curly Cute One</h1>
		 <h2>I am, ‘THE PANDA’</h2>
	</div>

5. Let’s try adding an image to the previous text.
 	<div>
		<img src="Panda.png" width="190"/>
		<br>
		<b><i>Keep Calm, And Follow My Diet</b></i>
		<br>
		<i>FYI, I just roll and eat</i>
	</div>

6. Let’s add some description by using the paragraph tag
 	<div>
		<p>Let me Introduce myself-<br>
		I am the one featured on all social platforms,<br>
		as a lazy roly-poly creature. Trust me, I ain't lazy :/
		</p>
	</div>

7. Let’s type this in a different color.
 	<div>
		<p style= "color: purple">
		It's just I get easily tired.<br>
		Surprisingly, It turns out I am the spirit animal for most of the humans.
		</p>
	</div>  
Want to add a background color to the above text?
Let’s add it

8. Just notice how we can add more than one properties to the style attribute.
 <div>
	<p style= "color: purple; background-color: yellow; width:25%">
	It's just I get easily tired.<br>
	Surprisingly, it turns out I am the spirit animal for most of the humans.
	</p>
</div>
PS: Try, using with and without width.

9. Let’s try referring to another webpage
Hint: The <anchor> tag
<div>
		<h5>We’ll keep taking you back to experience the awesomeness :D</h5>
		<a href="https://www.intellect.techa.tech/prev/css">
Let's try and click this one more time
		</a>
	</div>
</body>

Excited enough to check how your webpage look.
Open the html file in the browser.
Bazzinga!!
<img-of-your_first_webpage.png->
Isn’t it amazing? You just created your own webpage.

You’ve mastered the art of learning and creating your own webpage. Time to pat yourself on the back and celebrate.

This is just the first step, before leaving we will provide you with a brief description about HTML5.

(Topic-3) Our Learnings

Which tag, and attributes, were used to introduce the panda to the page we created?

`Select the right answer`
`<img>, src, width`
`<title>, src`
`<a>, href`
`<p>, style`

Which tag helped us in adding hyperlink to the webpage?

`Select the right answer`
`<img>`
`<a>`
`<b>`
`<h1>`

background-color: yellow was set under which attribute?

`Select the right answer`
`src`
`attri`
`style`
`color`


(Lesson-7) HTML5 Introduction

(Topic-1) Introduction to HTML5

Hurray!!
Congratulations on your newly achieved success!!
Cheers for keeping up with us.
So, before we say our final goodbyes, it’s our responsibility to upgrade you a little with the ongoing trends in HTML.

HTML5?
<img-of-html-5->
New updates generally leads to a better and smooth working of an application.
Such is the new and fifth version of HTML.
It was designed to deliver rich and enhanced media support.
This side of it lets you develop complex web applications.
Applications that run on a webserver and are accessed using a browser.

Various new elements and tags are added to make it more interactive.
The basic structure still remains the same with some minute changes (will discuss later)
It helps with cross platform development (click on Next to learn about it)

Cross platform means developing, applications and software for more than one platform such as web, desktop, mobile etc.
Coming back to the introduction, special tags have been added too, for embedding audio and video into the web page.
Let’s learn how it is different from basic HTML in the next topic.

HTML5 has been modified to include which of these characteristics?
`Select one or more answers`
`Cross Platform Application development.`
`Nothing special, they didn’t like the name so just changed it to HTML5.`
`To Develop Complex Web Applications`
`For better media support`

(Topic-2) How is HTML5 different from HTML

HTML5? HTML?
We are as excited as you are, about learning HTML5.
So, the first difference that you’ll notice is doctype declaration.
Denoted as: <!DOCTYPE html>
Don’t get confused, we’ll explain it to you in detail.

DOCTYPE declaration tells the browser in which version of HTML the page has been coded.
It is always the first line of a HTML document.
PS: It’s not a tag. Hence it doesn’t require a closing tag.

Unlike HTML, HTML5 has content specific elements, e.g. <header>, <footer>, <section> etc.
So, if we want to fix a specific text in Header and Footer, we just need to add the content inside the respective tags and TaDa!! :D

There is one more exciting feature which has been added in HTML5, it is GeoLocation.
Using this, the location of the site visitor can be discovered.
This feature is brought to life using the geolocation API.
Don’t worry, you’ll find out about it while learning HTML5 in detail.

<!_________ html> is not an HTML tag but the first line of an HTML5 document.
`Select the right answer`
`DOCTYPE`
`TITLE`

(Topic-3) Some Newly Added Tags

Let’s introduce you to some new tags.
To make this more exciting, let’s introduce you to some newly added tags.
Location for all: Placed inside <body>
1. <header> & </header>: Contains the introductory part of the page. You can add brand’s name, image, logo etc. <h1>..<h6> can be used to make it more approachable.

For any website have you noticed that information like Privacy Policy, Copyright Information, Contact etc. are at the bottom of the webpage.

2. <footer> & </footer>: Let’s use the above collected memory and put that inside <footer> TaDa! your web page will also display the same at the very bottom.

3. <nav> & </nav>: In a web page, have you ever noticed links like Home, Profile, My Account in a single section. Those all can be added under <nav>, to group them under one particular area.

4. <article> & </article> : Has a dedicated place for itself in the webpage. You can consider the example of a comment box, blog etc.

We have dutifully guided you through all this and we are so proud of it :D
Time to pat yourself on the back for this new achievement 🏆.

<______> is a replacement for <div>.
Select the right answer
<footer>
<article>

The tag which lets you add all the navigational links in a dedicated area?
`Select the right answer`
`<header>`
`<nav>`
`<footer>`
`<a>`


(Topic-4) Let's Answer These!

Which of the following is not an element in an HTML document?
`Select the right answer`
`<html>`
`<body>`
`<!DOCTYPE>`
`<title>`

Which of the following is not a semantic element?
`Select the right answer`
`<html>`
`<article>`
`<nav>`
`<footer>`

Which element is used to define a discrete unit of content such as a blogpost, comment, and so on?
`Select the right answer`
`<header>`
`<article>`
`<footer>`
`<head>`

HTML5 documents contains a ___________ element, used to set the header section of a document like a logo
`Select the right answer`
`<header>`
`<article>`
`<title>`
`<nav>`

(Lesson-8) The Final Adieu

(Topic-1) The Final Adieu

Time to liven up your brains a little.
Let’s do this

Try rearranging the code to display the content on the page
Drag & rearrange in the appropriate order
`It has been a wonderful`
`</p>`
`Journey so far`
`<p>`


Can you fill the opening and closing tags of every html document for us?
< ________>  & </_______>
`Tap the correct answer to fill in the blanks`
`<html>` | `</html>` | `<header>` | `</header>`

Do you remember the only friend of <head> that we have learnt so far?
<html>
<head>
	<_____> What’s up <______>
</head>
</html>

`Tap the correct answer to fill in the blanks`
`<title>` | `<article>` | `</title>` | `</article>`

Can you fill in the below tag please, to help us start from a new line? it’s a self-closing tag
<body>
Pizza is love <_____/> So are hamburgers
</body>
`br` | `break`

<img-of-<p_tag.png>->
Do you remember which one of these attributes were responsible for the image’s text above?
`Select the right answer`
`href`
`src`
`alt`
`width`

Do you guys remember the tag responsible for the largest heading?
`Select the right answer`
`<body>`
`<h1>`
`<heading>`
`<h6>`

What does the href attribute contains?
`Select the right answer`
`The link/URL of the new web page to be linked`
`Just the name of the page`
`Browser’s name`
`Anything that’s blue`

Which property of the Style attribute lets you add background color to the text?
`Select the right answer`
`<div style=”bg:blue”>`
`<div style=”background-color:blue”>`
`<div style=”color:blue”>`
`<div style=”bground:blue”>`

2 or more properties in a style attribute are separated by which one of these?
`Select the right answer`
`;(semicolon)`
`,(Comma)`
`:(Colon)`
`!(Exclamation mark)`

There are 2 self-closing tags that we have learnt about, can you fill them for us?
<body>
	We think it’s time for you take a break!<______/>
	<____ src=”image.jpg”/>
</body>
`Tap the correct answer to fill in the blanks`
`br` | `img` | `href` | `div`

Using one HTML tag inside the other was termed as?
`Select the right answer`
`Fasting`
`Mind Blasting`
`Testing`
`Nesting`