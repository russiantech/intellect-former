Django Full Course
1. Introduction To Django
    a. Basics Of Django:
        <kevin.png>
        Hi! My name is Dunis, and I am a Web developer by profession.
        Though the job isn’t easy, It is better now than it was a few years back.
        All dynamic websites perform various functions.
        For a regular user, the look and feel of the website matters more.
        While, for more sophisticated users, even the back-end matters.

        <frontend.png>
        For front-end, we have technologies like HTML, CSS, and JavaScript.
        But, what about the backend?
        Languages like PHP, Java, Python, and more help in developing Backend.
        
        <python_django.png>
        Django helps in building the backend using Python.
        Django is a high-level Python web framework.
        It helps to maintain rapid development and clean, pragmatic design.
        Django makes it easier to build better web apps quickly and with less coding effort.
        Django grew from a very practical need.

        In fall 2003, the World Online developers ditched PHP and began using Python to develop its websites.
        As they built intensive, richly interactive sites such as Lawrence.com, they began to extract a generic Web development framework that let them build Web applications more and more quickly.
        They tweaked this framework constantly, adding improvements over two years.
        In summer 2005, World Online decided to open-source the resulting software, Django.

        <python_django.png>
        Django comes with the following design philosophies:
        > Loosely Coupled − Django aims to make each element of its stack independent of the others.
        > Less Coding − Less code means a quick development.
        > Don't Repeat Yourself (DRY) − Everything should be developed only in exactly one place.
        > Clean Design − Django strictly maintains a clean design throughout its code and makes it easy to follow the best web-development practices.

        Advantages of Django
        Here are few advantages of using Django which can be listed out here:
        > Object-Relational Mapping (ORM) Support − Django provides a bridge between the data model and the database engine and supports a large set of database systems, including MySQL, Oracle, Postgres, etc.
        > Multilingual Support − Django supports multilingual websites through its built-in internationalization system. So you can develop your website, which would support multiple languages.
        > Framework Support − Django has built-in support for Ajax, RSS, Caching, and various other frameworks.
        > Administration GUI − Django provides a nice ready-to-use user interface for administrative activities.
        > Development Environment − Django comes with a lightweight webserver to facilitate end-to-end application development and testing.


    b. Installation of Django
        <python_django.png>
        Django development environment consists of:
        > Installing & setting up Python
        > Installing & setting up Django
        > And a Database System.

        Step 1. Installing Python
        <download.png>
        Django is written in 100% pure Python code.
        Hence, we need to install Python on your system.
        Latest Django version requires Python 2.6.5 or higher.
        You can download and install the latest version of Python from http://www.python.org/download.

        Step 2 .Installing Django
        You can download the latest version of Django from http://www.djangoproject.com/download
        Extract and install Django:
        `c:\>cd c:\Django-x.xx`
        Next, install Django by running the command for which you will need admin privileges in windows shell "cmd":
        `c:\Django-x.xx>python setup.py install`
        To test your installation, open a command prompt and type the following command:
        `c:\>python -c "import django; print(django.get_version())"`
        If you see the version of Django printed on screen, then everything is ready.

        Step 3. Database Setup
        <db.png>
        Django supports many database engines and we can set up any of them based on your comfort.
        `MySQL`
        `PostgreSQL`
        `SQLite 3`
        `Oracle`
        `MongoDb`
        `GoogleAppEngineDatastore`

        Step 4. Web Server
        Django comes with a lightweight web server.
        Major purpose of this is for developing and testing applications.
        This server is pre-configured to work with Django, and more importantly, it restarts whenever you modify the code.
        However, Django does support Apache and other popular web servers such as Lighttpd.
        We have a detailed discussion up ahead in the coming chapters.


    c. Let's Revise
        Choose the wrong answer out
        Django development environment consists of:
        `Select the right answer`
        `Python`
        `Django`
        `Java`
        `MySQL`
        
        Django does not apply Don't Repeat Yourself policy.
        Select the right answer
        `True`
        `False`
        
        Fill in the blank:
        _____ makes it easier to build better web apps quickly and with less coding effort.
        Tap the correct answer to fill in the blanks
        `Python` | `Java` | `MySQL` | `Django`

        Django is a high-level Python web framework.
        Select the right answer
        `True`
        `False`
        
        Which of the following is/are true about Django.
        Select one or more answers
        `Django aims to make each element of its stack independent of the others.`
        `Django means Less code which means a quick development.`
        `Django supports multilingual websites`
        `Django provides a nice ready-to-use user interface for administrative activities.`


2. Django Project MVT Structure
    a. Introduction to MVT Structure
        <mvt.png>
        Django is based on MVT (Model-View-Template) architecture.
        MVT is a software design pattern for developing a web application.
        MVT Structure has the following three parts:
        > Model
        > View
        > Template

        Model
        <model.png>
        The model acts as the interface of your data.
        It is responsible for maintaining data.
        It can be imagined as the logical data structure behind the complete application.
        It is represented by a database (generally relational databases such as MySql, Postgres).

        View
        <views.png>
        The View is the user interface.
        What you see in your browser when you render a website is because of View.
        It is represented by HTML/CSS/Javascript and Jinja files.

        Template
        <template.png>
        A template consists of static parts of the desired HTML output.
        It also contains special syntax describing how dynamic content will be inserted.
        It will be more clear from the next example.

        <mvt_0.png>
        A user requests for resources from Django.
        Django works as a controller and checks the available resource in the URL.
        If URL maps, a view is called that interacts with the model and template.
        It renders a template.
        Django then responds back to the user and sends a template as a response.
        In the next topic, We will learn how to create a basic project in Django.


    b. Create a Basic Project using MVT
        <mvt_1.png>
        You might have gotten a hold on how the MVT structure in Django works.
        In this coming unit, we will learn how to create a project.
        Creating a basic project to render a template using MVT architecture.
        We will use MVT (Models, Views, Templates) to render data to a local server.

        Create a basic Project
        • To initiate a project of Django on Your PC, open Terminal & Enter the following command
        `django-admin startproject <projectname>`

        • A New Folder with the name <projectname> will be created. Let's say the project name be Dunistech_Django.

        • To enter in the project using terminal enter command
        cd <projectName>

        <httpresponse.png>
        Create a new file `views.py` inside the project folder where `settings.py`, `urls.py`, and other files are stored.
        Save the above-given code in it.

        <urls.py.png>
        Open urls.py inside the project folder (<projectName>) and add your entry as below:
        Import hello_kevin function from views.py file:
        from projectName.views import hello_kevin

        Add an entry in url field inside url patterns:
        path('ph/', hello_kevin)

        Now to run the server follow these steps:
        • Open cmd and change directory to `env_site` by following command:
        `$ cd env_site`

        • Go to Script directory inside `env_site` and activate virtual environment
        `$ cd Script`
        `$ activate`

        • Return to the `env_site` directory and goto the project directory
        $ cd .. 
        $ cd <projectName>

        • Start the server: 
        Start the server by typing the following command in cmd:
        `$ python manage.py runserver`

        <kevin_0.png>
        Bingo!! You are done with creating and rendering a basic Project.


    c. Let's Revise

        Fill in the blank to import hello_kevin function from views.py file.
        from _____________ import hello_kevin
        Select the right answer
        `projectName.views`
        `views.py`
        
        Fill in the blank:
        The _____ acts as the interface of your data. 
        Tap the correct answer to fill in the blanks
        `Template` | `View` | `Model`

        The ___________ is the user interface.
        Select the right answer
        `Model`
        `Template`
        `View`
        
        Django is based on MVT (Model-View-Template) architecture.
        Select the right answer
        `True`
        `False`


3. Creating With Django
   a. Creating Apps with Django

        <django.png>
        Django is famous for its unique and fully managed app structure.
        As we know, Django supports loosely coupled modules,
        For every task, an app can be created like a completely independent module.
        In this section, we will learn how to create a basic app.
        For example, if you are creating a Blog, Separate modules should be created for Comments, Posts, Login/Logout, etc.
        In Django, these modules are known as apps.
        There is a different app for each task.

        Pre-installed apps
        <django_default_apps.png>
        Django provides some pre-installed apps for users.
        To see pre-installed apps, navigate to:
        `projectName -> projectName -> settings.py`
        In your settings.py file, you will find `INSTALLED_APPS`.
        Apps listed in INSTALLED_APPS are provided by Django for developers comfort.

        Let us start building an app.
        <django_create_app_command.png>
        To create a basic app in your Django project, you need to go to the directory containing manage.py
        And from there enter the above command.

        <django_default_apps_add.png>
        To consider the app in your project you need to specify your project name in the INSTALLED_APPS list in settings.py.
        The above code will help you do so.
        We have finally created an app.

        In order to render the app using URLs, we need to include the app in our main project.
        Let's see below.

        <django_url_patterns.png>
        Move to projectName -> projectName -> urls.py
        Add the below code in the header:
        `from django.urls import include`

        Now in the list of URL patterns, you need to specify the app name for including your app URLs.
        The above-given is the code for that.

        Bingo! Your app is now ready.
        You can use the default MVT model to create URLs, models, views, etc. in your app.
        They will be automatically included in your main project.
        The main feature of Django Apps is independence.

   b. Django Forms
        <django_forms.png>
        To understand what is form, you’ll have to imagine the Gmail create account page.
        We fill our details in various blocks like First Name, address, etc.
        These forms can be created using Django Modules too.
        Let's get started.!

        <django_forms.png>
        When one creates a Form class, the most important part is defining the fields of the form.
        Each field has custom validation logic.
        Forms are basically used for taking input from the user in some manner.
        We use that information for logical operations on databases.
        For example, Registering a user by taking input as his name, email, password, etc.

        <django_forms_0.png>
        Django maps the fields defined in forms to HTML input fields.
        Django handles three distinct parts of the work involved in forms:
        > Preparing and restructuring data to make it ready for rendering.
        > Creating HTML forms.
        > Receiving and processing submitted forms and data.
        Above given is the syntax to add field names in the Forms.

        Prerequisite
        To use Django Forms, one needs to have a project and an app working in it.
        After you start an app you can create a form in app/forms.py.
        Creating a project and running an App has been discussed previously in detail.
        We assume that you know how to create them.

        Creating a Django Form
        <django_forms_1.png>
        Creating a form in Django is similar to creating a model.
        One needs to specify what fields would exist in the form and of what type.
        For example, In a registration form one might need a First Name (CharField), Roll Number (IntegerField) and so on.

        <django_forms_2.png>
        Enter this above code in ph/forms.py.

        Render Django Forms
        Django form fields have several built-in methods that spare the load of the developer.
        Sometimes one needs to implement things manually for customizing User Interface(UI).
        A form comes with 3 in-built methods that can be used to render Django form fields:
        > {{ form.as_table }} will render them as table cells wrapped in <tr> tags
        > {{ form.as_p }} will render them wrapped in <p> tags
        > {{ form.as_ul }} will render them wrapped in <li> tags

        <django_forms_render.png>
        To render the form we made into a view, move to views.py and create a home_view as above.

        <django_forms_render_0.png>
        Model(form) is made, View of the form is also set.
        Next is the template.
        Let’s edit templates > `home.html`
        Write the above code there.

        <django_forms_render_1.png>
        Now, visit http://localhost:8000/
        Bingo! You just created your first form!!
        Wasn’t this so simple because of less code!!
        Thanks to Django!

   c. Let's Revise
        1.
        MAtch the following:
        Click to match the appropriate answers
        {{ form.as_table }}     |   Will render them wrapped in <li> tags
        {{ form.as_p }}         |   Will render them wrapped in <p> tags
        {{ form.as_ul }}        |   Will render them as table cells wrapped in <tr> tags
        
       2.
       Each field has custom validation logic.
        Select the right answer
        `True`
        `False`

        3.
        Fill in the blank:
        The _____ is used  to create URLs, models, views, etc. in your app.
        Tap the correct answer to fill in the blanks
        `MVT` | `model` | `Java` | `Django`

        4.
        Django supports loosely coupled modules
        Select the right answer
        `True`
        `False`


4. Django CMS
    a. Introduction to CMS

        <cms.png>
        Suppose you want to edit and modify your website.
        Suppose you want to edit and modify your website.
        He wants to edit the content and then publish it.
        Now Django CMS comes in the picture.
        You know about Django .
        But what is Django CMS?!

        <cms.png>
        A CMS is a Content Management System.
        This system lets its user add, modify and delete the content as per the user’s will.
        The content we are talking about is digital content.
        It includes text, images.

        The CMS provides an interface that can be easily used by clients to maintain their websites.
        The client need not be familiar with backend technologies.
        A CMS, in short, provides the client-user an interface to easily add, modify and remove the content.
        Also, it provides the tools to publish the content.

        <django_cms_users.png>
        Django CMS is trusted by many popular organizations.
        You will be surprised but it is used by:
        > NASA
        > National Geographic
        > Loreal Paris men
        > Canonical
        > etc

        Choose the right option
        What does CMS stand for?
        Select the right answer
        `Content Manager Signal`
        `Class Management System`
        `Content Management System`
        `Clone Marking System`

    b. 5 steps to Django CMS
        <venv.png>
        Step 1: Create a virtual environment
        Before you start installing the Django CMS,
        you need to create and activate your virtual environment.
        `python -m venv env` or using `virtualenv`:
        `virtualenv env`
        And activate the virtual environment:
        `source env/bin/activate`

        Step 2: Update pip
        Pip is the Python installer we use in this Django CMS tutorial.
        Make sure your pip is up to date, since earlier versions can be unreliable.
        `pip install --upgrade pip`

        Step 3: Use the django CMS installer
        Using the Django CMS tutorial, you can create a complete and fully featured Django CMS project saved locally.
        `pip install djangocms-installer`

        In the next step, you create a new project directory and add cd into it:
        `mkdir tutorial-project`
        `cd tutorial-project`

        Run the Django CMS installer to create a new Django project called mysite:
        `djangocms -f -p . mysite`

        Start the development server
        `python manage.py runserver`

        Step 4: Create your first page
        <new_page_create.png>
        > Once you login you can press Create on the top right.
        > Then you will see a pop-up window where the “New page” is marked blue.
        > Press New Page and select Next.

        After selecting Next, you will add in your title and some basic text content for the new page, click Create.

        Step 5: Publish your page
        <new_page_create_0.png>
        The page we just created is just a draft, It needs to be published once you finish.
        As an editor, only you can see and edit your drafts, other visitors to your site will only see your published pages.
        And there you have your CMS page published!


    c. Advantages

        Fast
        <django_advantage.png>
        This has been designed in a way to help the developers make an application as fast as possible.
        From idea, production to release, Django helps in making it both cost-effective and efficient.
        Thus it becomes an ideal solution for developers having a primary focus on deadlines.

        Fully Loaded
        <loader.png>
        It works in a way that includes dozens of extras to help with user Authentication, site maps, content administration, RSS feeds, and much more such things.
        These aspects help in carrying out the web development process completely.

        Secure
        <padlock.png>
        When you are doing it in Django, it is ensured that developers don’t commit any mistakes related to security.
        Some of the common mistakes include SQL injection, cross-site request forgery, clickjacking, and cross-site scripting.
        To effectively manage usernames and passwords, the user authentication system is the key.

        Scalable
        To meet the heaviest traffic demand, the benefits of the Django framework can be seen.
        Therefore, the busiest sites use this medium to quickly meet the traffic demands.

        Versatile
        Content management, scientific computing platforms, and even big organizations, all these aspects are very efficiently managed by the use of Django.

        Django helps in making it both cost-effective and efficient.
        Select the right answer
        `True`
        `False`

        Fill in the blank:
        The _____ is the key to effectively manage usernames and passwords.
        Tap the correct answer to fill in the blanks
        a. `SQL Injection` 
        b. user authentication 
        c. system XSS


    d. Let's Revise _ CMS

        What does CMS stand for?
        Select the right answer
        `Content Manager Signal`
        `Class Management System`
        `Content Management System`
        `Clone Marking System`
        
        Which of the following is correct about Django?
        Select one or more answers
       ` Content management, scientific computing platforms are very efficiently managed by the use of Django.`
        `Scalable = Django`
        `Django helps in making it both cost-effective and efficient.`
        `Django is a slow development language`
        
        ________ provides an interface that can be easily used by clients to maintain their websites.
        Select the right answer
        `SQL Injection`
        `User authentication system`
        `XSS`
        `CMS`


5. Creating Views & URL Mapping
    a. Creating Views

        <mvt_2.png>
        In the previous chapters, we came across a term called View.
        View is nothing but the look n feel of a website or a web app.
        Whenever you open the intellect app, the UI that you get for interaction is all due to the view function.
        This chapter deals with the detailed study of the View function.

        A view function, or “view” for short, is simply a Python function.
        It takes a web request and returns a web response.
        This response can be anything,
        The HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image, etc.
        But we need to associate this page to a URL to view it as a web page.
        Url mapping is discussed later in this Chapter.
        In Django, views have to be created in the app views.py file.
        This we have seen in the previous chapters.

        Simple View
        <views_0.png>
        We will create a simple view in myapp to say "welcome to my app!"
        In this view, we use HttpResponse to render the HTML.
        To see this view as a webpage we just need to map it to a URL.

        <views_0.png>
        Views can also accept parameters.
        When linked to a URL, the webpage will display the passed value as a parameter.
        Note that the parameters will be passed via the URL.
        In the above code “welcome to my app” is passed through a parameter text.

        Fill in the blank:
        A _____ takes a web request and returns a web response.
        Tap the correct answer to fill in the blanks
        `Template Function`, |` Model function`, |`view function`

        We need to associate the page to a URL to view it as a web page.
        Select the right answer
        `True`
        `False`

    b. URL Mapping

        <urlpatterns.png>
        Now that you are familiar with the view, we can move to URL Mapping.
        To access any view we need a URL.
        Django has its own way of URL mapping.
        It's done by editing your project url.py file (myproject/url.py).
        The url.py file looks like the above image.
        Don’t worry it’s not that complicated as it seems.

        <urlpatterns_0.png>
        When a user makes a request to a web page,
        Django controller takes over to look for the corresponding view via the url.py file.
        It will return the HTML response or a 404 not found error, if not found.
        In url.py, the most important thing is the "urlpatterns" tuple.
        It’s where we define the mapping between URLs and views.

        <urlpatterns_0.png>
        The above code maps the URL "/home" to the `hello` view created in myapp/view.py file.
        As you can see above a mapping is composed of three elements:
        1. The pattern:
            A regular expression matching the URL you want to be resolved and map.
            Everything that can work with the python re module is eligible for the pattern.
            It is useful when you want to pass parameters via URL.

        2. The python path to the view:
            It is the same as when you are importing a module.

        3. The name:
            To URL reversing, you’ll need to use named URL patterns as done in the examples above.

        Once done, just start the server to access your view via:http://127.0.0.1/hello

        How is URL Mapping done?
        We need to create a url.py file in my app using the following code:

        `from django.conf.urls import patterns, include, url `
        
        `urlpatterns = patterns('', url(r'^hello/', 'myapp.views.hello', name = 'hello'),)`

        <urlpatterns_0.png>
        Then myproject/url.py file will undergo changes as the above code.
        We have included all URLs from myapp application.
        The home.html that was being accessed through “/hello”,
        Can now be accessed by “/myapp/hello”

        <urlpatterns_1.png>
        Now let's imagine we have another view in myapp “morning”.
        We want to map it in myapp/url.py.
        We have to change our myapp/url.py.
        Rewrite the above code in the myapp/url.py.

        That's all from URL Mapping, just minor changes in the url.py file result in major improvements.

    c. Let’s Revise
        1.
        Match the following:
        Click to match the appropriate answers
        `The pattern`                     | `It is the same as when you are importing a module.`
        The python path to the view       | `A regular expression matching the URL you want to be resolved and map.`
        The name                          | `To URL reversing, you’ll need to use named URL patterns.`
        
        2.
        "urlpatterns" tuple is where we define the mapping between URLs and views.
        Select the right answer
        `True`
        `False`

        We need to associate the page to a URL to view it as a web page.
        Select the right answer
        `True`
        `False`


6. Working With Files
    a. Working with files
        <uploader.png>
        It is better if we have the freedom to upload images, pdf and other files in our Web app.
        Django has a provision for the same.
        This chapter deals with the same.
        Let's explore how you can add images and other files.

        Uploading an Image
        <uploader_django_forms.png>
        Before starting to learn how to add image, make sure you have the Python Image Library (PIL) installed.
        Now let's take an example and create a profile form, in our myapp/forms.py.
        The code is given above.
        The major change that we see here is a new field:
        `forms.ImageField`
        `ImageField` will make sure the uploaded file is an image.

        <django_models.png>
        Now let's create a model.
        Create a "Profile" model to save our uploaded profile.
        This is done in myapp/models.py.
        The ImageField takes a compulsory argument: upload_to.
        This represents the place on the hard drive where your images will be saved.
        (Note that the parameter will be added to the `MEDIA_ROOT` option defined in your settings.py file.)

        <django_profile_func.png>
        We have the Form and the Model.
        Let's create the view in myapp/views.py.
        There is a change when creating a ProfileForm, we have added a second parameter: request.FILES.
        If not passed the form validation will fail, giving a message that says the picture is empty.

        In the next steps, we will create two templates:
            > saved.html template and
            > the profile.html template
        Next, we pair URLs to these templates.
        Voila! You have your own Web application that accepts Image File.
        Now if you want to save some other file type, just replace the ImageField in both Model and Form with FileField.

        `forms.ImageField` will make sure the uploaded file is an image.
        Select the right answer
        `True`
        `False`

        If you want to save some other file type, just replace the ImageField in both Model and Form with:
        Select the right answer
        `FileField`
        `PDFFeild`
        `MP4Feild`
        `None`


    b. Setting up Apache
        <apache.png>
        So far, in our examples, we have used the Django dev web server.
        But this server is just for testing.
        It is not fit for the production environment.
        Once in production, you need a real server like Apache, Nginx, etc.
        We shall discuss Apache in this chapter.

        <django_project_structure.png>
        Serving Django applications via Apache is done by using mod_wsgi.

        So the first thing is to make sure you have Apache and mod_wsgi installed.
        The wsgi.py file is responsible for the link between Django and Apache.

        <django_project_structure_0.png>
        Let's say we want to share our project with Apache.
        We just need to set Apache to access our folder.
        Assume we put our myproject folder in the default location.
        Accessing the project will be done via 127.0.0.1/myproject.
        This will result in Apache just listing the folder as shown in the above snapshot.

        <httpd.conf.png>
        Apache is not handling Django stuff.
        For this, we need to configure Apache in `httpd.conf`.
        So open the httpd.conf and add the above code lines.

        <form_page.png>
        Now if we try to access the page,
        We can see the above given page.

    c. Let's Revise

        If you want to save some other file type, just replace the ImageField in both Model and Form with:
        Select the right answer
        `FileField`
        `PDF Field`
        `MP4Feild`
        `None`

        The wsgi.py file is responsible of the link between Django and Apache.
        Select the right answer
        `True`
        `False`

        <!-- Select the right answer
        True
        False -->


7. Security With Django
    a. Security Features

        Django solves many security issues for a web application.
        The architecture and structure protects both the client and the server from any malware.
        In this last chapter, we shall explore how Django helps in providing security against various threats.
        Let's get started.

        What is XSS?
        <attacks.png>
        It protects the client or user from XSS attack.
        Cross-site Scripting (XSS) is a client-side code injection attack.
        The attacker aims to execute malicious scripts in a web browser of the victim by including malicious code in a legitimate web page or web application.

        Using Django templates protects you against the majority of XSS attacks.
        However, it is important to understand what protections it provides and its limitations.

        Django templates escape specific characters that are particularly dangerous to HTML.
        While this protects users from most malicious input, it is not entirely foolproof.

        If you are using the template system to output something other than HTML, there may be entirely separate characters and words that require escaping.

        Cross-Site Request Forgery
        <attacks_0.png>
        Protecting the visitor or client from CSRF attack.
        An attack that persuades end-users to execute unwanted actions(like clicking on any event) on the website in which they are the authorized user.

        Django has built-in protection against most types of CSRF attacks.
        You should have enabled and used it where appropriate.
        However, as with any relief technique, there are limitations.
        For example, it is possible to disable the CSRF module globally or for particular views.
        You should only do this if you know what you are doing.
        There are other limitations if your site has subdomains that are outside of your control.

        SQL injection
        <sql_injection.png>
        It protects from SQL injection, an attack that results in data leakage or deleted data.
        SQL Injection (SQLi) is a type of an injection attack that makes it possible to execute malicious SQL statements.
        These statements control a database server behind a web application.
        Attackers can use SQL Injection vulnerabilities to bypass application security measures.

        Django’s querysets are protected from SQL injection.
        Reason being their queries are constructed using query parameterization.

        A query’s SQL code is defined separately from the query’s parameters.
        Since parameters may be user-provided and therefore unsafe.

        Django also gives developers the power to write raw queries or execute custom sql.
        You should always be careful to properly escape any parameters that the user can control.

        In addition, you should exercise caution when using extra() and RawSQL.


        Clickjacking Protection
        Clickjacking is a type of attack where a malicious site wraps another site in a frame.
        This attack can result in an unsuspecting user being tricked into performing unintended actions.

        Django contains clickjacking protection in the form of the X-Frame-Options middleware.
        This when used in a supporting browser can prevent a site from being rendered inside a frame.
        It is possible to disable the protection on a per-view basis or to configure the exact header value sent.

        These are the basic types of security threats and how Django deals with it.
        In the next chapter we have some tips for the developer to ensure security of the product.

    b. Tips for a more secure Web App

        Security becomes a huge issue when we are dealing with Web Apps.
        Django provides security yet it's not an assurance.
        Hence it becomes important that you should safeguard and follow some steps.
        Let's discuss some basic security steps in this chapter.

        <python_code_safe.png>
        Make sure that your Python code is outside of the Web server’s root.
        This will ensure that your Python code is not accidentally served as plain text (or accidentally executed).

        <python_code_safe.png>
        Take care with any user uploaded files.
        Django does not throttle requests to authenticate users.
        To protect against brute-force attacks against the authentication system, you should consider deploying a Django plugin or Web server module to throttle these requests.

        <password.png>
        Keep your SECRET_KEY a secret.
        Don't be like the person in the image.

    c. Let's Revise

        Fill in the blank:_____is a client-side code injection attack.
        Tap the correct answer to fill in the blanks
        `SQL Injection` | `Cross-site Scripting(XSS) |`Clickjacking`

        Clickjacking is a type of attack where a malicious site wraps another site in a frame.
        Select the right answer
        `True`
        `False`

        SECRET_KEY should not be a secret.
        Select the right answer
        `True`
        `False`

        Django does not throttle requests to authenticate users.
        Select the right answer
        `True`
        `False`


8. Miscellaneous Concepts
    a. Cookie Handling
        <cookies_concept.png>
        Sometimes you might have to store some data on a per-site-visitor basis as per the requirements of your web application.
        Always keep in mind that cookies are saved on the client-side.
        Depending on your client browser security level, setting cookies can at times work and at times might not.
        In this chapter, we shall learn about cookies and how to handle them.

        <cookies_client_side.png>
        A cookie is a small piece of information that is stored in the client browser.
        It is used to store the user's data in a file permanently.
        Cookie has its expiry date and time and removes automatically when it expires.
        Django provides built-in methods to set and fetch cookies.
        We shall learn about them one by one.

        The setcookie() method is used to set a cookie.
        The getcookies() method is used to get the cookie.
        The request.COOKIES['key'] array can also be used to get cookie values.
        Now I will teach you with an example of how you can implement cookies while making your own Web App.
        
        <django_setcookie.png>
        In views.py, two functions setcookie() and getcookie() are used to set and get cookie respectively.
        Let's edit and make the above changes in views.py file.

        <urlpatterns_2.png>
        Now edit URLs specified to access these functions.
        Let's edit and make the above changes in urls.py.
        Now we will start the server.

        <cookies_set.png>
        After starting the server, set cookies by using `localhost:8000/scookie` URL.
        It shows the above output to the browser.
        
        <<django_setcookie_0.png>
        And get a cookie by using localhost:8000/gcookie URL.

        The ________ method is used to set a cookie.
        Select the right answer
        `setcookie()`
        `getcookie()`

        The _______________ method is used to get the cookie.
        Select the right answer
        `setcookie()`
        `getcookie()`


    b. Sessions paradigm
        <session_time.png>
        A session is a mechanism to store information on the server-side during the interaction with the web application.
        In Django, by default session stores in the database.
        It also allows file-based and cache-based sessions.
        In this chapter we shall discuss sessions.

        `__getitem__(key)` is used to get session value.
        __setitem__(key, value) is used to set session value.
        `__delitem__(key)` is used to delete session objects.
        `__contains__(key)` checks whether the container contains the particular session object or not.

        `get(key, default=None)` is used to get session value of the specified key.

        Now with the help of an example Let's understand the concept of sessions.

        <django_session.png>
        The first function is used to set and the second is used to get session values.
        Let us edit the views.py file according to the above code.
        It is clear that sname and semail are being stored here.

        <urlpatterns_3.png>
        Now we need Url mapping to call both the functions.
        Let us edit the url.py file according to the above code.
        And then Run the server.

        <session_set.png>
        set the session by using `localhost:8000/ssession`

        <session_get.png>
        The session has been set, to check it, use `localhost:8000/gsession`

        Match the following
        Click to match the appropriate answers
        __getitem__(key)                |   is used to get session value
        __setitem__(key, value)         |   is used to delete session objects
        __delitem__(key)                |   is used to set session value
        __contains__(key)               |   -checks whether the container contains the particular session object or not

    c. Concept of Caching
        <cookies_concept.png>
        Caching is done when we need to access the same file again and again.
        Basically, to cache something is to save the result of a calculation, so that you don’t have to perform it the next time you need it.
        In this unit, we shall learn in detail about caching.

        <cache_essennce.png>
        The above-given Pseudo code explains how caching works.
        Django comes with its own caching system.
        It lets you save your dynamic pages, to avoid calculating them again when needed.
        In Django Cache framework you can cach:
        > The output of a specific view.
        > A part of a template.
        > Your entire site.

        Setting Up Cache in Database
        To use cache in Django, the first thing to do is to set up where the cache will remain.
        Setting is done in the settings.py file of your project.
        Setting Up Cache in File System
        Just make the above changes and set the location of the File system.
        Setting Up Cache in Memory
        This is the most efficient way of caching.
        That's all from the basic caching that you’ll require in building a Web App.
        Up next we have security & how Django helps in maintaining it.


    d. Let's Revise