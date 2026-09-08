# Root-port precedence has a minimal two-event holonomy digon

## Exact tetrahedral packing and the linear feedback/seam toll

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
                         N=\binom nM,
\qquad 3\le M\le n-1,
\tag{0.1}
\]

and consider the root-port projection of the collar-neutral three-top
packet. An oriented event

\[
                         e=(C;x,y,a)
\tag{0.2}
\]

has the three local root arcs

\[
\begin{array}{ccl}
 C+xy&:&x\longrightarrow y,\\
 C+ya&:&y\longrightarrow a,\\
 C+ax&:&a\longrightarrow x.
\end{array}
\tag{0.3}
\]

Whenever the literal \(\omega/\eta\) packet theorem is invoked below, we
specialize to its physical regime

\[
                         n=2m,\qquad M=m+H,\qquad H\ge3.
\tag{0.3a}
\]

There is an exact obstruction before any long precedence cycle is needed.
Two distinct packets can share two tops. If their arcs form directed
trails at both shared tops, the two local event orders are necessarily
opposite. They therefore form a directed precedence digon.

Explicitly, let \(|R|=M-3\), and let \(z,z',u,v\) be distinct outside
\(R\). On the four tops

\[
\begin{aligned}
 U&=R+z+z'+u, &V&=R+z+z'+v,\\
 W&=R+z'+u+v, &W'&=R+z+u+v,
\end{aligned}
\tag{0.4}
\]

take

\[
 e=(R+z';z,u,v),
 \qquad
 f=(R+z;u,z',v).
\tag{0.5}
\]

Their arcs are

\[
\begin{array}{c|ccc}
e&U:z\to u&W:u\to v&V:v\to z\\
f&U:u\to z'&V:z'\to v&W':v\to u.
\end{array}
\tag{0.6}
\]

Thus the rooted path at \(U\) forces \(e<f\), while the rooted path at
\(V\) forces \(f<e\). Reversing both packets reverses both local paths
and leaves the contradiction. Reversing only one packet destroys the
trail condition at both shared tops. No cut of a local cycle is available:
the two displayed local components are open paths.

The four tops in (0.4) are exactly the four \(M\)-set facets

\[
 R+(Z\setminus\{t\}),\qquad t\in Z,
 \qquad Z=\{z,z',u,v\}.
\tag{0.7}
\]

The \(4\)-uniform hypergraph of all such tetrahedral cells is regular of
degree

\[
                         D=\binom M3(n-M)
\tag{0.8}
\]

and has maximum pair codegree

\[
 \Delta _2=\binom{M-1}{2},
 \qquad
 {\Delta _2\over D}={3\over M(n-M)}.
\tag{0.9}
\]

Hence, when \(M,n-M\to\infty\), fixed-uniformity
Pippenger--Spencer gives \((1-o(1))N/4\) top-disjoint cells. Installing
the two formal root-port events (0.5) in every cell gives pairwise
event-disjoint precedence digons. Every feedback event set has size at
least

\[
                         (1-o(1)){N\over4}.
\tag{0.10}
\]

The same lower bound holds for

\[
 \#\{\text{deleted events}\}
 +\#\{\text{new local trail breaks at the displayed adjacencies}\}.
\tag{0.11}
\]

Thus flag Hall balance, exact root-label point margins, and local path
balance do **not** imply that deleting \(o(N)\) events produces a
topological schedule. Without the near-perfect matching theorem, a direct
greedy packing already gives \(N/16\) event-disjoint digons.

Excluding two-common-top pairs is still not sufficient. There is an exact
six-top family of three events in which every event pair shares exactly
one top, all local components are paths, and

\[
                         e_1<e_2<e_3<e_1.
\tag{0.12}
\]

It too has compatible full \(\omega/\eta\) state joins and a squarefree
coefficient-one endpoint table inside one cell. A symmetric greedy
packing gives \(N/36\) event-disjoint copies. Thus the genuine condition
is global feedback control, not merely top-pair linearity.

For \(M\ge8H+2\), the two events in every cell can moreover be equipped
with exact compatible \(\omega/\eta\) word charts: the target word of \(e\)
at \(U\) is the source word of \(f\), while the target word of \(f\) at
\(V\) is the source word of \(e\). Thus the digon survives the full local
word-state test, not merely its arc projection.

What is not asserted is that the packet owner supports from different
events and different cells are globally disjoint inside one exact middle
factor. The construction therefore does not refute a specially designed
high-degree, owner-disjoint physical RJTR. It does refute any scheduling
theorem whose hypotheses use only selected root-port flags, point margins,
local trail equations, pairwise packet legality, and even top-pair
linearity.

## 1. The exact precedence object

Let \({\cal E}\) be a selected family of oriented packet occurrences.
At a top \(T\), every incident occurrence supplies one directed arc between
two labels of \(T\). Suppose these arcs have been partitioned into rooted
directed trails. Whenever the arc of \(e\) is immediately followed by the
arc of \(f\) on one such trail, put

\[
                         e\prec_T f.
\tag{1.1}
\]

The **precedence digraph** \(D({\cal E})\) has vertex set \({\cal E}\)
and an arc \(e\to f\) for every relation (1.1).

### Proposition 1.1 (topological scheduling criterion)

At the root-port level, the prescribed local trails admit one common
chronological order if and only if \(D({\cal E})\) is acyclic.

If the packet occurrences carry full word states, the same assertion is
valid provided that, on every local adjacency, the full target word of the
first occurrence is the full source word of the second, and the first
source word on every local trail is the prescribed initial word at that
top.

#### Proof

Every physical chronology restricts at each top to the order of its unique
current root-port trail. It therefore respects every relation (1.1), so a
directed cycle is impossible.

Conversely, take a topological ordering of \(D({\cal E})\). At the
root-port projection, all earlier arcs on every incident local trail have
already occurred and no later arc has occurred, so the current root is the
tail of the present arc. Induction executes the events in topological
order. Under the additional full-state compatibility hypothesis the same
induction applies to the complete word, not merely its distinguished root
label. \(\square\)

If a local component is a directed cycle, choosing its initial root deletes
one cyclic successor relation. Hence the exact cycle version is

\[
 \boxed{\text{choose one cut in every local directed cycle, and require
 the remaining precedence digraph to be acyclic.}}
\tag{1.2}
\]

A local cut can eliminate a precedence obstruction only when it lies on
one of the adjacencies used by that obstruction.

## 2. Complete classification of two-common-top holonomy

Let

\[
 U=S+p,\qquad V=S+q,
 \qquad |S|=M-1,\quad p,q\notin S.
\tag{2.1}
\]

Every three-top support containing both \(U\) and \(V\) is obtained by
choosing one \(z\in S\). Its common core and third top are

\[
 C_z=S-z,
 \qquad
 W_z=S-z+p+q,
\tag{2.2}
\]

and its active pairs on \(U,V\) are respectively

\[
                         \{p,z\},\qquad\{q,z\}.
\tag{2.3}
\]

### Theorem 2.1 (two-common-top precedence reversal)

Take distinct \(z,z'\in S\), and let \(e_z,e_{z'}\) be oriented packets
on the supports (2.2). If their two arcs at \(U\) form one directed
two-edge path and their two arcs at \(V\) also form one directed two-edge
path, then the event orders on those paths are opposite.

Equivalently, after possibly reversing both packets, their arcs are

\[
\begin{array}{c|cc}
e_z&U:z\to p&V:q\to z\\
e_{z'}&U:p\to z'&V:z'\to q.
\end{array}
\tag{2.4}
\]

Thus \(e_z<e_{z'}\) at \(U\) and \(e_{z'}<e_z\) at \(V\).

If

\[
 \epsilon_T(e,f)=
 \begin{cases}
 +1,&e\text{ precedes }f\text{ on the local trail at }T,\\
 -1,&f\text{ precedes }e\text{ on that trail},
 \end{cases}
\tag{2.4a}
\]

then the theorem is the exact order-holonomy identity

\[
                 \boxed{\epsilon_U(e_z,e_{z'})
                        \epsilon_V(e_z,e_{z'})=-1.}
\tag{2.4b}
\]

Simultaneously reversing both packets changes both signs and preserves
their product. Thus (2.4b) is an intrinsic \(\mathbb Z_2\) holonomy of
the two shared-top charts.

#### Proof

The two active pairs at \(U\) meet only in \(p\). A directed trail must
therefore enter \(p\) on one packet and leave \(p\) on the other. Reverse
both orientations if necessary to obtain

\[
                         z\longrightarrow p\longrightarrow z'.
\tag{2.5}
\]

The cyclic orientation of the \(z\)-packet is then

\[
                         z\longrightarrow p\longrightarrow q
                           \longrightarrow z.
\tag{2.6}
\]

In particular its arc at \(V\) is \(q\to z\). Similarly, the cyclic
orientation of the \(z'\)-packet forced by \(p\to z'\) is

\[
                         p\longrightarrow z'\longrightarrow q
                           \longrightarrow p,
\tag{2.7}
\]

so its arc at \(V\) is \(z'\to q\). Therefore the only trail order at
\(V\) is

\[
                         z'\longrightarrow q\longrightarrow z,
\tag{2.8}
\]

which reverses the event order in (2.5). \(\square\)

If \(z=z'\), the two supports coincide. The opposite packet orientation
then gives reverse arcs on all three tops and can be ordered consistently.
Thus a genuine precedence cycle has length at least two, and Theorem 2.1
classifies the minimal length-two case.

### Corollary 2.2 (forbidden configuration in a flag-disjoint family)

In a root-port flag-disjoint packet family, the two arcs in (2.4) are
automatically consecutive at each shared intermediate flag \(p\) and
\(q\). Consequently a schedulable family cannot contain both events
unless

1. one event is deleted; or
2. at least one of those two local adjacencies is declared a trail break.

#### Proof

Flag-disjointness permits at most one incoming and at most one outgoing arc
at a fixed top-label flag. Hence no third event can be inserted between
the two arcs at \(p\) or at \(q\). Theorem 2.1 then gives a directed
digon. \(\square\)

This is hereditary: adding arbitrary arcs before and after the two
displayed segments does not remove the digon.

### Corollary 2.3 (top-pair linearity is necessary)

Fix two Johnson-adjacent tops \(U=S+p\) and \(V=S+q\). A root-port
flag-disjoint packet family contains at most two events whose supports
contain both \(U\) and \(V\). If it contains two with distinct third
core labels, those two events are a rigid precedence digon unless one of
their shared local adjacencies is a chosen trail break.

Consequently every schedulable, support-simple flag-disjoint family of
open local trails is **linear on top pairs**:

\[
 \boxed{\text{two distinct selected events share at most one top}.}
\tag{2.9}
\]

#### Proof

Every event containing \(U,V\) is indexed by \(z\in S\), as in (2.2).
At \(U\), its active pair is \(\{p,z\}\). Among all such events,
flag-disjointness allows at most one arc leaving the flag \((U,p)\) and
at most one arc entering it. Hence at most two events can be selected.

If two are selected, their \(U\)-arcs must have opposite incidence at
\(p\); otherwise they repeat an outgoing or incoming signed flag. Thus
they form a directed two-edge path at \(U\). The same argument at \(V\)
gives a directed two-edge path there, and Theorem 2.1 says their event
orders are opposite when their indices \(z,z'\) are distinct. For open
local trails neither adjacency can be cut, proving (2.9) in a
support-simple family. \(\square\)

Without support-simplicity there is one exception: the two opposite
orientations of the identical three-top support have \(z=z'\), share all
three tops, and can be ordered consistently on all three. This exception
has one direction component and supplies no new distinct support.

Thus the new obstruction is locally detectable before constructing the
full precedence digraph: repeated use of one Johnson edge by two distinct
packet triangles already carries nontrivial order holonomy.

## 3. The explicit tetrahedral digon

Take the data (0.4). For \(e=(R+z';z,u,v)\), formula (0.3) gives

\[
 U:z\to u,\qquad W:u\to v,\qquad V:v\to z.
\tag{3.1}
\]

For \(f=(R+z;u,z',v)\), it gives

\[
 U:u\to z',\qquad V:z'\to v,\qquad W':v\to u.
\tag{3.2}
\]

All outgoing flags and all incoming flags used by these six arcs are
distinct. In particular the pair is admissible in the root-port flag
hypergraph.

Root the four local paths initially at

\[
                         U:z,\qquad V:z',\qquad W:u,\qquad W':v.
\tag{3.3}
\]

Then \(e\) waits for \(f\) at \(V\), while \(f\) waits for \(e\) at
\(U\). Neither event is initially executable. Any chronology would have
to obey

\[
                         e<f<e.
\tag{3.4}
\]

There is nevertheless no root-label margin defect. The initial and final
root multisets are

\[
 \{z,z',u,v\}
 \quad\hbox{and}\quad
 \{z',z,v,u\},
\tag{3.5}
\]

respectively. They are identical. Each individual event also cyclically
permutes its three root labels and hence preserves every global label
count. Thus point-margin Euler balance does not see (3.4).

Deleting either \(e\) or \(f\) removes the obstruction. Alternatively,
splitting the path at \(u\) on \(U\), or at \(v\) on \(V\), removes one
of the two precedence relations. Both repairs cost one event or one
genuine new trail component.

### Lemma 3.1 (exact compatible matched-word charts)

Put \(L=2H-1\), and assume \(M\ge8H+2\). The four initial states in
(3.3), the two intermediate states needed by (3.1)--(3.2), and the four
final states can be chosen as literal retained \(\omega/\eta\) paths from
the three-top collar-neutral packet theorem. On each shared top, the
target state of the locally first event is exactly the source state of the
locally second event.

#### Proof

We first record the common-template form of the two bases. Write

\[
\begin{aligned}
 \omega&=(A,X,B,Y),\\
 \eta&=(A,Y,B,X),
\end{aligned}
\tag{3.6}
\]

where

\[
 X=A^+,F_1,\overleftarrow{B^-},
 \qquad
 Y=B^+,F_2,\overleftarrow{A^-}.
\tag{3.7}
\]

The \(\omega\)-path is rooted two letters before \(A\). The \(\eta\)-path
is rooted two letters before \(B\). After those rootings, both have the
same positional template

\[
             (\text{two prefix letters},\ \rho,\ X,\ \sigma,\ Y),
\tag{3.8}
\]

where \(\rho\) is the current root and \(\sigma\) is the remote
placeholder. The minus shore interchanges \(\rho,\sigma\). Therefore a
single ordered core in the positions of \(X,Y\) simultaneously supplies
the required \(\omega/\eta/\eta\) source chart.

Choose one cyclic position array with a distinguished root slot \(A\).
After \(A\), leave \(2L\) core positions and then a slot \(B_e\); let the
next position be a second slot \(B_f\). Thus, relative to \(B_e\), the
two core arcs have lengths at least

\[
                         2L,\qquad 2L+4,
\tag{3.9}
\]

and, relative to \(B_f\), at least

\[
                         2L+1,\qquad 2L+3.
\tag{3.10}
\]

The lower bounds follow from \(M\ge8H+2=4L+6\). Hence both choices
\((A,B_e)\) and \((A,B_f)\) admit the arm decomposition (3.7), with
\(|A^\pm|=|B^\pm|=L\), \(F_1\ge0\), and \(F_2\ge3\). They therefore
admit the exact matched cuts of the local packet theorem.

Put the labels of \(R\) in all remaining positions, identically on the
four tops, and prescribe the three distinguished slots by

\[
\begin{array}{c|ccc}
 &A&B_e&B_f\\ \hline
 U &z &u &z'\\
 V &z'&z &v\\
 W &u &v &z'\\
 W'&v &z &u.
\end{array}
\tag{3.11}
\]

Event \(e\) uses \(A,B_e\). Its source rows are

\[
\begin{array}{c|ccc}
 U &z&u&z'\\
 V &v&z&z'\\
 W &u&v&z',
\end{array}
\tag{3.12}
\]

where the row of \(V\) is the state obtained after \(f\). All three rows
have the identical ordered core \(R+z'\), with \(z'\) in slot \(B_f\).
They are precisely the \(\omega/\eta/\eta\) source chart for
\(e=(R+z';z,u,v)\), and switching \(e\) swaps \(A,B_e\).

Event \(f\) uses \(A,B_f\). Its source rows are

\[
\begin{array}{c|ccc}
 U &u&z&z'\\
 V &z'&z&v\\
 W'&v&z&u,
\end{array}
\tag{3.13}
\]

where the row of \(U\) is the state obtained after \(e\). All three rows
have the identical ordered core \(R+z\), with \(z\) in slot \(B_e\).
They are the \(\omega/\eta/\eta\) source chart for
\(f=(R+z;u,z',v)\), and switching \(f\) swaps \(A,B_f\).

Thus \(e^-(U)=f^+(U)\) and \(f^-(V)=e^+(V)\) as complete rooted retained
words, not merely at their distinguished labels. Nevertheless the two
global packets cannot be ordered, by (3.4). \(\square\)

The local theorem gives exact collar neutrality and a squarefree equal
middle-owner support for each individual switch. Lemma 3.1 does not say
that the owner supports of \(e\) and \(f\), or of different tetrahedral
cells, are mutually disjoint.

In fact the four-path endpoint tables inside one cell can also be made
coefficient-one.

### Proposition 3.2 (one-cell squarefree endpoints and exact telescoping)

Under the construction of Lemma 3.1, the four initial retained paths on
\(U,V,W,W'\) have distinct middle owners. The four formal final paths
also have distinct middle owners and have exactly the same middle-owner
set. More generally their aggregate physical target vectors agree at every
protected depth \(0\le h\le2H\).

#### Proof

Let \(\Omega=R+\{z,z',u,v\}\), so every top in the cell is obtained by
omitting one active label from \(\Omega\). Write \(E=B_e\), \(F=B_f\).
The active-label positions and the top omissions in the initial table are

\[
\begin{array}{c|c|cccc}
 &\text{omitted}&z&z'&u&v\\ \hline
 U &v &A&F&E&-\\
 V &u &E&A&-&F\\
 W &z &-&F&A&E\\
 W'&z'&E&-&F&A .
\end{array}
\tag{3.14}
\]

A middle owner on row \(T\) has the form

\[
                 \Omega\setminus\bigl(\{d_T\}\cup I_T\bigr),
\tag{3.15}
\]

where \(d_T\) is the omitted active label and \(I_T\) is one cyclic
\(H\)-window of that row. Equality of two owners forces the first row's
window to contain the second row's omitted label and, symmetrically, the
second row's window to contain the first row's omitted label.
Within one row, distinct cyclic \(H\)-windows give distinct owners because
the cyclic word is injective and \(H<M\).

The \(A\)-slot and the adjacent \(E,F\)-slots are separated in both
cyclic directions by more than \(2H\). Hence an \(H\)-window cannot meet
both regions. For the four cross-region row pairs

\[
                 (U,W),\ (U,W'),\ (V,W),\ (V,W'),
\tag{3.16}
\]

the two forced windows lie in disjoint positional context palettes.
Each contains at least \(H-2\ge1\) labels of \(R\), so their deleted
sets cannot agree.

It remains to check \((U,V)\) and \((W,W')\). For \((U,V)\), equality
would force the \(U\)-window to contain \(u\) at \(E\) and the
\(V\)-window to contain \(v\) at \(F\). If either window also contains
the other cluster slot, one deleted set contains respectively \(z'\) or
\(z\), while the other does not. Thus equality could occur only when
the \(U\)-window ends at \(E\) and the \(V\)-window starts at \(F\).
Their nonempty \(R\)-parts then lie on opposite sides of the adjacent
slots and are disjoint. They cannot be equal. The pair \((W,W')\) is
identical, with \(z,z'\) replacing \(u,v\). This proves squarefreeness
for the complete cyclic frames, hence also for the retained subpaths.

For the exact endpoint identity, denote the path target vector at depth
\(h\) by \({\cal D}_h(P)\). Event \(e\) gives

\[
 {\cal D}_h(U_0)+{\cal D}_h(V_1)+{\cal D}_h(W_0)
 =
 {\cal D}_h(U_1)+{\cal D}_h(V_2)+{\cal D}_h(W_1),
\tag{3.17}
\]

while event \(f\) gives

\[
 {\cal D}_h(U_1)+{\cal D}_h(V_0)+{\cal D}_h(W'_0)
 =
 {\cal D}_h(U_2)+{\cal D}_h(V_1)+{\cal D}_h(W'_1).
\tag{3.18}
\]

Here \(U_1=e^-(U)=f^+(U)\) and
\(V_1=f^-(V)=e^+(V)\). Adding (3.17)--(3.18) cancels both intermediate
paths and yields

\[
\begin{aligned}
 &{\cal D}_h(U_0)+{\cal D}_h(V_0)
   +{\cal D}_h(W_0)+{\cal D}_h(W'_0)\\
 &\qquad =
 {\cal D}_h(U_2)+{\cal D}_h(V_2)
   +{\cal D}_h(W_1)+{\cal D}_h(W'_1).
\end{aligned}
\tag{3.19}
\]

At \(h=H\), the left side is a \(0\)-\(1\) vector by the first part.
The right side is a nonnegative integral vector with the same total mass
and equal incidence vector, so it is the same \(0\)-\(1\) vector. Thus
the final table is squarefree and has exactly the same owner set.
\(\square\)

Proposition 3.2 makes the obstruction an exact one-cell coefficient-one
endpoint packet. It still does not provide a common owner-disjoint packing
of linearly many different cells.

## 4. Exact cut/deletion ledger for disjoint digons

Call a pair of events a **rigid digon** if it has the form in Theorem 2.1
and neither of its two conflicting local adjacencies is already a chosen
cycle cut or path break.

### Proposition 4.1 (matching lower bound)

Suppose a selected packet family contains \(b\) pairwise event-disjoint
rigid digons. Let \(X\) be a set of deleted events, and introduce \(s\)
new local trail breaks. If the remaining occurrences admit a chronology,
then

\[
                         |X|+s\ge b.
\tag{4.1}
\]

#### Proof

Every rigid digon must lose an event or one of its two forced precedence
adjacencies. Because the digons are event-disjoint, one deleted event hits
at most one of them. A trail break occurs at one specified local adjacency
and likewise hits at most one. Summing over the \(b\) digons gives (4.1).
\(\square\)

Thus cuts of local cycles do repair isolated digons, but they are a
capacity resource rather than a free logical erasure. In particular a
construction aiming at one long open trail per typical top has no internal
cycle cuts to spend.

## 5. Near-perfect tetrahedral packing

Let \({\cal Q}_{n,M}\) be the \(4\)-uniform hypergraph on
\(\binom{[n]}M\) whose hyperedges are

\[
 Q(R,Z)=\{R+(Z\setminus\{t\}):t\in Z\},
 \qquad |R|=M-3,\quad |Z|=4,\quad R\cap Z=\varnothing.
\tag{5.1}
\]

### Lemma 5.1 (exact degree and codegree)

The hypergraph \({\cal Q}_{n,M}\) is regular of degree

\[
                         D=\binom M3(n-M).
\tag{5.2}
\]

Two distinct tops have common-cell codegree zero unless they are
Johnson-adjacent. An adjacent pair has codegree

\[
                         \binom{M-1}{2}.
\tag{5.3}
\]

#### Proof

For a fixed top \(U\), choose the three members of \(Z\cap U\), and then
choose the fourth member of \(Z\) outside \(U\). The remaining \(M-3\)
members of \(U\) are \(R\). This proves (5.2).

Distinct facets of one tetrahedral cell differ by one coordinate, so only
Johnson-adjacent tops can share a cell. Write such a pair as

\[
                         U=S+p,\qquad V=S+q,
                         \qquad |S|=M-1.
\tag{5.4}
\]

A common cell is obtained uniquely by choosing the two elements of
\(Z\cap S\); then

\[
 R=S\setminus(Z\cap S),
 \qquad Z=(Z\cap S)+p+q.
\tag{5.5}
\]

There are \(\binom{M-1}{2}\) choices. \(\square\)

Consequently

\[
 {\Delta _2\over D}
 = {\binom{M-1}{2}\over\binom M3(n-M)}
 = {3\over M(n-M)}.
\tag{5.6}
\]

### Theorem 5.2 (elementary linear feedback-event obstruction)

There is a top-disjoint family of at least

\[
                         \left\lfloor {N\over16}\right\rfloor
\tag{5.7a}
\]

tetrahedral cells. Consequently there is a formal root-port
flag-disjoint packet family, locally one directed path at every used top,
for which every feedback event set and every combined
event-deletion/trail-break repair has size at least
\(\lfloor N/16\rfloor\).

#### Proof

Let \(E_{\cal Q}\) be the number of cells. Regularity and
four-uniformity give

\[
                         E_{\cal Q}={ND\over4}.
\tag{5.7b}
\]

Greedily choose cells. One chosen cell meets at most the sum of the
degrees of its four tops, namely \(4D\), candidate cells. Thus the
greedy matching has size at least

\[
                         {E_{\cal Q}\over4D}={N\over16},
\tag{5.7c}
\]

up to the integer floor. Put the rigid digon (0.5) on every chosen cell
and apply Proposition 4.1. \(\square\)

### Corollary 5.3 (near-perfect refinement)

Assume \(M,n-M\to\infty\). There is a formal root-port flag-disjoint
packet family on \((1-o(1))N\) tops whose precedence digraph is a
disjoint union of

\[
                         (1-o(1)){N\over4}
\tag{5.8}
\]

directed digons, together with isolated local incidences. Hence every
feedback event set has size at least (5.8), and every combined
event-deletion/trail-break repair has the same lower bound.

#### Proof

The uniformity of \({\cal Q}_{n,M}\) is four, its degree tends to
infinity, and (5.6) tends to zero. The fixed-uniformity
Pippenger--Spencer matching theorem therefore gives a matching covering
\((1-o(1))N\) tops, hence \((1-o(1))N/4\) cells.

Order the four active labels of every matched cell as \(z,z',u,v\), and
install the two formal events (0.5). Different cells are top-disjoint.
Inside one cell all signed root-port flags are distinct, as checked after
(3.2). Thus the entire family is flag-disjoint.

Every cell contributes the directed digon (3.4), and the event pairs are
disjoint between cells. Proposition 4.1 proves the claimed lower bound.
\(\square\)

If \(M\ge8H+2\), apply Lemma 3.1 independently in every top-disjoint
cell. This equips the packed digons with exact local matched-word charts.
Top-disjointness prevents conflicting word prescriptions at a top.
Global middle-owner disjointness across cells is a separate condition and
is not claimed.

The construction uses

\[
                         (1-o(1)){N\over2}
\tag{5.9}
\]

events. It is dense in the top layer but has bounded local trail length.
Therefore it disproves an unconditional \(o(N)\)-feedback theorem for
root-port Hall matchings. It does **not** disprove a theorem whose
hypotheses already include a carefully constructed growing-degree RJTR
with no two-common-top pairs.

## 5A. Linearity does not suffice: a literal three-event cycle

The proper double is the shortest obstruction, but excluding all
two-common-top pairs is not sufficient.

Choose an \((M-1)\)-set \(S\), distinct \(x,y,z\in S\), and distinct
\(a,b,c\notin S\). Put

\[
\begin{array}{lll}
 A=S+a,&B=S+b,&C=S+c,\\
 P_{ab}=S-x+a+b,&
 P_{bc}=S-y+b+c,&
 P_{ca}=S-z+c+a.
\end{array}
\tag{5A.1}
\]

Take

\[
\begin{aligned}
 e_{ab}&=(S-x;a,x,b),\\
 e_{bc}&=(S-y;b,y,c),\\
 e_{ca}&=(S-z;c,z,a).
\end{aligned}
\tag{5A.2}
\]

Their shared-top arcs are

\[
\begin{array}{c|cc}
e_{ab}&A:a\to x&B:x\to b\\
e_{bc}&B:b\to y&C:y\to c\\
e_{ca}&C:c\to z&A:z\to a,
\end{array}
\tag{5A.3}
\]

and their private arcs are

\[
 P_{ab}:b\to a,\qquad
 P_{bc}:c\to b,\qquad
 P_{ca}:a\to c.
\tag{5A.4}
\]

### Theorem 5A.1 (full-word linear precedence cycle)

Assume \(H\ge3\), \(M\ge8H+3\), and \(n-M\ge2\). The three events in
(5A.2) are signed-flag-simple, every pair of supports shares exactly one
top, and all six local port components are directed paths. They admit
exact compatible matched \(\omega/\eta\) word charts at every uncut local
adjacency. Nevertheless their precedence relation is

\[
                    e_{ca}\prec e_{ab}\prec e_{bc}\prec e_{ca},
\tag{5A.5}
\]

so no chronology exists.

#### Proof

The support and flag assertions follow directly from
(5A.1)--(5A.4). The local paths on the shared tops are

\[
 A:z\to a\to x,\qquad
 B:x\to b\to y,\qquad
 C:y\to c\to z,
\tag{5A.6}
\]

which already prove the precedence cycle at the root-port level.

It remains to audit complete word compatibility. Put \(L=2H-1\). Use
one root slot \(A_0\) and three adjacent remote slots
\(B_{ab},B_{bc},B_{ca}\), with exactly \(2L\) ordinary core positions
between \(A_0\) and \(B_{ab}\). Put the labels of
\(S\setminus\{x,y,z\}\) identically in all remaining positions, and use
the following table:

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
\tag{5A.7}
\]

Event \(e_{ab}\) uses the pair \(A_0,B_{ab}\). Its three source rows
are \(A\) after \(e_{ca}\), the initial \(B\), and the initial
\(P_{ab}\):

\[
 (a,x,y,z),\qquad(x,b,y,z),\qquad(b,a,y,z).
\tag{5A.8}
\]

They have the identical ordered core \(S-x\). Event \(e_{bc}\) uses
\(A_0,B_{bc}\), with source rows

\[
 (b,x,y,z),\qquad(y,x,c,z),\qquad(c,x,b,z),
\tag{5A.9}
\]

and common ordered core \(S-y\). Event \(e_{ca}\) uses
\(A_0,B_{ca}\), with source rows

\[
 (c,x,y,z),\qquad(z,x,y,a),\qquad(a,x,y,c),
\tag{5A.10}
\]

and common ordered core \(S-z\).

For the three remote choices, the forward core-arc lengths are

\[
                         2L,\quad2L+1,\quad2L+2.
\tag{5A.11}
\]

Their complementary core-arc lengths are at least

\[
                         2L+5,\quad2L+4,\quad2L+3,
\tag{5A.12}
\]

because \(M\ge4L+7=8H+3\). Thus every pair of placeholder positions
admits the decomposition

\[
 X=A^+,F_1,\overleftarrow{B^-},
 \qquad
 Y=B^+,F_2,\overleftarrow{A^-},
\tag{5A.13}
\]

with all four arms of length \(L\) and \(F_2\ge3\). By the common
template (3.8), (5A.8)--(5A.10) are exact matched
\(\omega/\eta/\eta\) source triples. Swapping the indicated two slots
gives exact equality with the next state on every shared top.

Thus the complete state equalities hold, while (5A.5) forbids a global
order. \(\square\)

### Proposition 5A.2 (six-path squarefree endpoint identity)

Assume additionally \(H\ge4\). The six initial paths in (5A.7) have
pairwise distinct middle owners. The formal six-path final table is also
squarefree and has exactly the same owner set. Its complete protected
target vector agrees with the initial table through every
\(0\le h\le2H\).

#### Proof

Use the common ambient set

\[
                         \Omega=S+\{a,b,c\}.
\tag{5A.16}
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
\tag{5A.17}
\]

An owner from row \(T\) is

\[
          \Omega\setminus\bigl(D_T\cup I_T\bigr),
 \qquad |D_T|=2,\quad |I_T|=H,
\tag{5A.18}
\]

where \(D_T\) is its omitted pair and \(I_T\) is a cyclic \(H\)-window.
If two owners agree, \(I_T\) must contain
\(D_{T'}\setminus D_T\), and conversely.
Owners at distinct phases of one row are distinct because its cyclic word
is injective and \(H<M\).

The root slot and the three-slot remote cluster are separated in both
directions by more than \(2H\). The table (5A.7) and omission list
(5A.17) now give three classes of row pairs.

1. For

   \[
   (A,P_{bc}),\ (B,P_{ca}),\ (C,P_{ab}),\
   (P_{ab},P_{bc}),\ (P_{ab},P_{ca}),\
   (P_{bc},P_{ca}),
   \tag{5A.19}
   \]

   at least one forced window would have to meet both the root region and
   the remote cluster. This is impossible.
2. For

   \[
   (A,P_{ab}),\ (A,P_{ca}),\
   (B,P_{ab}),\ (B,P_{bc}),\
   (C,P_{bc}),\ (C,P_{ca}),
   \tag{5A.20}
   \]

   one forced window lies in the root region and the other in the remote
   cluster. Their ordinary \(S\setminus\{x,y,z\}\) portions lie in
   disjoint positional palettes. Both are nonempty because \(H\ge4\),
   so the deleted sets cannot agree.
3. The remaining pairs are \((A,B),(A,C),(B,C)\). For \((A,B)\),
   the forced labels are respectively \(a\) in the third remote slot
   and \(b\) in the first. Equality of the active deleted coordinates
   is possible only if both windows include \(y\), or both exclude it,
   while respectively excluding \(x\) and \(z\). In either case one
   window takes its ordinary coordinates from after the remote cluster
   and the other from before it. Those nonempty sets are disjoint.

   For \((A,C)\), the forced labels are \(a\) in the third slot and
   \(c\) in the middle slot. A window containing the middle slot cannot
   exclude both adjacent slots; the possible active-coordinate sets
   therefore never agree. The pair \((B,C)\) is the same argument with
   the first and middle slots.

This proves squarefreeness of the six complete cyclic frames, hence of
their retained paths.

For the endpoint identity, let \(A_1,B_1,C_1\) be the intermediate
states after \(e_{ca},e_{ab},e_{bc}\), respectively. The three packet
identities are

\[
\begin{aligned}
 {\cal D}_h(A_1)+{\cal D}_h(B_0)+{\cal D}_h(P_{ab,0})
 &={\cal D}_h(A_2)+{\cal D}_h(B_1)+{\cal D}_h(P_{ab,1}),\\
 {\cal D}_h(B_1)+{\cal D}_h(C_0)+{\cal D}_h(P_{bc,0})
 &={\cal D}_h(B_2)+{\cal D}_h(C_1)+{\cal D}_h(P_{bc,1}),\\
 {\cal D}_h(C_1)+{\cal D}_h(A_0)+{\cal D}_h(P_{ca,0})
 &={\cal D}_h(C_2)+{\cal D}_h(A_1)+{\cal D}_h(P_{ca,1}).
\end{aligned}
\tag{5A.21}
\]

Adding cancels \(A_1,B_1,C_1\) and equates the complete initial and
final six-path vectors. At \(h=H\), the initial vector is \(0\)-\(1\);
therefore the identical final vector is \(0\)-\(1\) and has the same
support. \(\square\)

Thus the support-linear deadlock is already an exact coefficient-one
endpoint packet inside one six-top cell. Only simultaneous owner-disjoint
packing across different cells remains open.

### Corollary 5A.3 (elementary linear-cycle packing)

Under the hypotheses of Theorem 5A.1, there is a signed-flag-simple
family containing at least
\(\lfloor N/36\rfloor\) event-disjoint directed precedence
\(3\)-cycles of Theorem 5A.1, with every pair of event supports sharing
at most one top. Consequently every feedback event set has size at least
\(\lfloor N/36\rfloor\).

#### Proof

Regard all labelled choices in (5A.1)--(5A.2) as a \(6\)-uniform
multihypergraph on the rank-\(M\) tops. Coordinate symmetry makes it
regular; let its common labelled degree be \(\Delta\), and let its number
of labelled gadgets be \(G\). Incidence counting gives

\[
                         6G=N\Delta.
\tag{5A.14}
\]

A greedy top-disjoint packing deletes at most \(6\Delta\) labelled
gadgets at each choice. It therefore chooses at least

\[
                         {G\over6\Delta}={N\over36}
\tag{5A.15}
\]

gadgets, up to the integer floor. Their event cycles are vertex-disjoint,
so every feedback event set meets each one. \(\square\)

As before, the local charts in different gadgets have not been packed
into one common owner-disjoint exact middle factor. The theorem closes
the full-state precedence projection, not that global owner-packing gate.

## 6. Exact implication boundary

Proved here:

1. the exact precedence digraph and topological scheduling criterion;
2. the complete geometric classification of the minimal two-event
   precedence cycle;
3. an explicit four-top, two-event rigid digon with exact root-label point
   margins and flag-disjointness;
4. the fact that reversing packet orientations cannot repair the digon;
5. exact compatible full \(\omega/\eta\) charts and a squarefree
   coefficient-one endpoint table inside each cell;
6. the exact role of local-cycle cuts: one cut can hit one specified bad
   adjacency, while open paths have no cut to spend;
7. the degree, codegree, and relative-codegree constants of the
   tetrahedral-cell hypergraph; and
8. a \((1-o(1))N/4\) feedback-event or new-trail-break lower bound at
   the top/flag packing level;
9. a support-linear, full-word compatible three-event precedence cycle;
10. a squarefree coefficient-one endpoint identity inside its six-top
    cell; and
11. an elementary \(N/36\) packing of event-disjoint copies of that
    longer-cycle obstruction.

Not proved here:

1. simultaneous owner-disjoint installation of all packed local charts
   inside one exact middle factor;
2. a lower bound for every growing-degree packet resolution satisfying the
   full physical chart condition;
3. inevitability of two-common-top pairs in a near-full high-degree
   resolution; or
4. a construction of one long trail per typical top.

The exact new deterministic conditions are therefore:

1. a **linearity or cut budget** eliminating all but \(o(N)\)
   two-common-top holonomy pairs; and
2. a genuine global feedback invariant controlling the longer cycles
   which survive even in a support-linear family.

Linearity is necessary for open trails but not sufficient. A positive
global packet theorem must construct a common root/cut system whose full
precedence digraph has feedback number \(o(N)\), while retaining
\(o(N)\) aggregate trail components. Point margins, local Euler balance,
pairwise packet legality, and top-pair linearity do not imply this.
