import types

from PEP import build_models, predict_symptoms


def test_build_models_returns_models():
    tree, forest, gnb, symptoms, diseases = build_models(verbose=False)
    assert tree is not None
    assert forest is not None
    assert gnb is not None
    assert isinstance(symptoms, list) and len(symptoms) > 0
    assert isinstance(diseases, list) and len(diseases) > 0


def test_predict_returns_string_any_algorithm():
    # Use first two known symptoms to form a minimal input
    _, _, _, symptoms, _ = build_models(verbose=False)
    sample = set(symptoms[:2])

    for algo in ("tree", "random", "gnb"):
        pred = predict_symptoms(sample, algorithm=algo)
        assert isinstance(pred, str) and len(pred) > 0
