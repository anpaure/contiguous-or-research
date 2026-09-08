# Shadow slots after a pair-flip block factor

This note audits Stage B of `RANK_BALANCED_BLOCKS.md`, conditional on having
already selected a near-factor of full pair-flip blocks.  Its main conclusion
is negative but useful:

> A middle-block near-factor does not by itself imply the required shadow
> assignment.  With prescribed balanced loads, the exact missing property is
> a lossless-expansion (Hall) condition for every subfamily of blocks.  Without
> prescribed loads, there is no Hall problem at all: the sole condition is that
> every target colour actually occurs in at least one selected block.

In particular, the common fractional degree calculation is not evidence for
this integral expansion.  An unstructured random selection misses a positive
fraction of the first shadow layer.

Throughout, put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q}
             =\binom{2m}{m+q},\qquad
 \rho_q=N_q/W,\qquad R=2m.                        \tag{0.1}
\]

Let `F` be a selected family of pair-flip blocks.  A cyclic block has `R`
depth-`q` windows, and its lower colours and upper colours are separately
distinct.  After choosing a cut and refusing windows crossing it, it has
`R-q` available starts.  For a sign `epsilon in {-,+}`, write

\[
 C^{\epsilon}_{q}(B)\subseteq
 \begin{cases}
 \binom{[2m]}{m-q},&\epsilon=-,\\
 \binom{[2m]}{m+q},&\epsilon=+,
 \end{cases}                                      \tag{0.2}
\]

for the set of available colours in block `B`.  Thus
`|C^epsilon_q(B)|=R` cyclically and `R-q` after a cut.

## 1. The exact quota-Hall theorem

Suppose first that an integer quota `b_B` is prescribed for each block, with

\[
 0\le b_B\le |C^\epsilon_q(B)|.                  \tag{1.1}
\]

We ask to choose `b_B` depth-`q` slots in each block so that all chosen
colours are distinct.  When

\[
 \sum_{B\in\mathcal F}b_B=N_q,                   \tag{1.2}
\]

this is the same as covering the entire target layer exactly once.

### Theorem 1 (block-side Hall condition)

Such a choice exists if and only if, for every subfamily
`A subseteq F`,

\[
 \boxed{\left|\bigcup_{B\in\mathcal A}C^\epsilon_q(B)\right|
       \ge \sum_{B\in\mathcal A} b_B.}           \tag{1.3}
\]

#### Proof

Replace every block `B` by `b_B` identical left-hand clones, each adjacent to
all colours in `C^epsilon_q(B)`.  A choice of distinct colours is a matching
saturating all clones.  Hall's theorem applies.  For a fixed support
`A` of blocks, the most demanding set of clones contains all `b_B` clones of
every `B in A`, because adding another identical clone increases demand and
does not enlarge its neighbourhood.  Hall's inequalities therefore reduce
exactly to (1.3).  QED.

There is an equivalent target-side form.  If (1.2) holds, the two sides of
the cloned incidence graph have the same size, so Theorem 1 is equivalent to

\[
 |X|\le \sum_{B:\,C^\epsilon_q(B)\cap X\ne\varnothing}b_B
 \quad\hbox{for every target family }X.             \tag{1.4}
\]

More generally, the exact number of quota slots that must remain unmatched is

\[
 \boxed{\delta_q^\epsilon=
   \max_{\mathcal A\subseteq\mathcal F}
   \left(\sum_{B\in\mathcal A}b_B-
   \left|\bigcup_{B\in\mathcal A}C^\epsilon_q(B)\right|\right)_+.}
                                                        \tag{1.5}
\]

This is just the deficiency form of Hall's theorem.  Thus `delta=o(W)` is
necessary and sufficient for an `o(W)`-repair version of Stage B.

### Collision form

Let `a_B=|C^epsilon_q(B)|`, and define the colour-collision loss of a
subfamily by

\[
 \kappa_q^\epsilon(\mathcal A)
 =\sum_{B\in\mathcal A}a_B-
   \left|\bigcup_{B\in\mathcal A}C^\epsilon_q(B)\right|.
                                                        \tag{1.6}
\]

Then (1.3) is exactly

\[
 \boxed{\kappa_q^\epsilon(\mathcal A)
   \le \sum_{B\in\mathcal A}(a_B-b_B)
   \quad\hbox{for every }\mathcal A\subseteq\mathcal F.} \tag{1.7}
\]

For uncut cyclic blocks and balanced quota `b_B approximately R rho_q`, the
right side is approximately

\[
 R(1-\rho_q)|\mathcal A|.                        \tag{1.8}
\]

This is a **lossless**, not an ordinary positive-factor, expansion
requirement.  For `q=1`,

\[
 R(1-\rho_1)=2m\left(1-\frac m{m+1}\right)
             =\frac{2m}{m+1}<2.                  \tag{1.9}
\]

Thus every subfamily is allowed fewer than two repeated lower colours per
block on average, and simultaneously fewer than two repeated upper colours
per block.  This explains why degree regularity or a small pair-codegree in
the ambient block family is much too weak.

If one insists on one nonwrapping cut per block, then `a_B=R-1`, whereas the
same average quota is

\[
 R\rho_1=\frac{2m^2}{m+1}=2m-2+\frac2{m+1}.       \tag{1.10}
\]

The collision allowance drops to

\[
 (R-1)-R\rho_1=\frac{m-1}{m+1}<1                 \tag{1.11}
\]

per block on average.  With integral quotas, a proportion `2/(m+1)` of the
blocks must have quota `R-1` and hence zero collision allowance; the remaining
blocks have quota `R-2` and allowance one (up to divisibility at the ends).

Theorem 1 also gives a deterministic assignment whenever the expansion is
known: any augmenting-path or integral max-flow proof of Hall produces the
slots.  There is no further combinatorial choice hidden after (1.3).

## 2. If only the average is prescribed, Hall disappears

The phrase "average capacity `R rho_q`" must be interpreted carefully.
Suppose no individual `b_B` is prescribed.  We merely want every target to
have a witness, and a block may be used for any number of its available
windows.  Then the exact condition is only

\[
 \boxed{\bigcup_{B\in\mathcal F}C^\epsilon_q(B)
       =V_q^\epsilon,}                            \tag{2.1}
\]

where `V_q^- = binom([2m],m-q)` and
`V_q^+ = binom([2m],m+q)`.

Indeed, choose one occurrence of each target independently.  A block cannot
be overloaded: it receives at most one assignment for each of its distinct
available colours, hence at most `a_B` assignments.  Once all `N_q` targets
are assigned, the average load is automatically `N_q/|F|`, which is
`R rho_q+o(R)` for a near-factor.

This is the physical OR problem.  Windows of different lengths do not consume
one another, and one physical window may simultaneously witness its lower
intersection colour and its upper union colour.  Consequently:

* different depths `q` are not coupled by slot capacity;
* lower and upper assignments at one depth are not mutually exclusive; and
* prescribed per-block quotas are an auxiliary regularity condition needed by
  a one-stage decorated-hypergraph proof, not by the final OR sequence.

Therefore, conditional on a fixed Stage-A factor, Stage B is more accurately
called **shadow coverage**, not shadow matching.  If the selected blocks omit
a colour, no assignment can create it.

For later use, let `n(S)` be the number of available occurrences of target
`S`, and let `A_q=sum_B a_B` be the total number of slots.  The exact collision
ledger is

\[
 \begin{aligned}
 C_q&=\sum_S(n(S)-1)_+=A_q-|\{S:n(S)>0\}|,\\
 M_q&=|\{S:n(S)=0\}|=N_q-A_q+C_q.               \tag{2.2}
 \end{aligned}
\]

Thus the missing-colour count is exactly the collision excess above the
unavoidable slack `A_q-N_q`.  This identity is often a simpler certificate
than running a matching algorithm.

## 3. Why an arbitrary or random middle factor is insufficient

Middle-vertex disjointness gives no lower bound on the degree `n(S)` of a
fixed shadow colour.  Already for `q=1`, a lower colour `S` is used precisely
when the selected 2-factor/path factor takes an edge inside the Johnson clique
of the `m+1` middle sets containing `S`.  Covering the vertices of those
cliques does not force taking an internal edge of every clique.

The global count shows how rigid a successful cyclic factor must be.  If
`|F|=W/R`, there are `W` cyclic depth-one slots but only

\[
 N_1=\frac m{m+1}W                                      \tag{3.1}
\]

lower colours.  Complete coverage permits total repeated-colour excess only

\[
 W-N_1=\frac{W}{m+1}.                                  \tag{3.2}
\]

Hence all but at most `W/(m+1)` lower colours have multiplicity exactly one;
the same statement holds independently for upper colours.  Stage A would
have to be an almost-rainbow two-sided resolution already at its first
shadow.

An idealized independent random choice has the wrong behaviour.  Choose
`t=W/R` independent uniform parameter blocks, without conditioning on middle
disjointness.  By symmetry, a fixed rank-`m-q` target occurs in one cyclic
block with probability `R/N_q`.  Therefore

\[
 \Pr(S\hbox{ is absent})=\left(1-\frac R{N_q}\right)^t
   =\exp\left(-\frac1{\rho_q}+o(1)\right).          \tag{3.3}
\]

For `q=o(sqrt(m))`, `rho_q=1-o(1)`, so the expected missing proportion tends
to `e^{-1}`.  This calculation is not a theorem about a random factor
conditioned on exact middle disjointness, but it proves that unstructured
random block sampling and its first-moment symmetry are nowhere near enough.
Any successful factor must introduce strong negative correlations between its
shadow colours.

Full target-transitivity is not a way around this.  If the automorphism group
of a cyclic exact middle factor acted transitively on the rank-`m-q` targets,
then every target would have the same integer multiplicity `d`, and counting
would give

\[
 dN_q=W,\qquad d=1/\rho_q.                       \tag{3.4}
\]

For `q=1`, this is `d=(m+1)/m`, impossible for `m>1`.  Thus an integral
solution must break the exact symmetry exhibited by the fractional solution.
Group-averaging equalizes expected degrees but says nothing about Hall
expansion of an individual factor.

More explicitly, translating one selected factor by all coordinate
permutations produces a perfectly symmetric probability distribution, but a
translation preserves every union size in (1.3) and hence preserves its Hall
deficiency.  Symmetrizing a bad integral factor therefore yields good
fractional marginals while leaving every sampled factor bad.  This is the
precise logical gap between the common fractional degree theorem and Stage B.

## 4. A useful deterministic sufficient condition

There is one clean positive case.  Suppose every block has exactly `a`
available colours and every target occurs in exactly `d` selected blocks.
Then `ta=dN_q`.  If `b=a/d` is an integer, the constant quota `b` satisfies
Hall automatically: for every block subfamily `A`, the `a|A|` incidences
enter targets of total degree at most `d`, so

\[
 \left|\bigcup_{B\in\mathcal A}C_q^\epsilon(B)\right|
 \ge \frac{a|\mathcal A|}{d}=b|\mathcal A|.       \tag{4.1}
\]

Thus an exactly biregular shadow incidence graph has a deterministic
assignment.  The obstruction (3.4) shows why this attractive symmetric case
cannot hold at depth one: its required degree is nonintegral.  An actual
construction needs an almost-resolvable mixture of neighbouring degrees,
plus an integral absorber, rather than exact transitivity.

The full Hall inequalities can be guaranteed by a stronger sequential
property.  Order the blocks `B_1,...,B_t`.  If

\[
 \left|C_q^\epsilon(B_i)\setminus
       \bigcup_{j<i}C_q^\epsilon(B_j)\right|\ge b_{B_i}
 \quad(1\le i\le t),                                  \tag{4.2}
\]

then choosing `b_{B_i}` previously unused colours greedily gives the desired
assignment.  Equivalently, block `i` is allowed to collide with the past in
at most `a_{B_i}-b_{B_i}` colours.  At depth one this allowance is only about
two cyclic colours per block.

Condition (4.2) is stronger than Hall and will usually need a small absorber
at the end.  A plausible proof target is therefore:

1. order all but `o(|F|)` blocks so that (4.2) holds simultaneously for the
   two signs and all shallow depths;
2. reserve `o(W)` middle vertices/blocks as an absorber for the remaining
   colour and divisibility defects; and
3. use Theorem 1 on the absorber rather than demand greedy freshness there.

The exact non-greedy target is the following.

### Shadow-resolution property

For each `q<=h` and each sign, choose quotas and put

\[
 r_q^\epsilon=N_q-\sum_Bb^\epsilon_{B,q}\ge0,
 \qquad
 \delta_q^\epsilon=\max_{\mathcal A\subseteq\mathcal F}
 \left(\sum_{B\in\mathcal A}b^\epsilon_{B,q}-
 \left|\bigcup_{B\in\mathcal A}C^\epsilon_q(B)\right|\right)_+
 .                                                        \tag{4.3}
\]

The exact number left uncovered by an optimal quota assignment is
`r_q^epsilon+delta_q^epsilon`.  Hence the simultaneous asymptotic target is

\[
 \boxed{\sum_{q=1}^{h}\sum_{\epsilon\in\{-,+\}}
 (r_q^\epsilon+\delta_q^\epsilon)=o(W).}           \tag{4.4}
\]

This summed condition, rather than a separate unspecified `o(W)` at every
rank, is what guarantees `o(W)` total literal repair cost when `h` grows.
By Theorem 1 it is necessary and sufficient for the quota version of Stage B.

This is the precise Boolean-specific expansion theorem that would make the
two-stage program work.  It cannot be inferred from a generic near-factor of
the middle-block hypergraph.  Stage A must either be strengthened to produce
(4.4), or the block factor and shadow representatives must be selected
simultaneously by an absorption/design theorem.

## 5. Cuts: the only genuine cross-rank coupling, and how to remove it

Index the `R` transition edges of a cyclic block by `Z/RZ`.  A cyclic
depth-`q` window starting at `t` crosses the set `K_q(t)` of its `q`
transition edges.  If block `B` is cut at `kappa_B`, that occurrence survives
exactly when

\[
 \kappa_B\notin K_q(t).                                  \tag{5.1}
\]

For pure coverage, simultaneous cut feasibility is the exact finite CSP

\[
 \bigvee_{(B,t):\,\operatorname{col}^\epsilon_q(B,t)=S}
       [\kappa_B\notin K_q(t)]                            \tag{5.2}
\]

for every `q`, sign, and target `S`.  For fixed cuts, Theorem 1 applies with
the surviving colour sets.  Formula (5.2) is the only real coupling between
different depths and the two signs.

The scalar inequality

\[
 R\rho_q\le R-q                                      \tag{5.3}
\]

proves only that enough slots remain after a cut.  It does **not** prove that
an arbitrarily designated family of `R rho_q` cyclic windows has a common cut
avoiding all of them: their crossed-edge sets may cover the whole cycle.

For the asymptotic program this cut CSP is optional.  Since the desired
`h=Theta(sqrt(m log m))` satisfies `h=o(m)`, append the first `h` middle states
of every selected block after its full cycle.  This linearizes every cyclic
window through depth `h` at total cost

\[
 h|\mathcal F|=O(hW/R)=o(W).                       \tag{5.4}
\]

The existing seam padding has the same order.  Hence all cyclic slots can be
retained, and cuts create no coupling at all, without changing a
`W+o(W)` theorem.  Zero-copy nonwrapping cuts matter only for sharper finite
or second-order bounds.

## 6. Verdict on Stage B

Conditional only on a near-decomposition of the middle layer into full
pair-flip blocks, Stage B is **not proved and is not automatic**.  The first
shadow already demands an almost-rainbow two-sided block resolution, while a
random block family has a constant missing fraction.

The exact obstruction is now explicit:

* with balanced block quotas, it is the Hall deficiency (1.5), equivalently
  the collision-budget violation (1.7);
* without artificial quotas, it is simply the missing-colour count (2.2);
* if zero-copy cuts are insisted upon, add the cut CSP (5.2).

There is no additional coupling across ranks or between lower and upper
shadows in the OR problem.  A credible global theorem must therefore select
the Stage-A blocks with their shallow shadow colours already coordinated--a
resolvable, two-sided, multiscale design--rather than hope to repair an
arbitrary middle factor afterward.

## 7. A hybrid target: resolve shallow shadows, cover deep shadows

The rank-balanced quota formulation is a sufficient way to force every rank,
but it is stronger than the physical coverage problem.  In particular, it
needlessly asks outer shadow layers to behave almost injectively even though
their natural occurrence multiplicity is large.

In the independent-block model of Section 3, the mean number of occurrences
of a fixed depth-`q` target is

\[
 \lambda_q=\frac1{\rho_q}.                         \tag{7.1}
\]

Uniformly for `q=O(sqrt(m log m))`, expansion of the product defining
`rho_q` gives

\[
 \log\lambda_q=\frac{q^2}{m}+o(1).                \tag{7.2}
\]

Consequently, if a random or pseudorandom *middle factor* inherited the same
Poisson-scale upper bound

\[
 M_q^\epsilon\le (1+o(1))N_qe^{-(1-o(1))\lambda_q}+o(W/h),
                                                               \tag{7.3}
\]

then all sufficiently deep shadows could simply be covered with repetitions
and their omissions repaired literally.  Indeed, take

\[
 q_0=(1+o(1))\sqrt{m\log\log m}.                   \tag{7.4}
\]

At this point `lambda_(q_0)` is of order `log m`.  For
`h=Theta(sqrt(m log m))`, choosing the harmless constant in (7.4) so that
`lambda_(q_0)>=2 log h` gives

\[
 \sum_{q=q_0}^{h}\sum_\epsilon M_q^\epsilon=o(W).  \tag{7.5}
\]

Thus a plausible global proof does **not** need lossless Hall expansion all
the way to the literal-tail depth.  It would suffice to combine

1. a two-sided near-resolution through
   `q_0=Theta(sqrt(m log log m))`; and
2. a pseudorandom near-factor theorem giving (7.3) for
   `q_0<=q<=h`.

This remains conditional: independent blocks are not a middle factor, and
conditioning a growing-uniformity random packing on middle disjointness is
exactly one of the unresolved probabilistic steps.  Nevertheless, (7.1)--
(7.5) identify a smaller structured core than the fully rank-balanced program.
The difficult near-rainbow regime ends near `sqrt(m log log m)`, while the
remaining interval up to `sqrt(m log m)` should be a redundant covering
regime rather than a matching regime.
