# Independent code audit of the reported k17 literal-word checker

2026-09-08. Reviewer: `exact_b_induction`.

Reviewed file: `scratch/verify_reported_k17_upper25374_20260908.py`.
Method: complete source read and pure logical audit; no execution by this
reviewer. Root is separately running the checker on the supplied artifact.

Verdict: PASS for a normal Python run with assertions enabled. No logical
coverage or witness-validation bug was found. This code audit alone does
not assert that the input word passes.

## Parsing and dimension

The input is either a JSON list of exact Python integers or decimal integer
tokens separated by whitespace/commas, with optional plain-text comments.
JSON booleans and nonintegers are rejected by the exact type check. The
length must be25374 and every letter lies in1,...,2^17-1. Thus every letter
is a nonempty set on exactly the permitted17 coordinates. The SHA-256
records the actual input bytes, including their encoding and formatting.

## Suffix dictionary completeness

At an endpoint j, every nonempty interval ending there is either the
single new letter or a previous suffix extended by that letter. This is
exactly the construction of `current` from `suffix`. If two previous
suffixes have the same OR, they give the same OR after every common
extension, so retaining one start for each OR loses no possible target.

The retained start remains a valid interval start. `setdefault` may choose
the one-letter witness or any earlier valid suffix witness; no ordering
assumption is needed. Induction from the empty initial dictionary proves
that every nonempty ordinary interval OR is enumerated.

At a fixed endpoint, extending intervals leftward gives a chain under
set inclusion. Distinct nonempty members have distinct ranks among1,...,17,
so the assertion that `current` has at most17 keys is correct.

## Independent witness replay

The segment tree pads to a power of two with zero, the neutral element for
OR. Its internal nodes are exact child ORs. `range_or(left,right)` converts
the inclusive interval to the standard half-open leaf range and applies
the correct left/right parity steps.

Every stored witness is explicitly checked to satisfy
0<=left<=right<len(word), and the segment-tree OR must equal its target.
Thus no wrapping interval, empty interval, or fabricated endpoint is
accepted. These checks are independent of the suffix-dictionary recurrence.

The final missing-target list ranges over every integer mask1,...,131071.
A PASS therefore entails a validated ordinary interval witness for every
nonempty17-coordinate target. The rank census is a useful report, not a
substitute for this exhaustive target check.

## Execution and reporting scope

The report is written only after all stored witnesses have been replayed.
Its status is PASS exactly when the missing list is empty, and a missing
target also triggers the final failing assertion. The code uses assertions
for validation, so it must be run without `-O` or an optimizing
PYTHONOPTIMIZE setting. Root's planned normal `python3` invocation is the
intended mode.

The opening docstring predates arrival of the artifact and is now stale;
it has no effect on the algorithm. No user construction package is needed
to certify the literal upper bound if this independent checker succeeds.
