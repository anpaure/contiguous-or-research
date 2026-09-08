# The q4 k17 owner descent has a complete mixed depth-three typed-menu oracle

**Date:** 2026-08-14

**Status:** exact finite-pool algebra and pruning theorem.  It covers every
three-exchange containing at least one self lift: pair+pair+self (PPS),
pair+self+self (PSS), and self+self+self (SSS).  Each incoming self lift is
forced to replace the outgoing self lift in the same fixed-matching group.
No q4 pool has been searched with this oracle.

## 0. Typed configuration model

Let `ell` be the current row-load vector.  There are 54 selected reflected-
pair configurations and one selected self configuration `S_g` in each of
35 disjoint self groups `g`.  Let `B` be the bank of unselected reflected-
pair configuration indices, and let `G_g` be the alternative self indices
in group `g`, excluding `S_g`.  Configurations are indexed objects: two
indices may in principle have the same row support.  All intersections
below refer to their incidence supports.

For any incoming configuration `N` and selected outgoing configuration
`P`, regardless of their row cardinalities, put

```text
a(N)=sum_(x in N)(2ell_x-1),
r(P)=sum_(x in P)(3-2ell_x).                                  (0.1)
```

Fix three distinct selected indices, written `R=(P1,P2,P3)`, and define

```text
c_R = sum_i r(P_i)+2 sum_(i<j)|P_i intersect P_j|,
h_R(N)=a(N)-2 sum_i |N intersect P_i|.                        (0.2)
```

> **Theorem 0.1 (exact typed three-exchange score).**  For three legal
> incoming configurations `N1,N2,N3`,
>
> ```text
> Delta_R(N1,N2,N3)
>  =c_R+sum_i h_R(N_i)
>       +2 sum_(i<j)|N_i intersect N_j|.                      (0.3)
> ```

The configurations may have different row cardinalities or coincident
supports.  Formula `(0.3)` uses their indexed incidence vectors and
remains exact on rows contained in all six configurations.

## 1. Proof of the score

For `d_i=1_(N_i)-1_(P_i)`, square expansion gives

```text
Phi(ell+sum_i d_i)-Phi(ell)
 =sum_i [Phi(ell+d_i)-Phi(ell)]
  +2 sum_(i<j)<d_i,d_j>.                                     (1.1)
```

The one-atom term is

```text
             r(P_i)+a(N_i)-2|P_i intersect N_i|.              (1.2)
```

Expanding the three scalar products in `(1.1)` and regrouping the
outgoing-outgoing, incoming-outgoing, and incoming-incoming intersections
proves `(0.3)`.  Because the energy is quadratic, no triple-intersection
correction exists.

If a required self menu is empty (or the pair bank has too few distinct
indices), that face has no legal leaf and is discarded.  In all remaining
pruning statements, omitted overlaps are nonnegative.  Every
displayed strict inequality is therefore a lossless necessary condition,
not a sufficient negativity test.

## 2. Complete PPS oracle

Choose two distinct selected pairs `P_i,P_j` and one selected self lift
`S_g`.  There are

```text
                       C(54,2) 35 = 50,085                    (2.1)
```

such outgoing faces.  Incoming options have the form

```text
                    N,M in B, N!=M;  V in G_g.                (2.2)
```

Write `b_1+b_2` for the sum of the two smallest `h_R` values at distinct
pair indices in `B`, and `s_g=min_(V in G_g)h_R(V)`.  The face cut is

```text
                         c_R+b_1+b_2+s_g>=0.                  (2.3)
```

For a pair candidate `N`, let `b(N)` be the smallest pair score outside
`N`.  A negative triple containing `N` must satisfy

```text
                         c_R+h_R(N)+b(N)+s_g<0.               (2.4)
```

A self candidate `V` can occur only if

```text
                         c_R+h_R(V)+b_1+b_2<0.                (2.5)
```

For retained distinct pair candidates put

```text
             p_R(N,M)=h_R(N)+h_R(M)+2|N intersect M|.         (2.6)
```

The pair prefix survives only if

```text
                              c_R+p_R(N,M)+s_g<0.              (2.7)
```

For every surviving canonical pair `N<M`, scan retained `V in G_g` with

```text
                              h_R(V)<-c_R-p_R(N,M),            (2.8)
```

and add the exact last interaction

```text
                         2|V intersect N|+2|V intersect M|.    (2.9)
```

Every negative PPS triple passes `(2.3)`--`(2.8)` because the dropped
overlaps are nonnegative.  Conversely every tested leaf is a legal PPS
triple and is evaluated by `(0.3)`.  Hence the oracle is complete.

## 3. Complete PSS oracle

Choose one selected pair `P_i` and selected self lifts `S_g,S_h` with
`g<h`.  There are

```text
                       54 C(35,2) = 32,130                    (3.1)
```

outgoing faces.  Incoming options are

```text
                      N in B, V in G_g, W in G_h.             (3.2)
```

Let `b`, `s_g`, and `s_h` be the respective menu minima.  The face cut is

```text
                              c_R+b+s_g+s_h>=0.                (3.3)
```

The lossless singleton retention tests are

```text
c_R+h_R(N)+s_g+s_h<0,
c_R+h_R(V)+b+s_h<0,
c_R+h_R(W)+b+s_g<0.                                          (3.4)
```

For retained `V in G_g,W in G_h`, put

```text
             p_R(V,W)=h_R(V)+h_R(W)+2|V intersect W|.         (3.5)
```

Keep this labelled self-prefix only when

```text
                              c_R+p_R(V,W)+b<0.                (3.6)
```

Then scan retained `N in B` satisfying

```text
                              h_R(N)<-c_R-p_R(V,W)             (3.7)
```

and restore `2|N intersect V|+2|N intersect W|`.  The same
nonnegative-overlap argument proves completeness.  No interchange of the
two self menus is allowed: `V` replaces group `g` and `W` replaces group
`h`.

## 4. Complete SSS oracle

Choose selected self lifts `S_g,S_h,S_k` with `g<h<k`.  There are

```text
                         C(35,3) = 6,545                      (4.1)
```

faces, and incoming options lie respectively in `G_g,G_h,G_k`.  Let the
three menu minima be `s_g,s_h,s_k`.  Apply the face cut

```text
                              c_R+s_g+s_h+s_k>=0.              (4.2)
```

and retain candidates by

```text
c_R+h_R(V)+s_h+s_k<0,
c_R+h_R(W)+s_g+s_k<0,
c_R+h_R(X)+s_g+s_h<0.                                        (4.3)
```

For retained `V in G_g,W in G_h`, use `(3.5)`, retain the prefix when

```text
                              c_R+p_R(V,W)+s_k<0,              (4.4)
```

and scan retained `X in G_k` with `h_R(X)<-c_R-p_R(V,W)`.  Add
`2|X intersect V|+2|X intersect W|` exactly.  The group order supplies a
unique canonical description, and the preceding argument again proves
completeness.

## 5. Exact finite interface

Together PPS, PSS, and SSS have exactly

```text
                   50,085+32,130+6,545 = 88,760               (5.1)
```

outgoing faces.  Their menu minima are obtained by sorting the pair bank
once per face and taking literal minima in at most three self groups.
Every later prefix uses exact distinct-pair exclusion or a labelled group
minimum.  Bitset intersections evaluate the restored terms.  Arbitrary
top-K truncation is not lossless.

Combined with the already frozen three-pair oracle, this covers every
legal depth-three replacement in the fixed reflection face.  It does not
cover a column absent from the finite bank, a neutral pivot followed by a
descent, a four-or-more exchange, or changing the fixed matching.

## 6. Independent H100 replay

The synthetic verifier checks the rowwise square identity, compares
`(0.3)` to direct row-load changes for all legal triples in random PPS,
PSS, and SSS suites, and verifies that every layered oracle returns exactly
the literal negative set.  A disjoint exact-cover suite supplies
nonvacuous dead faces.  It performs no q4 pool search.

Verifier and output hashes are frozen in the accompanying audit.
