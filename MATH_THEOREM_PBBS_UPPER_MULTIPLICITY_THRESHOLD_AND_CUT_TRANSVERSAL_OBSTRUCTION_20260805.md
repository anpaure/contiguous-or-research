# PBBS upper multiplicity: the Gaussian capacity threshold and the exact cut-transversal obstruction

**Date:** 2026-08-05  
**Method:** pure PBBS occurrence counting and cyclic-interval mathematics; no computation or search  
**Status:** unconditional quantitative theorem and proof-safe obstruction.  It identifies the sharp scalar depth at which two occurrences per target first become possible, proves that the current synchronized ledger does not imply even two occurrences, and gives the exact componentwise cut-transversal condition needed by a bounded-degree connector.  It does not prove that the PBBS occurrence families satisfy that condition.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad
 W={n\choose m},
 \qquad
 N_q={n\choose m-q}
 \quad(1\le q\le m).
\]

A correct `q`-edge PBBS fan with lower intersection `S`, `|S|=m-q`, is the complementary occurrence of the upper target

\[
                         U=[n]\setminus S,
 \qquad |U|=m+q+1.                                      \tag{0.1}
\]

Let `mu_q(U)` be the number of all based correct PBBS occurrences of `U`.  Complete support and the fact that there are only `W` based middle states give

\[
 1\le \mu_q(U),
 \qquad
 \sum_U\mu_q(U)\le W.                                  \tag{0.2}
\]

The exact scalar doubling threshold is

\[
 q_2(m):=\min\{q:W\ge2N_q\}
        =\sqrt{m\log2}+O(1).                            \tag{0.3}
\]

Below this threshold PBBS itself necessarily has singleton upper targets.  More precisely, if `s_q` is the number of targets with `mu_q(U)=1`, then

\[
 \boxed{s_q\ge(2N_q-W)_+.}                              \tag{0.4}
\]

Thus, for `q=(c+o(1))sqrt(m)` with `c<sqrt(log 2)`, a positive fraction at least

\[
                         2-e^{c^2}+o(1)                 \tag{0.5}
\]

of all upper targets are singleton.

For the word deadline in odd dimension `k=2m+1`,

\[
 d(k)={\sqrt\pi\over2}\sqrt m+O(1),
 \qquad
 {W\over N_{d(k)}}\longrightarrow e^{\pi/4}=2.19328\ldots. \tag{0.6}
\]

So a resident protection band through depth `d(k)` does pass the scalar doubling threshold.  This is the positive part of the proposed shallow/deep hybrid.

The negative part is decisive: at the first unprotected Gaussian depths the average multiplicity is still only a constant.  At depth `d(k)+O(1)`, at least

\[
 \left({3-e^{\pi/4}\over2}-o(1)\right)N_q
 = (0.40335\ldots-o(1))N_q                              \tag{0.7}
\]

targets have at most two correct PBBS occurrences.  No aggregate multiplicity argument can make the deep bank highly redundant there.

Moreover, two occurrences do not imply resistance to one deleted connector edge: the two intervals may overlap.  A `q`-edge factor edge lies in at most `q` based `q`-intervals.  Consequently `mu_q(U)>q` forces avoidance of any one prescribed deleted edge, but the scalar capacity for this conclusion starts only at

\[
 q_{\rm hit}(m)
 :=\min\{q:W\ge(q+1)N_q\}
 =(1+o(1))\sqrt{{m\log m\over2}},                       \tag{0.8}
\]

which is a factor `Theta(sqrt(log m))` deeper than the word deadline.

Finally, the exact synchronized ledger

\[
 H_q=0,
 \quad E_q=G_q-N_q,
 \quad \widetilde E_q=0
\]

contains no hidden balancing.  Once `H_q=0`, its last two equalities are identities.  It is compatible, simultaneously at every depth, with every target having multiplicity exactly one.  Therefore the missing theorem is not another scalar ledger estimate.  It is a componentwise corridor-transversal theorem.

Throughout this note `q` is the **number of factor edges** in the witness.
Some older reports index an upper fan by its number of owners; in that
convention every displayed upper index here is shifted upward by one.

## 1. All-occurrence upper multiplicities

Let the canonical PBBS two-factor on the rank-`m` shore be oriented by `g=f^2`.  For a lower target

\[
                         S\in{[n]\choose m-q},
\]

write `mathcal W_q^-(S)` for all based correct-rank paths

\[
 X,gX,\ldots,g^qX
 \quad\hbox{with}\quad
 \bigcap_{t=0}^qg^tX=S.                                \tag{1.1}
\]

The audited all-depth fan theorem gives

\[
 1\le |\mathcal W_q^-(S)|\le {2q+1\choose q}.          \tag{1.2}
\]

Complementing every owner turns (1.1) into a `q`-edge upper occurrence of
`U=[n]\setminus S`.  Hence define

\[
 \mathcal W_q^+(U)
 :=\{\overline X,\overline {gX},\ldots,\overline {g^qX}:
       (X,\ldots,g^qX)\in\mathcal W_q^-(U^c)\},        \tag{1.3}
\]

and

\[
                         \mu_q(U)=|\mathcal W_q^+(U)|.  \tag{1.4}
\]

There are `N_q` possible targets `U`.  Every based middle state supplies at most one directed `q`-interval, and there are `W` based states.  Some intervals can have the wrong rank.  Therefore

\[
                         N_q\le G_q^{\rm all}
                         :=\sum_U\mu_q(U)\le W.         \tag{1.5}
\]

No equality `G_q^{all}=W` is used below.

## 2. The exact scalar thresholds

### Lemma 2.1 (central-layer ratio)

For `1<=q<=m`,

\[
 R_q:={W\over N_q}
 =\prod_{j=0}^{q-1}{m+j+2\over m-j}.                   \tag{2.1}
\]

Uniformly for `q=o(m^(2/3))`,

\[
 \log R_q={q(q+1)\over m}+O\left({q^3\over m^2}\right). \tag{2.2}
\]

#### Proof

The binomial recurrence gives

\[
 {{n\choose m-j}\over{n\choose m-j-1}}
 ={m+j+2\over m-j}.
\]

Multiplying from `j=0` to `q-1` proves (2.1).  Also

\[
 \log {m+j+2\over m-j}
 ={2j+2\over m}+O\left({(j+2)^2\over m^2}\right).
\]

Summation proves (2.2). `square`

### Corollary 2.2 (doubling threshold)

The least depth at which the total PBBS start capacity could give two occurrences to every target satisfies

\[
                         q_2(m)=\sqrt{m\log2}+O(1).      \tag{2.3}
\]

The same asymptotic holds for the fixed gap section, whose number of starts is

\[
 M=N_1={n\choose m-1},
 \qquad
 {M\over N_q}
 =\prod_{j=1}^{q-1}{m+j+2\over m-j}.                   \tag{2.4}
\]

#### Proof

The products are increasing in `q`.  In the Gaussian range (2.2) says that their logarithms are `q^2/m+o(1)`.  Equating this to `log 2` locates the crossing at `sqrt(m log 2)+O(1)`.  Removing the `j=0` factor changes the logarithm by `O(1/m)` and hence changes the integer crossing by only `O(1)`. `square`

### Corollary 2.3 (deadline location)

For `k=2m+1`, the established deadline asymptotic

\[
 d(k)=\sqrt{\pi k/8}+O(1)
\]

gives

\[
 {d(k)^2\over m}\longrightarrow{\pi\over4},
 \qquad
 R_{d(k)+O(1)}\longrightarrow e^{\pi/4}.               \tag{2.5}
\]

Since `pi/4>log 2`, the deadline lies beyond the scalar doubling threshold by

\[
 \left({\sqrt\pi\over2}-\sqrt{\log2}+o(1)\right)\sqrt m. \tag{2.6}
\]

This comparison is only a capacity statement; it gives no pointwise multiplicity lower bound.

## 3. Forced singleton and low-multiplicity targets

### Theorem 3.1 (forced singleton count)

Let `s_q=|{U:mu_q(U)=1}|`.  Then

\[
                         s_q\ge(2N_q-W)_+.               \tag{3.1}
\]

#### Proof

Every nonsingleton target contributes at least two occurrences.  Hence

\[
 G_q^{\rm all}
 =\sum_U\mu_q(U)
 \ge s_q+2(N_q-s_q)=2N_q-s_q.
\]

Use `G_q^{all}<=W` and rearrange. `square`

For `q=(c+o(1))sqrt(m)`, Lemma 2.1 gives `W/N_q=e^(c^2)+o(1)`.  Dividing (3.1) by `N_q` proves (0.5).

### Theorem 3.2 (many targets have bounded load)

For every integer `L>=1`,

\[
 \left|\{U:\mu_q(U)\le L\}\right|
 \ge
 \left(1-{R_q-1\over L}\right)N_q.                    \tag{3.2}
\]

The right side may of course be replaced by zero when negative.

#### Proof

If `A` targets have multiplicity at least `L+1`, then complete support gives

\[
 G_q^{\rm all}\ge(N_q-A)+A(L+1)=N_q+LA.
\]

Thus `A<=(W-N_q)/L=(R_q-1)N_q/L`. `square`

At `q=d(k)+O(1)`, take `L=2` and use (2.5).  This proves (0.7).  In particular a positive-density part of the first unprotected deep layer has only one or two old PBBS witnesses.  More generally, at every depth `q<=A sqrt(m)` with fixed `A`, some target has only `O_A(1)` occurrences.  A claim that every deep target has many occurrences cannot start anywhere in a fixed Gaussian window.

## 4. What the synchronized ledger does and does not say

For the fixed gap section let

\[
 a_q(S)
 :=|\{X\in\mathcal X:
       \bigcap_{t=0}^qg^tX=S\}|,                       \tag{4.1}
\]

where only correct-rank selected starts are counted.  The whole-fan theorem gives

\[
                         a_q(S)\ge1.                    \tag{4.2}
\]

Therefore

\[
 G_q=\sum_Sa_q(S),
 \qquad
 E_q=\sum_S(a_q(S)-1)=G_q-N_q.                        \tag{4.3}
\]

The floor subtracted in the definition of `tilde E_q` is exactly `(G_q-N_q)_+`.  Since (4.2) gives `G_q>=N_q`,

\[
                         \widetilde E_q
 =E_q-(G_q-N_q)=0.                                    \tag{4.4}
\]

Thus, after support is known, `tilde E_q=0` is an identity.  It does not say that the vector `(a_q(S))_S` is balanced, and it does not imply

\[
                         a_q(S)\ge\left\lfloor G_q/N_q\right\rfloor. \tag{4.5}
\]

The mortality identity is equally aggregate, since

\[
                         M-b_q=G_q=N_q+E_q.             \tag{4.6}
\]

Indeed the simultaneous numerical profile

\[
 a_q(S)=1\quad\hbox{for every }S,
 \qquad
 G_q=N_q,
 \qquad
 b_q=M-N_q,
 \qquad
 E_q=0                                               \tag{4.7}
\]

satisfies every synchronized ledger equation at every depth, including

\[
 (b_q-b_{q-1})+(E_q-E_{q-1})=N_{q-1}-N_q.             \tag{4.8}
\]

Equation (4.7) is a numerical witness to the logical scope of the ledger, not a claim that this is the actual PBBS histogram.  It proves that no pointwise multiplicity threshold follows from the ledger alone, even after the scalar ratio `M/N_q` exceeds two.

## 5. Exact cut-transversal calculus

Let `F` be the old PBBS two-factor.  Every PBBS component has length at least `2m+1`, while `q<=m`; hence a `q`-edge occurrence is a proper directed cyclic arc.

For a component `C`, let

\[
 \mathcal W_{q,C}(U)
 :=\{I\in\mathcal W_q^+(U):I\subseteq C\},
 \qquad
 \mu_{q,C}(U)=|\mathcal W_{q,C}(U)|.                    \tag{5.1}
\]

### Lemma 5.1 (edge congestion and disjoint packing)

For every factor edge `e\in E(C)`,

\[
 |\{I\in\mathcal W_{q,C}(U):e\in E(I)\}|\le q.        \tag{5.2}
\]

Moreover `\mathcal W_{q,C}(U)` contains at least

\[
 \left\lceil{\mu_{q,C}(U)\over2q-1}\right\rceil       \tag{5.3}
\]

pairwise edge-disjoint occurrences.

#### Proof

Exactly `q` directed `q`-arcs in `C` contain a fixed edge, one for each possible relative start position.  Restricting to one target proves (5.2).

Fix one `q`-arc.  Since `|C|>2q`, another `q`-arc overlaps it only when its start is one of the `2q-1` start positions from `q-1` steps before through `q-1` steps after the fixed start.  Greedily select an arc and discard all intersecting arcs.  Each selection discards at most `2q-1` members, proving (5.3). `square`

### Theorem 5.2 (componentwise bounded-degree connector criterion)

Let `D\subseteq E(F)` be the old edges deleted by a connector rethread,
and suppose

\[
                         |D\cap E(C)|\le\Delta          \tag{5.4}
\]

for every old component `C`.  An old target `U` survives whenever there is a component `C` such that

\[
                         \mu_{q,C}(U)>q\Delta.           \tag{5.5}
\]

A stronger geometric sufficient condition is that `\mathcal W_{q,C}(U)`
contain `\Delta+1` pairwise edge-disjoint occurrences.  By (5.3), this
follows from

\[
                         \mu_{q,C}(U)>(2q-1)\Delta.      \tag{5.6}
\]

#### Proof

If every old witness of `U` in `C` were cut, then by (5.2) the `Delta` deleted edges in `C` could meet at most `q Delta` of its occurrences.  This contradicts (5.5).  The edge-disjoint statement is immediate: one deleted edge can hit at most one member of an edge-disjoint family.  Equation (5.6) follows from (5.3). `square`

The exact condition, with no sufficient relaxation, is

\[
 \boxed{
 U\text{ survives}
 \iff
 \exists I\in\mathcal W_q^+(U)\quad E(I)\cap D=\varnothing.} \tag{5.7}
\]

This is the targetwise cut-transversal criterion already identified by the whole-fan theorem.

### Corollary 5.3 (conditional `O(1)` hole theorem)

Suppose a resident compound connector transports every upper target through depths `q<=d`.  Suppose its old-edge deletion set has component degree at most `Delta`.  If, among all targets at depths `q>d`, all but at most `C` satisfy (5.5) for some old component, then the resulting rethread has at most `C` old upper holes.

If every deep target satisfies (5.5), it has zero old upper holes.

This is a complete proof once the componentwise load premise is supplied.  No Hall coupling between distinct upper targets is required.

## 6. Why Gaussian multiplicity does not supply the premise

For a single deleted edge, `mu_q(U)>q` is a target-independent count sufficient to avoid it, because of (5.2).  Giving `q+1` occurrences to every target requires at least

\[
                         W\ge(q+1)N_q.                   \tag{6.1}
\]

Let `q_hit(m)` be the least `q` satisfying (6.1).  Lemma 2.1, now used at `q=Theta(sqrt(m log m))`, gives

\[
 \log R_q={q^2\over m}+o(1).
\]

Solving `R_q=q+1` yields

\[
 q_{\rm hit}(m)
 =(1+o(1))\sqrt{{m\log m\over2}}.                       \tag{6.2}
\]

At the deadline `q=d(k)+O(1)`, the entire start capacity per target is only
`e^{\pi/4}+o(1)`, whereas `q` tends to infinity.  Hence neither the
synchronized section nor the full PBBS occurrence deck can force (5.5) by
aggregate counts in the first unprotected deep layers.

Even the weaker statement `mu_q(U)>=2` would not prove one-edge resilience: two directed intervals can share a common edge.  What is needed there is either

1. two geometrically edge-disjoint corridors;
2. a direct proof that the connector edge avoids their common intersection; or
3. a phase-correlated compound packet which recreates the target.

None follows from `G_q,H_q,E_q,tilde E_q`.

## 7. Raw hole bound and the exact obstruction

At fixed depth `q`, one deleted factor edge lies in exactly `q` old based `q`-arcs.  Therefore, for arbitrary `D`,

\[
 \#\{\text{upper targets lost at depth }q\}
 \le q|D|.                                             \tag{7.1}
\]

If all depths through `d` are protected, summing only the unprotected rows gives

\[
 \#\{\text{old upper holes}
       \text{ at depths }>d\}
 \le |D|\sum_{q=d+1}^{m}q.                            \tag{7.2}
\]

This is generally `Theta(|D|m^2)`, not `O(1)`.  Improving (7.2) to `O(1)` requires the targetwise avoidance in Corollary 5.3 or a literal new-witness construction.

For a single selected-edge puncture `e`, define the old witness core

\[
 \operatorname {Core}_q(U)
 :=\bigcap_{I\in\mathcal W_q^+(U)}E(I).                 \tag{7.3}
\]

Then the exact one-edge criterion is

\[
 U\text{ is lost by deleting }e
 \iff e\in\operatorname {Core}_q(U).                   \tag{7.4}
\]

The selected-edge inverse-fan theorem lists at most `q` named liabilities
at depth `q`, and `binom(m+1,2)` across all depths, for this puncture.  If
a resident compound packet transports all liabilities through depth `d`,
the unpriced inverse fan still has size at most

\[
                         \sum_{q=d+1}^m q.              \tag{7.5}
\]

The multiplicity theorem does not show that `e` is absent from the cores
of these remaining targets.  It does show the sharp count-only fact

\[
                         \mu_q(U)>q
 \quad\Longrightarrow\quad
                         \operatorname {Core}_q(U)=\varnothing, \tag{7.6}
\]

but Section 6 proves that (7.6) cannot hold uniformly by scalar capacity
near `q=d`.  Thus the inverse-fan `q3` obstruction is not washed away by
the Gaussian repeat ledger; it must be cancelled by actual corridor
geometry or by a compound common-history packet.

The obstruction can now be stated exactly:

> **Connector obstruction.**  The current PBBS synchronized ledger
> controls only the total mass of the occurrence histogram.  A
> bounded-degree connector needs componentwise transversal rank of the
> actual corridor families.  In the first deep layer after an `O(d)`
> resident collar, a positive density of targets has at most two old
> corridors, so that transversal rank cannot be inferred from multiplicity
> or from floor-correct repeat excess.

The next proof target is therefore the following genuinely geometric statement.

> **Deep-corridor separation lemma.**  For every proper upper target at
> depth `q>d(k)`, either one correct PBBS corridor avoids the prescribed
> bounded-degree connector set, or the connector packet creates a new
> occurrence of that same target.  Equivalently, all but `O(1)` target
> families have connector-relative transversal rank greater than the
> deleted-edge budget.

No weaker rankwise average or repeat-excess identity implies this lemma.

## 8. Scope

Proved here:

1. the exact scalar doubling threshold `sqrt(m log 2)+O(1)`;
2. forced singleton counts below that threshold;
3. constant average multiplicity and a positive-density load-at-most-two
   family at the word deadline;
4. the tautological nature of zero floor-correct excess after full support;
5. the exact edge-congestion, disjoint-packing, and componentwise
   cut-transversal criteria;
6. the conditional `O(1)` upper-hole theorem under componentwise
   transversal rank; and
7. the later `sqrt(m log m/2)` threshold at which raw occurrence count
   could begin to force one-edge avoidance for every target.

Not proved here:

1. that every target above the scalar doubling threshold has two occurrences;
2. that low-multiplicity occurrences are edge-disjoint;
3. that PBBS multiplicity is spread across components;
4. that an actual global connector satisfies the deep-corridor separation
   lemma; or
5. an unconditional `B(k)`, `B(k)+O(1)`, or `k=17` construction.
