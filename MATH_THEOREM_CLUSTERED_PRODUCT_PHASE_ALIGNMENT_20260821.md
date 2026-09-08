# Clustered product schedules: exact phase alignment and its upper-hole ledger

**Status (2026-08-21).**  Every assertion below is proved.  The note gives
three exact advances for the two-block FIFO product route.

1. The nested type schedules `tau_r=A^r B^(b-r)` are legal throughout the
   DCC payload range and every resulting product atom is internally simple
   throughout the DCC band.  Balance of the type word is not necessary.
2. With common local cyclic orders, these nested schedules have an exact
   phase monotonicity: at rank `b+q` different payload ranks never collide on
   the same phase diagonal, while at rank `b-q` the algebraic phase profiles
   cover without holes and have exactly the `q` repetitions forced by the
   phase-domain/range cardinalities.
   The collision-free upper map has its own sharp cost: a rigid one-to-one
   order-bank alignment leaves a `q/b` fraction of the central split profiles
   empty, and these holes sum to `(1/2-o(1))W_b` over the upper DCC band.
3. Pairing the two middle MSW factors gives an unconditional exact
   `q=+/-1` construction on the balanced split slices.  In contrast,
   independently relabeling the factors at different payload ranks leaves at
   least `(1/4-o(1)) binom(2b,b+1)` rank-`(b+1)` targets uncovered in
   expectation.

The note does **not** prove coherent full-band aggregation.  It removes
cross-payload collisions in the torus coordinate, but the resulting upper
holes are linear in aggregate under a rigid order-bank coupling.  Ordinary
rank-by-rank Baranyai--Katona factors neither provide the required common
local order coordinates nor reassign the outer-layer occurrence surplus into
those holes.  That nonrigid multirank coupling remains open.

## 1. Nested clustered schedules are legal and band-simple

Let `A` and `B` be disjoint `b`-sets with cyclic orders `alpha` and `beta`.
For `1<=r<=b-1`, define the cyclic type word

\[
 \tau_r=A^rB^{b-r}.                                  \tag{1.1}
\]

At an `A`-step emit the next symbol of the periodic stream `alpha`, and at a
`B`-step emit the next symbol of `beta`.  As usual, if `gcd(r,b)=1`, the
first `b^2` length-`b` windows enumerate

\[
 \{I_\alpha(i,r)\cup I_\beta(j,b-r):(i,j)\in\mathbb Z_b^2\}
                                                               \tag{1.2}
\]

exactly once.  The proof uses only the count vector `(r,b-r)`, not the
spacing of the type letters: at a fixed type phase, passage through one
period translates the stream counters by `(r,-r)`, which has order `b`.

### Lemma 1.1 (exact recurrence gap in one clustered stream)

Suppose one type occurs in a consecutive block of `c` phases in a period of
length `b`.  A fixed symbol in its `b`-cycle stream recurs after exactly `b`
events of that type.  Its minimum physical recurrence gap is

\[
 g_b(c)=b\left\lfloor{b\over c}\right\rfloor+(b\bmod c).       \tag{1.3}
\]

In particular,

\[
 g_b(c)\ge
 \begin{cases}
  2b,&c\le b/2,\\
  2b-c,&c>b/2.
 \end{cases}                                                   \tag{1.4}
\]

#### Proof

Number the consecutive type events inside one period by `0,...,c-1`.
Write `b=qc+s`, where `0<=s<c`.  Moving forward by `b` type events advances
by `q` whole periods and `s` positions inside the type block.  If the latter
move does not wrap, its physical length is `qb+s`; if it wraps, its length
is `qb+(b-c+s)`.  The first is smaller, proving (1.3).  Formula (1.4) is
immediate.  \(\square\)

### Theorem 1.2 (legal nested schedules with full internal band simplicity)

Let `H>=0`, assume

\[
 H+2\le r\le b-H-2,\qquad \gcd(r,b)=1,               \tag{1.5}
\]

and put `f=b+H+2`.  Then the product word from (1.1) has cyclic
same-symbol separation at least `f`.  Moreover, its `b^2` cyclic
length-`ell` windows are pairwise distinct simultaneously for every

\[
 b-H\le\ell\le b+1+H.                               \tag{1.6}
\]

#### Proof

Apply Lemma 1.1 first with `c=r`.  If `r<=b/2`, its recurrence gap is at
least `2b>=b+H+2`; if `r>b/2`, it is at least
`2b-r>=b+H+2` by (1.5).  For the `B` stream use `c=b-r`.  If `b-r<=b/2`
the same `2b` bound applies; otherwise the gap is at least
`2b-(b-r)=b+r>=b+H+2`.  This proves legality.

It remains to check the type-count hypothesis needed for internal
simplicity.  Both constant type runs have length at most `b-H-2`, so every
cyclic interval of length at least `b-H` contains at least one event of each
type.  An interval of length at most `b+H+1` contains at most one full type
period plus `H+1` further phases.  Hence its number of `A` events is at most

\[
 r+H+1\le b-1,
\]

and the same holds for `B`.  Thus every interval length in (1.6) contains
between `1` and `b-1` events of each type.

If two length-`ell` targets were equal, intersection with `A` and `B` would
give equal local interval sets.  A proper nonempty interval set in a cyclic
order of distinct symbols fixes its endpoint.  The two stream-counter pairs
would therefore agree, and the bijection in (1.2) would force the two times
to agree modulo `b^2`.  \(\square\)

For prime `b`, condition `gcd(r,b)=1` holds at every payload rank in (1.5).
The schedules (1.1) are nested: if phases are identified with
`Z_b={0,...,b-1}`, their `A`-phase sets are

\[
 P_r=\{0,1,\ldots,r-1\},\qquad P_r\subset P_{r+1}.    \tag{1.7}
\]

This nesting drives the multirank phase theorem.

## 2. Exact phase monotonicity at every offset

Normalize the initial stream counters so that, after a middle window ending
at type phase `p`, its counter pair lies on a fixed sum diagonal

\[
 D_p=\{(i,j)\in\mathbb Z_b^2:i+j=p\pmod b\}.          \tag{2.1}
\]

Changing the two initial stream origins only translates these diagonals, so
the same normalization may be imposed on every atom which uses a fixed pair
`(alpha,beta)`.

Fix `q` with `0<=q<=b`, and let

\[
 J_p(q)=\{p+1,p+2,\ldots,p+q\}\pmod b                \tag{2.2}
\]

be the next `q` type phases after a middle window at phase `p`.  Put

\[
 z_{r,p}(q)=|P_r\cap J_p(q)|.                         \tag{2.3}
\]

Define the algebraic profiles

\[
 \phi_p(r)=r+z_{r,p}(q),\qquad b+q-\phi_p(r),         \tag{2.4}
\]

and

\[
 \psi_p(r)=r-z_{r,p}(q),\qquad b-q-\psi_p(r).         \tag{2.5}
\]

Whenever the indicated upper window is simple--in particular for the DCC
band and the admissible payload range (1.5)--these are its two local target
sizes.  The lower suffix has the sizes in (2.5).  The upper endpoint counters
lie on `D_(p+q)` and the lower endpoint counters on `D_p`, independently of
`r`.

### Theorem 2.1 (upper injections and lower surjections in phase space)

For every fixed `p,q`,

\[
 \phi_p(r+1)-\phi_p(r)
   =1+1_{\{r\in J_p(q)\}}\in\{1,2\},                 \tag{2.6}
\]

and

\[
 \psi_p(r+1)-\psi_p(r)
   =1-1_{\{r\in J_p(q)\}}\in\{0,1\}.               \tag{2.7}
\]

Consequently:

1. `phi_p` is injective on `{0,...,b}`.  Its image has `b+1` elements in
   `{0,...,b+q}` and misses exactly `q` local ranks.
2. `psi_p` maps `{0,...,b}` onto `{0,...,b-q}`.  Across its `b` successive
   increments, exactly `q` are zero, so its fibers contain exactly `q`
   repeated adjacent transitions in total.

Thus, when admissible atoms at different payload ranks use the **same** local
cyclic orders and aligned counter origins, their rank-`(b+q)` targets cannot
collide on a fixed phase diagonal.  Algebraically, allowing the endpoint
schedules `r=0,b`, the lower map reaches every phase/local-rank coordinate
with only the repetitions in (2.7).  For genuine atoms restricted to a
payload interval `I`, the same lower conclusion holds for every local rank
whose full preimage under `psi_p` lies in `I`; no claim is made for the
truncated tail profiles.

#### Proof

Passing from `P_r` to `P_(r+1)` adds the single phase `r`.  Equations
(2.6)--(2.7) follow immediately.  Now `phi_p(0)=0`, `phi_p(b)=b+q`, and its
increments are positive, exactly `q` of them being two.  This proves the
first conclusion.  Likewise `psi_p(0)=0`, `psi_p(b)=b-q`; its increments are
zero or one, exactly `q` being zero.  It therefore visits every integer
between its endpoints, proving the second conclusion.

For the target statement, different base phases occupy different sum
diagonals by (2.1), while at one phase (2.6) permits at most one payload rank
for any prescribed upper local size.  Equation (2.7) gives the corresponding
lower multiplicity statement.  \(\square\)

The common-order hypothesis is essential.  Distinct interval sets in two
different cyclic orders can represent the same labelled target, and a
rank-`r` tight-cycle factor supplies no canonical identification with a
rank-`(r+1)` factor.  Theorem 2.1 removes the type-schedule/torus part of the
problem; it does not manufacture a coherent multirank order bank.

### Proposition 2.2 (the rigid upper-hole ledger is linear in aggregate)

Assume `b` is prime and fix `q>=1`.  For a local upper rank `s` satisfying

\[
                         2q\le s\le b-q,             \tag{2.8}
\]

the number of base phases `p` for which some payload rank `r` satisfies
`phi_p(r)=s` is exactly

\[
                              b-q.                   \tag{2.9}
\]

Consequently, for one common cyclic-order pair, the clustered schedules
cover exactly `b-q` of the `b` counter-sum diagonals at that local rank and
leave exactly `q` diagonals empty.  If a rigid one-to-one family of such
order pairs partitions the Cartesian target profile

\[
 \{S:|S\cap A|=s, |S\cap B|=b+q-s\},               \tag{2.10}
\]

then it misses exactly a `q/b` fraction of that profile.

Let

\[
 W_b={2b\choose b},\qquad M_q={2b\choose b+q},       \tag{2.11}
\]

and let `H` satisfy

\[
 H/\sqrt b\longrightarrow\infty,qquad H=o(b^{2/3}). \tag{2.12}
\]

If the same rigid phase-diagonal accounting is used on every central split
profile at every `1<=q<=H`, its upper-band missed-target ledger is at least

\[
 \sum_{q=1}^H\left({q\over b}-e^{-\Omega(b)}\right)M_q
   =\left({1\over2}-o(1)\right)W_b.                  \tag{2.13}
\]

Thus collision-free phase injection by itself is not a coefficient-one
solution.  A successful construction must use nonrigid order-bank
multiplicity or the outer-layer occurrence surplus to fill the skipped
diagonals.

There is enough surplus by volume at each individual rank.  Indeed

\[
 {W_b\over M_q}
 =\prod_{j=1}^q{b+j\over b-j+1}
 \ge\left(1+{1\over b}\right)^q
 \ge1+{q\over b},                                    \tag{2.13a}
\]

so

\[
 W_b-M_q\ge {q\over b}M_q.                           \tag{2.13b}
\]

The obstruction is therefore alignment, not scalar capacity: the rigid
bank leaves holes despite having enough occurrences elsewhere in the same
rank.

#### Proof

For fixed `r`, a cyclic interval of `q` phases in the clustered word has a
specified number `z` of `A` phases.  Under (2.8), all relevant `A` and `B`
runs have length at least `q`.  The number of phase intervals with `z=0` is
`b-r-q+1`, the number with `z=q` is `r-q+1`, and for every
`1<=z<=q-1` there are exactly two, one crossing each type boundary.

The equation `phi_p(r)=s` has `r=s-z`.  Summing the preceding counts over
`z=0,...,q` gives

\[
 (b-s-q+1)+(s-2q+1)+2(q-1)=b-q,                    \tag{2.14}
\]

which proves (2.9).  Each phase supplies one entire `b`-point counter-sum
diagonal, and Theorem 2.1 makes the contributing diagonals disjoint.  This
proves the exact `q/b` profile hole.

For a uniformly random rank-`(b+q)` target, `|S\cap A|` is hypergeometric
with mean `(b+q)/2` and variance `Theta(b)`.  Uniformly for `q<=H=o(b)`, the
profiles outside (2.8) have total mass `e^{-Omega(b)}M_q`.  Hence the central
profiles alone give the lower bound in (2.13).

Finally,

\[
 {M_q\over W_b}
 =\prod_{j=1}^q{b-j+1\over b+j}
 =\exp\left\{-{q^2\over b}+O\left({q^3\over b^2}\right)\right\} \tag{2.15}
\]

uniformly for `q<=H`.  Therefore

\[
 {1\over b}\sum_{q=1}^Hq{M_q\over W_b}
 =(1+o(1)){1\over b}\sum_{q=1}^Hq e^{-q^2/b}
 \longrightarrow\int_0^\infty x e^{-x^2}\,dx={1\over2}.       \tag{2.16}
\]

This proves (2.13).  \(\square\)

## 3. An unconditional adjacent-rank MSW alignment

The common-order hypothesis is available at the two local middle ranks.
Put

\[
 b=2h+1,qquad H\le h-2.                              \tag{3.1}
\]

Let `F` be an MSW middle-wreath factor on a `b`-set.  Its cyclic orders have
pairwise disjoint `h`-window decks which partition the rank-`h` layer.  The
same orders' `(h+1)`-window decks partition the rank-`(h+1)` layer by
complementation.  Hence

\[
 |\mathcal F|={1\over b}{b\choose h}.                 \tag{3.2}
\]

Use one such factor on each of `A,B`.  For every ordered pair
`(alpha,beta)` of factor orders, form both clustered atoms

\[
 (\alpha,\beta;\tau_h),\qquad
 (\alpha,\beta;\tau_{h+1}),                          \tag{3.3}
\]

with aligned stream-counter origins.

### Theorem 3.1 (exact `q=+/-1` balanced-slice accounting)

The atoms in (3.3) have the following properties.

1. Their middle decks partition exactly the two disjoint profiles

   \[
   \{|S\cap A|=h,|S\cap B|=h+1\},\qquad
   \{|S\cap A|=h+1,|S\cap B|=h\}.                    \tag{3.4}
   \]

2. At rank `b+1`, their targets in the balanced profile

   \[
   \mathcal U=\{|S\cap A|=|S\cap B|=h+1\}           \tag{3.5}
   \]

   are all distinct and cover exactly

   \[
   \left(1-{1\over b}\right){b\choose h}^2           \tag{3.6}
   \]

   of its `binom(b,h)^2` targets.

3. At rank `b-1`, they cover every target in

   \[
   \mathcal L=\{|S\cap A|=|S\cap B|=h\}.             \tag{3.7}
   \]

   The total number of occurrences there is

   \[
   \left(1+{1\over b}\right){b\choose h}^2,          \tag{3.8}
   \]

   so the exact repeated-occurrence mass is `binom(b,h)^2/b`.

All these atoms are legal at floor `b+H+2` and internally simple throughout
the band (1.6).

#### Proof

The middle statement is the Cartesian product of the two MSW window
partitions and (1.2).

Fix one pair `(alpha,beta)`.  A rank-`(b+1)` target in (3.5) comes either
from an `A` extension of the `r=h` atom or a `B` extension of the `r=h+1`
atom.  In phase coordinates these sources use, respectively,

\[
 P_h=\{0,\ldots,h-1\},\qquad
 P_{h+1}^{c}=\{h+1,\ldots,b-1\}.                    \tag{3.9}
\]

They are disjoint and omit exactly phase `h`.  Each phase diagonal contains
`b` counter pairs, so this order pair supplies `b^2-b` distinct upper
targets.

For (3.7), a lower target comes either by deleting a `B` letter from the
`r=h` middle window or an `A` letter from the `r=h+1` window.  The phase sets
are

\[
 P_h^{c}=\{h,\ldots,b-1\},\qquad
 P_{h+1}=\{0,\ldots,h\}.                              \tag{3.10}
\]

They cover every phase and overlap only at `h`.  Thus one order pair covers
all `b^2` lower coordinate targets, with exactly one repeated diagonal of
size `b`, and has `b^2+b` lower occurrences.

A proper local interval determines its factor order and endpoint because
the MSW decks partition both local middle ranks.  Consequently targets from
different order pairs cannot collide.  Multiply the per-pair counts by
`|F|^2=binom(b,h)^2/b^2` to obtain (3.6) and (3.8).  Legality and internal
simplicity follow from Theorem 1.2.  \(\square\)

With `W_b=binom(2b,b)`, each balanced split slice above has size
`Theta(W_b/sqrt(b))=o(W_b)`.  Theorem 3.1 is therefore a genuine exact
coherence result, but it is not by itself a coefficient-one construction.

## 4. Independent rank alignment has a one-quarter miss barrier

This section is conditional on the existence of the requisite tight-cycle
factors, but the negative conclusion applies to **any** such factors.
Let `b` be an odd prime.  At every local rank, independently conjugate an
arbitrary tight-cycle factor on `A` and on `B` by fresh uniform label
permutations.  Product all orders within each payload rank, using any fixed
type schedule with the correct type counts.  Relabelings belonging to
different local ranks and different sides are mutually independent.

Fix a rank-`(b+1)` target `Y` with

\[
 |Y\cap A|=s,qquad |Y\cap B|=b+1-s.                 \tag{4.1}
\]

Only two payload ranks can produce it: an `A` transition from `r=s-1`, or a
`B` transition from `r=s`.  Let `N_s^-` and `N_s^+` be their respective
occurrence counts.  There are

\[
 {s-1\over b}{b\choose s-1}^2,qquad
 {b-s\over b}{b\choose s}^2                         \tag{4.2}
\]

total occurrences of the two types, spread by relabeling symmetry over

\[
 M_s={b\choose s}{b\choose s-1}                     \tag{4.3}

targets.  Therefore

\[
 \lambda_s^-:=\mathbb E N_s^-
 ={s(s-1)\over b(b-s+1)},\qquad
 \lambda_s^+:=\mathbb E N_s^+
 ={(b-s)(b-s+1)\over bs}.                            \tag{4.4}
\]

### Theorem 4.1 (independent-alignment miss lower bound)

Under the independent relabeling model above, the expected number `Z` of
uncovered rank-`(b+1)` targets satisfies

\[
 \boxed{\mathbb E Z\ge
   \left({1\over4}-o(1)\right){2b\choose b+1}.}       \tag{4.5}
\]

#### Proof

For a fixed `Y`, Markov's inequality gives

\[
 \Pr(N_s^->0)\le\lambda_s^-,\qquad
 \Pr(N_s^+>0)\le\lambda_s^+.                        \tag{4.6}
\]

The two counts depend on disjoint rank-and-side relabeling variables, so
they are independent.  Whenever both means are at most one,

\[
 \Pr(Y\text{ is uncovered})
 \ge(1-\lambda_s^-)(1-\lambda_s^+).                  \tag{4.7}
\]

Write `s=(b+1)/2+x`.  Uniformly for `|x|<=b^(2/3)`, (4.4) gives

\[
 \lambda_s^-=\frac12+O(b^{-1/3}),\qquad
 \lambda_s^+=\frac12+O(b^{-1/3}).                   \tag{4.8}
\]

In particular both are below one for large `b`, and the right side of
(4.7) is `1/4-o(1)` uniformly in this window.

For a uniformly random `(b+1)`-subset of a `2b`-set, the variable
`|Y\cap A|` is hypergeometric with mean `(b+1)/2` and variance `Theta(b)`.
A standard hypergeometric tail bound shows that the profiles with
`|x|>b^(2/3)` contain only an `exp(-Omega(b^(1/3)))` fraction of all
rank-`(b+1)` targets.  Summing (4.7) over the central profiles proves
(4.5).  \(\square\)

Internal repetitions inside either source only decrease its coverage
probability relative to the first-moment bound (4.6), so they cannot evade
the theorem.  The conclusion is an expectation statement about independent
rank alignment.  It neither says that every independently relabeled outcome
fails nor rules out the exceptional coherent alignment exhibited in Section
3.  Its point is that independent rank-by-rank Baranyai--Katona factors do
not automatically solve the multirank gate.

## 5. Exact remaining gate

The clustered schedules settle the following parts of the product route.

- They obey the DCC gap without balanced mechanical words.
- They preserve full internal band simplicity.
- Their nested phase sets eliminate upper cross-payload torus collisions and
  make lower phase multiplicities optimal **in phase space**, once local order
  coordinates are aligned.
- The required alignment exists unconditionally for the adjacent MSW middle
  ranks, giving Theorem 3.1.

What remains is a coherent multirank order-bank theorem: couple the local
tight-cycle factors at neighboring payload ranks so that almost every local
interval target has a common order/endpoint coordinate, with total uncoupled
mass `o(W_b)`.  Ordinary payload-only Baranyai--Katona decompositions and
independent random relabelings do not provide this coupling.  Theorem 2.1
shows that the clustered schedule introduces no additional upper-rank
collisions inside an aligned bank, while Proposition 2.2 shows that a rigid
one-to-one bank still has a linear aggregate upper-hole ledger.  The missing
theorem must therefore align the local orders **and** redistribute the
available outer-rank surplus across the skipped phase diagonals.

The finite audit script
`scratch/audit_clustered_product_phase_alignment_20260821.py` checks, for
`b=5,7,11,13,17`, every admissible `H,r`, every band rank in (1.6), all
`q<=b` phase maps in Theorem 2.1, and the exact `q=+/-1` per-order-pair
counts in Theorem 3.1.  These checks are only an audit; the proofs above are
independent of them.
