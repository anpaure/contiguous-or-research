# Adaptive rectangle orders and the first-eligible chronology Hall cut

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web input
is used.

## 0. Verdict

The context-dependent recursive cube factor does remove the fixed-common-order
obstruction inside a tensor rectangle packet.  It does not remove the outer
chronology imposed by the canonical first-eligible packet decomposition.

For a fixed rectangle shore, classify a six-coordinate block as follows.

* `E` means that its local middle restriction is one of the eight rectangle
  owners.
* `C` means that its local upper-target restriction is one of the eight
  triples occurring as the union of an edge of that fixed shore.

Let a rank-`m+q` target `T` have at least `r-q+1` `E`-blocks.  Before its
`(r-q+1)`-st `E`-block, let

\[
                         n(T)=\#\{C\text{-blocks}\}.              \tag{0.1}
\]

Then the exact number of canonical first-`r` rectangle macrocells in which
`T` is a block-simple upper `q`-face is

\[
                         \boxed{\binom{n(T)}q}.                   \tag{0.2}
\]

More importantly, this candidate count gives an exact target-side Hall cut.
If `mathcal T_n` is the stratum `n(T)=n`, then every choice of
context-dependent recursive factors, affine conjugates, block permutations,
and correlations among different macrocells misses at least

\[
 \boxed{
 |\mathcal T_n|
 \left(1-{\binom nq\over\binom rq}\right)_+
 }
                                                                    \tag{0.3}
\]

distinct upper targets in that stratum.  The same bound holds for fractional
mixtures of the macrocell menus.  It uses neither a common direction order
nor a bound on the number of cyclic intervals.  Its invariant is the outer
first-eligible chronology.

There is a stronger all-shore form.  If all three rectangle matchings may be
chosen state-dependently, use the maximal sixteen-triple upper alphabet and
define `widehat n(T)` analogously.  Then the missed number in its stratum is
at least

\[
 \boxed{
 |\widehat{\mathcal T}_n|
 \left(1-{\binom nq\over2^q\binom rq}\right)_+ .}                 \tag{0.3a}
\]

Thus the theorem already permits every local rectangle shore.  The extra
shore entropy enlarges the target alphabet by `2^q` and does not enlarge the
owner capacity.

This cut is decisive at every sublinear rectangle scale.  Suppose

\[
 q=A\sqrt m+O(1),\qquad q\le r=o(m),\qquad A>0.                    \tag{0.4}
\]

For a uniformly chosen rank-`m+q` target,

\[
 \Pr\left\{n(T)\le r-{q\over2}\right\}=1-o(1).                  \tag{0.5}
\]

For the maximal all-shore alphabet, the corresponding estimate is

\[
 \Pr\left\{\widehat n(T)\le2r-{3q\over2}\right\}=1-o(1).        \tag{0.5a}
\]

On that event,

\[
 {\binom{n(T)}q\over\binom rq}
 \le \exp\left(-{q^2\over2r}\right)=o(1).                       \tag{0.6}
\]

Consequently every such adaptive rectangle atlas has

\[
 \boxed{
 M_q^+\ge(1-o(1))\binom{2m}{m+q}
          =(e^{-A^2}-o(1))W.}                                    \tag{0.7}
\]

The exponentially small middle-owner leave of the canonical atlas cannot
alter (0.7).  In particular, the A/S recursive-factor combination fails on
every mesoscopic choice `H<=r=o(m)` at the single depth
`q=H=A sqrt(m)+O(1)`, even when `H=o(r)`.  At the phase-scale choice
`q<=r<2q`, a positive fraction of targets already has at most one candidate
macrocell, which is the finite version of the same cut.

This does not rule out a genuinely linear-scale `r=Theta(m)` construction,
or an outer atlas which changes the first-eligible chronology itself.  For
all `r`, equation (0.3) remains the exact surviving Hall inequality.

The phase-dense ternary carry is closed separately and more strongly: its
proved switches have zero block-order holonomy, so all ternary states retain
one quotient packet word.  The resulting physical run Hall cut is recorded
in
`MATH_THEOREM_RECTANGLE_TERNARY_CARRY_ZERO_BLOCK_HOLONOMY_20260726.md`.

No coefficient-one conclusion is claimed.  The proved conclusion is that
neither of the two proposed adaptive-order compositions supplies the missing
all-depth coverage in its audited form.

## 1. One fixed-shore rectangle block

Let

\[
 P=\{t,e\},\qquad A=\{a,b,c,d\},
\]

and fix a perfect matching

\[
                         M=\{E_0,E_1\}                            \tag{1.1}
\]

of `A`.  The local middle-owner alphabet is

\[
 \mathcal E=P*A
 =\{\{p,x\}:p\in P,\ x\in A\},
 \qquad |\mathcal E|=8.                                         \tag{1.2}
\]

The two squares `P*E_0` and `P*E_1` form the corresponding rectangle
factor.  Its upper edge traces form the alphabet

\[
 \mathcal C_M^+
 =\{P\cup\{x\}:x\in A\}
   \mathbin{\dot\cup}
   \{\{p\}\cup E:p\in P,\ E\in M\}.                             \tag{1.3}
\]

Both parts have four members, so

\[
                         |\mathcal C_M^+|=8.                     \tag{1.4}
\]

Every member of `mathcal C_M^+` is the upper union of a unique local edge
in the fixed-shore factor.  Indeed, `P union {x}` forces the direction `P`
and the unique matching edge containing `x`, while `{p} union E` forces
the direction `E` and the orientation `p` of the pair `P`.

This uniqueness is the upper-side asymmetry of the rectangle.  Lower
singletons in `P` have two carrier cells, but an upper triple in a fixed
shore has one.

If all three shores are allowed, the maximal upper alphabet is

\[
 \widehat{\mathcal C}^{+}
 =\{P\cup\{x\}:x\in A\}
  \mathbin{\dot\cup}
  \{\{p\}\cup\{x,y\}:p\in P,\ \{x,y\}\in\tbinom A2\},            \tag{1.5}
\]

and

\[
                         |\widehat{\mathcal C}^{+}|=4+12=16.      \tag{1.6}
\]

Every triple in (1.5) still determines one physical edge.  A triple
`P union {x}` determines the edge between `t x` and `e x`; a triple
`{p} union {x,y}` determines the edge between `p x` and `p y`.  The latter
edge selects the unique rectangle shore whose matching contains `{x,y}`.
Choices in distinct tensor blocks are independent, so any collection of
such local edges is simultaneously realizable after choosing one shore per
touched block.

## 2. The canonical first-`r` macrocell partition

Partition all but at most five of the `2m` ground coordinates into ordered
six-coordinate blocks

\[
                         B_1,\ldots,B_B,
 \qquad B=\left\lfloor{2m\over6}\right\rfloor.                  \tag{2.1}
\]

Give every block its labelled copy of `(P,A,M)`.  A middle owner `X` is
called eligible at `i` when

\[
                         X\cap B_i\in\mathcal E_i.                \tag{2.2}
\]

If `X` has at least `r` eligible blocks, let

\[
                         I(X)=(i_1<\cdots<i_r)                    \tag{2.3}
\]

be its first `r` eligible indices.  Fix the restrictions of `X` outside
these blocks and vary each selected restriction independently through
`mathcal E_i`.  The resulting macrocell has

\[
                              8^r                                \tag{2.4}
\]

middle owners.

These macrocells are pairwise disjoint and partition all middle owners with
at least `r` eligible blocks.  Varying a selected restriction does not
change eligibility or local rank, so it preserves both the index list (2.3)
and the ambient middle rank.

At middle density one half, a complete block is eligible with probability
`1/8` under the product law.  If `r=o(m)`, a Chernoff bound, followed by
conditioning on total rank `m`, shows that the omitted middle-owner mass is

\[
                         e^{-\Omega(m)}W.                         \tag{2.5}
\]

Each macrocell is tensor-partitioned into `2^r` physical cells `Q_(2r)` by
choosing one of `E_0,E_1` in every block.  Place the two directions of one
rectangle block at one bottom sibling pair of the recursive factor
`F_(2r)`.  Its bottom-sibling theorem implies that every window of at most
`r` transitions uses at most one direction from each selected block.
Arbitrary block permutations, within-block direction swaps, affine
translations, and independent choices in different product cells preserve
this property.

We call any exact macrocell factor with this property **block-simple through
depth `r`**.  The argument below applies to every such factor; it does not
use the particular recursion after block simplicity has been established.

## 3. Exact parsing of an upper target

Fix `1<=q<=r` and a physical rank-`m+q` target `T`.  In the ordered block
word of `T`, write

* `E` at blocks whose restriction lies in `mathcal E_i`;
* `C` at blocks whose restriction lies in `mathcal C_(M_i)^+`;
* a neutral letter otherwise.

If there are at least `r-q+1` letters `E`, let `b(T)` be the position of
the `(r-q+1)`-st such letter and define

\[
 n(T)=\#\{i<b(T):T\cap B_i\in\mathcal C_{M_i}^+\}.              \tag{3.1}
\]

If the required `E`-letter does not exist, put `n(T)=-\infty`.

### Lemma 3.1 (candidate-macrocell parsing)

The target `T` is a block-simple upper `q`-face of exactly

\[
                         \binom{n(T)}q                            \tag{3.2}
\]

canonical first-`r` macrocells, with the binomial coefficient interpreted
as zero when `n(T)<q`.

#### Proof

Suppose first that `T` is an upper face of a canonical macrocell.  Its `q`
touched selected blocks have local traces in `mathcal C_M^+`; its other
`r-q` selected blocks retain local restrictions in `mathcal E`.  Every
middle owner of the face is obtained by deleting one of the two variable
coordinates in each touched triple, so all `r` selected blocks are eligible
in every face owner.

No touched block may occur at or after `b(T)`.  Before `b(T)`, the target
already has exactly `r-q` eligible blocks.  If a touched block occurred
later, these `r-q` blocks together with the earlier touched blocks would
fill the first `r` eligible positions before it, contradicting the canonical
choice of the selected list.

Conversely, choose any `q` of the `n(T)` `C`-blocks before `b(T)`.  Adjoin
the first `r-q` `E`-blocks of `T`.  These `r` indices are exactly the first
`r` eligible blocks of every middle extension obtained from the chosen
upper face.  Fixing `T` outside them therefore defines one canonical
macrocell.  Local uniqueness following (1.4) determines one product cell
and one affine `q`-face inside that macrocell.

The two constructions are inverse.  Hence the number of candidate
macrocells is (3.2).  \(\square\)

The parsing is independent of any cyclic order subsequently placed in the
candidate product cells.

## 4. Chronology strata and the exact Hall inequality

For a canonical macrocell with selected list
`i_1<...<i_r`, let `b` be the next exterior block after `i_r` whose fixed
restriction lies in `mathcal E`.  Let

\[
 g=\#\{j<b:j\notin\{i_1,\ldots,i_r\},\
                 \ \xi_j\in\mathcal C_{M_j}^+\}                 \tag{4.1}
\]

be its **upper chronology gap**.  Blocks before `i_r` which are not selected
cannot be eligible, by the first-`r` rule; definition (4.1) counts only the
fixed exterior `C`-blocks.

### Lemma 4.1 (stratum invariance)

Every block-simple upper `q`-window emitted from a macrocell of gap `g` has

\[
                         n(T)=q+g.                                \tag{4.2}
\]

#### Proof

The `q` touched selected blocks become `C`-blocks.  The other `r-q`
selected blocks remain `E`-blocks.  The next target `E`-block is therefore
the fixed exterior block `b`.  Before `b`, the target's `C`-blocks are
exactly the `q` touched blocks together with the `g` fixed exterior
`C`-blocks.  This proves (4.2).  \(\square\)

Let `mathfrak M_g` be the family of macrocells with gap `g`, and let
`mathcal T_n` be the physical target stratum `n(T)=n`.

### Lemma 4.2 (exact incidence double count)

For `n=q+g>=q`,

\[
 |\mathfrak M_g|\binom rq8^r
 =|\mathcal T_n|\binom nq.                                     \tag{4.3}
\]

#### Proof

Count pairs consisting of a gap-`g` macrocell and one of its geometric
block-simple upper `q`-faces.

In one macrocell, choose the `q` touched blocks in `binom(r,q)` ways.  In
each touched block choose one of the eight triples (1.3), and in every
untouched block choose one of the eight middle owners (1.2).  Local
uniqueness makes all resulting physical targets distinct.  Thus one
macrocell contributes

\[
                         \binom rq8^q8^{r-q}
                         =\binom rq8^r                            \tag{4.4}
\]

incidences.

By Lemma 4.1 all lie in `mathcal T_(q+g)`.  Conversely Lemma 3.1 says that
every target in `mathcal T_n` has exactly `binom(n,q)` candidate
macrocells.  This proves (4.3).  \(\square\)

### Theorem 4.3 (chronology-stratum Hall cut)

At a fixed upper depth `q<=r`, every integral selection of one block-simple
exact factor in each canonical macrocell misses at least

\[
 \boxed{
 |\mathcal T_n|
 \left(1-{\binom nq\over\binom rq}\right)_+}                    \tag{4.5}
\]

targets in `mathcal T_n`.  This remains true for arbitrary menus,
component-dependent choices, fractional mixtures, and correlations among
different macrocells.

#### Proof

One macrocell contains `8^r` owners.  At one directed depth, any selected
successor factor therefore has `8^r` starts and can hit at most `8^r`
distinct targets.  Lemma 4.1 confines all of those targets to the one
stratum `mathcal T_(q+g)`.

Consequently all gap-`g` macrocells together can hit at most
`|mathfrak M_g|8^r` distinct members of `mathcal T_(q+g)`.  Divide (4.3)
by `binom(r,q)` to obtain

\[
 |\mathfrak M_g|8^r
 =|\mathcal T_n|{\binom nq\over\binom rq}.                        \tag{4.6}
\]

Subtracting this capacity from the stratum demand proves (4.5).  For a
fractional mixture, every menu state in one macrocell still contributes at
most `8^r` to the all-ones weight on its forced stratum, so the identical
dual cut applies.  Correlations cannot change the sum of the per-macrocell
maxima.  \(\square\)

Equation (4.5), rather than macro-support balance, is the exact remaining
Hall cut for the A/S composition.

### Theorem 4.4 (maximal all-shore chronology cut)

Replace `mathcal C_M^+` by the sixteen-state alphabet
`widehat mathcal C^+` in the definitions of `n(T)`, `g`, and the target
strata.  Then every integral or fractional state-dependent selection from
all three rectangle shores misses at least the quantity in (0.3a).

#### Proof

The parsing proof of Lemma 3.1 is unchanged: every touched upper triple
determines one physical edge, so a target with `widehat n=n` has exactly
`binom(n,q)` candidate first-`r` macrocells.

In one macrocell the all-shore geometric target universe has size

\[
 \binom rq16^q8^{r-q}
 =\binom rq2^q8^r.                                                \tag{4.7}
\]

All these targets are distinct, and every target emitted by a gap-`g`
macrocell has `widehat n=q+g`.  Hence the incidence double count becomes

\[
 |\widehat{\mathfrak M}_g|\binom rq2^q8^r
 =|\widehat{\mathcal T}_{q+g}|\binom{q+g}q.                       \tag{4.8}
\]

An owner-one factor still has only `8^r` starts.  Dividing (4.8) by
`2^q binom(r,q)` therefore gives the maximum stratum hit ratio

\[
 {\binom{q+g}q\over2^q\binom rq},                                 \tag{4.9}
\]

which proves (0.3a).  The same all-ones stratum weight proves the
fractional assertion.  \(\square\)

## 5. Gaussian evaluation at every sublinear tensor scale

We now prove (0.5)--(0.7).  Put

\[
                         M=m+q,qquad N=2m.                       \tag{5.1}
\]

Choose `T` uniformly from `binom([N],M)`.  For one complete six-coordinate
block, the exact probabilities of the letters `E` and `C` are

\[
 e_m=8{(M)_2(N-M)_4\over(N)_6},
 \qquad
 c_m=8{(M)_3(N-M)_3\over(N)_6}.                                  \tag{5.2}
\]

Here `(x)_j=x(x-1)...(x-j+1)`.  Hence

\[
 e_m={1\over8}+O_A(m^{-1/2}),
 \qquad
 {c_m\over e_m}
 ={m+q-2\over m-q-3}
 =1+{2q\over m}+O_A(m^{-1}).                                    \tag{5.3}
\]

We use the following elementary fixed-slice concentration fact.

### Lemma 5.1 (bounded-block prefix variance)

For the first `L=o(m)` complete blocks, let `E_L,C_L` be the numbers of
letters `E,C`.  Then

\[
 \mathbb E E_L=Le_m,qquad \mathbb E C_L=Lc_m,
 \qquad
 \operatorname {Var}E_L+\operatorname {Var}C_L=O(L).             \tag{5.4}
\]

The constants are uniform for `q=O(sqrt(m))`.

#### Proof

The expectation identities follow from (5.2).  Indicators belonging to
one block have bounded variance.  For two disjoint fixed blocks, expand the
joint probabilities by prescribed local subsets.  For fixed
`a,b<=6`,

\[
 { (M)_{a+b}\over (M)_a(M)_b}=1+O(m^{-1}),
 \qquad
 { (N-M)_{12-a-b}\over
   (N-M)_{6-a}(N-M)_{6-b}}=1+O(m^{-1}),                            \tag{5.5}
\]

and the analogous denominator ratio has the same form.  There are only
finitely many local patterns, so every cross-block covariance is
`O(m^(-1))`.  Therefore

\[
 \operatorname {Var}E_L+\operatorname {Var}C_L
 =O(L+L^2/m)=O(L),                                                \tag{5.6}
\]

because `L=o(m)`.  \(\square\)

Take

\[
 k=r-q+1,
 \qquad
 L=\left\lceil{k+q/8\over e_m}\right\rceil.                     \tag{5.7}
\]

Under (0.4), `L=O(r)=o(m)`.  From (5.4),

\[
 \mathbb E E_L=k+{q\over8}+O(1).                                 \tag{5.8}
\]

Using (5.3) and `r=o(m)`,

\[
\begin{aligned}
 \mathbb E C_L
 &=\left(k+{q\over8}+O(1)\right){c_m\over e_m}\\
 &=r-{7q\over8}+o(q).                                             \tag{5.9}
\end{aligned}
\]

Since `q^2/r -> infinity`, Chebyshev's inequality and Lemma 5.1 give

\[
 \Pr(E_L<k)=o(1),
 \qquad
 \Pr\left(C_L>r-{q\over2}\right)=o(1).                          \tag{5.10}
\]

On the complementary event, the `k`-th `E`-block occurs among the first
`L` blocks and the number of `C`-blocks preceding it is at most `C_L`.
Thus (0.5) follows.

For `n<=r-q/2`, termwise comparison gives

\[
 {\binom nq\over\binom rq}
 =\prod_{j=0}^{q-1}{n-j\over r-j}
 \le\left({n\over r}\right)^q
 \le\left(1-{q\over2r}\right)^q
 \le\exp\left(-{q^2\over2r}\right),                             \tag{5.11}
\]

with the left side zero when `n<q`.  This proves (0.6).

For the all-shore alphabet, the exact one-block probability is

\[
 \widehat c_m
 =16{(M)_3(N-M)_3\over(N)_6}=2c_m,                              \tag{5.11a}
\]

so

\[
 {\widehat c_m\over e_m}
 =2+{4q\over m}+O_A(m^{-1}).                                    \tag{5.11b}
\]

Use the same prefix length (5.7).  Lemma 5.1 applies verbatim to the
sixteen-pattern indicator and yields

\[
 \mathbb E\widehat C_L
 =2r-{7q\over4}+o(q).                                             \tag{5.11c}
\]

The threshold `2r-3q/2` lies `q/4+o(q)` above this mean.  Since
`q^2/r -> infinity`, Chebyshev gives (0.5a).  On that event,

\[
 {\binom{\widehat n(T)}q\over2^q\binom rq}
 =\prod_{j=0}^{q-1}{\widehat n(T)-j\over2(r-j)}
 \le\exp\left(-{q^2\over4r}\right)=o(1).                       \tag{5.11d}
\]

Indeed, `widehat n<=2r-3q/2` implies

\[
 2r-\widehat n-j\ge q/2
 \qquad(0\le j<q),
\]

and hence each factor in the product is at most
`exp(-q/(4r))`.

Summing Theorem 4.4 proves the same lower bound (0.7) even when all three
shores are available state-dependently.

Sum Theorem 4.3 over the strata in (0.5).  They contain
`(1-o(1))binom(2m,m+q)` targets, and (5.11) is `o(1)` uniformly there.
Therefore the good macrocells miss the amount in (0.7).  The bad middle
owners in (2.5) can create at most one additional distinct upper target
per owner, so their contribution is `o(W)`.  Finally

\[
 {\binom{2m}{m+q}\over W}
 =\exp\left(-{q^2\over m}+o(1)\right)
 =e^{-A^2+o(1)},                                                  \tag{5.12}
\]

which completes the proof.

## 6. Phase-scale corollary

There is a finite form which does not use concentration.  Suppose

\[
                         q\le r<2q,
 \qquad k=r-q+1\le q.                                             \tag{6.1}
\]

Every target with `n(T)<=k` has

\[
 {\binom{n(T)}q\over\binom rq}=o(1)                              \tag{6.2}
\]

as `q->infinity`: it is zero unless `n(T)=q`, and that exceptional case
has ratio at most `1/binom(2q-1,q)`.

Under the Bernoulli law of density `(m+q)/(2m)`, delete neutral letters
from the block word.  Conditional on seeing `E` or `C`, the letter is `E`
with probability

\[
                         {e_m\over e_m+c_m}
                         ={1\over2}+O_A(m^{-1/2}).                 \tag{6.3}
\]

The event `n(T)<=k` is the event that at least `k` of the first `2k`
nonneutral letters are `E`.  Its product-law probability is bounded below
by an absolute positive constant.  Restricting to the event that these
letters occur in the first `O(q)` blocks and conditioning on total rank
changes this lower bound by at most a constant depending on `A`, by the
local central-binomial estimate on the remaining `2m-O(q)` coordinates.
Thus

\[
                         |\{T:n(T)\le k\}|
                         \ge c_A\binom{2m}{m+q}.                  \tag{6.4}
\]

Equations (4.5), (6.2), and (6.4) give `Theta_A(W)` upper holes.  Hence the
least-power-of-two choice `q<=r<2q` used by a phase-scale tensor cannot be
rescued by replacing its common order with the recursive factor.

The phase-scale conclusion also survives all three shores.  Among erased
`E/widehat C` letters the `widehat C` probability is

\[
 {\widehat c_m\over e_m+\widehat c_m}
 ={2p_+\over1+p_+}={2\over3}+o(1).                               \tag{6.5}
\]

With `k=r-q+1<=q`, the negative-binomial count `widehat n` before the
`k`-th `E` has positive probability, uniformly after slice conditioning,
to be at most `r-1`.  On this event

\[
 {\binom{\widehat n}q\over2^q\binom rq}
 \le {r-q\over r}\,2^{-q}=o(1).                                 \tag{6.6}
\]

Thus the maximal shore menu also leaves `Theta_A(W)` upper holes.

## 7. Exact proved boundary

The rectangle and the recursive factor do compose locally:

1. every product cell remains an exact owner factor;
2. the recursive cycles use genuinely context-dependent direction orders;
3. all lower and upper traces are injective within one product cell through
   half depth;
4. arbitrary block-affine conjugates are legal.

What fails is the outer target Hall condition.  The canonical packet index
is defined before an order is chosen, and the value `n(T)` is a conserved
chronology stratum.  Equation (4.5) is therefore invisible to every
within-cell permutation array.

There are only three ways to leave the theorem's scope.

1. Use rectangle tensors of genuinely linear scale `r=Theta(m)` and prove
   all of the still-valid cuts (4.5), together with an integral common-depth
   rounding theorem.
2. Replace the first-eligible macrocell partition by an owner-exact atlas in
   which one physical target receives candidate cells from several chronology
   strata.
3. Construct a phase-compatible cross-block owner trade whose block-order
   projection is a nontrivial transposition.  This is the same primitive
   isolated independently by the zero-holonomy audit of the H carry.

The exact next positive lemma is therefore an **outer chronology-breaking
rectangle resolution**, not a richer menu of orders inside the existing
macrocells.
