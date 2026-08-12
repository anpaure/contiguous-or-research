# A \(B+1\) hub--residual Euler graft and the exact two-switch obstruction

**Date:** 2026-08-05  
**Method:** de Bruijn-state gluing and Boolean union algebra; no computation  
**Status:** unconditional lower-side \(B+1\) graft theorem under an exact
residual-factor hypothesis, plus an unconditional proof that a nontrivial
two-role colour-neutral fusion is impossible on the coatom-saturated
functional face.  Exact-\(B\) fusion therefore requires a cubic-or-higher
exchange or a noncoatom interface.

## 0. Outcome

The protected hub necklace can be rooted through any prescribed full
depth-\(d\) payload state.  If a residual stationary factor contains that
state, identifying the two copies joins the hub and residual supports into
one Euler component.

The price is exactly one duplicated role:

* one rank-\(r\) owner occurrence is repeated;
* one complete lower payload chain is repeated;
* no target is omitted; and
* no other owner or target is repeated.

Thus the lower factor has \(W+1\) owner occurrences and serializes at
physical length

\[
                         W+d+1=B(k)+1.                \tag{0.1}
\]

Trying to remove that repeated role by the obvious two-boundary
\(2\times2\) switch cannot work in the functional Boolean-union model.
Every nontrivial exact-\(B\) fusion on this face has support at least three.

## 1. Rooting the hub through a prescribed state

Let a full high-band payload chain be

\[
 B=S_1\subset S_2\subset\cdots\subset S_d\subset T,
 \qquad |S_q|=r-d+q-1,\quad |T|=r.                  \tag{1.1}
\]

Write

\[
 S_{q+1}-S_q=\{x_q\}\quad(1\le q<d),
 \qquad T-S_d=\{x_d\}.                               \tag{1.2}
\]

Thus its literal age state, up to the standard reversal of age order, is

\[
                         (B,\{x_1\},\ldots,\{x_d\}). \tag{1.3}
\]

### Lemma 1.1 (rooted hub aperture)

Let \(L>d+1\).  If

\[
                         L-(d+1)\le k-r,              \tag{1.4}
\]

there is a length-\(L\) literal hub necklace containing (1.1) as one of
its payload/owner roles.

#### Proof

Choose \(z_0\in B\), put

\[
                         K=B-\{z_0\},
\]

and place

\[
                         z_1=x_1,\ldots,z_d=x_d
\]

after \(z_0\) in the cyclic necklace.  These \(d+1\) labels, together with
\(K\), use exactly the owner \(T\).  By (1.4), choose the remaining
\(L-(d+1)\) cyclic labels fresh outside \(T\).

For the source letters \(A_t=K\cup\{z_t\}\), the chain starting at
\(z_0\) is exactly

\[
 B,\ B+x_1,\ldots,B+x_1+\cdots+x_{d-1},\
 B+x_1+\cdots+x_d=T.
\]

All other necklace properties follow from the coloured hub-necklace
theorem. \(\square\)

For the residue-reset choice

\[
                         L=2(d+1)+(W\bmod(d+1)),
\]

condition (1.4) holds for every sufficiently large \(k\).

## 2. Exact \(B+1\) Euler graft

We state the result in the functional rotor language.  A role consists of
one named rank-\(r\) owner and one named nested lower payload chain.  Its
literal trace is one directed arc between age states.

### Theorem 2.1 (one-shared-state graft)

Assume there are:

1. a connected integral stationary residual factor \(F\) with
   \(W-L+1\) role arcs;
2. a protected literal hub cycle \(C\) of length \(L\);
3. one full payload state \(h_*\) which occurs once in \(F\) and once in
   \(C\), with the two copies identified as the same age-state vertex;
4. disjoint owner and payload banks away from that role; and
5. owner and payload multisets satisfying

   \[
   \begin{array}{c|c}
   \text{resource}&\text{multiplicity in }F\cup C\\ \hline
   \text{one named owner }T_*&2\\
   \text{every other required owner}&1\\
   \text{every target in the chain }h_*&2\\
   \text{every other required lower target}&1.
   \end{array}                                       \tag{2.1}
   \]

Then \(F\cup C\) is one connected integral Eulerian state multigraph with
\(W+1\) role arcs.  It has no missing owner or lower target, and the
duplicates are exactly those displayed in (2.1).

#### Proof

Both \(F\) and \(C\) have zero boundary at every age state.  Their union is
therefore Eulerian.  Their supports are connected individually and meet at
\(h_*\), so the union support is connected.  It consequently has one Euler
tour.

All owner and payload multiplicities are hypotheses (4)--(5); identifying
the state vertices does not identify or delete either role arc.  Hence the
only repeated owner is \(T_*\), and the only repeated lower targets are the
members of the one chain \(h_*\).  Every required resource remains present.
\(\square\)

### Corollary 2.2 (lower-side \(B+1\) serialization)

Under the standard depth-\(d\) trace-to-source serialization, the Euler
tour of Theorem 2.1 serializes to a source of length

\[
                         (W+1)+d=B(k)+1.              \tag{2.2}
\]

Every strict-lower target is represented.  The extra physical position is
charged exactly to the duplicated role (2.1), whose at most \(d\) lower
cells are repetitions rather than omissions.

#### Proof

The Euler tour spells a cyclic source of \(W+1\) letters whose cyclic
length-\((d+1)\) traces are precisely the selected role arcs.  Cut the
cycle and append its first \(d\) source letters.  The resulting linear
source has length \(W+1+d\) and contains every cyclic trace once as an
ordinary interval.  Every target assigned inside a role trace is therefore
retained. \(\square\)

This is a lower-side theorem.  Residence, arbitrary upper witnesses, and
the final common cap must be included separately before it becomes a
universal OR-word theorem.

### Regenerative interpretation

For an additive theorem, it is enough to regenerate the following bounded
interface in every dimension:

* one full high-band payload state \(h_*\);
* one owner occurrence allowed to repeat;
* one protected opening socket; and
* the remaining upper/compiler guards.

The hub bank itself has size \(O(d)\), but its *physical excess* is one:
all its other roles replace ordinary owner roles.  Thus this interface is
compatible with a \(B(k)+1\) target and does not accumulate an
\(O(d)\)-length sidecar.

## 3. Why the exact-\(B\) two-boundary switch fails

Use the functional normal form.  A head role \(i\) has ordered state

\[
                         h_i=(A_{i,1},\ldots,A_{i,d})
\]

and top payload

\[
                         U_i=A_{i,1}\cup\cdots\cup A_{i,d},
 \qquad |U_i|=r-1.                                   \tag{3.1}
\]

An arc \(j\to i\) is legal when

\[
 (A_{j,2},\ldots,A_{j,d})
  =(A_{i,1},\ldots,A_{i,d-1}),                       \tag{3.2}
\]

and its owner colour is

\[
                         \kappa(j,i)=U_i\cup A_{j,1}.\tag{3.3}
\]

On the coatom-saturated face, \(A_{j,1}\) is a singleton, and legality of
the owner colour requires it to lie outside \(U_i\).

Take two selected arcs

\[
                         j\to i,\qquad \ell\to m.
\]

The two crossed arcs \(j\to m,\ell\to i\) exist only when the two head
prefixes in (3.2) agree.  Put

\[
                         A_{j,1}=\{x\},\qquad
                         A_{\ell,1}=\{y\}.            \tag{3.4}
\]

### Theorem 3.1 (no nontrivial colour-neutral \(2\times2\) fusion)

Assume:

1. all four original and crossed arcs are functional-state legal;
2. all four owner colours have rank \(r\);
3. \(U_i\) and \(U_m\) are distinct named rank-\((r-1)\) payloads; and
4. \(h_j\) and \(h_\ell\) are distinct named tail states.

Then

\[
 \{\!\{\kappa(j,i),\kappa(\ell,m)\}\!\}
 \ne
 \{\!\{\kappa(j,m),\kappa(\ell,i)\}\!\}.             \tag{3.5}
\]

Hence crossing two arcs cannot preserve the one-copy owner multiset.

#### Proof

Rank-\(r\) legality of all four arcs gives

\[
                         x,y\notin U_i\cup U_m.       \tag{3.6}
\]

Suppose the multisets in (3.5) were equal.  Substituting (3.3), this is

\[
 \{\!\{U_i+x,U_m+y\}\!\}
 =
 \{\!\{U_m+x,U_i+y\}\!\}.                            \tag{3.7}
\]

There are only two ways to match the two members of these multisets.
The direct matching gives

\[
                         U_i+x=U_m+x,
\]

and hence \(U_i=U_m\), contrary to hypothesis (3).  The crossed matching
gives

\[
                         U_i+x=U_i+y,
\]

and (3.6) forces \(x=y\).

But existence of both crossed arcs says that \(h_j\) and \(h_\ell\) have
the same final \(d-1\) blocks.  Together with \(x=y\), their first blocks
also agree, so \(h_j=h_\ell\), contrary to hypothesis (4).  This proves
(3.5). \(\square\)

### Corollary 3.2 (minimum support of an exact-\(B\) fusion)

On the distinct coatom/owner one-copy face, an exact fusion of a protected
hub component with a residual component cannot be a two-role alternating
exchange.  It must use at least:

* a three-role colour-neutral \(C_6\)-type move;
* a higher-degree structural-zero Markov move; or
* a noncoatom/pivot interface where the rank-\(r\) freshness assumption
  (3.6) is deliberately relaxed and separately paid.

Thus failure of the obvious two-boundary splice is structural, not a lack
of search.

## 4. The first algebraically possible exact-\(B\) move

The obstruction at support two is sharp at the owner-colour level.

### Proposition 4.1 (the coatom triangle \(C_6\))

Let \(C\) have rank \(r-2\), and choose distinct
\(a,b,c\notin C\).  Put

\[
                         U_a=C+a,\qquad
                         U_b=C+b,\qquad
                         U_c=C+c.                    \tag{4.1}
\]

The three old coatom/fresh-label pairs

\[
                         (U_a,b),\quad(U_b,c),\quad(U_c,a) \tag{4.2}
\]

have owner colours

\[
                         C+a+b,\quad C+b+c,\quad C+c+a. \tag{4.3}
\]

The reverse cyclic reassignment

\[
                         (U_c,b),\quad(U_a,c),\quad(U_b,a) \tag{4.4}
\]

has the same three owner colours, cyclically permuted.  Every colour has
rank \(r\).

#### Proof

Taking unions in (4.2) gives (4.3).  Taking unions in (4.4) gives,
respectively,

\[
                         C+b+c,\quad C+a+c,\quad C+a+b,
\]

the same multiset. \(\square\)

Thus the first possible owner-exact Markov move is the chordless
\(K_{3,3}-I=C_6\) trade.

There is a further state warning.  To make all six functional arcs legal,
the three relevant head prefixes must agree.  Writing that common prefix
as an ordered block list with union \(R\), the three head states necessarily
have final blocks \(D+a,D+b,D+c\), where \(C=R\mathbin{\dot\cup}D\).
The corresponding tail states have first blocks
\(D+a,D+b,D+c\) followed by the common prefix.  Hence the tail and head
banks use the same three coatom tops \(U_a,U_b,U_c\), but generally with
different ordered decompositions.

So Proposition 4.1 is not yet a fixed-role arc switch.  Its literal lift
must be a **three-role phase toggle** which replaces the three old chain
states by the three new chain states while preserving each coatom target.
This is exactly the form of a mixed-coatom \(C_6\) packet; treating all six
states as simultaneous one-copy roles would duplicate the three coatom
targets.

### Proposition 4.2 (a bare coatom triangle is not lower-transparent)

Under the common-prefix realization above, the three head states are

\[
 (P_1,\ldots,P_{d-1},D+a),\quad
 (P_1,\ldots,P_{d-1},D+b),\quad
 (P_1,\ldots,P_{d-1},D+c),                           \tag{4.5}
\]

whereas the corresponding tail-phase states are

\[
 (D+a,P_1,\ldots,P_{d-1}),\quad
 (D+b,P_1,\ldots,P_{d-1}),\quad
 (D+c,P_1,\ldots,P_{d-1}).                           \tag{4.6}
\]

The lowest target in the three chains (4.5) is respectively

\[
                         D+a,\quad D+b,\quad D+c,
\]

while the lowest target in all three chains (4.6) is the same set
\(P_{d-1}\).  Therefore the two three-role phases do not have the same
strict-lower target multiset.

In particular, the owner-exact \(C_6\) cannot by itself be the required
exact-\(B\) packet.  It must carry auxiliary lower rays, use a larger
phase block, or export a separately priced lower sidecar.

#### Proof

In the functional chain convention, the lowest target of
\((A_1,\ldots,A_d)\) is the final block \(A_d\).  Reading the final blocks
in (4.5)--(4.6) gives the assertion. \(\square\)

## 5. Exact remaining theorem

The \(B+1\) lower graft is complete once a guarded residual factor satisfying
Theorem 2.1 is supplied.  Exact \(B\) requires the following strictly
stronger statement.

> **Protected cubic fusion lemma.**  
> In the residual functional rainbow factor, there are three selected arcs,
> at least one on the hub component and at least one on the residual
> component, together with a phase-consistent realization of the coatom
> triangle in Proposition 4.1, whose toggle preserves every named lower
> target and the three owner colours.

The general \(q\)-way rainbow-fusion theorem would then join the components
without any repeated role.  Theorem 3.1 proves that \(q=2\) cannot replace
this lemma.
