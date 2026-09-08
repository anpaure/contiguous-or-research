# Independent audit: two-layer footprint gives bounded wedge defect

**Date:** 2026-08-04  
**Method:** pure mathematics; independent line-by-line replay; no computation,
search, or solver  
**Audited theorem:**
`MATH_THEOREM_TWO_LAYER_FOOTPRINT_GIVES_BOUNDED_WEDGE_DEFECT_20260804.md`  
**Audited theorem SHA-256:**
`42b522abb25158fe06ca54a60b10ad6b3a9b7028e55e640c595d4f385b5befe8`  
**Author self-audit:**
`MATH_AUDIT_TWO_LAYER_FOOTPRINT_GIVES_BOUNDED_WEDGE_DEFECT_SELF_20260804.md`  
**Author self-audit SHA-256:**
`6b0a4885ba66f0fe8642a13b45774d878a086e544755587f16335bee7c0d31d3`  
**Verdict:** **GO in the stated endpoint-factorized scope.**

No mathematical correction is required.  The conclusion is a
collision-free active-wedge selection with private direct routes.  As the
theorem itself records, extension of that selected bank to a spanning
middle-levels two-factor requires the separate protected-incidence budget.

## 1. Local active-menu count

For a fixed source \(L_i\), its \(m\) rank-\(m\) owner extensions are
indexed by the coordinates outside \(L_i\), and its q1 terminals are in
bijection with unordered pairs of those coordinates:

\[
 \{a,b\}\longmapsto L_i\cup\{a,b\}.
\]

Consequently, if \(r_i\) owner extensions are unavailable, exactly
\({r_i\choose2}\) wedges have both possible owner sides unavailable.  If
\(s_i\) terminals in the source's terminal cloud are unavailable, exactly
\(s_i\) wedges have unavailable terminal.  These two loss classes may
overlap, so the union bound is

\[
 |W_i^c|\ge {m\choose2}-{r_i\choose2}-s_i.
\]

Since

\[
 B_{p-1}(m)
 ={m\choose2}-{m-p+1\choose2}
 ={m\choose2}-T,
\]

the strict sufficient condition for the exact packing theorem is precisely

\[
 {r_i\choose2}+s_i<T.
\]

Declaring the reverse weak inequality to be bad is therefore conservative
and proof-safe.  It need not characterize every individually packable
menu; it only has to contain every menu not certified by this count.

## 2. Owner-star energy

Two distinct rank-\((m-1)\) sources have at most one common rank-\(m\)
owner: any such owner must equal their union.  If

\[
 d_U=|\{i:L_i\subset U\}|,
\]

then each pair of sources contributes to at most one term, giving

\[
 \sum_{U\in D_{\mathcal U}}{d_U\choose2}\le {p\choose2}.
\]

With

\[
 I=\sum_i r_i=\sum_{U\in D_{\mathcal U}}d_U,
\]

Cauchy--Schwarz over the \(f\) damaged owners yields, for \(f>0\),

\[
 {I^2\over f}
 \le \sum_Ud_U^2
 =I+2\sum_U{d_U\choose2}
 \le I+p(p-1).
\]

Solving the resulting quadratic gives exactly

\[
 I\le
 \Phi(f,p)
 ={f+\sqrt{f^2+4fp(p-1)}\over2}.
\]

The separately stated \(f=0\) case has \(I=0\), as required.

## 3. Terminal-cloud intersections and energy

Let

\[
 d=|L_i\setminus L_j|=|L_j\setminus L_i|
\]

for two distinct rank-\((m-1)\) sources.  Their union has rank
\(m-1+d\).  A common rank-\((m+1)\) terminal must contain this union.
Therefore:

* if \(d=1\), the union has rank \(m\), and there are exactly
  \((2m-1)-m=m-1\) choices for the final coordinate;
* if \(d=2\), the union itself is the unique common terminal; and
* if \(d>2\), the union is too large and no common terminal exists.

Thus

\[
 |N_{\mathcal Z}(L_i)\cap N_{\mathcal Z}(L_j)|\le m-1.
\]

For

\[
 e_Z=|\{i:L_i\subset Z\}|,
\]

the sum \(\sum_Z{e_Z\choose2}\) counts pairs of sources together with a
damaged terminal containing both.  Each source pair is counted at most
\(m-1\) times, so

\[
 \sum_{Z\in D_{\mathcal Z}}{e_Z\choose2}
 \le (m-1){p\choose2}.
\]

Writing

\[
 J=\sum_i s_i=\sum_{Z\in D_{\mathcal Z}}e_Z,
\]

Cauchy--Schwarz over the \(g\) damaged terminals gives, for \(g>0\),

\[
 {J^2\over g}
 \le \sum_Ze_Z^2
 =J+2\sum_Z{e_Z\choose2}
 \le J+(m-1)p(p-1).
\]

Hence

\[
 J^2-gJ-g(m-1)p(p-1)\le0,
\]

whose positive root is exactly

\[
 J\le
 \Psi(g,p,m)
 ={g+\sqrt{g^2+4g(m-1)p(p-1)}\over2}.
\]

For \(g=0\), both \(J\) and the displayed formula are zero.

## 4. Bad-source split

Fix any integer \(R\) in the theorem's admissible range and put

\[
 S_R=T-{R-1\choose2}>0.
\]

If a bad source satisfies \(r_i<R\), then

\[
 {r_i\choose2}\le {R-1\choose2}
\]

and badness forces

\[
 s_i\ge T-{R-1\choose2}=S_R.
\]

Thus the bad set is contained in

\[
 \{i:r_i\ge R\}\cup\{i:s_i\ge S_R\}.
\]

The incidence-sum bounds imply

\[
 \#\{i:r_i\ge R\}
 \le\left\lfloor{\Phi(f,p)\over R}\right\rfloor,
\]

and

\[
 \#\{i:s_i\ge S_R\}
 \le\left\lfloor{\Psi(g,p,m)\over S_R}\right\rfloor.
\]

No disjointness of these two heavy sets is assumed; the union bound gives
\(C_R\).  Every admissible \(R\) independently covers the full bad set,
so minimizing these valid upper bounds over \(R\) is legitimate.

After deleting the bad sources, say \(p'\le p\) remain.  Every retained
menu is strictly larger than \(B_{p-1}(m)\), while

\[
 B_{p'-1}(m)\le B_{p-1}(m).
\]

The exact active-wedge packing theorem therefore selects wedges with all
owner and q1-terminal values distinct.  Under the raw endpoint-factorized
premise, choosing a surviving owner side of every selected wedge gives
pairwise private direct routes: the source occurrences are protected,
values correspond to distinct unit capacities, the endpoint layers are
disjoint, and there is no unpriced shared interior capacity.

## 5. Asymptotic constant

Assume fixed nonnegative \(A,D,C\) and

\[
 f\le Am,\qquad g\le Dm^2,\qquad p\le C\sqrt m.
\]

Take

\[
 R=\lfloor m/2\rfloor+1.
\]

This is admissible for all sufficiently large \(m\).  Moreover,

\[
 S_R
 ={m-p+1\choose2}- {\lfloor m/2\rfloor\choose2}.
\]

Its leading quadratic term is \(3m^2/8\), while the loss caused by
\(p=O(\sqrt m)\) is only \(O(m^{3/2})\).  Therefore

\[
 S_R\ge {m^2\over4}
\]

eventually.  Also \(R>m/2\), and the owner-energy estimate gives

\[
 \Phi(f,p)
 \le {m\over2}\left(A+\sqrt{A^2+4AC^2}\right).
\]

For the terminal term, using \(m-1\le m\) and
\(p(p-1)\le C^2m\),

\[
 \Psi(g,p,m)
 \le {m^2\over2}\left(D+\sqrt{D^2+4DC^2}\right).
\]

Dividing by \(R\) and \(S_R\), respectively, and taking floors yields the
claimed explicit bound

\[
 \left\lfloor A+\sqrt{A^2+4AC^2}\right\rfloor
 +
 \left\lfloor
 2\left(D+\sqrt{D^2+4DC^2}\right)
 \right\rfloor.
\]

The estimate remains valid when \(A=0\) or \(D=0\), using the separately
handled zero-footprint cases.

## 6. Refinements and scope

The pairwise-Johnson-nonadjacent refinement is valid.  In that case owner
stars are disjoint, so \(I\le f\), and terminal clouds meet in at most one
value, so the terminal pair-energy loses the factor \(m-1\).

The hidden-hole extension is also valid.  If \(h_i\) additional wedge
pairs at source \(i\) are killed by explicitly priced hidden resources,
then

\[
 \sum_i(s_i+h_i)=J+H\le\Psi(g,p,m)+H,
\]

and the stated Markov bound follows.  Deleted source occurrences must be
paid separately.

The proof establishes only the endpoint-factorized packing/routing result.
It does not itself materialize that cap face.  In particular, it does not
derive completion-stable occurrence maps, phase typing, the owner or
terminal footprint bounds, hidden-resource pricing, or regeneration.

If the selected wedges must be embedded in a spanning middle-levels
two-factor, the separate dependency condition

\[
 2p'+|P_*|\le m-2
\]

is still required.  In the intended \(p'=O(\sqrt m)\) regime with a fixed
incumbent bank, it holds eventually, exactly as the theorem states.

## 7. Conclusion

The two-layer theorem is mathematically sound within its explicit literal
endpoint-factorized scope.  The q1-terminal improvement is genuine: the
bounded intersection multiplicity of distinct terminal clouds turns an
\(O(m^2)\) global terminal footprint into only \(O(1)\) bad source menus
when \(p=O(\sqrt m)\).  The remaining unproved input is the regenerative
physical realization of that footprint, not the incidence-energy or
packing argument audited here.
