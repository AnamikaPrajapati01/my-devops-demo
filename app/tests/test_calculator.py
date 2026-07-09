import pytest
from app.calculator import apply_discount

def test_apply_discount_normal_case():
    assert apply_discount(100, 10) == 90.00

def test_apply_discount_zero_discount():
    assert apply_discount(50, 0) == 50.00

def test_apply_discount_max_discount():
    assert apply_discount(200, 80) == 40.00

def test_amount_must_be_positive():
    with pytest.raises(ValueError):
        apply_discount(0, 10)

def test_discount_range_low():
    with pytest.raises(ValueError):
        apply_discount(100, -1)

def test_discount_range_high():
    with pytest.raises(ValueError):
        apply_discount(100, 81)
