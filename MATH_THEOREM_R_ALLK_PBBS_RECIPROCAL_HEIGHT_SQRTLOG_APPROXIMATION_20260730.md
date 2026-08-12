# Reciprocal-height PBBS packing gives an `O(sqrt(log k))` approximation

Date: 2026-07-30  
Lane: R, pure-mathematics all-`k` lane  
Status: unconditional theorem from previously audited PBBS support, seam,
deck, and Dyck-height estimates.  No finite search or solver is used.

## 0. The theorem

There is an absolute constant `C` such that, for every `k>=2`,

\[
 \boxed{
 \nu(k)\le
 C\sqrt{\log(k+2)}
 {k\choose\lfloor k/2\rfloor}.}                    \tag{0.1}
\]

Consequently

\[
 \boxed{\frac{\nu(k)}{B(k)}=O(\sqrt{\log k})
        =o(\sqrt k).}                               \tag{0.2}
\]

This improves the unconditional half-cube estimate from handoff item 1969,
whose approximation factor was `Theta(sqrt(k))`.  It does not prove
`B(k)+O(k)` or coefficient one.

The construction is one literal nonzero word.  In odd dimension it uses
the PBBS central-band word at

\[
                         H=\left\lceil
                         \sqrt{2m\log(m+2)}\right\rceil               \tag{0.3}
\]

and appends every target outside that band literally.  Even dimensions use
the exact word `A,{z},z+A`.

## 1. Imported uniform PBBS estimates

Put

\[
 n=2m+1,\qquad W={n\choose m},\qquad
 B_m=\operatorname{Cat}_m={W\over n}.                \tag{1.1}
\]

For an integer `H>=1` satisfying `2H<=m+1`, the audited dominance-staircase
and endpoint-capped erosion construction produces a literal nonzero word
covering every target in the central rank band

\[
 m+1-H,\ m+2-H,\ldots,m+1+H.                        \tag{1.2}
\]

Let `bar_nu_H` be the maximum packing of nonwrapping short-return intervals
on the long PBBS quotient cycles, and let `Z_H` count quotient edges on
cycles of length at most `H+1`.  Its exact length `L_H` obeys

\[
 {L_H-W\over W}
 \le {2H\over n}
 +4(5H-1){\overline\nu_H\over B_m}
 +2(5H-1){Z_H\over B_m}.                             \tag{1.3}
\]

The independently audited height-gap and Dyck-spectrum theorem gives an
absolute `C_0` with

\[
 \overline\nu_H
 \le\sum_{h\le H-1}{b_{m,h}\over h+2}
 \le C_0{B_m\over\sqrt m}                            \tag{1.4}
\]

for every `H`; restricting the sum can only decrease it.  Voltage-itinerary
rigidity gives

\[
                         Z_H\le(2H+2)n^{2H+2}.        \tag{1.5}
\]

These are respectively equation (4.3) and the boxed reciprocal-sum estimate
(0.3) proved in (5.1)--(5.3) of
`MATH_ATTACK_L_CORRECTED_CHRONOLOGY_TRACE_GATE_20260725.md`, and the
uniform voltage bound (17.2) of
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`.  The literal central-band
construction is proved in Sections 21 and 24 of the latter file.

The quantifier in (1.4) is important.  The full reciprocal-height sum is a
uniform absolute estimate, not merely the later `O_A` notation of (5.4)
for fixed Gaussian width.  This permits the slowly growing choice (0.3).

## 2. Central-band cost at growing width

Take `H` from (0.3).  For all sufficiently large `m`,

\[
                         2H\le m+1.                  \tag{2.1}
\]

The first two terms of (1.3) satisfy

\[
 {2H\over n}=O\left(\sqrt{{\log m\over m}}\right),  \tag{2.2}
\]

\[
 4(5H-1){\overline\nu_H\over B_m}
 \le20C_0{H\over\sqrt m}
 =O(\sqrt{\log m}).                                  \tag{2.3}
\]

The short-cycle term is negligible.  Indeed,

\[
 H\log n=O(\sqrt m(\log m)^{3/2})=o(m),             \tag{2.4}
\]

so (1.5) gives `H Z_H=exp(o(m))`.  The standard Catalan lower bound

\[
                         B_m\ge c_0{4^m\over m^{3/2}}                 \tag{2.5}
\]

therefore implies

\[
                         {H Z_H\over B_m}=o(1).       \tag{2.6}
\]

Substitution in (1.3) proves

\[
 \boxed{L_H=O(\sqrt{\log m}\,W).}                   \tag{2.7}
\]

Every letter counted here is literal and nonempty.  The estimate does not
combine independently chosen rankwise factors: all central ranks come from
one PBBS factor with its exact cut charts.

## 3. The outer Boolean tail is negligible

Append once, as a one-cell word, every nonempty mask whose rank is outside
the band (1.2).  Let `R_H` be their number.  Every outside rank `s` has

\[
                         |s-n/2|\ge H.               \tag{3.1}
\]

Hoeffding's inequality and (0.3) give

\[
 \begin{aligned}
 {R_H\over2^n}
 &\le2\exp\left(-{2H^2\over n}\right)\\
 &\le2(m+2)^{-4m/(2m+1)}
 =O(m^{-4/3}).                                      \tag{3.2}
 \end{aligned}
\]

The elementary central-binomial lower bound

\[
                         W\ge c_1{2^n\over\sqrt m}  \tag{3.3}
\]

then yields

\[
                         R_H=O(m^{-5/6}W)=o(W).      \tag{3.4}
\]

The concatenation of the central word and these literal tail masks is
universal: the first block covers the entire band, and every target outside
the band is its own one-letter interval.  Equations (2.7) and (3.4) prove

\[
 \nu(2m+1)=O(\sqrt{\log m}\,W).                     \tag{3.5}
\]

No witness is lost when the tail is appended.

## 4. Even dimensions

Let `A` be the odd word on `[2m+1]` and add a new coordinate `z`.  The word

\[
                         A,\ \{z\},\ z+A             \tag{4.1}
\]

is universal on `[2m+2]`: the first copy covers old targets, the central
letter covers `{z}`, and the tagged copy covers every `{z} union S` with
nonempty old part `S`.  Moreover

\[
 {2m+2\choose m+1}=2{2m+1\choose m}.                \tag{4.2}
\]

Thus (3.5) gives the same `O(sqrt(log k))` factor in even dimension.  The
finitely many dimensions excluded by (2.1) are absorbed into the absolute
constant `C`, proving (0.1).

## 5. Exact scope

Proved:

1. an unconditional `O(sqrt(log k))` approximation in one literal word;
2. the growing-width use of the previously proved reciprocal-height PBBS
   trace bound; and
3. exact parity transfer with no mixed-boundary hypothesis.

Not proved:

1. the critical little-oh improvement in the reciprocal-height packing
   needed for coefficient one;
2. `B(k)+O(k)`;
3. a flat depth-`d(k)` PBBS compiler; or
4. any uniform candidate-multiplicity assertion.

The result is orthogonal to the exact compiler expansion gate: it bypasses
deep source synchronization by supplying the exponentially small outer tail
literally, while keeping the PBBS central band globally correlated.
