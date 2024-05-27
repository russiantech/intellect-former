
HTML ADVANCED

Lesson-1(Introduction To Advanced HTML)

(Topic-1) Recap to Basic HTML

Time Travel into the Past
Hola People! Welcome back to the world of HTML. Let’s quickly look at what we have learnt up to now.

HTML : Yes, I agree that I am a Markup Language and share a strong bond with the browser and the webserver.

My basic structure comprises of elements like tags and attributes. All of them make me feel special.

Tags : We help HTML evolve and mutate. I have so many different names which can be used, as per the requirements of the webpage.
For Example <html>, <head>, <body> are used for providing basic structure.
a strong bond with the browser and the webserver.
My basic structure comprises of elements like tags and attributes. All of them make me feel special.
Tags : We help HTML evolve and mutate. I have so many different names which can be used, as per the requirements of the webpage.
For Example <html>, <head>, <body> are used for providing basic structure.
Then <p>, <h1> to <h6>, <br> for structuring the content.

Tags : Do you remember the special ones I carry with me? Let me help you to remember. <div> <a>, <image>, <title>
The above tags helps you to make your web page more interactive.

Select the right answer
How can we change the size of an image?
`<img src="image.png" alt="200%">`
`<img src="image.png" height="20%" width="10%">`
`No you just cannot do it`
`<img src="image.png" size="200%">`


Attributes : Let me tell you a secret, tags alone won’t help you enjoy the entire journey. We make them interesting and effective. We have different names.

href : You can use me with the anchor tag
src : You can use me with the image tag

style : I rule the presentation of the document. You can use me in paragraphs, headings, body etc..

Can you help us add a hyperlink to our webpage?
<
href="https://www.instagram.com/intellect/">Come and learn to code !</
>

Tap the correct answer to fill in the blanks

`a/` | `a` | `div` | `/div`


(Topic-2) Addition to Basic HTML tags

Newly added
Fear of Missing Out. Nobody wants to miss out on anything these days, such is our digital world.
Did you know that style can be used as a HTML tag?
We can build a new form, a table, we can even prepare a list just by using the <form>, <table>, <li> tags.

Using style as an element is termed as embedded style.
Denotation: <style> & </style>
Location : It’s placed inside the head tag.
Usage: It lets you enhance the look and feel of the webpage.

Let’s see how it is done.
 <html>
	<head>
		<style>
			<-- All headings visible with purple text color -->
			h1 {
				color:purple;
			}
			<-- All paragraphs text print in blue color -->
			p {
				color:blue;
			}
			<-- Background color of the body should be powderblue -->
			body {
				background-color:powderblue;
			}
		</style>
	</head>
	<body>
		<-- This is a Heading -->
		<h1>Hey, We meet again!!</h1>
		<-- This prints a paragraph-->
		<p>This time with Advanced features.</p>
	</body>
</html>

This is how the changed screen looks.
`<image of the changed screen here/>/the html snippet above`
This is how it's done, using embedded style. We’ll be learning about the other new tags in the next module.

We just told you about using style as a HTML Tag, What is it termed as?
`embedded style`
`Select the right answer`
`tag styling`
`embedded style`
`just style`
`inline styling`

(Topic-3) Let’s Revise - Introduction To Advanced Html

Do you remember learning about an HTML element which can be used both as a tag and an attribute?
`Select the right answer`
`style`
`head`
`body`
`style`
`anchor`

We want to make the background color ‘blue’ for our webpage using embedded styling
<style>
	body {
background-color
: blue; }
</style>
`Tap the correct answer to fill in the blanks`
`head`
`body` | `head`

In HTML we have _________ type of heading tags.
`Select the right answer`
`6`
`7`
`8`
`6`
`5`

(Lesson-2) Creating an Input Field

(Topic-1) Enhancing The Basics HTML

Creating an Input field
You might have noticed quite often websites want you to type information like your name, passwords etc. Here is a simple solution, 
use the input tag.
It comes as a package, with various attributes like id, name, type, placeholder etc.
PS: Don’t panic people, we’ll explain these attributes in detail.

Denotation: <input>
Location : Place it as per your convenience
Usage: Let’s you take input from the user
Special Characteristic: It’s a self closing HTML Tag
Common Attributes: id, type, name, placeholder, value.

Let’s make this more clear in our heads:
 `<-- This will print a paragraph with text color red and a textbox -->`

<p style="color:red;">
	Hey, Yes you. Can I have   your number please:
	<input type="text" placeholder="Number please">
</p>

We just love the color red, so we stylized our paragraph.

See, now even we are able to gather input from the user.
`<mage-of-styled-<p>-tag-above>`
Did you notice, the use of placeholder attribute. Think about it, we’ll get back to it.

Try and display a radio button on the webpage.
`text` | `radio` | `ssubmit` | `checkbox`
`<-- this will display a Radio button--> ` 
`<input type="___"> Yes`

`<-- This will print a paragraph -->`
`<p>Are you enjoying this ride with us?</p>`
`<p> Sorry :D You ran out of options </p>`

(Topic-2) Let’s Create a Form

The Interactive Section

Do you remember filling and submitting an application form online? We can create one using the <form> element.
The simplest form comprises of Text fields, Radio Buttons, CheckBoxes and a ‘Submit’ button.
Hint: You can always make use of the <input> tag.

Denotation: <form> </form>
Location : Place it as per your convenience (<body>)
Usage: Lets user enter data and submit it
Tags Involved: <input>, <button>, <label>
Common Attributes: action, type, id, name, value

The term, used for placing one tag inside another is called _____
`Select the right answer`
`Nesting`
`Egg-Sitting`
`Looping`
`Nesting`
`Trekking`

Let us explain this to you using a small code.
 <-- This will create a form -->
`<form action="/my-handling-form-page">
	<-- A textbox shows with label 'Name' -->
	Name: <input type="text"><br/>
	<-- A textbox shows with label 'Email'-->
	Email: <input type="text"> <br/>
	<--   Radio buttons created for Selecting Male or Female -->
	Gender: <input type="radio" name="gender" value="male">Male
	<input type="radio" name="gender" value="female">Female <br/>
	<-- This will show a Submit button -->
	<button   type="submit">Submit</button>
</form>`
`<image-of-the-form snippet-above>`

There’s your webform!

Let’s change this to something you may prefer:
action: Lets you define the location, where your collected data is submitted
name, value: Lets you specify name, value for input element. Used as a reference when the form is submitted

Rearrange the below code for creating a simple form
`Drag & rearrange in the appropriate order`
`<form>`
`First Name: <input type="text"><br>`
`Last Name <input type="text">`
`</form>`

For creating a submit button, which attribute contains the “submit” value?

`type`
`name`
`class`
`That’s not even a question!`

(Topic-3) Let’s Table this!

Creating tables in HTML
We all know how important it is sometimes store information in a ordered manner. That’s what tables are there for.
In HTML we use <table> element to create one.
<tr>, <td>, <th> are used to create rows, cells and headers.

Denotation: <table></table>
Location : Inside the <body> element.
Usage: Lets you arrange data in rows & columns.
Tags Involved: <tr>, <td>, <th>.
Common Attributes: align, border, cellpadding, cellspacing.

Let’s create a table:
 <-- This will create a table with border -->
<table border="1">
	<-- This will create a row -->
	<tr>
		<-- This   prints a Heading-->
		<th>Dogs</th>
		<-- This prints another Heading-->
		<th>Cats</th>
	</tr>
	<-- This will   create another row -->
	<tr>
		<-- This will create a column-->
		<td>1</td>
		<-- This will create another   column -->
		<td>0</td>
	</tr>
</table>

`<image-of-created-table-snippet-above>`

We just drew a table
Headings, by default, are bold & center aligned.

Can you help us create a table by filling in the correct answers?
<table border=”1”>
	<__>
		<td>Gelato</td>
		<td>Blueberry</td>
	<__>
</table>
`Select the right answer`
`tf`
`style`
`row`
`tr`

(Topic-4) Creating a List

Can you help us choose all the elements to design a basic form
`Select one or more answers`
`<head>`
`<form>`
`<input>`
`<button>`

A table row is displayed using _____ and the column using _______ .

`Select one or more answers`
`<tr>`
`<th>`
`<td>`
`<tc>`

Which of the following elements do we use for defining the content of a list?
`Select the right answer`
`<list>`
`<li>`
`<il>`
`<ul>`


(Lesson-3) Time To Learn HTML5 !

(Topic-1) Introducing HTML5

Time to move-on
As they say, a new day brings new hope. Such is HTML5 to us.
It is the 5th and latest version of HTML.
It lets you include rich content like, animation, graphics, videos etc on your webpage and marks its presence with <!DOCTYPE html>.

Do you guys remember the html element for creating line breaks?
Select the right answer
`<space>`
`<tr>`
`<br>`
`<dr>`

HTML5 lets you build more interactive forms & web applications.

It removes the need for additional browser plugins.

For a better semantic structure, new elements like header, footer, article etc. are introduced.

Semantic, in layman’s terms means meaningful.

User Experience & User Design both can be enhanced using HTML5.

Leads to a search engine friendly website with new attributes.
Geo-Location support is also provided by HTML5.

Character Set used within the webpage can just be defined using <meta> tag and charset attribute in HTML5.
<meta charset=”UTF-8”>
`UTF-8`, default character encoding used by HTML5.

What are all the new features we get with HTML5?
`Select one or more answers`
`Better media support`
`Cross platform application development`
`New semantic elements to replace most of <div> elemen`ts
`Nothing different, it’s the same`


(Topic-2) Welcoming new elements

All new html elements
New friends have always been welcomed into our lives, so are new elements to HTML5.
<!DOCTYPE html>- for all browsers to be on the same page.
For semantic structure: <header>, <footer>, <article>, <section>, <nav>.
Media Tags: <audio, <video>, <canvas>.
Better Forms with: required, min, max, autofocus, <datalist>, <output> many more..

Time to say Goodbye !
<center> - Centered Alignment
<font>, <u>, <strike> - Font-color, size, underline and strike-through text
<dir> - Directory

Some deprecated attributes.
Elements Removed - width, height, rules, summary
Usage - Attributes of <table> for studying rows and columns.
Name - Specifies name of an input element, deprecated for <form>  but not other elements.
type - Deprecated for <script> used for writing javascript in HTML. Type helps you identify the content in-between.

(Topic-3) Time for some Brain Streak

HTML5 marked its presence with
Select the right answer
`<DOCTYPE! html>.`
`<!DOCTYPE html>.`
`<!HTML doctype>.`
`<!DOCTYPE>.`

Do you remember the names of the newly added tags in HTML5?
Select one or more answers
`<canvas>`
`<div>`
`<header>`
`<audio>`

Which tag can be used for defining character encoding?
`Select the right answer`
`<charset>`
`<div>`
`<meta>`
`<audio>`

What are the various tags not present in HTML5?
`Select one or more answers`
`<center>`
`<font>`
`<u>`
`<audio>`


(Lesson-4) Providing A Semantic Structure

(Topic-1) Header of a webpage

Content that goes on the top
‘Semantic’ signifies meaning or finding logic. So, semantic elements clearly know their content.
To provide a semantic structure using HTML5, we generally ‘Divide and slay’.
Let’s start with the header element.

<image-showing-correct-html-page-structure-header-navigation-content-<aside>-or-<sidebar>-<footer>->

Just like a blog in a magazine has a header where the names goes, for a webpage we follow the same notion.
Denotation: <header> </header>
Location : Inside the <body>
Usage: Acts as a safeplace for your headings(<h1>..<h6>),introductory content. You can even place your website’s logo here.

Let’s take a quick look.
 <header>
	<-- This will print a Heading -->
	<h1>Always bold and big!</h1>
	<-- This will print another Heading -->  
	<h2>Don't underestimate me</h2>
 <header>

<image-of-snippet-above->

We can use as many headers as we want in a webpage.
Making life easier for headings.

Why do you think Semantics is important?
`Select one or more answers`
`For a better structure of a website`
`Makes code more efficient and readable.`
`Just for fun and gags.`
`Provides better accessibility to a webpage`

(Topic-2) Footer of a webpage!

The last section.
<image-showing-footer-section-of-a-web-page->
The same magazine blog would have a footer where the author’s name goes.
In HTML5, Contact information, other web links, Copyright etc of a webpage is segregated using <footer> element.
Denotation: <footer> </footer>.
Location : Inside the <body>.

Let’s have a look at this small code:
 <-- This will create a footer of the webpage -->
<footer>
	<-- This will print a paragraph -->
	<p>
		<-- This will   create a hyperlink with Text Contact -->
		<a href="contact.php"> Contact</a>
		<-- This will create a hyperlink with   Text Blog-->
		<a href="blog.php"> Blog</a>
	</p>
	<-- This will print another paragraph -->
	<p>All rights   reserved</p>
</footer>
You would have noticed, this is the footer content for most websites.
<image-of-footer-snippet-above->

What, according to you, are the purposes that the footer serves?
`Select one or more answers`
`Section for adding messages or reviews.`
`Section for displaying authorship, copyright information.`
`Ignores that section of the webpage.`
`Better Semantic structure and displaying related links`


(Topic-3) The Navigation Section
<image-of-navigation-part->
The menu card in a restaurant has pages marked that guide you to the respective food sections.
The major navigational links of a webpage are like a menu, About etc. are gathered together under the <nav> element.
Denotation: <nav> </nav>.
Location : Inside the <body>.
Creates a neat horizontal menu for major navigational links.

Let’s see how it is done!
 <-- This will create a section in webpage where links are present -->
<nav>
	<-- This will print a paragraph -->
	<p>  
		<-- This will print the texts in bold -->
		<b>Major links of a webpage</b>
	</p>
	<-- This will create a   hyperlink with text About -->
	<a href="About.html"> About</a>
	<-- This will create a hyperlink with text Gallery -->  
	<a href="Gallery.html"> Gallery</a>
	<-- This will create a hyperlink with Text Blog-->
	<a href="Blog.html">   Blog</a>
	<-- This will create a hyperlink with Text Menu -->
	<a href="Menu.html"> Menu</a>
</nav>

<image-of-snippet-above->

We hope you remember using the <b> tag for styling characters in bold.

We can use the <nav> element within the <header> element?
`Select the right answer`
`True`
`False`

(Topic-4) Let’s take a step back!

The following elements <header>, <footer>, <article>, <nav> are together called _____:

`Global Attributes`
`Multimedia Elements`
`Semantic Elements`
`Graphic Elements`

_____ element serves to encapsulate a group of links that works as a collection of offsite links, site navigation, major webpage links.
`Tap the correct answer to fill in the blanks`
`head`
`nav`

Can there be more than one header or footer in a web document?
`Select the right answer`
`True`
`False`

(Lesson-5) More To Semantic Structure

(Topic-1) The Generic Section

It’s different from <div>
Just like a small paragraph on a book’s page.
The section element in HTML5 comprises of the descriptive content like paragraphs of a webpage ,which can be grouped by different headings.
Denotation: <section> </section>.
Location : Inside the <body>.
Usage: Marking up different sections of a webpage

Check this out!
 <-- This will create a section in webpage -->
<section>
	<-- This will print a Heading-->
	<h3> A day in the life of a   sloth</h3>
	<-- This will print a Paragraph -->
	<p>Sloths have always been a spirit animal, for people who love to   sleep.</p>
	<-- This will print another Paragraph -->
	<p>But they only sleep upto 10 hours a day.</p>
</section>

<-- This will create another section in webpage -->
<section>
	<-- This will print a Heading-->
	<h3>Are they really   so slow?</h3>
	<-- This will print a Paragraph -->
	<p>No, they just conserve energy.</p>
</section>
Have a sloth day!
<image-of-<section>-snippet-above>
Learning- The content inside <div> does not have a special meaning whereas in.
<section> our core intention is to divide on the basis of meaning.

How can we distinguish between two section tags?
`Add different headings to them.`
`How does it matter?`
`Place it inside the <nav>.`
`No, we cannot do that.`


(Topic-2) Streamlining the content

Just another article!
Just like an article which is unique and independent. 
The <article> contains content like blog/forum posts. The comment is also an example.
Denotation: <article> </article>.
Location : Inside the <body>.
Usage: Reusable, meaningful, independent components of a webpage.

Give us chance to explain this:
 <-- This will create an article content-->
<article>
	<-- This will print a Heading-->
	<h2>Avengers: Infinity War</h2>
	<-- This will print a Paragraph -->
	<p>
		It's going to be an epic. Thanos, dude you need to relax.
	</p>
	<--   This will print another Paragraph -->
	<p>
		For reviews, keep following the article.
	</p>
</article>

It’s worth the wait.
<img-of-<article>-snippet-above>
<article> can always be used as a child to the <section>.

Can <article> be a part of <section> element?
`Select the right answer`
`True`
`False`

(Topic-3) The aside element

Last but not least.
Remember this sidebox Did you know, we encountered while reading?
Content which is indirectly related to the main content, but is still important, is clubbed together under the <aside> element, tangentially.
Denotation: <aside> </aside>.
Location: Inside the <body>.
Usage: Used as a sidebar; additional content which makes the main content look more useful can be placed inside <aside>.

 <body>
	<-- This will print a paragraph -->
	<p>
		Tony Stark is a part of the movie Infinity Wars.
	</p>
	<-- This will   create a sidebar -->
	<aside>
		<-- This will print a Heading-->
		<h4>Tony Stark</h4>
		<-- This will print a   paragraph -->
		<p>He is the Iron Man !!</p>
	</aside>
</body>
This will surely help you understand it in a better way.
<img-of-snippet-above->
Content is about Infinity Wars, and reference to Tony Stark is the additional information we’ve provided.

Can we use the <aside> element within the <article> element ?
`Select the right answer`
`Yes`
`No`

(Topic-4) Time to brush up!

<aside> can be used as a ______ .?
`Select the right answer`
`Navbar`
`Menubar`
`Sidebar`
`Nobar`

____ is independent and complete from another content.
`Select the right answer`
`<aside>`
`<title>`
`<article>`
`class`

(Lesson-6) Multimedia Elements

(Topic-1) The Audio Support

Let it play!
Who doesn’t enjoy good music!
HTML5 lets you embed music to your webpage.
Achieved using the <audio>, <source> tags.
PS: <source> can be replaced with the src attribute.
Don’t worry! We’ll learn about this via various examples.

Denotation: <audio> </audio>.
Location : Inside the <body>.
Tags Involved: <source>.
Major Attributes Involved: src, type, controls.

Let’s learn about these elements:
 <body>
	<-- This will load an audio -->
	<audio controls="controls">
		<-- This refers the main source of the audio   -->
		<source src ="music.mp3" type="audio/mpeg" >
	</audio>
	<-- This will print a paragraph -->
	<p>
		<--   This will print the text bold-->
		<b>Note:</b>
		The audio tag is not supported in Internet Explorer 8 and earlier   versions.</p>
</body>

Let’s check this out!
<img-of-above-page-displaying-audo-player>
controls: Provides you with the playback functionalities (play, pause, volume).
src: Lets you add URL to embed. Can replace <source> if added with <audio>.
type: Specifies the supported format for audio.

Can we define more than one <source> element in <audio>?
`Select the right answer`
`True` | `yes cos it allows browser choose the supported format`
`False`

(Topic-2) The Video Support

Videos easily catch a user’s attention.
Want to embed a video to your webpage? Here is the <video> element:
Denotation: <video> </video>.
Location : Inside the <body>.
Tags Involved: <source>.
Major Attributes Involved: src, type, controls, width, height, autoplay

Let’s see how we can achieve this:
 <body>
	<-- This will load a video which starts automatically-->
	<video controls="controls" width="200" height="200"   autoplay>
		<-- This refers the main source of the video -->
		<source src="walking_video.mp4" type="video/mp4">
	</video>
	<-- This will print a paragraph -->
	<p>Here is a video for you!!</p>
</body>
<img-of-<video-tag-above->

Adding autoplay, plays the video on webpage load. 
Can also be used for <audio>.
Try adding poster=”URL.png” attribute to the <video>.
Hint: poster lets you add a static frame to the video before the user plays it.

What are all the attributes that can be used with the <video> element?
`Let’s just say all of them?`
`Select the right answer`
`height`
`src`
`poster`
`Let’s just say all of them?`

What will happen if the height and width of the video are not set while the video loads?
`Select the right answer`
`page flickers`
`page does not load`
`page crashes`
`None`

(Topic-3) The Embed Element

Need some extra content?
Seeking help sometimes adds more strength to the task, we can make our web page more interactive by:
Adding third-party/external content to the webpage using <embed>
Denotation: <embed>.
Location: Inside the <body>.
Major Attributes Involved: src, type, width, height.

Let’s try embedding to the document:
 <-- This will create a container for adding an external content-->
<embed src="embed.mov" type="video/quicktime" width="300" height="200" >

<img-of-embeded-stuff-above->
	<-- This will print a paragraph -->
	<p> Embedded a quick video!! </p>

Additional Notes:
Most of the attributes <audio>, <video> and <embed>, can be kept on mute initially, using the muted attribute.
For removing autoplay you have to remove the attribute rather than assigning it’s value as false.

Which attributes help in adjusting the display of embedded content ---?
`Select the right answer`
`height/width`
`poster`
`looped`
`You cannot change for embedded plugins.`

(Topic-4) Try and Answer !

What indicates the browser should begin playing a video after page load, once enough content has been received?
`Select the right answer`
`autoplay`
`autoload`
`auto-buffer`
`buffer`

Which attributes allows users to control volume, playbacks etc.?
`Select the right answer`
`list`
`play`
`controlback`

Which tag is used to define multiple media types for media elements audio and video ?
`Select the right answer`
`<canvas>`
`<sound>`
`<source>`
`<type>`

(Lesson-7) New Additions to form elements
(Topic-1) New form attributes

Making forms more exciting!
With HTML5, forms have become more munchable. 
Let’s learn about them:
<form autocomplete=”on/off”>
Provides an auto-completion option via the browser.
On submitting and reloading the form, it provides the suggestion of the values previously entered.

<fieldset>
Groups together the related elements.
Better view by distinguishable sections.
<input>, <label>, <legend> are nested in.

<legend>
To provide a name/title to the <fieldset>

Wait, we’ll show how it is done.
 <-- This will create a form -->
<form>
	<-- This will create a container for storing similar elements-->
	<fieldset size="30">
		<-- This will provide a name for fieldset -->
		<legend>Contact Information:</legend>
		<-- This will   create a textbox for Email -->
		Email Address Please: <input type="text"><br>
		<-- This will create a textbox for   Phone number-->
		Phone Number Please: <input type="text"><br>
	</fieldset>
<form>

See, we told you it’s easy to achieve.
<img-of-<field-set-field>-above->

Let’s clear our concepts:
`answer`
`<form> <--------------------> Creating Exciting forms`
`<fieldset> <------------------> Similar content`
`<input>  <-------------------> Place to write`
`autocomplete <-------------> An Attribute`

`Question`
`Click to match the appropriate answers`
`<form>`          <---------> `place to write`
`<fieldset>`      <---------> `Creating Exciting forms`
`<input>`         <--------->  `An Attribute`
`autocomplete`    <--------->  `Similar content`


(Topic-2) New Input Elements

Let’s see what <input> has to offer!
Some more attributes have been introduced to <input>.
Have you ever noticed the text displayed in the text field before you enter something? That’s achieved using a placeholder attribute.
 Name: <input type="text" placeholder="ENTER YOUR NAME">

Some fields are supposed to be made mandatory for form submission. It’s easy, just use the required attribute.
 <-- This will create a form -->
<form>
	<-- This will create a textbox for Username -->
	User Name: <input type="text"   required>
	<-- This will create a textbox for Password-->
	Password :<input type="text" required>
</form>

Then we have different values for the type attribute:
<input type=”password”> Masks the password after we enter it.
<input type=”date”> Lets you enter date in YYYY-MM-DD format.
<input type=”number”> Collects numbers either integer or decimal.
<input type=”email”> Helps to enter an email in the abc@mail.com format.
<input type=”url”> Lets you enter an absolute URL.

On the loading of a web page the cursor is automatically placed inside that box bringing it into focus.

Lets you validate your field against a regular expression.

(Topic-3) Test Your Knowledge

Let’s brush up on what we’ve learnt!
___ is the attribute in HTML5 which lets you add a placeholder text in the form?
`Select the right answer`
`text`
`placeholder`
`type`
`img`

To which attribute do we assign values like email, number text etc..?
`Select the right answer`
`src`
`name`
`type`
`img`

Grouping together similar fields is achieved by using <____> element and providing a name to it is achieved by <____> element
`Select the right answer`
`fieldset, header`
`header, legend`
`fieldset, legend`
`legend, titans`

Which attribute lets you validate your field against a regular expression?
`Select the right answer`
`placeholder`
`pattern`
`type`

(Lesson-8) Some exciting feature by HTML5
(Topic-1) Content is Editable

You can edit your content!
Typing and then deleting your texts, it’s more friendly when your content is editable.
HTML5 also provides this simple feature of editing your content.
Achieved by using the attribute contenteditable.
We just have to set it as true <p contenteditable=”true”>.

This is how you can edit.
 <p contenteditable="true">
	  Hey people !!
</p>
<img-of-editable-<p>-tag-above->
Want just 1 exclamation? Use backspace.
<img-of-editable-<p>-tag-above-with-1-exclamation-redited-or-removed->

Does <input contenteditable> and <input contenteditable=”true”> mean the same?
`Select the right answer`
`Yes`
`No`

(Topic-2) Drag and Drop

Dragged and Dropped accomplished.
Rearranging your bookshelf, grouping all the same genres in one corner and Nicholas Sparks in another.
Any element can be dragged and dropped within the HTML page.
Achieved by setting draggable= ”true”.
Then we decide which elements are to be dragged and where.

ondragstart an event to be defined using Javascript on the element to be dragged.

ondragover an event to specify where data can be dropped.
You can learn about making it functional from our Javascript course.

What are all the elements you think can be made draggable?
`Select the right answer`
`image`
`links`
`selected text`
`All of the above`


(Topic-3) The <script> Tag

Introducing Javascript to HTML.
You can't light a torch without batteries, such is Javascript to HTML
<script>- the place where all our Javascript content goes.
FYI: Javascript is the most common client- side scripting language.
It makes your HTML content more dynamic and functional.

It’s easily rendered by the browser.
<script> and </script> can be placed both inside the <head> and <body>.
Attributes such as src, type, charset etc can be used with the <script> element.
So you can also add an external script file using the attributes involved in HTML.

What, according to you, can the type be assigned to when used with <script>?
`Select the right answer`
`type=”number”`
`type=”language”`
`type="text/javascript"`
`type=”time”`

`answer`
`On a roller-coaster! It is assigned as text/ javascript.(P.S. It’s no longer needed in HTML5)`

(Topic-4) Canvas your ideas

Graphics, charts, animations etc. can be added to HTML using <canvas> element.
You can mix it up with Scripting to make it more functional(canvas scripting API).
<canvas> requires a closing tag, </canvas>.
Attributes such as id, height, width can be used with it.

Let’s see how it is done:
 <-- This will create a container with specific width, height and border -->
<canvas id="createCanvas" width="100"   height=50"style="border:1px solid ;">
</canvas>
<img-of-above-canvas>-snippet->
This is the basic structure.

After that, we can add animation and colors to it using Javascript and CSS.

Which attributes helps you provide reference to the canvas in the <script>?
`Select the right answer`
`src`
`id`
`value`
`name`

(Topic-5) Little Brain Tweeks

Which of the following elements is used for canvas graphics?
`Select the right answer`
`<graphic>`
`<canvas>`
`<style>`
`It isn’t possible !`

Can you match the following with the respective elements?
`answer`:
`Editing the content` + `contenteditable=”true”`
`Making HTML dynamic` + `<script>`
`Dragging the button` + `draggable=”true”`
`Adding graphics` + `<canvas>`

`Question`

`Click to match the appropriate answers`
`Editing the content`  | `draggable=”true”`
`Making HTML dynamic`   | `<canvas>`
`Dragging the button`   | `<script>`
`Adding graphics`        | `contenteditable=”true”`


Can you list out the events related to draggable?

`ondragstart`
`ondragover`
`here`
`pick`

(Lesson-9) Wrapping Up

(Topic-1) It's a wrap

Hey, we have come a long way from where we started, Let’s go back down the path.

We started with the basic HTML elements- <head>, <html>, <body>.
Tags used for structuring <p>, <h1>..<h6>, <br>, <div>.

Tags that make documents interactive <a>, <image>, <title>.

Attributes always ready to help HTML Tags- href, src, style.
We learnt that style can be used as a <style> tag, termed as an embedded style.

We created an input field using <input>.
Added attributes like id, type, name, value.
We learnt to create a simple <form>.
We nested <input>, <button>, <label> inside the <form>.
We made the form dynamic by using action, also provided a name and value to it.

We learnt to store our data in tables using <table>.
Added a new row (<tr>), a column (<td>) and a header(<th>).

We felt the need for creating lists.
<ol> for ordered list, <ul> for unordered lists
Defined the element using <li>.

Wholeheartedly, we welcomed HTML5.

Starting with <!DOCTYPE html>, we learnt to define character encoding .
<meta charset=”UTF-8”>

We welcomed some new elements and waved goodbye to old ones.

Then Semantics, gained our focus.

So we learnt about content which can be placed in <header>.

Authorship, Copyrights placed inside <footer>.

How the major links on the website enters the <nav>.

We narrowed it down even further and learnt that:
The Descriptive content is placed under <section>.

<article> is a specific or a separate portion of the content.
And how the <aside> element indirectly helps.

With loud music on, which we added using <audio>.

Some funny videos of the panda <video>.
We did <embed> some third party plugins.

We learnt about how to create more interactive forms.

Autocomplete provides an option for autofill.
Similar content for a form can be grouped using <fieldset>.

<legend> is used to name that <fieldset>.

New attributes to the <input> were introduced.

For making field mandatory for submission we used required.

Bringing a field into focus on page load was achieved by using autofocus.

type was provided with more values like password, email, date, url etc.

We used pattern to validate our fields against an expression.

We moved a little ahead to understand some more features of HTML.

We learnt content can be made editable by contenteditable.

`draggable` is set to true for dragging elements from one place and dropping them.

Making HTML more functional using Javascript.
It is included under the <script> element.

Animations, graphics were included using <canvas>.

Kudos to us! We have successfully completed our mission.


(Lesson-10) The End of Resistance

(Topic-1) The End of Resistance

Quizzing up!

The ____ element is used to define a distinguishable unit of content such as a blog post, comment, article etc.

`Select the right answer`
`blog`
`article`
`post`
`img`

In HTML tables a table header is defined by?

`Select the right answer`
`<tr> tag`
`<td> tag`
`<th> tag`
`<head> tag`

When placing the ____ attribute on a field it should cause a supporting browser to immediately focus this field once the page is loaded.

`Select the right answer`
`autofill`
`autoplace`
`autofocus`
`autocomplete`

In HTML5, it is possible to validate data entry by setting the ____ attribute for the field
`Select the right answer`
`validate`
`required`
`restrict`
`allow`

<video controls="controls" autoplay>
	<source src="song.mp4" type="video/mp4" />
</video>
Which of the following statements are correct?

`Select one or more answers`
`The video plays when the page loads.`
`Mp4 won’t be supported`
`It will give you an error.`
`The video successfully gets embedded.`

How to make an element draggable?

`Select the right answer`
`<div drag="true" />`
`<div draggable =”true”/>`
`<div type=”drag”>`
`You cannot drag an element.`

The most sensible way to divide the document logically is:

`Select the right answer`
`<div></div>`
`<p></p>`
`<span></span>`
`<section>/<section>`

Which of the following attributes adds audio controls, like play, pause, and volume?

`Select the right answer`
`video`
`controls`
`source`
`autoplay`

The HTML5 document used to create graphics using scripting is _______?

`Select the right answer`
`<canvas>`
`<img>`
`<mark>`
`<figure>`

What is the html form element used to select or enter user data?

`Select the right answer`
`<link>`
`<group>`
`<input>`
`<label>`

The content can be made editable, but how?

`Select the right answer`
`contenteditable=true`
`content=true`
`content=editable`
`type= editable`

Which element may be used within content to represent material that is indirectly related(tangential)?

`Select the right answer`
`nav`
`article`
`aside`
`class`