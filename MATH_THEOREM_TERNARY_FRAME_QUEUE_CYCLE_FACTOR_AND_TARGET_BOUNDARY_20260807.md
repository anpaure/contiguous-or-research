# Ternary frames have an explicit positive-density queue cycle factor, but a fixed frame cannot carry a positive-density literal target factor

**Date:** 2026-08-07  
**Method:** a fixed partition into triples, a linear quotient of
\(\mathbb F_3^p\), and a sharp singleton-target obstruction  
**Status:** unconditional owner-only construction and exact scope boundary.
For every \(p\ge2\), each ternary owner frame has a phase-periodic,
q1-simple queue cycle factor covering more than one third of its owners.
If \(p\) is a power of three, the factor covers the entire frame, and this
divisibility condition is necessary for an all-cycle cover with the fixed
round-robin phase order.  Almost every middle owner belongs to a canonical
frame, so this gives an unconditional owner-disjoint queue bank of density
at least \(1/3-o(1)\).  The construction is q1-simple inside each frame,
not across different frames.  Moreover, the canonical literal realization
of one fixed frame has only \(3p\) possible bottom source letters.  Hence a
positive-density frame factor cannot simultaneously be a target-disjoint
literal factor.  The theorem solves the owner-only packing row and isolates
the remaining cross-frame palette/target recoupling.

## 1. Canonical ternary frames cover almost every middle owner

Use the odd merged-PBBS parameters

\[
 n=2m+1,\qquad p=d+1,\qquad c=m-2p,
\tag{1.1}
\]

and assume \(p=O(\sqrt n)\), as at the optimal triangular deadline.  Fix
once and for all a partition of all but at most two coordinates of \([n]\)
into ordered triples

\[
 \mathcal T=(T_1,\ldots,T_N),\qquad N=\lfloor n/3\rfloor.
\tag{1.2}
\]

For a middle owner \(X\in\binom{[n]}m\), call \(T_i\) a **two-triple**
when \(|X\cap T_i|=2\).  If \(X\) has at least \(p\) two-triples, let
\(J(X)\) be the first \(p\) such indices and put

\[
 K(X)=X\setminus\bigcup_{i\in J(X)}T_i.
\tag{1.3}
\]

Then \(|K(X)|=c\).  For a fixed signature \((J,K)\), write the selected
triples as

\[
 T_i=\{x_{i,0},x_{i,1},x_{i,2}\},\qquad 0\le i<p,
\tag{1.4}
\]

and define

\[
 O(e)=K\cup\bigcup_{i=0}^{p-1}
       \bigl(T_i\setminus\{x_{i,e_i}\}\bigr),
 \qquad e=(e_0,\ldots,e_{p-1})\in\mathbb F_3^p.
\tag{1.5}
\]

The set

\[
 \mathcal F(J,K)=\{O(e):e\in\mathbb F_3^p\}
\tag{1.6}
\]

is the ternary frame of \((J,K)\).

### Lemma 1.1 (canonical frame partition)

The good owners, namely those having at least \(p\) two-triples, are
partitioned by the frames (1.6).  Moreover,

\[
 \frac{\#\{X\in\binom{[n]}m:X\text{ is not good}\}}
      {\binom nm}
 =e^{-\Omega(n)}.
\tag{1.7}
\]

#### Proof

Changing the omitted element inside any selected triple leaves that triple
of type two and leaves the status of every unselected triple unchanged.
Consequently every member of (1.6) has the same first \(p\) two-triples
and the same outside set \(K\).  Conversely, these data recover the frame,
so the frames partition the good owners.

For (1.7), first choose every coordinate independently with probability
\(1/2\).  The number \(Y\) of two-triples is
\(\operatorname{Bin}(N,3/8)\).  Since \(p=O(\sqrt n)\) and
\(\mathbb EY=(3/8)N=\Theta(n)\), Chernoff's inequality gives

\[
 \Pr(Y<p)=e^{-\Omega(n)}.
\]

Conditioning the independent set to have size \(m\) produces the uniform
measure on \(\binom{[n]}m\), while
\(\Pr(\operatorname{Bin}(n,1/2)=m)=\Theta(n^{-1/2})\).  Dividing by this
conditioning probability preserves the bound \(e^{-\Omega(n)}\).
\(\square\)

## 2. A quotient construction inside one frame

Put

\[
 a=\lceil\log_3p\rceil,\qquad q=3^a,
\tag{2.1}
\]

so

\[
 p\le q<3p.
\tag{2.2}
\]

Let \(G=\mathbb F_3^a\).  Choose distinct elements

\[
 g_0,g_1,\ldots,g_{p-1}\in G
\tag{2.3}
\]

whose affine span is \(G\), order them cyclically, and put \(g_p=g_0\).
This is possible because \(p\ge a+1\).  Define

\[
 h_i=g_{i+1}-g_i\ne0,
 \qquad
 H:\mathbb F_3^p\longrightarrow G,quad H(e_i)=h_i,
\tag{2.4}
\]

where \(e_i\) now denotes the \(i\)-th standard basis vector.  The map
\(H\) is onto.  Let

\[
 B=\ker H,qquad
 v=e_0+\cdots+e_{p-1},\qquad
 w_i=e_0+\cdots+e_{i-1}\quad(0\le i\le p).
\tag{2.5}
\]

The telescoping sum in (2.4) gives

\[
 v\in B,qquad H(w_i)=g_i-g_0.
\tag{2.6}
\]

Thus the \(p\) cosets \(B+w_i\), \(0\le i<p\), are pairwise distinct.
Also

\[
 e_i\notin B
\tag{2.7}
\]

because \(H(e_i)=h_i\ne0\).

For every \(x\in B\) and \(0\le i<p\), put in the directed edge

\[
 x+w_i\longrightarrow x+w_{i+1}.
\tag{2.8}
\]

This increments omission coordinate \(i\) by one and no other coordinate.

### Theorem 2.1 (ternary-frame cycle factor)

The edges (2.8) form vertex-disjoint directed cycles of length \(3p\).
They cover exactly

\[
 p|B|=\frac pq,3^p
\tag{2.9}
\]

vertices of the frame.  In particular, the covered proportion is

\[
 \frac pq>\frac13.
\tag{2.10}
\]

There are \(|B|/3=3^{p-a-1}\) cycles.

#### Proof

The union of the selected vertices is

\[
 \mathcal U=\mathop{\dot\bigcup}_{i=0}^{p-1}(B+w_i).
\tag{2.11}
\]

Every vertex in \(B+w_i\) has the unique outgoing edge of phase \(i\).
For \(i>0\), it has the unique incoming edge of phase \(i-1\).  A vertex
\(x\in B\) has its incoming edge from \(x-v+w_{p-1}\), because
\(w_p=v\in B\).  Hence (2.8) is a directed cycle factor of \(\mathcal U\).

After one complete round of \(p\) phases, the boundary state \(x\in B\)
has become \(x+v\).  The nonzero vector \(v\) has order three.  Therefore
every orbit has three rounds and every cycle has length \(3p\).  Equations
(2.9)--(2.10) follow from \(|B|=3^p/q\). \(\square\)

### Corollary 2.2 (the exact cyclic divisibility boundary)

A phase-periodic cycle factor can cover all \(3^p\) vertices of a ternary
frame only if \(p\) is a power of three.  If \(p\) is a power of three,
the construction above covers the entire frame.

#### Proof

Every cycle whose edge phases advance cyclically through
\(0,1,\ldots,p-1\) has length divisible by \(p\).  An all-vertex cycle
factor would therefore imply \(p\mid3^p\), so \(p\) is a power of three.
Conversely, if \(p=3^a\), then \(q=p\), and (2.9) is \(3^p\).
\(\square\)

This necessity concerns cycle factors.  Exported endpoints remove the
divisibility obstruction for linear path factors; an all-vertex linear
factor with the additional literal conditions is not asserted here.

## 3. Literal queue realization

Map every omission state in a directed cycle through (1.5).  On the edge
of phase \(i\) which changes omission \(r\) to \(r+1\), insert the source
letter

\[
 A=K\cup\bigl(T_i\setminus\{x_{i,r+1}\}\bigr).
\tag{3.1}
\]

The last \(p\) inserted letters contain one current two-block from every
selected triple.  Their union is precisely the current owner (1.5).

### Theorem 3.1 (flatness, residence, q1 simplicity, and suffix ranks)

For the entire cycle factor in one fixed frame:

1. every \(p=d+1\) consecutive source letters have union rank \(m\);
2. the owners are distinct and consecutive owners are Johnson adjacent;
3. every selected-triple coordinate has an owner gap of exactly \(p\) and
   an owner run of exactly \(2p\), while every coordinate of \(K\) is
   permanent;
4. the immediate lower and upper owner colours are each simple across the
   whole selected factor;
5. every suffix of \(j\le p\) consecutive source letters has rank

   \[
   c+2j=m-2p+2j;
   \tag{3.2}
   \]

6. inside each individual \(3p\)-cycle, the proper suffix targets are
   distinct at every fixed depth \(1\le j<p\).

#### Proof

The flatness and rank formula follow because \(j\le p\) consecutive phases
are distinct, every active triple contributes two coordinates, and \(K\)
contributes \(c\).  An edge changes one omitted element in one triple, so
it exchanges exactly one owner coordinate.

After a full phase round the omission vector increases by \(v\).  Hence
each triple cycles through its three omitted elements.  Each omission lasts
\(p\) owner steps, giving gap \(p\) and complementary run \(2p\).

At an owner edge of phase \(i\), the lower colour has one element of
\(T_i\) and two elements of every other selected triple.  The upper colour
has all three elements of \(T_i\) and two elements of every other selected
triple.  Thus either colour identifies \(i\).  For two phase-\(i\) edges to
have the same upper colour, their omission states must agree outside
coordinate \(i\).  Their difference would then lie in

\[
 B\cap\langle e_i\rangle=\{0\}
\]

by (2.7), so the edges are identical.  The same argument applies to the
lower colour.  This proves q1 simplicity across all cycles in the frame.

Finally, for \(j<p\), a suffix target identifies its proper cyclic interval
of active phase triples.  On one fixed cycle that interval occurs in three
rounds, and all its omissions increase by one between rounds.  The three
targets are therefore distinct. \(\square\)

## 4. Global owner consequence

Apply Theorem 2.1 independently in every canonical good frame.  Different
frames contain disjoint owners by Lemma 1.1.

### Corollary 4.1 (unconditional fixed-density owner bank)

There is a collection of vertex-disjoint rank-two queue cycles covering

\[
 \left(\frac pq-e^{-\Omega(n)}\right)\binom nm
 >\left(\frac13-o(1)\right)\binom nm
\tag{4.1}
\]

middle owners.  In particular, the owner-only density is much larger than
the merged-PBBS reset density \(\theta\).

The q1 simplicity in Theorem 3.1 is a within-frame assertion.  A lower or
upper q1 colour can in principle be produced by edges in two different
canonical frames.  Thus (4.1) is an owner-only factor, not yet a global
owner/q1 common factor.

## 5. Exact target obstruction inside a fixed frame

Allow arbitrary nonstationary changes of the omitted symbols at the
round-robin phase updates, but retain the canonical source rule (3.1).
The possible rank-\(c+2\) singleton source targets in one frame are exactly

\[
 \mathcal A_1(J,K)=
 \left\{
 K\cup(T_i\setminus\{x\}):0\le i<p,\ x\in T_i
 \right\}.
\tag{5.1}
\]

Hence

\[
 |\mathcal A_1(J,K)|=3p.
\tag{5.2}
\]

### Theorem 5.1 (fixed-frame literal target no-go)

Any collection of canonical queue source positions in one fixed frame
whose rank-\(c+2\) singleton targets are pairwise distinct has at most
\(3p\) positions.  Consequently:

* a target-disjoint cycle bank in one frame covers at most \(3p\) owners;
* more generally, a target-disjoint linear path bank with \(C\) exported
  initial endpoints covers at most \(3p+C\) owner vertices.

In particular, if \(C=o(3^p)\), no such bank covers a fixed positive
fraction of the frame.

#### Proof

Every source position is one of the \(3p\) sets in (5.1), so injectivity at
the singleton row gives the first assertion.  A cycle has equally many
source positions and owner vertices.  A union of \(C\) linear paths has at
most one more owner vertex than source transition per component, giving
the second assertion. \(\square\)

Thus allowing the omitted symbols to change arbitrarily does not solve the
named-target row inside a fixed ternary frame: the obstruction already
occurs at depth one.  One must vary the literal base/core realization,
assign the lower targets in a second stage, or correlate several frames.

## 6. Exact proof boundary

The ternary-frame idea settles a substantial part of the growing-
uniformity problem without invoking a hypergraph matching theorem:

\[
 \boxed{
 \text{owner-only queue density at least }1/3-o(1),
 \text{ with an explicit local q1-simple cycle factor}.}
\]

It also identifies why this does not yet prove the rank-two rolling
block-factor theorem:

1. q1 colours are simple inside a frame but not proved disjoint between
   different frames;
2. all cycles in one frame reuse the same \(3p\) bottom source targets;
3. global fusion and the residual PBBS compiler remain occurrence-level
   conditions.

The next useful construction must therefore preserve the ternary quotient
factor on owners while changing the literal source/core labels from cycle
to cycle, or prove a cross-frame common matching which selects q1 colours
and lower chains after the owner factor is fixed.
