# Overlap-state Hall is a capacitated core flow; the common rounding is a root-coloured circulation

**Date:** 2026-08-01  
**Status:** unconditional exact reduction and an unconditional common
fractional point.  For a fixed flag table, every overlap-state perfect
matching is equivalent to a totally unimodular capacitated flow with one
explicit singleton exception.  Varying the flags while imposing one choice
per root produces a root-coloured circulation, and that extra partition row
is not generically integral.  Within one assigned core, Boolean owner
collisions are now classified exactly: they are directed two-cycles, and
the only owner-simple local obstruction beyond the Hall singleton is a
closed degree-two core.  Cross-core owner collisions remain open.  No
Boolean all-host one-copy obstruction is claimed.

## 0. Result and scope

Put

\[
        k=2m+1,\qquad 2\le d\le m,\qquad b=m-d+1.
\]

A complete depth-\(d\) flag is

\[
 f=(q;z_1,\ldots,z_{d-1}),\qquad
 B(f)=q-\{z_1,\ldots,z_{d-1}\},\quad |B(f)|=b.       \tag{0.1}
\]

The main conclusions are as follows.

1. For a fixed one-flag-per-root table, the statewise Hall system of
   `MATH_THEOREM_SCD_FLAG_RAIL_BALANCE_STATEWISE_HALL_AND_OWNER_GATE_20260801.md`
   is exactly a head-to-bottom-core capacitated bipartite flow.  After the
   core quotas are met, the only possible residual obstruction is a core
   used once whose unique tail-deletion label equals its unique incoming
   addition label.
2. Equivalently, choose for every flag one incoming bottom letter.  Such a
   choice is an arc in a directed graph on ordered-rail/core states.  The
   fixed table has all statewise perfect matchings exactly when these arcs
   form an Eulerian circulation and every degree-one state avoids the
   diagonal label collision.
3. The complete Boolean flag host has an exact uniform fractional point
   satisfying simultaneously: one unit at every root, nodewise
   circulation, one unit at every named high suffix after fractional
   marking, and one unit at every owner.  Thus there is no remaining
   fractional separator at the overlap-state or owner-marginal row.
4. Once the flags themselves vary, the constraints become a
   **root-coloured Eulerian transversal** plus the exact suffix-mark rows.
   The root-colour partition destroys generic total unimodularity.  A
   two-node determinant-two example is given below.  It is an abstract
   matrix obstruction, not an embedding in the Boolean flag host.
5. After the uncoloured statewise matching is chosen, the local
   owner-rainbow problem has the exact no-one/no-two-cycle solution of
   Theorem 7.2.  The remaining owner row is cross-core collision avoidance.
   None of the results below proves that global row, connectivity, voltage,
   residence, or an upper deck.

## 1. The exact geometry inside one overlap state

Let \(w=(w_1,\ldots,w_{d-2})\) be an ordered word of distinct coordinates.
Use the empty word when \(d=2\).  A tail flag in the state \(w\) has the
unique form

\[
 f=(w\mathbin{\dot\cup}A\mathbin{\dot\cup}\{z\};
                         z,w_1,\ldots,w_{d-2}),               \tag{1.1}
\]

where \(|A|=b\).  Call \(A=B(f)\) its **tail core** and \(z\) its exposed
tail label.

A head flag in the same state has the form

\[
 g=(w\mathbin{\dot\cup}H;
                         w_1,\ldots,w_{d-2},\gamma),           \tag{1.2}
\]

where \(|H|=b+1\) and \(\gamma\in H\).

### Lemma 1.1 (core form of a literal turn)

The literal turn \(f\to g\) is legal if and only if there is a unique
\(\beta\) such that

\[
            H=A\mathbin{\dot\cup}\{\beta\},\qquad
            \gamma\in A,\qquad z\ne\beta.                    \tag{1.3}
\]

Its owner is

\[
                   o=w\cup A\cup\{z,\beta\}.                 \tag{1.4}
\]

#### Proof

The literal shift law removes the oldest letter \(z\) from the tail root,
adds a new letter \(\beta\), shifts the word \(w\), and requires the new
last deletion \(\gamma\) to lie in the old bottom block \(A\).  Removing
the common word \(w\) gives \(H=A+\beta\).  The new letter is not already
in the tail root, so \(z\ne\beta\).  Conversely these three conditions are
exactly the literal shift law.  The union of the two roots is (1.4).
\(\square\)

## 2. Exact capacitated-flow compression

Fix a table \({\cal F}\), one flag at every rank-\(m\) root.  In state
\(w\), let \(L_w\) and \(R_w\) be respectively its tail and head flags.
For every \(b\)-set \(A\) disjoint from \(w\), put

\[
 t_w(A)=|\{f\in L_w:B(f)=A\}|.                               \tag{2.1}
\]

If \(t_w(A)=1\), denote the exposed label of its unique tail by \(z_A\).
For a head \(g\), put \(H_g=q(g)-w\) and let \(\gamma_g\) be its last
deletion.

Build a bipartite network from the heads \(g\in R_w\) to the core vertices
\(A\).  Join \(g\) to \(A\) when

\[
 A=H_g-\{\beta\}\quad\hbox{for some }\beta\in H_g-\{\gamma_g\}, \tag{2.2}
\]

except that, when \(t_w(A)=1\), delete the edge if \(\beta=z_A\).  Give
every head supply one and give core \(A\) demand \(t_w(A)\).

### Lemma 2.1 (the local derangement)

Let \(Z,P\) be two sets of the same size \(r\).  The bipartite graph
between them containing exactly the pairs \(z\ne\beta\) has a perfect
matching if and only if either \(r=0\), or \(r=1\) and the two labels are
different, or \(r\ge2\).

#### Proof

Only the one-by-one diagonal is impossible.  If \(r\ge2\), the
neighbourhood of a singleton has size at least \(r-1\ge1\), while the
neighbourhood of every set of at least two distinct left labels is all of
\(P\).  Hall's theorem applies. \(\square\)

The selected labels really are sets rather than multisets.  For fixed
\((w,A,z)\), the root and the complete tail flag are determined.  Likewise,
for fixed \((w,A,\beta)\), the head root \(w\cup A\cup\{\beta\}\) is
determined; a one-flag-per-root table cannot select two such heads.

### Theorem 2.2 (overlap-core flow theorem)

The overlap graph \(G_w\) has a perfect matching if and only if

\[
             |R_w|=\sum_A t_w(A)=|L_w|                       \tag{2.3}
\]

and the head-to-core network above has a flow saturating every head and
meeting every core demand.

Equivalently, for every \({\cal X}\subseteq R_w\),

\[
 |{\cal X}|\le
 \sum_{A\in N^*_w({\cal X})}t_w(A),                          \tag{2.4}
\]

where \(N^*_w\) uses (2.2) with precisely the singleton-diagonal deletions.

#### Proof

Given a perfect matching in \(G_w\), a matched pair \(f\to g\) determines
the unique \(\beta=H_g-B(f)\).  Assign \(g\) to the core \(B(f)\).  This
meets every quota, and (1.3) excludes every deleted singleton edge.

Conversely, suppose the capacitated assignment exists.  For each core
\(A\), collect its \(t_w(A)\) tails and the same number of assigned heads.
Write \(Z_A\) for their exposed tail labels and \(P_A\) for the assigned
addition labels \(\beta\).  Both are sets.  Lemma 2.1 and the explicit
singleton deletion give a bijection with \(z\ne\beta\).  Lemma 1.1 turns
these bijections into legal turns.  Their union is a perfect matching in
\(G_w\).

The cut form (2.4) is the ordinary capacitated Hall theorem. \(\square\)

### Corollary 2.3 (fixed-table integrality)

For a fixed flag table, fractional feasibility of every overlap-core flow
implies integral statewise perfect matchings.  There is no fractional versus
integral gap in this row: its matrix is a bipartite network matrix.

This is stronger than invoking normalized matching in the complete Boolean
incidence graph.  It also explains the limitation of that invocation: an
SCD selects a sparse, correlated set of heads and tail quotas, and only the
cut (2.4), not regularity of the complete host, controls that restriction.

### Corollary 2.4 (bottom-singleton/full-depth form)

When \(d=m\), one has \(b=1\).  Write a tail as
\((z,w,a)\), where \(a\) is its bottom singleton, and a head as
\((w,a,\beta)\).  Then every head has only the core \(\{a\}\) available.
Consequently \(G_w\) has a perfect matching if and only if, for every
coordinate \(a\),

\[
 \#\{\hbox{tails ending }(w,a)\}
 =\#\{\hbox{heads beginning }(w,a)\},                         \tag{2.5}
\]

and a class of size one does not use the same exterior label on its two
sides.  Thus full-depth statewise Hall is refined de Bruijn balance on the
state \((w,a)\), plus one explicit no-loop condition.

## 3. A single root-coloured circulation

For a complete flag \(f\), write

\[
 p(f)=(z_1,\ldots,z_{d-2}),\quad
 s(f)=(z_2,\ldots,z_{d-1}),\quad
 \gamma(f)=z_{d-1}.                                         \tag{3.1}
\]

For each \(\beta\in B(f)\), define two rail/core nodes

\[
 I(f,\beta)=
 \left(p(f),(B(f)-\{\beta\})\cup\{\gamma(f)\}\right),
 \qquad
 O(f)=\left(s(f),B(f)\right).                               \tag{3.2}
\]

Make a directed arc

\[
                         (f,\beta):I(f,\beta)\longrightarrow O(f), \tag{3.3}
\]

and colour it by the root \(q(f)\).

### Theorem 3.1 (root-coloured circulation equivalence)

A one-flag-per-root table has a perfect matching in every overlap-state
graph if and only if one can choose one arc (3.3) of every root colour such
that

\[
                   \deg^-(v)=\deg^+(v)\quad\hbox{for every }v, \tag{3.4}
\]

and, whenever this common degree is one, the exposed label \(z_1\) of the
unique incoming flag is different from the \(\beta\)-label of the unique
outgoing arc.

#### Proof

An arc entering \((w,A)\) is a selected flag appearing as a tail with
suffix \(w\) and bottom core \(A\).  An arc leaving \((w,A)\) is a selected
head assigned to predecessor core \(A\).  Thus (3.4) is exactly the quota
equation of Theorem 2.2 simultaneously at all states.  At degree one the
last matching is legal exactly when \(z_1\ne\beta\); at degree at least two
Lemma 2.1 supplies the derangement.

Conversely, a family of statewise perfect matchings assigns to every head
the parent core of its matched tail, and hence its unique \(\beta\).  The
resulting arcs satisfy (3.4) and the degree-one condition. \(\square\)

Consequently the exact common selector/overlap problem can be written as:

* choose one arc of every root colour;
* impose the Euler equations (3.4);
* choose the optional suffix marks so every named target is marked once;
* avoid the degree-one diagonal states.

The first two bullets alone are a root-coloured circulation, not an
ordinary circulation.

## 4. The exact common fractional point

The directed graph (3.3) is regular before the root colours are imposed.
At a node \((w,A)\), an incoming arc is obtained by choosing

* \(z_1\notin w\cup A\), in \(m+2\) ways; and
* \(\beta\in A\), in \(b\) ways.

An outgoing arc is obtained by choosing

* \(\gamma\in A\), in \(b\) ways; and
* \(\beta\notin w\cup A\), in \(m+2\) ways.

Hence both directed degrees equal

\[
                              b(m+2).                          \tag{4.1}
\]

### Theorem 4.1 (uniform fractional suffix circulation)

Give every arc \((f,\beta)\) weight

\[
                  x_{f,\beta}={1\over b(m)_{d-1}}.            \tag{4.2}
\]

Then every root colour has total weight one and every node satisfies exact
flow conservation.  Moreover these node marginals have a fractional local
coupling supported on the legal pairs \(z\ne\beta\).  At depth \(j\),
\(1\le j<d\), every named
rank-\((m-j)\) target has selected suffix load

\[
 \rho_j={\binom{m+j+1}{j}\over\binom mj}.                    \tag{4.3}
\]

Marking each such occurrence with the additional factor \(1/\rho_j\)
gives exact target load one at every high rank, simultaneously with the
root and circulation equations.  Under the displayed literal-turn
coupling, every rank-\((m+1)\) owner also has fractional load one.

#### Proof

There are \((m)_{d-1}\) flags at a root and \(b\) choices of \(\beta\) for
each, proving the root equation.  Equation (4.1) proves circulation.
At a fixed node, every exposed tail label \(z\) has total mass
\(b/[b(m)_{d-1}]=1/(m)_{d-1}\).  For every external addition label
\(\beta\), there are \(b\) possible last deletions \(\gamma\), each arc
having mass (4.2).  Send the mass of tail \(z\) equally to all
\(b(m+1)\) pairs \((\beta,\gamma)\) with \(\beta\ne z\).  Each such
head-assignment arc receives its required mass because it has exactly
\(m+1\) eligible tail labels.  This is a fractional matching on literal
turns, not merely equality of node totals.

The construction is invariant under every coordinate permutation.  Its
total turn mass is \(W=\binom{2m+1}{m}\), equal to the number of
rank-\((m+1)\) owners.  Transitivity therefore gives owner load one.

Fix a target \(T\) of rank \(m-j\).  Choose its root extension in
\(\binom{m+j+1}{j}\) ways, order the first \(j\) deletions in \(j!\) ways,
and choose the remaining deletion word in \((m-j)_{d-1-j}\) ways.  Dividing
by \((m)_{d-1}\) gives (4.3).  The value is independent of \(T\), and
\(\rho_j\ge1\), so the displayed thinning is legal. \(\square\)

This is a common fractional point of the exact high-target selector and the
overlap-state circulation.  It is compatible with the corrected pull-clock
theorem at the level of fractional trace marginals; it does not round the
triangular boundary profile or fix prepared roots integrally.

## 5. Why generic flow, matroid intersection, and SCD do not finish

If the flag at every root is fixed, Theorem 2.2 is a TU flow.  If the flags
vary, the equations also contain

\[
                \sum_{(f,\beta):q(f)=q}x_{f,\beta}=1          \tag{5.1}
\]

for every root colour \(q\).  A partition row of this kind does not preserve
circulation integrality.

### Proposition 5.1 (minimum abstract determinant-two face)

Take two directed nodes \(u,v\), one colour, and two allowed arcs
\(u\to v\) and \(v\to u\).  The colour equation and flow equation are

\[
 x_{uv}+x_{vu}=1,\qquad x_{uv}-x_{vu}=0.                     \tag{5.2}
\]

Their unique solution is \(x_{uv}=x_{vu}=1/2\), while there is no integral
solution.  The coefficient determinant has absolute value two.

This is the smallest fractional-but-integral obstruction to the **abstract
root-coloured circulation matrix**.  It is not asserted to be a face of the
complete Boolean flag catalogue.  The Boolean host has diagonal flags and
all-depth cubic trades which can destroy small abstract obstructions.  Thus
(5.2) rules out only a generic TU or ordinary matroid-intersection proof;
it does not refute the desired all-\(m\) integral selector.

Likewise, an SCD proves the named-target rows but supplies no reason for
(3.4).  The explicit recursive-SCD dead flag at \((k,m,d)=(7,3,3)\) is an
exact witness.  The all-depth cubic absorber preserves every target row,
but its two states need not have the same boundary vector in (3.4).
Therefore it becomes useful here only after one proves a
**circulation-transparent lift** of its auxiliary flags.

### Proposition 5.2 (one cubic trade is never core-circulation transparent)

Use the all-depth cubic trade on roots
\(R_i=Q-\{u_i\}+\{x_i\}\), reindexed so that its two flags at root \(R_i\)
are

\[
 f_i^+=(R_i;x_i,u_{i+1},W),\qquad
 f_i^-=(R_i;x_i,u_{i-1},W),                                  \tag{5.3}
\]

with indices modulo three.  Put

\[
 D=Q-\bigl(\{u_0,u_1,u_2\}\cup W\bigr).                     \tag{5.4}
\]

Then their outgoing core states are

\[
 O(f_i^+)=\bigl((u_{i+1},W),D\cup\{u_{i-1}\}\bigr),
 \qquad
 O(f_i^-)=\bigl((u_{i-1},W),D\cup\{u_{i+1}\}\bigr).         \tag{5.5}
\]

The two triples in (5.5) are disjoint.  Every incoming state
\(I(f_i^\pm,\beta)\) begins with the exterior letter \(x_i\), whereas every
outgoing state in (5.5) begins with an internal letter \(u_j\).  Therefore,
for every choice of incoming letters \(\beta\),

\[
 \sum_i\bigl({\bf e}_{O(f_i^+)}-{\bf e}_{I(f_i^+,\beta_i)}\bigr)
 \ne
 \sum_i\bigl({\bf e}_{O(f_i^-)}-{\bf e}_{I(f_i^-,\beta'_i)}\bigr). \tag{5.6}
\]

In particular one cubic trade cannot be inserted into an Eulerian
root-coloured circulation while leaving its exterior boundary unchanged.

#### Proof

Deleting the displayed words in (5.3) gives respectively
\(B(f_i^+)=D+u_{i-1}\) and \(B(f_i^-)=D+u_{i+1}\), which proves (5.5).
The first triple records one orientation of the three ordered pairs of
distinct \(u\)'s and the second records the reverse orientation, so they
are disjoint.

Restrict the boundary vector in (5.6) to nodes whose ordered rail begins
with one of the internal letters \(u_j\).  All incoming terms vanish on
this restriction because their first letters are the exterior \(x_i\).
The restriction is therefore the nonzero difference of the two disjoint
outgoing triples in (5.5). \(\square\)

If two cubes are jointly role-separated, meaning that neither cube's
exterior first letters are internal letters of either cube, then their
outgoing and incoming node classes are disjoint.  In that scoped face,
cancellation forces their decorated suffix/core triangles (5.5) to be the
same and oppositely oriented (up to cyclic reindexing).  Equality of
ordinary rail words is not enough: the bottom cores \(D+u_j\) must also
agree.  Even then, the exterior-prefix states and the chosen
\(\beta\)-modified cores in (3.2) must cancel separately.  Without joint
role separation, outgoing-to-incoming cross-cancellation is possible and
this conclusion does not follow.

### Proposition 5.3 (an exact depth-three paired-cube circulation packet)

At \(d=3\), suppose \(m\ge4\), so \(D=Q-\{u_0,u_1,u_2\}\) is nonempty.
For each \(i\), choose \(\delta_i\in D\) as the incoming letter in both
phases of the flag at \(R_i\).  Then

\[
 I(f_i^+,\delta_i)=I(f_i^-,\delta_i)
 =\left((x_i),(D-\{\delta_i\})\cup
                    \{u_{i-1},u_{i+1}\}\right).              \tag{5.7}
\]

Take a second cubic trade with the same \(Q\) and \(U\), but with an
exterior injection chosen so that its three roots are distinct from the
first three roots.  Toggle the first cube from \(+\) to \(-\) and the
second from \(-\) to \(+\).  The six-root packet:

* preserves the complete suffix-row multiset, cube by cube;
* has zero aggregate boundary in the refined circulation (3.4); and
* changes no root multiplicity.

#### Proof

Equation (5.7) follows by deleting \(\delta_i\) from
\(D+u_{i-1}\) and appending \(u_{i+1}\) in the plus phase, or deleting the
same \(\delta_i\) from \(D+u_{i+1}\) and appending \(u_{i-1}\) in the
minus phase.  Thus each cube has zero incoming-state change.  Its outgoing
change is the orientation reversal (5.5), which does not depend on the
exterior injection.  Oppositely toggling the second cube cancels it.
The all-depth cubic identity (here through the two proper suffix ranks)
proves the row-multiset statement. \(\square\)

Three cautions are exact.  The two cubes use the same auxiliary suffix-row
bank, so this is not a resource-disjoint absorber; optional marks must be
assigned consistently.  Although node degrees are preserved, labels at an
affected node can change, so the degree-one guard of Theorem 3.1 must still
be checked (degree at least two is sufficient).  Finally, the packet need
not preserve the owner colours (7.2).  Proposition 5.3 is therefore a
positive uncoloured circulation/target packet, not the full common
one-copy theorem.

### Proposition 5.4 (role-separated two-cube obstruction at depth at least four)

Let \(d\ge4\), and let the two standard cubic trades have internal-letter
sets \(U_1,U_2\) and exterior-first-letter sets \(X_1,X_2\).  Assume the
**role-separation condition**

\[
                  (X_1\cup X_2)\cap(U_1\cup U_2)=\varnothing. \tag{5.9}
\]

If the trades are supported on six distinct roots, they cannot be toggled
oppositely to give zero refined circulation boundary.  This remains true
for arbitrary choices of their incoming letters \(\beta\).

#### Proof

By (5.9), every outgoing node of either cube has first rail letter in
\(U_1\cup U_2\), while every incoming node has first rail letter in
\(X_1\cup X_2\).  These two node classes are disjoint.  Hence total
boundary cancellation forces cancellation of the outgoing parts
separately.  The two decorated triangles (5.5) must therefore coincide.
Their rail words recover the ordered tail \(W\) and the set \(U\);
intersecting their three bottom cores recovers \(D\).  Hence they recover
\(Q=D\cup U\cup W\).  Thus both cubes have the same \((Q,U,W)\), up to
cyclic reindexing.

Write \(W_0=(w_3,\ldots,w_{d-2})\).  If the exterior injection of one cube
assigns \(x_i\) to the root missing \(u_i\), the two incoming rail prefixes
at that root are

\[
            (x_i,u_{i+1},W_0),\qquad (x_i,u_{i-1},W_0).       \tag{5.8}
\]

Project the incoming boundary onto rail prefixes and forget the core.
For each exterior first letter \(x_i\), the signed ordered pair in (5.8)
uniquely recovers the omitted index \(i\).  Therefore equality of the two
projected incoming-boundary vectors forces the two exterior injections to
be identical.  Their three roots \(Q-u_i+x_i\) are then identical, contrary
to six-root support.  The choices of \(\beta\) affect only the forgotten
core and cannot change this conclusion. \(\square\)

Accordingly, in the role-separated standard-cubic face at the growing
depths relevant to the pull-clock problem, one needs either a packet of at
least three cubes or a nonstandard boundary actuator.  Without (5.9), an
outgoing node of one cube can coincide with an incoming node of the other;
the unrestricted two-cube cancellation problem remains open.  Proposition
5.4 is therefore an architecture-specific scoped obstruction, not a no-go
for the Boolean root-coloured circulation itself.

## 6. Protected ports and the exact robust cut

Suppose a fixed table already has a set of pairwise-disjoint forced legal
turns in state \(w\).  Delete their tail and head flags, reduce the
corresponding core quotas, and rebuild the singleton exclusions.  The
forced turns extend to a perfect matching if and only if the residual form
of (2.4) holds.  This is an exact finite criterion for prepared ports.

There is a useful stronger sufficient condition.  Suppose the forced bank
has \(r\) turns, where \(r\le h\).  Before forcing it, use the raw
head-to-core graph (2.2), without singleton deletions.  Assume

\[
 \sum_{A\in N_w({\cal X})}t_w(A)\ge |{\cal X}|+r             \tag{6.1}
\]

for every head family that can remain after the forced deletions, and
assume every residual positive core quota is at least two.  Removing the
\(r\) tail capacities leaves Hall, and the second assumption removes
the only diagonal obstruction.  Hence every such forced bank extends.

Condition (6.1) is the precise kind of robust expansion which a
normalized-matching/SCD/absorber argument would have to export.  Neither
the ordinary SCD theorem nor the uniform fractional point proves it.
In particular, fixing \(O(1)\) flags to a common robust order is not by
itself an \(O(1)\)-defect theorem: those flags still impose root-colour and
node-boundary constraints in (3.4).

## 7. The owner-rainbow row is genuinely later

After the head-to-core assignment, a node \(v=(w,A)\) has a set \(Z_v\) of
tail labels and an equal-size set \(P_v\) of incoming addition labels.  A
statewise matching chooses a bijection

\[
             \sigma_v:Z_v\longrightarrow P_v,qquad
             z\ne\sigma_v(z).                                \tag{7.1}
\]

The owner of that turn is

\[
              o(v,z)=w\cup A\cup\{z,\sigma_v(z)\}.            \tag{7.2}
\]

Thus owner exactness asks that the union of all local derangements (7.1)
use every owner (7.2) once.  This is a rainbow matching/three-index row.
Theorem 2.2 proves only that each local derangement exists.  It does not
couple their colours.

The functional-attachment balanced-turn theorem is a sufficient way to
close (7.2): preselect a bijective head-to-owner attachment whose
predecessor graph has Hall.  Nothing here constructs that attachment.

The Boolean union map nevertheless removes one generic rainbow
obstruction completely.  Put

\[
                         S_v=w\cup A .                         \tag{7.3}
\]

Thus every owner used at the node is \(S_v\cup\{z,\beta\}\), where
\(z\in Z_v\), \(\beta\in P_v\), and \(z\ne\beta\).

### Lemma 7.1 (owner-collision equals a directed two-cycle)

Let \(\sigma:Z_v\to P_v\) be a legal local bijection.  Two distinct
matched turns at labels \(z,z'\) have the same owner if and only if

\[
                         \sigma(z)=z',\qquad
                         \sigma(z')=z .                       \tag{7.4}
\]

Consequently the local owners are pairwise distinct if and only if the
directed matching \(z\mapsto\sigma(z)\) has no directed two-cycle.

#### Proof

All labels lie outside \(S_v\).  Equality of the two owners is therefore

\[
             \{z,\sigma(z)\}=\{z',\sigma(z')\}.               \tag{7.5}
\]

The tails and heads are each labelled injectively, so the two ordered
pairs are distinct.  The only remaining equality of unordered two-sets is
the reversal (7.4).  Its converse is immediate. \(\square\)

This also explains why the usual \(2\times2\times2\) parity gadget is not
a literal Boolean owner gadget.  If opposite legal cells of a local
\(2\times2\) rectangle had one common owner, their labels would be
reversed by (7.4), and the other two cells would be precisely the forbidden
equal-label cells \(z=\beta\).  Thus both perfect matchings of a legal
Boolean \(K_{2,2}\) cannot be monochromatic in two different owner colours.

### Theorem 7.2 (exact local owner-simple derangement)

Let \(Z,P\) be the exposed and addition label sets at one assigned core,
with

\[
                              |Z|=|P|=t.                       \tag{7.6}
\]

There is a legal bijection \(\sigma:Z\to P\) whose owner colours are
pairwise distinct if and only if

\[
        t=0\quad\hbox{or}\quad
        \neg\bigl(Z=P\ \hbox{ and }\ t\in\{1,2\}\bigr).       \tag{7.7}
\]

In particular:

* the closed singleton is exactly the statewise diagonal obstruction of
  Theorem 2.2;
* the closed doubleton has a unique legal matching, a transposition, and
  its two turns have the same owner;
* every closed core of degree at least three has an owner-simple matching,
  supplied by one cyclic permutation of all its labels.

#### Proof

If \(Z=P\) and \(t=1\), the sole edge is illegal.  If \(Z=P\) and \(t=2\),
the sole legal bijection is the transposition, which is a directed
two-cycle and hence repeats its owner by Lemma 7.1.

If \(Z=P\) and \(t\ge3\), order the labels cyclically and send each label to
its successor.  This has neither a fixed point nor a two-cycle.

It remains to treat \(Z\ne P\).  Put

\[
 C=Z\cap P,\qquad L=Z-P,\qquad R=P-Z .                        \tag{7.8}
\]

Then \(|L|=|R|=a\ge1\).  If \(C=\varnothing\), any bijection \(L\to R\)
works.  Otherwise write

\[
 C=\{c_1,\ldots,c_s\},\quad
 L=\{\ell_1,\ldots,\ell_a\},\quad
 R=\{r_1,\ldots,r_a\}
\]

and use the directed path

\[
 \ell_1\mapsto c_1\mapsto c_2\mapsto\cdots\mapsto c_s
                 \mapsto r_1                                  \tag{7.9}
\]

together with \(\ell_j\mapsto r_j\) for \(2\le j\le a\).  This is a
bijection \(Z\to P\).  It has no fixed point.  It also has no directed
two-cycle: the common labels form one directed path, every \(\ell_j\) is
absent from the target shore, and every \(r_j\) is absent from the source
shore.  Lemma 7.1 now proves owner injectivity. \(\square\)

### Corollary 7.3 (the first cubic owner lock)

After a feasible head-to-core flow has been fixed, all **within-core**
owner collisions can be removed independently except at closed degree-two
cores.  A degree-three closed core is the smallest positive cubic absorber:
the two cyclic orientations give three distinct owners and change no core
quota.

Thus the owner row left after Theorem 2.2 has exactly two parts:

1. avoid or absorb closed degree-two cores while choosing the core flow;
2. prevent collisions between owners selected at different cores.

The second part is genuinely global.  A simple sufficient separation
condition is available.  If the active bases \(S_v\) satisfy

\[
                   |S_u\cup S_v|>m+1\qquad(u\ne v),           \tag{7.10}
\]

then no rank-\((m+1)\) owner can occur at two different cores.  Under
(7.10), a feasible core flow with no closed degree-two core, followed by
the constructions in Theorem 7.2, is automatically owner-rainbow: it
produces \(W\) distinct rank-\((m+1)\) owners, hence all of them.  Condition
(7.10) is deliberately only a sufficient private-core face; no claim is
made that an SCD or the pull clock supplies so many separated cores.

## 8. Sharp remaining theorem

The common integral gate can now be stated without exponentially large
statewise graphs.

> **Boolean root-coloured circulation with marks.**  Select one arc
> \((f,\beta)\) of every middle root in the graph (3.3), retain the bounded
> prepared flags, satisfy every node equation (3.4), avoid every degree-one
> diagonal, and mark the selected nested suffixes so each named high target
> is used once.

A solution closes rail balance and every uncoloured statewise Hall row.
Theorem 7.2 closes each local owner palette except for the explicit closed
degree-two lock; one must still avoid those locks and all cross-core owner
collisions.  Connectivity, voltage, residence, upper shadows, and the
compiler follow only after that.

The complete host has the exact fractional solution of Theorem 4.1, while
Proposition 5.1 prevents a black-box integrality inference.  A positive
all-dimensional proof must therefore use a Boolean-specific correlated
rounding, for example circulation-transparent cubic absorbers or a
prospective serialized SCD.  Fractional feasibility alone does not imply an
\(O(1)\) one-copy defect.
