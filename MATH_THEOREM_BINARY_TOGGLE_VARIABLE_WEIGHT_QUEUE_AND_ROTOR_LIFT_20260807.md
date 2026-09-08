# Every positive age rotor has an owner-simple binary-toggle queue lift

**Date:** 2026-08-07  
**Method:** variable phase weights with a common two-state omission clock  
**Status:** unconditional local theorem and partial rotor lift.  Every
cyclic positive age composition admits a literal cycle with distinct flat
owners, simple local immediate palettes, exact rank profile, and two-sided
owner residence.  This directly lifts the short and ordinary long rotors.
It does not directly lift a mixed rotor with a fixed appended singleton
rail; that audited gap is repaired by the separate delayed multistate queue
theorem cited below.  None of these results selects each global owner or
named target once, joins the cycles, or proves the upper/compiler rows.

## 1. Variable weights with one common binary clock

Fix an owner rank \(R\), a trace depth \(d\ge1\), and put

\[
 p=d+1.
\tag{1.1}
\]

Let

\[
 \mathbf h=(h_0,h_1,\ldots,h_{p-1}),\qquad h_a\ge1,
 \qquad H=\sum_{a=0}^{p-1}h_a\le R.
\tag{1.2}
\]

Assume the ambient ground set has at least \(R+p\) coordinates.  Choose
pairwise disjoint sets

\[
 K,\quad P_a,\quad \{x_a^0,x_a^1\}\quad(0\le a<p)
\tag{1.3}
\]

with

\[
 |K|=R-H,\qquad |P_a|=h_a-1.
\tag{1.4}
\]

Exactly \(R+p\) coordinates are used.  For

\[
 i=up+a,\qquad 0\le a<p,\quad u\in\mathbb Z_2,
\]

define the cyclic source word of length \(2p\) by

\[
 \boxed{
 A_{up+a}=K\cup P_a\cup\{x_a^u\}.}
\tag{1.5}

Thus every phase has arbitrary positive weight, but all phases use the
same binary omission clock.  This common clock is the feature missing from
the naive unequal-support rotor, whose Chinese-remainder returns can repeat
owners.

## 2. Exact queue theorem

For an endpoint \(i=up+a\), let

\[
 Z_{i,j}=A_{i-j+1}\cup\cdots\cup A_i.
\tag{2.1}

### Theorem 2.1 (binary-toggle variable-weight queue)

The word (1.5) has all of the following properties.

1. Every \(p\)-letter owner has rank \(R\).
2. The \(2p\) owners are distinct and form a simple Johnson cycle.
3. The immediate lower and upper colours of the owner cycle are each
   simple within the component.
4. Every toggle coordinate has an owner run of exactly \(p\) and an owner
   gap of exactly \(p\); all core and \(P_a\)-coordinates are permanent
   whenever their phase is present in the owner, which here is always.
5. Every proper suffix rank is

   \[
   \boxed{
   |Z_{up+a,j}|=R-H+\sum_{v=0}^{j-1}h_{a-v}
   \qquad(1\le j\le p),}
   \tag{2.2}
   \]

   with phase indices cyclic.  In particular the value at \(j=p\) is
   \(R\).
6. All proper suffix targets in the entire \(2p\)-cycle are distinct,
   even when different depths happen to have the same numerical rank.
7. At endpoint \(up+a\), the age composition of its owner is

   \[
   \boxed{
   c(up+a)=
   (R-H+h_a,h_{a-1},h_{a-2},\ldots,h_{a-d}).}
   \tag{2.3}
   \]

8. After \(2p\) positions the full literal state returns.

#### Proof

A \(p\)-window contains one letter from every phase.  It contains \(K\),
all the \(P_a\), and exactly one of \(x_a^0,x_a^1\) for every phase.
Its rank is

\[
 (R-H)+\sum_a(h_a-1)+p=R.
\]

Moving one step updates exactly one phase and replaces \(x_a^0\) by
\(x_a^1\), or conversely.  Consecutive owners are therefore Johnson
neighbours.

At endpoint \(up+a\), the selected toggle bit in phase \(b\) is

\[
 \epsilon_b=
 \begin{cases}
 u,&b\le a,\\
 1-u,&b>a.
 \end{cases}
\tag{2.4}
\]

The \(2p\) vectors in (2.4) are the two constant vectors and the two
orientations of every nontrivial one-cut binary vector.  They are pairwise
distinct.  Since the phase supports are disjoint, the owner set recovers
this vector, proving owner simplicity.

An owner edge identifies its updated phase: its lower colour omits both
toggle points of that phase, while its upper colour contains both.  The
unchanged phase toggles recover the cut vector (2.4).  Hence neither the
lower nor upper immediate colour repeats.

One toggle choice persists between two successive updates of its phase,
namely for \(p\) owner steps, and then the other choice persists for the
next \(p\).  This proves Item 4.

A proper \(j\)-suffix meets precisely the cyclic phase interval
\(a-j+1,\ldots,a\), proving (2.2).  Its target set recovers that proper
phase interval from the disjoint supports, hence recovers \(a\) and \(j\).
The selected toggles then recover \(u\).  This proves Item 6.

The core \(K\) occurs at the current position and therefore has age zero.
The current phase contributes \(h_a\) further age-zero coordinates; each
preceding phase contributes its \(h_{a-v}\) coordinates at age \(v\).
This is (2.3).  Finally the cut phase and the common binary clock both
return after \(2p\) positions. \(\square\)

## 3. Exact lift of the monotone rotors

Let \(\mathcal M_{R,d}\) be the monotone marked-rank polytope from
`MATH_THEOREM_MONOTONE_ROTOR_FRACTIONAL_TRACE_CIRCULATION_20260801.md`:

\[
 \mathcal M_{R,d}=
 \left\{q:0\le q_1\le\cdots\le q_{R-1}\le1,
              \ \sum_s q_s\le d\right\}.
\tag{3.1}
\]

That theorem realizes its vertices by three clocks: the short singleton
clock, positive-composition long rotors, and long rotors with an appended
singleton rail.

### Theorem 3.1 (owner-simple realization of the nonmixed rotor vertices)

The zero, short, and ordinary long rotors used in the proof of
\(\mathcal M_{R,d}\subseteq\mathsf{ST}_{k,R,d}\) are rank projections
of binary-toggle variable-weight queues.

More precisely:

* the short clock \((R-d,1,\ldots,1)\) is obtained from
  \(h_0=\cdots=h_d=1\) and \(|K|=R-d-1\);
* a long rotor with permanent core \(R-b-1\) and positive mobile
  composition \((a_0,\ldots,a_d)\) is obtained by taking
  \(h_i=a_i\) and \(|K|=R-b-1\).

In each case the \(p\) endpoint profiles in one binary half-period are
exactly the cyclic rotations of the rotor's age composition, and the
second half-period supplies new literal owners with the same rank
profiles.

#### Proof

Equation (2.3) is exactly a permanent core added to the current block of a
cyclic positive composition.  The two displayed substitutions reproduce
the corresponding age types used in the monotone-rotor proof term for
term.  Marks in
that proof depend only on the offered suffix ranks, so they transfer along
(2.2).  The second clock parity changes literal owner and target labels but
not any rank. \(\square\)

### Corollary 3.2 (combined strengthened fractional chronology statement)

Together with
`MATH_THEOREM_DELAYED_MULTISTATE_QUEUE_MIXED_ROTOR_LIFT_20260807.md`,
every \(q\in\mathcal M_{R,d}\), including the optimal triangular Ferrers
residual vector, is a convex combination of literal cycles which
simultaneously have:

\[
 \boxed{
 \text{flat simple owners, local simple }q1\text{ palettes, exact owner
 biresidence, regeneration, and marked rank marginal }q.}
\tag{3.2}

The delayed theorem is essential here.  A full-depth positive-weight queue
has \(q_{R-1}=1\) only when every phase weight is one, so the binary queue
alone cannot realize any mixed vertex.  With that correction, the combined
result strictly strengthens the same-owner invariant circulation at the
local-component level.  It is still fractional across components and
coordinate embeddings.  It does **not** imply:

* one occurrence of every global owner;
* one occurrence of every named lower target;
* a connected component after integral selection;
* arbitrary-width upper coverage; or
* one common-cap compiler.

### Corollary 3.3 (owner-correlated triangular fractional factor)

Use the optimal Ferrers residual data

\[
 R=\left\lceil\frac k2\right\rceil,
 \qquad W={k\choose R},
 \qquad
 q_s=\frac{{k\choose s}-b_s}{W}\qquad(1\le s<R)
\tag{3.3}
\]

from the monotone-rotor theorem.  For all sufficiently large \(k\), there
is a symmetric fractional mixture of binary-toggle and delayed queue
components with
the following simultaneous loads:

1. every rank-\(R\) owner has load exactly one;
2. every rank-\(s\) lower target has designated load

   \[
   \boxed{1-\frac{b_s}{{k\choose s}};}
   \tag{3.4}
   \]

3. the Ferrers boundary contributes the complementary load
   \(b_s/\binom ks\);
4. every component in the support is already a simple resident Johnson
   owner cycle with simple local immediate palettes.

#### Proof

Write the convex combination from Corollary 3.2 as types \(c\) with
weights \(\lambda_c\), and let \(N_c\) be the number of endpoints in one
component of type \(c\).  Give type \(c\) endpoint mass
\(W\lambda_c\), equivalently component mass
\(W\lambda_c/N_c\), and average it uniformly over all coordinate
embeddings.  The total owner-occurrence mass is \(W\).  Symmetry
distributes it uniformly over the \(W\) rank-\(R\) owners, proving Item 1.

The marked rank-\(s\) occurrence mass is \(Wq_s\).  Symmetry distributes
it uniformly over \(\binom ks\) targets, giving

\[
 \frac{Wq_s}{\binom ks}
 =1-\frac{b_s}{\binom ks},
\]

which proves Items 2--3.  Item 4 follows from Theorem 2.1 here and
Theorem 3.1 of the delayed multistate queue theorem.  Both constructions
use only \(R+O(d)\) coordinates, so their ground-set conditions hold at
the optimal deadline for all sufficiently large \(k\). \(\square\)

This is stronger than separate fractional owner and trace feasibility:
both are carried by the same literal queue components.  It remains a
fractional mixture; it does not assert that its components can be rounded
without owner or named-target collisions.

### Corollary 3.4 (the immediate palettes have no fractional deficit)

In the symmetric mixture of Corollary 3.3, every rank-\((R-1)\) immediate
lower colour has load

\[
 \frac{W}{\binom{k}{R-1}},
\tag{3.6}
\]

and every rank-\((R+1)\) immediate upper colour has load

\[
 \frac{W}{\binom{k}{R+1}}.
\tag{3.7}

Thus neither immediate palette has a fractional coverage deficit.  More
explicitly:

* for \(k=2m+1\) and \(R=m+1\), the lower palette is exact and the upper
  load is \((m+2)/m\);
* for \(k=2m\) and \(R=m\), both loads are \((m+1)/m\).

#### Proof

Every cyclic component has one lower and one upper immediate colour per
owner.  Their lists are simple within the component.  The total mass in
each palette is therefore the owner mass \(W\), and full coordinate
symmetry distributes it uniformly over the corresponding rank layer.
The displayed specializations are the adjacent-binomial ratios. \(\square\)

## 4. Sharpened integral gate

The uniform dense-top queue fails globally because its fixed sparse rank
profile wastes \(\Theta(dW)\) cells.  The variable-weight family removes
that rank-histogram defect fractionally: it carries exactly the full
monotone-rotor mixture rather than one profile.

The remaining lower-side problem is now:

> **Queue rotor-fusion theorem.**  Round the convex combination in
> Corollary 3.2 to owner- and named-target-disjoint queue components, then
> splice their one-cut owner cycles into one chronology while keeping the
> marked Ferrers complement and protected upper/compiler resources.

Unlike the old same-owner rotors, every selected component already has a
simple resident Johnson owner cycle.  Thus owner variation and local
residence are no longer part of the missing lift; only global integral
recoupling and protected fusion remain.
