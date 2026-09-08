# Two-sided binary rotors: the exact incidence-hexagon cocycle, its calibrated reserve, and the activation gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or
external input is used.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad
 W=\binom n m,
 \qquad
 D=m!(m+1)!.
 \tag{0.1}
\]

The direct two-sided binary-rotor problem is the owner-coloured cycle-cover
problem in the injective de Bruijn graph from
`MATH_THEOREM_BINARY_ROTOR_DEBRUIJN_DIVERGENCE_AND_MINIMAL_SKELETON_20260726.md`.
This note starts at its exact uniform all-rank fractional circulation and
audits the first possible port-preserving in-place cycle switch.  No anti-dihedral,
fixed-pair, reflection, or additive-seam shortcut is used.

There are five conclusions.

1. **There is no owner-fixed rotor 2-switch.**  Once the selected state
   set is an owner transversal and is flow-balanced, its successor at
   every used state is unique.  In particular, the tempting reciprocal
   pair obtained by swapping positions \(1,n\) cannot occur in any
   owner-transversal rotor factor: its two forced successor states have
   the same middle owner.

2. **The first port-preserving circulation switch is an exact incidence
   \(C_6\).**  For an injective \((n-3)\)-word \(w\), with complementary
   labels \(\{a,b,c\}\), the six arcs

   \[
    e_{pq}=(p,w,q),\qquad p,q\in\{a,b,c\},\quad p\ne q,
   \tag{0.2}
   \]

   form \(K_{3,3}\) minus its diagonal.  Its two alternating matchings

   \[
    M^+=\{e_{ab},e_{bc},e_{ca}\},
    \qquad
    M^-=\{e_{ac},e_{cb},e_{ba}\}
   \tag{0.3}
   \]

   have identical tail, head, owner, and prefix ledgers through every
   length \(r\le n-2\).  Hence

   \[
    d_w={\bf1}_{M^+}-{\bf1}_{M^-}
   \tag{0.4}
   \]

   is an exact physical all-rank rotor cocycle.  For \(H\le m-2\), a
   legal flip preserves **both** prefix-cover systems through depth
   \(H\), while changing no owner and adding no seam.

3. **The primitive can really fuse cycles.**  If the three old arcs of
   one active hexagon lie on three distinct support cycles, flipping the
   hexagon merges those cycles into one.  A loose hexagon forest with
   \(h\) cells therefore lowers the component count by exactly \(2h\).

4. **Depth one gives the exact activation bound.**  If the lower
   rank-\((m-1)\) prefixes cover their whole layer and \(h\) hexagon
   cells are active, then

   \[
    \boxed{
    2h\le
       W-\binom n{m-1}
       ={2W\over m+2},
    \qquad
    h\le {W\over m+2}.}
   \tag{0.5}
   \]

   Starting from the wreath-scale component count \(W/n\), hexagon
   fusion to \(o(W/m)\) components needs at least

   \[
    \boxed{h\ge(1-o(1)){W\over2n}.}
   \tag{0.6}
   \]

   The required reserve is therefore only a \(1/4+o(1)\) fraction of
   the exact depth-one capacity.  There is no coefficient obstruction,
   but a positive fraction of the entire first-shadow excess must be
   organized into useful three-cycle routers.

5. **The fractional point contains precisely the right sparse reserve,
   but ordinary LP rounding does not activate it.**  Every arc belongs
   to one of \(n!/6\) disjoint hexagon cells.  At the uniform point
   \(y_e=1/D\), the local router relaxation admits total router mass
   \(W/3\), whereas every integral lower-covering factor has at most
   \(W/(m+2)\) active cells.  Thus the unstrengthened router LP has an
   integrality-gap lower bound \((m+2)/3\).  After imposing the valid cut
   (0.5), the calibrated fractional reserve

   \[
      \rho={3\over2n},
      \qquad
      \sum r_{w,\pm}=\rho {W\over3}={W\over2n}
   \tag{0.7}
   \]

   remains feasible and has exactly the fusion scale (0.6).

The missing theorem is consequently smaller and more concrete than an
arbitrary correlated rounding theorem: activate a calibrated family of
\(C_6\) cells, place their three arcs on a loose component forest, and
complete the remaining owner states so that both nested prefix systems
hold.  The \(C_6\) orientations themselves are then free exact cocycle
bits.

This activation step cannot begin inside a pure-\(B\) wreath factor.
Every pure-\(B\) owner transversal has **zero** active hexagons.  Thus the
uniform fractional reserve and the integral wreath endpoint lie in
different cells of the grouping complex; a state-changing activation
circuit is genuinely necessary.

No coefficient-one conclusion is claimed.

## 1. The exact direct rotor model

Let \({\cal V}\) be the injective ordered \((n-2)\)-words on \([n]\),
and let \({\cal E}\) be the injective ordered \((n-1)\)-words.  Write

\[
 e=(x_1,\ldots,x_{n-1}),
 \qquad
 t(e)=(x_1,\ldots,x_{n-2}),
 \qquad
 h(e)=(x_2,\ldots,x_{n-1}).
 \tag{1.1}
\]

Thus \(e\) is an arc \(t(e)\to h(e)\).  Let \(x_n\) be the unique
missing label and put

\[
 \pi(e)=(x_1,\ldots,x_n),
 \qquad
 \kappa(e)=\{x_1,\ldots,x_m\}.
 \tag{1.2}
\]

A Boolean owner-transversal rotor circulation is a vector
\(y\in\{0,1\}^{\cal E}\) satisfying

\[
 \sum_{e:\kappa(e)=X}y_e=1
 \qquad\left(X\in\binom{[n]}m\right),
 \tag{1.3}
\]

and

\[
 \sum_{e:t(e)=v}y_e=
 \sum_{e:h(e)=v}y_e
 \qquad(v\in{\cal V}).
 \tag{1.4}
\]

All outgoing arcs of one vertex have the same owner.  Hence (1.3)--(1.4)
make the selected arcs a vertex-disjoint directed cycle cover on their
used vertices.

For \(1\le r\le n-2\) define the prefix load

\[
 P_r(S;y)=
 \sum_e y_e
  {\bf1}\bigl[\{x_1,\ldots,x_r\}=S\bigr].
 \tag{1.5}
\]

The direct two-sided conditions through depth \(H\le m-2\) are

\[
 P_{m-q}(S;y)\ge1
 \quad
 \left(S\in\binom{[n]}{m-q},\ 0\le q\le H\right),
 \tag{1.6}
\]

and

\[
 P_{m+1+q}(U;y)\ge1
 \quad
 \left(U\in\binom{[n]}{m+1+q},\ 0\le q\le H\right).
 \tag{1.7}
\]

The uniform fractional point is

\[
                         y_e^*={1\over D}.
 \tag{1.8}
\]

There are exactly \(D\) arcs over each owner, and the two incoming arc
types at a vertex balance the two outgoing types.  Consequently (1.3)--
(1.4) hold fractionally.  Moreover, for every \(r\) and every \(r\)-set
\(S\),

\[
 \boxed{P_r(S;y^*)={W\over\binom nr}.}
 \tag{1.9}
\]

In particular, one common fractional point satisfies all inequalities
(1.6)--(1.7); this is not a separate marginal randomization at each
depth.

## 2. The owner-fixed 2-switch is impossible

The rotor moves on a full state are

\[
 A(x_1,\ldots,x_n)
  =(x_2,\ldots,x_{n-1},x_1,x_n),
 \tag{2.1}
\]

\[
 B(x_1,\ldots,x_n)
  =(x_2,\ldots,x_n,x_1).
 \tag{2.2}
\]

### Theorem 2.1 (state-set rigidity)

For a Boolean solution of (1.3)--(1.4), the selected state set uniquely
determines the rotor choice at every selected state.  Therefore no
nontrivial switch can change only the \(A/B\) controls while retaining
the selected states.

#### Proof

Let a selected arc enter the vertex \(v\).  Flow balance forces one
selected arc to leave \(v\).  There are two outgoing arcs, and both have
the same owner, namely the set of the first \(m\) entries of \(v\).
Equation (1.3) therefore permits at most one of them.  The selected
successor, and hence its \(A/B\) label, is unique. \(\square\)

The tempting reciprocal square fails even before a component audit.
Let \(\tau\) swap positions \(1,n\).  Directly from (2.1)--(2.2),

\[
 A\pi=B\tau\pi,
 \qquad
 A\tau\pi=B\pi.
 \tag{2.3}
\]

### Corollary 2.2 (no reciprocal selected pair)

No owner-transversal rotor circulation contains both \(\pi\) and
\(\tau\pi\).

#### Proof

The de Bruijn arcs associated with \(\pi\) and \(\tau\pi\) have the same
head, namely \((x_2,\ldots,x_{n-1})\).  Thus selecting both would give
indegree two at that vertex.  Its two outgoing arcs have one common
middle owner, so (1.3) gives selected outdegree at most one.  This
contradicts flow balance (1.4). \(\square\)

Thus the formal reciprocal coboundary is not a physical owner switch.
Any actual fusion must change selected de Bruijn arcs.

## 3. Classification of the first port-preserving trade

It is convenient to split every vertex into a tail copy and a head copy.
The resulting bipartite incidence graph has edge set \({\cal E}\).
A **port-preserving trade** replaces a set of selected arcs by another
set with the same tail multiset and the same head multiset.  Such a trade
preserves (1.4) without asking neighbouring arcs to move.

### Lemma 3.1 (no incidence rectangle)

The tail--head incidence graph contains no \(K_{2,2}\).

#### Proof

If two distinct tails have a common head, they have the form

\[
 u_a=(a,w),
 \qquad
 u_b=(b,w),
 \tag{3.1}
\]

for one injective \((n-3)\)-word \(w\).  Let the three labels outside
\(w\) be \(a,b,c\).  The two possible heads of \(u_a\) are
\((w,b),(w,c)\); those of \(u_b\) are \((w,a),(w,c)\).  Their unique
common head is \((w,c)\).  Hence two tails never have two common heads.
\(\square\)

Consequently there is no nonzero degree-two port-preserving trade.

### Theorem 3.2 (every minimal port trade is the incidence hexagon)

Every six-cycle in the tail--head incidence graph is obtained from one
injective \((n-3)\)-word \(w\) and its complementary triple
\(\{a,b,c\}\).  Its six arcs are exactly (0.2), and its two alternating
halves are (0.3).  Hence degree three is the minimum possible degree of
a nonzero port-preserving trade.

#### Proof

Two consecutive tail vertices on such a six-cycle share a head, so by
the proof of Lemma 3.1 they have the same ordered suffix of length
\(n-3\).  Connectivity propagates one common suffix \(w\) to all three
tails.  Their first labels are therefore the three labels outside \(w\).
The analogous heads are \((w,a),(w,b),(w,c)\), and injectivity forbids
the three diagonal arcs.  All six off-diagonal arcs occur, giving exactly
\(K_{3,3}\) minus a perfect matching.  Its alternating halves are the two
derangements of a three-set in (0.3).

Lemma 3.1 excludes degree two, while (0.3) supplies degree three.
\(\square\)

The qualifier "port-preserving" is essential.  This theorem does not
classify a larger trade which also changes neighbouring tail or head
occupancies.  Such a trade must be completed through the surrounding
flow and is precisely an activation circuit in the sense of Section 7.

### Theorem 3.3 (all-rank physical cocycle identity)

For every cell \((w;\{a,b,c\})\), the vector \(d_w\) in (0.4) lies in
the integral kernel of

1. the tail--head incidence equations;
2. every middle-owner row; and
3. every prefix-incidence row of length \(r\le n-2\).

In particular, a legal hexagon flip preserves (1.3)--(1.7) exactly for
every \(H\le m-2\).

#### Proof

Both matchings in (0.3) use each tail \((p,w)\) once and each head
\((w,q)\) once.  This proves the first assertion.

The owner of \(e_{pq}\) is

\[
 \kappa(e_{pq})=
 \{p,w_1,\ldots,w_{m-1}\},
 \tag{3.2}
\]

which depends on \(p\) but not on \(q\).  Each matching uses one arc for
each \(p\in\{a,b,c\}\), proving the owner identity.

Finally, the first \(n-2\) entries of \(e_{pq}\) are the tail
\((p,w)\), again independent of \(q\).  Pair the two arcs with common
tail in the two matchings.  Their prefix sets agree at every length
\(r\le n-2\).  Summing over the three tails proves the third assertion.
\(\square\)

Every arc belongs to exactly one such cell: for
\(e=(x_1,\ldots,x_{n-1})\), take

\[
 w=(x_2,\ldots,x_{n-2})
 \tag{3.3}
\]

and let the complementary triple consist of \(x_1,x_{n-1}\), and the
missing label.  Thus the cells partition \({\cal E}\), and there are

\[
                         {|{\cal E}|\over6}={n!\over6}
 \tag{3.4}
\]

of them.  Their kernel vectors have disjoint supports and generate a
direct summand isomorphic to \(\mathbb Z^{n!/6}\).  There is no parity
or lattice-index obstruction **inside this port-preserving sublattice**.

## 4. Exact component surgery

Call a cell **active** in an integral circulation if its selected arcs
are one of \(M^+,M^-\).  Owner transversality gives at most one selected
arc from each of its three tails.  Selected indegree at most one gives at
most one at each head.  Hence any cell containing three selected arcs is
automatically active.

### Lemma 4.1 (one router merges three cycles)

If the three selected arcs of an active cell lie in three distinct
support cycles, flipping the cell replaces those three cycles by one.

#### Proof

Delete the three old arcs.  Because they lie on different cycles, this
leaves three directed paths.  The old matching connects the three path
ends by one of the cyclic permutations \((abc)\), while the new matching
uses its inverse.  Relative to the old pairing, the new pairing is again
a three-cycle.  It therefore joins the three paths into one directed
cycle. \(\square\)

Let the vertices of a 3-uniform hypergraph be the support cycles of a
fixed circulation, and let an active cell be a hyperedge when its three
arcs lie on three distinct cycles.  Call a family of such cells **loose**
if its incidence bipartite graph (cycles versus cells) is a forest.

### Corollary 4.2 (loose-forest fusion)

If a loose active-cell forest has \(h\) cells and \(k\) connected
components, then it meets exactly \(2h+k\) support cycles.  Flipping its
cells in leaf-to-root order replaces those \(2h+k\) cycles by \(k\)
cycles.  The total component reduction is exactly \(2h\), and every
prefix load (1.5) is unchanged.

#### Proof

The incidence graph is a forest with \(h\) cell vertices, each of degree
three.  If it has \(v\) cycle vertices and \(k\) components, then
\(3h=(v+h)-k\), so \(v=2h+k\).

A leaf cell has two cycle vertices not used by the rest of its component.
At the moment it is processed, its three arcs therefore lie in three
distinct current cycles.  Lemma 4.1 merges them.  Delete the cell and its
two leaf cycle vertices and continue.  Theorem 3.3 preserves every prefix
load at every step. \(\square\)

This is a genuine in-place compiler operation.  It changes three physical
state arcs and introduces no new word positions.  Only the final number
of support cycles enters the usual \((m+H)C\) cyclic linearization toll.

## 5. The exact depth-one router cut

For a selected arc \(e=(x_1,\ldots,x_{n-1})\), put

\[
 \widehat L(P;y)=
 \sum_e y_e
  {\bf1}\bigl[\{x_2,\ldots,x_m\}=P\bigr],
 \qquad |P|=m-1.
 \tag{5.1}
\]

### Lemma 5.1 (one-step stationarity)

For every \((m-1)\)-set \(P\),

\[
                         \widehat L(P;y)=P_{m-1}(P;y).
 \tag{5.2}
\]

#### Proof

On every selected directed cycle, the first \((m-1)\)-block of the
successor arc is the positions \(2,\ldots,m\) block of the current arc.
The successor map permutes the selected arcs.  Summing around all support
cycles proves (5.2). \(\square\)

For a cell with word \(w\), all three arcs of either active orientation
have the common shifted lower target

\[
                         P(w)=\{w_1,\ldots,w_{m-1}\}.
 \tag{5.3}
\]

### Theorem 5.2 (exact active-cell capacity bound)

If \(P_{m-1}(P;y)\ge1\) for every \((m-1)\)-set \(P\), and \(h\) cells
are active, then (0.5) holds.

#### Proof

Let \(h_P\) be the number of active cells with common target \(P\).
By (5.3),

\[
                         \widehat L(P;y)\ge3h_P.
 \tag{5.4}
\]

There are \(W\) selected arcs, so

\[
 \sum_P\bigl(\widehat L(P;y)-1\bigr)
 =W-\binom n{m-1}.
 \tag{5.5}
\]

For every \(P\) with \(h_P>0\), (5.4) gives

\[
 \widehat L(P;y)-1\ge3h_P-1\ge2h_P.
 \tag{5.6}
\]

Sum (5.6), use Lemma 5.1 and the lower-cover hypothesis, and calculate

\[
 \binom n{m-1}={m\over m+2}W.
 \tag{5.7}
\]

This gives exactly (0.5). \(\square\)

One hexagon flip can lower the cycle count by at most two.  Hence a route
which begins with \(C_0=W/n\) components and uses only these exact routers
must use at least

\[
 h\ge{C_0-o(W/m)\over2}
   =(1-o(1)){W\over2n}
 \tag{5.8}
\]

productive cells.  Comparing (5.8) with Theorem 5.2 gives

\[
 {W/(2n)\over W/(m+2)}={m+2\over2n}={1\over4}+o(1).
 \tag{5.9}
\]

Thus the depth-one floor leaves constant slack, but it does not leave an
arbitrarily sparse problem: one quarter of the maximum router capacity
must be made productive.

## 6. The calibrated fractional reserve and its grouping gap

Introduce local activation variables \(r_{w,+},r_{w,-}\).  The elementary
LP relaxation of the assertion that orientation \(\sigma\) is active is

\[
 0\le r_{w,\sigma}\le y_e
 \qquad(e\in M^\sigma_w).
 \tag{6.1}
\]

At the uniform point (1.8), one may put

\[
                         r_{w,+}=r_{w,-}={1\over D}.
 \tag{6.2}
\]

Since there are \(n!/6\) cells and \(n!=WD\),

\[
\boxed{
 \sum_{w,\sigma}r_{w,\sigma}
 ={2\over D}{n!\over6}
 ={W\over3}.}
 \tag{6.3}
\]

This is the optimum of the elementary relaxation (6.1).  Indeed, for
every cell and orientation,

\[
 3r_{w,\sigma}\le\sum_{e\in M_w^\sigma}y_e.
 \tag{6.3a}
\]

The two orientations partition a cell and the cells partition
\({\cal E}\).  Summing (6.3a) and using \(\sum_e y_e=W\) gives
\(\sum r_{w,\sigma}\le W/3\), with equality in (6.2).

This is also the exact local identity

\[
 {1\over D}{\bf1}_{\mathcal E}
 ={1\over D}
   \sum_w\bigl({\bf1}_{M_w^+}+{\bf1}_{M_w^-}\bigr),
 \tag{6.4}
\]

because the two orientations partition the six arcs of each cell and the
cells partition \({\cal E}\).  Equation (6.4) is a ledger identity; an
individual matching \(M_w^\sigma\) is a router with boundary, not a
standalone circulation.

For an integral circulation, (6.1) may be taken Boolean, and
\(r_{w,\sigma}=1\) certifies one active cell.  Theorem 5.2 therefore gives
the following valid inequality for the integral lower-covering hull:

\[
 \boxed{
 2\sum_{w,\sigma}r_{w,\sigma}
 \le W-\binom n{m-1}={2W\over m+2}.}
 \tag{6.5}
\]

The fractional assignment (6.2) violates (6.5) by the factor

\[
 {W/3\over W/(m+2)}={m+2\over3}.
 \tag{6.6}
\]

Thus uniform all-rank marginals plus the local inequalities (6.1) do not
round the router grouping.  The elementary LP optimum is exactly \(W/3\),
while the integral optimum is at most \(W/(m+2)\); consequently (6.6) is
an integrality-gap lower bound.  This is an explicit linear-scale
separation, not a probabilistic warning.

The required reserve is nevertheless below the strengthened cut.  For
any \(0\le\rho\le1\), retain the same uniform \(y^*\) and set

\[
                         r_{w,\sigma}={\rho\over D}.
 \tag{6.7}
\]

Then

\[
                         \sum r_{w,\sigma}={\rho W\over3}.
 \tag{6.8}
\]

Taking \(\rho=3/(2n)\) gives (0.7), and (6.5) has the constant slack
computed in (5.9).  Therefore neither the exact all-rank fractional
circulation nor the first integral router cut rules out the calibrated
reserve.  What remains is its correlated activation.

## 7. Why the wreath endpoint has no reserve

A pure-\(B\) circulation is a union of full cyclic-order orbits.  It is
the natural exact integral endpoint of the fractional segment, with
\(W/n\) support cycles.

### Theorem 7.1 (pure-\(B\) factors contain no active cell)

Every pure-\(B\) owner-transversal circulation has zero active incidence
hexagons.

#### Proof

Suppose, for example, that a cell contains the selected arcs \(e_{ab}\)
and \(e_{bc}\) from \(M^+\).  Their full states have the forms

\[
 \pi_{ab}=(a,w,b,c),
 \qquad
 \pi_{bc}=(b,w,c,a).
 \tag{7.1}
\]

Pure \(B\)-closure selects both successors

\[
 B\pi_{ab}=(w,b,c,a),
 \qquad
 B\pi_{bc}=(w,c,a,b).
 \tag{7.2}
\]

Because \(|w|=2m-2\ge m\), these two successor states have the identical
middle owner

\[
                         \{w_1,\ldots,w_m\},
 \tag{7.3}
\]

contradicting (1.3).  The other orientation is identical after relabelling.
Thus no active cell exists. \(\square\)

A \(C_6\) flip changes only the orientation of an already active cell; it
does not change whether that cell is active.  Therefore the lattice
generated by the cocycles \(d_w\) cannot leave the zero-reserve wreath
face.  An activation circuit must change state choices outside the six
arcs of at least one cell and must be completed through the surrounding
flow.  This is the first unavoidable interface in the direct rotor route.

## 8. Exact remaining theorem

The preceding results reduce the direct two-sided compiler to the following
integral statement.

> **Calibrated hexagon activation theorem — open.**  For some
> \(H=\sqrt m\,\omega(m)=o(m)\), construct a Boolean solution of
> (1.3)--(1.7) such that:
>
> 1. its support has \(C_0\le(1+o(1))W/n\) cycles;
> 2. its active incidence hexagons contain a loose forest covering
>    all but \(o(W/m)\) cycle vertices and having \(o(W/m)\) forest
>    components; and
> 3. both orientations of every forest cell remain legal after the other
>    forest flips.

The last item is automatic for the physical arc equations because cells
have disjoint arc supports; it is stated to keep the sequential component
ledger explicit.  Corollary 4.2 then produces an owner-exact circulation
with \(o(W/m)\) cycles and exactly the same lower and upper prefix loads.
The direct rotor literalization has length

\[
                         W+o(W)
\]

through the protected band, with no additive seam per activation or per
hexagon.

The theorem is calibrated sharply enough to avoid both known false
routes:

* anti-dihedral closure is absent; and
* the pure-\(B\) wreath face is used only as a component-scale benchmark,
  not as a switchable endpoint.

The exact positive data are the primitive all-rank cocycle (0.4), the
factor-four depth-one capacity slack (5.9), and the sparse fractional
reserve (0.7).  The exact negative data are state-set rigidity, the
absence of a reciprocal 2-switch, the at-least-\((m+2)/3\) grouping
integrality gap, and zero router reserve in every pure-\(B\) factor.

This is the present boundary of the direct two-sided binary-rotor attack.
