#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:49:25 2022

@author: tommy

This file contains and example pyomo model that is build and used for testing.
"""

import pyomo.environ as pyo


def project_test_model():
    """
    Creates a simple Concrete Pyomo Model for testing of the functions.
    This model contains an indexed variable x, scalar variable y,
    scalar parameter p, constraints, expressions, and an objective function.

    Returns
    -------
    model : PyomoModel.ConcreteModel
        an instance of a pyomo concrete model

    """

    model = pyo.ConcreteModel()

    model.y = pyo.Var(domain=pyo.Reals)
    model.x = pyo.Var([1, 2], domain=pyo.NonNegativeReals)
    model.p = pyo.Param(initialize=2)

    model.OBJ = pyo.Objective(expr=2 * model.x[1] + 3 * model.x[2])

    # writing CONSTRAINTS with different combinations of
    # parameters, scalar vars, and indexed vars
    model.Constraint1 = pyo.Constraint(
        expr=model.y + 3 * model.x[1] + 4 * model.x[2] >= 1
    )
    model.Constraint2 = pyo.Constraint(expr=model.y >= 2)
    model.Constraint3 = pyo.Constraint(expr=model.x[1] >= 0)
    model.Constraint4 = pyo.Constraint(expr=model.p + model.x[2] >= 0)

    return model
