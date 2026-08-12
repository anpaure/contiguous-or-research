# The exact rank-one obstruction to the contiguous intersection lift

Let

\[
T_0,T_1,\ldots,T_{N-1}\in\binom{[k]}r
\]

be a linear Johnson path and suppose we want a nonzero base word
\(A_0,\ldots,A_{N+1}\) with

\[
T_i=A_i\cup A_{i+1}\cup A_{i+2}.
\]

Write \(E_p\) for the maximal erosion envelope,

\[
E_p=\bigcap_{\max(0,p-2)\le i\le\min(p,N-1)}T_i.
\]

Every realization has \(A_p\subseteq E_p\).

## 1. Forced cores

For each required incidence \((i,x)\) with \(x\in T_i\), inspect the
eligible witnesses

\[
\{p\in\{i,i+1,i+2\}:x\in E_p\}.
\]

If this set is a singleton \(\{p\}\), then every realization must have
\(x\in A_p\).  Let \(C_p\) be the union of all coordinates forced this way.

Let

\[
d_i\in T_i\setminus T_{i+1},\qquad
a_i\in T_{i+1}\setminus T_i
\]

be the deleted and inserted coordinates of the Johnson transition at \(i\).
Then the forced cores have the exact closed form

\[
C_p=
\begin{cases}
\{d_p\},&0\le p\le2,\\
\{a_{p-3},d_p\},&3\le p\le N-2,\\
\{a_{p-3}\},&N-1\le p\le N+1.
\end{cases}
\tag{1}
\]

The proof is just the run description.  If a coordinate has an internal
maximal run \([\ell,u]\) in the middle path, it is eligible in the base
precisely on \([\ell+2,u]\).  Its first middle occurrence forces it at
\(\ell+2\), and its last occurrence forces it at \(u\).  Boundary runs give
the first and last cases of (1).

In particular, every base position has a nonempty forced core.  At an
internal position the core has rank one exactly when

\[
a_{p-3}=d_p.
\tag{2}
\]

Equation (2) says that this coordinate has a middle residence run of exactly
three cells.

## 2. Singleton criterion

The singleton \(\{x\}\) can occur in the base row only at a position \(p\)
such that

\[
x\in E_p\quad\hbox{and}\quad C_p\subseteq\{x\}.
\tag{3}
\]

A singleton in the first derivative gives no additional freedom: if
\(A_p\cup A_{p+1}=\{x\}\) and entries are nonzero, then both entries already
equal \(\{x\}\).

Consequently every coordinate must occur in at least one of the following
roles before rank-one coverage is possible:

1. one of the first three deletions;
2. one of the last three insertions;
3. a length-three return \(a_{p-3}=d_p=x\).

This is a much cheaper precheck than the full compiler.

For an exact rank-one feasibility test, choose one position \(s(x)\) obeying
(3) for every coordinate, and also require that every middle incidence
\((i,y)\) retain an eligible witness in \(\{i,i+1,i+2\}\) that is either
unpinned or pinned to \(y\).  This **rank-one pin-safe Hall condition** is
necessary and sufficient: after fixing \(A_{s(x)}=\{x\}\), every remaining
coordinate-incidence can be assigned independently to any surviving
eligible witness, because entries have no upper cardinality capacity and
every added bit remains inside its envelope.

## 3. Exact audit of the persisted candidate

For `scratch/k14_intersection_candidate0.json`:

- forced-core ranks: \(436\) positions of rank one and \(2998\) of rank two;
- empty forced cores: \(0\);
- each old coordinate has \(33\)--\(35\) singleton positions;
- the new coordinate \(x=13\) has **zero** singleton positions.

Thus the explicit Hall witness is the one-target family

\[
\mathcal A=\{\{x\}\},\qquad N(\mathcal A)=\varnothing,
\]

of deficiency one.  The reversed path has exactly the same witness.  SAT
confirms the diagnosis: target rank 1 alone is UNSAT, and therefore every
prefix of target ranks \(1;1\!:\!2;\ldots;1\!:\!6\) is UNSAT.

All 25 calibrated intersection carriers have the same obstruction.  Inside
the all-\(x\) sector their old-coordinate forced-core histogram is
\(432/433\) rank-one and \(1283/1284\) rank-two positions, with no empty
old core.  Relabeling old coordinates cannot change this.

## 4. Consequence for the lift

A path consisting of one contiguous \(x\)-free sector followed by one
contiguous all-\(x\) sector cannot pass the depth-two rank-one compiler.
The new coordinate has one long boundary run; it is neither a boundary
deletion/insertion of the required kind nor a length-three return, while an
old coordinate is forced at every position where \(x\) is eligible.

The carrier feature that must change is therefore not the relabeling.  The
middle chronology must give \(x\) either

- a run of exactly three consecutive middle cells, or
- a first-three-deletion / last-three-insertion boundary flag.

For the natural rank-7 split this means interleaving the \(x\)-bearing and
\(x\)-free sectors.  A local pattern

\[
A\;(x+Q_1)\;(x+Q_2)\;(x+Q_3)\;A'
\]

with \(Q_1,Q_2,Q_3\) a Johnson 3-path makes \(x\) a length-three return and
creates the required singleton slot.  Subsequent searches should impose
the rank-one pin-safe Hall condition before testing upper shadows or calling
the full SAT compiler.

