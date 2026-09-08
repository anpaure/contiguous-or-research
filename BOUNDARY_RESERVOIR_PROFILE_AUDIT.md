# Independent audit of `BOUNDARY_RESERVOIR_PROFILE.md`

## 1. Verdict

The boundary-reservoir argument is correct under the hypotheses it actually
states.  In particular, I could not construct a counterexample to

\[
 \mu_a\Longrightarrow2\delta_x,
 \qquad H_a(c)\longrightarrow0\text{ for every sufficiently small fixed }c>0,
 \qquad D=o(a^2)
 \quad\Longrightarrow\quad x=\frac32.
\]

The crucial point is that the limits are sequential.  For each fixed `c`,
weak convergence makes all but `o(a)` dangerous plateaux have length near
`xa`, and vanishing `H_a(c)` makes the total `2L`-clipped internal-gap mass
`o(a^2)`.  The complement therefore supplies a reservoir of density
`3-2x`; the subset run-spectrum inequality bounds that density by
`9c^2/4`.  Only after taking `a -> infinity` may one send `c -> 0`.

There are two minor presentation issues, neither affecting the theorem.

1. The exact identity for `B_a(h)` in (2.2) requires an integer cap
   `1 <= h <= a`; the source says only `h <= a`.  Every later use satisfies
   the missing conditions.
2. The sentence after (6.2) should say that every **valid** one-sided window
   at an index outside `R_c` contains a dangerous plateau.  Near a word
   boundary only one orientation may be valid, so “both relevant one-sided
   senses” is slightly too loose.

There are also two harmless typesetting defects: the qualifier “regular” in
line 258 contains a stray control character, and line 366 is missing the
TeX command before `qquad`.

## 2. Audit of the finite reservoir inequality

For a subset `J`, the audited run-spectrum inequality is

\[
 |S_h|\le
 \sum_{i\in J}\min\{\lambda_i,h\}+(M_a-|J|)h
 +(C_\alpha+C_\beta+h)D.
\]

This is the correct subset form: unassigned indices are equivalent, at the
chosen cap, to assigning the formal cost `h`.  A run in the forward window
`[i+1,i+L]` has audited one-sided span at most `L+1`, not `L`; the backward
case is symmetric.  With mixed orientations,

\[
 C_\alpha\le L+1,
 \qquad C_\beta\le L+1,
\]

so the source's error coefficient `2L+2+h` is exact and safe.  No endpoint
or congestion unit is missing.

On `R_c`, the dangerous-free-window lemma supplies an integer cost at most
`floor(ca)`.  Substitution with `K=|R_c|` gives

\[
 |S_h|\le K\lfloor ca\rfloor+(M_a-K)h+(2L+2+h)D,
\]

and hence, for `floor(ca)<h<=a`,

\[
 K(h-\lfloor ca\rfloor)
 \le B_a(h)+(2L+2+h)D.
\]

Thus Theorem 3.1 applies the inherited inequality with the correct sign,
cap, subset, span, and endpoint constants.

For integer `1<=h<=a`, the exact lower-layer deficit is

\[
 B_a(h)=\sum_{q=1}^h q^2
 =\frac{h(h+1)(2h+1)}6
 =\frac{h^3}{3}+O(h^2).
\]

At `h=floor(3ca/2)`, with fixed `0<c<2/3`,

\[
 \frac{h}{a}\to\frac{3c}{2},
 \qquad
 \frac{h-\lfloor ca\rfloor}{a}\to\frac c2,
 \qquad
 \frac{B_a(h)}{a^3}\to\frac13\left(\frac{3c}{2}\right)^3.
\]

Moreover `(2L+2+h)D=o(a^3)` because `L=4a+2` and `D=o(a^2)`.
Dividing the finite inequality by `a^3` therefore yields

\[
 \limsup_{a\to\infty}\frac K{a^2}\le\frac94c^2.
\]

For the small-cap range, writing `h=ya` gives

\[
 f_c(y)=\frac{y^3}{3(y-c)},
 \qquad
 f_c'(y)=\frac{y^2(2y-3c)}{3(y-c)^2}.
\]

The unique minimum on `c<y<=1` is `y=3c/2` when `c<2/3`, so the
constant `9/4` and its stated range are correct.

## 3. Weak convergence and plateau-union bookkeeping

All normalized directed plateau lengths lie in `[0,2]`.  Hence weak
convergence on this common compact support implies both total-mass and
first-moment convergence.  Fix `c<x` and choose `epsilon` with
`c<x-epsilon`.  Since the boundary of
`[x-epsilon,x+epsilon]` carries no mass under `2 delta_x`,

\[
 \#\{P:|\lambda(P)/a-x|\ge\epsilon\}=o(a).
\]

Every regular plateau is `c`-dangerous, while every dangerous plateau not
regular is among this `o(a)` exceptional family.  It follows that

\[
 m_c=(2+o(1))a,
 \qquad
 \sum_{P\ c\text{-dangerous}}\lambda(P)=(2x+o(1))a^2.
\]

The second statement may equivalently be obtained by integrating
`t 1_(c,2](t)`: its only discontinuity is at `c`, where the limit measure
has no atom.

Dangerous plateau edge sets are pairwise disjoint.  Consecutive plateau
vertex intervals may share one endpoint, but no ordering edge, and no three
nontrivial plateaux can meet at one position.  If `omega` counts shared
endpoints, then

\[
 0\le\omega\le m_c-1,
 \qquad
 \left|\bigcup_jP_j\right|
 =\sum_j(\lambda_j+1)-\omega
 =\sum_j\lambda_j+O(a).
\]

Thus the dangerous vertex union has size `(2x+o(1))a^2`, and its
complement has size `(3-2x+o(1))a^2`.  Keeping shared endpoints in the
plateau union, as the source does, is essential; no overlap has been
double-counted as a gap.

## 4. From seam mass to clipped-gap mass

For a regular dangerous successor `P_j`, put

\[
 \eta=x-\epsilon-c>0,
 \qquad
 \kappa=4-x-\epsilon>0.
\]

Then

\[
 \lambda_j-ca\ge\eta a,
 \qquad
 L-\lambda_j\ge\kappa a+O(1).
\]

Consequently `H_a(c)->0` gives the quantitative implication

\[
 \sum_{j\ge2,\,P_j\text{ regular}}
 \min\{g_{j-1},L-\lambda_j\}
 \le\frac{a^3H_a(c)}{\eta a}=o(a^2).
\]

Because `L-lambda_j` is bounded below by a positive multiple of `a` and
`2L=O(a)`, there is a constant depending only on fixed
`x,epsilon` such that

\[
 \min\{g_{j-1},2L\}
 \le C\min\{g_{j-1},L-\lambda_j\}.
\]

There are only `o(a)` exceptional successors, and each contributes at most
`2L=O(a)`.  Hence

\[
 \sum_{\text{internal gaps}}\min\{g_j,2L\}=o(a^2).
\]

This is exactly the number, up to endpoint conventions of at most a
constant per gap, removed by deleting the first and last `L` positions of
every internal gap.  The prefix and suffix gaps are absent from `H_a(c)`,
but the same clipping deletes at most `2L` positions from each, only
`O(a)` in total.  Every retained position has a valid adjacent forward or
backward length-`L` window wholly in its complement gap.  Therefore

\[
 |R_c|\ge(3-2x+o(1))a^2.
\]

The proof deliberately uses the loose `2L` clipping.  The exact number of
positions in a gap having neither a forward nor a backward window is at
most `L`, but that improvement is unnecessary.

## 5. Saturation and limit order

For each fixed sufficiently small `c<min{x,2/3}`, Sections 2 and 4 give

\[
 3-2x\le\frac94c^2.
\]

No uniform estimate as `c->0` is used or available: all weak-convergence
and exceptional-count estimates may depend on the fixed `c`.  The
hypothesis supplies the displayed inequality separately for every fixed
small `c` along the same `a`-subsequence.  Taking `a->infinity` first and
then choosing a numerical sequence `c downarrow 0` gives `x>=3/2`.

Conversely, directed plateau edges are disjoint, so

\[
 \frac1{a^2}\sum_P\lambda(P)
 \le\frac{M_a-1}{a^2}=3+O(a^{-1}).
\]

First-moment convergence gives `2x<=3`, hence `x<=3/2`.  This verifies the
endpoint step and proves `x=3/2`.

## 6. Counterexample attempts

Three natural attempts fail for exactly the reasons claimed in the source.

* Put a macroscopic complement gap at a word boundary.  It contributes
  nothing to `H_a(c)`, but clipping loses only `O(a)` positions, so almost
  the whole gap lies in `R_c` and violates the quadratic run-spectrum bound
  when `x<3/2`.
* Put one or finitely many macroscopic gaps in the interior.  The seam
  functional may still vanish because its gap factor is clipped at
  `Theta(a)`, but those gaps again lose only `O(a)` boundary positions and
  create a macroscopic `R_c`.
* Split macroscopic complement mass among `Theta(a)` gaps.  For regular
  successors, their total `Theta(a^2)` clipped mass incurs weight
  `Theta(a)` in `H_a(c)`, producing nonvanishing normalized seam mass unless
  all but `o(a^2)` of that clipped mass disappears.

Thus neither boundary concentration, a bounded number of huge internal
gaps, nor extensive fragmentation evades the combined hypotheses.  The
saturated profile `2 delta_(3/2)` does evade the argument because its
complement is only `o(a^2)`; the source correctly leaves that endpoint
open.

## 7. Ledger

Proved under the stated inherited framework:

* the finite subset inequality (3.2), including its endpoint constants;
* the small-cap asymptotic and the optimized coefficient `9/4`;
* the `o(a^2)` clipped-gap conclusion from fixed-`c` seam convergence;
* the complement density `(3-2x)a^2+o(a^2)`; and
* the sequential-limit conclusion `x=3/2`.

Not proved, and not needed here:

* exclusion of `2 delta_(3/2)`;
* a conclusion from `H_a(c)->0` at only one threshold bounded away from
  zero; or
* any version with `c=c(a)->0` without new uniform estimates.
