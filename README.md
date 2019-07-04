# tangentSolutionTest

# how to run
###     - git clone https://github.com/kyle-manganyi/tangentSolutionTest.git
###     - cd tangentSolutionTest
###     - virtualenv myenv
###     - myenv\Scripts\activate
###     - cd tangent_solutions
###     - open http://localhost:5000 on your machine

# endpoints
| path  | method | body  | response |
| ------------- | ------------- | ------------- | ------------- |
| /leave  | GET  | {}  | return list of all leave objects in the databse  |
| /leave  | POST  | {emp_number,start_date,end_date,days_of_leave}  | "Employee Does not exist" - employee number does not exist in DB |
|   |  |   | "dates invalid" - end date is before start date  |
