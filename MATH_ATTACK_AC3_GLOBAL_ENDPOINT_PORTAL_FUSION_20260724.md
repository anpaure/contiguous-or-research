# AC3: global endpoint portals, exact MTF packets, and the integral support gate

Date: 2026-07-24

## 0. Verdict

Put

\[
  2m=3s,\qquad
  W=\binom{2m}{m},\qquad
  W_s=\binom{s}{s/2},\qquad
  N_s=W_s^3,
\]

and let \(H=\lceil A\sqrt m\rceil\), with \(A>0\) fixed.  Fix arbitrary
SCDs in three disjoint \(s\)-coordinate blocks and use their Cartesian
products as the product-box partition of \(2^{[2m]}\).

The unbounded-degree endpoint route is real.  More precisely, the following
statements are proved below.

1.  A single radius-\(H\) complementary-geodesic packet has
    \(m-2H+1\) consecutive MTF state endpoints, exact word length \(m+2\),
    and a literal saturated \((2H+1)\)-mask suffix flag at every endpoint.
    One common coordinate permutation makes all but an \(O(H/m)\) fraction
    of those endpoint flags meet \(2H+1\) distinct SCD product boxes.

2.  Working integrally inside one frozen exact odd wreath factor, these
    packets concatenate to a literal middle-covering word of length

    \[
       \boxed{W+(2H+1)\operatorname{Cat}_m
       =W+O_A(W/\sqrt m).}
    \]

    It has \(W-o(W)\) explicit radius-\(H\) state endpoints, and after one
    common relabelling all but \(O_A(W/\sqrt m)\) of them are box-rainbow.
    Thus the arms are genuinely fused into a middle-productive global word;
    they are not an appended family of isolated portal blocks.

3.  The same construction gives \(\Omega(W)\) unconditional, globally
    distinct depth-one selected-target sharings.  These are honest masks,
    not merely repeated canonical occurrences or nonzero projections.

4.  Radius labels with the exact SCD multiplicities give a convex
    combination of literal exact-factor words which tiles every mask in the
    whole Gaussian band with weight exactly one.  Its cost is
    \(W+O_A(W/\sqrt m)\), and its weighted same-box collision loss is
    \(O_A(W/\sqrt m)\).  This is an exact fractional packet-fusion theorem
    whose every atom remains inside one exact factor.  The missing step is
    an integral two-sided nested resolution of the flags.

5.  The endpoint ledger gives the matching necessary scale.  A near-width
    universal band word needs \(\Omega(W/\sqrt s)\) physical multiply used
    endpoint positions.  If only \(O(\sqrt s)\) portal positions are
    available per product box, their one-sided degree must be
    \(\Theta(\sqrt s)\).  A separate exact packet-distance ledger shows
    that every packet fusing \(B\) residual-consuming seams has length at
    least \(2H+1\); if it attains this bound, every one of its letters is
    active in all \(B\) boxes.

6.  For a PTAD witness, the exact necessary coupling is

    \[
      (R-1)(C+I)+R\bigl(\mathfrak P_H+\Phi_Z(\mathcal H_H)\bigr)
      \ge \Gamma,
    \]

    with \(\Gamma=\Theta(sN_s)\) and \(R=\Theta(\sqrt s)\).  Conversely,
    if \(\mathrm{PTAD}_A\) holds, a common relabelling yields
    \(\Theta(W/\sqrt m)\) genuine state endpoints of average selected-box
    degree \(\Theta(\sqrt m)\).

The literal global portal mechanism is therefore constructed.  The
unproved positive gate is not chronology or endpoint degree; it is the
integral support/trace theorem

\[
  \Phi_Z(\mathcal H_H)=o(W),
\]

or the stronger two-sided nested flag resolution stated in Section 6.
No web search, finite search, or computation is used.

---

## 1. Literal endpoints versus projection shadows

For a physical Boolean word \(A_1,\ldots,A_n\), all suffix unions ending at
a fixed right endpoint \(j\) form the chain

\[
 A_j\subseteq A_{j-1}\cup A_j\subseteq\cdots\subseteq
 A_1\cup\cdots\cup A_j.
 \tag{1.1}
\]

The analogous assertion holds at a fixed left endpoint.  Hence:

### Lemma 1.1 — rank-chain endpoint cap

If all selected targets lie in \(R\) global ranks, then one oriented
physical endpoint represents targets in at most \(R\) product boxes.

#### Proof

Choose one represented target from every incident box.  Product boxes
partition Boolean masks, so the chosen targets are distinct.  By (1.1) they
form an inclusion chain, and a strict inclusion chain contains at most one
mask of each rank. \(\square\)

This immediately separates projection activity from literal service.  A
single coordinate can have nonzero SCD projection in exponentially many
boxes, but a central-band endpoint has literal degree only \(O(\sqrt m)\).

There is also a useful cap for intervals which merely contain, rather than
end at, one physical position.

### Lemma 1.2 — two-chain portal cap

Let the ground set have size \(K\), fix position \(j\), and let
\(\mathcal R\) be a set of ranks.  At most

\[
  (K+1)|\mathcal R|
  \tag{1.2}
\]

distinct masks of ranks in \(\mathcal R\) can be represented by intervals
containing \(j\).  If \(j\) is a fixed-side endpoint, the bound improves to
\(|\mathcal R|\).

#### Proof

For a left endpoint \(a\le j\) and right endpoint \(b\ge j\), write

\[
 C_a=A_j\cup\bigcup_{t=a}^{j-1}A_t,
 \qquad
 D_b=\bigcup_{t=j+1}^{b}A_t.
\]

After duplicate values are deleted, \((C_a)\) and \((D_b)\) are two
inclusion chains of length at most \(K+1\), and every interval containing
\(j\) has union \(C_a\cup D_b\).  At one rank, choose one pair \((a,b)\)
for every distinct union.  Comparable pairs give comparable unions, so
equal-rank distinct unions correspond to an antichain in a product of two
chains.  Projection to either coordinate is injective on such an antichain;
its size is at most \(K+1\).  Summing over ranks proves (1.2).  At a fixed
side only one cumulative chain remains. \(\square\)

Thus the only useful unbounded endpoint degree in a Gaussian band is the
maximal order \(\Theta(\sqrt m)\), not exponential projection degree.

---

## 2. An exact literal radius-\(d\) MTF packet

Pair the \(2m\) coordinates as

\[
  \{a_1,b_1,\ldots,a_m,b_m\}.
\]

For \(0\le d\le m/2\) and \(d\le t\le m-d\), put

\[
 S_t=\{b_1,\ldots,b_t,a_{t+1},\ldots,a_m\},
 \tag{2.1}
\]

\[
 L_t^{(d)}=
 \{b_1,\ldots,b_t,a_{t+d+1},\ldots,a_m\},
 \tag{2.2}
\]

and \(R_t=\{b_{t+1},\ldots,b_m\}\).  Empty ranges are omitted.  Notice

\[
 S_{t+1}=S_t-a_{t+1}+b_{t+1},
 \qquad
 L_{t+1}^{(d)}=L_t^{(d)}-a_{t+d+1}+b_{t+1}.
 \tag{2.3}
\]

### Theorem 2.1 — exact packet atom

The word

\[
 \boxed{
 R_d,\{a_1\},\{a_2\},\ldots,\{a_{2d}\},
 L_d^{(d)},L_{d+1}^{(d)},\ldots,L_{m-d}^{(d)}}
 \tag{2.4}
\]

has exact length \(m+2\).  At the occurrence of \(L_t^{(d)}\), its
last-occurrence ordered partition is

\[
 \Pi_t^{(d)}=
 \bigl(L_t^{(d)},
 \{a_{t+d}\},\{a_{t+d-1}\},\ldots,\{a_1\},R_t\bigr).
 \tag{2.5}
\]

Consequently that one physical endpoint literally represents the saturated
flag

\[
 F_{t,-d}\subset\cdots\subset F_{t,0}=S_t
 \subset\cdots\subset F_{t,d},
 \tag{2.6}
\]

where

\[
 F_{t,-q}=S_t\setminus\{a_{t+1},\ldots,a_{t+q}\},
 \quad 0\le q\le d,
 \tag{2.7}
\]

and

\[
 F_{t,q}=S_t\cup\{a_{t-q+1},\ldots,a_t\},
 \quad 0\le q\le d.
 \tag{2.8}
\]

The \(m-2d+1\) flags belonging to different \(t\)'s are pairwise disjoint
as families of masks.

#### Proof

The first \(2d+2\) letters through \(L_d^{(d)}\) are the reverse-block
initialization of

\[
 (L_d^{(d)},\{a_{2d}\},\ldots,\{a_1\},R_d).
\]

Assume (2.5) holds at \(t\).  Updating by \(L_{t+1}^{(d)}\) puts that set
first, leaves the singleton \(a_{t+d+1}\) from the old first block, leaves
the old \(a\)-singletons in their order, and deletes \(b_{t+1}\) from the
old residual.  This gives (2.5) at \(t+1\).  Induction proves the exact MTF
trajectory.

The first block has size \(m-d\).  Adding the next \(d\) singleton blocks
gives \(S_t\), and adding the following \(q\) singleton blocks gives
(2.8).  Every prefix of a last-occurrence partition is the union of a
literal suffix ending at the current physical position, proving (2.6).

All masks in the flag at \(t\) contain exactly
\(\{b_1,\ldots,b_t\}\) among the \(b\)-coordinates.  Thus flags at
different \(t\)'s are disjoint.  Finally,

\[
 1+2d+(m-2d+1)=m+2.
\]

\(\square\)

For \(d=H\), the packet has

\[
  L_H=m-2H+1
  \tag{2.9}
\]

middle owners and reset excess exactly \(2H+1\).

### Theorem 2.2 — one packet is almost completely box-rainbow

Assume \(5d+1<m\), and fix arbitrary three-block SCD product boxes.  For a
uniform coordinate
permutation, let a radius-\(d\) endpoint be bad when two masks in its flag
lie in one product box.  Put

\[
 \beta_{m,d}=
 \sum_{g=1}^{2d}(2d+1-g)
 \frac{\binom{g+2}{2}}{\binom{m-d}{g}}.
 \tag{2.10}
\]

Then the expected number of bad endpoints in the packet is at most
\(L_d\beta_{m,d}\).  With

\[
 q_d=\frac{2d+2}{m-3d+1},
\]

\[
 \boxed{
 \beta_{m,d}\le
 \frac{3(2d+1)}{(m-d)(1-q_d)}.}
 \tag{2.11}
\]

In particular, for \(d=O(\sqrt m)\), one common permutation makes all but
an \(O(d/m)\) fraction of the packet endpoints have literal degree
\(2d+1\) in distinct product boxes.

#### Proof

Two flag masks at rank distance \(g\) form a uniformly relabelled nested
pair.  Conditional on the lower image, the upper image is uniform among
its \(\binom{m-d}{g}\) or more \(g\)-step supersets.  In its product box,
a \(g\)-step extension is determined by the three nonnegative factor-chain
advances, so there are at most \(\binom{g+2}{2}\) possibilities.  There are
\(2d+1-g\) flag pairs at distance \(g\), which proves (2.10).

If

\[
 a_g=\frac{\binom{g+2}{2}}{\binom{m-d}{g}},
\]

then

\[
 \frac{a_{g+1}}{a_g}=\frac{g+3}{m-d-g}\le q_d
\]

through the relevant range, while \(a_1=3/(m-d)\).  Bounding the distance
multiplicity by \(2d+1\) gives (2.11).  Linearity of expectation over the
packet endpoints and averaging over permutations finish the proof.
\(\square\)

The wording is important: the bad set is an \(O(d/m)\) *fraction* of the
\(\Theta(m)\) endpoints, hence \(O(d)\) endpoints when \(d=O(\sqrt m)\).

---

## 3. Integral global fusion inside one exact factor

Let \(z\) be a new coordinate.  An exact middle wreath factor on
\([2m]\cup\{z\}\) has

\[
 C=\frac{\binom{2m+1}{m}}{2m+1}
 =\frac{W}{m+1}=\operatorname{Cat}_m
 \tag{3.1}
\]

wreath rows.  Rotate and orient one row as

\[
  (z,a_1,\ldots,a_m,b_1,\ldots,b_m).
 \tag{3.2}
\]

Its \(m+1\) length-\(m\) intervals avoiding \(z\) are exactly the sets
\(S_0,\ldots,S_m\) from (2.1).  Across all rows these paths partition the
whole middle layer of \([2m]\), because the exact factor covers every
\(m\)-set avoiding \(z\) exactly once.

### Theorem 3.1 — literal global middle word with high-degree endpoints

Assume \(0\le H\le m/2\).  On every exact-factor path retain the states
\(S_H,\ldots,S_{m-H}\), encode them by the radius-\(H\) word (2.4), and
concatenate all \(C\) packet words.  Append the \(2HC\) discarded middle
masks as one-letter words.  The result is a literal nonzero word of exact
length

\[
 \boxed{
 C(m+2)+2HC
 =W+(2H+1)C.}
 \tag{3.3}
\]

It covers every middle mask and has

\[
 \boxed{W-2HC}
 \tag{3.4}
\]

radius-\(H\) state endpoints.  If \(H=A\sqrt m+O(1)\), one common
permutation of the \(2m\) unmarked coordinates makes all but

\[
 O_A(W/\sqrt m)
 \tag{3.5}
\]

of these endpoints meet \(2H+1\) distinct fixed product boxes.

#### Proof

Equations (3.1)--(3.2) prove the integral path partition.  Theorem 2.1
gives each retained packet word and all its literal interval certificates.
Independent reverse-block initializations erase the preceding MTF state, so
concatenation creates no state-compatibility condition.  The retained and
discarded centers partition the middle layer, proving coverage.  The length
and endpoint count are (3.3)--(3.4).

Apply one uniform permutation simultaneously to the entire exact factor,
fixing \(z\).  By Theorem 2.2, the expected total same-box pair count over
all retained flags is at most

\[
  (W-2HC)\beta_{m,H}=O_A(WH/m).
\]

Some permutation attains this bound.  Every bad flag contributes at least
one pair, proving (3.5). \(\square\)

Thus a literal \(W+o(W)\) middle word can have \(W-o(W)\) maximum-degree
Gaussian-band endpoint flags.  This is stronger than merely constructing
\(W/H\) isolated portal blocks.

### Theorem 3.2 — unconditional honest selected sharing at depth one

Use one orientation of the dominant height windows

\[
 p,q\in[\sqrt s,1.1\sqrt s],
 \qquad r\in[3\sqrt s,3.1\sqrt s],
 \tag{3.6}
\]

and select their full plateaux.  Put

\[
 \kappa_L=e^{-1/2}-e^{-121/200},
 \qquad
 \kappa_H=e^{-9/2}-e^{-961/200},
 \qquad
 \kappa=\kappa_L^2\kappa_H,
 \tag{3.7}
\]

and choose any fixed

\[
 0<\alpha<\frac{2\sqrt3}{\pi}\kappa.
 \tag{3.8}
\]

For all sufficiently large \(s\), some common relabelling of the word in
Theorem 3.1 has at least \(\alpha W/4\) endpoints which simultaneously
represent:

* a globally distinct middle target;
* a globally distinct rank-\((m+1)\) target in a selected dominant
  plateau; and
* those two targets in distinct product boxes.

The same relabelling has only \(O_A(WH/m)\) non-rainbow full flags.

#### Proof

The number of boxes in (3.6) is

\[
 (\kappa+o(1))N_s.
\]

Every plateau rank has at least \(s\) masks, and

\[
 \frac{sN_s}{W}\longrightarrow\frac{2\sqrt3}{\pi}.
\]

Hence at least \(\alpha W\) rank-\((m+1)\) masks lie in the selected
plateaux.

Choose the upper depth-one order in Theorem 2.1 as in (2.8).  At an internal
center \(S_t\), the upper depth-one mask is

\[
 U_t=S_t\cup\{a_t\}=S_{t-1}\cup S_t.
 \tag{3.9}
\]

Across the exact factor, all such edge unions are globally distinct.  One
direct proof is to take complements in \([2m]\cup\{z\}\): the complements
of the \(m\)-intervals containing \(z\) are precisely the \((m+1)\)-edge
unions, and exactness partitions the former family.

Let \(I=W-2HC\) be the retained endpoint count, and let \(G(\sigma)\)
count retained endpoints whose upper mask lands in the selected family and
whose middle and upper masks lie in different boxes.  A fixed upper mask is
uniform in rank \(m+1\).  Conditional on it, at most three of its \(m+1\)
lower neighbours lie in its product box.  Therefore

\[
 \mathbb E G\ge
 I\left(\frac{\alpha W}{\binom{2m}{m+1}}-rac3{m+1}\right)
 \ge \frac{\alpha W}{2}
 \tag{3.10}
\]

for large \(m\).

Let \(D(\sigma)\) be the total same-box pair count over all full flags.
For large \(m\), Theorem 2.2 gives

\[
 \mathbb E D\le 8HW/m.
\]

Set \(\lambda=\alpha m/(32H)\).  Then

\[
 \mathbb E(G-\lambda D)\ge\alpha W/4.
\]

Choose a permutation attaining the expectation.  It has
\(G\ge\alpha W/4\); since \(G\le W\), it also has

\[
 D\le \frac{32H}{\alpha m}W.
\]

The distinctness of the middle and upper target families is preserved by
relabelling. \(\square\)

This is honest distinct-target endpoint sharing.  It does not assert that
all deeper canonical masks are globally distinct.

---

## 4. Exact projected-state packet fusion

The product-box projection is a range maximum, not ordinary coordinate
restriction.  The correct simultaneous-state criterion is therefore a
max-plus timestamp theorem.

Let a factor SCD chain be

\[
 C_0\subset C_1\subset\cdots\subset C_p,
 \qquad C_t=C_0\cup\{e_1^C,\ldots,e_t^C\}.
\]

For a physical mask \(X\),

\[
 \pi_C(X)=\max(\{t:e_t^C\in X\}\cup\{0\}).
 \tag{4.1}
\]

Identifying height \(f\) with the prefix ideal
\(I_C(f)=\{e_1^C,\ldots,e_f^C\}\), the projection is a union
homomorphism.

For a packet \(X_1,\ldots,X_p\), define

\[
 \tau(x)=\max\{j:x\in X_j\}
\]

with value zero if \(x\) never occurs.  The induced local last-occurrence
profile is

\[
 \eta_C(t)=\max_{u\ge t}\tau(e_u^C).
 \tag{4.2}
\]

### Theorem 4.1 — forced-descent max-plus amalgamation

Prescribe a nonincreasing nonnegative integer profile

\[
 \eta_C(1)\ge\cdots\ge\eta_C(p_C)\ge0,
 \qquad \eta_C(p_C+1)=0,
\]

on every chain occurring in a selected family of product boxes.  One
physical timestamp map \(\tau\) realizes all profiles by (4.2) if and only
if:

1. whenever \(\eta_C(t)>\eta_C(t+1)\), the coordinate \(e_t^C\) is forced
   to timestamp \(\eta_C(t)\), and all demands forcing the same physical
   coordinate agree;
2. if a coordinate \(x\) is forced to value \(a(x)\), then at every
   occurrence \(x=e_u^D\) on every selected chain \(D\),

   \[
     a(x)\le\eta_D(u).
     \tag{4.3}
   \]

When these conditions hold, it is enough to set \(\tau(x)=a(x)\) on forced
coordinates and \(\tau(x)=0\) elsewhere.  After deletion-tail compatibility
with the source local states is imposed, this is an exact simultaneous MTF
reset theorem.  For prescribed target states, rather than prescribed
numeric timestamp labels, the shortest packet is the least number of
distinct positive levels over all representing profiles which satisfy both
the forced-descent conditions and the deletion-tail identities.  After
unused levels are order-compressed, the literal packet is

\[
 X_t=\{x:\tau(x)=t\}.
\]

#### Proof

The recurrence

\[
 \eta_C(t)=\max\{\tau(e_t^C),\eta_C(t+1)\}
 \tag{4.4}
\]

shows that every strict descent forces the displayed timestamp, and every
occurrence of a forced coordinate lies in the tail defining (4.3).  This
proves necessity.

For sufficiency, fix \(C,t\).  Condition (4.3) bounds every forced
timestamp in the tail by \(\eta_C(t)\).  If this value is positive, let
\(r\ge t\) be the last index of its constant plateau.  The strict descent at
\(r\) forces \(\tau(e_r^C)=\eta_C(t)\), so the tail maximum is exactly the
prescribed value.  The zero case is immediate.  Grouping local coordinates
by equal positive last-occurrence time and then appending the untouched
source residual gives the terminal local MTF state. \(\square\)

For one common update with desired factor cutoffs \(f_C\), every positive
cutoff forces the frontier coordinate \(e_{f_C}^C\) into the update.  A
forced coordinate occurring at index \(u\) of another selected chain may
not overshoot its cutoff: \(u\le f_D\).  This is an exact labelled
compatibility test.

It is strictly stronger than unlabelled overload control and is only a
sufficient architecture for arbitrary literal OR words.  No common-owner
synchronization is inferred from MWB.

---

## 5. Exact fractional band resolution inside literal exact-factor words

The full complementary geodesics are \(H\)-legal: no inserted coordinate is
later removed.  The audited adaptive-MTF lift therefore gives, at all \(W\)
middle owners of the exact odd factor, literal canonical flags

\[
 F_{v,-H}\subset\cdots\subset F_{v,0}\subset\cdots\subset F_{v,H}
 \tag{5.1}
\]

in a word of exact length

\[
 W+(2H+1)C.
 \tag{5.2}
\]

The self-contained atom of Section 2 independently verifies this lift away
from the two path boundaries.  The full-path endpoint padding is the
already audited adaptive-MTF theorem, not a new unproved lemma here.

Put

\[
 N_d=\binom{2m}{m-d},
\]

and define

\[
 c_d=N_d-N_{d+1}\quad(0\le d<H),
 \qquad c_H=N_H.
 \tag{5.3}
\]

Then

\[
 \sum_{d=q}^Hc_d=N_q,
 \qquad
 \sum_{d=0}^Hc_d=W.
 \tag{5.4}
\]

Assign a radius label \(d(v)\in\{0,\ldots,H\}\) to the \(W\) state
endpoints, using exactly \(c_d\) labels of value \(d\), and designate only
the subflag \(|q|\le d(v)\) at endpoint \(v\).

### Theorem 5.1 — exact fractional literal-word tiling

Average the resulting literal exact-factor word over all coordinate
permutations.  Every Boolean mask in every rank

\[
 m-H,\ldots,m+H
\]

has total designated occurrence weight exactly one.  Every word in the
mixture has length (5.2).  The total endpoint-degree mass is exactly

\[
 \boxed{
 \sum_{d=0}^H(2d+1)c_d
 =W+2\sum_{q=1}^HN_q,}
 \tag{5.5}
\]

the cardinality of the whole band.  Relative to any fixed three-block
product partition, the weighted same-box collision loss is

\[
 O_A(HW/m)=O_A(W/\sqrt m).
 \tag{5.6}
\]

#### Proof

At rank \(m\pm q\), the number of designated occurrences in every labelled
word is

\[
 \sum_{d=q}^Hc_d=N_q.
\]

Under a uniform coordinate permutation, each fixed occurrence is uniform in
that rank.  Thus every rank target has expected multiplicity
\(N_q/N_q=1\), proving the exact fractional tiling.  Every atom of the
mixture is the same literal exact-factor word, merely relabelled; no signed
or cross-factor interpolation is used.

Abel summation gives

\[
 \sum_{d=0}^Hd,c_d=\sum_{q=1}^HN_q,
\]

which proves (5.5).  Finally, a radius-\(d\) flag has expected same-box pair
count at most \(\beta_{m,d}\).  Hence total weighted collision is at most

\[
 \sum_{d=0}^Hc_d\beta_{m,d}
 \le
 \frac{9}{(m-H)(1-q_H)}\sum_{q=1}^HN_q
 =O_A(HW/m).
\]

\(\square\)

This theorem is stronger than an abstract LP solution: each support point
of the convex combination is a literal word built from one exact factor.
Clearing denominators produces a large exact multicover, not a
coefficient-one word, so it does not complete the problem.

### The exact integral resolution gate

For \(1\le q\le H\), let

\[
 E_q=\{v:d(v)\ge q\}.
\]

The radius labels are nested and \(|E_q|=N_q\).  Because the domain and
target rank have equal size, the designated flags cover the whole band
without repetitions if and only if, simultaneously for every \(q\), both

\[
 v\longmapsto F_{v,-q}\quad(v\in E_q)
 \tag{5.7}
\]

and

\[
 v\longmapsto F_{v,q}\quad(v\in E_q)
 \tag{5.8}
\]

are bijections onto ranks \(m-q\) and \(m+q\), respectively.

Call (5.7)--(5.8) the **two-sided nested resolution theorem**
\(\mathrm{TNR}_A\).  It is unproved.  If it holds for one exact factor,
then (5.2) is already a literal full-band word with no trace holes.  The
fractional theorem proves that the rankwise marginals and the portal cost are
exact; it does not prove this integral simultaneous resolution.  This is
the precise semigroup/rounding gap.

---

## 6. Exact endpoint and packet lower bounds

Use all three orientations of the dominant windows (3.6).  For one such
box \(\mathcal B\), let its chain heights be \(p,q,r\), with \(r>p+q\),
and put

\[
 \Delta_{\mathcal B}=r-p-q,
 \qquad
 w_{\mathcal B}=(p+1)(q+1).
\]

The window inequalities give

\[
 0.8\sqrt s\le\Delta_{\mathcal B}\le1.1\sqrt s,
 \qquad
 \frac{\Delta_{\mathcal B}}r\ge\frac4{15},
 \qquad
 w_{\mathcal B}\ge s.
 \tag{6.1}
\]

Let

\[
 G_s=\sum_{\mathcal B}
 \left\lceil\frac{w_{\mathcal B}\Delta_{\mathcal B}}{r_{\mathcal B}}
 \right\rceil,
 \qquad
 \Delta_*=\max_{\mathcal B}\Delta_{\mathcal B}.
 \tag{6.2}
\]

There are \((3\kappa+o(1))N_s\) such boxes, so

\[
 \boxed{
 G_s\ge\left(\frac45\kappa-o(1)\right)sN_s,}
 \qquad
 \Delta_*\le(1.1+o(1))\sqrt s.
 \tag{6.3}
\]

Select every plateau target in these boxes and only the local middle layer
in all other boxes.

### Theorem 6.1 — endpoint Pareto frontier

Let a word of length \(W+E\) cover the selected targets.  Choose one
witness for every target, and let \(\ell_j,r_j\) be the numbers of selected
boxes using physical position \(j\) as a left or right endpoint.  Then

\[
 \boxed{
 \sum_j\bigl((\ell_j-1)_++(r_j-1)_+\bigr)
 \ge G_s-2E.}
 \tag{6.4}
\]

Moreover,

\[
 \ell_j,r_j\le\Delta_*+1.
 \tag{6.5}
\]

If \(P_s\) physical positions have \(\ell_j\ge2\) or \(r_j\ge2\), then

\[
 \boxed{
 P_s\ge
 \left\lceil\frac{(G_s-2E)_+}{2\Delta_*}\right\rceil.}
 \tag{6.6}
\]

For \(E=o(W)\),

\[
 \boxed{
 P_s\ge
 \left(\frac{8\sqrt3}{11\pi}\kappa-o(1)\right)
 \frac{W}{\sqrt s}.}
 \tag{6.7}
\]

#### Proof

The audited two-endpoint plateau theorem gives, in every dominant box,

\[
 (C_L-w_{\mathcal B})+(C_R-w_{\mathcal B})
 \ge
 \left\lceil\frac{w_{\mathcal B}\Delta_{\mathcal B}}{r_{\mathcal B}}
 \right\rceil.
\]

All other boxes contribute at least their local width to both endpoint
counts.  Since the product-box middle widths sum to \(W\), total
endpoint--box incidence is at least \(2W+G_s\).

On the other hand,

\[
 \sum_j\ell_j\le W+E+\sum_j(\ell_j-1)_+,
\]

and similarly on the right.  This proves (6.4).  All selected targets lie
in \(\Delta_*+1\) ranks, so Lemma 1.1 proves (6.5).  One physical position
contributes at most \(2\Delta_*\) to (6.4), proving (6.6).  Finally use
(6.3) and

\[
 \frac{sN_s}{W}\longrightarrow\frac{2\sqrt3}{\pi}.
\]

\(\square\)

### Corollary 6.2 — minimum portal degree at corridor scale

Suppose all endpoint sharing is confined to at most \(u_sN_s\) physical
positions, and every oriented portal has degree at most \(K_s\).  The exact
inequality is

\[
 u_s\bigl(\min\{K_s,\Delta_*+1\}-1\bigr)
 \ge \frac{(G_s-2E)_+}{2N_s}.
 \tag{6.8a}
\]

If \(E=o(W)\), this becomes

\[
 \boxed{
 u_s\bigl(\min\{K_s,\Delta_*+1\}-1\bigr)
 \ge
 \left(\frac25\kappa-o(1)\right)s.}
 \tag{6.8}
\]

In particular:

* unlimited degree still requires \(u_s=\Omega(\sqrt s)\);
* if \(u_s=a\sqrt s\) and \(K_s=b\sqrt s\), then

  \[
    a\min\{b,1.1\}\ge\frac25\kappa;
    \tag{6.9}
  \]

* if \(K_s=o(\sqrt s)\), then \(u_sK_s=\Omega(s)\).

Thus the sharp architecture has \(\Theta(W/\sqrt s)\) physical portals of
degree \(\Theta(\sqrt s)\).  The construction in Section 3 realizes this
degree and supplies more than the required number of occurrence portals;
it is not claimed there to satisfy the universal deep-support hypothesis
under which the lower bound is invoked.

For a partition of all \(N_s\) product boxes into packets of sizes
\(b_\alpha\), so that \(\sum_\alpha b_\alpha=N_s\), suppose there are at most
\(u_sb_\alpha\) portal positions in packet \(\alpha\), and no cross-packet
portal.  Then the same proof gives

\[
 u_s\sum_\alpha b_\alpha
 \bigl(\min\{b_\alpha,\Delta_*+1\}-1\bigr)
 \ge \frac{G_s-2E}{2}.
 \tag{6.10}
\]

If every \(b_\alpha\le\Delta_*+1\), then

\[
 \frac1{N_s}\sum_\alpha b_\alpha^2
 \ge
 1+\frac{G_s-2E}{2u_sN_s}.
 \tag{6.11}
\]

This is the minimum packet second-moment requirement.

---

## 7. Coupling the endpoint demand to \(\mathrm{PTAD}_A\)

Let an adaptive-MTF system have \(C\) path pieces.  If \(b_j\) is the
exact nonempty MTF bridge distance at seam \(j\), put

\[
 \mathfrak P_H=(2H+1)+\sum_{j=1}^{C-1}(b_j-1).
 \tag{7.1}
\]

The initialization and all bridges occupy exactly

\[
 C+\mathfrak P_H
 \tag{7.2}
\]

physical positions, of which \(C\) are the initial state endpoints of the
pieces and \(\mathfrak P_H\) are non-owner excess positions.  Let the
actual trace repair use \(F\le\Phi_Z(\mathcal H_H)\) positions, and let
\(I\) count the actual internal middle-owner positions for which
\(y_j=(\max\{\ell_j,r_j\}-1)_+>0\).

Set

\[
 R=\Delta_*+1,
 \qquad
 \Gamma=G_s/2.
\]

### Theorem 7.1 — exact PTAD endpoint-capacity inequality

Every such construction which covers the selected targets satisfies

\[
 \boxed{
 (R-1)(C+I)+R\bigl(\mathfrak P_H+\Phi_Z(\mathcal H_H)\bigr)
 \ge \Gamma.}
 \tag{7.3}
\]

#### Proof

Put

\[
 y_j=(\max\{\ell_j,r_j\}-1)_+.
\]

Since

\[
 (\ell_j-1)_++(r_j-1)_+\le2y_j,
\]

Theorem 6.1 and the word excess \(E=\mathfrak P_H+F\) give

\[
 \sum_jy_j\ge\Gamma-(\mathfrak P_H+F).
 \tag{7.4}
\]

Every \(y_j\le R-1\).  All positions with positive \(y_j\) belong to the
\(C\) path starts, the \(I\) actual internal portals, the
\(\mathfrak P_H\) initialization/bridge excess positions, or the \(F\)
repair positions.  Hence

\[
 (R-1)(C+I+\mathfrak P_H+F)
 \ge\Gamma-(\mathfrak P_H+F).
\]

Rearrange and use \(F\le\Phi_Z\). \(\square\)

For the explicit windows, assume in addition that the PTAD band contains
their full plateaux.  Up to the harmless integer rounding at finite \(s\),
this is equivalent, for all sufficiently large \(s\), to

\[
 A\sqrt6>1.1.
 \tag{7.5a}
\]

If \(C=O(N_s)\) and internal positions are not used as portals, (7.3)
then forces

\[
 \mathfrak P_H+\Phi_Z(\mathcal H_H)
 \ge
 \left(\frac{4\kappa}{11}-o(1)\right)N_s\sqrt s.
 \tag{7.5}
\]

If \(\Phi_Z=o(N_s\sqrt s)\), then the same lower bound holds for the bridge
excess.  Since \(b_j-1\le2H+1=(A\sqrt6+o(1))\sqrt s\), a positive density
of \(\Omega(N_s)\) seams must have nonzero bridge excess.  Conversely, if

\[
 \mathfrak P_H+\Phi_Z=o(N_s\sqrt s),
\]

then

\[
 I\ge\left(\frac{4\kappa}{11}-o(1)\right)N_s\sqrt s.
\tag{7.6}
\]

For arbitrary fixed \(A>0\), the same statements hold with a narrower
positive-density dominant family.  Let \(X,Y,Z\) be independent Rayleigh
variables with density \(xe^{-x^2/2}\), and for \(L>0\) put

\[
 \psi(L)=\frac32\,
 \mathbb E\!\left[
 \frac{XY(Z-X-Y)}Z
 \mathbf 1_{\{0<Z-X-Y\le L\}}
 \right].
 \tag{7.7}
\]

Selecting all uniquely dominant boxes with
\(0<\Delta_{\mathcal B}\le L\sqrt s\) gives

\[
 \Gamma_L=(\psi(L)+o(1))sN_s,
 \qquad R_L\le L\sqrt s+1.
\tag{7.8}
\]

Indeed, the exact SCD height histogram, normalized by \(\sqrt s\), converges
with all fixed polynomial moments to the Rayleigh density.  For one labelled
choice of the long coordinate, one box contributes asymptotically

\[
 \frac{s}{2}\frac{XY(Z-X-Y)}Z
 \mathbf 1_{\{0<Z-X-Y\le L\}}
\]

to \(\Gamma_L\); summing the three possible long-coordinate labels gives the
factor \(3/2\) in (7.7).  Rayleigh tails give the required uniform
integrability.  The integrand is positive on a set of positive measure for
every \(L>0\), so \(\psi(L)>0\).  This proves (7.8), rather than assuming it
as an additional lemma.

Every \(0<L<A\sqrt6\) fits inside the PTAD band.  Hence (7.5)--(7.6)
remain valid with \(4\kappa/11\) replaced by
\(\psi(L)/L\), and the best flat-plateau constant is

\[
 \Xi_A=\sup_{0<L<A\sqrt6}\frac{\psi(L)}L>0.
 \tag{7.9}
\]

Thus a PTAD construction cannot hide all sharing in a tiny seam/reset pool;
many internal states must themselves be portals unless the Hamilton or
trace term pays the same surface-order cost.

There is also a converse capacity statement.

### Theorem 7.2 — PTAD produces genuine high-degree portals

Assume \(\mathrm{PTAD}_A\).  Put

\[
 h=\min\left\{H,\left\lfloor\frac{\sqrt s}{4}\right\rfloor\right\}.
\]

Relative to any fixed product-box partition, one common relabelling of the
PTAD word has a set of

\[
 \Theta_A(W/h)=\Theta_A(W/\sqrt m)
\]

state endpoints carrying \(\Omega_A(W)\) globally distinct selected-target
box incidences.  Their average degree is \(\Theta_A(h)\).

#### Proof

The trace sandwich gives at most \(\Phi_Z=o(W)\) holes in each signed rank,
so the total number of holes in the shallow \(2h\)-rank band is \(o(hW)\).
Since every such rank has \(\Theta_A(W)\) masks, the distinct canonical
support in this shallow band has size \(\Theta_A(hW)\).  Choose one state
occurrence for every distinct supported mask.

Every dominant box in (3.6) has plateau excess at least \(0.8\sqrt s\), so
all ranks within \(h\) of the middle lie in its plateau.  At every such
rank, a fixed positive fraction of masks is selected.  A uniform common
relabeling therefore gives expected selected representative mass
\(\Theta_A(hW)\).  The collision estimate of Theorem 2.2 gives only
\(O_A(HW/m)=o(W)\) expected same-box loss.  Hence some relabelling has
\(\Theta_A(hW)\) distinct representative endpoint--box incidences.

Take the \(\lceil W/h\rceil\) endpoints of largest representative degree.
Their total degree is at least their fraction of the global degree, namely
\(\Omega_A(W)\).  Each degree is at most \(2h+1\), so the average is
\(\Theta_A(h)\), and a positive proportion have degree
\(\Omega_A(h)\).  Relabelling preserves bridge distances, \(\mathfrak P_H\),
and \(\Phi_Z\). \(\square\)

This theorem is conditional on PTAD support.  The unconditional word in
Section 3 gives occurrence portals and honest depth-one support, but does
not prove deep rank surjectivity.

---

## 8. Exact reset-packet degree and the minimal-state obstruction

Let one physical packet \(X_1,\ldots,X_p\) be projected into a family of
local boxes.  Let \(a_b\) be the number of nonzero projected letters seen
by box \(b\), let

\[
 d_j=\#\{b:\pi_b(X_j)\ne0\},
\]

and let \(r_b\) be the exact nonempty MTF bridge distance from the old local
state to the prescribed new state.

### Theorem 8.1 — packet activity-distance ledger

\[
 \boxed{
 \sum_{j=1}^pd_j=\sum_ba_b\ge\sum_br_b.}
 \tag{8.1}
\]

Consequently,

\[
 \boxed{
 p\ge\max_br_b,
 \qquad
 \max_jd_j\ge
 \left\lceil\frac{\sum_br_b}{p}\right\rceil.}
 \tag{8.2}
\]

If \(B\) active boxes all have \(r_b\ge r\) and \(p=r+e\), then

\[
 \sum_{j=1}^p(B-d_j)\le Be.
 \tag{8.3}
\]

#### Proof

The equality double-counts nonzero packet-letter--box projections.  After
zero local letters are deleted, box \(b\) sees a bridge of length \(a_b\),
so \(a_b\ge r_b\).  The remaining assertions are averaging and
rearrangement. \(\square\)

For a local product box \(b\) with chain-height sum \(2m_b\), suppose the
source is a residual-consuming radius-\(H\) canonical terminal state, the
target is a fresh exact canonical state, and \(m_b-H\ge2\).  The audited
exact bridge metric then gives \(r_b\ge2H+1\).  Hence a packet fusing \(B\)
such seams has length at least \(2H+1\); at equality, every one of its
letters has activity degree exactly \(B\).  With excess \(e\), all but at
most \(e/\varepsilon\) letters have degree at least
\((1-\varepsilon)B\).

There is a complementary structural obstruction for minimal band states.

### Theorem 8.2 — top-prefix invariance of minimal states

Let \(1\le H\le m-2\) and

\[
 \Pi=(L,\{u_1\},\ldots,\{u_{2H}\},R),
 \qquad |L|=|R|=m-H.
\]

A non-idempotent one-update transition to another state of the same form is
possible if and only if, for some \(p\in L\) and \(j\in[2H]\),

\[
 L'=L-p+u_j,
 \tag{8.4}
\]

the new singleton order is

\[
 (p,u_1,\ldots,\widehat{u_j},\ldots,u_{2H}),
 \tag{8.5}
\]

and \(R'=R\).  Therefore the rank-\((m+H)\) prefix

\[
 L\cup\{u_1,\ldots,u_{2H}\}=[2m]\setminus R
 \tag{8.6}
\]

is invariant along every walk staying in the minimal-state class.

#### Proof

The target first block forces the update mask to be \(L'\).  If the state
changes, the first residual block \(L\setminus L'\) must be a singleton, so
\(L'=L-p+q\).  If \(q\in R\), the old \(2H\) singleton blocks all survive,
the new singleton \(p\) is prepended, and the residual shrinks to
\(R-q\).  This cannot equal a target having exactly \(2H\) singleton blocks
and a final block of size \(m-H\).  Hence \(q=u_j\), which forces (8.5)
and leaves \(R\) unchanged.  The converse follows by direct application of
the MTF update. \(\square\)

Thus minimal \((2H+2)\)-block states cannot tour the global upper band.
The literal packets in Sections 2--3 escape precisely by allowing the tail
to fragment after residual arrivals; no contradiction is present.

For completeness, fully split tails give another exact escape.  If

\[
 \widehat\Pi=(L,\{u_1\},\ldots,\{u_{m+H}\}),
 \qquad |L|=m-H,
\]

then all non-idempotent one-update successors are exactly

\[
 L'=L-p+u_j,
 \qquad
 (u'_1,\ldots,u'_{m+H})
 =(p,u_1,\ldots,\widehat{u_j},\ldots,u_{m+H}).
 \tag{8.7}
\]

A \(K\)-state sequence of such successors is realized by one reverse
initialization followed by the \(K-1\) new cores, with exact length

\[
 K+m+H.
 \tag{8.8}
\]

It exposes a literal radius-\(H\) suffix flag at every state.  A
\(W\)-state fully split rotor transversal with small support holes would
therefore be sufficient, but constructing that transversal is unproved.
Using \(C\) independently initialized fully split components costs
\((m+H)C\) initialization entries, so this escape is economical only when
\(C=o(W/m)\) unless the full tails themselves are fused.
The odd-factor packets already give the required occurrence chronology at
smaller reset cost; their remaining issue is support, not state existence.

---

## 9. Independent audit and exact remaining scope

The decisive steps were independently reconstructed.  The corrections
which matter are these.

1.  The collision statement is an \(O(H/m)\) *fraction* of bad packet
    endpoints, not \(O(H/m)\) endpoints as an absolute count.

2.  In a fractional construction made from full radius-\(d\) atoms, the
    correct orbit weight is \(c_d/(m-2d+1)\).  A common denominator is valid
    only after all paths are deliberately truncated to a common endpoint
    count.  Section 5 avoids this issue by radius-labelling the \(W\) states
    of one global exact-factor word.

3.  A good coordinate permutation controls within-flag product-box
    collisions.  It does not change whether two canonical occurrences at
    different state endpoints are the same Boolean mask.  Box-rainbow
    occurrence portals therefore do not imply deep support surjectivity.

4.  The exact odd factor supplies an integral partition of the middle
    layer into complementary geodesics.  Hence generic packet packing is
    not the center-level obstruction.  The remaining integrality is the
    simultaneous two-sided rank resolution (5.7)--(5.8).

5.  The max-plus common-owner theorem is labelled and architecture-scoped.
    It is sufficient for one projected reset packet and strictly stronger
    than unlabelled overload.  It is not promoted to a necessary condition
    for arbitrary literal OR words.

6.  Endpoint degree, projected-letter activity degree, and canonical
    occurrence multiplicity are three different quantities.  The report
    never substitutes one for another.

The proved conclusion is therefore

\[
 \boxed{
 \begin{gathered}
 \text{A literal integral global MTF word with }W-o(W)
 \text{ maximum-degree SCD-box endpoints exists;}\\
 \text{the exact-factor ensemble has a coefficient-one fractional band
 resolution;}\\
 \text{the universal coefficient-one gap is the integral support/trace
 resolution, not portal chronology.}
 \end{gathered}}
\]

The two clean remaining positive targets are:

* prove \(\mathrm{TNR}_A\) inside one exact factor; or
* prove the weaker joint PTAD estimate

  \[
    \mathfrak P_H+\Phi_Z(\mathcal H_H)=o(W).
  \]

For the exact odd-factor chronology the portal term is already
\((2H+1)W/(m+1)=o(W)\).  Only the support/trace term remains.
