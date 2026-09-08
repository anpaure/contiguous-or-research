# Audit: balanced wreath absorption reduction

Date: 2026-07-24

## Verdict

The exact-factor argument, the quota arithmetic, and the absorption
implication are correct.  The proposed lemma is a valid sufficient theorem,
not a consequence of the currently cited matching black boxes.

Its leave requirement can be weakened by a factor of `sqrt(log m)`.  The
MWB weights give

\[
\sum_{q<Q}\frac1{c_q}=O(\sqrt m),
\]

so it is enough to leave

\[
\boxed{R=o\!\left(\frac{W}{n\sqrt m}\right)}
\]

wreaths for the exact completion, rather than
`o(W/(n*sqrt(m log m)))`.

## 1. Exact factors

Mütze, Standke, and Wiechert prove that the odd graph `O_(2m+1)` has a
`C_(2m+1)`-factor.  The submitted shortest-cycle argument correctly shows
that every such cycle is the family of all length-`m` intervals of one
cyclic coordinate order.  Thus exact middle wreath factors are
unconditional; only simultaneous lower-shadow balancing is missing.

The cited primary source states this as Theorem 4:
`https://tmuetze.de/papers/dyck.pdf`.

## 2. Quotas and fractional marginals

For

\[
a_q=\frac W{N_q}
=\prod_{i=0}^{q-1}\frac{m+2+i}{m-i},
\]

the expansion

\[
\log a_q=\frac{q(q+1)}m+O(q^3/m^2)
\]

is uniform in the stated range.  The wreath hypergraph degree and lower-set
incidence degree are

\[
D=\frac{n!}{W}=m!(m+1)!,
\qquad
|\Gamma_{q,S}|=\frac{n!}{N_q}=a_qD.
\]

Consequently uniform edge weight `1/D` gives all top degrees one and all
lower marginals `a_q` simultaneously.  This is only a fractional solution.

The submitted codegree formula

\[
\frac{\deg(A,B)}D
=\frac{2}{\binom md\binom{m+1}d}
\]

for `|A\B|=|B\A|=d` is correct for distinct `A,B`, i.e. `1<=d<=m`.
At `d=0` the codegree is the ordinary degree, not the displayed right side.
The maximum for distinct vertices is `2/(m+1)` at disjoint middle sets.
Small normalized pair-codegrees do not supply the required exact completion
at growing uniformity.

## 3. Automatic large-depth contribution

Take

\[
Q=\lceil\sqrt{m\log m}\rceil,
\qquad H=\lceil2\sqrt{m\log m}\rceil.
\]

Then `a_Q=m exp(o(1))`, `c_q>=a_q/2` for `q>=Q`, and `O_q<=W` for every
factor.  Therefore

\[
\sum_{q=Q}^{H}\frac{O_q}{c_q}
\le
\frac{2W(H-Q+1)}{a_Q}
=O\!\left(W\sqrt{\frac{\log m}{m}}e^{o(1)}\right)
=o(W).
\]

So the constructive issue may indeed be confined to `q<Q` for this choice
of `H`.

The cutoff constant is not optimal.  Direct Gaussian summation shows that
one may already take

\[
Q=\left\lceil
\sqrt{\tfrac12m\log m}
\right\rceil,
\]

because

\[
\sum_{q\ge Q}\frac1{c_q}
=O\!\left(\frac1{\sqrt{\log m}}\right)=o(1).
\]

More sharply, `Q^2/m=(1/2)log m-(1/2)log log m+omega(1)` suffices.

## 4. Absorption implication

Let `b_q` be a balanced quota vector of total `W`.  Suppose an exact factor
`F` contains a submatching `M` such that

\[
\mu_q^M(S)\le b_q(S)\qquad(q<Q),
\]

and put `R=|F\M|`.  The completion has exactly `nR` depth-`q`
occurrences.  Relative to the particular quota `b_q`, all positive overload
is introduced by those occurrences, hence

\[
O_q(F)\le nR.
\]

This proves the submitted implication.  The only quantitative overpayment is
the subsequent use of `c_q>=1` separately at all `Q` depths.

## 5. Sharper leave scale

For every `q=o(m)`, the elementary lower estimate

\[
\log a_q
\ge\frac{q(q+1)}{m+q+1}
\]

and `c_q=floor(a_q)>=a_q/2` give, uniformly for `q<Q`,

\[
\frac1{c_q}
\le2\exp\!\left(-\frac{q(q+1)}{m+q+1}\right).
\]

Because `Q=o(m)`, comparison with a Gaussian sum yields

\[
\sum_{q=1}^{Q-1}\frac1{c_q}=O(\sqrt m).
\]

Consequently

\[
\sum_{q<Q}\frac{O_q(F)}{c_q}
\le
nR\sum_{q<Q}\frac1{c_q}
=O(nR\sqrt m).
\]

The corrected sufficient leave condition is therefore

\[
\boxed{
R=o\!\left(\frac{W}{n\sqrt m}\right).
}
\tag{BWA}
\]

This is strictly weaker than the submitted `o(W/(nQ))` condition by a
factor `sqrt(log m)`.

## 6. Exact missing theorem

It is enough to prove:

> For `Q=ceil(sqrt(m log m))`, there are balanced quota vectors `b_q`, an
> exact middle wreath factor `F`, and a quota-safe submatching `M subset F`
> through every `q<Q`, such that its extendible leave satisfies (BWA).

Equivalently, construct a simultaneously conflict-free near-factor whose
middle-layer leave can be absorbed by actual wreaths, while disturbing only
`o(W/(n sqrt(m)))` completed wreaths.

This is stronger than an ordinary almost-perfect conflict-free matching:
the leave must be exceptionally small and extendible to the same exact
factor.  The 2024 conflict-free matching theorem supplies almost-perfect
matchings, while the later matching-and-covering theorem completes a
specified part only under an additional fixed-parameter reserve-edge setup.
Neither theorem, as currently stated, gives this growing-uniformity wreath
absorption result.

The lemma is sufficient, not known necessary.  A successful proof could
instead control weighted overload directly by integral wreath trades.

Indeed, writing

\[
s_q(S)=b_q(S)-\mu_q^M(S)\ge0,
\qquad C=F\setminus M,
\]

the exact completion charge relative to these quotas is

\[
\sum_{q<Q}\frac1{c_q}
\sum_S\bigl(\mu_q^C(S)-s_q(S)\bigr)_+.
\]

Requiring this quantity to be `o(W)` is weaker and more faithful than any
cardinality-only bound on `R`: a much larger completion may be harmless when
it mostly fills the slack of the quota-safe near-factor.
