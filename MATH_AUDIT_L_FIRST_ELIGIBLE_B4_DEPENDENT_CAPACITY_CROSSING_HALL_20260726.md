# Independent audit of the unified first-eligible dependent-capacity Hall report

Date: 2026-07-26

Audited source:
`MATH_ATTACK_L_FIRST_ELIGIBLE_B4_DEPENDENT_CAPACITY_CROSSING_HALL_20260726.md`.

Method: pure mathematics only.

## 0. Certification

Theorems A and B are mathematically correct in their stated support regimes.
The robust suffix proof agrees with the prior independent audit: it covers
arbitrary affine phases, arbitrary direction orders, and repeated visits to
one active \(B_4\)-block because it uses only constancy of the physical
suffix on a component. The triangular theorem is correctly restricted to
the one-touch fibre.

The explicit choice of \(x_A\) in (4.11) does give \(\kappa_A>0\). The
good-component capacity identity (4.5) is exact, and the bad-component
envelope is correctly upgraded from raw \(U_m\) to \(U_{\mathrm{eff}}\).

Four clarifications are required.

1. Define “fractional uncovered mass” everywhere as
   \[
      D_q^\pm=\sum_T(1-\ell_q^\pm(T))_+.
   \]
   It is not the number of targets having zero fractional load.
2. In Theorem A, state explicitly that an adaptive mixed-seed packetization
   is included only when its scan is causal/predictable at each fresh block
   and its owner-importing bad-associated occurrence mass obeys the
   \(U_{\mathrm{eff}}\) bound. The fixed canonical packetization itself
   needs no extra assumption.
3. State that “contained in the active coordinates” means every vertex of a
   good component has one common restriction outside those coordinates and
   that the component supplies one signed depth-\(q\) occurrence per weighted
   phase owner. These are exactly the facts used in (4.5).
4. If “full affine cube group” means the full affine linear group
   \(\operatorname{AGL}(2r,2)\), the phrase is false: a general linear map
   need not preserve cube edges or literal one-swap transitions. Replace it
   by “the physical cube automorphism group
   \(\mathbb F_2^{2r}\rtimes S_{2r}\), together with any audited affine
   phase/resolution choices that still produce literal components.” Theorem A
   covers all such literal components because only suffix support matters.

With those clarifications, the final escape boundary is accurate. In
particular, Theorem A does not cover a cross-packet/affine operation whose
physical component changes a coordinate of the protected suffix.

## 1. Theorem A assumptions and localization

For the canonical first-eligible support, eligibility in each fresh
four-block has probability \(1/4\). Before the terminal quarter there are
\((3/8+o(1))m\) blocks, so the mean eligibility count is
\((3/32+o(1))m\). The condition \(r\le m/16\) leaves a fixed linear
Chernoff margin and proves (3.4). Dividing the unconditional failure
probability by

\[
 2^{-2m}\binom{2m}m=\Theta(m^{-1/2})
\]

justifies the exact-middle localization.

For mixed seeds, the same binomial statement is valid when the requested
seed is measurable with respect to the anchor and preceding scan data before
the current block is exposed. The report says this in the paragraph after
Lemma 3.1; it should also be incorporated into Theorem A if that extension is
advertised there.

The owner-importing correction is correct:

\[
 U_{\mathrm{eff}}
 =U_m^{\mathrm{leave}}+(3/2)^rU_m^{\mathrm{bad}}
 =e^{-\Omega(m)}W
\]

when \(r=o(m)\). The factor \((3/2)^r\) is the ratio between the union
\(6^r\) of all local seed supports and the canonical packet size \(4^r\).

## 2. Good/bad component capacity

For a good component, suffix conservation gives the pointwise equivalence

\[
 \tau_{q,C}^-(X)\in\mathcal Z_{q,a}^-
 \iff |X\cap R|\le a.                               \tag{A.1}
\]

Therefore (4.5) is an equality before its final inequality. Exact fractional
ownership gives

\[
 \sum_X\mathbf1_{\{|X\cap R|\le a\}}
       \sum_{C\ni X,\,C\ {m good}}x_C\le B_a.     \tag{A.2}
\]

Every bad-associated weighted phase occurrence is charged to an owner in
the audited exceptional union, so its total is at most
\(U_{\mathrm{eff}}\). Thus

\[
 \sum_{T\in\mathcal Z_{q,a}^-}\ell_q^-(T)
 \le B_a+U_{\mathrm{eff}}.                          \tag{A.3}
\]

Equation (A.3) implies the precise fractional conclusion

\[
 \sum_T(1-\ell_q^-(T))_+
 \ge|\mathcal Z_{q,a}^-|-B_a-U_{\mathrm{eff}},       \tag{A.4}
\]

and similarly above. For integral loads, the left side is exactly the
number of holes. Hence Proposition 4.1 is correct once “fractional uncovered
mass” is explicitly defined by (A.4).

## 3. Explicit \(\kappa_A\)

Put \(d=A\sqrt{2/3}\),

\[
 u_A=\max\left\{1,\frac{A^2+\log2+1}{d}\right\},
 \qquad x_A=d+u_A.
\]

The Mills bounds give

\[
 \frac{\Phi(-u_A)}{\Phi(-(u_A+d))}
 \ge
 \frac{u_A(u_A+d)}{u_A^2+1}
 e^{u_Ad+d^2/2}.                                    \tag{A.5}
\]

Since \(u_A\ge1\), the prefactor is at least \(1/2\). Also
\(u_Ad\ge A^2+\log2+1\), including when the maximum defining \(u_A\)
is attained at one. Consequently the logarithm of the right side of (A.5)
is strictly larger than \(A^2\). Thus

\[
 e^{-A^2}\Phi(d-x_A)-\Phi(-x_A)>0,
\]

and (4.12) is fully explicit and correct.

The hypergeometric constants used with it are also correct:

\[
 v=3/32,qquad d=(A/4)/\sqrt{3/32}=A\sqrt{2/3},
 \qquad N_q/W\to e^{-A^2}.
\]

## 4. Theorem B and fractional language

The packet-choice dual (2.2) is correct. A packet has \(4^r\) phase owners
and at most \(4^r\) distinct targets at one signed depth; no factor of
\(2h\) is missing.

The chronology identity (5.4), the source and target Hoeffding exponents,
and the choice \(q=\lceil20\sqrt{r\log m}\rceil\) all check out. In
particular,

\[
 q^2/(4r+2)=(100+o(1))\log m,
 \qquad q^2/(20r)=(20+o(1))\log m.
\]

For fractional choices, (6.12)--(6.14) must consistently use the deficit
\(D_q^\pm=\sum_T(1-\ell_q^\pm(T))_+\). With that convention the restoration
argument in (6.14) is valid: exceptional occurrence mass \(B_q^\pm\) can
reduce fractional deficit by at most \(B_q^\pm\).

## 5. Escape boundary

The final boundary is certified. The suffix proof survives every operation
which acts only inside a fixed normal packet support, even if it revisits
blocks, changes direction order, or destroys packetwise injectivity. It can
be escaped only by an operation which invalidates common suffix conservation,
for example:

1. a moving family of ambient block orders with no common positive-density
   frozen suffix;
2. a component joining owners with different suffix restrictions;
3. a physical transition using a suffix coordinate; or
4. leaving the exact-owner packet architecture for unrestricted SCI owner
   recycling.

These are necessary escape categories, not sufficient constructions. The
report correctly makes no claim against unrestricted SCI.
