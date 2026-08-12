# Cross-audit: protected Middle-Levels occurrence lift, opening loss, and parity

**Date:** 2026-08-04  
**Method:** independent symbolic derivation only; no search, numerical
experiment, or computational construction.  The companion audit was not
used as a premise.

**Audited theorem:**
`MATH_THEOREM_PROTECTED_ML_FACTOR_OCCURRENCE_LIFT_AND_OPENING_PARITY_20260804.md`,
SHA256
`a455c5804840e7bf13f90b44b4076fa46339a9d8e2247bb192ed140cb7ccb262`.

## 0. Verdict

The mathematical conclusions pass.  I made four scope-hardening edits to
the theorem while auditing it:

1. “edge-private prefix” now explicitly means an edge-private halfport and
   empty interior, not a private lower source or owner-cell alias;
2. repeated singleton labels and repeated upper-turn values are separated
   from occurrence-node collisions;
3. the parity theorem is explicitly restricted to roles on which reversal
   acts by one component bit; and
4. the Hamilton opening corollary is strengthened from the sufficient
   edge-count test to the exact lower-support test, including the useful
   two-coordinate case.

None of these changes weakens or repairs a false displayed formula.  They
make the capacity and phase scope fail-closed.

## 1. Serialization and address uniqueness

Let `C` be a component of the spanning two-factor.  Because the graph is
bipartite and the factor is simple, after an orientation and an upper-shore
root are chosen it has the form

\[
 U_0-L_0-U_1-L_1-\cdots-U_{\ell-1}-L_{\ell-1}-U_0.
\tag{1.1}
\]

The vertices in each displayed shore are distinct.  Since
`|L_j|=m-1`, `|U_j|=|U_(j+1)|=m`, and both adjacent owners contain `L_j`,
there are unique coordinates

\[
 a_j\in U_j\setminus L_j,\qquad
 b_j\in U_{j+1}\setminus L_j.
\]

They are distinct: equality would give `U_j=U_(j+1)`.  Hence

\[
 U_j=L_j\cup\{a_j\},\qquad
 U_{j+1}=L_j\cup\{b_j\}.
\tag{1.2}
\]

Every factor incidence is uniquely one of

\[
 U_jL_j\quad\hbox{or}\quad L_jU_{j+1}.
\]

Thus the assignments

\[
 U_jL_j\mapsto(C,j,-;L_j,U_j,a_j),\qquad
 L_jU_{j+1}\mapsto(C,j,+;L_j,U_{j+1},b_j)
\tag{1.3}
\]

are injective, and they are surjective onto the two declared half-turns at
every turn.  The component, turn index, and side already make the address
unique; the set values and singleton label are exact attached data.

There is no hidden length-four component.  If two distinct lower sets
`L,L'` share a rank-`m` upper set, then `|L union L'|=m` and every common
rank-`m` upper neighbour must equal `L union L'`.  They cannot have a
second one.  Therefore every component has at least three lower turns:

\[
 \ell\ge3.
\tag{1.4}
\]

## 2. Exact q1 and upper-turn identities

Equation (1.2) gives, without an injectivity assumption on the resulting
colours,

\[
 U_j\cap U_{j+1}=L_j,
 \qquad
 U_j\cup U_{j+1}=L_j\cup\{a_j,b_j\}.
\tag{2.1}
\]

The first value is the complete lower q1 turn and has rank `m-1`; the
second is the complete upper q1 turn and has rank `m+1`.  Different turns
may have the same upper value.  Likewise different incidence edges may
carry the same singleton coordinate label.  Neither repetition identifies
their occurrence addresses.

## 3. Collision and alias ledger

For a selected edge bank `H`, make one source node for each lower-turn
occurrence and one halfport node for each factor edge.  The incidence prefix
is a single directed arc from the source of its lower endpoint to its
edge-labelled halfport.  It has no interior.

Consequently:

* a halfport has load exactly one, because factor edges and halfport
  addresses are in bijection;
* a lower-turn source has load exactly `d_H(L)`;
* after quotienting the two halfports at an upper owner to its single owner
  cell, that owner-cell occurrence has load exactly `d_H(U)`.

There is no fourth occurrence-node type in this one-arc skeleton, so this is
the exact forced occurrence collision ledger.  It does **not** price a
different quotient which identifies equal coordinate labels or equal upper
turn values.  Nor does it embed the arc in a residual common-cap graph.

Thus the privacy claim is exact but deliberately local:

\[
 \boxed{\text{distinct halfports and empty interiors}}
\]

do not imply distinct lower sources, distinct owner-cell gates, active cap
capacity, or private suffixes.

## 4. Component parity

Fix a reference orientation and let `sigma_C(e)` be the side bit of an
incidence.  The only orientation choice on `C` is a bit `eta_C`: keeping
the orientation uses `eta_C=0`, while reversal swaps predecessor and
successor at every turn and uses `eta_C=1`.  A requested role labelling
`q` is therefore realizable precisely when

\[
 q(e)=\sigma_C(e)\mathbin\oplus\eta_C
 \qquad(e\in H\cap E(C)).
\tag{4.1}
\]

Such an `eta_C` exists if and only if

\[
 q(e)\mathbin\oplus\sigma_C(e)
\]

is constant over the protected edges of that component.  The condition is
vacuous on components containing none.  A cyclic shift by whole upper
turns preserves every local side, so it contributes no second bit.

At a lower vertex its two incidences have opposite side bits.  The same is
true at an upper vertex: one incident edge is the plus half of the preceding
turn and the other the minus half of the following turn.  Hence prescribing
equal side roles to either complete pair is impossible.

This proves the theorem only for role systems whose reversal action is the
one-bit action (4.1).  Absolute root-dependent occurrence phases require an
additional reduction before this criterion applies.

## 5. Opening loss and its sharp universal bound

Open `C` by deleting the owner transition through a lower turn `K_C`.
Exactly the two factor incidences at `K_C` cease to be internal half-turns.
Their protected subset has cardinality `d_P(K_C)`.  Choices on different
components are independent, so the exact loss and its optimum are

\[
 \operatorname{loss}(K)=\sum_Cd_P(K_C),
 \qquad
 \operatorname{loss}_{\min}
   =\sum_C\min_{L\in\mathcal L(C)}d_P(L).
\tag{5.1}
\]

For `b_C=|P cap E(C)|` and
`ell_C=|mathcal L(C)|`, every protected edge is counted at exactly one
lower endpoint.  Therefore

\[
 \sum_{L\in\mathcal L(C)}d_P(L)=b_C,
 \qquad
 \min_Ld_P(L)\le {b_C\over\ell_C}\le {b_C\over3}.
\tag{5.2}
\]

After summing, the left side is an integer, so

\[
 \operatorname{loss}_{\min}
 \le\left\lfloor {|P|\over3}\right\rfloor.
\tag{5.3}
\]

A lossless opening exists exactly when every component contains a lower
turn outside the lower support of `P`.  For one Hamilton component this is
equivalent to

\[
 \operatorname{supp}_{\mathcal L}(P)\ne\mathcal L.
\tag{5.4}
\]

The theorem's scalar corollary `|P|<|mathcal L|` implies (5.4), but is not
necessary.  In particular, if a two-coordinate protected bank is supported
on `iota(I)` and `|I|<|mathcal L|`, a Hamilton factor has a lossless opening
even when `2|I|>=|mathcal L|`.

The two exposed endpoint remnants are not internal q1 occurrences.  Any
reuse of them is correctly left to a separate boundary theorem.

## 6. One- and two-coordinate consequences

For one coordinate, `iota` is left-injective and `mu_0` is right-injective.
Thus all selected edges have distinct lower-turn sources, owner values, and
halfports.  The factor supplies exact singleton labels and empty-interior
prefixes.  Activation inside the cap still remains external.

For two coordinates, the sequential selection gives

\[
 \mu_0(i)\ne\mu_1(i).
\tag{6.1}
\]

The two selected incidences at `iota(i)` are therefore distinct.  A
completed two-factor has degree exactly two at this lower vertex, so those
incidences exhaust the turn and become its two opposite halfports.  Across
the whole bank:

* all `2|I|` edge-halfport addresses are distinct;
* each coordinate is right-injective;
* an owner value has union multiplicity at most two;
* multiplicity two can only consist of one edge from each coordinate;
* those two edge-halfports are distinct but quotient to the one owner-cell
  occurrence and have opposite side roles.

This checks the exact distinction between a halfport-capacity model and an
owner-cell-capacity model.  It also confirms why the factor does not provide
two independent units at a shared lower source: simultaneous routing of both
coordinate tickets needs an external source-multiplicity premise.

## 7. Final proof boundary

The theorem unconditionally supplies a serialized support-level object:

\[
 \text{factor incidence}
 \longmapsto
 \text{turn occurrence + side + singleton label + private halfport}.
\]

It does not supply any of the following:

1. occurrence-faithful activation in the residual cap after a compensation
   linkage;
2. a decision that halfport capacity, rather than owner-cell capacity, is
   the physical resource;
3. two source units for two simultaneously routed tickets at one lower
   turn;
4. typed, mutually disjoint suffixes to unused sinks;
5. a common product state for two occurrence coordinates; or
6. Johnson-safe, upper-transparent, resident joins of the opened paths.

Accordingly the theorem closes the exact factor-serialization and local
containment-prefix row, but not the common-cap router or the global carrier.
