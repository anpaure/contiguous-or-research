# A basis-changing folded-C8 socket removes the owner plateau at zero length charge

Date: 2026-08-01  
Lane: K, quotient-folded C8 physical comparator  
Status: unconditional local owner/common-cap/ungraded-ray theorem for every
`d>=2`, with exact ungraded and width-graded exterior-return ledgers.  It
does not prove a complete matching-closed ambient braid or transport to
every terminal adjacent pair.

## 0. Result and corrected boundary

The antitone-birail theorem closes the abstract Hall row of the folded C8:
the two threshold marginals are

\[
             \{0^{d-1},1,\ldots,d-1\},
\]

so the optimum corner deficiency is zero.  The literal two-host word still
does not give a physical comparator.  Its two consecutive depth-`d` owners
are the same set.

This note proves two sharper statements.

1. The duplicate is forced for every **overlap-coherent** realization: if
   the two extreme ray witnesses lie in the common `d`-position overlap of
   two rank-`r` owner windows, both owners coincide.
2. The obstruction can be escaped at the same source length.  One extreme
   ray is moved across a neutral separator, and one fresh basis coordinate
   replaces the omitted terminal filler.  The resulting two owners form a
   strict Johnson edge, are phase independent, and admit one pointwise
   common cap.  After forgetting interval width, its phase-exclusive support
   is exactly the two folded rays, with a literal diagonal ray SDR.

The new packet is a genuine local owner-legal comparator state.  Relative
to the canonical two-host reference word, however, it deletes two
phase-common chains of total size `2d-2` at the ungraded target level.  At
the width-graded level the exact loss is `3d` distinct target-width rows,
or `3d+1` units with multiplicity.  A same-length ambient use is
matching-closed exactly when the appropriate complete return bank, the cut
colours, and the owner edge have disjoint exterior returns in the same cap
state.  This exterior return and transport to arbitrary terminal
obligations are the remaining gates.  No `B(k)+O(1)` conclusion is claimed.

This result is complementary to the authenticated common-cut theorem in
`MATH_THEOREM_R_FOLDED_C8_SINGLE_CUT_BOUNDARY_RAIL_CLOSURE_AND_EXACT_GATES_20260801.md`.
That theorem makes the original folded-source plus opposite two-host word
graded/context exact on the audited range `2<=d<=12`, but leaves its host
owner legality open.  The packet below fixes the two-owner row for every
`d`, but does **not** inherit that graded identity: Theorem 4.3 is the exact
price of the substitution.  Thus the two positive halves cannot yet be
silently combined.

## 1. Folded rays and the plateau

Let the fixed core `K` be disjoint from

\[
             \{z,a_1,a_3,f_1,\ldots,f_d\}.
\]

Write `F[i,j]={f_i,...,f_j}` and define, in phase `epsilon`,

\[
 (\lambda_0,\rho_0)=(a_3,a_1),\qquad
 (\lambda_1,\rho_1)=(a_1,a_3),                         \tag{1.1}
\]

\[
 L_\epsilon=K\cup\{z,\lambda_\epsilon,f_1\},\qquad
 R_\epsilon=K\cup\{z,\rho_\epsilon,f_d\}.           \tag{1.2}
\]

The two directed ray families are

\[
 \mathcal P_\epsilon=
 \{K\cup\{z,\lambda_\epsilon\}\cup F[1,j]:1\le j<d\},
                                                               \tag{1.3}
\]

\[
 \mathcal S_\epsilon=
 \{K\cup\{z,\rho_\epsilon\}\cup F[j,d]:2\le j\le d\}.
                                                               \tag{1.4}
\]

Put

\[
 U=K\cup\{z,a_1,a_3\}\cup F[1,d],\qquad r=|U|.       \tag{1.5}
\]

The canonical two-host word is

\[
 G_\epsilon=(X_L,L_\epsilon,f_2,\ldots,f_{d-1},
                    R_\epsilon,X_R),                   \tag{1.6}
\]

where

\[
 X_L=K\cup\{z,a_1,a_3,f_1\},\qquad
 X_R=K\cup\{z,a_1,a_3,f_d\}.                          \tag{1.7}
\]

### Proposition 1.1 (literal owner plateau)

The two length-`d+1` windows of (1.6) both have value `U`.

#### Proof

The common `d`-position overlap

\[
                L_\epsilon,f_2,\ldots,f_{d-1},R_\epsilon
\]

already has union `U`: its two endpoint letters contain opposite active
labels and the two terminal fillers, while the intervening letters supply
the remaining fillers.  Both far hosts are subsets of `U`.  Adding either
one therefore leaves the union equal to `U`.  \(\square\)

Thus the isolated host word has an owner occurrence twice at the same
rank-`r` value.  It is not a strict Johnson edge.

### Proposition 1.2 (overlap-coherent no-go)

Let `P=P_(d-1)` and `S=S_2` be the maximal members of (1.3)--(1.4), so

\[
                         P\cup S=U.                    \tag{1.8}
\]

Suppose chosen occurrences of both `P` and `S` lie inside the common
`d`-position overlap of two consecutive owner windows `O_0,O_1`.  If both
owners have rank `r`, then

\[
                         O_0=O_1=U.                    \tag{1.9}
\]

#### Proof

Both owner windows contain both selected ray intervals, hence contain
`P union S=U`.  Since they and `U` all have cardinality `r`, equality is
forced.  \(\square\)

The hypotheses are load-bearing.  The statement is not true at rank
`r+1`, and it is not true after one extreme ray is rehosted outside the
common overlap.  Consequently every strict rank-`r` escape needs both an
extreme-ray rehosting and a basis coordinate outside `U`.

## 2. The same-length basis-changing packet

Choose a fresh coordinate `g` outside `U`, an index
`1<=s<=d-1`, and a nonempty neutral set

\[
                         \varnothing\ne C\subseteq K\cup\{z\}.
                                                               \tag{2.1}
\]

Set

\[
                         M=K\cup\{a_1,a_3,g\}.          \tag{2.2}
\]

Define the phase word

\[
 Q_\epsilon=(M,L_\epsilon,f_2,\ldots,f_s,C,
                    f_{s+1},\ldots,f_{d-1},R_\epsilon). \tag{2.3}
\]

Empty filler ranges in (2.3) are omitted.  In particular the construction
is valid at `d=2`.  Its length is exactly

\[
                         |Q_\epsilon|=d+2=|G_\epsilon|. \tag{2.4}
\]

### Proposition 2.0 (minimality in the ordered-ray class)

Assume that the filler order and the two literal extreme-ray witnesses are
retained, only `L_epsilon,R_epsilon` carry phase-dependent active labels,
and any fresh basis coordinate is excluded from every selected ray
interval.  Then a strict rank-`r` two-owner realization needs at least one
neutral separator in the ray hull and at least one fresh exterior basis
coordinate.  At the minimum span and length these data have exactly the
form (2.1)--(2.3), up to left/right reflection and addition of already
present core coordinates.

#### Proof

Without the separator, the two extreme witnesses lie in a `d`-position
overlap, so Proposition 1.2 forces the plateau.  At the minimum escape the
witness hull has span `d+1`; its one extra position must add no coordinate
to either ray crossing it.  At a gap after `f_s` this is exactly

\[
 C\subseteq
 \bigcap_{\epsilon=0}^1
   (P_\epsilon(s)\cap S_\epsilon(s+1))=K\cup\{z\}.     \tag{2.4a}
\]

The partial first-owner hull then contains `U-{rho_epsilon,f_d}`.
Phase-independent ownership forces the exterior marker to supply both
`a_1,a_3`.  To reach rank `r` it has one remaining basis slot.  Filling it
with `f_d` recreates `U,U`; filling it with one fresh `g` gives (2.5), and
two fresh coordinates create a rank ridge.  This proves the scoped
minimality.  \(\square\)

### Theorem 2.1 (owner-legal common-cap lift)

For both phases, the two depth-`d` owner windows of (2.3) are

\[
                 V=(U-\{f_d\})\cup\{g\},\qquad U.      \tag{2.5}
\]

They are distinct rank-`r` Johnson neighbours.  Their lower and upper edge
colours are respectively

\[
                         V\cap U=U-\{f_d\},\qquad
                         V\cup U=U\cup\{g\}.            \tag{2.6}
\]

Moreover both phase words lie in one exact maximal-envelope cap state.
The envelopes at their `d+2` source positions are

\[
             V,\ \underbrace{U-\{f_d\},\ldots,
                              U-\{f_d\}}_{d\text{ positions}},\ U.
                                                               \tag{2.7}
\]

#### Proof

The first owner omits the last letter `R_epsilon`.  The marker supplies
both active labels and `g`, while `L_epsilon`, the filler rail, and `C`
supply `z` and `F[1,d-1]`; this gives `V`.  The second owner omits `M` and
contains `L_epsilon` and `R_epsilon`, hence it has both active labels and
all of `F[1,d]`, giving `U`.  Equation (2.6) follows immediately.

For a two-owner depth-`d` path, source position zero belongs only to `V`,
positions `1,...,d` belong to both owners, and position `d+1` belongs only
to `U`.  This gives (2.7).  The phase union of the two possible
`L_epsilon` letters and of the two possible `R_epsilon` letters is contained
in the corresponding envelope, as are `M`, `C`, and every filler singleton.
Finally direct union of either phase word on the two owner windows gives
exactly (2.5), so the cap is attained rather than merely containing the
word.  \(\square\)

The owner socket is therefore typed: an ambient ledger must have a spare
occurrence of `U` and a demand for `V`, or must deliberately replace the
canonical duplicate `U,U` by `V,U`.  The associated lower/upper palette
socket is the pair in (2.6).

## 3. Exact all-depth ray action and local matching

### Theorem 3.1 (nothing but the two rays changes in support)

Let `Supp(Q_epsilon)` denote the set of OR values of all nonempty intervals
of `Q_epsilon`, with widths forgotten but physical interval occurrences
retained separately for matching.  Then

\[
 \operatorname{Supp}(Q_0)-\operatorname{Supp}(Q_1)
       =\mathcal P_0\mathbin{\dot\cup}\mathcal S_0,    \tag{3.1}
\]

\[
 \operatorname{Supp}(Q_1)-\operatorname{Supp}(Q_0)
       =\mathcal P_1\mathbin{\dot\cup}\mathcal S_1.    \tag{3.2}
\]

Every ray target has a distinct literal cell.  Hence each phase has a
diagonal matching of size `2d-2`, and the two phase words have a pointwise
common source cap.

In each directed graded-occurrence difference exactly two ray values have
excess multiplicity two: `P_s` and `S_(s+1)`.  Every other ray value has
excess multiplicity one.  Thus each directed occurrence difference has
total mass `2d`, not `2d-2`.

#### Proof

An interval is phase sensitive only if it contains exactly one of
`L_epsilon,R_epsilon`.  If it contains `M` and `L_epsilon`, the two active
labels already occur in their union, so it is phase common.  If it contains
both `L_epsilon` and `R_epsilon`, the same is true.  Therefore a
phase-sensitive interval containing `L_epsilon` must begin there and stop
before `R_epsilon`; its value is exactly a member of `P_epsilon`.
Similarly, a phase-sensitive interval containing `R_epsilon` must start
after `L_epsilon` and end there; its value is exactly a member of
`S_epsilon`.  This proves (3.1)--(3.2).

Choose for `P_j` the interval from `L_epsilon` through `f_j`, crossing `C`
when `j>s`.  Choose for `S_j` the interval from `f_j` through
`R_epsilon`, crossing `C` when `j<=s`.  These `2d-2` physical intervals
are pairwise distinct and have pairwise-distinct values.  The positionwise
unions of the two phase words give a common cap.

Because `C` adds no coordinate not already supplied by either ray endpoint,
`P_s` occurs both before and after adjoining `C`; dually `S_(s+1)` occurs
both with and without `C`.  No other interval can be duplicated in this
way.  This proves the multiplicity assertion.  \(\square\)

Thus the local common-Q and ray-Hall parts are closed.  The packet is
phase returning: switching phase does not alter its owner path, owner
envelopes, cap word, or typed edge colours.  This is the precise local sense
in which its length charge can be recycled.

## 4. Exact exterior-return ledger

For general `s`, compare `Q_epsilon` with `G_epsilon`.  Besides the two
host chains below, the exact ungraded loss consists of the pure filler
intervals

\[
       \{F[p,q]:2\le p\le s<q\le d-1\}.              \tag{4.0}
\]

Indeed these and only these old filler intervals cross the inserted neutral
cell, whose coordinate `z` is not in a pure filler target.  Hence the exact
ungraded loss count is

\[
              2d-2+(s-1)(d-1-s).                    \tag{4.0a}
\]

The same interval classification gives, before specializing,

\[
 \#\text{ lost target-width rows}
       =3d+(s-1)(d-1-s),                              \tag{4.0b}
\]

and one additional unit under exact multiplicity.  Thus the two endpoint
gaps are simultaneously optimal in the ungraded, graded-support, and
graded-multiplicity ledgers.

Choose `s=1` and `C={z}` from now on.  Compare `Q_epsilon` with the
canonical reference `G_epsilon` from (1.6), and define

\[
 \mathcal C_L=
 \{K\cup\{z,a_1,a_3\}\cup F[1,j]:1\le j<d\},         \tag{4.1}
\]

\[
 \mathcal C_R=
 \{K\cup\{z,a_1,a_3\}\cup F[j,d]:2\le j\le d\}.     \tag{4.2}
\]

### Theorem 4.1 (two-chain loss is exact)

In either phase,

\[
 \operatorname{Supp}(G_\epsilon)-\operatorname{Supp}(Q_\epsilon)
                     =\mathcal C_L\mathbin{\dot\cup}\mathcal C_R.
                                                               \tag{4.3}
\]

There are exactly `2d-2` lost common values.  The new common values are
exactly

\[
 \{M\}\ \cup\
 \{K\cup\{z,a_1,a_3,g\}\cup F[1,j]:1\le j\le d\}    \tag{4.4}
\]

together with

\[
 \{\{z\}\cup F[2,j]:1\le j<d\},                     \tag{4.5}
\]

where `F[2,1]` is empty.  The gain has `2d` distinct values.

#### Proof

Every interval internal to
`L_epsilon,f_2,...,f_(d-1),R_epsilon` transports across the neutral
insertion because `C={z}` adds nothing beyond the two endpoint letters.
The only old intervals which use a far host without spanning both active
endpoint letters are the left and right chains (4.1)--(4.2).  Any proposed
replacement using `M` contains the forbidden fresh coordinate `g`, while
an interval avoiding `M` cannot realize either missing full active-label
chain.  This proves (4.3).

Intervals newly using `M` give its singleton value and the `g`-chain
(4.4).  Intervals newly beginning at `C` and ending before the
phase-specific right endpoint give (4.5).  All remaining new intervals
either transport an old value or are one of the phase-exclusive rays in
Section 3.  \(\square\)

The common gains cannot cover the losses by equality: every member of
(4.4) contains `g`, while every member of (4.5) omits both active labels.
Therefore a literal same-length substitution needs an exterior occurrence
matching for (4.1)--(4.2).  Cardinality alone is insufficient.

### Corollary 4.2 (matching-closed return criterion)

Fix all retained ambient target-cell assignments and delete those using the
two far-host chains of `G_epsilon`.  Let `H_ext` be the bipartite graph from
`C_L union C_R` to unused exterior physical cells whose literal OR values
equal the target and whose source caps are compatible with the common cap
(2.7).  Then the basis-changing substitution is matching-closed on these
rows if and only if

\[
       |N_{H_{\rm ext}}(A)|\ge |A|
       \quad\text{for every }A\subseteq\mathcal C_L\cup\mathcal C_R.
                                                               \tag{4.6}
\]

Equivalently, `H_ext` has a matching saturating both chains.  This matching
must also avoid the `2d-2` fixed ray cells and the cut-colour cells.  The
criterion is ordinary Hall because Theorem 3.1 has already fixed a
pairwise-disjoint diagonal basis for the ray rows.

The antitone-birail theorem does not by itself prove (4.6): it optimizes the
two ray marginals after eligible cells exist, whereas (4.6) asks for literal
external occurrences of two phase-common chains.

### Theorem 4.3 (the exact width-graded return is larger)

Write

\[
 H_L(j)=K\cup\{z,a_1,a_3\}\cup F[1,j],\qquad
 H_R(j)=K\cup\{z,a_1,a_3\}\cup F[j,d].                \tag{4.7}
\]

For `s=1`, the target-width support lost from `G_epsilon` but absent from
`Q_epsilon` consists of exactly the following `3d` rows:

\[
\begin{aligned}
 \mathcal H_L^{\rm gr}={}&
   \{(1,H_L(1)),(2,H_L(1))\}
   \cup\{(j+1,H_L(j)):2\le j<d\},\\
 \mathcal H_R^{\rm gr}={}&
   \{(1,H_R(d)),(2,H_R(d))\}
   \cup\{(d-j+2,H_R(j)):2\le j<d\},\\
 \mathcal P_{\epsilon}^{\rm shift}={}&
   \{(j,P_\epsilon(j)):2\le j<d\},\\
 \mathcal U^{\rm gr}={}&\{(d,U),(d+2,U)\}.
                                                               \tag{4.8}
\end{aligned}
\]

The first two lines have `d` rows each, the third has `d-2`, and the last
has two.  If exact occurrence multiplicity is protected, there is one
additional unit demand at `(d+1,U)`: the canonical word has two such
occurrences and the basis-changing packet has one.  Consequently the exact
graded return floor is

\[
              3d\quad\text{for support},\qquad
              3d+1\quad\text{with multiplicity}.       \tag{4.9}
\]

#### Proof

In the canonical word, `H_L(1)` occurs at widths one and two, while
`H_L(j)` for `j>=2` occurs at width `j+1`; this gives `d` rows.  The
reflected calculation gives the `d` right-host rows.  In the packet with
`s=1`, `P_epsilon(j)` moves from width `j` to width `j+1` for
`2<=j<d`, while the suffix-ray old widths remain available.  Finally the
canonical full union `U` occurs at widths `d,d+1,d+1,d+2`, whereas the new
packet retains one occurrence at width `d+1`.  These classes are disjoint
and exhaust the interval classification in the proof of Theorem 4.1.  This
proves (4.8)--(4.9).  \(\square\)

Thus (4.6) is sufficient only for width-forgotten target coverage.  A
graded shadow braid needs a typed exterior matching saturating the entire
bank (4.8) in both phases, and a multiplicity-preserving braid needs the
extra `(d+1,U)` copy as well.

There is also an intermediate compiler scope.  If eligible lower cells are
restricted to intervals of width at most `d`, the canonical word contains
`U` at width `d`, while the new packet first realizes `U` at width `d+1`.
Consequently the width-truncated ungraded return bank is

\[
                 \mathcal C_L\cup\mathcal C_R\cup\{U\},       \tag{4.10}
\]

of size `2d-1`.  This extra row must be included whenever the compiler does
not permit the owner-width occurrence of `U` to serve as a lower cell.

## 5. Residence, boundaries, and the exact conditional comparator

The local owner path is `V,U`.  For positive-run residence, let
`alpha_x` be the number of consecutive ambient owners immediately before
`V` which contain coordinate `x`, and let `beta_x` be the analogous number
immediately after `U`.  The packet is depth-`d` residence-safe at its joins
exactly when

\[
 \alpha_g\ge d,\qquad \beta_{f_d}\ge d,\qquad
 \alpha_x+2+\beta_x\ge d+1
       \quad(x\in U-\{f_d\}),                            \tag{5.1}
\]

with the usual clipped interpretation at a genuine word boundary.  These
are occurrence conditions, not consequences of set containment.

The marker `M` makes every left prefix phase common.  The right suffix is
phase sensitive until an exterior screen containing

\[
                         X_R=K\cup\{z,a_1,a_3,f_d\}     \tag{5.2}
\]

is met.  Hence arbitrary fixed-context composition additionally requires a
right screen such as (5.2), or a separately audited seam pairing.  This is
why the local support theorem is not yet a global graded/context theorem.

Combining the preceding results gives the following exact sufficient
statement.

### Theorem 5.1 (conditional zero-charge ungraded comparator edge)

Suppose an ambient folded-C8 state supplies:

1. a reserved `d+2`-position reference block `G_epsilon` which may be
   replaced by `Q_epsilon` without changing total length;
2. the owner/palette socket `U,U -> V,U` with edge colours (2.6);
3. the residence ages and futures (5.1);
4. a phase-common right screen or an exact seam pairing as in (5.2);
5. an exterior matching satisfying (4.6), disjoint from ray and cut cells
   (and also returning `U` as in (4.10) for a width-`<=d` compiler);
6. exterior cells repairing the one lower cut colour and any chosen upper
   cut casualty; and
7. every additional ambient owner, protected, and matched-target row meeting
   a packet position leaves the full maximal envelope large enough for the
   displayed phase union; equivalently the actual ambient common-Q caps
   refine (2.7) without excluding any letter of either `Q_epsilon`.

Then replacing the reference block by the opposite-phase packet gives a
same-length, owner-simple, residence-safe, complete-ungraded-interval-
support-transparent, matching-closed folded comparator.  Its local
owner/cap/palette state is the same after either phase, so repeated use does
not accumulate a fresh host charge.

#### Proof

Items 1--3 and Theorem 2.1 give the physical Johnson owner path and
residence.  Theorem 3.1 cancels exactly the folded ray support in the
opposite orientation and supplies distinct cells for every ray target.
Item 4 makes all crossing context rows common.  Theorem 4.1 says that the
only reference support lost by the substitution is (4.1)--(4.2), and item 5
returns it without cell collisions.  Item 6 repairs the opening rows.
Finally item 7 and (2.7) put every chosen source value in one common-Q state.
Both phases have the same owners, envelopes and typed edge colours, proving
the return assertion.  \(\square\)

This theorem is constructive once its exterior matching and seam are
given.  What is still missing is an all-carrier proof of items 2--7 and a
transport theorem placing conjugate packets at every required adjacent
birail obligation while sharing one returned state.  For a width-graded
recursive braid, item 5 must be replaced by a typed matching for (4.8), plus
the extra unit in (4.9) when multiplicity is protected.  The local theorem
does not cancel the known linear graded-occurrence residue.

## 6. Independent audit and scope

The dependency-free replay

```text
python3 scratch/audit_k_folded_c8_basis_changing_ray_socket_20260801.py --write
```

exhausts every neutral-gap position for `2<=d<=16` and the two extreme plus
one central gap through `d=64`.  It checks the owner edge, maximal envelopes,
common caps, exact directed support, the two duplicate graded ray
occurrences, the diagonal occurrence matching, the exact common-chain
loss/gain ledger, and the `3d`/`3d+1` graded losses at the minimum gap.

The proof is dimension-uniform; the finite replay is an independent audit,
not an extrapolation.  The result does not supersede the separate no-go for
aligned pairwise-shared `K_(2,2)` tag rails, and it does not promote
distinct-support cancellation to graded multiplicity equality.
