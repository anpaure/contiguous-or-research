# Independent audit of the order-one and private-phase stationary-trace theorems

Date: 2026-08-01  
Audited order-one theorem SHA-256:
`490ebf5bc46a3c2a916f08c33e0909e76f974bb68709523aaa2362da9264b88e`  
Corrected private-phase reduction SHA-256:
`c2b3df17c3c4b54ae56a199d68241fe05d4e0099923e93a980be8d5a8d36bd37`

Verdict: **PASS** for the order-one characterization, threshold
self-coupling, literal subset lift, bridge reflection, private-pattern
circulation, and stationary concavity law.  The two-guard address identities
and the two-visit construction also pass.  One proof correction was required:
the original argument from the unique immediate letters did not by itself
exclude longer collars.  The corrected proof uses the inclusion chain of
all interval unions with one fixed endpoint and establishes the claimed
necessity for the exact equal-rank banks even with longer collars.

No finite LP output is used in this audit.  The reported `d=3` probes remain
architectural evidence only.

## 1. Order-one threshold characterization

Let

\[
 q=(q_1,\ldots,q_{r-1})\ge0,\qquad
 Q=\sum_{s<r}q_s,\qquad
 F(a)=\sum_{1\le s\le a}q_s.
\]

For the nonempty trace alphabet, endpoint ranks lie in `1,...,r`.  The
claimed equivalence is

\[
 q\in\mathsf{ST}_{k,r,1}
 \iff Q\le1\text{ and }
 F(a)+F(r-a-1)\le1\quad(0\le a<r).
 \tag{1.1}
\]

### 1.1 Necessity

Normalize a stationary order-one trace measure to owner mass one and let
`p_s` be its tail-rank law.  Literal balance makes this the head-rank law as
well.  Marked rank-`s` mass is a submeasure of the head-rank-`s` mass, so

\[
                              p_s\ge q_s.             \tag{1.2}
\]

Every edge `A->B` has `|A union B|=r`, hence `|A|+|B|>=r`.  The events

\[
 |A|\le a,\qquad |B|\le r-a-1
\]

are disjoint.  Equal endpoint marginals and (1.2) therefore give every cut
in (1.1).  An order-one atom has only one proper suffix position, giving
`Q<=1`.  In fact the latter is also the `a=0` (and `a=r-1`) cut once
`F(0)=0` is adopted.

### 1.2 Sufficiency and self-coupling

Set

\[
                  \widehat q=(q_1,\ldots,q_{r-1},1-Q).
\]

On two copies of the rank set `1,...,r`, allow `(a,b)` exactly when
`a+b>=r`.  If a nonempty left set of ranks has maximum `a`, its neighbour
set is the suffix `{r-a,...,r}`.  Filling the left set to the initial
segment `{1,...,a}` preserves that neighbourhood and weakly raises its
mass.  Thus weighted Hall has only the initial-segment cuts

\[
 \sum_{s\le a}\widehat q_s
 \le \sum_{s\ge r-a}\widehat q_s,
\]

which rearrange exactly to (1.1).  Fractional Hall supplies a transport
matrix `m_(a,b)` supported on `a+b>=r` with both marginals `qhat`.

This proves the stated self-coupling equivalence.  Equal left and right
marginals are all that is required; symmetry of the matrix is optional.
The coordinate `q_r=1-Q` is a constructive placement of all unmarked slack
at full-owner heads and does not classify the unmarked heads of every
possible witness.

## 2. Literal subset lift and target load

Fix one owner `T` of rank `r`.  For each allowed rank pair `(a,b)`, the
ordered pairs

\[
 A,B\subseteq T,\qquad |A|=a,\quad |B|=b,\quad A\cup B=T
\]

are nonempty and form a transitive `Sym(T)`-set on each endpoint shore.
Uniformly distributing `m_(a,b)` over them gives every fixed rank-`a`
tail outgoing mass

\[
                       \frac{\widehat q_a}{\binom ra}.
\]

The equal head marginal gives the same incoming mass to that literal set.
Balance is therefore ownerwise and literal, not merely rankwise.  Summing
over owners preserves it.

Marking exactly heads of rank below `r` gives histogram `q`.  A fixed global
rank-`s` target belongs to `binom(k-s,r-s)` owners, hence has marked load

\[
 \binom{k-s}{r-s}\frac{q_s}{\binom rs}
 =\frac{\binom kr}{\binom ks}q_s.                   \tag{2.1}
\]

At the triangular value

\[
 q_s=\frac{\binom ks-b_s}{\binom kr},
\]

this is exactly `1-b_s/binom(k,s)`.  Thus the lift proves the literal
target equations, not only their rank sums.

The order-one theorem does not establish connected support or integral
one-owner-per-colour rounding.  The separate explicit constructions for
the actual positive-depth cases `k=3,4,6` supply connected support only in
those cases.

## 3. Bridge-maximum reflection

Let `epsilon=k mod 2`, `r=(k+epsilon)/2`, and condition a length-`k`
simple walk to end at `epsilon`.  Reflect the suffix after its first visit
to height `t`.  The endpoint changes from `epsilon` to `2t-epsilon`, and
the transformed walk has exactly `r-t` downsteps.  Every walk ending at
`2t-epsilon` reaches `t`, so the map is bijective.  Therefore

\[
 \Pr(M\ge t)=\frac{\binom{k}{r-t}}{\binom kr}
 \qquad(1\le t\le r).                               \tag{3.1}
\]

Putting `t=r-s` gives the binomial survival profile.  The tail-sum formula
then yields

\[
 \frac1{\binom kr}\sum_{s=1}^{r-1}\binom ks
 =\mathbb E M-\Pr(M=r).
\]

The event `M=r` contains only `U^r D^(k-r)`, so its probability is
`1/binom(k,r)`.  The parity endpoints and `t=r` boundary all pass.

## 4. Private-phase circulation

Put `n=d+1`, choose distinct private coordinates `p_i`, and give every
remaining coordinate a nonempty pattern `P_x subseteq Z_n`.  Define

\[
 B_i=\{p_i\}\cup\{x:i\in P_x\}.
\]

The full cyclic window contains every private coordinate and every extra
coordinate, so its owner is `T`.  A proper phase interval omits at least one
phase `i` and consequently omits `p_i`.  Adding a new phase always adds its
previously absent private coordinate.  Hence every proper interval is
proper and the suffix unions are strictly increasing.

For

\[
 e_i=(B_i,B_{i+1},\ldots,B_{i+d}),
\]

the tail of `e_i` is the head of `e_(i-1)`.  Uniform mass on the `n` cyclic
phases is therefore a literal directed-cycle measure.  Marking suffixes
does not alter its boundary.  Averaging over owner and coordinate
relabelings gives a valid invariant member of `ST_(k,r,d)`.

For one configuration, full marking gives the profile `g(P)` and total
marked mass `d`.  Convex mixtures remain circulations.  Coordinatewise
downward closure is valid because marked occurrences of each rank may be
independently thinned by a rank-dependent probability; the underlying
trace mass and balance equations remain unchanged.

The missing-set formulas also pass.  If `J` is the omitted complement of a
suffix interval, its missing private coordinates contribute `|J|`.  An
extra coordinate is missing exactly when its pattern lies in `J`.  In the
pair-pattern submodel this count is the induced-edge number `e_G(J)`, giving
`r-|U(I)|=|J|+e_G(J)` exactly.

## 5. Stationary first-occurrence concavity

For one coordinate in one cyclic binary incidence word, the increment at
window length `j` counts occurrences of a `1` followed toward the current
endpoint by at least `j-1` zeros.  Equivalently, a zero gap of length `ell`
contributes one discovery at each `j=1,...,ell+1`.  These counts are
nonincreasing in `j`.  Summing over coordinates and averaging the root
gives

\[
                  \Delta_1\ge\Delta_2\ge\cdots.     \tag{5.1}
\]

If every `(d+1)`-window has rank `r`, then the first `d+1` increments sum
to `r`.  A nonincreasing nonnegative sequence with that sum has every
prefix average at least the total average, hence

\[
 \mathbb E R_j\ge\frac{jr}{d+1},
 \qquad
 \sum_{j=1}^{d}\mathbb E R_j\ge\frac{rd}{2}.        \tag{5.2}
\]

If all suffixes are marked, the left side of the second inequality is
`sum_s s q_s`.  With unmarked mass
`epsilon=d-sum_s q_s`, every omitted suffix position has rank between one
and `r`, giving exactly

\[
 \sum_s s q_s+\varepsilon
 \le\sum_{j=1}^d\mathbb E R_j
 \le\sum_s s q_s+r\varepsilon.                     \tag{5.3}
\]

This is a necessary law for stationary traces, not a proof that the
triangular vector belongs to the private-pattern cone.

## 6. Two-guard occurrence semantics

For the ordered-singleton state

\[
 v=(\{f_1\},\ldots,\{f_d\}),\qquad F=\{f_1,\ldots,f_d\},
\]

the literal traversal

\[
                         G,v,G
\]

has the two disjoint cells

\[
 P_G(j)=G\cup F[1,j],\qquad
 S_G(j+1)=G\cup F[j+1,d].
\]

Their intersection is `G` and their union is `G union F`, independently
of `j`.  This is a genuine occurrence-labelled antidiagonal.  Two visits
`G_1,v,G_1` and `G_3,v,G_3` therefore suffice for two banks and consume
two distinct physical address families.  In a rational circulation the
two visits may be separate positive branches through the same state;
denominator clearing makes them two visits of the Euler multigraph.

Necessity is stronger than the original immediate-letter proof.  If one
occurrence supplied both exact equal-rank banks, then at `j=1` the two
prefix cells would be

\[
                  G_1\cup\{f_1\},\qquad
                  G_3\cup\{f_1\}.
\]

They are distinct and have equal rank.  But every interval union ending at
the same physical occurrence `{f_1}` belongs to one inclusion chain as its
left endpoint moves.  Distinct equal-rank sets cannot both lie in that
chain.  Thus two visits are necessary even if one allows longer exterior
collars, provided the requested cells are the exact banks above.  The
suffix cells at the fixed occurrence `{f_d}` give the same proof.

## 7. Exact surviving frontier

The audited results prove:

1. the complete `d=1` rank-projection characterization;
2. an explicit sufficient private-pattern cone for every `d`;
3. a necessary stationary concavity inequality for every `d`; and
4. exact occurrence addresses, and exact two-visit necessity, for two
   equal-rank guarded singleton-root banks.

They do **not** prove that the triangular binomial vector belongs to the
private-pattern cone for arbitrary `d`.  Nor do they prove connected
support, simultaneous two-guard/common-cap compatibility, or one-copy
coloured Euler rounding.  The finite LP probes quoted in the reduction are
consistent with the proposed architecture but carry no theorem-level
weight.
