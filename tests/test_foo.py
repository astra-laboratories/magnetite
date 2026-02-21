from magnetite import foo


def test_rect():
    r = foo.Rect()
    assert r.pos == [0, 0], "Default position incorrect"

    r.translate_x(by=100)
    assert r.pos[0] == 100, "X translation incorrect"

    r.translate_y(by=50)
    assert r.pos[1] == 50, "Y translation incorrect"
