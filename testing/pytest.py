from calci import add, name, sub
def test_add():
    assert add(2,3)==5
def test_sub():
    assert sub(3,2)!=0
def test_name():
    assert name("monish")=="monishgowda"