# Hostile audit of the q4 four-by-four centre-support deficit

**Date:** 2026-08-14
**Verdict:** **PASS after display, exterior-scope and five-rail-gate
corrections.**

Audited source:

`MATH_OBSTRUCTION_Q4_CHARACTER_MINIMUM_FOUR_BY_FOUR_NEAR_C_ATOM_HAS_SUPPORT_DEFICIT_20260814.md`

H100 SHA-256:

```text
a91c985965c932aa5d66375912265c0586cb898c87a039a8567016951cf78cb7
```

## 1. Local equality states

At a target, equality in the q4 supporting plane is

```text
2|a|+2|b|-b=3,
2a+3b=1 mod 4.
```

If `b>=0`, the first equation is `2|a|+b=3`; if `b<0`, it is
`2|a|+3|b|=3`.  These bounds make the case list finite without any
computer range assumption.  Applying the congruence and then
`10a+11b+4t=1` gives exactly

```text
(-1,1,0), (1,1,-5), (0,-1,3), (0,3,-8).
```

At an exterior coordinate, equality has right side zero and every term is
nonnegative, forcing `(a,b,t)=(0,0,0)`.

## 2. Global profiles and shore-four obstruction

Four physical rails on each shore together with the centre-character lower
bound force net positive and negative masses exactly four.  Therefore there
is no aggregate centre/period cancellation, `sum(|a|+|b|)=8`, and the net
sum equations are `sum a=-1`, `sum b=1`.

Writing the four local-state multiplicities as `x,y,z,w`, the three global
equations solve to

```text
(x,y,z,w)=(2,1,2,0) or (1,0,3,1).
```

The first contains `t=-5`, the second `t=-8`.  A signed toggle-support
count from four rails per shore lies in `[-4,4]`, so neither profile is
physical.  Hence the minimum physical shore size is at least five.

The source's corrected exterior wording is important: arbitrarily many
exterior labels may exist in the ground, but at shore four no physical
positive/negative exterior centre pair can cancel, because all four units
of each shore survive in the net ledger.

## 3. Exact five-rail gate

At shore five, net mass is either four or five.  In the net-mass-four
branch there is exactly one cancelling centre/period pair.  Of the two
equality profiles, only Profile I passes the crude `|t|<=5` test.  Moreover
the cancelling pair cannot be placed at its `(1,1,-5)` target: that would
leave at most four negative noncentre rails there, raising the minimum
possible `t` to `-4`.  A correct support search must place the cancellation
elsewhere and solve the full binary incidence equations.  Net mass five
requires a separate local supporting-plane classification.

## 4. H100 replay

The strengthened verifier checks the four target states, the unique
exterior state, both global profiles, shore-four failure, and the unique
shore-five net-mass-four survivor:

```text
scratch/verify_q4_near_c_four_by_four_support_deficit_20260814.py
SHA-256 6256e7b2107cfe5b933fd6d11c87799525a124dd4f94358bd57c43d3635eaf09

H100 output SHA-256
7b942af8f0c344f6741674ffe1917ae527866d52f48c386c41c60c26873e6979
```

The replay returns `PASS` with
`minimum_physical_shore_lower_bound=5` and
`shore_five_survivor_is_profile_I=true`.

## 5. Scope

The theorem is a centre/support obstruction for periods 10 and 11.  It
does not classify net-mass-five ledgers, solve the five-rail support system,
or assert cyclic-window named-owner realizability.  Those are exactly the
next search layers.
