# Capacitated chain majorisation is not sufficient: the exact Hall ladder

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional counterexample, unconditional exact finite
characterization after the time slices are chosen, and a proof-safe
identification of the Boolean frontier.  This note does **not** prove an
atomic-to-named Boolean flag lift or an additive upper bound for `nu(k)`.

## 0. Outcome

Let `P` be a finite ranked poset, let

\[
                         c_1\ge\cdots\ge c_W\ge0
\tag{0.1}
\]

be proposed chain capacities, and put

\[
                         K_q=|\{i:c_i\ge q\}|.
\tag{0.2}
\]

If `P` can be partitioned into chains of lengths at most `c_i`, then, for
every `p`,

\[
 a_p(P)\le \sum_{i=1}^W\min(c_i,p),
\tag{0.3}
\]

where `a_p(P)` is the maximum cardinality of a union of `p` antichains.  In
a strongly Sperner ranked poset, `a_p(P)` is the sum of the `p` largest rank
sizes.  Thus (0.3) is exactly the proposed rank-majorisation test.

This note proves that (0.3), even together with total capacity, is **not
sufficient**.  The failure persists in a connected, pure, normal,
rank-symmetric, rank-unimodal, strongly Sperner poset, and every relevant
majorisation inequality in the example is strict.

The exact replacement is the following ordered-slice condition.

> Partition the named elements into time slices `A_1,...,A_D`, with
> `|A_q|<=K_q`, and find an inclusion matching
>
> \[
>                 A_{q+1}\hookrightarrow A_q
>                 \qquad(1\le q<D)
> \tag{0.4}
> \]
>
> at every adjacent interface.

For fixed slices these are ordinary Hall matchings, and they are necessary
and sufficient.  The atomic rank histogram is only the projection obtained
after the named slices and all the Hall incidences in (0.4) have been
forgotten.

For the Boolean lattice there is a sharper positive statement: if every
row of the rank schedule is supported on one consecutive rank interval in
the nondecreasing half, normalized matching lifts the interval rows to
named skipless Boolean chains automatically.  Thus the immediate rank-only
gate is not arbitrary named chainization but the construction of a
capacity-compatible **interval** histogram.  A second exact counterexample
below shows that atomic Gale majorisation does not imply this interval
property.

Finally, applying the proposed majorisation implication to the full Boolean
lattice with the balanced floor/ceiling capacity vector would prove
Furedi's uniform-chain conjecture exactly.  Therefore no unquoted
Greene--Kleitman or min-cost-flow theorem can be used to close the Boolean
lift: such a theorem would cross a known open frontier.

## 1. The necessary Greene--Kleitman cuts

For a positive integer `p`, define

\[
 a_p(P)=\max\{|X|:X\text{ is the union of }p\text{ antichains of }P\}.
\tag{1.1}
\]

### Proposition 1.1 (capacitated `p`-family inequality)

If

\[
                         P=C_1\mathbin{\dot\cup}\cdots
                           \mathbin{\dot\cup} C_W,
                         \qquad |C_i|\le c_i,
\tag{1.2}
\]

with every `C_i` a chain, then (0.3) holds for every `p`.

#### Proof

Let `X` be a union of `p` antichains.  A chain meets each antichain at most
once, so

\[
                         |X\cap C_i|\le p.
\]

It also satisfies `|X cap C_i|<=|C_i|<=c_i`.  Hence

\[
 |X|=\sum_i|X\cap C_i|
     \le\sum_i\min(c_i,p).
\]

Maximize over `X`. `square`

The Greene--Kleitman min--max theorem states, for each fixed `p`,

\[
 a_p(P)=
 \min_{\mathscr C\text{ a chain partition of }P}
       \sum_{C\in\mathscr C}\min(p,|C|).
\tag{1.3}
\]

Equation (1.3) does not say that a capacity vector whose truncated sums
dominate all the separate minima is itself realized by one chain partition.
The minimizing partition may depend on the requested objective, and
component fragmentation is invisible to the scalar quantities `a_p(P)`.
Section 3 gives a counterexample even when the poset is strongly Sperner,
so that

\[
                         a_p(P)=\text{sum of the `p` largest rank sizes}.
\tag{1.4}
\]

## 2. Exact capacitated Hall-ladder theorem

Empty chains are permitted.  Put `D=max_i c_i`, and use the convention that
`A_(D+1)` is empty.

### Theorem 2.1 (capacitated ordered-slice equivalence)

The following are equivalent.

1. `P` has a partition into at most `W` chains which can be injected into
   the capacity bins so that the chain in bin `i` has size at most `c_i`.
2. There is a partition

   \[
                          P=A_1\mathbin{\dot\cup}\cdots
                              \mathbin{\dot\cup}A_D
   \tag{2.1}
   \]

   satisfying

   \[
                          |A_q|\le K_q\qquad(1\le q\le D),
   \tag{2.2}
   \]

   together with injections

   \[
       \mu_q:A_{q+1}\longrightarrow A_q,
       \qquad x<\mu_q(x),
       \qquad 1\le q<D.
   \tag{2.3}
   \]

For fixed slices, condition (2.3) is equivalent to the ordinary Hall rows

\[
 |N_{A_q}(X)|\ge|X|
 \qquad(X\subseteq A_{q+1},\ 1\le q<D),
\tag{2.4}
\]

where the edges are strict comparabilities directed toward `A_q`.

#### Proof

Assume first that the chain packing is given.  Order each nonempty chain
from its maximum downward, and put its `q`-th member into `A_q`.  Consecutive
members give (2.3).  A chain contributes to `A_q` exactly when its length is
at least `q`; since it is assigned to a bin of capacity at least its length,
there are at most `K_q` such chains.  This proves (2.2).

Conversely, orient every edge in (2.3) from `A_(q+1)` toward `A_q`.  Every
vertex outside `A_1` has one outgoing edge, injectivity gives indegree at
most one, and the slice index strictly decreases.  The components are
therefore disjoint directed paths ending in `A_1`.  Transitivity makes each
path a chain, and the paths partition `P`.

Let their lengths, in decreasing order, be

\[
                          \ell_1\ge\ell_2\ge\cdots.
\]

The conjugate count is

\[
                          |\{j:\ell_j\ge q\}|=|A_q|\le K_q
                          =|\{i:c_i\ge q\}|.
\tag{2.5}
\]

These inequalities imply `ell_j<=c_j` for every `j`.  Indeed, if
`ell_j>c_j`, take `q=c_j+1`.  At least `j` path lengths are at least `q`,
whereas at most `j-1` capacities are at least `q`, contradicting (2.5).
Assign the paths in decreasing order to the capacities in decreasing
order.  This proves the packing.

For fixed slices, (2.3) is a bipartite matching saturating `A_(q+1)` at
each interface.  Hall's theorem gives (2.4). `square`

### Interpretation

Theorem 2.1 is an exact finite min--max theorem **after** the chronology
slices have been selected.  The different interface matchings may be found
independently: their union automatically consists of paths because slice
indices decrease.

What is not a flow variable in this theorem is the partition of every named
poset element among the slices.  Forgetting those names and retaining only
the number of rank-`s` elements in each row gives the atomic zero--one
histogram.  That projection forgets every neighborhood in (2.4), and this
loss is real.

## 2A. Positive Boolean theorem: interval rows lift automatically

The Boolean lattice has one important structure not present in an arbitrary
normal poset.  If the rank support of every row is a single interval, then
the naming problem can be solved rank by rank.

Let

\[
                         {\cal B}_s={[k]\choose s},
                         \qquad C_s=|{\cal B}_s|,
\tag{2.6}
\]

and restrict to a rank interval on which `C_s<=C_(s+1)`.  Let
`I_i=[a_i,b_i]` be integer intervals, empty intervals being allowed, and
suppose

\[
              |I_i|\le c_i,
              \qquad
              n_s=|\{i:s\in I_i\}|\le C_s.
\tag{2.7}
\]

### Theorem 2.2 (interval-histogram Boolean lift)

There are sets

\[
                         S_{i,s}\in{\cal B}_s
                         \qquad(s\in I_i)
\tag{2.8}
\]

such that

1. for every rank `s`, the `n_s` sets `S_(i,s)` are distinct; and
2. for every `i` and every two consecutive ranks in `I_i`,

   \[
                         S_{i,s}\subset S_{i,s+1}.
   \tag{2.9}
   \]

Thus every interval row lifts to a literal skipless Boolean chain of length
at most `c_i`.  If `n_s=C_s`, the construction uses the complete named
rank-`s` layer.

#### Proof

Proceed upward through the ranks.  At the first rank, assign arbitrary
distinct sets to the labels whose intervals start there.

Suppose rank `s` has been assigned.  Let `A` be the family of current sets
on labels which continue from `s` to `s+1`.  The upper-shadow graph from
`B_s` to `B_(s+1)` satisfies normalized matching.  Directly, edge counting
gives, for every \(X\subseteq{\cal B}_s\),

\[
 |N(X)|\ge {k-s\over s+1}|X|
          ={C_{s+1}\over C_s}|X|
          \ge |X|.
\tag{2.10}
\]

Hall therefore matches all members of `A` to distinct containing
rank-`s+1` sets.  Assign those sets to the continuing labels.  The number
of new labels starting at rank `s+1` is

\[
                         n_{s+1}-|A|.
\]

At least `C_(s+1)-|A|>=n_(s+1)-|A|` rank-`s+1` sets remain unused, so assign
arbitrary distinct unused sets to the new labels.  This maintains both
invariants and completes the induction. `square`

### Scope of Theorem 2.2

The theorem prescribes the rank cardinalities but is free to choose which
named sets survive in a punctured layer.  If an arbitrary family
\(X_s\subseteq{\cal B}_s\) is frozen in advance, the continuation matching must land
inside `X_(s+1)`; full-layer normalized matching no longer proves Hall.
Thus the theorem applies directly to complete layers and to a construction
in which the boundary deletions are co-chosen.  Prescribed literal
punctures require the Hall ladder of Theorem 2.1.

This theorem sharpens the surviving rank-only gate:

\[
 \boxed{
 \text{find a capacity-compatible interval decomposition of the rank
 histogram};
 \quad
 \text{then Boolean naming is automatic}.}
\tag{2.11}
\]

An arbitrary atomic Gale matrix need not have interval row supports.

## 2B. Exact rank-only interval formulations

Let the rank positions be `1,...,m`.  For `1<=a<=b<=m` with
`b-a+1<=D`, let `x_(a,b)` denote the number of rows with interval support
`[a,b]`.

### Proposition 2.3 (exact heterogeneous interval integer system)

A histogram `n_1,...,n_m` has an interval decomposition assignable to the
capacities `c_1,...,c_W` if and only if there are nonnegative integers
`x_(a,b)` satisfying

\[
 \sum_{a\le s\le b}x_{a,b}=n_s
                         \qquad(1\le s\le m),
\tag{2.12}
\]

and

\[
 \sum_{b-a+1\ge q}x_{a,b}\le K_q
                         \qquad(1\le q\le D).
\tag{2.13}
\]

#### Proof

An interval family gives (2.12), while (2.13) says that the number of
intervals of length at least `q` does not exceed the number of capacities
of size at least `q`.

Conversely, expand every integer `x_(a,b)` into that many literal interval
rows.  Sort their lengths decreasingly.  The conjugate inequalities
(2.13), by the same argument as (2.5), match the `j`-th largest interval
to `c_j`.  Pad with empty rows. `square`

The system (2.12)--(2.13) is the precise one-dimensional target for the
nonuniform collar capacities.  The atomic Gale system drops the
consecutive-support requirement from (2.12).

There is a useful family of necessary geometric cuts.  For a set `S` of
rank positions, put

\[
 \alpha_c(S)=
 \max\{|I\cap S|:I\text{ is an interval and }|I|\le c\},
 \qquad \alpha_0(S)=0.
\tag{2.14}
\]

Every interval decomposition satisfies

\[
                 \boxed{
                 \sum_{s\in S}n_s
                 \le\sum_{i=1}^W\alpha_{c_i}(S).}
\tag{2.15}
\]

Indeed, the interval placed in bin `i` contributes at most
`alpha_(c_i)(S)` to the left side.  When the points of `S` are pairwise at
distance at least `D`, every nonempty bin contributes at most one, and
(2.15) becomes

\[
                         \sum_{s\in S}n_s\le K_1.
\tag{2.16}
\]

These temporal-separation cuts are absent from rank majorisation.

For equal capacities there is a complete cut theorem.  Let `c_i=D` for
`1<=i<=W`, let `mathcal I_D` be all nonempty intervals of length at most
`D`, and define

\[
 \kappa_D(n)=
 \min\left\{
       \sum_{I\in\mathcal I_D}x_I:
       x_I\ge0\text{ integral},\quad
       \sum_{I\ni s}x_I=n_s\ (s\in[m])
     \right\}.
\tag{2.17}
\]

### Theorem 2.4 (uniform-capacity interval min--max)

The histogram has a decomposition into at most `W` intervals of length at
most `D` if and only if `kappa_D(n)<=W`.  Moreover

\[
 \boxed{
 \kappa_D(n)=
 \max\left\{
       \sum_{s=1}^m n_sy_s:
       \sum_{s\in I}y_s\le1
       \quad(I\in\mathcal I_D)
     \right\}.}
\tag{2.18}
\]

The dual variables `y_s` are unrestricted real numbers.

#### Proof

The position-by-interval incidence matrix has the consecutive-ones
property in every column and is therefore totally unimodular.  The linear
relaxation of (2.17) has an integral optimum for the integral right side
`n`.  Ordinary linear-programming duality gives (2.18).  Singletons make
the primal feasible.  Finally, an optimum with at most `W` intervals may
be padded with empty rows, and every `W`-row decomposition is a feasible
solution of value at most `W`. `square`

Theorem 2.4 is an exact min-cost-flow/TU answer for equal capacities.  It
also shows why cardinality-only majorisation is incomplete: its dual tests
do not include rank-position weight vectors such as separated spikes.

For the monotone histograms occurring below, the dual and the optimum have
a closed form.

### Theorem 2.5 (exact monotone uniform-capacity formula)

If

\[
                         0\le n_1\le n_2\le\cdots\le n_m,
\tag{2.19}
\]

then

\[
 \boxed{
 \kappa_D(n)=
 \sum_{\substack{j\ge0\\m-jD\ge1}}n_{m-jD}.}
\tag{2.20}
\]

#### Proof

Draw the Ferrers histogram with `n_s` cells in column `s`.  For every
height `1<=y<=n_m`, the occupied columns form a suffix `[a_y,m]`; let its
length be `L_y=m-a_y+1`.  Cut that suffix into
`ceil(L_y/D)` consecutive intervals, each of length at most `D`.  Over all
heights these intervals cover the histogram exactly.  Their number is

\[
 \begin{aligned}
 \sum_{y=1}^{n_m}\left\lceil{L_y\over D}\right\rceil
 &=\sum_{j\ge0}|\{y:L_y>jD\}|\\
 &=\sum_{\substack{j\ge0\\m-jD\ge1}}n_{m-jD}.
 \end{aligned}
\tag{2.21}
\]

For the reverse inequality, take the separated rank set

\[
                         \{m,m-D,m-2D,\ldots\}.
\]

An interval of length at most `D` meets this set at most once.  Therefore
every exact interval decomposition uses at least the right side of (2.20)
intervals.  The construction attains the bound. `square`

Thus, for a nondecreasing rank histogram and equal capacity `D`, the worst
dual cut is an explicit `D`-spaced comb.  This statement is special to the
uniform maximum length; it does not assign the resulting intervals to a
heterogeneous capacity multiset.

## 2C. The separated-spike obstruction is absent in the triangular
binomial profile

Return to the parameters of the atomic histogram theorem:

\[
 r=\left\lceil{k\over2}\right\rceil,
 \qquad W={k\choose r},
\qquad D=d(k),
 \qquad t_0=r-D,
 \qquad K_1=W-{k\choose t_0}.
\tag{2.22}
\]

The simplest interval obstruction is (2.16), with ranks separated by at
least `D`.  It does not occur here.

### Theorem 2.6 (uniform gap in every `D`-separated cut)

There are absolute constants `delta>0` and `k_0` such that, for `k>=k_0`,
every set

\[
 S\subseteq\{0,1,\ldots,t_0-1\},
 \qquad |s-s'|\ge D\quad(s\ne s')
\tag{2.23}
\]

satisfies

\[
 \sum_{s\in S}{k\choose s}
 \le K_1-\delta W.
\tag{2.24}
\]

The same statement holds after any triangular boundary deletions.

#### Proof

The binomial coefficients are increasing below the middle rank.  If the
members of `S` are listed decreasingly, its `j`-th member is at most
`t_0-1-jD`.  Hence

\[
 {1\over W}\sum_{s\in S}{k\choose s}
 \le {1\over W}\sum_{j\ge0}{k\choose t_0-1-jD}.
\tag{2.25}
\]

Put `a=pi/4`.  The standard central-binomial local estimate and

\[
                         D=\sqrt{{\pi k\over8}}+O(1)
\tag{2.26}
\]

give, for every fixed `j`,

\[
 {1\over W}{k\choose t_0-1-jD}
 \longrightarrow e^{-a(j+1)^2}.
\tag{2.27}
\]

The convergence may be summed over `j`.  Indeed, the product formula for
the ratio of an off-central binomial coefficient to `W`, together with
`log(1-u)<=-u`, bounds the `j`-th term by `exp(-c j^2)` for one absolute
`c>0`, uniformly in large `k`; after the rank index reaches zero the terms
vanish.  Dominated convergence therefore turns (2.25) into

\[
 \limsup {1\over W}\sum_{s\in S}{k\choose s}
 \le\sum_{j\ge1}e^{-aj^2}.
\tag{2.28}
\]

On the other hand,

\[
                         {K_1\over W}\longrightarrow1-e^{-a}.
\tag{2.29}
\]

The limiting gap is strictly positive:

\[
 \Delta=1-e^{-a}-\sum_{j\ge1}e^{-aj^2}
       =1-2e^{-a}-\sum_{j\ge2}e^{-aj^2}>0.
\tag{2.30}
\]

For completeness, positivity needs no numerical oracle.  Since
`a=pi/4>3/4`, elementary exponential-series bounds give

\[
 2e^{-a}<0.946,
 \qquad e^{-4a}<0.05.
\]

For `j>=3`, `j^2>=3j`, while `e^{-9a}<1/400` and
`e^{-3a}<1/7`; hence

\[
 \sum_{j\ge3}e^{-aj^2}
 \le {e^{-9a}\over1-e^{-3a}}
 <{7\over2400}.
\tag{2.31}
\]

The sum of the three displayed upper bounds is below one, proving
`Delta>0`.  Take any fixed `delta<Delta/3` and absorb the two `o(1)` terms
in (2.28)--(2.29).  Boundary deletions only lower the left side. `square`

Theorem 2.6 removes exactly the two-spike mechanism in Section 3, uniformly
over arbitrarily many separated ranks.  It does **not** prove the full
heterogeneous interval system: general dual weights and the nested
length-capacity rows (2.13) remain.

Combined with Theorem 2.5, it gives the exact positive statement

\[
 \kappa_D\left(\left({k\choose s}\right)_{1\le s<t_0}\right)
 \le K_1-\delta W.
\tag{2.32}
\]

Thus the complete residual binomial histogram fits into strictly fewer
than `K_1` intervals if every active socket is temporarily upgraded to
capacity `D`.  The number of active sockets is not the obstruction.  The
remaining one-dimensional gate is precisely assignment to their true,
highly nonuniform capacities `c_i` through (2.13).

## 3. A connected normal strong-Sperner counterexample

Let `P` have a bottom element `0`, a top element `1`, and three internally
disjoint arms

\[
 0<a_{j,1}<a_{j,2}<a_{j,3}<a_{j,4}<1
 \qquad(j=1,2,3),
\tag{3.1}
\]

with no comparabilities between internal elements of different arms.  Its
rank sizes are

\[
                              1,3,3,3,3,1.
\tag{3.2}
\]

The poset is connected and pure.  It is rank-symmetric and rank-unimodal.
It also has the normalized matching property.  Between consecutive
three-element internal ranks the cover graph is a perfect matching.  From
the bottom to the first internal rank every neighbor is available, and
from any nonempty subset of the last internal rank the upper neighborhood
is the singleton top.  The normalized inequalities follow immediately.
It even has an explicit symmetric-chain decomposition: put both endpoints
on the first arm and take each of the other two arms as its own chain.  The
three rank intervals are respectively `[0,5]`, `[1,4]`, and `[1,4]`.

It is strongly Sperner.  For `1<=p<=4`, the union of `p` internal ranks has
size `3p`.  If a union of `p` antichains uses `s` of the two endpoints, then
those endpoints occupy `s` singleton antichains because each endpoint is
comparable with every element.  Its size is at most

\[
                         s+3(p-s)\le3p.
\tag{3.3}
\]

For `p=5`, the maximum is the twelve internal elements plus one endpoint,
of size `13`; for `p=6`, it is all `14` elements.  Hence

\[
                 (a_1,a_2,a_3,a_4,a_5,a_6)
                    =(3,6,9,12,13,14),
\tag{3.4}
\]

exactly the partial sums of the largest rank sizes.

Now take five bins, each of capacity three:

\[
                              c=(3,3,3,3,3).
\tag{3.5}
\]

The right side of (0.3) is

\[
              \sum_i\min(c_i,p)=(5,10,15,15,15,15)
              \qquad(1\le p\le6).
\tag{3.6}
\]

Every inequality is strict, and the total capacity is `15>14`.

The corresponding atomic rank schedule exists.  Number the ranks
`0,1,...,5`; the following five row supports have size at most three and
give the exact column sums (3.2):

\[
 \begin{array}{c|c}
 1&\{0,1,2\}\\
 2&\{1,3,4\}\\
 3&\{1,2,3\}\\
 4&\{2,3,4\}\\
 5&\{4,5\}.
 \end{array}
\tag{3.7}
\]

This atomic schedule cannot be replaced by five interval rows of length at
most three.  Take the separated rank set `S={1,4}`.  No interval of length
three meets both positions, while

\[
                         n_1+n_4=3+3=6>5=K_1.
\tag{3.8}
\]

Thus (2.16) fails.  Equivalently, the dual vector with
`y_1=y_4=1` and every other `y_s=0` certifies
`kappa_3(n)>=6` in (2.18).

Nevertheless there is no named chain lift.  A chain can meet internal
elements from at most one arm.  Each arm has four internal elements, and a
capacity-three chain covers at most three of them.  Therefore each arm
requires at least two distinct chains.  The chain families used by
different arms are disjoint, so at least six chains are necessary.  Only
five bins are available.

Thus rank symmetry, rank unimodality, normalized matching, strong Sperner,
connectedness, purity, total slack, and strict `p`-family slack do not make
the majorisation test sufficient.  At rank level, the missing invariant is
already the consecutive-support condition.  In fact, the internal
nondecreasing band of this example itself satisfies the adjacent Hall
expansion used in Theorem 2.2.  If an interval histogram existed, naming
would succeed; the failure occurs entirely in interval feasibility, before
any further named-set obstruction. `square`

## 4. Why a Boolean majorisation theorem would settle the uniform-chain
frontier

Let

\[
 N=2^k,
 \qquad W={k\choose\lfloor k/2\rfloor},
 \qquad a=\left\lfloor{N\over W}\right\rfloor,
 \qquad b=N-aW.
\tag{4.1}
\]

Give `b` bins capacity `a+1` and the remaining `W-b` bins capacity `a`.
The total capacity is exactly `N`.

The Boolean lattice is strongly Sperner.  For `p<=a`, the sum of its `p`
largest ranks is at most `pW`, while

\[
                         \sum_i\min(c_i,p)=pW.
\tag{4.2}
\]

For `p>=a+1`, the right side is the total capacity `N`, so the cut is again
automatic.  Thus every proposed majorisation inequality holds.

If those inequalities were sufficient for Boolean lattices, they would
give a partition of `B_k` into `W` chains of sizes at most the displayed
capacities.  Since the chain sizes and capacities have the same total,
every capacity would be saturated.  There would be exactly `b` chains of
size `a+1` and `W-b` chains of size `a`.

That is precisely the floor/ceiling uniform-chain conjecture attributed to
Furedi.  It is not supplied by the Greene--Kleitman symmetric-chain
decomposition, by normalized matching, or by the presently known
asymptotically uniform decompositions.  This implication does not prove
that the particular lower-ideal collar capacities are impossible; it
proves that a blanket Boolean majorisation theorem would resolve a major
open chain-decomposition problem.

Theorem 2.2 itself is deliberately one-sided: it lifts interval rows only
on a nondecreasing rank interval.  It therefore does not, without an
additional middle-rank gluing argument, lift an arbitrary balanced
full-lattice interval histogram.  The Furedi-frontier implication above is
the direct implication from a hypothetical Boolean majorisation theorem.
For the lower-ideal application of this note, all relevant ranks lie in the
nondecreasing half, so Theorem 2.2 applies exactly as stated.

## 5. Exact implication for the atomic Boolean histogram

In the atomic histogram theorem, the capacity conjugate is

\[
                         K_q=W-{k\choose t_0+q-1},
                         \qquad 1\le q\le D,
\tag{5.1}
\]

and the Gaussian pair estimate proves every proper rank-majorisation cut
with uniform linear margin.  Section 3 shows that neither strict margin nor
normality can by itself upgrade an atomic matrix to named chains.

The exact static theorem still required is therefore the following.

### Atomic Boolean interval target

First solve the integer interval system (2.12)--(2.13) for the triangular
residual counts.  If the boundary deletion identities may be selected
together with the intervals, Theorem 2.2 then gives all named residual
chains without another Hall loss.

If the retained named targets are frozen in advance, or if their attachment
to fixed literal collar sockets is already prescribed, the stronger Hall
form is required:

### Prescribed-name Boolean Hall-ladder target

Partition the retained **named** lower targets into

\[
                         A_1\mathbin{\dot\cup}\cdots
                         \mathbin{\dot\cup}A_D
\tag{5.2}
\]

so that

\[
 |A_q|\le K_q
 \quad\text{and}\quad
 |N_{A_q}(X)|\ge|X|
 \quad(X\subseteq A_{q+1})
\tag{5.3}
\]

for every `q`.  Theorem 2.1 then gives the residual inclusion chains.
Their maxima must additionally be matched, with the correct length
eligibility, to containing collar-start sockets and thence to distinct
owners.  The existing joint-start orbit theorem performs this last step on
complete-layer flag batches; it does not apply to an arbitrary atomically
split family.

There are three useful positive faces.

1. An interval rank schedule in the nondecreasing Boolean half lifts by
   Theorem 2.2; no complete-layer orbit decomposition is required.
2. In a complete layered order, where every lower-rank element lies below
   every higher-rank element, even an arbitrary atomic matrix lifts by
   assigning each rank arbitrarily to its occupied rows.  Boolean
   containment is sparse, so this stronger argument is unavailable.
3. Once the named slices in (5.2) are chosen and their adjacent inclusion
   graphs satisfy normalized matching in the expanding direction, (5.3)
   follows and the lift is integral.  The missing work is the correlated
   selection of those slices, not the rounding of a fixed Hall ladder.

Thus the proof-safe boundary is

\[
\boxed{
 \text{atomic rank majorisation}
 \;\not\!\Longrightarrow\;
 \text{interval rank rows}
 \;\Longrightarrow\;
 \text{adaptively named Boolean flags};
 \qquad
 \text{named capacity-respecting Hall ladder}
 \;\Longleftrightarrow\;
 \text{capacitated chain packing}.}
\tag{5.4}
\]

The subsequent literal run automata, owner chronology, upper deck, and
safe opening remain separate gates even after (5.4) is solved.
