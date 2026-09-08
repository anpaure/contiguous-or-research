# Exact diagonal-cut ledger for partial relabeling near-trades

Date: 2026-07-25

Method: pure mathematics only.

## 0. Setup and outcome

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad B={W\over n}.
\]

Let `F` be an exact middle wreath factor, let `sigma in S_n`, and let
`A subseteq F`.  We form the row **multiset**

\[
             P=P(F,A,\sigma):=(F\setminus A)\sqcup\sigma A.
\tag{0.1}
\]

It still has exactly `B` wreath rows, but it need not own every middle set
exactly once.  Let

\[
 U(A)=\bigsqcup_{C\in A}{\cal W}_m(C)
 \subseteq\binom{[n]}m.
\tag{0.2}
\]

Because `F` is exact, the union in (0.2) is disjoint and
`|U(A)|=n|A|`.

The exact conclusions are:

1. the middle holes and middle duplicate excess of `P` are equal, and each
   is
   \[
       {1\over2}|U(A)\mathbin\triangle\sigma U(A)|;
   \]
2. the symmetric difference is exactly the diagonal cut boundary in the
   `F`--`sigma F` owner overlay;
3. the depth-one hole change is an exact repair-minus-damage formula;
4. in the literal cyclic-band compiler, the designated length change is
   \[
      |U(A)\triangle\sigma U(A)|+2(D_1-R_1)
   \]
   for the first band, and the analogous sum over all controlled depths;
5. for a positive-density partial replacement, conductance `o(1)` is
   exactly the middle-layer condition needed by a coefficient-one
   near-factor route.  It is not sufficient for the shadow layers by
   itself.

## 1. Exact middle holes and duplicates

For a middle set `X`, the multiplicity in `P` is

\[
 \mu_{P,0}(X)
 =\mathbf1_{X\notin U(A)}+\mathbf1_{X\in\sigma U(A)}.
\tag{1.1}
\]

Consequently

\[
 \mathcal H_0(P)=U(A)\setminus\sigma U(A),
\tag{1.2}
\]

while the multiplicity-two middle sets are

\[
 \mathcal D_0(P)=\sigma U(A)\setminus U(A).
\tag{1.3}
\]

The two sets have the same cardinality because
`|U(A)|=|sigma U(A)|`.  Hence

\[
 \boxed{
 M_0(P)=|\mathcal H_0(P)|=|\mathcal D_0(P)|
 ={1\over2}|U(A)\triangle\sigma U(A)|.}
\tag{1.4}
\]

There are no higher middle multiplicities in one partial replacement: the
two indicators in (1.1) are binary.

## 2. The owner-overlay diagonal cut

Form the bipartite owner overlay between `F` and `sigma F`.  Its left
vertices are the rows of `F`, its right vertices are the rows of `sigma F`,
and each middle set `X` is one edge joining its unique owners on the two
sides.

Identify a right row `sigma C` with `C in F`.  The result is a directed
`n`-in, `n`-out multigraph `D_sigma(F)` on vertex set `F`: the edge indexed
by `X` is

\[
 \operatorname{owner}_F(X)
 \longrightarrow
 \operatorname{owner}_F(\sigma^{-1}X).
\tag{2.1}
\]

Write `partial_sigma(A)` for the number of directed edges whose endpoints
lie on opposite sides of `A`.  Then

\[
 \begin{aligned}
 e(A,F\setminus A)
 &=|U(A)\setminus\sigma U(A)|,\\
 e(F\setminus A,A)
 &=|\sigma U(A)\setminus U(A)|.
 \end{aligned}
\tag{2.2}
\]

Since the directed graph is balanced, the two directional cut sizes are
equal.  Combining (1.4)--(2.2) gives

\[
 \boxed{
 \partial_\sigma(A)
 =|U(A)\triangle\sigma U(A)|
 =2M_0(P).}
\tag{2.3}
\]

Equivalently, in the original bipartite overlay select the left vertices
`F\A` and the right vertices `sigma A`.  An overlay edge has zero selected
endpoints exactly at a middle hole, two selected endpoints exactly at a
middle duplicate, and one selected endpoint otherwise.  This is the
literal diagonal-cut interpretation.

In particular,

\[
 \partial_\sigma(A)=0
 \quad\Longleftrightarrow\quad
 A\text{ is a union of weak components of }D_\sigma(F).
\tag{2.4}
\]

These are exactly the ordinary component switches, for which `P` is again
an exact factor.  The near-trade relaxation is therefore literally the
passage from zero-boundary component unions to cuts of small nonzero
boundary.

## 3. Exact depth-one hole drift

For a rank-`(m-1)` target `S`, put

\[
 \mu(S)=\mu_{F,1}(S),
 \qquad
 a(S)=\#\{C\in A:S\text{ is an }(m-1)\text{-interval of }C\}.
\tag{3.1}
\]

The new load is

\[
 \boxed{
 \mu'(S)=\mu(S)-a(S)+a(\sigma^{-1}S).}
\tag{3.2}
\]

Define the repaired and damaged target families

\[
 \mathcal R_1
 =\{S:\mu(S)=0,\ a(\sigma^{-1}S)>0\},
\tag{3.3}
\]

\[
 \mathcal D_1
 =\{S:\mu(S)=a(S)>0,\ a(\sigma^{-1}S)=0\}.
\tag{3.4}
\]

Let `R_1=|R_1|` and `D_1=|D_1|`.  Then

\[
 \boxed{
 H_1(P)-H_1(F)=D_1-R_1.}
\tag{3.5}
\]

### Proof

If `mu(S)=0`, then `a(S)=0` because `A subseteq F`.  Equation (3.2)
repairs the hole exactly in (3.3).

If `mu(S)>0`, all three terms in (3.2) are nonnegative except the displayed
subtraction, and `a(S)<=mu(S)`.  The new load is zero exactly when all old
occurrences lie in `A` and no new occurrence is supplied, which is (3.4).
No other target changes hole status. \(\square\)

The same statement holds at every depth `q` after replacing `mu,a` by the
rank-`(m-q)` load vectors `mu_q,a_q`:

\[
 H_q(P)-H_q(F)=D_q-R_q.
\tag{3.6}
\]

## 4. Exact literal OR ledger

Fix a controlled depth `H<m`.  Linearize every row of `P` by the usual
cyclic erosion block of length `n+2H+1`.  Since `P` has exactly `B` rows,
the block cost is still

\[
 B(n+2H+1)=W+(2H+1)B.
\tag{4.1}
\]

Let `M_q(P)` be the number of missing lower rank-`(m-q)` targets.  Rowwise
complementation gives the same number of missing upper
rank-`(m+q+1)` targets.  Appending all designated holes literally and then
the ordinary literal tails gives

\[
\boxed{
\begin{aligned}
 \nu(2m+1)\le{}&W+(2H+1)B
 +\partial_\sigma(A)\\
 &+2\sum_{q=1}^{H}M_q(P)
 +2\sum_{r=0}^{m-H-1}\binom nr-1.
\end{aligned}}
\tag{4.2}
\]

Here the middle repair term is exactly

\[
 2M_0(P)=\partial_\sigma(A),
\]

covering the missing rank-`m` sets and their complementary missing
rank-`(m+1)` sets.  Formula (4.2) is the exact **designated** construction
ledger; incidental seam intervals can only shorten the actual word.

Compared with the same designated compiler applied to the exact factor
`F`, the controlled-band repair change is

\[
 \boxed{
 \Delta L_H
 =\partial_\sigma(A)
  +2\sum_{q=1}^{H}(D_q-R_q).}
\tag{4.3}
\]

In particular, for the first band alone,

\[
 \boxed{
 \Delta L_1=\partial_\sigma(A)+2(D_1-R_1).}
\tag{4.4}
\]

Thus a near-trade strictly improves the designated first-band word exactly
when

\[
 \boxed{R_1-D_1>{1\over2}\partial_\sigma(A).}
\tag{4.5}
\]

Repairing holes is not enough: useful first-shadow gain must exceed the
middle diagonal-cut bill.

The established product-SCD tail can replace the final literal-tail term
in (4.2), without changing any near-trade term.

## 5. Conductance: the exact middle criterion

Define the normalized diagonal conductance

\[
 \Phi_\sigma(A)
 ={\partial_\sigma(A)\over
   n\min\{|A|,B-|A|\}}
\tag{5.1}
\]

for a nontrivial cut.

Suppose

\[
 |A|=\Theta(B),\qquad B-|A|=\Theta(B).
\tag{5.2}
\]

Since `nB=W`, equations (2.3) and (5.1) give the exact equivalence

\[
 \boxed{
 M_0(P)=o(W)
 \quad\Longleftrightarrow\quad
 \partial_\sigma(A)=o(W)
 \quad\Longleftrightarrow\quad
 \Phi_\sigma(A)=o(1).}
\tag{5.3}
\]

Thus vanishing conductance is necessary and sufficient for the **middle
ownership part** of a positive-density near-factor route.

The balance hypothesis (5.2) is forced when one starts and ends with very
different first-shadow behavior.  Indeed each changed row contains only
`n` depth-one intervals, so

\[
 |H_1(P)-H_1(F)|\le n|A|.
\tag{5.4}
\]

Also `P` differs from the relabeled exact factor `sigma F` in only
`B-|A|` rows, giving

\[
 |H_1(P)-H_1(\sigma F)|\le n(B-|A|).
\tag{5.5}
\]

Since `H_1(sigma F)=H_1(F)`, if the starting factor has
`H_1(F)>=delta W` and the near-factor has `H_1(P)=o(W)`, then

\[
 |A|,\ B-|A|\ge(\delta-o(1))B.
\tag{5.6}
\]

Consequently conductance `o(1)` is genuinely necessary for a one-shot
partial replacement which repairs a linear first-shadow defect at
coefficient-one middle cost.

### What conductance does not prove

Conductance alone is not sufficient for coefficient one.  It says nothing
about `M_q(P)` for `q>=1`.  A zero-boundary cut may merely exchange whole
owner components while leaving the same shadow defect.  The exact
coefficient-one criterion for this literal near-factor architecture is,
under the usual `H=o(m)` seam and `o(W)` tail hypotheses,

\[
 \boxed{
 \partial_\sigma(A)
 +2\sum_{q=1}^{H}M_q(P)=o(W).}
\tag{5.7}
\]

For balanced positive-density cuts, (5.7) is equivalent to conductance
`o(1)` **together with** aggregate shallow-shadow defect `o(W)`.

## 6. Multiple rounds and accumulation

The one-shot theorem cannot be iterated naively.

### 6.1 Loss of the exact owner overlay

After a genuine near-trade, `P` has middle holes and duplicates.  Middle
sets no longer have unique owners, so the next `P`--`sigma P` owner overlay
is not the regular exact-factor overlay used in Section 2.  A second-round
conductance claim therefore needs either re-exactification or a new
multi-owner definition and proof.

### 6.2 Common-baseline simultaneous replacements

There is one clean multiround model.  Take pairwise disjoint row families
`A_t subseteq F` in one exact baseline and replace each by `sigma_t A_t`.
Let

\[
 d_t=mathbf1_{\sigma_tU(A_t)}-mathbf1_{U(A_t)}
\tag{6.1}
\]

be its signed middle-incidence update.  The final middle load is

\[
                         \lambda=\mathbf1+\sum_td_t.
\tag{6.2}
\]

Because the final row count is still `B`, `sum_X(lambda(X)-1)=0`; because
`lambda` is a nonnegative integral load vector,

\[
 \boxed{
 M_0^{\rm final}
 ={1\over2}\left\|\sum_td_t\right\|_1
 \le {1\over2}\sum_t
 |U(A_t)\triangle\sigma_tU(A_t)|.}
\tag{6.3}
\]

Thus the **final signed boundary**, not the worst individual conductance,
is the exact quantity.  The summable condition

\[
 \sum_t\partial_{\sigma_t}(A_t)=o(W)
\tag{6.4}
\]

is sufficient but may be stronger than necessary because signed updates can
cancel.  Merely having `Phi_t=o(1)` in every one of a growing number of
rounds is not sufficient unless the weighted sum

\[
 \sum_t n\min\{|A_t|,B-|A_t|\}\Phi_t=o(W)
\tag{6.5}
\]

or a direct cancellation theorem is proved.

### 6.3 Flag defects also telescope non-monotonically

At depth `q`, a sequential legal row replacement has the exact one-step
change `D_(q,t)-R_(q,t)`.  Hence final hole counts telescope, but a target
repaired in one round may be damaged later.  Conductance controls none of
these signs.  A multiround theorem must control the **final common flag
histograms**, not sum nominal repair counts from separate rounds.

Finally, the rounds are an off-line mathematical search for one final row
family.  Emitting the cyclic word of every intermediate family would cost
one additional `W`-scale block per round and is incompatible with leading
constant one.

## 7. Exact remaining near-trade gate

A one-shot near-factor route to coefficient one is reduced exactly to:

1. find a balanced positive-density owner cut with
   `Phi_sigma(A)=o(1)`;
2. make its final cyclic shadow family satisfy
   \[
   \sum_{q<=H}M_q(P)=o(W)
   \]
   (or replace this literal sum by a separately proved cross-rank repair
   functional of cost `o(W)`);
3. retain the established `o(W)` seam and outer-tail ledgers.

For depth one, the sharp profit test is (4.5).  For multiple rounds, one
must additionally prove either summable cut boundary or cancellation of the
final signed middle-incidence updates, and one must rebuild legality after
the first nonexact step.
