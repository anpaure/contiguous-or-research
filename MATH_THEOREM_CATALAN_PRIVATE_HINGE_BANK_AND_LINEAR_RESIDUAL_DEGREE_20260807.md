# A full Catalan bank of private omitted-colour hinges with linear residual degree

**Date:** 2026-08-07  
**Method:** explicit Boolean hinge parameterization and greedy
seven-resource packing; no finite search  
**Status:** unconditional local-bank theorem.  It constructs the complete
private hinge bank required by the safe-deletion theorem and can keep the
remaining incidence host at any prescribed asymptotic minimum degree below
one half of its original degree.  It does not extend the bank to a doubly
adequate Hamilton cycle.

## 1. Setting and one hinge

Let `|Omega|=2m` and put

\[
 \mathcal A={\Omega\choose m-2},\qquad
 \mathcal B={\Omega\choose m-1},\qquad
 \mathcal U={\Omega\choose m},
\]

\[
 W=|\mathcal U|,qquad
 C=\operatorname {Cat}_m={W\over m+1}.
\]

Choose `U in U`, distinct `u,b in U`, and distinct
`x,y in Omega\U`.  Define

\[
 a=U\setminus\{u,b\},\qquad X=a+b,
\]

\[
 Q_x=a+b+x,\quad Q_y=a+b+y,qquad
 B_x=a+x,\quad B_y=a+y.                              \tag{1.1}
\]

Then

\[
 B_x\subset Q_x\supset X\subset Q_y\supset B_y      \tag{1.2}
\]

is a four-edge path in the incidence graph
`B <-> U`.  Suppressing `Q_x,Q_y` gives the Johnson hinge

\[
                         B_x-X-B_y,                  \tag{1.3}
\]

whose two intersection colours are both `a`.  Moreover

\[
                         X\subset U,                 \tag{1.4}
\]

so if `U` is omitted from an eventual union-rainbow cycle, either hinge
edge can be assigned to `U` through the endpoint `X`; deleting one leaves
the other occurrence of `a` intact.

Call the seven resources

\[
 \{U,Q_x,Q_y\}\subset\mathcal U,qquad
 \{X,B_x,B_y\}\subset\mathcal B,qquad
 \{a\}\subset\mathcal A                             \tag{1.5}
\]

the resource set of the hinge.  A bank is **private** when these resources
are pairwise distinct across all its hinges, within each rank class.

## 2. Exact candidate and load census

For fixed omitted colour `U`, the number of ordered candidates is

\[
 g=m(m-1)m(m-1)=m^2(m-1)^2.                         \tag{2.1}
\]

Hence the complete ordered catalogue has `Wg` members.

The maximum number of catalogue members using one fixed resource is as
follows.

* A fixed rank-`m` resource occurs `g` times in each of the roles
  `U,Q_x,Q_y`, hence at most

  \[
                              3g.                    \tag{2.2}
  \]

* A fixed rank-`(m-1)` resource occurs

  \[
  h=m(m+1)(m-1)^2={m+1\over m}g                     \tag{2.3}
  \]

  times in each of the roles `X,B_x,B_y`, hence at most `3h` times.

* A fixed rank-`(m-2)` colour occurs

  \[
  \ell=(m+2)(m+1)m(m-1)
       ={(m+2)(m+1)\over m(m-1)}g                   \tag{2.4}
  \]

  times.

For example, (2.3) in the central role follows by choosing
`u notin X`, `b in X`, and an ordered pair `x,y` outside `X+u`.
In an outer role, choose the distinguished outer label in the fixed
rank-`(m-1)` set, then choose the ordered pair `u,b` outside it and the
other exterior label.  Formula (2.4) chooses ordered `u,b` outside `a`
and then ordered `x,y` outside `a+u+b`.

Thus selecting one candidate can conflict, by the union bound, with at
most

\[
 L_m=9g+9h+\ell=D_mg,                               \tag{2.5}
\]

where

\[
 D_m=9+9{m+1\over m}
       +{(m+2)(m+1)\over m(m-1)}.                   \tag{2.6}
\]

## 3. Full private bank

### Theorem 3.1

For every `m>=19`, there is a private bank of at least `C` hinges.
Consequently there are `C` distinct omitted colours with pairwise
edge-disjoint private hinges and pairwise distinct protected intersection
colours.

#### Proof

Greedily choose a catalogue member and discard every member sharing one of
its seven resources.  By (2.5), one choice discards at most `L_m`
catalogue members.  A maximal bank therefore has size at least

\[
                         {Wg\over L_m}={W\over D_m}. \tag{3.1}
\]

Direct simplification gives

\[
                         D_m<m+1\qquad(m\ge19).      \tag{3.2}
\]

Since `C=W/(m+1)`, the lower bound (3.1) is strictly larger than `C`.
Retain any `C` hinges. \(\square\)

The ordered catalogue counts both orientations of a physical hinge.  This
does not affect the greedy proof: the two copies share all resources and
are discarded together.

## 4. Simultaneous linear residual degree

For a chosen omitted family `O subset U`, put

\[
 d_{\mathcal O}(B)=|\{U\in\mathcal O:B\subset U\}|
 \qquad(B\in\mathcal B).                            \tag{4.1}
\]

The degree of `B` in the residual incidence host

\[
 \mathcal B\longleftrightarrow\mathcal U\setminus\mathcal O
\]

is `m+1-d_O(B)`.

### Theorem 4.1 (degree-controlled hinge packing)

Fix an integer `delta` with `1<=delta<=m`.  If

\[
 \boxed{
 m+1>D_m+{\delta m\over m+1-\delta},}               \tag{4.2}
\]

then the private bank in Theorem 3.1 may be chosen so that

\[
 d_{\mathcal O}(B)\le m+1-\delta
 \quad(B\in\mathcal B).                             \tag{4.3}
\]

Thus every residual facet has degree at least `delta`.

#### Proof

Run the same greedy selection, but forbid a new omitted colour `U` whenever
it contains a facet `B` already used by exactly `m+1-delta` selected
omitted colours.

After `t` selections, the total number of omitted-colour/facet incidences
is `mt`.  Hence at most

\[
                         {mt\over m+1-\delta}        \tag{4.4}
\]

facets are saturated.  Each saturated facet has only `delta` still
unselected rank-`m` supersets.  Therefore at most

\[
                         {\delta mt\over m+1-\delta}\tag{4.5}
\]

omitted colours, and hence that number times `g` catalogue candidates, are
forbidden by the degree rule.

The previously chosen hinges rule out at most `tL_m` further candidates.
For every `t<C`, a new candidate remains provided

\[
 Wg>C\left(L_m+{\delta m\over m+1-\delta}g\right).
\]

Using `W=(m+1)C` and (2.5), this is exactly (4.2).  Induction supplies `C`
choices and (4.3) holds by construction. \(\square\)

### Corollary 4.2

For every fixed `alpha<1/2` and all sufficiently large `m`, the bank can be
chosen with

\[
 \delta=\lfloor\alpha(m+1)\rfloor,
\]

so the residual host has minimum degree at least
`alpha(m+1)-1`.

Indeed, `D_m=19+o(1)`, while the final term in (4.2) is
`(alpha/(1-alpha)+o(1))m`; the coefficient is smaller than one exactly
when `alpha<1/2`.

For the minimal degree-two gate, (4.2) holds already for every `m>=21`.

### Theorem 4.3 (all three rank-`m` roles may leave linear degree)

Let

\[
 \mathcal R_{\rm used}
 =\{U,Q_x,Q_y:\text{over the selected hinges}\}.     \tag{4.6}
\]

Fix `delta`.  If

\[
 \boxed{
 m+1>D_m+{9\delta m\over m+1-\delta},}               \tag{4.7}
\]

then the bank may instead be chosen so that every
`B in binom(Omega,m-1)` has at least `delta` supersets outside
`R_used`.

#### Proof

Cap the total `R_used`-load of every facet at `m+1-delta`.  After `t`
hinges, the three rank-`m` roles contribute `3mt` facet incidences, so at
most

\[
                         {3mt\over m+1-\delta}
\]

facets are saturated.  Each has `delta` unused rank-`m` supersets.  A
fixed rank-`m` resource occurs in at most `3g` catalogue candidates across
its three roles.  Thus the additional forbidden-candidate count is at
most

\[
 {3mt\over m+1-\delta}\,\delta\,3g
 ={9\delta mt\over m+1-\delta}g.
\]

Adding the ordinary `tD_mg` conflict loss and using `t<C` gives exactly
(4.7). \(\square\)

For every fixed `alpha<1/10`, condition (4.7) holds for all sufficiently
large `m` with `delta=floor(alpha(m+1))`: its linear loss coefficient is
`9alpha/(1-alpha)<1`.  Even after deleting all omitted and internal hinge
upper resources, every facet therefore retains `Omega(m)` available
upper neighbours.

## 5. Avoiding a protected pivot bank

One fixed resource occurs in at most `4g` catalogue members for
`m>=3`, by (2.2)--(2.4).  Thus a prescribed forbidden bank of `p`
rank-labelled resources removes fewer than `4pg` candidates.

Consequently Theorems 3.1 and 4.1 remain true, with the same greedy proof,
whenever their strict candidate inequality has an additional `4p` on the
right after division by `g`.  In the unweighted case this reads

\[
 W-4p>CD_m
 \quad\Longleftrightarrow\quad
 m+1-{4p\over C}>D_m.                               \tag{5.1}
\]

The protected loss is divided by the Catalan target size; it is not an
`O(p)` loss in the normalized `m+1` inequality.  In particular, for every fixed
`alpha<1/2`, every polynomial-size protected bank can be avoided for all
sufficiently large `m`.  A depth-`Theta(sqrt(m))` sharp pivot and its
buffer are therefore negligible at this packing stage.

### Theorem 5.1 (simultaneous sublinear two-sided exposure)

For all sufficiently large `m`, the private bank can be chosen, while
avoiding any polynomial-size protected resource bank, so that

\[
 \max_{B\in\mathcal B}
   |\{R\in\mathcal R_{\rm used}:B\subset R\}|
 \le {24m\over\log m},                              \tag{5.2}
\]

and

\[
 \max_{R\in\mathcal U}
   |\{B\in\mathcal B_{\rm used}:B\subset R\}|
 \le {24m\over\log m},                              \tag{5.3}
\]

where `R_used` is the union of the three rank-`m` roles and
`B_used` is the union of the three rank-`(m-1)` roles.

#### Proof

After deleting the polynomial-size protected catalogue neighbourhood,
the greedy proof produces a private matching `M` of catalogue members with

\[
                         |\mathcal M|\ge {W\over2D_m}             \tag{5.4}
\]

for all sufficiently large `m`.  Choose a uniformly random `C`-subset of
this matching.

Fix `B in mathcal B`.  Since all rank-`m` resources in `M` are distinct,
at most the `m+1` supersets of `B` occur among its three rank-`m` roles.
One gadget contributes at most three of them.  Put

\[
 L={24m\over\log m},\qquad s=\lceil L/3\rceil.
\]

If the selected load at `B` is at least `L`, then at least `s` members of
the at most `m+1` relevant gadgets were selected.  Uniform sampling without
replacement gives

\[
 \Pr(\text{load at }B\ge L)
 \le {m+1\choose s}\left({C\over|\mathcal M|}\right)^s
 \le \left({2eD_m\over s}\right)^s
 =\exp(-(8+o(1))m).                                 \tag{5.5}
\]

For fixed `R in mathcal U`, all rank-`(m-1)` resources in `M` are distinct
and `R` has only `m` facets.  The identical estimate proves (5.3).
There are fewer than `2^(2m+1)` tests of the two types, so their union
probability is `o(1)`.  Some `C`-subbank passes every test. \(\square\)

In particular, omission load, protected-owner exposure, and used-facet
exposure are all `o(m)` simultaneously.  This does not alone imply factor
extension: coordinate-cut or optional-middle-core balance remains a
genuinely global condition.

## 6. Exact host gate

Let `O` and `P` be the omitted-colour family and the union of the private
incidence hinges supplied above.  If the balanced residual incidence graph

\[
 G_{\mathcal O}
 =\mathcal B\longleftrightarrow
   (\mathcal U\setminus\mathcal O)                  \tag{6.1}
\]

has a Hamilton cycle containing `P` and whose suppressed intersection
palette covers `A`, then:

1. its suppressed Johnson cycle is union-rainbow and
   intersection-surjective;
2. choosing one hinge edge for every `U in O` gives a deletion set of size
   `C`;
3. the deletion edges are endpoint-matchable to `O` through their private
   central facets;
4. the distinct hinge colours remain represented by the unchosen mate;
   hence the deletion is palette-safe.

Thus the common-basis and endpoint rows of the interior rethread close
literally.  Theorem 4.1 shows that this host gate cannot fail merely because
some residual facet has sublinear degree: one may retain any fixed degree
fraction below one half.

What remains is a protected **coloured Hamilton extension theorem** for
`G_O`.  Large minimum degree in this sparse incidence graph does not by
itself imply Hamiltonicity, and this note makes no such claim.  The
exterior common-endpoint forest, residence, deeper upper rows, and the
literal compiler also remain beyond this local theorem.

### 6.1 Exact hinge contraction

There is a sharper balanced form of the same host gate.  Remove the
`C` omitted colours and the `2C` internal visited colours `Q_x,Q_y`.
Remove the `3C` hinge vertices `X,B_x,B_y`, but replace each complete
four-edge hinge by one supervertex whose incidence roles are its two outer
endpoints `B_x,B_y`.

The remaining ordinary rank-`(m-1)` shore has

\[
                         V-3C=(m-3)C
\]

vertices.  Adding the `C` supervertices gives `(m-2)C`.  The remaining
rank-`m` shore has

\[
                         W-3C=(m-2)C                             \tag{6.2}
\]

vertices as well.  Join a supervertex to a remaining rank-`m` set once
for each one of its two outer endpoint facets contained in that set; this
may give two parallel role edges at their unique common superset.

### Proposition 6.1 (contraction equivalence)

A Hamilton cycle of `G_O` containing every hinge path is equivalent to a
Hamilton cycle of this balanced contracted multigraph.  Expansion of the
supervertices restores the hinge paths verbatim.

#### Proof

In a Hamilton cycle containing a hinge, its three internal vertices have
both incident cycle edges forced, while each outer endpoint has exactly one
external cycle edge.  Contracting the forced path therefore preserves
degree two and cyclic order.  Conversely, the two role edges at a
supervertex specify one external edge at each outer endpoint; replacing the
supervertex by the forced path restores one spanning cycle.  A parallel
two-edge component through one upper vertex cannot occur inside a Hamilton
cycle unless it is the whole graph, so it creates no ambiguity here.
\(\square\)

Under Theorem 4.3, every ordinary vertex and every outer endpoint retains
at least `delta` neighbours on the contracted upper shore.  Hence every
supervertex also has degree at least `delta` (counting endpoint roles).
For fixed `alpha<1/10`, the contracted host can therefore be chosen with
linear minimum degree on both shores.

Theorem 5.1 is stronger asymptotically: every ordinary facet and each
outer endpoint retains `m-o(m)` neighbours.  The contracted host may thus
be chosen with minimum degree `m-o(m)` while avoiding the protected pivot.

This balances the host exactly but does not prove it Hamiltonian.  Nor does
ordinary Hamiltonicity enforce the remaining turn-colour condition: at
each retained rank-`m` vertex, the two selected facet roles must jointly
make the suppressed intersection palette cover all of `A`.
