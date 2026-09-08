# Dual trapezoid extrema and the complementary four-box sector

## Verdict

No uniform word of length

\[
                 |D(P,N)|+O(N),\qquad 0\le P\le N,
\]

is proved here for the complete dual-extrema family or for the relevant
four-box subfamily.  The investigation does produce:

1. an exact characterization of both target families;
2. a full-family `+1` construction for every `P=1` trapezoid;
3. an exact-once construction for an infinite family of thinnest nonempty
   four-box slices;
4. a sharp computational minimum of three repeats for the complete family on
   `D(2,2)`;
5. verified exact-once relevant-sector words for every nonempty slice through
   `N<=6` and for the square slice `P=N=7`; and
6. a verified three-repeat relevant-sector word at `P=N=8`.

The unrestricted small obstructions use targets outside the four-box family.
They therefore do **not** obstruct an exact-once complementary-sector braid.
Conversely, the finite positive certificates do not imply an all-`N`
construction.  No asymptotic bound in the main OR-word problem changes.

## 1. Full geometric target family

Put

\[
 D(P,N)=\{(d,a)\in\mathbb Z_{\ge0}^2:d\le P,\ d+a\le N\}.
\]

For an interval `I` of a word on this alphabet, define

\[
 (D_I,A_I,U_I)
  =\left(\max_{p\in I}d(p),\max_{p\in I}a(p),
           \min_{p\in I}(d(p)+a(p))\right).
\]

### Proposition 1: feasibility

A triple `(D,A,U)` is geometrically feasible if and only if

\[
 0\le D\le P,\qquad 0\le A\le N,\qquad
 0\le U\le\min(N,D+A).                              \tag{1.1}
\]

Necessity is immediate.  For sufficiency, all of the following points lie in
`D(P,N)` and in the rectangle `[0,D]x[0,A]`:

\[
 \begin{aligned}
 p_U&=(\min(D,U),U-\min(D,U)),\\
 p_D&=(D,\max(0,U-D)),\\
 p_A&=(\max(0,U-A),A).
 \end{aligned}                                      \tag{1.2}
\]

They respectively supply sum `U`, maximum first coordinate `D`, and maximum
second coordinate `A`; every displayed sum is at least `U` and at most `N`.
Thus their extrema are exactly `(D,A,U)`.

The full-family problem is therefore to represent every triple in (1.1), not
merely every triple occurring in the complementary four-box application.

## 2. Exact four-box target subfamily

In the complementary sector, put

\[
 N=m,\qquad c=N-P.
\]

The original parameters satisfy

\[
 0\le u<r\le P,\qquad 0\le x<r,\qquad c<x,
\]

and map to

\[
 D=x-c,\qquad A=c+r,\qquad U=u.                      \tag{2.1}
\]

Eliminating `x,r,u` gives exactly

\[
 \boxed{
 \begin{aligned}
 1&\le D\le2P-N-1,\\
 2(N-P)+D+1&\le A\le N,\\
 0&\le U\le A-(N-P)-1.
 \end{aligned}}                                      \tag{2.2}
\]

Indeed, `x=c+D` and `r=A-c`; the strict inequality `x<r` is
`A>=2c+D+1`, while `r<=P` is `A<=N`.  Conversely these formulas reconstruct
valid original parameters from every triple in (2.2).

The family is nonempty only when

\[
                         2P-N-1\ge1.                  \tag{2.3}
\]

For a square slice `P=N`, (2.2) becomes

\[
 1\le D<A\le N,\qquad0\le U<A,                       \tag{2.4}
\]

and has exact size

\[
 \sum_{A=2}^{N}A(A-1)=\frac{N(N+1)(N-1)}3.           \tag{2.5}
\]

In particular, the square `N=8` instance has 168 targets.

## 3. Two uniform positive constructions

### 3.1 The full family for `P=1`

For `N>=1`, write

\[
 A_j=(0,j)\quad(0\le j\le N),\qquad
 B_j=(1,j)\quad(0\le j<N).
\]

Then

\[
 \boxed{
 A_0,A_1,\ldots,A_N,
 B_{N-1},B_{N-2},\ldots,B_0,A_0}                    \tag{3.1}
\]

has length `|D(1,N)|+1` and represents every feasible triple.

For `D=0`, use `A_U,...,A_A`.  For `D=1`:

* if `U=0,A<N`, use `B_A,...,B_0,A_0`;
* if `U=0,A=N`, use `A_N,B_(N-1),...,B_0,A_0`;
* if `U>=1,A<N`, use `B_A,...,B_(U-1)`; and
* if `U>=1,A=N`, use `A_N,B_(N-1),...,B_(U-1)`.

Each interval visibly has maximum `d` equal to one, maximum `a` equal to
`A`, and minimum sum equal to `U`.  The degenerate `P=0` family has an
exact-once monotone vertical word.

### 3.2 Thinnest nonempty relevant slices

Suppose

\[
 2P-N-1=1.
\]

Writing `c=N-P`, this is `N=2c+2,P=c+2`.  Equation (2.2) then leaves only

\[
 (D,A,U)=(1,N,U),\qquad0\le U\le P-1.                \tag{3.2}
\]

Use the exact-once block

\[
 A_N,B_{N-1},\ldots,B_0,A_0,A_1,\ldots,A_{N-1}.     \tag{3.3}
\]

For `U=0`, the interval ends at `A_0`; for `U>=1`, stop at `B_(U-1)`.
All points with `d>=2` may be placed before or after this intact block in any
order.  This gives an exact-once relevant word for every slice in this
infinite family.

## 4. Complete-family exact-once obstructions

The complete feasible family cannot have an exact-once theorem valid for all
`P,N`.

At `D(1,1)`, there are seven feasible targets but a three-letter word has only
six physical intervals.  One repeat suffices, for example

\[
 (0,0),(0,1),(1,0),(0,0).                            \tag{4.1}
\]

The next case is sharper.  The alphabet `D(2,2)` has six points and the full
family has 23 targets.  Exhaustive enumeration gives:

| excess `q` | unique multiset permutations tested | result |
|---:|---:|---|
| 0 | 720 | UNSAT |
| 1 | 15,120 | UNSAT |
| 2 | 191,520 | UNSAT |
| 3 | explicit certificate | SAT |

The `q=0` result also follows immediately from `23>binom(7,2)=21`.  A
three-repeat certificate is

\[
 \begin{split}
 &(0,0),(0,1),(0,2),(1,1),(2,0),\\
 &(1,0),(0,0),(0,1),(1,0).
 \end{split}                                          \tag{4.2}
\]

Thus the complete-family minimum excess on `D(2,2)` is exactly three.

This is a finite exhaustive computation, not a symbolic lower-bound theorem.
More importantly, the relevant four-box family on this same alphabet consists
only of

\[
 (1,2,0),\qquad(1,2,1),                               \tag{4.3}
\]

and has an exact-once word.  The full-family obstruction cannot be imported
into the four-box problem.

## 5. Relevant-sector certificates

Explicit exact-once square certificates are stored for `P=N=2,...,7`.
Deleting every letter with `d>P` from the square-`N` certificate gives the
certificate for a smaller trapezoid `D(P,N)`.

This projection is rigorous.  Every smaller-slice target in (2.2) is also a
square target in (2.4).  A square witness for it has maximum first coordinate
`D<=P`, so it contains no deleted letter.  It therefore remains an intact
contiguous interval after projection.  Since the square word uses every point
once, its projection uses every point of `D(P,N)` once.

The stored square words consequently certify every nonempty slice through
`N<=6`, namely nine `(P,N)` pairs in total.  The square `N=7` word certifies
all `112/112` relevant targets.

At `P=N=8`, exact-once remains unresolved.  A stored word of length 48 spans
the 45-point alphabet and covers all `168/168` relevant targets.  Its three
extra occurrences are copies of

\[
                         (2,0),\quad(2,5),\quad(0,1).
\]

This proves excess at most three only.  There is no certified lower bound
excluding excess zero, one, or two at `N=8`.

## 6. Why the obvious barycentric recursion is insufficient

For the full simplex, deleting the outer boundary leaves the translate by
`(1,1)` of the simplex with parameter `N-3`.  It is tempting to recurse there
and append one closed perimeter cycle.

That construction already fails at `N=3`.  With the shifted interior point
placed before the closed boundary traversal, the resulting word in one
standard orientation is

\[
 \begin{split}
 &(1,1),(0,3),(1,2),(2,1),(3,0),(2,0),\\
 &(1,0),(0,0),(0,1),(0,2),(0,3).
 \end{split}
\]

For example, the target

\[
                         (D,A,U)=(1,1,1)              \tag{6.1}
\]

has no clean interval.  The only permissible provider letters are
`(1,1),(1,0),(0,1)`: the first is separated from the latter two by oversized
boundary points, while `(1,0)` and `(0,1)` are separated by `(0,0)`, whose
sum is zero.  Thus mixed boundary/interior portal placement is a genuine
ordering problem; the primal perimeter induction does not dualize
automatically.

## 7. Reproducible checker

The artifacts are

```text
scratch/dual_trapezoid_relevant/certificates.txt
scratch/dual_trapezoid_relevant/check_dual_trapezoid.cpp
```

The checker:

1. enumerates every physical interval of every stored word;
2. verifies spanning, exact-once status, and all relevant targets;
3. derives and verifies all nine projected nonempty slices through `N<=6`;
4. verifies the `N=7` and `N=8` certificates;
5. verifies the uniform constructions through twenty parameter values; and
6. exhaustively enumerates every unique `D(2,2)` multiset permutation with
   excess zero, one, and two.

It compiles warning-free under

```text
c++ -std=c++20 -O2 -Wall -Wextra -Wpedantic
```

and reports

```text
theorem_regressions P1=1..20 thin_c=0..20 PASS
relevant_certificates projected_N_le_6=9 square_N7=112/112 square_N8_q3=168/168 PASS
full_D22 targets=23 q0_tested=720 q1_tested=15120 q2_tested=191520 q3_certificate=PASS minimum_excess=3
PASS
```

SHA-256 inventory:

```text
ac76dc456e80f810458d7203abcbb91fc5bed05d6069413c079b287700a6cce8
    scratch/dual_trapezoid_relevant/check_dual_trapezoid.cpp
e5e1294db734fbbf63677665f9594efca4d4f96f15c9d86491de52fae99b63ca
    scratch/dual_trapezoid_relevant/certificates.txt
84d5a6edf98ddaf3e88e4b2e714d2e0b0ebe6ff52cfe10159f73a48ebd231511
    checker output
```

## 8. Scope for the main problem

The finite evidence is favorable to an exact-once or linear-excess relevant
braid, but supplies no uniform construction.  Even such a construction would
only solve the complementary **upper** sector in the equal four-chain box.
One would still need to merge sector orders, handle unequal boxes, realize
linked central intervals and lower common cores, and prove coordinatewise pin
survival.

Accordingly, the rigorous current conclusion is partial progress and a
sharper target.  It does not improve the established asymptotic upper constant
or settle `nu(k)=B(k)`.
