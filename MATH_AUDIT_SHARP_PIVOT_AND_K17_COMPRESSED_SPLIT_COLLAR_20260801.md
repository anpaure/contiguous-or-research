# Sharp-pivot audit and a literal compressed split collar at `k=17`

Date: 2026-08-01
Status: proof-safe local theorem and finite `k=17` witness.  No global
owner-factor, arbitrary-upper, or lower-compiler completion is claimed.

## 1. Verdict on the proposed sharp-aperture construction

Let `X` be inserted at a cut and let `M_0,...,M_h` be the `h+1`
length-`h+1` windows containing it.  The following parts of the proposal are
correct.

1. If the `M_j` are distinct rank-`r` sets, then

   \[
                              |X|\le r-h.
   \]

   For a coordinate outside `X`, its trace on these windows is a prefix
   union a suffix, so it can be deleted at most once.  The `h` distinct
   equal-rank transitions require `h` different deleted coordinates in
   `M_0-X`.

2. Choosing a core `B superset X`, `|B|=r-h`, and disjoint ordered banks
   `L=(lambda_1,...,lambda_h)` and `R=(rho_1,...,rho_h)` gives the explicit
   geodesic

   \[
   M_j=B\cup\rho[1,j]\cup\lambda[j+1,h].
   \]

   Its `h` lower and `h` upper transition colours are separately injective.
   Equality in the aperture bound alone does **not** imply this geodesic:
   a deleted coordinate may re-enter.  Disjointness of `L` and `R` is the
   additional hypothesis that proves geodesicity.

3. Inserting `X` between the two old letters `B+lambda_h` and `B+rho_1`
   preserves every old interval OR under convex-hull transport.  A crossing
   occurrence changes physical width by one; therefore this is literal
   deck inclusion, not preservation inside each fixed width bucket.

4. In the band of source intervals of length at most `h`, the cells outside
   the transport image are exactly the singleton `X` and the two nested
   rays

   \[
   B\cup\lambda[h-i+1,h],\qquad B\cup\rho[1,i],
   \quad1\le i<h.
   \]

   The `h-1` expelled old cells have the rank-`r` values
   `M_1,...,M_(h-1)`, so a strict-lower reference matching uses none of
   them.  Zero compiler damage nevertheless remains conditional on releasing
   the actual ray targets and `X`, admitting all displayed letters in one
   common cap, and identifying coincident physical roles rather than charging
   them twice.

Two corrections are essential.

* The pre-insertion length-`h+1` cells at this cut are the rank-`r+1`
  values `M_j union M_(j+1)`.  Hence the pivot is not inserted into an
  already-flat depth-`h` row.  It must be part of a jointly designed nonflat
  pre-scaffold.
* The first collar displayed in the sharp-aperture note is an abstract
  Johnson collar, not a source collar.  For the symmetric source, the first
  `h` source letters already union to `M_0` and the last `h` union to `M_h`.
  No distinct rank-`r` predecessor or successor can then be created by an
  exterior source letter.  The authoritative literal repair is the split-
  pivot source of
  `MATH_THEOREM_A_SPLIT_PIVOT_PHYSICAL_COLLAR_AND_BPLUS1_TERMINAL_PATH_20260801.md`.

## 2. A compressed literal split-pivot theorem

The authoritative split source used disjoint left and right boundary flag
banks.  That disjointness is sufficient but unnecessary.

Assume `h>=2`, `r-h>=2`, and split

\[
 B=C\mathbin{\dot\cup}X_L\mathbin{\dot\cup}X_R,
 \qquad X=X_L\mathbin{\dot\cup}X_R,
\]

with `X_L,X_R` nonempty.  Choose `x_L in X_L`, `x_R in X_R`, disjoint
ordered banks `L,R` of size `h`, one fresh flag `p`, and one fresh ordered
bank `D=(d_1,...,d_(h-1))`, all outside `B`.  Put

\[
 B^-=(B-\{x_R\})\cup\{p\},\qquad
 B^+=(B-\{x_L\})\cup\{p\}.
\]

For `0<=t<h`, define

\[
\begin{aligned}
 L_t&=B^-\cup\lambda[1,t+1]\cup D[t+1,h-1],\\
 R_t&=B^+\cup\rho[t+1,h]\cup D[1,t],
\end{aligned}
\]

and retain the central geodesic `M_0,...,M_h` above.

### Theorem 2.1 (shared-flag literal collar)

The path

\[
 L_0,\ldots,L_{h-1},M_0,\ldots,M_h,R_0,\ldots,R_{h-1}
\]

is the literal depth-`h` row of the following `4h+1`-letter source:

\[
\begin{array}{l}
 \{d_1\},\ldots,\{d_{h-2}\},
 (C\cup X_L)\cup\{d_{h-1}\}, B^-,\\
 \{\lambda_1\},\ldots,\{\lambda_{h-1}\},
 (B-\{x_R\})\cup\{\lambda_h\},\\
 X,\\
 (B-\{x_L\})\cup\{\rho_1\},
 \{\rho_2\},\ldots,\{\rho_h\},\\
 B^+,(C\cup X_R)\cup\{d_1\},
 \{d_2\},\ldots,\{d_{h-1}\}.
\end{array}
\]

Its owners are distinct rank-`r` sets forming a Johnson path.  Every native
shared length-`h` source cell is the corresponding owner intersection, and
every spanning length-`h+2` source cell is the corresponding owner union.
Both immediate palettes are therefore literal and injective.  Every
positive coordinate run wholly internal to the displayed owner path has
length at least `h+1`.

The construction uses only

\[
 |B|+|L|+|R|+1+|D|=(r-h)+2h+1+(h-1)=r+2h
\]

coordinates.

### Proof

The source calculation in the tight split-pivot theorem is shore-local.
The two occurrences of `p` are separated by more than `h+1` source
positions, as are the two occurrences of each `d_i`; consequently sharing
the banks introduces no new coordinate into an owner or q1 window.  The
same sliding-union calculation therefore gives the displayed owner row and
the exact shared intersections/unions.

For an intrinsic set-theoretic check, the five lower edge classes have
distinguished signatures

\[
 (x_L,p),\quad(x_L),\quad(x_L,x_R),\quad(x_R),\quad(x_R,p).
\]

The upper signatures are respectively

\[
 (x_L,p),\quad(x_L,x_R,p),\quad(x_L,x_R),
 \quad(x_L,x_R,p),\quad(x_R,p).
\]

Only the two seam signatures repeat in the upper list; their remaining
coordinates are the disjoint full banks `L` and `R`, so those two colours
are distinct.  Within either internal collar class, the prefix/suffix index
recovers the edge.  This proves both q1 injections and simplicity.

Every `lambda_j` and `rho_j` has one run of length exactly `h+1`; the
central `B` coordinates have the runs described in the tight theorem.  The
flag `p` and each `d_i` have one run touching the left endpoint and one run
touching the right endpoint.  These are clipped boundary flags, not short
internal runs.  This proves the local residence statement.  An ambient host
must still extend or protect both endpoint flag states.

## 3. Exact `k=17` specialization

For `k=17`,

\[
 r=9,\qquad h=d(17)=3,\qquad B(17)=24313.
\]

The original fresh-bank count was `r+3h=18`, so that literal version does
not fit on `[17]`.  The shared-bank theorem needs only `r+2h=15` labels and
does fit.

One authenticated instance uses

* `B={0,1,2,3,4,5}`;
* `X_L={0}`, `X_R={1}`;
* `L={6,7,8}`, `R={9,10,11}`;
* `p=12`, `D={13,14}`.

Its post-insertion source word is

```text
8192 16445 4157 64 128 317 3 574 1024 2048 4158 8254 16384
```

and its depth-three owner path is

```text
28797 20733 4605 511 959 1855 3647 7742 15422 30782
```

Direct C++ replay proves:

```text
10 distinct rank-9 owners
9 distinct literal rank-8 intersections
9 distinct literal rank-10 unions
0 short positive runs wholly internal to the owner path
78/78 old pre-insertion intervals transported with the same OR
5 exact insertion-born cells: X plus two 2-cell rays
3 pre-insertion crossing depth-three cells of rank 10
15 support coordinates
```

Artifacts:

```text
scratch/audit_k17_compressed_split_pivot_collar_20260801.cpp
42959c367b881a63d5a84492edc4e4c715ea2b2cfffc37c7c2e1b27c14a481e5

scratch/k17_compressed_split_pivot_collar_20260801.audit.json
f355b8bc45dd8881f856ed074283c3ea410c98d00d8684f29042884b8c6f141f
```

## 4. What gate this closes, and what it does not

This closes the finite coordinate-supply objection and supplies a literal,
source-compatible, locally resident, doubly-q1-rainbow pivot macro at
`k=17`.  It is strictly stronger than the abstract collar in the original
claim.

It does **not** by itself enter the current global owner factor.

1. The small protected-factor theorem would require

   \[
                              6Hh\le m-2.
   \]

   At `k=17`, `m=9,h=3`, even `H=1` asks for `18<=7`, which is false.
   Thus the asymptotic fixed-`H` planting corollary gives no finite
   `k=17` embedding.
2. The packet contributes only nine upper-q1 colours.  A global completion
   must keep them collision-free while covering all 19,448 rank-10 colours,
   arrange the remaining 24,300 owner occurrences with the one allowed
   surplus depth cell, and connect the resulting physical pieces.
3. Old-deck transparency is relative to this packet's own nonflat
   pre-insertion scaffold.  The three local rank-10 predecessor cells must
   already be integrated into a global arbitrary-width upper deck.
4. The lower compiler is zero-damage only after one jointly chooses the
   released ray targets, the task `X` (here necessarily of rank `2` through
   `6` for a two-sided split), the ambient caps, and every mixed exterior
   row.  The longest two rays coincide with native q1 cells and must not be
   double charged.
5. The endpoint flag runs remain exported boundary state.  Local residence
   is exact; regeneration inside an arbitrary global chronology is not.

Hence the strongest proof-safe conclusion is

\[
\boxed{\text{the missing pivot macro exists literally at }k=17,\text{ but
the protected Catalan/owner-factor embedding remains open.}}
\]
