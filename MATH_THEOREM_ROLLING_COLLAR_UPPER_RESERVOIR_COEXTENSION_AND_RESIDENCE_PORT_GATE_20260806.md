# The complete rolling-collar bank coextends with the upper-damage reservoir, and residence has an exact nested-port gate

**Date:** 2026-08-06  
**Method:** stabilizer-orbit separation, the protected Ore theorem, and
literal rolling-window algebra; no computation or search  
**Status:** unconditional asymptotic decorated-skeleton theorem and exact
residence/topology reduction.  The complete low-target rolling-collar bank
and the clipped-resident common-core upper-damage reservoir coexist in one
spanning owner/lower-`q1` two-factor.  Every protected local upper witness
and every low-target source ticket survives.  The theorem does not make the
unprotected completion resident, globally upper-complete, or bounded-component.

## 1. The two protected banks

Work in

\[
 \mathcal L=\binom{[2m-1]}{m-1},\qquad
 \mathcal U=\binom{[2m-1]}m,
 \qquad W=|\mathcal L|=|\mathcal U|,
\tag{1.1}
\]

and let `d=O(sqrt(m))`, with `4d+4<=m` for all sufficiently large `m`.

Let `R` be the co-selected hybrid clipped-resident common-core reservoir of

* `MATH_THEOREM_COMMON_CORE_HYBRID_CLIPPED_RESIDENT_WITNESS_RESERVOIR_20260804.md`,
* `MATH_THEOREM_UNIFORM_FORCED_FACET_SPREAD_ELIMINATES_OPTIONAL_CO_SMALL_CORES_20260804.md`, and
* `MATH_THEOREM_COSELECTED_RESERVOIR_SMALL_CUT_CLOSURE_AND_PROTECTED_FACTOR_20260804.md`.

Thus `R` is an incidence path forest with

\[
 |E(R)|=O(m2^m),\qquad
 \ell_R(x)\le10,\qquad
 e_R^{\rm priv}(x)\le10,\qquad
 z_U(R)\le9,
\tag{1.2}
\]

and with at most `2m` exceptional top-bank endpoint owners.  Its owner
paths are `d`-clipped resident, have disjoint immediate lower and upper
colours, and contain one literal owner-union witness for every target in
the full common-core hinge-ring damage family.

For every

\[
 S\in\mathcal S_d:=\{S\subseteq[2m-1]:1\le |S|\le d\},
\tag{1.3}
\]

let `P_S` be a rolling-star collar from
`MATH_THEOREM_ARBITRARY_LOW_TARGET_ROLLING_STAR_COLLAR_AND_Q1_EXTENSION_20260806.md`.
Write

\[
 L_d=|\mathcal S_d|=2^{o(m)}.
\tag{1.4}
\]

## 2. Cross-reservoir halo separation

For any protected incidence bank `H`, enlarge its full halo to contain

1. its protected owners and lower colours;
2. every lower facet of a protected owner;
3. every owner containing a protected lower colour;
4. every immediate-upper colour of a protected owner edge; and
5. the owner-neighbour roles used to distinguish an endpoint as private
   rather than exceptional.

The enlarged halo of `R` has size

\[
                         2^{m+o(m)}.                 \tag{2.1}
\]

Indeed `R` has `O(m2^m)` incidences and every one-neighbourhood costs only
a polynomial factor.

Fix a target `S` pointwise and apply a uniform permutation of its
complement to all background and nontarget marker labels of `P_S`.  Every
one of its `O(md)` halo roles has rank `m+O(1)`, meets `S` in at most `d`
labels, and has stabilizer orbit

\[
 \binom{2m-1-|S|}{m+O(d)-O(d)}=2^{2m-o(m)}.          \tag{2.2}
\]

### Lemma 2.1 (joint halo separation)

The collars may be selected so that

* their enlarged halos are pairwise disjoint; and
* every collar halo is disjoint from the enlarged halo of `R`.

#### Proof

For collar--collar collisions, the number of ordered role pairs is

\[
 O(m^2d^2L_d^2)=2^{o(m)},
\]

and one fixed collision has probability `2^{-2m+o(m)}`.

For collar--reservoir collisions, the number of ordered role pairs is

\[
 2^{o(m)}\,2^{m+o(m)}=2^{m+o(m)},
\]

while the same orbit estimate gives probability `2^{-2m+o(m)}` for a
fixed compatible equality.  The total cross-collision probability is
`2^{-m+o(m)}`.  The sum of the two union bounds is less than one.  Hence a
simultaneously separating choice exists.  \(\square\)

Put

\[
                         P=R\cup\bigcup_{S\in\mathcal S_d}P_S.
\tag{2.3}
\]

## 3. The protected-factor constants do not worsen

### Lemma 3.1 (maximum, not sum, of the exposure ledgers)

For the joint bank `P`,

\[
 \boxed{
 \ell_P(x)\le10,\qquad
 e_P^{\rm priv}(x)\le10,\qquad
 z_U(P)\le9.}
\tag{3.1}
\]

The only exceptional endpoint owners are the at most `2m` old top-bank
endpoints of `R`.

#### Proof

The enlarged-halo separation says that a lower star or owner star exposed
by `R` is exposed by no rolling collar, and a star exposed by one rolling
collar is exposed by no other collar.  Therefore the exposure at a star is
the contribution of one bank, not the sum of contributions from several
banks.

The reservoir bounds are `(1.2)`.  The rolling-window calculation gives
the sharper collar bounds

\[
 \ell_{P_S}(x)\le2,qquad
 e_{P_S}^{\rm priv}(x)\le2,qquad
 z_U(P_S)\le2.
\]

Every rolling-collar endpoint is private in the sense used by the exact
path-forest loss identity: its unique protected lower neighbour belongs to
the protected lower palette.  It need not be added to the exceptional
top-bank family.  Taking the maximum of the two ledgers proves `(3.1)`.
\(\square\)

Also

\[
 |E(P)|=O(m2^m)+O(dL_d)=O(m2^m).                    \tag{3.2}
\]

### Theorem 3.2 (joint protected `q1` extension)

For all sufficiently large `m`, the bank `P` extends to a spanning
two-factor of the middle-levels incidence graph.

#### Proof

The proof of the co-selected-reservoir protected-factor theorem uses only

1. the lower-star loss bound;
2. the private-endpoint exposure bound;
3. the `2m` exceptional top endpoints;
4. the forced-facet bound; and
5. the `O(m2^m)` near-shadow localization scale.

Equations `(3.1)`--`(3.2)` leave every one of these inputs unchanged.
Thus its small-shore proof, optional co-small proof, and bipartite
`b`-matching integrality apply verbatim to `P`.  \(\square\)

## 4. Decoration retained by the joint skeleton

The rolling collar

\[
 T_i=B\cup\{z_i,z_{i+1},\ldots,z_{i+d}\}
\tag{4.1}
\]

is `d`-clipped resident.  A marker occurs on one interval of owner indices;
if that interval meets neither path endpoint, it has exactly `d+1`
vertices.  Background coordinates occur throughout.  Consequently the
joint protected bank has all of the following simultaneously:

1. one literal source interval with OR `S` for every `S` of rank at most
   `d`;
2. pairwise distinct protected owners and immediate lower colours;
3. pairwise distinct protected immediate-upper colours;
4. clipped residence on every protected path;
5. every common-core upper-damage witness of `R`; and
6. one exact spanning owner/lower-`q1` two-factor containing the whole
   bank.

This is stronger than either protected-factor theorem separately: the
complete low source bank and the all-width hinge-damage backup bank now
coexist in the same exact `q1` factor.

It is not a global residence or upper-completeness theorem.  The residual
edges supplied by the `b`-matching proof are undecorated.

## 5. Exact residence signature of an open rolling collar

The remaining residence condition at a collar endpoint has a closed form.
Use the linear collar indices

\[
 -d\le i\le A+1,
\]

and define its left and right boundary markers by

\[
 \ell_j=z_{-d+j},\qquad r_j=z_{A+1+j}
 \qquad(0\le j\le d).
\tag{5.1}
\]

Let `V_{-h}` be the `h`-th owner immediately before `T_{-d}` in a cyclic
completion, and let `V_h` be the `h`-th owner immediately after
`T_{A+1}`.

### Theorem 5.1 (nested endpoint-port criterion)

Every positive run which meets the displayed collar has length at least
`d+1` if and only if

\[
 \boxed{
 \{\ell_0,\ldots,\ell_{d-h}\}\subseteq V_{-h}
 \quad(1\le h\le d),}
\tag{5.2}
\]

and

\[
 \boxed{
 \{r_h,r_{h+1},\ldots,r_d\}\subseteq V_h
 \quad(1\le h\le d).}
\tag{5.3}
\]

#### Proof

Inside the collar, `ell_j` occurs in exactly the first `j+1` owners.  If
`j<d`, its cyclic positive run must therefore extend through the preceding
`d-j` owners.  This is equivalent, after reversing the two quantifiers, to
`(5.2)`.

Similarly `r_j` occurs in exactly the last `d-j+1` collar owners.  It must
extend through the following `j` owners, which is equivalent to `(5.3)`.
Background coordinates already have a collar run longer than `d`, and no
other collar coordinate is boundary-truncated.  Thus the conditions are
also sufficient for all runs meeting the collar.  Positive runs supported
entirely in the exterior remain the responsibility of the exterior
completion.  \(\square\)

The endpoint state is therefore not one untyped socket.  It is a pair of
oppositely nested `d`-step containment flags.  Any claimed resident
completion must price these flags in the same physical owner chronology as
its topology and upper witnesses.

## 6. Every two collars have an explicit resident bridge

The nested flags can in fact be discharged prospectively.  Consider two
successive collars with backgrounds `B,B'`, outgoing marker window

\[
                         R=\{r_0,r_1,\ldots,r_d\},
\]

and incoming marker window

\[
                         L=\{\ell_0,\ell_1,\ldots,\ell_d\}.
\]

Assume

\[
 R\cap L=\varnothing,qquad
 (R\cup L)\cap(B\cup B')=\varnothing.                \tag{6.1}
\]

First put

\[
 U_t=B\cup\{r_t,r_{t+1},\ldots,r_d\}
          \cup\{\ell_0,\ldots,\ell_{t-1}\},
 \qquad0\le t\le d+1.                                \tag{6.2}
\]

Next order

\[
 B\setminus B'=\{b_1,\ldots,b_q\},\qquad
 B'\setminus B=\{b'_1,\ldots,b'_q\},
\]

and put

\[
 H_s=\left(B-\{b_1,\ldots,b_s\}
                +\{b'_1,\ldots,b'_s\}\right)\cup L,
 \qquad0\le s\le q.                                  \tag{6.3}
\]

Here `U_(d+1)=H_0`, and `H_q=B' union L` is the first owner of the
next collar.

### Theorem 6.1 (ordered marker/background bridge)

The concatenation of `(U_t)` and `(H_s)` is a simple Johnson geodesic from
the last owner of the first collar to the first owner of the second.  Every
positive coordinate run meeting this bridge and either collar has length
at least `d+1`.  The bridge has at most `m` Johnson transitions.

#### Proof

At transition `t`, `(6.2)` deletes `r_t` and inserts `ell_t`.  Equation
`(6.3)` then deletes `b_s` and inserts `b'_s`.  By `(6.1)` all deleted and
inserted labels are disjoint, so this is one monotone Johnson geodesic.
Its number of transitions is

\[
 d+1+|B\setminus B'|le d+1+(m-d-1)=m.
\]

Inside the first collar, `r_j` has already appeared for `d-j+1`
consecutive owners.  It remains in `U_1,...,U_j`, adding exactly `j`
owners before it is deleted.  Its completed run therefore has length
`d+1`.

The coordinate `ell_j` is inserted in `U_(j+1)` and remains through the
rest of both bridge phases.  Before counting the first `j+1` owners of the
next collar, it occurs in at least `d-j` earlier bridge owners.  Its run
therefore also has length at least `d+1`.

A coordinate of `B-B'` occurs throughout the first collar and the marker
phase before it is deleted.  A coordinate of `B'-B` persists throughout
the whole next collar after it is inserted.  Coordinates in `B cap B'`
never leave.  These runs are all longer than `d`.  This proves residence.
Monotonicity of the exchanged-coordinate lists proves simplicity.  \(\square\)

The bridge is the literal realization of `(5.2)`--`(5.3)`: the outgoing
markers are deleted in increasing required-delay order, while the incoming
markers are inserted in decreasing required-history order.

## 7. The entire low bank fits on one positive-resident protected cycle

The pair bridge can be packed simultaneously, rather than used only once.

### Theorem 7.1 (one-cycle positive-resident rolling-collar bank)

For all sufficiently large `m`, the targets in `mathcal S_d` may be
ordered and their rolling collars chosen so that:

1. the targets are cyclically ordered and every successive pair, including
   the last-to-first pair, is joined by a bridge from Theorem 6.1;
2. the resulting object `J` is one simple Johnson cycle;
3. all immediate lower and immediate upper colours of `J` are distinct;
4. every nonconstant positive run and every nonconstant zero gap on `J`
   has length at least `d+1`;
5. every `S in mathcal S_d` retains its literal singleton-thinned source
   interval; and
6. `|E(J)|=2^{o(m)}` at incidence level.

Moreover `J` can be selected with its enlarged halo disjoint from the
common-core reservoir `R`.  Consequently `R union J` extends to a spanning
owner/lower-`q1` two-factor.

#### Proof

Order the targets cyclically as `S_1,...,S_(L_d)`, with subscripts read
modulo `L_d`.  For collar `i`, choose
pairwise distinct auxiliary left and right markers outside `S_i`.  Over
every radius-three neighbourhood in the target order, make all auxiliary
marker banks disjoint from one another and from every target in that
neighbourhood.  The targets themselves need not be disjoint.  Since every
such local forbidden union has size `O(d)=o(m)`, this is possible greedily.

Choose `B_i` uniformly among the `(m-d-1)`-sets avoiding the complete
target-plus-auxiliary marker banks of every collar at distance at most
three from `i`.  There are

\[
 \binom{2m-O(d)}{m-d-1}=2^{2m-o(m)}                 \tag{7.1}
\]

choices.  In particular the cross-disjointness `(6.1)` holds for every
successive pair, including the last and first collars.  Choose the orders
of the two background differences uniformly and insert every cyclic bridge
`(6.2)`--`(6.3)`.

Within a collar or bridge, simplicity follows from rolling-window
simplicity and Theorem 6.1.  Among roles having a common background
variable, the complete incoming marker bank, outgoing marker bank, or
changed-background profile distinguishes every nonshared role.  The local
auxiliary-marker separation from all nearby targets prevents a marker-swap
role from masquerading as a collar role.  In particular, two adjacent
background bridges contain different full incoming marker banks, and the
backgrounds of either bridge avoid the other bank.  Thus the only
equalities among roles whose background supports overlap are the intended
shared endpoints.

Consider now any nonidentical pair of enlarged-halo roles not settled by
the preceding local profile check.  This includes all owner roles, all
lower facets of protected owners, all owners above protected lower
colours, and all immediate-upper roles.  Their background supports are
disjoint.  Conditional on
the `O(d)` fixed or locally chosen labels of one role, its law is invariant
under their pointwise stabilizer and independent of the other role.
Conditional also on its intersection pattern with those labels, its rank
is `m+O(1)`, so every such stabilizer orbit has size

\[
                         2^{2m-o(m)}.                 \tag{7.2}
\]

Hence a fixed nonlocal role pair collides with probability at most
`2^{-2m+o(m)}`.  There are

\[
 O(m^4L_d^2)=2^{o(m)}                               \tag{7.3}
\]

role pairs.  The union bound selects all data with no nonlocal collision.
The same calculation against the `2^{m+o(m)}` enlarged reservoir halo has
total probability `2^{-m+o(m)}`.  Therefore one selection is simultaneously
simple in all three ranks and avoids `R`.

Theorem 6.1 closes every seam, including the last-to-first seam.  The
rolling calculation closes every run internal to a collar.  Thus every
cyclic positive run in `J` has length at least `d+1`.  Every owner
window and adjacent maximal-envelope position used in the proof of the
target ticket lies inside its retained collar.  Hence the identity
`intersection_(h=0)^d T_(p-h)=P_p` and the singleton thinning are unchanged
by the bridges.

For zero gaps, first observe that no bridge deletes and reinserts the same
coordinate: its deletion and insertion banks are disjoint.  A background
coordinate which disappears and later returns is absent throughout at
least one complete intervening collar, because every `B_i` avoids the
marker banks in its radius-three neighbourhood.  An auxiliary marker is
not reused within that neighbourhood.  The only remaining possible nearby
reuse is a coordinate belonging to two successive fixed targets.  Its
first marker run ends before the outgoing bridge and its next marker run
starts after that bridge; `(6.2)` alone has `d+1` transitions.  Hence this
zero gap also has length at least `d+1`.  Every more distant reuse has a
still longer gap.  This proves the zero-gap assertion.

Because every cyclic positive run of `J` has length at least `d+1`, the
standard maximal-antecedent theorem gives a cyclic source antecedent for
the whole owner cycle.  At every selected target position its maximal
letter and two adjacent envelopes are exactly the retained rolling-collar
ones, so the mandatory core is the target singleton.  All target blocks
may therefore be thinned simultaneously; their physical positions are
disjoint and every owner window retains its required forced cores.

One collar plus its outgoing bridge uses `O(m)` owners.  Thus the complete
cycle has `O(mL_d)=2^{o(m)}` incidence edges.  Its enlarged-halo separation
gives the same bounds `(3.1)` as the disjoint collar bank.  Apply the
general maximum-degree-two protected Ore criterion.  The cyclic component
has no endpoint-loss term, while all small-shore, co-small, and
near-shadow estimates from Theorem 3.2 are unchanged.  Hence `R union J`
extends to a spanning two-factor.  \(\square\)

The complete low bank now contributes one cyclically bi-resident
protected component.  It does not force `L_d` components and exports no
unfinished residence boundary.  This removes both the collar-specific
component and residence rows from the decorated-completion gate.

## 8. Cyclic residence is easy but traps every target component

There is a useful sharp comparison.  Choose `2d+2` pairwise distinct
markers cyclically, include the ordered target `S` on consecutive marker
positions, and put

\[
 P_i=B\cup\{z_i\},\qquad
 T_i=B\cup\{z_i,z_{i+1},\ldots,z_{i+d}\},
 \qquad i\in\mathbb Z/(2d+2)\mathbb Z.
\tag{8.1}
\]

The coordinate count is

\[
 |B|+2d+2=m+d+1\le2m-1.
\]

### Theorem 8.1 (resident cyclic rolling ticket)

The owners `(T_i)` form a simple cyclic Johnson path.  Its immediate lower
and upper colours are simple, every nonconstant coordinate run has length
exactly `d+1`, and

\[
 \bigcap_{h=0}^{d}T_{p-h}=P_p.
\tag{8.2}
\]

Thinning the consecutive target positions to singleton letters therefore
gives a cyclic resident source word containing `S` as a literal interval.

#### Proof

Consecutive length-`d+1` marker windows exchange `z_i` for `z_(i+d+1)`.
Cyclic windows of lengths `d`, `d+1`, and `d+2` are all distinct because
their common ambient cycle has length `2d+2` and all markers are distinct.
This proves simplicity of the owner and two immediate palettes.

A marker lies in exactly `d+1` consecutive owner windows.  Equation `(8.2)`
follows because the `d+1` backward windows have the unique common marker
`z_p`.  The mandatory-core calculation is consequently the same as for
the linear rolling collar, and singleton thinning is legal.  \(\square\)

The complete family of these cycles can again be chosen with disjoint full
halos and can be coextended with `R` by the same protected-Ore proof.  Here
one uses the general maximum-degree-two Ore criterion, not the literal
path-forest statement of Theorem 3.2.  In the small-shore loss identity a
protected cyclic component has no endpoint contribution, while its
singleton loss is still at most two.  The co-small forced-facet and
near-shadow inputs are unchanged.  Thus every estimate in Sections 2--3
only improves.

### Proposition 8.2 (topology barrier)

Any spanning two-factor which retains every edge of one cyclic ticket for
each `S in mathcal S_d` has at least `L_d` components.

#### Proof

Every vertex of a protected cyclic ticket already has degree two in that
ticket.  A containing two-factor can attach no further incidence at any of
its vertices.  Halo disjointness makes the tickets vertex-disjoint, so each
is a separate factor component.  \(\square\)

Thus closing every collar locally solves residence in exactly the wrong
way for bounded topology.  A successful global construction must either

* keep collars open and satisfy the nested port conditions `(5.2)`--`(5.3)`;
  or
* delete at least one edge from essentially every cyclic ticket and use a
  value-preserving, upper-safe source rethread to fuse them.

An ordinary protected-factor extension proves neither alternative.

## 9. Sharpened decorated-completion gate

After Theorem 7.1, the remaining all-dimensional statement can be written
without any local low-source, internal collar-residence, collar-component,
or local upper-damage supply clause.

> **Nested-port relative completion.**  Complete the joint protected bank
> in one labelled chronology so that:
>
> 1. retain `J` as one component, or open one of its bridge edges by an
>    upper-safe fusion into the residual chronology;
> 2. make the residual owner paths resident, enforce the required zero-gap
>    state, and ensure their seams form only
>    `O(1)` components;
> 3. the fixed PBBS whole-fan bank, or an occurrence-complete replacement,
>    supplies every upper target outside the already protected hinge-damage
>    family;
> 4. all cuts are upper-safe; and
> 5. the same source chronology transports the terminal compiler/common-cap
>    state.

The exact new information is that all low literal tickets, one connected
internally resident host for them, and the complete localized upper-damage
reservoir are mutually compatible in one exact `q1` factor.  The unresolved
issue is one relative chronological extension of the **residual** factor,
together with global upper occurrence retention, an optional one-edge
fusion of `J`, and the terminal compiler state.

## 10. Dependencies and scope

Used as inputs:

* `MATH_THEOREM_ARBITRARY_LOW_TARGET_ROLLING_STAR_COLLAR_AND_Q1_EXTENSION_20260806.md`;
* `MATH_THEOREM_ALL_LOW_ROLLING_COLLAR_BANK_Q1_FACTOR_EXTENSION_20260806.md`;
* `MATH_THEOREM_COMMON_CORE_HYBRID_CLIPPED_RESIDENT_WITNESS_RESERVOIR_20260804.md`;
* `MATH_THEOREM_UNIFORM_FORCED_FACET_SPREAD_ELIMINATES_OPTIONAL_CO_SMALL_CORES_20260804.md`; and
* `MATH_THEOREM_COSELECTED_RESERVOIR_SMALL_CUT_CLOSURE_AND_PROTECTED_FACTOR_20260804.md`.

Not proved here:

* a resident antecedent for the arbitrary residual factor;
* preservation of the full PBBS whole-fan section;
* an `O(1)`-component connector;
* an upper-safe linear opening;
* a terminal common cap; or
* `nu(k)<=B(k)+O(1)`.
