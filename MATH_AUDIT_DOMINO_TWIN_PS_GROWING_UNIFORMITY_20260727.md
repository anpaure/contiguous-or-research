# Domino-twin catalogue: audit of the claimed classical nibble theorem

Date: 2026-07-27

## Verdict

The claimed black-box deduction of a leave `O(N/sqrt(m))` from
Pippenger--Spencer, Grable, or Vu is not justified.  The missing point is
not a constant: the published classical theorems either fix the edge
uniformity, or retain a growing-uniformity hypothesis which the packet
catalogue meets only at constant-critical order.

There is also a factor-two catalogue mismatch.  An ordinary cyclic packet
has uniformity `K=n=2m`; a domino-twin superpacket has uniformity

\[
K_\square=2n=4m.
\]

Thus even the purely formal *linear*-hypergraph Grable exponent would be
`m^{-1/4+o(1)}` for the twin catalogue, not `m^{-1/2+o(1)}`.  The twin
catalogue is not linear, so that formal estimate is not a theorem anyway.

## 1. The quantifier obstruction

Pippenger--Spencer assumes fixed uniformity.  In the quantitative matching
form quoted by Alon--Kim--Spencer, the statement is

\[
\forall K,\epsilon>0\ \exists\delta(K,\epsilon),D_0(K,\epsilon)\ \forall H.
\]

It does not give absolute exponents `c,c'>0` for

\[
\epsilon\lesssim (\Delta_2/D)^c+(\log N/D)^{c'}.
\]

To diagonalize at `K=Theta(m)` and `epsilon=m^{-1/2}` one would have to
prove separately that

\[
\Delta_2/D\le\delta(K,m^{-1/2}),\qquad D\ge D_0(K,m^{-1/2}).
\]

Neither follows from `Delta_2/D=o(1)`.  Alon--Kim--Spencer explicitly say
that their constants depend on fixed `K`; their proof uses `K(K+1)=O(1)`,
`3^{K-1}=O(1)`, and a bite covering `e^{-K}+o(1)` of the vertices.
Replacing their marking rate by `Theta(1/(KD))` is a sensible new slow
bite, but it is not their theorem: the residual regeneration estimates
must then be reproved with their full `K`-dependence.

Primary sources:

* N. Pippenger and J. Spencer, *Asymptotic Behavior of the Chromatic
  Index for Hypergraphs*, JCTA 51 (1989), whose abstract says `k` is fixed:
  https://scholarship.claremont.edu/hmc_fac_pub/585/
* N. Alon, J.-H. Kim and J. Spencer, *Nearly perfect matchings in regular
  simple hypergraphs*, Israel J. Math. 100 (1997), pp. 1--4:
  https://math.nyu.edu/~spencer/papers/alonkimjs.pdf

## 2. The actual growing-uniformity arithmetic

For the ordinary annular packet catalogue,

\[
K=2m,\qquad \frac{\Delta_2}{D}=\frac{2+o(1)}{m^2},
\qquad \log N=(2\log2+o(1))m.
\]

Grable's variable-rank sufficient condition is

\[
\Delta_2=o\!\left(\frac{D}{K\log N}\right).
\]

Here instead

\[
\frac{K\Delta_2\log N}{D}=8\log2+o(1),
\]

so the catalogue is constant-critical and the theorem does not apply.

For the domino-twin catalogue, the exact degree audit gives

\[
K_\square=4m,\qquad
\frac{\Delta_2^\square}{D^\square}
=\frac5{R(2m-R)}=\frac{5+o(1)}{m^2}.
\]

Consequently

\[
\boxed{
\frac{K_\square\Delta_2^\square\log N}{D^\square}
=40\log2+o(1),
}
\]

again not `o(1)`.  Notice that the exact maximum here is `Theta(D/m^2)`;
the `Theta(D/m)` antipodal codegree belongs to a different middle-layer
catalogue and should not be imported into this lower-annular one.

Kostochka--Rodl's summary of Grable's result records both the hypothesis
and the leave:

\[
N\left(\frac{KC\log N}{D}\right)^{1/(2K-1+o(1))}.
\]

See A. Kostochka and V. Rodl, *Partial Steiner systems and matchings in
hypergraphs*, RSA 13 (1998), abstract:
https://experts.illinois.edu/en/publications/partial-steiner-systems-and-matchings-in-hypergraphs/

Since the parenthesized quantity tends to a constant greater than one in
both packet catalogues, this gives no vanishing leave.

## 3. Why the displayed `N/sqrt(m)` is a formal artefact

Grable's estimate for a **linear** `K`-uniform regular hypergraph is

\[
O_K\!\left(N(D/\log N)^{-1/(2K-1+\eta)}\right).
\]

Using `log D=(2+o(1))m log m` gives formally

\[
N m^{-1/2+o(1)}\quad(K=2m),
\]

which explains the number in the proposed audit.  But the ordinary
catalogue has codegree `Theta(D/m^2)`, not one.  For twins, `K=4m`, so
the same invalid substitution would give only

\[
N m^{-1/4+o(1)}.
\]

Vu's non-linear fixed-`K` replacement has the shape

\[
O_K\!\left(N(D/C)^{-1/(K-1)}\log^{c_K}D\right).
\]

For `D/C=Theta(m^2)` and either `K=2m` or `4m`, its power term is
`1-o(1)`, not `m^{-1/2}`.  Moreover all constants and thresholds depend
on fixed `K`.  Vu states at the outset that the uniformity is fixed:
https://doi.org/10.1002/1098-2418(200008)17:1%3C29::AID-RSA4%3E3.0.CO;2-W

## 4. A primary-source check aimed specifically at growing uniformity

Alon--Bollobas--Kim--Vu explicitly observe that the fixed-uniformity
results do not determine what happens when `K` grows.  Their uniform
nibble hypothesis for matching/covering includes

\[
C=o\!\left(\frac{D}{e^{2K}\log D}\right).
\]

For the twin catalogue, `C/D=Theta(m^{-2})` and `K=4m`, so this condition
fails exponentially.  See pp. 1--2 and condition (8) on p. 14 of
N. Alon, B. Bollobas, J.-H. Kim and V. Vu, *Economical covers with
geometric applications*, PLMS 86 (2003):
https://web.math.princeton.edu/~nalon/PDFS/abkv4.pdf

This does not refute a theorem exploiting the twin catalogue's much
stronger *average factorial-overlap* estimates.  It does refute the claim
that such a theorem is already classical or follows from maximum
codegree alone.

## 5. What is actually available

A single slow isolated bite with marking probability `gamma/(KD)` is
uniformly valid and covers `Theta(N/K)` vertices.  Reaching density
`m^{-1/2}` takes `Theta(K log m)` bites.  The static twin audit now proves
factorial overlap bounds through order `O(log m)`, so it provides exactly
the kind of extra structure a custom proof could use.  What remains is
the stopped, hereditary version of those bounds along the chosen
trajectory (the dynamic ACLE).  No cited classical theorem supplies it.

Therefore the rigorous status is:

\[
\boxed{
\text{time-zero degree/codegree and factorial overlaps are proved;}
\quad
\text{the domino-twin near-factor is still a new dynamic theorem.}
}
\]
