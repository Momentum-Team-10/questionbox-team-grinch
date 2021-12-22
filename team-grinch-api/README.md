# team-grinch-api

Question Box API

required dependencies:
  * django-environ
  * django-extensions
  * django REST framework
  * djoser
  * django-cors-headers


API URLS

base url:
questbox-app.herokuapp.com

questions urls:
questbox-app.herokuapp.com/api/questions
questbox-app.herokuapp.com/api/questions/<int:question_pk>

questions search url:
questbox-app.herokuapp.com/api/questions/?search=<search_input>&search_fields=<model_field>

If you want to search, you can search any of the question model's fields by interchanging
the <model_field> in the above url.
Search-able fields:
"id", "title", "body", "author", "tags"


answers urls:
questbox-app.herokuapp.com/api/questions/<int:question_pk>/answers
      (Only can 'get' and 'post')
questbox-app.herokuapp.com/api/questions/<int:question_pk>/answers/<int:pk>

