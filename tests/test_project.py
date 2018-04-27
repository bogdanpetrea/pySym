import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))

import z3
import pySym
import pytest

def test_basic_project():
    proj = pySym.Project(os.path.join(myPath, "scripts", "basic_function.py"))
    pg = proj.factory.path_group()
    pg.explore()
    
    assert len(pg.deadended) == 1
    assert len(pg.completed) == 1
    assert pg.completed[0].state.any_int('x') == 1

    # Make sure we're passing the project through fully
    assert pg._project is proj
    assert pg.deadended[0]._project is proj
    assert pg.deadended[0].state._project is proj
    assert pg.completed[0]._project is proj
    assert pg.completed[0].state._project is proj

