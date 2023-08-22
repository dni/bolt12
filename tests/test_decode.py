import pytest


class TestScid:
    @pytest.mark.parametrize(
        "hello",
        [
            "hello world",
        ],
    )
    def test_init(self, hello):
        assert hello == "hello world"
