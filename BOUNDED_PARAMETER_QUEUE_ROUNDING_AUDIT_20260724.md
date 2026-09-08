# Audit of bounded-parameter zero-collision queue rounding

## Verdict

The fixed-parameter theorem is correct.  For every fixed `h>=1` and
`H>=2`, the monotone-profile queue hypergraph admits a matching whose real
parts are pairwise disjoint and cover all but `o(W)` masks in the fixed band.
The resulting literal OR word has length

\[
W+\frac{2h+1}{H}W+o_{h,H}(W).
\]

Diagonalization therefore gives *some* unbounded functions `h(m),H(m)` with
`h/H->0` and a band word of length `W+o(W)`.  There is no quantitative lower
bound on `h(m)`, so this does not reach the tail-killing or reservoir scale
and does not prove the constant-one theorem.

## 1. Atom audit

Index a coordinate permutation as

\[
z_{-h},\ldots,z_{2m-h-1}
\]

and put

\[
B_{t,s}=\{z_{t-s},\ldots,z_{t+m-1}\}.
\]

For a nonincreasing profile `d_0>=...>=d_(H-1)`, write

\[
L_t(d_t)=B_{t,-d_t}.
\]

The word consisting of the complement of `B_(0,d_0)`, the singleton blocks
`z_(-d_0),...,z_(d_0-1)`, and then
`L_0(d_0),...,L_(H-1)(d_(H-1))` has length `H+2d_0+1`.  The exact MTF
invariant is

\[
L_t(d_t),\{z_{t+d_t-1}\},\ldots,\{z_{-d_0}\},\ldots .
\]

Its prefix unions expose every `B_(t,s)` with `|s|<=d_t`.  The condition
`H+h<=m` keeps all position intervals inside the injective queue.  Different
advertised masks in one atom have either different sizes or different
interval endpoints, so they are distinct.  All are genuine suffix ORs.

## 2. Dummy completion and fractional perfect matching

Let `N_q=C(2m,m-q)`, `rho_q=N_q/W`, and, for uniform `U in [0,1)`, set

\[
a_q=\lfloor H\rho_q+U\rfloor.
\]

Then `E a_q=H rho_q`, and exactly `a_q` starts reach each signed depth `q`.
For every signed depth introduce `R_q=W-N_q` dummy vertices and inject the
`H-a_q` inactive slots into them.  Each augmented atom has fixed size

\[
K=H(2h+1)
\]

on an augmented universe of size `(2h+1)W`.

Under a uniform coordinate permutation, the random profile, and uniform
dummy injections, every augmented vertex lies in an atom with probability
exactly `H/W`.  Giving each distinct atom its probability times `W/H`
therefore defines an exact fractional perfect matching of total weight
`W/H`.

## 3. Weighted codegree

Condition on one real position interval mapping to a fixed mask `A`.  For a
second position interval to map to `B`, the exact conditional probability is

\[
\frac1{\binom{|A|}{|A\cap B|}
           \binom{2m-|A|}{|B\setminus A|}}.
\]

The denominator can equal one for distinct nontrivial masks only when the
two position intervals are complements.  Every active interval omits the
last queue position under `H+h<=m`, so two active intervals cannot be
complements.  Since both a mask and its complement have size at least
`m-h`, the probability is at most `1/(m-h)`.  Summing over the fixed number
of slots gives weighted real-real codegree at most

\[
H/(m-h)=o(1).
\]

Real-dummy and dummy-dummy codegrees are respectively
`O_(h,H)(m/W)` and `O_H(m^2/W)`.  Thus the maximum weighted codegree tends
to zero.

## 4. Kahn rounding and quotas

Kahn's bounded-rank fractional matching theorem says that, for fixed `K`,
an exact fractional matching with maximum weighted codegree tending to zero
has an ordinary matching of size `(1-o(1))` times its total fractional
weight.  Applying it here gives

\[
p_m=(1+o_{h,H}(1))W/H.
\]

Because the augmented hypergraph is `K`-uniform, only `o(W)` augmented
vertices remain uncovered.  Hence only `o(W)` real masks remain uncovered
in total, while disjoint augmented edges make every real duplicate count
zero.  Concatenating the literal atom words and appending the missing masks
gives the displayed length bound.

A convenient modern statement of the fixed-`K` theorem is Lemma 2.3 of
M. Liu and C. Shangguan, *Approximate generalized Steiner systems and
near-optimal constant weight codes*, arXiv:2401.00733v2.  The dependence on
`K` is not uniform and is exactly why the argument cannot simply take
`h,H` at the moderate-deviation scale.

## 5. Diagonal consequence and remaining gap

Apply the fixed theorem successively with `h=j`, `H=j^2`, and choose a
threshold `m_j` after which the total defect and relative atom-count error
are at most `1/j`.  Taking these parameters for
`m_j<=m<m_(j+1)` gives

\[
h(m)\to\infty,\qquad h(m)/H(m)\to0,
\]

zero duplicates, total missing mass `o(W)`, and a literal band word of
length `W+o(W)`.

The missing quantitative theorem is a growing-`K` version with at most
`o(W)` uncovered augmented vertices when

\[
h\gtrsim\sqrt{m\log\log m}
\]

(after the reservoir reduction), or at the larger direct tail scale.  A
generic unspecified `o(1)` matching error among `(2h+1)W` vertices is not
enough.

