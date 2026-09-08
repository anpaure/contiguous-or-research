# A split-core pivot has a literal two-sided residence collar

Date: 2026-08-01  
Status: unconditional local source construction for `h>=2`,
`r-h>=2`, `2<=|X|<=r-h`, and an ambient ground set of size at least
`r+3h`.
It closes the endpoint-overlap defect of the duplicated-core pivot.  Global
upper-exact Hamilton-path completion, exterior guards, and regeneration
remain open.

## 0. Outcome

The first pivot-rich source put the whole pivot target `X` into both source
letters adjacent to the insertion.  Consequently the `h` shared source
letters at each end already had union equal to the endpoint owner; any
flat predecessor or successor was forced to repeat that owner.  Its abstract
two-sided owner collar therefore was not a literal source collar.

This defect disappears by splitting

\[
                         X=X_L\mathbin{\dot\cup}X_R,
             \qquad X_L,X_R\ne\varnothing.             \tag{0.1}
\]

There is an explicit `4h+1`-letter final source word whose depth-`h` row is
the `3h+1`-owner path

\[
 L_0,\ldots,L_{h-1},M_0,\ldots,M_h,R_0,\ldots,R_{h-1}. \tag{0.2}
\]

All owners have rank `r`; the path is simple and Johnson; both immediate
palettes are injective as set-valued owner-transition palettes; every
internal coordinate run has length at least `h+1`.  Every immediate upper
colour is literal in the displayed source.  In the minimally written source,
four immediate lower colours can be strict supersets of their native shared
source cells.  They are not forced deficits: the native legal-enlargement
repair in
`MATH_THEOREM_SPLIT_CORE_PIVOT_NATIVE_LOWER_Q1_REPAIR_AND_TWO_ADDRESS_MINIMALITY_20260801.md`
makes every lower colour literal without changing the owner row or pivot
ledger.  Deleting the one source letter
`X` changes (0.2) exactly to

\[
 L_0,\ldots,L_{h-1},U_0,\ldots,U_{h-1},R_0,\ldots,R_{h-1}, \tag{0.3}
\]

where every `U_j` has rank `r+1`.  Reinserting `X` preserves every old
interval OR and replaces these `h` upper cells by the `h+1` pivot owners.
Its new strict-lower cells are exactly the one-letter cell with value `X`
and two complete nested rays.

Thus the nonflat pre-insertion scaffold and the literal residence collar
are compatible in one source word.  The construction does not yet embed
this word into the global `W+1` depth row.

## 1. Labels and owners

Let `h>=2` and `r-h>=2`, and assume that the ambient ground set has at
least `r+3h` labels.  Choose a base set `B` of size

\[
                              |B|=r-h,                    \tag{1.1}
\]

and a target `X subseteq B` with a nontrivial partition (0.1).  Put

\[
                              C=B\setminus X.             \tag{1.2}
\]

Choose `x_L in X_L`, `x_R in X_R`, two disjoint ordered `h`-banks

\[
 \Lambda=(\lambda_1,\ldots,\lambda_h),\qquad
 P=(\rho_1,\ldots,\rho_h),                              \tag{1.3}
\]

fresh seam labels `q^-,q^+`, and fresh banks

\[
 D^-=(d^-_1,\ldots,d^-_{h-1}),\qquad
 D^+=(d^+_1,\ldots,d^+_{h-1}).                          \tag{1.4}
\]

All displayed labels outside `B` are distinct.  Define

\[
 B^-=(B-\{x_R\})\cup\{q^-\},\qquad
 B^+=(B-\{x_L\})\cup\{q^+\}.                           \tag{1.5}
\]

For `0<=t<h`, put

\[
\begin{aligned}
 L_t&=B^-\cup\{\lambda_1,\ldots,\lambda_{t+1}\}
             \cup\{d^-_{t+1},\ldots,d^-_{h-1}\},\\
 R_t&=B^+\cup\{\rho_{t+1},\ldots,\rho_h\}
             \cup\{d^+_1,\ldots,d^+_t\},              \tag{1.6}
\end{aligned}
\]

and

\[
 M_j=B\cup\{\rho_1,\ldots,\rho_j\}
        \cup\{\lambda_{j+1},\ldots,\lambda_h\},
                         \qquad0\le j\le h.             \tag{1.7}
\]

Every displayed owner has rank `r`.  Consecutive transitions in the three
blocks exchange respectively

\[
 d^-_{t+1}\to\lambda_{t+2},\qquad
 \lambda_{j+1}\to\rho_{j+1},\qquad
 \rho_{t+1}\to d^+_{t+1},                              \tag{1.8}
\]

while the seams exchange

\[
                         q^-\to x_R,qquad x_L\to q^+.   \tag{1.9}
\]

Hence every consecutive pair in (0.2) is Johnson adjacent.  The three
blocks are mutually disjoint as owner sets: every `L_t` contains `q^-` and
omits `x_R`, every `M_j` contains both `x_L,x_R` and neither seam label,
and every `R_t` contains `q^+` and omits `x_L`.  Within each block the
fresh prefix/suffix index changes strictly.  Thus (0.2) is also simple.

## 2. The literal source word

Empty singleton ranges below are omitted.  Define the final source word

\[
\begin{array}{l}
 \{d^-_1\},\ldots,\{d^-_{h-2}\},
 C\cup X_L\cup\{d^-_{h-1}\},
 (X_R-\{x_R\})\cup\{q^-\},\\
 \{\lambda_1\},\ldots,\{\lambda_{h-1}\},
 C\cup X_L\cup\{\lambda_h\},\\
 X,\\
 C\cup X_R\cup\{\rho_1\},
 \{\rho_2\},\ldots,\{\rho_h\},\\
 (X_L-\{x_L\})\cup\{q^+\},
 C\cup X_R\cup\{d^+_1\},
 \{d^+_2\},\ldots,\{d^+_{h-1}\}.
                                                               \tag{2.1}
\end{array}
\]

Each displayed block has the intended total order.  Every source letter is
nonempty: the two seam letters remain nonempty even when
`X_R-{x_R}` or `X_L-{x_L}` is empty because they contain `q^-` or `q^+`,
and every other letter contains either a displayed fresh label or the
nonempty set `X`.  The word has

\[
             h+h+1+h+h=4h+1                             \tag{2.2}
\]

letters, so its depth-`h` row has `3h+1` cells.

### Theorem 2.1 (exact factorization)

The depth-`h` row of (2.1) is exactly (0.2).

#### Proof

The first length-`h+1` window contains the `h-1` labels of `D^-`, the seam
letter `(X_R-{x_R})+q^-`, the base `C+X_L`, and `lambda_1`; its union is
`L_0`.  Sliding through the lambda singletons successively removes
`d^-_(t+1)` and adds `lambda_(t+2)`, giving `L_1,...,L_(h-1)`.

At the next slide, the seam letter leaves and the inserted `X` enters.  The
coordinates `X_R-{x_R}` persist through `X`, while `q^-` is replaced by
`x_R`; the result is `M_0`.  Sliding across the central block successively
replaces `lambda_(j+1)` by `rho_(j+1)`, giving `M_1,...,M_h`.

At the right seam, `X` leaves and `(X_L-{x_L})+q^+` enters.  The other
members of `X_L` persist, while `x_L` is replaced by `q^+`; the result is
`R_0`.  The remaining slides replace `rho_(t+1)` by `d^+_(t+1)`, giving
the rest of (0.2).  \(\square\)

## 3. Pre-insertion row and full deck transparency

Delete the central letter `X` from (2.1).  The two newly adjacent letters
are

\[
              C\cup X_L\cup\{\lambda_h\},qquad
              C\cup X_R\cup\{\rho_1\}.                \tag{3.1}
\]

Their union contains `C union X=B`, hence contains the deleted letter `X`.
The monotone-insertion criterion therefore gives an injective transport of
every old interval occurrence to the final word with exactly the same OR,
for every old interval length and in every exterior context.  A crossing
interval gains one source position, so this is deck-value transparency, not
preservation of its width bucket; the expelled short-band rows are accounted
for explicitly in Section 5.

The `h` old depth-`h` windows crossing (3.1) are

\[
 U_j=M_j\cup M_{j+1}
   =B\cup\{\rho_1,\ldots,\rho_{j+1}\}
      \cup\{\lambda_{j+1},\ldots,\lambda_h\},
                  \qquad0\le j<h.                     \tag{3.2}
\]

They have rank `r+1`.  Every other depth-`h` window is unchanged.  This
proves (0.3) and the exact local rank surgery

\[
                 (U_0,\ldots,U_{h-1})
                     \longmapsto(M_0,\ldots,M_h).       \tag{3.3}
\]

## 4. Immediate palettes and residence

The immediate lower and upper colours of the central geodesic are the
usual distinct prefix/suffix splits.  Left internal intersections/unions
contain `q^-`, central ones contain the full base `B`, and right internal
ones contain `q^+`.  The two seam intersections contain neither seam label
and are

\[
        (B-\{x_R\})\cup\Lambda,qquad
        (B-\{x_L\})\cup P,                             \tag{4.1}
\]

and their unions contain `(q^-,x_R)` and `(x_L,q^+)`, respectively.  These
signatures, together with the moving filler index, prove that all
set-theoretic immediate lower colours are distinct and all immediate upper
colours are distinct.  This is an incidence statement; literal realization
of the lower intersections at their native shared cells is subtler.

For consecutive owners `V_i,V_(i+1)`, let `J_i` be the OR of their `h`
shared source letters.  Always `J_i subseteq V_i cap V_(i+1)`.  Equality
holds except at the following four transitions (an empty displayed deficit
makes that row tight):

\[
\begin{array}{c|c}
\text{transition}&(V_i\cap V_{i+1})\setminus J_i\\ \hline
L_{h-2}\to L_{h-1}&C\cup X_L\\
L_{h-1}\to M_0&X_R\setminus\{x_R\}\\
M_h\to R_0&X_L\setminus\{x_L\}\\
R_0\to R_1&C\cup X_R
\end{array}                                                   \tag{4.3}
\]

The first and fourth deficits are always nonempty in the minimally written
source.  The four-letter native repair cited above enlarges exactly the four
distinguished seam/collar letters by the displayed missing sets; each
enlargement lies in every owner window containing that source position.
Hence the owner row stays fixed and all four shared cells become exact
intersections.  No external lower-q1 occurrence is necessary after that
redesign.  Every upper colour is literal as the OR of the `h+2` source
letters spanning the two owner windows.

Every `lambda_j` and `rho_j` has one consecutive run of length `h+1`.
Every member of `C`, every member of `X_L-{x_L}`, and every member of
`X_R-{x_R}` persists through all three owner blocks.  Coordinate `x_L`
runs from the left endpoint through `M_h`; coordinate `x_R` runs from
`M_0` through the right endpoint.  The `D^-,q^-` runs are clipped at the
left endpoint and the `D^+,q^+` runs at the right endpoint.  Thus no
internal run has length below `h+1`; the only incomplete residence data in
the abstract owner subpath are the named endpoint flags.  If the literal
source word is concatenated to an exterior, its crossing depth-`h` windows
automatically extend each flag to length `h+1` (or the flag stays clipped at
a global source endpoint).  The exterior gate is validity of those crossing
owners and their palette/guard rows, not an additional run-length choice.

The ground-set cost is still

\[
                |B|+2h+2+2(h-1)=r+3h.                 \tag{4.2}
\]

## 5. Exact lower cells and compiler consequence

The cells of source length at most `h` outside the old-interval transport
image are exactly

\[
 X,qquad
 B\cup\{\lambda_{h-i+1},\ldots,\lambda_h\},qquad
 B\cup\{\rho_1,\ldots,\rho_i\},quad1\le i<h.          \tag{5.1}
\]

They are the one-letter task cell with value `X` and two complete
strict-lower rays.  The old
short cells which leave the band have the rank-`r` values
`M_1,...,M_(h-1)`.  Hence the flat monotone-pivot compiler theorem handles
the pivot rays and `X` with zero residual deficiency, subject to its
reference-matching, occurrence-release, and one-common-cap hypotheses.
For the minimally written source this statement does not discharge (4.3).
For the repaired source, all four lower-q1 cells are native and no such
protected-host obligation remains.  A compiler fixed on the unrepaired
source does not automatically transport through the enlargement and must be
chosen on the repaired scaffold.

Unlike the duplicated-core construction, Theorem 2.1 proves that the owner
collar and the literal source packet are one object; no separate source-
antecedent assumption remains locally.

## 6. Scope and remaining theorem

This result requires `|X|>=2` to split the target into two nonempty shores.
Within a one-letter monotone insertion it is also necessary for two
distinct equal-rank seam moves: if `X={x}`, the left seam can replace an
old seam label by `x` only when the old left adjacent letter omits `x`, and
the right seam can replace `x` by a new seam label only when the old right
adjacent letter omits `x`.  Their union then omits `x`, contradicting the
monotone-transparency condition.  This is not a no-go for a nonmonotone,
multi-insertion, or genuinely one-sided singleton host.

The local source has raw insertion charge one and zero old-deck damage.  It
does not prove that a global depth row contains the protected path (0.2),
that the exterior completes its clipped flags, or that the one nonowner
depth cell at total length `B+1` is correctly placed.  Combined with the
protected Hamilton-path reduction, the remaining central theorem is:

> embed (0.2) in an upper-exact rooted Catalan Hamilton path, attach the
> pre-insertion upper block (3.2) to the exterior, use the native repaired
> lower-q1 letters, and preserve one common
> lower cap and arbitrary-width upper witnesses with bounded regenerative
> state.

The split-core theorem removes the prior local endpoint-overlap obstruction
from that statement.
