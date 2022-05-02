# A read me file to explain what it is and how to use it 
This is a Python based package to help with the analysis of Pyomo
Concrete Models. If you are in the process of debugging a model,
this package may be able to help.

If you are not the individual who built the instance of the model
and are interested in finding all the constraints where a given variable
occurs, this is the package to help.

This package has one main function return_constraints_list.
This function accepts two arguments:
- The created instance of a Pyomo concrete model
- A pyomo variable (simple or indexed)
It will return a list.
- This list will contain all constraints where this variable occurs 

## Example
The full code illustrating this example can be found at the bottom of ```find_pyomo_constraints.py```

Consider a model with four constriants. Each constraint is a function of variables ```y```, ```x[1]```, or ```x[2]```:
```
Constraint1 : y + 3*x[1] + 4*x[2] >= 1
Constraint2 : y >= 2
Constraint3 : x[1] >= 0
Constraint4 : x[2] >= 0
```

If we were to run 
```
test = return_constraints_list(
                                model = project_test_model(), 
                                component = y
                                )
```
Where ```project_test_model()``` is the full model instance inside ```example_model.py```,
and we would like to know which constraints contain component ```y```
then ```test``` will contain ```Constraint1``` and ```Constraint2``` in the returned list.