# Independent audit of the shared-bank `k=17` pivot cycle

Date: 2026-08-01

Status: `PASS` for the stated cyclic local identities.  The stronger reading
that the object is boundary-state-free after an internal opening is false.

## Literal replay

The audited cyclic source is

```text
12348 20540 4157 125 189 317 3 574 1086 2110 6204
```

with `h=3`, owner rank `r=9`, and pivot position six.  An independent C++
replay obtains

```text
D^3 A =
28797 20733 4605 511 959 1855 3647 7742 15422 30782 30781.
```

Thus the additional closing owner is literally `H=30781`.  These eleven
owners are distinct rank-nine sets in one Johnson cycle.  Their eleven
intersections are distinct rank-eight colours, their eleven unions are
distinct rank-ten colours, and the two rows are literal:

```text
(D^2 A)[i+1] = (D^3 A)[i] & (D^3 A)[i+1],
(D^4 A)[i]   = (D^3 A)[i] | (D^3 A)[i+1].
```

The nonconstant cyclic positive-run lengths are

```text
8 7 4 4 4 4 4 5 7 4 4,
```

so the exact residence floor is four.  Four further coordinates are present
on every owner.

The pivot and two physical rays are exactly

```text
3; 319,447; 575,1599
```

of ranks `2; 7,8; 7,8`.  Deleting the pivot letter and opening before the
first source letter gives a ten-letter linear word.  All 55 of its nonempty
linear intervals transport to the reinserted eleven-letter word with the
same OR.  Among new physical intervals of source width at most three, the
only five not in that transport image are precisely the pivot and four rays
above.

## Boundary-state qualification

Cyclic residence is not the same as a boundary-state-free internal macro.
At every one of the eleven owner cuts, exactly four nonconstant coordinate
runs cross the cut, and opening the cycle creates exactly six endpoint
fragments shorter than four.  For the displayed opening before owner zero,
the split coordinates and `(prefix,suffix)` lengths are

```text
bit 0:  (7,1)
bit 12: (3,4)
bit 13: (1,3)
bit 14: (2,2).
```

Consequently the construction removes the old clipped-boundary state only
while it is retained as a cyclic component (or linearized at the one global
boundary).  Opening it as an internal path exports a four-coordinate endpoint
trace and requires compatible host continuation, a splice, or explicit
boundary handling.  It does not by itself solve extraction, component joining,
the killed old palettes, ranks above ten, or the common-cap compiler.

There are two further scope restrictions.  The shared-bank definition chooses
two distinct distinguished coordinates in `X`, so this form directly handles
`|X|>=2`, not an arbitrary singleton pivot.  Also, its core-bearing source
letters replace the earlier singleton presentation; guards naming those old
singleton pins must be regenerated.

The correct conclusion is therefore:

> The source is a genuine self-resident cyclic pivot packet with exact literal
> `D^3`, q1 palettes, and lower rays.  It closes the local cyclic residence
> algebra, but it does not erase the endpoint state needed to embed that cycle
> into a larger linear chronology.

## Artifacts

```text
scratch/audit_k17_shared_bank_pivot_cycle_independent_20260801.cpp
4f6d50e398e0c0f8d5987c5bf7803915db6f4359e707fce09da16d83465c4efe

scratch/k17_shared_bank_pivot_cycle_independent_20260801.audit.json
c066f4529e3dd41a23bc0dca6462628a3acdb2dac716a2eec070a85aeee7feec
```

The replay ran on one H100 CPU.  No GPU was used.
