# SecurityDashboard
Security Dashboard For Interactive Intelligence

To access the django rest api tutorial, go to:
http://www.django-rest-framework.org/tutorial/quickstart/

##AWS Configuration
+ open pgadmin in a terminal (non aws)
  - start the aws database

+ Connection to AWS:
  - Add the NCSUWebService.pem file to your ~/.ssh folder
  - ssh -i ~/.ssh/NCSUWebService.pem ec2-user@ec2-54-90-227-211.compute-1.amazonaws.com
+ cd 2016FallTeam03
  - source env/bin/activate
  - (follow all standard procedures to run server)

  
+ RDS for Postgres
  - https://aws.amazon.com/getting-started/tutorials/create-connect-postgresql-db/
+ EC2 Instance
  - http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-get-started-overview
+Django
  - http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html


##Installing Postrges on ubuntu 16.04
http://tecadmin.net/install-postgresql-server-on-ubuntu/#
+ Starting pgAdmin4: http://askubuntu.com/questions/831262/how-to-nstall-pgadmin-4-in-desktop-mode-on-ubuntu-16-04
+ To run the server:
- cd env
- source bin/activate
- python lib/python2.7/site-packages/pgadmin4/setup.py
- python lib/python2.7/site-packages/pgadmin4/pgAdmin4.py
+ Navigate to: http://localhost:5050/browser/

## To run python server:
1. python manage.py runserver
2. Go to http://127.0.0.1:8000/users/
3. Login credentials
+ username: admin
+ password: csc492team3

## Updating webpages:

1. Content of wepages are located in jekyll-site
2. Local version of site can be loaded by running jeyll serve from the /jekyll-site folder
3. All changes should be made through git and then rin jekyll serve which will update the 'site' folder
4.
+ To add a new endpoint/directory, create a folder within jekyll-site with an index.html file.

+ Then modify the 'config.yml' file to include the title, id, and url of the new page. The title is what will be displayed on the top bar of the wepage. The id and url should be identical and will be what is shown as the url endpoint. The url endpoint is appended to the base url, unless you indicate that it should be nested under another folder. Do not use underscores in urls, use hyphens.

5. Content of each index.html is what would go in the body of the file. To view the header, footer, and sidebar look in the 'incldues' folder. 
6. The first part of each index.html is the YAML block. See any existing index.html files for example. The title and id must match the config.yml file.
7. Custom css and js files can be included in the YAML block by writing the following: 
+ custom_css:

  '- {location of css file from the root directory}'

+ custom_js:

   '- {location of js file from the root directory}'

8. all custom css and js files should be saved within the desired index.html parent folder.
9. The layouts folder can be added to, but the default layout should be used across the site. 
10. See https://jekyllrb.com/ for all information on installation, and usage. 



