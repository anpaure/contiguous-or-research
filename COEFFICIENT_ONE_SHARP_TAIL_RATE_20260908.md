# Strongest recorded explicit PBBS rate

Date: 2026-09-08. The sharp exterior estimate, removal of the cutoff shift,
shrinking-window argument and logarithmic balance were supplied by the
user. Root and independent mathematical subagents checked their proofs
and extracted the numerical constants below. The full-cube result is on
the inherited finite PBBS inputs and retains the manuscript's proposed-
proof status. Internal reviews are not external or formal certification.

All logarithms are natural. Define

\[
 A=2^{2097152},\quad p=A^{-1/2}=2^{-1048576},\quad
 k_* =\left\lceil\exp\!\left(\exp(2^{1048616})\right)\right\rceil.
\]

## Numerical conclusions

For every integer k>=k_*,

\[
 \boxed{\frac{\nu(k)}{W(k)}\le1+
 2^{76}\frac{(\log\log k)^{\,3/2+2^{-1048577}}}
                 {(\log k)^{\,2^{-1048577}}}.} \tag{1}
\]

Thus C=2^76, the logarithmic exponent is2^-1048577, and the iterated-
logarithm exponent is3/2+2^-1048577. At the SAME threshold there is the
simpler C=1 corollary

\[
 \boxed{\nu(k)\le W(k)\left(1+(\log k)^{-2^{-1048578}}\right).} \tag{2}
\]

Since W(k)<=B(k)<=nu(k), either excess bound also bounds nu(k)-B(k)
after multiplication by W(k). These deliberately conservative constants
are not useful numerically at k=17. Its full-cube bounds remain
24313<=nu(17)<=25745.

## Unconditional finite exterior theorem

For the existing product-SCD exterior word and every r>=1,1<=H<=r,

\[
 \boxed{\frac{2L_r(r-H)}{W_r}
  \le\Theta_{r,H}\frac{\binom{2r}{r-H}}{\binom{2r}{r}}
  \le32\left(1+\frac{H^2}{r}\right)e^{-H^2/(r+1/2)},}
\]
\[
 \Theta_{r,H}=
 \frac{8(r+1)(r+H)(H^2-H+r)}{(2r+1)(r+2)^2}
                   \left(1+\frac1H\right)^3.
\]

Here W_r=binomial(2r+1,r). The proof keeps the total chain-pair deficit,
uses Vandermonde, and telescopes the exact identity

\[
 \sum_{q=H}^r q^3\binom{2r}{r-q}
  =\frac{(r+H)(H^2-H+r)}2\binom{2r}{r-H}.
\]

It includes H=1,r=1. At H=floor(c sqrt(r))+1, r>=16 and
c^2<=loglog r, the fully numerical tail estimate is

\[
                       2L_r(r-H)/W_r\le48(1+c^2)e^{-c^2}.
\]

[The complete finite proof](scratch/SHARP_PRODUCT_SCD_EXTERIOR_BOUND_INDEPENDENT_AUDIT_20260908.md)
also records one independently executed exact rational check on h100:

\[
 0.000037923376245\le
 \Theta_{1000,120}\frac{\binom{2000}{880}}{\binom{2000}{1000}}
 <0.000037923376246<1/25000.
\]

That is an upper bound for the exterior word covering ranks at most880
or at least1121 in dimension2001. It is not a full-cube cost.

## Complete probability and compiler proof

The complete independently reviewed derivation is
[the shrinking-window sharp-rate proof](scratch/PBBS_SHRINKING_WINDOW_SHARP_RATE_COMPLETE_INDEPENDENT_AUDIT_20260908.md).
It contains all of the following steps and numerical comparisons.

1. The pre-averaging clock estimate, with
   D_*=2^12 exp(2^19), gives beta=2^37 exp(2^19) and
   mu_H(Pi)<=2^28 exp(D_*) b^2 Q exp(beta bQ) for H<=b sqrt(r).
   The case of query depth below two is included. The constant exp(D_*)
   stays outside the profile-dependent exponential.
2. Average cutoffs from floor(c sqrt(r)) to
   floor((c+1/c)sqrt(r)). This integer set has at least sqrt(r)/c
   members. The profilewise cutoff strip is charged explicitly;
   the original no-success coefficient100/log r can be enlarged to128.
3. Retain the profile cap and use the sharp moment
   E[Q^v exp(uQ)]<=2^26(1+u)^3 exp(u^2). At the stated fixed p,
   pD_*<=1 and beta p<=1. Keeping these factors until p is selected
   gives packing prefactor2^68, and compiler prefactor2^73.
4. For r>=2^1000000 and1<=c<=sqrt(loglog r), the finite compiled bound is

\[
\begin{aligned}
 \frac{\nu(2r+1)}{W_r}\le1
 &+\frac{c+1}{\sqrt r}+2^{73}c^{2p+4}e^{c^2-py}\\
 &+e^{A(c+2)^2}r^{-1/400}+48(1+c^2)e^{-c^2},
 \qquad y=\log\log r.
\end{aligned}
\]

5. Choose c^2=py/2-(p+1)log(y)/2. At the stated k_* threshold,
   y>=2^39 sqrt(A) and py>=2^39. The function(log y)/y decreases,
   proving admissibility at every larger dimension. Both main terms
   have order y^((p+3)/2)exp(-py/2). The other two are smaller;
   absorption of their growing exponential is made at this larger
   A-dependent threshold, not at r=2^1000000.
6. The odd-dimensional constant is at most2^74. The exact trimmed
   lift doubles length and width, and the log conversion costs at
   most two. The conservative2^76 proves (1). At k>=k_*,
   76log2+((p+3)/2)logloglog k<=p loglog k/4, proving (2).

In the general notation the rate is

\[
 O\!\left((\log\log k)^{(3+A^{-1/2})/2}
                       (\log k)^{-1/(2\sqrt A)}\right).
\]

It has a larger boundary exponent than the preceding terminal bound
and replaces its exp(C sqrt(loglog k)) factor by the displayed fixed
iterated-logarithm power. The comparison uses a COMMON admissible A.
The finite literal compiler covers all ranks and charges every join;
one can enumerate its admissible apertures and retain the shortest word.

The full proofs are linked above, with earlier numerical PBBS inputs
linked from them. No unavailable verifier package was treated as evidence.
Neither this rate nor the finite exterior theorem proves nu(k)=B(k).
