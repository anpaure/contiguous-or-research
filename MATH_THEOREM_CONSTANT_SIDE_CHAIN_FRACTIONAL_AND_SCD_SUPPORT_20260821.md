# Constant-side band chains: an exact integral product-SCD cover

**Status (2026-08-21).** Every assertion below is proved.  In the abstract
two-block problem, one token is attached to each middle `b`-set and may run
for `H` steps using additions from only one side.  A product of two
symmetric-chain decompositions gives one fixed integral side and one full
`H`-chain for every middle source which together cover **every**
central target at **every** offset `q<=H`.  Thus the abstract row/column
coinstantiation problem has an exact integral solution; when `H=o(b)`, only
exponentially small split tails are omitted.

There is also an exact simultaneous fractional assignment which realizes the
previously computed physical endpoint capacity `E_(q,s)` and, for
`H=Theta(sqrt(b log b))`, hence has aggregate fractional deficit `o(W_b)`.
These are labelled Boolean-
containment statements, not a cyclic-factor/order or serialized-atom lift.
No coefficient-one construction is claimed.

## 1. The abstract constant-side chain problem

Let `A,B` be disjoint `b`-sets and let `1<=H<b/2`.  A middle source is a
set `U subset A union B` with `|U|=b`.  An **all-`A` `H`-chain** from `U`
is determined by distinct elements

\[
 (a_1,\ldots,a_H)\in(A\setminus U)_{\ne}^{H}
\]

and visits `U union {a_1,...,a_q}` at offset `q`; all-`B` chains are
defined symmetrically.  A fractional assignment puts nonnegative weights on
these full chains, with total weight at most one at every source.  The load
of a target is the total weight of chains which visit it.  Because weights
are assigned to full `H`-chains, all offsets use one common law; there is no
rankwise resampling.

Write

\[
 C_j={b\choose j},\qquad W_b={2b\choose b}.
\]

At offset `q`, identify a target of split `s` with `(X,Y)`, where `X` is its
`s`-element `A` part and `Y` is the complement of its `B` part, so

\[
 |X|=s,\qquad |Y|=t=s-q,qquad P_{q,s}=C_sC_t.       \tag{1.1}
\]

An all-`A` predecessor has payload split `t`; an all-`B` predecessor has
payload split `s`.

## 2. Exact simultaneous fractional chain laws

### Theorem 2.1 (unrestricted half--half law)

For every middle source of split `r` with `H<=r<=b-H`, put weight `1/2`
uniformly on all ordered all-`A` `H`-chains and weight `1/2` uniformly on
all ordered all-`B` `H`-chains.  Then every target with

\[
 1\le q\le H,\qquad H\le t=s-q,qquad s\le b-H       \tag{2.1}
\]

has load

\[
 \boxed{\lambda_{q,s}={1\over2}{C_t\over C_s}
                    +{1\over2}{C_s\over C_t}\ge1.} \tag{2.2}
\]

#### Proof

Fix a target `(X,Y)`.  It has `binom(s,q)` all-`A` predecessors.  From any
one, the first `q` entries of a uniform ordered `H`-tuple have a prescribed
unordered set with probability `1/binom(b-t,q)`.  Therefore its all-`A`
load is

\[
 {1\over2}{\binom{s}{q}\over\binom{b-t}{q}}
 ={1\over2}{C_t\over C_s}.                          \tag{2.3}
\]

The symmetric all-`B` calculation gives

\[
 {1\over2}{\binom{b+q-s}{q}\over\binom{s}{q}}
 ={1\over2}{C_s\over C_t}.                          \tag{2.4}
\]

Their sum is at least one by AM--GM.  Conditions (2.1) ensure that every
predecessor used above has at least `H` missing elements on the chosen side.
The weights are on full chains, so the calculation holds simultaneously for
all `q<=H`.  \(\square\)

If `H=o(b)`, the total mass over `q<=H` of the target profiles excluded by
(2.1) is `e^{-Omega(b)}W_b`: one binomial factor has rank at most `H+O(H)`
from an edge while `W_b=Theta(4^b/sqrt b)`, and the extra factor `H` is
subexponential.

### Theorem 2.2 (physical constant-origin weights)

For a source of split `r` in the same central range, define

\[
 \alpha_r={r-H+1\over b},\qquad
 \beta_r={b-r-H+1\over b}.                          \tag{2.5}
\]

Put total weight `alpha_r` uniformly on its all-`A` full chains and total
weight `beta_r` uniformly on its all-`B` full chains.  This is feasible
because

\[
 \alpha_r+\beta_r=1-{2(H-1)\over b}\le1.            \tag{2.6}
\]

Every admissible target has the exact load

\[
 \boxed{
 \lambda^{\rm phys}_{q,s}
 =\alpha_t{C_t\over C_s}+\beta_s{C_s\over C_t}.}    \tag{2.7}
\]

Equivalently,

\[
 P_{q,s}\lambda^{\rm phys}_{q,s}
 ={1\over b}\left[
 (b-s-H+1)C_s^2+(s-q-H+1)C_{s-q}^2\right]
 =E_{q,s}.                                          \tag{2.8}
\]

Thus, for `H=Theta(sqrt(b log b))`, the constant-origin capacity theorem
implies that the uncovered fractional demand satisfies

\[
 \sum_{q=1}^{H}\sum_s
 P_{q,s}(1-\lambda^{\rm phys}_{q,s})_+
 =O\!\left(W_b b^{-1/4}\log^{7/4}b\right)=o(W_b).   \tag{2.9}
\]

#### Proof

Repeat (2.3)--(2.4), replacing the two factors `1/2` by `alpha_t` and
`beta_s`.  Multiplication by `P_(q,s)=C_sC_t` gives (2.8).  The coefficients
in (2.5) are exactly the fractions of clustered counter origins whose next
`H` types stay in the corresponding constant run.  Equation (2.9) is the
proved aggregate positive-part estimate for (2.8), with the exponentially
small boundary profiles charged in full.  \(\square\)

Theorem 2.2 is stronger than a scalar count in one precise respect: it
realizes every coefficient by a genuine subprobability distribution on full
labelled containment chains, shared by all offsets (equivalently, one may add
a null outcome carrying the unused mass).  It remains fractional and ignores
cyclic-factor order coinstantiation.

## 3. One Boolean fiber has exact simultaneous integral support

### Lemma 3.1 (nested maximal support from one SCD)

Fix a symmetric-chain decomposition `D` of `2^[b]`, a rank `r`, and
`H<=b-r`.  For `0<=q<=H`, let `E_q` be the rank-`r` sets whose chain in
`D` reaches rank `r+q`.  Then

\[
 E_0\supseteq E_1\supseteq\cdots\supseteq E_H,
 \qquad |E_q|=\min(C_r,C_{r+q}).                    \tag{3.1}
\]

For every integer `0<=N<=C_r`, one can select `N` rank-`r` sources and
give each one full nested extensions through rank `r+H` so that, at every
offset `q`, their target support has exactly

\[
 \boxed{\min(N,C_{r+q})}                            \tag{3.2}
\]

distinct sets, the information-theoretic maximum.

#### Proof

A symmetric chain which contains rank `r` reaches rank `r+q` precisely when
its top rank is at least `r+q`; hence the sets `E_q` are nested.  If
`2r+q<=b`, every SCD chain through rank `r` reaches rank `r+q`, so the count
is `C_r`.  If `2r+q>=b`, every chain through rank `r+q` also crosses rank
`r`, so the count is `C_(r+q)`.  This proves (3.1), including equality at
the boundary.

Select the `N` rank-`r` chain labels with greatest top rank, breaking ties
arbitrarily.  Nestedness then gives

\[
 |S\cap E_q|=\min(N,|E_q|)                          \tag{3.3}
\]

for every `q`.  Follow the SCD chain until it ends, and after that append any
fixed ordering of unused elements to obtain a full `H`-extension.  If
`|E_q|>=N`, the `N` selected SCD chains give distinct rank-`r+q` targets.
If `|E_q|<N`, the selected set contains all of `E_q`; those chains cover
every rank-`r+q` set, because now `|E_q|=C_(r+q)`.  Extra continuations
cannot reduce support.  This proves (3.2).  \(\square\)

For one target rectangle put `a=C_s`, `c=C_t`.  The real half allocation
therefore has the scalar row/column support ledger

\[
 \min\!\left({c\over2a},1\right)
 +\min\!\left({a\over2c},1\right)\ge1.              \tag{3.4}
\]

Indeed, if `a/c` lies in `[1/2,2]`, the left side is
`c/(2a)+a/(2c)>=1`; outside that interval one term is already one.  This
explains why no scalar or one-fiber support deficit remains.

## 4. The product-SCD wider-side rule solves integral coinstantiation

At payload split `r`, a middle source is represented uniquely as

\[
 (X,Y)\in\binom Ar\times\binom Br,                 \tag{4.1}
\]

where `X=U cap A` and `Y=B setminus (U cap B)`.  Fix symmetric-chain
decompositions `D_A,D_B`.  If the chains containing `X,Y` have bottom ranks
`a,c`, their rank intervals are respectively

\[
 [a,b-a],\qquad[c,b-c].                             \tag{4.2}
\]

### Theorem 4.1 (exact integral central all-band cover)

For every source `(X,Y)` of central rank `H<=r<=b-H`, make the following
single permanent choice.

- If `a<=c`, choose side `A` and follow the `D_A` chain upward from `X`.
- If `a>c`, choose side `B` and follow the `D_B` chain downward from `Y`
  (equivalently, add the removed labels to the physical `B` part).

If the chosen SCD chain ends before `H` steps, continue on side `A` by adding
arbitrary unused `A`-labels, and on side `B` by removing arbitrary remaining
labels from the complement coordinate `Y` (equivalently, adding those unused
physical `B`-labels).  At every noncentral source, choose
arbitrarily a side having at least `H` missing labels and any full chain on
that side; such a side exists because `H<b/2`.  Then one fixed full
`H`-chain is assigned to every middle source, and for every

\[
 1\le q\le H,\qquad H\le t=s-q,qquad s\le b-H,     \tag{4.3}
\]

**every** rank-`(b+q)` target of split `s` is covered.

#### Proof

Fix a target `(X_s,Y_t)`, and let the two SCD chains containing its
coordinates have bottom ranks `a,c`.  Suppose first that `a<=c`.  Then

\[
 [c,b-c]\subseteq[a,b-a].                          \tag{4.4}
\]

Since `Y_t` lies on the second chain, rank `t` lies in its interval and
hence also in the first.  Let `X_t` be the rank-`t` member of the first
chain.  The diagonal pair `(X_t,Y_t)` is a middle source, has the same chain
bottoms `a,c`, and is assigned side `A`.  Its SCD continuation reaches
`X_s`, so its offset-`q` target is exactly `(X_s,Y_t)`.

If `a>c`, the reverse containment holds:

\[
 [a,b-a]\subset[c,b-c].                            \tag{4.5}
\]

Rank `s` therefore occurs on the second chain.  Let `Y_s` be its rank-`s`
member.  The middle source `(X_s,Y_s)` is assigned side `B`; following its
second SCD chain downward for `q` steps reaches `Y_t`, so it also reaches the
given target.

Conditions (4.3) ensure that each source used in the first case has at least
`H` missing `A` labels and each source used in the second case has at least
`H` missing physical `B` labels.  Thus the arbitrary continuation after an
SCD endpoint always exists.  The side rule and full continuations were fixed
once per source, independently of `q`, proving simultaneous coverage of the
whole central band.  \(\square\)

Consequently the abstract integral deficit, summed over all offsets, is
confined to the profiles excluded by (4.3).  Its full ledger is

\[
 \begin{aligned}
 T_{b,H}
 &=\sum_{q=1}^H\sum_{s:\ s-q<H\text{ or }s>b-H}C_sC_{s-q}\cr
 &\le 2H^2{b\choose 2H}^{\!2}
 =e^{-\Omega(b)}W_b                              \tag{4.6}
 \end{aligned}
\]

for `H=o(b)`.  Indeed the lower-tail condition gives
`0<=s-q<s<=2H`, and reflection gives the upper-tail bound.  Finally
`binom(b,2H)<=(eb/(2H))^(2H)=e^{o(b)}`, whereas
`W_b=Theta(4^b/sqrt b)`.  Thus the total abstract integral deficit over the
whole band is exponentially small.  The row/column side matrix is explicit:
it is constant on each product of an `A`-SCD chain and a `B`-SCD chain, and
points toward the chain with the wider rank interval.

Theorems 2.2 and 4.1 solve different relaxations.  The fractional theorem
respects the exact physical constant-origin masses `alpha_r,beta_r` and
therefore has the larger but still `o(W_b)` ledger (2.9).  The integral
theorem spends one unrestricted token at each source and need not respect
either side's cyclic-origin/color cap.  Its exponentially small abstract
deficit therefore does not supersede the cap-faithful fractional statement.

The surviving gate is now wholly physical.  The product-SCD chains need not
be consecutive-interval chains in any common cyclic order; many sources
that share one tight-factor order cannot choose their successors
independently.  The theorem supplies no internally simple product atom, no
coherent order-bank realization, and no short serialization.

## 5. A sharp finite tail obstruction

### Proposition 5.1 (unavoidable extreme-profile misses)

If `H>=2`, no integral assignment of one constant-side chain to every middle
source can cover every offset-one target.  It misses at least

\[
 \boxed{2(b-1)}                                      \tag{5.1}
\]

targets at offset one.

#### Proof

For each `a in A`, the target `B union {a}` can only be the first step of an
all-`A` chain from the unique source `B`.  An all-`B` chain cannot pass
through it and continue, because it already contains all of `B`.  The one
token at source `B` covers at most one of these `b` targets, leaving at least
`b-1`.  Interchanging `A,B` gives another `b-1` misses, and the two target
families are disjoint.  \(\square\)

This obstruction is only `O(b)=o(W_b)` and lies entirely in the extreme
split profiles.  Exact H100 MILPs for `(b,H)=(3,2),(5,2),(7,2)` attain
respectively `4,8,12=2(b-1)` offset-one misses while covering every
offset-two target.  Those finite optima are computational evidence only; no
all-`b` integral upper bound is asserted.

## 6. Audit and scope

The checker `scratch/audit_constant_side_chain_fractional_scd_20260821.py`
verifies the exact target-load identities for all admissible profiles at
`b<=13`, recursively constructs SCDs through `b=9`, checks (3.1)--(3.3) for
every rank, offset, and `N`, directly constructs the wider-side assignment
and verifies every central target through `b=9`, and exhaustively verifies
the unique-source extreme-profile argument through `b=9`.  A separate exact
SciPy/HiGHS MILP gave the three finite optima quoted after Proposition 5.1.

The results are abstract labelled-containment statements.  They do not
assume the conditional tight-cycle factors, and they do not manufacture
them.  They solve integral row/column coinstantiation and cross-offset side
consistency in the unrestricted Boolean model.  They do not solve cyclic-
order compatibility, atom simplicity, or serialization.  Their purpose is
to isolate the remaining obstruction as a physical coherent-order lift,
rather than fractional capacity, one-fiber nestedness, or abstract integral
rounding.
