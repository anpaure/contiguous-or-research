# PBBS global seam batching: the one-mountain compiler and the exact two-endpoint gate

Date: 2026-07-28

Status: theorem-level advance and obstruction.  No computation or web search
is used.  The batching theorems are unconditional under their stated
chronology hypotheses.  Those hypotheses are not proved for the canonical
PBBS factor, so coefficient one is not claimed.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 B=\frac{W}{n}=\operatorname {Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil .
\]

The current literal PBBS ledger pays `Theta(H)` letters at each member of a
short-residence transversal.  The existing critical estimate

\[
 \nu_H(P_m)=O_A(B\sqrt m)=O_A(BH)
 \tag{0.1}
\]

therefore gives only a linear-order repair.  This note separates three
logically different questions.

1. A **standalone or append-only** seam bank cannot in general remove the
   factor `H`.  At one fixed depth, distinct equal-rank target values consume
   distinct word endpoints.  For `J` separated cuts and maximum target
   multiplicity `mu_H`, its length is at least `HJ/mu_H`.

2. There is no universal integrated lower bound of `Omega(H)` per seam.
   The exact sliding-core Johnson model has `J` separated forced short-run
   collars but a word of only `2H` excess, independent of `J`.

3. There is a positive, baseline-recycling compiler substantially more
   general than that example.  If the nonpersistent coordinate runs of an
   owner block have a one-mountain endpoint order, a word of exact length

   \[
      \text{number of transitions}
      +\text{active width}+1
   \]

   represents **every** consecutive lower intersection and upper union in
   the block.  A one-sided `H`-halo partition of all owner starts then gives

   \[
      \boxed{L_H\le W+HR+\sum_{j=1}^R w_j,}
      \tag{0.2}
   \]

   where `R` is the number of blocks and `w_j` their active widths.

Consequently, if a residence transversal can be grouped into batches of
`b` seams whose intervening owner blocks have one-mountain `H`-halos of
width `O(H)`, then

\[
 \boxed{L_H\le W+O_A\!\left(HB+\frac{H\nu_H}{b}\right).}
 \tag{0.3}
\]

The choices

\[
 b=\lceil\sqrt H\rceil,
 \qquad
 b=\left\lceil\frac{H}{(\log(H+1))^c}\right\rceil
 \tag{0.4}
\]

give exactly the two requested scales

\[
 W+O_A(HB+\sqrt H\,\nu_H),
 \qquad
 W+O_A(HB+\nu_H(\log(H+1))^c).
 \tag{0.5}
\]

Either is `W+o(W)` under (0.1).  Thus the `H` factor is not a generic
information barrier; it is a chronology barrier.  A large-batch
one-mountain rethreading is one precise sufficient PBBS theorem.  A more
general two-sided baseline braid may achieve the same endpoint effect
without being one-mountain.

An exact two-endpoint inequality below is a valid necessary relaxation, but
the audit in Section 7 shows that actual consecutive-window towers nearly
saturate it automatically.  It therefore does **not** furnish the sought
negative interface.  Any genuine lower bound must use intervening letter
content or a stronger chronology invariant.

## 1. What is already closed in the additive architecture

For selected cuts `C` on one owner cycle, the proved upper compiler has
length

\[
 |S_H(\mathcal C)|+|\mathcal C|+O(H),
 \qquad
 |S_H(\mathcal C)|=sum_j\min(g_j,2H-1),
 \tag{1.1}
\]

where the `g_j` are cyclic cut gaps.  Lower dominance staircases and
endpoint initialization batch over a cluster of span `S` at cost

\[
 7H+3S-3.
 \tag{1.2}
\]

These are genuine sharing theorems.  However
`PBBS_ST_CS_EQUIVALENCE_20260726.md` proves that this whole additive
clustered-span architecture has sublinear cost if and only if the
corresponding `H nu_H` term is already subcritical.  Therefore (0.3) cannot
come from a sharper summation of the established independent cluster
charts.  It must recycle baseline positions.

There is a useful exact reduction on the return side.  Take any maximal
edge-disjoint subfamily `P` of the short residence intervals.  Its union of
edge supports meets every short residence interval: otherwise an interval
disjoint from that union could be added to `P`.  Hence the union is a
transversal made of at most `nu_H` disjoint blocks and has total raw span at
most `(H+1)nu_H`.  Deleting that union still loses the full factor `H`; an
in-place replacement must credit its baseline span back.

## 2. Standalone batching has a fixed-rank endpoint obstruction

### Lemma 2.1 (one fixed-rank target per endpoint)

A literal word of length `L` represents at most `L` distinct sets of any
one fixed cardinality.

#### Proof

Choose one witnessing interval for each represented target.  If two chosen
intervals have the same left endpoint, one contains the other.  Their ORs
are comparable by inclusion, so distinct ORs of the same cardinality are
impossible.  Thus all chosen left endpoints are distinct.  \(\square\)

The same proof uses right endpoints.

Let \(D_q^\sigma\) be the number of distinct, support-essential crossing target
values at depth `q` and shore \(\sigma\in\{-,+\}\).  “Support-essential” means
that no intact baseline witness is being retained for that value.

### Corollary 2.2 (standalone support bound)

Every auxiliary seam word, and every append-only extension which must newly
create these target values, has length at least

\[
 \boxed{L_{\rm aux}\ge\max_{q,\sigma}D_q^\sigma.}
 \tag{2.1}
\]

If `J` cuts are `q`-separated, all `qJ` crossing occurrences have the
correct rank, and no target value occurs more than `mu_q` times among them,
then

\[
 \boxed{L_{\rm aux}\ge\frac{qJ}{\mu_q},}
 \tag{2.2}
\]

provided those values are support-essential.

#### Proof

In an append-only word, assign every genuinely new target a witness ending
in the appended part.  Targets assigned to one endpoint form an inclusion
chain and hence contain at most one member of a fixed rank.  This proves
(2.1).  Separation gives `qJ` distinct starts; quotienting by maximum value
multiplicity gives at least `qJ/mu_q` target values and proves (2.2).
\(\square\)

For a full budget `O(HB+Jf(H))`, the exact consequence of (2.2) is

\[
 \mu_H=\Omega\!\left(\frac{HJ}{HB+Jf(H)}\right).
 \tag{2.3}
\]

In the saturated critical regime `J=Theta(BH)`, the polylogarithmic budget
in (0.5) would therefore require

\[
 \mu_H=\Omega\!\left(\frac{H}{(\log(H+1))^c}
                 \right),
 \tag{2.4}
\]

and the square-root budget would require

\[
 \mu_H=\Omega(\sqrt H),
 \tag{2.5}
\]

unless most targets retain alternative witnesses.  Neither large
multiplicity nor cut-avoiding support follows from (0.1).  Thus the requested
gain is impossible as a generic auxiliary collar theorem.

## 3. Why `Omega(H)` per seam is false for integrated words

Fix `H>=2` and `J>=1`, put `M=2JH`, and assume

\[
 M\le m+H.
 \tag{3.1}
\]

Choose a set `G` of size `m+1-H` and distinct cyclic labels
`a_0,...,a_(M-1)`.  Define rank-`(m+1)` owners

\[
 X_i=G\cup\{a_i,a_{i+1},\ldots,a_{i+H-1}\},
 \qquad i\in\mathbb Z_M.
 \tag{3.2}
\]

The ground set has size at most `2m+1` by (3.1), and unused coordinates may
be added.  Consecutive owners are Johnson adjacent.

For `0<=t<J`, the coordinate `a_((2t+1)H-1)` has a positive run of exactly
`H` owners.  The closed insertion/removal collars of these `J` runs are
pairwise edge-disjoint and separated by `H-1` unused transition edges.
Thus every `H`-resident path decomposition must meet each collar.

Put

\[
 E_i=G\cup\{a_i\}.
 \tag{3.3}
\]

For `0<=q<=H-1`, direct calculation gives

\[
 \bigcap_{h=0}^{q}X_{i+h}
   =\bigcup_{j=i+q}^{i+H-1}E_j,
 \tag{3.4}
\]

and, for `0<=q<=H`,

\[
 \bigcup_{h=0}^{q}X_{i+h}
   =\bigcup_{j=i}^{i+H+q-1}E_j.
 \tag{3.5}
\]

The depth-`H` lower intersection is `G`.  Therefore the word

\[
 E_0,E_1,\ldots,E_{M-1},
 E_0,E_1,\ldots,E_{2H-2},G
 \tag{3.6}
\]

has length exactly

\[
 \boxed{M+2H}
 \tag{3.7}
\]

and represents every lower intersection and upper union through depth `H`.
At depth `H-1`, the `J(H-1)` crossing lower targets belonging to the selected
collars are distinct.  The alternating complement lift is literal: put

\[
 A_i=\Omega\setminus X_i,qquad B_i=X_i\cap X_{i+1}.
\]

Both have rank `m`, and
\(A_i\cap B_i=B_i\cap A_{i+1}=\varnothing\).  The `A_i` and `B_i` are separately
distinct cyclic windows, while `G!=emptyset` distinguishes every `B_i` from
every `A_j`.  Hence

\[
 A_0,B_0,A_1,B_1,\ldots,A_{M-1},B_{M-1},A_0
\]

is a simple odd-graph cycle.  Thus target distinctness, Johnson legality,
and separated forced returns do not imply `Omega(HJ)` integrated excess.

This example is not asserted to occur as a canonical PBBS component.  Its
role is exact: any valid lower bound must use PBBS chronology or owner
coupling beyond generic collars.

## 4. The one-mountain run compiler

Let

\[
 X_0,X_1,\ldots,X_S\in\binom{\Omega}{k}
 \tag{4.1}
\]

be a directed Johnson path and put

\[
 K=\bigcap_{t=0}^{S}X_t.
 \tag{4.2}
\]

Assume `K` is nonempty.  For every coordinate \(x\notin K\), assume its
membership in the path is either empty or one nonempty interval

\[
 I_x=[l_x,r_x]\subseteq[0,S].
 \tag{4.3}
\]

List the coordinates which occur, say `x_1,...,x_N`, so that the `l_i` are
nondecreasing, with ties resolved once and for all.  Make the following
one-mountain hypothesis:

\[
 \boxed{\{i:r_i\ge t\}\text{ is an integer interval for every }t.}
 \tag{4.4}
\]

Equivalently, the exit sequence is weakly increasing up to one plateau and
weakly decreasing afterwards.  FIFO and LIFO endpoint orders are the two
monotone special cases.

### Theorem 4.1 (exact one-mountain compiler)

Under (4.1)--(4.4), the nonzero word

\[
 A_1,A_2,\ldots,A_N,K,
 \qquad A_i=K\cup\{x_i\},
 \tag{4.5}
\]

represents every consecutive lower intersection and every consecutive upper
union of the owner path.  Moreover, if

\[
 w=|X_0\setminus K|,
 \tag{4.6}
\]

then

\[
 \boxed{N=S+w,\qquad |(4.5)|=S+w+1.}
 \tag{4.7}
\]

Thus the exact excess over the `S+1` owner positions is `w`, independent of
the number of seam windows inside the block.

#### Proof

For an owner interval `[a,b]`, a noncore coordinate belongs to its total
intersection exactly when

\[
 l_i\le a,\qquad r_i\ge b.
 \tag{4.8}
\]

The first condition selects a prefix of the index order; by (4.4), the
second selects an interval.  Their intersection is an interval.  Hence the
lower target is the OR of the corresponding contiguous subword of the
`A_i`'s.  If the selected interval is empty, the target is `K`, represented
by the last letter.

A noncore coordinate belongs to the total union exactly when its run meets
`[a,b]`, equivalently

\[
 l_i\le b,\qquad r_i\ge a.
 \tag{4.9}
\]

Again this is a prefix intersected with an interval, hence an interval, and
the corresponding `A_i` subword has exactly the required OR.  Singleton
owner windows show that every `X_t` is represented as well.

It remains to count.  The `w` coordinates of `X_0\setminus K` give the
noncore runs starting at zero.  At every one of the `S` Johnson transitions,
the arriving coordinate starts a noncore run.  The single-run hypothesis
makes these arriving coordinates distinct from one another and from all
previously ended runs.  These are all noncore runs, so `N=w+S`.  Equation
(4.7) follows.  Every emitted letter contains the nonempty core `K`.
\(\square\)

### Remark 4.2 (boundary transparency in the FIFO case)

If the `r_i` are nondecreasing, the union of every owner prefix is represented
by a prefix of `A_1,...,A_N`, and every owner suffix by a suffix.  Therefore
the FIFO compiler can replace a literal owner block inside an ambient word
without changing any old interval OR which crosses one or both outer
boundaries.  The general one-mountain compiler is an exact internal block
compiler; no two-sided boundary substitution is asserted for it.

### Corollary 4.3 (intrinsic span ceiling)

For rank-`(m+1)` owners on `2m+1` coordinates, every block satisfying the
single-run hypothesis has

\[
 \boxed{S\le m.}
 \tag{4.8}
\]

#### Proof

The `N=S+w` noncore run coordinates all lie outside `K`.  Since

\[
 |K|=m+1-w,
\]

the number of coordinates outside `K` is `m+w`.  Hence
`S+w=N<=m+w`, proving (4.8).  \(\square\)

Thus one one-mountain carrier can contain at most `O(m/H)=O(H)` mutually
`H`-separated seams.  This ceiling still permits both batch sizes in (0.4).

## 5. Global one-sided halo batching

Let `P` be a disjoint union of oriented owner cycles with total length `W`.
Partition the owner **start indices** on each cycle into `R` nonempty
consecutive arcs

\[
 I_j=[a_j,b_j],\qquad s_j=|I_j|,qquad
 \sum_{j=1}^R s_j=W.
 \tag{5.1}
\]

Attach the forward `H`-halo and consider the path

\[
 Q_j=(X_{a_j},X_{a_j+1},\ldots,X_{b_j+H}).
 \tag{5.2}
\]

Assume this path does not traverse a cycle edge twice, has nonempty
persistent core, and satisfies the one-mountain hypothesis.  Write `w_j`
for its active width (4.6).

### Theorem 5.1 (one-mountain halo compiler)

There is one literal nonzero word which represents every lower intersection
and upper union of at most `H+1` consecutive owners of `P`, of length

\[
 \boxed{L_H(P)\le W+HR+\sum_{j=1}^R w_j.}
 \tag{5.3}
\]

#### Proof

The path `Q_j` has

\[
 S_j=s_j+H-1
\]

transitions.  Theorem 4.1 gives a word of length

\[
 S_j+w_j+1=s_j+H+w_j.
\]

Concatenate these `R` words.  A forward owner window of at most `H+1`
owners is assigned to the unique arc containing its start index; its whole
window lies in that arc's forward halo and is represented by the
corresponding compiler.  Summing the displayed lengths and using (5.1)
proves (5.3).  \(\square\)

For PBBS, the all-depth corridor theorem says that these owner windows
already contain a correct witness for every intended band target.  Thus
(5.3), followed by the audited outer product-SCD tail, proves coefficient
one whenever

\[
 HR+\sum_jw_j=o_A(W)
 \tag{5.4}
\]

for a slowly diagonalized Gaussian cutoff.

## 6. Quantitative seam batching

Let `c(P_m)<=B` be the number of PBBS projected owner cycles.  Circular
interval piercing gives a residence cut set of size

\[
 J\le\nu_H(P_m)+c(P_m).
 \tag{6.1}
\]

Fix `b>=1`.  Consecutively group the selected cuts on each cycle into
batches of `b`, except for at most one smaller remainder batch per active
cycle.  Leave cycles with no selected cut on the ordinary cyclic erosion
compiler, at additional cost at most `2H` per such cycle.  On an active
cycle, insert at most one additional block boundary if needed to ensure no
forward halo traverses a cycle edge twice.  Indeed every PBBS projected
cycle has length `ell>=2m+1>2H`.  At most one preliminary arc can have
`s_j>ell-H`; split that arc into two nonempty arcs of sizes at most
`ell-H`, which is possible because `ell>=2H`.  The resulting halos have
`s_j+H-1<ell` transitions.  The active-cycle partition then uses at most

\[
 R\le 2c(P_m)+\frac{J}{b}
 \le 2B+\frac{\nu_H(P_m)+B}{b}
 \tag{6.2}
\]

batches.  Partition the owner starts into the corresponding consecutive
arcs.

### Corollary 6.1 (conditional batched-seam theorem)

Assume every forward `H`-halo of the active-cycle partition in (6.2) is a
one-mountain block of active width at most `C_A H`, where `C_A` is
independent of `m`.  Then

\[
 \boxed{
 L_H(P_m)
 \le W+O_A\!\left(HB+\frac{H\nu_H(P_m)}{b}\right).}
 \tag{6.3}
\]

#### Proof

Use cyclic erosion on the inactive cycles.  Apply Theorem 5.1 to the active
partition and use

\[
 HR+\sum_jw_j\le(1+C_A)HR.
\]

More explicitly, if `c_0` is the number of inactive cycles and `R_1` the
number of final active blocks, the hybrid word has length at most

\[
 W+2Hc_0+HR_1+\sum_{j=1}^{R_1}w_j.
 \tag{6.3a}
\]

The inactive-cycle charge is at most `2HB`.  Substitute (6.2); the term
`HB/b` is absorbed by `HB`.  \(\square\)

With the choices (0.4), (6.3) is exactly (0.5).  Under (0.1), either
excess is `o_A(W)` because `W=(2m+1)B=Theta(BH^2)` and

\[
 \frac{HB+\sqrt H\,\nu_H}{W}=O_A(H^{-1/2}),
 \qquad
 \frac{HB+\nu_H(\log(H+1))^c}{W}
 =O_A\!\left(\frac{(\log(H+1))^c}{H}\right).
 \tag{6.4}
\]

This is a genuine composition theorem.  Its open hypothesis is not a
generic seam-count estimate: it requires the actual PBBS owner chronology,
or a literal exact Johnson/odd-factor rethreading with full all-depth PBBS
support (or independently sublinear support repair), to have large
one-mountain batches.
The explicit PBBS endpoint permutation `213` shows that the condition does
not hold automatically even in a three-run local collar.

## 7. The exact integrated lower interface

The preceding positive theorem shows why endpoint counting cannot prove an
unconditional per-seam lower bound.  It can nevertheless identify the
chronology which any near-width compiler must realize.

Let a nonzero word of length `M+e` represent

* `M` distinct owners of one rank `r`; and
* distinct target families `T_q^-` and `T_q^+` of ranks `r-q` and `r+q`,
  of sizes `D_q^-` and `D_q^+`, for `1<=q<=H`.

Choose one witness interval per represented set.  Equal-rank witnesses have
distinct left endpoints and distinct right endpoints.  Moreover, when they
are ordered by their left endpoints, their right endpoints have the same
order: reversing a pair would nest two intervals and make their distinct
equal-rank ORs comparable.

At a fixed depth and shore, at most `e` target witnesses have a left
endpoint outside the owner left-endpoint set, and at most `e` have a right
endpoint outside the owner right-endpoint set.  Hence at least

\[
 (D_q^\sigma-2e)_+
 \tag{7.1}
\]

targets are doubly anchored at owner endpoints.

For a doubly anchored lower target `T`, let `U` be the owner sharing its
left endpoint and `V` the owner sharing its right endpoint.  Its witness is
strictly inside both owner witnesses, and therefore

\[
 T\subseteq U\cap V.
 \tag{7.2}
\]

For a doubly anchored upper target, the owner witnesses lie inside its
witness and

\[
 U\cup V\subseteq T.
 \tag{7.3}
\]

At each depth the resulting owner pairs form a partial matching on both
endpoint orders.  Across depths, targets using a common left or right owner
are nested in rank order.

More explicitly, write the owners as
\(O_1\prec O_2\prec\cdots\prec O_M\) in their common left/right endpoint
order.  If a lower target has interval `[l_i,r_j]`, strict containment in
both anchored owner intervals gives `r_j<r_i` and `l_j<l_i`, hence `j<i`.
For an upper target the two owner intervals lie strictly inside its interval,
giving `i<j`.  In particular the two anchors are never equal.  Ordering
equal-rank target intervals by their left endpoints orders their right
endpoints the same way, so the anchor pairs are order-preserving.

Define \(\Lambda_{2,H}^{\pm}\) on these fixed owner and target families as
follows.  Maximize `|S|` over a subset `S` of the disjoint union of the
displayed `2H` target families, one common linear order `prec` on the
owners, and two maps

\[
 \lambda,\rho:\mathcal S\longrightarrow\mathcal U
 \tag{7.4a}
\]

subject to all of the following.

1. At each fixed depth and shore, both maps are injective and the pairs are
   order-preserving:

   \[
    \lambda(T)\prec\lambda(T')
    \quad\Longleftrightarrow\quad
    \rho(T)\prec\rho(T').
   \tag{7.4b}
   \]

2. For a lower target,

   \[
    \rho(T)\prec\lambda(T),\qquad
    T\subseteq\lambda(T)\cap\rho(T),
   \tag{7.4c}
   \]

   while for an upper target,

   \[
    \lambda(T)\prec\rho(T),\qquad
    \lambda(T)\cup\rho(T)\subseteq T.
   \tag{7.4d}
   \]

3. Across different depths and shores, targets reusing a value in the same
   endpoint role (two `lambda` uses or two `rho` uses) are nested in their
   rank order.  A cross-role equality `lambda(T)=rho(T')` is not a common
   word endpoint and imposes no nesting condition.

This is a set-theoretic relaxation: it deliberately omits the requirement
that one common literal word realize all intervening letters.

### Theorem 7.1 (two-endpoint chronology inequality)

Every literal realization satisfies

\[
 \boxed{
 \sum_{q=1}^{H}\sum_{\sigma\in\{-,+\}}
       (D_q^\sigma-2e)_+
 \le\Lambda_{2,H}^{\pm}.}
 \tag{7.4e}
\]

Consequently

\[
 \boxed{
 e\ge
 \frac{
   \sum_{q=1}^{H}(D_q^-+D_q^+)-\Lambda_{2,H}^{\pm}
 }{4H}.}
 \tag{7.5}
\]

The lower-only or upper-only version has denominator `2H`.

#### Proof

The endpoint argument above leaves at least (7.1) doubly anchored targets
in every family.  Their actual witness intervals and owner endpoints form a
system admitted in the definition of \(\Lambda_{2,H}^{\pm}\), proving
(7.4e).
Since `(x-2e)_+>=x-2e`, summing over the `2H` families gives

\[
 \Lambda_{2,H}^{\pm}
 \ge\sum_q(D_q^-+D_q^+)-4He,
\]

which is (7.5).  \(\square\)

### Proposition 7.2 (actual towers saturate the endpoint relaxation)

For one linear owner chronology `X_0,...,X_(M-1)`, every actual consecutive
lower and upper window through depth `H` has a simultaneous system admitted
by \(\Lambda_{2,H}^{\pm}\).  On a union of `c` cyclic chronologies, opening once
per cycle discards at most

\[
                       cH(H+1)
\tag{7.5a}
\]

lower-plus-upper occurrences through depth `H` and admits all the rest.

#### Proof

For

\[
 L_{i,q}=\bigcap_{t=i}^{i+q}X_t,
 \qquad
 U_{i,q}=\bigcup_{t=i}^{i+q}X_t,
\]

use

\[
 (\rho,\lambda)(L_{i,q})=(X_i,X_{i+q}),
 \qquad
 (\lambda,\rho)(U_{i,q})=(X_i,X_{i+q}).
\]

Containment is immediate.  At fixed `q`, the start and end maps are
injective and order-preserving.  Reuse of a fixed left endpoint as `q`
grows, or of a fixed right endpoint as the window grows leftward, gives
nested intersections and unions.  This is exactly the same-role nesting
condition.  On a rooted cycle, only the `q` windows crossing the root are
lost at depth `q`, on each of two shores.  Summing `2q` for `q=1,...,H`
gives (7.5a).  Passing from occurrences to distinct target values can only
decrease the number that must be retained.  \(\square\)

Consequently Theorem 7.1 is normally near equality on the old target
chronology.  It cannot produce a fixed-fraction `JH^2` deficit when
`J` is much larger than the component count.  The conditional calculation
below remains algebraically correct, but its hypothesis is not a plausible
PBBS obstruction without additional letter-content restrictions.

Suppose, conditionally, that the support-essential crossing families obey,
uniformly for `1<=q<=H`,

\[
 D_q^-+D_q^+=\Theta(qJ)
 \quad(1\le q\le H).
 \tag{7.6}
\]

Then their total size is `Theta(JH^2)`.  A fixed-fraction deficit in every
simultaneous two-endpoint system forces `e=Omega(JH)`, making `H` per seam
unavoidable.  More generally, a budget `e=O(HB+Jf(H))` necessarily forces

\[
 \frac{
  \sum_q(D_q^-+D_q^+)-\Lambda_{2,H}^{\pm}
 }{JH^2}
 =O\!\left(\frac{B}{J}+\frac{f(H)}H\right).
 \tag{7.7}
\]

In the saturated critical regime `J=Theta(BH)`, the proposed compressed
ledgers therefore force

\[
 \frac{
  \sum_q(D_q^-+D_q^+)-\Lambda_{2,H}^{\pm}
 }{JH^2}
 =
 \begin{cases}
  O((\log(H+1))^c/H),&e=O(J(\log(H+1))^c),\\
  O(H^{-1/2}),&e=O(J\sqrt H).
 \end{cases}
 \tag{7.8}
\]

Thus either requested gain requires an almost-complete simultaneous
two-owner nested lift.  This condition is necessary, not sufficient:
intervening-letter convexity can still fail after the relaxed lift
saturates.  Separate rankwise designs do not establish it.

## 8. Reconciliation with hypersimplex completion

The hypersimplex theorem says that, whenever

\[
 0\le\gamma_{q,x}\le e_q,
\]

the prescribed point-degree vector at depth `q` has a hole-free rankwise
realization connected by symmetric two-block exchanges.  In particular the
bounds hold with wide margins for the frozen `k=15` depth-two and
depth-three rows.

Theorem 7.1 requires more.  Almost every target must choose two owner
endpoints in one common order, these choices must be partial matchings at
each rank, and choices sharing either endpoint must nest across ranks.
Nothing in the integer decomposition of one hypersimplex supplies that
ordered convexity.  Therefore another rankwise balancing lemma cannot prove
(0.3).

Nor can an occurrence-private singleton-pin argument prove the opposite.
Unit flag
increments use ground coordinates as pins; many requests can share one pin,
and a common letter can contain the union of several compatible pins.
Thus treating physical occurrences as independent private colours fails.  A
remaining obstruction may use owner compatibility and/or intervening-letter
chronology.

## 9. Sharp remaining PBBS theorem

The proved implications are now exact.

* Additive cluster sharing is asymptotically equivalent to the old `H nu_H`
  gate and cannot yield (0.5) from (0.1).
* Standalone/append-only batching needs large target collision or intact
  alternative witnesses, quantified by (2.2)--(2.5).
* An integrated `Omega(H)`-per-seam lower bound is false, by Section 3.
* One-mountain baseline recycling replaces seam count by block count and
  active width, and Theorem 5.1 composes those blocks globally.
* The simultaneous two-endpoint system of Theorem 7.1 is necessary but is
  already near-saturated by Proposition 7.2; it is not the negative gate.

The positive PBBS target is therefore:

> Choose a short-residence transversal and group its cuts into batches of
> `b=sqrt(H)` (or `H/polylog(H)`).  Partition the complete owner-start arcs,
> not merely local cut neighborhoods, so that every associated forward
> `H`-halo is a one-mountain block of active width `O(H)`, with at most
> `O(B)` remainder blocks.  If the arcs are rethreaded rather than retained,
> require a literal exact Johnson/odd-factor chronology preserving the full
> PBBS all-depth support, or prove an independently sublinear support repair.

Corollary 6.1 would then give coefficient one from the already proved
critical packing estimate.  Proposition 7.2 closes the proposed
fixed-fraction \(\Lambda_{2,H}^{\pm}\) route: a negative theorem must instead use
intervening set-letter content, run-endpoint valleys, or a stronger
owner-chronology constraint.  None of those density statements is currently
proved.  This is the sharp boundary; pure seam-count bookkeeping is
exhausted.
