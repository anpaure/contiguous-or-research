# Audit of the private-phase bridge cuts and the two-guard root

Date: 2026-08-01  
Status: unconditional necessary cut family and unconditional rooted
obstruction.  The unrooted inclusion of the triangular vector in the full
private-pattern cone remains open.

## 0. Verdict

Let `n=d+1`, let

\[
 q_s=\frac{\binom ks-b_s}{W},\qquad
 r=\lceil k/2\rceil,\qquad W=\binom kr,
\]

and use deficiency coordinates `t=r-s`.  Reflection identifies the
unpunctured marginal with the survival function of the conditioned bridge
maximum `M`, but it does **not** construct the joint cyclic interval
addresses required by the private-pattern cone.

The exact consequence is instead a family of threshold-overflow cuts.  Its
first row is sharp and refutes the proposed joint root condition on every
odd instance with an extra coordinate.  In fact, when `k` is odd and
`d<r-1`, the ordered-singleton root is absent from every exact triangular
marked-trace circulation, not only from the private-pattern subclass.

The local two-guard address algebra remains correct.  At repeated
fractional scale, connected positive support on the four incident guard
edges is enough: a spare-copy contraction gives an Euler tour respecting
both same-guard passages.  Each passage uses two distinct trace edges of
the same owner, so preserving it in a one-edge-per-owner rounding is in
fact impossible within this literal address geometry.

No finite computation is used below.

Here “private-pattern cone” means the coordinatewise downward closure of
`conv{g(P)}`.  Every generator has total mass `d`, so if `sum_s q_s<d`, the
vector `q` cannot literally lie in that convex hull; it can only lie below
one of its points.

## 1. Exact threshold-overflow identity

Fix one private-pattern configuration on `Z_n`.  For a cyclic interval
`J`, put

\[
 N_P(J)=\#\{x:P_x\subseteq J\}.
\]

If `J` is the complement of a proper suffix interval, its deficiency is

\[
                         D_P(J)=|J|+N_P(J).          \tag{1.1}
\]

Write the deficiency histogram as

\[
                         h_t(P)=g_{r-t}(P).
\]

For `1<=a<=d`, define

\[
 Z_a(P)=\#\{J:\ J\text{ is cyclic},\ 1\le |J|\le a,
                         \ D_P(J)>a\}.              \tag{1.2}
\]

### Theorem 1.1 (private threshold cuts)

For every configuration `P`,

\[
 \boxed{
 a-\sum_{t=1}^{a}h_t(P)=\frac{Z_a(P)}n.}            \tag{1.3}
\]

Consequently, if a probability measure on configurations has mean profile
`gbar` with `gbar_s>=q_s` coordinatewise, then

\[
 \boxed{
 \mathbb E Z_a
 \le n\left(a-\sum_{t=1}^{a}q_{r-t}\right).}        \tag{1.4}
\]

#### Proof

There are exactly `n` cyclic intervals of each length.  A proper interval
has deficiency at most `a` only if its complement length is at most `a`.
Hence

\[
 n\sum_{t\le a}h_t(P)
  =\#\{J:1\le |J|\le a,\ D_P(J)\le a\}
  =na-Z_a(P),
\]

which is (1.3).  Average and use `gbar_(r-t)>=q_(r-t)` to obtain (1.4).
\(\square\)

This cut family is stronger than the first-moment concavity test: it
controls every initial deficiency threshold and retains the literal
containment overload `N_P(J)`.

## 2. Bridge-maximum form of every cut

Let `M` be the maximum of a length-`k` simple walk conditioned to end at
`k mod 2`.  Suffix reflection gives

\[
 \Pr(M\ge t)=\frac{\binom{k}{r-t}}W.                \tag{2.1}
\]

Put

\[
                         B_a=\sum_{t=1}^{a}b_{r-t}.
\]

Substituting the triangular profile into (1.4) gives the exact bridge form

\[
 \boxed{
 \mathbb E Z_a
 \le n\left(\mathbb E(a-M)_+ +\frac{B_a}{W}\right).} \tag{2.2}
\]

Indeed,

\[
 \sum_{t=1}^{a}\Pr(M\ge t)=\mathbb E\min(M,a),
\]

so the difference from `a` is `E(a-M)_+`.

Equation (2.2) is the complete implication furnished by the
bridge-maximum marginal alone.  It is a necessary budget on overloaded
cyclic intervals.  It supplies neither their occurrence patterns nor a
common coloured address system, so it is not a proof that `q` belongs to
the private-pattern cone.

## 3. The saturated top face

Let

\[
 c_1(P)=\#\{i\in\mathbb Z_n:\text{ some extra coordinate has }
                                      P_x=\{i\}\}.  \tag{3.1}
\]

### Corollary 3.1 (exact singleton-pattern face)

Every private configuration satisfies

\[
 \boxed{g_{r-1}(P)=1-\frac{c_1(P)}n.}               \tag{3.2}
\]

#### Proof

Deficiency one forces `|J|=1`.  For `J={i}`, (1.1) equals one exactly when
no extra pattern is the singleton `{i}`.  There are `n-c_1(P)` such
phases.  Divide by `n`.  Equivalently, (3.2) is (1.3) at `a=1`.
\(\square\)

Assume now that `k=2r-1` is odd and `d<r-1`.  The triangular boundary board
uses only ranks at most `d`, so `b_(r-1)=0`, while

\[
 q_{r-1}=\frac{\binom{2r-1}{r-1}}{\binom{2r-1}{r}}=1. \tag{3.3}
\]

Thus any mean private profile dominating `q` has `E c_1=0`; every positive
configuration has no singleton extra-coordinate pattern.

This is exactly the bridge endpoint obstruction: an odd bridge ends at
one, hence `Pr(M>=1)=1` and the first threshold budget in (2.2) is zero.

For completeness, every actual odd instance `k>=7` has `d<r-1`.  If
`r=4`, then `Lambda/W=63/35<2=r-2`.  If `r>=5`, monotonicity of the bridge
survival function gives

\[
 \frac\Lambda W
 \le 1+(r-2)\frac{r-1}{r+1}\le r-2.
\]

Since `d<=ceil(Lambda/W)`, this proves `d<=r-2`.

## 4. A singleton root forces the forbidden pattern

Let

\[
 v=(\{f_1\},\ldots,\{f_d\}),\qquad F=\{f_1,\ldots,f_d\}.
\]

### Theorem 4.1 (odd rooted private-cone obstruction)

Suppose `R=r-d-1>0`.  A private period-`n` configuration containing the
literal traversal

\[
                       G,\{f_1\},\ldots,\{f_d\},G   \tag{4.1}
\]

has `c_1(P)=1` and

\[
                         g_{r-1}(P)=\frac d{d+1}.    \tag{4.2}
\]

Consequently, for odd `k` no positive mass on such a root configuration
can coexist with domination of the exact triangular profile.  In
particular, the proposed positive two-guard rooted strengthening is false
for every odd `k>=7`.

#### Proof

The `d` singleton letters in (4.1) occupy all but one private phase.  Every
extra coordinate must avoid those phases, and its phase pattern is
nonempty.  Hence every one of the `R` extras has the singleton pattern
consisting of the remaining guard phase.  Exactly one phase is counted by
`c_1`, and (4.2) follows from (3.2).  Equations (3.2)--(3.3) then exclude
positive mass. \(\square\)

The exception `R=0` is genuine: there is no extra coordinate to create a
singleton pattern.  It does not rescue the claimed all-`k` rooted route.

For even `k=2r` with `b_(r-1)=0`,

\[
                         q_{r-1}=\frac r{r+1}.
\]

If `alpha` is the total probability of private configurations of form
(4.1), then (3.2) gives the exact necessary budget

\[
                         \alpha\le\frac{d+1}{r+1}.   \tag{4.3}
\]

More generally, the rooted star has

\[
 Z_a^\star=\sum_{\ell=\max(1,a-R+1)}^a\ell,
\]

and (2.2) gives

\[
 \alpha Z_a^\star
 \le n\left(\mathbb E(a-M)_+ +\frac{B_a}{W}\right) \tag{4.4}
\]

for every `a`.  These are necessary histogram budgets, not a construction.

## 5. The obstruction holds in the full marked-trace LP

The preceding no-go is not an artefact of private patterns.

### Theorem 5.1 (saturated-rank root exclusion)

In any triangular marked-trace circulation with `q_(r-1)=1`, every
positive marked atom contains a marked rank-`(r-1)` proper suffix.  If
`d<r-1`, the circulation has zero incoming and outgoing mass at every
ordered-singleton state `v` of (4.1).

#### Proof

The selected suffix cells of one atom are nested and required to be
distinct.  Hence an atom contains at most one marked cell of any fixed
rank.  The owner equations give total atom mass `W`, whereas the
rank-`(r-1)` histogram has total mass `Wq_(r-1)=W`.  Saturation forces every
positive atom to attain this per-atom upper bound.

An edge entering `v` ends in the letters
`{f_1},...,{f_d}`.  All of its proper suffix unions have ranks at most
`d<r-1`, so no marked atom on that edge can attain the bound.  Its incoming
weight is zero.  Literal de Bruijn balance then makes the outgoing weight
zero as well. \(\square\)

Therefore the odd obstruction cannot be repaired by leaving the private
subcone while retaining this root state.  A viable architecture must
puncture the saturated top face, decouple the root absorber from the exact
triangular circulation, or use a root state already exposing a
rank-`(r-1)` suffix.

## 6. Exact two-guard passage semantics

For fixed `F` and fixed rank-`r` owner `T`, the guard is uniquely
`G=T\setminus F`.  Thus distinct guards `G_1!=G_3` lie in distinct owner
fibres, although their incident trace edges share the same literal state
`v`.

The inclusion-chain argument in the reduction correctly proves that the
two exact equal-rank banks require two visits.  One occurrence cannot
supply them, even by using longer exterior intervals with the prescribed
fixed endpoint.

There is one additional Euler detail.

### Lemma 6.1 (spare-copy guarded Euler tour)

Let `x` be a rational balanced circulation whose positive directed support
is weakly connected.  Suppose the incoming and outgoing guard edges

\[
 e_i^-=(G_i,\{f_1\},\ldots,\{f_d\}),\qquad
 e_i^+=(\{f_1\},\ldots,\{f_d\},G_i)\qquad(i=1,3)
\]

all have positive weight.  Some integer multiple of `x` has one Euler tour
in which `e_i^-` is immediately followed by `e_i^+` for both guards.

#### Proof

Clear denominators and multiply further until every positive support edge
has at least one unused copy after reserving one copy of each prescribed
edge.  Replace each reserved two-edge passage `e_i^-e_i^+` by one macroedge
from the tail of `e_i^-` to the head of `e_i^+`.  Removing one incoming and
one outgoing edge at `v` preserves balance, as does the macroedge
replacement at its other endpoints.  One untouched copy of every support
edge remains, so the contracted multigraph is still weakly connected.  It
therefore has an Euler circuit.  Expanding the two macroedges gives the
claimed guarded visits. \(\square\)

At minimum multiplicity, the two guard cycles may form a figure eight and
every Euler tour may cross-pair the guards.  Lemma 6.1 explains why this is
not a fractional obstruction: spare copies restore both prescribed
passages.  It is nevertheless a genuine one-copy warning.  First-order
edge flow does not itself record the transition pairing, and the lemma does
not produce one-owner-per-colour Euler rounding.

### Corollary 6.2 (literal one-copy owner obstruction)

No owner-perfect integral marked trace can contain even one complete
immediate same-guard passage `G,v,G`.

#### Proof

The two incident edge words `e^-` and `e^+` are distinct, but both have
owner

\[
                              T=F\cup G.
\]

An integral solution of the owner equation selects exactly one trace edge
of owner `T`.  It cannot select both edges required by the passage.
\(\square\)

For two guards, the same duplication occurs independently in the two
owners `F union G_1` and `F union G_3`.  Thus Lemma 6.1 is strictly a
repeated fractional statement.  A physical one-copy construction must put
one side in an auxiliary boundary/uncoloured connector layer, puncture
owner exactness, or realize the target banks by a different address
geometry.

Only one visit can be chosen as the global cut/root of a linearized tour;
the other is a protected internal return.  Both occurrence address banks
remain literal.

## 7. Proof-safe frontier

The exact conclusions are:

1. the bridge maximum yields the threshold cuts (2.2), not an all-`d`
   private-cone construction;
2. unrooted membership of the triangular vector in the full
   private-pattern cone remains open;
3. the joint singleton-root/private-cone target is impossible throughout
   the odd family with `R>0`, and the full marked-trace LP excludes the root
   whenever `q_(r-1)=1` and `d<r-1`;
4. two distinct guards mean two owner fibres and two visits; connected
   positive two-sided throughput is sufficient only after denominator
   amplification, while the literal passage is categorically incompatible
   with one-edge-per-owner rounding; and
5. common-cap compatibility, connected unrooted support, and a different
   one-copy root/address realization remain separate open gates.
