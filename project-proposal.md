# Project Proposal: Creating Scientific Research Software
## Tom Krumpolc

### Motivation
Many times when debugging models, researchers are not necessarily the person who wrote the model. 
In this situation, the investigator may want to identify instances where a variable occurs within the model, such as in the constraints. 

### Proposed Package
I propose to write a package to help investigators do just this for the modeling language Pyomo. 
Given a Pyomo model and input scalar variable name, return all constraints within the model where this variable appears. 
If this works well, then extend this to take indexed variables.  
Future extensions include accepting parameters as arguments and searching expressions, and the objective function. 

### Plan for writing package
Such questions have been posed on stack overflow [here](https://stackoverflow.com/questions/48538945/access-all-variables-occurring-in-a-pyomo-constraint) 
but in this post require knowing the name of the constraint. In some cases, it is not obvious the name of the constraint(s) where the variable may occur. 
Pyomo has a functionality called ```identify_variables```. The preliminary package will involve loops to check all the constraints. 

### Summary of Final Deliverables

-   [x] Writing initial functionality to handle scalar/simple variable search: 3 hours
-   [x] Extending to indexed variables: 1 hour
-   [x] Tests: 2 hours 
-   [x] Documentation (readme.md, project-proposal.md): 1 hour
-   [x] Clean up code to pylint/flake8/black: 1 hours
-   [x] Debugging: 4 hours   

Total time ~8-12 hours