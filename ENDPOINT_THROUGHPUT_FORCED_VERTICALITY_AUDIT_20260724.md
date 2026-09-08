# Audit: endpoint throughput and forced verticality

## Verdict

The endpoint-capacity argument is correct, including seam-crossing intervals.
Two qualifications are required in the project's nonzero-target convention:

1. use `0<=H<=m-1` in even dimension, because `q=m` is rank zero and is not
   required by `nu(2m)`;
2. an `o(W)` appendage cannot repair a rank with `Theta(W)` holes, but it can
   repair `o(W)` holes in each of many ranks when those repairs align along
   its endpoint chains.  The broad phrase “cannot repair the remaining
   ranks” should therefore be read rankwise, not as a blanket prohibition.

The forced-verticality conclusion can be strengthened: the natural sufficient
range is every `H->infinity` satisfying

\[
 H\eta_m+\frac{H^3}{m}=o(1),
\]

or equivalently

\[
 H=o\!\left(\min\{\eta_m^{-1},m^{1/3}\}\right),
\]

with `eta_m^(-1)=infinity` when `eta_m=0`.

## 1. Exact endpoint capacity

At one right endpoint `j`, the unions of intervals ending at `j` are the
suffix unions

\[
 A_j\subseteq A_{j-1}\cup A_j\subseteq\cdots
 \subseteq A_1\cup\cdots\cup A_j.
\]

They form an inclusion chain and therefore contain at most one distinct set
of any fixed rank.  If `C` of length `R` is appended to `B`, every mask newly
represented by `B|C` has a witness ending in `C`; otherwise it was already a
mask of `B`.  Assigning each new fixed-rank mask one witnessing endpoint in
`C` is injective, so

\[
 |\mathcal R_r(B|C)\setminus\mathcal R_r(B)|\le R.
\]

Summing over a rank family `Q` gives at most `R|Q|`.  A witness crossing the
seam still ends at one of the `R` new endpoints, so there is no seam escape.

## 2. Even-dimensional count

Let a universal nonzero word have length `n`, put

\[
 W={2m\choose m},\qquad N_q={2m\choose m-q},
\]

and take `0<=q<=H<=m-1`.  The `N_q` distinct rank-`m-q` masks require
`N_q` distinct active endpoints.  Hence the number `B_H` of missing
endpoint-depth incidences satisfies

\[
 B_H\le(H+1)(n-W)+\sum_{q=0}^H(W-N_q).
\]

The exact ratio is

\[
 \frac{N_q}{W}=\prod_{i=0}^{q-1}\frac{m-i}{m+i+1}.
\]

Writing the factors as `1-x_i` gives

\[
 x_i=\frac{2i+1}{m+i+1}\le\frac{2i+1}{m+1}.
\]

Thus the product union bound yields the slightly sharper estimate

\[
 W-N_q\le\frac{q^2}{m+1}W,
\]

and therefore

\[
 \boxed{
 B_H\le(H+1)(n-W)
 +\frac{WH(H+1)(2H+1)}{6(m+1)}.}
 \tag{1}
\]

The submitted denominator `m` is weaker but valid.

## 3. Full endpoint flags

Suppose `n=(1+eta_m)W`.  From (1),

\[
 \frac{B_H}{W}
 \le(H+1)\eta_m+O(H^3/m).
\]

Hence `B_H=o(W)` for every unbounded `H` with
`H eta_m+H^3/m=o(1)`.  An endpoint that fails to carry the full range of
ranks contributes at least one missing incidence.  Consequently at most
`B_H=o(W)=o(n)` endpoints are bad, and every other endpoint carries a nested
saturated flag

\[
 S_{m-H}\subset S_{m-H+1}\subset\cdots\subset S_m
\]

of actual suffix unions.

There is also an owner form.  At most `B_H` middle masks can have all their
witness endpoints among the bad endpoints, because one endpoint carries at
most one middle mask.  Thus at least `W-B_H=W-o(W)` distinct middle masks can
be assigned distinct good endpoints, each owning a full depth-`H` flag.  This
is a necessary near-resolution property of every hypothetical width-order
word; it still does not impose cyclic-wreath alignment on those flags.

The displayed choice `H=min(m^(1/4),eta^(-1/2))` is safe but conservative.
The proof permits any

\[
 H=o\!\left(\min\{m^{1/3},\eta_m^{-1}\}\right)
\]

that tends to infinity.

## 4. Odd dimension

For `W={2m+1\choose m}` and `N_q={2m+1\choose m-q}`,

\[
 \frac{N_q}{W}=\prod_{i=0}^{q-1}\frac{m-i}{m+i+2},
\qquad
 1-\frac{m-i}{m+i+2}
 =\frac{2i+2}{m+i+2}\le\frac{2i+2}{m+2}.
\]

Therefore

\[
 W-N_q\le\frac{q(q+1)}{m+2}W
\]

and

\[
 B_H\le(H+1)(n-W)
 +\frac{WH(H+1)(H+2)}{3(m+2)}.
\]

The same `H eta+H^3/m` criterion follows.

## 5. Exact scope of the appendage obstruction

If `B|C` is universal and `|C|=R`, then for every required rank

\[
 M_r(B)\le R.
\]

Thus an `o(W)` appendage cannot repair a rank having `Omega(W)` holes.  Over
`Q`,

\[
 \sum_{r\in Q}M_r(B)\le R|Q|.
\]

This is the exact conclusion.  It rules out delegating a linearly defective
mesoscopic rank to a short patch, but it does not rule out a vertically
aligned patch that supplies one new mask per rank at each of its endpoints.

Accordingly the theorem is a strong necessary structural result, not the
missing construction theorem.  It leaves the global coefficient-one upper
bound unresolved.

The final paragraph of the submitted statement uses the older
`H asymp sqrt(m log m)` wreath target.  The audited symmetric-chain product
tail construction has already reduced the sufficient depth: it is enough to
obtain total central defect `o(W)` through any

\[
 H=\sqrt m\,\omega(m),\qquad \omega(m)\to\infty,\qquad H=o(m).
\]

This does not affect the endpoint theorem, but it is the current, strictly
weaker construction gate that should be quoted in the status section.
