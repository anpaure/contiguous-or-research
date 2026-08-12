# Thread K: compiler-ready MMM pairs and the Pascal diamond recursion

Date: 2026-07-29

## 0. Verdict

There is an exact simultaneous Catalan certificate and a finite recursive
invariant.  It is stronger than the existing decorated-carrier signature
because it carries the compiler ports, not merely the middle chronology.

The key structural identity is new and elementary.  In a depth-`d` resident
Johnson chronology, the maximal erosion envelope at a state is determined by
the residence queue: delete the last `d` insertion tokens from the current
owner.  The next erosion envelope deletes the current transition deletion
and reinserts the oldest queued token.  Consequently the one-core equation is
a local transition relation on the **same** residence queue automaton.  At
depth three, its edge union is exactly the lower-`q=2` root.  Residence,
lower `q=2`, the core, and the compiler port column therefore admit one
synchronized state, rather than four independently chosen decorations.

For an equivariant one-core, attach to each quotient position the set of
low-target rotation orbits which can use that port.  The complete weighted
Hall condition is the family

\[
 \sum_{O\in X}|O|\le k R(X)                             \tag{0.1}
\]

over all target-orbit families `X`, where `R(X)` counts quotient position
columns adjacent to `X`.  The vector `R` adds under concatenation, is
unchanged by reversal and coordinate rotation, and has one twisted closing
core equation.  It therefore tensors associatively with the MMM residence
queue, phase voltage, fixed-depth roots, and the exact
total/prefix/suffix/internal-union algebra for arbitrary upper intervals.

A nonexceptional MMM flippable pair is a literal alternating incidence
hexagon.  After contraction it is a three-head transfer: it preserves three
lower colours and replaces exactly three Johnson seams.  The correct
recursive object is the collection of occurrence-labelled retained fragment
signatures together with their six-port pairing.  A switch changes the
pairing and three seam atoms; all retained-fragment signatures transport,
including reversal.  This yields an exact bottom-up root test for a
compiler-ready pair in every fixed compatible MMM gluing library.

The new even-to-odd Pascal lemma fits the same algebra.  Its input is not two
separate rainbows but a **spaced common-colour perfect matching** in the
transition occurrence graph.  The matching indicator must also have long
enough runs to make the `Cat_r` lifted components nonsingleton (or
depth-`d` resident in the new coordinate).  Each selected component is then
evaluated by the same physical queue/shadow/core/compiler signature.  Thus a
joint SCD/Pascal certificate is exact and recursive; separate lower and upper
rainbows do not enter the theorem.

The audited `k=13` optimum shows that this direct lift is only a strict
subclass.  Its `AA` sector is a Catalan family of lower-rainbow paths, but its
adjacent unions cover only `645/792` upper colours.  The `AB/BA` collars
repair all 147 holes, while the `BB` paths complete the no-`z` lower and upper
channels.  The correct broader signature is therefore two labelled sector
path systems plus a capacitated endpoint matching.  Theorems 9.5--9.6 give
its exact degree, shadow, and Hall equations and couple its completed cycles
back to the same queue/compiler root algebra.

Two GMM tight enumerations give the clean all-semilength forest base for
that broader signature.  The lower projection has `Cat_m` components and a
complete lower deck, but bare tightness may create isolated owners; the
independent GMM--dummy construction supplies a nonisolated replacement.  The
upper projection starts with `3m/(m+2) Cat_m` components, and restoring
exactly `2(m-1)/(m+2) Cat_m` direct jumps leaves `Cat_m` components while
preserving every protected upper colour.  This count algebra is not yet a
fusion theorem.  The exact remaining interface is a coloured cut equation,
upper-hole exposure, the capacitated endpoint Hall inequalities (9.49), and
the consecutive protected-window inequalities (9.50).  Explicit `m=2` and
`m=3` tight enumerations show that nonisolation and opposite-colour
injectivity are not automatic.

A single tight enumeration of all four levels would unify these decks only
under an additional rank-localization theorem.  Tightness puts exactly `t`
two-flip steps on the larger parity shore but allows them to be low--low,
low--high, or high--high.  Quarantining all of them high--high is exactly
equivalent to constructing one Hamilton generalized-braid skeleton.  The
published GMM statement does not impose this corner.  Explicit `m=2` tight
listings realize all three step types, and even the quarantined listing
repeats an opposite lower colour and has a depth-two-short `A` path.
Conversely, a Hamilton child carrier with exact lower `q=1` and complete
adjacent-union `q=1` support already has the forced channel counts; selecting
one `BB` representative for each no-`z` upper target leaves exactly `t`
merges and lifts to a quarantined tight enumeration.  Its actual cross seams
discharge the fixed-port quotas, exposure, Hall, and monodromy automatically.
This converse is only about adjacent two-owner unions, not deeper shadows.
In the Mersenne-parity dimensions, complement coherence gives one further
collapse: the Middle Levels half-turn sends every lower-`q=2` label to the
complementary upper-`q=1` label.  At `k=15`, strict binary-trace complement
coherence is exactly the scalar law
`1-c_p=c_(p+3217)c_(p+3218)`; after multiplication of indices by `3218`,
the trace has neither `00` nor `111`.  This identifies two coverage tests
but does not prove either one.

The frozen fixed-path `k=15` system nevertheless has a simultaneous
degree-two solution with both lower decks exact and both upper decks
complete.  Its 1,527 residence defects and deeper holes prove that `q=1`
compatibility is not the remaining finite gate; chronology and protected
compiler windows are.

What is not proved is existence of an accepting root for every semilength.
The natural MMM gluing-tree/parallel-label family is already exactly closed
at `k=11` before compiler ports, and the audited 135-member saved `k=14` path
library has maximum common-colour matching `2739/3003`.  These are rigorous
obstructions to the two stated finite libraries only.  They are not
cardinality heuristics and not impossibility results for unrestricted
alternating circuits, new even
paths, or broader component-and-seam constructions.

No search, SAT solve, or web access was used in this report.

## 1. Odd-composite setup and the object sought

Put

\[
 k=2m+1,\qquad r=m+1,\qquad
 W=\binom{k}{r}=k\operatorname{Cat}_m,\qquad
 N=\operatorname{Cat}_m,                               \tag{1.1}
\]

and let `rho` be cyclic coordinate rotation.  Work in the phase-labelled
middle-levels quotient multigraph; parallel incidence-edge orbits retain
their physical phases.

Rotation is free on both central ranks and on central inclusion edges for
every odd `k`, including composite `k`.  Indeed, a set fixed by a nonidentity
rotation is a union of coordinate cycles of some length `e>1` dividing `k`,
so `e` divides its rank.  But

\[
                 \gcd(k,m)=\gcd(k,m+1)=1.              \tag{1.2}
\]

An inclusion edge fixed by a rotation would have both endpoints fixed.
Off-central target ranks need not be free.

Let

\[
 T=(T_i)_{i\in\mathbb Z_W},\qquad |T_i|=r,             \tag{1.3}
\]

be a strict-spiral lower-rainbow Johnson Hamilton cycle, oriented as

\[
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\},\qquad
 T_{i+N}=\rho^vT_i.                                    \tag{1.4}
\]

Its quotient lift is one physical cycle exactly when

\[
                         \gcd(v,k)=1.                  \tag{1.5}
\]

For an integer `1<=d<r`, call `T` depth-`d` resident when

\[
 \beta_i\ne\alpha_{i+t}qquad(1\le t\le d)             \tag{1.6}
\]

cyclically.  Put `h=r-d` and define the maximal erosion

\[
 P_i=\bigcap_{a=0}^{d}T_{i-a}.                         \tag{1.7}
\]

An equivariant one-core is a cyclic sequence `C` with

\[
 C_i\subseteq P_i,\qquad
 C_i\cup C_{i+1}=P_i\cup P_{i+1},\qquad
 C_{i+N}=\rho^vC_i.                                    \tag{1.8}
\]

Let

\[
 \mathcal S_h=\{S\subseteq\mathbb Z_k:1\le|S|\le h\}. \tag{1.9}
\]

The pair `(T,C)` is **graded compiler-ready** when the occurrence-labelled
graph

\[
 S\sim i\quad\Longleftrightarrow\quad
                  C_i\subseteq S\subseteq P_i          \tag{1.10}
\]

has a matching saturating `S_h`.  A matching produces a cyclic source word
by putting its target at the matched position and `P_i` at every idle
position.  The sandwich `C<=A<=P` gives `DA=DP` and hence fixes every higher
derivative row.

The target of this report is one simultaneous certificate for:

1. exact middle ownership, quotient connectivity and unit voltage;
2. residence;
3. lower `q=2` and every required upper root;
4. an equivariant one-core and the complete physical Hall condition; and
5. when a literal linear word is requested, an upper-safe cut.

The equivariant-core requirement is a sufficient and exactly recognizable
graded subclass.  It is not asserted that every possible compiler has an
equivariant core or satisfies `DA=DP`.

## 2. The residence queue already contains the erosion

At state `T_i`, define the ordered queue of the last `d` insertions

\[
 B_i=(\beta_{i-d},\beta_{i-d+1},\ldots,\beta_{i-1}).   \tag{2.1}
\]

### Theorem 2.1 (queue-to-erosion identity)

If `T` is depth-`d` resident, the entries of `B_i` are distinct, all lie in
`T_i`, and

\[
 \boxed{P_i=T_i\setminus B_i.}                         \tag{2.2}
\]

Moreover `alpha_i` is not in `B_i`, and

\[
 \boxed{
 P_{i+1}=P_i-\{\alpha_i\}+\{\beta_{i-d}\}.}           \tag{2.3}
\]

In particular `P` is itself a rank-`h` Johnson chronology.

#### Proof

An insertion among the last `d` transitions cannot be deleted before state
`T_i`, by (1.6), so every queued coordinate is in `T_i`.  If two queued
insertions were equal, the coordinate would have had to be deleted between
them in order to be inserted twice, creating a positive run of length at
most `d`.  Thus the queue is distinct.

A coordinate of `T_i` absent from one of
`T_(i-d),...,T_i` must have been inserted after that absence.  Its insertion
is one of the last `d` transitions, hence it lies in `B_i`.  Conversely every
queued coordinate was absent immediately before its insertion and therefore
is absent from the intersection (1.7).  This proves (2.2).

Residence also forbids deleting a queued coordinate at transition `i`, so
`alpha_i notin B_i`.  Expanding (2.2) at `i+1` cancels the newly inserted
`beta_i` and the common queue tail, leaving exactly (2.3).  The inserted
oldest token differs from `alpha_i` by (1.6) at delay `d`.  \(\square\)

### Corollary 2.2 (the core is a queue transition)

Augment a residence-queue state by a mask `C_i subseteq P_i`.  A legal
transition to `C_(i+1) subseteq P_(i+1)` is exactly

\[
 C_i\cup C_{i+1}=P_i\cup P_{i+1}.                     \tag{2.4}
\]

Equivalently it forces

\[
 \alpha_i\in C_i,\qquad \beta_{i-d}\in C_{i+1},       \tag{2.5}
\]

and every coordinate of `P_i intersect P_(i+1)` into at least one of the
two core masks.

For `d=3`, the same edge union is the lower-`q=2` root:

\[
 P_i\cup P_{i+1}
   =T_{i-2}\cap T_{i-1}\cap T_i.                      \tag{2.6}
\]

Thus one augmented queue arc simultaneously certifies residence legality,
one-core legality, and its lower-`q=2` label.

#### Proof

Equation (2.4) is the one-core definition.  By (2.3), `alpha_i` occurs only
in `P_i` and `beta_(i-d)` only in `P_(i+1)`, giving (2.5); common coordinates
give the remaining clauses.  Equation (2.6) is the adjacent-intersection
identity, or follows directly by taking the union of the two overlapping
`d+1`-state intersections.  \(\square\)

This is the main coupling theorem.  Choosing a carrier first and attempting
to decorate residence, `q=2`, and the core independently forgets that all
three live on the same queue arc.

## 3. Exact odd-composite Hall at the root

Let \(\mathscr O_h\) be the set of rotation orbits in `S_h`, with actual
weight

\[
                         w(O)=|O|.                     \tag{3.1}
\]

For a quotient position `0<=j<N`, define its port-neighbourhood type

\[
 \Lambda_j(C,P)=
 \left\{
 O\in\mathscr O_h:
 \exists S\in O, C_j\subseteq S\subseteq P_j
 \right\}.                                             \tag{3.2}
\]

For `X\subseteq\mathscr O_h`, put

\[
 R_{C,P}(X)=
 \#\{0\le j<N:\Lambda_j(C,P)\cap X\ne\varnothing\}.   \tag{3.3}
\]

### Theorem 3.1 (compiler-ready weighted root criterion)

Assume (1.5) and the twisted equivariance (1.8).  The physical port graph
(1.10) has a matching saturating every low target if and only if

\[
 \boxed{
  \sum_{O\in X}w(O)\le kR_{C,P}(X)
  \quad\hbox{for every }X\subseteq\mathscr O_h.}       \tag{3.4}
\]

This is exact for odd composite `k`.  No divisibility or equivariant-matching
condition is missing, and the final physical matching may break rotation
symmetry.

#### Proof

Translation by `N` acts freely on physical source positions because a unit
voltage cycles through all `k` sheets.  An invariant target shore
`union X` has as its neighbourhood exactly the `k` physical translates of
each quotient column counted by (3.3), so

\[
 |N(\bigcup X)|=kR_{C,P}(X).                            \tag{3.5}
\]

For an arbitrary physical target shore `A`, its deficiency

\[
                         \delta(A)=|A|-|N(A)|           \tag{3.6}
\]

is supermodular under unions and intersections.  If Hall fails, union all
rotates of a maximum-deficiency shore.  The result is an invariant
maximum-deficiency shore and hence a union of complete target orbits.
Therefore it suffices, and is necessary, to test (3.4).  Short target orbits
enter with their actual weights `w(O)`; freeness is needed only on the right.
Physical Hall then gives an ordinary phase-resolved matching.  \(\square\)

The quotient flow witnessing (3.4) is an existence certificate, not itself
a phased matching.  To emit a word one recovers an ordinary matching in the
physical occurrence graph.

### Corollary 3.2 (core thinning)

If `C'` and `C` are one-cores of the same `P` and `C'_i subseteq C_i` at
every position, then every port edge available for `C` is available for
`C'`.  Thus Hall readiness is preserved by thinning.  Every Hall-ready
equivariant core has an inclusion-minimal Hall-ready equivariant descendant.

#### Proof

The lower containment in (1.10) becomes weaker when the core shrinks.  The
second assertion follows by descending in the finite poset of equivariant
one-cores.  \(\square\)

This does not make a sparse core automatic: thinning is allowed only while
all one-core equations remain true.

## 4. The exact compiler transfer algebra

Let `B=(P_0,...,P_(ell-1))` be an ordered quotient envelope block.  Its
compiler transfer set `K(B)` consists of every triple

\[
                         (c_-,c_+,\mathbf R)            \tag{4.1}
\]

realized by masks `C_0,...,C_(ell-1)` satisfying all internal one-core
equations, where

\[
 c_-=C_0,\qquad c_+=C_{\ell-1},                       \tag{4.2}
\]

and, for every `X\subseteq\mathscr O_h`,

\[
 \mathbf R(X)=
 \#\{i:\Lambda_i(C,P)\cap X\ne\varnothing\}.          \tag{4.3}
\]

### Theorem 4.1 (endpoint-typed port algebra)

For compatible ordered blocks `B,B'`,

\[
\begin{split}
 \mathcal K(BB')=\{(c_-,c'_+,\mathbf R+\mathbf R'):\;&
 (c_-,c_+,\mathbf R)\in\mathcal K(B),\\
 & (c'_-,c'_+,\mathbf R')\in\mathcal K(B'),\\
 &c_+\cup c'_-=P_{\rm last}\cup P'_{\rm first}\}.
                                                               \tag{4.4}
\end{split}
\]

Reversal and rotation act by

\[
 \mathcal K(B^{\rm rev})=
 \{(c_+,c_-,\mathbf R):(c_-,c_+,\mathbf R)\in\mathcal K(B)\}, \tag{4.5}
\]

\[
 \mathcal K(\rho^aB)=
 \{(\rho^ac_-,\rho^ac_+,\mathbf R):
       (c_-,c_+,\mathbf R)\in\mathcal K(B)\}.          \tag{4.6}
\]

At a quotient root of voltage `v`, an equivariant compiler-ready core exists
exactly when one transfer satisfies the twisted closure

\[
 c_+\cup\rho^vc_-=P_{\rm last}\cup\rho^vP_{\rm first} \tag{4.7}
\]

and the root inequalities

\[
 k\mathbf R(X)\ge\sum_{O\in X}w(O)
 \quad(X\subseteq\mathscr O_h).                        \tag{4.8}
\]

#### Proof

The only new core equation in a concatenation is the displayed seam
equation; all position columns are disjoint, so their neighbourhood-count
vectors add.  Reversal swaps the endpoint masks and permutes the same port
columns.  Rotation preserves target rotation orbits and rotates only the
endpoint masks.  Equation (4.7) is precisely the missing quotient seam in
(1.8), and (4.8) is Theorem 3.1.  \(\square\)

The algebra is finite for fixed `k`, though exponentially large.  It is a
recursive invariant, not an efficiency claim.  An equivalent stronger
physical version stores, for each pair of endpoint core masks, the family of
low-target subsets matchable injectively inside the block.  Concatenation
takes disjoint unions of matchable target sets subject to the seam equation.
At cyclic closure the full target family must occur.  This version does not
require an equivariant core and is the correct fallback for a nonstrict or
multicomponent construction.

## 5. MMM flippable pairs are three-head transfers

Let `H` be a rank-`r-2` set and choose distinct coordinates `a,b,c` outside
it.  Put

\[
 L_a=H\cup\{a\},\quad L_b=H\cup\{b\},\quad
 L_c=H\cup\{c\},                                      \tag{5.1}
\]

\[
 Q_{ab}=H\cup\{a,b\},\quad Q_{bc}=H\cup\{b,c\},\quad
 Q_{ca}=H\cup\{c,a\}.                                 \tag{5.2}
\]

The six containments form a Boolean incidence hexagon.  Its alternating
matchings are

\[
 M_0=\{L_aQ_{ab},L_bQ_{bc},L_cQ_{ca}\},               \tag{5.3}
\]

\[
 M_1=\{L_aQ_{ca},L_bQ_{ab},L_cQ_{bc}\}.               \tag{5.4}
\]

### Theorem 5.1 (literal three-head transfer)

Suppose an exact middle-levels factor `F` is alternating on the hexagon,
namely

\[
                       F\cap E(C_6)=M_0               \tag{5.4a}
\]

and let `E_a,E_b,E_c` be the other upper neighbours of
`L_a,L_b,L_c`.  Toggling the hexagon preserves degree two on both central
shores.  After contracting the lower shore it changes exactly

\[
 E_aQ_{ab},\ E_bQ_{bc},\ E_cQ_{ca}                    \tag{5.5}
\]

to

\[
 E_aQ_{ca},\ E_bQ_{ab},\ E_cQ_{bc}.                   \tag{5.6}
\]

Thus the three lower colours are fixed and the three internal heads are
cyclically transferred among fixed external tails.

Every nonexceptional MMM gluing pair

\[
                     110u0v\longleftrightarrow101u0v \tag{5.7}
\]

is such a hexagon, equivariantly over its rotation orbit.

#### Proof

Each vertex of the hexagon loses and gains one selected incidence.  At lower
vertex `L_t`, contraction joins its unchanged external neighbour to its old
or new internal head, giving (5.5)--(5.6).  The MMM word pair is precisely
the paper's Boolean gluing hexagon; the exceptional star case is excluded by
its hypotheses.  \(\square\)

Deleting the three old contracted seams leaves the actual retained path
fragments and six occurrence-labelled ports.  The new seams re-pair those
ports.  One must retain the actual old endpoint pairing: a bare statement
that the old seams have a `2+1` distribution over two components does not
determine which fragment endpoints pair.  MMM compatibility guarantees the
prescribed new pairing merges the intended plane-tree components.  It does
not imply that an arbitrary order of simultaneous hexagon toggles remains
dynamically flippable.

## 6. What one hexagon changes

Consider any rethreading which deletes `s` old Johnson seams, retains the
resulting path fragments up to reversal and uniform rotation, and inserts
`s` new seams.

### Theorem 6.1 (fixed-depth occurrence identity)

For every fixed `1<=q<N`, every old `q`-edge intersection or union window wholly
inside a retained fragment has a unique new copy with the same target orbit,
and conversely.  Hence, target by target,

\[
 \lambda'_q(R)=\lambda_q(R)-B_q^-(R)+B_q^+(R),         \tag{6.1}
\]

where `B_q^-` and `B_q^+` count old and new based windows meeting a deleted
or inserted seam.  On one quotient cycle,

\[
 \sum_RB_q^-(R)\le sq,\qquad
 \sum_RB_q^+(R)\le sq.                                 \tag{6.2}
\]

For one MMM hexagon `s=3`: lower `q=2` changes at most six old and six new
quotient starts, and fixed upper depth `q` changes at most `3q` quotient
starts on each side.  The physical orbit lift multiplies these occurrence
counts by `k`.  These are occurrence bounds, not hole bounds.

#### Proof

A `q`-edge cyclic window changes if and only if it contains a changed seam.
Each seam lies in at most `q` admissible nonrepeating based starts, with
equality when its cycle is longer than `q`; overlaps only reduce the union.
Intersection and union are invariant under reversal, and rotation preserves
the target orbit.  \(\square\)

For a sequence of switches, retain every based occurrence together with its
fragment location and edge span.  If `tau_t` transports the retained
fragments at switch `t`, `K_t^-` is the span-hit old occurrence family, and
`B_t^+` is the new collar family, then exactly

\[
 \Omega_q(F_t)=
 \tau_t\bigl(\Omega_q(F_{t-1})\setminus K_t^-\bigr)
 \mathbin{\dot\cup}B_t^+.                              \tag{6.3}
\]

Thus every final witness has a unique last birth: it is a base witness or a
collar-born witness which survives every later deleted seam.  A root-load
histogram without span provenance is not a recursive state.

### Theorem 6.2 (residence update)

Every old short positive run whose closed span avoids all deleted seams
survives, possibly reversed and rotated.  After all old short spans are hit,
every new short run meets an inserted seam.  Therefore the new chronology is
depth-`d` resident if and only if

1. every old run of length at most `d` has a deleted seam in its closed
   span; and
2. the complete new multi-seam collar passes the `d`-queue test.

Independent one-seam safety is insufficient when short retained fragments
allow one queue comparison to cross two seams.

#### Proof

The trace `0 1^ell 0` is invariant under reversal.  A closed span retained
inside one fragment therefore survives.  Conversely a new short run wholly
inside a retained fragment would be an old short run with unhit span, so
every remaining candidate crosses a new seam and is read by the new collar
queue.  \(\square\)

### Theorem 6.3 (erosion/core/Hall collar identity)

One changed seam belongs to at most the `d` backward erosion windows ending
immediately after it (exactly `d` on a cycle longer than `d`).  Thus the
old and new seam sets each meet at most `sd`
erosion columns and at most `s(d+1)` adjacent core equations.  Every other
envelope column transports along a retained fragment; on a reversed fragment
it is the correspondingly shifted reversed intersection.

Suppose a chosen old core is transported on all stable columns and legally
completed on the new collar.  Let `K^-` and `K^+` be the distinct old and new
quotient port columns in those collars.  Then for every target-orbit family
`X`,

\[
\begin{split}
 R'(X)-R(X)
   ={}&\sum_{j\in K^+}
       \mathbf1_{\Lambda'_j\cap X\ne\varnothing}\\
     &-\sum_{j\in K^-}
       \mathbf1_{\Lambda_j\cap X\ne\varnothing},       \tag{6.4}
\end{split}
\]

and hence

\[
                         |R'(X)-R(X)|\le sd.            \tag{6.5}
\]

Every fixed-core weighted Hall slack changes by at most `ksd`.  In
particular, Hall is preserved if every old shore has reserve at least
`ksd` and the new core collar exists.

#### Proof

An erosion column is a `(d+1)`-state intersection, so Theorem 6.1 with
`q=d` gives the stable-column bijection and the collar count.  A core equation
touches one more boundary adjacency.  Stable port columns have identical
containment neighbourhoods after reversal/rotation, leaving exactly the two
collar sums in (6.4).  \(\square\)

The fixed-core qualification is essential.  Reselecting an optimal core can
propagate along a long coordinate-support run, so there is no unconditional
`O(sd)` Lipschitz theorem for the optimum over all cores.  The set-valued
transfer algebra (4.4), not a scalar minimum-deficiency score, retains that
propagation.

## 7. The simultaneous MMM Catalan certificate

Fix maximum fixed upper depth `H`.  A half-open, phase-labelled retained
fragment carries the direct product of the following exact records:

1. its entrance/exit owner and physical phase;
2. the partial transduction which, for every admissible incoming `d`-token
   queue, either rejects a residence violation or returns the outgoing queue
   together with every newly matured erosion column;
3. the first and last `min(H,ell)` owner masks, and all emitted internal
   lower-`q=2` and fixed upper root occurrences with span provenance
   (equivalently, the full partial root transduction on every admissible
   incoming `H`-owner history);
4. its compiler transfer set `K` from Section 4, indexed jointly by the
   entrance and exit residence/erosion boundary states; and
5. its voltage.

At concatenation, the owner queue first recomputes every erosion column that
matures in the new `d`-collar.  Those columns and their core choices are
then fed into the compiler transfer relation.  One must not concatenate stale
pre-switch envelope blocks independently of the queue.

If literal arbitrary-length upper intervals are required, add its total
union, every based prefix/suffix union with length, and every internal
interval union.  Concatenation uses

\[
 \operatorname{Tot}(AB)=\operatorname{Tot}(A)\cup
                         \operatorname{Tot}(B),         \tag{7.1}
\]

\[
 \operatorname{Pref}(AB)=\operatorname{Pref}(A)\cup
 \{\operatorname{Tot}(A)\cup p:p\in\operatorname{Pref}(B)\}, \tag{7.2}
\]

\[
 \operatorname{Suff}(AB)=\operatorname{Suff}(B)\cup
 \{s\cup\operatorname{Tot}(B):s\in\operatorname{Suff}(A)\}, \tag{7.3}
\]

\[
\begin{split}
 \operatorname{Int}(AB)={}&\operatorname{Int}(A)\cup
 \operatorname{Int}(B)\\
 &\cup\{s\cup p:s\in\operatorname{Suff}(A),
                  p\in\operatorname{Pref}(B)\}.        \tag{7.4}
\end{split}
\]

Lengths forbid reusing a cyclic position.  Unlike fixed-depth windows,
arbitrary upper intervals have no bounded seam-collar theorem.

For normalized quotient blocks, the product is the semidirect product

\[
 (A,g)\star(B,h)=\bigl(A\cdot\rho^gB,g+h\bigr),        \tag{7.5}
\]

so the closing prefix and core masks are rotated by accumulated voltage.
If `(A,v)` is the completed one-lap quotient signature, its literal physical
signature is the `k`-fold twisted power

\[
 (A,v)^{\star k}=
 \bigl(A\cdot\rho^vA\cdot\rho^{2v}A\cdots
       \rho^{(k-1)v}A,kv\bigr).                       \tag{7.6}
\]

The one-lap relation suffices for the equivariant core equations and the
weighted Hall test.  Cyclic residence and fixed-depth orbit support may also
be checked on one lap with its twisted boundary.  Arbitrary upper intervals,
however, must be evaluated on (7.6), because a witness may cross several
quotient laps.

### Theorem 7.1 (compiler-ready MMM root theorem)

Fix a compatible labelled MMM gluing library and either

* an admissible sequential order in which every selected hexagon is
  dynamically flippable; or
* the equivalent simultaneous occurrence-labelled final port pairing.

Mark every port needed by a future gluing edge.  Store both orientations of
every retained fragment signature.  At a gluing edge, retain the actual
fragment records, replace the old six-port pairing by the new pairing of
Theorem 5.1, insert the three literal seam records, and multiply.

Then a graded compiler-ready decorated pair exists in this library if and
only if some root record has all of the following properties:

1. one connected quotient factor and `gcd(v,k)=1`;
2. cyclic acceptance of the depth-`d` residence queue, equivalently on the
   `k`-fold physical signature (7.6);
3. positive support for every required lower-`q=2` and fixed-depth upper
   target orbit, or every required upper target on the full `k`-lap interval
   algebra (7.1)--(7.6);
4. a compiler transfer satisfying the twisted core closure (4.7); and
5. every weighted Hall inequality (4.8).

At `d=3`, saturation of all rank-`h` target ports automatically supplies
lower `q=3`, while lower `q=2` remains the separate queue-arc root in (2.6).

#### Proof

Theorem 5.1 gives the exact factor update and preserves every central owner
and lower-`q=1` colour.  The queue, root, upper-interval and core-transfer
records are semantic images of literal path concatenation, so their direct
product is associative; reversal and rotation are already included in the
record.  Induction through the marked gluing expression therefore computes
the exact terminal chronology and port graph.  Conditions 1--3 are exactly
the strict-lift and carrier gates.  Conditions 4--5 and Theorem 3.1 give an
equivariant one-core and a physical saturating port matching.  Conversely,
extract every marked fragment record, core, and root witness from a terminal
pair in the fixed library and reverse the induction.  \(\square\)

Equality of two endpoint-typed fragment records is a congruence: the two
fragments are interchangeable in every larger compatible MMM context.  This
marked-fragment record, not a marginal whole-cycle coverage count, is the
recursive invariant preserved by flippable-pair switches.

The theorem is an exact finite constructor/recognizer.  It does not assert
that an accepting root exists for every `m`.

## 8. Minimal port obstructions carried by the recursion

For a fixed core, the first possible positive-degree weighted Hall circuit
has two target orbits and one right orbit:

\[
 N(O_1)=N(O_2)=\{J\},\qquad w(O_1)+w(O_2)>k.           \tag{8.1}
\]

Each target orbit alone passes because `w(O)<=k`, while their pair fails.
This is an abstract root obstruction; no embedding in the MMM Catalan atlas
is asserted.

The first variable-core chronology obstruction uses one envelope coordinate
with guarded trace

\[
                         0\,1111\,0.                  \tag{8.2}
\]

The outer zeros force the first and fourth core bits to one, and the middle
core edge forces at least one of the two interior bits to one.  If two
targets have unique admissible interior columns and both omit the coordinate,
the static target-position graph matches them but no common core exists.
This obstruction is hereditary through a switch which retains the guarded
four-column block, creates no new port for either target, and avoids its core
collar.

Neither obstruction is a cardinality argument.  Positive target degree and
separate marginal Hall are simply weaker than the root relation (4.4).

## 9. The even-to-odd Pascal branch: a spaced diamond matching

Now let the even ground set have size `2r` and let

\[
 T_0,T_1,\ldots,T_{W-1},\qquad W=\binom{2r}{r},       \tag{9.1}
\]

be a rank-`r` Johnson Hamilton path.  For transition `0<=i<W-1`, put

\[
 X_i=T_i\cap T_{i+1},\qquad U_i=T_i\cup T_{i+1}.       \tag{9.2}
\]

Both colour layers have size

\[
 N=\binom{2r}{r-1}=\binom{2r}{r+1}.                   \tag{9.3}
\]

Let `H_T` be the occurrence multigraph with edge `X_i U_i` labelled by
transition `i`.

### Theorem 9.1 (spaced common-colour matching)

Fix an integer `d>=1`.  A selection `K subseteq {0,...,W-2}` is a common
perfect matching whose components after deleting transitions outside `K`
all have at least `d+1` vertices if and only if its indicator
`epsilon_i=1_(i in K)` satisfies

\[
 \sum_{i:X_i=X}\epsilon_i=1\quad\hbox{for every lower colour }X,  \tag{9.4}
\]

\[
 \sum_{i:U_i=U}\epsilon_i=1\quad\hbox{for every upper colour }U,  \tag{9.5}
\]

the first and last `d` transitions are selected, and between any two deleted
transitions there are at least `d` selected transitions.  Equivalently, if

\[
 D=\{0,\ldots,W-2\}\setminus K
   =\{\delta_1<\cdots<\delta_s\},                      \tag{9.6}
\]

then

\[
 \delta_1\ge d,\qquad
 \delta_{j+1}-\delta_j\ge d+1,\qquad
 \delta_s\le W-d-2.                                   \tag{9.7}
\]

If `D` is empty, (9.7) is replaced by the single condition `W>=d+1`.

For `d=1`, this says that both endpoint transitions are selected and no two
deleted transitions are consecutive; it is exactly the nonsingleton
hypothesis of the Pascal lift.

#### Proof

Equations (9.4)--(9.5) say precisely that the occurrence edges selected by
`K` form a perfect matching between the two colour layers.  Deleting a
transition at `delta_j` ends one vertex component and starts the next.
The first component has `delta_1+1` vertices, an internal component has
`delta_(j+1)-delta_j` vertices, and the last has
`W-1-delta_s` vertices.  Requiring each number to be at least `d+1` is
exactly (9.7), equivalently the selected-transition condition just stated.
\(\square\)

Without the spacing condition, (9.4)--(9.5) is one ordinary bipartite perfect
matching.  With it, occurrence choice and segmentation are coupled; separate
lower and upper rainbows, or even an arbitrary perfect matching with the
wrong order pattern, are insufficient.

For every component `T_a,...,T_b`, introduce a new coordinate `z` and form

\[
 zT_a,zT_{a+1},\ldots,zT_b,
 U_{b-1},U_{b-2},\ldots,U_a.                           \tag{9.8}
\]

The common-colour Pascal theorem proves that, for `d>=1`, these are exact
odd middle/lower-`q=1` cycles; together they enumerate every new middle owner
and every immediate lower colour once.  Their number is

\[
 W-N=\frac1{r+1}\binom{2r}{r}=\operatorname{Cat}_r.    \tag{9.9}
\]

Writing `C=Cat_r` and the component lengths as `ell_1,...,ell_C`, the exact
spacing ledger is

\[
 W=(r+1)C,\qquad N=rC,\qquad
 \sum_{j=1}^{C}\ell_j=(r+1)C,                          \tag{9.10}
\]

\[
 \sum_{j=1}^{C}(\ell_j-d-1)=(r-d)C.                   \tag{9.11}
\]

Hence `d<=r` is necessary, and at `d=r` every component has length exactly
`r+1`.  These are exact identities, not a sufficiency claim.

The new coordinate has run length `b-a+1`, so (9.7) supplies its depth-`d`
residence.  Old-coordinate residence, deeper roots, and compiler ports are
not consequences of the matching.

In this Pascal section the child upper-owner rank is `r+1`.  Its erosion
rank is therefore

\[
                         h_{\rm child}=r+1-d,          \tag{9.12}
\]

not `r-d`; all uses of the odd queue/core signature below make this
substitution.

### Theorem 9.2 (compiler-ready Pascal factor certificate)

Fix an even-path construction library, such as a specified SCD/Catalan
concatenation grammar.  Augment every half-open path block by the finite
relation which records

1. its used lower-colour and upper-colour sets;
2. its initial/terminal selected-run state for (9.7);
3. the still-open component word needed to form (9.8);
4. for each completed odd component, the physical residence/root/upper-
   interval signature of Sections 2, 6 and 7; and
5. the boundary-indexed family of low-target subsets matchable to its odd
   erosion/core ports.

Concatenation unions the two used-colour sets only when both unions are
disjoint, composes the run automaton, completes (9.8) whenever a deleted
transition closes a component, and composes the odd compiler relation by
disjoint union of assigned targets and the cyclic core equations.

Then an exact odd middle/`q=1` factor together with a depth-`d` resident,
root-complete, graded compiler exists in this Pascal library if and only if
some root record

* uses every lower and every upper colour exactly once;
* accepts the spacing language (9.7);
* accepts every lifted component's cyclic residence and required shadow
  signature; and
* contains the full low-target family in its global matchable-port relation.

#### Proof

Every item in the block relation is literal finite path data.  Equations
(9.4)--(9.7) prove that root acceptance is exactly a spaced common matching.
The common-colour Pascal theorem then identifies the odd factor (9.8)
exactly.  The queue/root and compiler relations are semantic images of those
literal odd component words and compose associatively.  Hence an accepting
root reconstructs every required object.  Conversely any object in the
fixed library supplies its selected occurrence set, component boundaries,
component signatures, cores and matchings, which recover an accepting root.
\(\square\)

Here “factor” is essential: the result gives `Cat_r` disjoint odd cycles,
componentwise cyclic cores, and one global physical target-to-port matching.
It does not by itself give one literal compiler word.  Any cuts and joins
must be declared and the resulting residence, shadows, erosion, cores and
ports recomputed, as in Section 11.

An explicit version is the following acyclic Catalan block graph.  Its
vertices are `0,...,W`.  For every interval `I=[a,b]` of length at least
`d+1`, insert an arc `a -> b+1`, labelled by

\[
 \mathcal X(I)=\{X_i:a\le i<b\},\qquad
 \mathcal U(I)=\{U_i:a\le i<b\},                       \tag{9.13}
\]

and by the exact odd profile `Xi(I)` of the cycle (9.8).  Reject an arc if
either colour set repeats internally.  A prefix state

\[
                       (a,A_X,A_U,\Psi)                 \tag{9.14}
\]

extends along `a -> b+1` only when both label sets are disjoint from the
used sets; it replaces them by their unions and replaces `Psi` by its
componentwise profile product with `Xi(I)`.  Accept at `W` exactly when both
colour sets are complete and the profile passes all residence, root and
compiler tests.  Induction on the prefix endpoint is a bijection between
these paths and the interval partitions in Theorem 9.1.  This is an explicit
finite recursion, not merely a restatement by existential block data.

This is the requested SCD/Pascal diamond-path-forest recursion.  Because the
lift need not be a strict rotational spiral, the physical matchable-subset
relation is the safe general compiler state.  Weighted quotient Hall may be
substituted only when an actual free right action and a twisted equivariant
core have separately been proved.

### Theorem 9.3 (protected parent witnesses forced by child ports)

Let `K` be a spaced common matching, and let `F_K` be its raw Pascal child
factor.  Assume that `F_K` is fully depth-`d` resident.  For every `q>=1`,
the `z`-containing intersections of `q+1`
consecutive child owners are exactly

\[
 \left\{
 \{z\}\cup\bigcap_{s=0}^{q}T_{i+s}:
 i,i+1,\ldots,i+q-1\in K
 \right\}.                                             \tag{9.15}
\]

For a kept component of length `L`, the child `z`-trace is

\[
                         1^L0^{L-1},                   \tag{9.16}
\]

and the depth-`d` erosion has a `z`-support run of length `L-d`.  Globally,
exactly

\[
 \sum_j(L_j-d)=W-d\operatorname{Cat}_r
  =(r+1-d)\operatorname{Cat}_r
  =h_{\rm child}\operatorname{Cat}_r                  \tag{9.17}
\]

erosion columns contain `z`.

In particular, a rank-`h_child` target

\[
                         \{z\}\cup A,\qquad |A|=r-d,  \tag{9.18}
\]

has positive compiler-port degree if and only if `A` has a parent
depth-`d` intersection witness whose `d` transitions all lie in `K`.
Therefore compiler readiness forces a `K`-protected witness for **every**
parent rank-`r-d` target.  No one-core choice can repair a missing witness.

Equivalently, in the matching indicators of Theorem 9.1, the exact positive-
degree rows are

\[
 \sum_{\substack{0\le i\le W-d-1:\\
       \bigcap_{s=0}^{d}T_{i+s}=A}}
       \prod_{s=0}^{d-1}\epsilon_{i+s}\ge1
 \quad\left(A\in\binom{[2r]}{r-d}\right).             \tag{9.18d}
\]

They are consecutive-run hyperedge constraints on the **same** common
matching, not a marginal parent coverage condition.

#### Proof

Every child owner outside the forward `zT` arm omits `z`.  Hence an
intersection containing `z` lies wholly in one forward arm, and its parent
transitions are precisely kept transitions of `K`, proving (9.15).  A
backward `(d+1)`-owner intersection contains `z` at exactly the `L-d`
starts wholly within that arm, giving (9.17).  Every erosion column has rank
`h_child` under full residence.  Thus containment of the equal-rank target
(9.18) in an envelope forces equality with that envelope, proving the final
claim.  \(\square\)

This is a genuine matching/chronology/compiler coupling.  A common perfect
matching and separate parent shadow coverage do not imply that the same
matching protects one witness of every required target.

The remaining internal Pascal root ledger is also exact.  Write the parent
transition as

\[
 T_{i+1}=T_i-\{d_i\}+\{c_i\}.                          \tag{9.18a}
\]

On the forward arm, child intersections and unions are `z` plus the
corresponding parent intersections and unions.  On the reversed `U` arm,

\[
 \bigcup_{s=0}^{q}U_{i-s}
       =\bigcup_{j=i-q}^{i+1}T_j,                      \tag{9.18b}
\]

so a no-`z` child upper depth-`q` internal root is a parent upper
depth-`q+1` root.  For lower `q=2`,

\[
 U_i\cap U_{i-1}\cap U_{i-2}
 =X_{i-1}
 \cup\bigl(\{d_{i-1}\}\ \hbox{if }c_i=d_{i-1}\bigr)
 \cup\bigl(\{c_{i-1}\}\ \hbox{if }c_{i-1}=d_{i-2}\bigr).
                                                            \tag{9.18c}
\]

If this triple is internal to a selected reverse arm, then the three
transitions `i-2,i-1,i` lie in `K`.  The equality `c_i=d_(i-1)` would give
`U_i=U_(i-1)`, and `c_(i-1)=d_(i-2)` would give
`U_(i-1)=U_(i-2)`; either contradicts the upper-colour matching equation
(9.5).  Hence every internal reverse-arm lower-`q=2` root is **exactly**
`X_(i-1)`.  The two arm-seam collars may supply additional roots.  Parent
rankwise completeness alone is still insufficient: which `X` roots occur
internally is determined by the selected component chronology and its seam
collars.

There are two further exact Hall shores.  All low targets containing `z`
can use only the columns counted by (9.17), so necessarily

\[
 \sum_{t=0}^{h_{\rm child}-1}\binom{2r}{t}
 \le h_{\rm child}\operatorname{Cat}_r.               \tag{9.19}
\]

On a `z`-support run of length `s=L-d`, every one-core has its two support
endpoints equal to one and has no adjacent zeroes.  It therefore contains
`z` in at least

\[
                         \left\lceil\frac{s+1}{2}\right\rceil \tag{9.20}
\]

columns.  No target omitting `z` can use such a port, so another necessary
Hall inequality is

\[
 \sum_{t=1}^{h_{\rm child}}\binom{2r}{t}
 \le
 \binom{2r+1}{r+1}
 -\sum_{j=1}^{\operatorname{Cat}_r}
   \left\lceil\frac{L_j-d+1}{2}\right\rceil.          \tag{9.21}
\]

These are exact architecture-specific Hall cuts, not sufficiency claims.
They are stronger than a comparison of total Catalan mass because they are
literal target shores in the port graph.

### Theorem 9.4 (the Pascal factor is radius one in the matching indicator)

Put `y_i=1_(i in K)` and add sentinels `y_(-1)=y_(W-1)=0`.  The complete
child edge set is given by the following cellular rules:

\[
 zT_i\ --\ zT_{i+1}\qquad\Longleftrightarrow\qquad y_i=1, \tag{9.22}
\]

and, for every vertex index `i`, exactly one of

\[
\begin{array}{c|c}
(y_{i-1},y_i)&\text{child edge}\\ \hline
(1,1)&U_{i-1}\ --\ U_i\\
(0,1)&zT_i\ --\ U_i\\
(1,0)&U_{i-1}\ --\ zT_i.
\end{array}                                             \tag{9.23}
\]

The pattern `(0,0)` is excluded by the spacing condition, including at the
sentinels.

Consequently, if two valid spaced matchings have symmetric-difference
support `S`, their Pascal factors differ in at most `3|S|` old and `3|S|`
new Johnson edges.  After discarding unchanged common cycle components, the
affected common graph has a retained-path decomposition (zero-edge paths
allowed).  Hence at fixed depth `q` at most `3q|S|` old and new based
windows change, and at most `3d|S|` erosion columns and `3(d+1)|S|` core
equations lie in each old/new collar.

#### Proof

Inside a kept run, (9.22) gives the forward `zT` arm and the `(1,1)` row of
(9.23) gives the reversed `U` arm.  The patterns `(0,1)` and `(1,0)` are its
two cross edges.  Thus the formulas reproduce (9.8) component by component.
Changing `y` on `S` changes at most `|S|` forward slots and only the
nonforward slots indexed by `S union (S+1)`, at most `2|S|`.  The remaining
claims follow from Theorems 6.1 and 6.3 with at most `3|S|` changed seams.
\(\square\)

This gives a bounded compound child switch for an alternating matching trade,
but not automatically an MMM hexagon decomposition.  The child symmetric
difference decomposes into incidence alternating circuits; dynamic
decomposition into compatible MMM `C6` moves is a separate open gate.

Repair of the common matching itself also has two distinct exact meanings.
With the exterior matching frozen, delete its saturated endpoints and apply
Hall to the exposed residual graph.  With the exterior reroutable, apply
Hall to the full allowed occurrence graph with forbidden/prescribed edges;
the new matching may drop old exterior edges, and its symmetric difference
uses alternating paths and cycles.  A scalar count of changed occurrences
is not a complete matching state.

The MMM hexagon theorem and the Pascal diamond theorem therefore share an
occurrence-labelled port algebra, but they are not the same operation: an
odd MMM owner-preserving switch must not be silently treated as a valid
even-path common-matching augmentation.

## 9A. The generalized Pascal braid and its endpoint theorem

The strict forward/reverse lift is not the correct universal recursive
normal form.  Let the old ground set be `V`, `|V|=2r`, distinguish `z`, and
split the child middle owners into

\[
 \mathcal A=\left\{\{z\}\cup T:T\in\binom{V}{r}\right\},\qquad
 \mathcal B=\binom{V}{r+1}.                           \tag{9.24}
\]

Write

\[
 W=|\mathcal A|=\binom{2r}{r},\quad
 N=|\mathcal B|=\binom{2r}{r+1},\quad
 C=W-N=\operatorname{Cat}_r.                          \tag{9.25}
\]

### Theorem 9.5 (two-sector path-braid normal form)

Let `F` be a degree-two factor on `A union B` which owns every middle state
once and every lower-`q=1` colour once.  Assume that every factor cycle meets
both sectors.  Then the subgraphs induced by `A` and by `B` are spanning
linear forests, and:

1. its `AA` edges are exactly `N` in number, and after deleting `z` their
   intersections are every member of `binom(V,r-1)` exactly once;
2. the `AA` forest has exactly `C` path components and no isolated vertex;
3. there are exactly `2C` cross edges and `N-C` `BB` edges; and
4. the cross-edge intersections are the `2C` distinct endpoint labels of
   the `AA` paths, while the `BB` intersections are every remaining member
   of `binom(V,r)` exactly once.

The `B` forest also has exactly `C` path components.  The full factor is
obtained by pairing the `2C` endpoint slots of the two path systems with the
cross edges; a singleton `B` path contributes two coincident endpoint slots.
This is the generalized Pascal braid.

For `U in B`, let

\[
 \lambda_U=\#\{TT'\in E(F[\mathcal A]):T\cup T'=U\},
 \qquad
 \kappa_U=\deg_{F[\mathcal A,\mathcal B]}(U).          \tag{9.26}
\]

Then the upper colours containing `z` are complete if and only if

\[
                         \lambda_U+\kappa_U\ge1
                         \qquad(U\in\mathcal B).       \tag{9.27}
\]

The upper colours omitting `z` are complete if and only if the unions of the
`BB` edges cover `binom(V,r+2)`.  Thus strict common-colour Pascal is only the
special case `lambda_U=1` for every `U`, together with the canonical reversed
`B` path for each `A` path.  In a general braid, cross collars may repair a
large `AA` upper-colour deficit.

In particular, if \(\mathcal H=\{U:\lambda_U=0\}\), then

\[
                         |\mathcal H|\le 2C.           \tag{9.27a}
\]

This is necessary because every hole needs a positive cross degree and the
sum of all cross degrees is `2C`.  When (9.27) holds, the total upper-`z`
excess, counted with multiplicity, is exactly `2C`.  Neither scalar identity
implies the endpoint Hall inequalities below.

#### Proof

A sector-induced cycle would already be a sector-pure component of the
degree-two factor, so the sector-mixed hypothesis makes both induced graphs
linear forests.  A lower colour contains `z` exactly on an `AA` edge.  There are
`binom(2r,r-1)=N` such colours, so lower exactness gives the first assertion
and `|E(F[A])|=N`.  A linear forest on `W` vertices with `N` edges has
`W-N=C` components.  An isolated `A_T` would have two cross edges, both with
lower colour `T`, contradicting lower exactness; hence every component is a
nontrivial path.  Its two endpoints each require one cross edge, proving the
cross count.  The degree sum on `B` gives

\[
                  |E_{BB}|=N-C.                       \tag{9.28}
\]

The cross edge from `A_T` to `B_U` exists exactly when `T subset U` and has
lower colour `T`.  Lower exactness therefore assigns the endpoint labels to
the cross edges and all other rank-`r` labels to the `BB` edges.  Equation
(9.28) gives `C` components in the `B` forest.  Finally an `AA` edge of old
union `U`, and a cross edge incident with `B_U`, both have upper colour
`{z} union U`; no `BB` edge contains `z`.  This proves (9.27), and the
no-`z` assertion is immediate.  \(\square\)

The exact completion relation can be stated without guessing the `B` paths.
Fix a spanning `AA` linear forest `P` with exactly `C` nontrivial paths and
`N` edges whose intersections biject `binom(V,r-1)`.  Let `E` be its set of
`2C` distinct endpoint labels, and let `I=binom(V,r) minus E`.  For `T in E`
and `U in B` with `T subset U`, introduce a cross variable `x_(T,U)`.  For
`T in I` and an
unordered pair `{a,b} subset V\T`, introduce `y_(T;a,b)` for the `BB` edge

\[
                   (T\cup\{a\})(T\cup\{b\}).          \tag{9.29}
\]

### Theorem 9.6 (exact endpoint-matching completion)

The fixed forest `P` extends to a middle-owner-exact degree-two factor with
exact lower `q=1` and complete upper `q=1` if and only if binary `x,y` satisfy

\[
 \sum_{U\supset T}x_{T,U}=1                           \tag{9.30a}
\]

for every `T in E`,

\[
 \sum_{\{a,b\}\subseteq V\setminus T}y_{T;a,b}=1     \tag{9.30b}
\]

for every `T in I`, and, for every `U in B`,

\[
 \sum_{\substack{T\in E\\T\subset U}}x_{T,U}
 +\sum_{\substack{T\in I,\{a,b\}\subseteq V\setminus T:\\
          U=T\cup\{a\}\ \text{or}\ U=T\cup\{b\}}}y_{T;a,b}=2, \tag{9.30c}
\]

\[
 \lambda_U+\sum_{\substack{T\in E\\T\subset U}}x_{T,U}\ge1,  \tag{9.30d}
\]

and, for every `Q in binom(V,r+2)`,

\[
 \sum_{\substack{T\in I\\T\subset Q}}y_{T;Q\setminus T}\ge1.   \tag{9.30e}
\]

The `B` shore is a path forest precisely when the additionally selected
`BB` graph is acyclic, equivalently

\[
 \sum_{e\in E_{BB}(S)}y_e\le |S|-1
 \quad(\varnothing\ne S\subseteq\mathcal B).          \tag{9.31}
\]

#### Proof

Equations (9.30a)--(9.30b) choose one cross edge for every `A` endpoint and
one `BB` edge for every unused rank-`r` lower colour.  Equation (9.30c) is
exactly degree two at each `B` vertex.  All `A` degrees are already two.
Thus the chosen edges and `P` form a spanning two-factor.  Its lower colours
are exact by their labels, while (9.30d)--(9.30e) are exactly the two upper
channels of Theorem 9.5.  This proves sufficiency, and extracting the edge
indicators from any completion proves necessity.  The last assertion is the
standard edge-subset characterization of a forest.  \(\square\)

There is a useful genuine Hall theorem inside (9.30).  Fix a proposed `BB`
skeleton satisfying (9.30b), with `0<=deg_BB(U)<=2` for every `U`, and put

\[
 b_U=2-\deg_{BB}(U),\qquad
 \mathcal H=\{U:\lambda_U=0\}.                        \tag{9.32}
\]

The cross endpoints can be assigned exactly when `b_U>=1` on \(\mathcal H\)
and

\[
 |S|\le\sum_{U\in N(S)}b_U
 \qquad(S\subseteq E),                                \tag{9.33}
\]

where `N(S)` is the upper-containment neighbourhood of the endpoint family
`S`.  Indeed, (9.30b) and the forced counts give
`sum_U b_U=2C=|E|`; capacitated Hall then produces a containment matching
which fills every `b_U` exactly.  The condition `b_U>=1` on \(\mathcal H\) is precisely
the upper-`z` repair (9.30d).  This is the exact inductive endpoint-matching
test.  Its first obstruction is already statewise: an endpoint family `S`
whose available residual `B` capacity is smaller than `|S|`.  Total capacity
or Catalan cardinality alone cannot exclude it.

Even before a `BB` skeleton is fixed, every upper hole must capture a
distinct `A` endpoint.  Hence the necessary hole-SDR inequalities are

\[
 |\mathcal Q|\le
 \left|\left\{T\in E:\exists U\in\mathcal Q, T\subset U\right\}\right|
 \qquad(\mathcal Q\subseteq\mathcal H).               \tag{9.34}
\]

They are not sufficient for the residual degree equations, the `BB` upper
cover, or chronology.

### Corollary 9.7 (raw endpoint capacity is automatic)

If the `BB` degree reservations and the forced-hole destinations are
discarded, every endpoint family admits a containment assignment with load at
most two on each `B` vertex.  Indeed, the endpoint-to-`B` incidence graph has
left degree `r` and ambient right degree `r+1`; hence for every endpoint
family `S`,

\[
                  r|S|\le(r+1)|N(S)|\le2r|N(S)|,
\]

so `|S|<=2|N(S)|` and capacitated Hall applies.  Thus the genuine inductive
obstruction is not raw endpoint supply.  It is the correlation between the
`BB` residual degree vector, the `AA` hole set, and the endpoint locations.

### Corollary 9.8 (protected witnesses survive generalized braiding)

Assume a completed generalized braid is fully depth-`d` resident.  If one
`A` path has old bases `T_0,...,T_(L-1)`, then its erosion columns containing
`z` are exactly

\[
 \left\{\{z\}\cup\bigcap_{s=0}^{d}T_{i+s}:
               0\le i\le L-d-1\right\}.              \tag{9.35}
\]

Every window crossing into `B` omits `z`.  Therefore a child target
`{z} union S`, `|S|=r-d`, has positive compiler-port degree if and only if it
is one of (9.35); equal target and envelope ranks force equality, so no
one-core can repair a missing witness.  Summed over the `C` paths, the number
of `z`-containing erosion columns is exactly

\[
                       W-dC=(r+1-d)C.                 \tag{9.36}
\]

Thus the protected-parent-witness gate of Theorem 9.3 does not depend on
reverse-union blocks or on a common-colour matching.  It is intrinsic to the
`A` path forest.

For recursion, an `A` block carries its two endpoints, used lower colours,
the multiplicity vector `lambda`, and its physical queue/root/core/port
signature.  A `BB` block carries its used lower label, its upper union,
endpoint degrees, and the same physical signature.  At the root one imposes
(9.30)--(9.33), pairs the sector paths, orients the resulting cycles, and
evaluates their full physical cyclic signature.  When the library supplies
an equivariant quotient record, this is the `k`-lap power from Section 7;
otherwise it is evaluated directly on the physical cycles.  Consequently
Theorem 9.6 plus root acceptance is necessary and sufficient in every fixed
two-sector Catalan/SCD braid library for residence, all requested shadows,
and compiler readiness.  The q1 equations alone do not imply those later
conditions.  There are `2C` cross seams, so at fixed depth `q` their old/new
collars contain at most `2qC` based starts per side; overlaps are deduplicated
by the occurrence ledger, and one short window may cross several seams.

### Exact `k=13` calibration

The solver-free audit
`scratch/audit_k13_pascal_braid.py` reconstructs the frozen source factor
and reproduces `scratch/k13_pascal_braid_audit.json` byte for byte.  Their
SHA-256 values are respectively

```text
42f17b473ba9ecd0d024079ee4064813ba173aa2396263439c26cae1488303a7
36d357c38e22cce7c8570f7d21c0dae0edbfcb1ed2adfa5fb5c9fd482fade487
```

At `r=6`, it gives `W=924`, `N=792`, `C=132`, two physical cycles of
lengths `1547,169`, and exactly

```text
AA=792,  AB=132,  BA=132,  BB=660.
```

The 132 `A` paths have lengths `4..18`, so the distinguished-coordinate
positive runs pass depth three.  They partition all 924 old rank-six sets;
their 792 intersections are the complete rank-five deck.  Their adjacent
unions, however, have support only `645/792`, with load histogram
`1^516 2^111 3^18`, hence 147 holes and 147 units of excess.  None of the
132 following `B` runs is its canonical reversed union path, and no block is
self-closing.  The `B` forest has nine singleton paths, hence 264 endpoint
slots on 255 distinct endpoint vertices.  All 537 `B` interiors and 108 of
those endpoint vertices lie in the `AA`-union support; its 147 holes are
exactly the remaining endpoint vertices.  The 264 cross edges therefore
repair the upper-`z` support
to `792/792`; cross plus `BB` gives the lower no-`z` deck `924/924`, and
`BB` gives the upper no-`z` deck `495/495`.  Thus the strict direct Pascal
matching is not necessary even at the first calibrated optimum.

### Exact fixed-path `k=15` calibration

The independent model in
`MATH_THEOREM_GENERALIZED_PASCAL_BRAID_LINEAR_MODEL_20260729.md` lets the
`AA` forest be selected from the current audited `k=14` Hamilton path rather
than fixing it in advance.  At `r=7` the forced counts are

```text
A=3432,  B=3003,  C=429,
AA=3003, cross=858, BB=2574.
```

The exact lower-rainbow/degree-two system is feasible, and remains feasible
after adding the upper-`z` correction channel.  Requiring every `AA` component
to have at least four vertices is nevertheless infeasible already in
presolve.  Exact optimization of that same fixed-path lower/degree system
gives minimum 17 short components: thirteen of length two and four of length
three, with optimum equal to the lower bound.  This is a proof for that one
fixed even path, not a generalized-braid no-go.  It shows sharply that raw
endpoint capacity and upper-hole correction can succeed while the
distinguished-coordinate residence chronology fails.  The even path and its
lower-rainbow forest must therefore move jointly; the old `2918/3003`
common-colour score was measuring the wrong constraint.

A subsequent seeded solve satisfies all six generalized `q=1` equation
families simultaneously.  The self-contained factor artifact is

```text
scratch/k15_generalized_pascal_braid/full_q1_s15105.json
SHA-256 e8092469c88b0a224bf0b11ed2661e06b5de260cc349717ea704732f47e00f29
```

It has degree two on all 6,435 owners and nine cycles of lengths

```text
2499, 2135, 780, 552, 444, 13, 5, 4, 3.
```

The `AA`, cross, and `BB` counts are exactly `3003,858,2574`.  The two lower
decks are exact (`3003/3003` and `3432/3432`), while the upper covers are
complete (`3003/3003` containing `z` and `2002/2002` omitting `z`).  Thus
endpoint degree, both lower-label systems, and both upper-cover systems are
simultaneously feasible on the fixed path; none is the remaining gate.

Chronology fails sharply.  There are 1,527 depth-three residence defects,
of which 97 involve `z` (52 runs of length two and 45 of length three).  At
depths `q=2,...,7`, the lower/upper hole pairs are

```text
(941,276), (447,33), (68,3), (5,0), (0,0), (0,0).
```

Consequently this factor proves fixed-path `q=1` feasibility only.  It does
not prove residence, protected-window coverage, a compatible compiler core,
physical Hall, or an all-semilength recursion.  The named input path is not
hash-embedded in the JSON; the current file
`scratch/k14_common_colour_3opt_best_20260729.json` has SHA-256
`eeccbd6be6edeba88a5d953a1f543c8f77895bbbec0e6ab0fd4eadb9e05af546`,
while the stored cycles make the output factor itself independently
checkable.

The `k=13` calibration proves that the generalized signature is nonempty;
neither finite calibration proves a semilength-raising theorem.  The exact
remaining inductive lemma is to construct, at every new `r`, an `AA`
lower-rainbow path forest and a
`BB` labelled skeleton satisfying (9.30b), (9.30e), (9.31), the residual
endpoint Hall inequalities (9.32)--(9.33), and one accepting simultaneous
queue/shadow/compiler root signature.  No expansion theorem presently proves
these conditions, and the `k=13` certificate alone does not imply them.

## 9B. Two tight bands give the all-`m` forest base

For `m>=2`, the GMM tight-enumeration theorem supplies a useful general base,
but one nontriviality qualification and one label-selection gate must be
retained.
Put

\[
 C=\operatorname{Cat}_m=\frac1{m+1}\binom{2m}{m},\qquad
 W=(m+1)C,\qquad N=mC,                               \tag{9.37}
\]

and

\[
 N_2=\binom{2m}{m+2}=\frac{m(m-1)}{m+2}C,\qquad
 D=N-N_2=\frac{3m}{m+2}C.                            \tag{9.38}
\]

Thus

\[
 t:=D-C=\frac{2(m-1)}{m+2}C,\qquad
 N_2+t=N-C=(m-1)C.                                  \tag{9.39}
\]

All quantities are integers because they are differences of the displayed
binomial coefficients.

### Theorem 9.9 (tight-band forest projection)

Let a tight enumeration of levels `m-1,m` of `Q_(2m)` be projected to its
rank-`m` owners.  Mark the projected edges whose original step passes through
a rank-`m-1` vertex.  Then:

1. the projection is a Johnson Hamilton cycle on all `W` owners;
2. exactly `N` marked edges occur, and their intersections are every
   rank-`m-1` set exactly once;
3. the remaining `C=W-N` edges are the direct rank-`m` jumps; and
4. deleting all direct jumps gives a spanning linear forest `P_A` with
   exactly `C` components and the complete marked lower deck.

A component of `P_A` is isolated exactly when two direct jumps are
consecutive in the projected Hamilton cycle.  Bare tightness does not forbid
this; equivalently, usability requires the direct-jump set to be a matching
in the projected cycle.  Already at `m=2`, the tight cyclic listing

```text
12,1,13,3,23,34,14,4,24,2,(12)
```

has consecutive direct jumps `23--34--14`, so deleting them isolates `34`,
even though the retained intersection labels are exactly `1,3,4,2`.  Such an
isolated `A_T` cannot occur in an exact generalized braid,
because it would need two cross edges, both of lower colour `T`.  Hence the
direct projection is usable only under the no-consecutive-direct-jumps
condition.  Independently, the audited GMM--dummy Hamilton augmentation
constructs for every `m>=2` a spanning **nontrivial** lower-rainbow rank-`m`
linear forest with exactly `C` paths, so this qualification is not an
existence obstruction to the `A` base.

Likewise, project a tight enumeration of levels `m+1,m+2` to the `N`
rank-`m+1` owners.  Mark the edges passing through rank `m+2`.  There are
exactly `N_2` marked edges, their unions are every rank-`m+2` set exactly
once, and the other `D` edges are direct rank-`m+1` jumps.  Deleting all
direct jumps gives a spanning forest `P_B^0` with `D` components.  Contracting
those components turns the deleted direct jumps into one cyclic order on the
`D` component vertices, with isolated components retained as vertices.
Consequently, adding any `t=D-C` of the deleted jumps produces a spanning
rank-`m+1` forest `P_B` with exactly `C` components and `N-C` edges.  The
complete rank-`m+2` union cover persists.

#### Proof

In a two-level tight enumeration, every cross step has length one, no step
joins two vertices of the smaller level, and the only same-level steps are
distance-two jumps on the larger level.  Suppressing the smaller shore gives
the asserted Johnson Hamilton cycle.  Each smaller vertex appears once and
labels the unique projected edge through it, proving both marked-deck
statements and the counts.  Deleting `s>0` edges from a cycle gives a linear
forest with `s` components, including singleton intervals between adjacent
deleted edges.  For the upper band, the deleted jumps join those intervals in
their original cyclic order.  Since `t<D`, any `t` of those component-cycle
edges are acyclic and merge exactly `t` pairs of components.  Equations
(9.37)--(9.39) finish the count.  \(\square\)

The added `B` edges do not have freely assignable lower labels.  Their
intersections are fixed by their endpoints, and the `N_2` protected upper-
colour edges may already repeat lower labels.  The exact selection theorem is
as follows.

This failure occurs already at `m=3`.  On `[6]`, take the projected rank-four
Hamilton cycle

```text
1236,1234,1235,1256,1356,1346,1345,2345,
2346,1246,1245,1456,3456,2456,2356,(1236).
```

Mediate the six edges

```text
1236--1234, 1234--1235, 1256--1356,
1346--1345, 2345--2346, 1246--1245.
```

Their unions are the six rank-five sets exactly once, and inserting those
sets gives a literal tight enumeration: its flip length is
`12+18=30=(15+6)+(15-6)`.  But the first two protected edges both have lower
intersection `123`.  No endpoint augmentation can erase that duplicate.

### Theorem 9.10 (exact two-tight-band fusion criterion)

Fix a nontrivial `A` forest `P_A` from Theorem 9.9 or the GMM--dummy
construction.  Let `E_A` be its `2C` endpoint labels and put

\[
                     I_A=\binom{[2m]}{m}\setminus E_A,
                     \qquad |I_A|=N-C.                \tag{9.40}
\]

Fix an upper tight enumeration.  Let `E_0` be its `N_2` protected edges and
`J` its `D` deleted direct jumps.  Write `ell(e)` for the rank-`m`
intersection label of a Johnson edge.  There is a subset `S subseteq J` of
size `t` for which the augmented `B` forest has lower-label set exactly
`I_A` if and only if

1. the labels `ell(E_0)` are pairwise distinct and lie in `I_A`; and
2. every label in `I_A minus ell(E_0)` occurs on at least one edge of `J`.

Indeed, the difference has size

\[
              |I_A|-|E_0|=(N-C)-N_2=t.               \tag{9.41}
\]

Choose one direct jump carrying each missing label.  Distinct labels choose
distinct edges, and Theorem 9.9 makes every such `t`-set acyclic.  Necessity
is immediate.  Thus the lower-label gate is an exact rainbow selection, not
a further component-count problem.

The restriction to deleted cycle jumps is convenient but not necessary.
For an arbitrary set `J_*` of new Johnson edges between endpoint slots of
`P_B^0`, assume first that `ell(E_0)` is pairwise distinct and contained in
`I_A`, and put

\[
 K=I_A\setminus\ell(E_0).
\]

It is a valid augmentation exactly when

1. `deg_(J_*)(U)<=2-deg_(P_B^0)(U)` at every `B` owner;
2. after contracting the components of `P_B^0`, the resulting multigraph
   `J_*` is a forest (in particular it has neither a loop nor a parallel
   two-cycle); and
3. the intersection labels of `J_*` biject `K`.

Then `|J_*|=|K|=t`, so the augmented graph has `C` path components and exact
internal `B` lower labels, while its protected upper cover persists.  In the
direct-jump sublibrary, the first two conditions are automatic and the two
bullets preceding (9.41) are the complete criterion.

For a chosen `P_B=P_B^0 union S`, define its endpoint capacity

\[
                     b_U=2-\deg_{P_B}(U).             \tag{9.42}
\]

Let `lambda_U` be the `AA` upper load of `P_A`.  The two forests extend by
cross edges to an owner-exact degree-two factor with both lower decks exact
and both upper decks complete if and only if

\[
 \lambda_U+b_U\ge1
 \qquad\left(U\in\binom{[2m]}{m+1}\right)            \tag{9.43}
\]

and the capacitated endpoint Hall inequalities hold:

\[
 |X|\le\sum_{U\in N(X)}b_U
 \qquad(X\subseteq E_A),                              \tag{9.44}
\]

where `N(X)` is upper containment.  The sums of both shores are `2C`, so
Hall fills every `B` endpoint slot.  Equation (9.43) is then precisely the
upper-`z` correction, while the protected edges `E_0` already give the full
no-`z` upper cover.  Theorem 9.6 proves the stated equivalence.

### Corollary 9.11 (coloured cut--Hall form)

In the direct-cycle sublibrary, let `O subseteq J` be the direct edges left
omitted, so `P_B=H_B minus O`.  For a rank-`m` colour `T`, let `a_T` and
`r_T` be its multiplicities on `E_0` and `J`, respectively, and let `J_T`
be the direct edges of colour `T`.  With `o_e=1_(e in O)`, exact internal
`B` lower ownership is equivalent, colour by colour, to

\[
 a_T+r_T-\sum_{e\in J_T}o_e
       =\mathbf1_{\{T\notin E_A\}}.                  \tag{9.45}
\]

Summing (9.45) forces `sum_e o_e=C`.  The endpoint capacity is literally the
cut incidence

\[
 b_O(U)=\#\{e\in O:U\in e\}=2-\deg_{H_B\setminus O}(U).  \tag{9.46}
\]

Therefore the fixed two-cycle scaffold has an exact generalized `q=1`
completion if and only if (9.45) holds, every `AA` upper hole is incident
with a cut edge, and

\[
 |X|\le\sum_{U\in N(X)}b_O(U)
 \qquad(X\subseteq E_A).                              \tag{9.47}
\]

Equation (9.45) exposes the obstruction sharply.  An `A` endpoint colour
forces every direct `B` edge of that colour to be cut and forbids the colour
on `E_0`; a nonendpoint colour may occur at most once on `E_0`, and if it is
absent there exactly one direct occurrence must be retained.  Tightness
alone controls none of these opposite-colour clauses.

### Theorem 9.12 (exact endpoint-Hall/protected-window gate)

Remain in the direct-cycle sublibrary of Corollary 9.11 and orient each
nontrivial `A` path

\[
                 P=(T_0,T_1,\ldots,T_{L(P)-1}).
\]

Fix `1<=H<=m`.  For `1<=d<=H` and `S in binom([2m],m-d)`, define its
protected-window load

\[
 \omega_d(S):=
 \sum_{P}\#\left\{0\le i<L(P)-d:
              \bigcap_{j=0}^{d}T_{i+j}=S\right\}.    \tag{9.48}
\]

Assume every `A` path has at least `H+1` vertices and is locally resident
through depth `H`, meaning that every displayed `d+1`-vertex intersection
has rank exactly `m-d`.  Thus these are literal erosion windows for every
`d<=H`.  Then a cut
`O subseteq J` and a cross matching fuse the two forests into an exact
generalized `q=1` factor whose entire `z`-containing protected tower is
present through depth `H` if and only if all four following conditions hold:

1. the colour equations (9.45) hold for every rank-`m` colour;
2. `deg_O(U)>=1` for every `AA` upper hole `U` (`lambda_U=0`);
3. the single family of endpoint inequalities

   \[
       |X|\le\sum_{U\in N(X)}\deg_O(U)
       \qquad(X\subseteq E_A);                        \tag{9.49}
   \]

4. the pointwise protected-window inequalities

   \[
       \omega_d(S)\ge1
       \qquad\left(1\le d\le H,
                    S\in\binom{[2m]}{m-d}\right).    \tag{9.50}
   \]

Here (9.45) already forces `|O|=C`; hence the two sides of the capacitated
matching in (9.49) both have size `2C`.  Thus (9.49) is the **complete
remaining endpoint Hall condition** after a coloured cut has been chosen.
This asserts exact feasibility, not irredundancy of every member of the Hall
family; the family cannot be replaced by the scalar identity
`sum_U deg_O(U)=2C`.

#### Proof

Corollary 9.11 proves that (9.45) is exactly the internal `BB` lower-deck
condition and that `deg_O(U)` is exactly the number of available `B` endpoint
slots at `U`.  Condition 2 is precisely upper-hole exposure, and capacitated
Hall makes (9.49) necessary and sufficient for matching all `A` endpoints to
all these slots.  The resulting cross edges repair the `z`-upper holes; the
protected `E_0` edges retain the complete no-`z` upper deck.

Every cross edge leaves the `z` sector.  Consequently a window containing
`z` lies wholly inside one `A` path, and Corollary 9.8 identifies its erased
old-coordinate set with the consecutive intersection in (9.48).  Hence a
protected target `{z} union S` occurs if and only if it contributes to
`omega_d(S)`, proving that (9.50) is necessary and sufficient for the
claimed protected tower.  \(\square\)

This theorem deliberately stops at the exact interface justified by the two
tight bands.  Conditions (9.45), (9.49), and (9.50) do not by themselves
give residence in the other coordinate sectors, no-`z` deeper shadows,
orientation-compatible voltage, one-core closure, or common-`Q` compiler
Hall.  Those data still belong to the simultaneous physical signature of
Section 7.

This is the clean all-`m` reduction.  Tight enumeration proves all owner,
component, edge-count, lower-`AA`, and upper-`BB` ledgers.  What it does **not**
prove is a nonisolating `A` enumeration (the GMM--dummy construction supplies
that separately), or the simultaneous existence of a coloured cut satisfying
(9.45), hole exposure, the endpoint Hall inequalities (9.49), and the
protected-window inequalities (9.50).  Nor does it prove old-coordinate
residence, no-`z` deeper shadows, voltage, core closure, or compiler Hall
after the endpoint matching is oriented.  These conditions, carried by the
simultaneous fragment signature of Section 7, are the exact remaining GMM
endpoint-braid induction lemma.

## 9C. One four-level tight enumeration: exact quarantine gate

There is a tempting way to unify the two forests of Section 9B.  For
`m>=2`, work in
`Q_(2m)` on the four consecutive levels

\[
 \mathcal L=\binom{[2m]}{m-1},\quad
 \mathcal M=\binom{[2m]}m,\quad
 \mathcal U=\binom{[2m]}{m+1},\quad
 \mathcal H=\binom{[2m]}{m+2}.                       \tag{9.51}
\]

Their sizes are respectively `N,W,N,N_2`, with the notation (9.37)--(9.39).
The two cube-parity shores are

\[
 \mathcal P=\mathcal L\mathbin{\dot\cup}\mathcal U,
 \qquad
 \mathcal Q=\mathcal M\mathbin{\dot\cup}\mathcal H,
\]

and

\[
 |\mathcal P|=2N,\qquad |\mathcal Q|=W+N_2,\qquad
 |\mathcal P|-|\mathcal Q|=t.                        \tag{9.52}
\]

Thus the numerical coincidence in the proposed construction is exact.
What tightness does with this imbalance requires a separate audit.

### Theorem 9.13 (four-level transition simplex)

Every tight cyclic enumeration of the four levels (9.51) has exactly `t`
same-shore transitions in `P`, each of Hamming length two; it has no
same-shore transition in `Q`, and every other transition is a one-bit cube
edge.

Let

```text
u = number of (m-1,m-1) two-flip steps,
v = number of (m-1,m+1) two-flip steps,
w = number of (m+1,m+1) two-flip steps.
```

Then

\[
                         u+v+w=t,                    \tag{9.53}
\]

and the three possible one-bit cross-rank counts are exactly

\[
\begin{aligned}
 e_{m-1,m}&=2N-2u-v,\\
 e_{m,m+1}&=2C+2u+v,\\
 e_{m+1,m+2}&=2N_2.
\end{aligned}                                        \tag{9.54}
\]

Consequently the desired **upper quarantine** is the special corner

\[
       u=v=0,\quad w=t,
 \qquad\Longleftrightarrow\qquad e_{m-1,m}=2N.        \tag{9.55}
\]

It is consistent with every rank and parity count, but it is not forced by
tightness.

#### Proof

Let `p` be the number of cross-shore steps and let `x,y` be the numbers of
same-shore steps in `Q,P`, respectively.  Counting cyclic incidences gives

\[
 p+2x=2(W+N_2),\qquad p+2y=4N.
\]

A cross-shore step costs at least one flip and a same-shore step at least
two.  The tight length is

\[
 |\mathcal P|+|\mathcal Q|+t=2|\mathcal P|=4N.
\]

The metric lower bound is `p+2x+2y=4N+2x`; hence `x=0`, `y=t`, and every
step attains its local minimum.  This proves the first assertion and
(9.53).  A rank-`m+2` vertex can now be adjacent only to rank `m+1`, giving
`e_(m+1,m+2)=2N_2`.  Counting incidences at ranks `m-1` and `m` gives the
first two equations of (9.54).  Finally,
`2N-e_(m-1,m)=2u+v`, so equality in (9.55) is equivalent to `u=v=0`.
\(\square\)

The source scope matters.  GMM Corollary 2 states existence of a tight
enumeration for every consecutive level interval; for this noncentral case
its proof delegates to the earlier trimming-and-gluing theorem.  The GMM
statement and its proof carry no parameter locating the same-shore steps
among the ranks.  Therefore the published GMM theorem proves (9.53), not
the corner (9.55); whether the delegated construction can be strengthened
to force that corner is a new question.

This is not merely a logical nicety.  At `m=2`, each of the following is a
tight cyclic listing of all nonempty subsets of `[4]`:

```text
low--low:
4,34,3,23,234,24,2,12,124,1234,123,13,134,14,1,(4)

low--high:
1,14,134,34,4,24,2,12,124,1234,234,23,3,13,123,(1)

high--high:
123,13,3,23,234,34,4,24,2,12,1,14,134,1234,124,(123)
```

Each has fourteen cube edges and one two-flip step, respectively
`1--4`, `123--1`, and `124--123`.  Thus all three vertices of the transition
simplex occur already in the smallest case.  In particular, no invariant of
bare tightness can quarantine the excess, while the last listing shows that
no rank-count obstruction forbids quarantine.

### Theorem 9.14 (quarantine is exactly a Hamilton braid skeleton)

Assume (9.55).  Suppress all vertices of `L` and `H`.  Relabel a retained
`T in M` as the child owner `A_T={z} union T`, and a retained `U in U` as
`B_U=U`.  The resulting cyclic order is one Johnson Hamilton cycle on the
middle level of `[2m] union {z}`.  Its exact sector census is

\[
\begin{array}{c|c|c}
\text{edge type}&\text{number}&\text{marked deck}\\ \hline
AA&N&\mathcal L\text{ intersections, once each}\\
AB+BA&2C&\text{cross seams}\\
BB_{\rm protected}&N_2&\mathcal H\text{ unions, once each}\\
BB_{\rm merge}&t&\text{unmarked direct joins}.
\end{array}                                           \tag{9.56}
\]

In particular, the total `BB` count is `N_2+t=N-C`.  The induced `AA` and
`BB` graphs are spanning linear forests with exactly `C` components each.
Either forest may still contain isolated owners; exact opposite lower
ownership will forbid `AA` isolates but may retain two-port `BB` singletons.

Conversely, suppose a child Johnson Hamilton cycle has the four counts
(9.56), its `AA` intersections biject `L`, and a distinguished set of
`N_2` protected `BB` edges has unions bijecting `H`.  Subdivide every `AA`
edge by its intersection and every protected `BB` edge by its union.  This
gives a quarantined tight enumeration of (9.51).  Hence upper-quarantined
four-level tight enumerations and Hamilton generalized-braid skeletons with
these two marked decks are equivalent objects.

#### Proof

Under (9.55), every rank-`m-1` vertex is flanked by two rank-`m` vertices,
and every rank-`m+2` vertex is flanked by two rank-`m+1` vertices.  Suppression
therefore turns them into the marked `AA` and protected `BB` Johnson edges.
The other transitions are the `2C` containment edges and the `t` direct
rank-`m+1` Johnson edges from (9.54).  Every retained owner occurs once, so
the result is one Hamilton cycle.  Removing the `2C>0` cross edges from
that cycle leaves sector path forests; their edge counts give `C`
components on each shore.

For the converse, expansion lists every vertex of the four levels once.
Its total Hamming length is

\[
                  2N+2N_2+2C+2t=4N,
\]

which is the tight value, and only the `t` unprotected `BB` edges remain
as same-shore transitions.  \(\square\)

Theorem 9.14 is a useful unification, but also identifies the exact scope:
proving quarantine for every `m` is already a new constrained-enumeration
theorem that constructs the Hamilton braid skeleton.  It is not a free
corollary of the GMM tight-enumeration existence theorem.

### Theorem 9.15 (opposite colours and Hall after quarantine)

For the projected cycle, define

\[
\begin{aligned}
 d_\times^A(T)&=\#\{A_TB_U\text{ cross edges}\},\\
 \mu_B(T)&=\#\{B_UB_V:U\cap V=T\},\\
 \lambda_U&=\#\{A_TA_{T'}:T\cup T'=U\},\\
 d_\times^B(U)&=\#\{A_TB_U\text{ cross edges}\}.
\end{aligned}                                        \tag{9.57}
\]

The quarantined cycle has both lower `q=1` decks exact and both upper
`q=1` decks complete if and only if

\[
 d_\times^A(T)+\mu_B(T)=1
       \qquad\left(T\in\binom{[2m]}m\right),          \tag{9.58}
\]

and

\[
 \lambda_U+d_\times^B(U)\ge1
       \qquad\left(U\in\binom{[2m]}{m+1}\right).      \tag{9.59}
\]

Indeed, the marked `AA` edges already give the complete `z`-lower deck and
the protected `BB` edges already give the complete no-`z` upper deck.
Equation (9.58) is exactly the opposite no-`z` lower deck, while (9.59) is
exactly the `z`-upper cover.  In particular, (9.58) forces
\(d_\times^A(T)\le1\), so the `AA` forest has no isolates; its cross labels
are its `2C` distinct endpoint set, and the `BB` intersections biject the
complement.

For one fixed quarantined enumeration satisfying (9.58), the `AA` endpoints
are distinct and its existing cross edges witness endpoint Hall and connected
monodromy.  Before (9.58), the same seams still fill endpoint *occurrences*,
but an `AA` isolate contributes two copies of one lower label and does not
belong to the distinct-label `E_A` formulation.  If instead two induced
`C`-path forests already satisfying the opposite-lower condition are retained
and their cross seams are reassigned, put

\[
                         b_U=2-\deg_{P_B}(U).
\]

The containment inequalities

\[
 |X|\le\sum_{U\in N(X)}b_U
       \qquad(X\subseteq E_A)                         \tag{9.60}
\]

are necessary and sufficient for a degree-two cross matching.  Together
with upper-hole exposure `lambda_U+b_U>=1`, they are necessary and sufficient
for such a matching to retain the complete `z`-upper deck.  To recover one
tight cyclic enumeration rather than an arbitrary two-factor, the
contracted path-component graph must additionally be connected; equivalently
the selected matching obeys

\[
 |\delta_{M_\times}(\mathscr S)|\ge2                  \tag{9.61}
\]

for every nonempty proper family \(\mathscr S\) of contracted components,
where \(M_\times\) is the selected cross matching.  Thus the
single chronology absorbs Hall and subtour feasibility only when its actual
cross edges are kept; it does not prove that a separately prescribed pair
of decks can be re-paired.

Finally, quarantine does not address protected chronology.  The `A` paths
must still be locally resident, have length at least `H+1`, and satisfy the
pointwise inequalities (9.50).  Other-coordinate residence, no-`z` deeper
shadows, voltage/core closure, and common-`Q` compiler Hall remain outside
the four-level theorem.

### Corollary 9.16 (a global `q=1`-perfect carrier lifts directly)

Let `F` be a Hamilton cycle of
`J([2m] union {z},m+1)`.  Assume that its edge intersections are exactly
all rank-`m` lower targets, once each, and that its adjacent edge unions
cover every rank-`m+2` upper target.  Split its owners into

```text
A_T={z} union T,  |T|=m,          B_U=U,  |U|=m+1.
```

Then the sector counts are forced:

\[
 |E_{AA}|=mC=N,\qquad |E_\times|=2C,\qquad
 |E_{BB}|=(m-1)C=N-C.                               \tag{9.62}
\]

Moreover every no-`z` upper target
`Y in binom([2m],m+2)` is the union of at least one `BB` edge.  Choose one
such edge for every `Y`.  These `N_2` choices are automatically distinct,
and the number of unchosen `BB` edges is

\[
                 (m-1)C-N_2=t.                      \tag{9.63}
\]

Declare the chosen edges protected and the rest merges.  Expanding every
`AA` edge through its old-coordinate intersection and every protected `BB`
edge through its union gives a `q=1`-decorated B-quarantined tight
enumeration whose contraction is `F`.

#### Proof

Only an `AA` edge has a lower colour containing `z`.  Exact lower ownership
therefore makes its intersections precisely the `N` targets
`{z} union binom([2m],m-1)`, proving the first count in (9.62).  Degree two
on the `W` A-owners gives

\[
                         2W=2|E_{AA}|+|E_\times|,
\]

so \(|E_\times|=2(W-N)=2C\); subtracting from the `W+N` cycle edges gives
`|E_BB|=W-2C=(m-1)C`.

An adjacent union omits `z` only on a `BB` edge.  Hence upper `q=1`
coverage makes every no-`z` target have a nonempty `BB` fibre.  Distinct
targets have disjoint fibres because one edge has one union, so one
representative per fibre uses `N_2` distinct edges.  Equation (9.63) is
(9.39), and Theorem 9.14 gives the claimed expansion.  \(\square\)

At upper `q=1`, adjacent-union coverage is equivalent to arbitrary
nontrivial-interval coverage: if a carrier interval has union `S` of rank
`m+2`, any adjacent Johnson pair inside it already has a rank-`m+2` union
contained in `S`, hence equal to `S`.  This argument is special to that
rank and fails for deeper upper targets.

Thus a global `q=1`-perfect Hamilton carrier automatically satisfies the
opposite-colour quotas (9.58), upper-hole exposure (9.59), endpoint Hall,
and the connected-component subtour condition: its actual cross seams are
the certificate.  These become independent gates only when the `AA` and
`BB` forests are chosen separately and then re-paired.

The word “upper” here is strictly depth one.  The hypothesis concerns unions
of two adjacent owners only.  Exact lower `q=1` already gives the depth-one
protected deck and forbids `AA` isolates (equivalently singleton `z`-runs),
but there is no protected-window or residence conclusion at depth at least
two, no coverage of unions of three or more consecutive owners, and no core
or compiler conclusion.

The desired `m=2` quarantined listing above calibrates both gaps.  Its
projected child cycle is

```text
B123,A13,A23,B234,A34,A24,A12,A14,B134,B124,(B123).
```

Its cross lower labels are `13,23,34,14`, while its two `BB` intersections
are `14,12`; it repeats `14` and misses `24`, violating (9.58).  Its `A`
path lengths are `2,4`, so it also fails depth-two protected residence.
Therefore even a literal quarantined tight enumeration does not by itself
solve either the opposite-colour or protected-window gate.

The exact new existence question is now sharply separated:

> **Quarantined four-band braid lemma.**  For every required `m`, construct
> a tight enumeration of (9.51) satisfying (9.55), (9.58), (9.59), and the
> protected-window conditions (9.50), with an accepting simultaneous
> residence/shadow/core/compiler signature.

No theorem audited here proves this lemma.  Counts and parity do not
obstruct its quarantine clause; the `m=2` example proves that quarantine
alone is strictly weaker than the decorated conclusion.

## 9D. Complement coherence collapses lower `q=2` and upper `q=1`

Let

\[
 \mathsf W=\binom{2m+1}{m+1}=(2m+1)C,
\]

and let `T=(T_i)_(i in Z_(mathsf W))` be a Hamilton cycle of
`J(2m+1,m+1)` with exact lower `q=1`.  Put

\[
                         X_i=T_i\cap T_{i+1}.         \tag{9.64}
\]

Then the alternating sequence

\[
 T_0,X_0,T_1,X_1,\ldots,T_{\mathsf W-1},X_{\mathsf W-1},T_0
                                                               \tag{9.65}
\]

is a Middle Levels Hamilton cycle, and conversely every such cycle contracts
to a lower-`q=1`-exact `T`.  Moreover

\[
 X_i=T_i\cap T_{i+1},\qquad T_i=X_{i-1}\cup X_i.     \tag{9.66}
\]

### Theorem 9.17 (complement half-turn duality)

If (9.65) is invariant under set complementation, meaning that
complementation preserves its selected cycle-edge set, then `mathsf W` is odd.
Write

\[
                         \mathsf W=2s+1.
\]

With the indexing (9.65), complementation is necessarily the half-turn

\[
 \overline{T_i}=X_{i+s},\qquad
 \overline{X_i}=T_{i+s+1}.                            \tag{9.67}
\]

Consequently

\[
 \overline{X_i\cap X_{i+1}}
        =T_{i+s+1}\cup T_{i+s+2}.                    \tag{9.68}
\]

The left side is the complement of the lower-`q=2` label of `T` at `i`;
the right side is its upper-`q=1` label at `i+s+1`.  Hence the two decks
have identical load multisets under complementation, and either is complete
if and only if the other is.

More generally, for every `q>=0`,

\[
 \overline{\bigcup_{j=0}^{q}T_{i+j}}
      =\bigcap_{j=0}^{q+1}T_{i+s+j}.                 \tag{9.68a}
\]

This is an exact set/multiset identity.  Expected-rank language at greater
depth still requires the corresponding rank or residence hypothesis.

#### Proof

Exact lower `q=1` makes the `X_i` distinct and exhaustive.  Consecutive
`X_(i-1),X_i` are distinct rank-`m` facets of `T_i`, proving (9.65)--(9.66).
Complementation induces an involutory dihedral automorphism of the abstract
cycle.  A vertex-axis reflection would fix a set.  An edge-axis reflection
would force an incident Middle Levels pair `S--overline S`, impossible
because a nonempty set is disjoint from its complement.  Thus only the
half-turn remains; it swaps the two rank shores exactly when `mathsf W` is
odd, and its position shift gives (9.67).  De Morgan gives (9.68), while
intersecting `overline(T_(i+j))=X_(i+s+j)` and using (9.64) gives (9.68a).
\(\square\)

In fact `mathsf W` is odd exactly when `m=2^a-1`.  This includes `k=15`
but not arbitrary odd dimension.  Complement symmetry does not itself make
either deck complete; it turns the two coverage tests into one.  In
particular, lower `q=2` completeness plus Theorem 9.17 supplies the
upper-`q=1` hypothesis of Corollary 9.16.

### Corollary 9.18 (strict `c`-space NAND law)

Assume additionally voltage-one equivariance and put

\[
 \mathsf N=\mathsf W/(2m+1)=C,
 \qquad
 T_i(c)=\{x\in\mathbb Z_{2m+1}:c_{i-x\mathsf N}=1\}. \tag{9.69}
\]

Then complement coherence (9.67) is equivalent to

\[
                  1-c_p=c_{p+s}c_{p+s+1}
                  \qquad(p\in\mathbb Z_{\mathsf W}).           \tag{9.70}
\]

Let `tau=s+1`, the inverse of two modulo `mathsf W`, and set
`d_i=c_(tau i)`.
Then (9.70) is equivalent to

\[
                 d_{i+1}=1-d_id_{i+2}
                 =\operatorname{NAND}(d_i,d_{i+2}). \tag{9.71}
\]

Equivalently, the cyclic word `d` contains neither `00` nor `111`.

Indeed, membership of coordinate `x` in
`overline(T_i)=T_(i+s) cap T_(i+s+1)` gives (9.70) with
`p=i-x mathsf N`.  Since `2(s+1)=1 mod mathsf W`, substituting
`p=(s+1)(i+1)` yields (9.71).  Its allowed triples are exactly
`010,011,101,110`, proving the forbidden-factor form.

The class sums force `(m+1)C` ones and `mC` zeros.  Hence `d` has `mC`
one-runs, of which exactly `C` have length two and `(m-1)C` are singletons.
Since `c_p=d_(2p)`, the physical `1`-to-`0` transitions of `c` are exactly
the `110` factors ending those length-two runs.  Thus `c` has exactly `C`
cyclic one-runs.

For `k=15`, `(mathsf W,mathsf N,s,tau)=(6435,429,3217,3218)`.  The NAND law
forces `d` to have 3,003 isolated zeros, 429 length-two one-runs, and 2,574
singleton one-runs, while `c` has 429 physical one-runs.  The short `d` runs
are not residence defects: residence is measured in the original `c` order.
The law is necessary and sufficient for complement coherence inside the strict
binary-trace gauge; it does not supply the rank-sum, Johnson, Hamilton,
lower-rainbow, lower-`q=2`, deeper-shadow, or compiler conditions.

## 10. Exact finite obstructions and their scope

The audited original 135-member `k=14` path library gives an exact obstruction
to that finite library.  Its best common-colour matching has size

\[
                         2739<3003,                    \tag{10.1}
\]

so deficiency `264` already prevents (9.4)--(9.5), before spacing,
residence, deeper roots, or compiler ports are imposed.  The fact that the
two colour families separately cover all targets does not alter this
matching obstruction.

This is not an invariant of every rank-seven Johnson path and not a
cardinality heuristic.  It proves only that none of those 135 paths activates
the strict Pascal lift.  Later local path trades reach `2918/3003`; the
generalized `k=13` braid moreover proves that even a deficit in this strict
score is not a barrier to a two-sector completion.

Independently, the exact complete audit of the natural MMM compatible
gluing-tree/parallel-label family at `k=11` contains no member simultaneously
passing residence, lower `q=2`, and upper `q=1`.  Therefore no all-odd rule
whose range is confined to that natural family can produce the root object
of Theorem 7.1.  This says nothing about unrestricted alternating circuits
from the MMM base factor, unrelated SCD path grammars, or the broader
component-and-seam architecture.

There is one exact capacity obstruction to the one-letter graded compiler:

\[
                     \sum_{s=1}^{h}\binom{k}{s}\le W. \tag{10.2}
\]

Its failure rules out this `DA=DP` one-position-per-low-target architecture,
because the left target shore is larger than the physical position shore.
It does not rule out a multirow compiler.  No other Catalan count or entropy
comparison in this report is used as an impossibility argument.

## 11. From a ready pair to a literal word

For a strict cyclic MMM pair `(T,C)`, Theorem 3.1 gives a cyclic graded word
`A`.  If an edge `e` of `T` is avoided by at least one based witness interval
of every required upper target, cut at `e`, rotate `A` accordingly, and append
its first `d` letters.  Every cyclic cell of `D^jA`, `0<=j<=d`, then occurs
among the first `W` linear starts, while all chosen upper witnesses remain
nonwrapping.  Explicitly, `D^dA=T`, and a nonwrapping carrier interval obeys

\[
                 \bigcup_{i=a}^{b}T_i
                  =\bigcup_{j=a}^{b+d}A_j.            \tag{11.0}
\]

Appending the first `d` letters therefore makes every chosen carrier
witness a literal letter interval after the cut.  Thus an all-upper interval
signature plus one such safe cut turns the compiler-ready pair into a
literal word of length `W+d`.

The safe-cut condition is exact.  If `W(U)` is the family of based cyclic
carrier-`T` witness intervals for upper target `U` and `E(I)` is the set of
internal cycle edges crossed by `I`, define

\[
 M(U)=\bigcap_{I\in\mathcal W(U)}E(I).                 \tag{11.1}
\]

An edge is simultaneously safe if and only if

\[
                     e\notin\bigcup_U M(U).            \tag{11.2}
\]

Fixed-depth root completeness alone certifies only the requested fixed
depths.  For literal arbitrary upper intervals at depths `q>=3`, one must use
the exact interval algebra (7.1)--(7.4) before applying (11.1)--(11.2).
If safe-cut eligibility is to be carried recursively, every upper witness
must retain its based endpoints and crossed-edge span, as in the occurrence
ledger of Section 6.  Deduplicating witnesses merely by union mask and length
does not determine `M(U)`.  Equivalently, one may first construct the final
explicit chronology by Theorem 7.1 and then rescan it exactly for (11.1).
Thus Theorem 7.1 certifies a cyclic decorated pair; the span-refined record or
this final rescan is additionally required to certify a literal safe cut.

The raw Pascal lift instead yields `Cat_r` cycles.  Its componentwise
compiler profile is exact, but one linear word additionally requires chosen
cuts and joins whose final queue, roots, upper witnesses and port relation
are re-evaluated.  Topological component count is not a decoration theorem.
In particular, a later `C6` or splice can shorten the `z`-runs, so the spacing
certificate (9.7) is not inherited without rerunning the final residence
queue.

## 12. Proved theorem and conjectural recursion

The following statements are proved in this report.

1. The residence queue determines the maximal erosion and carries the
   one-core transition; at depth three that transition is also the lower
   `q=2` root.
2. Actual stabilizer-weighted Hall is an exact root test for an equivariant
   core at every odd composite `k`.
3. The endpoint-typed port profile is associative under concatenation,
   reversal, rotation and the voltage-twisted quotient closure.
4. An MMM gluing hexagon is a literal three-head transfer, with exact
   fixed-depth, residence, erosion and port collar identities.
5. Within any fixed compatible MMM gluing library, Theorem 7.1 is a
   necessary-and-sufficient finite certificate for a compiler-ready pair.
6. In the strict direct Pascal sublibrary, the even-to-odd input is exactly a
   chronologically spaced common-colour matching, and Theorem 9.2 is a
   necessary-and-sufficient SCD/Pascal prefix recursion jointly carrying the
   odd compiler profile.
7. Compiler readiness in the Pascal branch forces the protected parent
   depth-`d` witness condition (9.15)--(9.18) and the literal Hall shores
   (9.19)--(9.21).
8. The Pascal child is radius one in the common-matching indicator, giving
   the exact bounded compound-switch and collar bounds of Theorem 9.4.
9. A generalized Pascal braid is exactly two lower-labelled sector path
   systems joined by the binary completion equations (9.30); conditional on
   its `BB` skeleton, the remaining cross-collar problem is precisely the
   capacitated endpoint Hall criterion (9.32)--(9.33), while (9.35)--(9.36)
   give its intrinsic protected compiler-witness gate.
10. Two GMM tight bands give the exact all-`m` forest and component counts.
    The upper forest can always be reduced from `D` to `Cat_m` components by
    restoring `D-Cat_m` deleted jumps.  Theorem 9.10 isolates the remaining
    opposite-label selection and endpoint Hall conditions exactly; bare
    tightness implies neither.  Theorem 9.12 gives the exact fusion gate:
    the coloured cut equations, upper-hole exposure, capacitated Hall
    (9.49), and the pointwise protected-window inequalities (9.50).
11. One four-level tight enumeration contracts to the desired Hamilton
    braid skeleton exactly when every parity-defect step is quarantined to
    rank `m+1`.  Theorem 9.13 proves the full rank-transition simplex and
    shows GMM tightness does not force that corner; Theorems 9.14--9.15 give
    the reversible projection and the exact remaining opposite-colour,
    upper-hole, Hall/subtour, and protected-window gates.
    Corollary 9.16 proves that a global lower-exact/upper-q1-complete
    Hamilton carrier automatically discharges all of those q1 port gates
    and lifts by choosing one protected `BB` edge per no-`z` upper target;
    it makes no deeper-shadow claim.
    Theorem 9.17 proves that complement coherence identifies its lower
    `q=2` and upper `q=1` decks by a shifted complement, while Corollary 9.18
    reduces strict `c`-space coherence to the cyclic NAND/no-`00`/no-`111`
    law.  This applies only when the middle-layer size is odd, including
    `k=15`, and does not imply coverage.
12. The frozen fixed-path `k=15` artifact satisfies both exact lower decks,
    both complete upper decks, and degree two simultaneously.  Its 1,527
    residence defects and explicit deeper holes show that the remaining
    finite gates are chronology, protected windows, and compiler coupling,
    not `q=1` compatibility.

The tempting uniform statement

> every odd semilength has an accepting compatible MMM gluing tree

is false for the natural published gluing-tree/parallel-label family, by the
exact `k=11` family audit.  The corresponding statement for the full
sign-compatible alternating-circuit class remains open:

> **Compiler-ready alternating-circuit conjecture.**  In every intended odd
> depth regime satisfying the exact one-letter capacity condition, some
> owner-exact alternating-circuit sum from an MMM base factor has a connected
> unit-voltage terminal quotient and an accepting terminal signature
> satisfying the conditions of Theorem 7.1.

This conjecture is stronger than needed for optima which use several factor
components.  It is not proved here.

The even recursion has a distinct open lemma:

> **Protected Pascal matching lemma.**  Construct an even Johnson path and
> one spaced common-colour matching which protects all required parent
> shadow witnesses and whose `Cat_r` odd component port-profile product
> satisfies physical Hall after any declared joins.

The saved `k=14` paths refute this lemma only for that saved path library.
No invariant obstruction for all even paths has been proved.

The generalized braid has the broader unresolved induction:

> **Decorated endpoint-braid lemma.**  For every required semilength, produce
> a nontrivial lower-rainbow `A` forest (from a nonisolating tight projection
> or the GMM--dummy construction), an upper tight-band cycle, and a direct
> cut `O` satisfying the colour equations (9.45), upper-hole exposure, the
> endpoint Hall inequalities (9.49), and the protected-window inequalities
> (9.50), such that the oriented completion has an accepting simultaneous
> queue/shadow/compiler signature.

The exact `k=13` factor is a positive instance.  No recursive expansion
theorem proving this statement for all `r` is known here.

Thus the mathematical advance is an exact compiler-ready Catalan state and
sharp architecture-specific gates, not an all-odd existence theorem.

## 13. Dependencies and audit scope

This report uses the proved results in

```text
MATH_MERINO_MICKA_MUTZE_STRICT_SPIRAL_PROJECTION_20260729.md
MATH_AUDIT_MMM_GLUING_SWITCH_PARAMETRIZATION_20260729.md
MATH_THEOREM_DECORATED_MMM_ALTERNATING_SWITCH_AND_K15_SUPPORT_OBSTRUCTION_20260729.md
THREAD_A_GENERAL_ODD_K_MMM_SHADOW_PATH_DECORATION_RECURSION_20260729.md
THREAD_D_STRICT_EQUIVARIANT_COMPACT_SHADOW_CIRCUIT_EXISTENCE_20260729.md
MATH_THEOREM_EQUIVARIANT_GRADED_COMPILER_QUOTIENT_HALL_20260729.md
THREAD_C15_WEIGHTED_ORBIT_QUOTIENT_HALL_AUDIT_20260729.md
THREAD_K_CATALAN_LEAVE_CORRECTION_FLOW_SDR_AND_MINIMAL_OBSTRUCTIONS_20260729.md
MATH_THEOREM_EVEN_TO_ODD_COMMON_COLOUR_PASCAL_LIFT_20260729.md
MATH_AUDIT_K13_GENERALIZED_PASCAL_BRAID_20260729.md
MATH_THEOREM_GENERALIZED_PASCAL_BRAID_LINEAR_MODEL_20260729.md
MATH_THEOREM_GMM_MIDDLE_LEVELS_DOUBLE_RAINBOW_FUSION_AUDIT_20260726.md
MATH_AUDIT_Q1_FIXED_COLOR_PAIR_NORMAL_FORM_20260726.md
MATH_THEOREM_FULL_BAND_TIGHT_ENUMERATION_CONTRACTION_DEFECT_20260726.md
MATH_THEOREM_QUARANTINED_FOUR_LEVEL_TIGHT_ENUMERATION_BRAID_20260729.md
MATH_THEOREM_BINARY_TRACE_SPIRAL_NORMAL_FORM_20260729.md
MATH_THEOREM_TRACE_QUARANTINE_COLLAPSE_20260729.md
MATH_THEOREM_COMPLEMENT_COHERENT_CSPACE_NAND_NORMAL_FORM_20260729.md
tmp/central/gmlc2.tex
```

Independent proof lanes checked the queue/shadow, switch, compiler-port,
generalized-braid, tight-projection, global-`q=1`, complement/NAND, and
finite-artifact parts.  The finite
`k=11`, `k=13`, `k=14`, and `k=15` statements are used only with their
audited scopes.  No numerical census is promoted to an asymptotic or
unrestricted impossibility claim.
