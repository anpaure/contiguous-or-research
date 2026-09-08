# Cyclic covariance for the repaired twelve-top recharge

## Owner preservation, phase holonomy, and the row-mixing gate

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, web
input, or probabilistic black box is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
 \qquad N=\binom{2m}{M},\qquad W=\binom{2m}{m},
\tag{0.1}
\]

and assume the hypotheses of
MATH_THEOREM_TWELVE_TOP_HISTOGRAM_NEUTRAL_BIDIRECTIONAL_RECHARGE_20260727.md.
The repaired packet has twelve distinct tops. On six \(P\)-rows it
rotates the current rooted word left by one position; on six \(Q\)-rows
it rotates right by one position. Its two shores are squarefree and
have the same middle-owner support.

The global deterministic conclusions are as follows.

1. **Coefficient-one ownership is dynamically automatic.** If a
   layer of currently available, top-disjoint repaired packets is
   switched inside a coefficient-one table, the new table has exactly
   the same global middle-owner set. This remains true through an
   arbitrary number of layers. Thus owner codegrees do not create a
   new inter-layer condition once a coefficient-one initial source
   table is present. They remain an initialization/embedding problem.

2. There is an exact cyclic-group sufficient condition. Let \(\sigma\)
   be a coordinate permutation of order \(L\), let \(T\) be a
   coefficient-one word table, and let \({\cal F}\) be a top-disjoint
   packet factor. If

   \[
                         S_{\cal F}T=\sigma T,
   \tag{0.2}
   \]

   where \(S_{\cal F}\) switches every packet of the factor, then

   \[
       T,\sigma T,\ldots,\sigma^{L-1}T
   \tag{0.3}
   \]

   is an exact \(L\)-layer chronology, using the translated factors
   \(\sigma^t{\cal F}\). Every layer is available and every table is
   coefficient one. For \(L=\Theta(m)\) and an almost-spanning factor,
   this gives \(\Theta(W)\) literal packet occurrences with no reset
   toll.

3. Equation (0.2) has a sharp phase-voltage condition. Give a top
   \(+1\) when it is a forward \(P\)-row and \(-1\) when it is a
   backward \(Q\)-row. Over one full group period, every top obeys

   \[
                         \sum_{t=0}^{L-1}
                           \epsilon(\sigma^{-t}U)
                            \equiv0\pmod M.
   \tag{0.4}
   \]

   Moreover, a top exposes \(\Theta(m)\) different rooted positions
   only if the cyclic partial sums of these signs have
   \(\Theta(m)\) range. Global six-plus/six-minus balance of each
   packet does not imply this orbitwise condition.

4. The natural block-preserving group construction fails exactly.
   If \(\sigma\) carries every marked twelve-top packet of
   \({\cal F}\) to another whole marked packet and preserves its two
   named shores, then (0.2) forces the shore choices to alternate along
   packet orbits. Every top then oscillates between two rooted states.
   It cannot supply \(\Theta(m)\) effective recharges, irrespective of
   the length of the packet orbit.

5. Therefore a successful group schedule must contain genuinely
   **row-mixing** transitions: every high-excursion top orbit must
   leave the block-preserving part of the successor graph. At such a
   transition, target rows of one packet are distributed among
   different successors and a successor is assembled from multiple
   predecessors. The common-core, carrier-cycle, repaired
   \(F/G\)-palette, and filler-column identities must survive this
   mixing.

6. Layer ordering by itself is also insufficient. Every top keeps one
   unrooted cyclic word throughout the chronology. In a
   phase-homogeneous template, its active seam pairs lie in one cyclic
   distance graph and consecutive packets move by one step on that
   graph. This flag information is absent from the solved abstract
   top edge-colouring.

The exact remaining finite object is a **row-mixed cyclic covariance
factor**, stated in Section 7. It is strictly smaller than the original
all-layer problem: one proves one equation (0.2), after which the group
orbit supplies all \(\Theta(m)\) layers and coefficient-one ownership
for free.

## 1. Marked packet states

Let \(r\) denote left rotation of a rooted cyclic word by one position.
For one repaired packet write its two shores as

\[
 A={\bf p}\sqcup r{\bf q},
 \qquad
 B=r{\bf p}\sqcup{\bf q}.
\tag{1.1}
\]

The packet switch is the involution

\[
                         s_P:A\longleftrightarrow B.
\tag{1.2}
\]

At a \(P\)-top it changes a word \(w\) to \(rw\); at a \(Q\)-top it
changes \(rw\) to \(w\). Thus attach the sign

\[
 \epsilon_P(U)=
 \begin{cases}
 +1,&U\text{ is a }P\text{-row},\\
 -1,&U\text{ is a }Q\text{-row}.
 \end{cases}
\tag{1.3}
\]

Reversing the packet shore reverses all twelve signs.

### Lemma 1.1 (unrooted-order invariant)

Along every chronology made only from repaired twelve-top packets, the
unrooted labelled cyclic order on each fixed top is invariant.

#### Proof

Every row transition is \(w\leftrightarrow rw\). Rotation changes the
rooted phase and fixes the underlying cyclic order. \(\square\)

This is the first state datum missing from the abstract top
hypergraph. Two occurrences at the same top can concatenate only if
their prescribed cyclic row orders agree up to rotation.

## 2. Coefficient one needs no new inter-layer packing theorem

For a word table \(T\), let \({\cal O}(T)\) denote its middle-owner
multiset.

### Theorem 2.1 (dynamic owner preservation)

Let \(T\) be coefficient one, and let \({\cal L}\) be any top-disjoint
family of repaired packet sources currently contained in \(T\).
Switching every packet in \({\cal L}\) gives a table \(T'\) with

\[
                         {\cal O}(T')={\cal O}(T)
\tag{2.1}
\]

as literal \(0\)-\(1\) incidence vectors.

Consequently every legal sequence

\[
                         T_0\to T_1\to\cdots\to T_s
\tag{2.2}
\]

starting from a coefficient-one table remains coefficient one and
keeps the same global middle-owner set.

#### Proof

For one packet, the repaired local theorem says that its two shores
are squarefree and have exactly the same middle-owner set. Since the
source packet rows occur in the coefficient-one table \(T\), owner
sets of distinct packets in \({\cal L}\) are disjoint. Replacing each
set by the identical target set therefore changes no coordinate of
\({\cal O}(T)\). Induction proves the assertion for (2.2).
\(\square\)

Thus an owner-aware hypergraph matching is needed only if one tries to
build \(T_0\) from independent packet shores. If one starts with an
existing coefficient-one atlas and uses available packet trades,
owners impose no further chronological or layer-ordering equation.

## 3. The cyclic covariance theorem

A coordinate permutation \(\sigma\in S_{2m}\) acts on tops, words,
packets, and owners by relabelling. For a word table \(T\), use the
left action

\[
 (\sigma T)(U)=\sigma\bigl(T(\sigma^{-1}U)\bigr).
\tag{3.1}
\]

Let \(S_{\cal F}\) denote simultaneous switching of a top-disjoint
packet factor \({\cal F}\).

### Theorem 3.1 (one-step covariance gives all layers)

Suppose:

1. \(T\) is a coefficient-one table;
2. \({\cal F}\) is a top-disjoint family of currently available
   repaired packet sources;
3. \(\sigma\) has order \(L\); and
4. the exact table identity

   \[
                         S_{\cal F}T=\sigma T
   \tag{3.2}
   \]

   holds.

Then, for \(0\le t<L\), put

\[
                         T_t=\sigma^tT,\qquad
                         {\cal F}_t=\sigma^t{\cal F}.
\tag{3.3}
\]

Every \({\cal F}_t\) is available in \(T_t\), and

\[
                         S_{{\cal F}_t}T_t=T_{t+1}.
\tag{3.4}
\]

All \(T_t\) are coefficient one and have the same middle-owner set.

If \({\cal F}\) covers \((1-o(1))N\) tops and
\(L=\Theta(m)\), the chronology contains

\[
             (1-o(1))\frac{LN}{12}=\Theta(W)
\tag{3.5}
\]

literal repaired-packet occurrences.

#### Proof

Relabelling commutes with the local switch:

\[
 S_{\sigma^t{\cal F}}(\sigma^tT)
       =\sigma^t(S_{\cal F}T)
       =\sigma^{t+1}T.
\tag{3.6}
\]

This proves availability and (3.4). Theorem 2.1 gives coefficient one
at every step. It also gives

\[
 {\cal O}(T)={\cal O}(S_{\cal F}T)
             ={\cal O}(\sigma T)=\sigma{\cal O}(T),
\tag{3.7}
\]

so the common owner set is \(\sigma\)-invariant. Finally, each factor
has \((1-o(1))N/12\) packets, which gives (3.5). \(\square\)

The theorem converts the \(\Theta(m)\)-layer problem into one
deterministic factor equation. It also makes the owner audit exact:
there is no accumulated collision or omitted-owner ledger after
(3.2).

An \(o(N)\) exceptional top set is harmless if it is
\(\sigma\)-invariant, omitted from the factors, and its restricted word
table is itself \(\sigma\)-invariant.

## 4. Orbitwise phase voltage

Assume (3.2), and orient every packet of \({\cal F}\) from its current
source shore to its target shore. Let \(\epsilon(U)\in\{+1,-1\}\) be
the resulting row sign at a covered top.

Fix a top \(U\). Its top-set orbit may have length smaller than \(L\),
because a power of \(\sigma\) can stabilize \(U\) while still
permuting its labels. Write the full group-period sequence as

\[
                         U_t=\sigma^tU\qquad(0\le t<L).
\tag{4.1}
\]

Use \(\sigma^{-t}\) to identify the cyclic word on \(U_t\) with a
word on \(U\). Equation (3.2) gives the phase recurrence

\[
                         h_{t+1}=h_t-\epsilon(U_{t+1})
                                  \pmod M.
\tag{4.2}
\]

### Theorem 4.1 (phase holonomy and excursion)

For every covered top \(U\), over one full group period,

\[
                         \boxed{\sum_{t=0}^{L-1}
                                  \epsilon(\sigma^{-t}U)
                                  \equiv0\pmod M.}
\tag{4.3}
\]

At a fixed top, the rooted phases exposed by the \(L\) translated
layers are the cyclic partial sums

\[
 0,\quad -\epsilon(U_{-1}),\quad
 -\epsilon(U_{-1})-\epsilon(U_{-2}),\quad\ldots
 \pmod M,
\tag{4.4}
\]

where indices follow the \(\sigma\)-orbit backwards. Therefore
\(\Theta(m)\) distinct rooted positions require partial-sum range
\(\Theta(m)\). In particular an alternating sign word exposes at most
two phases.

#### Proof

After the full \(L\) steps, \(\sigma^L=1\), so the coordinate
relabelling is the identity on the identified row state. The word is
injective, so its rooted phase can return to itself only when the
accumulated rotation is \(0\pmod M\). This proves (4.3). Iterating
(4.2) gives (4.4).
\(\square\)

If \(L<M\), (4.3) forces exact equality of the numbers of
plus and minus rows in the full-period sign word. Even when \(L\ge M\), the
congruence and the large-excursion requirement are both necessary.
The packetwise equality \(6-6=0\) gives only the sum over all top
orbits and does not imply either condition on each full-period word.

### Lemma 4.2 (the scalar voltage has a deterministic high-excursion solution)

Assume \(H=o(m)\), and let \(\sigma=(1\,2\,\cdots\,2m)\) be the long
coordinate cycle. All but \(e^{-\Omega(m)}N\) rank-\(M\) tops have
top-set orbit of length \(2m\).

Choose a canonical origin on every full orbit, for example its
lexicographically least binary incidence word, and prescribe the sign
word

\[
                         \underbrace{+\cdots+}_{m}
                         \underbrace{-\cdots-}_{m}.
\tag{4.5}
\]

It has zero voltage and partial-sum range \(m\). Hence it obeys (4.3)
and exposes \(m+1=\Theta(m)\) phases before returning.

#### Proof

If a rank-\(M\) incidence word is fixed by a nonidentity power
\(\sigma^k\), it is determined by at most
\(\gcd(2m,k)\le m\) bits. The union over the \(2m-1\) nonidentity
powers therefore contains at most

\[
                         2m\,2^m
\tag{4.6}
\]

tops. Since \(M=m+o(m)\),
\(\binom{2m}{M}=2^{2m-o(m)}\), so (4.6) is
\(e^{-\Omega(m)}N\). On a full orbit, (4.5) has total sum zero and its
partial sums are \(0,1,\ldots,m,m-1,\ldots,0\). \(\square\)

Lemma 4.2 is only a sign assignment on top orbits. It does not yet
partition each layer into packets with six plus and six minus rows.
It proves that neither congruence nor excursion is the scalar
obstruction; the missing constraint is the row-level packet assembly.

## 5. Whole-packet conjugation has period two

We now test the most natural group schedule.

Call \(({\cal F},\sigma)\) **shore-preserving block covariant** when
\(\sigma\) maps every marked packet block of \({\cal F}\) onto another
whole marked packet block, carries \(P\)-rows to \(P\)-rows and
\(Q\)-rows to \(Q\)-rows, and maps the named shore \(A\) to the named
shore \(A\) and \(B\) to \(B\).

### Theorem 5.1 (block-covariant period-two obstruction)

If (3.2) holds for a shore-preserving block-covariant pair
\(({\cal F},\sigma)\), then packet shore choices alternate along every
\(\sigma\)-orbit of packet blocks. Corresponding top-row signs also
alternate. Hence every covered top exposes at most two rooted phases.

In particular no such construction yields \(\Theta(m)\) effective
recharges per top, even when \(\sigma\) has order \(\Theta(m)\).

#### Proof

For a packet block \(B\), let \(o(B)\in\{0,1\}\) record whether \(T\)
contains shore \(A\) or shore \(B\) there. Switching replaces it by
shore \(1-o(B)\). On the block \(\sigma B\), the right side
\(\sigma T\) contains shore \(o(B)\), because the conjugation preserves
the shore names. Equation (3.2) therefore gives

\[
                         1-o(\sigma B)=o(B),
\qquad\text{so}\qquad
                         o(\sigma B)=1-o(B).
\tag{5.1}
\]

Reversing a packet shore reverses all twelve row signs. Since
\(\sigma\) also preserves the \(P/Q\) row designation, corresponding
signs alternate. Theorem 4.1 then bounds the exposed phase set by two.
\(\square\)

The same argument applies to a fixed packet factor used forward and
backward, to a cyclic ordering of whole packet blocks, and to any
Latin schedule whose group action merely permutes complete marked
packets. These schedules recycle tops but not effective rooted
positions.

The theorem deliberately assumes the natural shore-preserving
conjugation. A construction using a shore-swapping automorphism must
include that swap in its voltage ledger; it is not licensed to omit
(4.3). The only possible escape is still a nonalternating orbitwise
sign word, which requires row-level recoupling.

## 6. The seam-pair necklace

Fix a top \(U\) and its invariant cyclic word

\[
                         \pi_U=(u_0,u_1,\ldots,u_{M-1}).
\tag{6.1}
\]

In one phase-homogeneous marked row template, let its two active seam
positions have offsets \(a,b\pmod M\). At phase \(h\), the active seam
pair is

\[
                         e_U(h)=
              \{u_{a+h},u_{b+h}\}.
\tag{6.2}
\]

The graph

\[
                         K_{a,b}(\pi_U)
                   =\{e_U(h):h\in{\mathbb Z}_M\}
\tag{6.3}
\]

has maximum degree two; it is a union of cyclic distance components.
A forward or backward recharge changes \(h\) by \(+1\) or \(-1\).

### Corollary 6.1 (ordering cannot repair a bad flag set)

In a phase-homogeneous conjugate schedule, all active seam pairs used
at \(U\) must lie in one graph (6.3), and their chronological phases
must form a nearest-neighbour walk on its cyclic index set.

Consequently:

1. if the selected seam-pair graph at \(U\) has a vertex of degree at
   least three, no ordering of the layers can make it literal;
2. if it has \(c\) components in (6.3), at least \(c\) independent
   phase starts are needed; and
3. a finite catalogue of \(k\) seam offsets has degree at most \(2k\)
   at every label.

#### Proof

Lemma 1.1 fixes \(\pi_U\). Formula (6.2) lists every seam pair visible
under phase conjugation, and a local packet changes the phase by one.
The three assertions follow. \(\square\)

For a \(P\)-row on the old shore, the seam pair is the carrier pair
from the six-label cycle. For a rotated \(Q\)-row it is instead the
appropriate pair of first palette labels. Thus the relevant flag is
not merely the abstract top \(C+e\); it includes the current row role,
phase, and active seam pair. The solved top edge-colouring forgets all
three data.

## 7. The exact row-mixed covariance factor

Let \({\cal F}\) be one almost-spanning packet factor. Form its
**successor multigraph** \(D_\sigma({\cal F})\):

* its vertices are packet blocks of \({\cal F}\);
* for every top \(U\) in a block \(B\), draw a directed row arc from
  \(B\) to the block containing \(\sigma U\);
* label the arc by the source row role, target row role, sign, active
  seam pair, and protected \(F/G\)-palette incidences.

Every block has twelve outgoing and twelve incoming row arcs.
Block-preserving covariance is the degenerate case in which all twelve
arcs from a block have one common endpoint; Theorem 5.1 closes it.

The remaining finite theorem is:

> **RMCF\(_{12}\) (row-mixed cyclic covariance factor).** Find
> \((T,{\cal F},\sigma)\), after omitting \(o(N)\) tops, such that:
>
> 1. \(\sigma\) has order \(L=\Theta(m)\), and
>    \(D_\sigma({\cal F})\) is genuinely row mixing;
> 2. on every \(\sigma\)-orbit, the signs obey (4.3) and their partial
>    sums have \(\Theta(m)\) range;
> 3. at every top, the incoming row has the same unrooted cyclic word
>    as the outgoing row and its seam flags obey (6.2);
> 4. the twelve incoming target rows at every successor block assemble
>    into one repaired packet source: a common \((M-2)\)-core, two
>    edge-disjoint six-cycles, the proper six-colour \(F/G\) incidence
>    pattern, and the matched protected columns;
> 5. the filler occurrences admit the equivariant column matching
>    required by Lemma 3.1 of the local twelve-top theorem; and
> 6. the resulting initial table \(T\) is coefficient one.

Conditions 1--5 are exactly the word-state availability equation

\[
                         S_{\cal F}T=\sigma T.
\tag{7.1}
\]

Condition 6 is needed only at time zero; Theorems 2.1 and 3.1 then
preserve it through all layers.

The most useful reduction is therefore:

\[
\boxed{\text{construct one row-mixed covariance factor, not
              \(\Theta(m)\) independently packed layers}.}
\tag{7.2}
\]

The repaired local palette colouring is compatible with this route:
it gives distinct protected contexts at every outside carrier vertex.
What remains is to route those protected rows between different packet
blocks. A whole-packet Latin square, a block orbit, or a mere ordering
of the existing abstract colour classes cannot perform that routing.

## 8. Exact implication boundary

Proved here:

1. coefficient-one owners are automatically preserved through every
   legal layer sequence;
2. the one-step cyclic covariance theorem, giving all
   \(\Theta(m)\) layers from (3.2);
3. the exact orbitwise phase congruence and large-excursion condition;
4. a deterministic zero-voltage, linear-excursion sign schedule on all
   but exponentially few long-cycle top orbits;
5. the period-two obstruction for shore-preserving whole-packet
   conjugations;
6. the active seam-pair necklace obstruction to layer reordering; and
7. the precise row-mixed successor object RMCF\(_{12}\).

Not proved here:

1. a row-mixed factor satisfying RMCF\(_{12}\);
2. an equivariant filler completion on such a mixed factor; or
3. an initial coefficient-one table containing its source shores.

Thus the abstract top edge-colouring has the correct volume but the
wrong state space. A viable deterministic schedule must act on flagged
rows and mix packet blocks; any schedule which transports only whole
twelve-top packets is intrinsically two-periodic.
