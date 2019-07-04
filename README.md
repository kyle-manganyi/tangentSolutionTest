# Tangent Solution Test

# How to run
###     - git clone https://github.com/kyle-manganyi/tangentSolutionTest.git
###     - cd tangentSolutionTest
###     - virtualenv myenv
###     - myenv\Scripts\activate
###     - cd tangent_solutions
###     - open http://localhost:5000 on your machine

# Endpoints
| path  | method | body  | response |
| ------------- | ------------- | ------------- | ------------- |
| /leave  | GET  | {}  | return list of all leave objects in the databse  |
| /leave  | POST  | {emp_number,start_date,end_date,days_of_leave}  | "Employee Does not exist" - employee number does not exist in DB |
|   |  |   | "dates invalid" - end date is before start date  |
|   |  |   | {"days_of_leave": ,"emp_number": ,"status": } - leave created ad details displayed  |
|/leave/<id>/<status>   |PUT|{}|  {"days_of_leave": ,"emp_number": ,"status": } - leave updated and details displayed  |
|/user   |POST  | {emp_number, phone_number,first_name,last_name}  |  "invalid employee number" - user emp ID does match format |
|   |  |   | "okay" - user created|

# Hosted web service end points

## please reffer to the about end points table for usabe of the hosted API's 
## use postman for testing

### https://kylies97.pythonanywhere.com/leave
### https://kylies97.pythonanywhere.com/leave
### https://kylies97.pythonanywhere.com/leave/id/satus###
### https://kylies97.pythonanywhere.com/user
