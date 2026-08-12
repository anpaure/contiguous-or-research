# Intact central diagonals force cubic core-factor slack

## 1. Scope and conclusion

Let

\[
 P_m=[0,m]^4,
 \qquad
 M_m=[z^{2m}](1+z+\cdots+z^m)^4.
\]

This note rules out one specific version of the proposed four-box bridge.
Suppose a near-once middle row keeps every natural central diagonal as an
intact contiguous block and translates almost all of the natural lower
prefix/suffix meets by the corresponding variable-band core.  Then the
monotone factor-band slack is cubic.

More precisely, let the row have length

\[
                         L=M_m+E
\]

and contain every middle point.  Let its central witness intervals be

\[
 I_i=[i+\alpha_i,i+\beta_i],
 \qquad
 0\le \alpha_1\le\cdots\le\alpha_L\le d,
 \quad
 0\le \beta_1\le\cdots\le\beta_L\le d,
 \quad
 \alpha_i\le\beta_i.                                  \tag{1.1}
\]

Assume these intervals factor the middle row.  For each natural diagonal
block of radius `r`, there are `2r` nontrivial natural lower intervals
meeting one distinguished endpoint.  Let `t_B` be the number of these
targets which are **not** translated by their natural cores, and put

\[
                         T=\sum_B t_B.                  \tag{1.2}
\]

Then

\[
\boxed{
 2d\ \ge\
 {m(m+1)(2m+7)\over6}
 -T-(m+1)(m+2)-2E-O(m).
}                                                       \tag{1.3}
\]

An explicit safe boundary term in place of `O(m)` is `10m+5`.
Consequently, if `E=O(m^2)` and `d=O(m^2)`, then

\[
                         T=\Omega(m^3).                \tag{1.4}
\]

Thus `O(m^2)` literal central-square repairs cannot rescue the architecture.
A surface-error construction must replace a cubic family of the natural
lower witnesses globally, use non-core lower windows, or split/interleave
the central blocks.  The theorem does **not** obstruct any of those escape
routes.

## 2. Natural blocks and their rare endpoint atom

Use the hook coordinates

\[
 \gamma_H(p)=(H+\min(p,0),m-H+\max(p,0))
\]

and, for `H>=K`, the natural middle diagonal

\[
 D_{H,K}=\bigl(T_{H,K}(-K),T_{H,K}(-K+1),\ldots,
                    T_{H,K}(K)\bigr),
 \qquad
 T_{H,K}(s)=(\gamma_H(s),\gamma_K(-s)).               \tag{2.1}
\]

Its radius is `r=K` and its length is `2r+1`.  We use the family

\[
 \mathcal B={D_{H,r}:1\le r\le H\le m}
                \setminus\{D_{m,m}\}.                 \tag{2.2}
\]

The last block is omitted only because its full meet is the zero point; its
removal changes all estimates by `O(m)`.

Assume that the chosen occurrence of every block in `mathcal B` is a
contiguous, insertion-free copy of (2.1), in either orientation.  The hook
rectangles partition the middle layer, so these selected block occurrences
are position-disjoint.

Fix the atom

\[
                              b=(4,m).                  \tag{2.3}
\]

At the negative endpoint,

\[
 T_{H,r}(-r)=(H-r,m-H,r,m),                            \tag{2.4}
\]

so `b` is present.  At every other point of the same nondegenerate block,
the fourth coordinate is at most `m-1`.  Hence `b` occurs exactly once in
each selected block, at the endpoint (2.4).  Call it the **rare endpoint**.

Starting at the rare endpoint and moving through the natural diagonal, the
meets of the successive prefixes have spans

\[
                              1,2,\ldots,2r.           \tag{2.5}
\]

They are distinct: each extension lowers the meet rank by exactly one.  If
the block is reversed, use the corresponding suffixes ending at the rare
endpoint.  All of these targets are nonzero for the family (2.2).
Targets coming from different blocks are distinct as well, because the
product hook rectangles partition the entire four-box, not only its middle
layer.  Thus `T` really counts distinct lower targets which need alternate
witnesses or repairs.

## 3. The local run--core charge

For one selected block `B`, let `q_B` be the length of the maximal `b`-run
containing its rare endpoint.  Since the next position inside the block is
`b`-negative, this run extends only outwards from the block.

Among the `2r` intervals in (2.5), suppose `t_B` are not translated by their
natural cores.  If `h_B` is the largest span which is still core-translated
(put `h_B=0` if none remains), then

\[
                              h_B\ge 2r-t_B.           \tag{3.1}
\]

Indeed, making the maximum retained span at most `h` requires deleting all
`2r-h` spans above `h`.

We now use only two inherited exact facts about a monotone interval band.

1. If `[u,v]` is an internal positive run of one atom, factorability is
   equivalent to
   \[
                  \beta_{u-1}-\alpha_{v+1}\le v-u.    \tag{3.2}
   \]
2. The natural core for a row interval `[i,j]` is nonempty only if
   \[
                  \beta_i-\alpha_j\ge j-i.            \tag{3.3}
   \]

### Lemma 1 (one-block charge)

If the maximal `b`-run at the rare endpoint is internal, the block forces an
offset increase of at least

\[
                              h_B-q_B+1.               \tag{3.4}
\]

It is an increase of `beta` when the rare endpoint starts the block and an
increase of `alpha` when it ends the block.

### Proof

If `h_B=0`, then `h_B-q_B+1<=0` and the claim follows from
nonnegativity of every offset increase.  Assume below that `h_B>=1`.

First suppose the rare endpoint is the block's first index `s`.  Its maximal
run is `[u,s]`, where `q_B=s-u+1`, because position `s+1` is negative.  The
retained natural prefix of span `h_B` has core condition

\[
                       \beta_s-\alpha_{s+h_B}\ge h_B.
\]

Monotonicity gives `alpha_(s+h_B)>=alpha_(s+1)`.  Combining this with
(3.2),

\[
\begin{aligned}
 \beta_s-\beta_{u-1}
 &\ge h_B+\alpha_{s+1}-\beta_{u-1}\\
 &\ge h_B-(q_B-1)
  =h_B-q_B+1.                                         \tag{3.5}
\end{aligned}
\]

Now suppose the rare endpoint is the final index `e`.  Its maximal run is
`[e,v]`, of length `q_B=v-e+1`.  A retained natural suffix of span `h_B`
has

\[
                         \beta_{e-h_B}-\alpha_e\ge h_B.
\]

Since `beta_(e-1)>=beta_(e-h_B)`, (3.2) gives

\[
\begin{aligned}
 \alpha_{v+1}-\alpha_e
 &\ge \beta_{e-1}-(q_B-1)-\alpha_e\\
 &\ge h_B-q_B+1.                                     \tag{3.6}
\end{aligned}
\]

This proves the lemma.  Negative right sides are harmless.  `square`

## 4. Disjoint charging and run multiplicity

For a start-oriented rare endpoint, charge (3.5) to the `beta`-index
interval `[u-1,s]`.  Distinct such blocks use distinct maximal `b`-runs, and
their charge intervals are disjoint.  Therefore all start charges sum to at
most

\[
                         \beta_L-\beta_1\le d.         \tag{4.1}
\]

For an end-oriented rare endpoint, charge (3.6) to the `alpha`-index
interval `[e,v+1]`.  These intervals are likewise pairwise disjoint, so all
end charges sum to at most

\[
                         \alpha_L-\alpha_1\le d.       \tag{4.2}
\]

A maximal `b`-run contains rare endpoints of at most two selected
nondegenerate blocks: at most one block can end at that run and at most one
can start there.  Once a start-oriented block is entered, its second point
is `b`-negative; before an end-oriented endpoint, its penultimate point is
`b`-negative.  Consequently

\[
                         \sum_Bq_B\le2P_b,             \tag{4.3}
\]

where `P_b` is the total number of row positions containing `b`.

Only the maximal `b`-runs touching the two global row boundaries escape
(3.2).  Each contains rare endpoints of at most two selected blocks, so at
most four blocks are exceptional.  Deleting their possible contribution
costs at most

\[
                              4(2m+1)=8m+4.            \tag{4.4}
\]

Combining (3.4)--(4.4) gives

\[
\begin{aligned}
 2d
 &\ge \sum_B(h_B-q_B+1)-(8m+4)\\
 &\ge 2\sum_Br-T+|\mathcal B|-2P_b-(8m+4).            \tag{4.5}
\end{aligned}
\]

## 5. Global count

Among all middle points, those containing `b=(4,m)` are exactly

\[
             (x_1,x_2,x_3,m),\qquad x_1+x_2+x_3=m.
\]

There are

\[
                         {m+2\choose2}                 \tag{5.1}
\]

such points.  Since the row contains every middle point and has only `E`
occurrences beyond `M_m`,

\[
                         P_b\le {m+2\choose2}+E.       \tag{5.2}
\]

Before removing `D_(m,m)`, the exact weighted block count is

\[
\begin{aligned}
 2\sum_{H=1}^{m}\sum_{r=1}^{H}r
 +\sum_{H=1}^{m}\sum_{r=1}^{H}1
 &= {m(m+1)(m+2)\over3}+{m(m+1)\over2}\\
 &= {m(m+1)(2m+7)\over6}.                             \tag{5.3}
\end{aligned}
\]

Removing `D_(m,m)` subtracts `2m+1`.  Substituting (5.2)--(5.3) into
(4.5) yields the explicit audited form

\[
\boxed{
 2d\ge
 {m(m+1)(2m+7)\over6}
 -T-(m+1)(m+2)-2E-(10m+5).
}                                                       \tag{5.4}
\]

This proves (1.3).  Its leading term is `m^3/3`, so `E,d,T=O(m^2)` is
impossible.  Equivalently, with `E,d=O(m^2)`, one must replace
`Omega(m^3)` of the natural rare-endpoint lower witnesses.

## 6. Self-audit and exact limitations

The proof uses only:

* the exact internal-run factor criterion (3.2);
* nonemptiness of each retained natural core, not its stronger bit pins;
* monotonicity of `alpha` and `beta`;
* literal contiguity of the selected natural diagonal blocks; and
* the near-once bound on occurrences of the single atom `(4,m)`.

The constant checks are:

* `sum q_B<=2P_b`, not `P_b`, because one run can join the rare end of one
  block to the rare start of the next;
* the two disjoint charge families use different monotone sequences, hence
  give `2d` rather than `d`;
* omitting the possibly zero full meet costs exactly `2m+1` in (5.3);
* the two boundary runs cost at most `8m+4`; together these give `10m+5`;
* `2*binom(m+2,2)=(m+1)(m+2)` in (5.4).

The conclusion is deliberately architectural.  It does not apply if a
construction:

1. splits or interleaves most natural diagonal blocks;
2. represents a natural lower target by a different cross-block meet;
3. uses arbitrary non-core lower windows and passes the full global legal-set
   criterion; or
4. abandons the natural central-square witnesses altogether.

In particular, it is not a lower bound for unrestricted `g_4`.  It proves
that the proposed positive route cannot obtain its factor merely by placing
an `O(m^2)` triangular-tail superposition around intact natural diagonals
and repairing only `O(m^2)` central targets literally.
