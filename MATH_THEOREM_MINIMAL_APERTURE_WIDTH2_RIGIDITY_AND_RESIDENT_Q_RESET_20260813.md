# Minimal-aperture resident rails are width-two rigid, and phases admit a resident `q`-reset

**Date:** 2026-08-13  
**Method:** cyclic run counting, proper-window injectivity, and explicit
shift-register flushing  
**Status:** unconditional local theorem for actual pure-rail columns.  It
does not construct a zero-current phase braid or a global positive owner
factor.  The failed serpentine extension is audited separately in
`MATH_AUDIT_MINIMAL_APERTURE_WIDTH2_CHARACTER_Q_RESET_AND_SERPENTINE_WRAP_20260813.md`.

## 1. Setup

Put

\[
 q=d+1,
\]

and let

\[
 \mathcal H=(H_t)_{t\in\mathbb Z/\ell\mathbb Z},
 \qquad H_t=F\mathbin{\dot\cup}J_t,
 \qquad |J_t|=q,                                   \tag{1.1}
\]

be a closed Johnson walk of rank-`R` sets.  Thus every transition deletes
one point and inserts one point.  Assume that `F` contains every coordinate
which is constantly positive on the walk, and that every nonconstant
positive run has length at least `q`.

## 2. Minimal-aperture rigidity

### Theorem 2.1 (shift-register normal form)

Every nonconstant positive run has length exactly `q`.  If `x_s` is the
point entering at the transition from `H_(s-1)` to `H_s`, then

\[
 H_t=F\cup\{x_{t-q+1},x_{t-q+2},\ldots,x_t\}.      \tag{2.1}
\]

#### Proof

Each transition inserts a point absent just before that transition, and
hence begins one nonconstant positive run.  Conversely every such run
begins at an insertion.  There are exactly `ell` positive runs, counted
with multiplicity.  Moreover

\[
 \sum_{\rho\text{ positive run}}|\rho|
 =\sum_{t=0}^{\ell-1}|J_t|=q\ell.                  \tag{2.2}
\]

Every summand on the left is at least `q`, so equality forces every run to
have length `q`.  The entry event `x_s` is therefore present precisely at
times `s,s+1,...,s+q-1`.  At time `t`, the active entry events are exactly
`t-q+1,...,t`, proving (2.1).  They give `q` distinct physical labels
because `J_t` is a set of size `q`.  This proof also permits a physical
label to re-enter in a general closed walk; it counts entry events. \(\square\)

### Theorem 2.2 (width-two rigidity of a legal pure rail)

Assume in addition that the entry sequence is one cyclic ordering

\[
 \sigma=(x_0,\ldots,x_{m-1})                       \tag{2.3}
\]

of `m` pairwise distinct toggle points and that `m>=q+2`.  Then the map
from rail adjacency edges to their literal adjacent-owner unions is
injective:

\[
 \{H_t,H_{t+1}\}\longmapsto
 U_t:=H_t\cup H_{t+1}
 =F\cup\{x_{t-q+1},\ldots,x_{t+1}\}.              \tag{2.4}
\]

Consequently, if `E_0,E_1` are two sets of adjacency edges of this rail
and

\[
 \sum_{e\in E_0}e_{U(e)}
 =\sum_{e\in E_1}e_{U(e)},                         \tag{2.5}
\]

then `E_0=E_1`.

#### Proof

The toggle part of (2.4) is a proper cyclic interval of length `q+1<m`
in the distinct-label order (2.3).  A proper interval determines its two
boundary cuts, and distinct starts therefore give distinct underlying
sets.  This remains true at `m=q+2`, where the intervals are
co-singletons.  Equality (2.5) takes place in the free abelian group on
literal rank-`R+1` sets; injectivity recovers the coefficient of every
edge. \(\square\)

### Corollary 2.3 (the actual width-two collision equation)

For a compound rail bank and a literal rank-`R+1` set `U`, put

\[
 \chi_U(E)=|\{e\in E:U(e)=U\}|.                   \tag{2.6}
\]

Every zero-all-width switch from `E_0` to `E_1` must satisfy

\[
 \boxed{\chi_U(E_0)=\chi_U(E_1)
 \quad\text{for every }U\in{[k]\choose R+1}.}      \tag{2.7}
\]

In particular no nontrivial zero-all-width switch is supported on one
minimal-aperture legal pure rail.

The scope of (2.7) is local but literal.  It is an invariant of the actual
rail columns, not an abstract parity gadget.  It is **not** by itself a
global semigroup obstruction: changed edges on different rails or different
cores can cancel when they have the same literal union `U`.  A global
no-go theorem would have to prove that the required cross-rail equal-`U`
collision graph has insufficient matchings.

### Corollary 2.4 (ordered-phase determinism)

At owner `H_t`, retain the ordered phase

\[
 (x_{t-q+1},\ldots,x_t).
\]

Given this phase and a prescribed adjacent union `U superset H_t` of size
`R+1`, the next entry is the unique point in `U-H_t`, and the next phase is

\[
 (x_{t-q+2},\ldots,x_t,U\setminus H_t).            \tag{2.8}
\]

Thus a common-union clique becomes a matching after the minimal-aperture
residence phase is restored.  Any nontrivial actuator needs a genuine
cross-rail phase-changing braid.

## 3. A literal resident phase reset

Let `F` have size `R-q`.  Let

\[
 \alpha=(a_1,\ldots,a_q),\qquad
 Z=(z_1,\ldots,z_q)                                \tag{3.1}
\]

be ordered lists of pairwise distinct points, with disjoint underlying
sets.  Define

\[
 X_t=F\cup\{a_{t+1},\ldots,a_q,z_1,\ldots,z_t\},
 \qquad0\le t\le q.                               \tag{3.2}
\]

### Theorem 3.1 (shielded `q`-reset)

The sequence (3.2) is an owner-simple rank-`R` Johnson path.  Its
transition `t -> t+1` deletes `a_(t+1)` and inserts `z_(t+1)`.  Both
immediate palettes are simple, with

\[
 X_t\cap X_{t+1}
 =F\cup\{a_{t+2},\ldots,a_q,z_1,\ldots,z_t\},      \tag{3.3}
\]

\[
 X_t\cup X_{t+1}
 =F\cup\{a_{t+1},\ldots,a_q,z_1,\ldots,z_{t+1}\}. \tag{3.4}
\]

Every subinterval has the exact union

\[
 \bigcup_{j=s}^{t}X_j
 =F\cup\{a_{s+1},\ldots,a_q,z_1,\ldots,z_t\}
 \qquad(0\le s\le t\le q).                        \tag{3.5}
\]

If a predecessor owner `K` satisfies `K union X_0=U`, then

\[
 K\cup X_0\cup\cdots\cup X_t
 =U\cup\{z_1,\ldots,z_t\},                        \tag{3.6}
\]

which is independent of the ordering of `alpha`.

Finally, (3.2) is a segment of the pure `q`-window rail whose toggle order
begins

\[
 a_1,\ldots,a_q,z_1,\ldots,z_q.                   \tag{3.7}
\]

Extend (3.7) to any cyclic order of `m>=2q` distinct toggles.  Every
toggle then has one positive run of length `q` and one zero gap of length
`m-q>=q`.  The completed rail is both positively and dually resident.

#### Proof

The number of inserted `z`-coordinates in `X_t` is `t`, proving owner
simplicity.  Equations (3.3)--(3.4) follow from the single exchange.
In (3.5), the earliest owner supplies the largest remaining `alpha` suffix
and the latest supplies the largest `Z` prefix.  Since all `a_i` already
belong to `U=K union X_0`, equation (3.6) follows.  The consecutive
`q`-windows in (3.7) are exactly (3.2).  In a distinct-label cyclic order,
each toggle belongs to `q` consecutive windows and is absent from the
remaining `m-q`. \(\square\)

## 4. Exact remaining gate

The reset proves that phase flushing itself is compatible with Johnson
adjacency, palette simplicity, all local interval-union formulas, and both
residence directions.  It does not automatically give a zero-current
actuator.  Given different old and new input phases, one must still choose
cores and reset words so that all literal reset interval-union rows and
immediate-lower rows cancel simultaneously, while realizing the required
socket permutation.

Therefore the proof-safe conclusion is

\[
 \boxed{
 \text{minimal-aperture single-rail switches are width-two rigid, but a
 resident phase reset exists; the cross-rail reset braid remains open.}}
\]
