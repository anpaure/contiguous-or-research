# The natural `A_h` ladder misses every PBBS triangle by one survivor

**Date:** 2026-08-05  
**Method:** exact forward/reverse survivor cancellation and the classified
PBBS exchange triangles; no computation or search  
**Status:** unconditional ladder-wide obstruction to the shortest relative
return.  On the monotone height ladder, every connector edge retains its
natural `M_0` incidence, while the required `M_1` edge is a legal exchange
arc.  That arc lies in no directed triangle: its source carries the zero
immediately preceding the third unmatched zero of the common core.  The
general PBBS no-`C8` theorem also excludes a directed four-cycle.  Thus no
candidate in this natural ladder closes by a `C6` or `C8`.  Longer
`O(d)` directed returns are not ruled out.

## 1. The monotone height ladder

Put

\[
                         r=m-1,
             \qquad     n=2r+1,                              \tag{1.1}
\]

and index the cyclic coordinates by `0,1,...,2r`.  Use the rooted
deficit-one PBBS states

\[
 A_h=0\,1^h0^h(10)^{r-h},
             \qquad1\le h\le r.                             \tag{1.2}
\]

Their Dyck heights are `h`.  For `1<=h<r`,

\[
 A_{h+1}=A_h-\{2h+1\}+\{h+1\}.                             \tag{1.3}
\]

Thus the complements \(U_h=[n]\setminus A_h\) form a Johnson path.  Let

\[
 I_h=U_h\cap U_{h+1}
     =A_h^c-\{h+1\}                                        \tag{1.4}
\]

be its common rank-`r` facet.

The alternating height-one socket is exceptional.  At `h=1`, the facet
`I_1` belongs naturally to `U_2` in `M_0`, and the other required edge
contains the known long-bridge arc.  The useful prospective socket is
therefore `U_2`; below we take

\[
             2\le h<H\le\min\{2d+1,r\}.                    \tag{1.5}
\]

## 2. Both natural PBBS matchings on `I_h`

The word of `I_h` is

\[
 I_h=1\,0^{h+1}1^{h-1}(01)^{r-h}.                          \tag{2.1}
\]

### Lemma 2.1 (the two survivors)

For every `h>=2`,

\[
                         p_+(I_h)=h+1,
             \qquad     p_-(I_h)=1.                         \tag{2.2}
\]

Consequently

\[
 f(I_h)=A_h,
 \qquad
 f^{-1}(I_h)=B_h:=A_h-\{1\}+\{h+1\}.                       \tag{2.3}
\]

#### Proof

For the forward survivor, use weights `+1` on members and `-1` on
nonmembers.  In (2.1), the prefix sum reaches `-h` at the zero `h+1`.
For `h>=3` this is the unique global minimum.  For `h=2` it is the first
global minimum; the standard forward convention chooses it.  Hence
`p_+(I_h)=h+1`.

For reverse cancellation, delete every displayed `01` in the final
alternating tail.  Match the final `h-1` zeros of the initial zero block
with the following `h-1` ones.  The reduced cyclic word is `1,0,0`;
the second zero matches the cyclic one and the first zero, at coordinate
`1`, survives.  This proves (2.2).  Substitution into

\[
 f(Z)=Z^c-p_+(Z),
 \qquad f^{-1}(Z)=Z^c-p_-(Z)
\]

gives (2.3). \(\square\)

Recall that, at owner `U_Z=Z^c`, the natural matchings are

\[
                         M_0(U_Z)=f^{-1}(Z),
             \qquad     M_1(U_Z)=f(Z).                      \tag{2.4}
\]

Since `f(I_h)=A_h`, equation (2.3) says

\[
                         I_h=M_0(U_h).                       \tag{2.5}
\]

Thus the incidence path

\[
 U_2-I_2-U_3-I_3-\cdots-I_{H-1}-U_H                      \tag{2.6}
\]

keeps every tail edge `U_hI_h` in `M_0`.  Its head edge
\(I_hU_{h+1}\) must replace the old \(M_1\) edge at \(I_h\).  In the contracted
`M_1` exchange digraph it is the forced arc

\[
                         \boxed{B_h\longrightarrow A_{h+1}}.
                                                                    \tag{2.7}
\]

The arcs (2.7), `2<=h<H`, are pairwise endpoint-disjoint.  They form the
complete forced part of the one-colour return; `M_0` may remain unchanged.

## 3. The one-survivor displacement

The source and target of (2.7) have common rank-`(r-1)` core

\[
 K_h=B_h\cap A_{h+1}
     =A_h+\{h+1\}-\{1,2h+1\}.                              \tag{3.1}
\]

Its literal word is

\[
 K_h=00\,1^h0^{h+1}(10)^{r-h-1}.                           \tag{3.2}
\]

### Lemma 3.1 (exact unmatched-zero triple)

The three forward-unmatched zeros of `K_h` are

\[
                         \boxed{0, 1, 2h+2}.              \tag{3.3}
\]

But

\[
 B_h=K_h+\{2h+1\},
 \qquad
 A_{h+1}=K_h+\{1\}.                                       \tag{3.4}
\]

#### Proof

In (3.2), the zeros at `0` and `1` are exposed.  Between coordinate `1`
and coordinate `2h+2` lies the Dyck block `1^h0^h`; the zero at `2h+2`
is exposed, and the remaining suffix `(10)^(r-h-1)` cancels completely.
This is exactly the canonical three-survivor decomposition and proves
(3.3).  Formula (3.4) follows directly from (1.2), (2.3), and (3.1).
\(\square\)

The insertion in (2.7) is legal: `p_+(B_h)=1`, as is seen by deleting the
unmatched zero `1` from

\[
                         B_h=00\,1^h0^{h-1}(10)^{r-h};       \tag{3.5}
\]

the remaining rotation is Dyck.  The source deletion is `2h+1`.
Moreover

\[
                  f^2(B_h)=f(I_h)=A_h\ne A_{h+1},           \tag{3.6}
\]

so the arrow is not the forbidden \(M_0\)-collision successor.
Lemma 3.1 says that this deleted coordinate is **not** one of the three
unmatched zeros of the common core; it precedes the third one by exactly
one cyclic position.

## 4. No `C6` or `C8` return anywhere on the ladder

The complete directed-triangle classification for the natural PBBS
exchange graph says that every directed triangle on a rank-`(r-1)` core
uses exactly the three centers obtained by adding its three
forward-unmatched zeros.  By (3.3)--(3.4), `B_h` is not one of those three
centers.

### Theorem 4.1 (ladder-wide triangle obstruction)

For every `2<=h<r`, the forced exchange arc

\[
                         B_h\longrightarrow A_{h+1}
\]

lies in no directed triangle.  Hence the corresponding connector edge has
no relative `M_1` return on three matching-pair units.

Moreover the natural PBBS exchange graph has no directed four-cycle.
Therefore every directed cycle containing this forced arc has length at
least five.

#### Proof

The adjacent-rank incidence graph has no alternating \(C_4\), so the
exchange digraph has no directed two-cycle.  The first asserted exclusion
is the triangle classification combined with Lemma 3.1.  The second is the
general PBBS no-`C8` theorem: a directed four-cycle would lift to an
\(M_1\)-alternating Middle-Levels \(C_8\).
\(\square\)

This obstruction is uniform in the chosen terminal height `H`.  Choosing
`H` adaptively among `3,...,2d+1` never supplies a triangular or
four-cycle closure for any of the forced arcs in (2.7).

## 5. Exact remaining cycle-cover problem

The theorem does not prove that the ladder-relative graft is impossible.
A directed cycle of length five or more may contain one or several forced
arcs, and a family of such cycles could still have total support `O(d)`.

The precise residual statement is:

> **Displaced-survivor return lemma.**  For some
> `3<=H<=2d+1`, extend the partial injection
>
> \[
>              B_h\mapsto A_{h+1},\qquad2\le h<H,
> \]
>
> to a directed cycle cover of the natural `M_1` exchange graph on
> `O(H)` vertices, avoiding the fixed collar and upper-backup banks.

If this holds, keep `M_0` unchanged and toggle those `M_1` cycles.  The
resulting factor contains the complete path (2.6), agrees with the PBBS
factor outside `O(d)` matching-pair units, and reaches the local body
component `C_H` from the height-ladder co-selection theorem.

The typed collar endpoint can be kept out of the switched set: choose the
outer socket to be `U_2`, give its protected internal edge colour `M_1`,
and use the retained natural `M_0` edge `U_2I_2` as the first connector
edge.  Thus the remaining obstruction is genuinely the displaced-survivor
cycle cover, not another endpoint-degree equation.

Adding an `O(d)` eventual return support to the forbidden bank in the
rank-stratified stabilizer proof does not alter its asymptotics.  Hence the
already-proved isolated upper-backup occurrence bank can be reselected
disjointly after such a return is found.  This statement preserves the
backup **packing theorem**; it does not prove that the combined bank extends
to one relative PBBS factor or that no new upper casualties arise.

## 6. Dependencies

The body list and distance ladder are in
`MATH_THEOREM_PBBS_HEIGHT_LADDER_BODY_COSELECTION_20260805.md`.

The directed-triangle classification and general no-directed-`C4` result
are in
`MATH_THEOREM_PBBS_HAMILTONIZATION_CONNECTOR_BOUNDARY_20260726.md`
and
`MATH_THEOREM_PBBS_NO_C8_AND_LONG_PARITY_BRIDGE_20260726.md`.

The exact two-colour cycle-cover normal form is in
`MATH_THEOREM_C8_RELATIVE_PBBS_ALTERNATING_GRAFT_AND_UPPER_BACKUP_20260805.md`.
