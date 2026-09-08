# Remote PBBS blocks: exact interval anti-cover and palette-safe history fusion

**Date:** 2026-08-06  
**Method:** maximal-envelope pinning, coordinatewise interval duality, and
two-edge switching; no computation or search  
**Status:** unconditional exact selector reformulation, laminar
specialization, protected-anchor sufficient theorem, and exact
palette-safe fusion criterion.  The canonical PBBS trace is not proved to
satisfy the resulting global anti-cover selector.

The local deep-owner theorem proves that a depth-`q>d` target must be moved
away from its chosen owner-intersection occurrence.  This note gives the
exact global condition on such remote moves and separates it from the
component-fusion condition.

## 1. Resident trace and candidate blocks

Let `T=(T_i)` be a cyclic simple rank-`r` Johnson trace with positive
residence at least `d+1`.  Put

\[
 P_p=\bigcap_{h=0}^{d}T_{p-h},
 \qquad F_p=\{D_p,I_{p-d-1}\}.
\tag{1.1}
\]

For a cyclic interval `J` of length at most `d`, define

\[
 K(J)=\bigcup_{p\in J}F_p,
 \qquad M(J)=\bigcup_{p\in J}P_p.
\tag{1.2}
\]

The one-block target theorem says that a target `S` is individually
plantable on `J`, with maximal letters off `J`, exactly when

\[
                         K(J)\subseteq S\subseteq M(J).
\tag{1.3}
\]

Consider a finite atlas

\[
                 \mathcal A=\{(S_a,J_a):a\in A\}
\tag{1.4}
\]

of distinct occurrence addresses satisfying (1.3).  Intervals may overlap.
Its pinned maximal letter at position `p` is

\[
 E_p=P_p\cap\bigcap_{a:p\in J_a}S_a,
\tag{1.5}
\]

where the empty target intersection is the whole ground set.

For a coordinate `x`, put

\[
 Q_x=\{p:x\in P_p\},
 \qquad
 B_x=\bigcup_{a:x\notin S_a}J_a.
\tag{1.6}
\]

The set `Q_x` is the union of the eroded positive runs of `x`; `B_x` is
the union of selected blocks whose prescribed value forbids `x`.

## 2. Exact interval anti-cover theorem

### Theorem 2.1

Every forced set remains pinned:

\[
                         F_p\subseteq E_p.
\tag{2.1}
\]

Moreover, coordinatewise,

\[
                         x\in E_p
 \quad\Longleftrightarrow\quad
                         p\in Q_x\setminus B_x.
\tag{2.2}
\]

Consequently the atlas is realized by one antecedent of `T` if and only if
the following two interval anti-cover conditions hold:

\[
 J_a\cap(Q_x\setminus B_x)\ne\varnothing
 \quad(a\in A, x\in S_a),
\tag{TC}
\]

and

\[
 [i,i+d]\cap(Q_x\setminus B_x)\ne\varnothing
 \quad(i\in\mathbb Z_W, x\in T_i).
\tag{OC}
\]

When they hold, the literal choice `A_p=E_p` works simultaneously for all
selected targets and all owners.

#### Proof

If `p in J_a`, (1.3) gives `F_p subseteq K(J_a) subseteq S_a`.
Intersecting over all selected intervals through `p` proves (2.1).

By (1.5), `x in E_p` exactly when `x in P_p` and no selected target
whose interval contains `p` excludes `x`.  This is (2.2).

For a selected pair `(S_a,J_a)`, every `E_p`, `p in J_a`, is a subset of
`S_a`.  Therefore

\[
 \bigcup_{p\in J_a}E_p=S_a
\]

if and only if each `x in S_a` occurs in at least one `E_p` with
`p in J_a`.  By (2.2), this is `(TC)`.

Similarly, `E_p subseteq P_p` and the maximal-row identity gives

\[
 \bigcup_{p=i}^{i+d}E_p\subseteq
 \bigcup_{p=i}^{i+d}P_p=T_i.
\]

Equality holds exactly when every `x in T_i` survives at some position of
that owner window, which is `(OC)`.  Under `(TC)` and `(OC)`, the letters
`E_p` are nonempty by (2.1), have the required target unions, and have
depth-`d` derivative `T`.  \(\square\)

### Interpretation

The global obstruction is not a missing scalar capacity or ordinary Hall
neighbourhood.  For every required pair `(R,x)`, where `R` is either a
selected target interval or an owner window, the `x`-support

\[
                         R\cap Q_x
\]

must not be covered by the selected intervals whose labels omit `x`.
This is an exact one-dimensional interval-cover obstruction, simultaneously
for all coordinates.

## 3. Laminar specialization

Suppose the geometric interval family `{J_a}` is laminar.  For a fixed
coordinate `x`, let `\mathcal B_x^max` be the inclusion-maximal selected
intervals whose labels omit `x`.  They are pairwise disjoint and

\[
                         B_x=\bigcup_{J\in\mathcal B_x^{\max}}J.
\tag{3.1}
\]

Hence `(TC)` and `(OC)` reduce exactly to finding, in each required
`R cap Q_x`, a point outside a disjoint family of maximal blockers.  If in
addition labels are order-preserving,

\[
                         J_a\subseteq J_b
 \quad\Longrightarrow\quad S_a\subseteq S_b,
\tag{3.2}
\]

then no ancestor of a target containing `x` is an `x`-blocker; only proper
descendants can obstruct its target row.

This yields a monotone recursive test on the laminar tree: for every node
`(S,J)` and `x in S`, the set `J cap Q_x` must contain a point outside the
maximal descendant nodes whose labels omit `x`.  The same test is made for
each owner window against the maximal `x`-blocking nodes which meet it.

Laminarity therefore removes all higher intersection patterns, but does
not make success automatic: disjoint `x`-omitting children can still cover
the whole available `x`-support of their parent.

## 4. Protected-anchor selector

The anti-cover theorem has a useful conflict-form sufficient condition.
For every owner incidence `(i,x)`, choose a protected anchor

\[
                         o_{i,x}\in[i,i+d]\cap Q_x.
\tag{4.1}
\]

A **target package** for `S` consists of a candidate interval `J`
satisfying (1.3) and anchors

\[
                         a_{S,x}\in J\cap Q_x
                         \qquad(x\in S).
\tag{4.2}
\]

Delete a package if its interval contains some owner anchor `o_(i,x)` with
`x notin S`.  Two remaining packages `(S,J,a)` and `(R,K,b)` conflict if

\[
 \exists x\in S\setminus R: a_{S,x}\in K,
 \quad\hbox{or}\quad
 \exists y\in R\setminus S: b_{R,y}\in J,
\tag{4.3}
\]

or if they use the same occurrence address.

### Theorem 4.1 (protected-anchor selection)

Any choice of one package for every target with no conflicts gives one
literal antecedent realizing every chosen target and every owner.

#### Proof

For `x in S`, its anchor `a_(S,x)` lies in `J cap Q_x`.  Condition (4.3)
says that no other selected interval whose label omits `x` covers this
anchor.  Thus `(TC)` holds.  The pruning by (4.1) gives the same conclusion
for every owner anchor, hence `(OC)`.  Apply Theorem 2.1. \(\square\)

If, after the owner pruning, distinct target packages are automatically
pairwise compatible, the remaining selector is an ordinary bipartite
matching from targets to occurrence addresses and Hall's theorem is exact.
In the general case it is a conflict-free transversal.  For example, if
every target has a list of common size `L` and every package conflicts with
at most `Delta` packages in all other lists, the symmetric local lemma
selects one package per target whenever

\[
                         e(2L\Delta+1)<L^2.
\tag{4.4}
\]

Indeed a conflicting-pair event has probability `L^-2` and depends on at
most `2L Delta` other pair events.  This gives a precise list-versus-conflict
target for a remote PBBS atlas.

## 5. Why ordinary address Hall is insufficient

The bipartite graph defined only by (1.3) forgets `B_x`.  Several
individually legal intervals can together cover every available occurrence
of one coordinate inside a required target or owner window.  The pinned
letter then loses that coordinate.  Theorem 2.1 shows that this is the only
additional source-level obstruction, but it is a simultaneous interval
anti-cover constraint, not an ordinary matching constraint.

Equivalently, if every short cell is written as

\[
 U_{b,\ell}=\bigcup_{t=0}^{\ell-1}A_{b-t},
 \qquad 1\le\ell\le d,
\tag{5.1}
\]

then the whole table obeys the rigid sliding recurrence

\[
 U_{b,1}=A_b,
 \qquad
 U_{b,\ell}=U_{b-1,\ell-1}\cup U_{b,1}.
\tag{5.2}
\]

Any full remote assignment must embed into one such triangular OR table.
Separate Hall matchings at each depth do not impose (5.2).

## 6. Palette-safe common-history two-switch

The source-history fusion theorem splices two Euler circuits at one common
length-`d` history.  Let the incoming and outgoing owner labels at that
history be

\[
                         A\to B,qquad C\to D.
\tag{6.1}
\]

The splice deletes these arcs and installs

\[
                         A\to D,qquad C\to B.
\tag{6.2}
\]

### Theorem 6.1 (exact palette-safe seam)

The common-history splice joins the two directed components while
preserving the complete immediate lower and upper colour multisets if and
only if:

1. `A,D` and `C,B` are distinct Johnson-adjacent owner pairs;
2. neither crossed arc duplicates an unremoved factor arc; and
3. the two multiset identities

\[
 \{A\cap B,C\cap D\}_{multi}
   =\{A\cap D,C\cap B\}_{multi},
\tag{6.3}
\]

\[
 \{A\cup B,C\cup D\}_{multi}
   =\{A\cup D,C\cup B\}_{multi}
\tag{6.4}
\]

hold.

Under these conditions the splice preserves occurrence-injectively every
source cell of width at most `d+1`, preserves both `q1` palettes exactly,
and reduces the number of owner components by one.

#### Proof

The common-history Euler splice preserves all labelled de Bruijn edges and
their internal source cells.  At owner level, only the two adjacencies in
(6.1) change.  Conditions 1--2 say that (6.2) is a legal simple Johnson
two-switch.  Removing one arc from each of two directed cycles leaves two
directed paths; the crossed arcs concatenate them into one directed cycle.

The lower colour of an owner arc `X--Y` is `X cap Y`, and its upper colour
is `X cup Y`.  Therefore (6.3)--(6.4) are respectively necessary and
sufficient for exact preservation of the two affected colour multisets.
All other colours are unchanged. \(\square\)

### Corollary 6.2 (common-history tree fusion)

Let a tree of source components have separated common-history splice sites.
If every tree edge satisfies Theorem 6.1 at the moment it is used, then
successive two-switches produce one source Euler circuit and one simple
Johnson owner component, with the whole short deck and both immediate
palettes preserved exactly.

If exact palette multiplicity is unnecessary, (6.3)--(6.4) may be weakened:
each deleted lower/upper colour need only have a named witness outside the
two removed arcs.  Johnson legality and nonduplication of the crossed arcs
remain necessary for a simple factor.

## 7. Exact remaining PBBS statement

The terminal one-copy route is now reduced to two independent selections:

1. choose remote packages for every deep target so that `(TC)` and `(OC)`
   hold (equivalently, choose a conflict-free protected-anchor transversal);
2. choose a spanning tree of common-history sites satisfying the exact
   palette-safe seam predicate (6.3)--(6.4), or furnish named backups for
   its deleted colours.

The canonical gap-section theorem supplies neither selection.  Its deep
occurrences lie in the forbidden local collars, and it contains no bound on
the package conflict degree `Delta`.  Thus the strongest proof-safe open
lemma is a global remote-package spread theorem together with a
palette-safe common-history spanning tree.  No further terminal common-cap
matching is required once these two objects exist.
