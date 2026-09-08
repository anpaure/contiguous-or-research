# Fractional pull-clock membership and weighted conflict rounding for fresh phase tickets

**Date:** 2026-08-03
**Status:** exact abstract membership criterion, exact weighted Haxell
rounding theorem, and exact scope separation.  This note does not modify the
fixed `P*` materialization and does not assert a fresh bank on it.  It proves
one new sufficient integralization criterion for a replacement host.  The
common-host literal pushforward, its weighted conflict bound, and an
integral connected chronology remain unproved for the Boolean construction.

## 0. Outcome

The corrected pull clock and the fresh-ticket replacement theorem meet only
after a physical host and its carried boundary have been fixed.  Their exact
logical interface is

\[
 \text{stationary trace law}
 \xrightarrow{\text{one-host literal pushforward}}
 \text{fractional phase-ticket point}
 \xrightarrow{\text{TU or conflict expansion}}
 \text{integral private bank}
 \xrightarrow{\text{Euler fusion}}
 \text{integral chronology}.                         \tag{0.1}
\]

None of the three arrows is formal.

This note proves the middle arrow under a weighted conflict-expansion
hypothesis.  If `x` is a rational fractional choice of one candidate per
short role and

\[
 \lambda_x(c):=\sum_{d\sim c}x_d\le {1\over2}        \tag{0.2}
\]

for every positive candidate `c`, where `d~c` means a cross-role physical
conflict, then there is an integral conflict-free choice of one candidate
per role.  The proof clears denominators and applies the exact `2 Delta`
independent-transversal theorem to candidate clones.

The condition is genuinely stronger than fractional capacity.  The
two-by-two parity tensor has a fractional perfect point, complete two-shore
projections, footprint rank two, resource degree two, and conflict degree
two, but has no integral rainbow cover.  Disjoint copies give arbitrarily
large bounded-degree counterexamples.  Thus bounded codegree or marginal
Hall expansion alone cannot round the pull clock.

## 1. The one-host fractional ticket polytope

Fix all of the following before taking a convex combination:

* one replacement host `H` and one exact outer materialization `mu`;
* one owner phase `phi` and one local child mode `epsilon`;
* one literal carried boundary value `Y`, including its actual cells,
  addresses, endpoint aperture, and authenticated aggregate histories;
* a set `S` of occurrence-labelled short roles; and
* for every `s in S`, the complete finite set `C_s(Y)` of literal ticket
  candidates extending `Y` on `H`.

Each candidate includes its actual five cells, predecessor and successor
occurrences, inverse-rematerialized source labels, addresses, flags, and
every other resource whose capacity is used by the local bank.  Let
`R(c)` be its complete set of capacity-one private resources.  It is not
permitted to project away a cell or address which is later compared with
another selected candidate or with the exterior.

The **private fractional phase-ticket polytope** is

\[
\begin{aligned}
 P_{\epsilon,\phi}(H,Y)=\{x\ge0:
 &\sum_{c\in C_s(Y)}x_c=1 &&(s\in S),\\
 &\sum_{c:\,u\in R(c)}x_c\le1
       &&(u\text{ a capacity-one resource}),\\
 &B_Yx=b_Y\},                                         \tag{1.1}
\end{aligned}
\]

where `B_Y x=b_Y` denotes only those exact boundary, flag, state-balance, or
history rows that have actually been included in the candidate model.  If
there are no such extra rows, the last line is absent.

### Proposition 1.1 (exact meaning of fractional membership)

A rational vector in (1.1) certifies exactly the following facts.

1. Every short role has positive total legal mass on the one fixed host and
   actual boundary.
2. Every encoded capacity, boundary, and balance row is satisfied
   fractionally.
3. Every linear Farkas or Hall separator of this exact LP is cleared.

It does not certify an integral private bank, a common table for a different
phase, an owner-rainbow one-copy selection, an Euler component, residence,
upper/source legality, compiler compatibility, or birail cross matching
unless the corresponding literal rows were included in (1.1).

#### Proof

The first three assertions are the definition of membership and linear
duality.  Every item in the second paragraph is either an integrality
assertion, a statement about a different polytope, a connectivity assertion,
or an omitted predicate; none follows from membership in (1.1).  \(\square\)

### Theorem 1.2 (one-host literal pushforward criterion)

Let `Omega` be a finite set of positive trace atoms of a rational stationary
pull-clock law, with weights `w_omega`.  Suppose there is a map

\[
                    \pi:\Omega\longrightarrow
                    \bigcup_{s\in S}C_s(Y)             \tag{1.2}
\]

such that:

1. `pi` sends each trace atom to a literal candidate on the same fixed
   `(H,mu,epsilon,phi,Y)` and preserves its short role;
2. it preserves every selected physical cell, source, address, and boundary
   history read by the ticket predicate;
3. for each role `s`, the total weight of atoms mapped into `C_s(Y)` is one;
4. for every capacity-one resource `u`, the total weight of atoms whose
   images use `u` is at most one; and
5. the pushed weights satisfy every displayed row `B_Yx=b_Y`.

Then

\[
              x_c:=\sum_{\omega:\,\pi(\omega)=c}w_\omega \tag{1.3}
\]

belongs to \(P_{\epsilon,\phi}(H,Y)\).

#### Proof

Sum the five hypotheses over the fibres of `pi`.  They become respectively
literal candidate support, the role equalities, the resource inequalities,
and the extra equations in (1.1).  \(\square\)

The content of the theorem is its premise.  The corrected pull clock gives
exact rational rank marginals and stationary trace circulation after
averaging over owners, private sets, orders, core subsets, and payload
tables.  It does **not** supply (1.2) into one physical replacement host.
A convex combination of points belonging to different candidate matrices
is not a point of any one matrix.

Thus the already closed phrase **fractional pull-clock membership** means
membership in the literal trace-type circulation used by that theorem.  It
does not, without (1.2), mean membership in the fixed-host phase-ticket
polytope (1.1).  These two uses of “membership” must not be identified.

For two owner phases on a phase-common protected host, one needs separate
points

\[
 x^0\in P_{\epsilon,0}(H,Y),\qquad
 x^1\in P_{\epsilon,1}(H,\theta Y),                   \tag{1.4}
\]

where `theta` is the authenticated bounded-boundary conjugacy.  Averaging
the two phases does not prove either membership in (1.4).  The fixed-`P*`
local-menu no-go remains untouched; Theorem 1.2 concerns a prospective
replacement host only.  Allowing distinct physical hosts would require a
separate full host transport theorem; it is not hidden in `theta`.

## 2. The exact normality and TU alternatives

Temporarily omit the additional signed rows `B_Yx=b_Y`.  Add one unused
resource-slack column for each capacity row and let `A` be the resulting
zero-one exact-cover matrix, with one row for every role and resource.  Its
demand `b` is one on every row.  Then

\[
\begin{array}{ccl}
b\in A\mathbb R_{\ge0}^{E}&\Longleftrightarrow&
   \text{fractional private completion},\\
b\in A\mathbb Z_{\ge0}^{E}&\Longleftrightarrow&
   \text{integral private completion}.                \tag{2.1}
\end{array}
\]

Thus lattice membership and unit-fibre semigroup membership, not merely
fractional capacity, are the exact general integral rows.  Normality of the
augmented column semigroup is sufficient after the lattice row is checked;
it is not automatic.

There is one stronger positive face already available.  If all candidates
of one fixed exact owner-payload table form payload-transparent Cartesian
tail/head rectangles, and the rational root-conditioned circulation is
supported in those rectangles, the fixed-table Hoffman inequalities hold.
The network matrix is totally unimodular, so the rational circulation
rounds to an integral one-copy selector on that same table.  This is the
exact rotor theorem; it cannot be applied before the common table and
rectangle support have been proved.  Any extra private resource or upper,
residence, or compiler filter must first be shown to preserve the rectangle
face or must be added as an additional constraint and re-audited.

## 3. Weighted conflict rounding

The following theorem gives a second positive face which does not require a
network matrix.

Let `Gamma` be the graph on all candidates in `C=union_s C_s(Y)`.  Delete
within-role edges.  Join two candidates of different roles precisely when
they cannot occur together.  The edge relation must contain every shared
capacity-one resource and every other pairwise incompatibility needed for
simultaneous composition.  Assume the **composition-closure** statement:
every independent transversal of `Gamma` is literally a valid private
phase bank with boundary `Y`.

For a rational role-normalized vector `x`, define its external weighted
conflict load at `c` by

\[
       \lambda_x(c)=
       \sum_{\substack{d\in C:\,d\sim c\\
                       \operatorname{role}(d)\ne
                       \operatorname{role}(c)}}x_d.    \tag{3.1}
\]

### Theorem 3.1 (weighted `2 Delta` transversal)

Suppose

\[
        \sum_{c\in C_s(Y)}x_c=1\quad(s\in S),
        \qquad
        \lambda_x(c)\le {1\over2}\quad(x_c>0).        \tag{3.2}
\]

Then `Gamma` has an independent transversal.  Consequently there is an
integral private phase bank on `(H,Y)`.

#### Proof

Choose a common denominator `N` for `x`.  Replace every positive candidate
`c` by `N x_c` indistinguishable labelled clones in its role part.  Join a
clone of `c` to every clone of every conflicting candidate `d`.  Each role
part now has exactly

\[
                         \sum_{c\in C_s}Nx_c=N         \tag{3.3}
\]

vertices.  A clone of `c` has external degree

\[
                  \sum_{d\sim c}Nx_d
                     =N\lambda_x(c)\le N/2.           \tag{3.4}
\]

Hence the clone graph has maximum degree `Delta<=N/2`, while every part has
size `N>=2 Delta`.  Haxell's independent-transversal theorem, including
equality in the `2 Delta` bound, supplies one clone from every role part and
no conflict edge.  Projecting clones to their original candidates gives an
independent transversal of `Gamma`.  Composition closure makes it the
claimed literal bank.  \(\square\)

This is a rounding theorem for pairwise packing rows.  It does not preserve
an arbitrary extra equation `B_Yx=b_Y`.  Exact saturated flag quotas,
tail/head balance, owner counts, or history currents must either be built
into a TU face, encoded in candidate roles with a separately verified
expansion condition, or repaired by an explicit bounded absorber.
Likewise, a capacity larger than one must first be expanded into actual
unit slots, after which the new slot conflicts and the weighted bound must
be rechecked.  A residual outer-matching extension, long--long or supplier
perfect matching, and Euler/subtour connectivity remain separate Hall or
flow gates unless the complete matching was fixed before candidates were
formed or a proved equivalent pairwise encoding is included in `Gamma`.

No necessity or optimality of the numerical constant `1/2` is claimed; it
is the exact weighted corollary obtained from the proved `2 Delta`
independent-transversal theorem.

### Corollary 3.2 (resource-load criterion)

Suppose every cross-role conflict is witnessed by a capacity-one resource
shared by its two candidates, and every candidate uses at most `r` such
resources.  (A genuinely pairwise guard may be made a synthetic resource,
but it must then be counted in `r`.)  Suppose also that

\[
             L_x(u):=\sum_{d:\,u\in R(d)}x_d
                    \le {1\over2r}                    \tag{3.5}
\]

for every resource.  Then an integral private bank exists.

#### Proof

For each `c`, take a union bound over its resource footprint:

\[
 \lambda_x(c)
 \le\sum_{u\in R(c)}L_x(u)
 \le r\,{1\over2r}={1\over2}.                         \tag{3.6}
\]

The same-role contributions in (3.5) and multiply counted conflicts only
make the displayed bound more conservative.  Apply Theorem 3.1. \(\square\)

### Corollary 3.3 (bounded resource degree and menu expansion)

Under the shared-resource premise of Corollary 3.2, suppose each candidate
uses at most `r` resources, every resource occurs in at most `D` supported
candidates, every role has exactly `M` supported candidates, and use the
uniform law `x_c=1/M`.  If

\[
                         M\ge2r(D-1),                  \tag{3.7}
\]

then an integral private bank exists.  More sharply, it is enough that the
actual cross-role conflict degree be at most `Delta` and `M>=2 Delta`.

#### Proof

A candidate has at most `r(D-1)` conflicting supported candidates, with
repeated conflicts only lowering the number.  Hence
`lambda_x(c)<=r(D-1)/M<=1/2`.  The sharper statement is the same calculation
using the actual conflict degree.  \(\square\)

Condition (3.7) is the precise kind of bounded-codegree expansion that is
usable here: candidate footprint rank, resource degree, and post-filter
menu thickness are all controlled on the **actual fixed boundary**.  A
bound only on pair-codegree, or a large projected flag menu before physical
resource filters, does not imply (3.7).

### Theorem 3.4 (global conflict mass gives bounded defect)

For any rational role-normalized law `x`, put

\[
 M_x:=\sum_{\{c,d\}\in E(\Gamma)}x_cx_d
     ={1\over2}\sum_{s\in S}\sum_{c\in C_s}x_c
                         \lambda_x(c).                 \tag{3.8}
\]

There is an integral choice of one candidate from every role whose selected
conflict graph has at most `floor(M_x)` edges.  After deleting candidates
from at most `floor(M_x)` roles, the remaining choices form an independent
partial transversal.  In particular, `M_x<1` already implies an exact
independent transversal.

#### Proof

Choose one candidate independently in each role according to `x`.  For
each cross-role conflict edge `{c,d}`, the probability that both endpoints
are selected is `x_c x_d`.  Hence the expected number of selected conflict
edges is exactly `M_x`.  Since this number is integer-valued, some outcome
has at most `floor(M_x)` conflict edges.

For each conflict edge of that outcome choose one endpoint, and delete the
union of the chosen endpoints.  At most one role is lost per edge, and
every selected conflict edge is hit.  The undeleted candidates are
therefore independent.  If `M_x<1`, the selected outcome has zero conflict
edges and no deletion is needed.  \(\square\)

### Corollary 3.5 (square-resource-load defect bound)

Under the shared-resource premise of Corollary 3.2,

\[
                      M_x\le {1\over2}\sum_u L_x(u)^2. \tag{3.9}
\]

Consequently, if `sum_u L_x(u)^2=O(1)`, all but `O(1)` roles have a
simultaneous integral private selection.

#### Proof

Charge each conflict to every shared resource, which only overcounts it.
For one resource `u`, the total weight of unordered distinct candidate
pairs using it is

\[
 {1\over2}\left(L_x(u)^2-\sum_{c:\,u\in R(c)}x_c^2\right)
 \le {1\over2}L_x(u)^2.                               \tag{3.10}
\]

Summing over resources proves (3.9), and Theorem 3.4 gives the conclusion.
\(\square\)

### Corollary 3.6 (bounded exceptional roles)

Let `E subseteq S`.  If Theorem 3.1 holds after restricting the parts and
conflict graph to `S-E`, then all roles outside `E` have a simultaneous
integral private selection.

Corollary 3.6 or Theorem 3.4 produces an `O(1)` defect only when the omitted
set is bounded and a separate literal terminal theorem completes it without
invalidating the chosen bank.  Calling the omitted roles a sidecar is not
itself such a completion theorem.

There is also an incomparable existing probabilistic criterion.  If

\[
 Z_s=\sum_{c\in C_s}x_c\lambda_x(c),qquad
 \max_s Z_s\le {1\over2e},                            \tag{3.11}
\]

the conflict-mass local-lemma theorem gives an independent transversal.
Equation (3.11) tolerates a small amount of heavy mass; Theorem 3.1 permits
average conflict mass up to `1/2` but requires every positive candidate to
be light.  Neither condition has yet been proved for a replacement Boolean
host.

## 4. Why fractional capacity and bounded degree are insufficient

### Proposition 4.1 (bounded-degree parity obstruction)

Let the two role parts be tails `p in {0,1}`.  A candidate chooses a head
`h in {0,1}` and an owner colour

\[
                         kappa(p,h)=p\mathbin\oplus h. \tag{4.1}
\]

Heads and colours are capacity-one resources.  Giving each of the four
candidates weight `1/2` satisfies every role, head, and colour row with
equality.  Every candidate has resource footprint two; each resource occurs
in two candidates; and the cross-role conflict degree is two.  Nevertheless
there is no integral transversal.

#### Proof

The identity head matching uses colour zero twice, while the transposition
uses colour one twice.  These are the only two head-perfect matchings, so
neither is owner-rainbow.  Equivalently the four triples are

\[
                         000,\quad011,\quad101,\quad110,\tag{4.2}
\]

and any pair belonging to different tail roles shares a head or a colour.
The displayed half-point is therefore fractional but not integral.
\(\square\)

Disjoint copies give arbitrarily many roles while keeping footprint rank,
resource degree, and conflict degree bounded.  In each copy
`lambda_x(c)=1`, so Theorem 3.1 correctly refuses to round it.  This is an
abstract obstruction, not a Boolean-chain counterexample: the functional
Boolean union colouring excludes this smallest intercalate.  It nevertheless
proves that no theorem based only on fractional marginals and bounded local
degree can discharge the fresh-ticket gate.

The obstruction in Proposition 4.1 already fails a lattice row.  Even after
lattice membership, normality is not formal: the saturated marked-age
example at `(r,d,W)=(7,3,2)` has an integral rank histogram and a connected
rational stationary realization but no integral stationary age circulation;
its projected marked-age semigroup is nonnormal.  Thus the common-host step,
lattice/normality or a special integral face, and connected Euler chronology
are three separate requirements.

## 5. Chronology and protected-row scope

An independent transversal from Section 3 is a static bank.  It need not
satisfy state balance, and a balanced integral selector may still be a
disjoint union of Euler components.  The exact routes onward are:

1. prove that the selected point lies on one fixed Cartesian hinge-rectangle
   face and use the Hoffman/TU theorem;
2. reserve a distinct-role spanning skeleton and verify all residual
   Hoffman cuts, which is the exact connected one-copy criterion; or
3. prove a literal fusion operation preserving every owner, resource, and
   boundary row.

Fractional connected support alone proves none of these.

Even a complete private bank proves only the ticket-packing conjunct of the
phase-local predicate `Q_(epsilon,phi)(Y)` from the boundary-erasure theorem.
It cannot be declared a regenerated parent until every required outer,
supplier, chronology, and exported-boundary conjunct has also been
authenticated.

The other protected ingredients retain only their established scopes.

* The monotone pivot causes zero old arbitrary-width upper damage on its
  flat transported bank and requires its literal owner-legal rays.  It does
  not make an arbitrary rounded bank upper-safe.
* Upper/source, positive and negative residence, and compiler rows inherit
  only if they were used to filter the candidate menus or were proved
  invariant under the rounding face.
* Bounded compiler eviction applies after an integral word and its complete
  damage set are fixed.  It does not round (1.1).
* Zero-block birail collapse applies after the required physical cross
  matchings coexist in one compatible terminal state.  Fractional ray
  marginals do not supply those matchings.
* Boundary erasure applies only after both phase-specific integral banks
  exist at the actual conjugate boundary values and the complete exterior
  dependency factors through that boundary.

## 6. Exact remaining theorem

The new sufficient replacement-host target can be stated without reference
to the obsolete bulk ledger:

> Construct, for each required phase at the actual carried boundary, one
> common-host rational literal pushforward satisfying Theorem 1.2 and one of
> (i) the fixed-table Cartesian Hoffman hypotheses, (ii) the weighted
> conflict bound (3.2) outside only `O(1)` exceptional roles, or (iii) the
> global bound `M_x=O(1)`.  Give every exceptional role an authenticated
> terminal completion.  Then separately supply the connected integral
> chronology and the complete boundary conjugacy.

The following are **PROVED** here:

1. Theorem 1.2 is the exact one-host pushforward sufficient for fractional
   phase-ticket membership.
2. Theorem 3.1, Theorem 3.4, and Corollaries 3.2--3.6 are exact
   fractional-to-integral packing or bounded-defect theorems under their
   stated composition and expansion hypotheses.
3. Proposition 4.1 refutes generic rounding from fractional capacity plus
   bounded local degree.
4. Static packing, exact balance, and connected chronology are logically
   distinct.

The following are **UNPROVED**:

1. a one-host literal pushforward of the corrected pull clock for either
   required phase;
2. the weighted load bound (3.2), the resource expansion (3.7), the global
   conflict bound `M_x=O(1)`, or one common Cartesian rectangle face on a
   replacement host;
3. preservation or bounded repair of every exact flag/balance row under
   conflict rounding;
4. an integral connected owner-rainbow chronology;
5. the phase-common complete boundary, residence/upper/compiler compatibility,
   and terminal birail cross matchings; and
6. any unconditional `B(k)+O(1)` or `B+1` conclusion.

## 7. Proof-bearing inputs

```text
MATH_THEOREM_FRESH_TICKET_BOUNDARY_ERASURE_AND_BOUNDED_RESET_STATE_20260802.md
MATH_THEOREM_CORRECTED_PULL_CLOCK_PACKING_AND_FRACTIONAL_TRACE_CIRCULATION_20260801.md
MATH_THEOREM_A_INTEGRAL_COLOURED_ROTOR_ONECOPY_MINMAX_AND_RAINBOW_FUSION_20260802.md
MATH_THEOREM_K_HINGE_RECTANGLE_COLOURED_ROTOR_FLOW_AND_ROOTED_EULER_FUSION_20260802.md
MATH_THEOREM_INTEGRAL_AGE_CIRCULATION_NORMALITY_AND_LATTICE_OBSTRUCTIONS_20260801.md
MATH_THEOREM_BUFFERED_HEXAGON_LLL_REDUCTION_AND_MISSING_LOAD_GATE_20260731.md
MATH_THEOREM_AD_K17_RAINBOW_PROVIDER_HYPERGRAPH_AND_Q1_ABSORBER_20260731.md
```

The weighted-clone proof and the preceding pairwise/nonpairwise row split
were independently audited on 2026-08-03.  The audit introduced no finite
or computational claim.
