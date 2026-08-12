# Movable-frontier matching, strict-gammoid carry, and two-layer fusion

**Date:** 2026-08-02  
**Status:** unconditional static-payload theorems.  One movable chronology
block is integral; all suffix alternatives propagate exactly as a
dual-transversal carry matroid; and a clean two-block window is also an
ordinary bipartite matching.  No all-\(k\) \(d(k)+O(1)\) chronology or
literal contiguous-OR word is proved.

## 0. Outcome

Section 5 of
`MATH_THEOREM_K17_BOTTOM_TOKEN_PERFECT_MATCHING_AND_COMPOUND_RELAY_CIRCUITS_20260802.md`
is correct on its stated equal-cardinality payload face.  The form needed
for all-\(k\) chainization is slightly more general: \(b\) movable targets
face \(h\) optional frozen suffixes and \(f\) mandatory receivers.  Adding

\[
                              d=f+h-b                              \tag{0.1}
\]

dummies gives one square bipartite perfect matching.  Its exact Hall test
still consists of two explicit families.

For an ordinary \(W\)-chain chronology block, \(f=0\), \(h=W\), and
\(d=W-b\).  The unmatched suffix minima are not arbitrary bookkeeping:
they are precisely a base of the dual of a receiver transversal matroid,
hence of a strict gammoid.  This yields two exact conclusions.

1. With one realized suffix table fixed, a chronology can be built downward
   one block at a time with no rounding loss.  The only local test is
   ordinary bipartite Hall.
2. If all feasible suffix tables are retained, their possible exposed
   minima form one carry matroid.  Prepending the next block is exactly a
   matroid-intersection test
   \[
       r_C(X)+r_K(E\setminus X)\ge |P_t|\qquad(X\subseteq E).   \tag{0.2}
   \]

Thus there is no genuinely nonintegral multi-level payload gate for a
**fixed** chronology: its global successor polytope is bipartite-integral
at every depth.  The unresolved all-\(k\) difficulty is selecting a
capacity-\(d+O(1)\) chronology, or compressing the propagated carry rank
function, while preserving all future Hall cuts.  Literal state/history,
upper, topology, residence, and compiler rows remain separate possible
sources of nonintegrality.

## 1. Scope needed by the movable-bottom theorem

Before moving any target, assume:

1. every optional suffix is a fixed strict chain, and different suffixes
   use disjoint named targets;
2. every mandatory receiver has a fixed maximum, disjoint from all suffix
   and movable targets;
3. receiver labels and capacity one are fixed; and
4. compatibility of a movable target with a receiver is a fixed edge
   predicate, here strict containment in the first suffix target or receiver
   maximum.

These conditions are present in the K17 table surrounding the cited
Section 5, but they are necessary when exporting the lemma.  Adding state,
history, or a choice-dependent compatibility row leaves the pure matching
face and is not covered.

## 2. Rectangular movable-frontier theorem

Let \({\cal B}\) be \(b\) distinct named movable targets.  Let \({\cal F}\)
be \(f\) receivers which must each receive one target, and let \({\cal H}\)
be \(h\) optional frozen suffix slots.  Assume

\[
                         f\le b\le f+h,                         \tag{2.1}
\]

and put \(d=f+h-b\).  A real target \(B\) has fixed neighbour sets
\(N_F(B)\subseteq{\cal F}\) and \(N_H(B)\subseteq{\cal H}\), determined by
strict containment.

Create a bipartite graph with shores

\[
       {\cal B}\mathbin{\dot\cup}{\cal D}_d
       \quad\hbox{and}\quad
       {\cal F}\mathbin{\dot\cup}{\cal H},                    \tag{2.2}
\]

where every dummy is adjacent to every optional slot and to no mandatory
receiver.

### Theorem 2.1 (rectangular movable-frontier integrality)

Perfect matchings of (2.2), modulo dummy labels, are in bijection with
exact placements which use every movable target once, fill every mandatory
receiver, use an optional slot at most once, and leave exactly \(d\)
optional slots bottomless.  The placement polytope is integral.

It is nonempty if and only if, for every \(X\subseteq{\cal B}\),

\[
\boxed{
\begin{aligned}
 |N_F(X)|+|N_H(X)|&\ge |X|,\\
 |N_F(X)|&\ge |X|-(b-f).
\end{aligned}}                                               \tag{2.3}
\]

#### Proof

A perfect matching assigns each real target once.  No dummy can fill a
mandatory receiver, so all \(f\) of those receivers receive real targets.
The \(d\) dummy-matched optional slots are exactly the bottomless suffixes.
Conversely every valid placement has exactly \(d\) bottomless optional
slots; match them bijectively to the dummies.  This proves the bijection.
Bipartite perfect-matching integrality gives the polyhedral statement.

For Hall, a left subset containing no dummy gives the first family in
(2.3).  If it contains \(t>0\) dummies, its neighbourhood contains all
\(h\) optional slots and the free neighbours \(N_F(X)\).  The strongest
choice is \(t=d\), giving

\[
 h+|N_F(X)|\ge |X|+d
 \Longleftrightarrow
 |N_F(X)|\ge |X|-(b-f).
\]

These exhaust all left subsets. \(\square\)

The cited Section 5 is the specialization \(h=b=n\), \(d=f\).  For a
chronology block against \(W\) owner-suffix chains, the natural
specialization is instead

\[
                 f=0,\qquad h=W,\qquad d=W-b.                 \tag{2.4}
\]

Then the second row of (2.3) is automatic and the first row is ordinary
Hall from the current block into the exposed suffix minima.

## 3. Exact one-block Markov factorization

Fix a chronology

\[
                    {\cal T}=P_0\dot\cup\cdots\dot\cup P_{q-1},
                    \qquad |P_t|\le W,                         \tag{3.1}
\]

and let \({\cal O}\) be the \(W\) owners.  Process the blocks from late to
early.  Put \(S_q={\cal O}\).  If \(S_{t+1}\) is the set of \(W\) exposed
minima of already frozen later suffix chains, choose an inclusion matching

\[
                         \mu_t:P_t\hookrightarrow S_{t+1}.     \tag{3.2}
\]

Let

\[
 D_t=S_{t+1}\setminus\mu_t(P_t),\qquad
 S_t=P_t\mathbin{\dot\cup}D_t.                                \tag{3.3}
\]

Again \(|S_t|=W\).

### Theorem 3.1 (static one-block freezing is exact)

The fixed chronology has an owner-anchored chain factor if and only if
there is a sequence (3.2)--(3.3).  Once \(\mu_t\) is selected, every later
suffix row may be frozen permanently: all still lower targets see only the
new exposed-minimum set \(S_t\), not the physical identity of the suffix
row below which each member of \(P_t\) was placed.

For a fixed state \(S_{t+1}\), the possible carry sets \(D_t\) are exactly
the bases of the dual of the receiver transversal matroid on
\(S_{t+1}\) induced by the neighbourhoods of \(P_t\).

#### Proof

Theorem 2.1 with (2.4) gives the matching and says that its unmatched
receivers are exactly \(D_t\).  Attaching each member of \(P_t\) below its
matched suffix creates disjoint chains, and (3.3) lists their new minima.
Iteration gives a full factor.

Conversely, restrict any anchored chain factor to the blocks later than
\(t\).  Every member of \(P_t\) has a unique next member of its chain among
the exposed later suffixes, giving (3.2), while chains receiving no member
of \(P_t\) give \(D_t\).

For the matroid statement, let \(M_t\) be the transversal matroid on
\(S_{t+1}\): a receiver set is independent when it can be matched to
distinct members of \(P_t\).  The occupied receiver sets in a saturating
matching are the bases of \(M_t\); their complements are exactly the bases
of \(M_t^*\). \(\square\)

With mandatory receivers \(F\), feasible occupied sets are the bases of
the receiver transversal matroid containing \(F\), and the optional carry
sets are the bases of

\[
                             (M_t/F)^*.                         \tag{3.4}
\]

The dual of a transversal matroid is a strict gammoid.  Thus the exact
one-step carried reserve is a gammoid base, not merely its cardinality.

## 4. Propagating all suffix alternatives

The previous section fixes one realized suffix state.  There is also an
exact aggregate recurrence which retains every feasible suffix table.

Let \(G_{t+1}\) be the successor graph induced by the later blocks
\(P_{t+1},\ldots,P_{q-1}\) and the owners.  Its left shore consists of the
later targets and its right shore is

\[
                         E_{t+1}=
       P_{t+1}\dot\cup\cdots\dot\cup P_{q-1}\dot\cup{\cal O}.
                                                                    \tag{4.1}
\]

Assume the later left shore is saturable.  Let \(T_{t+1}\) be the
transversal matroid on \(E_{t+1}\) induced by that left shore and put

\[
                         C_{t+1}=T_{t+1}^*.                       \tag{4.2}
\]

Its rank is \(W\), and its bases are exactly the exposed-minimum sets of
all feasible suffix chain factors.

Let \(K_t\) be the transversal matroid on the same ground \(E_{t+1}\)
induced by the current block \(P_t\).

### Theorem 4.1 (one-block strict-gammoid expansion)

The current block can be prepended to some feasible later suffix factor if
and only if

\[
                         r_{K_t}(E_{t+1})=|P_t|                  \tag{4.3}
\]

and

\[
 \boxed{
 r_{C_{t+1}}(X)+r_{K_t}(E_{t+1}\setminus X)
       \ge |P_t|\qquad(X\subseteq E_{t+1}).}                    \tag{4.4}
\]

When these conditions hold, the expanded suffix again has a rank-\(W\)
dual-transversal carry matroid \(C_t\).  Starting from the free rank-\(W\)
matroid on the owner set and repeating (4.3)--(4.4) is an exact integral
recurrence for the whole fixed chronology.

#### Proof

A suffix exposed set \(S\) is a base of \(C_{t+1}\).  The current block
can attach to it exactly when \(S\) spans \(K_t\), equivalently when it
contains a \(K_t\)-basis \(J\) of size \(|P_t|\).  Such an \(S\) exists if
and only if \(C_{t+1}\) and \(K_t\) have a common independent set \(J\) of
size \(|P_t|\): a common set extends to a base of \(C_{t+1}\), while a
spanning base contains a \(K_t\)-basis.

The matroid-intersection min--max theorem says that the largest common
independent set has size

\[
 \min_{X\subseteq E_{t+1}}
 \bigl(r_{C_{t+1}}(X)+r_{K_t}(E_{t+1}\setminus X)\bigr),
\]

which proves (4.4), subject to the full-rank condition (4.3).  Choose a
suffix matching whose unmatched set is the resulting \(C_{t+1}\)-base and
attach \(P_t\) to the common \(K_t\)-basis.  The expanded successor graph
is bipartite and saturable.  The complement of every used right shore in
an expanded matching is, by the same transversal-duality argument, a base
of its new carry matroid \(C_t\). \(\square\)

### Corollary 4.2 (no fixed-chronology payload nonintegrality)

At every number of movable blocks, the static payload face of a fixed
chronology is an ordinary left-saturating bipartite matching polytope and
is integral.  The recurrence above is a primal factorization of the same
global matching theorem; chronological-upset expansion is its dual Hall
form.

Thus “the first genuinely nonintegral movable depth” does not exist on the
fixed-chronology payload face.  Nonintegrality can enter only after the
chronology/configuration itself is selected jointly, after one projects to
an insufficient multistage summary, or after literal state/history, upper,
topology, residence, or compiler constraints are imposed.

## 5. One-step lookahead and the greedy-freeze warning

Theorem 4.1 has a useful fixed-suffix specialization.  Suppose a current
movable-bottom matching has optional-slot carry matroid \(N\) on ground
\(H\).  Let the next lower block be \({\cal A}\), and let \(M_A\) be its
receiver transversal matroid on the always exposed current targets
\({\cal B}\) together with \(H\).  Assume

\[
                         r_{M_A}({\cal B}\cup H)=|{\cal A}|.     \tag{5.1}
\]

Put

\[
                         K=M_A/{\cal B}.                         \tag{5.2}
\]

A carry \(D\in{\cal B}(N)\) permits placement of \({\cal A}\) exactly
when it spans \(K\).  Consequently a future-viable carry exists if and only
if

\[
 r_N(X)+r_K(H\setminus X)\ge r(K)\qquad(X\subseteq H).        \tag{5.3}
\]

This closes one lookahead transition integrally.  It does not justify a
greedy first matching which forgets the chosen carry.

Indeed,

\[
 r_K(D)=r_{M_A}({\cal B}\cup D)-r_{M_A}({\cal B}).    \tag{5.4}
\]

Under (5.1), placement of all of \({\cal A}\) is equivalent to
\(r_{M_A}({\cal B}\cup D)=|{\cal A}|\), hence to \(D\) spanning \(K\).
If an \(N\)-base \(D\) spans \(K\), it contains a \(K\)-basis which is
independent in both matroids.  Conversely, any common independent set of
size \(r(K)\) is a \(K\)-basis and extends to an \(N\)-base which spans
\(K\).  The matroid-intersection min--max theorem is exactly (5.3).

### Theorem 5.1 (whole-prefix-preserving freeze)

The same test can protect the entire earlier prefix, not only the next
block.  Return to the general current frontier
\({\cal F}\dot\cup H\).  Let \(M_B\) be its receiver transversal matroid.
Under Theorem 2.1, \({\cal F}\) is independent, \(r(M_B)=b\), and the
occupied optional receiver sets are exactly the bases of

\[
                             L=M_B/{\cal F}                     \tag{5.5}
\]

on \(H\).  Thus if \(J\in{\cal B}(L)\) is occupied, the carried optional
set is \(D=H\setminus J\).

Let \({\cal A}\) now denote **all** still earlier targets with their fixed
internal chronology.  Form their successor transversal matroid \(Q_A\) on
the receiver ground

\[
                {\cal A}^{+}\mathbin{\dot\cup}
                \widehat{\cal B}\mathbin{\dot\cup}H,           \tag{5.6}
\]

where \({\cal A}^{+}\) are the internal right copies of earlier targets
and \(\widehat{\cal B}\) are the always exposed right copies of the current
movable targets.  Assume

\[
 r_{Q_A}({\cal A}^{+}\cup\widehat{\cal B}\cup H)=|{\cal A}|.   \tag{5.7}
\]

Contract the always available receiver ground and put

\[
 K=Q_A/({\cal A}^{+}\cup\widehat{\cal B})                       \tag{5.8}
\]

on \(H\).  A current placement with occupied optional set \(J\) preserves
completion of the whole earlier prefix if and only if

\[
       J\in{\cal B}(L),\qquad J\text{ is independent in }K^*.  \tag{5.9}
\]

Such a placement exists if and only if

\[
 r_L(X)+r_{K^*}(H\setminus X)\ge r(L)
                    \qquad(X\subseteq H).                      \tag{5.10}
\]

#### Proof

After the current placement, the external receivers visible to the earlier
prefix are exactly \(\widehat{\cal B}\cup D\).  The contraction rank
identity gives

\[
 r_K(D)=
 r_{Q_A}({\cal A}^{+}\cup\widehat{\cal B}\cup D)
 -r_{Q_A}({\cal A}^{+}\cup\widehat{\cal B}).
\]

Under (5.7), the earlier prefix is completable exactly when \(D\) spans
\(K\).  In any matroid, \(D\) spans \(K\) if and only if its complement
\(J=H\setminus D\) is independent in \(K^*\).  Current feasibility says
exactly that \(J\) is a base of \(L\).  Hence a protected placement is a
common independent set of \(L,K^*\) of size \(r(L)\), and the
matroid-intersection theorem gives (5.10). \(\square\)

Theorem 5.1 is an exact no-dead-end rule: with the whole earlier chronology
already fixed, one may choose the current matching, freeze it, and retain a
completion of every earlier level.  Its rank oracle contains the full
earlier successor problem; it is not a bounded-state all-\(k\) estimate.

### Example 5.2 (two first-step matchings, only one viable carry)

On ground \([5]\), take movable targets

\[
 b_1=\{1,2\},\qquad b_2=\{1,3\},
\]

one mandatory receiver \(r=\{1,2,3\}\), and optional suffix minima

\[
 m_1=\{1,2,4\},\qquad m_2=\{1,3,5\}.
\]

The legal real edges are

\[
 b_1r,\ b_1m_1,\ b_2r,\ b_2m_2.
\]

With one dummy, both

\[
 \{b_1r,b_2m_2,um_1\},
 \qquad
 \{b_2r,b_1m_1,um_2\}                                \tag{5.11}
\]

are perfect matchings.  The first carries \(m_1\); the next target
\(a=\{5\}\) is contained in none of
\(b_1,b_2,m_1\), so the recurrence dies.  The second carries \(m_2\), and
\(a\subset m_2\), so it continues.

Here \(N\) has bases \(\{m_1\},\{m_2\}\), while \(K\) has rank one and
\(m_2\) is its only nonloop.  Inequality (5.3) selects exactly the viable
carry.  Local Hall and carry cardinality alone cannot distinguish the two
first-step matchings.

### Example 5.3 (even the complete balanced type profile is not Markov)

On ground \([6]\), fix core \(\{1,2\}\) and the two suffixes

\[
                 123\subset1235,\qquad124\subset1246.          \tag{5.12}
\]

Their exposed minima have the same balanced type \((2,1)\), owner
coordinate \(p=2\), and owner interval \([2,2]\).  Let the current block
be \({\cal B}=\{12\}\), the earlier block be \({\cal A}=\{3\}\), and take
no mandatory receiver.  The current token may occupy either suffix, so
both singleton carries are bases of the same carry matroid.  But carrying
\(123\) permits the earlier placement \(3\subset123\), whereas carrying
\(124\) does not.

Thus the two realized frontiers have identical type-count vectors, owner
palettes, owner intervals, and scalar reserve, yet only one is viable.
The missing state is occurrence/address aware; no theorem based only on
the balanced type profile can justify greedy freezing.

## 6. Two movable layers are still a matching

For completeness, let \({\cal B}\) and \({\cal M}\) be ordered movable
layers of sizes \(b,m\), and let \({\cal S}\) be \(s\) fixed suffix slots,
where

\[
                         \max(b,m)\le s\le b+m.                  \tag{6.1}
\]

Require every slot to receive exactly one of

\[
 (B,M,T_v),\qquad(B,T_v),\qquad(M,T_v).                         \tag{6.2}
\]

Put \(g=s-b\).  Make a bipartite graph with shores

\[
 {\cal B}\dot\cup{\cal M}^{\rm out}\dot\cup{\cal D}_g,
 \qquad
 {\cal M}^{\rm in}\dot\cup{\cal S},                           \tag{6.3}
\]

using edges \(B M^{\rm in}\) for \(B\subsetneq M\), edges from \(B\) or
\(M^{\rm out}\) to compatible suffix slots, and every dummy edge to every
\(M^{\rm in}\).

### Theorem 6.1 (two-layer augmented matching)

Perfect matchings of (6.3), modulo dummy labels, are in bijection with the
tables (6.2).  Their forced histogram is

\[
 \#(B<M)=b+m-s,\qquad
 \#(B\text{-only})=s-m,\qquad
 \#(M\text{-only})=s-b.                              \tag{6.4}
\]

For \(X\subseteq{\cal B}\), \(Y\subseteq{\cal M}\), let \(N_M(X)\) be
the compatible middle receivers and let \(N_S(X,Y)\) be the union of
suffix slots compatible with a member of \(X\) or \(Y\).  Exact Hall is

\[
\boxed{
\begin{aligned}
 |N_M(X)|+|N_S(X,Y)|&\ge |X|+|Y|,\\
 |N_S(X,Y)|&\ge |X|+|Y|+s-b-m.
\end{aligned}}                                               \tag{6.5}
\]

#### Proof

A matched edge \(B M^{\rm in}\), together with the unique edge from
\(M^{\rm out}\) to a suffix, produces the first row type in (6.2).
A dummy at \(M^{\rm in}\) produces an \(M\)-only row, and a direct
\(B\)-suffix edge produces a \(B\)-only row.  Counting the three types
gives (6.4), and the converse is immediate.

A dummy-free left subset gives the first line of (6.5).  Any subset with a
dummy sees all \(m\) middle receiver copies; taking all \(g=s-b\) dummies
is strongest and gives the second line.  These exhaust Hall. \(\square\)

If untouched suffix slots are permitted, use the corresponding
left-saturating graph without forcing dummy coverage; this remains
bipartite-integral.

## 7. Relation to interval reserve carry

The earlier balanced-core theorem gives the exact dual criterion

\[
                         E_\tau(J)\le\operatorname {cap}(J)     \tag{7.1}
\]

for every owner interval \(J\).  The present theorem supplies its primal
state interpretation:

- a realized reserve is an exposed-minimum/gammoid base;
- one transition is a transversal matching;
- all suffix alternatives are encoded by the carry rank function; and
- the next transition is the matroid-intersection inequality (4.4).

This does permit all but the current block to be frozen when the **full**
exposed-minimum state is retained.  It does not show that the scalar debt
\(\sum(\varepsilon_t-\rho_t)\), a free-slot count, or an \(O(1)\)-endpoint
palette determines a future-viable base.  Examples 5.2--5.3 refute
count-only and balanced-type greedy freezing, and the previous top-rank
component theorem already rules out a literal \(O(1)\)-component palette
state.

The exact remaining all-\(k\) statement is therefore:

> choose at most \(d(k)+C\) balanced-core blocks so that the propagated
> dual-transversal carry matroid retains rank \(W\) through every expansion,
> equivalently so that every interval profile (7.1) passes.

No theorem here constructs those blocks.  Static chainization would still
leave literal overlap serialization, endpoint aperture, address/history,
residence, upper/common-cap, compiler, and regenerative pull-cell closure
unproved.
