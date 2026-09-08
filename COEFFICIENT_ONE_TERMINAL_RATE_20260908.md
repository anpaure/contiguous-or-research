# Stronger explicit rate from terminal charging

Date: 2026-09-08. The terminal-charging, profile-weighting and clipping
argument was supplied by the user. This numerical extension has passed
root and independent internal mathematical reviews on the manuscript's
finite PBBS inputs. It retains their proposed-proof status; it is not
external or formal certification of the inherited machinery.

All logarithms are natural. Use the same explicit constant

\[
                     A=2^{2097152}.
\]

## Result

The user's boundary exponent is valid with this numerical choice:

\[
 \gamma_*=\frac1{4\sqrt{2A}}=\frac{2^{-1048578}}{\sqrt2},
 \qquad
 \frac{\nu(k)}{W(k)}-1
   =O\!\left((\log k)^{-\gamma_*}
                   e^{C\sqrt{\log\log k}}\right).
\]

Every fixed exponent below gamma_* gives a pure logarithmic-power bound.
A completely numerical, deliberately conservative corollary is

\[
 \boxed{\nu(k)\le W(k)\left(1+(\log k)^{-\gamma_1}\right),
 \quad\gamma_1=2^{-1048580},\quad k\ge k_1,}
\]
\[
 k_1=\left\lceil\exp\!\left(\exp(2^{1048616})\right)\right\rceil.
\]

The multiplier in this corollary is C=1. Both its exponent and its
threshold improve the first numerical rate in
[the earlier explicit-rate proof](COEFFICIENT_ONE_EXPLICIT_RATE_20260908.md).
The threshold remains enormous, and this gives no new numerical estimate
for nu(17). The finite interval remains 24313<=nu(17)<=25745.

## Finite proof with all numerical inputs

Put R=sqrt(r), y=loglog r and J=2^38 exp(2^19). For
r>=2^1000000, 1<=c<=sqrt(y), 0<p<=1, the internally checked finite bound is

\[
\begin{aligned}
 \frac{\nu(2r+1)}{W_r}\le1
 &+\frac{c+1}{R}
 +2^{92}J^3(c+2)^6\frac{e^{Ap^2(c+2)^2}}{(\log r)^p}\\
 &+e^{A(c+2)^2}r^{-1/400}+2048e^{-c^2/8}.
\end{aligned} \tag{1}
\]

This display keeps the polynomial error's growing exponential instead of
silently discarding it at the original threshold. The exterior constant
2048 includes the floor in t=floor(cR). The main prefactor satisfies
log(2^92 J^3)<2^21.

The proof has four finite steps.

1. At each occupied edge, charge the containing trace with the latest
   starting time. An eligible later-starting partner prevents a base
   trace from being charged. Under the complete-vector coupling, the
   remaining no-success event is a first renewal gap exceeding K, with
   probability at most100/log r. This replaces the larger reciprocal
   renewal-count bound.
2. Use the profile-invariant edge weight omega=1+R/(h+2). Every packed
   trace has weight at least R, and omega<=2^26 Q. Thus no small-height
   split is needed. The profile law is the original root law, with the
   conditional incidence mass retained.
3. Average cutoffs separately in each profile. Monotonicity gives the
   bound at the prescribed cutoff floor(cR). Cap that profile's occupied
   fraction at one before taking expectation. The exact error function
   is an actual conditional bad-incidence mass plus a bounded coupling
   defect, not a conditional version of a global Markov estimate.
4. Use min(1,z)<=z^p and the explicit sharp moment
   E[Q^v exp(uQ)]<=2^26(1+u)^3 exp(u^2), 1<=v<=2. This produces p^2
   in the cutoff penalty while retaining p in the logarithmic gain.

The resulting finite packing inequality is

\[
 \frac{R P_{\lfloor cR\rfloor}(r)}{W_r}
 \le2^{88}J^3(c+2)^{2p+3}
     \frac{e^{J^2p^2(c+2)^2}}{(\log r)^p}
   +e^{(A_0+64)(c+2)^2}r^{-1/400},
\]

where A_0=2^80 exp(2^20). In particular, for every fixed c>0,
P_floor(cR)(r)=O_c(W_r/(R log r)). Compilation multiplies this by at
most10(c+2); its error exponent remains below A because A>A_0+128.
The literal compiler covers all ranks and charges every seam.

The complete conditional, finite-probability and numerical proof is
[the terminal/profile-capping audit](scratch/PBBS_TERMINAL_PROFILE_CAPPING_AND_SHARP_MGF_INDEPENDENT_AUDIT_20260908.md).
The independent full check of charging, profiles, floors, compilation,
optimization and every threshold is
[the terminal compiler and exponent audit](scratch/PBBS_TERMINAL_CHARGING_COMPILER_AND_DYADIC_RATE_INDEPENDENT_AUDIT_20260908.md).
Those notes contain the proof details; no unavailable user verifier
package was used as a premise.

## Numerical corollary

For the pure-power statement choose

\[
 p=\frac1{4\sqrt A}=2^{-1048578},\qquad
 z=p\log\log r,\qquad c=2\sqrt z-2.
\]

At k>=k_1 the odd source dimension is k or k-1 and
loglog r>=2^39 sqrt(A), so z>=2^37 and the parameter is admissible.
The four excess terms in (1) are each at most one eighth of exp(-z/4).
For the main term this follows from
64*2^92 J^3 z^3 exp(-3z/4) and log(2^92 J^3)<2^21.
For the tail it follows from2048 exp(-z/2+sqrt(z)-1/2).
For the error, A(c+2)^2=sqrt(A)loglog r<=(loglog r)^2, which permits
absorption into r^-1/1000 at this larger explicit threshold. The cycle
term is smaller still. These elementary comparisons are fully expanded
in the independent threshold audit linked above.

Their sum is at most(1/2)(log r)^-gamma_1. The exact trimmed lift doubles
both length and width. Since r>=sqrt(k), conversion to log k costs at
most2^gamma_1<=5/4, leaving an excess at most(5/8)(log k)^-gamma_1.
This proves the displayed C=1 statement in both parities.

## Scope

This is a constructive asymptotic rate, not exact equality nu(k)=B(k).
The user's subsequent sharper-tail and shrinking-window refinement has
now passed internal review and is recorded in
[the sharp-tail rate](COEFFICIENT_ONE_SHARP_TAIL_RATE_20260908.md).
It strengthens this result without being a premise of its proof.
