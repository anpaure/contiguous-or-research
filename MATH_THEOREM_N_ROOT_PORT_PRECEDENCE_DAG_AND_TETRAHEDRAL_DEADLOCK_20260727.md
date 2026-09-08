# Root-port packet precedence: the exact DAG criterion and a tetrahedral linear feedback obstruction

Date: 2026-07-27

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let

\[
 n=2m,\qquad 3\le M\le n-1,\qquad
 \mathcal T=\binom{[n]}M,\qquad N=|\mathcal T|.
\]

The root-port statements below hold for this full range.  Whenever the
protected retained-word parameter \(H\) is used, we specialize to the
upper annular rank

\[
 M=m+H,\qquad 3\le H\le m-1.
\]

For an \((M-2)\)-set \(C\) and distinct \(x,y,a\notin C\), an oriented
three-top root-port packet is

\[
 e(C;x,y,a):
 \quad
 \begin{cases}
 (C+xy,x)\longrightarrow(C+xy,y),\\
 (C+ya,y)\longrightarrow(C+ya,a),\\
 (C+ax,a)\longrightarrow(C+ax,x).
 \end{cases}
\tag{0.1}
\]

This note proves the following.

1. **Exact scheduling criterion.**  For a signed-flag-simple selected
   event family, form at every top its directed port graph.  A root-port
   chronology using every event once exists if and only if:

   - the used arcs at each top form one directed path, or one directed
     cycle with a chosen cut/root; and
   - after putting \(e\prec f\) whenever the head port of \(e\) is the
     next tail port of \(f\), and omitting the chosen wrap arc of every
     local cycle, the resulting event-precedence digraph is acyclic.

   Thus the global problem is literally a topological-sort problem after
   the local trails have been selected.  For local cycles, the choice of
   root is a choice of one precedence arc to delete; treating the wrap
   arc as forced is an off-by-one error.  The same theorem lifts to a
   literal exact-factor history when every uncut adjacency matches the
   complete retained word and the first source rows form the prescribed
   exact table.

2. **Deleting \(o(N)\) events cannot manufacture long local trails.**
   If the local component edge sizes at top \(U\) are
   \(s_{U,1}\ge s_{U,2}\ge\cdots\), then every deletion set \(F\) leaving
   at most one nonempty component at every top satisfies

   \[
      \boxed{
      |F|\ge\frac13\sum_{U\in\mathcal T}
      \left(d_U-s_{U,1}\right),}
   \tag{0.2}
   \]

   where \(d_U=\sum_i s_{U,i}\).  Hence an \(o(N)\)-event repair is
   possible only if all but \(o(N)\) tops already have one component.
   If their flag coverage is \(M-o(M)\), that component is already one
   \(M-o(M)\)-edge path or cycle.

3. **Acyclicity does not follow from the local trail condition.**  Four
   tops forming one Johnson tetrahedral cell support two flag-compatible
   packet events.  At one shared top the first event must precede the
   second; at the other shared top the second must precede the first.
   Both simultaneous event orientations give the same directed
   precedence digon, while reversing only one event violates signed
   flag simplicity.  Each local port graph is nevertheless a directed
   path, not a cycle.  If \(H\ge3\) and \(M\ge8H+2\), the cell also has compatible
   literal retained-word charts for both switches: on each shared top,
   the target word of the locally first switch is exactly the source
   word of the locally second switch.  Thus the circular wait survives
   the single-cell common-context test.

4. **The root-port obstruction has the exact \(N\)-scale.**  At the
   signed-flag projection, the four-top cell hypergraph is regular of
   degree

   \[
      D_\square=\binom M3(n-M)
   \]

   and maximum pair codegree

   \[
      \Delta_2^\square=\binom{M-1}{2},
      \qquad
      \frac{\Delta_2^\square}{D_\square}
      =\frac3{M(n-M)}.
   \]

   An elementary greedy argument gives at least \(N/16\) top-disjoint
   deadlock cells.  Consequently there is a signed-flag-simple packet
   family, locally one-trail on every used top, for which every event
   deletion making the precedence relation acyclic has size at least

   \[
      \boxed{N/16.}
   \tag{0.3}
   \]

   The standard fixed-uniformity Pippenger--Spencer theorem upgrades the
   packing to \((1-o(1))N/4\) cells when
   \(M,n-M\to\infty\), and correspondingly upgrades (0.3) to
   \((1-o(1))N/4\).  The elementary \(N/16\) bound is sufficient for the
   root-port no-go and uses no external matching theorem.  This packing
   is not asserted to lie in one common exact owner table.

5. **Forbidding two-common-top pairs is still insufficient.**  There is
   a six-top, three-event gadget in which every pair of events shares
   exactly one top, every local component is a path, and the three
   forced precedence relations form a directed \(3\)-cycle.  An
   elementary symmetric greedy packing gives \(N/36\) top-disjoint
   copies.  For \(M\ge8H+3\), one copy has exact compatible full-word
   charts at all three shared adjacencies.  Thus even a linear
   packet-support hypergraph needs a genuine global cycle invariant.

6. **The exact-factor scope is narrower.**  One three-event deadlock
   extends to a full injective predecessor-owner baseline whenever

   \[
      \left(\frac{M}{n-M+1}-1\right)(M-6)\ge6.
   \]

   On the other hand, for every fixed \(q\)-coordinate set \(Q\), any
   such baseline has at most

   \[
      \frac{q(2M-n)}nN
   \]

   roots in \(Q\).  Hence, at \(n=2m,M=m+H\) with
   \(H=O(\sqrt m)\), top-disjoint deadlocks using one fixed bounded
   coordinate seed have only \(o(N)\) copies.  A physical linear
   obstruction must be coordinate-diffuse or growing-scale.

7. **A cyclic primitive family can still be one legal macro packet.**
   Exact packet identities telescope over any full-state-linked event
   family, with every internal state cancelling.  The six-top
   three-cycle is jointly squarefree at its boundary and therefore,
   whenever those six source rows are jointly embedded in one exact
   factor, is an exact coefficient-one endpoint macro despite having no
   sequential primitive schedule.  Thus \(\Psi_{\rm prec}\) is the exact obstruction
   to primitive chronology, not an unconditional obstruction to
   simultaneous exact replacement.

Therefore the proposed implication

\[
 \text{selected root-port events}
 \Longrightarrow
 \text{topological schedule after deleting }o(N)\text{ events}
\]

is false as a theorem about signed root-port events.  A successful
exact-factor rooted Johnson triangle resolution must select
an **anti-deadlock** family from the start, already arranged as one long
trail at almost every top.  It must then satisfy the separate
global exact-owner conditions.  The present result supplies compatible
full word contexts inside one deadlock cell, but not simultaneous
owner-disjoint installation of a linear packing of cells.  It is
therefore not a no-go for every specially designed context-aware
resolution.  In particular, a chosen boundary-disjoint family of
jointly installed exact neutral strongly connected packets may be
contracted before the remaining precedence problem is scheduled.

## 1. Selected signed root-port events

For a top \(U\in\mathcal T\) and \(x\in U\), use separate outgoing and
incoming port resources

\[
 (U,x)^+,\qquad (U,x)^-.
\tag{1.1}
\]

An event \(e(C;x,y,a)\) uses the three outgoing ports at the tails in
(0.1) and the three incoming ports at the heads.

### Definition 1.1 (signed-flag simplicity)

A selected oriented event family \(\mathcal E\) is
**signed-flag-simple** if every resource \((U,x)^+\) and every resource
\((U,x)^-\) is used by at most one selected event.

At a fixed top \(U\), let \(D_U(\mathcal E)\) be the directed graph on
the labels of \(U\) whose arcs are the local root transitions supplied
by the events incident with \(U\).  Signed-flag simplicity is equivalent
to

\[
 \deg_{D_U}^+(x)\le1,\qquad \deg_{D_U}^-(x)\le1
 \quad(x\in U).
\tag{1.2}
\]

Thus every nontrivial component of \(D_U\) is a directed path or a
directed cycle.

The abstraction keeps one current root token \(r_U\in U\) at every top.
An event is applicable when the three current tokens are its three
tails; applying it moves them to its three heads.

## 2. Exact local and global precedence constraints

Suppose first that, for every used top \(U\), the nontrivial part of
\(D_U\) is connected.

- If it is a directed path, its initial root is the tail of its first
  arc and its final root is the head of its last arc.
- If it is a directed cycle, choose one port as the initial/final root.
  Cutting the cycle immediately before the event leaving that port turns
  its cyclic event order into a linear order.

For every internal port \(x\) of the resulting local trail, there are
unique events \(e,f\) such that \(e\) enters \(x\) and \(f\) leaves
\(x\).  Put a precedence arc

\[
 e\longrightarrow f.
\tag{2.1}
\]

On a local directed cycle, do **not** put the wrap precedence arc from
the last event into the first event across the chosen initial port.
Let \(P(\mathcal E,\kappa)\) be the resulting digraph on packet events,
where \(\kappa\) records the chosen cut of every local cycle.
Parallel precedence relations coming from different top-port
incidences are retained as distinct arcs for cut accounting.  They may
be identified only after all cuts are fixed; cutting one incidence does
not erase another parallel incidence.

### Theorem 2.1 (root-port chronological realizability)

Fix compatible initial roots at all used tops.  A signed-flag-simple
family \(\mathcal E\) has a root-port chronology using every event
exactly once if and only if:

1. at every top, its incident arcs form the one path from the prescribed
   initial root, or one cycle cut at that root; and
2. \(P(\mathcal E,\kappa)\) is acyclic.

When these conditions hold, every topological ordering of
\(P(\mathcal E,\kappa)\) is a valid root-port chronology.

#### Proof

In any chronology, restrict the global event order to events incident
with one top \(U\).  The unique current token must traverse the local
arcs consecutively.  Hence the arcs form one directed trail from the
prescribed initial root.  At every internal port, the entering event
precedes the leaving event.  All these local orders are restrictions of
one global linear order, so their union is acyclic.

Conversely, take a topological ordering of
\(P(\mathcal E,\kappa)\).  Proceed by induction through that order.
When event \(e\) is reached, every earlier event on each of its three
local trails has occurred and every later event has not: the consecutive
precedence arcs generate the full local trail order by transitivity.
Therefore the current root at each of the three tops is exactly the tail
required by \(e\).  Apply \(e\).  Induction realizes every event once.
\(\square\)

### Corollary 2.2 (cycle-cut transversal form)

Let \(P^0(\mathcal E)\) contain every matched head-to-tail precedence
arc, including the wrap arcs of local directed cycles.  For each local
cycle \(K\), let \(A_K\) be its set of wrap candidates.  Choosing its
initial root is choosing one arc \(c_K\in A_K\) to remove.

There is a root-port chronology if and only if one can choose one
\(c_K\) per local cycle so that

\[
 P^0(\mathcal E)-\{c_K:K\text{ a local cycle}\}
\tag{2.2}
\]

is acyclic.  Equivalently, the chosen cuts hit every directed cycle of
\(P^0(\mathcal E)\).

This is a simultaneous cycle-transversal problem: choosing a cut
independently at each top is not enough unless the resulting union is a
DAG.

Equivalently, introduce a binary variable \(z_\alpha\) for every
successor incidence \(\alpha\) on a local directed cycle, with
\(z_\alpha=1\) meaning that \(\alpha\) is the chosen wrap cut.  The
exact integral feasibility system is

\[
 \sum_{\alpha\in A_K}z_\alpha=1
 \qquad(K\text{ a local directed cycle}),
\tag{2.2a}
\]

and

\[
 \sum_{\alpha\in Z}z_\alpha\ge1
 \qquad(Z\text{ a directed cycle of }P^0),
\tag{2.2b}
\]

where fixed path-precedence arcs have cut variable zero.  Thus the free
root choices form a partitioned directed-cycle transversal, not
independent local choices.

### Corollary 2.3 (deadlock certificate)

For fixed cuts, \(P(\mathcal E,\kappa)\) is cyclic if and only if it has
a nonempty event set \(\mathcal Q\) such that every \(e\in\mathcal Q\)
has an immediate predecessor in \(\mathcal Q\).

#### Proof

A directed cycle has this property.  Conversely, repeatedly follow an
in-neighbour inside the finite set \(\mathcal Q\); some vertex repeats
and yields a directed cycle. \(\square\)

Thus the obstruction is a circular wait, not a failure of scalar root
balance.

### Lemma 2.4 (exact predecessor-owner histogram invariant)

Associate to a rooted top ((U,r)) its lower predecessor owner

\[
 p(U,r)=U\setminus\{r\}.
\tag{2.3}
\]

Every packet event preserves pointwise the full histogram

\[
 L(P)=|\{U:p(U,r_U)=P\}|,
 \qquad P\in\binom{[n]}{M-1}.
\tag{2.4}
\]

Consequently, an injective predecessor-owner baseline stays injective
after every prefix of any legal packet chronology.

#### Proof

Immediately before (e(C;x,y,a)), the predecessor owners at its three
tops are

\[
 C+y,\qquad C+a,\qquad C+x.
\]

Immediately afterwards they are, in the same top order,

\[
 C+x,\qquad C+y,\qquad C+a.
\]

The event merely cyclically permutes these three owners and fixes every
other owner. \(\square\)

### Theorem 2.5 (full-state exact-factor lift)

For each selected event occurrence \(e\), choose one literal exact
packet implementation.  At every incident top \(U\), let

\[
 s^{\rm src}_{e,U}\longrightarrow s^{\rm tar}_{e,U}
\tag{2.5}
\]

be its complete rooted retained-word state arc.  A primitive
coefficient-one chronology using every occurrence exactly once exists
if and only if there are, at every used top, linear orders

\[
 e_{U,1},\ldots,e_{U,d_U}
\]

such that:

1. every consecutive pair has complete state equality

   \[
   s^{\rm tar}_{e_{U,i},U}
   =
   s^{\rm src}_{e_{U,i+1},U};
   \tag{2.6}
   \]

2. the first source state on every used top, together with the fixed
   background rows, is one exact coefficient-one table; and
3. the union of the consecutive-event precedence arcs is acyclic.

When these conditions hold, every topological ordering is a legal
primitive history and every prefix remains inside one exact factor.
If the initial table is prescribed, the first source state in Item 2
must equal its prescribed row; pairwise internal gluing alone is not
enough.

#### Proof

Every legal history restricts on a top to the successive complete states
of that row, proving (2.6), the initial-boundary condition, and
acyclicity of the induced orders.

Conversely, take a topological ordering.  At each incident top of the
next event, all earlier local events and no later local events have
fired.  Induction using (2.6) makes the current complete row exactly the
required source row.  The event is therefore literally applicable.
Its source and target shores are squarefree and have the same middle
owner set, so replacing the three rows preserves the global owner
incidence vector.  Hence the table remains coefficient one after every
prefix.  Induction executes all events. \(\square\)

The root-port Theorem 2.1 is the projection of Theorem 2.5.  It is exact
at that projection, but complete word equality and the initial exact
table are additional physical hypotheses.

## 3. The deletion scale and one long trail per typical top

At top \(U\), let the nontrivial component edge sizes of \(D_U\) be

\[
 s_{U,1}\ge s_{U,2}\ge\cdots\ge s_{U,c_U}>0,
 \qquad d_U=\sum_i s_{U,i},
\tag{3.1}
\]

and put

\[
 r_U=d_U-s_{U,1}.
\tag{3.2}
\]

### Theorem 3.1 (exact component-deletion toll)

If deleting an event set \(F\subseteq\mathcal E\) leaves at most one
nontrivial local component at every top, then

\[
 \boxed{3|F|\ge\sum_{U\in\mathcal T}r_U.}
\tag{3.3}
\]

#### Proof

Deletion cannot join two original local components.  Hence, at top
\(U\), all retained arcs lie in one original component and number at
most \(s_{U,1}\).  At least \(d_U-s_{U,1}=r_U\) arcs incident with \(U\)
were deleted.

Each packet event is incident with exactly three distinct tops, so

\[
 \sum_U|\{e\in F:e\text{ is incident with }U\}|=3|F|.
\]

Summing the per-top lower bounds proves (3.3). \(\square\)

### Corollary 3.2 (an \(o(N)\) edit cannot create the trail property)

If \(|F|=o(N)\), then \(r_U=0\) for all but \(o(N)\) tops.  In
particular, if before deletion

\[
 d_U=M-o(M)
\tag{3.4}
\]

on all but \(o(N)\) tops, then those tops already contain one directed
path or cycle of length \(M-o(M)\).

There is an even simpler support observation: \(o(N)\) deleted events
touch only \(o(N)\) tops.  Therefore a positive-density family of bad
tops cannot be repaired at this scale at all.

This quantifier is substantially stronger than an \(o(MN)\)-event
repair.  The previously audited inverse-doublet factor shows that an
arbitrary near-perfect flag matching can require
\(\Omega(MN)\) edits merely to reach the one-component condition.
The next section shows that even after the component condition holds,
global precedence can require \(\Omega(N)\) further deletions.

## 4. The tetrahedral precedence deadlock

The obstruction has a complete two-common-top classification.

### Lemma 4.1 (two-common-top precedence reversal)

Let

\[
 U=S+p,\qquad V=S+q,\qquad |S|=M-1,
\]

with \(p,q\notin S\).  Every packet support containing both \(U\) and
\(V\) is indexed by a label \(z\in S\); its core and third top are

\[
 C_z=S-z,\qquad W_z=S-z+p+q.
\tag{4.0a}
\]

Take distinct \(z,z'\in S\) and one oriented packet on each support.
If their arcs at \(U\) form one directed two-edge path and their arcs at
\(V\) also form one directed two-edge path, then the two event orders
at \(U\) and \(V\) are opposite.

After possibly reversing both packets, the only possibility is

\[
 \begin{array}{c|cc}
  e_z&U:z\to p&V:q\to z\\
  e_{z'}&U:p\to z'&V:z'\to q.
 \end{array}
\tag{4.0b}
\]

Thus \(e_z\prec e_{z'}\) at \(U\) and
\(e_{z'}\prec e_z\) at \(V\).

#### Proof

The two active pairs at \(U\) meet only in \(p\).  A directed trail must
therefore enter \(p\) on one packet and leave on the other.  Reverse both
events if necessary to obtain

\[
 z\longrightarrow p\longrightarrow z'.
\]

The cyclic packet orientation containing \(z\to p\) is

\[
 z\longrightarrow p\longrightarrow q\longrightarrow z,
\]

so its arc at \(V\) is \(q\to z\).  The cyclic orientation containing
\(p\to z'\) is

\[
 p\longrightarrow z'\longrightarrow q\longrightarrow p,
\]

so its arc at \(V\) is \(z'\to q\).  The only local trail at \(V\) is
therefore

\[
 z'\longrightarrow q\longrightarrow z,
\]

which reverses the event order. \(\square\)

Fix an \((M-3)\)-set \(R\) and four distinct labels

\[
 z,z',u,v\notin R.
\]

Define four rank-\(M\) tops

\[
 \begin{aligned}
 U&=R+z+z'+u,\\
 V&=R+z+z'+v,\\
 W&=R+z'+u+v,\\
 W'&=R+z+u+v.
 \end{aligned}
\tag{4.1}
\]

They are the four \(M\)-facets of the \((M+1)\)-set
\(R+\{z,z',u,v\}\).

Take the two oriented packet events

\[
 e=e(R+z';\,z,u,v),
 \qquad
 f=e(R+z;\,u,z',v).
\tag{4.2}
\]

Their complete local actions are

\[
 \begin{array}{c|ccc}
 &U&V&W\\ \hline
 e&z\to u&v\to z&u\to v
 \end{array}
\tag{4.3}
\]

and

\[
 \begin{array}{c|ccc}
 &U&V&W'\\ \hline
 f&u\to z'&z'\to v&v\to u.
 \end{array}
\tag{4.4}
\]

### Theorem 4.2 (orientation-stable tetrahedral digon)

The pair \(\{e,f\}\) is signed-flag-simple.  Its local port graphs are:

\[
 U:\ z\longrightarrow u\longrightarrow z',
 \qquad
 V:\ z'\longrightarrow v\longrightarrow z,
\tag{4.5}
\]

and one-edge paths at \(W,W'\).  Therefore the local trail at \(U\)
forces

\[
 e\prec f,
\tag{4.6}
\]

whereas the local trail at \(V\) forces

\[
 f\prec e.
\tag{4.7}
\]

Thus no root-port chronology uses both events.

There are exactly two simultaneous orientation choices compatible with
signed-flag simplicity and the displayed local trail supports:
the orientations (4.2), or reversal of both events.  Reversing both
reverses (4.6)--(4.7) and leaves a precedence digon.  Reversing only one
event creates either two equal tails or two equal heads at a shared port
and violates signed-flag simplicity.

#### Proof

Equations (4.3)--(4.4) show that every outgoing flag and every incoming
flag is used at most once.  At \(U\), the head \(u\) of \(e\) is the
tail \(u\) of \(f\), giving (4.6).  At \(V\), the head \(v\) of \(f\)
is the tail \(v\) of \(e\), giving (4.7).  These are path-internal
ports, so there is no local-cycle cut which can remove either
precedence arc.

Upon reversing both events, the two path orders reverse.  If only \(f\)
is reversed, both \(e\) and \(f^{-1}\) enter \(u\) at \(U\); if only
\(e\) is reversed, both events leave \(u\).  The same conclusion is
visible at \(V\). \(\square\)

The root-port obstruction is stable under every signed-flag-simple
extension in which the displayed two-edge segments remain internal to
local paths.  A later extension which closes a local path into a cycle
can remove one displayed precedence arc only by choosing its initial cut
at that exact internal port.  The next lemma shows that the obstruction
is not an artefact of forgetting the retained word state.

### Lemma 4.3 (exact compatible retained-word realization)

Put

\[
 L=2H-1
\]

and assume \(H\ge3\) and \(M\ge8H+2\).  The four initial states, the two intermediate
states, and the four final states of the tetrahedral digon can be chosen
as literal retained paths in the exact three-top collar-neutral
\(\omega/\eta/\eta\) packet.  At \(U\), the complete target word of
\(e\) is the complete source word of \(f\); at \(V\), the complete
target word of \(f\) is the complete source word of \(e\).

#### Proof

Write the two positional bases from the three-top packet theorem as

\[
 \omega=(A,X,B,Y),\qquad \eta=(A,Y,B,X),
\tag{4.8a}
\]

where

\[
 X=A^+,F_1,\overleftarrow{B^-},\qquad
 Y=B^+,F_2,\overleftarrow{A^-},
 \qquad |A^\pm|=|B^\pm|=L,\quad |F_2|\ge3.
\tag{4.8b}
\]

The retained \(\omega\)-word is rooted two letters before its positional
\(A\), and the retained \(\eta\)-word two letters before its positional
\(B\).  After aligning these roots, both have one common template

\[
 (\hbox{two prefix letters},\ \rho,\ X,\ \sigma,\ Y),
\tag{4.8c}
\]

where \(\rho\) is the current root label and \(\sigma\) is the remote
placeholder.  Passing from the plus shore to the minus shore interchanges
\(\rho\) and \(\sigma\).  Thus it is enough to prescribe a common
ordered core and two possible remote-placeholder slots.

Choose one cyclic position array with a distinguished root slot
\(A_0\).  Clockwise after \(A_0\), place \(2L\) core slots, then a slot
\(B_e\), then a slot \(B_f\).  For the pair \((A_0,B_e)\), the two open
arcs have at least

\[
 2L,\qquad 2L+4
\tag{4.8d}
\]

core positions.  For \((A_0,B_f)\), they have at least

\[
 2L+1,\qquad 2L+3.
\tag{4.8e}
\]

Indeed the second bounds in (4.8d)--(4.8e) are exactly the consequence
of

\[
 M\ge8H+2=4L+6.
\]

Hence both pairs admit the arm decomposition (4.8b), including
\(|F_2|\ge3\), and the exact matched retained cuts of the three-top
packet theorem.

Put the labels of \(R\) identically into all remaining slots and assign
the three distinguished slots as follows:

\[
\begin{array}{c|ccc}
 &A_0&B_e&B_f\\ \hline
 U &z &u &z'\\
 V &z'&z &v\\
 W &u &v &z'\\
 W'&v &z &u.
\end{array}
\tag{4.8f}
\]

For event \(e\), use \(A_0,B_e\).  Its three source rows, expressed in
these slots, are

\[
\begin{array}{c|ccc}
 U &z&u&z'\\
 V &v&z&z'\\
 W &u&v&z'.
\end{array}
\tag{4.8g}
\]

The \(V\)-row is the state obtained after applying \(f\).  All three
rows have the same ordered core \(R+z'\), with \(z'\) frozen in \(B_f\),
and are exactly the \(\omega/\eta/\eta\) source chart for
\(e(R+z';z,u,v)\).  The switch interchanges \(A_0,B_e\).

For event \(f\), use \(A_0,B_f\).  Its source rows are

\[
\begin{array}{c|ccc}
 U &u&z&z'\\
 V &z'&z&v\\
 W'&v&z&u.
\end{array}
\tag{4.8h}
\]

The \(U\)-row is the state obtained after applying \(e\).  These rows
have the common ordered core \(R+z\), with \(z\) frozen in \(B_e\), and
are the exact source chart for \(f(R+z;u,z',v)\).  The switch
interchanges \(A_0,B_f\).

Therefore the two forced shared-top adjacencies agree as complete rooted
retained words, not merely in their distinguished root labels.  The
precedence relations remain \(e\prec f\) at \(U\) and \(f\prec e\) at
\(V\), so no global order exists. \(\square\)

For each switch separately, the imported three-top theorem gives exact
collar neutrality and squarefree equal-owner shores.  Lemma 4.3 does
not assert that the owner supports of \(e\) and \(f\), or of different
tetrahedral cells, are mutually disjoint in one global exact factor.

### Proposition 4.4 (exact digon cut/deletion ledger)

Suppose a selected family contains \(b\) pairwise event-disjoint
precedence digons of Lemma 4.1, and neither conflicting adjacency of a
digon is already a chosen local-cycle cut.  If \(X\) events are deleted
and \(s\) additional local trail breaks are introduced so that the
remaining precedence relation is acyclic, then

\[
 \boxed{|X|+s\ge b.}
\tag{4.8}
\]

#### Proof

Every digon must lose one of its two event vertices or one of its two
precedence arcs.  Event-disjointness makes the deletion charges
injective across digons, and a trail break is attached to one specified
adjacency.  Summing gives (4.8). \(\square\)

### Corollary 4.5 (proper-double cut Hall obstruction)

In any flag-simple one-component family, let \(\mathcal Q\) be the set
of two-common-top precedence digons from Lemma 4.1.  Form a bipartite
graph \(B_{\rm cut}\) from \(\mathcal Q\) to the local cyclic tops:
a conflict on shared tops \(U,V\) is adjacent to \(U\) precisely when
its forced adjacency at \(U\) lies on a local directed cycle and can be
chosen as that cycle's single chronological cut, and similarly for
\(V\).

Every chronology induces a matching of \(\mathcal Q\) into the eligible
top cuts.  In particular,

\[
 |\mathcal F|\le
 |N_{B_{\rm cut}}(\mathcal F)|
 \qquad(\mathcal F\subseteq\mathcal Q)
\tag{4.9}
\]

is necessary.  If

\[
 h=|\mathcal Q|-\nu(B_{\rm cut}),
\tag{4.10}
\]

then every repair by primitive event deletion uses at least

\[
 \boxed{\left\lceil\frac h3\right\rceil}
\tag{4.11}
\]

deleted events.

#### Proof

Every proper-double digon must spend one of its two shared-top cuts.
A top has only one chronological cut, and flag simplicity makes one
specified successor adjacency belong to only one such conflict.
Therefore the chosen cuts give the asserted matching.

At least \(h\) conflicts must disappear before the remaining cut graph
can have a matching saturating its left shore.  One packet event has
three unordered pairs among its three tops.  On each pair, flag
simplicity permits it to belong to at most one proper-double conflict.
Deleting one event therefore removes at most three conflicts, proving
(4.11). \(\square\)

## 5. Packing linearly many independent deadlocks

Let \(\mathcal K_\square\) be the four-uniform hypergraph on
\(\mathcal T\) whose edges are the four-facet sets

\[
 \{R+Q-\{q\}:q\in Q\},
\tag{5.1}
\]

where

\[
 R\in\binom{[n]}{M-3},
 \qquad
 Q\in\binom{[n]\setminus R}{4}.
\]

The intersection of the four vertices recovers \(R\), and their union
recovers \(R\cup Q\), so (5.1) defines a simple hypergraph.

### Lemma 5.1 (exact cell degrees)

\(\mathcal K_\square\) is regular of degree

\[
 \boxed{D_\square=\binom M3(n-M).}
\tag{5.2}
\]

Its maximum pair codegree is

\[
 \boxed{\Delta_2^\square=\binom{M-1}{2},}
\tag{5.3}
\]

and hence

\[
 \boxed{
 \frac{\Delta_2^\square}{D_\square}
 =\frac3{M(n-M)}.}
\tag{5.4}
\]

#### Proof

For a fixed top \(U\), choose the three members of \(Q\) which lie in
\(U\), and then choose the fourth member of \(Q\) outside \(U\).  This
gives (5.2).

Two distinct tops occur together in a cell only if they are Johnson
adjacent.  For adjacent \(U,V\), their union is the unique
\((M+1)\)-set of the cell, their two private labels are forced members
of \(Q\), and the remaining two members of \(Q\) may be chosen from the
\((M-1)\)-set \(U\cap V\).  This gives (5.3).  Division gives (5.4).
\(\square\)

### Theorem 5.2 (elementary linear deadlock packing)

There is a matching in \(\mathcal K_\square\) of size at least

\[
 \left\lfloor\frac N{16}\right\rfloor.
\tag{5.5}
\]

Choosing one tetrahedral event digon from every matched cell gives a
signed-flag-simple event family \(\mathcal E_\square\) such that:

1. every nonempty local port graph is one directed path;
2. its event-precedence digraph contains at least
   \(\lfloor N/16\rfloor\) vertex-disjoint directed digons; and
3. every event set whose deletion makes the precedence relation acyclic
   has size at least \(\lfloor N/16\rfloor\).

#### Proof

Let \(E_\square\) be the number of hyperedges.  Regularity and
four-uniformity give

\[
 E_\square=\frac{ND_\square}{4}.
\tag{5.6}
\]

Run the greedy matching algorithm.  Selecting one cell deletes at most
the sum of the degrees of its four vertices, namely
\(4D_\square\), candidate cells.  Thus it selects at least

\[
 \frac{E_\square}{4D_\square}=\frac N{16}
\]

cells, up to the integer floor.

Matched cells have disjoint top sets, so their event pairs use disjoint
signed flag resources.  Theorem 4.2 gives one directed digon on each
pair of events.  These digons are vertex-disjoint.  Every feedback
vertex set meets every one of them, proving the deletion bound.
\(\square\)

### Corollary 5.3 (near-perfect refinement; standard matching input)

Assume \(M\to\infty\) and \(n-M\to\infty\).  The fixed-uniformity
Pippenger--Spencer near-matching theorem, applied using (5.4), gives a
cell matching covering \((1-o(1))N\) tops.  Hence there is an event
family satisfying Items 1--3 of Theorem 5.2 with

\[
 \left(\frac14-o(1)\right)N
\tag{5.7}
\]

vertex-disjoint precedence digons.

The standard Pippenger--Spencer theorem is the only unproved external
input in this corollary.  It is not used for the unconditional
\(N/16\) obstruction.

## 5A. A linear-support three-event deadlock

The tetrahedral digon uses two events sharing two tops.  Excluding every
such pair does not make precedence automatic.  In this subsection assume
\(M\ge4\) and \(n-M\ge2\).

Fix \(S\in\binom{[n]}{M-1}\), distinct

\[
 a,b,c\notin S,
\qquad
 x,y,z\in S,
\]

with \(x,y,z\) distinct.  Put

\[
 A=S+a,\qquad B=S+b,\qquad C=S+c
\tag{5A.1}
\]

and

\[
 P_{ab}=S-x+a+b,\quad
 P_{bc}=S-y+b+c,\quad
 P_{ca}=S-z+c+a.
\tag{5A.2}
\]

Take

\[
 \begin{aligned}
 e_{ab}&=e(S-x;\,a,x,b),\\
 e_{bc}&=e(S-y;\,b,y,c),\\
 e_{ca}&=e(S-z;\,c,z,a).
 \end{aligned}
\tag{5A.3}
\]

Their local actions on the shared tops are

\[
 \begin{array}{c|cc}
 e_{ab}&A:a\to x&B:x\to b\\
 e_{bc}&B:b\to y&C:y\to c\\
 e_{ca}&C:c\to z&A:z\to a.
 \end{array}
\tag{5A.4}
\]

Each event has one further, private top:

\[
 P_{ab}:b\to a,\qquad
 P_{bc}:c\to b,\qquad
 P_{ca}:a\to c.
\tag{5A.5}
\]

### Theorem 5A.1 (linear three-event precedence cycle)

The family in (5A.3) is signed-flag-simple.  Any two event supports
share exactly one top.  Its three shared-top paths force

\[
 e_{ca}\prec e_{ab}\prec e_{bc}\prec e_{ca}.
\tag{5A.6}
\]

Hence it has no root-port chronology, despite having a linear
event-support hypergraph and only local directed paths.

#### Proof

The six tops in (5A.1)--(5A.2) are distinct under the stated
distinctness assumptions.  Equations (5A.4)--(5A.5) show signed-flag
simplicity and show that the only pairwise support intersections are
\(A,B,C\).  At those three tops the local paths are respectively

\[
 z\to a\to x,\qquad
 x\to b\to y,\qquad
 y\to c\to z,
\]

which give (5A.6). \(\square\)

Prescribe the initial roots

\[
 r_A=z,\quad r_B=x,\quad r_C=y,qquad
 r_{P_{ab}}=b,\quad r_{P_{bc}}=c,\quad r_{P_{ca}}=a.
\tag{5A.7}
\]

The six predecessor owners are then

\[
\begin{array}{lll}
 S-z+a,&S-x+b,&S-y+c,\\
 S-x+a,&S-y+b,&S-z+c.
\end{array}
\tag{5A.8}
\]

They are pairwise distinct: every one is recovered from its unique
missing member of \(\{x,y,z\}\) and its unique outside member of
\(\{a,b,c\}\).

### Lemma 5A.2 (extension to a full injective owner baseline)

Put

\[
 \rho=\frac{M}{n-M+1}.
\tag{5A.9}
\]

If

\[
 (\rho-1)(M-6)\ge6,
\tag{5A.10}
\]

then the six prescribed top-to-predecessor edges in (5A.8) extend to
an injective predecessor choice on every top of \(\mathcal T\).  In
particular, for \(n=2m\), \(M=m+H\), fixed \(A>0\), and
\(H\ge A\sqrt m\), (5A.10) holds for all sufficiently large \(m\).

#### Proof

Use the inclusion bipartite graph from rank \(M\) to rank \(M-1\).
Every left vertex has degree \(M\), and every right vertex has degree
\(n-M+1\).  Therefore every nonempty left family \(\mathcal S\) has

\[
 |\Gamma(\mathcal S)|
 \ge \max\{M,\rho|\mathcal S|\}.
\tag{5A.11}
\]

The first bound is the neighborhood of any one member; the second is
edge counting.  Remove the six already matched left vertices and the
six distinct right vertices in (5A.8).  For a family \(\mathcal S\) of
remaining left vertices,

\[
 |\Gamma'(\mathcal S)|
 \ge \max\{M,\rho|\mathcal S|\}-6.
\tag{5A.12}
\]

If \(|\mathcal S|\le M-6\), the \(M-6\) term proves Hall's inequality.
If \(|\mathcal S|>M-6\), (5A.10) gives

\[
 \rho|\mathcal S|-6\ge |\mathcal S|.
\]

Hall's theorem completes the six prescribed edges to a matching
saturating the full rank-\(M\) shore.  For \(n=2m,M=m+H\),

\[
 \rho-1=\frac{2H-1}{m-H+1},
\]

so (5A.10) follows in the stated regime. \(\square\)

Thus the three-event deadlock occurs inside a literal full injective
predecessor-owner baseline; it is not forced by an owner collision.
This statement still concerns the root/predecessor table.  It does not
install all retained paths of the three exact switches simultaneously
inside one middle factor.

### Lemma 5A.3 (full retained-word gluing for the linear cycle)

Assume \(H\ge3\) and \(M\ge8H+3\).  The three events in (5A.3) admit
literal compatible \(\omega/\eta/\eta\) retained-word charts at all
three forced shared-top adjacencies.  Thus the directed cycle (5A.6)
persists after the complete local word state, not only its root label,
is imposed.

#### Proof

Put \(L=2H-1\).  In one cyclic positional array choose a root slot
\(A_0\) and three consecutive remote slots

\[
 B_{ab},\quad B_{bc},\quad B_{ca},
\]

placing exactly \(2L\) ordinary core positions between \(A_0\) and
\(B_{ab}\).  Put the labels of
\(S\setminus\{x,y,z\}\) identically in all remaining positions, and use

\[
\begin{array}{c|cccc}
 &A_0&B_{ab}&B_{bc}&B_{ca}\\ \hline
 A      &z&x&y&a\\
 B      &x&b&y&z\\
 C      &y&x&c&z\\
 P_{ab} &b&a&y&z\\
 P_{bc} &c&x&b&z\\
 P_{ca} &a&x&y&c.
\end{array}
\tag{5A.13}
\]

Event \(e_{ab}\) uses \(A_0,B_{ab}\).  Its source rows are \(A\) after
\(e_{ca}\), the initial \(B\), and the initial \(P_{ab}\):

\[
 (a,x,y,z),\qquad (x,b,y,z),\qquad (b,a,y,z).
\tag{5A.14}
\]

They have one identical ordered core \(S-x\).  Event \(e_{bc}\) uses
\(A_0,B_{bc}\), with source rows

\[
 (b,x,y,z),\qquad (y,x,c,z),\qquad (c,x,b,z),
\tag{5A.15}
\]

and common ordered core \(S-y\).  Event \(e_{ca}\) uses
\(A_0,B_{ca}\), with source rows

\[
 (c,x,y,z),\qquad (z,x,y,a),\qquad (a,x,y,c),
\tag{5A.16}
\]

and common ordered core \(S-z\).

For the three remote slots, the forward open-arc core lengths are

\[
 2L,\qquad 2L+1,\qquad 2L+2,
\tag{5A.17}
\]

and their complementary lengths are at least

\[
 2L+5,\qquad 2L+4,\qquad 2L+3,
\tag{5A.18}
\]

because \(M\ge4L+7=8H+3\).  Every root/remote pair therefore has the
four length-\(L\) arms and the filler of length at least \(3\) required
by the exact three-top retained-word theorem.  Equations
(5A.14)--(5A.16) are its three exact common-core source charts.  Swapping
the indicated root and remote slot gives precisely the next full state
on \(A,B,C\), respectively.  The three full-state adjacencies therefore
force the same cycle (5A.6). \(\square\)

The three switches cannot be executed successively, but their aggregate
initial-to-final replacement can still be viewed as one macro packet.
The next proposition verifies its endpoint integrality exactly.

### Proposition 5A.4 (squarefree coefficient-one endpoint packet)

Assume additionally \(H\ge4\).  The six initial retained paths in
(5A.13) have pairwise distinct middle owners.  The formal six-path final
table is also squarefree and has exactly the same middle-owner set.
More generally, its complete protected target vector agrees with the
initial table for every \(0\le h\le2H\).

#### Proof

Use the common ambient set

\[
 \Omega=S+\{a,b,c\}.
 \tag{5A.19}
\]

The six tops omit the following coordinate pairs from \(\Omega\):

\[
\begin{array}{c|c}
A&\{b,c\}\\
B&\{a,c\}\\
C&\{a,b\}\\
P_{ab}&\{x,c\}\\
P_{bc}&\{y,a\}\\
P_{ca}&\{z,b\}.
\end{array}
 \tag{5A.20}
\]

Write the middle owner in row \(T\) as

\[
 \Omega\setminus(D_T\cup I_T),
 \qquad |D_T|=2,\quad |I_T|=H,
 \tag{5A.21}
\]

where \(D_T\) is the omitted pair from (5A.20) and \(I_T\) is the cyclic
\(H\)-window at the relevant retained phase.  Within one row, distinct
phases give distinct \(H\)-windows in an injective \(M\)-cycle because
\(H<M\); hence within-row owners are distinct.

It remains to exclude cross-row equality.  Equality in (5A.21) forces
\(I_T\) to contain \(D_{T'}\setminus D_T\), and \(I_{T'}\) to contain
\(D_T\setminus D_{T'}\).  The root slot and the three-slot remote
cluster in (5A.13) are separated in both directions by more than
\(2H\).  The fifteen row pairs split exhaustively as follows.

1. For

   \[
   (A,P_{bc}),\ (B,P_{ca}),\ (C,P_{ab}),\
   (P_{ab},P_{bc}),\ (P_{ab},P_{ca}),\
   (P_{bc},P_{ca}),
   \tag{5A.22}
   \]

   one forced window would have to meet both the root region and the
   remote cluster, impossible for an \(H\)-window.

2. For

   \[
   (A,P_{ab}),\ (A,P_{ca}),\
   (B,P_{ab}),\ (B,P_{bc}),\
   (C,P_{bc}),\ (C,P_{ca}),
   \tag{5A.23}
   \]

   one forced window lies at the root and the other at the remote
   cluster.  Their ordinary
   \(S\setminus\{x,y,z\}\)-coordinates lie in disjoint positional
   palettes.  Both palettes contribute because \(H\ge4\), so the two
   deleted sets cannot be equal.

3. The remaining pairs are \((A,B),(A,C),(B,C)\).  For \((A,B)\), the
   forced active labels are \(a\) in the third remote slot and \(b\) in
   the first.  The two possible statuses of the intervening label \(y\)
   force the ordinary coordinates of the windows onto opposite shores
   of the remote cluster, so equality is impossible.  For \((A,C)\),
   the forced labels lie in the third and middle remote slots; a window
   containing the middle slot cannot exclude both adjacent slots, which
   equality would require.  The pair \((B,C)\) is identical with the
   first and middle slots.

Thus the six initial retained paths are jointly squarefree.

Let \(A_1,B_1,C_1\) be the intermediate rows after
\(e_{ca},e_{ab},e_{bc}\), respectively, and let subscripts \(0,2\)
denote the initial and final shared rows.  For a retained row \(T\), let
\(\mathcal D_h(T)\) be its physical depth-\(h\) target incidence vector.
The three exact packet identities are

\[
\begin{aligned}
 \mathcal D_h(A_1)+\mathcal D_h(B_0)+\mathcal D_h(P_{ab,0})
 &=
 \mathcal D_h(A_2)+\mathcal D_h(B_1)+\mathcal D_h(P_{ab,1}),\\
 \mathcal D_h(B_1)+\mathcal D_h(C_0)+\mathcal D_h(P_{bc,0})
 &=
 \mathcal D_h(B_2)+\mathcal D_h(C_1)+\mathcal D_h(P_{bc,1}),\\
 \mathcal D_h(C_1)+\mathcal D_h(A_0)+\mathcal D_h(P_{ca,0})
 &=
 \mathcal D_h(C_2)+\mathcal D_h(A_1)+\mathcal D_h(P_{ca,1}).
\end{aligned}
\tag{5A.24}
\]

Adding cancels \(A_1,B_1,C_1\) and equates the complete initial and
final six-path vectors at every protected depth.  At \(h=H\), the
initial vector is \(0\)-\(1\), by the squarefreeness just proved.
The identical final vector is therefore also \(0\)-\(1\) and has the
same support. \(\square\)

Thus one six-top cell is a literal coefficient-one endpoint packet.
This does not supply a legal sequential switch history—the precedence
cycle proves that none exists—and it does not pack different six-top
cells owner-disjointly into one global exact factor.

### Lemma 5A.5 (bounded-coordinate root-capacity ceiling)

Let \(r_U\) be any injective predecessor choice on all rank-\(M\) tops,
and let \(Q\subseteq[n]\), \(|Q|=q\).  If

\[
 b_Q=|\{U:r_U\in Q\}|,
\]

then

\[
 \boxed{b_Q\le \frac{q(2M-n)}{n}N.}
\tag{5A.25}
\]

For \(n=2m,M=m+H\), this is

\[
 \boxed{b_Q\le \frac{qH}{m}N.}
\tag{5A.26}
\]

#### Proof

Let \(\mathcal I\subseteq\binom{[n]}{M-1}\) be the image of the
injective predecessor map, so \(|\mathcal I|=N\), and put
\(R_-= \binom n{M-1}\).  Deleting a root in \(Q\) lowers intersection
with \(Q\) by one, while deleting a root outside \(Q\) does not.  Hence

\[
 b_Q=
 \sum_{U\in\binom{[n]}M}|U\cap Q|
 -
 \sum_{P\in\mathcal I}|P\cap Q|.
\tag{5A.27}
\]

The first sum is \(qMN/n\).  The sum over the whole rank \(M-1\) is
\(q(M-1)R_-/n\).  The image omits \(R_--N\) sets, each contributing at
most \(q\), so

\[
 \sum_{P\in\mathcal I}|P\cap Q|
 \ge
 \frac{q(M-1)R_-}{n}-q(R_--N)
 =
 \frac{q(n-M)}{n}N.
\tag{5A.28}
\]

Here the last equality uses

\[
 \frac{R_-}{N}=\frac{M}{n-M+1}.
\]

Substitution into (5A.27) proves (5A.25), and the central specialization
gives (5A.26). \(\square\)

In particular, if top-disjoint copies of the three-event gadget all use
one fixed six-label set \(Q\), their six initial roots give

\[
 6g\le b_Q,\qquad g\le \frac{H}{m}N.
 \tag{5A.29}
\]

At \(H=O(\sqrt m)\), this is \(o(N)\).  Thus a fixed bounded-coordinate
deadlock family cannot refute the desired \(o(N)\)-feedback conclusion
inside a full injective owner baseline.  Any physical linear obstruction
must be coordinate-diffuse or growing-scale.  By Lemma 2.4, once the
initial predecessor map is injective, the same capacity ceiling applies
after every prefix of every legal primitive chronology.

### Corollary 5A.6 (elementary \(N/36\) linear-cycle packing)

There is a signed-flag-simple family containing at least
\(\lfloor N/36\rfloor\) event-disjoint directed precedence \(3\)-cycles,
such that within each gadget every pair of packet supports shares at
most one top.  Under \(H\ge4\), \(M=m+H\ge8H+3\), and \(n-M\ge2\),
each gadget separately carries the literal full-word, squarefree
coefficient-one endpoint packet of Proposition 5A.4.

#### Proof

Consider all labelled parameter choices in (5A.1)--(5A.3) as a
six-uniform multihypergraph on the top set \(\mathcal T\).  The symmetric
group on \([n]\) is transitive on \(\mathcal T\) and preserves the
parameter family, so every top has the same labelled degree
\(\Delta\).  If \(G\) is the number of labelled gadgets, incidence
counting gives

\[
 6G=N\Delta.
\]

A greedy top-disjoint packing removes at most \(6\Delta\) labelled
gadgets at each choice.  It therefore selects at least

\[
 \frac{G}{6\Delta}=\frac N{36}
\]

gadgets, up to the integer floor.  Top-disjointness makes their events
and signed flags disjoint, and Theorem 5A.1 supplies the precedence
cycles.  The local full-word assertion follows from
Proposition 5A.4.  It does not assert cross-gadget middle-owner
disjointness. \(\square\)

## 6. The directed-cycle invariant

For a selected family whose local components are already single trails,
let \(\mathscr K\) range over all admissible choices of one cut per local
directed cycle.  Define

\[
 \Psi_{\rm prec}(\mathcal E)
 =
 \min_{\kappa\in\mathscr K}
 \nu_{\rm cyc}\bigl(P(\mathcal E,\kappa)\bigr),
\tag{6.1}
\]

where \(\nu_{\rm cyc}\) is the maximum number of vertex-disjoint directed
cycles.

### Proposition 6.1 (feedback lower bound)

Every event deletion set which permits a root-port chronology has size
at least

\[
 \boxed{\Psi_{\rm prec}(\mathcal E).}
\tag{6.2}
\]

#### Proof

For the cuts used by the alleged chronology, every vertex-disjoint
directed cycle must lose a vertex.  Thus the deletion set has size at
least \(\nu_{\rm cyc}\) for those cuts, and hence at least the minimum
over all admissible cuts. \(\square\)

For the tetrahedral family in Theorem 5.2, every local component is a
path, so there are no cut choices and

\[
 \Psi_{\rm prec}(\mathcal E_\square)
 \ge\left\lfloor\frac N{16}\right\rfloor.
\tag{6.3}
\]

This is the requested directed-cycle invariant.  It is stricter than
the global root-label census.  Indeed, if \(s_U,t_U\) are the start and
end labels of the local paths, every packet merely cyclically permutes
its three root labels, so automatically

\[
 \sum_U(e_{t_U}-e_{s_U})=0.
\tag{6.4}
\]

The tetrahedral deadlock satisfies (6.4) exactly but still has positive
\(\Psi_{\rm prec}\).

### Theorem 6.2 (exact linked-family cancellation)

Let \(\mathcal Q\) be a finite family of literal exact packet switches.
For every event \(e\), every protected depth \(h\), and its three source
and target retained words, assume the exact packet identity

\[
 \sum_{U\in\operatorname{supp}(e)}
 \mathcal D_h(w^{\rm src}_{e,U})
 =
 \sum_{U\in\operatorname{supp}(e)}
 \mathcal D_h(w^{\rm tar}_{e,U}).
\tag{6.5}
\]

Match some target occurrences bijectively to source occurrences on the
same top, requiring equality of the complete rooted retained word on
every matched pair.  Let \(\partial_{\rm src}\mathcal Q\) and
\(\partial_{\rm tar}\mathcal Q\) be the unmatched source and target
occurrences.
Then, without any acyclicity assumption,

\[
 \boxed{
 \sum_{w\in\partial_{\rm src}\mathcal Q}\mathcal D_h(w)
 =
 \sum_{w\in\partial_{\rm tar}\mathcal Q}\mathcal D_h(w)
 \qquad(0\le h\le2H).}
\tag{6.6}
\]

If the boundary source paths are distinct row occurrences in one
existing exact factor, the boundary targets are literal valid rows with
the same topwise row-slot multiplicities, and the untouched exterior is
held fixed, then a \(0\)-\(1\) boundary source owner vector gives the
same \(0\)-\(1\) boundary target owner vector.  Provided every structural
constraint not encoded by the vectors \(\mathcal D_h\)—for example a
separately prescribed predecessor table—is also verified on the target
shore, the linked family can then be applied as one simultaneous
coefficient-one endpoint macro packet, even when its primitive
event-precedence digraph is cyclic.

#### Proof

Sum (6.5) over \(e\in\mathcal Q\).  Every matched complete word occurs
once on each side and cancels.  The remaining terms are precisely the
two boundary sums in (6.6).  At \(h=H\), equality with a \(0\)-\(1\)
source incidence vector makes the target vector the same \(0\)-\(1\)
vector.  Since the source rows occur in one exact factor, their owner
set is disjoint from the fixed exterior; the identical target owner set
is disjoint from it as well.  The stated literal-row and auxiliary
structural hypotheses complete the replacement. \(\square\)

### Corollary 6.3 (the linear deadlock is contractible as a macro)

The three-event family of Theorem 5A.1, with the endpoint packet of
Proposition 5A.4, has
\(\Psi_{\rm prec}\ge1\) when its three primitive switches must be
executed sequentially.  Whenever its six boundary source rows are
jointly embedded as distinct occurrences in one exact factor and the
auxiliary target constraints of Theorem 6.2 hold, it is instead one
legal exact six-row endpoint macro packet under simultaneous replacement.

Consequently the \(N/36\) root-port packing does not by itself impose an
\(N/36\) physical deletion toll.  Such a toll would additionally require
either:

1. a proof that the packed boundary source shores cannot be installed
   jointly and squarefreely; or
2. a rule that primitive switches, rather than exact endpoint macros,
   are the only allowed moves.

For unrestricted exact-factor constructions, one may therefore choose
a pairwise boundary-disjoint and compatible family of jointly installed
coefficient-one neutral macros, contract it, and schedule the quotient.
Alternatively, one may verify one globally compatible net macro family
directly.  Individually legal overlapping macros cannot automatically
all be contracted.  An acyclic primitive schedule is sufficient, but it
is not necessary once certified contractions are allowed.

## 7. What a positive construction must now prove

At the root-port level, a positive deterministic theorem must select the
events, their orientations, and their local linkages jointly so that:

1. all but \(o(N)\) tops already have one path or one cut cycle before
   any \(o(N)\)-event cleanup;
2. that trail has length \(M-o(M)\) at a typical top;
3. either \(\Psi_{\rm prec}=o(N)\), or all but \(o(N)\) of its feedback
   is covered by pairwise compatible exact macro packets from
   Theorem 6.2 whose contracted quotient is acyclic; in the purely
   sequential route, it is enough that the selected local orders come
   with an explicit global height

   \[
      h:\mathcal E\longrightarrow\mathbb Z
   \]

   which strictly increases on every forced precedence arc; and
4. the exact predecessor-owner histogram of Lemma 2.4 agrees with the
   prescribed injective source table; and
5. no bounded-coordinate bottleneck such as (5A.25) is violated.

An ordered-round construction would be sufficient: if packet events are
partitioned into rounds and every local trail meets those rounds in
strictly increasing order, then the round number is the height \(h\)
and Theorem 2.1 gives the chronology.  No such growing changing-core
resolution is constructed here.

Even these five properties do not finish the physical packet lift.
Every literal matched-cut packet requires its three current words to
have one common oriented core-order signature and the same admissible
gap pattern.  Root-port flags do not record that context.  The evolving
middle-owner table must also remain integral and squarefree.  Therefore

\[
 \boxed{
 \text{one long local trail}
 \;+\;
 \left[
 \begin{array}{c}
 \text{acyclic primitive precedence, or}\\
 \text{acyclic quotient after certified exact macro contractions}
 \end{array}
 \right]
 }
\]

is the exact chronological gate for the chosen implementation route,
but it is not a sufficient coefficient-one theorem.

## 8. Exact implication boundary

Proved:

1. the necessary-and-sufficient root-port scheduling theorem and its
   full-state exact-factor lift;
2. the exact cycle-cut transversal formulation;
3. the component-deletion lower bound (3.3);
4. a four-top, two-event precedence deadlock with no local cycle;
5. an elementary \(N/16\) packing of independent deadlocks;
6. a linear-support three-event deadlock and an elementary \(N/36\)
   packing of its directed \(3\)-cycles;
7. the sharper \((1/4-o(1))N\) tetrahedral packing under the standard fixed-uniformity
   near-matching theorem;
8. the cut-optimized directed-cycle invariant \(\Psi_{\rm prec}\);
9. a predecessor-owner-feasible linear three-event cycle whose six prescribed
   predecessor edges extend to a full injective baseline under
   (5A.10);
10. the bounded-coordinate capacity ceiling (5A.25), which prevents a
    fixed bounded seed from supplying a physical linear obstruction at
    \(H=O(\sqrt m)\);
11. the exact linked-family cancellation theorem (6.6), showing that
    certified coefficient-one cyclic packets may be contracted rather
    than deleted; and
12. the proper-double cut-Hall obstruction (4.9)--(4.11).

Not proved:

1. a specially selected anti-deadlock family with one \(M-o(M)\)-edge
   trail on almost every top;
2. an \(o(N)\)-feedback precedence orientation for such a family;
3. simultaneous owner-disjoint installation of the locally compatible
   \(\omega/\eta\) charts, or of their contracted endpoint macros,
   across a growing event family;
4. exact middle-owner capacity at every prefix; or
5. coefficient one.

The deterministic gate is now exact: arbitrary root-port matching and
even local one-trail feasibility do not imply a schedulable chronology.
The missing positive object is either a **context-decorated,
anti-deadlock, round-monotone rooted Johnson triangle resolution**, or
a globally embedded boundary-disjoint cover by exact neutral macros
whose contracted precedence quotient has \(o(N)\) feedback.

## 9. Independent audit record

An independent adversarial proof audit checked:

1. the root-port and full-state DAG equivalences, including the initial
   source-word boundary condition;
2. the factor \(3\) in (3.3);
3. \(D_\square=\binom M3(n-M)\),
   \(\Delta_2^\square=\binom{M-1}{2}\), the ratio
   \(3/[M(n-M)]\), and the \(N/16,N/36\) greedy constants;
4. the aligned-root interpretation and all four gap bounds in
   Lemmas 4.3 and 5A.3;
5. all fifteen cross-row cases and within-row injectivity in
   Proposition 5A.4;
6. the Hall extension constant (5A.10) and capacity ceiling (5A.25);
   and
7. the algebraic cancellation in Theorem 6.2 and the extra common-factor
   embedding hypotheses needed before it becomes a legal macro
   replacement.

The only external unproved input retained in this note is the standard
fixed-uniformity Pippenger--Spencer near-matching theorem used solely for
the optional \((1/4-o(1))N\) refinement.  The unconditional \(N/16\)
and \(N/36\) obstructions do not use it.
