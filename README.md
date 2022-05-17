# WEBSITE EG-EXPERT.RU
#### Final project CS50 2022
#### VIDEO DEMO: -------------------!!!!!!

#### Description:

The Web application was developed for an electric expertise company. The purpose of the project is getting client' requests and purchase orders.
The site was build with Python language, HTML5 and CSS. Was Used web framework - Flask, templating engine - Jinja and Bootstrap library.
The project was developed in Visual Studio Code at [my own repository](https://github.com/Denis-Bez/MyRepose)

**Files in the project:** 
 - "app.py": a backend part of the site. It contains Mail and flask configurations, rendering templates, spam filter, sending mail function
 - "text_library.py": the library has text for lyouts namely -  "title", "descripton" tags text, text for are selling services pages and conditions the spam filter
 - folder "templates": 36 pages, 2 layouts and the file "sitemap.xml". The Site has 4 section - "About company", "Services" with 30 product' pages, "Ours experts" and "Contacts". The contact' forms are in header and in services pages
 - folder "static": contain bootstrap files, custom CSS styles file

**Features which have been Implemented:**
- The application was started on a hosting with "https" protocol
- Was started advertise and getting first sales. Integrate with a advertise system
- Using the layouts for generate site' pages
- Feedback forms with validation
- The Spam filter with own spam base
- Information notification via "flash" Flask's function
- Sending mail notification from the site. Sending mail notification to clients
- Using own metatag library for a search engine
