# The endpoint port-word reduction for the extremal (k=11) branch

Date: 2026-07-25

## 1. Verdict

This note does **not** decide whether the length-(465) equality case exists.
It gives a new exact combinatorial reduction of the endpoint-ordered physical
problem, and it rules out a natural first-order parity attack on the forced
line-graph transitions.

In the six-component, zero-interface quotient subbranch

\[
E=132,\qquad V_Y=5\quad(Y\in\tbinom{[11]}4),
\]

used by the current exact certificate, the complete six-path object is
equivalently a pair of matchings in the
six-regular bipartite double cover of the odd graph.  In that model:

* the ordinary rank-four colours and complementary rank-seven colours are
  the turn colours on the two sides;
* the two local physical conditions become the two coordinate inequalities
  \(a_i\ne b_{i+1}\) and \(a_i\ne b_{i+2}\);
* every lower rank-four colour has multiplicity at most three;
* the inclusion-matching coordinate histogram \(42^{11}\) is automatic;
* the (126) forced star turns in the central line-graph quotient can always
  be chosen as a matching on the (330) central vertices.  Consequently
  neither parity in the five-regular design graph nor the number of forced
  star turns alone can force even one adjacent-star physical defect.

After the last theorem, the unresolved central ordering is exactly a rainbow
connector problem: concatenate (204) star segments by (202) distinct
\(K_4\)-colour transitions into two paths, while satisfying the port-word
inequalities and both (319)-support requirements.

## 2. The bipartite odd-graph double cover

Put \(\Omega=[11]\), and let \(\mathscr O\) be the bipartite graph with two
labelled copies of \(\binom\Omega5\):

\[
V_L=\{S_L:S\in\tbinom\Omega5\},\qquad
V_R=\{D_R:D\in\tbinom\Omega5\}.
\]

Join \(S_L\) to \(D_R\) when \(S\cap D=\varnothing\).  Every vertex has
degree six.  Give the edge the coordinate label

\[
\ell(S,D)=\text{the unique member of }\Omega\setminus(S\cup D).
\tag{2.1}
\]

Complementing a rank-six target \(U\) to \(D=\Omega\setminus U\) turns
the containment \(S\subset U\) into the edge \(S_LD_R\) of \(\mathscr O\).

### Theorem 2.1 (two-matching equivalence)

An endpoint-ordered spanning six-path quotient with four external and two
central target components is equivalent to a pair
\((M,N)\) with the following properties.

1. \(M\) is a perfect matching of \(\mathscr O\).
2. \(N\) is a matching of size \(456\).
3. \(M\cup N\) is the disjoint union of six alternating paths, each beginning
   on the left and ending on the right.
4. Along four components all right vertices lie in the external design
   \(\mathcal H\), and along two components all right vertices lie in
   \(\mathcal K=\binom\Omega5\setminus\mathcal H\).

The six unmatched left vertices of \(N\) are the root sources, and the six
unmatched right vertices are the terminal targets.

More generally, with \(c\) target-path components and \(d\) interfaces,
replace (456) by (462-c), replace six by (c), and allow the right-hand
sector to change exactly (d) times along the alternating components.  All
port identities below are unchanged.  The numerical (204/202) conclusion
in Section 6 specializes to the current (c=6,d=0) quotient.

#### Proof

Orient a target path from its root and write it uniquely as

\[
S_0,D_0,S_1,D_1,\ldots,S_{t-1},D_{t-1}.
\tag{2.2}
\]

Here \(S_i\) is the source assigned to the target
\(U_i=\Omega\setminus D_i\).  Thus \(S_i\cap D_i=\varnothing\), and the
edges \(S_iD_i\), over all six paths, form the perfect inclusion matching
\(M\).  For \(i<t-1\), the source \(S_{i+1}\) is the common rank-five
facet of \(U_i,U_{i+1}\), so it is disjoint from both \(D_i,D_{i+1}\).
The edges \(S_{i+1}D_i\) form \(N\).  Every nonroot source and every
nonterminal target occurs once in \(N\), proving the assertions.

Conversely, orient every alternating component of \(M\cup N\) from its
left endpoint.  Reading it as (2.2), the \(M\)-edge assigns each source to
one target and the \(N\)-edge makes the next source a facet of the preceding
target.  Hence consecutive targets are Johnson-adjacent and the original
six-path quotient is recovered.  The sector condition is exactly item 4.
\(\square\)

This reformulation removes the separately named inclusion matching: it is
just \(M\).  The target forest is the permutation/path structure produced by
the second matching \(N\).

## 3. Exact port words

On one component (2.2), define

\[
a_i=\ell(S_i,D_i)\quad(0\le i<t),
\qquad
b_i=\ell(S_{i+1},D_i)\quad(0\le i<t-1).
\tag{3.1}
\]

The alternating component therefore carries the coordinate port word

\[
a_0,b_0,a_1,b_1,\ldots,b_{t-2},a_{t-1}.
\tag{3.2}
\]

### Lemma 3.1 (state recurrences)

For every valid index,

\[
S_{i+1}=S_i-b_i+a_i,
\qquad
D_{i+1}=D_i-a_{i+1}+b_i.
\tag{3.3}
\]

Also

\[
a_i\ne b_i,
\qquad
a_i\ne b_{i-1}\quad(i\ge1).
\tag{3.4}
\]

#### Proof

The six-set \(\Omega\setminus D_i\) has the two distinct facets

\[
S_i=(\Omega\setminus D_i)-a_i,
\qquad
S_{i+1}=(\Omega\setminus D_i)-b_i.
\]

This proves the first recurrence and \(a_i\ne b_i\).  Similarly,
\(D_{i-1},D_i\) are distinct facets of \(\Omega\setminus S_i\), proving
the second recurrence and \(a_i\ne b_{i-1}\). \(\square\)

For \(0\le i<t-1\), put

\[
B_i=S_i\cap S_{i+1}.
\tag{3.5}
\]

These are the literal rank-four pair values.  For \(0\le i<t-2\), put

\[
A_i=B_i\cap B_{i+1}.
\tag{3.6}
\]

### Theorem 3.2 (physicality is a distance-three/five port rule)

One has

\[
B_i=(\Omega\setminus D_i)-\{a_i,b_i\}.
\tag{3.7}
\]

Moreover,

\[
B_i\ne B_{i+1}
\quad\Longleftrightarrow\quad
a_i\ne b_{i+1},
\tag{3.8}
\]

and, assuming the adjacent \(B\)'s are distinct,

\[
A_i\ne A_{i+1}
\quad\Longleftrightarrow\quad
a_i\ne b_{i+2}.
\tag{3.9}
\]

Thus the complete ordinary lower physical condition is exactly

\[
\boxed{
a_i\notin\{b_{i-1},b_i,b_{i+1},b_{i+2}\}
}
\tag{3.10}
\]

whenever the displayed indices exist; the first two exclusions in (3.10)
are automatic, and the last two are the actual physical constraints.

#### Proof

Equation (3.7) follows immediately from the two facet expressions in the
proof of Lemma 3.1.  From (3.3),

\[
\Omega\setminus D_{i+1}
=((\Omega\setminus D_i)-b_i)+a_{i+1},
\]

and hence

\[
B_{i+1}=(\Omega\setminus D_i)-\{b_i,b_{i+1}\}.
\tag{3.11}
\]

Both sides of (3.7) and (3.11) are four-subsets of the same six-set and
both omit \(b_i\).  They are equal exactly when \(a_i=b_{i+1}\), proving
(3.8).

If (3.8) holds, then \(A_i\) is the facet of \(B_{i+1}\) obtained by
deleting \(a_i\).  Applying (3.11) one index later shows that
\(A_{i+1}\) is the facet of the same \(B_{i+1}\) obtained by deleting
\(b_{i+2}\).  The facets are equal exactly when
\(a_i=b_{i+2}\).  This proves (3.9). \(\square\)

So the rank-three/rank-four physical reconstruction is not an opaque OR
condition.  A coordinate inserted at the source step labelled \(a_i\)
may not occur as a deletion port in either of the next two source steps.

## 4. Both shadow supports in the same model

The lower rank-four colour at the right turn \(D_i\) is (3.7).  The
complement of the upper rank-seven hull on the target transition
\(D_iD_{i+1}\) is

\[
Y_i=D_i\cap D_{i+1}=D_i-a_{i+1}.
\tag{4.1}
\]

Thus the two (319)-support requirements are precisely

\[
\left|\{B_i:\text{all six components}\}\right|\ge319,
\qquad
\left|\{Y_i:\text{all six components}\}\right|\ge319.
\tag{4.2}
\]

There are exactly

\[
\sum_j(t_j-1)=462-6=456
\]

occurrences in each ledger.

### Proposition 4.1 (physical lower multiplicity cap)

For every \(B\in\binom\Omega4\),

\[
\boxed{\#\{i:B_i=B\}\le3.}
\tag{4.3}
\]

#### Proof

If \(B_i=B\), the edge \(S_iS_{i+1}\) joins two of the seven five-sets

\[
B+x\qquad(x\in\Omega\setminus B).
\]

Every source occurs once in the six source paths.  If two \(B\)-coloured
edges shared a source, they would be consecutive there, contradicting
\(B_i\ne B_{i+1}\).  Hence the \(B\)-coloured edges form a matching on
seven vertices and have size at most three. \(\square\)

In particular, if \(n_j\) is the number of lower colours of multiplicity
\(j\), physicality and (4.2) force

\[
n_0+n_1+n_2+n_3=330,
\quad
n_1+2n_2+3n_3=456,
\quad
n_0\le11,
\tag{4.4}
\]

or equivalently

\[
n_2+2n_3=126+n_0.
\tag{4.5}
\]

This is an exact small-integer profile, not merely a support inequality.

## 5. The automatic coordinate ledger

### Proposition 5.1 (the (42^{11}) histogram)

For every perfect matching \(M\) of \(\mathscr O\), each coordinate occurs
as an \(M\)-edge label exactly (42) times:

\[
\#\{e\in M:\ell(e)=x\}=42\qquad(x\in\Omega).
\tag{5.1}
\]

#### Proof

Return to the uncomplemented target \(U=\Omega\setminus D\).  An
\(M\)-edge is an inclusion \(S\subset U\), and its label is the unique
element of \(U\setminus S\).  Among all six-sets, exactly
\(\binom{10}{5}=252\) contain (x); among all five-sets, exactly
\(\binom{10}{4}=210\) contain (x).  Since (M) is a bijection from all
five-sets to all six-sets by inclusion, exactly (252-210=42) matched
inclusions add (x). \(\square\)

There is an equally exact endpoint formula for the (N)-edge labels.  Let
\(r_x\) be the number of the six root (M)-edges labelled (x), and let
\(d_x^{\rm root},d_x^{\rm term}\) count root and terminal right-hand sets
containing (x).  If

\[
q_x=\#\{e\in N:\ell(e)=x\},
\]

then summing the second recurrence in (3.3) along all six paths gives

\[
\boxed{
q_x=42-r_x+d_x^{\rm term}-d_x^{\rm root}.
}
\tag{5.2}

Hence the coordinate marginals of the two matchings are already fixed up to
the twelve endpoints.  No contradiction can come from a large global label
imbalance.

The local inequalities alone also have no scalar scheduling obstruction.
For example, modulo (11), the periodic port template

\[
a_i=i,\qquad b_i=i+6
\tag{5.3}
\]

satisfies every exclusion in (3.10).  It is only a port-word template (its
sets repeat after eleven steps), but it shows that a proof must use the
set-valued matching geometry or the shadow colours, not just coordinate
frequencies and finite-distance avoidance.

## 6. The forced star turns have no first-order parity obstruction

In the design branch, identify the central target set
\(\mathcal K\) with the edge set of the five-regular design graph (G).
A central transition whose source colour is (v\in\mathcal H=V(G))
pairs two edges of (G) incident with (v).  Distinct source colours mean
that each (v) is used at most once.

The quotient forces (126) such star turns in the six-component certificate
(and at least (124) in the general ledger).  It is tempting to seek a
parity contradiction by claiming that so many turns must concatenate in
(L(G)).  The next theorem disproves that claim at the exact numerical
scale.

### Theorem 6.1 (disjoint star-pairing theorem)

Let (G) be any five-regular graph, and let (R\subseteq V(G)).  One can
choose two incident edges at every (v\in R) so that no edge of (G) is
chosen at both of its endpoints.

Equivalently, the corresponding star-clique transitions in (L(G)) form a
matching.

#### Proof

Form the incidence bipartite graph between two demand clones of every
vertex in (R) and the edges of (G), with the natural incidence
adjacency.  Give every edge-vertex capacity one.  The capacitated Hall
condition for (U\subseteq R) is

\[
|\{e\in E(G):e\cap U\ne\varnothing\}|\ge2|U|.
\tag{6.1}
\]

If (e_G(U)) is the number of internal edges, the left side is

\[
5|U|-e_G(U)\ge5|U|-\frac{5|U|}{2}
=\frac52|U|\ge2|U|.
\]

Thus the required (b)-matching exists.  Pair the two selected edges at
each (v).  Capacity one says that the resulting pairs are vertex-disjoint
in (L(G)). \(\square\)

### Corollary 6.2 (the exact residual connector count)

Take (|R|=126) in the (132)-vertex design graph.  The (126) star
turns can be chosen as (126) disjoint two-edge segments on the (330)
central vertices.  The other (78) central vertices are singleton
segments.  Hence there are

\[
126+78=204
\tag{6.2}
\]

segments.  Exactly (202) further transitions are needed to concatenate
them into two paths.

Those transitions must use (202) distinct colours in \(\mathcal K);
for a colour (S\in\mathcal K), the legal pair is any edge of its exact
(K_4(S)) class.  Therefore the remaining central gate, after satisfying
all forced star transitions with no local overlap at all, is:

> Choose (202) distinct (K_4)-colours that join the (204) star
> segments into two paths, while the resulting alternating port words obey
> (3.10), the lower (B)-support is at least (319), and the upper
> (Y)-support is at least (319).

This proves that the forced line-graph count, odd-degree parity of (G),
and distinctness of the (126) star colours do not themselves create a
physical defect.  Any successful obstruction must couple the (K_4)
connectors to the two turn-colour ledgers (or to the endpoint sectors).

## 7. Exact finite formulation

The physical endpoint problem in this branch can now be stated without OR
words or endpoint offsets.

Find matchings (M,N\subseteq E(\mathscr O)) such that:

1. (M) is perfect and (N) has size (456);
2. (M\cup N) consists of four ‎\(\mathcal H\)-right paths and two
   ‎\(\mathcal K\)-right paths;
3. the (456) lower turn colours (3.7) have support at least (319);
4. the (456) upper turn colours (4.1) have support at least (319);
5. the port word on every component satisfies (3.10);
6. in the central sector, at least (124) (and in the exact six-root
   quotient, (126)) (N/M)-transitions use distinct source colours from
   \(\mathcal H\), with all remaining transition colours also injective.

Every condition is a local matching, turn-colour, or path-component
condition in a six-regular bipartite graph.  Conversely, Theorems 2.1 and
3.2 reconstruct the complete ordinary rank-three through rank-seven
physical windows from any solution.

This is strictly smaller conceptually than the prior endpoint-offset model
for the six-component, zero-interface subbranch:
the only temporal variables are two matchings and the component order they
already induce.

## 8. Exact status

Proved here:

* the two-matching equivalence;
* the exact port recurrences;
* the equivalence of physical nonlaziness to (3.10);
* the two exact shadow-colour maps;
* the lower multiplicity-three cap and profile (4.4)--(4.5);
* the automatic (42^{11}) matching histogram and endpoint correction;
* the disjoint star-pairing theorem, showing that all (126) forced
  line-graph turns may be locally defect-free and mutually nonconsecutive;
* the resulting (204\)-segment/(202\)-connector residual problem.

Not proved here:

* existence of the (202)-colour connector forest with both shadow
  supports and (3.10);
* impossibility of that connector forest;
* a physical length-(465) word.

The useful negative conclusion is exact:

\[
\boxed{
\text{The forced (124/126) line-graph turns admit a completely disjoint
realization, so a parity or trail-count argument on (G) alone cannot
close the branch.}
}
\]
