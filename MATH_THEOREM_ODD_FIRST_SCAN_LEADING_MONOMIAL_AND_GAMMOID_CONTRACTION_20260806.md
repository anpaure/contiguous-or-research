# Odd current: first-scan leading monomial and exact gammoid contraction

**Date:** 2026-08-06  
**Method:** one boundary-containing coordinate scan, alternating-linkage
representation of a cotransversal matroid, and Pfaffian coefficient
extraction; no computation  
**Status:** unconditional one-layer factorization.  A full physical scan
installs a macroscopic part of the same-shore current with no algebraic
cancellation.  The coefficient of that scan monomial is exactly the
coloured surplus Pfaffian of a contracted strict gammoid whose sources are
the quiet compressed residue.  Proving that this contracted Pfaffian is
nonzero, or identifying it recursively with the next capacity-two layer,
remains open.

## 1. A scan which uses the boundary direction

Work first in a labelled odd sector

\[
 {\cal T}_{n,R},\qquad n=2m+1,\quad R\text{ odd},
\tag{1.1}
\]

and cut the coordinate cycle at one physical boundary \(e_\partial\).
Choose a matching of the coordinate cycle which:

1. contains \(e_\partial\);
2. contains \(m-1\) further disjoint coordinate edges; and
3. leaves one coordinate \(r\) unpaired.

On every ordered coordinate pair use

\[
 01-10,\qquad02-11,\qquad12-21,
\tag{1.2}
\]

with quiet states \(00,20,22\).  Scan the coordinate pairs in any fixed
order and act at the first nonquiet pair.

Let \(M_{\rm scan}\) be the resulting state matching.  Split it as

\[
                         M_{\rm scan}=P\mathbin{\dot\cup}N,
\tag{1.3}
\]

where \(P\) consists of the selected state edges across
\(e_\partial\), and \(N\) consists of all selected nonwrap state edges.
Let \(Q\) be the unmatched quiet residue.

### Lemma 1.1 (partial current basis)

Relative to the bipartite cut-open graph \(B=(L,R;E_B)\), every endpoint
of \(P\) lies in the majority shore \(L\), \(N\) matches every vertex
outside

\[
                         U_0=V(P)\mathbin{\dot\cup}Q,
\tag{1.4}
\]

and \(U_0\) is a basis of the surplus cotransversal matroid \(S\).
Consequently

\[
                         2|P|+|Q|=\operatorname{rank}S.
\tag{1.5}
\]

The residue is canonically

\[
 Q\cong{\cal T}_{m,(R-1)/2}.
\tag{1.6}
\]

#### Proof

The scan is a fixed-point-free involution away from the states for which
every coordinate pair is quiet.  Each nonwrap selected edge reverses the
cut-open parity, whereas the selected boundary edges preserve it.  All
quiet pairs have even local mass and even parity contribution; odd total
mass therefore forces the unpaired digit to equal one.  Hence every
unmatched state lies in the majority shore, and replacing every quiet
pair by its code \(0,1,2\) gives (1.6).

Remove the boundary edges \(P\) from the scan matching.  The remaining
matching \(N\subseteq B\) covers every vertex except their endpoints and
the quiet residue \(Q\).  Thus \(B-U_0\) has a perfect matching.  The
surplus-basis theorem makes \(U_0\) a basis of \(S\), and its cardinality
gives (1.5). \(\square\)

At central mass \(R=n\), the residual mass in (1.6) is \(m\).  One scan
therefore performs the exact dyadic quiet compression.

## 2. The strict-gammoid representation based at the scan

Orient the cut-open graph relative to \(N\):

* every edge of \(E_B-N\) is directed from \(L\) to \(R\);
* every edge of \(N\) is directed from \(R\) to \(L\).

Call the resulting digraph \(D_N\).  Every vertex of \(U_0\) has indegree
zero, because it is unmatched by \(N\).

### Theorem 2.1 (surplus bases are scan linkages)

A set \(X\subseteq L\) of size \(|U_0|\) is a basis of \(S\) if and only
if \(D_N\) contains \(|U_0|\) pairwise vertex-disjoint directed paths
linking \(U_0\) onto \(X\).

#### Proof

Suppose \(B-X\) has a perfect matching \(N_X\).  The symmetric difference
\(N\triangle N_X\) is a disjoint union of alternating cycles and
alternating paths.  Every nontrivial path starts at a vertex unmatched by
\(N\), hence in \(U_0\), and ends at a vertex unmatched by \(N_X\), hence
in \(X\).  Orienting relative to \(N\) makes these paths directed.
Common vertices of \(U_0\cap X\) use trivial paths.  Since both sets have
the same size, this is a linkage onto \(X\).

Conversely, flip \(N\) along a vertex-disjoint linkage from \(U_0\) onto
\(X\).  Directedness makes every nontrivial path alternating, beginning
with a nonmatching edge and ending with a matching edge in the reverse
description.  The flip matches every former source and leaves exactly
\(X\) unmatched.  Hence \(B-X\) has a perfect matching and \(X\) is a
surplus basis. \(\square\)

Thus \(S\) is the strict gammoid represented by \((D_N,U_0,L)\).

## 3. Contracting the installed scan current

The set \(V(P)\) is a subset of the source basis \(U_0\).  Put

\[
                         D'=D_N-V(P).
\tag{3.1}
\]

### Corollary 3.1 (exact source contraction)

The contracted matroid

\[
                         S'=S/V(P)
\tag{3.2}
\]

is the strict gammoid represented by

\[
                         (D',Q,L\setminus V(P)).
\tag{3.3}
\]

It has rank \(|Q|\).

#### Proof

A basis \(X\) of \(S'\) is characterized by
\(V(P)\cup X\) being a basis of \(S\).  Apply Theorem 2.1.  A source
vertex in \(V(P)\) has indegree zero in \(D_N\).  In any linkage whose
target set contains that same vertex, its only possible incoming path is
the trivial path from itself.  Delete all those forced trivial paths.
What remains is precisely a linkage from \(Q\) onto \(X\) in \(D'\).
The converse adjoins the deleted trivial paths. \(\square\)

This contraction is the proof-safe recursive state.  Merely recognizing
the source set \(Q\) as a smaller capacity-two layer does not yet identify
the whole digraph \(D'\), its allowed boundary occurrences, or its hub
colours with the next smaller physical sector.

## 4. Exact leading-monomial factorization

Use the coloured surplus-current Pfaffian construction.  Normalize a
matrix representation \(A\) of \(S\) so that the basis columns \(U_0\)
form the identity matrix.  Order those rows and columns with \(V(P)\)
first and \(Q\) second.

For every selected pointed boundary occurrence \(o_e\) over \(e\in P\),
let \(x_{o_e}\) be its occurrence variable and
\(\epsilon_{c(o_e)}\) its square-zero hub-colour variable.  Put

\[
 \mu_P=
 \left(\prod_{e\in P}x_{o_e}\right)
 \left(\prod_{e\in P}\epsilon_{c(o_e)}\right).
\tag{4.1}
\]

Let \(\Psi_S\) be the even-rank coloured surplus Pfaffian (or its
one-dummy socket extension when the rank is odd).  Delete \(V(P)\) and
the used occurrences, contract the corresponding source columns, and
delete every occurrence whose hub colour already occurs in (4.1).  Let
\(\Psi_{S'}^{\rm res}\) be the resulting contracted Pfaffian.

### Theorem 4.1 (scan coefficient identity)

If the selected scan occurrences in \(P\) have distinct hub colours, then

\[
 \boxed{
 [\,\prod_{e\in P}x_{o_e}\,]\,\Psi_S
 =
 \pm
 \left(\prod_{e\in P}\epsilon_{c(o_e)}\right)
 \Psi_{S'}^{\rm res}.}
\tag{4.2}
\]

If a hub colour repeats inside \(P\), the left side is zero.

#### Proof

Expand \(\Psi_S\) by surplus bases and physical boundary matchings.  A
term containing every specified variable \(x_{o_e}\) must contain both
endpoints of every edge of \(P\), and those endpoints are already paired
with one another.  Removing these forced pairs leaves:

1. a basis of the contraction \(S/V(P)\);
2. a physical boundary matching on that contracted basis; and
3. no occurrence using an already consumed endpoint or hub colour.

Conversely every contracted witness adjoins uniquely to the forced pairs
in \(P\).  In the normalized representation, the determinant minor on
the forced source columns is one, so Pfaffian expansion contributes only
the global ordering sign in (4.2).

The independent occurrence variables prevent mixing with any other edge
choice.  The product of colour variables is zero exactly when one selected
hub colour repeats. \(\square\)

Therefore the first scan layer never suffers a hidden algebraic
cancellation: after fixing its occurrence monomial, the remaining
coefficient is exactly one smaller contracted coloured-current problem.

## 5. The exact recursive theorem still missing

Equations (1.6), (3.3), and (4.2) isolate the desired continuation.

> **Quiet-compression Pfaffian-minor theorem.**  After the first-scan
> contraction, the strict gammoid \((D',Q)\), the residual physical
> boundary occurrence matrix, and the residual hub-colour partition have
> a coloured Pfaffian minor isomorphic to the next central
> capacity-two sector, up to a finite protected socket bank.

If this theorem holds, iterate (4.2).  The dimensions follow the dyadic
chain

\[
 n\longmapsto\lfloor n/2\rfloor
\longmapsto\lfloor n/4\rfloor\longmapsto\cdots
\tag{5.1}
\]

and end at the unique one-coordinate socket.  A hub-rainbow choice of the
scan occurrence banks at every level would then give a unique nonzero
leading monomial for the full coloured Pfaffian.

The existing circulation-blossom theorem supplies every individual
smaller-layer adjacency and proves fixed-level interior injectivity.
What it does not supply is precisely the simultaneous statement above:
distinct hub colours for the macroscopic scan bank and a cross-level
minor identification after earlier sources and colours are contracted.

## 6. Smallest exact obstruction

The companion extreme-wrap theorem proves that the obvious zero-length
continuation fails.  On the quiet source basis \(Q\), and indeed on the
union of all canonical quiet-root bases, the literal physical boundary
graph is empty at nonextreme compressed mass.  Thus
\(\Psi_{S'}^{\rm res}\) cannot be certified by pairing the remaining
sources directly.

Every nonzero continuation must use nontrivial directed paths in the
gammoid \(D'\) before reaching its physical boundary endpoints.  The
smallest exact unresolved object is consequently:

\[
\boxed{
\text{pair the quiet sources through vertex-disjoint alternating
linkages to a hub-rainbow boundary-edge bank}.}
\tag{6.1}
\]

This is smaller than the original Tutte family and more precise than
“pack the blossoms”: it is a source-paired strict-gammoid matching with a
partition constraint on the terminal edge occurrences.

## 7. Scope

Proved:

1. one boundary-containing physical scan installs a partial current whose
   endpoints plus the quiet residue form a surplus basis;
2. an exact strict-gammoid representation of every surplus basis relative
   to that scan;
3. exact contraction from the installed current to the quiet source set;
4. a leading-monomial identity with no first-layer cancellation; and
5. reduction of the residual problem to the source-paired linkage (6.1).

Not proved:

1. nonvanishing of the contracted Pfaffian;
2. recursive identification of the contracted gammoid with the smaller
   physical sector;
3. a macroscopic hub-rainbow scan occurrence choice across backgrounds;
4. cross-level protected-minor compatibility; or
5. the all-\(k\) upper bound.
