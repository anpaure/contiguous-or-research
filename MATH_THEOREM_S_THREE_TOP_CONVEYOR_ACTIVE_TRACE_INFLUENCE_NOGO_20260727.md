# The three-top conveyor has an exact active kernel but cannot by itself control active trace influence

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},
\]

and

\[
 M=m+H,\qquad L=m-3H+1,
\tag{0.1}
\]

where

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 \Lambda=\frac W{N_H}=m+O(H).
\tag{0.2}
\]

For a tagged path family, let \(\mu_{q,\sigma}^\tau(T)\) be the number of
tag-active occurrences at signed depth \((q,\sigma)\) having literal
target \(T\), and put

\[
 \Xi_{\tau,\sigma}
 =\sum_q\sum_T\binom{\mu_{q,\sigma}^\tau(T)}2,
 \qquad
 \Xi_\tau=\Xi_{\tau,+}+\Xi_{\tau,-},
\tag{0.2a}
\]

where the internal ranges are \(1\le q<H\) above and \(1\le q\le H\)
below. The separately allowed root endpoint is excluded. Positive-length
traces inside one path are distinct, so (0.2a) is exactly the active
cross-path pair influence used in the repaired-ring gate. We also write

\[
 e_{q,\sigma}
 =\sum_T\bigl(\mu_{q,\sigma}^\tau(T)-1\bigr)_+;
 \qquad e_{q,\sigma}\le\sum_T\binom{\mu_{q,\sigma}^\tau(T)}2.
\tag{0.2b}
\]

This report combines the active trace-influence gate
\(\Xi_\tau=o(W)\) with the three-top/two-base conveyor of
`MATH_THEOREM_THREE_TOP_TWO_BASE_PROMOTION_CONVEYOR_20260726.md`.
It proves the following exact statements.

1. The complete conveyor clips verbatim to three literal common-core
   \(L\)-phase paths. Both shores have the same squarefree support of
   exactly \(3L\) middle owners, so the switch has **zero middle
   damage**.

2. After tags are transported with their physical middle owners, the
   exact active upper kernel at depth \(q\) is supported on at most
   \(4q\) target cells. The active lower kernel is supported on at most
   \(20q\) cells. For fully active carriers the upper kernel is zero and
   the lower kernel has exactly \(8q\) positive and \(8q\) negative
   unit coefficients. The full-activation clauses are packet identities,
   not assertions that the exact global SCD tag census permits full
   activation at every depth.

3. At every depth and for arbitrary transported binary tags, the
   collision-energy derivative has no quadratic self-toll:

   \[
   \mathcal C(R+\Gamma^1)-\mathcal C(R+\Gamma^0)
   =\langle R,\delta^\tau\rangle,
   \qquad
   \mathcal C(L)=\sum_T\binom{L_T}{2}.
   \tag{0.3}
   \]

   The identical formula holds for every integer floor baseline.

4. The certified carrier is intrinsically one-sided. Its direct upper
   derivative is coordinatewise zero at every positive depth. Combining
   this with the previously proved local-reversal bank gives, conditional
   on the already isolated legal full-SCD tag completion, a state with
   middle defect \(o(W)\), rank deficit \(o(W)\), and

   \[
   \Xi_{\tau,+}\ge(c/42+o(1))W
   \tag{0.4}
   \]

   which is unchanged by every packing, overlapping family, or serial
   composition that is carrier-faithful at every step.

5. Allowing arbitrary owner-transported tags removes the literal zero-side
   invariant, but not the one-round capacity obstruction. There is an
   integral, path-uniform, floor-correct partial tag state, with aggregate
   census deficit \(o(W)\), conditional on any prescribed owner-disjoint
   one-path-per-top common-core family from the already separate physical
   fusion gate, and whose direct upper repeat excess at one depth is

   \[
   (1/4-o(1))W.
   \tag{0.5}
   \]

   Every top-disjoint conveyor packing changes at most \(o(W)\) relevant
   occurrences at that depth, so (0.5) survives. Any serial escape in
   this more permissive, globally counted owner-transport model needs

   \[
   \left(\frac1{8\sqrt{\log2}}-o(1)\right)\frac W{\sqrt m}
   =\left(\frac1{8\sqrt{\log2}}-o(1)\right)\sqrt m\,N_H
   \]

   conveyor operations and hence average top participation at least
   \((3/(8\sqrt{\log2})-o(1))\sqrt m\).

6. Even locally, a flat exterior load makes every nonzero conveyor
   derivative energy-neutral. Thus no statewise strict contraction
   theorem follows from the packet kernel alone.

Therefore the requested dense influence-preserving absorber is not
supplied by the exact conveyor. The certified packet cannot change the
bad sign at all; an arbitrary noncoherent owner-transported extension has
only \(O(q)\)
throughput per packet and no uniform charge. A positive successor would
need a genuinely two-sided, globally charged, repeatedly overlapping
tag-transport theorem. No coefficient-one conclusion is claimed.

## 1. Physical trace notation and the clipping

Use the conveyor tops

\[
 U_0=C\cup\{x,y\},\qquad
 U_1=C\cup\{x,a\},\qquad
 U_2=C\cup\{a,y\},
\tag{1.1}
\]

with \(|C|=M-2\). The old and new shores are the plus and minus
specializations of the two positional bases \(\omega,\omega'\) from the
source theorem.

For one retained phase on a top \(U\), the direct physical trace at
signed rank \(m+r\) is

\[
 T_{r}=U\setminus I_{H-r},
\tag{1.2}
\]

where \(I_\ell\) is its length-\(\ell\) deletion interval. Thus direct
upper depth \(q\) uses length \(H-q\), and direct lower depth \(q\)
uses length \(H+q\).

### Theorem 1.1 (exact common-core clipping)

Assume \(M\ge12H-4\). The positional fillers can be chosen so that the
complete three-frame conveyor restricts to three literal common-core
\(L\)-phase paths, with the same derivative at every internal signed
depth. Both clipped shores have the same squarefree middle support of
size \(3L\).

#### Proof

Put all filler into \(F_1\), so

\[
 |F_1|=M-8H+2\ge4H-2.
\]

The placeholder-free segment

\[
 B=(\widehat A^+,F_1,\overleftarrow{\widehat B^-})
\]

is ordered identically in \(\omega\) and \(\omega'\) and has length at
least \(6H-2\). Choose a consecutive \(2H\)-block \(Q\subset B\) with
at least \(2H-1\) labels of \(B\) on each side.

Exactly \(4H-1\) cyclic central \(2H\)-words meet \(Q\). Every one lies
wholly in the common segment \(B\), and hence is unchanged by every
placeholder transposition at all truncated depths. Delete precisely these
phases. The number retained is

\[
 M-(4H-1)=L.
\]

Every retained central word avoids \(Q\), so every retained chain mask
contains the same \(2H\)-core. The deleted contribution is identical on
both shores, hence every complete-deck derivative survives unchanged.
The full conveyor's middle support was equal and squarefree; deleting the
same \(3(4H-1)\) fixed occurrences leaves equal squarefree supports of
size \(3L\). \(\square\)

At the calibrated scale, \(M/H\to\infty\), so the numerical hypothesis
holds for all sufficiently large \(m\).

## 2. The exact transported-tag kernel

Let \(\mathcal O\) be the common \(3L\)-element middle support. Match old
and new occurrences by their literal middle owner, and transport the tag
with that owner. Write

\[
 \alpha_q(X)={\bf1}_{\{\tau(X)\ge q\}}.
\tag{2.1}
\]

Unless stated otherwise, **owner transport** means that \(\tau(X)\) stays
attached to the literal physical middle set \(X\) when that owner moves to
a new frame position. Only the global nested tag multiset is then fixed;
the number of active phases on an individual rank-\(M\) top may change.
Freezing the active count of every top is an additional constraint, and
keeping tags on top positions instead is a different transport law. These
three models are separated explicitly in Proposition 2.5 below.

### Lemma 2.1 (middle overlay)

The old-to-new occurrence permutation on \(\mathcal O\) is the disjoint
union of

\[
 2H\text{ directed }3\text{-cycles}
 \quad\text{and}\quad
 3L-6H\text{ fixed owners}.
\tag{2.2}
\]

The cycles are indexed by a type \(A\) or \(B\) and an index
\(u=0,\ldots,H-1\); the two types rotate in opposite directions.

#### Proof

For an \(A\)-context

\[
 K=K_{A,u}^{\omega}(H)=K_{B,u}^{\omega'}(H),
\]

the three old owners on \((U_0,U_1,U_2)\) are

\[
 (C\setminus K)+y,\qquad
 (C\setminus K)+x,\qquad
 (C\setminus K)+a.
\]

On the new shore they occupy the cyclically shifted top positions. The
\(B\)-contexts give the reverse shift. These \(2H\) context families are
pairwise disjoint by the arm construction. Every middle interval avoiding
one of these contexts is ownerwise fixed. \(\square\)

### Lemma 2.1a (shore squarefreeness)

For either conveyor shore and every direct deletion length
\(2\le h\le2H\), the union of its three frame decks is squarefree. At
\(h=1\), exactly the three cells obtained by deleting the exclusive
coordinate from each adjacent pair of tops have load two; on the two
shores, the unordered pair of physical middle owners feeding each such
cell is the same (the two owners are merely interchanged).

#### Proof

Within one frame, distinct cyclic \(h\)-intervals give distinct targets.
A collision between two of the three tops must delete their two exclusive
coordinates and retain their shared outside coordinate. It would therefore
identify the two corresponding \((h-1)\)-label placeholder contexts.

For \(2\le h\le H\), those two contexts contain labels from distinct
inner-arm alphabets, so they cannot agree. For \(H<h\le2H\), each context
still contains at least \(H-1\) labels from its own inner-arm alphabet;
the added labels lie only in its outer collar. The three pair comparisons
are respectively between disjoint inner types in \(\omega\) and
\(\omega'\), or between the opposite placeholder roles inside
\(\omega'\). Hence equality is again impossible.

When \(h=1\), the context is empty and precisely the three adjacent-top
collisions remain. The inner-neighborhood interchange at the middle
\(H\)-window shows directly that each old owner pair is the corresponding
new owner pair in the opposite order. \(\square\)

### Theorem 2.2 (active upper kernel)

For \(1\le q<H\), at direct upper depth \(q\), exactly the cycles with
\(u<q\) can act.
If \(n_q\) of these \(2q\) cycles are nonmonochromatic under
\(\alpha_q\), then

\[
 \boxed{
 \|\delta_{q,+}^{\tau}\|_0
 =\|\delta_{q,+}^{\tau}\|_2^2
 =2n_q\le4q.}
\tag{2.3}
\]

There are exactly \(n_q\) positive and \(n_q\) negative cells.

#### Proof

Use the common right-end convention. The upper trace is obtained by
removing the first \(q\) letters of the middle deletion window. If
\(u\ge q\), the distinguished placeholder remains visible, so the trace
travels with its owner and is unchanged. If \(u<q\), the placeholder is
removed: the three target cells remain fixed while their three owner tags
rotate.

On an \(A\)-cycle, the derivative on those cells is

\[
 (\alpha_1-\alpha_0,\ \alpha_2-\alpha_1,\
   \alpha_0-\alpha_2),
\tag{2.4}
\]

and the \(B\)-cycle has the reverse gradient. For binary \(\alpha_i\),
this is zero for a monochromatic cycle and otherwise is a permutation of
\((1,-1,0)\). The context cells of different cycles are disjoint, proving
(2.3). At \(q=H-1\), the three possible singleton double cells have the
same unordered owner pairs on both shores by Lemma 2.1a and contribute
zero; they do not alter the count. \(\square\)

In particular, if the active carrier is coherent on every middle
3-cycle, then

\[
 \delta_{q,+}^{\tau}=0
\tag{2.5}
\]

coordinatewise. This includes the complete certified conveyor.

### Theorem 2.3 (active lower kernel)

For \(1\le q\le H\), at direct lower depth \(q\), exactly \(12q\)
middle owners can change:

* \(6q\) fixed owners whose left extension first meets a placeholder;
* the \(6q\) owners in the last \(q\) cycles of each type.

On these owners, the old and new target images have exactly

\[
 4q\text{ common cells},\qquad
 8q\text{ old-only cells},\qquad
 8q\text{ new-only cells}.
\tag{2.6}
\]

Consequently

\[
 \boxed{
 \|\delta_{q,-}^{\tau}\|_0
 =\|\delta_{q,-}^{\tau}\|_2^2\le20q.}
\tag{2.7}
\]

The positive and negative support sizes agree. If all affected owners are
active, the common-cell terms vanish and

\[
 \boxed{
 \|\delta_{q,-}\|_0
 =\|\delta_{q,-}\|_2^2=16q,}
\tag{2.8}
\]

with \(8q\) coefficients of each sign.

#### Proof

The boundary-index calculation in the source theorem gives the two listed
owner classes and no others. By Lemma 2.1a, each clipped shore is
squarefree at this rank. Its support has size \(3L\), while the fully active derivative has
support \(16q\); hence the full shore supports intersect in

\[
 3L-8q
\]

targets. The \(3L-12q\) unaffected owners already give that many common
targets. Thus the affected images have exactly \(4q\) common cells and
the two unique shores have size \(8q\) each.

The common cells form a matching between one old and one new affected
owner. Their coefficient is the difference of two activity bits. The
old-only and new-only cells carry one activity bit each. This gives at
most \(4q+8q+8q=20q\) nonzero unit coefficients and proves (2.7). Full
activation kills every common-cell difference and leaves the two unique
supports, proving (2.8). \(\square\)

The exact all-depth worst-case edit ledger for one tagged conveyor is

\[
 \sum_{q=1}^{H-1}4q+\sum_{q=1}^{H}20q
 =12H^2+8H.
\tag{2.9}
\]

For the fully active lower carrier, its total moved support is

\[
 16\sum_{q=1}^Hq=8H(H+1).
\tag{2.10}
\]

Equations (2.8)--(2.10) are formal complete-packet identities. They do
not assert simultaneous feasibility under the global SCD tag census. In
particular, at the endpoint \(q=H\) a legal promotion-path census has at
most one tag-\(H\) phase per top; the fully active \(q=H\) packet is only
an extremal kernel calculation.

For two conveyors \(P,Q\), the local theorem supplies only

\[
 |\langle\delta_{P,q,+},\delta_{Q,q,+}\rangle|\le4q,
 \qquad
 |\langle\delta_{P,q,-},\delta_{Q,q,-}\rangle|\le20q.
\tag{2.11}
\]

No smaller global overlap constant follows without a packet-codegree
theorem.

### Proposition 2.4 (exact per-top tag-profile condition)

Let \(A_i(q),B_i(q)\) be the active-owner counts at old top
\(i\in\mathbb Z/3\mathbb Z\) among the two cycle orientations. Fixed
owners cancel. The same number of active phases remains on every top if
and only if

\[
 \boxed{
 A_{i+1}(q)+B_{i-1}(q)=A_i(q)+B_i(q)
 \quad(i\in\mathbb Z/3\mathbb Z).}
\tag{2.12}
\]

This condition does not force the upper kernel to vanish: opposite mixed
patterns on one \(A\)- and one \(B\)-cycle satisfy it. Full lower action
requires \(4q\) affected active phases per top, so it is scalarly possible
exactly when \(b_q\ge4q\), where the common-core quota is

\[
 b_q=\min\!\left\{L-1,
 \max\!\left(0,\left\lfloor\frac{N_q}{N_H}\right\rfloor-1\right)
 \right\}.
\]

For every \(q\le\lfloor2H/3\rfloor\), the common-core quota has

\[
 b_q\ge m^{5/9+o(1)}\gg H.
\tag{2.13}
\]

Since \(q\le2H/3\), this implies \(b_q\ge4q\) for all sufficiently large
\(m\). Thus scalar tag capacity does not block the active kernel in the
critical reversal range at any fixed depth. This is not a simultaneous
nested-tag realization or a completion inside one full SCD.

### Proposition 2.5 (the three tag-transport laws are inequivalent)

Fix a direct upper depth \(q<H\), put \(h=H-q\), and suppose initially
that every retained phase on top \(U_i\) has the same activity bit
\(a_i\in\{0,1\}\).

1. Under physical-owner transport with no per-top count constraint, every
   nonmonochromatic triple \((a_0,a_1,a_2)\) mixes all \(2q\) acting
   middle cycles, and therefore

   \[
   \|\delta_{q,+}\|_0=4q,
   \qquad |\operatorname{supp}(\delta_{q,+})_+|=2q.
   \tag{2.14}
   \]

2. Under owner transport plus exact preservation of the active count on
   each top, a path-uniform triple is legal only when
   \(a_0=a_1=a_2\); its upper derivative is then zero.

3. If tags are instead kept on their top positions, then, for
   \(2\le h\le H\), every nonmonochromatic triple has

   \[
   \|\delta_{q,+}^{\rm pos}\|_0=4h,
   \qquad |\operatorname{supp}(\delta_{q,+}^{\rm pos})_+|=2h.
   \tag{2.15}
   \]

   At \(h=1\), this positional derivative is zero. Position transport
   reassigns tags between physical middle owners and is not the transport
   law used in Theorems 2.2 and 5.2.

#### Proof

The first assertion is Theorem 2.2 with all \(2q\) acting cycles mixed.
For the second, path uniformity gives

\[
 A_i(q)=B_i(q)=H a_i.
\]

Equation (2.12) becomes

\[
 a_{i+1}+a_{i-1}=2a_i
 \qquad(i\in\mathbb Z/3\mathbb Z),
\]

whose binary solutions are exactly the two monochromatic triples.

For position transport, the direct-deck derivative is

\[
 \begin{aligned}
 \delta_h^{\rm pos}
 &=a_0d_h^\omega(x,y)
   +a_1d_h^{\omega'}(x,a)
   +a_2d_h^{\omega'}(a,y)\\
 &=(a_0-a_1)d_h^\omega(x,a)
   +(a_0-a_2)d_h^\omega(a,y),
 \end{aligned}
\]

using \(d_h^{\omega'}=-d_h^\omega\) and endpoint telescoping. If
\(h\ge2\), the \(2h\) placeholder contexts are distinct, and a
nonmonochromatic binary triple contributes one positive and one negative
cell per context. This proves (2.15). For \(h=1\), the two empty
placeholder contexts coincide and every complete singleton deck is
order-independent, so the derivative is zero. \(\square\)

## 3. Exact collision-energy derivative

Let \(\Gamma_{q,\sigma}^0,\Gamma_{q,\sigma}^1\) be the packet load
vectors on its two shores, after transported tags, and let
\(R_{q,\sigma}\) be the external load. Put

\[
 \mathcal C(L)=\sum_T\binom{L_T}{2}.
\]

### Theorem 3.1 (no active quadratic self-toll)

At every internal signed depth,

\[
 \boxed{
 \mathcal C(R+\Gamma^1)-\mathcal C(R+\Gamma^0)
 =\langle R,\delta^\tau\rangle.}
\tag{3.1}
\]

The same identity holds for every integer floor baseline \(c\), with

\[
 \Phi_c(L)=\frac12\sum_T(L_T-c)(L_T-c-1)
\tag{3.2}
\]

in place of \(\mathcal C\).

#### Proof

Expanding the left side gives the displayed linear term plus

\[
 \mathcal C(\Gamma^1)-\mathcal C(\Gamma^0).
\]

By Lemma 2.1a, each complete lower shore is squarefree, and each upper
shore with deletion length \(h\ge2\) is squarefree. Thus changed cells
cannot acquire a hidden collision with unchanged cells, and both packet
self-energies are zero there. At upper deletion length \(h=1\)
(equivalently \(q=H-1\)), the only nonsquarefree cells are the three
double targets. The unordered pair of physical owners feeding each such
cell is identical on the two shores, merely swapped; transported tags
therefore give the same two activity bits and the same binomial
self-energy. Hence the remaining difference is zero. \(\square\)

Indeed, owner transport preserves the number of active occurrences, so
\(\sum_T\delta_T^\tau=0\). Since

\[
 \Phi_c(L)=\mathcal C(L)-c\sum_TL_T+\text{constant},
\]

the floor-baseline term has zero derivative, proving the asserted
extension of (3.1).

At the middle rank the load vector is identical, not merely
energy-equivalent. At the root endpoint \(q=H\), keep the already allowed
\(O(N_H)=o(W)\) boundary exception unless tag-\(H\) locations are separately
synchronized.

## 4. The exact carrier-faithful one-sided obstruction

For a carrier-faithful activation, every acting middle 3-cycle is
monochromatic. By (2.5), every exact conveyor substitution has

\[
 \delta_{q,+}^{\tau}=0
 \qquad(1\le q<H).
\tag{4.1}
\]

This is the direct-upper zero side in the source theorem. Reversing the
shore, cyclically reversing the frames, or relabeling coordinates does not
change (4.1). A global-complement packet acting on this side would be a
different physical construction, because it would use rank-\((m-H)\)
roots rather than the given rank-\(M\) tops.

### Theorem 4.1 (carrier invariant and conditional tagged realization)

Given any one-path-per-top common-core family with middle overload plus
leave \(o(W)\), there is a bank of literal replacement path pairs which
keeps that defect \(o(W)\) and has untagged upper collision potential of
order \(W\). Conditional on completing the source report's minimum-tag
prescription inside one legal full SCD, this bank has aggregate rank
deficit \(o(W)\) and

\[
 \Xi_{\tau,+}\ge(c/42+o(1))W,
\tag{4.2}
\]

such that every sequence of carrier-faithful exact conveyor substitutions
leaves the complete direct-upper load vector, and hence (4.2), unchanged,
provided every conveyor is carrier-faithful at the moment it is applied.

#### Proof

Use the middle-disjoint local-reversal gadget from
`MATH_THEOREM_S_COMMON_CORE_PHYSICAL_FUSION_COMPENSATED_NIBBLE_20260726.md`.
Put

\[
 h=\lfloor H/2\rfloor,\quad
 q_0=\lceil H/2\rceil,\quad
 q_1=\lfloor2H/3\rfloor,
\]

and

\[
 K=\left\lfloor\frac{cW}{H^2}\right\rfloor
\tag{4.3}
\]

for one sufficiently small fixed \(c>0\). On each of \(K\) disjoint
adjacent-top pairs, the two new paths have no common middle owner and have
exactly \(H-q\) common direct-upper targets at depth
\(q_0\le q\le q_1\).

Replacing the \(2K\) old paths changes middle overload plus leave by at
most

\[
 4KL=O(W/\log m)=o(W).
\tag{4.4}
\]

The minimum-tag threshold flow proved with that gadget activates every
displayed collision and fits the exact scalar tag capacities. Completion
of the remaining tags in one full SCD retains the explicit caveat from the
source report; in the partial common-core census its aggregate occurrence
deficit is \(o(W)\).

At each depth, the distinguished collision pairs use disjoint physical
occurrences. Therefore

\[
 \begin{aligned}
 \Xi_{\tau,+}
 &\ge K\sum_{q=q_0}^{q_1}(H-q)\\
 &\ge KH^2/21\\
 &\ge(c/42+o(1))W.
 \end{aligned}
\tag{4.5}
\]

Equation (4.1) says that one carrier-faithful switch leaves every direct
upper target load unchanged. Induction proves the same for an arbitrary
overlapping or serial composition in which carrier-faithfulness remains
true at every step. \(\square\)

More generally, distinguish all collision pairs in (4.5) by occurrence
tokens. If arbitrary active substitutions \(s\) are allowed, put

\[
 \mathfrak R_+
 =\sum_s\sum_{q=q_0}^{q_1}
 \|(-\delta_{s,q,+}^{\tau})_+\|_1.
\tag{4.6}
\]

One negative unit can kill at most one distinguished equal-target pair,
so

\[
 \boxed{
 \Xi_{\tau,+}^{\rm final}
 \ge(c/42+o(1))W-\mathfrak R_+.}
\tag{4.7}
\]

Thus every noncoherent escape must manufacture a linear upper negative
edit. The exact certified carrier has \(\mathfrak R_+=0\).

## 5. Arbitrary transported tags: a top-disjoint capacity wall

The preceding invariant disappears on nonmonochromatic middle cycles.
The \(4q\) kernel bound nevertheless rules out a single top-disjoint dense
packing.

This section deliberately grants the conveyor the more permissive model:
tags move with physical middle owners, only the global nested counts are
preserved, and individual top profiles may change. Thus Proposition 2.4
is not imposed. A lower bound in this model also applies to any
owner-transport process with frozen per-top profiles; it says nothing
about the distinct, position-transport operation in Proposition 2.5(3).

Fix a coordinate \(z\), and let

\[
 N^{\bar z}=\#\{U\in\tbinom{[2m]}M:z\notin U\}
 =\binom{2m-1}M=\frac{m-H}{2m}N_H.
\tag{5.1}
\]

Define

\[
 q_*=\min\{1\le q<H:N_q\le L N^{\bar z}\}.
\tag{5.2}
\]

Since

\[
 \frac{L N^{\bar z}}W
 =\frac L\Lambda\frac{m-H}{2m}
 =\frac12-o(1),
\]

and, uniformly for \(q=O(\sqrt m)\),

\[
 \frac{N_q}{W}=\prod_{j=1}^q\frac{m-j+1}{m+j},
 \qquad
 \log\frac{N_q}{W}
 =-\frac{q^2}{m}
  +O\!\left(\frac q m+\frac{q^4}{m^3}\right),
\]

minimality in (5.2) gives

\[
 \frac{q_*}{\sqrt m}\longrightarrow\sqrt{\log2},
 \qquad
 \frac{N_{q_*}}W\longrightarrow\frac12.
\tag{5.3}
\]

For \(0\le q<H\), put

\[
 r_q=\min\left\{N_H,\left\lfloor\frac{N_q}{L}\right\rfloor\right\}.
\tag{5.4}
\]

Choose nested top sets \(\mathcal S_{q+1}\subseteq\mathcal S_q\), with
\(|\mathcal S_q|=r_q\), such that

\[
 \mathcal S_q\subseteq\{U:z\notin U\}
 \qquad(q\ge q_*).
\tag{5.5}
\]

This is possible by (5.2); first choose \(\mathcal S_{q_*}\) on that
shore, shrink inside it for larger \(q\), and extend arbitrarily for
smaller \(q\).

Give every one of the \(L\) phases on top \(U\) the common tag

\[
 \tau(U)=\max\{q<H:U\in\mathcal S_q\}.
\tag{5.6}
\]

This is an integral literal nested phase schedule in the owner-transport
model. Place it on any prescribed owner-disjoint one-path-per-top
common-core family. The middle support then remains owner-disjoint, with
leave exactly \(W-LN_H\). Existence of that family is the already separate
physical fusion gate, not a conclusion of this report. The schedule is
only a partial floor-correct census: completing these annotations inside
one full SCD is not proved here.

### Lemma 5.1 (all-depth partial-census deficit ledger)

The number of active occurrences at each sign and depth \(q<H\) is

\[
 A_q=Lr_q,
\tag{5.7}
\]

and the aggregate middle occurrence deficit plus signed occurrence deficit
is \(o(W)\). The middle overload is zero and the middle leave is exactly
\(W-LN_H\).

#### Proof

At the middle rank the deficit is

\[
 W-LN_H=O(HN_H)=o(W).
\]

If the floor, rather than the cap, is active in (5.4), then
\(0\le N_q-A_q<L\). If the cap is active, then
\(N_q-A_q=N_q-LN_H\); this can occur only for \(q=O(\sqrt H)\), and its
sum is \(O(H^{3/2}N_H)=o(W)\), exactly as in the common-core floor
ledger. Summing the floor errors over \(H\) depths costs \(O(HL)\), which
is polynomial and hence \(o(W)\). Leave depth \(H\) exceptional at cost
\(2N_H=o(W)\). Doubling for the two signs proves the assertion.
Explicitly, the complete ledger is bounded by

\[
 (W-LN_H)
 +O\!\left(H^{3/2}N_H+HL+N_H\right)
 =o(W).
\tag{5.7a}
\]

\(\square\)

### Theorem 5.2 (linear statewise repeat and packing lower bound)

At direct upper depth \(q_*\), the state (5.4)--(5.6) has

\[
 e_{q_*,+}\ge(1/4-o(1))W.
\tag{5.8}
\]

After any top-disjoint packing of owner-transported-tag conveyors, it still has

\[
 e_{q_*,+}^{\rm final}\ge(1/4-o(1))W.
\tag{5.9}
\]

#### Proof

Every active top at this depth avoids \(z\), so every direct upper target,
being a subset of its top, also avoids \(z\). The number of possible
rank-\((m+q_*)\) targets avoiding \(z\) is

\[
 B_{q_*}^{\bar z}
 =\binom{2m-1}{m+q_*}
 =\frac{m-q_*}{2m}N_{q_*}.
\tag{5.10}
\]

Since \(A_{q_*}\ge N_{q_*}-L\), support is at most
\(B_{q_*}^{\bar z}\), and therefore

\[
 \begin{aligned}
 e_{q_*,+}
 &\ge A_{q_*}-B_{q_*}^{\bar z}\\
 &\ge\frac{m+q_*}{2m}N_{q_*}-L\\
 &=(1/4-o(1))W.
 \end{aligned}
\tag{5.11}
\]

A top-disjoint packing has at most \(N_H/3\) packets. By Theorem 2.2,
one packet has at most \(2q_*\) positive upper cells and hence can enlarge
the occupied support by at most \(2q_*\). Thus the total possible support
gain is at most

\[
 \frac{2q_*N_H}{3}=O(W/\sqrt m)=o(W).
\tag{5.12}
\]

Subtracting (5.12) from (5.11) proves (5.9). \(\square\)

More generally, after any serial sequence of \(S\) owner-transported
conveyors,

\[
 \boxed{
 e_{q_*,+}^{\rm final}
 \ge (1/4-o(1))W-2q_*S.}
\tag{5.12a}
\]

Consequently, any serial repair of this state needs at least

\[
 \frac{(1/4-o(1))W}{2q_*}
 =\left(\frac1{8\sqrt{\log2}}-o(1)\right)\frac W{\sqrt m}
 =\left(\frac1{8\sqrt{\log2}}-o(1)\right)\sqrt m\,N_H
\tag{5.13}
\]

upper-active conveyor operations. Since every operation touches three
tops, the mean top participation is at least

\[
 \left(\frac3{8\sqrt{\log2}}-o(1)\right)\sqrt m.
\tag{5.14}
\]

This is a necessary condition, not a proof that such a highly overlapping
serial repair is impossible.

The direct lower targets in the same state may have additional repeats;
they only increase \(\Xi_\tau\). Every conveyor has zero middle damage,
so no hidden middle correction weakens (5.9).

### Corollary 5.3 (stronger profile constraints do not rescue one round)

If owner transport is required also to preserve the active count on every
top, then every path-uniform packet triple in the state above is either
monochromatic or illegal by Proposition 2.5(2). Hence a legal
top-disjoint packing has zero direct-upper action at \(q_*\).

If tags are instead held on their top positions, put
\(h_*=H-q_*\). Proposition 2.5(3) gives at most \(2h_*\) positive cells
per packet, so a top-disjoint packing gains support at most

\[
 \frac{2(H-q_*)N_H}{3}=O(HN_H)=o(W).
\tag{5.15}
\]

Thus the same linear repeat survives in that non-owner-transport model as
well. A serial positional repair needs at least

\[
 \left(\frac18-o(1)\right)\frac W{H-q_*}
 =\Omega(W/H)
\tag{5.16}
\]

operations, with mean top participation at least
\((3/8-o(1))m/H\). This comparison does not make position transport a
legal substitute for physical-owner transport; it only records its exact
statewise throughput.

## 6. A local energy-flat exterior

The kernel also has no uniform statewise charge.

### Proposition 6.1 (flat exterior)

For every nonzero active conveyor derivative \(\delta\), there is a
physical external load \(R\) such that

\[
 \langle R,\delta\rangle=0,
\tag{6.1}
\]

while both conveyor shores have exactly \(\|\delta\|_0/2\)
packet--external collision pairs on the changed cells.

#### Proof

Put one unit of external load on every target in
\(\operatorname{supp}\delta\). Since every conveyor derivative has equal
positive and negative mass,

\[
 \langle R,\delta\rangle=\sum_T\delta_T=0.
\]

This exterior is physically realizable one cell at a time. On the direct
lower side, use the \((H+1)\)-fresh-marker construction from the source
conveyor report to make a prescribed changed target the unique packet
derivative target of its exterior frame. On the direct upper side, adjoin
a fresh \((H-q)\)-set \(Z\), make \(Z\) consecutive, and use the top
\(U_e=T\dot\cup Z\), so \(T=U_e\setminus Z\). All other traces contain a
fresh marker and avoid the packet derivative support.

One common fresh marker reservoir, disjoint from the conveyor's coordinate
set, is reused for all changed cells. At a fixed signed depth all changed
targets have the same size; because the common reservoir is disjoint from
them, distinct targets give distinct exterior tops. Pairwise disjoint
fresh-label reservoirs are neither required nor asserted.

Indeed, the three conveyor tops use exactly \(M+1\) coordinates, leaving
\(m-H-1\) outside coordinates. The upper construction needs \(H-q\)
markers, and the lower construction needs \((H+1)+(q-1)=H+q\le2H\).
The standing hypothesis \(M\ge12H-4\) gives \(m-H-1\ge2H\) for all
sufficiently large \(H\), so the common reservoir exists.

The external middle occurrence budget is at most

\[
 M\|\delta\|_0,
\]

and is identical on the two shores. The two shores therefore have equal
energy despite a nonzero kernel. \(\square\)

This is a bounded local witness, not an \(\Omega(W)\) obstruction to a
globally correlated atlas. It rules out only a packetwise uniform strict
drift lemma.

## 7. Exact boundary

Proved:

1. an exact common-core clipping with zero middle damage;
2. the complete transported-tag upper and lower kernels, including the
   constants \(4q,20q,16q\);
3. the no-self-toll energy identity and local overlap constants;
4. the direct-upper load invariant for every composition that remains
   carrier-faithful at every step, together with a literal reversal bank
   whose tagged linear-\(\Xi\) realization is conditional on the already
   isolated middle-family and full-SCD tag-completion gates;
5. an integral floor-correct partial-census state, with aggregate deficit
   \(o(W)\), conditional on the separately prescribed owner-disjoint
   middle path family, and retaining linear repeat after every
   top-disjoint arbitrary owner-transported-tag conveyor packing;
6. the exact \((3/(8\sqrt{\log2})-o(1))\sqrt m\) average-participation
   requirement for any owner-transport serial escape from that state; and
7. a physical energy-flat exterior for every nonzero local kernel.

Not proved:

1. impossibility of a deeply overlapping serial conveyor process with
   \(\Omega(\sqrt m)\) uses per top;
2. a global packet-codegree or charged-coverage theorem;
3. completion of the local-reversal tag prescription inside one full
   SCD, beyond its exact scalar and partial-census feasibility;
4. the separate owner-disjoint common-core middle path factor required to
   instantiate Section 5, unless it is granted as the repaired-ring input;
5. completion of the concentrated state in Section 5 inside one full SCD;
6. a genuinely two-sided rank-\(M\) conveyor; or
7. the coefficient-one theorem.

The first failed implication is now exact:

\[
 \text{middle-perfect three-top conveyor}
 \not\Longrightarrow
 \text{aggregate active trace contraction}.
\]

The obstruction is not middle ownership, scalar tag capacity, or a
quadratic self-toll. It is the certified carrier's one-sidedness together
with only \(O(q)\) active edit throughput on its noncoherent extension.
