# The planted coatom breakers remove every rational coupled-depth invariant below q1

Date: 2026-08-01  
Lane: R, coatom flag transport and terminal compiler linkage  
Status: unconditional signed-catalogue theorem in the central Boolean
range and independent harmonic proof.  Its rational conclusion has since
been strengthened integrally in
`MATH_THEOREM_R_COATOM_BREAKER_FULL_INTEGRAL_PRODUCT_AND_COMPILER_BOUNDARY_20260801.md`.
This note remains an independent check that no higher Boolean harmonic
invariant survives.  It does not prove nonnegative physical reachability, a
terminal common-cap matching, or `B(k)+O(1)`.

## 0. Result and exact scope

Fix

\[
 d\ge 3,\qquad r\ge d+4,\qquad
 v\in\{2r-1,2r\},\qquad |\Omega|=v,
\]

and put

\[
 g=r-d-2,qquad k_t=g+1+t=r-d-1+t
       \quad(1\le t\le d-1).
\]

Thus `t=d+1-q` corresponds to lower depth `q`, and `k_t=r-q`.
For each layer let

\[
 V_t=\mathbb Q^{\binom{\Omega}{k_t}},\qquad
 \partial_t e_X=\sum_{x\in X}e_x,qquad
 K_t=\ker\partial_t.
\]

For a packet replacement `P`, let \(\sigma_{2:d}(P)\) denote the direct sum of
its signed lower occurrence increments at depths `q=2,...,d`.  Let `M` be
the rational span of the complete injective coordinate-relabelling orbit of
the following vectors \(\sigma_{2:d}(P)\) and their reverses.

1. The canonical common-order coatom packet, with every ordering of the
   internal fillers `f_1,...,f_d` and with its two extreme bridge fillers
   fixed.
2. The authoritative endpoint-planted packet with first `Iab` omission
   order

   \[
                  (p,f_1,\ldots,f_d,f_0)
   \]

   and upper-screen set `E={0,2,4,6,8,10}`.
3. For every admissible internal adjacent pair, the same planted packet
   with `f_s,f_(s+1)` transposed only in the label-attached `Ica` block.

The untwisted and twisted planted actions both belong to the catalogue, so
their signed difference belongs to `M`.  This is the incremental breaker
used below.

### Theorem 0.1 (full rational coupled span)

\[
 \boxed{
 M=\bigoplus_{t=1}^{d-1}K_t.
 }
 \tag{0.1}
\]

Equivalently, the only rational linear invariants of the complete
all-depth occurrence action are the coordinate degrees in each depth
separately.  In particular:

* the common-order reflection law is completely removed;
* no higher Boolean harmonic invariant replaces it; and
* there is no remaining rational cross-depth moment obstruction in the
  complete relabelled catalogue.

Here and throughout, “all-depth” means the movable lower decks
`q=2,...,d`.  The immediate `q=1` palette is deliberately not in (0.1):
within each current local replacement, the old and new phases have the same
q1 multiset and the same two attachment endpoints.  Section 6 records the
resulting frozen boundary-Hall countercondition for a serial walk.

The theorem is deliberately not a fixed-carrier assertion.  The canonical
common-order packet orbit and the planted-breaker orbit need not all occur
as slots in one chronology.  Equation (0.1) is a signed catalogue-span
identity.

For `d=2` there is only one nontrivial depth and the ordinary integral
Pluecker theorem already gives (0.1); no reflection breaker is needed.

## 1. Exact canonical action

Let

\[
 F=\{f_1,\ldots,f_d\},\qquad
 P_t=\{f_1,\ldots,f_t\},\qquad
 S_t=\{f_{d-t+1},\ldots,f_d\},
\]

and choose a disjoint core `G` of size `g` and distinct active labels
`a,b` outside (G\cup F).  At layer `t` the canonical signed action is

\[
 \Delta_t=
 e_{G\cup\{a\}\cup P_t}
 +e_{G\cup\{b\}\cup S_t}
 -e_{G\cup\{b\}\cup P_t}
 -e_{G\cup\{a\}\cup S_t}.
 \tag{1.1}
\]

Every coordinate has the same total multiplicity with each sign in (1.1),
so

\[
                         \partial_t\Delta_t=0.       \tag{1.2}
\]

The same point balance holds for the planted adjacent-order breakers.  It
follows immediately that

\[
                         M\subseteq\bigoplus_tK_t.   \tag{1.3}
\]

The rest of the proof establishes the reverse inclusion.

## 2. Boolean harmonic decomposition

For `0<=j<=k<v/2`, write

\[
                         H_j=S^{(v-j,j)}.
\]

The rank-`k` Boolean permutation module has the multiplicity-free
decomposition

\[
 \mathbb Q^{\binom{\Omega}{k}}
      =H_0\oplus H_1\oplus\cdots\oplus H_k.          \tag{2.1}
\]

Here (H_0\oplus H_1) is exactly the row space of the point-incidence map;
therefore

\[
                 \ker\partial_k=H_2\oplus\cdots\oplus H_k.    \tag{2.2}
\]

In the present range `k_t<=r-2<v/2`.  Hence

\[
 \bigoplus_{t=1}^{d-1}V_t
   =\bigoplus_{j=0}^{r-2}H_j\otimes\mathbb Q^{T_j},  \tag{2.3}
\]

where the multiplicity index set is the interval

\[
 T_j=\{t:L_j\le t\le d-1\},\qquad
 L_j=\max(1,j-g-1).                                  \tag{2.4}
\]

Empty `T_j` are omitted.  Because the catalogue is closed under every
coordinate relabelling, `M` is an `S_v`-submodule.  Semisimplicity lets us
analyze each `H_j`-isotypic component independently.

## 3. The quadratic component is already complete

For one layer define pair incidence by

\[
 D_t(z)_{xy}=\sum_{X\supseteq\{x,y\}}z_X.            \tag{3.1}
\]

On the decomposition (2.1), `D_t` annihilates every `H_j` with `j>2` and
is a nonzero equivariant map on `H_2`.  Since `H_2` occurs once on each
side, this restriction is an isomorphism up to a nonzero scalar.

The planted adjacent-order theorem gives, integrally, the full product of
the zero-point-degree pair-current lattices over all depths.  Its diagonal
increment at the reflected pair selected by `s` is the primitive square

\[
 [f_0f_s]+[f_{s+1}p]-[f_0f_{s+1}]-[f_sp],           \tag{3.2}
\]

and all later reflected coordinates vanish.  Canonical packets supply the
reflection-even part and descending triangular elimination supplies the
reflection-odd part.  Consequently

\[
             M\cap(H_2\otimes\mathbb Q^{T_2})
                   =H_2\otimes\mathbb Q^{T_2}.       \tag{3.3}
\]

The scalar `2` obtained by testing (3.2) with one cut functional is not an
index-two obstruction: (3.2) itself is a primitive four-cycle, and such
cycles generate the pair-current lattice integrally.  This observation is
specific to the quadratic projection.  It does not prove integral
saturation in higher harmonic degrees.

## 4. Polytabloid step probes for every higher component

Fix `j>=3` with `T_j` nonempty.  We prove that the canonical packet orbit
alone supplies

\[
                         H_j\otimes\mathbb Q^{T_j}.  \tag{4.1}
\]

### 4.1 The tests

For disjoint ordered coordinate pairs `(u_i,v_i)`, `1<=i<=j`, define on a
uniform layer

\[
 \Phi(S)=\prod_{i=1}^j
       \bigl({\bf1}_{u_i\in S}-{\bf1}_{v_i\in S}\bigr).       \tag{4.2}
\]

When `j<=min(k,v-k)`, this is a nonzero Boolean polytabloid of shape
`(v-j,j)` and hence lies in `H_j`.  Such polytabloids span `H_j`.

Take `(u_1,v_1)=(a,b)`.  Choose the remaining positive labels as a set
`A_s` of size `j-1`, with some labels in `F` and all remaining labels in
`G`.  Choose their negative mates distinctly in

\[
                       Z=\Omega\setminus(G\cup F\cup\{a,b\}). \tag{4.3}
\]

No mate in `Z` occurs in any of the four terms of (1.1).  Direct
substitution therefore gives

\[
 \langle\Phi,\Delta_t\rangle
  =2\bigl({\bf1}_{A_s\cap F\subseteq P_t}
           -{\bf1}_{A_s\cap F\subseteq S_t}\bigr).             \tag{4.4}
\]

### 4.2 Exact choice of labels

For every `s in T_j`, choose the filler part of `A_s` as follows.

* If `L_j=1` and `s=1`, use `{f_1}`.
* If `L_j=1` and `s>=2`, use `{f_1,f_s}`.
* If `L_j>=2`, use

  \[
                         \{f_1,\ldots,f_{L_j-1},f_s\}.          \tag{4.5}
  \]

Fill the remaining positions of `A_s` with distinct labels of `G`.
These choices are possible:

* when `L_j=1,s=1`, one needs `j-2<=g` core labels;
* when `L_j=1,s>=2`, one needs `j-3<=g` core labels; and
* when `L_j>=2`, the definition `L_j=j-g-1` leaves exactly `g` core
  labels.

Every selected filler set contains `f_1`.  Since `1<=t<=d-1`, no suffix
`S_t` contains `f_1`.  The first indicator in (4.4) is one exactly when
`t>=s`.  Hence

\[
                \boxed{\langle\Phi_s,\Delta_t\rangle
                        =2{\bf1}_{\{t\ge s\}}.}       \tag{4.6}
\]

The absent mates also exist.  The union
\(G\cup F\cup\{a,b\}\) has exactly `r` labels, so

\[
 |Z|=v-r\ge r-1,
 \qquad j-1\le r-3.                                  \tag{4.7}
\]

Thus there are enough distinct negative mates for every occurring `H_j`.

### 4.3 Triangularity

Restricted to `t in T_j`, the vectors

\[
                    \bigl({\bf1}_{\{t\ge s\}}\bigr)_{t\in T_j},
                    \qquad s\in T_j,                \tag{4.8}
\]

form a unit lower-triangular matrix.  They are a basis of
\(\mathbb Q^{T_j}\).  Matrix coefficients of the `H_j` projections of catalogue
vectors therefore span the full multiplicity space.  Since `H_j` is
irreducible and `M` is `S_v`-stable, this proves (4.1).

For completeness, the module step used here is exact.  If an irreducible
`S_v`-module `H` occurs with multiplicity set `T`, every `S_v`-submodule of

\[
                              H\otimes\mathbb Q^T
\]

has the form \(H\otimes L\) for a subspace
\(L\subseteq\mathbb Q^T\).  Moreover `L` is the span of all coefficient
vectors

\[
                  (\ell(w_t))_{t\in T},\qquad
                  w=(w_t)_{t\in T}\in M,\quad \ell\in H^*.
\]

This follows from semisimplicity and
\(\operatorname{End}_{S_v}(H)=\mathbb Q\).  The coefficient vectors (4.6)
span all of \(\mathbb Q^{T_j}\), so the corresponding `L` is the full
multiplicity space.

If one identifies the copies of `H_j` at different ranks using normalized
intertwiners, (4.6) becomes

\[
                         2c_{j,t}{\bf1}_{\{t\ge s\}},
\]

with every \(c_{j,t}\) nonzero.  The same matrix remains triangular and
invertible.  Thus the conclusion is independent of normalization.

Combining (3.3) and (4.1) for all `j>=3`, and using (2.2), proves the reverse
inclusion in (1.3), hence Theorem 0.1.

## 5. Exact invariant corollary

### Corollary 5.1

Let `L` be a rational linear functional on the direct sum of the depth
decks.  If `L` is unchanged by every complete relabelling of every canonical
packet and every planted adjacent-order breaker, then there are constants
\(c_{t,x}\) such that

\[
                         L(z)=\sum_{t=1}^{d-1}
                              \sum_{x\in\Omega}c_{t,x}
                              \sum_{X\ni x}z_t(X).    \tag{5.1}
\]

Thus invariant hunting at higher moments cannot yield another rational
obstruction for this complete catalogue.

#### Proof

The annihilator of `M` is, by (0.1), the direct sum of the row spaces of
the maps \(\partial_t\).  Equation (5.1) is exactly a general element of that
row space. \(\square\)

## 6. What remains for compiler linkage

The theorem closes the algebraic question raised by the single-block
reflection breaker, but it does not close physical or compiler reachability.
The boundaries are exact.

1. **Integral occurrence lattice.**  Section 4 alone is rational, but the
   later boundary-role commutator isolates one primitive Johnson square at
   one depth and closes the full integral product.  Thus torsion is no
   longer an open algebraic gate; physical realization still is.
2. **Nonnegative physical fibre.**  Signed span does not imply a sequence
   through nonnegative occurrence decks.  The authenticated mass-two flag
   example has identical degree/reflection data yet isolated endpoints; a
   returned catalyst is necessary.
3. **Guarded support.**  In a fixed literal support graph, all alternating
   even circuits are the Markov basis.  Four-cycles suffice only under the
   proved chordal-bipartite and literal-square hypotheses.  An induced
   `C_6` is the first exact missing generator.
4. **Basis-changing compiler paths.**  A Pluecker square preserves the used
   physical-cell set.  It cannot by itself close a common-cap deficiency
   whose alternating discrepancy contains a cell-to-cell path.  An exterior
   unused cell, dummy, or other basis-changing return is necessary.
5. **Planting.**  The proof uses the complete relabelling orbit.  It does
   not prepare the required old packet slots, owner halos, residence collars,
   or their order in one safe carrier.
6. **Nonlinear U5.**  Common-cap Hall deficiency is a maximum over target
   cuts and a disjunction over cap states.  It is not a rational linear
   invariant of the natural occurrence decks.  Equation (0.1) therefore
   removes a possible linear obstruction but does not supply a matching.

### Theorem 6.1 (the exact surviving q1 candidate-cap countercondition)

Let `T` be a simple rank-`r` Johnson path with a nonzero depth-`d` factor,
equipped with the standard maximal-erosion short-cell compiler.  Let its
missing immediate lower targets be partitioned into
`Z,L,R,B`, according as they lie in neither endpoint, only the left
endpoint, only the right endpoint, or both endpoints.  Write their sizes as

\[
                         z,\ell,\rho,b,
\]

and put \(u_L=\min(\ell,d)\), \(u_R=\min(\rho,d)\).  Every current canonical
or adjacent-breaker walk preserves

\[
 \delta_{\rm top}=
 z+\ell+\rho+b-u_L-u_R-
       \min\{b,2d-u_L-u_R\}.                         \tag{6.1}
\]

The quantity `delta_top` is the exact deficiency of the q1 candidate-cap
graph, and every terminal compiler has deletion number at least
`delta_top`.  Hence a regenerative `B(k)+O(1)` theorem based only on the
present catalogue must export

\[
                         \delta_{\rm top}=O(1).       \tag{6.2}
\]

#### Proof

A missing rank-`r-1` immediate target `Q` has no internal short-cell cap.
Indeed, every such cap spanning a carrier edge is contained in some
adjacent intersection \(T_i\cap T_{i+1}\).  If the cap contained
`Q`, then, since that adjacent intersection also has rank `r-1`, it would
equal `Q`, contradicting that `Q` is missing from the immediate palette.
The same argument handles a partial boundary cell after the first edge.
Only the `d` repeated left endpoint cells and the `d` repeated right
endpoint cells remain.  The exact maximum matching size in this two-bank
graph is

\[
 u_L+u_R+\min\{b,2d-u_L-u_R\},
\]

which gives (6.1).  All current packets preserve the immediate palette and
both endpoints, so the four classes and (6.1) are invariant. \(\square\)

Thus the algebraic closure is exact: below q1, only point degrees survive;
at q1, the two-bank boundary deficiency is the first genuine frozen
compiler gate.  Even after (6.2), common-Q compatibility at lower ranks is
still not automatic.

The exact next theorem is consequently not another moment calculation.  A
successful continuation may instead supply one of the following sufficient
physical resources in the prepared carrier:

* a guarded alternating-circuit/catalyst bank realizing the required
  signed directions nonnegatively;
* an exterior basis-changing return with bounded Ferrers endpoint cost; or
* a direct common-cap augmenting linkage whose packet slots regenerate.

The four-packet twisted-cube absorber supplies a literal owner- and
q1-compatible all-depth-neutral macro on four prepared slots.  It still
lacks the last global planting and U5 extension, so it does not alter the
scope above.

## 7. Independent audit

Two independent symbolic audits checked the decisive isotypic step.

* The first verified the `H_2` pair-incidence separation and the label-count
  inequalities.  It identified the necessary exact filler count in (4.5).
* The second independently found the `L_j=1` corner: using `{f_s}` for
  `s>1` would also meet a suffix and is not a step vector.  The corrected
  choices `{f_1}` for `s=1` and `{f_1,f_s}` for `s>=2` give (4.6).

Both audits verified

\[
 4\le k_t\le r-2<v/2,
 \qquad |Z|\ge r-1>j-1,
\]

and agreed that (0.1) holds over `Q` with precisely the fixed-carrier,
positivity, planting and compiler exclusions stated above.  The independent
integral commutator theorem subsequently removed the integrality exclusion.
