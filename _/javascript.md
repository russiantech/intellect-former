**(Lesson-1). Introduction To Javascript
(Topic-1) What is JavaScript?
Introduction.
<animated_js.gif>
JavaScript is a programming language used to make interactive webpages.
JavaScript’s main motto is to “make it move”.
JavaScript is like Oxygen.
It gives life to the web page and hence fascinates us with the wonderfull interactions.
Isn’t that cool? :D
Javascript is responsible for all the cool animations that keeps us engaged on the web pages.
If you've ever used a search box to search your favorite meme, watched a Mr. Bean video or checked a live cricket score, JavaScript is probably running through it.

(Topic-2) Is JavaScript similar to Java?
JavaScript? or Java?
<js_vs_java.jpg->
Java and JavaScript are similar as Car and Carpet are similar.
Haha ;) Now you get it! ;)
JavaScript and Java are two different computer languages.
Both have their own merits and demerits.

(Topic-3) What do we build using JavaScript?
<animated_blocks.gif>
JavaScript is everywhere.
JavaScript is the most universal language in the world.
The beauty of JavaScript is that you can build anything (not literally 😊 ) with it.
Here’s the list of things, we can build with JavaScript...

Interactive Webpages
<animated_webpages.gif>
JavaScript is used to create interactive web pages for both Desktop and Mobile applications.

Mobile Applications
<animated_mobibile.gif->
JavaScript is used to create mobile applications which we use everyday.
We can also create iOS and Android applications with it.

Desktop Applications
<animated_desktop.gif>
JavaScript is also used to create full-fledged Desktop applications.

Who else uses JavaScript?
<who_else_uses_javascript.gif>
JavaScript is used by Google, Facebook, Microsoft, Uber and every other company you could think of!
Knowingly or unknowingly we’ve used their services and hence we’ve utilised JavaScript.

Now, the fun part begins.
Let’s dive into the world of JavaScript!
Shall we?
Let’s revise first!

(Topic-4) Let's revise _ Javascript Initroductino

Choose the invalid option:
`Select the right answer`
JavaScript can’t be used to perform animations on web pages.
JavaScript can be used to create Desktop applications.
JavaScript can be used to create iOS applications.
JavaScript is everywhere.


Choose the valid option
`Select the right answer`
JavaScript and Java are similar.
JavaScript is not a web based language.
JavaScript has no relation with the web.
JavaScript is used to make web pages interactive.

Summary
In this topic we’ve learnt:
1. What is JavaScript? It is a programming language used to make interactive web pages.

2. Is JavaScript similar to Java? No, they are two different programming languages.

3. What can we build using JavaScript? Web applications, mobile applications, desktop applications, games etc. Pretty much everything.

**(Lesson-2). Your First Program

(Topic-1) What is a Computer Program(JS)?
Introduction.
<animated_computer.gif>
Computers are just boxes that blindly follow instructions.
But, unlike humans, they follow the instructions accurately.
If your mother asks you to add 2 onions to the grocery list, there’s a high possibility of you forgetting to bring the onions.
Unlike us, computers remember everything.
So, now you know how to avoid your mother’s scolding ;).

Computer Program
<animated_program.gif>
As we discussed, computers follow a set of `instructions` and `perform tasks` accordingly.
If we take the previous example, your mother had given you instructions about what all to add in the grocery list.
So those set of instructions are nothing but computer programs.
Computer program is a set of instructions that a computer follows to complete a task.

What’s the sole job of a computer?
`Select the right answer`
`Sit ideally.`
`Follow a few set of instructions.`
`Follow all the instructions.`
`Go against the provided instructions.`

<js_program_sum.mp4>

(Topic-2) Writing our first JavaScript program

Introduction.
Let’s start by commanding the computer to print “Hello World”.
So can you guess how we will be going about this?
We will start by providing the required instructions to the computer to print “Hello World”.
We are going to write those instructions in a language that the computer understands.
Yes! JavaScript it is!

Printing text
The command to print text in JavaScript is :
`document.write`
This command tells the computer to write(print) something on a document i.e. a web page.
But this command is incomplete without few special characters.
Let’s go ahead and add them.

Round Brackets
<bracket.png>
Round Brackets'()' tells the computer to separate the command from the text that is to be printed.
Let’s add Round Brackets to our command.
`document.write()`

Double quotes.
<quotes.png>
Double quotes(" ") are added to instruct the computer about which part is to be printed.
Let’s add Double Quotes to our command along with Hello World.
`document.write(“Hello World”)`

Semicolons
<semi_colons.png>
Semicolon indicate the end of a command and hence is added after every command.
Now our command will change to:
`document.write(“Hello World”);`
The result of the above command will be:
`Hello World` or `output-of-above-snippet`

Congratulation!
And Voila! We’ve successfully completed our first JavaScript Program!
Give oneself a pat on the back!
Congratulations !
Now you’re ready to build the next “Facebook” !
Just kidding!
There’s a lot to learn..
Let’s revise before we move forward.
Shall we?

Computers can’t perform tasks without instructions.
`Select the right answer`
`True`
`False`

Double quotes are not required to print texts.
`Select the right answer`
`True`
`False`

Choose the correct command of printing a text.
`Select the right answer`
`write.document`
`Printf`
`System.out.println`
`document.write`

Wow! Great!
You remember everything!
Let’s dive deeper!
Shall we?


3. Storing Values
(Topic-1) Storing a value

Storing a value
<variables.jpg>
Previously, we learned how to command the computer to print something.
Now, let’s dive deeper and learn how to store values in JavaScript.
Imagine yourself as a scientist in a chemistry lab.
So if you look around the lab, you’ll find several cylinders.
Each cylinder contains different types of gases, starting from Oxygen to Nitrogen.
But how do we differentiate which cylinder contains which gas?
To solve that problem, we get it labelled with the gas’ name on it.

Similarly, if we want to store some information, we store it in our memory.
And we’ve all the information labelled in order to avoid confusion.
If someone asks our age, we don’t tell them our grandfather’s name. :p
Do we?
Definitely no!
In Programming, this storing container is called “Variable”.

Variables
<values.jpg>
So, variables are containers which store values.
We place values in these containers and then use those values by referring to the container’s name.

(Topic-2) Storing a word

Let’s say we want to print “Russian Developers”
`document.write(“Russian Developers);`
This command will do it for you.

Don’t you think that’s a lot of writing??
Instead let’s use a variable to save our energy. :D

In JavaScript, creating a variable is called “declaring” a variable.
Every programming language has their set of reserved names which are called keywords.

Variables are declared with the ‘var’ keyword followed by an equal to(“=”) and the value.

Let’s go ahead and save the word “Russian Developers” in a variable x.
`var x = “Russian Developers” ;`
Don’t forget to close the statement with a semicolon `;`.
Now, if we want to print the word twice, we can do it in the following manner:
`var x = “Russian Developers” ;`
`document.write(x) ;`
`document.write(x) ;`
Ps: There’s a better a way to write less code to perform the same task, which we’ll learn soon. :D

So, words are called Strings in programming language. Hope you remember it, we will use this name a lot.
Strings are sequences of alphanumeric characters.
String values are always written with quotations (“ ”).

(Topic-3) Storing true or false
<boolean.jpg>
In life, we’ve to make several decisions.
But all of that comes down to two options, i.e. “yes” or “no”, which in programming terms is referred to as true or false.
This true or false is called Boolean values.
A boolean value is declared in the following way:
`var JS_sucks = false ;`

Few points to keep in mind while creating a variable with a boolean value :
Boolean represents either true or false.
Boolean is always defined without quotations.
`var JS_Rocks = true	 \\boolean`
`var JS_rocks = "true"	\\not a boolean`
If you remember, double quotations are used to declare Strings.
Hence we don’t use double quotations while creating a variable with boolean values.

(Topic-4) Storing a number
Integer
<number.jpg>
Let’s say we want to store our age in a variable and print it.
We would do this by first storing the age in a variable followed by printing it out.

Let’s start by `creating` a `variable`.
`var age  = 22 ;`
Mind you, age and Age will be two different variables because JavaScript is a case-sensitive language.

Let’s store our age in a variable and print it.
Tap the correct answer to fill in the blanks
`var age = ____?; `
`document.write(____);`

Few points to keep in mind while creating variable with number as a value :
Numbers can be written with or without decimal.
`var without_decimal = 10;`
`var with_decimal = 11.07;`

Numbers are always numeric values written without quotations(“”) as we already know, only strings are written with quotations.

(Topic-5) Let's revise

Which is the correct way to declare a number?
`Select the right answer`
`var x = “22”;`
`var x = 22;`

Choose the variables with boolean values:
`Select one or more answers`
`var JS_rocks = true;`
`var JS_rocks = false;`
`var JS_rocks = ”false”;`

Choose the correct one.
Select the right answer
`var fav_food = “burger`
`var fav_food = “burger” ;`
`“Burger” = fav_food ;`
`None of the above`

That’s great!
You remember everything!
Let’s move on to the next topic!
<variables.mp4>

4. Performing Basic Calculations
(Topic-1) Basic math calculation

Introduction
Mathematics is such a subject which most of us have come across at least once in our life.
Some of us hate it, some of us have fallen for it.
For those who hate it, don’t worry we’re not going to learn anything complex, instead we will focus on basics.
As a wiseman had quoted once,
“If you look at all aspects of all programming languages, everything comes down to basics and fundamentals.”
So, let’s examine, if you know some commonly used mathematical symbols.

Match the following:
`Click to match the appropriate answers`
`Addition`                      | `-`
`Subtraction`                   | `+`
`Multiplication`                | `%`
`Division`                      | `*`
`Modulus(division remainder)`   | `/`

Voila! You know it all!

So, let’s now construct a program to utilise the above symbols.

Create two variables, give them values.
`Tap the correct answer to fill in the blanks`
var ____ =  ___;
var ____ =  ___;
`x` | `2`, `y`| `3`

Create another variable to store the addition of previous two variables in it.
`Tap the correct answer to fill in the blanks`
var a = 3 ;
var b = 3 ;
var ___ = ___ + ___;
`c` | `a` | `b`

Finally print the 3rd variable i.e the one where we stored the addition result.
`Tap the correct answer to fill in the blanks`
var x = 3 ;
var y = 2 ; 
var z = x + y ; 
document.write(_____);

Similarly, if we have to perform other mathematical operations, the command would be as follows:
`var z = x - y ;`
`var z = x / y ;`
`var z = x % y ;`

(Topic-2) Adding and Subtracting one

Increment
<increment.jpg>
Till now, we’ve learned how to perform basic math calculations.
Let’s say, if we want to increase the value of a variable by 1, we would do it the following way:
`var pizza = 1 ;`
`pizza = pizza + 1;`

What If I tell you that there’s an easy way to perform the same thing plus it will save your energy on typing so much ;) .

This is where the concept of incrementation comes into play.
Incrementation is nothing but increasing the value of a variable by 1.

Increment
The syntax for incrementation is the name of the variable and “`++`” followed by a `semi-colon(;)`.
Let’s rewrite the above program:
Let’s rewrite the above program:
`var pizza = 1 ;`
`pizza++;`

Yes, that’s it!
That’s how you increment a variable’s value by one.

Decrement
Similarly if we’ve to decrease a value of a variable by 1, we will do it the following way:
`var pizza = 2 ;`
`pizza--;`
Yes, you got it right!
The syntax for decrementation is the name of the variable and “--” followed by a semi-colon.

(Topic-3) Let’s revise

Choose the valid one for incrementing x by one:
`Select the right answer`
`var x = 0 ;`
`x+;`
`+x+;`
`x++;`
`None`

Decrement x, increment y and print both of them.
`Tap the correct answer to fill in the blanks`

`var x = 2 ;`
`var y = 3 ;`
x _______
y _______
document.write( _____ ) ;
document.write( _____ ) ;

`x` | `--` | `;` | `y` | `++` | `;`

Let’s revise

In this topic we’ve learned:
1. How to perform basic mathematical operations.
2. Storing the result in a variable and printing it out.
3. Incrementing and Decrementing a variable.

(Lesson-5) Making Comparisons
(Topic-1) Comparison Craziness
Introduction
<comparison.jpg>
We as human beings love to compare.
Even in our daily life, we do lots of comparisons like
“Is Iphone better than Samsung?” and the list goes on. :p
And guess what?
We also perform comparisons in programming.
Let’s see how..
But before that let’s examine your knowledge regarding the same.

Match the following:
`Click to match the appropriate answers`
`Greater than`              | `x >= y`
`Less than`                 | `x > y`
`Greater than or equal to`  | `x <= y`
`Less than or equal to`     | `x >= y`

Equal to
<flow_chart.png>
Wow! Good work!
We use `==` to check if two values are equal or not, if the values are equal then the condition becomes true.
Remember, there’s a difference between `“=”` & `“==”`.
`“=”` is used to declare variables like,
`var x = 2 ;`
`var y = 4 ;`
Whereas, `“==”` is used to check the equality of the two values.
`x == y //false`

Not Equal to
<flow_chart.png>
And “!=” is to check if two values are unequal or not. If the values are not equal then the condition becomes true else it becomes false.
`x != y  //true`
In a nutshell, the end result of all the comparisons, as we can see in the image comes down to either true or false.

(Topic-2) Deep into comparison
Comparisons
<not_equal.jpg>
Let’s say, you want to buy a new mobile phone and for that you’ve two main requirements,
One, the phone’s megapixel should be more than 10mp and phone’s memory should be more than 16gb.
Let’s write a program for the same using the concept of comparisons we learned just now.
`var mp = 5 ;`
`var gb = 16;`
Let `mp` be phone’s megapixels and `gb` be phone’s memory.
So the condition would be:
`mp > 5 and gb > 16 `
Now these two conditions are independent of each other.
What if we want an answer as yes or no when both the values are equal?
i.e. how do we write `“and”` condition in programming?
It’s really simple!. The syntax is` “&&”`.
Let’s rewrite the above program:
`mp > 5 && gb >16`
So, “&&” is added when there’s a situation where two or more conditions are meant to be true.

Similarly, if we modify our needs to: phone’s megapixel should be more than `10mp` `or` memory should be more than `16gb`.
`mp > 10 || gb >16` 
`“||”` also known as `“or”`. It is used when only one condition out of the many is to be true in order to proceed.

(Topic-3) Let's Revise _ Comparison

`var x = 1 ;`
`var y = 5 ;`
Choose the valid ones:(`Select one or more answers`)
`x > y`
`y >= x`
`x != y`
`None`

`var x = 2 ;`
`var y = x ;`
Choose the invalid ones:(`Select one or more answers`)
`x == y`
`x > y`
`x != y`
`x <= y`

Choose the valid one for: x and y should be greater than 7.
`Select the right answer`
`x > 7 && y > 7`
`x > 7 | & y > 7`
`x > 7 || y > 7`
`None`

Choose the valid one for: x should be less than 2 or y should be greater than 7:
`Select the right answer`
`x < 2 || y > 7`
`x < 2 |& y > 7`
`x < 2 && y > 7`
`None`

Good going!
Now that we know how to perform comparisons,
Let’s go ahead and learn how to implement them in JavaScript.

6. Making Decisions
(Topic-1) Decision Making In Life

Decision making
<decision.jpg>
The importance of decision making in an individual’s daily life is massive.
It requires making a definite choice between two or more alternative courses of actions that are available.
Like, choosing your major in college or choosing a hairstyle in a barber's shop.

You actively made the decision to learn JavaScript even after having so many other programming languages.
Similarly, a computer has to perform different tasks based on different conditions. And guess what?
We are the one who has the control over which task the computer should perform and on the basis of which conditions.
Are you excited to help the computer in making decisions? :D
Let’s check it out…

(Topic-2) If...else
Conditional Statements
<decision.jpg>
In programming, conditional statements are used to perform different tasks based on different conditions.
For example, “if it doesn’t rain, we’ll go for a drive and if it does, then we won’t” is a conditional statement.
The conditional statement consists of if..else.

if...else
<flowchart_condition.png>
In JavaScript, a conditional statement could be written in the following way:
`if (condition) {
	Task to be performed if the condition is true.
}else{
	Task to be performed if the condition is false.
}`
Let’s write a program using if..else..
Before that let’s see if you can answer these questions.
`Click to match the appropriate answers`
`Greater than`     | `x == y`
`Less than`        | `x != y`
`Equality`         | `x > y`
`Inequality`       | `x < y`

Great Work! You remember everything from the previous lesson!
if and else are the keywords we use to write a conditional statement.
The condition is included after the if keyword within round brackets.
`if(conditions)`
Followed by opening a curly bracket where we write the task that is to be performed if the condition is true.
`if (conditions) {
	//task to be performed if true
}`
Followed by an else keyword and a curly bracket where we write the task that is to be performed if the condition is false.
`else{
	//task to be performed if false
}`
Now, we’re ready to write a program using if...else…

Select appropriate options to print "x isn’t greater than y"
Tap the correct answer to fill in the blanks
`var x = ___ ;`` var y = _____;`
`if( x > y){
	document.write(“x is greater than y”)
}
else{
	document.write(“x isn’t greater than y”)
}`

`23`, `43`


(Topic-3) Let's Revise
If

`var x = 1 ;` 
`var y = 5 ;`
Choose the valid ones:
Select one or more answers
if(x > y ){document.write(“true”)}
if(y > x ){document.write(“true”)}
if(y >= x ){document.write(“true”)}
if(x == y){document.write(“true”)}

Write a conditional statement to print “true” when a is greater than b .
`if( ___ > ___ ){
	document.write(“true”)
}else{
	document.write(“false”)
}`
`Tap the correct answer to fill in the blanks`

That’s great!
You remember everything!

Let’s move on to the next topic!

7. Storing Similar Values Together
(Topic-1) Array introduction
Introduction
<bucket_list.jpg>
We all have a “before I die, I want to-” list i.e. the bucket list.
In general, the bucket list would contain the following items:
`1. Swim in the world’s largest swimming pool`
`2. Do skydiving`
`3. Master one programming language`
`4. Visit Lagos`
And the list goes on..

Arrays
If you want to replicate this list in programming, you’ll go ahead and create multiple variables and store each element from the list.
Like,
`var wish1= “Visit Lagos” ;`
`var wish2 = “Do skydiving” ;`
Etc...
What if I tell you there’s a way to perform the same thing but without having to write so much!
Yes you guessed it right….Arrays to the rescue!!

JavaScript Arrays
<array.jpg>
Array is a special variable which lets us store multiple values in a single variable.
Isn’t that cool? :D
It eases our work to another level! :D
Now, let’s see how to create one..

(Topic-2) Creating Arrays

Before that, let’s see if you remember how to create a variable.. Create a variable named “y” with value as 7.
`Tap the correct answer to fill in the blanks`
`var ___ = ____ ;`
`y` | `7`

How to create arrays?
<animated_array.gif>
Arrays are written just like variables, i.e var keyword followed by the array name:
`var array_items`

Once, we’ve the array’s name, we add values to it. Values are written in between square brackets.
`var array_items = [];`

The values are separated by commas(“,”).
`var array_items = [“item1”, “item2”, “item3”] ;`

Important points about arrays
But the catch here is, we can only store collection of variables of the same type.

`var array = [“go skydiving”, 1, 44, “visit Paris”] ;`
This is an invalid array since it has a combination of strings and numbers.
`var array_strings = [“go skydiving”, “visit paris”];`
`var array_numbers = [20, 40, 34, 11];`

Crux: An array can only hold variables of the same type.

Now that we know how to create arrays, let’s go ahead and learn how to access each item of the array and print them.

(Topic-3) Accessing Arrays
Accessing arrays.
Arrays are like attendance sheets.
Attendance sheets consist of two main things, first roll number followed by name of the person who’s associated with the particular roll number.
The teacher calls out the roll number of a student and hence the student acknowledges the teacher.
Similarly in arrays, don’t you think there should be a way to access the items?
Yes, in fact there is a way to do so!
Like the roll numbers, the items in the arrays are assigned a particular number depending on the order of the item they’ve been added.
The items are assigned a number starting from zero. The first item is assigned `zero` followed by the next `one` and so on.
Luckily, computers don’t proxy like we do for our friends ;)
Hence when a particular number is called, the item associated with it always responses.

Accessing arrays
<access_array.jpg>
Let’s create an array with names of students from a class.
`var students = [“Ashley”, “John”, “Tim”, “Mac”, “Wesley”] ;`
If we want to access the first element i.e. “Ashley”, we would do it in following way:
write the name of the array followed by opening a square bracket and writing the item number and closing it.
`students[0] would give me access to “Ashley”.`
Similarly, can you guess how to access the rest of the items?

Match the following for, 
`var students = [“Ashley”, “John”, “Tim”, “Mac”, “Wesley”] ; `

`Click to match the appropriate answers`
`student[0]`  | `John`
`student[1]`  | `Wesley`
`student[2]`  | `Tim`
`student[3]`  | `Mac`
`student[4]`  | `Ashley`

Great! You seem to have mastered Arrays!
<animated_arrays.gif>
Before moving forward, let’s solve one more problem…

`var grocerry_list = [“banana”, “Maggie”, “wheat”, “Cornflakes”]`
Choose the valid one to print “Maggie”.
`Select the right answer`
`document.write(grocerry_list[0]) ;`
`document.write(grocerry_list[1]) ;`
`document.write(grocerry_list[2]) ;`
`document.write(grocerry_list[3]) ;`

Great!
Similarly, we can print all the other items by writing their order numbers within the square brackets.

(Topic-3) Let's Revise _ Arrays
In this topic we’ve learned:

1. What is an array? : 
`Array is a special variable which lets us store multiple values in a single variable.`

2. How to create an array?: 
`var array = [“this”, “is”, “how”, “you”, “do”, “it”];`

3. How to access an item in an array?: 
`array[3] will print “you”.`

Do remember the first element in the array can be accessed by `array[0]` and not `array[1]`.

The numbering in an array always starts from zero.
Alright, let’s move on to the next topic….

8. Repeating A Task
(Topic-1) Why do we repeat a task?

Introduction
<animated_task.gif>
Let’s be honest, we all are very lazy creatures!
We love to automate stuff just for the sake of not repeating it manually.
Do you remember the times when we were given to write all the alphabets 10 times as homework?
That sucked right?
Luckily, we can repeat stuff in programming.
And it is super easy to learn.

Example
<animated_repeat.gif>
Let’s say we want to print “I love JavaScript” 10 times.
We’ll start with creating a variable and storing the required value.
`var x = “I love JavaScript” ;`
Followed by printing it..
`document.write(x) ;`
`document.write(x) ;`
`document.write(x) ;`
`..10 times.`

Looping
What if the same task could be performed in 3-4 lines of code?
Yes! 3-4 lines! You read it right! :D
This procedure is called looping.
Looping is basically repeating a sequence of instructions until a condition is satisfied.

It’s like performing 50 push ups, here 50 is the maximum limit and performing push ups, is the sequence of instructions.

Let’s consider the previous example,
Print “I love JavaScript” is an instruction and 10 times is a condition.
So, “I love JavaScript” should be repeated 10 times.

Let’s dive in
Now that we know what looping is and why it is required, let’s dive in right away!!

(Topic-2) Loops in JavaScript
Loops in JavaScript
<animated_loops.gif>
As we mentioned in the previous subtopic, loops are used when sequence of instructions are to be executed multiple times.
In JavaScript, two most common loops are:
`for loop`
`do...while loop`
We’ll look into each, one by one..

For Loop
<for_looop.png>
For loop consist of three main parts:
1. Giving initial value to the variable.
2. Condition(eg. i<10)
3. Counter statement: used to increase or decrease the variable value so that the conditions are satisfied.

For Loop
<for_looop.png>
Once, we’re done giving initial value to the variable and condition followed by increasing/decreasing the variable’s value, we’re ready to write the statement to be executed until the condition is satisfied.
Let’s understand it with the help of an example..

For Loop Example
<flowchart_for_loop.png>
Let’s consider the previous example and try printing `“I love JavaScript”`, ten times.

We’ll start by creating a variable.
`var i ;`

Followed by writing a for loop in the following way:
`for(i = 1 ; i <= 10 ; i ++)`
The point to note here is,
`Initial value`, `condition` and `counter statement` are separated by `semicolons (“;”)`.

Till now, we’ve written the following code:
`var i ;
for(i = 1 ; i<=10 ; i++)`

Now, all we’ve to do is write the statement inside curly brackets, which is to be repeated 10 times.

`var i ;
for(i = 1 ; i < 10 ; i++){
	document.write(“I love JavaScript”);
}`

Repeat “I can Loop”, 50 times
`Tap the correct answer to fill in the blanks`

`var i;`
`for(i = 1 ; i <= ___ ; i++){`
	`document.write(“I can Loop”)`
`}`

`50` , `I can Loop`

Great! You have mastered the `for loop`!!
Now, let’s go ahead and learn the `do...while loop`…

Do..While Loop
<flow_chart_do_while_loop.png>
`Do..while loop` is pretty similar to `for loop`.
As we can guess from the name, the `do..while` loop has two main parts:
1. do: this is where we write the code to be executed until it satisfies the condition(inside curly brackets).
2. while: this is where we mention the condition(inside round brackets).
Let’s look into an example for the same...

`do..while Loop` Example

`do{
	block of code to be executed
}while(condition);`

Let’s repeat the same example for `do...while` loop as well.
Let’s try printing `“I love JavaScript”`, 10 times.

The first step is to create a variable.
`var i = 1 ;`

Followed by writing the do block.
`do {
	document.write(“I love JavaScript”);
	i = i + 1; 
}`
In the above code, we’re printing `“I love JavaScript”` followed by increasing the value of i by `i + 1`, which basically means, add 1 to current value of `‘i’` variable.
In this way we’ll meet our condition.

Till now, we’ve written the following code:
`var i = 1;`
`do{
	document.write(“I love JavaScript”);
	i = i + 1;
}`

Now, let’s add the while part mentioning the condition in round brackets.
Repeat `“I can Loop”`, 50 times:

`var i = 1 ;`
`do{ 
	document.write("I can Loop");
	i = i + 1;
} 
while ( i <= 10 );`
Note: Do not forget the semicolons after while().

Repeat “I can Loop”, 50 times
`Tap the correct answer to fill in the blanks`

`var i = 1 ;`
`do{ 
	document.write("I can Loop");
	i = i + 1;
} while(i <= ___ );`

`50`, `I can Loop`

<animated_do_while_loops.gif>
Wow! Great!
You remember everything!
Let’s dive in deeper!
Shall we?

9. Showcasing Important Messages
(Topic-1) What are dialog boxes?
Dialog boxes
<animated_announce.gif>
There has been situations where we want to convey something crucial, and we generally go shouting about it .
Like, when mom gives us the grocery list, she mentions something like, 
“DO NOT FORGET THE TOMATOES”, “THE MILK SHOULD BE SUGAR FREE”.
In articles, writers generally bold the crucial words.
Similarly, on a website when we want to display an important message, we showcase it using something known as dialog box.

What is a Dialog Box?
<dialog_box.png>
Dialog box is a small window that pops up when a particular key is pressed.
Usually it is used to deliver important messages.

(Topic-2) Types of dialog boxes
Types _ dialog boxes
<animated_dialog_box.gif>
There are three types of dialog boxes in JavaScript.
These dialog boxes can be used to either show confirmation messages, pop up an error or show warning messages.
We can also get inputs from these dialog boxes.

Types of dialog boxes
The following are the dialog boxes in JavaScript:
1. Alert Dialog Box
2. Prompt Dialog Box
3. Confirm Dialog Box
Don’t worry, we’ll study each of them in detail.


1. Alert Dialog Box
<animated_alert_box.png>
An alert box is usually used to display messages .
It can also be used to display warning messages.
Alert box has only one button "OK" to select and proceed.
Let’s see how we can generate an alert dialog box.

Alert Dialog Box
<dialog_box.png>
Let’s say you want to display the message, “I am a cool dude!” ;)
We’ll start by writing the alert keyword followed by opening and closing round brackets.
`alert() ;`
Do not forget the semicolon.
In between the round brackets, we write our message.

Alert Dialog Box
`alert(“I am a cool dude”);`
The above code would give an output as the above.
Haha! Easy right?
Let’s get into the next Dialog Box.. :D

But before that, let’s take up a quiz.
`Choose the valid one by select the right answer`

`alert(I know how to JS”);`
`alert“I know how to JS”);`
`alert(“I know how to JS”);`
`(“I know how to JS”)alert;`

Prompt Dialog Box
<dialog_box_prompt.png>
Prompt Dialog Box is usually used when we want the user to input something.
It consists of two buttons, “OK” and “Cancel”.
It also consist of a text box where the user can input values.
Let’s see how to create one…

Prompt Dialog Box
<dialog_box_prompt.png>
Let’s say, we want the user to input his name in the text box provided.
We’ll start by writing the prompt keyword followed by opening and closing round brackets.
`prompt() ;`
In between the round brackets, we write our message.
In this case the message would be “What’s your name?”.

Prompt Dialog Box
`prompt(“What’s your name?”);`
The above code would give an output like the one above.
Let’s get into the next Dialog Box.. :D
But before that, let’s take up a quiz.

Choose the valid one:
`Select the right answer`
`prompt(“Do you know JS?”);`
`prompt(Do you know JS?”);`
`prompt(“Do you know JS?”;`
`(“Do you know JS?”)prompt;`

Confirm Dialog Box
<dialog_box_confirm.png>
This dialog box is usually used, to provide `confirmation` for a specific action.
For example, when we delete a picture on Facebook then it could request confirmation from the user, like “Do you really want to delete this picture permanently?”.
We can either say Yes or No right?
It consist of two buttons, “OK” and “Cancel”.
When we click on the “OK” button it returns true(yes) otherwise it returns false(no).
Let’s see how we can generate a confirm dialog box..

Confirm Dialog Box
Let’s take the previous example and create a dialog box which asks the user if they really want to delete the picture or not.

We’ll start by writing the confirm keyword followed by opening and `closing round brackets‘()’`.
`confirm() ;`
Do not forget the semicolon.
In between the round brackets, we write our message.
In this case the message would be “Do you really want to delete this picture permanently?”.

Confirm Dialog Box
<dialog_box_confirm.png>
`confirm(“Do you really want to delete this picture permanently?”);`
The above code would give an output similar to above.
And this is how we create dialog boxes.

Let’s take up a quiz.
`Choose the valid one: Select the right answer`

`confirm(“Do you know JS?”);`
`confirm(Do you know JS?”);`
`confirm(“Do you know JS?”;`
`(“Do you know JS?”)confirm;`

(Topic-3) Let's Revise _ Dialog Boxes

Choose the invalid one:
`Select the right answer`

`confirm(“Are you sure?”);`
`alert(“We’ll delete your picture now”);`
`prompt(“enter your age”);`
`prom(“enter your date of birth”);`

Let’s revise
In this topic we’ve learned:
1. What is a dialog box?: Dialog box is a small window that pops up when a particular key is pressed.

2. What are dialog box used for?: Dialog boxes are used to either show a confirmation messages, raise an error or show a warning message.

3. Types of dialog boxes: Alert Dialog Box, Prompt Dialog Box and Confirmation Dialog Box.

Alright, let’s move on to the next topic….


(Lesson-10). Grouping Tasks Together.

(Topic-2) Final Chapter
<animated_loop.gif>
Final Chapter
Congrats! You made it to the final chapter of basic JavaScript.
We boarded the journey together and have come this far, starting from `variables`, to `if..else`, to `loops`..

It has been quite a progressive journey!
Let’s go ahead and learn one last topic (`functions`).
Shall we?

Introduction
<calculator.jpg>
Let’s say we want to create a program which will print the result of addition of two numbers.

We would create 2 variables to hold the values of two numbers and another variable which will hold the value of the addition of the numbers.

`var x = 2;`
`var y = 3;`
`var z = x + y;`

Followed by printing the 3rd variable as follows:
`document.write(z);`

What if we’ve to calculate the results of several combinations like, `1 and 2`, `4 and 5`, `6 and 7` etc ?

Then creating a new variable every time and adding it in the third variable would be a lot of work to do.. Right?

What if I tell you that there’s a way to just write the code once and use it for any combination of numbers?

That is, to write reusable code which could be used anywhere in the program.

The term we’re looking for is called `Functions`.
Let’s learn about it.


(Topic-2) Creating a function

What’s a function?
<animated_loo.gif>
A function is a block of reusable code which can be used anywhere in the program.
The main aim of a function is to eliminate the need of writing the same code again and again.
Like if we can create a function which would perform addition, and we can call it several times to perform the same task rather than writing separate codes whenever we want to perform addition.
Now that we know what a function is, let’s go ahead and learn how to create one.

How to create a function?
A function can only be used when it is called.
Until and unless we call the function which adds numbers, the function will sit ideally being jobless. :p

So the first step is function definition, which basically means to define the function i.e. to create a function.

Once we’re done defining the function, the next step is to call and use it.
Don’t worry, we will learn each and every step.
Let’s start with the first one.

How to create a function.
A function can be defined in the following way:

    `function functionname(){
        code
    }`

We start defining the function by using the function keyword followed by the name of the function which is then followed by open and close round brackets. Once we’re done with it, we write the reusable code inside the curly brackets.

Function example.
Let’s create a function which prints “I know JavaScript!”.

We’ll start by writing the `function` keyword followed by `naming the function` and opening and closing the `round brackets`.

`function print()`

We’ve named our function as `print`.

Once we’re done with it let’s write the code to print inside curly brackets.

`function print() {
	document.write(“I know JavaScript!”);
}`

Yes, we’re done with the function definition, let’s move on to `calling the function`.

Calling a function
<calling_a_function.jpg>
Now, we've got a function named `print` which prints `“I know JavaScript!”`.

The next step is calling the function.

`Calling a function` is as easy as writing the name of the function followed by `opening and closing round brackets`.

So, the whole code would look something like:

`function print() {
	document.write(“I know JavaScript”);
}`

`print();`

Let’s say we’ve a function called add() which performs addition of two numbers, don’t worry, we shall write it soon. 
`Choose the valid option to call that function.`

`add( ;`
`()add ;`
`add() ;`
`add{} ;`

(Topic-3) Using an outside variable inside a function

Why do we need an outside variable inside a function?
Let’s build up on the addition function.

We’ll create a function followed by declaring two variables and then performing addition in the third variable and finally printing it out. 
Finally, we will call the function.. Right?

As we had mentioned earlier, the main aim of function was to make the code reusable.

So how do we put in different values in the function so that it will print the result?

The solution to that is Parameters!

Parameters?

    `function functionname(parameter){
        code
    }`

`functionname(parameter)`

Parameters are passed while calling the functions and later those passed parameter can be manipulated inside the functions.

That is, let’s say we pass 2 and 3 in our add function while calling it, then inside the function we can use the passed parameters i.e 2 and 3 to perform their addition and hence printing it out.

Similarly, we can pass 4 and 5 as a parameter to that function and hence printing the result.

Thus becoming successful in making our function reusable.

Let’s write a program to get a clear picture of the same.

Addition function example.
Let’s create a function to add two numbers.

Let’s start by creating a function.

    `function add(){
    }`

Now, since we are going to call this function using parameters, thus we’ve to mention it while creating the function. 

This is how we do it.

    `function add(num1, num2){
    }`

Here, num1 and num2 are the two numbers we’ll get as parameters while the function is called.

Addition function example.

Now let’s go ahead and create a variable which would store the value of the end result.

    `function add(num1, num2){
        var result = num1 + num2 ;
        document.write(result);
    }`

We’re ready to call the function!
    `add(3,4);`
    
In this scenario, we’re passing `3 and 4` as `parameters` to the function.

So, `num1` becomes 3 and `num2` becomes 4 and hence the result variable stores the result and prints it out.


(Topic-4) Let's revise _ Grouping | Funtions

Choose the valid one to create function:

`function functionName{} ()`
`function functionName() {}`
`function() functionName{}`
`Function{} functionName{}`

Choose the valid one to call function with parameters:

`add(3,4);`
`add{3,4};`
`add(3,4){};`
``add{3,4}``

Let's Revise
And this is the end of this course..
But not the end of learning.
I hope we’ve done our job to fullest.
And motivated you enough to explore Advanced JavaScript..

