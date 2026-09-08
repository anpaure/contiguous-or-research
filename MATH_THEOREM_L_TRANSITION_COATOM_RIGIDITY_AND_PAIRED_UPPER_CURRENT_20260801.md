# Lane L: fixed-transition coatom rigidity and the unavoidable paired upper current

Date: 2026-08-01  
Status: exact labelled obstruction and exact degree-preserving cocycle.  The
results rule out nontrivial transition-transparent coatom retiming on a fixed
Johnson chronology and rule out a clean primitive lower-provider root when
the immediate-upper state is returned exactly.  They do not rule out
compound point-degree-zero packets or the use of genuine upper surplus.

## 0. Verdict

At a coatom-bearing age state, the proposed ``retiming'' is not a free mark
choice.  If

\[
 P=(T;C_0,\ldots,C_d),\qquad |C_d|=1,
\]

is followed by a distinct Johnson-adjacent owner `T+`, then literal age
recurrence forces

\[
                 C_d=T-T^+,
 \qquad Q=T-C_d=T\cap T^+.                         \tag{0.1}
\]

Thus a fixed directed owner edge fixes its rank-`r-1` coatom.  There is no
nonidentity transition-transparent coatom retiming on fixed owner arcs.

Changing owner arcs does not produce a clean lower unit root either.  For
every degree-preserving rethread on a fixed rank-`r` owner multiset,

\[
       \partial_{r-1}\Delta L+\partial_{r+1}\Delta U=0,          \tag{0.2}
\]

where `Delta L,Delta U` are the signed lower-intersection and upper-union
palette changes and `partial_s[S]=sum_(x in S)e_x`.  Hence exact return of
the upper palette implies `Delta L in ker partial_(r-1)`.  In particular,
no primitive root `e_V-e_Q`, `V!=Q`, can be carried by a returned separator
whose upper state is also returned.

The smallest topology move that does carry one lower unit is an octahedral
two-edge rectangle.  It necessarily carries one opposite upper unit.  This
is the minimal labelled obstruction promised by the fixed-transition gate.

## 1. Exact coatom rigidity on a Johnson edge

Let consecutive rank-`r` owners be

\[
                         T^+=T-\{\alpha\}+\{\beta\}.             \tag{1.1}
\]

An age state on `T` is an ordered partition

\[
                         T=C_0\mathbin{\dot\cup}\cdots
                              \mathbin{\dot\cup}C_d.              \tag{1.2}
\]

Literal age recurrence says that an element which leaves the owner at the
next step must belong to the oldest cell `C_d`.  Equivalently, in the exact
changing-owner formula the deleted element `alpha` is selected from `C_d`.

### Theorem 1.1 (fixed-edge coatom rigidity)

If `|C_d|=1`, then every literal transition (1.1) satisfies

\[
                         C_d=\{\alpha\},\qquad
                         T-C_d=T\cap T^+.                         \tag{1.3}
\]

Consequently, after the directed owner transition `T->T+` is fixed, its
coatom target cannot be changed by retiming the age partition while
preserving that transition.

#### Proof

The only element of `T` absent from `T+` is `alpha`.  Since it leaves, exact
recurrence gives `alpha in C_d`.  The latter cell is a singleton, proving
`C_d={alpha}`.  Taking complements inside `T` gives (1.3).  \(\square\)

This is stronger than a Hall obstruction: the local supported menu on a
fixed edge has size one.  It applies independently of the chosen type of
the next state, survivor choices, topology outside the edge, or compiler
constraints.

### Lemma 1.2 (incoming filter when only the upper cofacet is fixed)

Let the preceding labelled partition be

\[
                         A=(T^-;A_0,\ldots,A_d).
\]

For any compatible current coatom state on `T`, its omitted letter `alpha`
obeys

\[
                         \alpha\in A_{d-1}\cap T.                 \tag{1.4}
\]

If `A_(d-1) cap T={alpha}`, then the current coatom is rigid even when one
fixes only the new letter `beta`, equivalently the outgoing upper cofacet
`T+{beta}`, and allows the successor owner to vary.

#### Proof

The survivor recurrence contains `C_d subseteq A_(d-1)`.  Since
`C_d={alpha}` and `alpha in T`, (1.4) follows.  A singleton intersection
leaves no second omission choice.  \(\square\)

## 2. A dimension-uniform literal fork

The preceding rigidity is not a vacuous lack of alternative supported
marks.  There are two individually legal coatom assignments with identical
rank types and identical outgoing upper cofacet, while a fixed incoming
partition admits only one of them.

Fix

\[
                         r\ge d+3,\qquad k\ge r+1.                 \tag{2.1}
\]

Choose a rank-`r` owner `T`, a letter `z notin T`, distinct
`a,b,c in T`, and distinct filler letters
`f_1,...,f_(d-1) in T-{a,b,c}`.  Put

\[
 G=T-\bigl(\{b\}\cup\{f_1,\ldots,f_{d-1}\}\bigr).               \tag{2.2}
\]

Choose the fillers so that `a,c in G`; this is possible because
`|G|=r-d>=3`.  Define the current partition `C` on `T` by

\[
 C_0=G,\qquad C_i=\{f_i\}\ (1\le i<d),\qquad C_d=\{b\}.          \tag{2.3}
\]

On the preceding owner `T^-=T-{c}+{z}`, define

\[
 A_i=C_{i+1}\ (0\le i<d),\qquad
 A_d=(G-\{c\})\cup\{z\}.                                       \tag{2.4}
\]

Then `A->C` is a literal transition: all displayed survivors are retained,
`z` leaves, and `c` is refreshed.  From `C`, retain every nonoldest cell and
move to `T_b^+=T-{b}+{z}`.  This is also literal, and its upper cofacet is

\[
                         T\cup T_b^+=T+\{z\}.                     \tag{2.5}
\]

Now swap `a` and `b` between the extreme cells:

\[
 \widetilde C_0=(G-\{a\})\cup\{b\},\qquad
 \widetilde C_i=C_i\ (1\le i<d),\qquad
 \widetilde C_d=\{a\}.                                         \tag{2.6}
\]

With the correspondingly retimed predecessor partition and successor owner
`T_a^+=T-{a}+{z}`, this is another literal two-sided fragment.  It has the
same source type `(r-d,1,...,1)`, the same successor type
`(1,r-d,1,...,1)`, and the same outgoing upper cofacet `T+{z}` as (2.5).
But it is incompatible with the fixed partition `A`, because

\[
             \widetilde C_d=\{a\}\not\subseteq A_{d-1}=\{b\}.   \tag{2.7}
\]

Thus rank data, owner containment, and even the complete adjacent upper
union do not make coatom marks transition-transparent.  A compiler guard
can only remove choices from this menu; the obstruction already holds with
no compiler guard imposed.

For `d=1,r=2`, the smallest local instance is

\[
 T=\{a,b\},\quad T^-=\{b,x\},\quad
 T_b^+=\{a,z\},\quad T_a^+=\{b,z\}.                              \tag{2.8}
\]

The two outgoing choices have common union `{a,b,z}`.  A fixed incoming
state on `{b,x}` forces the current oldest cell to be `{b}`, hence forces
the successor `{a,z}`.  Taking `x=z` gives the three-letter backtracking
version on `k=3`; taking `x!=z` gives four distinct owners on `k=4`.

## 3. The smallest owner--coatom reassignment is a hexagon

Let `I_(k,r)` be the bipartite containment graph between rank-`r` owners
and rank-`r-1` coatoms.

### Lemma 3.1 (girth six)

For `2<=r<k`, the graph `I_(k,r)` has no four-cycle and has a six-cycle.

#### Proof

If two distinct rank-`r` sets contained two distinct common
rank-`r-1` subsets, the union of those two subsets would have rank `r` and
would equal both owners, a contradiction.  Hence there is no four-cycle.

For a fixed `(r-2)`-set `S` and distinct `a,b,c notin S`, the alternating
sequence

\[
 S+ab,\ S+b,\ S+bc,\ S+c,\ S+ca,\ S+a                         \tag{3.1}
\]

is a six-cycle.  \(\square\)

The symmetric difference of two owner--coatom matchings is a union of
alternating cycles.  Therefore the smallest nontrivial supported
reassignment changes three owner marks, never two.  If one further fresh
letter `z` is available, the two matchings of (3.1) can be realized by
directing each owner to the matched coatom plus `z`.  They use the same
three successor owners and, source by source, the same upper cofacet
`T+{z}`.  (Without `z`, the two matchings instead orient the three displayed
owners in the two opposite cyclic directions.)  In either form Theorem 1.1
says that changing between them changes the directed owner edges; it is a
three-edge topology circuit, not retiming on a fixed chronology.  This is
an owner--coatom/topology statement; a depth-`d` age lift of the whole
circuit still needs residence-compatible incident states.

## 4. Lower and upper currents are inseparable

For a rank-`s` palette define the point-incidence homomorphism

\[
 \partial_s:\mathbb Z^{\binom\Omega s}\longrightarrow
             \mathbb Z^\Omega,
 \qquad \partial_s[S]=\sum_{x\in S}e_x.                          \tag{4.1}
\]

Let `F,F'` be directed multisets of Johnson edges on rank-`r` owners.  Assume
separately for every owner `T` that
`d_F^+(T)=d_(F')^+(T)` and `d_F^-(T)=d_(F')^-(T)`; this
includes every rethread of a one-copy owner permutation and every literally
returned separator macro whose auxiliary owner occurrences are restored.
Let `L(F),U(F)` be the occurrence-count vectors of intersections and unions,
and write

\[
                         \Delta L=L(F')-L(F),\qquad
                         \Delta U=U(F')-U(F).                     \tag{4.2}
\]

### Theorem 4.1 (paired-current cocycle)

Every such rethread satisfies

\[
             \boxed{\partial_{r-1}\Delta L+
                    \partial_{r+1}\Delta U=0.}                   \tag{4.3}
\]

Consequently:

1. if the immediate-upper occurrence vector is returned exactly, then
   `Delta L in ker partial_(r-1)`;
2. if `Q!=V`, no macro with exact upper return has
   `Delta L=e_V-e_Q`;
3. along any sequence whose upper state returns only at the end, a net
   lower primitive root leaves the nonzero upper point current
   `chi_Q-chi_V` and therefore cannot end with the upper state returned.

#### Proof

For each Johnson edge `X->Y`, coordinatewise

\[
                 \chi_X+\chi_Y=\chi_{X\cap Y}+\chi_{X\cup Y}.    \tag{4.4}
\]

Sum over `F` and `F'`.  The two owner-side sums agree by the in/out degree
hypothesis, leaving (4.3).  If `Delta U=0`, then
`partial_(r-1) Delta L=0`.  But

\[
                 \partial_{r-1}(e_V-e_Q)=\chi_V-\chi_Q\ne0       \tag{4.5}
\]

for distinct named sets `Q,V`.  This proves all three assertions. \(\square\)

Without owner-degree return, the exact right side of (4.3) is
`partial_r(Delta d^+ + Delta d^-)`.  Thus open owner endpoints are an
additional state coordinate, not a harmless omission.

If the old upper deck is exact (every upper target occurs once and the
number of selected edges is unchanged), merely preserving upper coverage
already forces `Delta U=0`; there is no multiplicity slack in which to hide
the current.  Locally, the same conclusion holds when every deleted upper
occurrence is a protected unique witness.  Mere upper completeness with
multiplicity slack does not force occurrence return.

At rank one, `partial_1` is the identity, so an exact-upper rethread cannot
change the lower palette at all.  In higher ranks, clean lower changes can
exist, but they must be point-degree-zero combinations.  The primitive
objects are Pluecker/Johnson-square relations, not one-for-one provider
roots.  Their physical serializability and compiler guards remain separate.

## 5. The minimal octahedral obstruction

The paired current of Theorem 4.1 is sharp on two changed edges.  Let `W`
be an `(r-1)`-set, choose `x in W`, and choose distinct
`a,b,t notin W`.  Define four rank-`r` owners

\[
\begin{aligned}
 C&=W+\{a\},& D&=W+\{b\},\\
 A&=(W-\{x\})+\{a,b\},& B&=W+\{t\}.
\end{aligned}                                                    \tag{5.1}
\]

All four edges between the source shore `{A,B}` and head shore `{C,D}` are
Johnson edges.  Replace

\[
                         A\to C,\ B\to D
 \quad\hbox{by}\quad A\to D,\ B\to C.                           \tag{5.2}
\]

The lower and upper payloads are exactly

\[
\begin{aligned}
 \Delta L&=e_{(W-x)+b}-e_{(W-x)+a},\\
 \Delta U&=e_{W+t+a}-e_{W+t+b}.                                  \tag{5.3}
\end{aligned}

Thus the lower primitive is accompanied by the opposite upper primitive;
their point currents cancel.

Conversely, after possibly transposing the source and head shores (time
reversal) and swapping the two diagonals, any nondegenerate two-edge Johnson
rectangle whose lower payload reduces after cancellation to one primitive
root is isomorphic to (5.1).  Indeed the unchanged lower colour is a common
`(r-1)`-set `W` of
the two heads.  The source incident twice through that colour is `W+t`.
The other common neighbour must be a top neighbour
`(W-x)+a+b`; otherwise its two lower colours would also agree.  Formula
(5.3) follows.  Hence every support-two lower unit transfer pays exactly one
upper unit transfer.

This converse is an owner-edge/palette classification.  It does not supply
a fixed-age literal lift; residence and compiler guards remain separate.

The smallest instance is `r=2,k=4`.  With

\[
 W=\{x\},\quad A=\{a,b\},\quad B=\{x,t\},
 \quad C=\{x,a\},\quad D=\{x,b\},                               \tag{5.4}
\]

the lower singleton changes from `a` to `b`, while the upper triple changes
from `{x,t,b}` to `{x,t,a}`.  One changed edge cannot preserve both owner
degrees, so (5.4) is support-minimal; four ground letters are minimal for a
nondegenerate mixed star--top rectangle.

## 6. Consequence for the recycled-separator proposal

The lower-only returned-root hypothesis in the earlier min--cut theorem is
not a literal consequence of coatom support:

* on fixed owner arcs, Theorem 1.1 leaves no coatom motion at all;
* after owner rethreading, a clean lower unit root is excluded by (4.3);
* the first nontrivial actuator (5.2) carries a paired upper current.

Therefore the smallest faithful regenerative state is at least

\[
       (\hbox{lower provider},\ \hbox{upper-current state},\
          \hbox{compiler guard state}),                           \tag{6.1}
\]

and a literal arc must record both signed palette payloads.  Strong
connectivity after projecting away the upper-current coordinate is
insufficient.  A possible positive replacement is a strongly connected
catalogue of point-degree-zero lower circuits, or a paired lower/upper
current network whose upper coordinate also returns.  Neither existence is
proved here.

The theorem does not exclude use of a genuine upper surplus, a nonexact
upper-complete deck with safe repeat capacity, or a compound packet in
`ker partial_(r-1)`.  It only proves that these are additional resources;
they cannot be silently supplied by transition-transparent coatom retiming
or by a lower-only returned separator.
