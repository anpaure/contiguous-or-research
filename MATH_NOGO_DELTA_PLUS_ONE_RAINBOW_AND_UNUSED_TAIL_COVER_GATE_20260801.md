# The Delta-plus-one rainbow shortcut is false; the unused-tail cover is a dominating dual-base gate

**Date:** 2026-08-01  
**Status:** exact reduction of the corrected ordered-diamond selector and a
literature-backed no-go for the proposed generic rainbow theorem.  The
Boolean-specific rainbow selector and the Catalan-sized unused-tail cover
remain open.

## 0. Outcome

Fix an injection of every rank-`m+1` upper colour to a distinct containing
rank-`m` tail,

\[
 \psi:{\cal U}\longrightarrow{\cal O},\qquad
 T_R:=\psi(R)\subset R.                                  \tag{0.1}
\]

Write `a_R` for the unique element of `R-T_R`.  Every possible rooted
diamond continuation is indexed by `b in T_R`:

\[
 J(R,b)=T_R-b,\qquad V(R,b)=J(R,b)+a_R.                 \tag{0.2}
\]

For fixed `R`, the `m` pairs `(J(R,b),V(R,b))` form a matching between the
rank-`m-1` lower shore and the rank-`m` second-facet shore.  Colour these
`m` edges by `R`.

The exact corrected projection asks for a full rainbow matching: one edge
of every upper colour, with all `J` and all `V` distinct.  Its degrees obey

\[
                         \deg(V)\le m-1,qquad
                         \deg(J)\le m.                   \tag{0.3}
\]

If the unused tail bank covers every lower set, then also `deg(J)<=m-1`, so
each colour is a matching of size

\[
                         m=\Delta+1.                     \tag{0.4}

\]

That numerical condition does **not** imply a full rainbow matching.  A
2024 theorem of Wdowinski constructs, for every `Delta>=2`, a simple
bipartite graph of maximum degree `Delta` with a proper edge-colouring in
which every colour occurs on at least `Delta+1` edges but no full rainbow
matching exists.  Thus no generic properly-coloured-bipartite theorem can
close (0.2) from (0.4).  Any positive proof must use the extra Boolean
identity `V=J+a_R` and the containment labelling of the colours.

## 1. Exact degree ledger

### Proposition 1.1

In the coloured bipartite graph (0.2):

1. every colour class is a matching of order `m`;
2. every second-facet vertex has degree at most `m-1`;
3. every lower vertex has degree at most `m`;
4. a lower vertex `J` has degree `m` only if every owner `T superset J` is
   used by `psi`.

#### Proof

For fixed `R`, distinct choices of `b` give distinct sets `T_R-b` and
distinct sets `R-b`, proving the first statement.

A rank-`m` second facet `V` lies in exactly `m-1` rank-`m+1` upper sets on a
`2m-1` point ground.  Each such upper colour contributes at most one edge
to `V`, proving statement 2.

A rank-`m-1` set `J` has exactly `m` rank-`m` supersets.  Since `psi` uses
each tail at most once, each such tail contributes at most one candidate
edge at `J`.  This proves statements 3 and 4. \(\square\)

Let

\[
                         H={\cal O}\setminus\psi({\cal U}). \tag{1.1}

\]

Since

\[
 |H|=|{\cal O}|-|{\cal U}|=\operatorname {Cat}_m=:C,  \tag{1.2}

\]

the condition

\[
 \forall J\in{[2m-1]\choose m-1}\quad
 \exists T\in H\quad J\subset T                         \tag{1.3}

\]

reduces both vertex degrees to at most `m-1`.  This is exactly the proposed
unused-tail cover.

## 2. The generic rainbow implication is false

The proposed abstract implication was:

> In a properly edge-coloured bipartite graph of maximum degree `Delta`, if
> every colour class is a matching of size greater than `Delta`, then there
> is a full rainbow matching.

This statement is false.  Theorem 7(2) of

* Ronen Wdowinski, *Bounded degree graphs and hypergraphs with no full
  rainbow matchings*, arXiv:2401.06029 (2024),
  <https://arxiv.org/abs/2401.06029>

states that for every integer `Delta>=2` there is a **bipartite simple**
graph `G` of maximum degree `Delta` and a **proper** edge-colouring with

\[
                         |E_c|\ge\Delta+1                \tag{2.1}

\]

for every colour `c`, but with no full rainbow matching.

This matches every generic adjective available in (0.4): the host is
bipartite and simple, the colour classes are matchings, and their order is
strictly larger than maximum degree.  Consequently (0.3)--(0.4), by
themselves, cannot prove the ordered-diamond selector.

The standard general sufficient theorem of Aharoni--Berger--Meshulam uses
the much larger threshold `2 Delta` for graph edges; Wdowinski's paper also
shows the general bounded-degree threshold is essentially sharp.  Our
colour classes have only `Delta+1`, so that theorem is inapplicable.

The Wdowinski examples do not have the Boolean form (0.2).  Hence they do
not refute the desired Boolean selector; they refute only the proposed
degree-only proof.

## 3. The unused-tail cover is a domination problem

Condition (1.3) has two equivalent standard forms.

Taking complements, put

\[
 {cal F}=\{[2m-1]\setminus T:T\in H\}
 \subseteq {[2m-1]\choose m-1}.                         \tag{3.1}

\]

Then (1.3) says that every rank-`m-1` set is disjoint from some member of
`F`.  Thus `F` is a total dominating set of order `C` in the odd graph

\[
                         O_m=KG(2m-1,m-1).              \tag{3.2}

\]

Equivalently, `H` is a covering design with parameters

\[
                         (v,k,t)=(2m-1,m,m-1)           \tag{3.3}

\]

and exactly `Cat_m` blocks.

But an arbitrary such cover is still insufficient.  Because `H` is
required to be the **unused** tail bank of (0.1), its complement must admit
the upper-tail perfect matching.  The exact additional condition is

\[
 |\partial X\setminus H|\ge |X|
 \qquad(X\subseteq{[2m-1]\choose m+1}),                \tag{3.4}

\]

with the protected tail tickets contracted when the reset path is present.
In matroid language, `H` must be a dominating set whose complement is a
base of the upper-to-owner transversal matroid.  This is a correlated
**dominating dual-base** problem, not an ordinary covering design alone.

## 4. The canonical Catalan endpoint bank does not cover

The size `Cat_m` suggests taking the unmatched rank-`m` endpoints of the
standard Greene--Kleitman symmetric-chain matching.  In the usual binary
word model this is the ballot family

\[
 {cal H}_{\rm GK}=\{T:|T|=m,
 \text{ every prefix has at least as many members as nonmembers}\}.
                                                               \tag{4.1}

\]

It has order `Cat_m`, but for every `m>=3` it fails (1.3).  Let

\[
                         J_*=\{m+1,m+2,\ldots,2m-1\}.   \tag{4.2}

\]

Every rank-`m` superset of `J_*` adds exactly one point from `[m]`.  At the
prefix of length `m`, such a word has one member and `m-1` nonmembers, so
its prefix balance is `2-m<0`.  Therefore no member of `H_GK` contains
`J_*`.

Thus even the natural Catalan-sized dual-base candidate does not supply the
degree drop.  A successful bank must be noncanonical and must satisfy the
cover and transversal-base conditions jointly, while avoiding the protected
used tails.

## 5. Correct frontier

The proposed two-step shortcut

\[
 \text{Catalan cover }H
 \Longrightarrow \Delta\le m-1
 \Longrightarrow \text{full rainbow matching}          \tag{5.1}

\]

breaks at its second implication in general.

A viable positive theorem must instead prove one of:

1. a **Boolean rainbow theorem** for the special atoms
   `(T_R-b, T_R-b+a_R)`;
2. a direct common-basis/Rado construction that represents the lower and
   second-facet resources in one aligned matroid;
3. a stronger structured unused-tail bank for which the resulting coloured
   graph belongs to a rainbow-perfect subclass.

Even then, the partial incidence matching `J(R)->T_R` must extend to the
full predecessor matching and the selected owner arcs must be graphic
independent.  The degree ledger removes neither correlation automatically.
