# Heptagonal cap holonomy, duplicate backups, and boundary-history tickets

**Date:** 2026-08-02  
**Status:** unconditional interface algebra.  This note audits and combines the
holonomy extension in
`MATH_THEOREM_HEPTAGONAL_CAP_CIRCULATION_AND_PROSPECTIVE_ABUNDANCE_20260802.md`
with the directed-history port monoid.  It gives an exact cap-support
circulation, its wreath-product exact face, and the phase action on boundary
history tickets.  It does **not** prove that a Pascal, pull-ear, or SCD host
contains the required duplicate caps and compatible path histories.

## 0. Outcome

There are three separate pieces of data in an equivariant endpoint packet.

1. The moving circuit has a group voltage `h`.
2. Its old and new immediate-upper caps have a signed orbit-load boundary
   `z`.
3. Its retained paths have positive and negative boundary-history relations.

The first two pieces are related by a sharp holonomy obstruction only on a
role-preserving cap-transport face.  If every new cap is required to be the
successor old cap with the same retained extension role, then the extension
labels form a parallel section.  Its circuit holonomy must fix the initial
label.  For a free cyclic coordinate action this forces `h=0`.  Thus a
coprime-voltage packet must use a nontrivial cap permutation, duplicate-cap
slack, or a compound return.

The exact duplicate requirement is not heuristic.  If `s(O)` is the old
duplicate slack in cap orbit `O`, cap support survives exactly when

\[
                         s(O)+z(O)\ge0                 \tag{0.1}
\]

for every orbit.  For a sequence of packets, the required slack is the
largest negative prefix load.  These prefix requirements form a closed
max-plus circulation monoid.

Cap feasibility still does not transport residence.  An exact cap
permutation is a labelled element of a wreath product.  Its phase labels act
diagonally on the deletion/insertion history collars.  Every join is governed
by the **relative** phase of its two tickets.  Already at depth one, an exact
cap permutation can turn two distinct collar labels into the same label and
destroy residence.

Consequently the proof-safe regenerative state is

\[
 (h;z,b;\mathcal W_{\rm cap};
   \mathcal R^+_d,\mathcal R^-_d;
   D^+,I^+,D^-,I^-;\text{ opening/topology}),          \tag{0.2}
\]

where `b` is the cap prefix-deficit vector and `mathcal W_cap` is present on
the exact-multiset face.  Raw `Theta(k^7)` heptagon supply proves none of the
duplicate-slack or history-ticket rows in (0.2).

## 1. The signed cap-load circulation

Let a finite group `Gamma` act on the coordinate set and hence on cap sets.
For clarity assume that every cap orbit used below is free.  Let `mathcal O`
be the set of cap orbits.  A quotient packet removes cap representatives
`U_1,...,U_t` and adds `V_1,...,V_t`.  Define

\[
 \mu^-(O)=|\{i:\Gamma U_i=O\}|,
 \qquad
 \mu^+(O)=|\{i:\Gamma V_i=O\}|                         \tag{1.1}
\]

and its signed cap boundary

\[
                    z(O)=\mu^+(O)-\mu^-(O).             \tag{1.2}
\]

Let `L(O)>=1` be the old multiplicity of every physical cap in orbit `O` and
put

\[
                            s(O)=L(O)-1.                 \tag{1.3}
\]

Thus `s` is the duplicate-cap slack above one mandatory witness.

### Theorem 1.1 (exact backup criterion)

The developed packet preserves immediate-upper support exactly when

\[
                            s(O)+z(O)\ge0                \tag{1.4}
\]

for every `O`.  The minimum number of independently plantable duplicate
units needed by this packet is

\[
 B(z)=\sum_O(-z(O))_+.
                                                               \tag{1.5}
\]

Because `sum_O z(O)=0`,

\[
                    B(z)=\frac12\sum_O|z(O)|.           \tag{1.6}
\]

Equivalently, after maximally matching equal old and new cap-orbit
occurrences,

\[
 B(z)=t-\sum_O\min\{\mu^-(O),\mu^+(O)\}.               \tag{1.6a}
\]

#### Proof

Every quotient row develops once through each physical member of its cap
orbit.  Hence the new load in orbit `O` is

\[
                    L(O)-\mu^-(O)+\mu^+(O)=1+s(O)+z(O).
\]

It is positive exactly under (1.4).  Starting from one mandatory copy, the
least required slack at `O` is `(-z(O))_+`; summing gives (1.5).  The total
signed boundary is zero because the packet removes and adds the same number
of rows, proving (1.6).  Cancelling the common part of `mu^-` and `mu^+`
gives (1.6a).
\(\square\)

This count is after cancellation.  Two packets may pay one another's cap
debts, so in general

\[
 B(z_1+z_2)\le B(z_1)+B(z_2).                           \tag{1.7}
\]

### Theorem 1.2 (prefix-safe cap monoid)

Let `A` be a word of atomic factor switches.  For each prefix `A_{<=j}` let
`z_{A,<=j}` be its cumulative signed cap boundary.  Define

\[
 z_A=z_{A,\mathrm{final}},\qquad
 b_A(O)=\max_j\bigl(-z_{A,<=j}(O)\bigr)_+.              \tag{1.8}
\]

An initial slack vector `s` keeps every intermediate factor cap-complete if
and only if

\[
                              s\ge b_A                 \tag{1.9}
\]

coordinatewise.  For concatenated packet words,

\[
\begin{aligned}
 z_{AB}&=z_A+z_B,\\
 b_{AB}&=\max\{b_A,\ b_B-z_A\},                        \tag{1.10}
\end{aligned}
\]

where the maximum and subtraction are coordinatewise.

#### Proof

After a prefix the load above the mandatory copy is `s+z_prefix`.  All
prefixes are legal exactly when its minimum is nonnegative, which is (1.9).
Prefixes of `AB` either lie in `A`, or have boundary `z_A+z_{B,<=j}`.
Taking the largest negative part gives (1.10).  \(\square\)

If duplicate units can be planted on arbitrary cap orbits and only a scalar
reserve `R` is prescribed, a prefix-safe planting exists exactly when
`sum_O b_A(O)<=R`.  In a literal factor the orbit locations of the duplicates
are fixed, so the coordinatewise condition (1.9), not the scalar inequality,
is authoritative.

## 2. The exact face is a wreath-product transport

Suppose `z=0`, so the developed old and new cap multisets agree.  Equality
can be recorded by a permutation `pi in S_t` and group labels `q_i in Gamma`
such that

\[
                         V_i=q_iU_{\pi(i)}.              \tag{2.1}
\]

The pair

\[
                 \mathcal W_{\rm cap}=(\pi,(q_i)_i)
                         \in \Gamma\wr S_t              \tag{2.2}
\]

acts on developed cap occurrences by

\[
                    (i,g)\longmapsto(\pi(i),gq_i).       \tag{2.3}
\]

Conversely every equality of developed cap multisets admits such a labelled
permutation.  This is exactly Theorem 1.1(3) of the heptagon note, written as
an occurrence permutation.

For a cycle `C=(i,pi(i),...,pi^(ell-1)(i))` of `pi`, define its cap-transport
holonomy

\[
                Q_C=q_iq_{\pi(i)}\cdots q_{\pi^{\ell-1}(i)}. \tag{2.4}
\]

Under a regular cyclic action, the developed occurrence cycles over `C` are
the cycles of translation by `Q_C`.  This describes cap occurrence transport;
it does not by itself impose `Q_C=0`.

The vanishing condition appears when one insists that a distinguished
coordinate role be transported consistently.

### Theorem 2.1 (parallel-section holonomy obstruction)

Let the quotient moving circuit have row voltages `a_i`, moving holonomy

\[
                              h=\prod_i a_i,             \tag{2.5}
\]

and retained owners

\[
                         y_i=f_i\cup\{z_i\}.             \tag{2.6}
\]

Assume the natural successor cap transport is forced:

\[
                 \pi(i)=i+1,\qquad q_i=a_i,             \tag{2.7}
\]

and the extension role `z` is preserved.  Then exact cap transport is
equivalent to

\[
                              z_i=a_i z_{i+1}.            \tag{2.8}
\]

In particular

\[
                              z_0=h z_0.                 \tag{2.9}
\]

Thus `h` must lie in the stabilizer of `z_0`.  For a free cyclic coordinate
action, exact role-preserving successor transport forces `h=0`.

#### Proof

The old successor cap is `U_(i+1)=x_(i+1) union {z_(i+1)}`, while the new
row-`i` cap is `V_i=a_i x_(i+1) union {z_i}`.  Under (2.7), equality
`V_i=a_iU_(i+1)` is precisely (2.8).  Multiplication around the circuit
gives (2.9).  \(\square\)

The same statement holds on each cycle of an arbitrary cap permutation
whenever a coordinate role is preserved around that cycle: its cap-cycle
holonomy `Q_C` must stabilize the initial role label.

This is a sharply scoped obstruction.  A cap equality may use a different
permutation or change which element of an `(r+1)`-cap is regarded as the
extension role.  Neither alternative is forbidden by Theorem 2.1.  If those
alternatives are unavailable, nonzero moving holonomy forces at least one
nontransported row and hence at least one backup unit.  It does not force
three units in general.

## 3. Phase transport of boundary-history tickets

Let

\[
                         \mathsf H_d=\Omega^d            \tag{3.1}
\]

be the ordered positive history space and let `Gamma` act diagonally.  For a
path ticket `P`, write

\[
 \mathcal T_d(P)=
   (\mathcal R_d^+(P),\mathcal R_d^-(P),
       D^+(P),I^+(P),D^-(P),I^-(P)).                    \tag{3.2}
\]

Here `mathcal R_d^+` is the insertion-history relation, `mathcal R_d^-` is
its deletion-history dual, and the four collars are stored in their endpoint
frames.  For `q in Gamma`, let `q_*` act on every coordinate label in a
history tuple, collar, or relation.

### Lemma 3.1 (ticket pullback along a cap transport)

Under the cap equality (2.1), an old ticket attached to row `pi(i)` and used
at physical phase `gq_i`, when expressed in the new row-`i` phase-`g` frame,
is

\[
                         q_{i*}\mathcal T_d(P_{\pi(i)}). \tag{3.3}
\]

Thus an exact cap permutation does not automatically preserve decorated
tickets: a literal decorated lift must realize the transformed ticket in
(3.3).

#### Proof

The physical occurrence of every label in the old ticket is acted on by
`gq_i`.  Removing the common new-row phase `g` leaves the diagonal action
of `q_i`.  \(\square\)

Suppose shifted tickets `q_{i*}P` and `q_{j*}Q` are concatenated without a
connector.  The exact positive cross-collar inequalities are

\[
 q_i I_u^+(P)\ne q_jD_v^+(Q)
       \qquad(u+v\le d+1),                              \tag{3.4}
\]

or equivalently

\[
 I_u^+(P)\ne(q_i^{-1}q_j)D_v^+(Q).                     \tag{3.5}
\]

The negative inequalities are the dual ones.  Hence only the relative phase
`q_i^(-1)q_j` appears at a join, but it is indispensable.

With a connector transition `(a,b)` between the tickets, the positive tests
become

\[
\begin{aligned}
 a&\ne q_i I_u^+(P) &&(1\le u\le d),\\
 b&\ne q_j D_v^+(Q) &&(1\le v\le d),\\
 q_iI_u^+(P)&\ne q_jD_v^+(Q) &&(u+v\le d),             \tag{3.6}
\end{aligned}
\]

together with the deletion/insertion-dual tests for negative residence.
These are the phase-labelled version of the directed-history collar theorem.

### Theorem 3.2 (an exact cap-connector ticket count)

Fix a cap `U` of size `n`.  Let the left endpoint be `U-{alpha}` and the
right endpoint `U-{beta}`.  The connector transition deletes `beta` and
inserts `alpha`.  Assume all old positive and negative cross-collar tests
between the two retained paths already hold.  Put

\[
 E_\alpha=D^+\cup I^-,\qquad
 E_\beta=I^+\cup D^-,                                  \tag{3.7}
\]

where `I^+` is the left past-insertion collar, `D^+` the right
future-deletion collar, `I^-` the left past-deletion collar, and `D^-` the
right future-insertion collar.  Then the number of oriented biresident
connector choices is exactly

\[
 |U\setminus E_\alpha|\,|U\setminus E_\beta|
       -|U\setminus(E_\alpha\cup E_\beta)|.             \tag{3.8}
\]

In particular, if each forbidden set has size at most `2d`, the count is at
least

\[
                         (n-2d)^2-n.                    \tag{3.9}
\]

#### Proof

Positive residence requires `beta notin I^+` and
`alpha notin D^+`.  Negative residence requires `alpha notin I^-` and
`beta notin D^-`.  Thus `alpha` and `beta` may be chosen from the two sets
in (3.8).  They must be distinct; the subtracted term is exactly the number
of equal choices.  The lower bound follows by bounding both first factors
below by `n-2d` and the diagonal term above by `n`.  \(\square\)

The formula is equivariant: translating `U,E_alpha,E_beta` by a common group
element does not change the count.  It does not remove the relative-phase
condition (3.5) when the two endpoint tickets are transported by different
cap labels.

In the central regime `n=k/2+O(1)` and `d=O(sqrt(k))`, (3.9) is
`Theta(k^2)`.  Thus, once a cap and two compatible collars have been supplied,
the bare biresident Johnson connector is abundant.  This does not assert that
its two endpoint owners, lower colour, or compiler cell are unused in the
ambient protected factor.

## 4. Two minimal obstructions

The projections in (0.2) are genuinely independent.

### 4.1 Coprime voltage versus a fixed retained role

Under the hypotheses of Theorem 2.1, any nonzero `h` under a free cyclic
action is impossible with zero cap backup.  This is the smallest cap-side
obstruction: one may escape it with a nontrivial cap permutation or one
nontransported row plus one suitable duplicate, but raw moving-circuit
abundance alone does not choose either escape.

### 4.2 Exact caps versus history

At depth one, take two unshifted tickets with

\[
                         I_1^+(P)=0,\qquad D_1^+(Q)=1    \tag{4.1}
\]

under a `Z_3` coordinate action.  They pass the unshifted join test.  An
exact cap transport with ticket phases `q_P=1,q_Q=0` changes the two labels
to `1,1`, so (3.4) fails.  The cap multiset can remain exact throughout;
the obstruction lives entirely in the decorated lift.

Depth one and two tickets are minimal: at depth zero there is no residence
row, and with one open ticket there is no cross-boundary equality to violate.
This example is an interface counterexample, not a claim that every such
phase pair occurs in a Boolean heptagon host.

## 5. The `k=17` coprime-holonomy calibration

For the authenticated `2,822 -> 2,754` endpoint `C14`, the quotient moving
holonomy is

\[
                              h=5\pmod {17}.             \tag{5.1}
\]

It therefore develops to one moving circuit of row length `7*17=119`.
Four of the seven quotient cap occurrences are transported.  The remaining
three old cap orbits are replaced by three new cap orbits, so

\[
                              B(z)=3.                    \tag{5.2}
\]

Every net-lost old cap has load two.  Its one duplicate unit pays precisely
the corresponding coordinate of `(-z)_+`.  Thus (1.4) is tight on three
orbits.  The independent factor replay also proves a negative total boundary
history drift, but this is one literal accepted history and not an abundance
statement.

This calibration proves that coprime voltage, one-cycle topology, cap
backups, and biresidence can coexist.  It does not show that a positive
fraction of the prospective twisted seven-run atlas has those three backup
orbits or the required history tickets.

## 6. Consequence for the protected Pascal/pull-ear recurrence

The cap-exact phasewise rooted heptagon family has `Theta(k^7)` choices and
nonanchor central-token load `O(k^6)`.  Twisted seven-run anchors have the
larger prospective count

\[
 {r-1\choose6}{k-r-1\choose6}(7!)^2\,\Omega(k)^7,       \tag{6.1}
\]

before cap closure and history planting.  Neither count addresses the live
rows of (0.2).

The exact next lemma is therefore not another central-supply lemma.  It is a
**balanced decorated-backup planting theorem**:

> choose, for each bounded protected Pascal/pull-ear task, one packet and a
> bounded accepting return so that the combined cap prefix vector satisfies
> `s>=b`, every transported endpoint has the phase-adjusted positive and
> negative history ticket of Section 3, and the selected openings retain the
> regenerative pivot collar.

The one-aperture pivot can reset the history relation after a legal triangular
input guard, but it does not change the cap boundary `z` and cannot create a
duplicate cap.  Conversely, cap backups do not repair a failed relative-phase
collar.  These two resources must be planted jointly.

A proof by the existing prospective-count ratio would require two new load
bounds:

1. each required duplicate-cap orbit excludes only `O(k^6)` candidates in a
   different rooted atlas; and
2. each complete phase-labelled boundary-history ticket excludes only
   `O(dk^6)` candidates.

The heptagon theorem proves the analogous bound only for central named
tokens.  Until these two rows are established, `Theta(k^7)` supply cannot be
converted into a regenerative all-`k` packet theorem.

Upper shadows below the immediate cap row, source antecedents, component
joining/opening, and the terminal common-cap compiler remain separate gates.
