# Audit of the binary-rotor de Bruijn/divergence/skeleton theorem

Date: 2026-07-26

Source audited:
`MATH_THEOREM_BINARY_ROTOR_DEBRUIJN_DIVERGENCE_AND_MINIMAL_SKELETON_20260726.md`.

## Verdict

The requested mathematical claims are correct in the final source.  In
particular, I found no reversal of the (A/B) labels, no off-by-one error
in the suffix indices, and no sign error in the divergence identity or
LP dual.

The audit and concurrent strengthening made three points explicit:

1. the literal repair cost is
   (2\mathcal M_H^-+(H+1)a), because lower holes are appended once and
   the upper-hole bound contains a second copy of the lower-hole count;
2. the cumulative supporting-wreath cut strengthens the switch lower
   bound all the way to (a\ge(1/2-o(1))W), so the sparse-switch compiler
   is formally correct but unusable for (H\to\infty); the surviving
   gate is signed-divergence cancellation;
3. Theorem 4.1 now includes the implicit no-premature-recurrence argument
   needed to justify the claimed ((n-1)^2) states.

## 1. Clustered de Bruijn equivalence

An injective ((n-1))-word (e=(x_1,\ldots,x_{n-1})) determines the
state ((x_1,\ldots,x_{n-1},x_n)), where (x_n) is the missing symbol.
At (h(e)=(x_2,\ldots,x_{n-1})), the two possible outgoing arcs are

\[
 (x_2,\ldots,x_{n-1},x_1),\qquad
 (x_2,\ldots,x_{n-1},x_n),
\]

which are exactly the (A)- and (B)-successor states.  Both arcs
leaving a fixed de Bruijn vertex have the same middle-owner colour.
Thus the owner equation makes selected outdegree at most one; flow
balance then makes selected indegree and outdegree both zero or both
one.  This proves both directions of Theorem 1.1 and uniqueness of the
reconstructed rotor transition.

The projected matrix in Corollary 1.2 has row sums one by the owner
equations and column sums one by summing conservation over all vertices
of a fixed next-owner colour.  Its support is on
(X\mapsto X-\{x_1\}+\{x_{m+1}\}), hence on directed Johnson edges.

## 2. Divergence indices, sign, and compiler

For

\[
 K_r(e)=\{x_{n-r+1},\ldots,x_{n-1}\},
\]

the last internal (r)-block (positions (n-r,\ldots,n-1)) of the
successor is

\[
 \begin{cases}
 K_r(e)\cup\{x_n\},&B\text{-transition},\\
 K_r(e)\cup\{x_1\},&A\text{-transition}.
 \end{cases}
\]

Internal-block stationarity identifies the load of these successor
blocks with (L_r), whereas (R_r) counts
(K_r(e)\cup\{x_n\}) for every selected root.  Therefore the displayed
sign is indeed

\[
 R_r-L_r=\sum_ez_e^A
 \bigl(\mathbf e_{K_r(e)\cup\{x_n\}}
       -\mathbf e_{K_r(e)\cup\{x_1\}}\bigr).
\]

Both terms are distinct adjacent vertices of (J(n,r)).  Equal total
mass gives

\[
 \sum_T(L_r-R_r)_+=\tfrac12\|R_r-L_r\|_1\le a,
\]

and hence (M(R_r)\le M(L_r)+a).

For (r=m-q), the suffix counted by (R_r) is precisely the complement
of the prefix of size (m+1+q).  To linearize a component, the largest
required prefix has length (m+1+H), so repeating the first (m+H)
symbols is exactly sufficient.  The lower repairs cost
(\mathcal M_H^-), while the upper repairs cost at most
(\mathcal M_H^-+(H+1)a).  This verifies all terms in

\[
 W+C(m+H)+2\mathcal M_H^-+(H+1)a.
\]

Keeping cancellation before the triangle inequality gives the valid
replacement

\[
 W+C(m+H)+2\mathcal M_H^-+\mathfrak D_H(z).
\]

## 3. Switch and run bounds

Every non-pure component with (a_C) (A)-transitions has (a_C)
maximal (B)-runs, each of length at most (n-1); a pure (B)-orbit
has length (n).  Summation gives Theorem 3.2:

\[
 W\le(n-1)a+nc_0.
\]

The stronger adjacent-run cut in the current source also checks.  The
cyclic orders supporting consecutive runs differ by one adjacent
transposition.  Exactly two of their (n) length-(m) cyclic-interval
sets change, so the two supports share at least (n-2) owners.
Disjointness of selected owners therefore forces

\[
 \ell_i+\ell_{i+1}\le n+2.
\]

Summing cyclically yields

\[
 W\le\frac{n+2}{2}a+nc_0,
\]

and consequently (a\ge(2-o(1))W/(n+2)) when
(C=o(W/m)).  The parity observation used there is valid: (A) is odd,
(B) is even, and the free action on injective states forces a closed
component to contain an even number of (A)-moves.

More decisively, each next supporting wreath differs by an adjacent
swap and therefore adds at most two new owner sets to the union.  A
non-pure component with (a_C) switches consequently has at most
(n+2(a_C-1)) distinct owners.  Summing components gives

\[
 W\le nC+2a-2c_1,
\]

so (C=o(W/m)) forces (a\ge(1/2-o(1))W).  This cumulative cut is
valid and is strictly stronger than the adjacent-length average.

## 4. Full-run collapse and reset count

For a full run, if (h_j) is its omitted point then

\[
 AB^{-1}h_j=Bh_{j+1},\qquad
 B^{-1}AB^{-1}=A^{-1},
\]

so (h_{j+1}=A^{-1}h_j).  Since (A) rotates the first (n-1)
coordinates, its orbit has length (n-1).  The added source sentence
now explicitly rules out two earlier holes in one (B)-orbit: their
two ((n-1))-subsets of the same (n)-state orbit would intersect.

Writing a hole as ((c_1,\ldots,c_{2m},z)), its successive supporting
(B)-orders insert (z) in the gaps of one fixed (2m)-cycle.  A
middle interval either avoids (z) (at most (2m) possibilities) or,
after deleting (z), is an ((m-1))-interval of that cycle (again at
most (2m)).  This verifies the (2(n-1)) owner bound of Theorem 4.2.

After deleting all short runs, full runs split into at most (s_C)
blocks.  Each block has at most (2(n-1)) possible owners and each short
run contributes at most (n-2), giving

\[
 W\le nc_0+(3n-4)s.
\]

Moreover, the adjacent-run cut forbids adjacent full runs for (n\ge5),
so (s\ge a/2).  Together with the global supporting-wreath cut this
gives the current (s\ge(1/4-o(1))W).  Thus Theorem 4.4 is correct in both its
coarse and sharpened forms.

## 5. Macro composition and LP dual

A run of ℓ states makes ℓ-1 (B)-moves followed by (A), so

\[
 F_\ell=AB^{\ell-1}.
\]

Then

\[
 F_\ell^{-1}F_{\ell+1}=B,
 \qquad A=F_\ell B^{-(\ell-1)},
\]

and ⟨(F_\ell,F_{\ell+1})⟩=⟨(A,B)⟩=(S_n).  Proposition
4.5 is therefore correct (and, as stated in the source, is only an
ambient reachability result).

Finally, the cycle master is exact.  An owner equality excludes a cycle
that repeats an owner and excludes two chosen cycles sharing a de Bruijn
vertex, because their outgoing arcs there have the same owner.  For the
minimization primal with owner equalities and covering inequalities, the
dual owner variables are free and the covering variables are
nonnegative.  Hence (5.2), including the direction

\[
 \sum_Xa_X(C)\alpha_X+\sum_Tb_T(C)\beta_T\le1,
\]

has the correct signs.

## Final status

The note is valid as a conditional reduction and obstruction theorem.
It does **not** prove the remaining integral clustered cycle cover
(6.1).  The surviving task is a low-component integral rounding with
aggregate lower holes (o(W)) and aggregate nested divergence
(\mathfrak D_H=o(W)); the source correctly labels that construction as
open.
