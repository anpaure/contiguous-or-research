# Self-audit: six-slot `h=5` all-face and complete closure

**Date:** 2026-08-04  
**Verdict:** `GO_SELF`.  The strengthening from face `Z` to all three
endpoint faces was rederived directly from the exact compact inequalities.
No equality specific to `X`, `Y`, or `Z` is used.  This audit is entirely
mathematical; no search or chamber sampling is involved.

## 1. Audited theorem

| file | SHA-256 |
|---|---|
| `MATH_THEOREM_SIX_SLOT_H5_SMALL_DELTA_ALL_FACE_AND_COMPLETE_POSITIVITY_20260804.md` | `209c353358d372113ae31fc5e5450d5e33d31d9a3acdf7a4d495b209220f96c7` |

## 2. The globalization step

Every point of the compact physical face union satisfies

\[
 A-2m\le\delta.
\]

Hence, throughout `0<delta<A/15`,

\[
 m\ge(A-\delta)/2>7A/15.
\]

This inequality is common to all faces; equality is not required.

If `m<=A/2`, the authenticated decreasing interval gives

\[
 F(m)\le F(7A/15)<7121\cdot10^{-6}.
\]

If `m>A/2`, then `0<=A-m<A/2`, so

\[
 F(m)=\Theta(m)-F(A-m)<\varepsilon<7121\cdot10^{-6}.
\]

The same reflection branch is valid for every upper estimate on `F(v)`
when `v>A/2`.  The compact polytope supplies `m,v<=A`, so both reflected
arguments lie in the authenticated positive lower half.

Since `y<=2A/5`, the no-interior-minimum theorem gives

\[
 F(y)\ge F(2A/5)>18879\cdot10^{-6}.
\]

Therefore

\[
 F(y)-F(m)>11758\cdot10^{-6}
\]

uniformly on the entire face union.

## 3. Remaining compact ledger

The common rows

\[
 x\le A/5,
 \qquad v\ge(A+4u)/5,
 \qquad u<A/6
\]

are likewise independent of the active face.  The quarter endpoint and
no-interior-minimum theorem imply `F(x)>=C`, so the exact first-two-ray
bank is bounded below by `2C-F(u)-F(v)`.

The three cases recompute as follows, in units of `10^-6`:

| `u` interval | lower bound for first-two-ray bank | third-ray credit | three-theta charge | final margin |
|---|---:|---:|---:|---:|
| `[0,A/32]` | `-10682` | `11758` | `-150` | `926` |
| `[A/32,A/16]` | `-10952` | `11758` | `-150` | `656` |
| `[A/16,A/6)` | `-10412` | `11758` | `-150` | `1196` |

The relevant forced anchors are respectively

\[
 v\ge A/5,
 \qquad v\ge9A/40,
 \qquad v\ge A/4.
\]

If `v<=A/2`, strict monotonicity prices these at `49730`, `48000`, and
`45160`; if `v>A/2`, reflection prices `F(v)` by `epsilon=50`, which is
strictly stronger.  Thus no hidden `v<=A/2` assumption survives from the
face-`Z` predecessor.

All six period gains are nonnegative and were discarded safely.  No theta
positivity is used: all three errors are charged by the absolute bound.

## 4. Exhaustion of the branch

The normalized branch has exactly

\[
 0\le\delta<A/5.
\]

The three rigorously disjoint ranges are:

* `delta=0`, margin `163/70000`;
* `0<delta<A/15`, margin `656/1000000`;
* `A/15<=delta<A/5`, margin `59573/132500000`.

They exhaust the canonical endpoint normalization.  Hence the conclusion
is complete positivity of the canonical six-slot `h=5` branch, and no
larger claim.

## 5. Scope

The audit does not promote this to complete six-slot positivity without
separate citations for all other least-density branches.  It makes no
claim about arbitrary grids, universal Bellman positivity, or OR words.

**Final self-audit verdict:** `GO_SELF`.
