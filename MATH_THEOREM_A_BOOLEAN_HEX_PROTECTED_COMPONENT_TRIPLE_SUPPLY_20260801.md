# Protected Boolean-hex cycle triples: normalized two-sum lift and exact supply criteria

**Date:** 2026-08-01  
**Status:** exact local normalized lift, exact protected cut/topology
composition, and elementary near-perfect component-triple matching theorems.
The required dense decorated packet bank is not constructed.

## 0. Verdict

The ternary Boolean hex resolves the **algebraic** part of the protected
two-sum condition.  Under its natural depth-three decoration, the three
changed head-root rows have

* one normalized resource deck fixed pointwise;
* the other normalized resource deck permuted by a three-cycle; and
* the normalized \(z\)-deck permuted by a three-cycle.

Thus, whenever the three moved bottom necklace classes are distinct, the
hex is a primitive normalized resource-zero triple.  If one changed row is
an external puncture for a Hall shore and the other two rows are protected
exterior rows, their deltas automatically provide the required negative
two-sum.  At the same time, if the three old central edges lie on three
distinct directed cycles, the same packet merges those cycles into one.

Raw central applicability is not enough.  A usable packet must be decorated
with literal flag options, functional attachment/alignment phases, an
external puncture, and all downstream guards.  The correct global object is
therefore a **list-coloured three-uniform hypergraph on current cycle
components**.  Literal packet multiplicity must first be collapsed to
component triples.

Two exact supply theorems are proved below.

1. If the collapsed certified triple hypergraph has independence number
   \(a\), any maximal matching leaves at most \(a\) components.
   Equivalently, if only \(o(c^3)\) of the \(\binom c3\) component triples
   lack a certified packet, a matching covers \(c-o(c)\) components.
2. If every selected component triple has at least \(L\) literal
   certificates, each certificate uses at most \(b\) auxiliary tokens, and
   one token occurs in at most \(\lambda\) certificates of any one list,
   then

   \[
                          L>b\lambda(c/3)
   \]

   is sufficient to choose compatible literal certificates along the
   component matching.

These hypotheses give one-round contraction

\[
                         c'={c+2r\over3},
\]

where \(r\) is the uncovered component count.  Hereditary regeneration
gives logarithmically many rounds.  Minimum list size or minimum component
degree alone is insufficient: already on six cycles, all triples through
one common hub have minimum degree four but matching number one.

The remaining theorem is exactly a **decorated collapsed-link expansion**
statement.  The central hex supplies the two-sum once a decorated occurrence
exists; it does not supply the occurrence distribution, fixed
\(\vartheta/\zeta\) compatibility, exterior chronology, or the simultaneous
all-cut Hall inequalities.

## 1. The normalized one-sided cubic carried by a Boolean hex

Work additively in the cyclic ground set and write \(X-t\) for translation
of every element of \(X\) by \(-t\).  Write \(K_0+x\) for
\(K_0\cup\{x\}\).  Choose

\[
 |K_0|=m-3
\]

and five distinct coordinates \(w,a,b,c,d\) outside \(K_0\).  Put
\(S_0=K_0+w\).  The six middle roots of the Boolean hex are

\[
\begin{array}{lll}
 A=S_0+a+d,&B=S_0+a+c,&C=S_0+c+d,\\
 D=S_0+b+c,&E=S_0+b+d,&F=S_0+a+b.
\end{array}                                                \tag{1.1}
\]

Its old and new directed phases are

\[
 {\cal O}=\{A\to B,\ C\to D,\ E\to F\},\qquad
 {\cal N}=\{A\to F,\ C\to B,\ E\to D\}.                    \tag{1.2}
\]

The changed head roots are \(B,D,F\).  The natural normalized old/new
row options at these roots are

\[
\begin{array}{c|cc}
 &f_R^-&f_R^+\\ \hline
B&((K_0+c)-a,\ w-a)&((K_0+a)-c,\ w-c)\\
D&((K_0+b)-c,\ w-c)&((K_0+c)-b,\ w-b)\\
F&((K_0+a)-b,\ w-b)&((K_0+b)-a,\ w-a).
\end{array}                                                \tag{1.3}
\]

Each entry is in normalized form \((S,z)\).

### Theorem 1.1 (hex-to-normalized resource identity)

Every option in (1.3) is rooted at its displayed root.  Its normalized
\(P=[S+0]\) deck is fixed pointwise:

\[
\begin{array}{c|ccc}
R&B&D&F\\ \hline
P(f_R^-)=P(f_R^+)&[K_0+a+c]&[K_0+b+c]&[K_0+a+b].
\end{array}                                                \tag{1.4}
\]

The \(T=[S]\) deck changes by the three-cycle

\[
 ([K_0+c],[K_0+b],[K_0+a])
       \longmapsto
 ([K_0+a],[K_0+c],[K_0+b]),                                \tag{1.5}
\]

and the \(z\)-deck changes by

\[
 (w-a,w-c,w-b)\longmapsto(w-c,w-b,w-a).                    \tag{1.6}
\]

Consequently the simultaneous change at \(B,D,F\) is resource zero in the
two normalized decks, and also on the \(z\)-augmented balance face.  It is
primitive in the two-deck ledger if and only if

\[
                [K_0+a],\ [K_0+b],\ [K_0+c]                \tag{1.7}
\]

are pairwise distinct necklace classes.

#### Proof

For the first old option, translating its normalized root by \(a\) gives

\[
 ((K_0+c)-a)+\{0,w-a\}+a=K_0+w+a+c=B.
\]

Translating the first new root by \(c\) gives the same set.  The other four
root identities are identical with the displayed letters permuted.

For \(B\), translating the old \(P\)-set by \(a\) and the new \(P\)-set
by \(c\) gives \(K_0+a+c\) in both cases.  The calculations at \(D,F\)
give (1.4).  Translation invariance of necklace labels gives (1.5)
directly from the six bottom sets in (1.3), and (1.6) is literal.

Thus both occurrence multisets are unchanged.  The row at \(B\) has
nonzero two-deck delta exactly when \([K_0+c]\ne[K_0+a]\), and similarly
at \(D,F\).  All three row deltas are nonzero exactly under (1.7).
The normalized three-row criterion then gives primitivity. \(\square\)

The packet is a one-sided Latin cubic: the \(P\)-permutation is the
identity and the \(T\)-permutation is a three-cycle.  It is not restricted
to the particular two-cross display used as one sufficient example in the
protected two-sum theorem.

Theorem 1.1 is an algebraic decoration statement.  A physical application
must still verify that the old and new flag options belong to the actual
root menus and that both phases are literal chronology transitions.  A
permutation of the \(z\)-deck preserves only its histogram; a frozen
headwise alignment additionally requires each new option to retain its
prescribed alignment.

## 2. A packet which repairs one Hall shore and fuses three cycles

Let \(M\) be an exact four-resource factor and let
\({\cal C}(M)\) be its directed cycle components.  Fix a functional
attachment \(\vartheta\), a selected normalized table \(F\), and a head
shore \(Y\).  Put

\[
                         K_Y=N_F(Y).                         \tag{2.1}
\]

An occurrence-labelled Boolean hex \(h\) includes its coordinate data,
orientation, physical phases, the common tail-row decorations at \(A,C,E\),
the old/new head-row decorations at \(B,D,F\), and any required external
guard choices.  Write

\[
 \kappa(h)=\{C_1,C_2,C_3\}\subseteq{\cal C}(M)              \tag{2.2}
\]

for the three components containing the old edges in (1.2), and put

\[
                         R(h)=\{B,D,F\}.                     \tag{2.3}
\]

Call \(h\) a **\(Y\)-protected fusion certificate** if:

1. the three old atoms belong to \(M\) and lie on three distinct directed
   cycles;
2. the baseline selected table satisfies

   \[
             F_B=f_B^-,\qquad F_D=f_D^-,\qquad F_F=f_F^-,
                                                               \tag{2.3a}
   \]

   while the declared rows at \(A,C,E\) are unchanged by the toggle; the
   six old/new normalized options in (1.3) are allowed, (1.7) holds, and
   every arc of both \({\cal O}\) and \({\cal N}\) passes the exact literal
   turn predicate against those declared tail and head rows;
3. the functional attachment sends \(B,D,F\) to the three literal central
   owner orbits/phases of the forward hex, and both \(f_R^-\) and \(f_R^+\)
   pass the fixed \(\vartheta\) and, when present, prescribed
   \(\zeta(R)\) compatibility tests;
4.

   \[
                         R(h)\cap(K_Y\cup Y)=\varnothing;    \tag{2.4}
   \]

5. for at least one \(r\in R(h)\), the new option \(f_r^+\) is a punctured
   predecessor of some head in \(Y\); and
6. every additional occurrence, residence, upper, or compiler guard
   declared by the application is satisfied.

The service set

\[
 \Lambda_Y(h)=
 \{r\in R(h):f_r^+\text{ is a punctured predecessor of }Y\} \tag{2.5}
\]

is nonempty by definition.

### Theorem 2.1 (protected fusion actuator)

Toggling a \(Y\)-protected fusion certificate:

1. preserves the exact central lower, upper, tail, and head resources;
2. is a primitive normalized resource-zero support-three circuit;
3. has

   \[
                         \kappa_h(Y)\ge1;                    \tag{2.6}
   \]

4. merges the three components in \(\kappa(h)\) into one directed cycle;
   and therefore
5. decreases the cycle count by exactly two.

#### Proof

Central four-resource preservation and the three-cycle fusion are the
Boolean-hex identities.  Theorem 1.1 and (1.7) give a primitive normalized
resource circuit.  Choose \(r\in\Lambda_Y(h)\).  By (2.4),
\(r\notin K_Y\), so the new punctured edge makes \(r\) a new distinct
neighbour of \(Y\).

Every changed root lies outside \(K_Y\cup Y\).  An old edge from
\(K_Y\) into \(Y\) depends only on its tail and head endpoint rows, neither
of which changes.  Hence no old neighbour is lost.  The other two hex
deltas automatically sum to the negative of the anchor delta by Theorem
1.1.  This is precisely the protected two-sum argument and proves (2.6).
\(\square\)

The protected exterior condition is sufficient, not necessary.  A hex with
a changed head in \(Y\) can also improve the cut, but then added and lost
neighbours must be evaluated by the full cut formula rather than by
Theorem 2.1.

Component disjointness and cut exteriority are different conditions:
\(\kappa(h)\) concerns the three old central edges, while \(R(h)\) concerns
the changed normalized head rows.  Neither one implies the other.

## 3. The collapsed certified component hypergraph

Let

\[
                         c=|{\cal C}(M)|.
\]

For every component triple \(e\in\binom{{\cal C}(M)}3\), let
\({\cal L}_Y(e)\) be the set of all occurrence-labelled \(Y\)-protected
fusion certificates with footprint \(e\).  Different coordinate choices,
flag decorations, rotations, and phases remain different list members.

For an integer \(L\ge1\), define the **collapsed threshold hypergraph**

\[
 {\cal H}_{Y,L}=
 \left\{e\in\binom{{\cal C}(M)}3:|{\cal L}_Y(e)|\ge L\right\}.
                                                               \tag{3.1}
\]

This collapse is essential.  A million literal certificates on one
component triple still provide only one vertex-disjoint triple choice.

### Theorem 3.1 (hereditary expansion gives a near-perfect triple matching)

Let \(a=\alpha({\cal H}_{Y,L})\) be the largest number of components
spanning no certified triple.  Then every maximal matching in
\({\cal H}_{Y,L}\) leaves at most \(a\) components uncovered.

Equivalently, if every component set of size greater than \(a\) contains
one certified triple, there is a component-triple matching covering at
least \(c-a\) components.

#### Proof

The uncovered vertices of a maximal hypergraph matching span no hyperedge:
otherwise that edge could be added.  They therefore form an independent
set and have size at most \(a\). \(\square\)

There are two useful exact numerical versions.

### Corollary 3.2 (global missing-triple load)

Put

\[
 B_3=\binom c3-|E({\cal H}_{Y,L})|.                         \tag{3.2}
\]

If a maximal matching leaves \(r\) components, then

\[
                         \binom r3\le B_3.                   \tag{3.3}
\]

In particular \(B_3=o(c^3)\) implies \(r=o(c)\), while \(B_3=0\) implies
\(r\le2\).

#### Proof

Every triple inside the uncovered independent set is absent from
\({\cal H}_{Y,L}\), giving (3.3). \(\square\)

### Corollary 3.3 (local link-complement load)

For a component \(C\), let \(\operatorname{Lk}(C)\) be the graph on the
other \(c-1\) components in which \(C_1C_2\) is an edge exactly when
\(\{C,C_1,C_2\}\in{\cal H}_{Y,L}\).  Put

\[
 B_2=\max_C
 \left(\binom{c-1}{2}-|E(\operatorname{Lk}(C))|\right).      \tag{3.4}
\]

If a maximal matching leaves \(r>0\) components, then

\[
                         \binom{r-1}{2}\le B_2.              \tag{3.5}
\]

Consequently \(B_2=o(c^2)\) implies \(r=o(c)\), and \(B_2=0\) implies
\(r\le2\).

#### Proof

Choose an uncovered component \(C\).  The other \(r-1\) uncovered
components form an independent set in \(\operatorname{Lk}(C)\), so all
their pairs are missing link edges. \(\square\)

Corollaries 3.2--3.3 are deterministic expansion theorems.  They need no
independence assumption on the generation of the certificates and do not
count literal multiplicity as component expansion.

## 4. Lifting a component matching to compatible literal packets

Component-disjoint old phases have disjoint central four-resource supports,
but decorated certificates can still conflict through exterior phase,
guard, cap, or compiler tokens.  Let \(Q(h)\) be a set of auxiliary
capacity-one tokens witnessing all such extra conflicts.  Assume

\[
                         |Q(h)|\le b                         \tag{4.1}
\]

for every retained certificate, and define the within-list token load

\[
 \lambda=
 \max_{e,q}
 |\{h\in{\cal L}_Y(e):q\in Q(h)\}|.                         \tag{4.2}
\]

### Theorem 4.1 (literal list-load lift)

Let \({\cal M}\) be a matching of \(s\) component triples in
\({\cal H}_{Y,L}\).  If

\[
                         L>b\lambda(s-1),                    \tag{4.3}
\]

then one can select a literal certificate from every list indexed by
\({\cal M}\) so that all selected auxiliary token sets are pairwise
disjoint.

It is sufficient to impose the census-level inequality

\[
                         L>b\lambda c/3.                     \tag{4.4}
\]

#### Proof

Order the \(s\) triple lists arbitrarily.  Before the \(j\)-th choice, the
previous certificates use at most \(b(j-1)\) tokens.  Each such token
forbids at most \(\lambda\) members of the current list.  Thus fewer than
\(b(j-1)\lambda<L\) members are forbidden, and a choice remains.
\(\square\)

The theorem assumes every cross-certificate conflict outside the disjoint
component footprints is witnessed by a token in \(Q(h)\).  Without that
complete conflict catalogue, (4.3) is not a physical compatibility test.

## 5. Combined contraction and cut gain

### Theorem 5.1 (one-round protected ternary supply)

Assume the hypotheses of Sections 2--4 for one common Hall shore \(Y\).
Let a component matching cover \(c-r\) cycles and let

\[
                         s={c-r\over3}.                      \tag{5.1}
\]

After choosing compatible literal certificates by Theorem 4.1 and toggling
them in parallel:

\[
                         c'=c-2s={c+2r\over3},               \tag{5.2}
\]

all four central resource inventories and the normalized static resource
ledger remain exact, and

\[
                         \kappa_{\rm total}(Y)\ge s.         \tag{5.3}
\]

In particular, either \(B_3=o(c^3)\) or \(B_2=o(c^2)\), together with
(4.4), gives

\[
                         c'=\left({1\over3}+o(1)\right)c.    \tag{5.4}
\]

If \(B_3=0\) or \(B_2=0\), at most two components are unmatched in the
round.

#### Proof

The selected component footprints and auxiliary tokens are disjoint, so
the packet toggles commute.  Every packet replaces three cycles by one and
preserves its resource inventories.  This gives (5.2).

For the common shore \(Y\), every certificate retains all old neighbours
and adds a neighbour at one of its changed roots.  Disjoint component
footprints make all changed roots, and hence all chosen anchors, distinct.
Thus no added neighbour is counted twice and (5.3) follows.  The remaining
claims are Corollaries 3.2--3.3. \(\square\)

The parity of \(c\) is unchanged, since every packet changes the cycle
count by two.

Positive gain on one old Hall shore is not by itself a common-matching
gain.  The final union of packets must still satisfy the all-cut
inequalities

\[
 \kappa(Y')\ge |Y'|-|N_F(Y')|-D+a
 \qquad\text{for every head shore }Y'                      \tag{5.5}
\]

to raise the matching by \(a\).

### Corollary 5.2 (regenerative contraction)

If the same collapsed-expansion and literal list-load hypotheses hold after
each nonterminal round, with uncovered fraction \(o(1)\), then

\[
                         c_{t+1}=
                   \left({1\over3}+o(1)\right)c_t.           \tag{5.6}
\]

Thus \(O(\log c_0)\) rounds reduce the cycle count to the scale at which the
hypotheses stop or a bounded terminal absorber applies.  Reaching one or
two cycles requires either the corresponding terminal-strength expansion
or a separate bounded sidecar; near-perfect supply alone does not imply it.

## 6. Why list size and minimum degree are insufficient

The list threshold in (3.1) does not help if its supported component triples
all pass through a small hub set.

### Proposition 6.1 (sharp common-hub obstruction)

Let \(c=3q+s\), where \(s\in\{0,1,2\}\), and let
\(A\subseteq V\) have size \(q-1\).  Define

\[
 {\cal H}_A=\{e\in\binom V3:e\cap A\ne\varnothing\}.         \tag{6.1}
\]

Then

\[
                         \nu({\cal H}_A)=q-1,                \tag{6.2}
\]

so every component-triple matching leaves at least \(s+3\) components, and
a maximum matching leaves exactly \(s+3\).  Moreover \({\cal H}_A\) is
edge-maximal subject to \(\nu<q\): adding any one missing triple raises the
matching number to \(q\).  Nevertheless its minimum vertex degree is

\[
 \delta_1({\cal H}_A)
 =\binom{c-1}{2}-\binom{c-q}{2},                            \tag{6.3}
\]

which is asymptotic to \((5/9)\binom c2\).

The smallest nonempty instance has \(c=6\): take all ten triples through
one hub.  The hub has degree ten, every other component has degree four,
but the matching number is one and three cycles remain.

#### Proof

Every hyperedge meets \(A\), so a matching uses at most one edge per member
of \(A\), proving \(\nu\le q-1\).  There are

\[
 |V-A|=2q+s+1\ge2(q-1)
\]

nonhub vertices, so match each \(a\in A\) to two private nonhub vertices;
this proves equality in (6.2).  A nonhub vertex lies in every triple
through it except those whose two other vertices also lie in \(V-A\).
This gives (6.3); hub vertices have the larger degree
\(\binom{c-1}{2}\).

Every missing triple \(e\) lies wholly in \(V-A\).  After selecting \(e\),
the remaining nonhub set has

\[
 |V-A-e|=2q+s-2\ge2(q-1)
\]

vertices, so each member of \(A\) can be matched to two private remaining
nonhub vertices.  Together with \(e\), these edges form a \(q\)-matching.
This proves edge-maximality. \(\square\)

Arbitrarily many literal certificates may be placed on every edge of
\({\cal H}_A\) without changing (6.2).  Hence neither raw certificate
count, minimum list size, nor a positive-density minimum component degree
forces a near-perfect contraction; this example has asymptotic minimum
degree \((5/9)\binom c2\).  This is a sharp common-hub obstruction, not a
claim about the global optimal minimum-degree threshold.  The collapsed
support must satisfy a
genuine no-large-independent-set, link-cover, codegree, or absorber
condition.

## 7. Exact remaining theorem

The prospective all-dimensional supply statement exposed by the new
actuator is:

> Jointly choose the exact four-resource factor and its depth-three flag
> decoration so that, after every bounded protected deletion and every
> prior contraction round, the collapsed hypergraph of
> occurrence-labelled \(Y\)-protected fusion certificates has
> \(B_3=o(c^3)\) or \(B_2=o(c^2)\), while its literal lists satisfy
> \(L>b\lambda c/3\).

Under this hypothesis, Theorems 4.1 and 5.1 give a near-perfect
component-triple matching and exact contraction.  The Boolean hex has made
the protected negative two-sum local and automatic; the remaining problem
is distribution and regeneration of **decorated** occurrences.

The following distinctions remain essential.

1. Three distinct central cycle components do not imply that the changed
   roots \(B,D,F\) lie outside a chosen Hall shore and its neighbourhood.
2. Central four-resource preservation does not imply fixed
   \(\vartheta/\zeta\) compatibility or preservation of external flag
   chronology.
3. A displayed new central edge can have its own general cut effect, but
   the protected theorem above uses only the exterior-puncture subclass.
4. Huge literal multiplicity on a few component triples is not component
   expansion.
5. Per-packet positivity for different Hall shores does not imply any
   one all-cut matching improvement.
6. The known hex-free near-factor construction proves that none of these
   supply properties follows from near-perfectness or high girth alone.

Thus the new central actuator closes the topology-plus-resource algebra,
but not the decorated component-triple supply theorem.
