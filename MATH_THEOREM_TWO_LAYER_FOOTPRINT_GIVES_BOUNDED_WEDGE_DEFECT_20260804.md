# Linear owner and quadratic terminal footprints give bounded wedge defect

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional endpoint-factorized bounded-defect theorem.  It
strengthens the uniform-terminal estimate in the linear-footprint theorem
by using the exact overlap geometry of the q1 terminal clouds.  It does not
derive the required physical footprint or its regeneration from the
current Pascal construction.

## 0. Setting and conclusion

Let

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal U={ [2m-1]\choose m},\qquad
 \mathcal Z={ [2m-1]\choose m+1},
\]

and fix distinct required lower turns

\[
 L_1,\ldots,L_p\in\mathcal L,
 \qquad 1\le p\le m-1.
\]

Assume the same raw endpoint-factorized cap face as in the protected-wedge
activation theorem: before a frozen background is deleted, every direct
branch

\[
 L_i\longrightarrow L_i+a\longrightarrow L_i+a+b
\tag{0.1}
\]

is present, typed legal and completion-stable; distinct owner and terminal
values use distinct unit capacities; source occurrences are protected; and
there are no unpriced hidden branch capacities.

Let

\[
 D_{\mathcal U}\subseteq\mathcal U,quad |D_{\mathcal U}|=f,
 \qquad
 D_{\mathcal Z}\subseteq\mathcal Z,quad |D_{\mathcal Z}|=g
\tag{0.2}
\]

be the unavailable owner and q1-terminal values.  Put

\[
 r_i=|D_{\mathcal U}\cap N_{\mathcal U}(L_i)|,
 \qquad
 s_i=|D_{\mathcal Z}\cap N_{\mathcal Z}(L_i)|,
\tag{0.3}
\]

where the two clouds have sizes (m) and ({m\choose2}), respectively.
Define

\[
 T={m-p+1\choose2},
\tag{0.4}
\]

\[
 \Phi(f,p)=
 {f+\sqrt{f^2+4fp(p-1)}\over2},
\tag{0.5}
\]

and

\[
 \Psi(g,p,m)=
 {g+\sqrt{g^2+4g(m-1)p(p-1)}\over2}.
\tag{0.6}
\]

For any integer (R\) with

\[
 1\le R\le m,
 \qquad
 S_R:=T-{R-1\choose2}>0,
\tag{0.7}
\]

put

\[
 C_R=
 \left\lfloor{\Phi(f,p)\over R}\right\rfloor+
 \left\lfloor{\Psi(g,p,m)\over S_R}\right\rfloor.
\tag{0.8}
\]

### Theorem

All but at most

\[
 \boxed{\min_R C_R}
\tag{0.9}
\]

required lower turns admit a simultaneous globally owner/terminal-distinct
active-wedge selection and pairwise private direct routing.

In particular, for fixed constants (A,D,C\), if

\[
 f\le Am,
 \qquad g\le Dm^2,
 \qquad p\le C\sqrt m,
\tag{0.10}
\]

then the number of omitted turns is (O_{A,D,C}(1)).  One explicit
eventual bound is

\[
 \boxed{
 \left\lfloor A+\sqrt{A^2+4AC^2}\right\rfloor
 +
 \left\lfloor
 2\left(D+\sqrt{D^2+4DC^2}\right)
 \right\rfloor.
 }
\tag{0.11}
\]

Thus the cap may damage a quadratic number of distinct q1-terminal values,
not merely a linear number, without causing an unbounded one-coordinate
wedge sidecar.

## 1. Local badness uses the terminal incidence, not its global size

At (L_i), exactly ({r_i\choose2}) wedges have both owner alternatives
damaged.  The map

\[
 \{a,b\}\longmapsto L_i\cup\{a,b\}
\]

is injective, so exactly (s_i) wedges have damaged q1 terminal.  The two
classes may overlap; therefore the active menu obeys

\[
 |W_i^c|
 \ge {m\choose2}-{r_i\choose2}-s_i.
\tag{1.1}
\]

The exact simultaneous packing threshold is

\[
 B_{p-1}(m)={m\choose2}-T.
\tag{1.2}
\]

Hence (L_i) is certainly packable whenever

\[
 {r_i\choose2}+s_i<T.
\tag{1.3}
\]

Call a source **bad** when the reverse weak inequality holds.

## 2. Owner incidence energy

Two distinct lower turns have at most one common rank-(m) owner.  For
each damaged owner (U\), let

\[
 d_U=|\{i:L_i\subset U\}|.
\]

Then

\[
 \sum_{U\in D_{\mathcal U}}{d_U\choose2}\le {p\choose2}.
\tag{2.1}
\]

Writing (I=\sum_i r_i=\sum_Ud_U\), Cauchy--Schwarz gives

\[
 I\le\Phi(f,p),
\tag{2.2}
\]

with (I=0) when (f=0).  This is the exact owner-star energy bound.

## 3. Terminal incidence energy

For two distinct lower turns, write

\[
 d=|L_i\setminus L_j|=|L_j\setminus L_i|.
\]

Their union has rank (m-1+d).  A common rank-((m+1)) terminal exists
only for (d\le2).  At (d=1), there are exactly (m-1) common
terminals; at (d=2), there is exactly one; and at (d>2), there are
none.  Consequently

\[
 |N_{\mathcal Z}(L_i)\cap N_{\mathcal Z}(L_j)|\le m-1.
\tag{3.1}
\]

For each damaged terminal (Z\), let

\[
 e_Z=|\{i:L_i\subset Z\}|.
\]

Counting pairs of sources inside damaged terminal clouds and using (3.1),

\[
 \sum_{Z\in D_{\mathcal Z}}{e_Z\choose2}
 \le (m-1){p\choose2}.
\tag{3.2}
\]

Let (J=\sum_i s_i=\sum_Ze_Z\).  For (g>0), Cauchy--Schwarz gives

\[
 {J^2\over g}
 \le\sum_Ze_Z^2
 =J+2\sum_Z{e_Z\choose2}
 \le J+(m-1)p(p-1).
\tag{3.3}
\]

Solving the quadratic inequality yields

\[
 \boxed{J\le\Psi(g,p,m).}
\tag{3.4}
\]

When (g=0), (J=0), agreeing with (0.6).

## 4. Split every bad source between the two layers

Fix (R) satisfying (0.7).  A bad source with (r_i<R) has

\[
 {r_i\choose2}\le {R-1\choose2}
\]

and therefore, by (1.3),

\[
 s_i\ge T-{R-1\choose2}=S_R.
\tag{4.1}
\]

Thus every bad source lies in the union of

\[
 \{i:r_i\ge R\}
 \quad\hbox{and}\quad
 \{i:s_i\ge S_R\}.
\]

Equations (2.2) and (3.4) give

\[
 \#\{i:r_i\ge R\}
 \le\left\lfloor{\Phi(f,p)\over R}\right\rfloor,
\tag{4.2}
\]

\[
 \#\{i:s_i\ge S_R\}
 \le\left\lfloor{\Psi(g,p,m)\over S_R}\right\rfloor.
\tag{4.3}
\]

This proves the bad-source bound (0.8)--(0.9).

Remove the bad sources.  Every retained menu is larger than
(B_{p-1}(m)).  The exact active-wedge packing theorem applies to the
smaller family because its own threshold is no larger.  It selects wedges
with all owner and terminal values distinct; choosing one active owner side
then gives pairwise private direct routes under the endpoint-factorized
premise.

## 5. Constant evaluation

Assume (0.10) and take

\[
 R=\lfloor m/2\rfloor+1.
\tag{5.1}
\]

For all sufficiently large (m), (p\le m/4), and

\[
 S_R
 ={m-p+1\choose2}-{\lfloor m/2\rfloor\choose2}
 \ge {m^2\over4}.
\tag{5.2}
\]

As in the owner-only theorem,

\[
 \Phi(f,p)
 \le {m\over2}
 \left(A+\sqrt{A^2+4AC^2}\right).
\tag{5.3}
\]

Since (R>m/2), the first summand of (0.8) is at most the first
summand in (0.11).

Also (p(p-1)\le C^2m) and (m-1\le m), so

\[
 \Psi(g,p,m)
 \le {m^2\over2}
 \left(D+\sqrt{D^2+4DC^2}\right).
\tag{5.4}
\]

Divide (5.4) by (5.2) to obtain the second summand in (0.11).  This proves
the constant conclusion.

## 6. Useful refinements

### 6.1 Pairwise nonadjacent sources

If the (L_i) are pairwise nonadjacent in the Johnson graph, then their
owner stars are disjoint and their terminal clouds meet in at most one
value.  In that case

\[
 I\le f,
 \qquad
 J\le {g+\sqrt{g^2+4gp(p-1)}\over2}.
\tag{6.1}
\]

Substituting these sharper quantities into (0.8) improves the constant.

### 6.2 Hidden branch holes

If source (i) has (h_i) additional wedges killed by explicitly priced
hidden resources, replace (s_i) in (1.1) by (s_i+h_i).  If
(H=\sum_i h_i\), then (4.3) is replaced by

\[
 \#\{i:s_i+h_i\ge S_R\}
 \le\left\lfloor{\Psi(g,p,m)+H\over S_R}\right\rfloor.
\tag{6.2}
\]

Deleted source occurrences must still be added directly to the sidecar.

### 6.3 Factor completion

The endpoint-only packing/routing conclusion does not itself build the
Middle-Levels factor.  To protect the selected full wedges inside the
small protected-factor theorem, one separately requires

\[
 2p'+|P_*|\le m-2,
\tag{6.3}
\]

where (p') is the number of retained sources and (P_*\) is the incumbent
protected incidence bank.  This is automatic for (p'=O(\sqrt m)) and a
fixed incumbent bank for all sufficiently large (m).

## 7. Regenerative two-layer footprint target

The cap row would have bounded one-coordinate wedge defect if the
same-parity construction proved, in one endpoint-factorized state,

\[
 p=O(\sqrt m),\qquad
 |D_{\mathcal U}|=O(m),\qquad
 |D_{\mathcal Z}|=O(m^2),
\tag{7.1}
\]

with only (O(m^2)) explicitly priced hidden wedge holes and with the
resulting constant sidecar regenerated rather than accumulated.

This is strictly weaker on the terminal layer than the earlier linear
footprint target.  It is also robust to a long compensation linkage whose
q1 projection is quadratic, provided its owner projection remains linear.

The current record does not prove (7.1), endpoint factorization, or
nonaccumulation.  It therefore does not by itself prove (B(k)+O(1)).

## 8. Dependencies

- `MATH_THEOREM_CAP_AWARE_PROTECTED_WEDGE_ACTIVATION_AND_EXACT_MENU_THRESHOLD_20260804.md`
- `MATH_THEOREM_LINEAR_LAYER_FOOTPRINT_GIVES_BOUNDED_WEDGE_DEFECT_20260804.md`
- `MATH_THEOREM_SEPARATED_TURN_STARS_ONE_STEP_FULL_PORT_LINKAGE_20260804.md`
