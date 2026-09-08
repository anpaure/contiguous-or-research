# Squarefree moving-hole packets have a vanishing active fringe: an exact provider-transport and shadow-capacity obstruction

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Put

\[
 V=[2m],\qquad M=m+H,\qquad s=m-H,
 \qquad W=\binom{2m}{m},\qquad
 N_H=\binom{2m}{m-H}.
\tag{0.1}
\]

Assume the separation hypotheses of the audited packet theorems and
(H=o(m)).  At the promotion calibration we additionally use

\[
 H^2/m=\log m+o(1),\qquad MN_H=(1+o(1))W.
\tag{0.2}
\]

Consider the following exact-middle packets:

1. the three-top two-base conveyor, in full or protected common-hole
   form;
2. its symmetric six-top realization;
3. the squarefree four-top one-hole cube; and
4. the squarefree eight-top one-hole cube.

For a packet (P), let (S(P)) be its common squarefree middle-owner
support, and let

\[
 p_P^0,p_P^1:S(P)\longrightarrow \binom Vs
\tag{0.3}
\]

be the unique old and new provider-root maps.  The principal exact
census is

\[
\begin{array}{c|c|c|c|c}
P&\text{roots}&\text{phases/root}&
 |\mathcal D_A^0\cap\mathcal D_A^1|&
 \mu(P):=|\{D:p_P^0(D)\ne p_P^1(D)\}|\\ \hline
T_3\text{ full}&3&M&M-2H&6H\\
T_3\text{ protected}&3&M-1&M-2H-1&6H\\
T_6^{\rm sym}\text{ full}&6&M&M-2H&12H\\
T_6^{\rm sym}\text{ protected}&6&M-1&M-2H-1&12H\\
T_4&4&M-1&M-2H-1&8H\\
T_8&8&M-1&M-3H-1&24H.
\end{array}
\tag{0.4}
\]

Here (mathcal D_A^i) is the middle deck at one touched root (A) on
shore (i).  Consequently every eligible packet satisfies

\[
 \boxed{\quad
 \frac{\mu(P)}{|S(P)|}\le \frac{3H}{M-1}.
 \quad}
\tag{0.5}
\]

This gives the requested statewise packing obstruction.  If a
simultaneous packet packing is owner-disjoint, then

\[
 \boxed{
 \sum_P\mu(P)
 \le {3H\over M-1}\sum_P|S(P)|
 \le {3H\over M-1}W=o(W).}
\tag{0.6}
\]

Thus even a hypothetical packet packing covering (W-o(W)) middle
owners cannot change a positive density of MSW provider fibres.  This is
not a failure of a particular signing or nibble: it is a pointwise
exposure obstruction.

More generally, if every middle owner belongs to at most (B) packet
supports, counted with multiplicity along a sequential composition,
then

\[
 \sum_D d_J\bigl(p_{\rm initial}(D),p_{\rm final}(D)\bigr)
 \le {3HB\over M-1}W.
\tag{0.7}
\]

Moving (arepsilon W) provider fibres therefore forces

\[
 B\ge {\varepsilon(M-1)\over3H}
   =\left({\varepsilon\over3}+o(1)\right)
      \sqrt{m\over\log m}
\tag{0.8}
\]

at (0.2).  The surviving architecture is necessarily a high-overlap
serial or catalytic braid; it cannot be a bounded-overlap packing.

There is one essential endpoint caveat.  The four- and eight-top
patterns reverse long core runs, and therefore can reverse the directed
terminal phase of (Theta(M)) same-root owners per touched root.  Those
owners keep the same provider and the same unordered (H)-window.  This
dense operation lies in the unphased/load-neutral reversal corridor.  It
does not contradict (0.5)--(0.8), and it is not presently known to have
a simultaneous MSW mechanical-provenance embedding.  The theorem closes
positive-density **provider transport and unphased shadow repair**, not
the separate directed-endpoint-only route.

Finally, the older mixed-placeholder six-frame rectangle is not an
eligible exact-owner packet: its middle derivative has squared norm
(8H), and the favorable closing-collar shore contains exactly (2H)
middle collisions.  The symmetric six-top two-base realization in
(0.4) is the legal six-frame object.

## 1. Root frames, owner decks, and provider maps

For a promotion root

\[
 A\in\binom Vs,
 \qquad U_A=V\setminus A,
 \qquad |U_A|=M,
\tag{1.1}
\]

a retained cyclic frame on (U_A) has a family (mathcal J_A) of
retained cyclic (H)-windows.  Its physical middle deck is

\[
 \mathcal D_A=\{A\cup J:J\in\mathcal J_A\}
 \subseteq\binom Vm.
\tag{1.2}
\]

Equivalently, global complementation identifies (1.2) with the direct
(m)-window deck (U_A\setminus J).  A full frame has (M) middle
phases; a one-hole or protected frame has (M-1).

An exact-middle packet has two shores indexed by (i=0,1), uses one
frame at each of the same touched roots, and satisfies

\[
 \sum_{A\in\mathcal R(P)}1_{\mathcal D_A^0}
 =\sum_{A\in\mathcal R(P)}1_{\mathcal D_A^1}
 =1_{S(P)}.
\tag{1.3}
\]

The right side is a (0)-(1) vector.  Therefore the decks on either
shore partition (S(P)), and the unique maps (p_P^i) in (0.3) are
defined by

\[
 D\in\mathcal D_{p_P^i(D)}^i.
\tag{1.4}
\]

The next identity is independent of every geometric detail.

### Lemma 1.1 (provider-exposure identity)

For every exact-middle squarefree packet,

\[
 \boxed{
 \mu(P)=
 \sum_{A\in\mathcal R(P)}
   |\mathcal D_A^0\setminus\mathcal D_A^1|
 ={1\over2}\sum_{A\in\mathcal R(P)}
   |\mathcal D_A^0\triangle\mathcal D_A^1|.}
\tag{1.5}
\]

#### Proof

If (p_P^0(D)=p_P^1(D)=A), then (D) belongs to the intersection at
(A) and contributes zero to every difference in (1.5).  If the
provider changes from (A) to (A'), then (D) belongs once to
(mathcal D_A^0\setminusmathcal D_A^1), once to
(mathcal D_{A'}^1\setminusmathcal D_{A'}^0), and nowhere else,
because each shore is squarefree.  Summing over (D) proves both
equalities.  (square)

## 2. Exact active-fringe census

The census uses only two facts shared by the four eligible families.

First, the active placeholders are separated so that no cyclic
(H)-window contains two of them.  A fixed placeholder belongs to
exactly (H) cyclic (H)-windows.  Hence a frame with (d) active
placeholders has exactly (dH) placeholder windows and (r-dH)
retained core-only windows, before accounting for a prescribed common
core hole.

Second, the context-separation lemmas in the source packet theorems say
that no old placeholder window has the same target at the same root as
a new placeholder window.  Therefore the same-root intersection is
exactly the retained common core-only family.

### Proposition 2.1 (three-top and symmetric six-top packets)

For a full two-base conveyor frame,

\[
 |\mathcal D_A^0|=|\mathcal D_A^1|=M,
 \qquad
 |\mathcal D_A^0\cap\mathcal D_A^1|=M-2H.
\tag{2.1}
\]

For the certified protected common-core deletion, both first two terms
decrease by one:

\[
 |\mathcal D_A^0|=|\mathcal D_A^1|=M-1,
 \qquad
 |\mathcal D_A^0\cap\mathcal D_A^1|=M-2H-1.
\tag{2.2}
\]

Consequently the three-top packet moves (6H) providers and the
symmetric six-top packet moves (12H).

#### Proof

The two positional placeholders lie farther than (H) apart.  Thus
exactly (H) middle windows meet the first placeholder, exactly (H)
meet the second, and the two families are disjoint.  Every core-only
window is unchanged by the plus/minus label swap.  Conversely, equality
of an old and a new placeholder target would identify an (A)-context
with a (B)-context.  The two-base construction gives disjoint
radius-(H) context families, so this is impossible.  This proves
(2.1).  The protected deleted phase is common and core-only, proving
(2.2).  Lemma 1.1, multiplied by three or six roots, gives the claimed
provider counts.  (square)

### Proposition 2.2 (four-top moving-hole cube)

At each of the four roots,

\[
 |\mathcal D_A^0|=|\mathcal D_A^1|=M-1,
 \qquad
 |\mathcal D_A^0\cap\mathcal D_A^1|=M-2H-1.
\tag{2.3}
\]

Hence

\[
 |S(T_4)|=4(M-1),\qquad \mu(T_4)=8H.
\tag{2.4}
\]

#### Proof

In the notation of the four-top theorem, the two patterns
(alpha,eta) have identical retained core-only middle-window
families.  The internal (R)-run contributes (|R|-H) windows, and the
possibly reversed (S)-run contributes (|S|-H+1).  Since
(|R|+|S|=M-2), their total is

\[
 (|R|-H)+(|S|-H+1)=M-2H-1.
\tag{2.5}
\]

The different deleted phases remove the two exceptional (R)-windows
and no retained placeholder window.  The long-run neighborhood lemma
excludes equality between an (alpha)- and a (eta)-window meeting
the same placeholder; different placeholders carry different external
labels.  Thus (2.5) is the entire same-root intersection.  There are
(2H) old-only owners per root, and Lemma 1.1 proves (2.4).
(square)

### Proposition 2.3 (eight-top moving-hole cube)

At each of the eight roots,

\[
 |\mathcal D_A^0|=|\mathcal D_A^1|=M-1,
 \qquad
 |\mathcal D_A^0\cap\mathcal D_A^1|=M-3H-1.
\tag{2.6}
\]

Hence

\[
 |S(T_8)|=8(M-1),\qquad \mu(T_8)=24H.
\tag{2.7}
\]

#### Proof

Write the three core-run lengths as (L_1,L_2,L_3), with
(L_1+L_2+L_3=M-3).  After the two exceptional (R_1)-windows are
deleted, the common retained core-only family has size

\[
 (L_1-H)+(L_2-H+1)+(L_3-H+1)=M-3H-1.
\tag{2.8}
\]

The eight-top placeholder-neighborhood separation lemma excludes every
additional same-root coincidence.  Thus there are (3H) old-only
owners per root.  Lemma 1.1 gives (2.7).  (square)

Equations (2.1)--(2.8) prove the table (0.4) and inequality (0.5).

## 3. The six-frame ambiguity and exact eligibility correction

Two different six-root objects occur in the packet library and must not
be conflated.

The symmetric six-top realization in Proposition 2.1 consists of two
three-edge two-base conveyors.  Its shores have identical squarefree
middle support of size (6M), or (6(M-1)) after the certified common
deletion.  It is an eligible exact-owner exchange, but its signed-depth
action is the same (16q) endpoint telescope as for the smaller
three-top packet; it is not a new capacity source.

The older mixed-placeholder six-frame rectangle has, at middle length
(H),

\[
 \|1_{S^1}-1_{S^0}\|_2^2=8H>0.
\tag{3.1}
\]

Thus its changed six-frame shores do not have the same middle incidence
vector.  Its favorable fixed closing collar does not repair this
eligibility defect: the seven old decks have exactly (2H) colliding
pairs and the seven new decks are disjoint.  Therefore it cannot be
switched inside an already exact middle-owner factor.  It is a genuine
collision-repair direction, but not a member of the exact-owner packet
packing studied here.

This distinction is forced by literal ownership, not terminology.

## 4. Exact owner-star overlap and Johnson-edge transport

The provider changes above are not arbitrary long jumps.

### Lemma 4.1 (three-top star intersection)

After relabelling, the three packet roots have the form

\[
 A_x=L\cup\{x\},\qquad A_a=L\cup\{a\},\qquad
 A_y=L\cup\{y\},\qquad |L|=s-1.
\tag{4.1}
\]

For every middle target (D),

\[
 |\{A_x,A_a,A_y\}\cap\{A:A\subset D\}|=
 \begin{cases}
 |D\cap\{x,a,y\}|,&L\subset D,\\
 0,&L\nsubseteq D.
 \end{cases}
\tag{4.2}
\]

For (D\in S(T_3)), the value in (4.2) is one exactly when its
provider is fixed and two exactly when its provider moves.

#### Proof

The first assertion follows by testing (A_z\subset D) separately for
the three labels (z=x,a,y).  On the packet support, the complementary
(H)-window contains zero or one separated placeholder.  These are
respectively the one-compatible-root and two-compatible-root cases.
(square)

### Lemma 4.2 (cube-star intersection)

For a (d)-cube, (d=2,3), write its roots as

\[
 A_\varepsilon=L\cup
 \{a_{r,1-\varepsilon_r}:1\le r\le d\},
 \qquad |L|=s-d.
\tag{4.3}
\]

If (L\nsubseteq D), or if some pair
({a_{r,0},a_{r,1}}) misses (D), no packet root lies in (D).
Otherwise

\[
 |\{A_\varepsilon:A_\varepsilon\subset D\}|=2^{u(D)},
\tag{4.4}
\]

where (u(D)) is the number of coordinate pairs wholly contained in
(D).  For a packet owner, (u(D)=0) precisely in the fixed-provider
case and (u(D)=1) precisely in the moved-provider case.

#### Proof

Once (L\subset D), each coordinate pair must contribute the selected
root label.  A pair meeting (D) once fixes the corresponding bit of
(arepsilon), while a pair wholly contained in (D) leaves two
choices.  This proves (4.4).  A packet owner's complementary
(H)-window contains at most one separated placeholder, so at most one
coordinate pair can be wholly contained in (D).  The zero- and
one-placeholder cases are exactly the fixed and moved cases from the
census.  (square)

### Corollary 4.3 (unit transport)

Every moved provider in every eligible packet travels across one edge of
the Johnson graph on (inom Vs).

#### Proof

Lemmas 4.1 and 4.2 show that a moved owner has exactly two compatible
packet roots.  They differ in one external coordinate choice and hence
have intersection size (s-1).  (square)

This is the promised explicit overlap description: fixed owners see one
packet root, and active owners see exactly the two endpoints of one
packet edge.  There is no hidden multi-root provider jump.

## 5. Bounded-overlap packing and sequential-composition obstruction

Let (mathscr P) be a multiset of eligible packets.  Its middle-owner
support congestion is

\[
 B(\mathscr P)=
 \max_{D\in\binom Vm}
 |\{P\in\mathscr P:D\in S(P)\}|,
\tag{5.1}
\]

where sequential occurrences are counted with multiplicity.  Hence

\[
 \sum_{P\in\mathscr P}|S(P)|\le B(\mathscr P)W.
\tag{5.2}
\]

### Theorem 5.1 (active-fringe transport ceiling)

Suppose a sequence of literal packet switches is compatible with an
exact middle-owner state at every step.  If (p_0,p_1) are its initial
and final provider maps, then

\[
 \boxed{
 \sum_Dd_J(p_0(D),p_1(D))
 \le\sum_{P\in\mathscr P}\mu(P)
 \le {3HB(\mathscr P)\over M-1}W.}
\tag{5.3}
\]

In particular,

\[
 |\{D:p_0(D)\ne p_1(D)\}|
 \le {3HB(\mathscr P)\over M-1}W.
\tag{5.4}
\]

#### Proof

Corollary 4.3 says that each nonfixed owner event has Johnson length
one.  The triangle inequality bounds the final distance of each owner by
the number of its movement events, and summing over owners gives the
first inequality in (5.3).  Inequality (0.5), followed by (5.2), gives
the second.  Every nonzero Johnson distance is at least one, proving
(5.4).  (square)

A literal simultaneous owner-star packet packing has (B=1).  Theorem
5.1 proves (0.6) and therefore refutes a positive-density
provider-changing packing, even under the following three favorable
assumptions:

1. the packet supports cover (W-o(W)) owners;
2. all touched roots admit one mutually compatible old frame; and
3. every required root-owner incidence has perfect MSW provenance.

The obstruction is therefore downstream of the growing-uniformity
matching problem.

There is an equivalent root-congestion form.  If no root is touched
more than (K) times, then every touched root exposes at most (3H)
moving owners, and

\[
 \sum_Dd_J(p_0(D),p_1(D))\le3HKN_H.
\tag{5.5}
\]

At (0.2), the right side is

\[
 (3+o(1)){HK\over M}W.
\tag{5.6}
\]

Thus either owner congestion or root reuse must grow on the scale
(M/H) before positive-density transport is possible.

Finally, one packet moves at most (24H) providers.  Transporting
(arepsilon W) distinct providers requires at least

\[
 {\varepsilon W\over24H}
\tag{5.7}
\]

packet switches.  If the completed braid is to use at most (K_0N_H)
physical components, those components must recycle on average at least

\[
 {\varepsilon\over24K_0}{W\over HN_H}
 =\left({\varepsilon\over24K_0}+o(1)\right){M\over H}
\tag{5.8}
\]

packet switches.  This is a necessary recycling rate, not a claim that
seam costs add independently.

## 6. Rankwise shadow-capacity obstruction

Let (Delta_{P,q}) be the certified untagged load derivative of one
packet at one complementary signed depth (q), (1\le q\le H).  The
source theorems give

\[
\begin{array}{c|c}
P&\|\Delta_{P,q}\|_1\\ \hline
T_3&16q\text{ on its active sign, }0\text{ on the other},\\
T_6^{\rm sym}&16q\text{ on its active sign, }0\text{ on the other},\\
T_4&4\text{ on the lower sign, at most }8\text{ on the upper},\\
T_8&8\text{ on the lower sign, at most }16\text{ on the upper}.
\end{array}
\tag{6.1}
\]

At the terminal upper depth the four- and eight-top values are zero;
the inequalities in (6.1) remain valid.  Comparing (6.1) with the
middle support sizes in (0.4) gives the uniform estimate

\[
 \boxed{
 \|\Delta_{P,q}\|_1
 \le {16q\over3(M-1)}|S(P)|.}
\tag{6.2}
\]

### Theorem 6.1 (one-row action and hole ceiling)

For any compatible packet composition of owner congestion (B), and
for either certified signed depth,

\[
 \boxed{
 \|\mu_q^{\rm final}-\mu_q^{\rm initial}\|_1
 \le {16qB\over3(M-1)}W.}
\tag{6.3}
\]

If

\[
 h_q(\mu)=|\{T:\mu_q(T)=0\}|
\tag{6.4}
\]

is the number of uncovered targets at that rank, then

\[
 \boxed{
 h_q(\mu^{\rm final})
 \ge h_q(\mu^{\rm initial})
      -{8qB\over3(M-1)}W.}
\tag{6.5}
\]

#### Proof

The triangle inequality, (6.2), and (5.2) prove (6.3).  Every packet
preserves total target mass at the fixed rank.  Therefore the positive
variation of the final-minus-initial load vector equals half its
(\ell^1)-norm.  Filling one old hole requires at least one unit of
positive variation, proving (6.5).  (square)

For bounded (B), the right sides of (6.3)--(6.5) are (o(W))
uniformly for (q\le H=o(M)).  Repairing (arepsilon W) holes at
depth (q) requires

\[
 B\ge {3\varepsilon(M-1)\over8q}.
\tag{6.6}
\]

Thus depth one requires linear-in-(m) overlap, and even depth (H)
requires overlap (Omega(M/H)).  This conclusion is independent of
floor-energy orientation: choosing every packet in its favorable shore
cannot create more positive variation than (6.3).

The moving-hole cubes admit a stronger all-depth statement.  Their exact
two-sided action totals are

\[
 \sum_{q,\pm}\|\Delta_{T_4,q}^{\pm}\|_1=12H-8,
 \qquad
 \sum_{q,\pm}\|\Delta_{T_8,q}^{\pm}\|_1=24H-16.
\tag{6.7}
\]

Since their middle support sizes are (4(M-1)) and (8(M-1)), both
ratios equal

\[
 {3H-2\over M-1}.
\tag{6.8}
\]

Hence any (B)-congested mixture of four- and eight-top cubes has total
all-depth action at most

\[
 {B(3H-2)\over M-1}W.
\tag{6.9}
\]

For bounded (B), this is (o(W)).  The corresponding aggregate bound
does not close the three-top conveyor, whose (16q) actions sum to
(Theta(H^2)) per packet.  Its provider transport is nevertheless
closed by Theorem 5.1.  This distinction prevents an invalid
all-depth extrapolation.

## 7. Fractional capacity versus integral packing

The obstruction is not a fractional quota shortage.  Let one packet
orbit under all coordinate relabellings have (t) roots and (k)
middle owners per packet.  By transitivity, uniform orbit weights with
total packet weight (Z) give root load (tZ/N_H) and owner load
(kZ/W).  The maximum simultaneous fractional owner mass is therefore

\[
 k\min\left\{{N_H\over t},{W\over k}\right\}
 =W\min\left\{1,{kN_H\over tW}\right\}.
\tag{7.1}
\]

For the full three- and six-top packets, (k/t=M); for every protected
or moving-hole packet, (k/t=M-1).  Thus (0.2) makes (7.1)
((1-o(1))W).  Fractional root and owner capacities are compatible with
nearly full coverage.

An integral owner-disjoint refinement is a growing-uniformity matching
problem: its hyperedges contain (Theta(M)) owners.  The exact labelled
orbit has small pair codegrees, but the existing repaired-ring analysis
does not justify importing a fixed-uniformity nibble theorem at this
rank.  No integral positive-density packing is claimed here.

This remaining matching gate does not weaken the provider result.  Even
granting an integral realization of the fractional point in (7.1), its
provider-changing mass is at most the (o(W)) quantity in (0.6).

## 8. Directed endpoint split

The provider obstruction must not be misreported as an endpoint
obstruction.

For the three-top and symmetric six-top packets, every core-only
(H)-window appears at the same root, with the same positional terminal
endpoint, on both shores.  Hence only the (2H) placeholder windows per
root can change their directed phase.

For the four-top packet, write the core-run lengths as
(ho=|R|) and (sigma=|S|).  The (sigma-H+1) internal
(H)-windows of (S) have the same unordered window set in
(alpha) and (eta), but the run is reversed.  Their directed
terminal endpoint therefore reverses while their provider root remains
fixed.  Taking (ho=2H) gives

\[
 \sigma-H+1=M-3H-1=(1-o(1))M.
\tag{8.1}
\]

For the eight-top packet, the two reversed runs contribute exactly

\[
 (L_2-H+1)+(L_3-H+1)
\tag{8.2}
\]

same-provider directed reversals per root.  Taking (L_1=2H) makes
(8.2)

\[
 M-4H-1=(1-o(1))M.
\tag{8.3}
\]

These are genuine positive-density abstract directed-phase changes.
They preserve the target (D), the provider (A), and the unordered
(H)-window.  In particular, they disappear after quotienting by the
already-closed unphased/load-neutral fixed-core reversal corridor.  The
only nonneutral/provider-changing image of the packet is the
(O(H))-window active fringe counted in Section 2.

There are two unresolved interfaces before (8.1)--(8.3) can become an
MSW braid:

1. an integral owner- and root-compatible repaired-ring packing of the
   four/eight-top packets; and
2. a simultaneous MSW provenance theorem realizing the prescribed long
   (alpha/\beta) frame orders and their nested phase chronology.

The exact MSW owner-star lift is incidencewise: it certifies one witness
frame for each pair (A\subset D).  It does not assert that all phases
required at one root share the prescribed moving-hole frame, nor that
the several roots of a packet occur simultaneously.  The source
four/eight-top theorems likewise prove unrestricted physical-frame
identities, not preservation of the fixed MSW/PBBS mechanical support or
of an arbitrary externally assigned tag schedule.

Therefore the dense endpoint reversal is a precisely isolated surviving
route, not a proved positive-density MSW owner-star packing.

## 9. MSW fibre consequence

Let (kappa(D)) be any fixed MSW component label of a middle owner, and
let (b(A)) be any label of a promotion root.  Define the joint fibre
histogram

\[
 H_i(\gamma,\beta)
 =|\{D:\kappa(D)=\gamma, b(p_i(D))=\beta\}|.
\tag{9.1}
\]

Changing one provider moves one unit from one histogram cell to another.
Theorem 5.1 therefore gives

\[
 \|H_1-H_0\|_1
 \le {6HB\over M-1}W.
\tag{9.2}
\]

Likewise, for any desired root/component alignment predicate
(G(D,A)\in\{0,1\}),

\[
 \left|
 \sum_DG(D,p_1(D))-
 \sum_DG(D,p_0(D))
 \right|
 \le {3HB\over M-1}W.
\tag{9.3}
\]

Thus a bounded-overlap packet bank cannot correct an
(Omega(W)) MSW component/provider mismatch, regardless of how its
shore bits are correlated.  This is a statewise obstruction beyond
component colouring: it applies to every dependent selection and to the
entire provider histogram.

## 10. Audited implication boundary

The following statements are proved.

1. The exact provider-motion counts in (0.4) hold for every labelled
   instance of the eligible packet templates.
2. Every moved provider is one Johnson edge.
3. Every owner-disjoint packing changes only (o(W)) providers and only
   (o(W)) targets at each certified depth.
4. Any positive-density provider transport requires owner or root
   overlap (Omega(M/H)); at the promotion scale this is
   (Omega(\sqrt{m/\log m})).
5. Every bounded-overlap four/eight-top bank has aggregate all-depth
   unphased action (o(W)).
6. The mixed-placeholder six-frame rectangle is ineligible for an exact
   middle-owner switch.

The following statements are not proved and are not implied.

1. No claim is made that a positive-density integral packet-support
   packing exists; only its fractional margins are compatible.
2. No obstruction is claimed for dense directed endpoint reversal in
   the four/eight-top packets.
3. No fixed-MSW mechanical embedding or arbitrary nested-tag theorem is
   claimed for those reversals.
4. No obstruction is claimed against a moving-core, high-congestion
   serial braid, a recyclable catalyst, or a new growing packet whose
   number of exposed placeholders is (Theta(M)).
5. No coefficient-one conclusion follows from this report.

The exact conclusion for the requested lane is therefore:

\[
 \boxed{
 \begin{gathered}
 \text{bounded-overlap squarefree moving-hole packing}\
 \text{cannot transport a positive density of MSW providers}\
 \text{and cannot repair a positive-density unphased shadow defect;}\\
 \text{the only surviving effect is a directed same-provider reversal}\
 \text{whose integral packing and MSW provenance remain open.}
 \end{gathered}}
\tag{10.1}
\]

## Source dependencies

The packet identities used above are the audited results in:

- `MATH_THEOREM_THREE_TOP_TWO_BASE_PROMOTION_CONVEYOR_20260726.md`;
- `MATH_THEOREM_SIX_TOP_TWO_BASE_CONVEYOR_FLOOR_DESCENT_20260726.md`;
- `MATH_THEOREM_PROMOTION_FOUR_TOP_SQUAREFREE_MOVING_HOLE_CUBE_20260726.md`;
- `MATH_THEOREM_PROMOTION_EIGHT_TOP_SQUAREFREE_MOVING_HOLE_EXCHANGE_20260726.md`; and
- `MATH_THEOREM_SIX_FRAME_MIXED_PLACEHOLDER_RECTANGLE_AND_MINIMALITY_20260726.md`.

The MSW interface and calibration are as in
`MATH_THEOREM_K_MSW_OWNER_STAR_GLOBAL_EXCHANGE_BRAID_OBSTRUCTION_20260726.md`
and its independent audit.
