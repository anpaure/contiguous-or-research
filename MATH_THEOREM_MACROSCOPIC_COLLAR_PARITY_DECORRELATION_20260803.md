# Macroscopic-collar parity decorrelation for Boolean flag atoms

**Date:** 2026-08-03  
**Status:** unconditional weighted residual-law theorem and exact collar
chainization.  No computation is used.  The two constructions are not yet
proved compatible in one owner-chain factor, and this note does not invoke a
fixed-uniformity nibble diagonally or prove an `o(W)` integral matching.

## 0. Outcome

Put

\[
 k=2r,\qquad W={2r\choose r},\qquad
 p_s={{2r\choose s}\over W}\quad(1\le s<r).
\]

The symmetric uniform-order atom law is on a critical collision surface if
it retains the ranks immediately below `r`: adjacent retained ranks force
normalized pair codegree `(1-o(1))/r`.  This note proves that the critical
surface is confined to a macroscopic central collar.

Fix any constant

\[
 c>\sqrt{\log 2},\qquad a=\lceil c\sqrt r\rceil,
 \qquad b=\lceil\sqrt{6r\log r}\rceil .                 \tag{0.1}
\]

Remove the central collar of strict-lower ranks

\[
 r-a,\ldots,r-1                                           \tag{0.2}
\]

and discard the negligible far tail of ranks below `r-b`.  On the retained
band

\[
 \mathcal I=\{r-b,\ldots,r-a-1\},                         \tag{0.3}
\]

there is an explicit symmetric owner-flag law with all of the following
properties.

1. Every retained named target has weighted degree `1-o(1)`, uniformly, and
   the total missing retained target mass is `o(W)`.
2. Every atom uses ranks of only one parity, so no two adjacent ranks occur.
3. If `K` is the maximum atom cardinality including its owner, then

   \[
   K\le d+1=O(\sqrt r).                                   \tag{0.4}
   \]

4. If `rho_2` is maximum pair codegree divided by the smaller incident
   degree, over supported positive-degree vertices, then

   \[
   \rho_2=O(r^{-2}),\qquad K^2\rho_2=O(r^{-1})=o(1).       \tag{0.5}
   \]

5. The discarded far tail has only `o(W)` named targets.

Thus a collar of width just beyond `sqrt(log 2) sqrt(r)` changes the
residual flag law from the critical scale `K^2 rho_2=Theta(1)` to a genuinely
subcritical pair-collision scale.  This is an object-specific improvement,
not an application of a black-box growing-uniformity matching theorem.

Independently, the entire collar (0.2) has an exact partition into inclusion
chains ending at distinct rank-`r` owners, with at most `a` collar targets per
chain.  The remaining open gate is to choose that collar partition and the
residual atoms **jointly**, so that each residual flag lies below the bottom
of its assigned collar chain and respects the residual capacity of that
owner.

## 1. The parity law

For `j=r-s`, the central binomial ratio is

\[
 p_{r-j}=\prod_{i=0}^{j-1}{r-i\over r+i+1}.               \tag{1.1}
\]

Since

\[
 \log {r-i\over r+i+1}
 \le -{2i+1\over r+i+1},
\]

we have, uniformly for `1<=j<=r`,

\[
 p_{r-j}\le \exp\left(-{j^2\over r+j}\right)
             \le \exp\left(-{j^2\over2r}\right).         \tag{1.2}
\]

For `j>=a+1`, (1.1), or the standard local central-binomial
asymptotic, gives

\[
 \max_{s\in\mathcal I}p_s
 \le e^{-c^2+o(1)}<\frac12                                \tag{1.3}
\]

for all sufficiently large `r`.

Choose a fair parity bit `epsilon in {0,1}`.  Conditional on `epsilon`, for
each `s in mathcal I` with `s=epsilon (mod 2)`, retain `s` independently with
probability `2p_s`; retain no rank of the other parity.  Denote the resulting
random rank set by `R_0`.  Equation (1.3) makes every stated probability legal,
and

\[
 \Pr(s\in R_0)=p_s\qquad(s\in\mathcal I).                 \tag{1.4}
\]

The unconditioned size must now be capped, because an owner-chain atom may
carry at most `d` targets.  Conditional on either parity, `|R_0|` is a sum of
independent Bernoulli variables.  Its mean is at most

\[
 2\sum_{j\ge a}p_{r-j}
 =\left(2\int_c^\infty e^{-x^2}\,dx+o(1)\right)\sqrt r.    \tag{1.5}
\]

The standard lower-bound ledger gives

\[
 d=\left({\sqrt\pi\over2}+o(1)\right)\sqrt r.             \tag{1.6}
\]

Mills' inequality and `c>sqrt(log 2)` give

\[
 2\int_c^\infty e^{-x^2}\,dx
 \le {e^{-c^2}\over c}
 <{1\over2c}< {\sqrt\pi\over2}.                           \tag{1.7}
\]

Therefore the conditional mean in (1.5) is at most `theta d` for some fixed
`theta<1`.  The Chernoff bound for a Poisson-binomial sum gives

\[
 \Pr(|R_0|>d)\le e^{-\kappa\sqrt r}                        \tag{1.8}
\]

for a constant `kappa=kappa(c)>0`.  Define

\[
 R=\begin{cases}R_0,&|R_0|\le d,\\
                  \varnothing,&|R_0|>d.
   \end{cases}                                             \tag{1.9}
\]

For every owner `T in binom([2r],r)`, choose a uniform ordering of `T` and
take the initial subsets at the ranks in `R`.  Average over all owners,
orders, parities and Bernoulli choices, giving total weight one at every
owner.

The exact degree formula for uniform-order flag atoms is

\[
 d_x(S)={q_s\over p_s}\qquad(|S|=s),                       \tag{1.10}
\]

where `q_s=Pr(s in R)`.  Hence (1.4) gives

\[
 0\le p_s-q_s\le e^{-\kappa\sqrt r}.                      \tag{1.11}
\]

The local central-binomial expansion, uniformly for `j<=b`, gives

\[
 p_{r-j}=\exp(-j^2/r+o(1))\ge r^{-7}                       \tag{1.12}
\]

for all large `r`.  Thus (1.11) is `o(p_s)` uniformly on `mathcal I`, and

\[
 d_x(S)=1-o(1)                                             \tag{1.13}
\]

uniformly for every retained target.  Moreover,

\[
 \sum_{s\in\mathcal I}(p_s-q_s)
 =\mathbb E\bigl[|R_0|1_{\{|R_0|>d\}}\bigr]
 \le b e^{-\kappa\sqrt r}=o(1).                           \tag{1.14}
\]

Every supported rank set has one parity and, by (1.9), size at most `d`.
Therefore

\[
 K\le d+1=O(\sqrt r),                                     \tag{1.15}
\]

where the extra one is the owner vertex.

## 2. Exact pair codegrees

Before the cap (1.9), the joint rank marginal at distinct retained ranks is

\[
 \eta^0_{s,t}=\begin{cases}
 2p_sp_t,&s\equiv t\pmod2,\\
 0,&s\not\equiv t\pmod2.
 \end{cases}                                               \tag{2.1}
\]

After the cap, `eta_{s,t}<=eta^0_{s,t}` and `q_s=(1-o(1))p_s`
uniformly.

Two target vertices have nonzero codegree only when they form a flag
`S subset U`.  Their degrees are both `1-o(1)`, uniformly.  If their codegree is nonzero,
then `g=t-s>=2`, and the uniform-order flag formula gives either of the
equal expressions

\[
 {d_x(S,U)\over d_x(U)}
 \le{(2+o(1))p_s\over {t\choose s}},
 \qquad
 {d_x(S,U)\over d_x(S)}
 \le{(2+o(1))p_t\over {2r-s\choose t-s}}.                 \tag{2.2}
\]

For large `r`, every retained rank is at least `r-b>=r/2`, while
`2<=g<=b-a<r/4`.  Hence

\[
 {t\choose g}\ge {t\choose2}=\Omega(r^2),
 \qquad
 {2r-s\choose g}\ge {2r-s\choose2}=\Omega(r^2).           \tag{2.3}
\]

Since `p_s,p_t<=1`, (2.2)--(2.3) show

\[
 {d_x(S,U)\over\min(d_x(S),d_x(U))}=O(r^{-2}).             \tag{2.4}
\]

For an owner-target pair with `S subset T`,

\[
 d_x(o_T,S)={q_s\over {r\choose s}}
 \le{p_s\over {r\choose s}}
 ={1\over {2r-s\choose r-s}}.                             \tag{2.5}
\]

Here `r-s>=a+1>=2` and `r-s=o(r)`, so the denominator in (2.5) is at least
`binom(r,2)` for large `r`.  Thus owner-target pairs also have codegree
`O(r^-2)`.  Distinct owners never share an atom.  Equations (1.6), (2.4)
and (2.5) prove

\[
 \rho_2=O(r^{-2}).                                         \tag{2.6}
\]

Combining (1.7) and (2.6) proves (0.5).

The higher codegrees retain the same laminar form.  A supported target
collection must be a flag whose ranks all have one parity.  Before the cap,
for distinct `s_1<...<s_j` its joint rank marginal is

\[
 \eta^0_{s_1,\ldots,s_j}=2^{j-1}\prod_{i=1}^j p_{s_i};     \tag{2.7}
\]

the cap only decreases this joint marginal.  This domination formula is
available to any future flag-specific matching or absorption argument; no
independence assertion is being made about overlapping named flags.

## 3. The discarded far tail is negligible

By (1.2), for `j>b`,

\[
 p_{r-j}\le e^{-b^2/(2r)}\le r^{-3}.                      \tag{3.1}
\]

There are fewer than `r` such ranks, so

\[
 \sum_{s<r-b}p_s\le r^{-2}=o(1).                           \tag{3.2}
\]

Multiplying by `W`, the number of named strict-lower targets in the far
tail is `o(W)`.  Equation (1.14) shows that the capacity cap loses another
`o(W)` total named-target load.

## 4. Exact chainization of the central collar

For each `s<r`, consider the inclusion graph between
`binom([2r],s)` and `binom([2r],s+1)`.  It is biregular.  If `X` is a
family of rank-`s` sets, double-counting the inclusion edges incident with
`X` gives

\[
 (2r-s)|X|\le(s+1)|N(X)|.                                 \tag{4.1}
\]

For `s<=r-1`, `2r-s>=s+1`, and hence `|N(X)|>=|X|`.  Hall's theorem gives a
matching which saturates the entire rank-`s` shore.

Choose one such matching independently between every consecutive pair of
ranks

\[
 r-a,r-a+1,\ldots,r.                                      \tag{4.2}
\]

Orient every matched edge upward.  Every nonmiddle collar vertex has one
outgoing edge, and every vertex has at most one incoming edge.  Rank strictly
increases, so the union is a vertex-disjoint family of directed paths.
Every collar target lies on exactly one path, every path ends at a distinct
rank-`r` owner, and a path contains at most one vertex at each of the `a`
strict-lower collar ranks.  Adding empty paths at the unused middle owners
therefore gives exactly `W` owner-indexed chains, each containing at most `a`
collar targets.

This proves exact collar chainization without symmetry, randomness or an
asymptotic matching theorem.

## 5. The remaining collar-extension gate

Theorems in Sections 1--3 and Section 4 cannot simply be superposed.  Let
`B_T` be the bottom vertex of the collar path ending at owner `T` (and put
`B_T=T` for an empty collar path), and let `ell_T` be the number of collar
targets on that path.  A residual flag assigned to `T` must satisfy both

\[
 \max R_T\subseteq B_T,
 \qquad |R_T|\le d-\ell_T.                                \tag{5.1}
\]

The parity law only enforces containment in `T` and the unconditioned
capacity bound (1.7); it does not enforce (5.1).  Conversely, choosing the
collar matchings first destroys the transitive owner symmetry used in the
degree ledger (1.5)--(2.7).

Accordingly, the exact next static statement is:

> **Macroscopic-collar extension theorem.**  Choose the adjacent-rank
> collar matchings and a residual parity-separated owner-flag matching
> jointly so that (5.1) holds, while leaving `o(W)` named residual targets
> uncovered.

Proving this theorem would settle the static anchored-chain deletion target
`gamma_d(2r)=o(W)`.  It would still leave the sliding suffix cocycle,
literal interval closure, upper coverage and regeneration.  The present
note proves neither this extension theorem nor an integral residual
matching; it identifies a residual law in which the former forced
`pi/4` pair-collision barrier has disappeared.

## 6. Scope

The conclusions are exactly these.

* A central collar of width slightly above `sqrt(log 2) sqrt(r)` is enough
  to support an exact residual-marginal law with no adjacent retained ranks.
* The residual law obeys the owner capacity `d`, has only `o(W)` fractional
  target defect, has `K^2 rho_2=o(1)`, and has an explicit all-flag ledger.
* The central collar itself has an exact owner-chain partition.
* Compatibility of the two pieces is open.

In particular, this note does not apply a fixed-`K` Pippenger theorem along
a growing sequence, does not satisfy the exponential hypotheses of the ABKV
growing-rank theorem, and does not claim that pair-codegree control alone
implies the required `o(W)` leave.
