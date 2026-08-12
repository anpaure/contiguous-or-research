# Independent proof audit: product-Johnson seam extension and rare-defect
# containers

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_PRODUCT_JOHNSON_SEAM_LOCAL_EXTENSION_AND_RARE_DEFECT_CONTAINERS_20260804.md`  
**Verdict:** PASS at the stated conditional scope.  The theorem gives exact
counts and sufficient seam-survival criteria; it does not establish that the
current complete host relation has any of the required decompositions.

## 1. Parameter audit

The eligible token has

\[
 |J\cap H|=R-D,\qquad |J-H|=D-1,
 \qquad J\cap F=\varnothing.                         \tag{1.1}
\]

With

\[
 A=H-F,\quad |A|=p=R-1-a,
 \qquad B=H^c-F,\quad |B|=q=R-b,                    \tag{1.2}
\]

the old-shore selection has size `R-D`; its complement inside `A` therefore
has size

\[
 p-(R-D)=R-1-a-R+D=D-1-a=h.                         \tag{1.3}
\]

The new-shore selection has size `ell=D-1`.  Hence the asserted bijection

\[
 S_D(H;F)\longleftrightarrow {A\choose h}\times{B\choose\ell}     \tag{1.4}
\]

is exact.  The feasibility inequalities are precisely `0<=h<=p` and
`0<=ell<=q`, equivalent to the source inequalities on `a,b`.

Edge cases are handled:

* `h=0` makes the old-shore factor a singleton;
* `ell=0` is not used in the one-pivot regime `D>=2`, but the formulas remain
  valid;
* a binomial coefficient with an impossible lower argument is declared
  zero.

## 2. Local projection audit

For one prescribed local state `(S,T)`, the outside choices are independent
because `A-U` and `B-V` are disjoint shores.  Their exact number is

\[
 {p-u\choose h-|S|}{q-v\choose\ell-|T|}.             \tag{2.1}
\]

Different `(S,T)` give disjoint state fibres.  Therefore summation in
Theorem 2.1 neither misses nor double-counts a seam.

The extension interval on the old shore follows from

\[
 0\le h-|S|\le p-u,qquad 0\le|S|\le u,              \tag{2.2}
\]

and is exactly

\[
 \max\{0,h-(p-u)\}\le|S|\le\min\{h,u\}.             \tag{2.3}
\]

The new shore is identical.  To make **every** local state extend, it is
necessary and sufficient that both endpoints `0,u` lie in (2.3), namely

\[
                         u\le h,qquad u\le p-h.      \tag{2.4}
\]

This confirms Corollary 2.3 and its symmetric condition on `v`.

The running-intersection specialization uses that theorem only to identify
the exact projected local state set.  It does not claim that occurrence
variables are coordinate variables.  The scope is correct.

## 3. Occurrence-exception audit

On a `q1`-exact carrier, each lower colour labels one seam, so the map from
eligible token values to their seam occurrences is injective.  A fixed bank
of `e` occurrences removes at most `e` members of any coordinate-accepted
family.  Therefore

\[
                         |accepted|\ge A_{U,V}(L)-e  \tag{3.1}
\]

is exact as a lower bound.  No independence between the coordinate and
occurrence conditions is assumed.

The theorem correctly distinguishes a fixed union bank `E` from a moving
one-occurrence explanation attached separately to every seam.

## 4. Cylinder audit

For an old-shore cylinder with `i` forced holes and `o` forced nonholes,
the remaining choice is an `(h-i)`-subset of `p-i-o` coordinates.  Hence

\[
 {p-i-o\choose h-i}/{p\choose h}
 ={(h)_i(p-h)_o\over(p)_{i+o}}.                      \tag{4.1}
\]

The same calculation gives the new-shore factor, proving the exact product
weight in Lemma 4.1.

For the rare-degree bound, dropping all forced-nondefect conditions enlarges
the cylinder.  Thus

\[
 w(C)\le{(h)_i\over(p)_i}{(\ell)_j\over(q)_j}
 \le\left({h\over p-t+1}\right)^i
    \left({\ell\over q-t+1}\right)^j.               \tag{4.2}
\]

This confirms Corollary 4.3.  It makes no claim when a certificate has zero
positive sparse literals.

The transversal theorem is also exact: choosing both defect sets outside a
transversal invalidates at least one required positive literal of every
cylinder.  Forced negative literals cannot restore a cylinder after a
required positive literal fails.

## 5. Barrier audit

The singleton cover is valid because every nonempty fixed-size defect set
contains a coordinate.  Its support hypergraph is an edgeless collection of
singletons, yet the corresponding events cover the whole slice.  Therefore
disjoint coordinate footprints are not an ordinary dependency graph under
fixed-cardinality sampling.

The complementary unary pair

\[
                         x\in P\quad\text{or}\quad x\notin P             \tag{5.1}
\]

is a cover by two proper relations when `0<h<p`.  This independently shows
that a constant number of bounded-scope, individually feasible constraints
can have empty common acceptance.

The occurrence singleton cover is valid by the same injective seam map used
positively in Theorem 3.1.  Hence the theorem does not silently infer a
small global exception set from small per-event occurrence scope.

## 6. Module-scope audit

The applicability table in the theorem is conservative.

* Coordinate avoidance and the aperture sphere are exact value-level rows.
* A fixed finite occurrence reservation is legitimately charged to `E`.
* The lower multisocket constraints quantify over global path subfamilies.
* Upper witness survival and component topology depend on the full
  occurrence chronology.
* The residual router is an all-cut physical occurrence statement after a
  frozen compensation deletion.

No cited source currently proves that the latter three dependencies factor
through a fixed bounded coordinate projection or a small occurrence bank.
The theorem therefore does not promote its seam criteria to `PPC(1)`.

## 7. Final audit verdict

The exact statements checked are:

1. the product-Johnson defect parametrization;
2. the local-state extension count and its positivity interval;
3. the hybrid coordinate/occurrence lower bound;
4. the exact hypergeometric cylinder weight;
5. the weighted and transversal seam-survival criteria; and
6. the counterexamples to scope-only local-lemma reasoning.

All are valid.  The open premise is structural: prove that the actual joint
lower/upper/router bad set has one of the three `PSSC` forms.  No finite
search or solver output is used in this audit.

