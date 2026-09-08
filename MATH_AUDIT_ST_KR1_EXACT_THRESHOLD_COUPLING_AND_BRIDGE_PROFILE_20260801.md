# Independent audit of the order-one marked-trace threshold theorem

Date: 2026-08-01  
Audited input SHA-256:
`03c8275a6f8f9001ecbfc82650c469f4807fa287b59dff197126b6808c0618c1`  
Corrected theorem SHA-256:
`490ebf5bc46a3c2a916f08c33e0909e76f974bb68709523aaa2362da9264b88e`  
Verdict: **PASS**, with wording/scope clarifications only.  Every assertion
in this audit is restricted to order `d=1`.

## 0. Audited claims

Let

\[
 q=(q_1,\ldots,q_{r-1})\ge0,
 \qquad Q=\sum_{s<r}q_s,
 \qquad F(a)=\sum_{1\le s\le a}q_s.
\]

For the nonempty trace alphabet, the theorem correctly proves

\[
 q\in\mathsf{ST}_{k,r,1}
 \quad\Longleftrightarrow\quad
 Q\le1,
 \qquad F(a)+F(r-a-1)\le1\quad(0\le a<r).
 \tag{0.1}
\]

It also correctly proves the equal-marginal coupling interpretation, the
literal uniform-subset lift, the list of nontrivial triangular `d=1`
instances, and the bridge-maximum identity.

Two clarifications were inserted in the theorem source.

1. The coordinate `q_r=1-Q` is a **canonical slack realization**, placed on
   unmarked full-owner heads in the constructive lift.  A different feasible
   witness may have unmarked proper heads.
2. Endpoint ranks are `1,...,r` because trace letters are nonempty.  If the
   empty letter were admitted, the transport ground set and inequalities
   would have to be reformulated.

The displayed condition `Q<=1` is redundant with the `a=0` inequality, but
is useful for making the slack coordinate visibly nonnegative.

## 1. Necessity is exact

Normalize an invariant order-one circulation by its total owner mass and
let `p_s` be its tail-rank law.  Literal flow balance makes `p` also the
head-rank law.  Since every marked rank-`s` head is a rank-`s` head,

\[
                         p_s\ge q_s\qquad(s<r).       \tag{1.1}
\]

For every edge `A->B`,

\[
                         |A|+|B|\ge|A\cup B|=r.       \tag{1.2}
\]

Thus the two edge events

\[
 |A|\le a,
 \qquad |B|\le r-a-1
\]

are disjoint.  Stationarity and (1.1) give

\[
 F(a)+F(r-a-1)\le1.
\]

At order one an atom has at most one marked proper suffix, so `Q<=1`.
There is no hidden connectedness assumption in this direction.

## 2. Fractional Hall gives sufficiency

Put

\[
 \widehat q=(q_1,\ldots,q_{r-1},1-Q).
\]

On two copies of ranks `1,...,r`, join `a` to `b` exactly when
`a+b>=r`.  If a left-rank set `I` has maximum `a`, its neighbour set is
the suffix `{r-a,...,r}`.  Replacing `I` by `{1,...,a}` leaves that suffix
unchanged and only increases left mass.  Hence fractional Hall reduces
exactly to

\[
 \sum_{s\le a}\widehat q_s
 \le \sum_{s\ge r-a}\widehat q_s,
\]

which is (0.1).  Therefore there is a nonnegative transport matrix
`m_(a,b)` supported on `a+b>=r` with both marginals equal to `qhat`.

“Self-coupling” here means equal marginals, not a symmetric matrix.
Symmetrizing `m` with its transpose is optional and preserves all rows.

The edge cases also pass: for `r=1` the vector `q` is empty and the lift is
the unmarked loop `T->T`; for `q=0` all mass may likewise be placed at rank
`r`; and equality in any threshold cut is harmless.

## 3. The literal lift is statewise

Fix an owner `T` of rank `r`.  For every allowed `(a,b)`, distribute
`m_(a,b)` uniformly over ordered pairs

\[
 A,B\subseteq T,\qquad |A|=a,\qquad |B|=b,\qquad A\cup B=T.
\]

Such pairs exist exactly when `a+b>=r`.  The action of `Sym(T)` is
transitive on the rank-`a` tails and on the rank-`b` heads.  Thus every
fixed rank-`a` subset has outgoing mass

\[
                         \frac{\widehat q_a}{\binom ra},
\]

and incoming mass equal to the same expression.  Balance therefore holds
at every literal subset inside every owner, not only after rank projection.
Summing ownerwise balanced contributions preserves global literal balance.

Marking precisely the proper heads gives marked rank histogram `q`.  For a
fixed global rank-`s` target `S`, its owner load is

\[
 \binom{k-s}{r-s}\frac{q_s}{\binom rs}
 =\frac{\binom kr}{\binom ks}q_s.
 \tag{3.1}
\]

For the triangular value

\[
 q_s=\frac{\binom ks-b_s}{\binom kr},
\]

equation (3.1) is exactly `1-b_s/binom(k,s)`.  Hence the lift is genuinely
targetwise.

## 4. Complete classification of triangular `d=1`

The cases with positive depth one are exactly

\[
                              k\in\{3,4,6\}.          \tag{4.1}
\]

For odd `k=2m+1`,

\[
 W=\binom{2m+1}{m},\qquad \Lambda=4^m-1,
\]

and `d=1` is equivalent to

\[
                         4^m\le W+2.                  \tag{4.2}
\]

This holds at `m=1` and fails at `m=2`.  The ratio

\[
 \frac{\binom{2m+3}{m+1}}{\binom{2m+1}{m}}
 =\frac{2(2m+3)}{m+2}<4
\]

propagates failure for every larger `m`.

For even `k=2m`,

\[
 W=\binom{2m}{m},\qquad
 \Lambda=\frac{4^m-W}{2}-1,
\]

and `d=1` is equivalent to

\[
                         4^m\le3W+4.                  \tag{4.3}
\]

It holds at `m=2,3`, fails at `m=4`, and failure again propagates because

\[
 \frac{\binom{2m+2}{m+1}}{\binom{2m}{m}}
 =\frac{2(2m+1)}{m+1}<4.
\]

The smaller cases `k=1,2` have `d=0`.  The three depth-one histograms are

\[
 \begin{array}{c|c|c}
 k&r&q\\ \hline
 3&2&(1)\\
 4&2&(2/3)\\
 6&3&(1/4,3/4).
 \end{array}
\]

They satisfy (0.1).  At `k=4`, the explicit fully supported coupling

\[
 m_{11}=\frac12,qquad
 m_{12}=m_{21}=m_{22}=\frac16
\]

also proves connected support.  At `k=6`, the recorded twelve-edge lift has
coupling `m_12=m_21=1/4`, `m_22=1/2`; every singleton gets owner load
`5/6` plus boundary load `1/6`, and every pair gets owner load one.  The
literal positive supports in all three cases are weakly connected and meet
every singleton root state.

## 5. Reflection-principle identity

Let `epsilon=k mod 2`, `r=(k+epsilon)/2`, and choose a simple random-walk
path uniformly conditional on starting at zero and ending at `epsilon`
after `k` steps.  Let `M` be its maximum.

Reflect the suffix after the first visit to level `t`.  This bijects paths
ending at `epsilon` and hitting `t` with unrestricted paths ending at
`2t-epsilon`.  The latter have exactly `r-t` downsteps, so

\[
 \Pr(M\ge t)=\frac{\binom{k}{r-t}}{\binom kr}
 \qquad(1\le t\le r).                                 \tag{5.1}
\]

Putting `t=r-s` gives

\[
 \frac{\binom ks}{\binom kr}=\Pr(M\ge r-s).
 \tag{5.2}
\]

Since `0<=M<=r`, the tail-sum formula yields

\[
 \frac1{\binom kr}\sum_{s=1}^{r-1}\binom ks
 =\mathbb E M-\Pr(M=r).                               \tag{5.3}
\]

Only the unique mountain path `U^r D^(k-r)` reaches height `r`, so the last
probability is exactly `1/binom(k,r)`.  All parity and endpoint cases,
including `t=r`, are valid.

## 6. Scope

The audit establishes only

\[
 q\in\mathsf{ST}_{k,r,1}.
\]

It does not infer any characterization of `ST_(k,r,d)` for `d>1`.
Connected support is not part of the polytope definition, although explicit
connected lifts exist in the three actual depth-one cases.  Rational
circulation also remains weaker than one-owner-per-colour integral Euler
rounding.
