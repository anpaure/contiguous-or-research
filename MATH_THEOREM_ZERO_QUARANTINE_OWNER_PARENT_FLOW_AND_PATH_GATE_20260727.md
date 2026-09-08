# Zero-quarantine installation: owner-parent closure and the path gate

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, web
input, or probabilistic black box is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
 \qquad N=\binom{2m}{M},\qquad W=\binom{2m}{m},
\tag{0.1}
\]

and

\[
 a=\binom MH,\qquad b=\binom mH,\qquad
 \lambda=\frac ab=\frac WN,\qquad g=\lambda-d.
\tag{0.2}
\]

Assume the calibrated regime \(H=o(m)\), \(g>0\), and the hypotheses
of the repaired twelve-top packet. Start with the deterministic
\(15n\)-top source bank from
MATH_THEOREM_BROAD_POSITION_THREE_PACKET_SEEDING_AND_OWNER_QUARANTINE_20260727.md:
one three-top and one repaired twelve-top source packet for every
coordinate label.

Let \(T\) be a coefficient-one retained-path table. Every covered
middle owner has a unique current **parent top**, namely the top whose
row contains it. This parent map gives the exact zero-quarantine
condition.

The conclusions are:

1. For a fixed internally resource-disjoint bank \({\cal B}\), the
   minimum number of nonbank rows which must be quarantined is exactly

   \[
       q_T({\cal B})
       =\left|
          \{\operatorname{par}_T(X):X\in{\cal O}({\cal B}),
             \ \operatorname{par}_T(X)\notin{\cal U}({\cal B})\}
         \right|.
   \tag{0.3}
   \]

   In particular, zero quarantine is equivalent to the directed
   parent-closure condition

   \[
       \operatorname{par}_T({\cal O}({\cal B}))
                       \subseteq{\cal U}({\cal B})\cup\{\bot\},
   \tag{0.4}
   \]

   where \(\bot\) denotes a current owner hole.

2. If the bank copies are still to be chosen from their prescribed
   relabelling orbits, zero-quarantine selection is the integral system
   (3.2)--(3.5) below. Its fractional relaxation has an exact
   owner-potential dual. The packet-disjointness family is not a
   matroid, so ordinary matroid intersection or a TU claim is
   unavailable.

3. At the atomic containment level, zero quarantine is always
   possible for the polynomial bank. Reserve the bank's \(15nd\)
   owners. If

   \[
                 \binom MH\ge K\left(1+\frac d g\right),
       \qquad K=15nd,
   \tag{0.5}
   \]

   then every nonbank top can be assigned \(d\) distinct contained
   owners, no owner is repeated, and no top is omitted. Condition
   (0.5) holds throughout the growing-\(H\) calibrated regime.

4. This atomic flow does not produce retained paths. The bank can be
   chosen with cross-packet top intersections smaller than \(m\).
   For such a separated bank, every two-outside owner of a repaired
   twelve-top row is private to its own top among all bank tops.
   Therefore zero-quarantine installation into \(T\) forces, on every
   twelve-top row \(U=C+e\),

   \[
       {\cal O}^{(2)}_P(U)
                  \subseteq {\cal O}_T(U)\cup{\cal H}(T),
       \qquad |{\cal O}^{(2)}_P(U)|=d-H.
   \tag{0.6}
   \]

   Here \({\cal H}(T)\) is the current hole set. A single violation of
   (0.6) is a literal statewise obstruction. It is invisible in the
   atomic Hall flow.

5. More generally, repairing conflicts without deleting tops is an
   alternating **AND-hypergraph closure** problem: changing one row
   imports \(d\) owners and forces changes at all their current parent
   tops. The exact physical completion is a rainbow matching of
   retained Johnson paths in the residual owner set. This grouping
   problem, not scalar owner capacity, is the unresolved gate.

6. Once a zero-quarantine physical installation exists, every packet
   in the bank may be fired in any order. The complete global owner
   vector is unchanged after every firing. Thus chronology introduces
   no further owner condition.

This gives a positive zero-quarantine theorem for the integral atomic
flow and an exact statewise obstruction for the physical path lift. It
does not prove a positive-density retained-path installation.

## 1. The parent map of a coefficient-one table

Let

\[
                         {\cal C}(T)
      =\bigcup_{U\in{\cal U}(T)}{\cal O}_T(U)
\tag{1.1}
\]

be the covered middle-owner set of \(T\), and put

\[
                         {\cal H}(T)
      =\binom{[n]}m\setminus{\cal C}(T).
\tag{1.2}
\]

Coefficient one makes the map

\[
 \operatorname{par}_T:{\cal C}(T)\longrightarrow\binom{[n]}M
\tag{1.3}
\]

well-defined: \(\operatorname{par}_T(X)=U\) when
\(X\in{\cal O}_T(U)\). Extend it by
\(\operatorname{par}_T(X)=\bot\) on holes.

Let \({\cal B}\) be a fixed bank whose packet tops are distinct and
whose inserted owner decks are pairwise disjoint. Write

\[
                         S={\cal U}({\cal B}),\qquad
                         B={\cal O}({\cal B}).
\tag{1.4}
\]

### Theorem 1.1 (exact quarantine number)

If all old rows on \(S\) are replaced by the source rows of
\({\cal B}\), the minimum additional set of old rows which must be
deleted to restore coefficient one is

\[
                         Q_T({\cal B})
       =\operatorname{par}_T(B)\setminus(S\cup\{\bot\}).
\tag{1.5}
\]

In particular the minimum extra-row count is (0.3), and the
installation uses zero quarantine exactly when (0.4) holds.

#### Proof

Every old row on \(S\) is removed because a table has at most one row
on a top. If \(X\in B\) is currently covered by a row on
\(U\notin S\), that row collides with the inserted occurrence of
\(X\), so it must be deleted. Thus every top in (1.5) is necessary.

Conversely, delete the rows on \(S\cup Q_T({\cal B})\). Every inserted
owner which was formerly covered has now lost its unique parent row,
and holes had no parent. The bank is internally owner-disjoint, so no
collision remains. Hence (1.5) is also sufficient. \(\square\)

This refines the bound \(15n(1+d)\) from the quarantine theorem: that
bound counts owner witnesses, while (1.5) identifies the exact number
of distinct external parent rows.

## 2. Fixed candidates give a directed closure graph

Suppose first that a finite list of internally owner-disjoint candidate
packets has already been chosen with pairwise distinct tops. Make a
directed dependency graph as follows.

* There is one packet vertex for every candidate packet.
* If an owner inserted by packet \(P\) has current parent top in packet
  \(Q\), draw \(P\to Q\).
* If its parent top lies outside the candidate bank, draw
  \(P\to\dagger\).
* Hole owners draw no edge.

### Proposition 2.1 (closed-subbank criterion)

A subcollection \({\cal A}\) of these packets can be installed without
quarantining an external row if and only if:

1. no packet of \({\cal A}\) reaches \(\dagger\); and
2. \({\cal A}\) is out-closed: \(P\in{\cal A}\) and \(P\to Q\) imply
   \(Q\in{\cal A}\).

#### Proof

This is Theorem 1.1 with the selected bank tops partitioned by their
unique candidate packets. \(\square\)

Thus, for fixed candidates, the maximal zero-quarantine subbank is the
union of the sink strongly connected components which do not reach
\(\dagger\), together with all their predecessor components that also
avoid \(\dagger\). It is found by ordinary reachability. The hard
problem is choosing one candidate copy for every prescribed request
before this graph is known.

## 3. Exact selection IP and its owner-potential dual

Let \({\cal R}\) be the \(2n\) requests

\[
                         (3,c),\ (12,c)\qquad(c\in[n]),
\tag{3.1}
\]

and let \(\Omega_r\) be the legal labelled packet copies for request
\(r\). For \(P\in\Omega_r\), write \(U(P)\) and \(O(P)\) for its top
and owner sets. Introduce \(y_P\in\{0,1\}\).

### Theorem 3.1 (exact zero-quarantine packet system)

A zero-quarantine bank exists relative to \(T\) if and only if the
following integer system is feasible:

\[
 \sum_{P\in\Omega_r}y_P=1
                         \qquad(r\in{\cal R}),
\tag{3.2}
\]

\[
 \sum_{P:U\in U(P)}y_P\le1
                         \qquad(U\in\tbinom{[n]}M),
\tag{3.3}
\]

\[
 \sum_{P:X\in O(P)}y_P\le1
                         \qquad(X\in{\cal H}(T)),
\tag{3.4}
\]

and, for every covered owner \(X\),

\[
 \boxed{
 \sum_{P:X\in O(P)}y_P
 \le
 \sum_{P:\operatorname{par}_T(X)\in U(P)}y_P.}
\tag{3.5}
\]

#### Proof

Equations (3.2) choose one copy per request, and (3.3) makes the bank
top-disjoint. Equation (3.4) prevents two bank packets from using the
same hole.

For a covered owner \(X\), the right side of (3.5) is at most one by
(3.3). If a selected packet inserts \(X\), (3.5) forces selection of a
packet containing its current parent top. It simultaneously prevents a
second selected packet from inserting \(X\). Hence the selected bank
is internally owner-disjoint and parent-closed. Theorem 1.1 proves
sufficiency. Necessity is immediate from the same parent condition.
\(\square\)

The system is a directed hyperedge closure, not ordinary matching.
Its fractional relaxation has a useful exact dual. Replace (3.2) by
\(\le1\) and maximize \(\sum_Py_P\). Give the request, top, hole-owner,
and covered-owner constraints dual variables

\[
 a_r,\lambda_U,\nu_X,\mu_X\ge0,
\tag{3.6}
\]

respectively. The dual is

\[
 \min\left(
       \sum_ra_r+\sum_U\lambda_U+\sum_{X\in{\cal H}(T)}\nu_X
     \right)
\tag{3.7}
\]

subject, for every candidate packet \(P\in\Omega_r\), to

\[
 \boxed{
 a_r+\sum_{U\in U(P)}\lambda_U
 +\sum_{X\in O(P)\cap{\cal H}(T)}\nu_X
 +\sum_{X\in O(P)\cap{\cal C}(T)}\mu_X
 -\sum_{U\in U(P)}\sum_{X\in{\cal O}_T(U)}\mu_X
 \ge1.}
\tag{3.8}
\]

A feasible dual of value smaller than \(2n\) certifies that even the
fractional zero-quarantine bank is impossible. The zero-cost potential
\(\mu\) measures the discrepancy between owners imported by a packet
and current owner decks freed on its tops.

The dual is exact for the LP, not for the integer system. The latter
also has genuine set-packing odd-set obstructions.

### Proposition 3.2 (no matroid-intersection shortcut)

Even top-disjointness of packet candidates is not a matroid.

#### Proof

Fix one twelve-top support \(P\) and two distinct tops
\(U_1,U_2\in U(P)\). Choose a packet \(Q\) containing \(U_1\) and no
other top of \(P\). Then choose a packet \(R\) containing \(U_2\), no
other top of \(P\), and no top of \(Q\).

These choices exist for large \(m\). Indeed, the top degree \(D\) in
the twelve-top support hypergraph tends to infinity, while the maximum
pair codegree is \(O(D/m^2)\). Avoiding the \(O(1)\) other tops
therefore excludes only \(O(D/m^2)<D\) incident packets at each
choice.

Now \(\{P\}\) and \(\{Q,R\}\) are top-disjoint families, but neither
\(Q\) nor \(R\) can be added to \(\{P\}\). This violates the matroid
exchange axiom. \(\square\)

Thus neither the request partition matroid nor the owner-parent
constraints can be combined with top disjointness by ordinary matroid
intersection.

## 4. The atomic owner flow is positively solvable

Erase the requirement that the \(d\) owners assigned to one top form a
retained cyclic-window path. Keep the bank owner set \(B\), where

\[
                         s=|S|=15n,\qquad K=|B|=ds=15nd.
\tag{4.1}
\]

We assign new atomic owners to every top outside \(S\), avoiding \(B\).

### Theorem 4.1 (zero-quarantine atomic completion)

If (0.5) holds, there are sets

\[
 D_U\subseteq\{X:X\subseteq U,\ |X|=m\},
 \qquad |D_U|=d\qquad(U\notin S),
\tag{4.2}
\]

such that all \(D_U\) are pairwise disjoint and disjoint from \(B\).
Together with the fixed bank rows, they give one \(d\)-owner bundle on
every rank-\(M\) top and no repeated owner.

#### Proof

Use \(d\) left clones of every nonbank top in the containment graph,
and delete the \(K\) reserved owners \(B\) from the right side. For a
nonempty family \(A\) of nonbank tops, let \(\Gamma(A)\) be its owner
neighbourhood before deletion.

The biregular incidence count gives

\[
                         |\Gamma(A)|\ge\lambda|A|.
\tag{4.3}
\]

If \(|A|\ge K/g\), then

\[
 |\Gamma(A)\setminus B|
       \ge\lambda|A|-K
       \ge d|A|.
\tag{4.4}
\]

If \(0<|A|<K/g\), the neighbourhood contains all
\(a=\binom MH\) owners of any one top in \(A\). Hence

\[
 |\Gamma(A)\setminus B|
       \ge a-K
       \ge\frac{dK}{g}
       >d|A|
\tag{4.5}
\]

by (0.5). Thus every clone set satisfies Hall's inequality. An
integral bipartite matching saturates all clones and gives (4.2).
\(\square\)

At the calibrated growing height,
\(K(1+d/g)\) is polynomial in \(m\), while
\(\binom MH\) is superpolynomial, so (0.5) holds.

The theorem is a genuine zero-quarantine owner-flow result: no top is
left empty. Its limitation is exact and severe—an arbitrary set
\(D_U\) need not be a Johnson path, much less the retained deck of one
cyclic word.

## 5. A separated bank and private two-outside owners

The deterministic bank can be strengthened without changing its size
or local packet algebra.

### Lemma 5.1 (cross-packet top separation)

The \(2n\) requested packet copies can be chosen so that, in addition
to top and owner disjointness,

\[
 |U\cap V|<m
\tag{5.1}
\]

whenever \(U,V\) belong to different bank packets.

#### Proof

For one fixed top \(U\), the number of rank-\(M\) tops \(V\) with
\(|U\cap V|\ge m\) is at most

\[
 B_H=\sum_{i=0}^{H}\binom Mi\binom{n-M}{i}
     =\exp\!\left[O\!\left(H\log\frac mH\right)\right]
     =e^{o(m)}.
\tag{5.2}
\]

At a greedy step there are only \(O(m)\) earlier bank tops. In the
conditional labelled orbit for the next requested position-three
label, the probability that one of its at most twelve tops lies in
one of these forbidden balls is at most

\[
                         O\!\left(\frac{nmB_H}{N}\right)=o(1).
\tag{5.3}
\]

The top- and owner-collision exclusions from the original bank proof
also remove only an \(o(1)\) fraction of the conditional orbit.
Therefore at least one legal copy remains at every step.
\(\square\)

Consider now one repaired twelve-top packet with common core \(C\),
outside six-set \(S_6\), and top

\[
                         U_e=C\cup e,
          \qquad e\in\binom{S_6}2\setminus J.
\tag{5.4}
\]

Its source row has \(d-H\) **two-outside owners**

\[
                         {\cal O}^{(2)}_P(U_e)
       \subseteq\{A\cup e:A\in\tbinom C{m-2}\}.
\tag{5.5}
\]

### Lemma 5.2 (privacy of the dominant owner block)

Within the twelve packet tops, an owner
\(X=A\cup e\in{\cal O}^{(2)}_P(U_e)\) is contained only in \(U_e\).
Under the separation (5.1), it is contained in no top of another bank
packet.

#### Proof

If \(X\subseteq C\cup f\) for another packet edge \(f\), then
\(e\subseteq f\), because \(e\subseteq S_6\) is disjoint from \(C\).
Both have size two, so \(e=f\). This proves the within-packet claim.

If \(X\subseteq V\) for a top in another bank packet, then
\(|U_e\cap V|\ge|X|=m\), contradicting (5.1). \(\square\)

### Theorem 5.3 (same-top two-outside wall)

Let a separated bank be installed by replacing only its own top rows
in \(T\). For every repaired twelve-top row \(U_e\), zero quarantine
forces

\[
 \boxed{
 {\cal O}^{(2)}_P(U_e)
             \subseteq{\cal O}_T(U_e)\cup{\cal H}(T).}
\tag{5.6}
\]

If one owner violates (5.6), its current parent is an external nonbank
top, giving an edge to \(\dagger\) in the dependency graph and making
zero quarantine impossible.

#### Proof

Let \(X\) be a two-outside bank owner which is not a current hole.
By Theorem 1.1 its parent must be a selected bank top. Lemma 5.2 says
the only selected bank top containing \(X\) is \(U_e\). Therefore
\(\operatorname{par}_T(X)=U_e\), which is equivalent to
\(X\in{\cal O}_T(U_e)\). \(\square\)

The condition applies to \(12(d-H)=(12-o(1))m\) owners in every
repaired packet. It is a statewise source constraint, not a marginal
capacity estimate. The remaining \(12H\) one-outside owners may route
among adjacent packet tops and are governed by the full parent-closure
system (3.5).

## 6. Why whole retained paths remain the gate

For a top \(U\), let \({\mathscr R}(U)\) be the family of all legal
retained decks

\[
 R(U,\pi)=
 \{U\setminus I_H(\pi,t):0\le t<d\}
\tag{6.1}
\]

over rooted cyclic words \(\pi\) on \(U\).

After reserving the bank owners \(B\), a full physical completion is
the integer system

\[
 \sum_{R\in{\mathscr R}(U)}x_{U,R}=1
                         \qquad(U\notin S),
\tag{6.2}
\]

\[
 \sum_{\substack{U\notin S,\ R\in{\mathscr R}(U)\\X\in R}}
        x_{U,R}\le1
                         \qquad(X\notin B),
\tag{6.3}
\]

\[
                         x_{U,R}\in\{0,1\}.
\tag{6.4}
\]

Every owner in \(B\) is forbidden to the nonbank rows. The atomic flow
of Theorem 4.1 is obtained by replacing each bundled variable
\(x_{U,R}\) by \(d\) independent owner clones.

The bundled system is a rainbow \(d\)-uniform hypergraph matching, not
a bipartite flow. A useful statewise obstruction is immediate: if, for
some top \(U\), the residual Johnson graph on

\[
 \{X\subset U:|X|=m,\ X\notin B\}
\tag{6.5}
\]

contains no retained promotion path of length \(d\), then (6.2)--(6.4)
is infeasible although every atomic Hall inequality may hold.

Equivalently, writing a path transition as

\[
                         X_{t+1}=X_t-a_t+b_t,
\tag{6.6}
\]

every legal cyclic completion must obey the portal identity

\[
                         a_t=b_{t+H}
\tag{6.7}
\]

where both sides occur. Atomic owner flow does not record (6.7).

## 7. Alternating closure relative to the current table

One need not replace every nonbank row. Let \(S_0\) be the bank top
set. A zero-quarantine repair relative to the current table consists
of:

* a finite top set \(S\supseteq S_0\);
* the fixed bank rows on \(S_0\); and
* one new retained deck \(R_U\in{\mathscr R}(U)\) for every
  \(U\in S\setminus S_0\),

such that the new decks are pairwise disjoint and

\[
 \boxed{
  B\cup\bigcup_{U\in S\setminus S_0}R_U
   \subseteq
  {\cal H}(T)\cup\bigcup_{U\in S}{\cal O}_T(U).}
\tag{7.1}
\]

Condition (7.1) says that every imported covered owner has its parent
inside the changed top set. It is necessary and sufficient: unchanged
rows outside \(S\) then retain disjoint owners, while the new rows use
only holes or owners freed inside \(S\).

This is an AND-hypergraph closure. Choosing a new row forces every
current parent of its \(d\) imported owners into \(S\). Unlike an
ordinary augmenting path, one state has up to \(d\) simultaneous
successors. A closed alternating component satisfying (7.1) installs
the bank with no empty top; failure of every such component is a
statewise obstruction.

## 8. Chronology after installation

### Theorem 8.1 (owner-aware bank chronology)

Suppose the source bank has been installed by either the direct
criterion (0.4) or an alternating closure (7.1). Then every
subcollection of its top-disjoint packets may be switched in any
order. At every intermediate state:

1. there is one row on every nonquarantined top;
2. the middle-owner multiplicity vector is unchanged coefficientwise;
3. coefficient one is preserved; and
4. every protected trace vector is unchanged.

#### Proof

Each local three-top and repaired twelve-top packet has squarefree,
identical middle-owner supports on its two shores. The bank packets are
top- and owner-disjoint. Switching one packet therefore replaces its
owner set by the same set and does not affect availability of the
others. Induct over the chosen order. The protected trace statement is
the corresponding local packet identity. \(\square\)

Thus chronology is solved once zero-quarantine physical installation
is solved. There is no separate temporal owner accumulation.

## 9. Exact implication boundary

Proved here:

1. the exact parent-closure criterion and minimum external quarantine
   count for a fixed bank;
2. the exact zero-quarantine selection IP and its fractional
   owner-potential dual;
3. failure of the matroid exchange axiom;
4. a zero-quarantine integral atomic owner completion for the whole
   polynomial bank;
5. a separated deterministic bank refinement;
6. the dominant same-top two-outside statewise obstruction;
7. the exact retained-path factor and alternating-closure systems; and
8. automatic coefficient-one chronology after installation.

Not proved here:

1. a retained-path solution of (6.2)--(6.4) after reserving the bank;
2. a finite physical alternating closure satisfying (7.1) for an
   arbitrary coefficient-one table; or
3. a positive-density owner-aware repaired-packet layer.

The owner-capacity relaxation is therefore closed positively. The
remaining zero-quarantine gate is exactly the grouping of that flow
into portal-respecting retained paths, with the parent-closure
condition imposed statewise.
