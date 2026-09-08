# Exact queue rotors for the Catalan hazard law

## 0. Outcome

The proposed hazard law has an exact deterministic model.  Put

\[
 K=2r-1,
 \qquad
 \Omega_r=\{(x_1,\ldots,x_r):x_i\in[K]\text{ distinct}\}.
\]

From an ordered active set `x=(x_1,...,x_r)`, delete the front letter and
append any letter outside the current active set:

\[
 (x_1,x_2,\ldots,x_r)\longrightarrow(x_2,\ldots,x_r,y),
 \qquad y\notin\{x_1,\ldots,x_r\}.
\tag{0.1}
\]

The resulting directed graph is `(r-1)`-in/(r-1)-out regular.  Euler tours
in the components of its higher-block graph give a deterministic finite
family of cyclic schedules which, in aggregate and up to any prescribed
depth `H`, realizes every legal continuation equally often.  (When the
relevant path graph is connected this is one schedule; connectedness is not
needed below.)  Consequently every fixed section `Q` has

\[
 \frac{F_q(Q)}{F_0(Q)}
 =\frac{\binom{r-q}{|Q|}}{\binom r{|Q|}}
 \qquad(0\le q\le H),
\tag{0.2}
\]

and its mean containing-block length is exactly `r/|Q|`.  Thus the ballot
block law and the hypergeometric survival law are mutually compatible for
*all* sections at once.  There is no scalar or local-time obstruction.

What is not supplied is the hard integral transversal: the Euler schedule
uses every `r`-set with a huge multiplicity.  The new precise residue is to
choose one ordered representative above each `r`-set so that those
representatives form a one-hole lower-rainbow Hamilton path while retaining
the cylinder balance of (0.2).  No standard rotor-router theorem gives this
transversal.

## 1. The exact law is hypergeometric, not literally geometric

Fix a `t`-set `Q` and suppose the current active set contains `Q`.  In the
queue model, the next `q<=r` deleted letters are the first `q` entries of
the current ordered active set.  Under the uniform ordering of that set,
they form a uniform ordered `q`-sample without replacement.  Hence

\[
 \alpha_{r,t}(q)
 :=\Pr(Q\text{ survives the next }q\text{ deletions})
 =\frac{(r-t)_q}{(r)_q}
 =\frac{\binom{r-q}{t}}{\binom rt}.
\tag{1.1}
\]

In the critical regime `q,t=o(r)`,

\[
 \alpha_{r,t}(q)
 =\exp\!\left(-\frac{qt}{r}
 +O\!\left(\frac{qt(q+t)}{r^2}\right)\right).
\tag{1.2}
\]

Thus `exp(-qt/r)` is the correct asymptotic slogan, but (1.1) is the exact
finite law.  Its first-step hazard is `t/r`.

For a nonexceptional `t`-section in a one-hole lower-rainbow path, put

\[
 V=\binom{2r-1-t}{r-t},
 \qquad
 b=\frac trV.
\tag{1.3}
\]

The established ballot theorem gives exactly `V` containing vertices and
exactly `b` containing blocks, so their mean length is `V/b=r/t`.  This is
exactly the occupation/block-start ratio of the queue law.

## 2. A scalar rounding theorem for one section

The following eliminates a possible arithmetic objection independently of
any path realization.

### Theorem 2.1 (near-ideal integral block lengths)

Let `1<=t<=r` and let positive integers `V,b` satisfy `b=tV/r`.  There are
positive integer block lengths `ell_1,...,ell_b` with sum `V` such that,
simultaneously for every `q>=0`,

\[
 \left|
 \sum_{j=1}^b(\ell_j-q)_+
 -V\frac{\binom{r-q}{t}}{\binom rt}
 \right|\le r+1,
\tag{2.1}
\]

where the binomial coefficient is zero when `r-q<t`.

#### Proof

Let

\[
 F_q^*=V\frac{\binom{r-q}{t}}{\binom rt}
\]

and define the desired real tail counts

\[
 A_s:=F_{s-1}^*-F_s^*
 =V\frac{\binom{r-s}{t-1}}{\binom rt}
 \qquad(s\ge1).
\tag{2.2}
\]

The sequence `(A_s)` is nonincreasing, is zero after at most `r` terms,
has `A_1=b`, and has total sum `V`.  Round each `A_s` to its nearest
integer, keeping `A_1=b`.  Monotonicity is preserved because nearest-integer
rounding is monotone.  The resulting nonincreasing integer sequence is the
tail sequence

\[
 N_s=\#\{j:\ell_j\ge s\}
\]

of a partition with exactly `b` positive parts.  Its total differs from
`V` by at most `r/2`.  Add or remove that many boxes from the Ferrers
diagram, never touching its first column, to make the total exactly `V`.
Each box edit changes every fixed truncated sum by at most one.  Before the
edit, summing the coordinatewise rounding errors in the tail gives error at
most `r/2`; after the edit the total error is at most `r` (and `r+1` covers
the harmless endpoint convention).  Since

\[
 \sum_j(\ell_j-q)_+=\sum_{s>q}N_s,
\]

this proves (2.1).  QED.

The error is polynomial while `V` is Catalan/binomial scale throughout the
useful section range.  Therefore a single section can have the desired
truncated-local-time profile essentially perfectly.  The difficulty is
joint realizability over all `Q`, not the distribution of lengths for one
`Q`.

## 3. The universal queue-rotor theorem

Let `G_r` be the directed graph on `Omega_r` with the transitions (0.1).
It has degree `d=r-1`.  The symmetric group on `[K]` acts transitively on
its vertices and commutes with the transition rule.

For `H>=1`, form the usual order-`H` path graph: its vertices are directed
walks of length `H-1` in `G_r`, and its arcs are directed walks of length
`H`.  It is again `d`-in/`d`-out regular.  An Euler circuit (componentwise,
with all components taken together) lists every directed `H`-walk once.
Reading the underlying queue states gives a deterministic family of de
Bruijn schedules.

### Theorem 3.1 (exact simultaneous cylinder balance)

Across this family every queue state occurs with the same multiplicity, and
every directed `q`-continuation from it occurs with the same multiplicity
for every `q<=H`.  Therefore, for every `t`-set `Q`,

\[
 F_0(Q)=\Lambda\binom{K-t}{r-t}
\tag{3.1}
\]

for a common integer scale `Lambda`, and

\[
 \boxed{
 F_q(Q)=F_0(Q)\frac{\binom{r-q}{t}}{\binom rt}}
 \qquad(0\le q\le H).
\tag{3.2}
\]

Moreover, the number `b_Q` of maximal containing blocks satisfies

\[
 \boxed{b_Q=\frac trF_0(Q)},
 \qquad
 \frac{F_0(Q)}{b_Q}=\frac rt.
\tag{3.3}
\]

#### Proof

The de Bruijn/Euler construction gives uniform multiplicity for every
starting ordered queue and every continuation of length at most `H`.
There are `r! binom(K-t,r-t)` ordered queues whose active set contains `Q`;
the factor `r!` is absorbed into `Lambda`.  For a uniform ordering, `Q`
survives `q` steps iff none of the first `q` entries lies in `Q`, which has
probability (1.1).  This proves (3.1)--(3.2).

In the cyclic indicator word of `Q`, the number of containing blocks equals
the number of exits.  An exit occurs exactly when the current queue contains
`Q` and its front letter lies in `Q`.  Exactly a `t/r` fraction of the
uniform ordered queues containing `Q` have this property.  This proves
(3.3).  QED.

After division by `Lambda`, (3.3) is precisely the nonexceptional
Catalan/ballot block theorem

\[
 b_Q=\frac tr\binom{2r-1-t}{r-t}.
\]

This gives a conceptual explanation of the finite exact paths: their forced
ballot block count is the multiplicity-one shadow of the uniform queue
hazard.

## 4. Two-sided freshness and exact fractional shadow balance

The queue theorem controls deletion survival.  To control intersections and
unions simultaneously through depth `H`, impose the finite-memory rule that
no coordinate may be flipped twice among any `H` consecutive Johnson swaps.
Equivalently, every such window is a Johnson geodesic: its `q` deletions and
`q` arrivals are pairwise distinct and disjoint for `q<=H`.

Encode a state by the current `r`-set together with its last `H` directed
swaps, whose `2H` labels are distinct.  A legal next swap deletes one of the
`r-H` active labels not among the recent arrivals and inserts one of the
`r-1-H` inactive labels not among the recent deletions.  Hence the finite
state graph is regular of degree

\[
 D_H=(r-H)(r-1-H)
 \qquad(H\le r-2),
\tag{4.1}
\]

with equal indegree by time reversal.  Apply the same higher-block Euler
construction to this graph.  Componentwise it enumerates all legal local
histories with equal multiplicity.  By `S_K`-symmetry:

* every rank-`(r-q)` intersection target has the same aggregate load;
* every rank-`(r+q)` union target has the same aggregate load;
* all windows through depth `H` have the correct ranks `r-q` and `r+q`.

Thus there is an exact, integral, deterministic **high-multiplicity** cover
whose normalized lower and upper shadow vectors are perfectly uniform at
every depth `q<=H`.  This is stronger than a fractional LP witness and more
structured than independent random sampling.  It proves that simultaneous
freshness and hazard balance are locally compatible.

It still does not select each middle set once.

## 5. The precise sufficient selection lemma

The preceding theorem suggests the following clean target.  It uses only
finite memory `H`, not the full length-`r` queue constraint.

### Fresh-rotor transversal Catalan lemma (open)

For `K=2r-1` and `H=H(r)`, the high-multiplicity fresh rotor cover has a
subpath/section `P=(T_0,...,T_{W-1})` such that:

1. the projections `T_i` are all `r`-sets exactly once;
2. consecutive intersections are distinct and omit only the prescribed
   terminal colour `C_*`;
3. every `q<=H` window is fresh (all `2q` flip labels are distinct);
4. writing `L_q^-` and `L_q^+` for its rank-`(r-q)` intersection and
   rank-`(r+q)` union load vectors, their aggregate factorial excess obeys

\[
 \sum_{q\le H}\left(
 \sum_S(L_q^-(S)-c_q^-)(L_q^-(S)-c_q^--1)
 +\sum_U(L_q^+(U)-c_q^+)(L_q^+(U)-c_q^+-1)
 \right)=o(W),
\tag{5.1}
\]

with the usual floor loads `c_q^\pm`.

Conditions 1--2 give the endpoint-rooted one-hole lower-rainbow path;
condition 3 gives the residence/freshness required by the factor compiler;
condition 4 is CPCR at every required shadow.  Therefore this lemma is a
direct sufficient statement for the chronological half of the
Catalan-design path theorem.

The useful reformulation is:

> **The hazard problem is an integral transversal/rounding problem inside
> an exactly balanced de Bruijn rotor cover.**

The exact high-multiplicity object is already present.  The missing theorem
must round multiplicity `Lambda` to one while preserving one lower-rainbow
constraint and aggregate cylinder discrepancy.

This rounding problem is now formalized in
`MATH_FRESH_ROTOR_TRANSVERSAL_ROUNDING_GATE_20260727.md`.  The decisive
refinement is that (5.1) is a **pair-collision** objective, whereas the rotor
cover proves only one-point cylinder balance.  At depth one the central and
lower constraints reduce to a bipartite 2-factor, but adjoining upper-colour
coverage produces a Boolean-diamond matrix with a determinant-two minor.
Thus neither total unimodularity nor ordinary marginal-preserving dependent
rounding closes the lemma.

## 6. A genuine obstruction to naive per-section balancing

The scalar construction in Theorem 2.1 cannot simply be performed
independently for every `Q`.  Section indicators of actual sets satisfy the
pointwise Boolean compatibility laws

\[
 \mathbf1_{Q\cup R\subseteq T_i}
 =\mathbf1_{Q\subseteq T_i}\mathbf1_{R\subseteq T_i},
 \qquad
 \sum_{|Q|=t}\mathbf1_{Q\subseteq T_i}=\binom rt.
\tag{6.1}
\]

Independent balanced words almost never satisfy (6.1).  This is why the
queue rotor is the right ambient object: it enforces all Boolean
compatibility identities automatically.  A proof based only on separate
Sturmian/Beatty schedules for each section cannot work without an additional
coupling theorem at least as strong as (6.1).

### 6.1 The transversal already contains the central subset-Ucycle problem

There is an important scope warning about the *full-queue* version.  A path
in the queue graph whose
projection uses every `r`-set once is exactly a sliding-window universal
cycle (or path) for the `r`-subsets of `[2r-1]`: the symbol stream is obtained
by reading the successive appended letters, and its length-`r` windows are
the projected active sets.  Requiring the lower overlaps to be rainbow asks
in addition that the length-`(r-1)` windows enumerate that adjacent rank.

Thus a full-queue transversal is not a routine rotor rounding statement.  It
strictly contains the linear-uniformity subset-Ucycle problem already
audited in `MATH_AUDIT_BINARY_ROTOR_VS_SUBSET_UCYCLE_LITERATURE_20260726.md`.
Known fixed-uniformity and `r=o(K)` near-Ucycle results do not cover
`K=2r-1`.  The exact high-multiplicity theorem is new/useful as a
compatibility certificate, but it does not evade that literature boundary.

The finite-memory fresh-rotor lemma in Section 5 is genuinely weaker when
`H=o(r)`: it asks only that no coordinate be reused inside an `H`-window,
not that every active coordinate remain for exactly `r` steps.  It is the
right formulation if the factor compiler needs only delay
`H=Theta(sqrt(r))`.  Whether that weaker transversal can be obtained from
PBBS/middle-levels machinery is not settled by the Ucycle literature
boundary.

## 7. What is established rotor theory, and what remains conjectural

Established/elementary:

1. Euler tours balance outgoing arcs exactly in finite Eulerian digraphs.
2. Passing to the order-`H` path graph produces a de Bruijn schedule which
   enumerates all length-`H` cylinders exactly.
3. Applied to the queue graph, this proves Theorem 3.1.
4. Applied componentwise to the finite-memory fresh-exchange graph, it gives
   exact high-multiplicity lower/upper balance.

Not supplied by standard rotor-router discrepancy theorems:

1. a transversal containing one lift of every projected `r`-set;
2. Hamilton connectivity of that transversal;
3. the one-hole lower-rainbow property;
4. preservation of CPCR after reducing multiplicity from `Lambda` to one.

Already item 1 together with queue adjacency is the central subset-Ucycle
gate; item 3 strengthens it further.

Generic rotor-router occupation bounds concern discrepancies of a walk from
a Markov chain.  Their constants depend on global graph parameters and they
do not perform the required projection-transversal rounding.  Invoking them
without a separate integral selection theorem would merely relocate the
original gap.

## 8. Recommended mathematical attack

Work in the exactly balanced fresh rotor cover, not directly in the space of
Hamilton paths.  The next theorem should be a discrepancy-constrained
transversal theorem with three matroid-like constraints:

1. one representative above each middle set;
2. one representative above each lower colour (apart from `C_*`);
3. small aggregate cylinder discrepancy through depth `H`.

The first two are the two sides of the middle-levels incidence graph; the
third consists of nested cylinder counts in the de Bruijn lift.  Any total
unimodularity, exchange, or dependent-rounding structure must exploit that
nestedness.  Independent rounding destroys adjacency, while arbitrary
Hamilton switching destroys the queue cylinder law.

The exact queue theorem proves that the desired local statistics are not in
conflict.  The remaining difficulty is global and integral, exactly in line
with the rest of the coefficient-one program.
