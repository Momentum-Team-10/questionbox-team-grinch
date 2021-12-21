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

answers urls:
questbox-app.herokuapp.com/api/questions/<int:question_pk>/answers
      (Only can 'get' and 'post')
questbox-app.herokuapp.com/api/questions/<int:question_pk>/answers/<int:pk>