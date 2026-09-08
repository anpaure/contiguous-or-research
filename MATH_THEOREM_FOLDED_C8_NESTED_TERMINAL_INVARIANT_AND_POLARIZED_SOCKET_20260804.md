# Folded-C8 antidiagonals versus nested terminals: a sharp invariant and the minimal polarized socket

**Date:** 2026-08-04

**Status:** unconditional semantic/lattice no-go, together with an exact
conditional stateful conversion theorem.  A canonical incomparable
prefix/suffix ticket cannot be replaced by a native nested Hasse pair when
the two coordinates are literal OR-target witnesses.  If the literal ray
witnesses remain upstream and the native pair is used only as a terminal
socket, one binary polarity state is necessary and sufficient to encode the
four-element diamond.  This does not construct the missing all-dimensional
host, transported background, or accepted cap state.

## 0. Canonical ticket and native terminal types

Fix `d>=2`, a Boolean core `C`, and an ordered filler set

\[
                         F=\{f_1,\ldots,f_d\}.
\]

For `1<=j<d`, put

\[
 \begin{aligned}
 X_j&=C\cup\{f_1,\ldots,f_j\},\\
 Y_j&=C\cup\{f_{j+1},\ldots,f_d\},\\
 U&=C\cup F.
 \end{aligned}
\tag{0.1}
\]

These are the abstract values of either canonical folded-C8 antidiagonal,
after absorbing its fixed active labels into `C`.  They obey

\[
 X_j\cap Y_j=C,
 \qquad
 X_j\cup Y_j=U,
 \qquad
 X_j\not\subseteq Y_j,
 \qquad
 Y_j\not\subseteq X_j.
\tag{0.2}
\]

Thus

\[
                         \mathcal D_j=\{C,X_j,Y_j,U\}
\tag{0.3}
\]

is a four-element Boolean diamond.

By contrast, either the first-exit bank or the q1/q2 upper ladder supplies
a native nested pair

\[
                         R\subset V,
 \qquad |V-R|=1.
\tag{0.4}
\]

The physical occurrences of `R,V` may be distinct and already present,
but their availability does not by itself identify their terminal type
with `(X_j,Y_j)`.

## 1. What an exact terminal ticket is allowed to forget

The terminal two-Rado theorem forms its gammoids only after one complete
cap/background state has been fixed.  A complete occurrence record retains
at least

\[
 \begin{gathered}
 \text{logical ticket label},\quad
 \text{occurrence coordinate},\quad
 \text{phase, ray, and role},\\
 \text{physical interval address and capacity},\quad
 \text{terminal type},\quad
 \text{flag, endpoint, guard, and common cap state}.
 \end{gathered}
\tag{1.1}
\]

It may contract internal owners or source-labelled Hasse steps only when a
complete canonical bundle records their full literal semantics.  It may
coinstantiate two roles on one occurrence only when those roles assert the
same occurrence fact in the same cap state.

There is a precise general meaning of the **weakest exact semantic data**.
For complete records `a,b`, write

\[
 a\equiv b
\tag{1.2}
\]

when, in every admitted fixed cap/background context, replacing `a` by `b`
preserves

1. route legality;
2. every terminal target/type assertion;
3. every capacity conflict with every other complete record; and
4. the legal paired-occurrence relation between the two coordinate
   systems.

### Proposition 1.1 (contextual quotient)

The quotient by (1.2) is the coarsest sound terminal signature.  Any
further identification can change a feasible complete selection into an
infeasible one, or conversely.

#### Proof

Every predicate used to define a legal simultaneous selection is constant
on an equivalence class by definition, so replacing records by their
classes is sound.  If two distinct classes are identified, the negation of
(1.2) supplies a context in which one of the four listed properties
differs.  The identification is therefore unsound in that context.
\(\square\)

For the presently proved canonical cross-ray interface, no theorem makes
the exact Boolean target value, phase/role, occurrence address, or complete
cap state contextually redundant.  In particular, `(C,U)` is not an exact
ticket signature: all `d-1` cuts have the same meet and join, while their
two literal targets are different.

If the cut label `j` is retained as part of the logical ticket, then meet,
join, `j`, and an ordered ray role determine the two values in (0.1).
This is the weakest **value-level description** of the canonical pair.
It still does not turn a physical occurrence of value `R` or `V` into a
literal occurrence of value `X_j` or `Y_j`.

## 2. Sharp literal no-go

### Theorem 2.1 (incomparability obstruction)

There is no deterministic replacement of the two literal target
occurrences `(X_j,Y_j)` by the two native occurrences `(R,V)` which both

1. preserves the two target identities; and
2. uses only the two native cells.

More strongly, there is no injective lattice homomorphism from the diamond
`mathcal D_j` to a chain which sends its two atoms to the two members of a
nested pair.

#### Proof

Under literal OR-word semantics, a cell assigned to target `Z` must have
OR value exactly `Z`.  Hence a two-cell identity-preserving replacement
would require, up to swapping,

\[
                         (R,V)=(X_j,Y_j).
\]

But `R,V` are comparable, while `X_j,Y_j` are incomparable by (0.2), a
contradiction.

For the lattice statement, an injective lattice homomorphism is an order
embedding.  Indeed, if `phi(a)<=phi(b)`, then

\[
 \phi(a\cap b)=\phi(a)\cap\phi(b)=\phi(a),
\]

and injectivity gives `a cap b=a`, hence `a<=b`.  Therefore it cannot send
the incomparable atoms `X_j,Y_j` to comparable elements. \(\square\)

The collapse is completely determined even without injectivity.  If a
lattice homomorphism sends

\[
                         X_j\longmapsto R,
 \qquad Y_j\longmapsto V,
 \qquad R<V,
\]

then

\[
 \phi(C)=\phi(X_j\cap Y_j)=R,
 \qquad
 \phi(U)=\phi(X_j\cup Y_j)=V.
\tag{2.1}
\]

Thus it identifies `C` with `X_j` and `Y_j` with `U`.  Reversing the two
atom images gives the symmetric collapse.  These are exactly the two
chain quotients of the diamond which keep its atoms distinct; each loses
one binary distinction.

The simpler meet/join replacement

\[
                         (X_j,Y_j)\longmapsto(C,U)
\tag{2.2}
\]

is nested but is not target preserving.  It also cannot equal the native
Hasse type: its Boolean rank gap is

\[
                         |U-C|=d\ge2,
\tag{2.3}
\]

whereas `|V-R|=1`.

### Corollary 2.2 (sharp physical occurrence lower bound)

If the native cells are required to remain part of the gadget, the number
of additional exact target occurrences needed is at least

\[
             2-\bigl|\{X_j,Y_j\}\cap\{R,V\}\bigr|.
\tag{2.4}
\]

Since a nested pair contains at most one member of an incomparable pair,
this lower bound is at least one.  If neither native value equals a ray
target, as on the generic distinct-rank type, two exact ray occurrences are
necessary.  Existing cells elsewhere in the word may supply them without
increasing word length, but they still consume two occurrence capacities.

## 3. The minimal state extension

The no-go above is about raw Boolean values.  At the level of typed terminal
sockets, the obstruction has an exact one-bit repair.

Let

\[
                         \mathcal N=\{R<V\},
 \qquad \mathcal B=\{0<1\}.
\tag{3.1}
\]

Order the product `mathcal N times mathcal B` coordinatewise.

### Theorem 3.1 (polarized-chain coding)

The map

\[
 \boxed{
 \begin{array}{c|c}
 C&(R,0)\\
 X_j&(R,1)\\
 Y_j&(V,0)\\
 U&(V,1)
 \end{array}}
\tag{3.2}
\]

is a lattice isomorphism from the canonical diamond `mathcal D_j` to
`mathcal N times mathcal B`.

Moreover one binary state is minimal among reversible extensions of the
two-element native chain.

#### Proof

The product of two two-element chains is the four-element Boolean lattice.
The four cover relations

\[
 C<X_j<U,
 \qquad
 C<Y_j<U
\]

map respectively to

\[
 (R,0)<(R,1)<(V,1),
 \qquad
 (R,0)<(V,0)<(V,1).
\]

The two middle images are incomparable.  Hence (3.2) preserves the whole
order, and therefore meet and join.

Without extra state the native chain has only two semantic values and
cannot reversibly encode four distinct diamond values.  Thus a state set
has size at least two.  The binary state in (3.2) attains that lower bound.
\(\square\)

The logical ticket label must still retain the cut `j`.  If all cut labels
are erased and one fixed core has to encode the full family

\[
                         \{C,U,X_j,Y_j:1\le j<d\},
\]

then there are `2d` distinct value types.  A two-point physical chain with
a state set `S` has only `2|S|` codes, so reversibility forces

\[
                         |S|\ge d.
\tag{3.3}
\]

Thus the one-bit statement is exact only because the Rado ground set
already retains the logical ticket/cut label.

The terminal Rado record also already retains a binary occurrence
coordinate and an ordered ray role.  If one fixed phase normalization
identifies that existing role field with `0,1` in (3.2), the polarity bit
requires no new stored field.  What is new is the cap's acceptance of the
**product type** `(native value, role polarity)`.  If the existing role
field cannot be used consistently in both systems, then one new binary
state is necessary by Theorem 3.1.

## 4. Conditional no-new-cell terminal conversion

The state code becomes a correct physical theorem only under socket
semantics.

### Definition 4.1 (polarized diamond socket)

For one logical ticket `i=(C,F,j,...)`, a polarized diamond socket is one
complete canonical record containing

1. two exact upstream occurrence witnesses `x_i,y_i` with values
   `X_j,Y_j`;
2. one native pair of distinct terminal occurrences `r_i,v_i` with values
   `R_i subset V_i`;
3. the fixed code `(R_i,1)` for the prefix role and `(V_i,0)` for the
   suffix role, or the symmetric orientation;
4. the ticket/cut label, common cap state, phase normalization, flags,
   endpoints, guards, and every used capacity; and
5. a declaration that `r_i,v_i` are routing sockets, while literal target
   identity remains certified by `x_i,y_i`.

The record is a conjunction.  Its four occurrences are not four
alternatives in one Rado menu.

### Theorem 4.2 (deterministic polarized-socket conversion)

Fix one complete cap/background state.  Suppose, for every ticket `i` in a
set `I`, there is one polarized diamond socket such that

1. all upstream ray witnesses are legal exact target occurrences;
2. the native pairs `(r_i,v_i)` are pairwise capacity-disjoint over `i`;
3. the state-aware terminal specification accepts the code (3.2);
4. the complete bundles coexist with the transported background; and
5. the paired relation is the deterministic graph selecting this one
   complete bundle for each `i`.

Then the terminal system has a simultaneous two-coordinate linkage of size
`|I|`.  No additional word cell is required beyond the already present ray
witnesses and native terminal banks.

#### Proof

The exact target identities remain at `x_i,y_i`.  Theorem 3.1 gives an
injective, role-preserving terminal code on `(r_i,v_i)`.  Hypothesis 2 makes
the deterministic terminal representatives mutually capacity-disjoint,
and hypothesis 4 includes all background capacities.  Since there is one
fixed complete representative per ticket, no product-of-marginals or
matroid-parity inference is being made.  Selecting all representatives is
the required joint linkage. \(\square\)

This is a genuine no-**new**-cell theorem, not a two-cell theorem: the two
literal ray witnesses remain load-bearing.  If they are absent from the
physical state, Theorem 2.1 applies and the conversion is impossible.

## 5. Exact union-envelope coalescence

There is one still weaker terminal semantics under which the two terminal
coordinates can coalesce on one occurrence.

### Theorem 5.1 (dual-role join coalescence)

Suppose a complete ticket already contains exact occurrences `x_i,y_i` of
`X_j,Y_j`, and an existing occurrence `u_i` of their common envelope

\[
                         U=X_j\cup Y_j.
\tag{5.1}
\]

Assume there are complete source-free bundle incidences

\[
                         x_i\rightsquigarrow u_i,
 \qquad y_i\rightsquigarrow u_i,
\tag{5.2}
\]

and that the terminal specification observes only the declared envelope
`U`, while retaining the logical ticket and the two ray roles, and permits
both roles to coinstantiate the same occurrence fact
`OR(u_i)=U`.  If the `u_i` are distinct over tickets and avoid the
background, all terminal roles coalesce on the `|I|`-element union bank
with no second terminal capacity bank.

#### Proof

The literal ray identities are certified at `x_i,y_i`; (5.2) records their
two complete conjunctive routes.  Both terminal roles assert the same
occurrence fact `OR(u_i)=U`, so dual-role acceptance charges `u_i` once.
Distinctness over `i` gives a full unit-capacity linkage. \(\square\)

For a native nested pair `(R_i,V_i)`, this theorem applies with `u_i=v_i`
only if

\[
                         V_i=U
\tag{5.3}
\]

as an exact Boolean value and the two source-free bundle incidences are
proved.  Mere containment `R_i subset V_i`, or equality of ranks, does not
imply (5.3).  Thus the first-exit and q1/q2 terminal banks do not satisfy
the coalescence premise automatically.

## 6. Minimal remaining gadget and exact frontier

The preceding results give a sharp dichotomy.

### Literal-witness semantics

No state label can change the OR value of a physical interval.  The
minimal escape from Theorem 2.1 is therefore one of:

1. retain the two exact ray occurrences and use the native pair only as a
   socket;
2. provide an exact value- and address-preserving transport of those two
   ray occurrences into the terminal state; or
3. exhibit an existing common-envelope occurrence and prove the dual-role
   join coalescence theorem's hypotheses.

The sharp additional occurrence count is (2.4).

### Socket semantics

The minimal additional semantic gadget is exactly:

\[
 \boxed{
 \text{logical cut label }j
 +\text{one polarity bit (possibly the existing coordinate-role bit)}
 +\text{one deterministic complete paired bundle}.}
\tag{6.1}
\]

Every term is load-bearing:

* without `j`, different antidiagonal cuts have the same meet and union;
* without the polarity bit, the Boolean diamond collapses to a chain;
* without the complete paired bundle, two marginal Rado linkages may choose
  incompatible representatives; and
* without the upstream exact witnesses or an accepted envelope-only
  quotient, target identity is lost.

Accordingly, a deterministic lattice gadget does **not** unconditionally
convert canonical folded-C8 tickets to the existing native nested pair.
What can be proved is the exact polarized-socket theorem above.  The next
construction theorem must either materialize those polarized complete
bundles in one cap/background state, or prove that the actual terminal
predicate factors through the union-envelope quotient of Theorem 5.1.

## 7. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| native diagonal diamond and one-coordinate dual role | `MATH_THEOREM_DIAGONAL_INTERVAL_DIAMOND_SOURCE_FREE_DUAL_ROLE_ROUTER_20260803.md` | `2e71b1f3a7c26c23accf9e3cee9a23ba01ef17658f959b73ac69c622ce2a2802` |
| first-exit nested terminal bank | `MATH_THEOREM_DIAGONAL_FIRST_EXIT_SECOND_TERMINAL_BANK_20260803.md` | `25dc0c20f14254a9f9419caa41912c5fdc480f6fb3178e20822a6e6cd8a89ab0` |
| q1/q2 native two-coordinate ladder | `MATH_THEOREM_DIAGONAL_Q1_Q2_TWO_COORDINATE_UPPER_LADDER_ROUTER_20260803.md` | `dbd2f671d07e1e4c09ecadbbade9e9ea0a55e1dfca4054ead15fd09fbe8a7151` |
| terminal two-cross-ray Rado/gammoid theorem | `MATH_THEOREM_TERMINAL_COMMON_CAP_TWO_CROSS_RAY_RADO_GAMMOID_V2_20260803.md` | `108c4b0ad2adc99d9e9c91df9f1bfdb9f816494670f7473c51e7751f134177cc` |
| folded-C8 antidiagonal address/halo gate | `MATH_THEOREM_THREAD_D_FOLDED_C8_ANTIDIAGONAL_ADDRESS_AND_HALO_GATE_20260801.md` | `ab8519229624c97a1cede8bacdf5b5b60add4fe47035e2a1f61f9031c5afee22` |
| independent folded-address/transport scope audit | `MATH_AUDIT_ZERO_BLOCK_BIRAIL_CROSSMATCH_AND_ADDRESSED_TRANSPORT_SCOPE_20260801.md` | `ccc29b2ae8a5f4036d2a707a84091f0c08b669a378a441fd4e5d3f4da50d88d5` |
