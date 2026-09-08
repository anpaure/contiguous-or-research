# The order-one marked-trace polytope is a threshold-coupling polytope

Date: 2026-08-01  
Status: exact theorem.  This proves the marked-trace fractional gate for
every parameter set with `d=1`.  Weak connectivity and integral
one-owner-per-colour rounding remain separate conditions.

## 0. Statement

Fix `1 <= r <= k`, and let

\[
             q=(q_1,\ldots,q_{r-1})\in\mathbb R_{\geq0}^{r-1},
             \qquad Q=\sum_{s=1}^{r-1}q_s .
\]

Write

\[
 F(a)=\sum_{1\leq s\leq a}q_s,
 \qquad F(a)=0\quad(a\leq0).
\]

Recall that `ST_(k,r,1)` is the projection of the `Sym(k)`-invariant
order-one marked-trace circulation polytope onto the marked head-rank
histogram.

Throughout, trace letters are nonempty subsets.  Thus endpoint ranks range
over `1,...,r`; admitting the empty trace state would change the transport
ground set and the statement below.

## Theorem 0.1 (exact order-one characterization)

One has

\[
 \boxed{
 q\in\mathsf{ST}_{k,r,1}
 \quad\Longleftrightarrow\quad
 Q\leq1
 \ \text{and}\ 
 F(a)+F(r-a-1)\leq1\quad(0\leq a<r).}
 \tag{0.1}
\]

Equivalently, append the canonical slack mass

\[
                         q_r=1-Q.                    \tag{0.2}
\]

Then (0.1) says exactly that the probability vector
`(q_1,...,q_r)` has a self-coupling supported on

\[
                         a+b\geq r.                  \tag{0.3}
\]

The literal lift is explicit: conditionally on ranks `(a,b)`, choose
uniformly an ordered pair `(A,B)` of subsets of an owner `T` with

\[
 |A|=a,\qquad |B|=b,\qquad A\cup B=T,               \tag{0.4}
\]

use the trace edge `A -> B`, and mark `B` exactly when `b<r`.

Here self-coupling means a coupling with equal left and right marginals; it
need not be symmetric, although averaging it with its transpose makes it
so.  Formula (0.2) is a constructive normalization which places all slack
on unmarked full-owner heads.  It does not assert that an arbitrary witness
for `q` has no unmarked proper heads.

## 1. Necessity

Let `x` be any invariant order-one marked-trace circulation of total owner
mass one per owner.  Normalize by the total owner mass and let

\[
                         p_s
\]

be the rank distribution of a tail state.  Flow balance makes this also
the rank distribution of a head state.  A marked rank-`s` head is in
particular a rank-`s` head, so

\[
                         p_s\geq q_s\quad(s<r).       \tag{1.1}
\]

Every trace edge has owner rank `r`; hence its endpoint ranks `(a,b)` obey
`a+b>=r`.  Therefore the events

\[
 \{\text{tail rank}\leq a\},
 \qquad
 \{\text{head rank}\leq r-a-1\}
\]

are disjoint.  Stationarity gives

\[
 \sum_{s\leq a}p_s+
 \sum_{s\leq r-a-1}p_s\leq1.                        \tag{1.2}
\]

Using (1.1) in (1.2) proves every inequality in (0.1).  Finally, at most
one proper suffix can be marked on an order-one edge, so `Q<=1`.

## 2. The rank-level transport theorem

Put

\[
 \widehat q=(q_1,\ldots,q_{r-1},1-Q).
\]

Make a bipartite graph with ranks `1,...,r` on both shores and edge
`a b` precisely when `a+b>=r`.  We claim that (0.1) is Hall's condition
for a transport plan with both marginals `qhat`.

Indeed, for a set `I` of left ranks, let `a=max I`.  Its neighbourhood is

\[
                  N(I)=\{b:b\geq r-a\}.              \tag{2.1}
\]

Moreover, replacing `I` by the full initial segment `{1,...,a}` can only
increase its mass and leaves the neighbourhood unchanged.  Thus the only
Hall inequalities that can be tight are

\[
 \sum_{s\leq a}\widehat q_s
 \leq
 \sum_{s\geq r-a}\widehat q_s .                     \tag{2.2}
\]

For `a<r`, (2.2) is precisely

\[
                         F(a)+F(r-a-1)\leq1.          \tag{2.3}
\]

The case `a=r` is equality of the two total masses.  Fractional bipartite
matching (or max-flow/min-cut) therefore supplies numbers

\[
 m_{ab}\geq0,qquad m_{ab}=0\ (a+b<r),               \tag{2.4}
\]

with row and column sums both equal to `qhat`.

The separately displayed condition `Q<=1` is redundant: it is already the
`a=0` (equivalently `a=r-1`) inequality in (0.1).  It is retained to make
nonnegativity of the slack coordinate (0.2) explicit.

This also identifies a generating transportation model for
`ST_(k,r,1)`: they are the allowed ordered rank pairs `(a,b)` with
`a+b>=r`, combined into balanced transportation cycles.  The inequalities
(0.1) are a complete inequality description after projection to marked
lower head mass (some inequalities can of course be redundant in small
rank).

## 3. Literal subset lift

Fix an owner `T in binom([k],r)`.  For every allowed rank pair `(a,b)`,
there are ordered pairs `(A,B)` satisfying (0.4): choose an intersection
of rank `a+b-r`, then the two disjoint remainders.  Distribute the mass
`m_(a,b)` uniformly over all such ordered pairs and place it on the trace
edge

\[
                              A\longrightarrow B.    \tag{3.1}
\]

The conditional law is invariant under `Sym(T)`.  Consequently, for every
fixed `A subseteq T` of rank `a`, the outgoing mass is

\[
                         \frac{\widehat q_a}{\binom ra},
\]

and the incoming mass is the same, because the two marginals of `m` agree.
Thus every literal state is balanced, not merely every state rank.

Repeat this independently and identically at every owner.  A literal set
can lie in several owners, but every owner contribution is already
balanced, so their sum is balanced as well.  The total edge mass at each
owner is one.

Mark the head `B` on every edge with `b<r`, and leave a rank-`r` head
unmarked.  The marked rank histogram per owner is exactly `q`.  This proves
the sufficiency direction of Theorem 0.1.

For the triangular target

\[
 q_s=\frac{\binom ks-b_s}{\binom kr},                \tag{3.2}
\]

the literal load of a fixed rank-`s` target `S` is

\[
 \binom{k-s}{r-s}\frac{q_s}{\binom rs}
 =1-\frac{b_s}{\binom ks},                           \tag{3.3}
\]

using

\[
 \binom ks\binom{k-s}{r-s}=\binom kr\binom rs.
\]

Hence this is the full targetwise marked-trace solution, not only a rank
calculation.

## 4. The actual `d=1` triangular cases

The nontrivial cases are `k=3,4,6`:

* `k=3`: `r=2`, `q_1=1`;
* `k=4`: `r=2`, `q_1=2/3`;
* `k=6`: `r=3`, `(q_1,q_2)=(1/4,3/4)`.

They all satisfy (0.1).  For `k=6`, one rank coupling is

\[
 m_{12}=m_{21}=\frac14,
 \qquad m_{22}=\frac12,                              \tag{4.1}
\]

which is the rank projection of the twelve-edge balanced clock already
recorded in the handoff.  Thus Theorem 0.1 proves the marked-trace
fractional gate for every actual order-one instance.

## 5. Reflection-principle meaning of the binomial profile

Let

\[
 \varepsilon=k\bmod2,
 \qquad r=\frac{k+\varepsilon}{2},
\]

and choose uniformly among length-`k` simple random-walk paths conditioned
to run from `0` to `epsilon`.  Let `M` be its maximum.  Reflection after the first visit to
level `t` is a bijection from paths ending at `epsilon` and hitting `t` to
unrestricted paths ending at `2t-epsilon`.  Therefore

\[
 \Pr(M\geq t)
 =\frac{\binom{k}{r-t}}{\binom kr}
 \qquad(1\leq t\leq r).                              \tag{5.1}
\]

In the deficiency coordinate `t=r-s`, the unpunctured lower histogram is
therefore exactly the survival function of the bridge maximum:

\[
 \boxed{
 \frac{\binom{k}{s}}{\binom kr}
       =\Pr(M\geq r-s).}                             \tag{5.2}
\]

In particular,

\[
 \frac{1}{\binom kr}\sum_{s=1}^{r-1}\binom ks
 =\sum_{t=1}^{r-1}\Pr(M\geq t)
 =\mathbb E M-\Pr(M=r).                              \tag{5.3}
\]

The final correction is `1/binom(k,r)`: only the unique mountain path
`U^r D^(k-r)` reaches level `r`.  Formula (5.3) explains both the `Theta(sqrt(k))` depth
and the Catalan/ballot signature of the triangular profile.  It suggests
that a general-`d` stationary clock should be built from cyclically rooted
bridge excursions, rather than from the divergent consecutive clock.

## 6. Scope: balance versus connected support

Theorem 0.1 characterizes membership in `ST_(k,r,1)`, whose definition
requires nonnegative invariant balance but not connected support.  It does
not assert that every feasible `q` has a weakly connected literal support.

For the three actual triangular cases above, connected solutions can be
chosen explicitly:

* for `k=3`, the singleton edges supplied by the three owners connect the
  singleton states;
* for `k=4`, the explicit rank coupling

  \[
    m_{11}=\frac12,\qquad
    m_{12}=m_{21}=m_{22}=\frac16
  \]

  puts positive mass on all four allowed rank pairs; and
* for `k=6`, the recorded twelve-edge construction is connected.

Thus boundary rooting is also available in every actual `d=1` case.
In higher order, membership, connected support/root exposure, and coloured
one-copy rounding must continue to be treated as three distinct gates.
