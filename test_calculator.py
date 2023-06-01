from main import calculate_efficiency


def test_calculate_efficiency(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    assert calculate_efficiency(315, 4.5) == 7.0


def test_calculate_efficiency_export(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    assert calculate_efficiency(315, 4.5) == 7.0
