# Block-reroot upper-shadow ledger and the exact seam/slack boundary

Date: 2026-07-31  
Lane: A, reroot/upper-shadow  
Status: unconditional dimension-uniform ledger and sufficient repair theorem

## 0. Scope

This note isolates what a block reroot can and cannot change. It treats both:

1. fixed-depth windows of \(q+1\) consecutive middle states; and
2. arbitrary-width interval ORs, which are needed for the complete upper
   tower.

The result is purely deterministic. It does not assume PBBS, four-filter
lineage, or a particular compiler. The solved K16 endpoint reroot is the
calibrating instance.

## 1. Fixed-depth seam ladders

For a set word \(X=(X_0,\ldots,X_{n-1})\), define the depth-\(q\) window
multiset

\[
\mu_q(X)=
 \left\{\!\left\{
   \bigvee_{t=0}^{q}X_{i+t}:0\le i<n-q
 \right\}\!\right\}.                                  \tag{1.1}
\]

If \(A,B\) are nonempty words, define their crossing depth-\(q\) ladder

\[
L_q(A,B)=
 \left\{\!\left\{
 \bigvee\operatorname{suf}_t(A)\ \vee\
 \bigvee\operatorname{pre}_{q+1-t}(B):
 \begin{array}{l}
 1\le t\le q,\\
 t\le |A|,\ q+1-t\le |B|
 \end{array}
 \right\}\!\right\}.                                  \tag{1.2}
\]

Let a source word be partitioned into consecutive blocks

\[
T=B_1\Vert\cdots\Vert B_c.                              \tag{1.3}
\]

A block reroot \(T'\) uses every \(B_i\) exactly once, in an arbitrary block
order and with each block independently oriented forward or backward.
Write the resulting oriented blocks as \(C_1,\ldots,C_c\).
Treat seams as labelled occurrences between oriented block occurrences. A
seam is **retained** only when that same labelled oriented adjacency occurs
in both words. After cancelling all retained occurrences, let \(h\) be the
number of old seams left; exactly \(h\) new seams are left as well. This
definition is deliberately conservative and remains unambiguous when two
different seams happen to have the same OR ladder. Without any cancellation,
one may always take \(h=c-1\).

For an oriented block \(C_i\), let \(P_i(u)\) and \(S_i(u)\) be the ORs of
its first and last \(u\) entries, and let \(W_i=\bigvee C_i\).

### Theorem 1.1 (general multiplicity-exact window ledger)

For every window length \(\ell\ge1\), without a lower bound on block sizes,
the complete crossing contribution in the reroot is

\[
\sum_{1\le p<r\le c}
\ \sum_{\substack{1\le u\le|C_p|, 1\le v\le|C_r|\\
u+\sum_{p<j<r}|C_j|+v=\ell}}
\delta_{\,S_p(u)\vee(\bigvee_{p<j<r}W_j)\vee P_r(v)}.   \tag{1.4a}
\]

Adding the internal length-\(\ell\) windows of every block gives the whole
multiset \(\mu_{\ell-1}(T')\). The identical formula in the old block order
gives \(\mu_{\ell-1}(T)\). Hence the multiplicity change of a value is
exactly its new crossing multiplicity minus its old crossing multiplicity.

#### Proof

Every crossing window has a unique first block \(C_p\), last block \(C_t\),
nonempty suffix length \(u\), and nonempty prefix length \(v\); it contains
all intervening blocks. Conversely every term satisfying the length equation
is one such window. ∎

If the block lengths are \(n_1,\ldots,n_c\) and \(0\le q<N\), the exact number of
length-\((q+1)\) windows crossing at least one seam is

\[
C_q=(N-q)-\sum_{i=1}^{c}(n_i-q)_+
    =\sum_{i=1}^{c}\min(n_i,q)-q.                       \tag{1.4b}
\]

In particular \(C_q\le(c-1)q\), with equality exactly when every block has
length at least \(q\). Old and new crossing multisets both have size \(C_q\);
their total lost-occurrence mass equals their total gained-occurrence mass
and is at most \(C_q\). The two-sided multiset \(L^1\) change is at most
\(2C_q\).

### Corollary 1.2 (separated depth-\(q\) seam ledger)

If every block has length at least \(q\), then

\[
\mu_q(T)=\sum_{i=1}^{c}\mu_q(B_i)
          +\sum_{i=1}^{c-1}L_q(B_i,B_{i+1}),             \tag{1.4}
\]

and

\[
\mu_q(T')=\sum_{i=1}^{c}\mu_q(B_i)
           +\sum_{i=1}^{c-1}L_q(C_i,C_{i+1}).            \tag{1.5}
\]

Here reversal does not alter the internal multiset \(\mu_q(B_i)\). Thus:

* every lost occurrence lies in an old seam ladder;
* every added occurrence lies in a new seam ladder; and
* if \(h\) block adjacencies are changed, at most \(hq\) old occurrences
  can be lost and at most \(hq\) new occurrences can be added.

#### Proof

A window of length \(q+1\) either lies inside one block or crosses a seam.
Because each block has length at least \(q\), no such window crosses two
seams. A window crossing \(A\Vert B\) uses a nonempty suffix of \(A\) and a
nonempty prefix of \(B\), whose lengths sum to \(q+1\); these are exactly
the entries of (1.2). Reversing an internal window reverses its order but
does not change its OR. Equations (1.4)--(1.5) and the count follow. ∎

### Corollary 1.3 (all depths through \(d\))

If \(d<N\) and every block has length at least \(d\), then changing \(h\) seams can
affect only

\[
h\sum_{q=1}^{d}q
  =h\binom{d+1}{2}                                      \tag{1.6}
\]

old depth-at-most-\(d\) window occurrences, and supplies the same number of
new seam-ladder slots. For \(h=O(d)\), the complete shallow disturbance is
\(O(d^3)\).

The statement concerns occurrences. Distinct colours may collide, and one
colour may have witnesses at several seams or in the internal bank. More
generally, for arbitrary block sizes the exact cumulative crossing count is

\[
\sum_{i=1}^{c}\phi_d(n_i)-\binom{d+1}{2},
\quad
\phi_d(n)=
\begin{cases}
dn-\binom n2,&n<d,\\
\binom{d+1}{2},&n\ge d.
\end{cases}                                             \tag{1.7}
\]

## 2. Arbitrary-width block ledger

Fixed-length windows are insufficient for the complete upper tower: a
rank-\((r+q)\) target may have a longer witness if some transitions add no
new coordinate. We therefore record every interval.

For a word \(A\), let \(\mathcal D(A)\) be the set of all interval ORs of
\(A\). For consecutive oriented blocks \(C_i,\ldots,C_j\), \(i<j\), define

\[
\begin{aligned}
\mathcal L(C_i,\ldots,C_j)=
\biggl\{
 &\bigvee\operatorname{suf}_{u}(C_i)
 \ \vee\!\bigvee_{i<t<j}\!\bigvee C_t
 \ \vee\bigvee\operatorname{pre}_{v}(C_j):\\
 &1\le u\le|C_i|,\quad1\le v\le|C_j|
\biggr\}.                                               \tag{2.1}
\end{aligned}
\]

This is a one-seam ladder when \(j=i+1\), and a multi-seam ladder otherwise.

Let \(\mathfrak D(X)\) denote the **multiset** of all interval ORs of a word.
With the prefix/suffix notation of Section 1, the complete multiplicity
ledger is

\[
\begin{aligned}
\mathfrak D(T')={}&
 \sum_{i=1}^{c}\mathfrak D(C_i)\\
&+\sum_{1\le p<t\le c}
  \sum_{u=1}^{|C_p|}\sum_{v=1}^{|C_t|}
  \delta_{S_p(u)\vee(\bigvee_{p<j<t}W_j)\vee P_t(v)}.  \tag{2.2a}
\end{aligned}
\]

The cross-block occurrence count in (2.2a) is exactly

\[
C_* = \sum_{1\le p<t\le c}|C_p|\,|C_t|.                \tag{2.2b}
\]

Filtering (2.2a) by output rank gives the exact rank-depth ledger. If
\(x_q^{\rm old}(Z)\) and \(x_q^{\rm new}(Z)\) are the old and new
cross-block multiplicities of a rank-\((r+q)\) target \(Z\), then

\[
m_q^{\rm new}(Z)-m_q^{\rm old}(Z)
 =x_q^{\rm new}(Z)-x_q^{\rm old}(Z).                  \tag{2.2c}
\]

In particular, rank depth \(q\) is not synonymous with window length
\(q+1\) unless a geodesic/no-return hypothesis is separately available.

### Theorem 2.1 (complete block-deck identity)

For every block reroot,

\[
\mathcal D(T')=
 \bigcup_{i=1}^{c}\mathcal D(B_i)
 \ \cup\!
 \bigcup_{1\le i<j\le c}\mathcal L(C_i,\ldots,C_j).     \tag{2.2}
\]

The internal bank \(\bigcup_i\mathcal D(B_i)\) is independent of all block
orientations and of the block order. All possible losses and additions are
therefore confined exactly to the old and new cross-block ladders.

#### Proof

An interval either lies in one block or meets a consecutive run of at least
two blocks. In the latter case it consists of a nonempty suffix of its first
block, every intervening block in full, and a nonempty prefix of its last
block. This is exactly (2.1). Reversal preserves the internal interval-OR
set of each block. ∎

Suppose now that every \(T_i\) has rank \(r\), and let

\[
\mathcal U_q=\binom{[k]}{r+q}.
\]

Write \(K_q\) for the rank-\((r+q)\) slice of the internal bank and
\(L'_q\) for the same rank slice of all new ladders in (2.2).

### Theorem 2.2 (protected-bank plus boundary-ladder criterion)

The rerooted word covers the complete upper tower if and only if

\[
\mathcal U_q\subseteq K_q\cup L'_q
\qquad(1\le q\le k-r).                                 \tag{2.3}
\]

Equivalently, let \(\mathcal V\) be the old covered family and
\(\mathcal H\) its complement in the required upper tower. The reroot is
complete if and only if:

1. every \(Z\in\mathcal V\) has positive multiplicity in the internal bank
   plus the new cross-block bank; and
2. every \(Z\in\mathcal H\) has positive new cross-block multiplicity.

The convenient protected-bank sufficient condition is stronger: give every
\(Z\in\mathcal V\) one block-internal witness and every
\(Z\in\mathcal H\) one new ladder witness.

#### Proof

Take the rank slices of the exact identity (2.2). ∎

### Proposition 2.3 (nested boundary rays)

At one separated seam \(A\Vert B\), choose integers \(t_q\) with

\[
1\le t_q\le q,
\qquad t_q\le|A|,
\qquad q+1-t_q\le|B|,
\qquad t_{q+1}-t_q\in\{0,1\}.                           \tag{2.4}
\]

Then the windows

\[
J_q=\operatorname{suf}_{t_q}(A)
    \Vert\operatorname{pre}_{q+1-t_q}(B)                \tag{2.5}
\]

are nested as \(q\) increases. Hence one seam repairs an entire defect ray
\((Z_q)\) whenever \(Z_q=\bigvee J_q\) at every required depth. If the
unprotected defect tower partitions into \(h=O(d)\) such rays and the old
covered family has a protected bank, \(h\) seams suffice for the full tower.

#### Proof

From depth \(q\) to \(q+1\), condition (2.4) adds exactly one entry, on the
left if \(t_{q+1}=t_q+1\) and on the right otherwise. ∎

For fixed \((q+1)\)-window defects, \(h\) separated seams offer at most
\(hq\) slots at depth \(q\) and at most
\(hD(D+1)/2\) slots through depth \(D\). Thus necessary counting conditions
for \(h_q\) unprotected distinct fixed-window defects are

\[
h\ge\max_q\left\lceil\frac{h_q}{q}\right\rceil,
\qquad
h\ge\left\lceil
 \frac{2\sum_{q=1}^{D}h_q}{D(D+1)}
\right\rceil.                                           \tag{2.6}
\]

These counts are not sufficient without the actual OR identities. In
particular, no dimension-only theorem says that \(O(d)\) seams repair an
arbitrary exponentially large defect tower. They suffice precisely for a
protected carrier whose residual defects satisfy (2.3), for example the
nested-ray hypothesis above. A single arbitrary-width seam ladder may have
slices at many ranks, so the full-deck theorem is stronger than the
fixed-window count.

## 3. Endpoint reroot as the three-block specialization

Take

\[
B_1=T[0,a],\qquad B_2=T[a+1,b-1],\qquad B_3=T[b,N-1]
\]

and reroot as

\[
T'=\operatorname{rev}(B_1)\Vert B_2\Vert
   \operatorname{rev}(B_3).                            \tag{3.1}
\]

There are exactly two changed seams. Its adjacent-union multiset is

\[
\begin{aligned}
\mu_1(T')=\mu_1(T)
 &-\delta_{T_a\vee T_{a+1}}
  -\delta_{T_{b-1}\vee T_b}\\
 &+\delta_{T_0\vee T_{a+1}}
  +\delta_{T_{b-1}\vee T_{N-1}}.                     \tag{3.2}
\end{aligned}
\]

The complete new cross-block bank consists of a left endpoint ladder, a
right endpoint ladder, and one two-seam ladder. This is exactly the
three-family decomposition used by the genuine-four-filter K16 carrier.

For K16, \(a=6388\), \(b=12826\). The two new q1 seams install `d3cc` and
`b3cc`; the endpoint ladders also install

```text
d3ce f3cc dbce fbce.
```

The three block lengths are 6389, 6437, and 44. Hence both seams are buffered
through depth eight and contribute exactly \(2q\) crossing
\((q+1)\)-windows at every \(q\le8\), 72 shallow crossing windows in total.
The authenticated replay shows that all 39,197 old distinct middle/upper
interval values retain a block-internal witness, while the new ladders add
precisely the six displayed missing masks. Hence (2.3) holds at every rank,
giving the authenticated carrier SHA

```text
c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906.
```

## 4. Relation to the exact lower-bound slack

Let

\[
W=\binom{k}{r},\qquad
\Lambda=\sum_{j=1}^{r-1}\binom{k}{j},
\]

and let \(d=d(k)\) be minimal with

\[
dW+\binom{d+1}{2}\ge\Lambda.                          \tag{4.1}
\]

At length \(B(k)=W+d\), write \(m\) for the actual number of usable lower
cells in a scalar-viable compiler schedule and

\[
s=m-\Lambda                                             \tag{4.2}
\]

for its schedule surplus. Also define the raw deadline-capacity surplus

\[
\sigma=dW+\binom{d+1}{2}-\Lambda.                      \tag{4.2a}
\]

For \(d\ge1\), scalar viability and minimality give

\[
0\le s\le\sigma\le W+d-1.                              \tag{4.3}
\]

Indeed, \(m\le dW+\binom{d+1}{2}\), while minimality and integrality give

\[
\Lambda\ge(d-1)W+\binom d2+1.
\]

The case \(d=0\) is trivial. There is no automatic positive lower bound on
either \(s\) or \(\sigma\), and neither should be confused with the length
slack \(d=B(k)-W\).

A block reroot is a permutation/orientation of the \(W\) middle states and
therefore consumes no length slack. Suppose, as an additional architectural
hypothesis, that each of \(c_j\) collar letters for seam \(j\) must occupy a
position outside \(W\) distinct chosen middle deadlines (equivalently, it is
charged as an added position beyond a \(W\)-position baseline). Then exact
length \(W+d\) requires

\[
\sum_j c_j\le d                                          \tag{4.3a}
\]

within the one common schedule. Without this disjoint-position hypothesis,
a collar letter may lie in many middle witnesses and no such charge follows.

By contrast, in a monotone P/Q retiming with fixed starts and an unchanged
boundary-restitution catalogue, deadline displacement \(\tau\) preserves
word length and lowers the proper-prefix inventory, hence the raw schedule
surplus, by exactly \(\tau\). Provider feasibility may still change
nonlinearly. These are different budgets.

### Proposition 4.1 (conservative seam-quarantine budget)

Assume that \(h\) changed middle seams are, as an additional hypothesis,
aligned with \(h\) specified physical cut positions in the length-\(W+d\)
compiler word. Quarantine every usable catalogue cell which is a physical
interval of length \(2,\ldots,d+1\) crossing one of those cuts. If the
remaining pin/retiming operations cost \(\tau\) additional lower cells, the
quarantine removes at most

\[
h\binom{d+1}{2}+\tau                                    \tag{4.4}
\]

cells. Consequently the raw post-quarantine cardinality remains viable
whenever

\[
h\binom{d+1}{2}+\tau\le s.                             \tag{4.5}
\]

#### Proof

At most \(\ell-1\) intervals of length \(\ell\) cross a fixed cut; equality
requires sufficient distance from both physical endpoints and the presence
of every such interval in the catalogue. Summing for
\(2\le\ell\le d+1\) gives \(\binom{d+1}{2}\). Overlap between cuts can only
reduce the union. ∎

Condition (4.5) proves only cardinality. It proves neither Hall nor common-Q.
A literal compiler may safely reuse many crossing cells, and an upper reroot
itself costs no word positions at all. A middle-chronology seam is not
automatically a physical compiler cut; that alignment is a genuine extra
hypothesis in Proposition 4.1.

### Corollary 4.2 (asymptotic versus exact use of \(O(d)\) seams)

If \(h=O(d)\), the chosen shallow physical-collar quarantine costs
\(O(d^3)\) cells. Since

\[
d(k)=\sqrt{\pi k/8}+O(1),
\]

this is \(O(k^{3/2})=o(W)\). It does not count the arbitrary-width
cross-block upper bank, whose correctness comes only from (2.3). If a
separate construction replaces every quarantined lower slot with \(O(1)\)
additional letters, or otherwise supplies a compiler after their deletion,
then the resulting additive overhead is \(o(W)\) and preserves coefficient
one. The count alone does not construct such a repair.

It does **not** automatically fit the exact value \(B(k)=W+d\), because the
schedule surplus \(s\) may be smaller than (4.4), or zero. Exact equality
requires both the upper ladder condition (2.3) and one literal common-Q
compiler of length \(W+d\). If that compiler quarantines the stated collars,
(4.5) prevents only a scalar deficit; Hall and common-Q remain mandatory.
Alternatively, the compiler may reuse the crossing cells directly.

This is the precise seam/slack boundary. The shallow collar charge of
\(O(d)\) seams is \(o(W)\), but converting it into an upper bound still
requires an upper-safe reroot and a literal repair/compiler construction.

## 5. General construction consequence

A dimension-uniform upper-shadow construction may now be split cleanly:

1. partition the middle chronology into blocks of length at least \(d\);
2. use at most \(O(d)\) reroot seams whose new ladder slices satisfy (2.3);
3. certify that every old cross-seam-only target is protected; and
4. couple the resulting chronology to one literal common-Q compiler;
   Proposition 4.1 is only a scalar screen for a quarantine-based route.

The first three items completely settle the upper tower. The fourth is a
lower/common-Q question and must not be inferred from upper-shadow counts.

For K16 all four items are realized: two endpoint seams repair the complete
upper tower, singleton retiming costs two cells, and the exact common-cap
matching decodes to `answers/k16.word`, SHA-256

```text
890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe.
```

Here the raw surplus is \(\sigma=12284\), while the actual c7be schedule
surplus is \(s=5898\); contracting the singleton target and its reserved cell
leaves \(s\) unchanged. Neither number equals the length slack \(d=3\).
