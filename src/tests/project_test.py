#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 15:03:39 2022

@author: tommy

This file contains all of the tests
for the package.
"""

from src.find_pyomo_constraints import (
    return_constraints_list,
)  # noqa: E501
from src.example_model import project_test_model


def test_scalar_variable_constraints():
    """
    A test to check the output of the function for a scalar VARIABLE.
    There are 2 constraints where this variable occurs: 1,2.
    """

    model = project_test_model()
    desired_component = model.y
    test = return_constraints_list(model=model, component=desired_component)
    assert len(test) == 2


def test_indexed_variable_constraints():
    """
    A test to check the output of the function for an indexed VARIABLE.
    There are 3 constraints where this variable occurs: 1,3,4.
    """

    model = project_test_model()
    desired_component = model.x
    test = return_constraints_list(model=model, component=desired_component)
    assert len(test) == 3


def test_scalar_parameter_constraints():
    """
    A test to check the output of the function for a scalar PARAMETER.
    This functionalty does not exist yet, so just checking that the if
    statement is correctly catching and exectuing the return of an
    empty list.
    """

    model = project_test_model()
    desired_component = model.p
    test = return_constraints_list(model=model, component=desired_component)
    assert len(test) == 0
