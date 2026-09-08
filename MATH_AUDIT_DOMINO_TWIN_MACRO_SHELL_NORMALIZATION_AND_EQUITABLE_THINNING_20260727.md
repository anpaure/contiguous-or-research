# Domino twins: macroscopic shell normalization and the missing equitable thinning

Date: 2026-07-27

## 0. Verdict

Put

\[
 n=2m,\qquad K=4m,
 \qquad z=m^{-1/2},
\]

and let (D) be the entrance degree of the simple domino-twin
catalogue.  Thus

\[
 \log D=2m\log m+O(m).
 \tag{0.1}
\]

For two packets write

\[
 \delta(F,G):=K-|F\cap G|
\]

for their defect.  Suppose the inverse list estimate is

\[
 L_t(F):=|\{G:\delta(F,G)\le t\}|
 \le \exp(Cm)n^{ct},\qquad t=o(m).
 \tag{0.2}
\]

Then the threshold (c<1/2) is indeed the right **raw-shell**
threshold at (z=m^{-1/2}).  It is also the right threshold after a
quarantine only if the thinning is proportional on every overlap shell.

The present local-minimum conflict thinning proves proportional entrance
degrees and proportional pair codegrees.  It does **not** prove
proportional overlap-shell counts around a retained packet.  Without
that extra conclusion, its degree loss introduces a second list factor:

\[
 \begin{array}{c|c}
 \text{normalization} & \text{exponent at defect }t=s\\ \hline
 \text{raw catalogue}
     &-(\frac12-c)s\log m+O(m),\\[1mm]
 \text{degree-thinned only}
     &-(\frac12-2c)s\log m+O(m),\\[1mm]
 \text{shell-equitably thinned}
     &-(\frac12-c)s\log m+O(m).
 \end{array}
 \tag{0.3}
\]

Consequently the (c=1/3) inverse estimate does **not**, by itself,
close the macroscopic survivor comparison.  The negative sign in
Section 4 of
`MATH_THEOREM_MACRO_OVERLAP_QUARANTINE_BY_CONFLICT_THINNING_20260727.md`
is the correct sign for one retained neighbour, and also for a
proportionally thinned shell, but it is not justified for the full
retained shell by the theorem currently proved there.

## 1. The normalized survivor shell

Fix an entrance target (X\in F).  If (G\ni X) and
(delta(F,G)=t), then

\[
 |F\cap G|-1=K-t-1.
\]

Its independent-survivor amplification relative to two disjoint packets
is therefore

\[
 z^{-(K-t-1)}=m^{(K-t-1)/2}.
 \tag{1.1}
\]

For a subcatalogue (mathcal J), define

\[
 d_{\mathcal J}(X)=|\{G\in\mathcal J:X\in G\}|
\]

and the cumulative shell count

\[
 N_{\mathcal J,t}(X,F)
 =|\{G\in\mathcal J:X\in G,\ G\ne F,
                  \ \delta(F,G)\le t\}|.
 \tag{1.2}
\]

The normalized contribution of defects in ([s,u]) is bounded by

\[
 \Omega_{\mathcal J}(X,F;s,u)
 \le \frac1{d_{\mathcal J}(X)}
       \sum_{t=s}^{u}
       N_{\mathcal J,t}(X,F)m^{(K-t-1)/2}.
 \tag{1.3}
\]

Using cumulative rather than exact shells only overcounts and is
convenient because (0.2) is a ball estimate.

The cancellation controlling every calculation below is

\[
 -\log D+\frac K2\log m=O(m),
 \qquad \log n=\log m+O(1).
 \tag{1.4}
\]

## 2. Raw catalogue

In the raw catalogue, (d(X)=D) and
(N_t(X,F)\le L_t(F)).  Equations (0.2)--(1.4) give

\[
 \begin{aligned}
 \Omega_{\rm raw}(X,F;s,u)
 &\le \sum_{t=s}^{u}
 \exp\!\left(
 O(m)+ct\log n-\frac t2\log m\right)\\
 &\le \exp\!\left(
 O(m)-(\tfrac12-c)s\log m\right),
 \end{aligned}
 \tag{2.1}
\]

uniformly for (u=o(m)), provided (c<1/2).  The last sum is
geometric because its ratio is

\[
 n^c m^{-1/2}=m^{c-1/2+o(1)}=o(1).
\]

Thus, for

\[
 s=A\frac m{\log m},
 \tag{2.2}
\]

the raw contribution from defects at least (s) is exponentially small
once (A) is a sufficiently large constant.  The raw catalogue cannot
be used directly because the defects (t<s), including the
near-parallel twins, have enormous survivor weight.

## 3. Merely degree-proportional conflict thinning

Let (mathcal J\) be a conflict-independent thinning with retention
scale (p), where

\[
 d_{\mathcal J}(X)=(1+o(1))pD,
 \qquad
 p^{-1}\le \exp(Cm)n^{cs}.
 \tag{3.1}
\]

The second inequality is the loss supplied by colouring or
local-minimum thinning the defect-(<s) conflict graph.  Suppose no
information is known about the retained overlap shells beyond the
tautological bound

\[
 N_{\mathcal J,t}(X,F)\le L_t(F).
 \tag{3.2}
\]

Then (1.3) is the raw estimate multiplied by (p^{-1}):

\[
 \Omega_{\mathcal J}(X,F;s,u)
 \le
 \exp\!\left(
 O(m)+cs\log n-(\tfrac12-c)s\log m\right).
 \tag{3.3}
\]

At the first allowed shell (t=s), this is

\[
 \boxed{
 \Omega_{\mathcal J}
 \le \exp\!\left(
 O(m)-(\tfrac12-2c)s\log m\right).}
 \tag{3.4}
\]

Hence degree proportionality alone needs (c<1/4).  For (c=1/3),
the displayed exponent has the wrong sign.  Entrance-degree regularity
and ordinary pair-codegree regularity do not imply (or even mention)
(1.2), so they cannot remove this second list factor.

This identifies the precise omission in the current macro-quarantine
note.  Its calculation

\[
 \frac{z^{-(K-s)}}{pD}
 =\exp\!\left(O(m)-(\tfrac12-c)s\log m\right)
 \tag{3.5}
\]

is a **one-neighbour** calculation.  Multiplying it by all potentially
retained neighbours in the first shell gives (3.4), unless the thinning
is known to reduce that shell proportionally.

## 4. Proportional shell thinning

The correct equitable estimate has an unavoidable integer (1) term.
Indeed (pL_t) can be below one although one neighbour remains.  Assume
that, for every retained incidence (X\in F) and every
(s\le t\le u=o(m)),

\[
 N_{\mathcal J,t}(X,F)
 \le \exp(C_0m)\bigl(1+pL_t(F)\bigr).
 \tag{4.1}
\]

Then (1.3) splits into two terms.  The (pL_t) term cancels the
degree-thinning factor (p) and is exactly the raw estimate (2.1).  The
integer term gives

\[
 \begin{aligned}
 \frac1{pD}\sum_{t=s}^{u}m^{(K-t-1)/2}
 &\le
 \exp\!\left(
 O(m)+cs\log n-\frac s2\log m\right)\\
 &=\exp\!\left(
 O(m)-(\tfrac12-c)s\log m\right).
 \end{aligned}
 \tag{4.2}
\]

Therefore

\[
 \boxed{
 \Omega_{\mathcal J}(X,F;s,u)
 \le \exp\!\left(
 O(m)-(\tfrac12-c)s\log m\right).}
 \tag{4.3}
\]

This restores the threshold (c<1/2).  In particular (c=1/3) would
be sufficient at (s=A m/\log m), **conditional on** (4.1).

## 5. A rigorous sufficient equitable-thinning theorem

The following is the exact statement needed from a quarantine theorem.
It is a sufficiency theorem, not a claim that the present local-minimum
construction satisfies its shell hypothesis.

> **Theorem 5.1 (shell-equitable quarantine is sufficient).**
> Fix (c<1/2), and suppose the simple domino-twin catalogue satisfies,
> uniformly for (t\in[s,u]) with (u=o(m)),
> \[
>  L_t(F)\le e^{Cm}n^{ct}.
> \]
> Let (s=A m/\log m).  Suppose there is a subcatalogue
> (mathcal J) and a number (p) such that:
>
> 1. (d_{\mathcal J}(X)=(1+o(1))pD) for every entrance target (X);
> 2. (p^{-1}\le e^{C_1m}n^{cs});
> 3. distinct packets in (mathcal J) have defect at least (s); and
> 4. for every retained incidence (X\in F) and every
>    (s\le t\le u),
>    \[
>      N_{\mathcal J,t}(X,F)
>      \le e^{C_2m}\bigl(1+pL_t(F)\bigr).
>      \tag{5.1}
>    \]
>
> Then there is a constant (A_0=A_0(c,C,C_1,C_2)) such that, for
> every fixed (A>A_0),
> \[
>  \sup_{X\in F\in\mathcal J}
>  \Omega_{\mathcal J}(X,F;s,u)=e^{-\Omega(m)}=o(1).
>  \tag{5.2}
> \]
>
> The same conclusion holds if (5.1) has (n^{(c+\eta)t}) in place
> of (n^{ct}), provided (c+\eta<1/2).

### Proof

Insert (5.1) in (1.3), use clauses 1--2, and apply the two estimates in
Section 4.  Both geometric sums are bounded by

\[
 \exp\!\left(C_3m-(\tfrac12-c)s\log m\right)
 =\exp\!\left((C_3-(\tfrac12-c)A)m+o(m)\right).
\]

Choose (A>C_3/(1/2-c)).  This proves (5.2).  The version with
(c+\eta) is identical. \(square)

There is also an incidence-averaged version: it is enough that (5.1)
fail on (o(1/K)) of the selected incidence intensity, because packets
carrying those incidences may be deleted into the final (o(N)) leave.
This is the natural form for a stopped matching proof, but the weighting
must be by actual selected-edge intensity, not merely by raw catalogue
incidence count.

## 6. What random local-minimum thinning gives for free

There is a useful first-moment fact, but it falls short of Theorem 5.1.
Let (Gamma) be a regular conflict graph of degree (Delta), put
(p=1/(\Delta+1)), and retain local priority minima.  If nonadjacent
vertices (F,G) have (h) common conflict neighbours and
(a=\Delta+1-h), direct integration gives

\[
 \Pr(F,G\text{ both retained})
 =\frac{2}{(\Delta+1)(\Delta+a+1)}
 \le 2p^2.
 \tag{6.1}
\]

Indeed, conditioning on priorities (x\le y), the integral is

\[
 2\int_0^1\int_0^y
 (1-x)^{\Delta-h}(1-y)^\Delta\,dx\,dy.
\]

Consequently, conditional on (F) being retained, the expected number
of retained nonconflicting neighbours from any prescribed list
(mathcal L(F)) is at most

\[
 2p|\mathcal L(F)|.
 \tag{6.2}
\]

Thus local-minimum thinning has the correct shell scale **in
expectation**.  At time zero this expectation can in fact be converted
to a pointwise statement by an alteration.

> **Proposition 6.1 (static shell-equitable alteration).**
> Assume the simultaneous entrance-degree conclusion
> \[
>  d_{\mathcal J}(X)=(1+o(1))pD
> \]
> for the local-minimum thinning, and let (T_m\le m) be the number of
> shell thresholds under consideration.  For any polynomial (M_m)
> with
> \[
>  \frac{KT_m}{M_m}=o(1),
> \]
> there is a realization and a deletion of (o(1)) of its retained
> packets such that every remaining incidence (X\in F) satisfies,
> simultaneously at all the thresholds,
> \[
>  N_{\mathcal J,t}(X,F)
>  \le M_m\bigl(1+pL_t(F)\bigr).                       \tag{6.3}
> \]
> Moreover all but (o(N_R)) entrance targets still have degree
> ((1-o(1))pD).  Conflict independence and all upper codegree bounds
> are preserved.

### Proof

For a fixed raw incidence ((X,F)) and threshold (t), (6.1) gives

\[
 \mathbb E\!\left[
 {\bf1}_{\{F\ {\rm retained}\}}N_{\mathcal J,t}(X,F)
 \right]
 \le 2p^2L_t(F).
\]

Markov's inequality therefore gives

\[
 \Pr\left(
 F\text{ retained and }
 N_{\mathcal J,t}(X,F)>M_m(1+pL_t(F))
 \right)
 \le \frac{2p}{M_m}.                                  \tag{6.4}
\]

Sum (6.4) over the (K) incidences of a packet and over the (T_m)
thresholds.  The expected fraction of retained packets which violate at
least one inequality is at most

\[
 \varepsilon_m:=\frac{2KT_m}{M_m}=o(1).               \tag{6.5}
\]

The degree-concentration event used in the original thinning theorem has
probability (1-o(1)).  Markov applied to the number of violating
retained packets therefore supplies a realization on that event with at
most (o(1)) violating fraction.  Delete all violating packets.

If (\ell_X) is the entrance-degree loss at (X), then

\[
 \sum_X\ell_X=K\,|\{\text{deleted packets}\}|
              =o(N_RpD).
\]

For any auxiliary (\rho_m\to0) slower than this incidence-loss
fraction, the number of targets with
(\ell_X>\rho_mpD) is (o(N_R)).  Every other target retains degree
((1-o(1))pD).  Deletion only lowers codegrees and preserves conflict
independence.  This proves the proposition.

For example (M_m=m^6) is more than sufficient.  Since any polynomial
factor is absorbed by the (e^{O(m)}) slack in Theorem 5.1,
Proposition 6.1 supplies the required **static** shell equitability, up
to an (o(N_R)) exceptional entrance set.

What remains missing is the trajectory version: after packets are
successively selected and their entrance resources deleted, the live
catalogue is no longer a fresh local-minimum thinning of the raw regular
catalogue.  A stopped selected-intensity maximal theorem must propagate
the altered shell bounds, or periodically regenerate them, without
accumulating a critical leave.

## 7. Correct frontier

The macroscopic lane now has two logically separate inputs:

1. the inverse list exponent (c<1/2); and
2. shell-equitable thinning, in the pointwise form (5.1) or an
   incidence-weighted stopped analogue.

The (c=1/3) paired-window theorem, if its independent audit succeeds,
would settle the first input.  It would not settle the second.  The
claim in the present macro-quarantine note that inverse stability alone
closes the survivor comparison should therefore be weakened to a
conditional statement using Theorem 5.1.
