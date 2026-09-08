# The two-queue reset plus a long square return is exactly biresident and reversal-transparent

**Date:** 2026-08-01  
**Lane:** K, guarded square planting / functional common residual  
**Status:** independent symbolic audit, sharp coordinate-supply correction,
and positive local theorem. Choosing
the long-return deletion labels in the permanent reset core and its
insertion labels outside the complete reset support gives an
occurrence-simple cycle. Pairing the two reset orientations with opposite
orientations of that return makes the complete macro a literal reversal.
All cyclic union/intersection decks and maximal-erosion antecedents are then
transported exactly. The result is a closed local component; exterior
opening, topology gain, and one global compiler/common-cap matching remain
separate.

## 0. Verdict and distinction from the older collar

The rail \(R_d\) from
MATH_THEOREM_BOOLEAN_HEX_RESIDENT_LONG_SQUARE_COLLAR_20260801.md
has two different uses.

1. In the older hex actuator, the rail has the **same** orientation in both
   phases while a ternary hex is toggled. That operation can remove a
   cycle, but it is not all-width upper-transparent; it has the explicit
   triangular cut collateral.
2. In the construction audited here, the rail is paired with the opened
   two-queue reset and is itself reversed with the reset. The entire closed
   owner cycle is reversed. This gives exact all-width cyclic transparency
   and exact erosion transport, but performs no component-count
   augmentation.

The two conclusions must not be combined: all-width reversal transparency
does not come for free in the cycle-removing hex phase.

The anchored version in
MATH_THEOREM_RESET_RETURN_RAIL_COMPLETE_REVERSAL_GUARDED_CYCLE_20260801.md
reserves one untouched core coordinate and assumes \(r\ge2d+2\). That is a
valid convenient sufficient face, but the anchor is not necessary for
nonempty maximal erosion. The sharp displayed rail needs only \(d\) core
labels and \(d\) exterior labels.

## 1. Two-queue reset and its seam

Fix depth \(d\ge1\), put

\[
                         n=d+1,\qquad N=2n,                    \tag{1.1}
\]

and let \(K\), \(\Xi=\{\xi_0,\ldots,\xi_{N-1}\}\) be disjoint, with

\[
                         |K|=r-n.                             \tag{1.2}
\]

Indices on \(\Xi\) are read modulo \(N\). The two-queue reset roots are

\[
             T_i=K\cup\{\xi_i,\xi_{i+1},\ldots,\xi_{i+d}\}.
                                                                  \tag{1.3}
\]

They form a simple Johnson \(N\)-cycle. Open the seam between

\[
\begin{aligned}
 E=T_0&=K\cup\{\xi_0,\ldots,\xi_d\}=L\cup\{\delta\},\\
 F=T_{N-1}&=K\cup\{\xi_{N-1},\xi_0,\ldots,\xi_{d-1}\}
                                      =L\cup\{\alpha\},
\end{aligned}                                                    \tag{1.4}
\]

where

\[
\begin{aligned}
 L&=K\cup\{\xi_0,\ldots,\xi_{d-1}\},\\
 \delta&=\xi_d,\qquad \alpha=\xi_{2d+1}.
\end{aligned}                                                    \tag{1.5}
\]

Write

\[
                         \Omega=K\cup\Xi                         \tag{1.6}
\]

for the complete reset support.

Choose pairwise distinct labels

\[
             x_1,\ldots,x_d\in K,\qquad
             y_1,\ldots,y_d\notin\Omega.                         \tag{1.7}
\]

Thus the \(x_j\) are present in every reset root, while every \(y_j\) is
absent from every reset root. The exact supply assumptions are

\[
                         |K|\ge d,\qquad
                         |[k]\setminus\Omega|\ge d.              \tag{1.8}
\]

Since \(|K|=r-d-1\) and \(|\Omega|=r+d+1\), these are exactly

\[
                         r\ge2d+1,\qquad k-r\ge2d+1.             \tag{1.9}
\]

For the central odd case \(k=2m+1,r=m\), they hold whenever
\(m\ge2d+1\). The slightly stronger anchored-reset hypothesis
\(m\ge2d+2\) is therefore sufficient.

## 2. The long return

Put \(X_j=\{x_1,\ldots,x_j\}\) and
\(Y_j=\{y_1,\ldots,y_j\}\). Define

\[
 P_j=L-X_j+Y_j+\alpha\qquad(0\le j\le d),                    \tag{2.1}
\]

so \(P_0=F\), and

\[
 Q_0=L-X_d+Y_d+\delta,                                       \tag{2.2}
\]

\[
 Q_j=L-\{x_{j+1},\ldots,x_d\}
       +\{y_{j+1},\ldots,y_d\}+\delta
          \qquad(1\le j\le d),                               \tag{2.3}
\]

so \(Q_d=E\). The return is

\[
       R_d:\quad F=P_0,P_1,\ldots,P_d,Q_0,\ldots,Q_d=E.       \tag{2.4}
\]

Join it to the forward opened reset and omit duplicate endpoints. The
resulting cyclic owner word is

\[
\mathcal T^+=
 (T_0,T_1,\ldots,T_{N-1},P_1,\ldots,P_d,Q_0,\ldots,Q_{d-1}).
                                                                  \tag{2.5}
\]

Its length is

\[
                         M=N+2d=4d+2.                         \tag{2.6}
\]

The opposite phase is the literal cyclic reversal

\[
                         \mathcal T^-_i=\mathcal T^+_{-i},    \tag{2.7}
\]

after an irrelevant choice of cyclic origin. Equivalently it consists of
the reverse reset path and the reverse return path.

## 3. Exact occurrence and palette disjointness

### Theorem 3.1 (resource-simple long return)

The cycle \(\mathcal T^+\) is simple on roots, immediate lower colours,
and immediate upper owners. The same is true of \(\mathcal T^-\), and the
two phases use exactly the same three resource sets.

More sharply:

1. the only return roots which are reset roots are the endpoints \(E,F\);
2. no nonseam return lower colour is a reset lower colour;
3. no nonseam return upper owner is a reset upper owner; and
4. the direct seam pair
   \[
                         L,\qquad L+\alpha+\delta             \tag{3.1}
   \]
   occurs in neither open path and remains one common exposed residual
   pair.

#### Proof

Every internal return root contains at least one \(y_j\notin\Omega\),
whereas reset roots are subsets of \(\Omega\). Thus the root sets meet only
at \(E,F\).

Every reset lower colour contains the whole permanent core \(K\) and no
\(y_j\). A return lower colour either contains a \(y_j\), or is one of the
two boundary intersections \(F-x_1\), \(E-x_d\); those omit a member of
\(K\). Hence no return lower equals a reset lower.

Every return upper owner contains at least one \(y_j\notin\Omega\), whereas
every reset upper owner is contained in \(\Omega\). Hence the upper
palettes are disjoint. The prefix structure in (2.1)--(2.3) makes the
return roots and its lower and upper palettes internally injective, exactly
as in the long-rail theorem. Finally, all return edges differ from the
direct seam, proving (3.1). Reversal changes no undirected edge resource.
\(\square\)

The conditions in (1.7) are load-bearing. Taking an \(x_j\) outside the
permanent core removes the simple lower-palette separator; taking a \(y_j\)
inside \(\Omega\) removes the simple upper/root separator. This theorem
does not assert disjointness for those weaker choices.

## 4. Exact cyclic run census

The complete coordinate run table can be read without case search. Define

\[
\Xi_{\mathrm{seam}}=\{\xi_0,\ldots,\xi_{d-1}\},\qquad
\Xi_{\mathrm{opp}}=\{\xi_{d+1},\ldots,\xi_{2d}\}.             \tag{4.1}
\]

### Theorem 4.1 (exact biresidence)

Every nonconstant coordinate trace on \(\mathcal T^+\) has exactly one
positive and one zero run. Their cyclic lengths are:

\[
\begin{array}{c|c|c}
\text{coordinate class}&\text{positive run}&\text{zero run}\\ \hline
x_j\ (1\le j\le d)&3d+1&d+1\\
\xi\in\Xi_{\mathrm{seam}}&3d+1&d+1\\
y_j\ (1\le j\le d)&d+1&3d+1\\
\xi\in\Xi_{\mathrm{opp}}&d+1&3d+1\\
\alpha,\delta&2d+1&2d+1.
\end{array}                                                   \tag{4.2}
\]

Coordinates of \(K-\{x_1,\ldots,x_d\}\) are constantly one, and all other
outside coordinates are constantly zero. The same table holds for
\(\mathcal T^-\). In particular both phases satisfy positive and zero
residence through depth \(d\), with the sharp minimum \(d+1\).

#### Proof

Every \(x_j\) is present on all reset roots. Along the return it is absent
exactly on

\[
               P_j,\ldots,P_d,Q_0,\ldots,Q_{j-1},             \tag{4.3}
\]

a consecutive block of \((d-j+1)+j=d+1\) vertices. This proves its row of
(4.2). Dually, \(y_j\) is absent on the reset and present exactly on the
block (4.3), proving its row.

Every \(\xi\in\Xi_{\mathrm{seam}}\) has its reset positive run across the
deleted seam. It occurs on every return vertex, so inserting the \(2d\)
internal return vertices extends its old \(d+1\) run to \(3d+1\). Every
\(\xi\in\Xi_{\mathrm{opp}}\) has a reset positive run of length \(d+1\)
away from the seam and is absent throughout the return, so that run is
unchanged.

The reset run of \(\delta\) has length \(d+1\) beginning at \(E\), and its
return occurrence on \(Q_0,\ldots,Q_{d-1}\) adds \(d\) vertices across the
cyclic join. Thus its positive run has length \(2d+1\). The calculation for
\(\alpha\), using \(P_1,\ldots,P_d\) after \(F\), is symmetric. Since the
cycle length is \(4d+2\), all complementary lengths in (4.2) follow.
Reversal preserves the table. \(\square\)

This corrects the raw three-edge square: its new coordinate has trace
\(0,1,1,0\) and fails strict residence already for \(d\ge2\). The long
return replaces that length-two run by the exact \(d+1\) blocks in (4.2).

### Corollary 4.2 (exact two-sided depth-\(d\) flag ranks)

For every \(0\le q\le d\), every intersection of \(q+1\) consecutive
owners in either phase has rank \(r-q\), and every union of \(q+1\)
consecutive owners has rank \(r+q\). For \(q<d+1\), consecutive shadow
states obey the corresponding Johnson transition law.

#### Proof

The positive-run floor \(d+1\) prevents a departure coordinate from
returning inside any \(q\le d\) transition window, so the \(q\) deletions
are distinct. The zero-run floor gives the dual assertion for the \(q\)
insertions. Hence intersections lose and unions gain exactly \(q\)
coordinates. The strict inequality \(q<d+1\) gives the adjacent shadow
transition law. \(\square\)

This proves the local two-sided rank/chronology antecedent. It does not say
that the displayed windows cover every Boolean target of those ranks.

## 5. Full cyclic shadow equality

### Theorem 5.1 (all-width reversal transparency)

For every cyclic width \(1\le\ell\le M\), reversal gives bijections of
occurrences satisfying

\[
 \bigcup_{t=0}^{\ell-1}\mathcal T^-_{i+t}
 =
 \bigcup_{t=0}^{\ell-1}
       \mathcal T^+_{-i-t}
 =
 \bigcup_{t=0}^{\ell-1}
       \mathcal T^+_{-i-\ell+1+t},                           \tag{5.1}
\]

and

\[
 \bigcap_{t=0}^{\ell-1}\mathcal T^-_{i+t}
 =
 \bigcap_{t=0}^{\ell-1}
       \mathcal T^+_{-i-\ell+1+t}.                           \tag{5.2}
\]

Hence the complete cyclic interval-union and interval-intersection
multisets agree at every width, occurrence for occurrence under the
reversal address map \(i\mapsto-i-\ell+1\).

#### Proof

Substitute (2.7). The indices \(-i,-i-1,\ldots,-i-\ell+1\)
are precisely the reverse of the consecutive block beginning at
\(-i-\ell+1\). Union and intersection are insensitive to that reversal.
\(\square\)

This is stronger than the internal-interval theorem for the rail alone:
it includes every interval crossing either reset--return join because the
**whole cycle**, not only the rail, is reversed.

## 6. Exact erosion-antecedent reversal

Use the cyclic end-indexed maximal depth-\(d\) erosion

\[
 \mathcal E_d(\mathcal T)_i
     =\bigcap_{t=0}^{d}\mathcal T_{i-t}.                     \tag{6.1}
\]

Let \(D^d\) denote the corresponding forward dilation,

\[
 (D^dP)_i=\bigcup_{t=0}^{d}P_{i+t}.                          \tag{6.2}
\]

### Theorem 6.1 (antecedent conjugacy)

Put \(P^\pm=\mathcal E_d(\mathcal T^\pm)\). Then

\[
                         P^-_i=P^+_{d-i}                     \tag{6.3}
\]

for every cyclic address \(i\). Moreover,

\[
        |P^\pm_i|=r-d,\qquad
        D^dP^\pm=\mathcal T^\pm,                             \tag{6.4}
\]

and consecutive \(P^\pm_i\) are equal or Johnson-adjacent (in the present
simple event stream they are Johnson-adjacent).

More generally, if \(A^+\) is any exact antecedent
\(D^dA^+=\mathcal T^+\), then

\[
                         A^-_i=A^+_{d-i}                     \tag{6.5}
\]

is an exact antecedent of \(\mathcal T^-\).

#### Proof

By (2.7),

\[
\begin{aligned}
 P^-_i
 &=\bigcap_{t=0}^{d}\mathcal T^+_{-i+t}\\
 &=\bigcap_{t=0}^{d}\mathcal T^+_{d-i-t}
  =P^+_{d-i},
\end{aligned}
\]

proving (6.3). The run table (4.2) has no positive run shorter than
\(d+1\). Across any \(d\) transitions the \(d\) departure coordinates are
therefore distinct and none is reinserted soon enough to survive the whole
window. Hence every intersection in (6.1) has rank \(r-d\). Coordinatewise
erosion followed by dilation restores every positive run, proving (6.4);
the strict inequality \(d<d+1\) gives the Johnson event-stream statement.

Finally,

\[
 (D^dA^-)_i
   =\bigcup_{t=0}^{d}A^+_{d-i-t}
   =(D^dA^+)_{-i}
   =\mathcal T^+_{-i}
   =\mathcal T^-_i,
\]

which proves (6.5). \(\square\)

Thus the two maximal erosions have exactly the same set-valued cell
multiset, with a known shifted reversal of physical addresses. Any purely
internal containment matching can be transported through (6.3). This is
not yet a fixed-address global common-cap theorem.

## 7. Functional Rado and exact remaining scope

Both phases use the same roots, immediate lower colours, and upper owners,
but their protected functional attachments are opposite orientations of
the same cycle. Thus no one pointwise \(\theta\) describes both phases.
Contracting the whole protected macro deletes the same resource sets in
both phases. If every phase-dependent flag/guard atom is also contracted or
deleted and the exterior aligned-column/predecessor atlas is literally
common, then one residual \(\theta_0\) and the ordinary protected Rado
inequalities extend both phases.

The positive conclusions stop at that interface.

1. **Exterior opening.** If the macro is cut and inserted into a larger
   chronology, windows crossing the new exterior cuts are not paired by
   (5.1) unless a separate two-sided collar theorem is supplied.
2. **Common cap.** Equation (6.3) transports an internal containment
   matching, but it permutes occurrence addresses. Fixed boundary pins,
   background cells, and one occurrence-labelled terminal compiler still
   require an exact common matching audit.
3. **Augmentation/topology.** Both phases are one directed cycle. The flip
   has zero cardinality gain and zero component-count gain. Any Hall or
   Dulmage--Mendelsohn improvement must come from how the changed
   attachment meets the exterior; any cycle reduction needs a separate
   guarded fusion packet.
4. **Seam tasks.** The direct seam lower/upper pair in (3.1) remains
   unfilled and needs one common exterior provider.
5. **Regeneration.** The theorem supplies one prepared macro, not a
   positive-density or recursively regenerating bank of mutually private
   copies.

Accordingly, the long return solves the native residence defect of the
support-four square without reintroducing the opposite-Cartesian-ear
common-support obstruction. The remaining exact lemma is a
**common-cap exterior opening theorem** for this reversed cycle, not
another local resource or residence identity.

## 8. Dependencies

This audit uses:

* MATH_THEOREM_TWO_QUEUE_ROLLING_GUARDED_RESET_20260801.md;
* MATH_THEOREM_K_BIDIRECTIONAL_ROLLING_RESET_FUNCTIONAL_ATTACHMENT_AND_DOUBLETON_GATE_20260801.md;
* MATH_THEOREM_BOOLEAN_JOHNSON_SQUARE_OPEN_THREE_RETURN_MACRO_20260801.md;
* MATH_THEOREM_BOOLEAN_HEX_RESIDENT_LONG_SQUARE_COLLAR_20260801.md; and
* MATH_THEOREM_K_PROTECTED_FUNCTIONAL_RADO_FACE_AND_LITERAL_TRIANGLE_EXCHANGE_OBSTRUCTION_20260801.md.

The symbolic conclusions agree with the separately frozen
MATH_AUDIT_RESET_RETURN_RAIL_COMPLETE_REVERSAL_GUARDED_CYCLE_20260801.md;
the present note additionally records the complete zero-run table,
two-sided exact-rank corollary, and the residual-\(\theta\) scope.
