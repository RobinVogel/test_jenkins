import test_jenkins
from test_jenkins.fun1 import fun1
from test_jenkins.fun2 import fun2

def test_funs():
    assert fun1() is None
    assert fun2() is None
