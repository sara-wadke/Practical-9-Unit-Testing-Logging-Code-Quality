
import pytest
from order import (
    calculate_discount,
    calculate_gst,
    calculate_order_total,
)


def test_calculate_discount():
    assert calculate_discount(1000, 10) == 100


def test_zero_discount():
    assert calculate_discount(1000, 0) == 0


def test_calculate_gst():
    assert calculate_gst(1000, 18) == 180


def test_calculate_order_total():
    assert calculate_order_total(1000, 10) == 1062


def test_negative_price():
    with pytest.raises(ValueError):
        calculate_discount(-100, 10)


def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_discount(1000, 110)
