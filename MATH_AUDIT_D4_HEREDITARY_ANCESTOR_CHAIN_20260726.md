# The `D_4` switch on a hereditary invisible block: ancestor carriers and chain cap derivative

Date: 2026-07-26

Method: pure mathematics only.

## 0. Result

Let an aligned invisible block of semilength $r$ be contained in the zero
interval of each of its boundary-served ancestor windows of depths

\[
                         r\le q\le H.
\tag{0.1}
\]

Install the canonical/noncanonical anchored $D_4$ switch in a common
one-hole context wholly inside that block.  The switch is exactly legal:
its row endpoints are $P,P^c$ and its complete state and adjacent-union
ledgers agree, so the anchored port-context substitution theorem applies.

On the hereditary plateau source chain, however, the switch has identically
zero action.  If $O_{C,q}$ is the exterior target of the ancestor window,
then for every local row $P$ both packet shores have physical target

\[
                              T^F_{C,q,P}=T^G_{C,q,P}=O_{C,q}.
\tag{0.2}
\]

Equivalently, the row-resolved carrier map is the collapse

\[
                 \kappa_{C,q}(e_S)=e_{O_{C,q}}
\tag{0.3}
\]

for every local set $S$.  It annihilates every signed row atom of total
mass zero.  Consequently

\[
 \boxed{
 D^{\rm source}_{C,q}=0\quad(r\le q\le H),\qquad
 \Delta\operatorname {PCap}^{\rm source}_{C,[r,H]}=0.}
\tag{0.4}
\]

This is a chainwise erasure invariant.  The physical source targets
$O_{C,q}$ form one or two nested chains as $q$ grows, but the same switch
does not transport any member of either chain.

The nonzero local length-two and length-three profiles are not contradicted
by (0.4).  They occur only for ancestor windows whose boundary cuts the
$D_4$ packet.  Such windows belong to the two-boundary frontier/collar
sector, not to the invisible-block source fibre.

There is a sharp conditional positive statement for that separate sector.
Suppose a one-sided boundary placement exposes the complete length-two
profile at every $q$ through an injective common carrier, with multiplicity
$M_q$, and suppose the normalized residual capacity on its thirty-six
cells is within $L^1$ error $\varepsilon_q$ of a scalar $c_q$.  If, for
some $0<\eta\le9/10$,

\[
              {21\over10}+\eta\le c_q\le5-\eta
              \qquad(r\le q\le H),
\tag{0.5}
\]

then the one common switch has aggregate derivative

\[
 \boxed{
 \Delta\operatorname {PCap}_{[r,H]}
       \le-10\eta\sum_{q=r}^H M_q+\sum_{q=r}^H\varepsilon_q.}
\tag{0.6}
\]

Thus it gives strict chain descent when the last error sum is smaller than
$10\eta\sum_qM_q$.  This is a theorem about a boundary-straddling collar
chain.  It does not drain the hereditary source in (0.2), unless an
additional theorem identifies its overloaded targets with the negative
cells of that collar chain.  No such identification follows from the
$D_4$ factor.

At length three there is a second cancellation: under a scalar background
the old and new multiplicity multisets agree at every depth, so the whole
length-three chain has zero cap derivative.  A length-three gain requires
nonuniform residual capacities.

## 1. Exact legality of the contextual switch

Let $J=[8]$, let $9$ be the distinguished local odd-graph coordinate,
and index the rows by $P\in\mathcal D_4$.  On both packet shores the local
infinity-cut trace has endpoints

\[
                         X_0=P,\qquad X_4=J\setminus P.
\tag{1.1}
\]

Both factors enumerate every local four-state once and every adjacent
five-state union once.  Hence their complete $X$ and $Y$ ledgers agree.

### Proposition 1.1 (aligned-context legality)

The replacement $F\rightsquigarrow G$ is a legal exact-factor
substitution in every common aligned one-hole ordered-tree context.

#### Proof

Equation (1.1) is precisely the anchored port condition.  The fixed
entrance and exit states leave the two outer incident edges unchanged.
Equality of the $X$ ledgers preserves every middle owner inside the slab,
and equality of the $Y$ ledgers preserves, by complementation and adjoining
the interface coordinate, every owner on the opposite shore.  These are
the two discrepancies in the context-substitution theorem, so both vanish.
Wrapping by left concatenation, right concatenation, or an outer primitive
therefore remains exact, and induction gives every common one-hole
context.  \(\square\)

The internal exchange symbols $a_1,b_4$ may change.  They affect crossing
window targets, but they are not outer endpoint states and create no
legality defect.

## 2. Row-resolved carriers in an arbitrary ancestor

For a row $P$, write the two local coordinate words as

\[
 q_H(P)=(a_1^H,a_2^H,a_3^H,a_4^H,
          b_1^H,b_2^H,b_3^H,b_4^H,9),qquad H\in\{F,G\}.
\tag{2.1}
\]

An ancestor target selects a fixed set $A_\omega\subseteq\mathbb Z_9$
of local positions and a set $O_\omega$ of exterior coordinates.  Here

\[
                         \omega=(C,q,k,P)
\tag{2.2}
\]

records the outer context, ancestor depth, window start, and local row.
Let $\iota_C$ be the inherited injection of local labels.  Define

\[
 I_{A_\omega}(q_H(P))
       =\{q_H(P)_j:j\in A_\omega\}.
\tag{2.3}
\]

The exact row-resolved carrier action is

\[
 \boxed{
 d_\omega
 =e_{O_\omega\cup\iota_C(I_{A_\omega}(q_G(P)))}
  -e_{O_\omega\cup\iota_C(I_{A_\omega}(q_F(P)))}.}
\tag{2.4}
\]

For a family $\mathcal A_q$ of affected windows at depth $q$,

\[
                         D_{C,q}=\sum_{\omega\in\mathcal A_q}d_\omega.
\tag{2.5}
\]

Formula (2.4) is authoritative even when the exterior carrier depends on
the row and the start.  If one fixed map applies to all fourteen rows at a
given position set $A$, it may be summed to

\[
 (\Phi_{C,q,A})_*D_A,
 \qquad
 D_A=\sum_P
   \left(e_{I_A(q_G(P))}-e_{I_A(q_F(P))}\right).
\tag{2.6}
\]

Without that common-map hypothesis, (2.6) must not replace (2.4).

## 3. Every ancestor of an invisible block

Let the local $D_4$ hole lie wholly inside a maximal invisible $r$-block,
and let the depth-$q$ zero interval contain that whole block.  The ancestor
window therefore traverses both local endpoint states in (1.1).  In a
common exterior state $K$ their local slab states are

\[
                         K\cup P,qquad K\cup(J\setminus P).
\tag{3.1}
\]

Their intersection is $K$.  No local coordinate can occur throughout the
ancestor window, since it is absent from one of the complementary endpoint
states.

### Theorem 3.1 (rowwise hereditary collapse)

For every $q$ satisfying (0.1), every local row $P$, and every filling of
the rest of the invisible block,

\[
                         A_{C,q,k,P}=\varnothing.
\tag{3.2}
\]

Consequently the physical target is $O_{C,q}$ on both shores and the
signed row atom (2.4) is zero.

#### Proof

The target is the intersection of the states in the ancestor window.
Because that window contains both states in (3.1), its local part is
contained in

\[
                         P\cap(J\setminus P)=\varnothing.
\tag{3.3}
\]

All exterior coordinates present throughout the window form the same set
$O_{C,q}$ on both packet shores.  This proves (0.2), (3.2), and the
rowwise vanishing.  \(\square\)

The dual union statement is equally rigid: the local union is all of $J$
on both shores.

### Corollary 3.2 (chainwise erasure invariant)

Any finite composition of anchored, port-preserving switches wholly
inside the invisible block has zero signed action on every ancestor source
target in (0.1).  Hence its aggregate PCap derivative on those source
occurrences is exactly zero for every cap and every background.

#### Proof

The proof of Theorem 3.1 uses only the fixed complementary endpoints, not
the internal path.  It therefore applies after every sequence of such
switches.  Equal target histograms have equal hinge values for arbitrary
backgrounds.  Summing over $q$ proves the assertion.  \(\square\)

This invariant is stronger than cancellation of the aggregate local
profiles $\Delta_1,\Delta_4,\Delta_5,\Delta_8$: it is rowwise and
statewise.

## 4. Chronology of the physical source chain

For a fixed aligned $r$-block occupying pair positions
$[s,s+r-1]$, the canonical boundary service chooses

* the depth-$q$ zero window beginning at $s$ when $s+q\le m$;
* the depth-$q$ zero window ending at $s+r$ when $s+q>m$.

On either fixed side, increasing $q$ by one extends the zero interval by
one cell and deletes one endpoint coordinate from the complementary target
interval.  Thus the exterior targets satisfy

\[
 O_{C,q+1}\subset O_{C,q}
\tag{4.1}
\]

within each side regime.  The service rule changes side at most once, so
the targets form at most two nested chains.

The collapse maps for all ancestors are therefore

\[
 \boxed{
 \kappa_{C,q}:e_S\longmapsto e_{O_{C,q}},
 \qquad O_{C,q+1}\subset O_{C,q}.}
\tag{4.2}
\]

For every zero-mass local signed measure $z$,

\[
                         \kappa_{C,q}z=0.
\tag{4.3}
\]

The family $(O_{C,q})$ is a coherent physical source chain, but the
$D_4$ choice does not move it.  In particular, the nonzero local tensors
$\Delta_2$ and $\Delta_3$ cannot be credited against the hereditary
plateau load $\operatorname {Cat}_r$ on this chain.

## 5. Where the length-two and length-three profiles live

Suppose instead that an ancestor boundary cuts the local packet.  For a
cyclic local interval

\[
                         A=\{j,j+1,\ldots,j+\ell-1\},
\qquad \ell\in\{2,3\},
\tag{5.1}
\]

the carrier does not collapse.  On a one-sided chain choose an ordered
exterior collar $c_1,c_2,\ldots$ so that the target at depth $q$ contains

\[
 O_q=\{c_1,\ldots,c_{m-q-\ell}\}.
\tag{5.2}
\]

Then

\[
 O_{q+1}=O_q\setminus\{c_{m-q-\ell}\},
\tag{5.3}
\]

and the row-resolved maps are the genuine injections

\[
 \boxed{
 \Phi_{q,A}(e_S)=e_{O_q\cup\iota_C(S)},
 \qquad |S|=\ell.}
\tag{5.4}
\]

For each fixed local target $S$, its physical images form the nested chain

\[
 O_{q+1}\cup\iota_C(S)
       \subset O_q\cup\iota_C(S).
\tag{5.5}
\]

The opposite boundary has the same formula after reversing the exterior
collar order.  If the service rule changes side, the two formulae give two
chain segments and need not join.

Equations (5.2)--(5.5) show the exact distinction:

* an invisible descendant has local length $0$ and is killed by (4.2);
* a frontier descendant can retain local length $2$ or $3$ through a
  one-sided ancestor chain and is transported injectively by (5.4).

The second object is a different two-boundary skeleton class.  It is not
one of the $\operatorname {Cat}_r$ indistinguishable fillings producing
the plateau source in Theorem 3.1.

## 6. Exact aggregate PCap derivative

Let $u_q(T)$ be the old affected load at depth $q$, let $D_q(T)$ be the
complete signed profile from (2.5), and let

\[
                         c_q(T)=(p-\beta_q(T))_+
\tag{6.1}
\]

be the residual capacity left by all unaffected windows.  One common
binary switch across all depths has exact derivative

\[
 \boxed{
 \Delta\operatorname {PCap}_{[r,H]}
 =\sum_{q=r}^H\sum_T
   \left[(u_q(T)+D_q(T)-c_q(T))_+
               -(u_q(T)-c_q(T))_+\right].}
\tag{6.2}
\]

For $D_q(T)<0$, define the removable excess

\[
 R_q(T)=\min\{-D_q(T),(u_q(T)-c_q(T))_+\};
\tag{6.3}
\]

for $D_q(T)>0$, define the created excess

\[
 G_q(T)=\min\{D_q(T),(u_q(T)+D_q(T)-c_q(T))_+\}.
\tag{6.4}
\]

Then

\[
 \boxed{
 \Delta\operatorname {PCap}_{[r,H]}
       =\sum_{q,T}G_q(T)-\sum_{q,T}R_q(T).}
\tag{6.5}
\]

Thus the exact necessary and sufficient condition for positive chain gain
is

\[
                         \sum_{q,T}R_q(T)>
                         \sum_{q,T}G_q(T).
\tag{6.6}
\]

For the hereditary source family, $D_q=0$ by Theorem 3.1, so both sides
of (6.6) are zero.

## 7. Explicit positive theorem for a length-two frontier chain

Let $h_F,h_G$ be the complete all-start local pair histograms.  The
canonical histogram has eighteen cells of multiplicity five and eighteen
of multiplicity two.  The new histogram has

\[
          8\text{ cells at }5,\quad11\text{ at }4,\quad
          9\text{ at }3,\quad7\text{ at }2,\quad1\text{ at }1.
\tag{7.1}
\]

For a scalar normalized residual capacity $c$, the exact new-minus-old
hinge is

\[
\varphi(c)=
\begin{cases}
0,&c\le1,\\
c-1,&1\le c\le2,\\
21-10c,&2\le c\le3,\\
-6-c,&3\le c\le4,\\
10c-50,&4\le c\le5,\\
0,&c\ge5.
\end{cases}
\tag{7.2}
\]

### Theorem 7.1 (uniformly favourable ancestor chain)

Assume that, for every $q\in[r,H]$,

1. the same legal switch exposes the whole length-two profile through the
   injective common carrier (5.4);
2. its local histogram has a common multiplicity scale $M_q>0$;
3. a scalar background $\beta_q^0$ leaves normalized residual capacity
   $c_q=(p-\beta_q^0)/M_q$; and
4. the actual background satisfies
   
   \[
   \varepsilon_q=
   \sum_{S\in\binom{[9]}2}
   |\beta_q(O_q\cup\iota_C(S))-\beta_q^0|.
   \tag{7.3}
   \]

Then

\[
 \Delta\operatorname {PCap}_{[r,H]}
       \le\sum_{q=r}^H M_q\varphi(c_q)
                         +\sum_{q=r}^H\varepsilon_q.
\tag{7.4}
\]

If (0.5) holds, this implies (0.6).

#### Proof

Under the scalar background, the old and new contributions at depth $q$
are respectively

\[
 18M_q(5-c_q)_++18M_q(2-c_q)_+
\tag{7.5}
\]

and

\[
 M_q\bigl[8(5-c_q)_++11(4-c_q)_++9(3-c_q)_+
                 +7(2-c_q)_++(1-c_q)_+\bigr].
\tag{7.6}
\]

Their difference is $M_q\varphi(c_q)$.  Every hinge is one-Lipschitz in
the background, so changing from $\beta_q^0$ to the actual background
changes the difference by at most $\varepsilon_q$.  Summation gives
(7.4).

For $0<\eta\le9/10$ and
$c\in[21/10+\eta,5-\eta]$, inspection of the last three negative
branches of (7.2) gives

\[
                              \varphi(c)\le-10\eta.
\tag{7.7}
\]

Substitute this in (7.4).  \(\square\)

The strongest scalar descent is $-10M_q$ at $c_q=4$.  The same switch is
harmful for $1<c_q<21/10$, so no background-free monotonicity theorem is
possible.

## 8. Length-three chain cancellation under scalar backgrounds

On the support changed by the aggregate length-three profile, the old and
new multiplicity multisets are both

\[
                         \{0^4,1^{18},2^{16},3^1\}.
\tag{8.1}
\]

### Proposition 8.1 (scalar chain neutrality)

Under an injective common carrier (5.4) and a scalar background on its
image, the length-three cap derivative is zero at every depth and hence on
the entire ancestor chain.

#### Proof

A scalar hinge depends only on the multiplicity, not the name of the
target.  Equality of the two multisets in (8.1) makes the old and new
hinge sums identical for every scalar cutoff.  Sum the zero differences
over $q$.  \(\square\)

A nonuniform background can expose the nonzero vector $\Delta_3$, but its
sign must then be checked by the literal criterion (6.6).

## 9. Decision

The same internal $D_4$ switch does **not** transport the hereditary
plateau source through its ancestors.  All row-resolved source maps are
the collapse maps (4.2), so the aggregate source derivative is exactly
zero.  This closes the proposed direct use of the nonzero length-two/three
profiles on a completed invisible block.

A boundary-straddling $D_4$ atom can transport a coherent nested collar
chain, and Theorem 7.1 gives an explicit positive residual-capacity regime.
But that atom belongs to the frontier skeleton, and its negative cells are
not the source cells carrying the $\operatorname {Cat}_r$ invisible-fibre
plateau.  Turning its conditional descent into a coefficient-one repair
requires a new correlation theorem between frontier negative cells and
the canonical hereditary overload.  Exact contextual legality is already
settled; carrier/load correlation is the remaining obstruction.
