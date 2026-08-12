# Audit: linear layer footprint gives bounded wedge defect

**Date:** 2026-08-04  
**Method:** independent line-by-line mathematical replay; no computation,
search, or solver  
**Audited theorem:**
`MATH_THEOREM_LINEAR_LAYER_FOOTPRINT_GIVES_BOUNDED_WEDGE_DEFECT_20260804.md`  
**Audited theorem SHA-256:**
`242c752d5344a00658d821f2e0b0b0210e0a3dc3d923903be1a96a2bba1fcd16`  
**Verdict:** **GO within the stated endpoint-factorized scope.**

## 1. Local menu count

For a fixed lower turn (L_i), the map from an unordered extension pair
({a,b}) to its terminal (L_i+a+b) is injective.  Exactly
({r_i\choose2}) wedges have both owners in the damaged owner set, and at
most (g) further wedges have damaged terminal.  Hence the union bound

\[
 |W_i^c|\ge {m\choose2}-{r_i\choose2}-g
\]

is valid, with overlap only improving it.  Since

\[
 B_{p-1}(m)={m\choose2}-{m-p+1\choose2},
\]

the strict menu row follows exactly from
({r_i\choose2}+g<{m-p+1\choose2}).  The definition of (ho) is valid
when (g<T), and then every (r_i<ho) satisfies that strict row.

## 2. Incidence energy bound

Two distinct rank-((m-1)) sets have at most one common rank-(m)
superset.  Thus each pair of source stars contributes to at most one
damaged owner and

\[
 \sum_{U\in D_{\mathcal U}}{d_U\choose2}\le {p\choose2}.
\]

With (I=\sum_i r_i=\sum_Ud_U), Cauchy--Schwarz gives, for (f>0),

\[
 I^2/f\le\sum_Ud_U^2
 =I+2\sum_U{d_U\choose2}
 \le I+p(p-1).
\]

The positive root of (I^2-fI-fp(p-1)\le0) is precisely

\[
 \Phi(f,p)={f+\sqrt{f^2+4fp(p-1)}\over2}.
\]

For (f=0), (I=0) separately.  If (h) sources have (r_i\geho),
then (h\rho\le I\le\Phi(f,p)), proving
(h\le\lfloor\Phi(f,p)/\rho\rfloor).

## 3. Packing and routing

After deleting the heavy sources, let (p'\le p) remain.  Every retained
menu is strictly larger than (B_{p-1}(m)), while monotonicity gives
(B_{p'-1}(m)\le B_{p-1}(m)).  The exact active-wedge packing theorem
therefore selects wedges with all owner and terminal values distinct.
Every selected wedge is active by construction, so choosing one surviving
owner side gives the private direct routes under the theorem's explicit
endpoint-factorized capacity premise.

No suffix-gammoid inference, rank-monotone path claim, or unpriced hidden
capacity is used here.

## 4. Asymptotic evaluation

For fixed (C,G), (p\le C\sqrt m) implies (p\le m/4) eventually, and

\[
 {\lfloor m/2\rfloor\choose2}+Gm
 <{m-p+1\choose2}
\]

eventually because the right-minus-left quadratic leading coefficient is
positive.  Hence (ho>m/2).  Also, from (f\le Am) and
(p(p-1)\le C^2m),

\[
 \Phi(f,p)\le {m\over2}
 \left(A+\sqrt{A^2+4AC^2}\right).
\]

Dividing by (ho>m/2) and taking floors proves the displayed constant
casualty bound.  The case (A=0) is consistent: there is no owner damage
and therefore no heavy source.

## 5. Edge cases and scope checks

- The hypotheses include (1\le p\le m-1), as required by the packing
  threshold.
- When (g<T), (ho\ge2), so the denominator is nonzero.
- Terminal holes are counted injectively only within a fixed source, which
  is all the local menu estimate requires.
- The result bounds a sidecar, not exact zero defect.
- Source deletions and hidden branch killers are not absorbed silently;
  Section 5 prices them explicitly.
- The proof does not derive endpoint factorization, a linear physical
  footprint, phase-one transport, product closure, or regeneration.

## 6. Audit conclusion

The theorem is mathematically sound under its stated literal-capacity
premises.  Its substantive new point is that a linear number of damaged
owner values cannot nearly saturate more than (O(1)) of the fixed lower
stars when (p=O(\sqrt m)).  This bypasses the earlier per-path
rank-crossing obstruction for an additive-constant goal, but it leaves the
Regenerative LLF premise open.
