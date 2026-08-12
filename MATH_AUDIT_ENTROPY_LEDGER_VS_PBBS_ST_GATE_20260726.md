# Audit of the entropy-ledger note against the current PBBS frontier

Date: 2026-07-26

## Verdict

The three positive reductions in the note contain useful mathematics, but
they do **not** support the claimed 35% verdict or the proposed logarithmic
threshold.

1. The maximal-chain theorem is correct as a coverage theorem.  Its
   ``optimal multiplicity'' assertion is only an aggregate statement:
   there are exactly
   \(W-\binom nr\) surplus rank-\(r\) slots.  Arbitrary maximal-chain
   extensions need not distribute those slots evenly.
2. The random \((\tfrac12+\varepsilon)\log m\)-loss theorem is correct.
3. The band-shrinking theorem needs an aggregate shallow-band hypothesis.
   Pointwise statements \(M_q=o(W)\) for every member of a growing family
   of depths do not imply \(\sum_{q\le q_0}M_q=o(W)\).
4. The entropy ledger and the fresh-end argument are heuristics for random
   cyclic-order families, not upper bounds on structured constructions.
   More importantly, the current PBBS construction supplies exactly the
   cross-depth correlation mechanism the fresh-end heuristic assumes away.
5. Balanced wreath flag systems are a legitimate stronger cyclic-order
   target, but their proposed ``if and only if \(Q=O(\log m)\)'' threshold
   is unsupported and is not equivalent to the constant-one theorem.

The present factor-blind route is separated from constant one by the
critical PBBS short-residence packing estimate \((\mathrm{ST}_A)\), not by
an independent-depth entropy bill.

## 1. The maximal-chain statement

Let a symmetric chain decomposition of \(2^{[2m+1]}\) be given.  Every
symmetric chain contains exactly one rank-\(m\) set, so the decomposition
has exactly

\[
 W=\binom{2m+1}{m}
\]

chains.  Extending each symmetric chain to a maximal chain therefore gives
one maximal chain through every middle set, and their union covers the
whole cube.  This proves the stated coverage theorem.

At rank \(r\), the extended chains have \(W\) occurrences and the SCD
itself already supplies one occurrence of every one of the \(\binom nr\)
targets.  Hence

\[
 \sum_{S\in\binom{[n]}r}(\mu_r(S)-1)
   =W-\binom nr.
\]

This is the forced total surplus.  It does not say that the extension
loads are floor/ceiling balanced; that simultaneous integral balancing is
a stronger theorem.

## 2. The random logarithmic-loss theorem

For a fixed \(r\)-set \(A\), a uniform cyclic order contains \(A\) as a
cyclic interval with probability

\[
 {r!(n-r)!\over(n-1)!}={n\over\binom nr}.
\]

Thus \((\tfrac12+\varepsilon)C_m\log m\) independent orders leave expected
total hole count at most

\[
 e^{-(1/2+\varepsilon)\log m}2^n=o(W).
\]

This proves a useful logarithmic-loss upper bound.  It does not show that
the logarithmic factor is necessary.

## 3. The missing quantifier in the band-shrinking theorem

Put

\[
 q_0=\left\lceil\sqrt{2m\log\log m}\right\rceil,
 \qquad \delta={1\over\log m}.
\]

The sprinkling estimate for \(q>q_0\) is correct: since

\[
 {W\over N_q}\ge
 \exp\!\left({q(q+1)\over m+1}\right),
\]

the added \(\delta C_m\) random orders leave expected deep-tail holes
\(o(W)\).

But the stated shallow hypothesis

\[
 M_q=o(W)\quad\hbox{for every }q\le q_0
\]

does not control a sum over \(q_0\to\infty\).  A valid version is, for
example,

\[
 \boxed{\sum_{q=0}^{q_0}M_q=o(W),}
\]

or the stronger uniform estimate

\[
 \max_{q\le q_0}M_q=o(W/q_0).
\]

With either replacement, the proof goes through.

## 4. The deterministic cross-depth mechanism omitted by the ledger

The fresh-end heuristic treats the choice of successive truncation ends as
essentially new information at every depth.  The audited PBBS chronology
does not behave that way.

In fact the heuristic's literal transition description is already
incorrect for one cyclic order.  A length-\(r\) cyclic interval has both
of its end-truncations as length-\((r-1)\) intervals of the same order; no
new binary choice is made at that occurrence.  Conversely, each shorter
interval has its two one-element extensions.  Adjacent shadows therefore
form a deterministic parent/child incidence.  Coverage at one rank need
not imply coverage at the next because the descendants can coalesce, but
the transition is not a fresh independent end choice.

For every

\[
 S\in\binom{[2m+1]}{m-q},
\]

the global-maximum corridor supplies a forward \(q\)-edge PBBS path whose
full intersection is exactly \(S\).  The same global mark determines all
successive truncations.  Moreover the number of forward oriented starts
for a fixed target is at most

\[
 \binom{2q+1}{q}.
\]

This is a deterministic, simultaneous, all-depth support theorem.  It is
not yet the growing-window literal word, because short coordinate
residences create cuts and crossing windows.  But it directly disproves
the premise that no single construction parameter can control many depths.

The crossing-window problem is also no longer open.  At each cut, a
dominance-staircase chart encodes every floor-correct lower intersection
and every upper union through depth \(H\) using exactly

\[
 4H-1
\]

nonzero letters.  Combining this with endpoint-capped erosion gives the
audited central-band ledger

\[
 \boxed{
 L_H\le W+2H C_m+2(5H-1)\nu_H(P_m),
 }
\]

where \(\nu_H(P_m)\) is the maximum number of pairwise edge-disjoint PBBS
coordinate-residence arcs of length at most \(H\).

For every fixed \(A>0\), set \(H_A=\lceil A\sqrt m\rceil\).  The exact
remaining sufficient estimate is

\[
 \boxed{
 \nu_{H_A}(P_m)=o_A(C_m\sqrt m).
 }
 \tag{ST_A}
\]

Indeed \(W=(2m+1)C_m\), so \((\mathrm{ST}_A)\) makes both overhead terms
\(o_A(W)\).  Fixed-\(A\) diagonalization, the product-SCD tail, and the
trimmed parity lift then give the constant-one theorem.

After the deck reduction, \((\mathrm{ST}_A)\) is

\[
 \overline\nu_{H_A}=o_A(C_m/\sqrt m).
\]

The proved height-gap spectrum already gives

\[
 \overline\nu_{H_A}=O_A(C_m/\sqrt m).
\]

Thus the live gap is a vanishing improvement over a critical-order bound.
It is not the payment of \(\Theta(\sqrt m)\) independent rank costs.

## 5. What the entropy calculation can and cannot say

The supply calculation

\[
 \log\binom{(2m)!/2}{C_m}
   =W(\log m-1+o(1))
\]

is correct.  The saddle-point demand is the rate for an occupancy model.
There is no inequality comparing that occupancy probability with the
number of PBBS-type structured families.  An exponentially tiny algebraic
subclass can contain all good objects; exact designs routinely have this
form.

Consequently the ledger supports the following limited conclusion:

> independent or weakly cross-depth-correlated cyclic-order sampling is
> not a plausible route to the Gaussian band.

It does **not** support:

\[
 Q^*=(1+o(1))\log m,
\]

nonexistence of Gaussian-band balanced wreath flags, or falsity of the
constant-one theorem.

The proposed balanced-wreath-flag conjecture is also route-specific.  Even
if exact cyclic bundling were limited to logarithmic depth, the PBBS
factor-blind compiler could still prove constant one without producing a
balanced wreath flag system.

It is also not stated at the precision predicted by its own ledger.  An
``if and only if \(Q=O(\log m)\)'' assertion includes, for example,
\(Q=100\log m\), whereas the heuristic claims a threshold constant near
one.  If one wanted to turn that prediction into a conjecture, it would
need a sharp form such as \(Q\le(1+o(1))\log m\), not big-O notation.
Likewise, constructing depth-two systems for infinitely many \(m\) would
be important evidence, but would not contradict a logarithmic threshold:
\(2\ll\log m\).

Finally, the statement that the \(m=4\) depth-one factor is the only
nontrivial finite instance is not consistent with the checked project
record: balanced depth-one exact wreath factors are known at
\(m=2,3,4\).  What is absent is an asymptotic construction.

## 6. Corrected frontier

The established chain is

\[
 \text{PBBS all-depth support}
 \;\Longrightarrow\;
 \text{exact }(4H-1)\text{ cut seam}
 \;\Longrightarrow\;
 \text{ledger above}.
\]

The single remaining PBBS gate is \((\mathrm{ST}_A)\).  Current work should
therefore target the equality/near-equality cases in the reciprocal-height
packing estimate, seeking

\[
 O_A(C_m/\sqrt m)quad\longrightarrow\quad
 o_A(C_m/\sqrt m).
\]

The logarithmic-band conjecture remains plausible and useful, but it is a
weaker target, not the corrected form forced by the evidence.
