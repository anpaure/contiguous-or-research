# Ideal chainization: the normalized-ladder theorem and two quantitative chronology walls

Date: 2026-08-01  
Status: unconditional fixed-chronology theorem, unconditional asymptotic
obstructions to two canonical chronology choices, and an established
factor-two fallback.  This note does **not** refute depth-`d+O(1)`
chainization for the complete Boolean lower ideal.

## 0. Verdict

Put

\[
 r=\lceil k/2\rceil,\qquad W={k\choose r},\qquad
 \Lambda=\sum_{s=1}^{r-1}{k\choose s},\qquad
 D=\left\lceil {\Lambda\over W}\right\rceil .       \tag{0.1}
\]

Item `2416ROOT` proves an integral containment SDR into `D` labelled
slots at each rank-`r` owner and `D<=d+1`.  It does not choose which
targets should be consecutive members of one owner chain.

The strongest clean positive statement is the following.

> Once the targets have been assigned to `q` ordered time slices, the
> chainization problem is exactly a ladder of ordinary bipartite
> matchings.  If every adjacent slice interface is a normalized-matching
> graph in the expanding direction, the ladder is integral and gives
> owner chains of depth at most `q`.

Thus fixed chronology is polynomial and integral.  Choosing the slices is
the correlation gate.

Two natural ways of choosing them do not reach `D+O(1)`.

1. Consecutive full-rank blocks require `D+Theta(sqrt(k))` slices already
   from scalar indivisibility of the central ranks.
2. Cutting any symmetric-chain decomposition into `D`-pieces, without
   cross-chain splicing, creates

   \[
                    (e^{-\pi/4}-o(1))W                 \tag{0.2}
   \]

   more fragments than there are middle owners.

Consequently a successful `d+O(1)` theorem must interleave ranks inside
the time slices, or equivalently perform `Theta(W)` correlated exchanges
between the original symmetric chains.  Ordinary normalized matching and
an unmodified Greene--Kleitman SCD do not supply those exchanges.

## 1. Exact ordered-slice equivalence

Let

\[
 {\cal L}=\{S\subseteq[k]:1\le |S|<r\},\qquad
 {\cal O}={ [k]\choose r}.                              \tag{1.1}
\]

An **anchored `q`-chain factor** is a family `(C_T:T in O)` which
partitions `L`, in which every `C_T` is an inclusion chain of at most `q`
targets and every member of `C_T` is contained in `T`.  Empty chains are
allowed.

### Theorem 1.1 (right-aligned ladder equivalence)

An anchored `q`-chain factor exists if and only if there is a partition

\[
                         {\cal L}=A_1\sqcup\cdots\sqcup A_q              \tag{1.2}
\]

and inclusion matchings

\[
 M_0:A_1\longrightarrow{\cal O},\qquad
 M_i:A_{i+1}\longrightarrow A_i\quad(1\le i<q)          \tag{1.3}
\]

which saturate their left shores.  Here `A_1` is the slice nearest the
owner.

For fixed slices, the exact min--max conditions are therefore

\[
 |X|\le |N_{{\cal O}}(X)|\quad(X\subseteq A_1),
 \qquad
 |X|\le |N_{A_i}(X)|\quad(X\subseteq A_{i+1}).           \tag{1.4}
\]

#### Proof

Given a chain factor, number each target by its distance below its owner.
The targets at distance `i` form `A_i`; consecutive members of each chain
give (1.3).

Conversely, orient every edge of `M_i` from `A_(i+1)` to `A_i` and every
edge of `M_0` toward its owner.  Every target has one outgoing edge and at
most one incoming edge.  Slice indices strictly decrease, so directed
cycles are impossible.  The components are target paths ending at
distinct owners.  Inclusion is transitive along a path, and there are at
most `q` target slices.  These paths are the required owner chains.
Hall's theorem gives (1.4).  \(\square\)

This is the sliced form of the fixed-chronology Hall theorem in
`MATH_THEOREM_IDEAL_CHAINIZATION_BLOSSOM_OBSTRUCTION_AND_CHRONOLOGY_HALL_20260801.md`.
The latter allows successor edges which skip empty time slices; compressing
the occupied positions of each path gives the form above.

### Corollary 1.2 (normalized-ladder criterion)

Suppose the slices in (1.2) satisfy

\[
 |A_q|\le\cdots\le |A_1|\le W,                         \tag{1.5}
\]

and every adjacent inclusion graph `(A_(i+1),A_i)` has the normalized
matching property in the direction `A_(i+1)->A_i`.  Suppose the same is
true of `(A_1,O)`.  Then an anchored `q`-chain factor exists.

Indeed, normalized matching gives

\[
 { |N(X)|\over |A_i|}\ge { |X|\over |A_{i+1}|},
\]

and (1.5) implies `|N(X)|>=|X|`.  Apply Theorem 1.1.

For laminar adjacent neighborhoods, only the laminar Hall cuts need be
checked.  For Ferrers/suffix neighborhoods, those cuts reduce further to
the usual ordered threshold inequalities and the antitone greedy matching.
These are genuine positive faces, but selecting Boolean slices which lie
on one of them is extra structure, not a consequence of the ideal SDR.

## 2. Full-rank blocks do give a normalized ladder

The most obvious attempt is to place whole consecutive ranks in one time
slice.  The following lemma shows that its only gate is the scalar block
sizes.

### Lemma 2.1 (separated unions of complete ranks match)

Let

\[
 A=\bigcup_{s\in I}{[k]\choose s},\qquad
 B=\bigcup_{t\in J}{[k]\choose t},qquad
             \max I<\min J.                              \tag{2.1}
\]

If `|A|<=|B|`, the inclusion graph has a matching saturating `A`.

#### Proof

Write `n_s=binom(k,s)`.  Choose nonnegative transportation numbers
`a_(s,t)` with row sums `n_s` and column sums at most `n_t`; this is
possible because the rank-index transportation graph is complete and
`|A|<=|B|`.

For `S` of rank `s`, send total mass `a_(s,t)/n_s` uniformly to its
rank-`t` supersets.  A fixed rank-`t` target receives from rank `s`

\[
 { {t\choose s}a_{s,t}\over
    n_s {k-s\choose t-s}}
   ={a_{s,t}\over n_t},                                  \tag{2.2}
\]

because

\[
 {k\choose s}{k-s\choose t-s}={k\choose t}{t\choose s}.
\]

Thus every left vertex sends one unit and every right vertex receives at
most one.  Bipartite integrality gives the matching.  \(\square\)

Consequently, if the lower ranks can be split into consecutive intervals
whose total sizes are nondecreasing toward the middle and at most `W`,
then Lemma 2.1 and Theorem 1.1 produce the desired anchored chains.

## 3. Consecutive rank blocks have a positive `sqrt(k)` toll

The preceding sufficient condition is quantitatively too rigid.

### Theorem 3.1 (rank-block toll)

For even `k=2m`, let `q_block(k)` be the minimum number of consecutive
rank intervals which partition ranks `1,...,m-1`, each interval containing
at most `W=binom(2m,m)` sets.  Then

\[
 q_{\rm block}(2m)\ge
 \left(\sqrt{\log2}+\int_{\sqrt{\log2}}^\infty e^{-x^2}\,dx-o(1)\right)
 \sqrt m.                                                \tag{3.1}
\]

On the other hand,

\[
 d=D+O(1)=\left(\int_0^\infty e^{-x^2}\,dx+o(1)\right)\sqrt m. \tag{3.2}
\]

Therefore

\[
 q_{\rm block}(2m)-d\ge
 \left(\sqrt{\log2}-
       \int_0^{\sqrt{\log2}}e^{-x^2}\,dx-o(1)\right)\sqrt m
 =\Theta(\sqrt k).                                      \tag{3.3}
\]

The coefficient in parentheses is positive.

#### Proof

Put

\[
 b_j={2m\choose m-j},\qquad j\ge1.
\]

Uniformly for bounded `j/sqrt(m)`, the central-binomial local limit gives

\[
                         {b_j\over W}=e^{-j^2/m+o(1)}.     \tag{3.4}
\]

Let `a=sqrt(log 2)`.  There are `(a+o(1))sqrt(m)` consecutive central
ranks with `b_j>W/2`.  No block of capacity `W` can contain two of them.
Moreover, because the blocks are rank-consecutive, only the block
containing the lowest such heavy rank can also contain any of the lower
tail; it absorbs less than one additional unit of `W`.

The remaining tail has total size

\[
 \sum_{j>(a+o(1))\sqrt m}b_j
 =\left(\int_a^\infty e^{-x^2}\,dx+o(1)\right)W\sqrt m. \tag{3.5}
\]

After losing at most `W` of it to the last heavy block, it needs the
corresponding number of further blocks.  This proves (3.1).

Summing (3.4) from `j=1` upward gives (3.2), also directly from
`d<=D<=d+1` and `D=ceil(Lambda/W)`.  Subtracting (3.2) from (3.1) gives
(3.3); positivity follows from `e^(-x^2)<1` for `x>0`.  \(\square\)

Thus complete-rank normalized matching is a valid integrality engine, but
not a zero-defect chronology.  A successful ladder must distribute
members of the same Boolean rank among different time slices.

## 4. A symmetric-chain decomposition cannot merely be cut

The second canonical attempt starts with a Greene--Kleitman or other
symmetric-chain decomposition and cuts every long lower segment into
pieces of length at most `D`.

### Theorem 4.1 (SCD fragmentation wall)

For even `k=2m`, take any symmetric-chain decomposition of `B_(2m)` and
restrict it to the nonempty ranks below `m`.  If every restricted chain is
cut into fragments of size at most `D` and fragments belonging to
different original chains are never spliced, then the number of nonempty
fragments is at least

\[
 \left(1+e^{-\pi/4}-o(1)\right)W.                       \tag{4.1}
\]

In particular it exceeds the `W` owner endpoints by

\[
                         (e^{-\pi/4}-o(1))W.             \tag{4.2}
\]

#### Proof

Every SCD has exactly

\[
 B_s={2m\choose s},\qquad c_s=B_s-B_{s-1}              \tag{4.3}
\]

chains beginning in rank `s`.  Hence exactly

\[
                         B_{m-1}={2m\choose m-1}        \tag{4.4}
\]

chains have a nonempty lower segment.  A chain beginning below rank
`m-D` has more than `D` lower elements and therefore contributes at least
one extra fragment.  The number of such chains is

\[
                         B_{m-D-1}+O(1).                \tag{4.5}
\]

The harmless `O(1)` covers the unique chain containing the empty set and
integer endpoint conventions.  Therefore the fragment count is at least
`B_(m-1)+B_(m-D-1)-O(1)`.

Now

\[
 {B_{m-1}\over W}={m\over m+1}=1-o(1),
 \qquad {D\over\sqrt m}\longrightarrow{\sqrt\pi\over2}, \tag{4.6}
\]

and the local limit (3.4), now with central distance `D+1`, gives

\[
 {B_{m-D-1}\over W}\longrightarrow
       \exp\left(-{(D+1)^2\over m}\right)=e^{-\pi/4}.   \tag{4.7}
\]

This proves (4.1)--(4.2).  Chains of length above `2D`, `3D`, and so on
only increase the fragment count.  \(\square\)

The wall is independent of which SCD is chosen, because (4.3) fixes the
chain-length histogram.  It rules out only **cut and re-anchor**.  It does
not rule out a nonsymmetric chain factor obtained by cross-chain
exchanges.  Rather, it proves that a successful SCD-based proof must make
linearly many such splices.

## 5. What normalized matching proves unconditionally

Let

\[
 P_k=\{S\subseteq[k]:1\le |S|\le r\}.                    \tag{5.1}
\]

This is a monotone unimodal normalized-matching poset of width `W` and
size `Lambda+W`.  A theorem of Tomon for unimodal normalized-matching
posets gives a partition into `W` chains, each of size at most

\[
                         {2|P_k|\over W}+5.             \tag{5.2}
\]

Every one of those chains contains exactly one rank-`r` owner, because
that rank is an antichain of size `W`.  Removing the owners therefore
gives an unconditional anchored lower chainization of depth

\[
                         2d+O(1).                       \tag{5.3}
\]

Reference: Istvan Tomon, *On a conjecture of Furedi*, European Journal of
Combinatorics 49 (2015), 1--12, DOI `10.1016/j.ejc.2015.02.026`.

The factor two is the strongest conclusion justified here from normalized
matching alone.  It must not be silently replaced by `d+O(1)`.

## 6. Relation to the uniform-chain conjecture

Appending the distinct owner to every lower chain identifies depth-`D`
chainization with a partition of `P_k` into exactly `W` chains, each of
size at most `D+1`.  For even `k`, complementation identifies this, up to
the empty/full endpoint, with the upper-half setting of Conjecture 4.2 in
Sudakov--Tomon--Wagner, *Uniform chain decompositions and applications*,
`arXiv:1911.09533`.

The upper-half uniform partition asserted by that conjecture would imply
the present maximum-depth statement.  The converse is not asserted: a
maximum bound permits much shorter chains and is weaker than prescribing
the balanced chain-size multiset.  Their proved theorem controls almost
all chains asymptotically; it leaves an exceptional family and does not
give an all-chain additive `O(1)` maximum.  Therefore neither their theorem
nor ordinary Boolean normalized matching closes the present gate.

## 7. Exact surviving target

The abstract integrality counterexamples in
`MATH_THEOREM_IDEAL_CHAINIZATION_BLOSSOM_OBSTRUCTION_AND_CHRONOLOGY_HALL_20260801.md`
show that no theorem can round ideal slots in arbitrary containment
instances.  The complete Boolean ideal may still have additional exchange
structure.

The weakest exact positive hypothesis now isolated is:

1. choose `D+O(1)` **rank-interleaved** slices of the complete lower ideal;
2. make their sizes nonincreasing away from the owner shore;
3. prove adjacent inclusion Hall, preferably by a protected normalized,
   laminar, or Ferrers reserve after all earlier choices; and
4. only then concatenate the ladder matchings.

Equivalently, start with an SCD and provide the `Theta(W)` cross-chain
splice system quantified by Theorem 4.1.  These are two descriptions of
the same missing chronology correlation.  Even after this static chain
factor is built, the sliding suffix-OR cocycle, upper language, residence,
and common-cap compiler remain separate physical gates.
