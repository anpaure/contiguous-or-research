# Full canonical `(2 3)` MSW cube at the first shadow

Date: 2026-07-25

Method: pure mathematics only.  No finite search or solver is used.

## 0. Verdict

Let `F=F_m^MSW`, let `tau=(2 3)`, and let `C` be the proved Catalan
component set of the ownership overlay of `F` and `tau F`.  For
`I subseteq C`, write `F_I` for the exact factor obtained by switching
precisely the components in `I`, and let

\[
                         h(I)=H_1(F_I).
\]

The presently proved mathematics gives the following exact answer.

1. It is **false** that every component is non-improving throughout the
   full cube.  In fact every worsening cube edge has an antipodal improving
   edge of exactly the opposite size.
2. The private size-two components `K_V` are genuinely anti-repair at the
   canonical corner:
   \[
                   h(I)=h(\varnothing)+|I|
   \]
   on their private face.  Each such switch creates one first-shadow hole
   and repairs none.
3. Consequently the antipodal edge at the opposite face is a literal
   improving component edge of size one.  Thus improving components really
   occur in the same exact integral cube, although not at the canonical
   corner.
4. No proved structural load table currently determines the sign of every
   nonprivate component at the canonical corner, nor the sign of the full
   fair-cube drift from that corner.  The colex-pivot theorem proves that
   every full component effect is nonzero and the effects are linearly
   independent; it does **not** determine whether its positive cells are
   old holes or whether its negative cells are fragile singletons.
5. The claim that the **complete** canonical overlay has total depth-one
   action `O(Cat_m)` is not established by the cited hierarchy results.
   What is proved is `O(Cat_m)` action for the contextual size-two atlas,
   and `O(W/sqrt(m))` rankwise diameter for a `3/8`-mass Catalan tail.
   The published triangle ledger for the entire hierarchy gives only the
   trivial coefficient-scale bound `O(W)`.  Therefore the stronger
   whole-cube `o(W)` inertness conclusion must not be used without a new
   cancellation theorem.
6. Nevertheless the complete fixed cube is now ruled out for coefficient
   one by a different, sharper invariant.  The marked-gap certificates
   force at least
   \[
   (m-3)\operatorname{Cat}_{m-2}-{2W\over m+2}
   =\left({1\over32}-o(1)\right)W
   \]
   canonical holes which are fixed by `(2 3)`.  They survive every corner
   component by component.  The proof is in
   `MATH_THEOREM_MSW_23_FIXED_HOLE_FLOOR_20260725.md`.

Thus the fixed canonical cube may contain productive cuts, but it is now
proved incapable of reducing the first-shadow defect to `o(W)`.  The
repair-versus-fragility census in Section 4 remains the exact test for how
much of the **nonfixed** defect a cut can repair.

## 1. Exact antipodal symmetry

The side-exchanging coordinate involution sends a cube vertex to its
complement:

\[
                         \tau F_I=F_{{\cal C}\setminus I}.
\tag{1.1}
\]

Since relabeling coordinates preserves the number of missing targets,

\[
                  \boxed{h(I)=h({\cal C}\setminus I).}
\tag{1.2}
\]

Fix a component `K notin I` and put

\[
                 J={\cal C}\setminus(I\cup\{K\}).
\]

Then (1.2) gives

\[
 h(I\cup\{K\})=h(J),\qquad h(I)=h(J\cup\{K\}).
\]

Therefore

\[
 \boxed{
 h(I\cup\{K\})-h(I)
 =-\bigl(h(J\cup\{K\})-h(J)\bigr).}
\tag{1.3}
\]

Every oriented edge drift is paired with an antipodal drift of the opposite
sign.  In particular, a theorem saying that every component switch is
non-improving at every cube vertex would force every edge drift to be zero.

This is a purely integral symmetry statement; no averaging is involved.

## 2. The private components give explicit counteredges

For every `V in D_(m-4)`, the proved private size-two component `K_V`
has the four-cell depth-one effect

\[
 -e_{S_V}+e_{\tau S_V}-e_{T_V}+e_{\tau T_V},
\tag{2.1}
\]

and the canonical loads are

\[
 (\mu(S_V),\mu(\tau S_V))=(3,1),\qquad
 (\mu(T_V),\mu(\tau T_V))=(1,1).
\tag{2.2}
\]

The displayed supports are disjoint as `V` varies.  Hence switching an
arbitrary private subfamily `P` sends the first pair to `(2,2)` and the
second to `(0,2)`, so

\[
                  \boxed{h(P)=h(\varnothing)+|P|.}
\tag{2.3}
\]

Thus every private edge in the canonical private face is worsening by one.
Apply (1.3).  If

\[
                  J={\cal C}\setminus(P\cup\{K_V\}),
\]

then the edge `J -> J union {K_V}` improves the hole count by one.  This is
an explicit all-dimensional counterexample to global componentwise
non-improvement:

\[
       \boxed{h(J\cup\{K_V\})-h(J)=-1.}
\tag{2.4}
\]

The improving edge is at the antipodal face; (2.4) says nothing by itself
about descent from the canonical corner.

## 3. Why the colex hierarchy does not decide signs

For the full component `C_(j,R)`, the exact histogram displacement is

\[
             \Delta_{j,R}=(\tau-1)C_{j,R}.
\tag{3.1}
\]

The colex-pivot theorem supplies a unique leading positive target
`P_(j,R)` with coefficient `+1`, and these pivots are pairwise distinct.
Consequently all component displacement vectors are nonzero and linearly
independent.

Hole drift, however, is nonlinear in the histogram.  If `a_K,b_K` are the
old/new component loads and `mu` is the complete canonical load, then

\[
 H_1(F_K)-H_1(F)=D_K-R_K,
\tag{3.2}
\]

where

\[
 R_K=\#\{S:\mu(S)=0,\ b_K(S)>0\},
\tag{3.3}
\]

\[
 D_K=\#\{S:\mu(S)=a_K(S)>0,\ b_K(S)=0\}.
\tag{3.4}
\]

The sign of a coefficient in (3.1), including the leading pivot, determines
neither (3.3) nor (3.4).  One also needs the full canonical load at that
target and the distribution of all its occurrences among components.
Linear independence therefore supplies degrees of freedom but no descent
sign.

## 4. The exact unresolved canonical test

For a single component, canonical descent is exactly

\[
                         R_K>D_K.
\tag{4.1}
\]

Summing over all components gives a slightly softer sufficient test.  For
each exclusive moved target pair `P={S,tau S}` (one endpoint a canonical
hole and the other covered), let `s_P` be the number of components carrying
the covered endpoint.  Let `D_common` count targets covered by both endpoint
factors whose complete canonical support lies in one old-side component
while its new side in that component is empty.  Then the proved identity is

\[
 \sum_K\bigl(H_1(F_K)-H_1(F)\bigr)
 =D_{\rm common}-\sum_{P:s_P\ge2}s_P.
\tag{4.2}
\]

Thus a canonical improving component follows from

\[
                    \sum_{P:s_P\ge2}s_P>D_{\rm common}.
\tag{4.3}
\]

For the fair full cube, let `C` be the family of targets covered by both
endpoint factors but not supplied on both sides of any one component, and
let `d_S` be their one-sided component support count.  The exact drift is

\[
 \boxed{
 \mathbb E h(I)-h(\varnothing)
 =-\sum_{\text{exclusive }P}(1-2^{1-s_P})
   +\sum_{S\in{\cal C}}2^{-d_S}.}
\tag{4.4}
\]

Equations (4.3) and (4.4), not the Catalan size spectrum alone, are the
two exact sign tests.  The missing data are the hereditary support counts
`s_P`, `d_S`, and `D_common` for the full component hierarchy.

## 5. Audit of the action-size claim

Three different component menus must not be conflated.

### 5.1 Contextual size-two atlas

The shifted size-two charts contain

\[
 \sum_{s=0}^{m-2} C_sC_{m-s-2}=C_{m-1}
\]

components and four depth-one action cells per component.  Their total
action incidence is

\[
                         4C_{m-1}=O(C_m)=O(W/n).
\tag{5.1}
\]

This is rigorously `o(W)`, but these charts overlap across transpositions
and are not the complete `(2 3)` component hierarchy.

### 5.2 The proved `3/8` canonical tail

For the suffix tail `r>=m/2`, the proved triangle ledger gives, uniformly
at depth one,

\[
 \operatorname {diam}_1
 \le \left({5\over4\sqrt\pi}+o(1)\right){W\over\sqrt m}
 =o(W).
\tag{5.2}
\]

This tail carries `(3/8+o(1))C_m` rows.  It is a genuine subcube of the
fixed `(2 3)` overlay, but it is not the full cube.

### 5.3 The complete hierarchy

The available all-component bound is

\[
 \|\Delta_{j,R}^{(1)}\|_1
 \le(4j+10)(C_j+C_{j+1}).
\tag{5.3}
\]

Summing (5.3) over the `C_(m-j-2)` suffixes does not give
`O(C_m)`; its large-`j` endpoint is only bounded at coefficient scale.
The universal rowwise bound likewise gives `O(W)`.  The colex theorem
proves at least one nonzero pivot per component, but not a compensating
whole-hierarchy upper bound.

Accordingly, the sentence “the complete canonical fixed-transposition
overlay has total first-shadow action `O(Cat_m)`” is presently unsupported
by the cited theorems.  It may be true after further Catalan cancellation,
but that cancellation theorem is itself missing.

## 6. Consequence for coefficient one

The private anti-repair theorem closes the most obvious local correction,
and the `3/8` tail is rankwise `o(W)`-inert.  These are meaningful no-go
results.  They do not close the full fixed overlay: the remaining `5/8`
large-atom head can in principle contribute coefficient-scale action, and
its hole sign is not determined.

The next useful theorem in this lane is therefore one of exactly two
forms:

1. **canonical productive cut:** prove (4.3), or prove the right side of
   (4.4) is negative by `Omega(W)`;
2. **whole-hierarchy inertness:** prove a new cancellation estimate
   \[
       \sum_{j,R}\|\Delta_{j,R}^{(1)}\|_1=o(W),
   \]
   which would show that no corner of this fixed overlay can repair the
   canonical linear hole defect.

The second statement is no longer needed to rule out this fixed fibre.
The fixed-hole theorem in
`MATH_THEOREM_MSW_23_FIXED_HOLE_FLOOR_20260725.md` proves directly that
every complete-cube corner retains `(1/32-o(1))W` first-shadow holes.  The
first statement remains meaningful only as a possible partial reduction of
the nonfixed holes before changing bridges.

The exact advance is therefore threefold: the stronger global
non-improvement claim is false; literal improving antipodal edges exist;
but a linear transposition-fixed hole family proves that no corner of this
one complete fixed fibre can attain the `o(W)` first-shadow target.
