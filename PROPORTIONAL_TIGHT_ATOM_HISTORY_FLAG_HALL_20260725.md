# Proportional tight atoms: exact flag pools and the history-conditioned Hall gate

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver, or
computer experiment is used.

## 0. Outcome

This note gives a positive integral sufficient reduction for the
proportional tight-atom matching problem.  It is not claimed to be
equivalent to every possible atom matching.

The start sets may be chosen so that every start carries one saturated
symmetric flag and the flag radii are nondecreasing from left to right.
An arbitrary symmetric-chain decomposition of the Boolean lattice then
supplies exactly `p` flags at every start, with **all target sets in all
start pools globally distinct**.  Consequently target-disjointness can be
settled before physical rows are assembled.  The remaining problem is to
route these flags through the starts as coherent injective interval words.

For this routing problem an exact Hall-deficiency recurrence is proved.  If
the history-conditioned extension graph at every seam has additive Hall
deficiency at most

\[
  C\frac{p}{m^2}+1,
\]

then the final atom leave is at most

\[
  C\frac{bp}{m^2}+b
  =O(p m^{-5/4})
  =o(p/\sqrt m).
\]

Thus the `O(m^{-2})` scale really is more than sufficient **when it is an
expansion bound for conditioned whole-flag histories**.  The previously
proved `O(m^{-2})` noncover row sum is not such a bound: it controls a
second intersection after one target has already collided, whereas the
Hall inequality below controls the number of distinct extendible physical
histories.

For comparison, the unrestricted adjacent compatibility graph on complete
saturated flags is proved to be biregular and to have exact normalized
Hall expansion; all its degrees are computed.  There is also an
unconditional literal-strip theorem:

\[
\nu_{\rm strip}\ge
\left(\sum_q\frac{c_q^2}{N_q}\right)^{-1}.
\]

For the initial block of the exact increasing-radius profile this packs
`p` target-disjoint literal strips through every
`L=o(m^(1/4))`, and even through
`L<=lambda_0 m^(1/4)` for the explicit positive constant in (3.19a).

What remains unproved is
that this expansion survives restriction to the globally target-disjoint
flag pools and to the history imposed by earlier starts.  A four-set
Boolean diamond shows that perfect Hall expansion on every individual
cover side does not imply this simultaneous extension property.

No proportional atom matching, literal word, or constant-one conclusion is
claimed here.  The theorem-level advance is the exact integral flag-pool
reduction and the quantitatively sufficient history-conditioned expansion
inequality.

## 1. Exact proportional radii with a favorable orientation

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 b=\lfloor m^{3/4}\rfloor,\qquad
 p=\left\lfloor\frac Wb\right\rfloor,
\]

and retain the Gaussian band and proportional quotas

\[
 N_q=\binom n{m+q},\qquad
 b_q=\left\lfloor\frac{N_q}{p}\right\rfloor
 \quad(-H\le q\le H+1).
\tag{1.1}
\]

For all sufficiently large `m`,

\[
 b_0=b_1=b.
\tag{1.2}
\]

Binomial symmetry gives, exactly,

\[
 b_{-d}=b_{d+1}\qquad(0\le d\le H).
\tag{1.3}
\]

Write

\[
 \beta_d=b_{-d}=b_{d+1},\qquad
 a_d=\begin{cases}
 \beta_d-\beta_{d+1},&0\le d<H,\\
 \beta_H,&d=H.
 \end{cases}
\tag{1.4}
\]

The sequence `beta_d` is nonincreasing, every `a_d` is a nonnegative
integer, and

\[
 \sum_{d=0}^H a_d=\beta_0=b.
\tag{1.5}
\]

Choose a nondecreasing radius sequence

\[
 d(0)\le d(1)\le\cdots\le d(b-1)
\tag{1.6}
\]

which contains exactly `a_d` copies of `d`.  Define the start sets by

\[
 I_{-d}=I_{d+1}=\{i:d(i)\ge d\}
 \qquad(0\le d\le H).
\tag{1.7}
\]

Then `|I_q|=b_q` exactly.  At start `i` the designated depths are exactly

\[
 -d(i),-d(i)+1,\ldots,d(i),d(i)+1.
\tag{1.8}
\]

Thus the targets at one start form a saturated flag

\[
 A_{i,-d(i)}\subset A_{i,-d(i)+1}\subset\cdots
 \subset A_{i,d(i)+1}.
\tag{1.9}
\]

The nondecreasing order in (1.6) is optional for the original atom
reduction, but it is the favorable routing orientation: passing from start
`i` to `i+1` never truncates a larger flag to a smaller one without adding
new endpoint choices.

## 2. Exact globally disjoint flag pools

Let a symmetric chain of radius `r` mean a chain beginning in rank `m-r`
and ending in rank `m+r+1`.

### Theorem 2.1 (integral target-disjoint start pools)

There are families

\[
 \mathscr F_i\qquad(0\le i<b)
\tag{2.1}
\]

with the following properties.

1. `mathscr F_i` consists of exactly `p` saturated flags of radius `d(i)`.
2. Every set occurring in any flag in any `mathscr F_i` is distinct from
   every set occurring in every other flag.
3. At rank `m+q`, the union of the pools contains exactly `p b_q` sets.

All objects in this theorem are integral.

#### Proof

Fix a symmetric-chain decomposition `mathscr D` of the Boolean lattice.
Let `mathscr D_{>=d}` be the chains of radius at least `d`.  Every chain in
this family contains one set in rank `m-d`, and every set of that rank is
on one such chain.  Hence

\[
 |\mathscr D_{\ge d}|=N_{-d}.
\tag{2.2}
\]

Put

\[
 M_d=p\beta_d=p b_{-d}.
\tag{2.3}
\]

Choose nested chain-index sets

\[
 K_H\subseteq K_{H-1}\subseteq\cdots\subseteq K_0,
 \qquad K_d\subseteq\mathscr D_{\ge d},
 \qquad |K_d|=M_d.
\tag{2.4}
\]

This is possible recursively.  If `K_{d+1}` has been chosen, then

\[
 |\mathscr D_{\ge d}\setminus K_{d+1}|
 =N_{-d}-M_{d+1}
 \ge M_d-M_{d+1},
\tag{2.5}
\]

because `M_d<=N_{-d}`.

For a chain in `K_0`, retain only its central segment out to the largest
`d` for which it lies in `K_d`.  The number of retained segments of exact
radius `d` is

\[
 M_d-M_{d+1}=p a_d\quad(d<H),
 \qquad M_H=p a_H.
\tag{2.6}
\]

There are exactly `a_d` starts of radius `d`.  Partition the `p a_d`
segments of that radius into those start pools, putting `p` segments in
each pool.  This proves item 1.

Distinct retained segments lie on distinct chains of one symmetric-chain
decomposition, so none of their Boolean sets are equal.  This proves item
2.  A retained segment meets rank `m-d` (and, symmetrically, rank
`m+d+1`) exactly when its radius is at least `d`; there are `M_d=p b_{-d}`
such segments.  This proves item 3.  ∎

Theorem 2.1 removes all target collisions before any row ownership is
chosen.  The remaining question is whether the flags can be ordered into
literal tight rows.

## 3. Exact unrestricted Hall expansion for whole flags

Let `Phi_d` be the set of all saturated flags

\[
 F_{-d}\subset F_{-d+1}\subset\cdots\subset F_{d+1},
 \qquad |F_q|=m+q.
\tag{3.1}
\]

Here `(z)_r=z(z-1)\cdots(z-r+1)` and `(z)_0=1`.

Choosing the bottom set and then ordering the `2d+1` added elements gives

\[
 \boxed{
 |\Phi_d|
 =\binom n{m-d}(m+d+1)_{2d+1}
 =\frac{n!}{(m-d)!^2}.}
\tag{3.2}
\]

For radii `0<=d,e<=H` (and all sufficiently large `m`, so `H<=m-1`),
join `F in Phi_d` to `G in Phi_e` if they can occur at
two consecutive starts of one injective interval word.  Call this the
adjacent flag-compatibility graph `C_{d,e}`.

### Theorem 3.1 (biregularity and normalized flag Hall)

The graph `C_{d,e}` is nonempty and biregular.  Consequently, for every
`A subseteq Phi_d`,

\[
 \boxed{
 \frac{|N(A)|}{|\Phi_e|}
 \ge
 \frac{|A|}{|\Phi_d|}.}
\tag{3.3}
\]

If `e=d`, both degrees equal

\[
 \boxed{(m-d)^2.}
\tag{3.4}
\]

If `e>=d+1`, the degree on the `Phi_d` side is

\[
\boxed{
 (m-d)(m-d-1)_{e-d-1}(m-d)_{e-d+1}.}
\tag{3.5}
\]

If `e<=d-1`, the degree on the `Phi_d` side is

\[
 \boxed{m-d.}
\tag{3.6}
\]

#### Proof

The symmetric group on `[n]` is transitive on `Phi_d`, transitive on
`Phi_e`, and preserves physical compatibility.  The graph is nonempty by
taking two consecutive starts in any injective word.  Therefore its degree
is constant on each side.

Double-counting edges between `A` and `N(A)` gives

\[
 d_L|A|\le d_R|N(A)|,
\]

while double-counting all edges gives

\[
 d_L|\Phi_d|=d_R|\Phi_e|.
\]

Division proves (3.3).

In particular, when `e>=d`, (3.2)--(3.3) give the explicit expansion

\[
 |N(A)|\ge
 \left(\frac{(m-d)!}{(m-e)!}\right)^2|A|.
\tag{3.3a}
\]

For a strict radius increase this factor is larger than one; for equal
radii it is exactly one.

It remains to audit the displayed degrees.  Fix `F in Phi_d`.  If the next
flag has the same radius, choose the label at the old left endpoint from
the bottom `F_{-d}` (`m-d` choices), and choose the one new right-end label
outside the top `F_{d+1}` (`m-d` choices).  This proves (3.4).

Suppose `e>=d+1`.  First choose the old left-end label in `m-d` ways.  The
overlap of the two flags then fixes the next flag from rank `m-d-1` through
rank `m+d`.  Extending it down to rank `m-e` requires an ordered choice of
`e-d-1` elements from a set of size `m-d-1`.  Extending it up to rank
`m+e+1` requires an ordered choice of `e-d+1` new elements.  The old
left-end label cannot be reused, leaving exactly `m-d` available labels at
the first upper step.  This gives (3.5).

Finally suppose `e<=d-1`.  Once the old left-end label is chosen from
`F_{-d}`, every member of the shorter next flag is forced by

\[
 G_{q-1}=F_q\setminus\{x\}.
\tag{3.7}
\]

Different choices of `x` give different flags, proving (3.6).  ∎

Theorem 3.1 is a genuine simultaneous Hall theorem for an entire saturated
endpoint flag.  It is stronger than applying Boolean shadow Hall to each
cover separately.  It is nevertheless unrestricted: (3.3) says nothing
about the intersection of `N(A)` with a target-disjoint pool chosen from
one symmetric-chain decomposition.

The increasing-radius order (1.6) avoids (3.6).  In the decreasing
orientation, after the earlier word history has fixed the old left-end
label, a strict radius drop has a unique next flag.  Thus a decreasing
profile creates forced images rather than an expanding extension graph.

### Theorem 3.2 (unconditional packing of short physical flag strips)

Fix `L>=1` consecutive starts and prescribed radii

\[
 0\le d_0,\ldots,d_{L-1}\le D,
 \qquad L+D\le m+1.
\]

At start `i`, require the complete saturated flag of radius `d_i`.  Put

\[
 c_q=|\{i:-d_i\le q\le d_i+1\}|,
 \qquad
 k=\sum_qc_q=\sum_{i=0}^{L-1}(2d_i+2),
\tag{3.8}
\]

and let

\[
 N_{\min}=N_{-D}=N_{D+1}.
\]

The simple hypergraph of literal injective `L`-start strips has a matching
of size at least

\[
 \boxed{
 \left(\sum_q\frac{c_q^2}{N_q}\right)^{-1}
 \ge\frac{N_{\min}}{kL}.}
\tag{3.9}
\]

In particular it has `p` pairwise target-disjoint literal strips whenever

\[
 \boxed{
 p\sum_q\frac{c_q^2}{N_q}\le1.}
\tag{3.10}
\]

The simpler sufficient condition `p kL<=N_min` follows immediately.

Uniformly for `D<=A sqrt(m)` with fixed `A`, condition (3.10) holds for

\[
 L=o_A(m^{1/8}).
\tag{3.11}
\]

#### Proof

Let `E` be the number of distinct strip target systems.  Coordinate
permutations act transitively on these systems: map the injective position
labels of one realizing word to those of another and extend the map to a
permutation of `[n]`.  A strip contains exactly `c_q` distinct targets in
rank `m+q`.  Coordinate transitivity within that rank and incidence double
counting therefore give the exact vertex degree

\[
 \deg_q=\frac{c_qE}{N_q}.
\tag{3.12}
\]

Take a maximal strip matching of size `s`.  Every one of the `E` strip
edges meets a selected edge.  One selected edge has `k` vertices and hence
meets, with multiplicity, at most

\[
 \sum_q c_q\deg_q
 =E\sum_q\frac{c_q^2}{N_q}
\tag{3.13}
\]

strip edges.  Thus

\[
 E\le sE\sum_q\frac{c_q^2}{N_q},
 \qquad
 s\ge\left(\sum_q\frac{c_q^2}{N_q}\right)^{-1}.
\]

Since `c_q<=L`, `sum_q c_q=k`, and `N_q>=N_min`,

\[
 \sum_q\frac{c_q^2}{N_q}
 \le\frac{kL}{N_{\min}}.
\]

This proves (3.9)--(3.10).

If `D<=A sqrt(m)`, the local central estimate gives

\[
 N_{\min}=\Theta_A(W),
 \qquad
 \frac{N_{\min}}p=\Theta_A(b).
\]

Also `k<=L(2D+2)=O_A(L sqrt(m))`.  Therefore

\[
 \frac{pkL}{N_{\min}}
 =O_A\left(\frac{L^2\sqrt m}{b}\right)=o(1)
\]

under (3.11), proving the last assertion.  ∎

This is a genuine growing-length, integral, literal packing theorem.  It
does not concatenate independently chosen strips: target-disjointness and
word state across the seams between strips remain the history problem in
the next section.

### Corollary 3.3 (exact residual strip-expansion bound)

For each rank in the strip, let

\[
 \mathcal U_q\subseteq\binom{[n]}{m+q}
\]

be a forbidden target family.  Put

\[
 \theta(\mathcal U)=\sum_q
   \frac{c_q|\mathcal U_q|}{N_q},
 \qquad
 \sigma=\sum_q\frac{c_q^2}{N_q}.
\tag{3.14}
\]

The hypergraph of literal strips avoiding every forbidden target has a
matching of size at least

\[
 \boxed{
 \frac{(1-\theta(\mathcal U))_+}{\sigma}.}
\tag{3.15}
\]

#### Proof

A fixed forbidden rank-`q` target belongs to exactly `c_qE/N_q` strips.
The union bound therefore shows that at least

\[
 E_{\rm free}
 \ge E\left(1-\sum_q
       \frac{c_q|\mathcal U_q|}{N_q}
       \right)
 =E(1-\theta(\mathcal U))
\tag{3.16}
\]

strips survive.  Restriction cannot increase any vertex degree above its
unrestricted value.  Hence one free strip meets at most

\[
 E\sum_q\frac{c_q^2}{N_q}=E\sigma
\]

free strips, with multiplicity.  A maximal free matching consequently has
size at least `E_free/(E sigma)`, which is (3.15).  ∎

Corollary 3.3 is hereditary and interval-specific, but its first-order
union bound becomes vacuous near global saturation.  The history Hall
condition below is the stronger correlated residual inequality needed
there.

### Theorem 3.4 (the initial increasing-radius block reaches `o(m^(1/4))`)

Take the exact nondecreasing radius profile (1.6), and restrict it to its
first `L` starts.  Let `c_q(L)` be the strip multiplicities (3.8).  If

\[
 L=o(m^{1/4}),
\tag{3.17}
\]

then, uniformly with all proportional floors retained,

\[
 \boxed{
 p\sum_q\frac{c_q(L)^2}{N_q}=o(1).}
\tag{3.18}
\]

Consequently, for all sufficiently large `m`, the first `L` starts have
`p` pairwise target-disjoint literal strip realizations.  Their maximum
radius `D_L` also satisfies

\[
 D_L=O\left(\sqrt{\frac{m(L+1)}b}\right),
\tag{3.19}
\]

so the necessary word-length condition `L+D_L<=m+1` holds automatically.

In fact, with `gamma_0=1-e^{-1/2}`, the same conclusion holds uniformly for

\[
 L\le\lambda_0m^{1/4},
 \qquad
 \lambda_0=\left(\frac{\sqrt{\gamma_0}}{16}\right)^{2/5},
\tag{3.19a}
\]

for all sufficiently large `m`.

More quantitatively,

\[
 \boxed{
 p\sum_q\frac{c_q(L)^2}{N_q}
 \le
 \frac4{\sqrt{\gamma_0}}
 \frac{(L+1)^{5/2}\sqrt m}{b^{3/2}}
 +\frac{4(L+1)^2}{b}.}
\tag{3.20}
\]

#### Proof

Recall `beta_h=b_{-h}=b_{h+1}`.  Among all `b` starts, exactly
`b-beta_h` have radius less than `h`.  Since the radii are in
nondecreasing order, the number of radius-at-least-`h` starts in the first
`L` positions is exactly

\[
 t_h:=c_{-h}(L)=c_{h+1}(L)
 =\bigl(L-b+\beta_h\bigr)_+.
\tag{3.21}
\]

Put

\[
 R_h=\frac{N_{-h}}W
 =\prod_{j=0}^{h-1}\frac{m-j}{m+2+j}
 =\prod_{j=0}^{h-1}\left(1-\frac{2(j+1)}{m+2+j}\right).
\tag{3.22}
\]

For all large `m`, `H<m-1`.  Therefore

\[
 R_h
 \le\exp\left(-\sum_{j=0}^{h-1}
             \frac{2(j+1)}{m+2+j}\right)
 \le\exp\left(-\frac{h^2}{2m}\right)
 \qquad(0\le h\le H).
\tag{3.23}
\]

The elementary inequality

\[
 1-e^{-x/2}\ge \gamma_0\min(x,1),
 \qquad \gamma_0=1-e^{-1/2},
\]

now gives

\[
 1-R_h\ge \gamma_0\min(h^2/m,1).
\tag{3.24}
\]

The floor is harmless but must be kept.  Since `W/p<b+1`,

\[
 \beta_h=\left\lfloor\frac{N_{-h}}p\right\rfloor
 \le R_h\frac Wp<R_h(b+1),
\]

and hence

\[
 b-\beta_h\ge b(1-R_h)-1.
\tag{3.25}
\]

Equations (3.21), (3.24), and (3.25) imply

\[
 t_h\le
 \left(L+1-\gamma_0b\min(h^2/m,1)\right)_+.
\tag{3.26}
\]

Because `(L+1)/b=o(1)`, every `h` with `t_h>0` satisfies

\[
 h\le
 T:=\sqrt{\frac{m(L+1)}{\gamma_0b}}.
\tag{3.27}
\]

This proves (3.19).  Moreover `T^2/m=o(1)`.  Uniformly for `h<=T`, the
product (3.22) is `1-o(1)` (use
`log(1-z)>=-2z` once `z<=1/2`).  In particular

\[
 N_{-h}\ge W/2
\tag{3.28}
\]

for all active `h` and all sufficiently large `m`.

Using the exact symmetric pairing of ranks,

\[
 p\sum_q\frac{c_q(L)^2}{N_q}
 =2p\sum_{h=0}^H\frac{t_h^2}{N_{-h}}
 \le\frac4b\sum_{0\le h\le T}t_h^2,
\tag{3.29}
\]

where `p<=W/b` was used.  Finally (3.26) gives the simple uniform bound

\[
 \sum_{0\le h\le T}t_h^2
 \le(T+1)(L+1)^2.
\tag{3.30}
\]

Substitution of (3.27) into (3.29)--(3.30) proves (3.20).  Since
`b=floor(m^(3/4))`, both terms in (3.20) tend to zero under (3.17).
Theorem 3.2 then supplies the `p` literal strips.  Also
`L+D_L=o(m^(1/4))+O(m^(1/4))=o(m)`, proving the word-length condition.
If (3.19a) holds, the first term in (3.20) has limsup at most `1/4`
because `b/m^(3/4)->1`, while the second tends to zero.  Thus (3.10)
again holds for all sufficiently large `m`, with the floor in `b` fully
retained.
∎

## 4. The exact history-conditioned Hall recurrence

A sequence

\[
 (F_0,F_1,\ldots,F_i),
 \qquad F_j\in\mathscr F_j,
\tag{4.1}
\]

is called a **coherent history** if one injective coordinate word of the
full atom-template length realizes all its flags as the designated interval
flags at starts `0,...,i`.

A routed family `mathscr R_i` is a collection of coherent histories such
that no two histories use the same flag from any pool.  Start with the `p`
one-flag histories

\[
 \mathscr R_0=\{(F):F\in\mathscr F_0\}.
\tag{4.2}
\]

Every single saturated flag has such a realization: order its bottom set
arbitrarily, use the successive one-point differences for its right-end
extensions, and fill unused word positions with unused coordinates.

Given a routed family `mathscr R_i`, form a bipartite graph between its
histories and the next pool `mathscr F_{i+1}`.  Join a history `R` to a flag
`F` exactly when appending `F` gives a coherent history.  For
`X subseteq mathscr R_i`, write `Gamma_i(X)` for its neighborhood and put

\[
 \delta_i(\mathscr R_i)
 =\max_{X\subseteq\mathscr R_i}
   \bigl(|X|-|\Gamma_i(X)|\bigr)_+.
\tag{4.3}
\]

### Theorem 4.1 (exact routing-deficiency recurrence)

From `mathscr R_i` one can construct a routed family `mathscr R_{i+1}`
with

\[
 \boxed{
 |\mathscr R_{i+1}|
 =|\mathscr R_i|-\delta_i(\mathscr R_i).}
\tag{4.4}
\]

Consequently, if numbers `Delta_i` satisfy

\[
 \delta_i(\mathscr R_i)\le\Delta_i
\tag{4.5}
\]

for every routed family reachable by this procedure, then the proportional
atom hypergraph has a matching of size at least

\[
 \boxed{
 p-\sum_{i=0}^{b-2}\Delta_i.}
\tag{4.6}
\]

#### Proof

The deficiency form of Hall's theorem says that the maximum matching in a
bipartite graph with left side `L` has size

\[
 |L|-\max_{X\subseteq L}(|X|-|N(X)|).
\tag{4.7}
\]

Apply this to the extension graph.  Retain the matched histories and append
their matched next flags.  This gives (4.4), and iteration gives (4.6).

At the last start, every surviving history is one literal injective atom.
No two such atoms share a target, because every target in every flag pool
was globally distinct in Theorem 2.1.  Hence the histories form an atom
matching.  ∎

The exact additional expansion inequality is now explicit.

> **History-conditioned flag Hall, `HFH(eta_i)`.**  For every routed family
> `mathscr R_i` reachable from (4.2), and every
> `X subseteq mathscr R_i`,
> \[
> |\Gamma_i(X)|\ge |X|-\eta_i p-1.
> \tag{HFH}
> \]

### Corollary 4.2 (the `m^{-2}` expansion scale is sufficient)

If `(HFH)` holds with

\[
 \eta_i\le C/m^2
 \qquad(0\le i<b-1)
\tag{4.8}
\]

for one absolute constant `C`, then the atom matching has size at least

\[
 p-C\frac{bp}{m^2}-b
 =p-O(p m^{-5/4}).
\tag{4.9}
\]

In particular its leave is `o(p/sqrt(m))`.

#### Proof

Under (4.8), equations (4.3) and `(HFH)` give

\[
 \Delta_i\le Cp/m^2+1.
\]

Sum this over at most `b-1` seams and use
`b=floor(m^(3/4))`.  The additive `b` is negligible compared with
`p/sqrt(m)`, and

\[
 \frac{bp}{m^2}=p m^{-5/4+o(1)}=o(p/\sqrt m).
\]

Apply Theorem 4.1.  ∎

More generally, (4.6) shows that the exact sufficient threshold is

\[
 \sum_{i=0}^{b-2}\Delta_i=o(p/\sqrt m).
\tag{4.10}
\]

This recurrence has `b` stages, not edge rank
`kappa=Theta(b sqrt(m))`, because every adjacent-rank flag at one start is
transported as one dependent object.

## 5. Pairwise Boolean Hall does not synchronize a diamond

The need to condition on whole histories is already visible in one exact
Boolean diamond.  Consider the following four two-element pools:

\[
\begin{array}{c|cc}
\text{pool}&1&2\\ \hline
B&\{1\}&\{2\}\\
X&\{1,3\}&\{2,4\}\\
Y&\{1,4\}&\{2,3\}\\
T&\{1,2,3\}&\{1,2,4\}.
\end{array}
\tag{5.1}
\]

Use ordinary inclusion on each of the four sides `B-X`, `B-Y`, `X-T`,
and `Y-T`.  The first three side graphs have the identity as their unique
perfect matching, while `Y-T` has the transposition as its unique perfect
matching.  Thus every side separately satisfies perfect Hall expansion.

There is nevertheless no coherent diamond.  Starting at `{1}` forces
`{1,3}` on the `X` side and `{1,4}` on the `Y` side; the former lies only
under `{1,2,3}`, while the latter lies only under `{1,2,4}`.  The same
contradiction holds at `{2}`.  Hence the four-partite hypergraph of genuine
diamonds is empty.

This example is an actual Boolean inclusion configuration, not an abstract
incidence matrix.  It proves that even perfect Hall on all adjacent cover
graphs does not imply simultaneous endpoint synchronization.  The
neighborhood in `(HFH)` is taken only after the two branches have been
joined into one physical history, so it detects exactly this holonomy.

## 6. Relation to the local overlap estimates

The proportional atom calculation proves that after the adjacent-cover
terms are removed, the remaining conditional overlap row sum is
`O(m^{-2})`.  Corollary 4.2 shows that an `O(m^{-2})` **history Hall
deficiency per start seam** would be quantitatively stronger than needed.
It does not identify the two statements.

The row sum has the form

\[
 \Pr(\text{a second prescribed target collision}
       \mid\text{one target collision}),
\]

summed over targets of a test atom.  By contrast, `(HFH)` asks how many
distinct flags remain available to every set of already synchronized,
globally target-disjoint partial rows.  Conditioning on the SCD pools and
on the earlier word history can destroy both transitivity and the
unrestricted degrees in Theorem 3.1.  Therefore neither the
`O(m^{-2})` row sum nor normalized flag Hall (3.3) currently proves
`(HFH)`.

The precise remaining positive task is:

\[
\boxed{
\text{Choose the SCD segments and their radius-ordered start pools so that
`(HFH)` has total deficiency }o(p/\sqrt m).}
}
\tag{6.1}
\]

Proving the stronger uniform estimate (4.8) would immediately finish the
proportional matching lemma through Theorem 4.1.  It would preserve
integrality and literal contiguous-interval ownership at every step.

## 7. Audited boundary

### Proved

1. The proportional floor quotas admit the nondecreasing saturated-flag
   start profile (1.6)--(1.9).
2. One SCD supplies `b` pools of `p` flags with every target globally
   distinct and with all floor quotas exact.
3. The unrestricted adjacent whole-flag graph is biregular, has normalized
   Hall expansion, and has the exact degrees (3.4)--(3.6).
4. Every `D<=A sqrt(m)`, `L=o_A(m^(1/8))` shallow strip profile has `p`
   pairwise target-disjoint literal realizations, and (3.15) is an exact
   hereditary residual bound.  For the initial block of the exact
   increasing-radius profile, the range improves to `L=o(m^(1/4))`.
5. The history-conditioned Hall deficiency obeys the exact integral
   recurrence (4.4)--(4.6).
6. An additive `O(p/m^2)` deficiency at each of the `b` seams gives leave
   `O(p m^{-5/4})`, which is `o(p/sqrt(m))`.
7. Pairwise cover Hall is strictly weaker than history synchronization,
   even inside the Boolean lattice.

### Unproved

1. No choice of SCD and start-pool assignment is proved to satisfy
   `(HFH)`.
2. The unrestricted transitivity in Theorem 3.1 is not proved to survive
   the global target-disjointness and earlier-history conditioning.
3. The `O(m^{-2})` noncover row sum is not proved to bound the Hall
   deficiencies in (4.3).
4. Therefore this note does not prove the proportional matching lemma or
   constant one.
