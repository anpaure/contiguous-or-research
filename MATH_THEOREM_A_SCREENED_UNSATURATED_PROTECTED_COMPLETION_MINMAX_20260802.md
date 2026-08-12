# Screened unsaturated hinges: exact protected completion and the finite forbidden-cut bank

**Date:** 2026-08-02  
**Lane:** A, integral rotor completion  
**Status:** exact conditional global theorem, deterministic expansion rows,
and an all-depth raw-menu obstruction.  No fractional-clock input is used.
The occurrence binding of the screens, expiration scheduling, common source,
and compiler remain explicit hypotheses.

## 0. Outcome

The unsaturated hinge has enough local freedom to support a genuine
protected-completion theorem, but not an unconditional one.

* A physically bound screen and collar make residence and every owner-level
  upper interval invariant across the entire Boolean tail cube.
* On those accepted complete-state menus, global one-copy completion is
  exactly a capacitated predecessor Hall problem.
* Reserving a connected distinct-role skeleton costs precisely one explicit
  low-slack damage function.  There is no hidden topology term.
* Weighted menu expansion proves Hall; a row/column rejection inequality
  proves protected two-switch fusion to one Euler component.
* Raw unsaturated menus nevertheless have a deficit-one Hall obstruction at
  every depth.  Disjoint copies rule out any dimension-uniform `O(1)`
  boundary-only sidecar theorem on a fixed table based only on unsaturation
  or menu cardinality.

Thus the missing positive theorem is now a Boolean-specific **bounded-load
occurrence-binding theorem** for one chosen global chain table.

## 1. The load-bearing accepted-menu hypothesis

Let `I` be the owner/payload roles and `V` a finite bank of complete
interface states.  Besides the literal order-`d` source tuple, a state
contains clipped coordinate run ages, the adjacent owner type, and the
boundary signature used by every named upper occurrence.

Role `i` has one owner and one fixed lower-target payload, a fixed completed
head `h_i`, and an accepted tail menu `M_i subset V`.  The phrase
**accepted menu** means that, for every `a in M_i`, a literal physical
packet `a -> h_i` has already been supplied which

1. uses the same role resources;
2. has private interior apart from its declared endpoint states;
3. passes every internal and boundary residence transition;
4. retains the same named upper-witness tickets and exterior signature; and
5. is compatible with the fixed protected bank `P`, including exact
   capacity for every owner and lower/upper q1 colour introduced by a screen.

This occurrence binding is not a marginal condition.  In particular, a
local proof that a screen letter *could* precede a hinge does not prove that
the preceding selected packet supplies that literal occurrence.  The
designated source cell must equal the literal screen `G` (not merely contain
it), and the screen/collar must be physically bound, or their exact effect
must be carried by a proved exterior-realization theorem, before the
resulting cube is placed in `M_i`.  Cross-role collisions among the screen
owner and its q1 colours are part of this binding.

For a strict chain `S_1<...<S_ell<T`, the screened construction gives such
a role-local cylinder whenever the fixed exterior really contains

\[
 G=(S_1-\{y\})\cup\{z\},\qquad z\notin T,             \tag{1.1}
\]

and the two signed collars omit `y` on the left and `z` on the right.  Once
one pair `(y,z)` and its filler schedule is accepted, every

\[
 B_0=(T-S_\ell)\cup A,qquad A\subseteq S_1-\{y\},    \tag{1.2}
\]

survives with the same owner-derived residence/upper signature.  The
complete literal tail states remain distinct.  Hence the accepted relation
is exactly

\[
                         M_i\times\{h_i\},            \tag{1.3}
\]

with `|M_i|=2^(|S_1|-1)` on the full screened cylinder.

The original repeated filler is not generally a physical multi-edge flush.
Within the generalized singleton-filler class, all local zero-novelty
repeats can be removed exactly when

\[
 d-\ell\le |S_\ell|-|S_1|-(\ell-1).                 \tag{1.4}
\]

Even then, exact expiration and rank preservation at every transition must
still be audited.  Equation (1.4) is an aperture, not a completed path.

## 2. Exact protected predecessor min--max

Put

\[
 \eta=\partial P,\qquad
 m(v)=|\{i:h_i=v\}|,\qquad b(v)=m(v)+\eta(v).         \tag{2.1}
\]

For `J subset I` let `N(J)=union_(i in J) M_i`.  For `X subset V` put

\[
 \ell(X)=|\{i:M_i\subseteq X\}|,
 \qquad \sigma(X)=b(X)-\ell(X).                      \tag{2.2}
\]

### Theorem 2.1 (screened protected completion)

Assume the accepted-menu hypothesis of Section 1.  A physical protected
one-copy selection exists if and only if `b>=0`, `b(V)=|I|`, and

\[
 \boxed{|J|\le b(N(J))\quad(J\subseteq I).}           \tag{2.3}
\]

Equivalently, `sigma(X)>=0` for every `X subset V`.  It suffices to test
sets `X` which are unions of accepted menus.  The selected carrier retains
all compiled residence histories and upper tickets literally.

#### Proof

Balance requires state `v` to be chosen as a free tail exactly `b(v)`
times.  Clone `v` into `b(v)` capacity copies and join role `i` to the
copies of its states in `M_i`.  Equation (2.3) is Hall's theorem.  The
equivalent state-shore form follows by taking the roles whose complete menu
lies in `X`; a failed shore shrinks to the union of those menus.  Finally,
every selected tail--head pair is a physical packet by Section 1, so all
compiled guards lift with the matching.  \(\square\)

The literal tail menus split by their last `(d-1)` source letters.  Thus
Theorem 2.1 decomposes into independent de Bruijn-spine fibres.  In
particular, every used fibre `V_s` must satisfy

\[
                         b(V_s)=|\{i:M_i\subseteq V_s\}|.              \tag{2.4}
\]

This is the first linear forbidden-cut row.

### Theorem 2.2 (deterministic Boolean expansion)

Let

\[
                         \Delta(v)=|\{i:v\in M_i\}|.                  \tag{2.5}
\]

If every role satisfies

\[
 \boxed{\sum_{v\in M_i}{b(v)\over\Delta(v)}\ge1,}                   \tag{2.6}
\]

then all cuts (2.3) hold.  In particular, if every offered state has
positive capacity, maximum accepted load is at most `Delta`, and every full
screened cylinder has size at least `Delta`, protected completion exists.

#### Proof

Sum (2.6) over any `J` and interchange the sums.  The contribution at a
state is at most `b(v)`, giving `|J|<=b(N(J))`.  Apply Theorem 2.1.
\(\square\)

This is the promised positive expansion statement.  Its bounded-load
hypothesis, not the raw cube size, is decisive.

### Proposition 2.3 (connected forbidden-cut reduction)

Make the accepted-menu overlap graph on the roles, joining `i,j` exactly
when `M_i cap M_j` is nonempty.  If a predecessor Hall cut fails, then one
fails on a role set inducing a connected subgraph.  Hence it is complete to
test connected role unions inside each spine fibre.

For two unlabelled raw Boolean intervals in one common fibre,

\[
 [U_i,U_i\cup F_i]\cap[U_j,U_j\cup F_j]\ne\varnothing              \tag{2.7}
\]

exactly when

\[
 U_i\subseteq U_j\cup F_j,
 \qquad U_j\subseteq U_i\cup F_i.                                  \tag{2.8}
\]

For complete states one additionally requires equality of the fixed spine
and every auxiliary label.

#### Proof

If a role set `J` is disconnected in the overlap graph, split it into two
nonempty parts with disjoint neighbourhoods.  Then its Hall deficit is the
sum of the two part deficits, so a positive deficit occurs in at least one
part.  Iteration gives a connected deficient subset.  Two Boolean intervals
intersect exactly when their lower-set union belongs to both upper bounds,
which is (2.8).  \(\square\)

## 3. Exact connected skeleton and an adaptive fusion row

Reserve tails `a_i in M_i` from distinct roles `i in I_R`, and put

\[
 t_R(v)=|\{i\in I_R:a_i=v\}|,
 \qquad
 D_R(X)=|\{i\in I_R:a_i\in X,\ M_i\not\subseteq X\}|.               \tag{3.1}
\]

### Theorem 3.1 (skeleton damage identity)

Fix an exact intended non-isolated support `V_*` containing the states used
by `P` and every fixed head.  Restrict every menu to `M_i cap V_*`, require
it to remain nonempty, and compute `b,sigma,D_R` on this restricted
instance.  The reserved packets extend to a protected completion with at
most `c` weak components if and only if

1. `P union R` spans `V_*` with at most `c` weak components;
2. `b-t_R>=0`; and
3.

\[
                         \boxed{D_R(X)\le\sigma(X)}                   \tag{3.2}
\]

for every residual-menu union `X`.  Thus `c=1` gives one connected Euler
component exactly.  If `|R|=t`, only shores with
`sigma(X)<t` can obstruct it.

#### Proof

Deleting a reserved role removes one menu and consumes its selected tail
capacity.  The residual Hall slack is

\[
 (b-t_R)(X)-\ell_R(X)=\sigma(X)-D_R(X).              \tag{3.3}
\]

Theorem 2.1 proves the equivalence; item 1 supplies the spanning forest.
Conversely, extract such a forest from any completed solution on `V_*`; its
remaining packets certify (3.2).  \(\square\)

On the unit-capacity face, identify roles with their fixed heads and write
`N=|V|`.  A stronger but readily checkable route starts with any Hall cycle
cover.  For `C subset V` put

\[
 \mathcal D(C)=
 \sum_{i\in C}|(V-C)-M_i|+
 \sum_{j\notin C}|C-M_j|.                            \tag{3.4}
\]

If

\[
                         \mathcal D(C)<|C||V-C|       \tag{3.5}
\]

for every nontrivial `C`, a legal protected two-switch crosses every union
of current cycles, so repeated switches produce one Euler cycle.  It is
enough that

\[
 \rho+\kappa<N/2,qquad
 \rho=\max_i|V-M_i|,quad
 \kappa=\max_v|\{i:v\notin M_i\}|.                  \tag{3.6}
\]

These are sufficient expansion rows, not consequences of Boolean interval
cardinality.

## 4. Exact global separators after a fully audited local catalogue

The screen construction exposes three useful local rejection certificates.

1. **Screen:** a variable coordinate and a crossing window in which the
   fixed exterior does not cover it.
2. **Collar:** the chosen deleted coordinate occurs in the left collar, or
   the inserted outside coordinate occurs in the right collar.
3. **Freshness:** one incoming source cell has no coordinate outside the
   preceding owner; equivalently its local novelty set is empty.  Inside the
   generalized filler class, failure of (1.4) is the aggregate aperture
   certificate.

These three rows do **not** constitute a complete physical acceptance test.
Every proposed multi-edge packet must additionally replay exact expiration,
rank preservation (the outgoing loss and fresh incoming gain must realize
the declared Johnson transition), and all remaining finite-state histories.
Only after that replay has produced the accepted menus are the following
global separators exact.

4. **Spine flux:** (2.4) fails.
5. **Predecessor Hall:** a union `X` of accepted menus has
   `sigma(X)<0`.
6. **Skeleton damage:** a proposed reserved forest has
   `D_R(X)>sigma(X)` on a residual-menu union.  For a `t`-edge forest it is
   enough to retain the shores with `sigma(X)<t`.
7. **Two-switch lock:** for some union `C` of current cycles, every cross
   pair is rejected by at least one of the two literal menu incidences.  This
   obstructs that fusion basis, though a larger protected circuit may still
   exist.

Items 4--6 are exact necessary-and-sufficient separators for balance and a
fixed spanning skeleton after the fully audited accepted catalogue is
supplied.  Item 7 is only the exact obstruction to the stated two-switch
descent.

## 5. Why unconditional expansion and `O(1)` sidecar are false

For every `d>=1` and `r>=d+1`, there is a raw unsaturated table with
distinct owners and heads and a nonempty local predecessor menu at every
role, but with a two-role Hall shore of deficit one.  The construction uses
`2(d+1)` cyclic disjoint blocks, whose empty-`A` tails are the preceding
heads, and one fresh-block role sharing one of those sole predecessors.

At `d=1`, four roles are already sufficient and minimal under distinct
owners/heads and local nonemptiness.  Taking disjoint copies makes the
deficient neighbourhoods disjoint, so a boundary-only correction by paths
or arcs, while keeping the roles, heads and menus fixed, needs at least one
positive boundary unit per copy.  Hence no uniform `O(1)` boundary-only
sidecar on a fixed table follows from unsaturation alone.  A correlated
macro which changes that table is outside this lower bound.

Even after Hall is exact, two singleton-menu unsaturated banks on disjoint
alphabets force two Euler cycles whose cross-bank de Bruijn overlap distance
is `d`.  Therefore `O(1)` component count alone also does not imply an
`O(1)` literal sidecar.

These counterexamples are intentionally scoped: they do not satisfy an
independently required all-upper/residence specification.  They refute only
the claimed implication from raw unsaturated menus to global protected
completion.

## 6. Exact remaining theorem

A positive all-dimensional construction may now target the following
single object:

> Choose one integral owner/chain table and physically bind its
> screen/collar/filler occurrences so that the resulting complete-state
> menu loads satisfy (2.6), then reserve a connected distinct-role skeleton
> satisfying (3.2).

This would give a protected one-copy Euler carrier with zero route sidecar.
For an `O(1)` sidecar version, replace connectedness by a constant-component
skeleton and additionally exhibit `O(1)` total literal overlap-routing cost.

What is still absent is the occurrence-binding/load theorem.  The local
screen is not a free letter at every role: in a global chronology it must be
supplied by the preceding physical occurrence or by a protected macro, and
those supplies compete.  Exact source/common-Q and compiler closure remain
downstream.  The corrected stationary pull clock proves none of these
correlations.

## 7. Audited sources

The exact component theorems and literal replays are frozen in:

* `MATH_THEOREM_A_UNSATURATED_HINGE_PREDECESSOR_HALL_AND_BOOLEAN_INTERVAL_OBSTRUCTION_20260802.md`;
* `MATH_THEOREM_A_UNSATURATED_HINGE_SCREENED_UPPER_SIGNATURE_AND_FRESHNESS_OBSTRUCTION_20260802.md`;
* `MATH_THEOREM_A_UNSATURATED_HINGE_SKELETON_DAMAGE_AND_TWO_SWITCH_EXPANSION_20260802.md`.

Their lightweight verifiers replay the all-depth Hall obstruction through
depth seven, 33,474 screened instances, 90,070 menu words, 117,536 screen
grids, 6,910 skeleton-damage identities, 3,564 expanding menu systems, and
132 separated-cycle roles.
