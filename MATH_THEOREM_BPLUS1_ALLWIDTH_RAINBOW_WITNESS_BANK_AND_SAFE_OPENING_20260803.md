# All-width witness banks for the protected `B+1` Catalan path

**Date:** 2026-08-03  
**Status:** exact witness-selection, component-omission Hall, safe-opening,
and retained-channel theorems.  No computation is used.  The result gives
a proof-safe all-width interface; it does not prove that the required
rainbow witness bank exists in every dimension.

## 0. Outcome

Immediate-upper surjectivity and arbitrary-width upper coverage are
different resources.  The protected `B+1` path route admits two exact ways
to keep them synchronized.

### Born-linear opening face

For an all-width-complete Hamilton cycle, every proper upper target `X` has
a family `mathcal W_X` of cyclic interval witnesses.  Its forced-cut core is

\[
                         K_X=\bigcap_{I\in\mathcal W_X}E(I).
\tag{0.1}
\]

If `D_1` is the set of edge occurrences whose immediate-upper colour is
duplicated and `P` is the protected pivot bank, then an opening preserving
the pivot, every immediate-upper colour, and every old upper target exists
if and only if

\[
 \boxed{
 D_1\setminus\left(P\cup\bigcup_XK_X\right)\ne\varnothing.}
\tag{0.2}
\]

This is the exact safe-opening test.  The large duplicate count guarantees
many q1-safe cuts, but does not by itself imply (0.2).

### Rooted-forest face

Let `F` be an upper-q1-surjective directed cycle cover relative to a fixed
root matching `M_0`.  For every proper higher target `X`, choose one old
path witness `I_X` inside a component of `F`.  Put

\[
                         H_\sigma=P\cup\bigcup_XE(I_X).
\tag{0.3}
\]

There is an upper-exact representative set `Q_0 subseteq F` containing the
pivot and one old witness of every `X` exactly when the witnesses can be
chosen so that `H_sigma` contains at most one occurrence of every
immediate-upper colour.  Call this a **rainbow witness bank**.

For a cycle cover, making `Q_0` a rooted Catalan forest adds precisely one
capacitated component-omission Hall system.  Write

\[
 \mu_R=|\{e\in F:u(e)=R\}|,
 \qquad b_R=\mu_R-1,                                   \tag{0.4}
\]

and let `N_R^sigma` be the factor components containing an occurrence of
colour `R` outside `H_sigma`.  Then such a forest exists iff

\[
 \boxed{
 |Y|\le
 \sum_{R:N_R^\sigma\cap Y\ne\varnothing}b_R
 \qquad(Y\subseteq\operatorname {Comp}(F)).}          \tag{0.5}
\]

For one Hamilton cycle, (0.5) is automatic.  For several cycles it is the
exact residual obstruction.

Once `Q_0` exists, any Hamiltonizing connector which adds edges without
deleting `H_sigma` retains all selected witnesses.  Hence the ordered
component-port Hall theorem supplies an all-width-complete Hamilton path
with no further upper check.  On the nonacyclic route, every cycle-absorbing
switch must avoid `H_sigma`, or must explicitly redeliver the targets whose
selected witness it cuts.

Finally, the monotone pivot itself contributes no new arbitrary-width loss:
under

\[
                          X\subseteq A_{-1}\cup A_1,    \tag{0.6}
\]

every old source interval transports with exactly the same OR.  Thus the
all-width gate belongs to the owner Hamiltonization/opening stage, not to
the final one-letter pivot insertion.

## 1. Witness notation and exact retained channel

Let `G` be a maximum-degree-two graph on distinct middle-owner occurrences.
For a required upper target `X`, let

\[
 \mathcal W_G(X)={I:I\text{ is a path or cyclic interval of }G,
                         \ \bigcup_{v\in I}v=X\}.       \tag{1.1}
\]

Write `E(I)` for the internal adjacency set of `I`.  If `H` is a final
chronology on the same owners, put

\[
                         D(G,H)=E(G)\setminus E(H).     \tag{1.2}
\]

### Theorem 1.1 (retained-witness equivalence)

An old target `X` has a retained old witness in `H` iff

\[
             \exists I\in\mathcal W_G(X):
                         E(I)\cap D(G,H)=\varnothing.   \tag{1.3}
\]

Equivalently, for a family `mathcal U`, all targets retain an old witness iff
there is a selector

\[
                         \sigma:X\mapsto I_X\in\mathcal W_G(X)
\tag{1.4}

such that

\[
              D(G,H)\cap H_\sigma=\varnothing,
              \qquad H_\sigma=\bigcup_XE(I_X).         \tag{1.5}

### Proof

An old path remains consecutive in `H` exactly when every one of its old
internal adjacencies remains selected.  This is (1.3).  If every target has
such a survivor, choose one for each target and take their union, giving
(1.4)--(1.5).  Conversely (1.5) retains every selected witness.  `square`

The quantifier exchange in (1.4)--(1.5) is useful: an all-target statement
is one protected edge bank, but the bank must be chosen jointly with the
Hamiltonization.

New seams may redeliver a target even when (1.3) fails.  Thus Theorem 1.1 is
necessary and sufficient for the retained-old channel, and sufficient but
not necessary for the final all-width deck when new witnesses are allowed.

### Corollary 1.2 (sharp black-box deletion radius)

Let

\[
 \tau_G(X)=\min\{|D|:D\cap E(I)\ne\varnothing
                  \text{ for every }I\in\mathcal W_G(X)\}.
\tag{1.6}
\]

Then every Hamiltonization deleting at most `b` old edges preserves `X`
through the old channel whenever `tau_G(X)>=b+1`.  This is sharp uniformly
over all `b`-edge deletion sets.  On one **linear** old path,
`tau_G(X)` is also the maximum number of pairwise edge-disjoint old
witnesses.  On a cyclic component the witness sets are circular arcs; the
exact transversal definition (1.6) remains valid, but equality with the
packing number is not asserted without first fixing a linearizing cut.

### Proof

A deletion set of size below the transversal number cannot meet every
witness.  If `tau_G(X)<=b`, a transversal of at most `b` edges destroys all
old witnesses.  On a linear path, interval packing equals interval piercing
by the greedy smallest-right-endpoint argument.  `square`

For `z` serial octagons, the union of original edges ever deleted has size
at most `4z`; hence `tau_G(X)>=4z+1` is a universal but deliberately strong
sufficient guard.  Exact support-specific safety is (1.3).

## 2. The exact one-cut core

Assume now that `G` is one directed Hamilton cycle.  For every proper
covered target `X`, define `K_X` by (0.1).  The full-ground target is omitted
from the definition because the whole opened path always witnesses it.

### Theorem 2.1 (forced-cut core)

Opening cycle edge `e` retains `X` as a nonwrapping linear interval iff

\[
                              e\notin K_X.              \tag{2.1}
\]

### Proof

A cyclic witness becomes a linear interval after cutting `e` exactly when
its internal edge set avoids `e`.  Such a witness exists iff not every
member of `mathcal W_G(X)` contains `e`, which is (2.1).  `square`

There is also an explicit interval form.  Restrict the cycle to the owners
contained in `X` and take its maximal compatible cyclic blocks.  A block can
witness `X` only when the union of all its owners is `X`.

* If no compatible block witnesses `X`, then `K_X=E(G)` by the empty-family
  convention.
* If at least two different compatible blocks witness `X`, their edge
  interiors are disjoint, so `K_X=emptyset`.
* If exactly one block witnesses `X`, then `K_X` is the interval between
  the latest possible left endpoint and earliest possible right endpoint of
  an `X`-witness inside that block.

Thus the all-width forbidden-cut bank is an explicit union of cyclic edge
intervals.  It need not be small or empty.

Let `u(e)` be the immediate-upper colour of edge `e`, and let

\[
             D_1=\{e:|u^{-1}(u(e))|\ge2\}.             \tag{2.2}
\]

### Theorem 2.2 (protected all-width safe opening)

For an all-width-complete upper-q1-surjective Hamilton cycle and a protected
edge bank `P`, a cut preserving `P`, every immediate-upper colour, and every
proper upper target exists iff (0.2) holds.

### Proof

The cut must avoid `P`.  Its q1 colour survives exactly when another
occurrence exists, namely when the cut lies in `D_1`.  By Theorem 2.1, every
proper higher target survives exactly when the cut avoids every `K_X`.
These three conditions are jointly (0.2).  `square`

The duplicated-provider count proves only that `D_1-P` is nonempty when the
protected bank is small.  Higher forced cores may still cover all of it.
Therefore q1-safe opening is not an all-width theorem.

## 3. Rainbow witness-bank equivalence

Let `F` be a directed cycle cover relative to `M_0`.  Assume its immediate-
upper map

\[
                         u:E(F)\longrightarrow\mathcal U_1
\tag{3.1}
\]

is surjective.  Let `P subseteq E(F)` be a protected pivot bank.  Assume
the colours on `P` are distinct; otherwise no upper-exact representative
set can contain it.

Let `mathcal U_+` be a family of proper higher targets already witnessed
inside components of `F`.  A **rainbow witness selector** chooses

\[
                   I_X\in\mathcal W_F(X)
                         \qquad(X\in\mathcal U_+)       \tag{3.2}

such that the edge set

\[
                   H_\sigma=P\cup\bigcup_XE(I_X)       \tag{3.3}

contains at most one edge of each colour under `u`.

### Theorem 3.1 (rainbow bank iff upper-exact protected support)

The following are equivalent.

1. There is a set `Q_0 subseteq E(F)` containing exactly one occurrence of
   every immediate-upper colour, containing `P`, and containing one complete
   old witness of every target in `mathcal U_+`.
2. A rainbow witness selector exists.

### Proof

Assume Item 1.  Choose inside `Q_0` one witness for every higher target.
Their union with `P` is a subset of `Q_0`, and `Q_0` contains only one edge
of each immediate-upper colour.  Hence it is rainbow.

Conversely, start from `H_sigma`.  For every colour used by `H_sigma`, keep
that unique occurrence.  For every unused immediate-upper colour, keep an
arbitrary occurrence of that colour in `F`.  The resulting `Q_0` contains
exactly one occurrence per colour and contains `H_sigma`.  `square`

This is an exact occurrence-level condition.  Separate existence of a
witness for each target is insufficient: witnesses for two targets may
force two different occurrences of the same immediate-upper colour.

## 4. Adding the rooted-forest condition

Let the directed-cycle components of `F` form `mathcal K`.  For every
immediate-upper colour `R`, put

\[
                 \mu_R=|u^{-1}(R)|,
                 \qquad b_R=\mu_R-1.                  \tag{4.1}
\]

Fix a rainbow selector `sigma`.  Define

\[
 N_R^\sigma=\{K\in\mathcal K:
     K\text{ contains an occurrence of }R
            \text{ outside }H_\sigma\}.               \tag{4.2}
\]

### Theorem 4.1 (all-width component-omission Hall)

There is an upper-exact rooted forest `Q_0 subseteq F` which contains
`H_sigma` iff the capacitated Hall inequalities (0.5) hold.

Every resulting `Q_0` contains one retained old witness for every target in
`mathcal U_+`.  If `F` spans `W` owners and `|mathcal U_1|=U`, then it has
exactly `W-U=Cat_m` path components.

### Proof

Choosing one occurrence of every colour is equivalent to deleting exactly
`b_R` occurrences of colour `R`.  Because `H_sigma` is rainbow, there are
at least `b_R` occurrences of `R` outside `H_sigma`: exactly `b_R` if the
bank uses `R`, and `b_R+1` otherwise.

A subset of a directed cycle cover is a forest iff at least one edge is
deleted from every cycle.  Designate one such deletion per component.  A
colour `R` can supply at most `b_R` designated deletions and can hit
component `K` exactly when `K in N_R^sigma`.  The capacitated Hall theorem
therefore gives exactly (0.5).

After selecting the designated deletions, extend them colour by colour to
exactly `b_R` deletions, which is possible by the preceding availability
count.  The complement `Q_0` is upper exact, contains `H_sigma`, and breaks
every cycle.  Conversely every such `Q_0` supplies a deletion set; choose
one of its deletions from each old cycle to obtain the saturating capacitated
matching and hence (0.5).

Finally, `Q_0` is a maximum-degree-two forest with `U` edges on `W` rooted
vertices, so it has `W-U` path components.  `square`

### Corollary 4.2 (one-cycle collapse)

If `F` is one Hamilton cycle, every rainbow witness selector extends to an
upper-exact rooted Catalan forest containing its bank.

### Proof

There is one component.  Since

\[
                  \sum_Rb_R=|E(F)|-|\mathcal U_1|=W-U>0,
\]

some repeated colour has positive deletion capacity.  Its rainbow protected
bank occupies at most one occurrence, leaving a deletable occurrence on the
unique cycle.  Thus the only nonempty Hall cut holds.  `square`

## 5. Hamiltonization while retaining the bank

Fix a `Q_0` from Theorem 4.1 and form its protected free-component port graph
as in
`MATH_THEOREM_BPLUS1_PROTECTED_COMPONENT_PORT_HALL_AND_OCTAGON_HAMILTONIZATION_20260803.md`.

### Theorem 5.1 (direct all-width Catalan connector)

If some ordered prescribed-endpoint component-port Hall system produces a
directed Hamilton path `Q_0 union Q_1`, then this path

* contains the protected pivot bank `P`;
* is immediate-upper surjective; and
* retains one old interval witness of every target in `mathcal U_+`.

### Proof

The connector adds edges and deletes none from `Q_0`.  Hence it retains
`H_sigma` and all its selected witness paths.  The forest already contains
one edge of every immediate-upper colour.  Ordered port Hall makes the
union one Hamilton path.  `square`

On the one-defect nonacyclic route, the connector first gives one path plus
cycles.  A subsequent palette-preserving switch sequence remains all-width
safe through the protected old channel whenever none of its deleted edges
lies in `H_sigma`.  More generally Theorem 1.1 is the exact targetwise test;
newly created paths may explicitly redeliver a cut witness.

Therefore the following is an exact sufficient chain:

\[
 \boxed{
 \begin{array}{c}
 \text{rainbow witness selector}\\
 +\ \text{component-omission Hall}\\
 +\ \text{ordered component-port Hall}
 \end{array}
 \Longrightarrow
 \text{protected all-width upper-complete Hamilton path}.}
\tag{5.1}
\]

Within the strategy requiring every higher witness to lie already in
`Q_0`, all three rows are also necessary.  A general final Hamilton path
may instead create new cross-component witnesses, so (5.1) is not claimed
necessary for every possible construction.

## 6. Exact switch-sequence formulation

Let `Pi` be any family of legal Hamiltonization plans from reference `G`.
For `pi in Pi`, let `D_pi` be its set of deleted reference edges, and let
`N_pi(X)` assert that the final new seams contain a newly verified witness
of `X`.

### Theorem 6.1 (plan-specific all-width criterion)

A plan `pi` is all-width safe exactly when

\[
 \boxed{
 \forall X:\quad
 \bigl[\exists I\in\mathcal W_G(X),\ E(I)\cap D_\pi=\varnothing\bigr]
 \ \lor\ N_\pi(X).}                                  \tag{6.1}
\]

If no new delivery is credited, this is equivalent to the existence of one
witness selector `sigma` with

\[
                              D_\pi\cap H_\sigma=\varnothing. \tag{6.2}
\]

### Proof

Every final witness is either a retained old path or uses at least one new
adjacency.  Theorem 1.1 characterizes the first class, and `N_pi(X)` is
exactly the second.  This proves (6.1).  Setting every `N_pi(X)` false and
exchanging the finite existential choices gives (6.2).  `square`

Equation (6.1), rather than q1 palette equality, is the exact guard for a
serial C6/C8 Hamiltonization.  There is no monotonicity in the number of
switches: an extra deleted edge can hit a last old witness, while a new seam
can redeliver it.

## 7. The monotone pivot does not reopen the upper gate

Suppose the all-width-complete owner Hamilton path has been realized by a
source word, and insert the protected pivot letter `X` at an old cut

\[
                         \cdots,A_{-1}\mid A_1,\cdots
\]

satisfying (0.6).  Transport every old source interval by its convex hull in
the inserted word.

### Theorem 7.1 (pivot transparency at every width)

Every transported old interval has exactly the same OR after insertion.
Consequently every arbitrary-width upper witness certified before insertion
survives literally afterward.

### Proof

A one-sided interval is unchanged.  A crossing interval gains only `X` and
already contains both `A_(-1)` and `A_1`; condition (0.6) makes `X`
redundant in its union.  `square`

Thus the sharp-aperture pivot's remaining difficulties are owner flatness,
residence, named lower flags, and common cap.  It does not require another
arbitrary-width upper reconstruction once the pre-insertion path has a
protected witness bank.

## 8. Proof-safe frontier

The all-width topology problem is now separated into exact objects.

1. **One-cycle face:** the forced-core test (0.2) is necessary and
   sufficient for an all-width-safe protected opening.
2. **Rooted-forest retained-channel face:** a rainbow witness selector plus
   component-omission Hall is necessary and sufficient for an upper-exact
   forest carrying one old witness per target.
3. **Direct connector face:** ordered component-port Hall then preserves
   those witnesses automatically.
4. **Switch face:** (6.1) is the exact targetwise retained-or-redelivered
   test.
5. **Pivot insertion:** monotonicity (0.6) transports the complete old deck
   literally.

What remains unproved all-dimensionally is the first genuinely correlated
choice: a protected rainbow witness selector satisfying the omission and
connector Hall systems, or alternatively a safe cut satisfying (0.2).
No q1 count, duplicate surplus, or palette-preserving local identity forces
that choice.
