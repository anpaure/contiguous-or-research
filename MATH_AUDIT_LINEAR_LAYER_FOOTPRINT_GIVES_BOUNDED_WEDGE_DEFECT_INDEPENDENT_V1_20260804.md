# Independent audit: linear layer footprint gives bounded wedge defect

**Date:** 2026-08-04  
**Method:** pure mathematics; independent line-by-line replay; no computation,
search, or solver  
**Audited theorem:**
`MATH_THEOREM_LINEAR_LAYER_FOOTPRINT_GIVES_BOUNDED_WEDGE_DEFECT_20260804.md`  
**Audited theorem SHA-256:**
`242c752d5344a00658d821f2e0b0b0210e0a3dc3d923903be1a96a2bba1fcd16`  
**Author self-audit:**
`MATH_AUDIT_LINEAR_LAYER_FOOTPRINT_GIVES_BOUNDED_WEDGE_DEFECT_20260804.md`  
**Author self-audit SHA-256:**
`61244b8d9cff9459f525465fa459b010c0cbbe1a61d22c62774b304f1c1a54c9`  
**Verdict:** **GO in the stated endpoint-factorized scope.**

No mathematical correction is required.  Two scope clauses must remain
explicit when the theorem is cited:

1. every use of \(\rho\) is on the face \(g<T\) (as imposed by its
   definition); and
2. the conclusion gives the collision-free active-wedge selection and
   private direct routes.  Extension of that selected bank to a spanning
   middle-levels two-factor still requires the separate degree-compatible
   incidence budget from the packing theorem.

## 1. Local active-menu union bound

Fix a lower turn \(L_i\).  Its \(m\) owner extensions are in bijection
with the coordinates outside \(L_i\), and its wedges are the unordered
pairs of those extensions.

If

\[
 r_i=|D_{\mathcal U}\cap N(L_i)|,
\]

then exactly \({r_i\choose2}\) wedges have both owner sides unavailable.
For fixed \(L_i\), the terminal map

\[
 \{a,b\}\longmapsto L_i\cup\{a,b\}
\]

is injective, so the global bank \(D_Z\) kills at most \(g\) additional
wedges at this source.  The two types of loss may overlap, which only
improves the lower bound.  Therefore

\[
 |W_i^c|\ge {m\choose2}-{r_i\choose2}-g.
\]

With

\[
 T={m-p+1\choose2},\qquad
 B_{p-1}(m)={m\choose2}-T,
\]

the strict inequality

\[
 {r_i\choose2}+g<T
\]

is exactly what is needed to obtain
\(|W_i^c|>B_{p-1}(m)\).  On the face \(g<T\), minimality in the
definition

\[
 \rho=\min\{r\ge0:{r\choose2}+g\ge T\}
\]

therefore makes every source with \(r_i<\rho\) nonheavy and admissible.
Since \(g<T\), one also has \(\rho\ge2\), so the later division by
\(\rho\) is legitimate.

This count uses the full endpoint-factorized premise.  Namely, after the
frozen background is imposed, a direct branch may fail only through its
priced owner or q1-terminal endpoint.  Any further complete branch killer
belongs in the explicit \(H_i\) extension of Section 5, not in the main
endpoint-only row.

## 2. Owner-star intersection energy

For two distinct rank-\((m-1)\) turns \(L_i,L_j\), a common rank-\(m\)
owner, if it exists, must equal \(L_i\cup L_j\).  Hence their owner stars
intersect in at most one value.

Writing

\[
 d_U=|\{i:L_i\subset U\}|,
\]

each pair of source turns is consequently counted by at most one damaged
owner, and

\[
 \sum_{U\in D_{\mathcal U}}{d_U\choose2}\le {p\choose2}.
\]

For

\[
 I=\sum_i r_i=\sum_{U\in D_{\mathcal U}}d_U,
\]

Cauchy--Schwarz over the \(f\) damaged owners gives, when \(f>0\),

\[
 {I^2\over f}
 \le \sum_Ud_U^2
 = I+2\sum_U{d_U\choose2}
 \le I+p(p-1).
\]

Thus

\[
 I^2-fI-fp(p-1)\le0
\]

and the nonnegative root gives exactly

\[
 I\le
 \Phi(f,p)={f+\sqrt{f^2+4fp(p-1)}\over2}.
\]

The case \(f=0\) is correctly split off, with \(I=0\).  If \(h\)
sources are owner-heavy, then \(h\rho\le I\), whence

\[
 h\le\left\lfloor{\Phi(f,p)\over\rho}\right\rfloor.
\]

No independence assumption on the damaged owner incidences is used.

## 3. Selection of the nonheavy family

Let \(p'\le p\) be the number of nonheavy sources.  Every retained menu is
strictly larger than \(B_{p-1}(m)\), and monotonicity gives

\[
 B_{p'-1}(m)\le B_{p-1}(m).
\]

The exact active-menu theorem therefore applies to the smaller family and
selects wedges with all owner values and all q1-terminal values distinct.
Because the selected wedge is active, it has at least one owner side
outside \(D_{\mathcal U}\) and its terminal is outside \(D_Z\).  Choosing
such a side gives pairwise private direct routes under the literal
endpoint-factorization hypothesis: sources are protected and distinct,
owner and terminal values have distinct physical capacities, the layers
are disjoint, and no unpriced interior capacity remains.

This step proves routing.  If a spanning two-factor containing the selected
wedges is also claimed, one must additionally invoke the dependency's
degree compatibility and edge-budget row

\[
 2p'+|P_*|\le m-2.
\]

That row is not needed for the bounded route/sidecar statement itself.

## 4. Asymptotic evaluation

Assume fixed nonnegative constants \(A,G,C\), with

\[
 f\le Am,\qquad g\le Gm,\qquad p\le C\sqrt m.
\]

Eventually \(p\le m/4\), and

\[
 {m-p+1\choose2}-\left({\lfloor m/2\rfloor\choose2}+Gm\right)>0,
\]

because the first term has quadratic leading coefficient \(1/2\), the
binomial on the left of the subtraction has leading coefficient \(1/8\),
and the \(p\)-dependent loss is only \(O(m^{3/2})\).  In particular
\(g<T\) eventually.  Since even \(r=\lfloor m/2\rfloor\) does not meet
the defining threshold for \(\rho\), integrality gives

\[
 \rho>{m\over2}.
\]

Also \(p(p-1)\le C^2m\), and \(\Phi\) is nondecreasing in its
nonnegative inputs, so

\[
 \Phi(f,p)
 \le {m\over2}\left(A+\sqrt{A^2+4AC^2}\right).
\]

Combining the last two displays gives a strict ratio bound by the displayed
constant, and hence

\[
 \left\lfloor{\Phi(f,p)\over\rho}\right\rfloor
 \le
 \left\lfloor A+\sqrt{A^2+4AC^2}\right\rfloor.
\]

The edge case \(A=0\) is consistent: \(D_{\mathcal U}=\varnothing\), so
there are no owner-heavy sources.

## 5. Hidden losses and exact scope

The Section 5 extension is conservative and valid.  At source \(i\), an
explicit set \(H_i\) of additional fully killed wedge pairs can be added
to the terminal loss budget.  Overlap with endpoint losses can only weaken,
not invalidate, the resulting lower bound.  A uniform
\(\rho_i\ge\rho_*\) again gives at most \(\Phi(f,p)/\rho_*\) heavy
sources.  Deleted required sources must be paid separately, as stated.

The theorem does **not** derive any of the following:

* the endpoint-factorized physical cap state;
* the linear owner/q1-terminal footprint;
* a bound on unpriced hidden branch killers;
* factor completion without its separate edge budget;
* transported phase-one authenticity, two-coordinate product closure, or
  nonaccumulating regeneration.

It also does not refute the snake obstruction.  It bypasses the need for a
per-path crossing bound only after the **total distinct endpoint footprint**
has independently been bounded linearly.

## 6. Conclusion

The theorem is correct within its stated literal endpoint-factorized
scope.  Its quantitative core is exact enough for the claimed purpose:
when \(p=O(\sqrt m)\), an \(O(m)\) damaged owner layer can make only
\(O(1)\) of the protected source stars cross the active-menu threshold.
The unproved all-dimensional input remains Regenerative LLF, not any step
of the incidence-energy argument audited here.
