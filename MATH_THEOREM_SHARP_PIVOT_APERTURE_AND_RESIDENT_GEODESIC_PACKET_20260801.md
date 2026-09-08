# Sharp pivot aperture and an explicit resident geodesic packet

Date: 2026-08-01  
Status: unconditional local construction and conditional fixed-`H`
owner/`q1` planting consequence.  The latter assumes an
incidence-vertex-disjoint protected bank on the odd middle-levels host.  No
upper-decorated bounded-component completion, regenerative Pascal lift, or
all-`k` upper bound is claimed.

## 0. Outcome

Let a nonempty source letter `X` be inserted at an internal cut, and let
`M_0,...,M_h` be the `h+1` consecutive length-`h+1` unions containing it.
If these unions are distinct rank-`r` sets, then

\[
                              |X|\le r-h.                 \tag{0.1}
\]

This is sharp.  Whenever `|X|<=r-h` and the ground set has at least `r+h`
coordinates, an explicit `2h`-letter source block produces after insertion:

* a simple rank-`r` Johnson geodesic `M_0,...,M_h`;
* pairwise-distinct immediate lower colours and pairwise-distinct immediate
  upper colours;
* exact preservation of every old contiguous-union occurrence in every
  exterior context (a crossing occurrence gains one source position); and
* exactly one singleton cell `X` and two complete nested strict-lower rays
  outside the old-cell transport image.

The block has an explicit rank-`r` residence collar.  Its owner path has
`3h+1` vertices and `3h` Johnson transitions.  Every active `lambda` and
`rho` coordinate has one internal run of exactly `h+1` owner vertices; all
remaining short runs are clipped flags at the two path endpoints.

Consequently, `H` pairwise resource-disjoint copies have a protected
middle-levels incidence bank of size `6Hh`.  The existing small
protected-factor theorem embeds this bank in a spanning owner/lower-`q1`
two-factor whenever

\[
                              6Hh\le m-2.                \tag{0.2}
\]

For fixed `H` and `h=Theta(sqrt(m))`, this holds in every sufficiently large
dimension.  The arbitrary completion need not be upper-surjective,
bounded-component, or globally resident.

## 1. Aperture bound

Number the windows containing the inserted position by `0,...,h`.  For a
coordinate `z notin X`, occurrences of `z` on the left of the cut make a
prefix of this index set present, and occurrences on the right make a
suffix present.  Hence

\[
               \{j:z\in M_j\}=\text{a prefix}\ \cup\ \text{a suffix}.
                                                               \tag{1.1}
\]

In particular the binary trace of `z` has at most one transition `1->0`.
At each of the `h` transitions `M_(j-1)->M_j`, the sets are distinct and
have equal rank, so at least one coordinate is deleted.  Deleted coordinates
at different transitions are distinct by (1.1), and none lies in `X`.
They all lie in `M_0-X`.  Therefore

\[
                         h\le |M_0-X|=r-|X|,
\]

which proves (0.1).

### Equality scope

If `|X|=r-h`, every step deletes exactly one coordinate and, by equal rank,
inserts exactly one coordinate.  Thus equality forces a single-swap Johnson
walk

\[
 M_j=X\cup\{\rho_1,\ldots,\rho_j\}
          \cup\{\lambda_{j+1},\ldots,\lambda_h\}.       \tag{1.2}
\]

The entering and leaving labels in (1.2) need not be disjoint: a coordinate
may have trace `1...10...01...1` and be reinserted.  Thus equality alone does
**not** force a shortest Johnson geodesic.  Geodesicity follows under the
additional no-reinsertion condition, and is built explicitly below by
choosing the two banks disjoint.

## 2. Explicit sharp block

Choose `Q superseteq X` with

\[
                              |Q|=r-h,                    \tag{2.1}
\]

and choose two disjoint ordered `h`-tuples outside `Q`,

\[
 L=(\lambda_1,\ldots,\lambda_h),\qquad
 R=(\rho_1,\ldots,\rho_h).                               \tag{2.2}
\]

The required number of coordinates is `(r-h)+2h=r+h`.  Take the old word

\[
 \{\lambda_1\},\ldots,\{\lambda_{h-1}\},Q\cup\{\lambda_h\}
 \ \big|\
 Q\cup\{\rho_1\},\{\rho_2\},\ldots,\{\rho_h\}.         \tag{2.3}
\]

Insert the letter `X` at the displayed cut.  Directly, the `h+1` windows of
length `h+1` which contain it are

\[
 M_j=Q\cup\{\rho_1,\ldots,\rho_j\}
        \cup\{\lambda_{j+1},\ldots,\lambda_h\},
                   \qquad0\le j\le h.                   \tag{2.4}
\]

Every `M_j` has rank `(r-h)+j+(h-j)=r`, and

\[
                  M_{j+1}=M_j-\{\lambda_{j+1}\}
                                +\{\rho_{j+1}\}.         \tag{2.5}
\]

Since `L,R` are disjoint, these owners are distinct and (2.5) is a shortest
Johnson geodesic from `Q union L` to `Q union R`.

Its immediate lower and upper colours are

\[
\begin{aligned}
 I_j&=M_j\cap M_{j+1}
   =Q\cup\{\rho_1,\ldots,\rho_j\}
      \cup\{\lambda_{j+2},\ldots,\lambda_h\},\\
 U_j&=M_j\cup M_{j+1}
   =Q\cup\{\rho_1,\ldots,\rho_{j+1}\}
      \cup\{\lambda_{j+1},\ldots,\lambda_h\},
                       \qquad0\le j<h.                 \tag{2.6}
\end{aligned}
\]

The `I_j` are pairwise distinct, as are the `U_j`.  They have ranks `r-1`
and `r+1`, respectively.

## 3. Exact deck transparency and lower rays

The two old letters adjacent to the cut are

\[
                    Q\cup\{\lambda_h\},\qquad
                    Q\cup\{\rho_1\}.                    \tag{3.1}
\]

Their union contains `Q`, and hence `X`.  By the exact monotone-insertion
criterion, transporting an old interval across the enlarged word preserves
its literal OR: intervals on one side are unchanged, while every crossing
interval already contains (3.1) and therefore gains no new coordinate from
`X`.  Crossing intervals gain one source position, so the statement is
value/occurrence transport for intervals of every original length, not
width-bucket preservation.  Thus

\[
                    \operatorname{Deck}(A^{old})
                     \subseteq\operatorname{Deck}(A^{new})             \tag{3.2}
\]

occurrence by occurrence, at every width and in every fixed exterior.

Inside the width-at-most-`h` compiler band, the cells outside the transport
image are the singleton `X` and the two rays

\[
\begin{aligned}
 P_i&=Q\cup\{\lambda_{h-i+1},\ldots,\lambda_h\},\\
 S_i&=Q\cup\{\rho_1,\ldots,\rho_i\},
                         \qquad1\le i<h.                 \tag{3.3}
\end{aligned}
\]

They have rank `r-h+i<r` and form two strict nested chains.  The `h-1`
old crossing width-`h` cells which leave the short band have values
`M_1,...,M_(h-1)`, all of rank `r`.  Hence no strict-lower edge of a
reference matching can use a lost cell.

It follows from the flat monotone-pivot compiler theorem that, provided

1. the ray targets in (3.3) are released from the old target matching;
2. `X` is either a new task or its old matching edge is also released; and
3. the displayed letters are admitted by the one common cap/guard state,

the transported background edges together with the `2h-2` ray assignments
and the singleton assignment form a complete literal lower matching.  The
construction itself is a common-`Q` witness, so there is no further maximal-
cap obstruction.  This conclusion is local to the declared target bank and
does not manufacture a global carrier containing the block.

## 4. Explicit residence collar

Assume `k>=r+3h`.  Fix `q in Q`; choose fresh `q^-`,`q^+` and fresh banks

\[
 D^-=(d^-_1,\ldots,d^-_{h-1}),\qquad
 D^+=(d^+_1,\ldots,d^+_{h-1}).                           \tag{4.1}
\]

Put

\[
 Q^-=(Q-\{q\})\cup\{q^-\},\qquad
 Q^+=(Q-\{q\})\cup\{q^+\}.                             \tag{4.2}
\]

For `0<=t<h`, define

\[
\begin{aligned}
 L_t&=Q^-\cup\{\lambda_1,\ldots,\lambda_{t+1}\}
          \cup\{d^-_{t+1},\ldots,d^-_{h-1}\},\\
 R_t&=Q^+\cup\{\rho_{t+1},\ldots,\rho_h\}
          \cup\{d^+_1,\ldots,d^+_t\}.                   \tag{4.3}
\end{aligned}
\]

Empty displayed ranges are omitted.  Every set in (4.3) has rank `r`.
Consecutive left-collar owners exchange `d^-_(t+1)` for
`lambda_(t+2)`; the left seam exchanges `q^-` for `q`.  The central path is
(2.5), the right seam exchanges `q` for `q^+`, and consecutive right-collar
owners exchange `rho_(t+1)` for `d^+_(t+1)`.  Therefore

\[
 L_0,\ldots,L_{h-1},M_0,\ldots,M_h,R_0,\ldots,R_{h-1}   \tag{4.4}
\]

is a simple rank-`r` Johnson path with `3h+1` owners and `3h` transitions.

All immediate lower colours in (4.4) are distinct, and all immediate upper
colours are distinct.  For intersections, left internal edges contain
`q^-`, central edges contain `q`, and right internal edges contain `q^+`.
Neither seam intersection contains any of `q^-,q,q^+`; the two seams are
respectively `(Q-{q}) union L` and `(Q-{q}) union R`, hence are distinct.
For unions, the three internal classes have the same one-label signatures,
whereas the left and right seams contain `(q^-,q)` and `(q,q^+)`,
respectively.  Within each internal class, the exchanged `lambda/D^-` or
`rho/D^+` index recovers the edge.

For `1<=j<=h`, coordinate `lambda_j` occurs in

\[
             h-j+1\text{ left-collar owners}+j\text{ central owners},
\]

and `rho_j` occurs in

\[
             h-j+1\text{ central owners}+j\text{ right-collar owners}.
\]

These occurrences are consecutive, so every such run has length exactly
`h+1`.  Coordinate `q` has the central run `M_0,...,M_h`, also of length
`h+1`; every member of `Q-{q}` persists through the whole path.  The
`q^-,D^-` runs meet the far-left endpoint and the `q^+,D^+` runs meet the
far-right endpoint.  They are clipped boundary flags, not certified
internal resident runs after an arbitrary ambient completion.  A global
host must extend, protect, or keep them at path boundaries.

The distinct-coordinate count is

\[
        |Q|+|L|+|R|+2+|D^-|+|D^+|=r+3h,                \tag{4.5}
\]

which explains the stated ground-set hypothesis.

## 5. Fixed-`H` owner/`q1` planting

Specialize here to the odd middle-levels host on `[2m-1]`, with owner rank
`r=m`.  The generic `(k,r)` packet above cannot be fed into the protected
factor theorem without this specialization or an independently identified
isomorphic odd host.

Lift each Johnson transition in (4.4) through its rank-`r-1` intersection
to the middle-levels incidence graph.  Each transition contributes two
incidence edges, so one collared path contributes `6h` edges.  The
distinct-lower-colour property makes the lift 2-bounded.  Here
“resource-disjoint” means that different copies share neither an owner
vertex nor a rank-`m-1` lower-colour vertex in `ML_m`; it does not mean that
their coordinate supports are disjoint.  For `H` such copies the union
remains 2-bounded and has `6Hh` edges.

The small protected-factor theorem therefore extends it to a spanning
owner/lower-`q1` two-factor whenever (0.2) holds.  For fixed `H` and
`h=Theta(sqrt(m))`, this is eventually automatic.

This completion theorem controls neither the number of components nor the
paired upper palette.  It also does not protect residence outside (4.4),
all-width witnesses outside the packet, or one common compiler cap.  The
new local theorem closes the formerly missing **pivot-rich flat chain pair**;
the remaining theorem is a protected upper-decorated Catalan connector and
regenerative boundary-state completion.

## 6. Correct frontier

The construction proves:

\[
 \boxed{\text{sharp aperture + explicit flat pivot + zero local OR damage
        + exact two-ray compiler + fixed-}H\text{ q1 planting}.}
\]

It does not prove `nu(k)<=B(k)+O(1)`.  A sufficient next theorem is an
upper-surjective near-factor containing a fixed bank of paths (4.4), with
`O(1)` components and upper holes, together with a bounded regenerative
state for the clipped flags and the terminal common cap.
