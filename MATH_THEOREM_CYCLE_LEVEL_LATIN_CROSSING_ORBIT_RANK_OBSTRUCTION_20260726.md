# Cycle-level crossing layers: orbit-rank obstruction to a fragmented Beneš lift

Date: 2026-07-26

This note studies the finer cycle-level escape left open by the
matching-status Beneš dichotomy.  It gives a statewise obstruction for the
only crossing-layer model whose exact ownership law is currently proved:
each physical switch closes on the same cycle-label matching after every
crossing.

## 1. Exact cycle-label switch maps

For a physical coordinate transposition (e=\{a,b\}), put

\[
\delta_e=e_a+e_b.
\]

The exact two-cycle owner trade pairs compiler-cycle labels by
(k\leftrightarrow k+\delta_e).  A componentwise switch field is therefore
an involution

\[
S_e(k)=k+\varepsilon_e(k)\delta_e,
\qquad
\varepsilon_e(k)=\varepsilon_e(k+\delta_e).
\tag{1.1}
\]

When two physical switch slabs cross and both are required to close on their
original label matchings, exact ownership forces

\[
S_eS_f=S_fS_e.
\tag{1.2}
\]

This is the fixed-matching crossing condition already obtained by conjugating
one layer through the other.  Disjoint phase slabs avoid (1.2).  If their
**complete** layer matchings are all included in the component overlay, that
overlay is the ordinary translation cube and the same rank bound is
immediate.  No such assertion is made for an arbitrarily sparse subset of
edges chosen from disjoint-phase layers.

## 2. Orbit size is controlled by physical incidence rank

Let (O) be one connected component of the cycle-label overlay.  Let
(E(O)) consist of the physical switches whose involutions are nontrivial
somewhere on (O), and put

\[
r(O)=\operatorname {rank}_{\mathbb F_2}
       \{\delta_e:e\in E(O)\}.
\tag{2.1}
\]

### Theorem 2.1 (cycle-overlay rank bound)

Under the commuting fixed-matching law (1.2),

\[
\boxed{|O|\ge2^{r(O)}.}
\tag{2.2}
\]

#### Proof

Choose switches (e_1,\ldots,e_r) whose displacement vectors form a basis.
Their restrictions to (O) are commuting involutions.  They generate an
elementary abelian permutation group (H).

No nonempty product of the basis involutions can act identically on (O).
Indeed, if such a product were the identity, choose one constituent
(S_{e_i}) which is nontrivial at some (k\in O), and apply it first.
It adds (\delta_{e_i}).  Every remaining constituent adds either zero or
its own basis vector.  Linear independence prevents the final displacement
from vanishing.

Moreover an element of (H) which fixes one point of the transitive
(H)-orbit (O) fixes every point, because (H) is abelian.  The preceding
paragraph therefore makes the stabilizer trivial.  Hence the orbit of any
point under the basis subgroup has size (2^r) and lies in (O). \(\square\)

Let (G_O) be the graph on physical wires with edge set (E(O)).  The
binary edge-incidence vectors satisfy the standard exact rank formula

\[
\operatorname {rank}_{\mathbb F_2}{e_a+e_b:ab\in E(O)}
=|V(G_O)|-c(G_O),
\tag{2.3}
\]

where (c(G_O)) is the number of nonempty connected components.  Therefore
any connected physical route on (t) wires forces

\[
\boxed{|O|\ge2^{t-1}.}
\tag{2.4}
\]

In particular, an alternating frame-defect path of length (\ell) in one
cycle-label component forces

\[
\boxed{|O|\ge2^\ell.}
\tag{2.5}
\]

This is a statewise component bound, not a count of possible factors.

## 3. Fragmentation versus literal correction capacity

Suppose all useful cycle-overlay components are required to have size at
most (R^C) for a fixed constant (C).  Theorem 2.1 gives

\[
\ell\le C\log_2R.
\tag{3.1}
\]

Insert this into the defect-path capacity theorem.  For bounded threshold
interaction degree (\Delta), every owner-disjoint fragmented atlas has
depth-(q) cooperative correction at most

\[
O\!\left({\Delta q\log R\over R}W\right).
\tag{3.2}
\]

Thus, whenever (\Delta q\log R=o(R)), polynomial cycle-level components
cannot repair a linear target defect.  In particular they cannot repair a
linear depth-one defect for any (\Delta=R^{o(1)}).

Conversely, the path length (\ell=\Omega(R/q)) needed for linear
correction forces

\[
|O|\ge2^{\Omega(R/q)}.
\tag{3.3}
\]

At (q=1), the component is exponential in (R).  Hence the desired pair
of properties

\[
|O|=\operatorname {poly}(R),
\qquad
\ell=\Omega(R/q)
\tag{3.4}
\]

is impossible in the fixed-matching cycle-Latin model.

## 4. Why a formal Beneš network does not contradict the theorem

A Beneš network routes a long wire permutation through (O(\log R))
switching stages.  Theorem 2.1 depends on the rank of the **physical switch
edges**, not on the number of stages.  A route whose physical switch graph
connects (t) wires has incidence rank (t-1), even if its switching depth
is logarithmic.

There is one genuine escape from the theorem.  At a crossing, instead of
closing an entering matching (S) as the same matching, a true Beneš lift
may close it as the conjugate

\[
RSR^{-1}.
\tag{4.1}
\]

The generators then change with the route and need not commute.  A
nonabelian action can have an orbit of only (t) points while moving through
(t-1) independent physical edge directions.  This is exactly how an
ordinary switching network avoids an exponential state cube.

But no current compiler theorem proves that conjugated cycle-label matchings
remain legal whole-owner trades at every crossing.  The existing local
calculation gives only twelve legal states out of sixteen for two crossing
switch fields; it does not supply the routed conjugate (4.1) with independent
component controls.

Therefore an abstract Beneš wiring diagram is not yet a cycle-level Latin
construction.

## 5. Exact verdict

The proposed finer escape fails for every cycle-granular construction which
uses the presently proved fixed-matching Latin closure:

\[
\boxed{
\text{polynomial overlay components}
\Longrightarrow
\text{only }O(\log R)\text{ frame paths}
\Longrightarrow
o(W)\text{ one-sided correction capacity}.
}
\tag{5.1}
\]

The only surviving version is a genuinely conjugated, noncommuting Beneš
lift.  Its exact remaining theorem must show that every crossing transports
the cycle-label matching to (RSR^{-1}), preserves whole-owner exactness,
and retains literal all-depth traces.  No result presently in the project
establishes that theorem.
