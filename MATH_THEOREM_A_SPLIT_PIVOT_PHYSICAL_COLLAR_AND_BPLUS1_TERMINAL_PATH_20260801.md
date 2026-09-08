# Split-pivot physical collars and the exact `B+1` terminal-path interface

Date: 2026-08-01  
Lane: A, monotone pivot / fixed-`H` planting / `B+1` owner path  
Status: theorem and correction.  The central pivot block and the abstract
Johnson collar proposed in the sharp-aperture note are separately correct,
but their displayed source formulas are not composable.  The proposed
two-shore split gives a literal owner collar but has four non-tight lower-q1
addresses.  A tighter two-pivot-bit allocation closes all four and gives a
literal source-compatible collar with both q1 palettes.  Independently, one
saturated endpoint can be absorbed by the unique surplus depth cell in a
`B+1` terminal construction.  Neither statement supplies the remaining
upper-surjective path matching or the global common compiler.

## 0. Exact verdict

Let the depth be `h>=2` and the owner rank be `r`.

1. The sharp aperture inequality, the explicit central geodesic, monotone
   preservation of every old interval OR, and the two new strict-lower rays
   are correct.
2. The previously displayed `3h`-edge collar is a valid **abstract** simple
   Johnson path with injective lower and upper q1 palettes.  For the original
   source with `X subseteq Q` on both sides, however, it is not a literal
   depth-`h` source collar: the `h` shared source letters at each endpoint
   already union to the endpoint owner.
3. If the pivot is split as `X=X_L dotcup X_R`, with both parts nonempty,
   the adjacent old letters can be changed so that the same central owner
   geodesic has a genuine aperture at both ends.  The proposed sparse source
   has four exactly identified lower-q1 deficits.  Reallocating the common
   core to the two seam letters yields an explicit `4h+1`-letter source
   whose depth-`h`, depth-`h-1`, and depth-`h+1` rows contain the complete
   owner, lower-q1, and upper-q1 collar.
4. A bank of `H` incidence-resource-disjoint corrected collars still has
   exactly `6Hh` middle-levels incidence edges.  The small protected-factor
   theorem applies when `6Hh<=m-2`, but yields only an owner/lower-q1
   two-factor.  It does not give the upper-surjective Hamilton path needed
   for `B+1`.
5. At `B+1`, the correct owner target is a near-perfect matching whose
   contraction is a tree, not a two-factor with a residual closure edge.
   The original saturated pivot can occur at a terminal end: its one forced
   duplicate owner is the unique surplus depth cell, after which a distinct
   neighbour can be reached under an exact exposed-coordinate condition.

In particular, neither the original collar claim nor the fixed-`H`
two-factor theorem proves a physical `B+1` word.

For future use, Theorem 4.2 is the superseding literal local source.
Theorem 4.1 is retained only to audit the proposed smaller-letter
serialization and to record its exact four-deficit boundary.

## 1. The central monotone pivot, including the pre-insertion row

Choose a core `B` with

\[
        \varnothing\ne X\subseteq B,\qquad |B|=r-h,          \tag{1.1}
\]

and disjoint ordered banks outside `B`,

\[
 L=(\lambda _1,\ldots,\lambda _h),\qquad
 R=(\rho _1,\ldots,\rho _h).                               \tag{1.2}
\]

The original symmetric source uses the adjacent letters
`B+lambda_h` and `B+rho_1`, and inserts `X` between them.  The `h+1`
new depth-`h` cells through `X` are

\[
 M_j=B\cup\{\rho _1,\ldots,\rho _j\}
        \cup\{\lambda _{j+1},\ldots,\lambda _h\},
        \qquad 0\le j\le h.                                \tag{1.3}
\]

Thus

\[
 M_{j+1}=M_j-\lambda _{j+1}+\rho _{j+1}.                   \tag{1.4}
\]

The two banks are disjoint, so (1.3) is a shortest Johnson geodesic.
Its lower and upper transition colours are

\[
\begin{aligned}
 I_j&=B\cup\rho[1,j]\cup\lambda[j+2,h],\\
 U_j&=B\cup\rho[1,j+1]\cup\lambda[j+1,h],
                    \qquad 0\le j<h,                       \tag{1.5}
\end{aligned}
\]

and are separately injective.

Insertion is monotone because the union of the two adjacent old letters
contains `X`.  Every old interval not crossing the cut is unchanged; every
old crossing interval contains both adjacent old letters, so inserting `X`
does not change its OR.  Its physical width increases by one.

The new cells of width at most `h` outside the transported old-cell image
are exactly

\[
 X,\qquad
 P_i=B\cup\lambda[h-i+1,h],\qquad
 S_i=B\cup\rho[1,i],\quad 1\le i<h.                        \tag{1.6}
\]

The `h-1` old crossing width-`h` cells expelled from that band have values
`M_1,...,M_{h-1}` and rank `r`; hence a strict-lower reference matching
uses none of them.

There is also a load-bearing temporal fact.  Before insertion, the `h`
crossing depth-`h` cells (intervals of source length `h+1`) are

\[
              U_j=M_j\cup M_{j+1},\qquad 0\le j<h,          \tag{1.7}
\]

and have rank `r+1`.  After insertion they are replaced by the `h+1`
rank-`r` cells (1.3).  Therefore this pivot cannot be inserted into an
already-flat rank-`r` depth row.  Its preimage must be a jointly designed
nonflat scaffold.

The aperture inequality `|X|<=r-h` remains sharp, but equality does not by
itself imply geodesicity: a deleted coordinate can re-enter.  Disjointness
of `L` and `R`, not equality alone, proves the geodesic assertion above.

## 2. Exact endpoint-hull theorem

Let a fixed post-insertion source block be

\[
                  A_0,A_1,\ldots,A_{2h},                   \tag{2.1}
\]

and suppose its depth-`h` cells

\[
                  T_j=\bigcup_{i=j}^{j+h}A_i               \tag{2.2}
\]

have rank `r`.  Put

\[
 S_-:=\bigcup_{i=0}^{h-1}A_i,qquad
 S_+:=\bigcup_{i=h+1}^{2h}A_i.                             \tag{2.3}
\]

### Theorem 2.1 (one-letter seam criterion)

After adjoining a nonempty source letter `E_-` immediately on the left,
the new predecessor is exactly

\[
                         P_-=S_-\cup E_-.                   \tag{2.4}
\]

Consequently a prescribed set `P_-` is realizable iff

\[
 S_-\subseteq P_-
 \quad\text{and there is a nonempty }E_-\subseteq P_-
 \text{ with }S_-\cup E_-=P_-.                             \tag{2.5}
\]

If `E_-` is required to lie in a cap `K_-` and contain a mandatory set
`D_-`, this is equivalent to

\[
\begin{gathered}
 S_-\subseteq P_-,\qquad D_-\subseteq P_-,\\
 (P_-\setminus S_-)\cup D_-\subseteq K_-\cap P_-,          \tag{2.6}
\end{gathered}
\]

together with the existence of a nonempty choice between the lower and
upper sets in (2.6).  The right criterion is identical with `+` signs.

If `P_-` must be a distinct rank-`r` Johnson neighbour of `T_0`, then a
clean singleton-entry seam exists precisely when

\[
 |S_-|=r-1,qquad S_-=P_-\cap T_0,                          \tag{2.7}
\]

with the entering singleton equal to `P_-\setminus T_0`.  More generally,
assuming the ground set has a coordinate outside `T_0`, some distinct
rank-`r` Johnson predecessor exists iff `|S_-|<=r-1`: choose
`x in T_0-S_-`, `y notin T_0`, put `P_-=T_0-x+y`, and take an entering
letter containing `(T_0-S_-)-x+y`.  The capped version is still governed
by (2.6).

#### Proof

The predecessor window consists of `E_-` and the first `h` fixed source
letters, giving (2.4).  This proves (2.5).  Intersecting the allowed letter
with the cap and imposing its mandatory subset gives (2.6).  Two distinct
rank-`r` Johnson neighbours intersect in rank `r-1`; since `S_-` is in both
windows, (2.7) is necessary in the singleton-entry case and plainly
sufficient.  The right endpoint is symmetric.  \(\square\)

### Corollary 2.2 (the original collar is not physical)

For the symmetric source in Section 1,

\[
                   S_-=M_0,qquad S_+=M_h.                \tag{2.8}
\]

Indeed, the first `h` source letters already contain the whole left owner,
and the last `h` already contain the whole right owner.  Thus every
rank-`r` predecessor equals `M_0`, and every rank-`r` successor equals
`M_h`.  No choice of exterior source letter, cap, or longer exterior word
changes the immediate saturated overlap.

Hence the old formulas

\[
 L_0,\ldots,L_{h-1},M_0,\ldots,M_h,R_0,\ldots,R_{h-1}    \tag{2.9}
\]

define a correct abstract Johnson collar but not the depth-`h` row of the
displayed symmetric source.

## 3. A necessary two-sided pivot condition

Monotonicity requires

\[
                         X\subseteq A_{h-1}\cup A_{h+1}
                              \subseteq S_-\cup S_+.       \tag{3.1}
\]

If both endpoint owners have genuine apertures, then some pivot coordinate
must be absent from `S_-` and some pivot coordinate must be absent from
`S_+`.  By (3.1), these two coordinates occur on opposite sides.  In
particular, a singleton pivot cannot give two physical seams in this
monotone one-cell architecture.

This is only a necessity.  The following split construction proves it is
also the right design principle for the present geodesic.

## 4. Split-pivot physical collar

Assume here

\[
 r-h\ge2,\qquad 2\le |X|\le r-h,
 \qquad |\Omega|\ge r+3h,                                 \tag{4.0}
\]

where `Omega` is the ambient coordinate set.  These are exactly the
feasibility conditions needed to split `X` into two nonempty parts and to
choose all displayed fresh labels.

Partition

\[
 B=C\mathbin{\dot\cup}X_L\mathbin{\dot\cup}X_R,qquad
 X=X_L\mathbin{\dot\cup}X_R,                              \tag{4.1}
\]

where `X_L,X_R` are nonempty.  Choose

\[
                       x_L\in X_L,qquad x_R\in X_R,       \tag{4.2}
\]

and fresh coordinates `q^-`,`q^+`, fresh banks
`D^-=(d^-_1,...,d^-_{h-1})`, `D^+=(d^+_1,...,d^+_{h-1})`,
all disjoint from `B,L,R` and from one another.

Replace the two large adjacent old letters by

\[
 A^-:=C\cup X_L\cup\{\lambda_h\},qquad
 A^+:=C\cup X_R\cup\{\rho_1\},                            \tag{4.3}
\]

and insert the full letter `X` at their cut.  Thus the central source is

\[
 \{\lambda_1\},\ldots,\{\lambda_{h-1}\},A^-,X,A^+,
 \{\rho_2\},\ldots,\{\rho_h\}.                            \tag{4.4}
\]

### Theorem 4.1 (literal split-pivot packet)

The depth-`h` cells through `X` are still exactly (1.3).  The insertion
preserves every old interval OR, and the new strict-lower cells are still
exactly (1.6).

Define

\[
 B^-=(B-\{x_R\})\cup\{q^-\},\qquad
 B^+=(B-\{x_L\})\cup\{q^+\},                              \tag{4.5}
\]

and, for `0<=t<h`,

\[
\begin{aligned}
 L_t&=B^-\cup\lambda[1,t+1]\cup D^-[t+1,h-1],\\
 R_t&=B^+\cup\rho[t+1,h]\cup D^+[1,t].                    \tag{4.6}
\end{aligned}
\]

Then

\[
 L_0,\ldots,L_{h-1},M_0,\ldots,M_h,R_0,\ldots,R_{h-1}    \tag{4.7}
\]

is literally the depth-`h` row of a source word.  It is a simple rank-`r`
Johnson path with `3h` transitions, and its set-theoretic lower and upper
owner-transition colours are separately injective.  Literal realization of
the lower colours at the shared source addresses is characterized below.

#### Proof: central row and old-deck transport

The union of `A^-`, `X`, and `A^+` restores the whole core `B`.  Every
window through `X` therefore has value (1.3).  Every old interval crossing
the cut contains both `A^-` and `A^+`, whose union contains `B` and hence
`X`; monotone preservation follows.  The same calculation for intervals
ending or beginning at `X` gives the two rays (1.6).

#### Proof: source serialization

Adjoin on the left, from far to near,

\[
 \{d^-_1\},\ldots,\{d^-_{h-2}\},
 (C\cup X_L)\cup\{d^-_{h-1}\},
 (X_R-\{x_R\})\cup\{q^-\},                               \tag{4.8}
\]

and on the right, from near to far,

\[
 (X_L-\{x_L\})\cup\{q^+\},
 (C\cup X_R)\cup\{d^+_1\},
 \{d^+_2\},\ldots,\{d^+_{h-1}\}.                        \tag{4.9}
\]

Empty singleton lists are omitted when `h=2`.  The first window is
`B^-+lambda_1+D^-`; sliding right successively replaces
`d^-_{t+1}` by `lambda_{t+2}`.  The last left window is
`B^-+L=L_{h-1}`.  Its overlap with the central source is

\[
 S_-=C\cup X_L\cup L=M_0\setminus X_R,                   \tag{4.10}
\]

and the near letter in (4.8) restores `X_R-x_R` and adds `q^-`, producing
`L_{h-1}=M_0-x_R+q^-`.  The next window is `M_0`.  The right calculation is
symmetric:

\[
 S_+=C\cup X_R\cup R=M_h\setminus X_L,                   \tag{4.11}
\]

and (4.9) produces `R_0=M_h-x_L+q^+`, then the remaining `R_t`.
This proves literal source compatibility.

#### Proof: ranks, simplicity, and q1 palettes

Every owner in (4.7) consists of a core of size `r-h` and exactly `h`
fresh moving coordinates, so has rank `r`.  Internal left steps replace a
`d^-` by a `lambda`, the left seam replaces `q^-` by `x_R`, central steps
replace `lambda_{j+1}` by `rho_{j+1}`, the right seam replaces `x_L` by
`q^+`, and internal right steps replace a `rho` by a `d^+`.

On the four distinguished coordinates `x_L,x_R,q^-,q^+`, the lower-colour
signatures of the five edge classes are respectively

\[
 (x_L,q^-),\quad (x_L),\quad (x_L,x_R),\quad (x_R),
 \quad (x_R,q^+),                                         \tag{4.12}
\]

and the upper-colour signatures are

\[
 (x_L,q^-),\quad (x_L,x_R,q^-),\quad (x_L,x_R),
 \quad (x_L,x_R,q^+),\quad (x_R,q^+).                     \tag{4.13}
\]

Thus different classes cannot collide.  Within an internal class the
moving prefix/suffix index determines the edge; the two seams are unique.
This proves simplicity and both q1 injections.

### Physical lower-q1 ledger

For two consecutive depth-`h` owners `V_i,V_{i+1}`, let `J_i` be the OR of
their `h` shared source letters.  Always

\[
                       J_i\subseteq V_i\cap V_{i+1}.       \tag{4.14}
\]

Equality is the condition that the owner intersection itself occurs at the
native shared depth-`h-1` address.  In the split source, equality holds at
every transition except the following four (when a displayed missing set
is empty, that row becomes tight):

\[
\begin{array}{c|c|c}
\text{transition}&J_i&(V_i\cap V_{i+1})\setminus J_i\\ \hline
L_{h-2}\to L_{h-1}
 &(X_R-\{x_R\})\cup\{q^-\}\cup\lambda[1,h-1]
 &C\cup X_L\\
L_{h-1}\to M_0
 &C\cup X_L\cup\lambda[1,h]
 &X_R-\{x_R\}\\
M_h\to R_0
 &C\cup X_R\cup\rho[1,h]
 &X_L-\{x_L\}\\
R_0\to R_1
 &(X_L-\{x_L\})\cup\{q^+\}\cup\rho[2,h]
 &C\cup X_R.
\end{array}                                               \tag{4.15}
\]

The first and fourth deficits are always nonempty because `X_L,X_R` are
nonempty; the two seam deficits vanish when their opposite split shore is a
singleton.  Every upper colour `V_i union V_{i+1}` is literal: it is the OR
of the `h+2` source letters spanning the two owner windows.

Thus “both q1 palettes are injective” is an abstract Johnson/incidence
statement.  The literal source realizes the full upper palette locally but
does not realize four lower intersections at their native shared cells.
Those target values need protected additional occurrences (possibly at
nonnative local addresses), or a further source redesign.  Merely invoking
a common cap cannot turn the strict
subsets in (4.15) into the missing intersections.

### Theorem 4.2 (authoritative tight two-pivot-bit source)

The four deficits are not an invariant of the owner path.  Retain the
partition `X=X_L dotunion X_R` and choose the distinguished coordinates

\[
                         x_L\in X_L,\qquad x_R\in X_R.    \tag{4.16}
\]

Retain the owner definitions (1.3), (4.5), and (4.6), but replace the
four sparse letters exactly as follows:

\[
\begin{array}{rcl}
(X_R-\{x_R\})\cup\{q^-\}&\longmapsto&B^-,\\
(C\cup X_L)\cup\{\lambda_h\}&\longmapsto&
                  (B-\{x_R\})\cup\{\lambda_h\},\\
(C\cup X_R)\cup\{\rho_1\}&\longmapsto&
                  (B-\{x_L\})\cup\{\rho_1\},\\
(X_L-\{x_L\})\cup\{q^+\}&\longmapsto&B^+.
\end{array}                                               \tag{4.16a}
\]

Equivalently, replace the source serialization by the following
partition-retaining word.  The two outer core-bearing donor letters are
unchanged from the sparse source:

\[
\begin{array}{l}
 \{d^-_1\},\ldots,\{d^-_{h-2}\},
       (C\cup X_L)\cup\{d^-_{h-1}\}, B^-,\\
 \{\lambda_1\},\ldots,\{\lambda_{h-1}\},
       (B-\{x_R\})\cup\{\lambda_h\},\\
 X,\\
 (B-\{x_L\})\cup\{\rho_1\},
       \{\rho_2\},\ldots,\{\rho_h\},\\
 B^+,(C\cup X_R)\cup\{d^+_1\},
       \{d^+_2\},\ldots,\{d^+_{h-1}\}.
\end{array}                                               \tag{4.17}
\]

Then the depth-`h` row is again exactly (4.7), every shared depth-`h-1`
cell equals the corresponding owner intersection, and every spanning
depth-`h+1` cell equals the corresponding owner union.  Hence both q1
palettes are literal and injective.

#### Proof

Sliding across the left exterior bank gives

\[
 L_t=B^-\cup\lambda[1,t+1]\cup D^-[t+1,h-1],
\]

because the source letter `B^-` is present in every left owner window.
The left seam drops `B^-` and gains `X`, while the shared central letter
`(B-x_R)+lambda_h` retains every coordinate except the exchanged
`q^- -> x_R`.  The central calculation is (1.3).  The right side is
symmetric, with `x_L -> q^+`.  Thus the owner row is (4.7).

For a general source `a_0,a_1,...`, put

\[
 O_t=\bigcup_{j=t}^{t+h}a_j,qquad
 C_t=\bigcup_{j=t+1}^{t+h}a_j.                            \tag{4.18}
\]

Distributivity gives the exact identity

\[
 O_t\cap O_{t+1}
   =C_t\cup(a_t\cap a_{t+h+1}).                           \tag{4.19}
\]

Hence the shared cell is tight iff
`a_t intersect a_(t+h+1) subseteq C_t`.  In (4.17), internal collar
steps are immediate because the full letters `B^-` or `B^+` lie in the
shared block.  At the left seam,

\[
 B^-\cap X=X-\{x_R\}\subseteq B-\{x_R\}\subseteq C_t,
\]

and the right seam is symmetric.  Central steps contain `X` in their
shared block.  Thus (4.19) is tight at all `3h` transitions.  The union of
two adjacent owner windows is tautologically the OR of their `h+2`
spanning source letters, proving literal upper q1.

Before insertion, the adjacent large letters in (4.17) have union `B`
plus their moving labels because `x_L != x_R`.  Therefore they contain
`X`; every old interval OR transports literally.  Inserting `X` again
exposes exactly the cells (1.6), and the old crossing depth-`h` cells are
the rank-`r+1` values (1.7).  All owner, palette, residence, support, and
incidence counts are unchanged.

The word (4.17) is itself a simultaneous local common-source witness.  Its
full-core letters `B^-,B^+,(B-x_R)+lambda_h,(B-x_L)+rho_1` must still be
admitted by every ambient cap and mixed exterior row.  Also

\[
 P_{h-1}=I_0,\qquad S_{h-1}=I_{h-1}.                     \tag{4.20}
\]

These are identities of physical interval addresses, not merely equal
target values: the longest left ray is the native shared cell of
`M_0,M_1`, and the longest right ray is the native shared cell of
`M_(h-1),M_h`.  Thus one cell serves both roles.  A ledger must identify
the obligations rather than charge two target or cell capacities.

For `h=2`, (4.17) is the nine-letter word

\[
 (C\cup X_L)+d^-_1,B^-,\{\lambda_1\},
 (B-\{x_R\})+\lambda_2,X,
 (B-\{x_L\})+\rho_1,\{\rho_2\},B^+,
 (C\cup X_R)+d^+_1.                                     \tag{4.20a}
\]

Its seven length-three unions are exactly
`L_0,L_1,M_0,M_1,M_2,R_0,R_1`, and its six shared length-two unions are
their exact intersections.  Removing `X` gives
`L_0,L_1,U_0,U_1,R_0,R_1`.  The only insertion-born cells of at most two
letters are `X`, `B+lambda_2`, and `B+rho_1`, exactly the specialization of
(1.6).  Thus no edge-case cell or guard is hidden at `h=2`.

Relative to the sparse source, (4.17) enlarges four **existing** letters;
relative to its own pre-insertion word, it adds only `X`.  Consequently it
creates no extra short-cell class beyond (1.6), but every ambient guard on
those four enlarged positions must be rechecked.  Their legality does not
follow merely from the unchanged owner row.  More precisely, at each fixed
source length `1<=q<=h`, generically exactly four interval addresses change
value (an empty opposite-shore addition can reduce this number), and no
interval of source length at least `h+1` changes.  Thus unchanged owner and
q1 rows do not transport shorter matching, equality, deadline, or guard
rows from the sparse word.

The transparency assertion has the exact direction

\[
 \operatorname{Deck}(A^{\rm tight}_{\rm pre})
    \subseteq
 \operatorname{Deck}(A^{\rm tight}_{\rm post})             \tag{4.20b}
\]

under the monotone occurrence map.  No containment between the sparse and
tight source decks is claimed.  Indeed the sparse near-left singleton cell
`(X_R-x_R)+q^-` is replaced by `B^-` and gains the nonempty set
`C union X_L`; analogous changes occur at the other three enriched
positions and can alter pre-existing shorter interval values.  Therefore
all transport, matching, and guard claims for Theorem 4.2 compare its own
enriched pre/post pair only.

### Residence and label ledger

Every `lambda_j` and `rho_j` has one consecutive positive owner run of
length exactly `h+1`.  Every coordinate in `B-{x_L,x_R}` persists
throughout (4.7).  Coordinate `x_L` occurs in the left and central blocks,
while `x_R` occurs in the central and right blocks; each has a positive run
of length `2h+1`.

All shorter positive runs or zero-gaps are clipped at a path endpoint:
these include the `q^-`,`D^-` positive runs on the left, the
`q^+`,`D^+` positive runs on the right, the short initial zero-gaps of some
`lambda_j` and of `x_R`, and the short final zero-gaps of some `rho_j` and
of `x_L`.  Hence the packet has no short run or gap wholly internal to the
displayed path.  For an abstract owner-path embedding the clipped flags
remain boundary obligations.  For a literal source embedding, every source
occurrence automatically supports a length-`h+1` interval of depth-`h`
windows, so the exterior crossing windows continue them without a separate
run choice; those windows must still be legal owners satisfying all guards.
The total labelled support is

\[
 |B|+|L|+|R|+|D^-|+|D^+|+2=r+3h.                          \tag{4.21}
\]

Both constructions are explicit common source words for their actual local
OR rows.  For the sparse proposed source (4.4), zero residual compilation
requires additional hosts for every nonempty deficit in (4.15).  The tight
source (4.17) removes those four hosts.  In either case one must release the
actual old target occurrences assigned to the two rays and the one-letter
cell with value `X`, admit every displayed letter under the ambient caps,
and replay all mixed exterior rows.  Local source existence is not a global
common-cap theorem.

Each full post-insertion source, the sparse serialization (4.8)--(4.9) or
the tight serialization (4.17), has `4h+1` letters and hence `3h+1`
depth-`h` cells, all the owners in (4.7).  Deleting `X` leaves
`4h` source letters and `3h` depth cells: the `2h` left/right collar owners
transport unchanged, while the central `h+1` owners are replaced by the
`h` rank-`r+1` cells (1.7).  Thus even the repaired literal collar has an
intrinsically nonflat pre-insertion row.

## 5. Fixed-`H` planting: exact scope

Specialize to the odd middle-levels incidence host `ML_m` with owner rank
`r=m`.  The path (4.7) has `3h` Johnson transitions.  Subdividing each
through its rank-`m-1` intersection gives exactly `6h` incidence edges.

For `H` copies whose owner and lower-colour incidence vertices are pairwise
disjoint, their union has maximum degree at most two and `6Hh` edges.  The
small protected-factor theorem therefore embeds all these incidence edges
in a spanning two-factor whenever

\[
                             6Hh\le m-2.                   \tag{5.1}
\]

If `b` additional boundary incidence edges are also protected, the exact
hypothesis is `6Hh+b<=m-2`; those edges cannot be hidden in the packet
count.

There is no hidden coordinate shortage in the pure packet bank.  Share one
base `B` of size `m-h` and give the `H` copies pairwise disjoint
`L,R,q^\pm,D^\pm` labels.  This uses

\[
                         (m-h)+4Hh=m+(4H-1)h             \tag{5.1a}
\]

coordinates, which is at most `2m-1` under (5.1).  This explicit face also
makes the owner, lower, and upper resources of different copies distinct.
It still does not place their literal source histories in one global word.

This protects the owner path and its lower q1 colours as set-valued
incidence edges.  If the global source actually contains the tight local
word (4.17), all those lower edges are already literal locally; if one uses
the sparse source (4.4), the four rows (4.15) remain separate compiler
obligations.  Abstract factor containment alone places neither source
history.  It also does **not** protect upper colours against collisions with
the completion.  Even local
upper injectivity across several packets requires their upper resources to
be disjoint.  The theorem supplies neither orientation, global residence,
component control, upper surjectivity, nor a common source cap.

There is a separate sharp upper-tail Hall statement.  Once a perfect
matching `F` contains one protected parity and the other parity determines
`3Hh` distinct upper-colour/root-tail tickets, those tickets extend to an
upper-exact rooted-tail semimatching whenever

\[
                              3Hh\le m.                    \tag{5.2}
\]

Condition (5.1) implies this numerical inequality.  The extension may
still repeat its opposite heads and its rooted links may branch or cycle;
it is not the matching/tree object of Section 6.  Thus the protected lower
factor and the protected upper-tail extension close two different marginal
rows, not their correlation.

Most importantly, (5.1) is a two-factor extension theorem.  It does not
imply the near-perfect matching/tree certificate in the next section.

## 6. The exact `B+1` owner target

Let `ML_m` have shores

\[
 {\cal L}={[2m-1]\choose m-1},\qquad
 {\cal M}={[2m-1]\choose m},qquad |{\cal L}|=|{\cal M}|=W. \tag{6.1}
\]

Fix a perfect matching `F`.  If `e=LV` is an incidence edge outside `F`,
let `lambda_F(e)` join the two contracted `F`-vertices containing `L` and
`V`, and put

\[
                         \operatorname{up}(e)=F(L)\cup V.  \tag{6.2}
\]

### Theorem 6.1 (upper-surjective Hamilton-path certificate)

For a matching `Q subseteq ML_m-F`, the following are equivalent.

1. `|Q|=W-1`, `lambda_F(Q)` is acyclic, and the values
   `operatorname{up}(Q)` cover every rank-`m+1` set.
2. `F union Q` is a spanning alternating Hamilton path, and its internal
   lower-shore turns cover every rank-`m+1` upper colour.

#### Proof

Contract `F`.  The graph `lambda_F(Q)` has `W` vertices and `W-1` edges.
Because `Q` is a matching, its maximum degree is two.  If it is acyclic it
is a spanning tree, hence a path.  Undoing the contractions gives the
alternating Hamilton path.  A turn at `L` has owner neighbours `F(L)` and
`V`, so its union is (6.2).  The converse follows by contracting the fixed
parity of an alternating Hamilton path.  \(\square\)

Put

\[
 U={[2m-1]\choose m+1},\qquad C=W-U=\operatorname{Cat}_m. \tag{6.3}
\]

Choosing one edge of `Q` for each upper colour gives an exact decomposition

\[
 Q=Q_0\mathbin{\dot\cup}Q_1,qquad |Q_0|=U,qquad |Q_1|=C-1. \tag{6.4}
\]

The link graph of `Q_0` is a forest with exactly `C` components, and `Q_1`
is a tree after those components are contracted.  Conversely, compatible
matchings `Q_0,Q_1` with these properties give Theorem 6.1.  There is no
third residual matching, Hall completion, or closure edge.  Compatibility
of the two matchings and the contracted tree remains the integral gate.

A protected pivot packet can be imposed only if one parity of its incidence
path is contained in `F` and the other in `Q_0 union Q_1`, with all forced
upper turns compatible.  The fixed-`H` two-factor result in Section 5 does
not prove this stronger extension.

## 7. The original saturated pivot as a terminal `B+1` socket

Although Corollary 2.2 forbids an internal seam, one saturated seam can be
priced by the unique surplus depth cell at `B+1`.

For the original symmetric block, append on the right a letter
`E_0 subseteq M_h`.  The next depth-`h` cell is another copy of `M_h`.
Write

\[
                       K_+=\{\rho_2,\ldots,\rho_h\}.       \tag{7.1}
\]

After appending one further letter `E_1`, the following depth cell is

\[
                       N=K_+\cup E_0\cup E_1.             \tag{7.2}
\]

### Theorem 7.1 (one-duplicate escape)

Let

\[
                       N=M_h-x+y                           \tag{7.3}
\]

be a desired rank-`r` Johnson neighbour, with `y notin M_h`.  The terminal
socket can realize

\[
                 \ldots,M_h,M_h,N                          \tag{7.4}
\]

by two appended source letters iff

\[
                       x\notin K_+.                         \tag{7.5}
\]

In the present construction this means

\[
                       x\in B\cup\{\rho_1\}.               \tag{7.6}
\]

When (7.5) holds, take

\[
                       E_0=M_h-\{x\},\qquad E_1=\{y\}.     \tag{7.7}
\]

#### Proof

Every cell in (7.2) contains `K_+`, so deleting a member of `K_+` is
impossible.  Conversely, if `x notin K_+`, (7.7) gives first the duplicate
`M_h`, and then exactly `M_h-x+y`.  \(\square\)

Place `M_0` at the global left endpoint and use (7.4) on the right.  After
contracting the single equality in (7.4), the selected distinct owner row
can begin

\[
                       M_0,M_1,\ldots,M_h,N,\ldots.         \tag{7.8}
\]

Thus a sufficient `B+1` owner certificate is a Hamilton path from Theorem
6.1 containing this prescribed terminal segment and a port-compatible edge
satisfying (7.6).  This is only an owner-layer statement; the duplicate's
lower/compiler rows and all ambient cap equations still require literal
replay.

There is a symmetric left terminal socket.  A one-sided split pivot can
instead place its saturated side at the global boundary and use its open
side as the direct seam.  A singleton `X` cannot have two open seams, but is
therefore not excluded from a `B+1` terminal architecture.

## 8. Exact `B+1` cell ledger

Assume the source length `B_0+1` is such that its depth-`h` row has `W+1`
cells.  A valid owner projection selects `W` distinct rank-`r` owner
occurrences forming the path of Theorem 6.1 and leaves one controlled
surplus cell.  The surplus may be a duplicate rank-`r` value as in (7.4);
“nonowner” means unselected in the owner projection, not necessarily of
nonmiddle rank.

If the terminal pivot supplies `h+1` selected owners, the post-insertion row
has the exact form

\[
 \underbrace{W-h-1}_{\text{retained selected owners}}
 +\underbrace{h+1}_{M_0,\ldots,M_h}
 +\underbrace{1}_{\text{surplus}}=W+1.                    \tag{8.1}
\]

Before insertion the depth row has `W` cells:

\[
 \underbrace{W-h-1}_{\text{retained selected owners}}
 +\underbrace{h}_{U_0,\ldots,U_{h-1}\text{ of rank }r+1}
 +\underbrace{1}_{\text{surplus}}=W.                      \tag{8.2}
\]

Equations (8.1)--(8.2) are the exact reason an already-flat length-`B_0`
factor cannot be the pivot preimage.  The preimage must be nonflat, while
the final row has `W` selected owners plus one controlled surplus.

If the **full split collar** of Section 4 is planted instead, the exact
ledger is

\[
\begin{aligned}
\text{post: }&(W-3h-1)\text{ outside selected owners}
 +(3h+1)\text{ packet owners}+1\text{ surplus}=W+1,\\
\text{pre: }&(W-3h-1)\text{ outside selected owners}
 +2h\text{ collar owners}+h\text{ rank-}(r+1)\text{ cells}
 +1\text{ surplus}=W.
\end{aligned}                                             \tag{8.3}
\]

This requires `W>=3h+1`.  The surplus must lie at a boundary or have an
explicit equality-collapse/rethread certificate; an uncontrolled internal
nonowner would interrupt the owner Hamilton path.

## 9. Sharp remaining hypotheses

The corrected local packet is unconditional.  A dimension-uniform `B+1`
construction would still need all of the following in one object:

1. an upper-surjective Hamilton-path certificate `F,Q_0,Q_1` of Section 6
   containing either the split-pivot protected incidence path or the
   terminal socket of Section 7;
2. a jointly designed nonflat pre-insertion scaffold satisfying (8.2) for
   the terminal socket or (8.3) for the full collar;
3. continuation or global-boundary placement of every clipped residence
   flag;
4. preservation/regeneration of all higher upper shadows; and
5. one literal common-cap lower compiler, including the pivot rays, the
   one-letter `X` cell, the full-core letters of (4.17) (or, for the sparse
   source, all nonempty deficits in (4.15)), the surplus cell, and every
   mixed exterior row.

The fixed-`H` theorem proves none of items 1--5 beyond embedding the
abstract owner/lower-q1 incidence bank in some two-factor.  No exact
`B+1` or all-`k` bound is claimed here.

## 10. Adversarial audit

The following possible shortcuts were checked and rejected.

* **Aperture is not geodesicity.**  Equality `|X|=r-h` gives one deletion
  and one insertion per step, but a deleted coordinate may re-enter.
* **An abstract owner collar is not a source collar.**  The endpoint hulls
  (2.3), not merely Johnson adjacency of the desired owners, decide literal
  realizability.  The symmetric source fails with hull rank `r` on both
  sides.
* **The split hull need not have rank `r-1`.**  In (4.10) its rank is
  `r-|X_R|`, and analogously on the right.  The multi-coordinate near
  letters in (4.8)--(4.9) restore every missing pivot coordinate except the
  one exchanged at the Johnson seam.  The proof therefore remains valid
  for arbitrary nonempty `X_L,X_R`, not only singleton parts.
* **The `h=2` boundary case is literal.**  The singleton lists in
  (4.8)--(4.9) are empty, leaving exactly two exterior letters per side;
  all displayed windows and signatures remain valid.  The tight variant is
  the explicit nine-letter word (4.20a), whose seven owner and six lower
  cells replay exactly.
* **Residence is clipped.**  Positive central runs have the claimed
  lengths, but short endpoint zero-gaps and the `D^\pm,q^\pm` runs require
  exterior continuation or global-boundary placement.
* **Fixed-`H` planting is marginal.**  The edge count proves a lower-q1
  two-factor, and the separate Hall theorem proves an upper/root-tail
  semimatching.  The tight word (4.17) closes its four local source-address
  deficits, but abstract factor containment does not embed that source word
  or its exterior history.  Neither marginal theorem proves the common
  head/tree/source realization.
* **The `B+1` surplus is an occurrence, not necessarily a new value.**  In
  Section 7 it is a duplicate rank-`r` cell.  Collapsing that equality is
  valid only for the owner projection; every physical lower, upper,
  residence, and cap row still sees the cell and must be replayed.
* **Immediate upper q1 is not the full upper tower.**  No statement here
  preserves all wider interval-union witnesses.

These checks leave the split-pivot packet theorem unconditional and isolate
the exact global correlation gates in Section 9.
