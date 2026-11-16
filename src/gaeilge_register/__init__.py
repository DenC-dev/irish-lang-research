"""Transparent, rule-based register and variation features for Irish text.

Every function returns *candidates* for a human to inspect. Nothing here is an
error detector, a proficiency measure, or a speaker classifier.
"""
from .features import (  # noqa: F401
    FeatureReport,
    analyse,
    eclipsis_candidates,
    lenition_candidates,
    strip_fada,
    tokenise,
)

__version__ = "0.1.0"
