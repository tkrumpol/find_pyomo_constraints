#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 12:16:37 2022

@author: tommy

This file contains the main functions for finding all of the constraints
in a Pyomo Model given an input variable, indexed or not.
"""

import pyomo.environ as pyo
from pyomo.core.expr.visitor import identify_variables


def is_indexed_variable(component, all_constraints):
    """
    Given a Pyomo indexed variable and list of all constraints in
    and instance of the model, return a list of all constraints
    where the indexed variable occurs.

    Parameters
    ----------
    component : pyomo.core.base.var.IndexedVar
        a pyomo indexed variable

    all_constraints : list
        a list of all constraints in the pyomo model

    Returns
    -------
    con_with_desired_var_list : list
        the list of pyomo constraints where the component occurs

    """

    con_with_desired_var_list = []

    for const in all_constraints:
        vars_in_const = [
            var.parent_component().name
            for var in identify_variables(const.expr)  # noqa: E501
        ]
        vars_in_const = list(set(vars_in_const))  # remove duplicate names
        if component.name in vars_in_const:
            con_with_desired_var_list.append(const)

    return con_with_desired_var_list


def is_scalar_variable(component, all_constraints):
    """
    Given a Pyomo simple/scalar variable and list of all constraints in
    and instance of the model, return a list of all constraints
    where the simple/scalar variable occurs.

    Parameters
    ----------
    component : pyomo.core.base.var.SimpleVar
        a pyomo scalar variable

    all_constraints : list
        a list of all constraints in the pyomo model

    Returns
    -------
    con_with_desired_var_list : list
        the list of pyomo constraints where the component occurs

    """

    con_with_desired_var_list = []

    for const in all_constraints:
        vars_in_const = [var.name for var in identify_variables(const.expr)]
        vars_in_const = list(set(vars_in_const))  # remove duplicate names
        if component.name in vars_in_const:
            con_with_desired_var_list.append(const)

    return con_with_desired_var_list


def return_constraints_list(model, component):
    """
    Given a Pyomo indexed variable and list of all constraints in
    and instance of the model, return a list of all constraints
    where the indexed variable occurs.

    Parameters
    ----------
    model : pyomo.core.base.PyomoModel.ConcreteModel
        a pyomo concrete model

    component : pyomo.core.base.{var.IndexedVar, var.SimpleVar,
                                 param.SimpleParam}
        a pyomo variable, indexed variable, or parameter

    Returns
    -------
    con_with_desired_var_list : list
        the list of pyomo constraints where the component occurs

    """

    all_constraints = list(
        c for c in model.component_data_objects(pyo.Constraint, active=True)
    )

    if component.is_parameter_type():
        print("The input object is a scaler PARAMETER")
        print("No functionality to handle this yet")
        return []

    if component.is_indexed():
        print("The input object is an indexed VARIABLE")
        con_with_desired_var_list = is_indexed_variable(
            component=component, all_constraints=all_constraints
        )
    else:
        print("The input object is a scalar VARIABLE")
        con_with_desired_var_list = is_scalar_variable(
            component=component, all_constraints=all_constraints
        )

    return con_with_desired_var_list


if __name__ == "__main__":

    from src.example_model import project_test_model

    desired_component = project_test_model().x
    test = return_constraints_list(
        model=project_test_model(), component=desired_component
    )
    print(f"The desired variable occurs in {len(test)} different constraints:")
    for t in test:
        print(t.name)
