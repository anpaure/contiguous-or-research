# A rank-separation deadline theorem and the literal-facet barrier

Date: 2026-07-30  
Lane: R, pure-mathematics all-`k` upper-bound lane  
Status: unconditional lower-structure theorem.  It rules out a broad
literal PBBS/Pascal recursion near the deadline, but not derivative-level
PBBS compilation.

## 0. Main conclusions

For `1<=s<=k`, let `mu(k,s)` be the minimum length of a nonzero set-word
whose interval unions contain every nonempty subset of `[k]` of rank at
most `s`; set `mu(k,0)=0` only as a recursion base.  Put

\[
 M_s={k\choose s},\qquad
 \Lambda_s=\sum_{j=1}^{s-1}{k\choose j},             \tag{0.1}
\]

and

\[
 d_s=\min\left\{t\ge0:
       tM_s+{t+1\choose2}\ge\Lambda_s\right\}.       \tag{0.2}
\]

If a universal word `A` has `H_(>s)` cells of rank greater than `s`, then

\[
 \boxed{|A|\ge H_{>s}+M_s+d_s.}                     \tag{0.3}
\]

This is a deletion theorem: a target of rank at most `s` cannot use a cell
of rank greater than `s`, so removing all high cells leaves a word for the
complete lower ideal.  The established monotone-deadline theorem applies
to that retained word.

For odd `k=2m+1>=5`, set

\[
 W={k\choose m},\qquad M={k\choose m-1},
 \qquad \Lambda=\sum_{j=1}^{m}{k\choose j}=2^{k-1}-1,\tag{0.4}
\]

\[
 d=\min\left\{t:tW+{t+1\choose2}\ge\Lambda\right\},
 \qquad B(k)=W+d,                                    \tag{0.5}
\]

and

\[
 \delta=\min\left\{t:tM+{t+1\choose2}
                  \ge\Lambda-W-M\right\}.           \tag{0.6}
\]

Then every universal word with `H` cells of rank at least `m` obeys

\[
 \boxed{|A|\ge H+M+\delta.}                         \tag{0.7}
\]

Consequently a construction which retains all `W` PBBS rank-`m` facets as
literal physical cells has

\[
 \boxed{|A|\ge W+M+\delta
       =B(k)+(M+\delta-d).}                          \tag{0.8}
\]

For all sufficiently large odd `k`, `delta` is either `d-2` or `d-1`.
Thus the excess in (0.8) is an entire adjacent middle layer, namely `M-2`
or `M-1`.  Recursive decoration, optimal seam collars, and arbitrary
interleaving do not remove this cost.  A deadline-scale construction must
realize almost all PBBS facets as overlapping derivative windows rather
than as literal cells.

## 1. The truncated monotone deadline

The monotone-deadline proof does not require targets above its chosen top
rank.  Applied to the initial Boolean ideal it gives the following form.

### Lemma 1.1 (initial-ideal deadline)

For every `1<=s<=k`,

\[
                         \mu(k,s)\ge M_s+d_s.         \tag{1.1}
\]

#### Proof

The rank-`s` targets form an antichain of size `M_s`.  The usual monotone
deadline argument therefore first gives `n>=M_s`.  Write `n=M_s+t`.
Every selected witness below rank `s` has length at most `t`; assigning it
to its right endpoint, the number of available intervals of lengths at
most `t` is

\[
 \sum_{e=1}^{n}\min(t,e)
   =tn-{t\choose2}
   =tM_s+{t+1\choose2}.                              \tag{1.2}
\]

There are `Lambda_s` distinct lower targets, so (1.2) is at least
`Lambda_s`.  Minimality in (0.2) gives `t>=d_s`, proving (1.1).  This is
exactly the proved monotone-deadline argument, restricted to an initial
Boolean ideal; no upper target is used.  QED.

## 2. Rank separation

### Theorem 2.1 (high-cell deletion)

Let `A=(A_1,...,A_n)` cover every nonempty target of rank at most `s`, and
let

\[
                         H_{>s}=|\{i:|A_i|>s\}|.      \tag{2.1}
\]

Then (0.3) holds.

#### Proof

If an interval has union `S`, every letter in that interval is a subset of
`S`.  Hence a witness for `|S|<=s` contains no cell of rank greater than
`s`.

Delete all such high cells and concatenate the remaining low-cell
components in their original order.  Every old lower-ideal witness lay
wholly in one retained component, so it remains a contiguous interval
after deletion.  The resulting word has length `n-H_(>s)` and covers the
complete nonempty ideal through rank `s`.  Lemma 1.1 gives

\[
                         n-H_{>s}\ge M_s+d_s,
\]

which is (0.3).  QED.

Concatenation may create additional interval labels, but this can only
help.  The proof does not assume that high cells form one block or that
the retained low pieces have compatible boundary states.

Taking `s=m-1` in odd dimension gives (0.7), because cells of rank greater
than `m-1` are exactly the cells of rank at least `m`, while the strict
lower-target count below rank `m-1` is

\[
 \Lambda_{m-1}
 =\sum_{j=1}^{m-2}{k\choose j}
 =\Lambda-W-M.                                       \tag{2.2}
\]

### Corollary 2.2 (near-deadline high-cell capacity)

If an odd-dimensional universal word has length at most `B(k)+C`, then

\[
 \boxed{H\le W-M+d-\delta+C.}                       \tag{2.3}
\]

If a PBBS-based construction begins with `W` designated literal facets
and replaces or compiles `q` of them into lower-rank physical structure,
then

\[
 \boxed{q\ge M+\delta-d-C.}                         \tag{2.4}
\]

#### Proof

Combine (0.7) with `|A|<=W+d+C` to obtain (2.3).  If `W-q` literal
rank-`m` facets remain, then `H>=W-q`; substitution into (2.3) gives
(2.4).  QED.

This is the exact minimal countercondition for the literal-facet
architecture.  It does not say that a derivative chronology loses its
facets: one lower-rank cell may participate in several overlapping
rank-`m` windows, which is precisely the compiler mechanism left open.

## 3. Exact comparison of the adjacent deadlines

Define the central deadline slack

\[
 \sigma=dW+{d+1\choose2}-\Lambda.                   \tag{3.1}
\]

### Theorem 3.1 (two-value adjacent deadline)

Always `delta>=d-2`.  If

\[
                         W\ge d(W-M)+d,              \tag{3.2}
\]

then

\[
                         \delta\in\{d-2,d-1\}.      \tag{3.3}
\]

Under (3.2), the exact alternative is

\[
 \boxed{
 \delta=d-2
 \iff
 \sigma\ge(d-1)(W-M)+2d-1;}                        \tag{3.4}
\]

otherwise `delta=d-1`.

#### Proof

For `d<=2`, the lower assertion `delta>=d-2` is immediate.  Suppose
`d>=3`.  Minimality of `d` gives

\[
 \sigma<W+d.                                        \tag{3.5}
\]

Evaluating the left side of (0.6) at `t=d-3` and subtracting its target
gives

\[
 \begin{aligned}
 &(d-3)M+{d-2\choose2}-(\Lambda-W-M)\\
 &\qquad=
 \sigma-(d-2)(W-M)-W-3d+3<0,                       \tag{3.6}
 \end{aligned}
\]

where the last inequality uses (3.5).  Hence `delta>=d-2`.

At `t=d-1`, the analogous difference is

\[
 (d-1)M+{d\choose2}-(\Lambda-W-M)
   =\sigma+W-d(W-M)-d.                              \tag{3.7}
\]

Condition (3.2) makes this nonnegative, so `delta<=d-1` and (3.3)
follows.  Finally, at `t=d-2` the difference is exactly

\[
 \sigma-(d-1)(W-M)-2d+1.                            \tag{3.8}
\]

It is nonnegative exactly under (3.4).  Together with (3.3), this proves
the alternative.  QED.

For `k=2m+1`,

\[
 {M\over W}={m\over m+2},
 \qquad W-M={2W\over m+2}={4W\over k+3}.            \tag{3.9}
\]

The standard central-binomial estimate gives `d=O(sqrt(k))`.  Therefore
(3.2) holds for all sufficiently large odd `k`.  Equations (0.8) and
(3.3) then give the exact eventual literal-facet excess `M-2` or `M-1`.
Likewise, for `C=O(k)`, (2.4) becomes

\[
 q\ge W-{4W\over k+3}-O(k).                         \tag{3.10}
\]

Thus a `B(k)+O(k)` construction must compile a `1-O(1/k)` fraction of the
facet deck.

## 4. Pascal recursion does not evade the barrier

For `1<=s<=k-1`, there is a legal literal recursion for the truncated
ideals:

\[
 \boxed{\mu(k,s)\le\mu(k-1,s)+1+\mu(k-1,s-1).}     \tag{4.1}
\]

Indeed, take an optimal old-coordinate word `A` through rank `s`, a word
`C` through rank `s-1`, and a new coordinate `z`.  Then

\[
                         A,\ \{z\},\ z+C             \tag{4.2}
\]

covers every old target through rank `s`, the singleton `{z}`, and every
marked target `{z} union S` with `1<=|S|<=s-1`.  Iterating the coarser
bound `mu(k-1,s)<=nu(k-1)`, with the harmless convention
`mu(a,0)=0`, yields

\[
                         \mu(k,s)
 \le s+\sum_{j=1}^{s}\nu(k-j).                       \tag{4.3}
\]

Thus replacing the literal lower ideal in the PBBS half-cube theorem by a
recursive Pascal word is a valid constructional idea.  Theorem 2.1 shows
why it cannot reach the deadline while the PBBS facets remain literal:
even an optimal lower-ideal word has at least `M+delta` cells, independently
of its recursion, seams, or interleaving.

## 5. Finite-certificate scope

For the retained exact odd cases,

\[
\begin{array}{c|c|c|c|c}
k&B(k)&M&\delta&W+M+\delta\\ \hline
11&465&330&1&793\\
13&1719&1287&1&3004\\
15&6438&5005&1&11441
\end{array}                                          \tag{5.1}
\]

The authenticated `k=11,13,15` optimal words therefore cannot retain the
complete rank-`m` facet layer as literal cells.  This is consistent with
the derivative-level ownership separately established in their
carrier/compiler audits, but that normal form is not inferred from length
alone.  Direct doubling of a literal-facet `k=15` word would already cost at
least

\[
                         2(11441)+1=22883,            \tag{5.2}
\]

far above the authenticated `k=16` length `12874` word.

These comparisons do not infer a flat chronology from the finite words.
They use only their verified lengths and the unconditional deletion bound.

## 6. Proved boundary

Proved:

1. the general rank-separation bound (0.3);
2. the exact literal PBBS facet barrier (0.8);
3. the two-value deadline relation (3.3)--(3.4) under the explicit
   hypothesis (3.2), which holds for all sufficiently large odd `k`; and
4. the quantitative conclusion that sparse literal-facet replacement
   cannot give `B(k)+O(k)`.

Not proved or claimed:

1. a lower bound stronger than `B(k)` for unrestricted universal words;
2. an obstruction to representing PBBS facets as overlapping derivative
   windows of one lower-rank word;
3. a failure of the run-boundary conflict-profile criterion; or
4. `nu(k)<=B(k)+O(1)`.

The surviving coefficient-one route is therefore sharply identified:
retain the PBBS/Pascal facet **order** as a derivative chronology, but
compile almost all facets through one common physical source.  This is
exactly the pair-and-higher conflict expansion problem isolated in
`MATH_THEOREM_R_ALLK_RUN_BOUNDARY_CONFLICT_GIRTH_TWO_20260730.md`.
