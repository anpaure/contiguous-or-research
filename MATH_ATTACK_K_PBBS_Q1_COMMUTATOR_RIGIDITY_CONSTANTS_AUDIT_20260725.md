# Independent constants audit: PBBS \(q=1\) commutator rigidity

Date: 2026-07-25

Scope: Sections 2--5 and 8 of
`MATH_ATTACK_K_PBBS_Q1_COMMUTATOR_RIGIDITY_20260725.md` only.  This is a
pure hand audit of the reconstruction, complementation, residual-path,
Lipschitz, averaging, and divisibility constants.  It does not audit the
external PBBS reservoir assertions.

## Verdict

All displayed mathematical formulas audited here are correct.  In
particular, there is no off-by-one error in the complementary upper depth,
the sharp universal boundary-deck constants are indeed \(4q\) and
\(4(q-1)\), and the ternary exception is exactly
\(m\equiv1\pmod 3\).  No counterexample was found, including paths shorter
than the flag window and the cases in which deleted old edges are adjacent.

There is one terminology caveat, not a mathematical correction.  The
quantity \(e\) is simultaneously the number of deleted old factor edges and
the number of maximal common residual paths after common cycles are
discarded.  It is not the number of path endpoints: that number is \(2e\).
Thus the average lower bound \(\delta n/(4H)\) is correct when a “residual
seam” means one cut edge or one residual path.  If “seam” is instead used
for an individual boundary port, the corresponding average is
\(\delta n/(2H)\).  The report should define that word once.  Also, the
quantity \(C\) in the averaging statement must mean affected old complete
\(n\)-wreaths; it should not be read as the number of connected components
of the two-factor overlay.

## 1. Owner-labelled reconstruction

Fix an owner \(X\).  Its complement has size \(m+1\), and every odd-graph
neighbour is an \(m\)-subset of \(X^c\).  Distinct neighbours therefore
have unique forms

\[
Y=X^c\setminus\{a\},\qquad Z=X^c\setminus\{b\},\qquad a\ne b.
\]

Consequently

\[
Y\cap Z=X^c\setminus\{a,b\},
\]

and, if this intersection is denoted by \(\chi\), then

\[
\{Y,Z\}=\{\chi\cup\{a\},\chi\cup\{b\}\}.
\]

This proves (2.2)--(2.4) owner by owner.  It also proves the support
identity (2.7): changing the unordered neighbour pair is equivalent to
changing \(\chi\).  The conclusion remains valid at \(m=1\): the odd graph
is \(K_3\), its spanning two-factor is unique, and \(\chi=\varnothing\).

The same two-element-difference calculation verifies the paired-token
formula (3.5).  A fixed paired map \(S\mapsto U(S)\), with the lower labels
rainbow, fixes every undirected transition edge.  A two-regular edge set
then fixes its cyclic components and hence all deeper flag multisets.

## 2. Complement indexing

For a cyclic row, complementation sends an \(r\)-interval bijectively to an
\((n-r)\)-interval, so

\[
B_{n-r}z=\kappa_r B_rz.
\]

With \(n=2m+1\), the two relevant substitutions are

\[
n-m=m+1,
\qquad
n-(m-h)=m+h+1.
\]

Thus exact middle preservation gives upper depth \(1\), while lower depth
\(h\) preservation gives upper depth \(h+1\).  In particular, lower
\(q=1\) neutrality fixes upper depth \(2\), not upper depth \(1\) or
upper depth \(3\).  Conversely, a lower depth-\(2\) increment is paired
with upper depth \(3\).  Equations (4.2)--(4.4) have the correct indices.

This uses full cyclic-wreath rows.  The report correctly withholds the
identity from raw PBBS long components and separately sourced token rows.

## 3. Boundary-deck count

Let a residual path have \(L\) vertices.  A lower depth-\(q\) flag uses
the stride-two block from positions \(j\) through \(j+2q\), hence uses
\(2q\) consecutive factor edges.  In either orientation, exactly

\[
\max\{L-2q,0\}
\]

starts remain wholly internal.  Therefore the number of boundary-crossing
starts assigned to this path is

\[
L-\max\{L-2q,0\}=\min\{L,2q\}.
\]

Reversal of the path does not spoil cancellation: the internal stride-two
blocks occur in reverse order but with the same underlying intersections.
Summing over residual paths gives one-sign mass at most

\[
b_q=\sum_i\min(L_i,2q)\le2qR.
\]

The difference of the two one-sign decks has \(\ell^1\)-norm at most
\(2b_q\), proving

\[
\|B_{m-q}(F'-F)\|_1\le4qR.
\]

Complementing an upper depth-\(q\) flag gives rank

\[
n-(m+q)=m-(q-1),
\]

so applying the lower estimate at depth \(q-1\) gives

\[
\|B_{m+q}(F'-F)\|_1\le4(q-1)R.
\]

The value at \(q=1\) is correctly zero, because both spanning exact
factors have the same middle incidence vector.

## 4. Why \(R=e\), and the owner inequality

On an affected old cycle containing \(d\ge1\) old-only edges, deleting
those edges leaves exactly \(d\) path components.  This remains true when
some deleted edges are adjacent: the intervening vertex is simply an
isolated residual path.  If all edges of the old cycle are deleted, all
vertices are isolated and their number again equals \(d\).  Completely
common cycles cancel.  Summing over affected cycles proves

\[
R=e=|E(F)\setminus E(F')|.
\]

Every endpoint of an old-only edge is a changed owner.  Conversely every
changed owner is incident with at least one old-only edge.  Hence the
old-only graph on the \(s\) changed owners has minimum degree at least one
and maximum degree at most two, and therefore

\[
\frac{s}{2}\le e\le s.
\]

The report uses only the correct half \(e\le s\).  Substitution into the
boundary estimate proves (5.8)--(5.9).

## 5. Averaging constants

If the support of an integral increment is at least \(\delta W\), its
\(\ell^1\)-norm is at least \(\delta W\).  For a lower or upper depth
\(q\le H\), the preceding bounds therefore imply

\[
e\ge\frac{\delta W}{4H}.
\]

If \(C\) affected old exact-wreath components carry the cuts, then
\(C\le B=W/n\), so

\[
\frac eC\ge
\frac{\delta W}{4HB}
=\frac{\delta n}{4H}.
\]

For fixed \(A>0\) and \(H=A\sqrt m\) (or \(H=\lceil A\sqrt m\rceil\)),

\[
\frac{\delta n}{4H}
=\left(\frac{\delta}{2A}+o(1)\right)\sqrt m.
\]

At lower depth \(2\), the direct constant is \(4q=8\), giving

\[
e/C\ge\delta n/8.
\]

Thus (5.10)--(5.13), as well as the summary constants (0.2)--(0.3), are
correct.  Finally,

\[
\frac{B}{W/H}=\frac Hn=o(1),
\qquad
HB=W\frac Hn=o(W)
\]

whenever \(H=o(n)\), verifying (5.14).

## 6. The gcd and ternary exception

For a distinguished three-vertex path with core \(K\), the incidence
count is \(\mathbf1+\mathbf1_K\).  Therefore its centered charge is

\[
n(\mathbf1+\mathbf1_K)-3m\mathbf1
=n\mathbf1_K-(m-1)\mathbf1,
\]

as used in (8.1).  If the remaining residual pieces have zero centered
charge, point-regularity gives

\[
n\sum_{i=1}^t\mathbf1_{K_i}=(m-1)t\mathbf1.
\]

Coordinatewise, \(n\mid(m-1)t\).  Euclid's algorithm gives

\[
g=\gcd(2m+1,m-1)=\gcd(3,m-1)\in\{1,3\},
\]

and hence \(n/g\mid t\).  Vertex-disjointness gives \(3t\le n\).
If \(g=1\), the only multiple of \(n\) in this interval is zero.  If
\(g=3\), a positive \(t\) must equal \(n/3\), and equality in the vertex
bound makes the three-paths tile the component.  Substitution yields

\[
\sum_{i=1}^{n/3}\mathbf1_{K_i}
=\frac{m-1}{3}\mathbf1.
\]

The exceptional case is equivalently \(m\equiv1\pmod3\); then both
\(n/3\) and \((m-1)/3\) are integral.  Equations (8.2)--(8.5) and both
case conclusions are exact.  The theorem gives a necessary condition and
does not assert that the resulting one-design is PBBS-sewable; the report
correctly describes it only as the possible zero-background escape.

