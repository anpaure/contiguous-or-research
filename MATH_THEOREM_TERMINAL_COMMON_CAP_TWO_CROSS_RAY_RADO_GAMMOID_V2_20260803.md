# Terminal common-cap linkage for two occurrence-labelled cross-ray systems

**Date:** 2026-08-03  
**Status:** exact abstract strict-gammoid/Rado theorem and conditional
common-cap corollary. The theorem separates frozen background routes from
adaptive background contraction, handles structural zeros, and treats the
two physical occurrence coordinates of the union of the canonical
cross-ray matchings. It does not infer the required occurrence-labelled
lifting from value-level ray matchings.

## 0. Result

Fix one complete common-cap/guard state. Let \(I\) be a cap-independent set
of logical terminal ticket labels. Here \(p\in\{0,1\}\) indexes the two
physical occurrence coordinates required of every ticket in the **union**
of the two canonical cross-ray matchings; it does not index those two
matchings. In each occurrence system, protect the transported background
and retain the complete physical occurrence menu of every ticket. Subject
to the product-closure and capacity-separation hypotheses in Section 2,
Rado gives a matroid \(R_p\) on \(I\). A common compiler selects a set
independent in both \(R_0\) and \(R_1\).

If \(N_p\) is the residual gammoid, \(A_{p,i}\) is the literal entry menu of
ticket \(i\), and

\[
 A_p(J)=\bigcup_{i\in J}A_{p,i},
\]

then the exact common deficiency is

\[
\boxed{
 \delta=
 \max_{\substack{J_0,J_1\subseteq I\\J_0\cap J_1=\varnothing}}
 \left[
 |J_0|-r_{N_0}(A_0(J_0))
 +|J_1|-r_{N_1}(A_1(J_1))
 \right].}
\tag{0.1}
\]

Thus \(\delta\le K\) is an all-ticket-subset theorem. Menger converts
(0.1) into an exact all-cut theorem.

Let

\[
 Z=\{i:\text{\(i\) is a loop in \(R_0\) or in \(R_1\)}\}.
\]

Then structural zeros separate exactly:

\[
 \boxed{\delta_I=|Z|+\delta_{I\setminus Z}.}
\tag{0.2}
\]

If \(|Z|\le z\) and both residual ray systems lose at most \(k_p\) ranks on
every ticket subset, then

\[
 \boxed{\delta\le z+k_0+k_1.}
\tag{0.3}
\]

Consequently, two occurrence-exact cross-ray linkages plus an
occurrence-exact transported background have \(O(1)\) terminal deficiency
when their exceptional ticket set and their two residual cut defects are
\(O(1)\), all cross-system capacities have been resolved, and every
phase-pair of representatives is a legal complete ticket bundle. Exact
private side-cell ray matchings and exact background transport give
deficiency zero only under those same lifting hypotheses.

## 1. Fixed cap state and literal occurrences

Let \({\cal C}\) be the family of complete terminal cap states. A state
\(c\in{\cal C}\) fixes:

- every common declared state and flag;
- every physical occurrence row or interval cell;
- every endpoint, deadline, and guard, and thereby determines every
  structural zero;
- every shared unit-capacity resource; and
- the transported background semantics.

No graph is formed before \(c\) is fixed. Feasible cap choices need not form
a matroid.

Let \(I\) be one cap-independent set of logical ticket labels. The cap
\(c\) assigns the common declared state and flags of every \(i\in I\);
thus every matroid below has the same logical ground set as \(c\) varies.
Equivalently, one may restrict \({\cal C}\) to cap states compatible with
one state-labelled ground set fixed in advance. For \(p\in\{0,1\}\), let

\[
 A_{p,i}^c
\]

be the complete set of entry ports for ticket \(i\) in system \(p\). A port
record retains at least

\[
 (i,c,p,\text{ray},\text{role},\text{physical row/cell},
   \text{flag},\text{endpoint},\text{guard footprint}).
\tag{1.1}
\]

Equal masks at different addresses are different ports. Two occurrences
sharing one physical resource pass through the same capacity-one vertex.
Two distinct physical resources with the same value retain multiplicity two.
System 0 and system 1 may use different physical occurrence rows. The
common requirement is the declared state/flags fixed by \(c\); literal
tuple equality is not imposed unless chronology or the specification makes
it part of \(K_i^c\).

Let \(D_p^c\) be the unit-vertex-split directed network and \(T_p^c\) its
terminal bank. Linkable port sets form the strict gammoid

\[
 M_p^c=L(D_p^c,T_p^c).
\tag{1.2}
\]

### Transported background

Let \(B_p^c\) be an independent occurrence-labelled background set of size
\(b_p\).

If the named background paths are frozen and private, remove their used
capacities and terminal slots before forming the residual network. Writing
those named routes as \(Q_p^c\), define

\[
 N_{p,\mathrm{fr}}^c
 =L(D_p^c-\operatorname{cap}(Q_p^c),
     T_p^c-T(Q_p^c)).
\tag{1.3}
\]

This deletion model is the definition of the **frozen** problem whenever
the named routes are literal and private from the admitted residual
routes. It agrees with adaptive matroid contraction only under a direct-sum
separation (or another separately proved equality of the two residual
rank functions). Deleting one arbitrary realization is not matroid
contraction.

If adaptive background recourse is allowed, protect its service by matroid
contraction:

\[
 N_{p,\mathrm{ad}}^c=M_p^c/B_p^c,
\qquad
 r_{N_{p,\mathrm{ad}}^c}(X)
 =\lambda_p^c(B_p^c\cup X,T_p^c)-b_p,
\tag{1.4}
\]

where \(\lambda_p^c\) is maximum vertex-disjoint linkage size. This may
reroute paths from the fixed authenticated background entry set \(B_p^c\).
It does not allow the background tickets to switch among alternative
occurrence labels. That stronger recourse requires a Rado matroid for the
background tickets followed by contraction of those ticket elements.

Choose exactly one of (1.3) and (1.4) for each \(p\), and denote it by
\(N_p^c\). Every ray menu must lie in its ground set; in the adaptive case,

\[
 A_{p,i}^c\subseteq E(M_p^c)\setminus B_p^c.
\tag{1.5}
\]

The ray menus are static in one fully materialized terminal state.
Candidate-created hosts that exist only when another candidate is selected
are not unconditional ports. Legal own-new-host self-support may be encoded
inside that ticket's complete canonical route; mutual support between
different tickets is not a fixed-menu gammoid unless the activating block
is retained as one exact element.

## 2. The two Rado matroids

For \(J\subseteq I\), put

\[
 A_p^c(J)=\bigcup_{i\in J}A_{p,i}^c.
\tag{2.1}
\]

A set \(S\subseteq I\) is system-\(p\) feasible when it has representatives
\(a_i\in A_{p,i}^c\) whose representative set is independent in \(N_p^c\).
Each representative must encode a complete canonical route for the entire
system-\(p\) occurrence block of that logical ticket; a menu lists
alternatives, not several conjunctive atoms. Rado's theorem makes these
feasible sets a matroid \(R_p^c\) on \(I\), with
rank

\[
\boxed{
 \rho_p^c(S)=
 \min_{J\subseteq S}
 \left(|S\setminus J|+r_{N_p^c}(A_p^c(J))\right).}
\tag{2.2}
\]

For each ticket \(i\), let

\[
 K_i^c\subseteq A_{0,i}^c\times A_{1,i}^c
\tag{2.3}
\]

be its legal paired-occurrence relation. The two-system reduction requires
**global product closure**: for every \(S\subseteq I\), any system-0
representative linkage for \(S\) and any system-1 representative linkage
for \(S\) combine to one legal physical bank after \(c\). Ticketwise, a
necessary component and a sufficient form when no cross-ticket
cross-system constraint remains is

\[
 K_i^c=A_{0,i}^c\times A_{1,i}^c,
\tag{2.4}
\]

or that \(c\) fixes one deterministic canonical bundle. Otherwise two
marginal Rado matroids forget a correlation and need not describe the
logical tickets. Ticketwise rectangularity alone is not sufficient if a
cross-ticket constraint still couples the two systems.

The reduction also assumes that, after \(c\) is imposed, the remaining
system-0 and system-1 capacity vertices are conditionally separate. A
genuinely shared capacity must be allocated or reserved by \(c\), then
removed from the other system. Merely retaining it in one combined network
does not prove a two-matroid representation: a shared vertex required by
both phase paths is an immediate counterexample. A new exact joint
gammoid/Rado representation would have to be proved before Edmonds'
two-matroid theorem could be applied.

### Theorem 2.1 (exact common-label min-max)

Let

\[
 \nu(c)=\max\{|S|:S\in R_0^c\cap R_1^c\},
\qquad
 \delta(c)=|I|-\nu(c).
\tag{2.5}
\]

Then

\[
 \nu(c)=
 \min_{U\subseteq I}
 \left(\rho_0^c(U)+\rho_1^c(I\setminus U)\right),
\tag{2.6}
\]

and (0.1) holds with \(N_p=N_p^c\) and \(A_p=A_p^c\).

#### Proof

Equation (2.6) is Edmonds' two-matroid intersection theorem. Substitute
(2.2). For \(J_0\subseteq U\) and \(J_1\subseteq I\setminus U\), the
summand is

\[
\begin{aligned}
 &|U\setminus J_0|+r_{N_0}(A_0(J_0))
 +|(I\setminus U)\setminus J_1|+r_{N_1}(A_1(J_1))\\
 &=|I|-\left[
 |J_0|-r_{N_0}(A_0(J_0))
 +|J_1|-r_{N_1}(A_1(J_1))\right].
\end{aligned}
\]

As \(U\) varies, the possible pairs \((J_0,J_1)\) are exactly the disjoint
pairs. Taking the minimum and subtracting from \(|I|\) proves (0.1).
\(\square\)

The disjointness of \(J_0,J_1\) shares one omission budget between the two
systems. Separate phase deficiencies provide a valid additive upper bound,
but need not be exact.

## 3. Exact all-cut form

For a port set \(X\), add a super-source with one capacity-one arc to
each start in \(X\), node-split every physical unit-capacity vertex, and
connect the correctly typed terminal bank to a super-sink. Let

\[
 \gamma_{p,C}^c(X)
\]

be the capacity of such a cut \(C\) in the original network, and let
\(\gamma_{p,C}^{c,Q_p}(X)\) be the corresponding capacity after the named
frozen paths \(Q_p^c\), their used capacities, and their used sink slots
have been removed. Define the uniform pair

\[
\bigl(\Gamma_{p,C}^c(X),d_p\bigr)=
\begin{cases}
\bigl(\gamma_{p,C}^c(B_p^c\cup X),b_p\bigr),
   &\text{adaptive contraction},\\[2mm]
\bigl(\gamma_{p,C}^{c,Q_p}(X),0\bigr),
   &\text{frozen private background}.
\end{cases}
\tag{3.1}
\]

Menger and the two definitions in Section 1 give

\[
 r_{N_p^c}(X)=\min_C\Gamma_{p,C}^c(X)-d_p.
\tag{3.2}
\]

### Theorem 3.1 (all-subset/all-cut criterion)

The fixed state \(c\) has common deficiency at most \(K\) if and only if,
for every disjoint \(J_0,J_1\subseteq I\) and every pair of cuts
\(C_0,C_1\),

\[
\boxed{
 \Gamma_{0,C_0}^c(A_0^c(J_0))
 +\Gamma_{1,C_1}^c(A_1^c(J_1))
 \ge d_0+d_1+|J_0|+|J_1|-K.}
\tag{3.3}
\]

#### Proof

Substitute (3.2) into (0.1). Since the negative of a minimum is a maximum,

\[
\begin{aligned}
\delta(c)=
\max_{\substack{J_0\cap J_1=\varnothing\\C_0,C_1}}
 \{&|J_0|+|J_1|+d_0+d_1\\
   &-\Gamma_{0,C_0}^c(A_0^c(J_0))
    -\Gamma_{1,C_1}^c(A_1^c(J_1))\}.
\end{aligned}
\tag{3.4}
\]

This maximum is at most \(K\) exactly when (3.3) holds. \(\square\)

A full-union linkage rank is not enough. Rado requires every ticket subset.
For example, one ticket may own many independent ports while every other
ticket has only the same single port.

## 4. Structural zeros

Define

\[
 Z(c)=
 \{i\in I:\rho_0^c(\{i\})=0
             \text{ or }\rho_1^c(\{i\})=0\}.
\tag{4.1}
\]

A raw empty menu is sufficient but not necessary. A nonempty menu consisting
only of loops after background contraction is also a structural zero.
Menus used for this test include every legal own-new-host route and all
admitted phase-specific occurrences under \(c\).
The zero-threshold shores in the abstract birail problem are not structural
zeros: they are intended to be cross-matched to the opposite positive shore.

### Lemma 4.1 (exact zero separation)

\[
 \delta_I(c)=|Z(c)|+\delta_{I\setminus Z(c)}(c).
\tag{4.2}
\]

#### Proof

Every member of \(Z(c)\) is a loop in at least one of the two matroids and
belongs to no common independent set. Deleting \(Z(c)\) leaves the maximum
common independent-set size unchanged. Comparing the two ground-set sizes
proves (4.2). \(\square\)

Arbitrary forbidden incidences outside \(Z(c)\) remain inside the ranks and
cuts. They cannot be charged one by one. In particular, \(m\) tickets may
all have the same sole nonloop port; no ticket is a structural zero, but the
deficiency is \(m-1\).

## 5. Bounded-deficiency theorem

### Theorem 5.1

Fix \(c\), put \(I'=I\setminus Z(c)\), and suppose

\[
 |Z(c)|\le z
\tag{5.1}
\]

and

\[
 r_{N_p^c}(A_p^c(J))\ge |J|-k_p
 \qquad
 (J\subseteq I',\ p=0,1).
\tag{5.2}
\]

Then

\[
 \boxed{\delta(c)\le z+k_0+k_1.}
\tag{5.3}
\]

If the total target universe is the disjoint union of the logical ray
tickets \(I\) and a background target set, and the same fixed-\(c\)
frozen residual or adaptive contraction services all but \(\beta\) of those
background targets, total terminal deficiency is at most

\[
 \boxed{\beta+z+k_0+k_1.}
\tag{5.4}
\]

#### Proof

By (2.2) and (5.2),

\[
 \rho_p^c(S)\ge |S|-k_p
 \qquad(S\subseteq I').
\]

Therefore (2.6) gives

\[
 \nu_{I'}(c)\ge
 \min_{U\subseteq I'}
 \left(|U|-k_0+|I'\setminus U|-k_1\right)
 =|I'|-k_0-k_1.
\]

Apply Lemma 4.1 and then add the independently omitted background targets.
\(\square\)

### Canonical linkage certificate

Put \(I'=I\setminus Z(c)\), and let \(E_p\subseteq I'\). Suppose system
\(p\) has pairwise vertex-disjoint, correctly typed routes for every ticket
in \(I'\setminus E_p\). In the frozen model these routes avoid the named
paths \(Q_p^c\). In the adaptive model there is one simultaneous linkage of
the fixed entry set \(B_p^c\) together with those ray representatives.
Then, for every \(J\subseteq I'\),

\[
 r_{N_p^c}(A_p^c(J))
 \ge |J\setminus E_p|
 \ge |J|-|E_p|
\]

and more precisely

\[
 |J|-r_{N_p^c}(A_p^c(J))\le |J\cap E_p|.
\tag{5.5}
\]

In adaptive cut form this is exactly

\[
 \gamma_{p,C}^c(B_p^c\cup A_p^c(J))-b_p
 \ge |J|-|E_p|
\tag{5.6}
\]

for every \(J,C\), with the frozen analogue obtained by replacing the left
side by \(\gamma_{p,C}^{c,Q_p}(A_p^c(J))\). Informally, a cut traps a ticket
only when all of its admissible complete-route ports lie behind that cut.

### Corollary 5.2 (two cross-ray matchings plus transported background)

Assume in one common state \(c\):

1. the transported background is an occurrence-labelled linkage omitting
   at most \(\beta=O(1)\) background targets;
2. every abstract edge of each canonical cross-ray matching is expanded to
   all required physical occurrences;
3. outside \(Z(c)\cup E_p\), the resulting routes are pairwise
   vertex-disjoint in system \(p\) and correctly typed at their terminals;
   in the frozen model they avoid the named routes \(Q_p^c\), while in the
   adaptive model they belong to one simultaneous linkage together with
   the fixed background entry set \(B_p^c\);
4. \(E_0,E_1\subseteq I\setminus Z(c)\) and
   \(|Z(c)|,|E_0|,|E_1|=O(1)\); and
5. folding and unfolding preserve ticket, common state, occurrence address,
   terminal type, and every physical capacity;
6. global product closure holds after \(c\), and every shared or
   cross-ticket cross-system coupling has been exhausted as required in
   Section 2.

Then

\[
 \boxed{
 \operatorname{def}_{\rm terminal}
 \le\beta+|Z(c)|+|E_0\cup E_1|=O(1).}
\tag{5.7}
\]

Indeed, first apply Lemma 4.1 and work on
\(I'=I\setminus Z(c)\). Apply (5.5) inside the exact formula (0.1)
restricted to \(I'\). Since \(J_0,J_1\) are disjoint, an exceptional
logical label is charged at most once. Because
\(E_0,E_1\subseteq I'\), the display is equivalently

\[
 \beta+|Z(c)\cup E_0\cup E_1|.
\]

If the background is exact, \(Z(c)=\varnothing\),
\(E_0=E_1=\varnothing\), every logical ticket has a complete
occurrence-labelled route in both systems under the same \(c\), and every
cross-system coupling has been resolved as above, the literal union is a
complete common compiler and the deficiency is zero.

For an asymptotic family, the notation \(O(1)\) in this corollary means that
there is one common cap \(c_n\) for each instance and

\[
 \sup_n\bigl(\beta_n+|Z(c_n)|+|E_{0,n}\cup E_{1,n}|\bigr)<\infty.
\tag{5.8}
\]

Local constant losses cannot be summed over a growing regeneration chain.

## 6. The occurrence-labelled lifting obligation

The canonical corollary requires a lifting theorem with all of the following
properties.

1. Every legal physical full block maps to a folded path.
2. Every folded path unfolds to a legal physical full block.
3. Vertex-disjoint folded paths are equivalent to simultaneous physical
   feasibility, with each shared capacity represented once.
4. Path switching preserves ticket label, common state, phase, occurrence
   row or cell, role, endpoint class, and terminal type; alternatively every
   switch has a legal normalization preserving those data.
5. The lift commutes with protection or contraction of the transported
   background.
6. No selected ticket receives an unactivated provider created only by a
   different candidate.

Every representative selected from \(A_{p,i}^c\) must be a complete
canonical full-block route traversing every physical capacity required by
the system-\(p\) occurrence of \(i\). Listing two required atoms in one
menu would make them alternatives, not a conjunction. An alternative exact
formulation may expand \(I\) to occurrence atoms, but then incomplete
logical tickets must be discarded and the resulting logical deficiency
recomputed.

Ordinary Rado does not optimize arbitrary choices of multi-cell bundles.
Without a fixed canonical full-block lift, the problem is matroid parity or
a more general set-packing problem. The paired relation \(K_i^c\) must also
be rectangular; otherwise two marginal complete-route menus still forget
which phase-0 and phase-1 routes may be paired.

Terminal sinks are interchangeable only within a complete occurrence type
for which every path permutation is physically legal. Otherwise terminal
identity must be encoded in the state or gadget.

## 7. Choosing the cap

The true optimum over complete cap states is

\[
 \max_{c\in{\cal C}}\nu(c)
 =
 \max_{c\in{\cal C}}\min_{U\subseteq I}
 \left(\rho_0^c(U)+\rho_1^c(I\setminus U)\right).
\tag{7.1}
\]

For finite \({\cal C}\), deficiency at most \(K\) is equivalent to

\[
\boxed{
 \exists c\in{\cal C}\ \forall U\subseteq I:
 \quad
 \rho_0^c(U)+\rho_1^c(I\setminus U)\ge |I|-K.}
\tag{7.2}
\]

The quantifiers cannot be exchanged, and the two systems cannot choose
different cap states. A proof must exhibit one cap, prove a uniform bound on
a nonempty cap family, or establish a genuine intersection theorem for the
good-cap sets. The fixed logical ground set from Section 1 is essential to
this optimization.

Common declared states are choices made by \(c\), outside Theorem 2.1. If
one instead expands the ground set to copies \((i,s)\), the copies of one
logical ticket must already be parallel in **both** Rado matroids, for
example through one capacity-one logical-ticket gate. Imposing
at-most-one state afterward is a third partition matroid and invalidates
the two-matroid min-max formula. Further cross-state compatibility likewise
leaves the present reduction.

Phase 1 may be used as transported theorem input. Transport does not
authenticate it as a private or native phase.

## 8. Sharp failure modes

1. **Common-state mismatch.** One ticket has only state \(a\) in system 0
   and only state \(b\ne a\) in system 1. Both marginal ranks are one, but
   true common-state rank is zero.
2. **Shared bottleneck.** \(m\) nonzero tickets have the same sole
   capacity-one occurrence. Deficiency is \(m-1\).
3. **Correlated two-ray choices.** One ticket allows \((a,c)\) or \((b,d)\);
   another allows \((a,d)\) or \((b,c)\). Each ray projection is perfectly
   matchable, but no two full pairs are resource-disjoint.
4. **Dynamic support.** Ticket \(i\) exists only using a host created by
   \(j\), and conversely. The pair can be feasible while neither singleton
   is, violating matroid heredity.
5. **Unlabelled terminal swap.** Aggregate linkage may connect two sources
   to the wrong prescribed sinks. Ordinary Menger cuts permit the
   permutation unless the occurrence type makes it legal.
6. **Accumulating local defect.** A sequence of layers can kill a different
   ticket at every step. Per-layer deficiency one does not imply terminal
   \(O(1)\); one global layered-gammoid cut or one fixed \(O(1)\) exceptional
   set is required.
7. **Frozen route versus contraction.** Let a background start \(b\) have
   routes \(b\to u\to t_1\) and \(b\to v\to t_2\), while a ray start \(x\)
   has only \(x\to u\to t_1\). Freezing the first named background route
   kills \(x\); adaptive contraction reroutes \(b\) through \(v\) and leaves
   \(x\) linkable.
8. **Abstract factor without a router.** An abstract perfect incidence
   factor and an exact background matching may coexist while every physical
   ray suffix crosses one common unit vertex. Every singleton is supported,
   but the full ray rank is one. A factor or parent matching is therefore
   not an all-cut supplier theorem.

## 9. Scope

Theorems 2.1, 3.1, and 5.1 are exact abstract matroid/linkage statements.
Corollary 5.2 is conditional on the occurrence-labelled physical lifting
obligation of Section 6 and one fixed compatible cap state. It does not
prove that a particular folded carrier supplies this lift, nor owner,
residence, chronology, upper-shadow, regeneration, or a final OR word.
In particular, it treats transported phase 1 only as theorem input and
does not authenticate it as a native or private phase.
