# -*- coding: UTF-8 -*-

# Import from our lib
from mlproject.distance import haversine
import pytest

def test_haversine():
    assert haversine(48.865070,2.380009,48.235070,2.393409) == 70.01
