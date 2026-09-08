# Audit of the minimal ROTS parity marker and reset curvature theorem

**Date:** 2026-08-02  
**Status:** separate symbolic replay PASS.  This audit concerns the
abstract local face and its exact ROTS interface; it does not certify a
literal K17/K19/K21 bridge.

## 1. Exact pair enumeration

The even triples are

```text
e00 = a0 b0 c0
e01 = a0 b1 c1
e10 = a1 b0 c1
e11 = a1 b1 c0
```

Covering both `A` and `B` exactly leaves only two pairs:

```text
e00 + e11  -> c0 twice
e01 + e10  -> c1 twice.
```

Hence the even face has no integral cover.  Its four half-columns cover
every one of the six resources once.

The four odd bridges and their forced even complements are

```text
o00 + e11
o11 + e00
o01 + e10
o10 + e01.
```

Each displayed pair contains one `a0/a1`, one `b0/b1`, and one `c0/c1`.
Thus one odd bridge is sufficient, and exact `A/B` coverage proves that its
complement is forced.  This independently verifies Theorem 1.1.

## 2. Tag and dummy scope

Any exact cover in a refined catalogue whose columns retain one of the four
even physical footprints projects to an exact cover by the even columns.
The pair enumeration disproves that projection.  Private identity rows and
forced singleton columns vanish under the projection, so they do not alter
the contradiction.

An optional marker must therefore contain a physical odd mode.  With one
private marker row, the off and on modes are respectively `m` and
`m+o_ij`; the on mode plus the forced complement is an exact cover.  The
word “marker” must not be used for a duplicated even state with a new label.

## 3. Reset-curvature replay

Write `r_ij=lambda(e_ij)` and assume the odd twin keeps the corresponding
reset signature.  The fractional signature is

\[
                  \bar r=(r_{00}+r_{01}+r_{10}+r_{11})/2.
\]

The diagonal integral repair has defect

\[
 r_{00}+r_{11}-\bar r
   ={1\over2}(r_{00}+r_{11}-r_{01}-r_{10}),
\]

while the off-diagonal repair has the negative defect.  Thus one vertical
bridge is transparent exactly when the rectangle curvature vanishes.  Two
cells of equal curvature cancel when opposite diagonal classes are chosen.
No divisibility assumption was hidden: when the half-sum is nonintegral, a
single integral repair cannot equal it, and the paired cancellation remains
the first possible local repair.

## 4. Rooted Hall replay

After choosing a two-edge protected pair `P`, residual Hall is

\[
 |N(X)\setminus V_R(P)|\ge |X\setminus V_L(P)|.
\]

Moving the two deletion terms gives

\[
 |V_R(P)\cap N(X)|-|V_L(P)\cap X|
     \le |N(X)|-|X|,
\]

which is exactly the cut-charge formula in the theorem.  Hence physical
resource complementarity and reset transparency do not silently imply
rooted extension.

## 5. Direct-sum replay

For one parity cell, the demand class is nonzero of order two: subtracting
an odd bridge leaves its even complement.  Direct sum preserves cokernels,
so `t` independent cells give `(Z/2)^t`.  `b` binary tickets contribute at
most `b` residue vectors.  If every ticket touches at most `h` cells, fewer
than `ceil(t/h)` active tickets leave some nonzero demand coordinate
untouched.  This verifies both lower bounds and rules out an `O(1)` marker
claim based only on local determinant two.

## 6. Proof-safe scope

Verified:

* one odd completed column is the smallest algebraic repair;
* an optional repair has one parity bit/two modes;
* zero reset curvature is necessary and sufficient for a vertical
  one-ticket transparent repair;
* protected rooted extension is exactly the residual Hall cut system; and
* independent parity cells can require an unbounded marker bank.

Not verified or claimed:

* existence of an odd completed socket in the K17 joint catalogue;
* bounded two-primary cokernel rank of the full ROTS common selector;
* normality after its lattice class is cleared;
* chronology connectivity, residence, upper decks, common-cap, compiler,
  or a word.
