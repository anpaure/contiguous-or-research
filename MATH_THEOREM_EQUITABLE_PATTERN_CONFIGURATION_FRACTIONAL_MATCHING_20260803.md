# Canonical fractional matching and the exact saturated-prechain obstruction

**Date:** 2026-08-03  
**Status:** unconditional fractional configuration theorem, exact normalized
pair ledger, and an exact obstruction to rounding through one fixed
saturated Boolean prechainization.  No computation is used.  The theorem
starts from any exact rank-pattern schedule and builds a canonical
owner/order fractional matching with exact pattern and owner degrees and
explicit named-target degrees.  It does not round that matching integrally.

## 0. Result

Put

\[
k=2r,\qquad W=\binom{2r}{r}.
\]

Let

\[
\mathcal R=(R_1,\ldots,R_W),\qquad R_i\subseteq[r-1],
\]

be any rank-pattern schedule. Write

\[
N_s=\#\{i:s\in R_i\},\qquad
0\le N_s\le\binom{2r}{s}.                                \tag{0.1}
\]

Form the occurrence-labelled configuration hypergraph whose vertices are:

1. one pattern vertex \(p_i\) for every \(i\in[W]\);
2. one owner vertex \(o_T\) for every \(T\in\binom{[2r]}r\); and
3. every named target \(S\in\binom{[2r]}s\) for every scheduled rank \(s\).

For every triple consisting of a pattern \(i\), an owner \(T\), and a
permutation \(\pi\) of the coordinates of \(T\), introduce one labelled
configuration

\[
e(i,T,\pi)=\{p_i,o_T\}\cup
\{\operatorname{pref}_s(\pi):s\in R_i\}.                 \tag{0.2}
\]

Give every labelled configuration weight

\[
x_{i,T,\pi}=\frac1{W\,r!}.                               \tag{0.3}
\]

Then:

\[
d_x(p_i)=1,\qquad d_x(o_T)=1,                            \tag{0.4}
\]

and every rank-\(s\) named target has degree

\[
d_x(S)=\frac{N_s}{\binom{2r}{s}}.                        \tag{0.5}
\]

Thus \(x\) is a fractional matching saturating all \(W\) pattern vertices
and all \(W\) owner vertices while respecting unit capacity at every named
target. Its total weight is \(W\).

An integral matching of size \(W\) in this same configuration hypergraph is
exactly a choice of every owner once and one ordering per pattern which
uses \(N_s\) distinct named targets at each rank \(s\). The omitted
\(\binom{2r}{s}-N_s\) targets are then determined automatically; they need
not be fixed before the matching.

On a retained central band

\[
\mathcal I=\{r-b,\ldots,r-a-1\},\qquad
1\le a<b=o(r),                                           \tag{0.6}
\]

assume:

* every positive \(N_s\), \(s\in\mathcal I\), tends to infinity;
* no pattern contains two adjacent ranks of \(\mathcal I\); and
* only pattern, owner, and target vertices with target ranks in
  \(\mathcal I\) are included in the normalized pair ledger.

Then the maximum pair degree divided by the smaller positive incident
degree satisfies

\[
\rho_2\le
\max\left\{
\frac1W,\ 
\max_{s\in\mathcal I:N_s>0}\frac1{N_s},\
O(r^{-2})
\right\}.                                                \tag{0.7}
\]

For the optimal noncontiguous residual schedule,
\(N_s=\binom{2r}{s}-b_s\) is exponential uniformly on every standard
retained band and the first two terms are negligible. Hence

\[
\rho_2=O(r^{-2}),\qquad
K^2\rho_2=O(r^{-1})                                      \tag{0.8}
\]

when every pattern has size at most the optimal
\(d=O(\sqrt r)\), where \(K\le d+2\).

This is the exact post-rank-rounding subcritical configuration object. The
remaining obstruction is integral hypergraph matching/absorption together
with the collar and literal chronology.

There is also a sharp warning about the most direct integral rounding.
Fix any partition of the lower half of the Boolean lattice into \(W\)
saturated chains, each ending at a different rank-\(r\) owner.  Put

\[
 A(t)=\#\{i:R_i\ne\varnothing,\ \min R_i\le t\}.
\tag{0.9}
\]

The exact deficiency for assigning the patterns to those fixed chains is

\[
 \boxed{\delta_{\rm sat}(\mathcal R)
 =\max_{0\le t<r}
 \left(A(t)-\binom{2r}{t}\right)_+.}
\tag{0.10}
\]

In particular, if two consecutive residual ranks \(s,s+1\) are forbidden
from occurring in one pattern, then

\[
 \delta_{\rm sat}(\mathcal R)
 \ge N_s+N_{s+1}-\binom{2r}{s+1}.
\tag{0.11}
\]

For the optimal inventory \(N_j=\binom{2r}{j}-b_j\), this becomes

\[
 \delta_{\rm sat}(\mathcal R)
 \ge \binom{2r}{s}-b_s-b_{s+1}.
\tag{0.12}
\]

At any residual pair a distance \(O(\sqrt r)\) below the middle, the
right-hand side is \(\Theta(W)\), because the entire Ferrers boundary has
only \(O(r)=o(W)\) targets.  Thus the canonical fractional point can be
subcritical on the residual bank while *every* one-SCD or fixed saturated-
prechain rounding has linear deficiency.  Integral cross-chain splicing is
not optional.

## 1. Vertex degrees

For fixed \(i\), there are \(W r!\) labelled configurations
\((i,T,\pi)\). Equation (0.3) gives

\[
d_x(p_i)=Wr!\frac1{Wr!}=1.
\]

For fixed \(T\), there are \(W\) pattern choices and \(r!\) orders, so

\[
d_x(o_T)=Wr!\frac1{Wr!}=1.
\]

Fix \(S\in\binom{[2r]}s\). For one pattern containing rank \(s\), the
number of pairs \((T,\pi)\) whose rank-\(s\) prefix equals \(S\) is

\[
\binom{2r-s}{r-s}s!(r-s)!.
\]

Therefore its degree contribution from one such pattern is

\[
\frac{\binom{2r-s}{r-s}s!(r-s)!}{Wr!}
=\frac1{\binom{2r}{s}}.                                  \tag{1.1}
\]

There are \(N_s\) such patterns, proving (0.5). The hypothesis (0.1)
makes every target degree at most one.

Every configuration contains one pattern and one owner, so total edge
weight equals either sum in (0.4), namely \(W\).

## 2. Integral interpretation

Every configuration edge contains exactly one pattern vertex and one owner
vertex. A matching of size \(W\) therefore saturates both \(W\)-element
shores. For each scheduled occurrence \(s\in R_i\), its edge also contains
one named rank-\(s\) prefix. Hypergraph disjointness makes all these target
vertices distinct. Since rank \(s\) occurs in exactly \(N_s\) patterns, the
matching uses exactly \(N_s\) rank-\(s\) targets.

Conversely, any assignment of the patterns to distinct owners, together
with owner orderings whose scheduled prefixes are all distinct, gives
exactly these \(W\) disjoint configuration edges. This proves the integral
equivalence.

## 3. Exact pair ledger

All degrees below refer to the weights (0.3).

### 3.1 Pattern--owner

For fixed \(i,T\), all \(r!\) orders contribute, so

\[
d_x(p_i,o_T)=\frac1W.                                    \tag{3.1}
\]

Both endpoint degrees are one.

### 3.2 Pattern--target

If \(s\in R_i\), (1.1) gives

\[
d_x(p_i,S)=\frac1{\binom{2r}{s}}.                        \tag{3.2}
\]

Dividing by the target degree \(N_s/\binom{2r}{s}\) gives \(1/N_s\).
Dividing by the pattern degree gives an even smaller quantity on the
retained band.

### 3.3 Owner--target

If \(S\subseteq T\), every one of the \(N_s\) relevant patterns has
\(s!(r-s)!\) orders with prefix \(S\). Hence

\[
d_x(o_T,S)=\frac{N_s}{W\binom rs}.                       \tag{3.3}
\]

Using

\[
\frac{\binom{2r}{s}}{W\binom rs}
=\frac1{\binom{2r-s}{r-s}},                              \tag{3.4}
\]

the ratio of (3.3) to the target degree is the right side of (3.4).
The ratio to the owner degree is no larger, because
\(N_s\le\binom{2r}{s}\). On (0.6), \(r-s\ge a+1\); in
particular this is \(O(r^{-2})\) once \(a\ge1\).

### 3.4 Target--target

Two distinct target vertices occur together only if they form a flag
\(S\subset U\), of ranks \(s<t\), and one pattern contains both ranks.
Put

\[
N_{s,t}=\#\{i:s,t\in R_i\}.
\]

Uniform owner/order counting gives

\[
d_x(S,U)=
\frac{N_{s,t}}
{\binom{2r}{t}\binom ts}.                                \tag{3.5}
\]

Dividing by the degree of \(U\) gives

\[
\frac{d_x(S,U)}{d_x(U)}
=\frac{N_{s,t}}{N_t\binom ts}
\le\frac1{\binom ts}.                                    \tag{3.6}
\]

Using

\[
\binom{2r}{t}\binom ts
=\binom{2r}{s}\binom{2r-s}{t-s},
\]

division by the degree of \(S\) gives

\[
\frac{d_x(S,U)}{d_x(S)}
=\frac{N_{s,t}}{N_s\binom{2r-s}{t-s}}
\le\frac1{\binom{2r-s}{t-s}}.                            \tag{3.7}
\]

On the retained band, the nonadjacency condition forces \(t-s\ge2\).
Since \(s,t=r-o(r)\), both denominators in (3.6)--(3.7) are
\(\Omega(r^2)\).

Distinct patterns never share an edge. Distinct owners never share an
edge. Equations (3.1)--(3.7) exhaust every pair type, proving (0.7).

## 4. Application and scope

The equitable rank-decomposition theorem supplies exactly \(W\) patterns,
each of size at most \(d\), with the desired integral multiplicities and
no adjacent residual ranks. The present theorem shows that after that
rounding:

* pattern demand is exactly one;
* owner demand is exactly one;
* named-target capacities are respected fractionally;
* every residual pair codegree is subcritical on the retained band; and
* the target subset sent to the boundary may be chosen by the eventual
  integral matching rather than frozen beforehand.

The theorem does not prove a growing-uniformity matching theorem applicable
to this configuration hypergraph. It also does not control target vertices
in the macroscopic collar, prove that the omitted targets form literal
Ferrers boundary chains, serialize the selected flags into one sliding
word, or preserve the upper/router/regeneration rows.

The exact next lower theorem is therefore:

\[
\boxed{\text{round this subcritical residual configuration matching while
coordinating its omitted targets with an integral collar absorber}.}
\]

## 5. Adaptive boundary is equivalent to configuration packing

The fixed-boundary configuration hypergraph in the rank-law theorem first
chooses families \(B_s\subseteq\binom{[2r]}s\) and forbids them.  For the
integral question that order of quantifiers is unnecessary.

### Proposition 5.1 (adaptive-boundary equivalence)

An integral matching of size \(W\) in the full configuration hypergraph
(0.2) is equivalent to an exact named-target flag realization for some
boundary families \(B_s\) of sizes

\[
 |B_s|=\binom{2r}{s}-N_s.
\tag{5.1}
\]

### Proof

A size-\(W\) matching uses every pattern and every owner once.  At rank
\(s\), exactly the \(N_s\) patterns containing \(s\) contribute a target.
Matching disjointness makes those \(N_s\) targets distinct.  Declare the
complementary rank-\(s\) targets to be \(B_s\).  This gives (5.1) and an
exact realization outside the boundary.

Conversely, a realization with any such boundary uses one configuration
for every pattern, uses every owner once, and repeats no nonboundary target.
Those configurations are a size-(W) matching in the full hypergraph.
\(\square\)

The proposition does not say that the adaptively omitted targets form the
literal triangular Ferrers boundary.  That is a later physical condition.
It does show that prescribing their names before solving the owner flags is
strictly unnecessary at the static configuration stage.

## 6. Exact fixed-saturated-chain criterion

Let

\[
 \mathcal P_{\le r}=\{S\subseteq[2r]:|S|\le r\}.
\]

Fix a partition \(\mathscr D\) of \(\mathcal P_{\le r}\) into \(W\)
inclusion chains, one ending at each rank-\(r\) owner, and assume every
chain is saturated between its minimum and its owner.  A symmetric-chain
decomposition restricted to the lower half is the canonical example.  For
\(C\in\mathscr D\), write \(h(C)\) for the rank of its minimum.

A **\(\mathscr D\)-restricted realization** assigns each pattern to one
chain and uses the unique member of that chain at every scheduled rank.
Empty patterns may be assigned to any unused chain.

### Lemma 6.1 (chain-start census)

For every \(0\le t\le r\),

\[
 \#\{C\in\mathscr D:h(C)\le t\}=\binom{2r}{t}.
\tag{6.1}
\]

### Proof

A saturated chain ending at rank \(r\) contains a rank-\(t\) member exactly
when its minimum rank is at most \(t\).  The chains partition all
rank-\(t\) sets, and each chain contains at most one of them.  Counting the
rank-(t) layer proves (6.1).  \(\square\)

### Theorem 6.2 (exact saturated-prechain deficiency)

For the fixed partition \(\mathscr D\), the maximum number of patterns
which can be assigned to distinct compatible chains is

\[
 W-\delta_{\rm sat}(\mathcal R),
\]

where \(\delta_{\rm sat}\) is (0.10).  Hence a
\(\mathscr D\)-restricted exact realization exists if and only if

\[
 A(t)\le\binom{2r}{t}\qquad(0\le t<r).
\tag{6.2}
\]

Whenever it exists, all scheduled named targets are automatically distinct
and nested ownerwise; the omitted rank-(s) targets automatically form an
adaptive boundary of the required size.

### Proof

Join pattern \(i\) to chain \(C\) exactly when either \(R_i\) is empty or

\[
 h(C)\le \min R_i.
\tag{6.3}
\]

Condition (6.3) is necessary and sufficient for the saturated chain to
contain every scheduled rank of the pattern.  The nonempty-pattern
neighbourhoods are nested threshold sets.  The patterns with deadline at
most \(t\) have neighbourhood precisely contained in the
\(\binom{2r}{t}\) chains counted by Lemma 6.1.  Therefore their Hall
deficiency is \(A(t)-\binom{2r}{t}\).

Conversely, for any family \(X\) of nonempty patterns, put
\(t=\max_{i\in X}\min R_i\).  Its neighbourhood is the set of chains with
minimum rank at most \(t\), while

\[
 |X|\le A(t).
\]

A family containing an empty pattern has all \(W\) chains as its
neighbourhood and has nonpositive deficiency.  Thus the maximum Hall
deficiency over *all* pattern families is exactly (0.10).  The deficiency
form of Hall's theorem gives maximum matching size
\(W-\delta_{\rm sat}\), proving the formula and (6.2).

For a perfect assignment, different chains are disjoint.  Their selected
rank members are therefore distinct, and the selected members of one chain
are nested.  At rank \(s\) there are exactly \(N_s\) of them, so the
complement has the size asserted in Proposition 5.1.  \(\square\)

This theorem is independent of which symmetric-chain decomposition is
chosen: the start census (6.1) is forced by the Boolean rank sizes.

## 7. Consecutive residual ranks force linear prechain deficiency

### Corollary 7.1 (single-SCD obstruction)

Suppose \(s,s+1\) are residual ranks and the schedule forbids their joint
occurrence in one pattern.  Then (0.11) holds for every fixed saturated
prechainization \(\mathscr D\).

For the optimal inventory \(N_j=\binom{2r}{j}-b_j\), (0.12) follows.  If
\(r-s=O(\sqrt r)\) and \(\sum_jb_j=O(r)\), then

\[
 \delta_{\rm sat}(\mathcal R)=\Omega(W).
\tag{7.1}
\]

### Proof

Let \(I_j=\{i:j\in R_i\}\).  Residual nonadjacency makes \(I_s\) and
\(I_{s+1}\) disjoint.  Every pattern in their union has minimum rank at
most \(s+1\).  Hence

\[
 A(s+1)\ge |I_s|+|I_{s+1}|=N_s+N_{s+1}.
\]

Insert this in (0.10) to obtain (0.11).  Substitution of the optimal
inventory gives (0.12).

When (r-s=O(\sqrt r)), the local central-binomial estimate gives

\[
 \binom{2r}{s}=\Theta\!\left(\binom{2r}{r}\right)=\Theta(W).
\]

The triangular boundary has at most \(\binom{d+1}{2}=O(r)=o(W)\) cells,
so \(b_s+b_{s+1}=o(W)\).  Equation (0.12) proves (7.1).  \(\square\)

The obstruction is deliberately scoped.  It does not refute an integral
configuration matching whose flags are chosen jointly.  It proves that
one cannot obtain such a matching by assigning the patterns to one frozen
SCD, or to any other frozen saturated owner-chain partition.  A successful
proof must use genuinely skipping chains or make \(\Theta(W)\) cross-chain
splices before the nonadjacent residual schedule can be realized.
