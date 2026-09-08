# A rooted pentagon packet and the Dyck-port obstruction

Date: 2026-07-26

This note separates two versions of a Tamari associator which cannot be
identified.

* A **literal associator path** contains two different Dyck roots in one
  Johnson path.  Such a path can occur in a complete-wreath trade, but it
  can never belong to a Dyck-port-transversal local factor and hence cannot
  be substituted recursively into a labelled MSW hole.
* A **rooted associator packet** keeps every Dyck port fixed and reroutes
  the intermediate states of several paths.  This is the correct object for
  context substitution.  There is an explicit five-row example on six core
  coordinates.  It is the first packet which crosses the component
  partition left by the certified leaf rotations.

No computation or search is used below.

## 1. The port obstruction

Let (J) have size (2r), and let

\[
                     D_r\subseteq\binom Jr
\]

be the standard family of Dyck (r)-sets.  Recall that a
(D_r)-port-transversal middle-levels path factor consists of paths

\[
 P=X_0\subset Y_0\supset X_1\subset\cdots\subset
 Y_{r-1}\supset X_r=J\setminus P,\qquad P\in D_r,       \tag{1.1}
\]

which partition both middle ranks, with each member of (D_r) used once as
an initial port.

### Theorem 1.1 (one-Dyck-vertex-per-path)

Every path in a (D_r)-port-transversal factor contains exactly one member
of (D_r), namely its initial port.  Consequently no path in such a factor
can contain a literal nontrivial Tamari step

\[
                         P\longrightarrow Q,
             \qquad P,Q\in D_r,\quad P\ne Q.             \tag{1.2}
\]

The conclusion is unaffected by adding arbitrarily many auxiliary paths.

#### Proof

The paths partition the (r)-sets of (J), so every (Q\in D_r) occurs
in exactly one path.  Port transversality simultaneously requires every
(Q\in D_r) to occur as the initial vertex of exactly one path.  If (Q)
were an interior vertex of the path rooted at a different (P\in D_r), it
could not occur again as a port, contradicting the partition.  Thus the
only Dyck vertex of the path rooted at (P) is (P).  This proves both
claims. \(\square\)

### Corollary 1.2 (the four-row complete-wreath associator cannot be
port-repaired)

The positive distinguished row

\[
             (1245,1256,1268,1678,3678)                 \tag{1.3}
\]

from `MATH_ATTACK_E_FOUR_ROW_TAMARI_ASSOCIATOR_20260726.md` cannot occur in
any (D_4)-port-transversal local factor.  Hence no compensating packet can
restore its Dyck-port allocation while retaining (1.3).

#### Proof

Both `1245` and `1256` are Dyck four-sets.  The first is the initial port
of (1.3), while the second is an interior state.  Theorem 1.1 applies.
\(\square\)

Thus the four-for-four table is a valid complete-wreath circuit but is not
a recursive context substitute.  A recursively usable associator must
implement its effect by multirow routing while keeping all Dyck roots out
of path interiors.

## 2. An involution preserving every Chung--Feller layer

Represent a balanced word on ([2r]) by steps in ({+1,-1}), and let its
flaw number be the number of steps lying strictly below the horizontal
axis.  For (I\subseteq\{1,\ldots,r-1\}), put

\[
                   \tau_I=\prod_{i\in I}(2i\ \ 2i+1).   \tag{2.1}
\]

The transpositions in (2.1) are disjoint.

### Lemma 2.1 (even-pair invariance)

The permutation \(\tau_I\) preserves the flaw number of every balanced
word.  In particular it preserves every Chung--Feller class \(D^t_{2r}\),
including the Dyck class (D^0_{2r}=D_r).

#### Proof

It is enough to swap the steps in positions (2i,2i+1).  Immediately
before these two steps the height has the parity of (2i-1), and is
therefore nonzero.  Equal steps are unchanged.  For the two orders `+-`
and `-+`, if the initial height is positive, both steps in either order lie
on or above the axis; if it is negative, both steps in either order lie
strictly below it.  The endpoint after the pair is the same in the two
orders, so every later step has the same status.  Thus the flaw count is
unchanged. \(\square\)

Let (X_t(w)), (0\le t\le r), be the even states of the canonical MSW
trace rooted at (w\in D_r).  The Chung--Feller column theorem says that

\[
       w\longmapsto X_t(w)\quad\hbox{is a bijection}
       \quad D_r\longrightarrow D^t_{2r}.               \tag{2.2}
\]

Consequently Lemma 2.1 defines permutations \(\kappa_t\) of \(D_r\) by

\[
                   \tau_I X_t(w)=X_t(\kappa_t w).        \tag{2.3}
\]

Since complementation commutes with \(\tau_I\), one has
\(\kappa_r=\kappa_0\).  Reindexing the rows by their initial ports gives the
phasewise interleaving

\[
 X'_t(u)=\tau_I X_t(\kappa_0^{-1}u)
        =X_t(\kappa_t\kappa_0^{-1}u),                   \tag{2.4}
\]

with (X'_0(u)=X_0(u)) and (X'_r(u)=X_r(u)).  It is a rooted path factor:
coordinate relabelling preserves Johnson edges, (2.2) preserves every
(X)-layer, and the aggregate adjacent-union family is the full
((r+1))-st rank and is therefore also preserved.

## 3. The five-row rooted pentagon

Set (r=3), list the Dyck roots in the order

\[
                  123,\quad124,\quad125,\quad135,\quad134. \tag{3.1}
\]

and take

\[
                         \tau=(2\ 3)(4\ 5).             \tag{3.2}
\]

The canonical MSW rooted paths are

\[
\begin{array}{c|cccc}
1&123&136&146&456\\
2&124&126&156&356\\
3&125&145&345&346\\
4&135&235&245&246\\
5&134&234&236&256.
\end{array}                                             \tag{3.3}
\]

Applying (2.4) gives the alternative paths

\[
\begin{array}{c|cccc}
1&123&126&156&456\\
2&124&234&345&356\\
3&125&235&236&346\\
4&135&136&146&246\\
5&134&145&245&256.
\end{array}                                             \tag{3.4}
\]

### Theorem 3.1 (rooted pentagon packet)

The tables (3.3) and (3.4) are two (D_3)-port-transversal exact path
factors of the middle-levels graph on ([6]).  Replacing (3.3) by (3.4)
is a five-for-five exact wreath trade after adjoining \(\infty\).

The phase permutations in (2.4) are

\[
 f_1=(1\ 2\ 5\ 3\ 4),\qquad
 f_2=(1\ 2\ 3\ 5\ 4),\qquad f_0=f_3=1.                \tag{3.5}
\]

In particular the packet is transitive on the five Catalan fillings at
each internal phase and does not preserve the two components of the
certified leaf-rotation graph.

#### Proof

Every row in both tables is a Johnson geodesic from the displayed Dyck
root to its complement.  The two tables both enumerate all twenty
three-subsets of ([6]), once each.

For completeness, the adjacent-union colours of (3.3) are

\[
\begin{array}{c|ccc}
1&1236&1346&1456\\
2&1246&1256&1356\\
3&1245&1345&3456\\
4&1235&2345&2456\\
5&1234&2346&2356,
\end{array}                                             \tag{3.6}
\]

whereas those of (3.4) are

\[
\begin{array}{c|ccc}
1&1236&1256&1456\\
2&1234&2345&3456\\
3&1235&2356&2346\\
4&1356&1346&1246\\
5&1345&1245&2456.
\end{array}                                             \tag{3.7}
\]

Each table enumerates all fifteen four-subsets of ([6]), once each.
Thus both ownership ledgers agree exactly.  The initial states in (3.4)
are the five members of (D_3), and none of its ten internal states is a
Dyck root, so the port condition holds literally.

On the layers in (3.3), \(\tau\) induces respectively

\[
 \kappa_0=(2\ 4)(3\ 5),\quad
 \kappa_1=(1\ 2)(4\ 5),\quad
 \kappa_2=(1\ 2)(3\ 4),\quad
 \kappa_3=\kappa_0.
\]

Formula \(f_t=\kappa_t\kappa_0^{-1}\) gives (3.5).  Both are five-cycles,
which proves the last assertion. \(\square\)

The intrinsic intersections over the three noninitial states change as

\[
 (6,6,4,2,2)\quad\longrightarrow\quad(6,3,3,6,5).       \tag{3.8}
\]

Thus the packet has genuine lower-target action; it is not merely a
different drawing of the same rooted paths.
Writing \(e_j\) for the unit mass at local target \(j\), its exact
intrinsic signed target vector is

\[
                  \boxed{\Delta_{\rm pent}
                    =2e_3+e_5-e_4-2e_2.}                \tag{3.9}
\]

## 4. Rooted packets are functorial under one-hole tree contexts

The port condition is exactly what makes a local packet recursively usable.
The following elementary closure statement is useful independently of the
pentagon.

### Theorem 4.1 (rooted context functor)

Let \(\mathcal P^-\) and \(\mathcal P^+\) be two rooted complement-path
factors on the same (2r) coordinates, indexed so that the two paths with
index (u) have the same initial port (P_u) and terminal port
(\overline{P_u}).  Suppose their aggregate (X)- and (Y)-ledgers agree.
Then the packet remains exact after any common one-hole ordered-binary-tree
context is wrapped around every port.

#### Proof

Every one-hole context is built from the following three operations:

\[
             x\mapsto Ax,\qquad x\mapsto xB,\qquad
             x\mapsto J(x)=1x0,                        \tag{4.1}
\]

with fixed Dyck words (A,B).  It is enough to verify these operations.

For right concatenation, the MSW path identity is

\[
 P(P_uB)=P(P_u)B\ \Vert\
       \overline{P_u}\bigl(P(B)\setminus\{B\}\bigr).  \tag{4.2}
\]

The first part is the old local packet with a common spectator appended,
so both ledgers remain equal.  The second part is identical on the two
sides row by row because their terminal ports agree.  Left concatenation
is the same argument with the fixed path (P(A)) first and the local
packet, with the fixed spectator (\overline A), second.

For \(J\), the flip order of a rooted path with local flip word \(\rho\)
becomes

\[
                  (2r+2,\ 1+\operatorname{rev}\rho,\ 1). \tag{4.3}
\]

The two boundary edges in (4.3) depend only on the common ports.  Between
them, reversal, complementation and adjoining the two outer coordinates
give injective images of the old local (X)- and (Y)-ledgers.  Hence the
two aggregate ledgers still agree, and the new endpoints again agree
row by row.  Induction through (4.1) proves the theorem. \(\square\)

Consequently the rooted pentagon packet can be installed at every common
size-three one-hole context, with arbitrary fixed material outside that
hole.  Phase-disjoint installations commute.

## 5. Exact scope

Theorems 3.1 and 4.1 give a genuine multirow associator which survives the
recursive interface and crosses the leaf-rotation component invariant.
They do **not** yet give the full operadic associator

\[
                  N(N(A,B),C)\longleftrightarrow N(A,N(B,C))
                                                               \tag{5.1}
\]

for three independently varying nonempty subtrees.  Inflating the four
leaves of the pentagon by different trees is not a common one-hole context,
and equality of the two ledgers under such row-dependent substitutions
does not follow from Theorem 4.1.

Theorem 1.1 also shows that the desired extension cannot keep a literal
within-row edge between the two Dyck bracketings.  The correct remaining
gate is therefore an **operadically natural rooted packet**: all Dyck ports
must stay at path endpoints, while the internal routing implements the
associator collectively across several rows.  This is strictly narrower
than the former unrestricted complete-wreath associator gate and avoids
the false hope of repairing (1.3) with more auxiliary rows.

## 6. The induced five-shape rewrites and their exact invariant

Under the order (3.1), the five ordered binary trees of size three are

\[
\begin{aligned}
T_1&=111000,&T_2&=110100,&T_3&=110010,\\
T_4&=101010,&T_5&=101100 .
\end{aligned}                                           \tag{6.1}
\]

At the two internal phases the rooted pentagon therefore induces the
owner-routing permutations

\[
                 c_1=(T_1\,T_2\,T_5\,T_3\,T_4),\qquad
                 c_2=(T_1\,T_2\,T_3\,T_5\,T_4).          \tag{6.2}
\]

Both cycles meet the two components of the leaf-rotation graph.  Thus the
leaf normal form from Section 16 of the plateau audit is not invariant
under rooted pentagon routing.

It is nevertheless important not to infer a full Catalan conveyor from
(6.2).  First consider the **fringe-context subfamily**.  Let
\(\mathscr G^{(3),\mathrm{fr}}_r\) be the graph on size-\(r\) ordered
binary trees in which, at any node whose fringe subtree has exactly three
nodes, that subtree may be replaced by an arbitrary one of
\(T_1,\ldots,T_5\).

This is only a subgraph of the full common-context graph supplied by
Theorem 4.1.  In particular, the allowed operation \(x\mapsto xB\) need
not present \(x\) as a fringe subtree in the first-return binary-tree
encoding.  The distinction is essential below.

Define the collapsed three-skeleton recursively by

\[
\mathfrak c_3(T)=
\begin{cases}
\star_3,&|T|=3,\\
\varnothing,&T=\varnothing,\\
N(\mathfrak c_3(L),\mathfrak c_3(R)),&T=N(L,R),\ |T|\ne3.
\end{cases}                                             \tag{6.3}
\]

### Theorem 6.1 (fringe three-skeleton classification)

Two size-\(r\) trees lie in the same component of
\(\mathscr G^{(3),\mathrm{fr}}_r\) if and only if they have the same collapsed
three-skeleton.

Consequently the fringe-context graph is disconnected for every
\(r\ge4\).  In particular, rooted pentagon packets restricted to fringe
subtrees cannot realize a root Tamari rotation.

#### Proof

Two distinct fringe subtrees of the same size cannot be nested.  Hence all
size-three fringe subtrees of a tree are pairwise disjoint.  Replacing one
of them changes neither the size of any ancestor subtree nor any material
outside that fringe root.  It therefore leaves (6.3) unchanged.

Conversely, if two trees have the same collapsed skeleton, their only
differences are the five possible fillings of the disjoint
\(\star_3\)-slots.  The cycle \(c_1\) is transitive on those five fillings,
so each slot can be changed independently while all other slots are fixed.
This joins the two trees in the enlarged graph.

For \(r\ge4\), no move is supported at the root.  The ordered pair of root
subtree sizes \((|L|,|R|)\) is therefore invariant.  Left and right combs
have different such pairs, proving disconnection.  A root Tamari rotation
\(N(N(A,B),C)\leftrightarrow N(A,N(B,C))\) changes the left-subtree size
from \(|A|+|B|+1\) to \(|A|\), so it cannot be generated by proper
size-three substitutions. \(\square\)

The qualification "restricted to fringe subtrees" cannot be removed.
For example, right-concatenation is allowed by Theorem 4.1 and directly
connects

\[
                         T_1\,10\quad\hbox{to}\quad T_4\,10.
\]

In first-return form the first word has root-left size two, whereas the
second has root-left size zero; their collapsed three-skeletons differ.
Thus Theorem 6.1 is not an invariant of the full common-context packet
graph.  There is nevertheless a simpler obstruction for that full graph.

### Theorem 6.2 (factor-free isolated owners)

For every \(r\ge4\), the full common-context pentagon graph on \(D_r\) is
disconnected.  Explicit isolated vertices are

\[
 U_{2k}=(1100)^k,\qquad
 U_{2k+1}=1(1100)^k0\qquad(k\ge2).                       \tag{6.4}
\]

#### Proof

The context operations \(x\mapsto Ax\), \(x\mapsto xB\), and
\(x\mapsto1x0\) retain the six-letter local word \(x\) as a contiguous
Dyck factor.  It is therefore enough to show that the words in (6.4)
contain no size-three Dyck factor.

In the four-periodic interior \((1100)^\infty\), a six-letter block in
the four possible starting residues is respectively

\[
 110011,\qquad100110,\qquad001100,\qquad011001.
\]

The first is unbalanced, the second falls below its starting height at
the third step, and the last two begin with a down-step.  For the odd word
in (6.4), the only block meeting the new first symbol is \(111001\), which
is unbalanced, while the only block meeting the new last symbol begins
with a down-step.  Thus no local word from (6.1) occurs, so no pentagon
packet contains \(U_r\) as a port.  It is isolated. \(\square\)

Hence arbitrary common-context copies still do not generate a full
Catalan conveyor, although Theorem 6.1 is not the reason.

## 7. Root-scale pair-swap conjugates still have a Motzkin invariant

There is a different root-scale enlargement for which one can give a
complete obstruction.  Let

\[
 \mathcal H_r=\left\langle(2i\ \ 2i+1):1\le i<r\right\rangle
             \cong(C_2)^{r-1},                           \tag{7.1}
\]

and enlarge the leaf-rotation graph by every \(\mathcal H_r\)-conjugate of
every leaf edge.

For \(w\in D_r\), retain the first and last steps separately and encode the
remaining adjacent pairs by

\[
 s_i(w)=w_{2i}+w_{2i+1}-1\in\{-1,0,1\},
       \qquad1\le i<r.                                  \tag{7.2}
\]

Write \(D,L,U\) for the values \(-1,0,1\), respectively.

### Lemma 7.1 (Motzkin quotient)

The word

\[
                         M(w)=s_1(w)\cdots s_{r-1}(w)   \tag{7.3}
\]

is a Motzkin path of length \(r-1\).  Two Dyck words are in the same
\(\mathcal H_r\)-orbit if and only if they have the same Motzkin path.

#### Proof

After the initial up-step, the height is one.  Each pair in (7.2) changes
the height by \(2s_i\).  Just before the final down-step the height is again
one.  Dividing the odd heights minus one by two gives a nonnegative walk
starting and ending at zero.

The group \(\mathcal H_r\) fixes pairs 00 and 11 and independently
exchanges the two orientations 01 and 10 of every level pair.  Both
orientations remain Dyck because a pair begins at an odd positive height.
Thus every orientation in one Motzkin fibre occurs, and no generator
changes that fibre. \(\square\)

Orient the abstract leaf rule as

\[
                         1100\longrightarrow1010.       \tag{7.4}
\]

For an obstruction it is harmless to allow (7.4) at every occurrence in a
Dyck word, not only at literal tree-context roots.

### Lemma 7.2 (quotient action of a conjugated leaf edge)

On Motzkin paths, a leaf edge or any of its
\(\mathcal H_r\)-conjugates either acts trivially or has the form

\[
                              UD\longleftrightarrow LL. \tag{7.5}
\]

#### Proof

If the four changed bits start at an even position, they are exactly two
pairs from (7.2), and

\[
                         11\,00\longleftrightarrow10\,10
\]

is (7.5).  If they start at an odd position, the middle full pair changes
orientation 10 to 01 while the sums of it and of the two boundary pairs
remain fixed.  The Motzkin word is then unchanged.  Conjugation by
\(\mathcal H_r\) changes only level-pair orientations. \(\square\)

For a Motzkin path \(M\), let \(\operatorname{nf}(M)\) be obtained by
repeatedly replacing every adjacent peak \(UD\) by \(LL\).

### Theorem 7.3 (peak-erasure obstruction)

The rewrite \(UD\to LL\) is terminating and confluent.  Hence

\[
                         \boxed{\operatorname{nf}(M(w))}
                                                               \tag{7.6}
\]

is invariant under all leaf rotations and all their
\(\mathcal H_r\)-conjugates.  The generated graph is disconnected for
every \(r\ge4\); for \(r=3\), its Motzkin quotient is connected.

#### Proof

Every forward rewrite reduces the number of \(U\)-steps.  Two occurrences
of \(UD\) cannot overlap, and replacing one by \(LL\) creates no new
\(UD\) across either boundary.  Thus all reductions commute and end in one
peak-free normal form.  Lemma 7.2 proves invariance.

For \(r\ge4\), the two valid Motzkin paths

\[
                      L^{\,r-1},
             \qquad U L^{\,r-3}D                       \tag{7.7}
\]

are already peak-free and distinct.  Lemma 7.1 supplies Dyck words above
both.  For \(r=3\), the only length-two Motzkin paths are \(LL\) and
\(UD\), which (7.5) joins. \(\square\)

Thus root-scale even-pair conjugation explains why the size-three
pentagon escapes the leaf normal form, but it still cannot furnish the
all-\(r\) conveyor.  A successful new packet must change the peak-free
Motzkin skeleton, for example by moving a level step past an unmatched
\(U\) or \(D\).

## 8. Arbitrary common contexts still do not give a full conveyor

The qualification left open in Section 6 can in fact be settled.  A
one-hole context built from

\[
                 x\mapsto Ax,\qquad x\mapsto xB,\qquad
                 x\mapsto 1x0                              \tag{8.1}
\]

always retains the hole word as a contiguous factor.  Consequently every
common-context use of the rooted pentagon replaces one contiguous Dyck
factor of semilength three by another such factor.  This elementary
observation supplies isolated vertices at every larger size.

### Theorem 8.1 (full common-context obstruction)

Let \(\mathscr G^{(3),\mathrm{ctx}}_r\) be the graph on \(D_r\) generated
by all common-context installations of the rooted five-row packet of
Theorem 3.1.  Equivalently, an edge may replace one of the five Dyck words
of length six by another one inside any context generated by (8.1).
Then \(\mathscr G^{(3),\mathrm{ctx}}_r\) is disconnected for every
\(r\ge4\).  More precisely, it has an isolated vertex.

#### Proof

Every operation in (8.1) keeps its argument as a contiguous subword.
Hence a word which has no contiguous Dyck factor of length six is incident
with no rooted-pentagon move.

For even \(r=2k\), \(k\ge2\), take

\[
                         a_{2k}=(1100)^k .                \tag{8.2}
\]

The four length-six factors of the bi-infinite periodic word
\((1100)^\infty\), according to their starting residue, are

\[
        110011,\qquad100110,\qquad001100,\qquad011001.    \tag{8.3}
\]

The first is not balanced; the second is balanced but falls below its
initial height at its third step; and the last two begin with a down-step
(the third is also unbalanced).  Thus none is a Dyck word, and (8.2) has
no eligible factor.

For odd \(r=2k+1\), \(k\ge2\), take

\[
                         a_{2k+1}=1(1100)^k0 .             \tag{8.4}
\]

Every length-six factor wholly inside the periodic core is covered by
(8.3).  The unique factor meeting the initial added step is \(111001\),
which is unbalanced, and the unique factor meeting the final added step is
\(011000\), which is not a Dyck word.  Hence (8.4) also has no eligible
factor.

Both (8.2) and (8.4) are Dyck words.  They are isolated vertices, while
\(|D_r|>1\), proving disconnection. \(\square\)

Thus the rooted pentagon really does cross the leaf and even-pair
normal-form obstructions, but a *bounded size-three packet library* still
cannot be an all-Catalan conveyor, even when every arbitrary common
one-hole context is allowed.  Any successful conveyor must include rooted
packets of other (in particular, unbounded) hole sizes, or a collective
operation which is not supported on one contiguous bounded-size Dyck
factor.
