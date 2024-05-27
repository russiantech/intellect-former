(Course) JavaScript Advanced

(Lesson-1) Scope
Topic-1. What is scope?

What is scope?
<scope.png>
How often and in what context do you use the word scope?
In a normal scenario, if you can access something then it falls within your scope or else it falls out of your scope.
The same concept applies to programming.

The accessibility or validity of a variable is determined by its scope.
Suppose a variable is declared inside a function. And we try to access the variable outside that function.
Then we will encounter an error that the variable we are trying to access is undeclared.

Why?
<scope_local_global.png>
Because the scope of that variable is limited to that function.

In JavaScript there are two types of Scope:
1. Local Scope
2. Global Scope
Let’s explore each one of them in detail.

Which of the following sentences are correct with respect to scope ?

`Select one or more answers`
`The scope of a variable depends on where it is declared.`

`We will encounter an error when the variable we are trying to access is out of scope.`

`The accessibility or validity of a variable is determined by its scope.`

`We declare scope with the variable declaration.`


Topic-2. Local scope

Local scope
<scope_local.png>
Whenever a variable is declared inside a function it is said to have local scope.

A variable declared inside a function can only be used inside that function.

A variable declared inside a function cannot be accessed or used outside the function.

Let’s write a function localFunction and declare a variable localVar inside it.

Do you remember how to write a function and a variable?

 <-- Define a function -->
`function localFunction(){
	<-- Create a variable and store value 50 -->
  	var localVar = 50;
}`

Here, localVar is a variable whose scope is limited to the function localFunction.

Now, let's try to log the value of localVar outside the function.

 <-- Define a function -->
function localFunction(){
	<-- Create a variable and store value 50 -->
  	var localVar = 50;
}
<--Print the value of variable -->
console.log(localVar);
Can you guess the output of the above snippet?

We will encounter an error, something similar to
Uncaught ReferenceError: localVar is not defined, 
Because the scope of that variable is limited to the function.

 <-- Define a function -->
`function localFunction(){
	<-- Create a variable and store value 50 -->
  	var localVar = 50;
	<--Print the value of variable -->
	console.log(localVar);
}`

<-- Call the   function localFunction -->
localFunction();

Now, if we try to log the value of the variable inside the function and call the function, we will get the output `50`

Because the variable is now accessed within its scope.

A local variable can be accessed anywhere in the program.
Select the right answer
`False`
`True`

Topic-3. Global scope

Global scope
The variables which can be accessed everywhere are said to have global scope.

These variables are not declared inside any function.

A global variable is defined outside all functions.

And a global variable can be accessed by any function.

Let’s see how we can declare a global variable and how it can be used.

 <-- Create a variable and store value 5 -->
var globalVar = 5;

<-- Define a function -->
function newFunction(){
	<--Print the value of variable -->
	console.log(globalVar);
}

<-- Again print the value of variable -->
console.log(globalVar);

<-- Call the function using function name-->
newFunction();

The output of the above program will be
5 5

In the above snippet, we have a variable globalVar whose scope is not limited to any function and thus can be accessed everywhere, even within a function.

A global variable can be accessed anywhere in the program.
Select the right answer
False
True


Topic-4. Hoisting

Hoisting
<javascript_flag.png>
In JavaScript, all the variable declarations are moved to the top of their scope.
This is known as hoisting.

In JavaScript, a variable can be used before it is declared.
What does this mean?
It means that:

var newVar = 50;
…
…

And
…
…

var newVar = 50;

Will result the same output, because all the variables are automatically moved to top when we run the program.

This concept is known as hoisting.

Topic-5. Let’s Revise

<-- Define a function -->
`function someFunction(){
	<--create a variable and store value 6 -->
  	var a = 6;
}`

<--print value of variable -->
console.log(a);

<-- call the function using function name-->
someFunction();

What will be the output of the above snippet?
Select the right answer
`6`
`0`
`Nothing will be printed, blank screen.`
`An error will be encountered stating undeclared variable a.`

What is hoisting in JavaScript?
Select the right answer

`JavaScript’s behaviour of moving variable declarations to the top.`

`Making every variable a global variable.`

To Summarize
A scope of a variable is the block where it can be accessed and used.

If a variable is declared inside a function it is known as a local variable and it is said to have a local scope.

If a variable is declared globally, it is said to have a global scope.

Hoisting is JavaScript’s behaviour of moving variable declarations to the top.


(Lesson-2) Playing With Strings
(Topic-1) What is a string?

What is a string?
A string is a sequence of characters.
All the textual data that you can see floating on the screen right now are strings.

In JavaScript, strings are used to store and manipulate textual data.
Anything written inside quotes is a string.
`var newStr = “Hey! I am a string.”;`
Here, newStr is of type string containing `“Hey! I am a string.”` as value.

How do you declare a string in Javascript?
<var.png>
Just like every other variable declaration, strings are declared using the var keyword in Javascript.
For example :
`var strName=”Mike”;`
Here, `var` is the keyword,
`strName` is the string variable name,
`Mike` is the value of the variable.

JavaScript accepts both single quotes (‘ ‘) and double quotes (“ “) for enclosing strings.
Be careful, not to mix up the quotes.
If you begin a string using a single quote, you should end it with a single quote
If you begin a string using double quotes then you should end it with double quotes.

Which of the following statements are correct with respect to a string?
Select one or more answers
`A string can be written using both single and double quotes.`
`A string is a sequence of characters.`
`A string is declared using var keyword.`
`Strings are used to store and manipulate textual data.`


(Topic-2) Operations on strings

Operations on strings
<operations.png>
Awesome, we know how to declare and initialize strings in JavaScript.
Let’s see some of the built-in properties and methods that are used to perform operations on the strings.

Finding the length of the string
To find the length of the string, we use the built in length property.
To use this property we write
`stringName.length;`

So, what should we write in order to find the length of the string `“HeyString”`?
 <-- Create a variable and store a string value  -->
`var newStr = “HeyString”;`

<-- Find the length of defined variable and store in another varibale -->
`var strLength = newStr.length;`

Can you guess what should we get as output?
We will get the length of the variable as 9.

Joining two strings
<concatenation.png>
To join or concatenate two strings, `concat()` method is used.
`string1.concat(string2);`
Just like that!

And the method returns a new string formed by joining `string2` after `string1`.

 <-- Create a variable and store a string value  -->
`var string1 = “Hey”;`
<-- Create another variable and store another string value  -->
`var string2 = “String”;`
<-- Create another variable and store the combinaton of first two variable values -->
`var string3 = string1.concat(string2);`

So, the value of the string3 will be `HeyString`.
This is how string concatenation works.

String concatenation can also be achieved using the ‘+’ operator.

 <-- Create a variable and store a string value  -->
`var string1 = “Hey”;`
<-- Create another variable and store another string value  -->
`var string2 = “String”;`
<-- Create another variable and store the combinaton of first two variable values -->
`var string3 = string1 + string2;`

So, the value of the string3 will be `HeyString`.
Wow! That’s easy as abc. Let’s move ahead.

Finding a substring
<sub_str.png>
`substr()` method is used to extract a substring from a string.
It takes two parameters,
`stringName.substr(starting index of substring, length of the substring);`

Let’s see this in action.
Let’s extract a substring from “I am in love with strings.”.

 <-- Create a variable and store a string value  -->
`var myString = “I am in love with Strings.”;`

<-- Extract a string from the variable from position 5 upto length 7 -->
`myString.substr(5,7);`

The statement , `myString.substr(5,7)` says/means to pick 7 characters beginning from position 5th.

The above snippet will return `“in love”`.

Remember! space is counted as a character.

Converting string to uppercase & lowercase
What better than built-in methods to transform strings to uppercase and lowercase.

`toUpperCase()` method is used to convert a string to `uppercase`.

And, `toLowerCase()` method is used to convert a string to `lowercase`.

Let’s see these in action.
 <-- Create a variable and store a string value  -->
`var myString = “Don’t mess with my case.”;`

<-- Convert the value of variable to `Uppercase` -->
`myString.toUpperCase();`

The above snippet will return `"DON’T MESS WITH MY CASE."`

And writing
 <-- Convert the value of variable to Lowercase -->
`myString.toLowerCase();`
will return `"don’t mess with my case."`


(Topic-3) Let’s Revise

Which of the following is an accepted syntax to declare a string in JavaScript?
Select the right answer
`var stringName = “Hello”;`
`string stringName = “Hello”;`
`“Hello” = stringName`
`stringName = “Hello”;`


`var newStr = “Another Hey!”;`
<-- Create a variable and store a string value  -->

<-- Print the length of the variable value -->
`console.log(newStr.length);`

What will be the above snippet return?
Select the right answer

`10`, `11`, `12`, `9`

substr() is used to
Select the right answer:
`Cut out the string into two parts`
`Write a new string in place of the present one`
`Extract a substring from the present string.`
`Concatenate two strings`

To summarize
A string is a `sequence of characters`.
Anything written inside `quotes` is a string in JavaScript.
To find the length of the string the built-in property, `length`, is used.
To join or concatenate two strings, `concat()` method is used.
`toUpperCase()` method is used to convert a string to uppercase and `toLowerCase()` method is used to convert a string to lowercase.


(Lesson-3) Numbers & Booleans
(Topic-1) What are Numbers?
What are Numbers?
<why_numbers.png>
Unlike other programming languages, JavaScript does not have different data types for integers and floating points.
Numbers are categorized into only one data type which is number.
Thus, 5 and 5.62 both have same type number.

Just like every other variable declaration, numbers are also declared using the var keyword.
For example:
`var height=5.62;`
`var age= 19;`

Here, var is the keyword, Height and age are the variable names, 5.62 and 19 are the respective values of the variables
Both the variables height and age are of type number.
Awesome, we know how to declare numbers in JavaScript.

Let’s jump to the operations that can be carried out on these numbers.
JavaScript has many built-in methods to do so. Let’s explore few of them.

Which of the following statements are correct with respect to a number?
Select one or more answers
`A number in JavaScript can be of two types: integer or floating point.`
`JavaScript identifies all the numbers under one category which is numbers.`
`A number is declared using var keyword.`
`None of the above.`

(Topic-2) Operations on numbers

Rounding off the numbers
<number_rounding_off.png>
Many times a situation arises when we need to round off the numbers to the fixed number of decimal places.
That’s when `toFixed()` method comes to rescue.

How to use it?
`variable _name.toFixed(number_of_decimal_places);`

Example: To round off 3.142 upto two digits we write,
`var myNum=3.142;`
`myNum.toFixed(2);`
Yeah. It is that easy!

<-- Create a variable and store a decimal value -->
`var newNum = 34.463;`

<-- Round off the variable value to 2 decimal places -->
`newNum.toFixed(2);`

The above method will return `34.46`.

And, `newNum.toFixed(1)` will return `34.5`. 

Can you guess the what `newNum.toFixed(0)` will return?
If your answer was `34`, you are awesome.

Converting a number into a string
<num_to_str.png>
Yes, you can convert a number to a string.
This can be done using `toString()` method.

 <-- Create a variable and store an integer value -->
`var myNum = 456;`

<-- Convert the integer value to String value -->
`myNum.toString();`

The above method will return `456` but this time its data type will be string.

Writing numbers up to a precision
Just like `toFixed()`, `toPrecision()` method also returns a rounded off number.

But it takes the total number of digits as the argument.

Suppose, we write `toPrecision(3)` so it will return a number which has exactly 3 digits.

Let's see how it works:

<-- Create a variable and store a decimal value -->
`var myNum = 34.563;`

<-- Round off the variable value to exactly 3 digits -->
`myNum.toPrecision(3);`

The above method will return `34.6`. And, 
`myNum.toPrecision(5)` will return 34.563.

Isn’t that cool?
Awesome, time to move to our next data type - Boolean. True!


(Topic-3) What is a boolean?

What is a boolean?
<boolean.png>

Are you a human being? `YES`.
Do you like pizza? `NO`.
Do you like dogs? `YES`.

See how the questions to the above answers can either be YES or NO. This is exactly what boolean is all about.

In programming, we often require variables which can have either true or false as values.

These variables come under the type - `Boolean`.
Here’s how we declare a boolean variable,
<-- Create a variable and store value as True -->
`var myBool = true;`

<-- Create another variable and   store value as False-->
`var newBool = false;`

Booleans are used in making decisions.
They find application in conditional statements.
A lot has been said. Let’s answer few questions at our disposal.


(Topic-4) Let’s Revise

<-- Create a variable and store a decimal value -->
`var myNum = 54.4634;`
<-- Round off the variable value to exactly 3 digits -->
`myNum.toPrecision(3);`

What will the above function return?
Select the right answer
`54.463`
`54.47`
`54.5`
`54.45`

`toString()` is used to:
Select the right answer
`Convert a string to number`
`Convert a number to string`
`Both (1) and (2)`
`None of the above`

Which of the following best describes a boolean?
Select the right answer
`A variable which can take true as a value.`
`A variable which can take false as a value.`
`A variable which can either take true or false as values.`
`None of the above.`

To summarize
In JavaScript, all the numbers are categorized into only one data type which is number.

`toFixed()` is used to round off the numbers to the fixed number of decimal places.

`toString()` is used to convert a number to a string.

`toPrecision()` is used to round off a number to a fixed number of digits.

A variable which can take either true or false as values is known as a boolean.
Boolean variables are useful in controlling the flow of a program.

(Lesson-4) Objects In Javascript
(Topic-1)

What are objects?
<objects.png>
Let’s take an example of a class of students.
Necessary information about each student needs to be maintained in a record.

Name, Class and roll_No of the student is the most basic information that identifies a particular student in a class.

So, if we say student is an object then its name, class and roll_No becomes its properties.

Assigning properties helps to maintain structured information about each student.

Although the value of these properties keeps on varying from student to student but the structure of information about each of them remains the same.

We have something similar in JavaScript too.

An object is a collection of related information.Objects consists of properties and methods.

In the earlier example we saw that student is an object and Name, Class and Roll No are its properties.
Our objects may also consist of functions.

For example, a function to calculate the attendance of the students.

We know that variables store values.
<key_val.png>
You shouldn’t be surprised to know that objects store value too.
The only difference is that variables store single values
And objects store multiple values.
These values are written in the form of key-value pairs.
`name: “Chris”`
Here, name is the `key` and Chris is its `value`.
Such named values are called as properties of that object.

Did you notice the `var keyword` in the object above?
<objects.png>
Do you feel any bells ringing in your brains?
Object is also a data type in JavaScript.

It can contain properties of all the other types starting from number, string, boolean, arrays and even other objects.
Isn’t that awesome?

Above example talks about the properties of student object like name, class, roll no and grade.

What if we want the object to perform certain actions using these properties?
For instance, what do we need to do if we wish to calculate age of each student?
To achieve this, we write methods.
Methods are the operations that can be performed on the properties of such objects.

Which of the following sentences are correct with respect to an object in JavaScript?
Select one or more answers
`It is a data type.`
`It is a collection of properties and methods.`
`An object is a representation of a real-world entity.`
`Objects can contain other objects as items.`

(Topic-2) Defining an object

Defining an object
There are three ways to define an object:
1. Using an object literal.
2. Using the new keyword.
3. Using object constructor.
Let’s explore each of them.

Using an object literal
Using an object literal simply means writing object just like we declare any other variables.

`var` followed by the `name of the object` followed by `items inside curly brackets`.

 <-- Create an object with different items -->
`var Student = {
	<-- First item -->
	name: “Chris”,
	<-- Second item -->
	class: 10,
	<-- Third item -->
	roll_no: 45
	};`

That’s it, we have our Student object.

Using the new keyword
Using the new keyword refers to creating an instance of the object.

 <-- Create an object with new keyword -->
`var Student = new object();`

<-- Access the 1st item of object and assign string value -->
`Student.name = “Chris”;`

<-- Access the 2nd item of object and assign integer value -->
`Student.class = 10;`

<-- Access the 3rd item of object and assign integer value -->
`Student.roll_no = 45;`

Here, dot `operator (.)` is used to write keys and assign values to it.

Using object constructor
Object constructor is a function which has the same name as the object.

 <-- Define a constructor with same name as object -->
`function Student(name, class, roll_no){
	<-- Assign the user-defined values to items -->
	this.name = name;
	this.class = class;
	this.roll_no = roll_no;
	}`

<-- This creates an object and send values in the argument to constructor -->
`var Student1 = new Student(“Chris”, 10, 45);`
`this refers to the current object.`

The values are passed as arguments to the object constructor.

Awesome, we learnt all the methods to define an object.
It’s time we learn how to access the properties of these objects.
Track my steps. :)

(Topic-3) Accessing object properties

Accessing object properties
<what_is_ur_name.png>
Accessing properties of any object is similar to the above illustration.
You need something, just ask for it. Go on. Come on. Try.
“Object Student I need to know your name.” That’s it.
But, JavaScript is not intelligent enough to parse that sentence.
So, let’s write the same thing in the format that JavaScript understands.
There are two ways to access properties of the object.
1. Using a dot operator
2. Using bracket notation
Let’s explore each one of them one by one.

Using a dot operator
The same syntax can be used to write new properties as well as reassign the values of existing properties.

`Student.name = “Edet”;`

Will replace the current value of name in the object. 
And,
`Student.house = “Green”;`

Will add a property `house` with value `Green` to the object.

Using bracket notation
We can also access object properties using bracket notation `[ ]`.

`Student[‘name’];`

Will also return the same result as `Student.name`.

And, writing `Student[‘name’] = “Edet”;` will assign a new value to the property name of object Student.

Similarly, we can add new properties.


(Topic-4) Let's Revise _ Js Objects

1.
<-- Define a constructor with same name as object -->
`function School(name, location){
	<-- Assign   the userdefined values to items -->
	this.name = name;
	this.location = location;
	}`

<-- Create an object and send values in the argument to constructor -->
`var School1 = new School(“KVP”, “XYZ Area”);`

Does the above snippet represents a valid object in JavaScript?
Select the right answer
`Yes, it is the literal method of object declaration`
`No`
`Yes, it is declared using object constructor.`
`None of the above`

2. 
<-- Create an object with different items -->
var Car = {
	<-- First item -->
	model: “Fiat ABC”,
	<--   second item -->
	year: 1997
};

Writing `car.model` and `car[‘year’]` will respectively return ____ and ______ ?
Select the right answer

`“Fiat ABC” and 1997`
`“Fiat ABC” only`
`1997 and “Fiat ABC”`
`1997 only`

An object can contain properties of different data types.
Select the right answer
`True`
`False`

To Summarize
An object is a collection of properties and methods.
These properties are written in the form of key-value pairs.

There are three ways to define an object: Using an `object literal`, using the `new keyword` and using `object constructor`.

There are two ways to access properties of the object using a `dot operator` and using `bracket notation`.


(Lesson-5) Dates In Javascript

(Topic-1) The date object

The date object
<date.png>
JavaScript can help you land a date. Seriously!
You just need to grab the gift offered by JavaScript - `The Date Object`.
That’s it. Then you can create your own date. :D

What is Date In Js ?
Date is a built-in JavaScript object.
<date_js.png>
Yes! You heard it right.
It is a JavaScript object.
Can you re collect what does objects consists of?
We have learnt that it consists of certain properties and methods.
We shall explore few of them in the coming chapters.

Date Objectt
<calender.png>
Using this object we can obtain information like current year, current date, current day, current time.

Also, we can specify a new date and a new time.
And, we can also carry out operations on these values starting from manipulating the format of dates to finding the difference between two dates.

Have you ever thought how does this object deal with dates?

Well, it understands and stores date based on a Unix time timestamp.

Which is nothing but the number of milliseconds that have passed since Thursday, 1 January 1970.
We shall see the method that is used to get the date as milliseconds in coming chapters.

That seems pretty interesting to me.
Let’s explore this date object and find out what are the operations that can be performed using these.


(Topic-2) Operations on date

Operations on date
<calender.png>
Let’s start by defining an instance of the date object.
Do you remember how we used the new operator to write an instance of the object?

<-- Create a instance of the Date object -->
`var myDate = new Date();`

This will initialize a new instance of the date object.
Can you guess the value of `myDate` variable?
The variable `myDate` will contain something similar to
`Sat Apr 27 2024 12:15:21 GMT+0100 (British Summer Time)`

A long string containing `day`, `month`, `day of the month`, `year`, `time` and the `time zone`.
This is nothing but the current date and time.

So, writing
<date_time.png>
`var myDate = new Date();`
Will store the current date and time in the variable `myDate`.

Mesmerizing! isn’t it? So much information to play with.
Time to explore few common methods present in the date object.

Remember, we studied that we can obtain current year, current date, current day, current time, and what not!

To get all these information, use the following methods:

1. getDate() - Returns the current day of the month. A number between 1 and 31.
2. getDay() - Returns the current day of the week. A number between 0 and 6.
3. getTime() - Returns the number of milliseconds elapsed since January 1, 1970 which is nothing but the current time.
4. getFullYear() - Returns the current year.
5. getMonth() - Returns the current month of the year.

Similarly, `getMinutes()`, `getHours()`, `getSeconds()` are some other methods present in the date object.

Awesome! But how to use these methods?
It is as simple as ABC.
<-- Create a instance of the Date object -->
`var myDate = newDate();`

<-- Call the required method  using the dot operator -->
`myDate.getFullYear();`

And the above method `getFullYear()` will return `2024` as of now.
Similarly, other methods can also be used to get the respective data.

Use Date
<copyright_c.png>
Have you noticed the year mentioned right next to the copyright symbol on the websites?

I am pretty sure, that by now you have guessed how that works.
`myDate.getTime()` to move ahead and explore few more methods present in the date object. ;)

Just like the way we can obtain the data from the date object, we can also set our own.

To do so, it provides the following methods:

1. `setDate()` - Sets the day of the month. A number between 1 and 31.
2. `setTime()` - Sets the number of milliseconds elapsed since January 1, 1970.
3. `setFullYear()` - Sets the year.
4. `setMonth()` - Sets the month of the year.

Similarly, `setMinutes()`, `setHours()`, `setSeconds()` are some other methods present in the date object.

<-- Create a instance of the Date object -->
`var myDate = newDate();`

<-- Call the required method with arguments using the dot operator -->
`myDate.setFullYear(2030);`

The above method setFullYear() will set the year to be 2030.

In the same way, other set methods can also be used.
Let’s move ahead and see if you get the date.


(Topic-3) Let’s Revise

1. 
The getDay() method of the date object will return _____?
Select the correct option.
`Day of the year`
`Day of the week`
`Day of the month`
`Day since January 1, 1970`

2. 
<-- Create a instance of the Date object -->
`var yourDate = new Date();`
<-- Call the required method   with arguments using the dot operator -->
`yourDate.setDate(24);`

The above method will do _______?
Select the right answer
`Set the day of the month to 24`
`Return the day of the month`
`Set the day of the month to 23`
`Set the day of the year to 23`

3. 
<-- Create an instance of the Date object -->
`var myDate = new Date();`
The variable `yourDate` will have the value of ________?
Select the right answer

`The number of seconds elapsed since Jan 1, 1970`
`The number of seconds elapsed since the beginning of the day`
`The current date and time`
`None of the above`

To summarize
The JavaScript date object contains methods and properties related to date and time.

JavaScript stores dates as number of milliseconds passed since the Unix time.

To use the methods and properties of the date object, we first create an instance of it using the new keyword.
`var myDate = new Date();`

There are many methods which we can use `to get` the date, time, year, month, etc.

Similarly, we can `also set` the above things using the various set methods.


(Lesson-6) Document Object Model

(Topic-1) What is a DOM?

What is a DOM?
Can you draw your family tree on a paper?
Starting from your forefather’s generation, then your grandfather’s generation, then your parents and then you.
Similarly, browser also creates a tree, but this tree consists of HTML elements, attributes, values, content and more.

What is a DOM?
<dom.png>
DOM or Document Object Model is the soul of web applications.
It is a tree structure of objects created by the browser.
This tree consists of elements, attributes, values, content, basically everything that we have written in HTML.
Thus HTML DOM outlines a standard in which we can add, delete, get or change the elements of HTML.

Now we know that DOM enables us to manipulate the content or the HTML using JavaScript.
Let’s see how this DOM actually looks like.
Consider a basic HTML webpage with the following markup.
 <html>
	<head>
	</head>
	<body>
		<p>
		</p>
	</body>
</html>
This is a simple HTML markup containing nothing but a sequence of elements.
DOM is created when such a file is opened in the web browser.

And the DOM looks like above
<dom.png>

In the above image you can see the element nodes and their children.
The outer nodes are the parent nodes and the enclosed ones are the children nodes.

`<html>` is at the root, then `<head>` and `<body>` are its children.

`<p>` becomes the child of `<body>`

The topmost or the root node is always the document node and It represents the web page.

As the markup grows the DOM also grows and becomes more complex adding all the elements, attributes, values, content, etc.

What is the full form of DOM
Select the right answer
`Document Object Manipulation`
`Document Oriented Model`
`Document Object Model`
`Document Oriented Module`

Before we can learn how to manipulate the web page using JavaScript or how to make changes in DOM, we should first learn how to access the objects of the DOM.
So, let’s first learn how we can access the elements of the DOM.

So, let’s first learn how we can access the elements of the DOM.

(Topic-2) Accessing Elements in DOM

Accessing Elements in DOM
<dom_access.png>
We learned that document is the root node.
Thus to access any of the below nodes we first need to access the document node, always.
There are three identifiers by which these nodes can be identified.
There are three ways by which we can access the nodes.
Let’s have a look at them:

1. Tag name - The name of the tag
2. Class - The classes attached to the nodes/elements.
3. Id - The id assigned to the nodes/elements.

So, we can access the elements:
1. by their name,
2. by the classes attached to them or
3. by the id assigned to them.

There are certain methods which can be used to access the elements via the above identifiers.

1. `getElementsByTagName() `- To find the elements using the tag name.
2. `getElementsByClassName()` - To find the elements using the class assigned to the element.
3. `getElementById()` - To find the element using the id assigned to it.

Awesome! Let’s see these three in action.

Access using Tag Name
<ptag_class.png>
Suppose we want to access all the paragraph tags present in the webpage.

We can simply write:
`document.getElementsByTagName(‘p’);`
The above method will get all the paragraph tags present on the webpage.

Access using Class Name
<ptag_class.png>
Now, to access the elements using the class present in the element we use `getElementsByClassName()` method.

To access the paragraph tag with a class `newClass` as shown above, we can write
`document.getElementsByClassName(‘newClass’);`
This will select all the elements containing the class newClass.

Access using ID
<ptag_id.png>
To access the elements using the id present in the element we use `getElementById()` method.
We can access the `<p> tag` with the id that is assigned to it which is `newId` ,
We write,
`document.getElementById(‘newId’);`
This will select the element containing the id - `newId`.

Awesome. That’s all about accessing elements in DOM using JavaSCript.
Let’s try and answer few questions about the same.


(Topic-3) Let’s Revise _ DOM

To access the element using the class we use
Select the right answer
`document.getElementsByClassName();`
`document.getElemensById();`
`document.getElementsByName();`
`None of the above`

Which one of the following is the root node of the DOM?
Select the right answer
`HTML`
`body`
`document`
`None of the above`

document.getElementById(“me”) will
Select the right answer
`Select all the elements with class - me`
`Select all the elements with tag name - me`
`Select all the element with id - me.`
`None of the above`

What is the full form of DOM?
Select the right answer
`Document Object Manipulation`
`Document Oriented Model`
`Document Object Model`
`Document Oriented Module`

To summarize
DOM stands for Document Object Model.
DOM is a tree structure of objects created by the browser.
DOM enables us to manipulate the content or the HTML using JavaScript.
We can access the elements by their name, by the classes attached to them or by the id assigned to them using getElementsByName(), getElementsByClassName() and getElementById() respectively.


(Lesson-7) Accessing HTML Elements Using Javascript

(Topic-1) Introduction To Accessing Elements In Js

Introduction
<dom_0.png>
Using JavaScript, we can manipulate the HTML of the website
How?
Ask yourself.
Do you remember the browser creates a tree structure of objects which is known by the name of DOM or Document Object Model?

To make changes in HTML, we have to make changes to the DOM.
And the changes made to the DOM are reflected on our webpage.
And, all of that happens at a flick of a wand.
All the magic is done by JavaScript.
That’s awesome.
But before we can learn how to change the contents of HTML, we should know how to access the HTML of our website through JavaScript.
Right?
So, let’s begin our exciting journey.


(Topic-2) Accessing HTML elements

Accessing HTML elements
<access_dom.png>
There are many ways to access the content of the HTML using JavaScript. And believe me, these ways are easier than asking for an element to HTML.

Using the tag name
The document object which is nothing but our DOM provides a method to access the elements using their tag name.
`getElementsByTagName();`
This method takes in the name of the tag as a parameter and returns all the elements having the same tag name.
So, if we write
`getElementsByTagName(“h1”);`
The method will return all the elements with h1 tags.
Since this method is a part of the document object, to use it we need to write
`document.getElementsByTagName(“h1”);`
And that’s it. We will have all the h1 elements which we can modify.

Using Class Name
<ptag_class_0.png>
We all know that HTML elements contain class attributes.
And they can be identified using these class names.
To do so in JavaScript, the document object provides a method.
`getElementsByClassName();`
This method takes in name of the class as a parameter and returns all the elements containing that class.

So, in order to access the `p element` in the above image, we need to write.
`document.getElementsByClassName(“custom-p");`
This will return the elements containing custom-p as a class. In this case, it will return the p element.

<p class=”this-p”>Are you serious?</p>
How can we access the above element?
Select the right answer

`document.getElementById(“this-p”) ;`
`document.getElementsByClassName(“this-p”);`
`document.getElementsByTagName(“this-p”);`
`None of the above.`

Using Id
The method used for accessing the elements by their id is :
`getElementById();`
This method takes in the name of id as a parameter and returns the element having that id.

To access the above p element, we can write
`document.getElementById(“custom-p”);`

Accessing HTML Elements by CSS Selectors
CSS selectors are used to select the elements you want to style which can be `id`, `class names`, `types`, `attributes`, `values of attributes`, etc
We have two methods that can be used to access HTML elements based on the specified CSS selectors.
1. querySelector()
2. querySelectorAll()
Using querySelector is a modern approach of accessing DOM elements.
This method takes in a selector as a parameter and returns the respective elements.
Let us understand how each of them works.

-> `querySelector()` method returns only first element that matches with the specified selector whereas `querySelectorAll()` returns all the matching elements.

querySelectorAll() can be used in the same way as above..

Bingo! We have learnt the ways to access any HTML element using JavaScript.
Let me grab a bite while you give a test of your knowledge. :D

Both these methods take class name, id and element name as arguments.
`document.querySelector(“.className”);`	//to access using class
`document.querySelector(“#idName”);`	//to access using id
`document.querySelector(“tagName”);	`

`querySelector()` returns _____ and querySelectorAll returns _____?
`Tap the correct answer to fill in the blanks`
`all the elements`, `first element`


(Topic-3) Let’s Revise

document.getElementsByClassName(“me”); will return
Select the right answer
`All the elements containing the class “me”`
`Only one element containing the class “me”`
`All the elements containing the id “me”`
`None of the above`

To access any element using its id we use the method
Select the right answer
`getElementsById()`
`getElementById()`
`getAllElementsById()`
`None of the above.`

<--Print a paragraph -->
<p> Now, dare to access me. </p>
How can we access the above element?
Select the right answer

`document.getElementById(“p”)`
`document.getElementsByClassName(“p”)`
`document.getElementsByTagName(“p”)`
`None of the above.`

document.querySelectorAll(“p”) will return _________?
Select the right answer
`The first p element it encounters`
`The last p element it encounters`
`All the p elements it encounters`
`None of the above.`

To summarize
We can access HTML content using JavaScript.
To do so, the document object provides these methods.
`getElementsByTagName()` - It returns all the elements with the tag name specified as a parameter.

`getElementsByClassName()` - It returns all the elements with the class name specified as a parameter.

`getElementById()` - It returns the elements with the Id specified as a parameter.

`querySelector()` - It returns the first element that matches the specified CSS selector.

`querySelectorAll()` - It returns all the elements that matches the specified CSS selector.


(Lesson-8) Manipulating HTML Elements Using Javascript

(Topic-1) Introduction To Manipulating Elements

Introduction
Now we know how to access the elements of HTML.
Also, we know if we make any changes to the DOM, these changes are reflected in our web page.

Manipulating HTML elements is just a two step process:
1. Select the HTML element.
2. Play with it

So, what’s stopping us?
Let’s dig in and learn how to manipulate HTML using the JavaScript.

(Topic-2) Manipulating HTML elements

Manipulating HTML elements
There are a lot of things that we can do to our HTML using JavaScript.
Be it -
`writing some text or HTML elements in the document,`
`creating new HTML elements,`
`removing the present ones.`
Let’s see how.

Writing HTML content
JavaScript provides `innerHTML` property which can be used to set the contents of HTML.
Obviously, the first thing we need to do is `access the element`.
And then use `innerHTML` property using a dot operator
`document.getElementById("lone-p").innerHTML = "Here is some text for you!";`
This will print “Here is some text for you!” on the web page.

Changing the content of HTML
<ptag_class_1.png>
What if there’s some text already present in the p element?
Then writing
`document.getElementById(“not-alone”).innerHTML = “Replaced you!”;`
will overwrite the text present and replace it with the new value.
Let’s try to see this work using an example;

We can also add HTML tags by writing the tags within values of `innerHTML` property:
For instance, we consider this p element.
 <-- This will declare a paragraph with id name -->
`<p id= “bold-me”></p>`
We want to write some bold text inside the above mentioned p element. We can do
 <-- Access the paragraph and store the content with bold text -->
`document.getElementById(“bold-me”).innerHTML = “<b>Just like this</b>”;`

<h1></h1>
How can we write some text inside the above mentioned h1 element?
Select the right answer

`document.querySelector(“h1”).innerHTML(“Some text.”)`
`document.querySelector(“h1”).write = “Some text.”`
`document.querySelector(“h1”).innerHTML = “Some text.”`
`document.querySelector(“h1”).inner = “Some text.”`

Creating new elements
Let us explore how to create new elements using JavaScript..
To do so, we use the method `createElement()` of the document object.
An element get created when we simply write,
`document.createElement("p");`
Now you’re smart enough to understand that we are passing the element which we want to create as its parameters.

Appending elements
<-- Create a division tag with Id name -->
<div id=”meDiv”></div>

Consider we have to insert a p element inside an existing div.
We know how to create a new element, but we also need to insert it into the DOM.

 <--Create a new element and store it in a variable -->
`var newEl = document.createElement("p");`

<--Create some text for new element and store it in a variable -->
`var someText = document.createTextNode("Some Text Here!");`

<-- Insert text into newly created p element and store it in a variable -->
`var insertThis = newEl.appendChild(someText);`

<-- Insert the p element inside the present div -->
`document.getElementById("meDiv").appendChild(insertThis);`

This will insert the p element into the div.
Also, createTextNode() method is used to create a new text node.

Remove an element
Consider the below HTML markup.
 <--Create a division tag with Id name -->
`<div id=”thisDiv”>
	<--Create a paragraph with Id name and print the text -->
	<p id=”thisP”> Hehe! I am going to die. </p>
</div>`
We wish to remove the p element present inside the div.
To do so we have a method removeChild().

 <-- Access the division with specific ID name-->
`var divEl = document.getElementById(“thisDiv”);`

<-- Access the paragraph element -->
`var pEl = document.getElementById(“thisP”);`

<-- Remove paragraph element from division -->
`divEl.removeChild(pEl);`

Although we have removed the tag in the example above but learning JavaScript is still cool, isn’t it?

Setting an attribute
Attributes provide additional information about the element.
We can set the values of attributes present in the elements using JavaScript.
This can be achieved using the setAttribute() method.
The setAttribute() method takes in two parameters - name of the attribute and its value.
`setAttribute(“attribute”,”value”);`

Let’s see how this works.
Let’s try to add href attribute to the below anchor tag.

<--Create a link with given text -->
<a>Google</a>

<-- Access the anchor element -->
`var aEl = document.querySelector("a");`

<-- Set a href attribute in the <a> tag -->
`aEl.setAttribute("href","http://google.com");`
This will add the href attribute to the anchor tag.
Similarly, other attributes can also be added.

In case an attribute already exists then its value will be replaced.
Awesome, now we know how to add an attribute.
Let’s learn now how to remove the attributes through JavaScript.

Remove Attribute
To remove any attribute we use the method `removeAttribute()`.
Suppose, we want to remove the `href` attribute from the `a` element.

<-- Create a link -->
<a href=”http://google.com”>Google</a>

To do so, we can write
`document.querySelector(“a”).removeAttribute(“href”);`
The `removeAttribute()` method takes only the name of the attribute as an argument.

We have learnt a lot about changing HTML.
Let’s put this knowledge to test.

(Topic-3) Let's Revise _ Manipulating Elements

What is the correct syntax to create a new element?
Select the right answer
`document.create(elementName)`
`elementName.create();`
`createElement(“elementName”);`
`document.createElement(“elementName”);`

To set the value of any attribute which method is used?
Select the right answer
`attr()`
`setAttribute()`
`attributeSet()`
`None of the above.`

<p>Write Something Here</p>
How can we replace the text inside the above p element?
Select the right answer

`document.querySelector(“p”).write(“Some text.”)`
`document.querySelector(“p”).write = “Some text.”`
`document.querySelector(“p”).innerHTML = “Some text.”`
`document.querySelector(“p”).inner = “Some text.”`

To summarize
1. `innerHTML` property can be used to set the contents of HTML.
2. We can write HTML tags inside the value we pass to the innerHTML property.
3. `createElement()` is used to create new elements.
4. `createTextNode()` method is used to create a new text node.
5. `appendChild()` method is used to append elements to another element.
6. `setAttribute()` method is used to set the value of attributes and `removeAttribute()` is used to remove the present attributes.


(Lesson-9) Manipulating CSS Using Javascript

(Topic-1) Introduction _ Manipulate CSS

Introduction
<css_artist.jpg>
JavaScript is truly an artist.
We have already seen how it can manipulate the HTML of a web page.
Now it’s time to see what it can do to the CSS.
Well, to our expectations, It can do everything.
It can change the font, font-size, colors, add images, and what not.
Exciting! Isn’t it?
Warning: Cool stuff ahead.


(Topic-2) Manipulating CSS

Manipulating CSS
<css_artist.jpg>
We can add any CSS or change the existing CSS of any element.
To do so we use the `style property `of the element.
The syntax of which is as follows:
`el.style.cssProperty = value;`

Where `el` is the element, `style` is the property of the element, `cssProperty` is the property to be manipulated and `value` is the value of that property.

Apparently, we need to access the element first to change its property.

 <--Print the paragraph text -->
<p>Here I come, again.</p>

Let’s see how we can change the font-size of the text in the p tag.

 <--Access the paragraph element -->
`var el = document.querySelector(“p”);`

<-- Make paragraph font-  size 25px -->
`el.style.fontSize = “25px”;`

This will make the font-size of the text in p tag equal to 25px.

What if we wish to change the colour of the text?
To do so, we can simply write
`el.style.color = “green”;`
This will change the color of the text to green.

Do you want me to make the text invisible?
This can be done using the display property.
`el.style.display = “none”;`

This will set the paragraph’s display property to none and the text will be hidden.

We can also change the background color of the text.
To do so, we need to write
`el.style.background = “red”;`

This will set the background color red.

On similar lines, we can change the margin, padding, border, change alignment, etc.

Basically, everything that can be done using CSS.
Awesome! We have learnt how to change CSS using JavaScript.
Let’s put this knowledge to test.

(Topic-3) Let’s Revise

To change the CSS of any element, style property can be used
Select the right answer
`False`
`True`

To change the background of the webpage to black, we can write
Select the right answer
`document.querySelector(“body”).style.color = “black”;`
`document.querySelector(“body”).color = “black”;`
`(“body”).background = black;`
`document.querySelector(“body”).background = “black”;`

We can change every CSS property using JavaScript.
Select the right answer
`True`
`False`

document.querySelector(“p”).style.margin = “20px”; will
Select the right answer
`Create a margin of 20px from the top`
`Create a margin of 20px from the top, left and bottom`
`Create a margin of 20px on all sides.`
`None of the above`

To Summarize
We can add any CSS or change the existing CSS of any element using JavaScript.

To do so, we use the style property of the element.
The syntax of style is
`el.style.cssProperty = value;`

Where `el` is the element, `cssProperty` is the property to be manipulated and value is the value of that property.

We can change the margin, padding, border, alignment, color, background-color, etc. 
Basically, everything that we can do using CSS, can be done using JavaScript as well.


(Lesson-10) Events In Javascript
(Topic-1) What are Events?

What are Events?
<events.png>
An event is an occurence.
Just like the boy in the image kicking the ball. Here, the kick is an event.
JavaScript mostly interacts with the HTML when events are encountered.
Event can either occur by action of the user or by the action of the browser itself.
Clicking a button, hovering over, resizing the browser window, pressing a key on the keyboard are events done by the user.
Whereas, loading of the web page, resizing the browser window is an event that happens to the browser.
JavaScript is a powerful language.
It gives us the power to act when these events occur.
We can decide what actions we want to perform when these events occur.
For this purpose ,each event has an event handler which is a block of code that runs when an event occurs.

(Topic-2) Types of Events
Types of Events
<events_0.png>
Time to learn about the different types of events.
onclick() - This event is fired when any HTML element is clicked.
onload() - This event is fired when the browser finishes loading the web page.
onkeydown() - This event occurs when any key on the keyboard is pressed.
onmouseout() - This event occurs when the pointer is moved out of any element.
onmouseover() - This event occurs when the pointer moves over any element.
Oh! The list is endless.
But these are some of the most commonly used events.
Let’s learn how to attach these events to our HTML elements.


(Topic-3) Attaching events to HTML elements

Attaching events to HTML elements
<events_1.png>
In the above image, stopping of music is an event.
And we are specifying what action needs to be done when the music stops.
We have to do the same thing in JavaScript.
Attaching events to the HTML element is nothing but deciding what happens when some event takes place on that element or page.

Events can be written in `two ways`.
First, writing the events inline.
Suppose, there’s a button to which we want to assign an `onclick event`.
Let’s see how we can do that.
<button onclick="alert('Oh! Clicked.')">Click me</button>

Here, we define the action that needs to be performed within the onclick attribute of button itself..
That’s it. An alert box will pop up when the button is clicked.
This type of approach is used when the action to be performed on an event, is a simple one.
Another way, is to call a function which is defined elsewhere in the program when the button is clicked.
This approach is used when the functions are complex and it also structures the HTML code and the JavaScript Code separately.
`<button onclick="clicked()">Click me</button>`
In JavaScript:
`function clicked(){
	alert('Oh! Clicked.'); 
}`

Awesome, isn’t it?
But there’s another way which allows us to attach events to the HTML elements instead of writing it directly inside the HTML element.
This is done using the `addEventListener()` function.
Using `addEventListener()`, we can attach the events to the HTML elements.

Let’s see how.
Let’s try to attach the same click event to the button.
`<button>Click Me</button>`
In JavaScript:
<-- Access the button element -->
`var myBtn = document.querySelector(“button”);`
<-- Add an event using proper method -->
`myBtn.addEventListener(‘click’,function(){
	alert(“Oh! Clicked.”);
});`

The `addEventListener()` function takes two parameters - the `type` of event and the `function`.
The function tells what to do when the event is encountered.
In the above example, the type of the function is `‘click’` and then the function contains the actions that needs to be performed.
And the `addEventListener()` is attached to the element on which the event occurs.
BooYa!
Similar to this, we can also remove the attached event.


(Topic-4) Removing events from HTML elements

Removing events from HTML elements
<events_remove.png>
To remove an event attached to any HTML element, we use the function `removeEventListener()`.
`removeEventListener()` also takes two arguments, the event to remove and the function to perform when the event is removed.
But the function is optional in this case.
Let’s remove the click event we attached to the button previously.
<-- Access the button element -->
`var myBtn = document.querySelector(“button”);`

<--Remove an event using proper method -->
`myBtn.removeEventListener(‘click’);`
That’s it. Easy as ABC.
This proves efficient when writing huge programs.
Incoming Questions Alert!!!


(Topic-5) Let’s Revise _ Events In Js

Which of the following are valid events?
Select one or more answers
`onclick`
`onmouseover`
`onmouseout`
`onkick`

What will be the output of the following snippet when the button is hovered?
<-- Access the button element -->
`var myBtn = document.querySelector(“button”);`
<-- Add an event using proper method -->
`myBtn.addEventListener(‘onmouseover’, function(){
alert(“Keep the mouse away”);
});`

Select the right answer
`An error will be encountered`
`No output`
`An alert box containing text “Keep the mouse away” will show up`
`There is no function as addEventListener`

To remove an event which function is used ?
Select the right answer
`addEventListener()`
`dontaddEventListener()`
`removeEventListener()`
`None of the above`

To summarize
An event is an occurence.
Clicking a button, hovering over an element, loading of the web page, resizing the browser window, are few examples of an event.
We can write the events `inline` or use the `addEventListener()` function to add one.
Similarly, we can use `removeEventListener()` function to remove an attached event.


(Lesson-11) Browser Object Model

(Topic-1) What is BOM?

What is BOM?
<bom.png>
BOM stands for Browser Object Model.
The grand-dad of Document Object Model. Just kidding.
The Browser Object Model enables JavaScript to interact with the browser.
The Browser object model consists of an object known as window.

Window Object
<bom_window_object.png>
The window object represents the browser window, every object is a child of the window object.
Even the document object is a child of the window object.
Other than the `document object`, the `window object` also consists of many other objects.
The `screen object` which contains the information about the user’s screen.
The `history object` which contains the browser’s history.
The `location object` which gives us access to the URL.
The `navigator object` which gives us the details about visitor’s browser.

BOM stands for
Select the right answer
`Browser Object Module`
`Browser Object Model`
`Browser Objective Model`
`None of the above`

Window object consists only of document object.
Select the right answer
`True`
`False`

(Topic-2) Exploring the window object

Window Size
<bom_window_size.png>
The `window object` stores the information about the window size of the user’s browser.
We can find out the height and width of the browser window.
To do so, we use the `innerHeight` and `innerWidth` properties of the window object.

`window.innerHeight` returns the `innerHeight` of the browser window.

`window.innerWidth` returns the `innerWidth` of the browser window.
These values are returned in pixels.
It excludes the toolbar and scroll bar while calculating. Only the browser’s view part is considered.

The screen object
The `screen object` contains the information about the user’s screen.
To access the screen object we can write:
`window.screen` or `screen`
The screen object can be written without the window, just like the document object.

We can get the height, width, color depth, pixel depth and many more things using the `screen object`.
To find out the `height` and `width` of the screen we can simply use
`screen.height` and `screen.width` respectively.
It will return the height and width of the user’s screen in pixels.
Remember, screen.height is similar to window.screen.height.

`window.innerWidth` will return _________?, `Select the right answer`
`The inner width of the screen`
`The width of the screen`
`The inner width of the browser window`
`None of the above.`

What is the correct syntax to write a screen object?
Select the right answer
`window.screen`
`screen`
`Both 1 and 2`

The History object
The history object gives us access to the history of the browser which is pretty interesting to play with.
We can navigate `back` and `forth` using the history object.
The history object provides two methods - `back()` and `forward()`.
Writing `history.back()` is same as pressing the back button of the browser.
And, on the same lines, `history.forward()` will take the navigation forward onto the next screen.

Writing `history.back()` is same as writing `window.history.back()`.
Awesome, let’s see what we got under the `location object`.

The location object
Using the location object we can get details about the URL, hostname, protocol.
Some of the properties which the location object provides are:

`window.location.href` - It returns the URL of the current page.
`window.location.hostname` - It returns the domain name of the website.
`window.location.protocol` - It returns the protocol of the website.

Awesome! A lot has been said about the window Browser object model and the window object.

The Navigator object
This object is used to detect the browser’s information such as `appName`, `appVersion` etc.
1. appName - returns the name
2. appVersion-returns the version
3. cookieEnabled-returns true if cookie is enabled else returns false
4. online - returns true if browser is online else returns false.


(Topic-3) Let’s Revise

BOM stands for
Select the right answer
`Browser Object Module`
`Browser Object Model`
`Browser Objective Model`
`None of the above`

window.screen.width will return
Select the right answer
`The width of the browser window`
`The width of the screen`
`The inner width of the browser window`
`None of the above.`

window.location.hostname returns the
Select the right answer
`URL of the current page.`
`Protocol of the web page`
`Domain name of the website`
`None of the above.`

`window.innerHeight` and `screen.height` will return the same value.
Select the right answer
`True`
`False`

To summarize
BOM stands for Browser Object Model.
The `Browser Object Model` enables JavaScript to interact with the browser.
The `window object` represents the `browser window`, every object is a child of the window object.
The `screen object` contains the information about the user’s screen.
The `history object` contains the browser’s history.
The `location object` gives us access to the url.


(Lesson-12) Cookies
(Topic-1) What are cookies?

What are cookies?
<cookies.png>
Who doesn’t love a choco-chip cookie?
Soon, you will be in love with the cookies in JavaScript too :D
Cookies in JavaScript enables us to store data in the user’s browser.
Cookie is a piece of data that is stored in the user’s browser.
But why do we need to store data in the browser?
It proves useful when we want to remember information about the user.
But, what kind of information?

Like remembering your username for a particular website, so when you visit the same website again, you don’t need to type it again.
Or storing `session variables` - This is used for maintaining a login session among different pages.

JavaScript can read, create, modify and delete cookies.
Let’s see how.

What is a cookie?
Select the right answer
`Memory in the browser.`
`Memory space in CPU allocated to store website data.`
`A piece of data that is stored in the user’s browser.`
`None of the above`


(Topic-2) Playing with cookies

Creating a cookie
A cookie can be created by using the `cookie property` of our very own document object.
To create a cookie following syntax is used:
`document.cookie = “key=value”;`
Where the key is the name of the cookie and value is the value of the cookie.

Creating Multiple cookies
We cannot create multiple cookies at once with document.cookie. To write multiple cookies
`document.cookie = “key1=value1”;`
`document.cookie = “key2=value2”;`
We need to write as many key-value pairs as required by using document.cookie repeatedly.

Cookies come with an expiry date. Yeah, they aren’t permanent.

document.cookie = “username=chrisjsm”; will ________?
Select the right answer
`Delete the cookie Chris`
`Create a cookie with key username and value chrisjsm.`
`An error will be encountered.`
`Nothing will happen`

Deleting a cookie
By default, the cookie is deleted when the browser is closed.
But we can also specify the expiry time manually.
This is done using an extra field - expires, while creating cookies.
`document.cookie = “key:value; expires:Date”`;
The expires takes Date as a value.

Read the cookies
Since we know how to create cookies, let’s see how we can read the cookies which are active.
Writing document.cookie returns the cookies which are already present.
`var myCook = document.cookie;`
The above will store a string containing all the information about cookies in the variable `myCook` which will be in the same key-value format.

Change the cookie in JavaScript
We can change the value of the cookie in the same way as we created it:
`document.cookie = "username=Edet James; expires=Thu, 18 Dec 2025 12:00:00 UTC; path=/";`
The old cookie is replaced with the new one.

We can also delete the existing cookies.
<cookies_del.png>
To do so, we need to simply write a past date in the expires field like this. `document.cookie = “key=; expires= Past_date;”;`

Where key is the name of the cookie which is to be deleted.
There is no need to specify the value while deleting a cookie.

Wasn’t that a tasty ride with cookies?
Time to burst the dream cloud.
Get ready to put your knowledge to test.


(Topic-3) Let’s Revise

Which of the following statements are true with respect to the cookie?
Select one or more answers
`Cookies enable us to store data in the user’s browser`
`Cookies are used to store session variables.`
`We can read, write, modify and delete cookies using JavaScript.`
`None of the above`

document.cookie = “name=Chris”; will
Select the right answer
`Create a cookie with key name and value Chris.`
`Delete the cookie Chris`
`An error will be encountered.`
`Nothing will happen`

To delete a cookie we assign the value of a past date to the expires field.
Select the right answer
`True`
`False`

To Summarize
Cookies in JavaScript enable us to store data in the user’s browser.
Cookie is a piece of data that is stored in the user’s browser.
Cookie is a small piece of data which consists of a name and value pair stored on the browser.
We can create a cookie using following syntax
`document.cookie = “key=value”;`
We can delete a cookie by assigning the value of a past date in the expires field.



(Lesson-13) Getting Started With Es6
(Topic-1) What Is es6?

What is es6?
<es6.png>
Boom! This was all a joke.
We have been studying ECMAScript until now.
Puff! JavaScript.
Chill! ECMAScript is nothing but the other name of JavaScript.

ES6
<es6_0.png>
ECMA is a standard organization for information and communication systems.
The standardized implementation of JavaScript came to be known as ECMAScript.
In simple terms, we can say that JavaScript is governed by ECMA standards.
The standardization continued in cycles and the 6th major release of ECMAScript also known as es6 came out in 2015.

ES6 comes with many new features.
<es6_1.png>
Some of which fairly enhance the way we do the most usual things in JavaScript.
Let’s explore few features of ES6.

(Topic-2) Exploring New Es6 Features

let and const
<es6_2.png>
Before ES6, variables were declared using `var`.
Variables declared using var are `function scoped`.
In ES6, we can declare variables using `let` and `const`.
let is same as the var, except it is `block scoped`, unlike var.

What do you mean by block scoped?
<scope_block_function.png>
A function scope is created for every function.
Whereas, block scope is created when we write conditional statements or loops.

let vs var
When we learnt about scope we saw that a variable declared inside a function using var isn’t available outside the function.
But, a variable declared inside a block scope using var is still available outside the block.
For example:

`for(var count = 0; count < 5; count++) 
{//some action }
console.log(count);`

The variable count will be available outside the block scope and its value would be logged as 5.
Here’s a twist,
we don’t really need block scope variable to exist outside the block.
This is where `let` comes in picture.
If we write,
`for( let count = 0; count < 5; count++){//some action } 
console.log(count);` // Reference Error

const is used to declare constant variables.
It works exactly like let but the value of the variable declared using const remains the same throughout the program.
Both let and const are used in the same fashion as var.
Let’s see how.

`let variable_name = value;`
`let` is the `keyword` , `variable_name` can be any valid variable name and `value` is the variable value.

`const const_name = value;`
`const` is the `keyword`, `const_name` can be any valid variable name and `value` is the constant value .

Just like that.
It is advised to avoid the use of var and use block scoped let and const.

Arrow functions
<arrow_function.png>
Remember how we write functions in JavaScript?
<-- defines a function -->
`function nameOfFunction(){
	<-- This is function body -->
}`
Right?
ES6 introduced a shorthand and an efficient way to do the same thing, which is known as `arrow function`.
The arrow function is written as
<-- Define an Arrow function using Fat arrow-->
`(parameters) => {
	<-- This is function body -->
}`

Which is same as writing like below:
<--Defines a function with Parameters -->
`function (Parameters){
	<-- This is function body -->
}`

We can also ignore the use of curly braces if the function body is confined to one statement, like so.
`(parameters) => statement;` 

Isn’t that awesome?
Further, we can assign the function to a variable, so the function reference will be stored in that variable.

`let varName = (parameters) => {
	<-- This is function body -->
};`

That’s it.
Replace all your old age function definition practices with arrow functions.

The correct syntax for an arrow function is
_____  _____ _____ ?
Tap the correct answer to fill in the blanks

`=>`, `{//body }`, `(parameters)`

Template strings
<template_str.png>
Large strings and variable concatenation?
Seriously, it’s a tedious task breaking strings using the “+” operator to concat variables.
ES6 brings the solution in the form of Template Strings.
To write template strings we use `backticks ( ` `)` instead of single or double quotes.
`let str = `Hey! String me.`;`
Simple as that.
Let’s see one more example:
<-- Declares a variable and assign an integer value -->
`let a = 5;`
<-- Declares another variable and assign a template string value -->
`let str1 = `I am ${a} years old.`;`
`str1 will be I am 5 years old.`
This is crazy! Isn’t it?
JavaScript makes you fall in love.
There are many more es6 features waiting for you to explore them.
For now, let’s put your knowledge to test.

(Topic-3) Let's Revise ES6

JavaScript and ECMAScript are different languages.
Select the right answer
`True`
`False`

Which of the following statements are correct with respect to const?
Select one or more answers
`It has a function scope.`
`It has a block scope.`
`The value of const doesn’t change throughout the program.`
`None of the above.`

<-- Declares a variable and assign an integer value -->
`let a = 10;`
<-- Declares another variable and assign a template   string value -->
`let str1 = `Do you have any problem understanding the ${a}plate strings?`;`
What will be the value of str1?
Select the right answer
`Do you have any problem understanding the ${a}plate strings?.`
`Do you have any problem understanding the ${10}plate strings?.`
`Do you have any problem understanding the 10plate strings?`
`None of the above.`

To Summarize
ECMA is a standard organization for information and communication systems.
ECMAScript is nothing but the other name of JavaScript.
The 6th major release of `ECMAScript` is known as `es6` and it came out in `2015`.
In ES6, we can declare variables using `let` and `const`.
To write template strings we use `backticks ```.


(Lesson-14) Classes In Es6
(Topic-1) What is a Class?

What is a Class?
<classes.png>
ES6 introduced classes to the JavaScript.
The newly introduced class syntax is just a syntax upgraded from the existing purely object based JavaScript.
As JavaScript didn’t have explicit classes, the same thing was achieved using the objects.
Classes in JavaScript are more or less special type of functions.
Classes are variables and methods bunched together.
Methods are nothing but the functions declared inside a class.
The members in the class can be accessed by creating the instance of the class.
These instances of the class are nothing but the objects.
When an object is created from a class it is known as an instance of the class.
Let’s see how we can write a class.

(Topic-2) Writing a Class

Writing a Class
To declare a class, the keyword class is used.
Classes can be written in two ways.
First:

    `class className{
        <-- This is class body -->
    }`

where `className` is the name of the class.
And, the second way to do this is using the class expression.
<-- Declare a class without name and store in a variable -->

    `var varName = class{
        <-- This is class body -->
    };`

The class expressions can be `named` or `unnamed`.
 <-- Declare a class with a name and store in a variable -->

    `var varName = class className{
        <-- This is class body -->  
    }`;

Constructor method is a special method in a class.
It is used for creating and initializing the objects created within its class.
There can only be one constructor method in a class.
Let’s write a class Student which takes name and roll number of the student and returns it as well.

 <-- defines a class -->
    `class Student{
        <-- defines a constructor for the class -->
        constructor(name, roll_no){
            <-- This initialises the variables -->
            this.name = name;
            this.roll_no = roll_no;
            }

        <-- defines a method of the class -->
        showName(){	
            <-- This is a method to return name -->
            return name;
        }

        <-- defines another method of the class -->
        showRoll(){
            <-- This is a method to return roll_no   -->
            return roll_no;
        }
    }`

The above class simply takes the name and roll number of the student and returns them.
Awesome, we have successfully declared our first class.
But it is just a template unless played with.
Let’s see how we can write an instance of the class and access the class methods.
Get to next topic, let's roll...


(Topic-3) Accessing members of the class

Accessing members of the class
<access_class.png>
The members of the class can be accessed by creating the instance of the class.
Objects are used to access and assign values to the variables.
It is done using the `new` keyword.
`let objName = new ClassName();`
The new keyword `instantiates` the object for use.
`ClassName()` is the name of the constructor of the class.

Let’s write an instance of the class Student.

 <-- This defines a class -->
    `class Student{
        <-- define a constructor for the class -->
        constructor(name, roll_no){
            <-- This initialises the variables -->
            this.name = name;
            this.roll_no = roll_no;
            }

        <-- define another method of the class -->
        showName(){	
            <-- This is a method to return name -->
            return name;
        }

        <-- This defines another method of the class -->
        showRoll(){
            <-- This is a method to return roll_no   -->
            return roll_no;
        }
    }`

<-- create an instance of defined class with parameters -->
`let student1 = new Student(“Edet”, 45);`

That’s it! Now we can call the function 
`showName()` and `showRoll()`.

<-- This calls 1st method using instance variable -->
    `student1.showName();`

<-- This calls 2nd method using instance variable -->
    `student1.showRoll();`
    
This will call the above methods and they will return `Edet` and `21` respectively.

Awesome, we have learnt how to write a class and access them using the instance of the class.
Let’s put this knowledge to test.


(Topic-4) Let’s Revise _ Classes In Js

What is the correct syntax to define a class?

`className class{}`
`class className {}`
`className {}`
`class {}`

Which of the following statements are correct with respect to Constructor?
`Select one or more answers`
`There can only be one constructor method in a class.`
`Constructor method is a special method in a class.`
`It is used for creating and initializing the object created with class.`
`None of the above`

`let objName = new ClassName();`
is the correct syntax to create an instance of the object?
`Select the right answer`
`True`
`False`

To Summarize
Classes in JavaScript are more or less special type of functions.
Classes are variables and methods bunched together.
Methods are nothing but the functions declared inside a class.
The members in the class can be accessed by creating the instance of the class.
Constructor is used for creating and initializing the object created with class.

Well well well!
From JavaScript to ES6, from functions to arrow functions, looks like someone came a long way :D
We have definitely reached the end of the course but JavaScript is immense in its own way and there’s always more to explore.
Keep exploring! Keep Learning! Make the web a better place.