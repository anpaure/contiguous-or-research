# Multi-slab cross-SCD chainization: exact sockets, Hall system, and the top-slab obstruction

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction and obstruction.  The
variable collar socket ledger and the named attachment Hall theorem are
exact.  The rank-density transportation system is exact for the symmetrized
fractional relaxation.  The canonical decomposition into maximal depth-`d`
slabs fails the first capacity cut by linear mass.  More strongly, in all
sufficiently large even dimensions, **every** decomposition into common
consecutive rank slabs fails the rank-density cuts.  Thus any successful
second-SCD construction must split different SCD chains at different ranks.
No integral complete lower-ideal chainization is claimed.

## 0. Setup and outcome

Put

\[
 r=\left\lceil {k\over2}\right\rceil,
 \qquad C_s={k\choose s},
 \qquad W=C_r,
 \qquad \Lambda=\sum_{s=1}^{r-1}C_s,
\]

and let `d` be least with

\[
 dW+{d+1\choose2}\ge\Lambda .                       \tag{0.1}
\]

Write

\[
 t=r-d,
 \qquad H_b=C_b-C_{b-1}\quad(C_{-1}:=0).             \tag{0.2}
\]

Take one symmetric chain decomposition `S_C` for the collar ranks
`t,...,r-1`.  Every one of its `W` chains has a unique rank-`r` owner.
If its bottom rank is `b`, its collar load is

\[
 \ell_b=\min(d,r-b)
\]

and its unused owner capacity is

\[
 c_b=d-\ell_b=(b-t)_+.                               \tag{0.3}
\]

Hence the positive owner sockets have the exact histogram

\[
 \boxed{\#\{\hbox{owner sockets of capacity }u\}=H_{t+u}
        \quad(1\le u\le d).}                         \tag{0.4}
\]

In particular the full-capacity owner sockets are exactly

\[
 H_r=W-C_{r-1},                                      \tag{0.5}
\]

the owner chains having no rank-`(r-1)` collar member.  These are the
previously omitted empty owner sockets.

The endpoint-triangular capacity vector contributes, in addition, one
boundary socket of each capacity

\[
                         d,d-1,\ldots,1.              \tag{0.6}
\]

Thus the multi-slab proposal has a completely explicit receiving side.
For any second SCD whose ranks below `t` have been cut into chain chunks,
Section 2 gives the exact named Hall criterion for attaching every chunk.
Section 3 gives the exact rank-density relaxation.  Section 4 first shows
that cutting the second SCD into maximal consecutive `d`-slabs cannot work:
its very first threshold cut, at capacity `d`, fails asymptotically by
`Theta(W)`.  It then proves that no common consecutive rank-slab partition
can pass all threshold cuts in sufficiently large even dimension.

## 1. Exact collar and scalar ledgers

An SCD has exactly `H_b` chains whose bottom rank is `b`.  This follows by
subtracting the numbers `C_(b-1)` and `C_b` of chains reaching the two
successive ranks.  Formula (0.4) is therefore independent of which SCD is
chosen.

The collar chunks partition every target of ranks `t,...,r-1`.  Consequently
the total unused owner capacity is

\[
 \sum_{u=1}^d uH_{t+u}
 =dW-\sum_{s=t}^{r-1}C_s.                             \tag{1.1}
\]

This also follows directly by subtracting the number of collar targets from
the `dW` owner capacity.

After adjoining the boundary sockets (0.6), the capacity available for the
strictly lower ranks is

\[
 dW-\sum_{s=t}^{r-1}C_s+{d+1\choose2}.               \tag{1.2}
\]

The demand in those ranks is `sum_(s=1)^(t-1) C_s`, so the exact vacancy is

\[
 \boxed{
 dW+{d+1\choose2}-\Lambda .}                         \tag{1.3}
\]

It is nonnegative by (0.1).  Thus the variable collar, the empty owner
sockets, and the clipped endpoint sockets reproduce the optimal triangular
scalar ledger exactly; no capacity has disappeared in passing to the
multi-slab model.

## 2. Exact named multi-slab Hall theorem

Let `S_R` be an arbitrary second SCD.  Partition the nonempty members of its
chains in ranks `1,...,t-1` into disjoint nonempty consecutive chunks.  Let
`R` be the resulting chunk family.  For a chunk `F`, write

\[
 S_F=\max F,\qquad a_F=|F|.                           \tag{2.1}
\]

For a collar chain with bottom rank `b>t`, let `B` be its bottom set.  When
`b=r`, its collar is empty and `B` is the rank-`r` owner itself.  Regard it
as an owner socket `(B,b)` of capacity `b-t`.  Also let `partial_u` denote
the boundary socket of capacity `u`.

Define a bipartite graph `Gamma` from chunks to sockets by

\[
 F\sim(B,b)
 \Longleftrightarrow
 a_F\le b-t\ \hbox{ and }\ S_F\subset B,             \tag{2.2}
\]

and

\[
 F\sim\partial_u\Longleftrightarrow a_F\le u.        \tag{2.3}
\]

### Theorem 2.1 (exact multi-slab attachment criterion)

The second-SCD chunks and all collar targets form a partition into the
endpoint-triangular capacities if and only if

\[
 \boxed{|N_\Gamma(X)|\ge |X|\qquad(X\subseteq R).}    \tag{2.4}
\]

The minimum number of chunks that must be discarded is

\[
 \boxed{\delta=
 \max_{X\subseteq R}(|X|-|N_\Gamma(X)|)_+.}           \tag{2.5}
\]

#### Proof

Hall's theorem gives a matching saturating `R` exactly under (2.4), and its
deficiency form gives (2.5).  If `F` is matched to `(B,b)`, then its top is
contained in the bottom of that collar chain, so concatenating the two gives
one inclusion chain.  Its load is at most

\[
 a_F+(r-b)\le (b-t)+(r-b)=d.                          \tag{2.6}
\]

If `F` is matched to `partial_u`, it is already a chain and has load at most
`u`.  Different chunks use different sockets.  Conversely, any such
attachment selects a distinct adjacent socket for every chunk and hence is
a matching.  \(\square\)

Theorem 2.1 is the exact integral statement.  Unlike the one-slab theorem,
its owner roots at rank `b` form the SCD-dependent family of chain minima,
not the complete rank-`b` layer.  Therefore binomial rank counts alone do
not prove (2.4).

## 3. Exact rank-density transportation relaxation

Let `A_(s,a)` be the number (or fractional mass) of residual chunks having
top rank `s<t` and load `a`.  Ignore the literal identities temporarily and
retain only these types.  Let

* `x_(s,a,u)` be mass sent to owner sockets of capacity `u`;
* `y_(s,a,u)` be mass sent to the unique boundary socket of capacity `u`.

The rank-density transportation system is

\[
 \sum_{u\ge a}\bigl(x_{s,a,u}+y_{s,a,u}\bigr)=A_{s,a},
                                                               \tag{3.1}
\]

\[
 \sum_{s,a\le u}x_{s,a,u}\le H_{t+u},
 \qquad
 \sum_{s,a\le u}y_{s,a,u}\le1,                     \tag{3.2}
\]

with all variables nonnegative.  Since eligibility is ordered only by
chunk load, the threshold version of Hall gives the following equivalence.

### Theorem 3.1 (rank-density threshold cuts)

System (3.1)--(3.2) is feasible if and only if, for every `1<=q<=d`,

\[
 \boxed{
 \sum_s\sum_{a\ge q}A_{s,a}
 \le W-C_{t+q-1}+d-q+1.}                             \tag{3.3}
\]

#### Proof

The left side is the number of chunks which require a socket of capacity at
least `q`.  The number of owner sockets of capacity at least `q` telescopes:

\[
 \sum_{u=q}^dH_{t+u}=W-C_{t+q-1}.                    \tag{3.4}
\]

There are `d-q+1` boundary sockets of capacity at least `q`.  Thus (3.3) is
necessary.  Conversely, the type-to-capacity graph is a Ferrers bipartite
graph; its only inclusion-minimal Hall cuts are the upper load thresholds.
The inequalities (3.3) therefore imply a saturating fractional (indeed
integral when the `A_(s,a)` are integral) transportation.  \(\square\)

There is a precise containment interpretation.  Average the collar SCD and
the residual SCD over all coordinate permutations.  At owner-root rank
`b=t+u`, every `b`-set then has socket capacity density `H_b/C_b`; within a
residual type `(s,a)`, every `s`-set is equally frequent.  For a prescribed
amount `x_(s,a,u)`, send each `s`-top uniformly to its containing `b`-sets.
A fixed `b`-set receives the uniform load `x_(s,a,u)/C_b`, summed over the
`C_s` top mass according to the normalization in (3.1), and (3.2) is exactly
the resulting layer capacity condition.  Hence (3.3) is not merely a scalar
count: it is the exact named-containment condition for the fully symmetrized
fractional relaxation.

For a fixed pair of literal SCDs it remains only a relaxation.  Their
minimum-set families can have nonuniform containment cuts, and Theorem 2.1,
not (3.3), is then authoritative.

## 4. The maximal `d`-slab construction fails its first cut

The most direct extension of the one-slab theorem partitions the ranks below
`t` from the top downward into consecutive blocks of width `d`:

\[
 I_j=[t-jd,\ t-(j-1)d-1]\qquad(j\ge1),               \tag{4.1}
\]

discarding or clipping blocks outside ranks `1,...,t-1`.

Restrict one SCD chain to a full block `[a,a+d-1]`.  Its chunk has length
`d` precisely when the chain begins at or below rank `a`.  The number of
such chains is `C_a`.  Therefore the first full block alone creates

\[
                         C_{t-d}=C_{r-2d}             \tag{4.2}
\]

chunks of load `d` (when `r-2d>=1`).  But the receiving side has only

\[
 H_r+1=W-C_{r-1}+1                                   \tag{4.3}
\]

capacity-`d` sockets: the empty owner sockets and the one unclipped boundary
socket.  Thus the `q=d` instance of (3.3) already demands

\[
 \boxed{C_{r-2d}\le W-C_{r-1}+1.}                    \tag{4.4}
\]

For even `k=2r`,

\[
 W-C_{r-1}={W\over r+1}.                             \tag{4.5}
\]

At the optimal depth,

\[
 {d\over\sqrt r}\longrightarrow{\sqrt\pi\over2},
\]

and the central binomial ratio gives

\[
 {C_{r-2d}\over W}\longrightarrow e^{-\pi}.         \tag{4.6}
\]

The left side of (4.4) is therefore `Theta(W)`, while the right side is
`O(W/r)`.  Hence (4.4) fails by `Theta(W)` for all sufficiently large even
dimensions.  In odd dimension `W=C_(r-1)`, so there is no full-capacity
owner socket at all and the same cut has right side one.

This is the first failing rank-density cut of the maximal-slab proposal.  It
does **not** rule out adaptive multi-slab chunking.  It proves the sharp
design requirement

\[
 \#\{\hbox{load-}d\hbox{ residual chunks}\}
 \le W-C_{r-1}+1,                                    \tag{4.7}
\]

and, more generally, every adaptive chunking must obey all thresholds
(3.3).  In particular, almost all residual chains which cross a full
`d`-rank block must be split before attachment.

### Theorem 4.1 (common rank slabs are asymptotically impossible)

Let `k=2r`, and partition all ranks `1,...,t-1` into common consecutive
intervals of length at most `d`.  Cut every chain of a second SCD at these
same rank boundaries.  For all sufficiently large `r`, the resulting chunk
profile violates (3.3).

#### Proof

Let the top interval be

\[
                         I=[a,t-1],\qquad L=t-a.       \tag{4.8}
\]

Thus `1<=L<=d`.  For large `r`, `a>1`, so there is a second interval whose
top rank is `a-1`.

An interval with top rank `s` produces exactly `C_s` nonempty SCD chunks,
one for each rank-`s` set.  The `q=1` cut therefore implies

\[
 C_{t-1}+C_{a-1}\le W-C_t+d.                         \tag{4.9}
\]

On the other hand, the top interval produces `C_a` chunks of full length
`L`, namely those whose SCD chains reach its bottom rank `a`.  The `q=L`
cut implies

\[
 C_a\le W-C_{t+L-1}+d-L+1.                           \tag{4.10}
\]

Suppose, for a contradiction, that such partitions exist for infinitely
many `r`.  Pass to a subsequence on which

\[
 {L\over\sqrt r}\longrightarrow x,
 \qquad 0\le x\le A:={\sqrt\pi\over2}.               \tag{4.11}
\]

The local central-binomial estimate and `d/sqrt(r)->A` turn (4.9) into

\[
 e^{-A^2}+e^{-(A+x)^2}\le1-e^{-A^2},                 \tag{4.12}
\]

whereas (4.10) becomes

\[
 e^{-(A+x)^2}+e^{-(A-x)^2}\le1.                     \tag{4.13}
\]

Put

\[
 z_0=\sqrt{-\log(1-2e^{-\pi/4})},
 \qquad x_0=z_0-A.                                   \tag{4.14}
\]

Equation (4.12) forces `x>=x_0`.  Define

\[
 f(x)=e^{-(A+x)^2}+e^{-(A-x)^2}.                     \tag{4.15}
\]

Now `f(A)=1+e^{-\pi}>1`, and direct substitution in (4.14) gives

\[
 f(x_0)
 =1-2e^{-\pi/4}+e^{-(2A-z_0)^2}>1.                  \tag{4.16}
\]

For completeness, `f'(x)` has the sign of

\[
 A\tanh(2Ax)-x.
\]

The latter function is strictly concave on the positive axis, is initially
positive, and has at most one positive zero.  Hence `f` increases and then
decreases.  Its minimum on `[x_0,A]` is attained at an endpoint; (4.16) and
`f(A)>1` show

\[
                         f(x)>1\quad(x_0\le x\le A). \tag{4.17}
\]

This contradicts (4.13).  Therefore no common rank-slab partition passes
the rank-density transportation cuts for all sufficiently large even
dimensions.  \(\square\)

The numerical separation in (4.16) is substantial:

\[
 A=0.886\ldots,qquad z_0=1.558\ldots,qquad
 f(x_0)=1.04\ldots .                                  \tag{4.18}
\]

The theorem is not a no-go for chain-dependent splitting.  It says that the
rank cuts themselves must move with the individual SCD chain; a fixed slab
grid cannot exploit the variable socket profile.

## 5. Exact frontier

The multi-slab idea has therefore advanced to the following proof-safe
form.

1. The collar supplies the exact capacity histogram (0.4), including all
   `W-C_(r-1)` empty owner sockets.
2. The endpoint boundary supplies exactly one socket of each capacity
   `1,...,d`.
3. The scalar ledger closes with precisely the optimal vacancy (1.3).
4. For any declared residual chunking, the complete named problem is the
   single Hall family (2.4).
5. Before literal containment is considered, the exact rank-density gate is
   the one-dimensional threshold family (3.3).
6. Equal maximal slabs fail the top threshold by linear mass, and every
   common consecutive slab grid eventually fails the pair of cuts `q=1`
   and `q=L` from Theorem 4.1.

What remains is a genuinely chain-adaptive theorem: cut different chains of
the second SCD at different ranks so that (3.3) holds, and simultaneously
choose or switch the collar SCD so that every literal Hall cut (2.4) holds.
Passing the first part would be an integral bounded-chain partition theorem;
passing the second is the new cross-SCD containment correlation.  Neither
follows from the anonymous triangular capacity equality alone.
