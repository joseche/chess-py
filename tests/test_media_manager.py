from chess_py.media_manager import MediaManager


def test_media_manager_is_singleton():
    m1 = MediaManager()
    m2 = MediaManager()
    assert id(m1) == id(m2)
    m1.test_property = True
    assert m2.test_property
