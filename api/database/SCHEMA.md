# schema
## users
- id > integer
- created > text (datetime object)
- username > text
- name > text
- email > text
- asked > integer
- answered > integer
## tackboards
- id > integer
- name > text
- subject > text
- description > text
- public > integer (0 for false, 1 for true)
- owner id > integer
- created > text (datetime object)
- member ids > text (python list serialized into json; has all if public, empty if nobody is member)
- question ids > text (python list serialized into json)
- answers ids > text (python list serialized into json)
### questions
- id > integer
- author id > text
- upvotes > integer
- downvotes > integer
- answered member ids > text (python list serialized into json; has all if public, empty if nobody is member)
- created > text (datetime object)
- question > text
### answers
- id > integer
- question id > integer
- author id > integer
- upvotes > integer
- downvotes > integer
- created > text (datetime object)
- answer > text