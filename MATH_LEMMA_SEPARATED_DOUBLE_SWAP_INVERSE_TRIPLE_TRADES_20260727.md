# Separated double swaps and inverse-triple wreath trades

Date: 2026-07-27

## 1. A linear-size near-wreath family

Let \(n=2m+1\), let

\[
 \pi=(x_0,x_1,\ldots,x_{n-1}),
\]

and write \(\mathcal M(\pi)\) for its \(n\) cyclic intervals of length
\(m\).  Fix \(p\in\mathbb Z_n\).  Form \(\pi^{(p)}\) by simultaneously
swapping

\[
 (x_p,x_{p+1})
 \quad\text{and}\quad
 (x_{p+m},x_{p+m+1}).                              \tag{1.1}
\]

### Lemma 1 (three-window law)

For every \(m\ge2\),

\[
 |\mathcal M(\pi)\setminus\mathcal M(\pi^{(p)})|
 =|\mathcal M(\pi^{(p)})\setminus\mathcal M(\pi)|=3.   \tag{1.2}
\]

In particular the two wreaths share exactly \(n-3\) middle owners.

### Proof

Swapping adjacent positions \(a,a+1\) changes exactly the two length-\(m\)
windows whose starts are

\[
 a+1\quad\text{and}\quad a+m+2 pmod n.
\]

For the swaps in (1.1), these start sets are

\[
 \{p+1,p+m+2\}
 \quad\text{and}\quad
 \{p+m+1,p+2m+2\}.
\]

Since \(2m+2\equiv1\pmod n\), the second pair is
\(\{p+m+1,p+1\}\).  Their union has three starts.  At each start exactly one
of the two swapped coordinates lies in the window, so all three window sets
really change.  This proves (1.2). \(\square\)

Thus an exact factor of \(C_m=W/n\) wreaths has only

\[
 nC_m=W
\]

separated-double-swap moves.  This is a linear catalogue, compared with the
factorial catalogue of all cyclic orders.

## 2. Inverse signed triples give exact 2-trades

Write

\[
 R(\pi,p)=\mathcal M(\pi)\setminus\mathcal M(\pi^{(p)}),
 \qquad
 A(\pi,p)=\mathcal M(\pi^{(p)})\setminus\mathcal M(\pi).
\]

Both are triples by Lemma 1.  Suppose \(\pi,\rho\) are distinct rows of an
exact factor and

\[
 R(\rho,s)=A(\pi,p),qquad A(\rho,s)=R(\pi,p).       \tag{2.1}
\]

Then

\[
 \boxed{
 \{\pi,\rho\}\longleftrightarrow
 \{\pi^{(p)},\rho^{(s)}\}
 }
                                                               \tag{2.2}
\]

is an exact support-matched 2-trade.

Indeed, the unchanged \(n-3\) owners remain on their original rows, and the
two signed triples in (2.1) exchange places.  Hence the new supports are
disjoint and their union is the old union.  The four cross-intersection sizes
are necessarily

\[
 \boxed{3,3,n-3,n-3}.                                \tag{2.3}
\]

## 3. Directed triple graph

For an exact factor \(F\), form a directed labelled multigraph
\(\Gamma_F\) whose vertices are triples of middle owners and whose arcs are

\[
 R(\pi,p)\longrightarrow A(\pi,p),qquad \pi\in F, p\in\mathbb Z_n.
\]

Then inverse-triple 2-trades are exactly directed 2-cycles of \(\Gamma_F\)
using arcs from two distinct factor rows.  The compensation-trade problem for
this family is therefore reduced to a signed 2-cycle problem on exactly
\(W\) arcs.

There is no reason a priori to stop at length two.  The removed triple of a
move is the length-two path of the factor wreath centred at one middle owner.
Exact middle ownership therefore makes all \(W\) removed triples distinct,
so \(\Gamma_F\) is a partial functional graph.  Consequently **all**
directed triple cycles, with no length cutoff, can be decomposed in linear
time.  `enumerate_all_near_carrier_cycles` implements this decomposition and
emits every cycle whose atoms use distinct factor rows.  In the currently
audited \(m=4,5\) states all legal pure triple cycles happen to have length
two; the full routine nevertheless removes that unproved restriction from
the search atlas.

This is the first trade family in the search whose size is on the natural
\(W\) scale and whose middle-layer legality is automatic.

## 4. Finite converse audit

The forward construction above is a theorem.  The converse statement

> every nontrivial wreath 2-trade is an inverse-triple trade

is not yet proved.  It has, however, been checked against the complete
geometric wreath universe in the following instances:

\[
\begin{array}{c|r|r|r|c}
m&|F|&\text{near moves}&\text{exhaustive 2-trades}&
\text{inverse generator}\\ \hline
3&5&35&5&5\\
4&14&126&1&1\\
5&42&462&21&21
\end{array}
\]

There are no missing or extra trades.  A second \(m=5\) seed has 35
exhaustive 2-trades, again all with profile (2.3).  The independent verifier
is `scratch/audit_near_wreath_two_trades.py`.

The equality at three small values is evidence for the converse, not a
substitute for a proof.

## 5. Search integration

`scratch/near_wreath_two_trades.py` implements the linear generator and
inverse-triple pairing.  The main support-trade search accepts

```
--near-move-catalogue
```

and computes MWB, weighted CPCR, coherent compensation gain, and Dirichlet
noise on its exact trades.  At the audited \(m=5\) factor this structural
catalogue finds the same 21 trades as the 1,814,400-wreath exhaustive census,
while visiting only 94 closure states.

## 6. Remaining theorem on this lane

Combining this note with the support-trade Dirichlet identity reduces the
2-trade route to a concrete statement:

> If the weighted CPCR potential of an exact factor is \(\Omega(W)\), then
> its directed triple graph contains an inverse pair whose induced lower-rank
> coherent gain exceeds its Dirichlet noise.

This statement may fail for factors with too few directed 2-cycles; the
finite data do not rule that out.  If it fails, the same signed-triple graph
still supplies the atoms for longer directed circuits, corresponding to
3-, 4-, and higher support-matched trades.  Thus the graph is useful even if
2-cycles alone are not asymptotically sufficient.
