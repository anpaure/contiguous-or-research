# The height-ladder pentagons have component load seven

**Date:** 2026-08-05  
**Method:** normalized Dyck roots, the largest-soliton invariant, permutation
cycle calculus, and exact cut-transversal transport; no computation or search  
**Status:** unconditional integration theorem for the explicit PBBS
height-ladder pentagons.  The simultaneous return connects all named ladder
bodies, changes component parity by zero, and deletes at most seven old
factor edges from any one PBBS component.  Upper and lower occurrence
regeneration reduce to explicit cut-load quantities.  The theorem does not
prove that those quantities are uniformly bounded.

## 1. The simultaneous pentagon switch

Use the notation of
`MATH_THEOREM_PBBS_AH_LADDER_PENTAGON_RETURN_20260805.md`.  Thus

\[
 A_h=0\,1^h0^h(10)^{r-h},
 \qquad U_h=A_h^c,
\]

and, for every \(2\le h<H\), the five exchange states

\[
 Z_h^0,Z_h^1,Z_h^2,Z_h^3,Z_h^4
\]

form a legal directed pentagon whose first arrow installs the connector
edge \(I_hU_{h+1}\).  Assume

\[
                   r\ge4,
 \qquad 3\le H\le r-1.                                  \tag{1.1}
\]

The second inequality is automatic in the eventual application
\(H\le2d+1\), since \(d=\Theta(\sqrt r)\).

Let

\[
 S_H=\{Z_h^i:2\le h<H,\ 0\le i\le4\}                  \tag{1.2}
\]

be the switched exchange support and let \(D_H\) be the corresponding set
of deleted old \(M_1\)-incidences.  Then

\[
                         |S_H|=|D_H|=5(H-2).             \tag{1.3}
\]

## 2. Normalized roots and the seven-load theorem

For a deficit-one PBBS state \(Z\), delete its forward-unmatched zero and
cut immediately after that zero.  The remaining Dyck word is its normalized
root.  Directly from the literal words of the pentagon, the five normalized
roots are

\[
\begin{aligned}
 D_h^0&=1^h0^{h-1}(10)^{r-h}0,\\
 D_h^1&=1^{h+1}0^{h+1}(10)^{r-h-1},\\
 D_h^2&=(10)^{r-h-1}1101^{h-1}0^h,\\
 D_h^3&=1(10)^{r-h-1}0101^{h-1}0^{h-1},\\
 D_h^4&=1^{h-1}0^{h-1}11(10)^{r-h-1}00.
                                                               \tag{2.1}
\end{aligned}
\]

Because \(h<H\le r-1\), the alternating exponent in the last four rows is
positive whenever it is used in the height calculation.  Factoring the
rows into Dyck mountains and primitive wrappers gives

\[
\begin{array}{c|ccccc}
i&0&1&2&3&4\\ \hline
\operatorname{ht}(D_h^i)
 &h&h+1&h&\max\{2,h-1\}&\max\{3,h-1\}.
\end{array}                                                \tag{2.2}
\]

For example,

\[
\begin{aligned}
D_h^2&=(10)^{r-h-1}\,1\bigl((10)1^{h-1}0^{h-1}\bigr)0,\\
D_h^3&=\bigl(1(10)^{r-h-1}0\bigr)(10)
       \bigl(1^{h-1}0^{h-1}\bigr),\\
D_h^4&=\bigl(1^{h-1}0^{h-1}\bigr)
       1\bigl(1(10)^{r-h-1}0\bigr)0,
\end{aligned}                                             \tag{2.3}
\]

which proves the last three entries of (2.2).

The largest Dyck height is the largest PBBS soliton part and is invariant
on every \(f^{-2}\)-component.  Therefore a fixed old PBBS component can
meet only support states in one row of the following census:

\[
\begin{array}{c|c}
\text{component height }s&
 \text{possible support states of height }s\\ \hline
s=2& Z_2^0,Z_2^2,Z_2^3,Z_3^3\\
s=3& Z_3^0,Z_3^2,Z_2^1,Z_4^3,Z_2^4,Z_3^4,Z_4^4\\
s\ge4& Z_s^0,Z_s^2,Z_{s-1}^1,Z_{s+1}^3,Z_{s+1}^4.
\end{array}                                               \tag{2.4}
\]

Rows whose subscripts fall outside \(2\le h<H\) are simply omitted.
This proves the main local-load statement.

### Theorem 2.1 (component load seven)

For every old PBBS component \(C\),

\[
                         |D_H\cap E(C)|\le7.              \tag{2.5}
\]

The bound is a worst-case action-height bound; it does not assert that the
seven displayed states actually lie on one angle component.

## 3. What is known exactly about components

Let \(\sigma=M_1^{-1}M_0=f^{-2}\) be the old component permutation.  The
simultaneous switch left-multiplies it by

\[
 \tau_H=
 \prod_{h=2}^{H-1}
 (Z_h^0\ Z_h^1\ Z_h^2\ Z_h^3\ Z_h^4),                  \tag{3.1}
\]

where the displayed five-cycles have disjoint supports.

Every five-cycle is even.  Hence \(\tau_H\) is even, and the number of
factor components satisfies

\[
             c(\tau_H\sigma)\equiv c(\sigma)\pmod2.       \tag{3.2}
\]

A five-cycle is a product of four transpositions, and multiplication by
one transposition changes the number of permutation cycles by one.
Consequently

\[
 |c(\tau_H\sigma)-c(\sigma)|\le4(H-2).                   \tag{3.3}
\]

This is not the important named-topology conclusion.  The switched factor
literally contains

\[
 U_2-I_2-U_3-I_3-\cdots-I_{H-1}-U_H.                    \tag{3.4}
\]

The PBBS components containing \(U_2,\ldots,U_H\) were pairwise distinct,
because their largest soliton heights are \(2,\ldots,H\).  Equation (3.4)
puts every one of those named owners on one component of the new factor.
Thus the desired collar/body subsystem is connected regardless of the
unresolved angle-level value of the global derivative (3.3).

## 4. Exact upper-occurrence consequence

Let \(\mathcal W_{q,C}(Y)\) be the old directed \(q\)-edge occurrences of
an upper target \(Y\) in an old component \(C\), and put

\[
                         \mu_{q,C}(Y)=|\mathcal W_{q,C}(Y)|.
\]

One old edge belongs to at most \(q\) directed \(q\)-arcs.  Combining
this congestion bound with Theorem 2.1 gives:

### Theorem 4.1 (seven-cut upper survival)

An old upper target \(Y\) survives the simultaneous ladder graft whenever
there is an old component \(C\) such that

\[
                         \mu_{q,C}(Y)>7q.                 \tag{4.1}
\]

More generally the exact criterion is

\[
 Y\text{ survives from the old deck}
 \iff
 \exists I\in\mathcal W_q^+(Y)
       \quad E(I)\cap D_H=\varnothing.                    \tag{4.2}
\]

#### Proof

If all occurrences in \(C\) met \(D_H\), then the at most seven deleted
edges in that component could hit at most \(7q\) of them.  This proves
(4.1).  The rethread preserves every directed old arc between consecutive
cuts verbatim, which proves (4.2).  \(\square\)

Define the genuine deep exception set

\[
 \mathcal E_H=
 \{Y:\text{every old witness of }Y\text{ meets }D_H
       \text{ and the graft creates no new witness of }Y\}.             \tag{4.3}
\]

Then \(|\mathcal E_H|\), not the total number of graph-theoretic
stabilizer paths, is the exact upper price of the pentagon graft.

## 5. Exact terminal-compiler transport

Let \(\mathcal M\) be any occurrence-labelled reference compiler before
the switch.  Thus every compiled lower target \(X\) is assigned a distinct
old interval cell \(J_X\).  Put

\[
 e_H(\mathcal M)
 :=|\{X:E(J_X)\cap D_H\ne\varnothing\}|.                 \tag{5.1}
\]

### Theorem 5.1 (cut-load compiler regeneration)

After the simultaneous pentagon switch, the unchanged assignments

\[
                 \{X\mapsto J_X:E(J_X)\cap D_H=\varnothing\}
\]

remain a valid matching.  Hence the terminal compiler deficiency is at
most

\[
                         e_H(\mathcal M),                  \tag{5.2}
\]

before using any new crossing cells created by the graft.

#### Proof

Deleting \(D_H\) cuts the old factor into directed arcs.  Every interval
cell counted outside (5.1) lies inside one such arc, and that arc occurs
with identical order and labels after reassembly.  Its target value is
unchanged.  The old cells were distinct, so their surviving subset remains
a matching.  Only the assignments counted by (5.1) are released.  New
cells can only reduce the final deficiency.  \(\square\)

This is stronger than solving a fresh unrestricted Hall problem, but it
still needs one correlated input: choose the terminal compiler so that its
matched cut load \(e_H(\mathcal M)\) is bounded, or recreate the released
targets on the explicit collar rays.

## 6. Why the isolated stabilizer theorem does not automatically finish

The rank-stratified isolated-backup theorem constructs, for each target
\(Y\), a path \(\pi W_Y\) in the Middle-Levels incidence graph using a
coordinate permutation \(\pi\in\operatorname{Stab}(Y)\).  After the
relative pentagon graft, however, the factor is already fixed.  Such a
path is an occurrence of \(Y\) in the new factor only if

\[
                         E(\pi W_Y)\subseteq E(F').        \tag{6.1}
\]

The natural PBBS factor is cyclically covariant, not invariant under the
full target stabilizer.  Thus graph-disjoint stabilizer packing does not
imply (6.1).  Adding the \(O(d)\) pentagon support to its forbidden bank
preserves that packing theorem asymptotically, but does not remove its
common-factor caveat.

Once the factor is fixed, simultaneous disjointness of backup paths is not
needed merely to witness upper targets.  The exact remaining condition is
the factor-relative cut-transversal statement (4.2).

## 7. Proof-safe combined implication

Suppose the other carrier gates provide:

1. a resident source antecedent for the switched owner chronology;
2. recreation of every shallow upper casualty and all but \(C_U\) members
   of \(\mathcal E_H\); and
3. a reference lower compiler \(\mathcal M\) with
   \(e_H(\mathcal M)\le C_L\), after crediting the explicit new collar
   cells.

Then the switched carrier has at most \(C_U+C_L\) literal target holes.
Appending those masks individually yields the corresponding conditional
bound

\[
                         \nu(k)\le B(k)+C_U+C_L.           \tag{7.1}
\]

In particular, uniform constants \(C_U,C_L\) would prove
\(\nu(k)=B(k)+O(1)\); zero values would prove exact equality on this
architecture.

The new unconditional content is that the PBBS return itself contributes
no length charge, connects the complete named ladder, and has old-component
cut degree at most seven.  The remaining all-dimensional bridge is now the
bounded deep-corridor exception count \(|\mathcal E_H|\), together with a
bounded matched compiler cut load and residence regeneration.

## 8. Dependencies

The legal disjoint pentagons are in
`MATH_THEOREM_PBBS_AH_LADDER_PENTAGON_RETURN_20260805.md`.

The height ladder and distinct named body components are in
`MATH_THEOREM_PBBS_HEIGHT_LADDER_BODY_COSELECTION_20260805.md`.

The componentwise occurrence-congestion theorem is in
`MATH_THEOREM_PBBS_UPPER_MULTIPLICITY_THRESHOLD_AND_CUT_TRANSVERSAL_OBSTRUCTION_20260805.md`.

The graph-level stabilizer packing theorem is in
`MATH_THEOREM_ISOLATED_C8_UPPER_BACKUP_RANK_STRATIFIED_PACKING_20260805.md`.
