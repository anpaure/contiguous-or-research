# H25 two-collar portal/cut theorem and common-\(Q_x\) compiler gate

Date: 2026-07-28

Status: proved exact two-collar Hall-current theorem, proved alternating
portal packing/cut duality, proved a cross-witness dichotomy at a one-move
local minimum, reduced every compound of two three-cut braids to a bounded
six-seam catalogue, and reconciled the theorem with the subsequently frozen
exact H25-to-H24 two-braid escape.  No literal common-\(Q_x\) lift is
claimed.

## 0. Verdict

The certified Hall-25 carrier is the correct base point for the
local-minimum lane.

Let \(G_{25}\) be its exact one-pin lower compiler graph.  Its left shore
contains all \(16\,383\) nonempty targets of ranks at most seven, its right
shore contains all \(19\,311\) depth-zero, depth-one, and depth-two physical
cells, and

\[
 \nu(G_{25})=16\,358,
 \qquad
 h(G_{25})=25.
\tag{0.1}
\]

The canonical alternating-reachable Dulmage--Mendelsohn shore is

\[
 \boxed{
 |\mathcal A_{25}|=1320,
 \qquad
 |N_{G_{25}}(\mathcal A_{25})|=1295.
 }
\tag{0.2}
\]

Its target-rank census is

\[
\begin{array}{c|rrrr}
\text{rank}&4&5&6&7\\ \hline
\#&8&72&359&881.
\end{array}
\tag{0.3}
\]

The exact shore is frozen by digest

\[
\texttt{89449e9fe9fb085c96ec911e3a9fad61f1e0409e4c6ef0133ed72677eb273e83}.
\tag{0.4}
\]

The carrier is a certified local minimum under the complete safe
single-three-cut catalogue.  This rules out the direct assertion

\[
\text{every positive-deficiency carrier has a strictly improving
single three-cut.}
\tag{0.5}
\]

It does not rule out two interacting collars.  In fact the subsequently
frozen pair

\[
 \operatorname{FR}(1512,2458,4103),
 \qquad
 \operatorname{FR}(2664,3491,6201)
\tag{0.6}
\]

has the exact score chronology

\[
 25\longrightarrow25\longrightarrow24.
\tag{0.7}
\]

Thus the radius-two Hall obstruction is now positively closed: the first
collar is a neutral portal relocation and the second converts it into one
additional matched target.  The general exact two-collar theorem explaining
this mechanism is as follows.

* Delete all old cells whose complete signatures meet the two compound
  collars and retain the common stable graph \(K\).
* Let \(O\) be the old boundary cells and \(N\) the final compound boundary
  cells.
* The compound is a projected Hall descent precisely when the new boundary
  supplies one more alternating portal through \(K\):

  \[
  \boxed{
  \pi_K(N)\ge \pi_K(O)+1,
  }
  \tag{0.8}
  \]

  where

  \[
  \pi_K(B)=\nu(K\cup B)-\nu(K).
  \tag{0.9}
  \]

Equivalently, for every target shore \(Y\),

\[
 n_N(Y)-n_O(Y)\ge1-\sigma_{25}(Y),
\tag{0.10}
\]

where \(n_B(Y)\) counts boundary cells adjacent to \(Y\), and
\(\sigma_{25}\) is the old Hall slack.

For a compound of two three-cut braids at depth three, there are at most six
changed seams and at most \(180\) candidate Hall cells on each side.
Therefore only H25 shores of slack at most \(180\) can obstruct a one-unit
compound descent.

The portal theorem is exact at the one-pin matching level.  It is not a
literal compiler theorem.  A selected portal augmentation must additionally
pass the final common-\(Q_x\) conditions:

\[
 Q_x=
 \{p:x\in P_p\}
 \setminus
 \bigcup_{\alpha:x\notin S_\alpha}I_\alpha,
\tag{0.11}
\]

with central positive hits, pin positive hits, and nonempty point cores.
Those physical conditions remain global because the selected lower pins are
globally exceptional, even though the graph edit is collar-local.

## 1. Frozen H25 data

Let

\[
 T=(T_0,\ldots,T_{6434}),
 \qquad
 T_i\in {[15]\choose8},
\tag{1.1}
\]

be the path in

\[
\texttt{scratch/k15_segment_braid_hall25.json}.
\tag{1.2}
\]

The audited finite facts used in this note are:

1. \(T\) is a Hamilton path through all rank-eight masks;
2. it is depth-three resident;
3. every upper target of rank \(8+q\), \(1\le q\le7\), occurs as a union
   of \(q+1\) consecutive owners;
4. the lower shadow-hole vector by depth is

   \[
   (4,19,4,1,0,0,0);
   \tag{1.3}
   \]

5. its one-pin lower compiler graph has the parameters (0.1);
6. the exact DM shore is (0.2)--(0.4);
7. exactly seven targets have no candidate cell:

   \[
   \boxed{
   2575,5801,13616,13620,17738,21641,29776;
   }
   \tag{1.4}
   \]

8. target \(6308\) has degree \(14\), so it is not an isolated prerequisite
   for further Hall descent; and
9. exhaustive evaluation of the safe FF, RF, FR, and RR single-three-cut
   catalogue finds no carrier of deficiency below \(25\).

The H25 shore is a persistent shield along the whole certified descent
chain.  If \(G_{29},G_{28},G_{27},G_{26},G_{25}\) are the five successive
graphs, then

\[
 |\mathcal A_{25}|-|N_{G_j}(\mathcal A_{25})|=25
 \qquad(j=29,28,27,26,25).
\tag{1.5}
\]

Thus the earlier four one-unit moves removed other active deficits without
changing this eventual H25 obstruction.  Any strict next move must finally
increase the neighbourhood of \(\mathcal A_{25}\), as required by (4.6).

The path and Hall data are independently recomputed in

\[
\texttt{scratch/k15_segment_braid_descent_audit_20260728.json}
\tag{1.6}
\]

and

\[
\texttt{scratch/audit_k15_segment_braid_descent.py}.
\tag{1.7}
\]

The local-minimum assertion in item 9 is frozen separately in

\[
 \texttt{MATH\_K15\_THREE\_CUT\_SEGMENT\_BRAID\_DESCENT\_20260728.md}.
\tag{1.8}
\]

It is used here as certified finite input; it is not inferred from the Hall
audit JSON alone.
The mathematical results below explain exactly what a richer two-collar
certificate must contain.

### 1.1 Exact radius-two portal witness

After the first draft of this reduction, the bounded compound gate was
settled positively in

\[
 \texttt{MATH\_K15\_TWO\_BRAID\_DM\_PORTAL\_ESCAPE\_20260728.md}.
\tag{1.9}
\]

Starting at \(T\), put

\[
 \beta=\operatorname{FR}(1512,2458,4103),
 \qquad
 \gamma=\operatorname{FR}(2664,3491,6201),
\tag{1.10}
\]

where \(\gamma\) is evaluated on the chronology after \(\beta\).  The frozen
carriers are

\[
 \texttt{scratch/k15\_segment\_braid\_hall25\_portal.json}
\quad\text{and}\quad
 \texttt{scratch/k15\_segment\_braid\_hall24.json}.
\tag{1.11}
\]

The full cross-gap and boundary-rank audit is frozen in
\(\texttt{scratch/k15\_segment\_braid\_hall24\_portal\_audit.json}\).

Both the intermediate and final carriers are deck-exact Johnson paths,
depth-three resident, complete on every upper depth \(1,\ldots,7\), and
retain four immediate-lower support holes.  Their exact Hall chronology is

\[
 h(G_{25})=25,\qquad
 h(G_{\beta})=25,\qquad
 h(G_{\gamma\beta})=24.
\tag{1.12}
\]

Let \(\mathcal A_0,\mathcal A_1,\mathcal A_2\) be the canonical DM shores of
\(G_{25},G_\beta,G_{\gamma\beta}\), respectively.  With graphs indexing rows
and shores indexing columns, their exact cross-gap matrix is

\[
 \left(
 |\mathcal A_j|-|N_{G_i}(\mathcal A_j)|
 \right)_{0\le i,j\le2}
 =
 \begin{pmatrix}
 25&24&23\\
 22&25&24\\
 21&24&24
 \end{pmatrix}.
\tag{1.13}
\]

Thus the old canonical shore \(\mathcal A_{25}=\mathcal A_0\) has chronology
\(25\to22\to21\), the first column, not the first row.  The new shore
\(\mathcal A_1\) replaces it at value \(25\) after \(\beta\).
If \(J_\beta\) and \(J_{\gamma\mid\beta}\) denote the two sequential
neighbourhood currents, the matrix gives the exact active-shore ledger

\[
\begin{array}{c|rr}
Y&J_\beta(Y)&J_{\gamma\mid\beta}(Y)\\ \hline
\mathcal A_0& 3&1\\
\mathcal A_1&-1&1\\
\mathcal A_2&-1&0
\end{array}.
\tag{1.14}
\]

The neutral first move therefore opens three units on the old DM shore but
spends one unit on each replacement shore; the second move repairs
\(\mathcal A_1\) and lowers the maximum.
In the two sequential stable-core contractions, the boundary portal
capacities are

\[
 15\longrightarrow15,
 \qquad
 20\longrightarrow21.
\tag{1.15}
\]

The first move is consequently a genuine plateau move, while the second
supplies the extra portal unit in Theorem 5.2.  For the one common stable
core of the whole at-most-seven-block compound, Theorem 5.2 and (1.12) also
imply directly

\[
 \pi_K(N)-\pi_K(O)=1.
\tag{1.16}
\]

The second current is state-dependent.  For every shore \(Y\),

\[
 |N_{G_{\gamma\beta}}(Y)|-|N_{G_{25}}(Y)|
 =
 \bigl(|N_{G_\beta}(Y)|-|N_{G_{25}}(Y)|\bigr)
 +
\bigl(|N_{G_{\gamma\beta}}(Y)|-|N_{G_\beta}(Y)|\bigr).
\tag{1.17}
\]

It would be invalid to replace the last bracket by the current of the same
numerical cuts applied directly at H25.  Accordingly the exact witness is
governed unconditionally by Theorems 4.1 and 5.2; the cross-witness
Theorem 6.1 applies only if both standalone H25 moves satisfy its separate
safety hypothesis.

This closes the projected two-collar existence question.  It does not close
the physical question: neither frozen H25 matching nor the resulting H24
matching is yet supplied with one simultaneous common-\(Q_x\) compiler.

## 2. Hall slack is the exact local-minimum energy

Let \(G=(L,R;E)\) be any finite bipartite graph with all left vertices
required.  Define

\[
 h(G)=|L|-\nu(G)
     =\max_{Y\subseteq L}\bigl(|Y|-|N_G(Y)|\bigr).
\tag{2.1}
\]

For a fixed base graph of deficiency \(h\), define its shore slack

\[
 \sigma_G(Y)
 =
 h-\bigl(|Y|-|N_G(Y)|\bigr)
 \ge0.
\tag{2.2}
\]

Thus the critical Hall shores are exactly the zero set of
\(\sigma_G\).  Since \(Y\mapsto |N_G(Y)|\) is submodular,
\(\sigma_G\) is submodular.  Its zero shores form a lattice under union and
intersection.

For H25 write simply

\[
 \sigma(Y)=
 25-|Y|+|N_{G_{25}}(Y)|.
\tag{2.3}
\]

The canonical DM shore \(\mathcal A_{25}\) satisfies
\(\sigma(\mathcal A_{25})=0\).

The functional \(h(G)\), not a quadratic collision energy, is the exact
local-minimum potential.  It is a maximum of linear cut deficits.  A
descent must improve every currently or nearly critical cut, and the active
cut may change after the move.

## 3. One-pin cell signatures and collar locality

Let \(d\ge1\), let \(T\) be a resident middle chronology, and let \(P\) be
its maximal erosion.  For a physical lower cell

\[
 c=(s,e),
 \qquad
 0\le e<d,
 \qquad
 I_c=[s,s+e],
\tag{3.1}
\]

put

\[
 E_c=\bigcup_{p\in I_c}P_p.
\tag{3.2}
\]

For \(x\in T_i\), define its central carrier set

\[
 C_{i,x}=\{p\in[i,i+d]:x\in P_p\},
\tag{3.3}
\]

and define the cell-mandatory mask

\[
 F_c=
 \{x:\text{ for some }i,\ x\in T_i
                   \text{ and }C_{i,x}\subseteq I_c\}.
\tag{3.4}
\]

### Lemma 3.1 (exact one-pin predicate)

A target \(S\) is adjacent to cell \(c\) in the exact one-pin compiler graph
if and only if

\[
 F_c\subseteq S\subseteq E_c
\tag{3.5}
\]

and

\[
 S\cap P_p\ne\varnothing
 \qquad(p\in I_c).
\tag{3.6}
\]

#### Proof

Pinning \(I_c\) to \(S\) deletes every coordinate outside \(S\) on the
whole cell.  A central occurrence \(x\in T_i\) is lost exactly when all of
its available positions \(C_{i,x}\) lie in the deleted cell, giving the
left inclusion in (3.5).  Every positive coordinate of \(S\) must occur in
the cell, giving the right inclusion.  The maximal letter at \(p\in I_c\)
is \(P_p\cap S\), so (3.6) is exactly source nonzeroness.  These are the
one-pin common-\(Q_x\) conditions.  \(\square\)

The complete signature

\[
 \Sigma_T(c)=
 \bigl(E_c,F_c,(P_p)_{p\in I_c}\bigr)
\tag{3.7}
\]

depends only on

\[
 P_{s-d},P_{s-d+1},\ldots,P_{s+e+d},
\tag{3.8}
\]

with boundary truncation.

At a carrier seam between middle positions \(a-1\) and \(a\), precisely

\[
 P_a,P_{a+1},\ldots,P_{a+d-1}
\tag{3.9}
\]

have erosion windows crossing that seam.  A cell signature can therefore
change at that seam only if

\[
 a-e-d\le s\le a+2d-1.
\tag{3.10}
\]

There are \(e+3d\) such starts.  Summing through \(e=0,\ldots,d-1\) gives

\[
 h_d=\sum_{e=0}^{d-1}(e+3d)
     =\frac{7d^2-d}{2}
\tag{3.11}
\]

candidate cells per seam.  At \(d=3\),

\[
 h_3=30.
\tag{3.12}
\]

This is a proof-safe complete-signature bound.  A smaller controller-only
collar omits the lookback required by the mandatory mask (3.4).

## 4. Two-collar Hall current

Let \(G_0=G_{25}\), and let \(G_*\) be the one-pin graph of a final compound
carrier.  Identify every right cell whose complete signature is transported
unchanged.  Let \(K\) be the resulting common stable graph, and write

\[
 G_0=K\cup O,
 \qquad
 G_*=K\cup N,
\tag{4.1}
\]

where \(O\) and \(N\) are multisets of distinct old and new boundary cells.
Cells with equal neighbourhoods remain distinct physical right vertices.

For a target shore \(Y\subseteq L\), put

\[
 n_B(Y)=
 |\{c\in B:N(c)\cap Y\ne\varnothing\}|.
\tag{4.2}
\]

The stable neighbourhood cancels, so the exact compound current is

\[
 \Delta_*(Y)
 =
 |N_{G_*}(Y)|-|N_{G_0}(Y)|
 =
 n_N(Y)-n_O(Y).
\tag{4.3}
\]

### Theorem 4.1 (two-collar cut criterion)

The final compound has Hall deficiency at most \(24\) if and only if

\[
 \boxed{
 n_N(Y)-n_O(Y)\ge1-\sigma(Y)
 \qquad(Y\subseteq L).
 }
\tag{4.4}
\]

Equivalently,

\[
 h(G_*)
 =
 25-\min_{Y\subseteq L}
 \bigl(\sigma(Y)+\Delta_*(Y)\bigr).
\tag{4.5}
\]

In particular every compound descent must satisfy the exact H25 DM portal
inequality

\[
 \boxed{
 n_N(\mathcal A_{25})
 \ge
 n_O(\mathcal A_{25})+1.
 }
\tag{4.6}
\]

#### Proof

For every shore \(Y\),

\[
\begin{aligned}
 |Y|-|N_{G_*}(Y)|
 &=
 |Y|-|N_{G_0}(Y)|-\Delta_*(Y)\\
 &=
 25-\sigma(Y)-\Delta_*(Y).
\end{aligned}
\tag{4.7}
\]

Take the maximum over \(Y\).  The inequality \(h(G_*)\le24\) is equivalent
to (4.4).  Apply it to the zero-slack shore
\(\mathcal A_{25}\) to obtain (4.6).  \(\square\)

If \(|O|,|N|\le H\), then

\[
 -H\le\Delta_*(Y)\le H.
\tag{4.8}
\]

Therefore shores with \(\sigma(Y)\ge H+1\) satisfy (4.4) automatically.

### Corollary 4.2 (exact boundary-hit-profile compression)

Pad the old and new boundary banks by empty dummy cells so that they have a
common index set \(\mathcal B\).  For \(c\in\mathcal B\), let
\(U_c^-,U_c^+\subseteq L\) be its old and new target neighbourhoods.  Define
the boundary hit profile of a shore \(Y\) by

\[
 z(Y)=
 \left(
 \mathbf1[U_c^-\cap Y\ne\varnothing],
 \mathbf1[U_c^+\cap Y\ne\varnothing]
 \right)_{c\in\mathcal B},
\tag{4.9}
\]

and define the least old slack in that profile by

\[
 \Sigma(z)=\min\{\sigma(Y):z(Y)=z\},
\tag{4.10}
\]

with value \(+\infty\) for an unrealized profile.  Then

\[
 \boxed{
 \min_Y\bigl(\sigma(Y)+\Delta_*(Y)\bigr)
 =
 \min_z\left[
 \Sigma(z)+
 \sum_{c\in\mathcal B}(z_c^+-z_c^-)
 \right].
 }
\tag{4.11}
\]

Thus the full Hall audit of a fixed compound factors through the finite
boundary-hit profiles.  For a two-braid depth-three compound, only profiles
with \(\Sigma(z)\le180\) can obstruct descent.

The padded signature has at most \(180+180=360\) bits, and hence at most
\(2^{360}\) formal profiles.  This is an exact finite catalogue; it is not
a claim that the number of realized profiles has a small polynomial bound.

#### Proof

The current (4.3) depends on \(Y\) only through \(z(Y)\).  Minimize the old
slack first within each fibre of the profile map and then over profiles.
\(\square\)

## 5. Alternating portals and the exact cut dual

The cut criterion has a constructive matching form.

For a boundary multiset \(B\), define its portal capacity over the stable
graph \(K\) by

\[
 \pi_K(B)=\nu(K\cup B)-\nu(K).
\tag{5.1}
\]

Fix a maximum matching \(M\) in \(K\).  Form the usual alternating digraph:

1. orient every nonmatching edge from left to right;
2. orient every matching edge from right to left;
3. connect a source to every \(M\)-unmatched left vertex;
4. append the boundary cells \(B\), with their incident edges directed from
   left vertices into \(B\); and
5. connect every boundary cell to a sink.

Split all graph vertices and give them unit capacity.

### Theorem 5.1 (portal packing/cut duality)

For every boundary multiset \(B\), the following three quantities are equal:

1. \(\pi_K(B)\);
2. the maximum number of pairwise vertex-disjoint \(M\)-alternating paths
   from unmatched left vertices to distinct cells of \(B\); and
3. the minimum capacity of a vertex cut separating the unmatched left
   vertices from all boundary cells.

#### Proof

Any family of \(t\) disjoint alternating paths augments \(M\) by \(t\), so
\(\pi_K(B)\ge t\).  Conversely, take a maximum matching \(M'\) of
\(K\cup B\).  The symmetric difference \(M\triangle M'\) decomposes into
alternating cycles and paths.  Since \(M\) is maximum in \(K\), every
component contributing positively to \(|M'|-|M|\) starts at an
\(M\)-unmatched left vertex and ends at a new boundary cell.  A component
on which \(M\) has one more edge than \(M'\) cannot occur, since replacing
\(M'\) by \(M\) on that disjoint component would enlarge the maximum
matching \(M'\).  Thus the positive components are vertex-disjoint and
their number is exactly
\(|M'|-|M|=\pi_K(B)\).  The equality with the minimum vertex cut is the
integral max-flow/min-cut theorem in the vertex-split network.  \(\square\)

Boundary cells are therefore literal matching portals, not merely new
neighbour counts.

### Theorem 5.2 (two-collar portal theorem)

With the stable decomposition (4.1),

\[
 \boxed{
 \nu(G_*)-\nu(G_0)=\pi_K(N)-\pi_K(O).
 }
\tag{5.2}
\]

Consequently the compound is a strict Hall descent if and only if

\[
 \boxed{
 \pi_K(N)\ge\pi_K(O)+1.
 }
\tag{5.3}
\]

Equivalently, the final boundary admits one more disjoint alternating
portal path than the old boundary, and the final source-to-boundary minimum
cut value exceeds the corresponding old minimum-cut value by at least one.
The minimizing cuts need not be the same on the two sides.

#### Proof

By definition,

\[
 \nu(G_0)=\nu(K)+\pi_K(O),
 \qquad
 \nu(G_*)=\nu(K)+\pi_K(N).
\tag{5.4}
\]

Subtract.  The remaining equivalences follow from Theorem 5.1. \(\square\)

This theorem is the exact constructive target for a two-collar search.
Counting new cells is insufficient: they must survive the alternating
network's vertex capacities and jointly supply an extra portal.

### Theorem 5.3 (repair paths plus one extra portal)

Fix a maximum matching \(M_{25}\) of \(G_{25}\).  Let

\[
 M_{\rm ret}=M_{25}\cap E(G_*)
\tag{5.5}
\]

be the old matching edges which remain present in the final compound graph,
and put

\[
 r=|M_{25}|-|M_{\rm ret}|.
\tag{5.6}
\]

Orient the final graph relative to the partial matching \(M_{\rm ret}\),
split vertices with unit capacity, and let \(\alpha\) be the maximum number
of pairwise vertex-disjoint augmenting paths from
\(M_{\rm ret}\)-unmatched left vertices to
\(M_{\rm ret}\)-unmatched right vertices.  Then

\[
 \boxed{
 h(G_*)=25+r-\alpha.
 }
\tag{5.7}
\]

In particular,

\[
 \boxed{
 h(G_*)\le24
 \quad\Longleftrightarrow\quad
 \alpha\ge r+1.
 }
\tag{5.8}
\]

#### Proof

The retained matching has size

\[
 |M_{\rm ret}|=16\,358-r.
\tag{5.9}
\]

For any partial matching, the maximum number of simultaneous
vertex-disjoint augmenting paths equals the difference between the maximum
matching size and the partial matching size.  This follows by decomposing
the symmetric difference with a final maximum matching; conversely,
toggling disjoint augmenting paths increases the matching by their number.
Hence

\[
 \nu(G_*)=16\,358-r+\alpha.
\tag{5.10}
\]

Subtract from \(16\,383\).  \(\square\)

An explicit sufficient portal menu is therefore:

1. \(r\) disjoint repair paths restoring the left endpoints exposed when
   old collar matching edges disappear; and
2. one additional disjoint path beginning at an original H25-unmatched
   target and ending at a final free cell.

The extra path may enter through a first collar, traverse the stable
alternating core, and leave through a second collar.  Contracting the stable
core preserves reachability but not vertex-disjointness; the unit-capacity
network in Theorem 5.3 is authoritative.

## 6. The interaction current and the local-minimum dichotomy

Suppose two proposed collar operations give graphs \(G_1,G_2\), while their
compound gives \(G_{12}\).  All are compared to \(G_0=G_{25}\) after stable
cell identification.  Define

\[
 \Delta_j(Y)=|N_{G_j}(Y)|-|N_{G_0}(Y)|
 \qquad(j=1,2),
\tag{6.1}
\]

and define the exact mixed interaction, or collar holonomy,

\[
 \boxed{
 \Omega_{12}(Y)
 =
 |N_{G_{12}}(Y)|
 -|N_{G_1}(Y)|
 -|N_{G_2}(Y)|
 +|N_{G_0}(Y)|.
 }
\tag{6.2}
\]

Then

\[
 \Delta_{12}(Y)
 =
 \Delta_1(Y)+\Delta_2(Y)+\Omega_{12}(Y).
\tag{6.3}
\]

If the two moves have disjoint dependency collars and simply replace their
two boundary multisets independently, then

\[
 \Omega_{12}\equiv0.
\tag{6.4}
\]

Nonzero \(\Omega_{12}\) records a genuinely fused seam signature, an overlap
correction, or noncommutativity of the two block operations.

Suppose now that each standalone move \(j\) is itself a resident,
upper-safe member of the certified H25 single-three-cut catalogue.  Because
H25 is a local minimum in that catalogue, each such move has a nonempty
witness family

\[
 \mathcal W_j
 =
 \{Y:\sigma(Y)+\Delta_j(Y)\le0\}.
\tag{6.5}
\]

### Theorem 6.1 (cross-witness portal theorem for two safe constituent moves)

If the compound \(G_{12}\) has deficiency at most \(24\), then:

1. at the canonical DM shore,

   \[
   \Delta_1(\mathcal A_{25})
   +\Delta_2(\mathcal A_{25})
   +\Omega_{12}(\mathcal A_{25})
   \ge1;
   \tag{6.6}
   \]

2. for every \(Y\in\mathcal W_1\),

   \[
   \Delta_2(Y)+\Omega_{12}(Y)
   \ge
   1-\sigma(Y)-\Delta_1(Y)
   \ge1;
   \tag{6.7}
   \]

3. symmetrically, for every \(Y\in\mathcal W_2\),

   \[
   \Delta_1(Y)+\Omega_{12}(Y)\ge1.
   \tag{6.8}
   \]

Conversely, the compound descends if and only if

\[
 \sigma(Y)+\Delta_1(Y)+\Delta_2(Y)+\Omega_{12}(Y)\ge1
 \qquad(Y\subseteq L).
\tag{6.9}
\]

#### Proof

Equation (6.9) is Theorem 4.1 and (6.3).  Apply it first to
\(\mathcal A_{25}\), and then subtract
\(\sigma(Y)+\Delta_1(Y)\le0\) for
\(Y\in\mathcal W_1\).  The other case is symmetric.  \(\square\)

The hypothesis that both standalone moves are safe is essential for
(6.7)--(6.8).  An arbitrary seven-block compound may have an unsafe or even
undefined intermediate carrier.  If its standalone graphs are still
defined, only (6.6) and (6.9) survive; without them one must use the raw
DM and all-shore criteria (4.6) and (4.4).

This gives the following exact structural split.

### Corollary 6.2 (complementarity versus fusion)

Every compound of two individually safe H25 catalogue moves has one of the
following structural forms.

1. **Cut complementarity.**  The interaction current vanishes.  One collar
   opens the H25 DM portal, while the other supplies positive current on
   every witness cut blocking the first; the same holds with the roles
   reversed.
2. **Nonadditive interaction.**  The mixed current is nonzero somewhere.
   It is *forced for the escape* only if some active shore \(Y\) obeys

   \[
   \sigma(Y)+\Delta_1(Y)+\Delta_2(Y)\le0
   \quad\hbox{but}\quad
   \sigma(Y)+\Delta_1(Y)+\Delta_2(Y)+\Omega_{12}(Y)\ge1.
   \tag{6.10}
   \]

   In particular, if both individual collars have nonpositive current on
   \(\mathcal A_{25}\), then necessarily

   \[
   \Omega_{12}(\mathcal A_{25})
   \ge
   1-\Delta_1(\mathcal A_{25})
    -\Delta_2(\mathcal A_{25})
   \ge1.
   \tag{6.11}
   \]

Thus a pair of collars which are both DM-nonpositive and have no fused
signature cannot escape the local minimum.

This is the positive-cut form of the local-minimum theorem.  It specifies
what interaction must be sought instead of merely enlarging the move
radius.

## 7. Exact weighted-Gram interpretation

The portal network provides the correct integral object behind a weighted
Gram heuristic.

Let \(\Gamma(B)\) be the family of all simple \(M\)-alternating paths from
unmatched left roots to boundary cells.  For each path \(\gamma\), let

\[
 v_\gamma\in\{0,1\}^{V(K)}
\tag{7.1}
\]

be its incidence vector on all stable graph vertices, including its
unmatched left starting vertex and excluding only its new boundary-cell
endpoint.  Give every stable graph vertex a strictly positive weight
\(w_z\), and define

\[
 \mathsf G_{\gamma,\gamma'}
 =
 \sum_{z\in V(K)}
 w_z\,v_\gamma(z)v_{\gamma'}(z).
\tag{7.2}
\]

### Lemma 7.1 (Gram portal certificate)

A path subfamily \(\mathcal P\subseteq\Gamma(B)\), with distinct boundary
endpoints, is pairwise vertex-disjoint if and only if its weighted Gram
matrix has zero off-diagonal entries.  Consequently,

\[
 \pi_K(B)
 =
 \max\{|\mathcal P|:
       \mathsf G[\mathcal P]\text{ is diagonal and the boundary endpoints
       are distinct}\}.
\tag{7.3}
\]

#### Proof

Strict positivity of the weights makes
\(\mathsf G_{\gamma,\gamma'}=0\) equivalent to disjoint internal supports.
Theorem 5.1 identifies the largest such path packing with \(\pi_K(B)\).
\(\square\)

The decisive local-minimum quantity is therefore not the average Gram
energy.  It is the maximum zero-overlap portal packing, equivalently the
minimum portal cut.  A quadratic decrease which does not increase
\(\pi_K\) does not improve Hall deficiency.

The exact H25 DM indicator provides one mandatory linear weight:

\[
 \ell_{25}(c)
 =
 \mathbf1[N(c)\cap\mathcal A_{25}\ne\varnothing].
\tag{7.4}
\]

Every compound descent must have net positive \(\ell_{25}\)-current by
(4.6), but that one weight is not sufficient.  The cross-witness family in
Theorem 6.1 supplies the additional active cut weights.

## 8. Bounded seven-block catalogue for two three-cuts

Composition of two three-cut braids need not be tested as two independent
moves.

Start with one linear owner word.  The first move cuts it at at most three
places, producing four oriented intervals.  Pulling the three cuts of a
second move back to the original word splits at most three additional
intervals.  Therefore the final word is a signed permutation of at most
seven original contiguous intervals.

### Theorem 8.1 (bounded compound signature)

Every compound of two three-cut braids has a representation by:

1. at most seven original intervals;
2. at most six final seam adjacencies;
3. at most six old cut adjacencies; and
4. one signed permutation of the intervals.

For such a compound:

* the exact Johnson-path test consists of at most six endpoint adjacency
  tests;
* at depth \(q\), at most \(6q\) old and \(6q\) new lower or upper shadow
  windows are affected, so

  \[
  \|\Delta M_q^\cap\|_1,\ \|\Delta M_q^\cup\|_1\le12q;
  \tag{8.1}
  \]

* depth-\(H\) residence requires at most

  \[
  6\sum_{\ell=1}^{H}(\ell+1)
  =
  3H(H+3)
  \tag{8.2}
  \]

  seam-comparison occurrences before overlap deduplication; and
* the one-pin Hall graph has at most

  \[
  6h_d=3(7d^2-d)
  \tag{8.3}
  \]

  candidate boundary cells on each side.

At \(d=H=3\), the exact proof-safe bounds are

\[
 54\text{ residence comparisons},
 \qquad
 180\text{ Hall boundary cells per side}.
\tag{8.4}
\]

#### Proof

Each new cut can increase the common refinement of the original interval
partition by at most one, giving at most seven atoms.  Internal edges and
windows of every oriented atom transport exactly.  Only the at most six
atom boundaries contribute to the Johnson, shadow, and residence ledgers.
Apply (3.11) at each boundary for the Hall bound.  \(\square\)

This is a rigorous bounded richer-catalogue reduction.  It includes:

* two disjoint commuting collars;
* overlapping collars;
* compounds whose intermediate chronology is not resident or
  upper-complete but whose final chronology is;
* fused signatures with \(\Omega_{12}\ne0\); and
* plateau moves followed by a descent, after multiplying their signed
  interval permutations.

The final candidate need only be audited through its seven-block endpoint
signature, its \(q\le7\) prefix/suffix shadow signatures, its depth-three
transition collars, and its at most \(180\) Hall cells.

The numerical pair (1.10) is an exact successful member of this catalogue.
What remains unproved is a structural characterization of all successful
six-seam signatures or a no-go for the rest of the catalogue.

## 9. The common-\(Q_x\) physical theorem

The portal/cut theorem is still a projected matching theorem.

Let \(T^*\) be a final compound carrier, let \(P^*\) be its maximal
depth-three erosion, and let

\[
 \phi:\mathcal S\hookrightarrow\mathcal C
\tag{9.1}
\]

be a selected partial target-to-cell injection.  Write

\[
 I_S=I_{\phi(S)}
\tag{9.2}
\]

for the physical interval assigned to target \(S\).  For each coordinate
\(x\in[15]\), define the final maximal common support

\[
 \boxed{
 Q_x(\phi)
 =
 \{p:x\in P^*_p\}
 \setminus
 \bigcup_{S\in\mathcal S:\ x\notin S} I_S.
 }
\tag{9.3}
\]

### Theorem 9.1 (exact physical portal installation)

There is one nonzero physical word \(A\) satisfying

\[
 D^3A=T^*
\tag{9.4}
\]

and

\[
 \bigcup_{p\in I_S}A_p=S
 \qquad(S\in\mathcal S)
\tag{9.5}
\]

if and only if all three conditions hold:

\[
 Q_x(\phi)\cap[i,i+3]\ne\varnothing
 \qquad(i,\ x\in T_i^*),
\tag{9.6}
\]

\[
 Q_x(\phi)\cap I_S\ne\varnothing
 \qquad(S\in\mathcal S,\ x\in S),
\tag{9.7}
\]

and

\[
 \{x:p\in Q_x(\phi)\}\ne\varnothing
 \qquad(p=0,\ldots,6437).
\tag{9.8}
\]

When these conditions hold, the coordinatewise maximal literal compiler is

\[
 \boxed{
 A_p=\{x:p\in Q_x(\phi)\}.
 }
\tag{9.9}
\]

#### Proof

The central pins force \(A_p\subseteq P_p^*\).  Every selected pin whose
label omits \(x\) forbids \(x\) throughout its interval, so every feasible
support is contained in (9.3).  Conditions (9.6) and (9.7) are exactly all
central and selected-pin positive hits, while (9.8) is source
nonzeroness.  Maximality then proves both necessity and sufficiency.
\(\square\)

### Corollary 9.2 (port/gap form)

On every internal maximal \(x\)-run \([u,v]\) of \(P^*\), condition (9.6)
is equivalent to:

1. \(u,v\in Q_x(\phi)\); and
2. consecutive surviving positions of \(Q_x(\phi)\cap[u,v]\) have distance
   at most \(4\).

Equivalently, after all selected negative pins are united and touching
pieces coalesced, every deleted component has at most three positions and
no forced internal endpoint is deleted.  Boundary runs have the exact
one-sided version.

This test is global.  Two matched cells in different Hall collars can omit
the same coordinate, and their deletions can coalesce through transported
exceptional pins even when the matching portal paths are disjoint.

### Corollary 9.3 (when the Boolean audit localizes)

Let \(\Pi_{\rm off}^{\rm old}\) and \(\Pi_{\rm off}^*\) be the selected pin
families outside the compound collars, identified by the signed block
transport.  Suppose that for every coordinate \(x\),

\[
 \bigcup_{\substack{(I,S)\in\Pi_{\rm off}^*\\x\notin S}} I
 =
 \operatorname{transport}\left(
 \bigcup_{\substack{(I,S)\in\Pi_{\rm off}^{\rm old}\\x\notin S}} I
 \right).
\tag{9.10}
\]

Then the off-collar negative Boolean current is zero.  If the old pin system
had a common compiler, the final common-\(Q_x\) audit reduces to:

1. changed pins in the compound collars;
2. stable positive pins whose chosen witness lies in a changed collar;
3. central windows meeting a changed controller position;
4. controller runs whose deleted components meet a collar boundary; and
5. point cores in the collars.

Without (9.10), an alternating matching path can relabel stable cells far
from the geometric graph edit, and Hall locality does not imply physical
locality.

#### Proof

Equation (9.10) says exactly that the forbidden-position union in (9.3) is
transported unchanged off the collars.  Hence every old off-collar central,
positive-pin, run-gap, and nonzero witness survives unless its support meets
a changed controller or pin position.  These are precisely the five listed
families.  \(\square\)

## 10. Literal two-collar portal theorem

The matching portal theorem and common-\(Q_x\) theorem combine without any
hidden implication.

### Theorem 10.1 (conditional literal compound descent)

Assume:

1. a maximum old target injection \(\phi_0\), with domain
   \(\mathcal S_0\) and size \(\nu(G_0)\), has one common compiler, and let
   \(M_0\) be its matching in \(G_0\);
2. a final seven-block compound carrier \(T^*\) passes exact deck, Johnson,
   depth-three residence, and every upper last-witness test;
3. after transporting stable cells, let

   \[
   M_{\rm ret}=M_0\cap E(G_*),
   \qquad
   r=|M_0|-|M_{\rm ret}|.
   \tag{10.1}
   \]

   Relative to \(M_{\rm ret}\), the final unit-capacity alternating network
   contains \(r+1\) disjoint augmenting paths whose starting vertices are
   all \(r\) targets of \(\mathcal S_0\) exposed by deleted \(M_0\)-edges,
   together with one target in \(L\setminus\mathcal S_0\);
4. let \(\phi_*\) be the matching obtained by toggling those paths; and
5. the complete injection \(\phi_*\), including every transported stable
   pin, satisfies (9.6)--(9.8).

Then one literal final word realizes every transported old target and one
additional target.

#### Proof

Toggling the \(r+1\) paths repairs every old domain target exposed by the
compound and matches one formerly absent target, while all untouched
\(M_0\)-edges remain.  Thus \(\phi_*\) extends the transported domain
\(\mathcal S_0\) by one target.  In particular it implies the unlabelled
portal gain of Theorem 5.2.  Theorem 9.1 turns that complete injection, not
merely its individual edges, into one physical word.  \(\square\)

The weaker cardinality condition
\(\pi_K(N)\ge\pi_K(O)+1\) alone does **not** imply this labelled extension:
a larger final matching may drop one target of \(\mathcal S_0\) and add two
others.  This is why item 3 freezes every exposed old-domain source.

The common-\(Q_x\) hypothesis in item 5 can be certified structurally by the
native--laminar theorem:

1. recompute every pin against the final global controller \(P^*\);
2. treat trace pins \(S=\bigcup_{p\in I}P_p^*\) as negative-inert;
3. place all changed exceptional pins and all transported exceptional pins
   meeting them in common collar clusters;
4. in a laminar cluster, require nested labels and the exact atom condition;
5. retain all native positive anchors;
6. retain all forced controller ports and keep every coalesced deletion
   component of length at most three; and
7. keep every point core nonempty.

The fact that each individual physical cell has length at most three is not
sufficient.  Adjacent exceptional cells can make a longer deleted component.

### H25 scope warning

No old H25 matching of size \(16\,358\) is presently certified as one
simultaneous compiler.  Moreover, every rank-at-most-four target is
necessarily exceptional because every nonempty controller trace has rank at
least five.  There are

\[
 \sum_{j=1}^{4}{15\choose j}=1940
\tag{10.2}
\]

such exceptional targets.  An arbitrary maximum H25 matching can omit
twenty-five targets, so the universal guarantee is only

\[
 1940-25=1915
\tag{10.3}
\]

matched global exceptional pins.  The particular audited deterministic
maximum omits only ranks six and seven and therefore matches all \(1940\);
that stronger count is a property of that matching, not of every maximum
matching.  A two-collar graph edit does not localize this physical
exceptional family.

Therefore Theorem 10.1 is an exact conditional bridge, not a claim that an
H25 Hall portal is already a literal contiguous-OR gain.

## 11. Strongest proved boundary

The following are proved.

1. H25 has the exact DM cut (0.2)--(0.4), Hall deficiency \(25\), lower-hole
   vector (1.3), and seven isolated targets (1.4).
2. It is a certified local minimum for the complete safe single-three-cut
   catalogue.
3. A compound two-collar Hall descent is equivalent both to the all-shore
   inequality (4.4) and to the extra alternating portal condition (5.3).
4. Every compound of two individually safe H25 catalogue moves obeys the
   cross-witness inequalities (6.6)--(6.8); an arbitrary seven-block
   compound obeys the raw criteria (4.6) and (4.4), with (6.6) and (6.9)
   available only when its standalone graphs are defined.
5. Such a safe two-move compound is structurally additive or has nonzero
   interaction current \(\Omega_{12}\); the interaction is causally forced
   only when it repairs an otherwise blocking active cut as in (6.10).
6. Every compound of two three-cuts reduces to a signed permutation of at
   most seven original intervals, at most six seam tests, and at most
   \(180\) candidate Hall cells per side.
7. The explicit pair (1.10) realizes the portal gain: it has Hall chronology
   \(25\to25\to24\), old-DM chronology \(25\to22\to21\), and sequential
   boundary capacities \(15\to15\) and \(20\to21\).
8. A matching portal becomes literal exactly after the final injection
   passes the common-\(Q_x\) conditions (9.6)--(9.8).

The following remain open.

1. A size-\(16\,359\) matching on the frozen H24 carrier whose physical
   pins pass common \(Q_x\).
2. A labelled repair-plus-one augmentation of a common-\(Q_x\) H25 matching
   through the exact pair (1.10), should such an H25 matching be supplied.
3. A structural characterization of successful seven-block signatures and
   a continuation below Hall \(24\).
4. Any implication from projected Hall \(24\), or even Hall zero, to a literal
   compiler without the physical test.

The next bounded theorem target is therefore precise:

\[
\boxed{
\begin{gathered}
\text{on the already certified H24 carrier, select a matching }
\phi_{24}\text{ of size }16\,359,\\
\text{and verify }Q_x(\phi_{24})\text{ satisfies }
(9.6)\text{--}(9.8)\text{ simultaneously for every }x.
\end{gathered}
}
\tag{11.1}
\]

Searching only for a lower Hall score omits the last line.  Searching only
for a low quadratic or Gram energy omits the integral portal packing and its
cut dual.
