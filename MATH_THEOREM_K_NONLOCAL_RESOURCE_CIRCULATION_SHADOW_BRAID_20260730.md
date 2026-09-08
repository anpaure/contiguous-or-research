# Nonlocal resource-circulation braids and phase-resolved shadow absorption

Date: 2026-07-30

## 0. Verdict

This note proves a reusable braid theorem for Johnson factors.

The central point is that a braid is one simultaneous head permutation, not
a sequence of factors which must remain shadow-complete after every atomic
move.  Its constituent alternating circuits may temporarily lose q1 colours
or shadow witnesses.  Only the final signed ledgers must be nonnegative.

There are three exact payment mechanisms.

1. Existing multiplicity above one is a q1 slack bank.
2. Other braid atoms can return a lost q1 token; their common selection is an
   integer resource circulation.
3. In a linearized carrier, explicitly certified boundary/compiler cells can
   absorb the residual unmatched tokens.

For fixed windows, the same old-minus-cut-plus-new identity gives an exact
shadow bank.  For arbitrary upper shadows, the exact condition is an uncut
survivor or an accepting accumulated-union path in the final braid.

For a cyclic symmetry group, all translated q1 and additive fixed-shadow
responses form a block-circulant phase matrix.  This gives an exact
phase-resolved theorem:
a locally unsafe seed atom may be globally safe after a selected collection
of translates, even though no translate is safe alone.  Full orbit closure
keeps only the trivial Fourier mode and gives the familiar physical weight
\(15/d\) on a target orbit of size \(d\).

At the post-triangle \(K=16\) state, the canonical objective has \(108\)
holes, while the stronger fixed-window phase bank still has \(123\) rows:
\[
45\text{ lower }q2+63\text{ upper }q3+15\text{ fixed upper }q4.
\]
These are nine phase blocks: eight free \(Z_{15}\)-blocks and one
size-three block.

A newer frozen construction supersedes this numerical endpoint.  The first
positive q1/deep-safe single circuit after the triangle state occurs at
length eight.  Its full \(Z_{15}\)-orbit repairs the upper orbit represented
by \(40623\), so the current canonical deficit is
\[
45+48=93.
\]
The current stronger fixed-window bank has \(108\) rows.  This exact descent
is a calibration of the general theorem, not a proof that a globally
token-cancelling packet always exists.

The reduction in Section 11 is strengthened in Sections 14--17.  The physical
Johnson port graph has a uniform surplus-expansion theorem; bounded protected
service matchings therefore extend integrally.  Independently, the Johnson
colour graphs have spectral gap exactly the ground-set size, so every bounded
zero-sum token debt has an integral Hoffman/TU routing.  A pointwise
degree--codegree inequality then gives an integral repair of every promoted
Pascal compiler halo.  These are existence theorems, not just reformulations
of the endpoint model.

What remains is literal rather than polyhedral: construct a witness-clear
PBBS/Pascal service reservoir or a path-composable router atlas whose tiles
preserve the full lower tower, arbitrary upper witnesses, residence, and the
chosen compiler pins.  No complete \(K=16\) carrier, compiler, or unconditional
all-\(k\) formula is claimed.

## 1. Physical head-permutation normal form

Let \(F\) be an oriented simple spanning two-factor of a Johnson graph.
Write its successor as \(f\), and put \(W=|V(F)|\) for its middle-owner
count.  Select distinct old transitions
\[
 e_i=(a_i,b_i),\qquad b_i=f(a_i),\qquad i\in I.
\tag{1.1}
\]
For a permutation \(\pi\) of \(I\), delete the transitions (1.1) and insert
\[
 e_i^\pi=(a_i,b_{\pi(i)}).
\tag{1.2}
\]

### Lemma 1.1: ownership and degree

The operation (1.2) preserves one outgoing and one incoming transition at
every middle owner.  It is a literal simple Johnson two-factor if and only
if:

1. every new pair in (1.2) is a Johnson edge;
2. no inserted undirected edge duplicates another inserted edge or any
   retained old edge; and
3. no directed two-cycle is created.

#### Proof

The tails in (1.1) are distinct and retain one outgoing transition.  Since
\(\pi\) permutes the distinct old heads, every head retains one incoming
transition.  Thus the successor is a permutation of the owner deck.
Johnson legality and the two simple-graph conditions are exactly the
remaining requirements.  Condition 3 is redundant if condition 2 is read
as simplicity of the entire final undirected edge set; it is displayed
because directed successor implementations commonly test it separately.
A two-cycle of the index permutation \(\pi\) is not automatically a physical
directed two-cycle; condition 3 is tested on the resulting owner arcs.
\(\square\)

The nontrivial cycles of one \(\pi\) are the alternating head-permutation
circuits.  Their tail supports are automatically disjoint, so they commute,
although they need not be legal resource moves separately.  For atoms
proposed independently, disjoint cut supports again make their product a
single permutation of the form (1.2).  If independently proposed supports
interact, their union must instead be rebuilt as one partial head assignment
and audited only after it has been completed to a permutation.

### Lemma 1.2: fragment monodromy

After deleting (1.1), start at head \(b_i\) and follow old factor edges until
the next exposed tail \(a_{\rho(i)}\).  This defines the old-fragment
permutation \(\rho\) on \(I\).  The final macro successor on fragment heads
is
\[
 i\longmapsto\pi(\rho(i)).
\tag{1.3}
\]
Consequently the final physical components are the cycles of
\(\pi\circ\rho\).

For a linear carrier, let \(\sigma\) be the partial tail-to-head matching of
the new seams: exactly one tail \(t\) is terminal and exactly one head \(h\)
is initial.  Add the formal closing seam \(t\mapsto h\), obtaining a
permutation \(\widehat\pi\) of the fragment indices.  The physical fragments
form one spanning path from \(h\) to \(t\) exactly when
\[
 c(\widehat\pi\circ\rho)=1.
\tag{1.4}
\]

#### Proof

The old fragment beginning at \(b_i\) ends at \(a_{\rho(i)}\).  Its new seam
goes to \(b_{\pi(\rho(i))}\), proving (1.3).  Cycles of this macro successor
are exactly closed physical components.  The virtual edge converts one path
to one cycle and conversely, proving (1.4). \(\square\)

Thus topology is a permutation condition, separate from q1 and shadows.

## 2. Exact final-state resource ledgers

For a Johnson edge \(e=(A,B)\), write
\[
 c^-(e)=A\cap B,\qquad c^+(e)=A\cup B.
\tag{2.1}
\]
Let \(\lambda_C^\pm\) be the old load of q1 colour \(C\).  The exact q1
change under (1.2) is
\[
\Delta_C^\pm(\pi)
=
\#\{i:c^\pm(e_i^\pi)=C\}
-
\#\{i:c^\pm(e_i)=C\}.
\tag{2.2}
\]
Therefore q1 support is preserved exactly when
\[
\boxed{\lambda_C^\pm+\Delta_C^\pm(\pi)\geq1
\quad\text{for every lower and upper q1 colour }C.}
\tag{2.3}
\]

Put
\[
 s_C^\pm=\lambda_C^\pm-1.
\tag{2.4}
\]
This is the initial q1 slack.  Formula (2.3) says that the aggregate braid
may spend at most this slack after all cross-atom repayments are included.
There is no requirement that one atom, or one prefix of the atoms, satisfy
(2.3).

### Theorem 2.1: exact fixed-shadow ledger

Fix a required depth \(q\) and a physical target \(Z\).  Let:

- \(\lambda_{q,Z}\) be its old fixed-window load;
- \(D_{q,Z}(I)\) be the number of its old occurrence-labelled windows whose
  internal edge set meets the complete cut set \(I\);
- \(G_{q,Z}(I,\pi)\) be the number of its final occurrence-labelled windows
  which use at least one new seam.

Then
\[
\boxed{
\lambda'_{q,Z}
=\lambda_{q,Z}-D_{q,Z}(I)+G_{q,Z}(I,\pi).
}
\tag{2.5}
\]
This is exact even when one window contains several cuts or several seams.

#### Proof

A final window using no new seam lies inside one retained old fragment and
is a unique old window avoiding every cut.  These contribute
\(\lambda-D\).  Every remaining final window uses a seam and is counted once
by \(G\), irrespective of how many seams it contains.  The two classes are
disjoint and exhaustive. \(\square\)

Coverage is precisely positivity of (2.5).  If all relevant cut and seam
halos are disjoint, \(D\) and \(G\) split as sums of atomic signed
signatures.  Without that separation they must be evaluated from the final
macro successor.

### Theorem 2.2: exact arbitrary-upper condition

For a proper upper target \(U\), let \({\cal W}_F(U)\) be all old contiguous
intervals with union \(U\).  After choosing the cuts and head permutation,
\(U\) remains covered if and only if:

1. some interval in \({\cal W}_F(U)\) avoids every cut; or
2. the final fragment-and-seam accumulated-union automaton has an accepting
   path using a new seam and having union \(U\).

More explicitly, if \(f'\) is the final successor, the automaton has states
\((V,R)\), where \(V\) is the current middle owner and
\(V\subseteq R\subseteq U\).  It may start at \((V,V)\), and it has the
transition
\[
 (V,R)\longrightarrow
 \bigl(f'(V),R\cup f'(V)\bigr)
\tag{2.6}
\]
whenever the new accumulated union is contained in \(U\).  A state with
\(R=U\) is accepting.  The start owner and a step counter bounded by the
length of its final physical component are implicit; this forbids traversing
a cyclic component more than once.  Fragment compression merely replaces
maximal strings of retained transitions in this automaton by labelled macro
arcs.

#### Proof

An old interval avoiding the cuts survives with its old orientation and
unchanged union.  Every other final witness uses a new seam and is a path in
the displayed automaton.  Conversely every accepting automaton path is a
literal contiguous interval of the final factor.  The component-length
counter excludes artificial repeated-cycle witnesses. \(\square\)

This condition, rather than a fixed upper width, is authoritative for the
contiguous-OR compiler.

### Residence condition

Residence is also a final-state predicate.  If every positive run shorter
than \(d+1\) meets at most one seam, let \(s,t\in\{0,1,\ldots,d+1\}\)
be the trailing and leading positive lengths, each truncated at \(d+1\).
The seam creates or exposes a forbidden positive run exactly when
\[
0<s+t<d+1.
\tag{2.7}
\]
For interacting or short fragments, one must replay the final coordinate
runs.  Atomic residence safety alone is not a composition theorem.

### Theorem 2.3: separated-port finite master and exact long-window residue

Assume the source factor has minimum positive run length \(d+1\).  Let the
selected cuts have cyclic distance greater than \(d\) on each source
component, and let every nonold seam pass the exact \(d\)-collar insertion/
deletion test of

    MATH_THEOREM_K16_SEPARATED_PORT_PERMUTATION_MASTER_20260730.md.

Write \(x_{ij}\) for the assignment choosing tail \(a_i\) to old head
\(b_j\), and put \(c_i=1-x_{ii}\).  Then:

1. the final port-permuted factor has minimum positive run length \(d+1\);
2. for every \(1\le q\le d\), every \(q\)-edge window crosses at most one
   seam, and the exact occurrence load is
   \[
   \lambda'_{q,Z}
   =\lambda_{q,Z}
    -\sum_i c_iD_{i,q}(Z)
    +\sum_i\sum_{j\ne i}x_{ij}A_{ij,q}(Z);
   \tag{2.8}
   \]
3. for \(q>d\), the exact lower fixed-window rows and all arbitrary-upper
   rows are finite path-hypergraph constraints on the same assignment.

For item 3, let \(\mathcal P^-_{q,L}\) be every physically legal directed
path pattern of exactly \(q\) selected transitions whose \(q+1\) owners have
intersection \(L\).  Let \(\mathcal P^+_U\) be every directed path pattern
with no repeated owner and at most \(W-1\) transitions whose owner union is
\(U\).  A pattern \(P\) carries the finite set \(E(P)\) of assignment
literals it uses.  Introduce a Boolean
\[
 y_P=\bigwedge_{e\in E(P)}x_e
\tag{2.9}
\]
by the standard exact linearization
\[
 y_P\le x_e\quad(e\in E(P)),\qquad
 y_P\ge1-\sum_{e\in E(P)}(1-x_e).
\tag{2.10}
\]
Then the exact deep rows are
\[
 \sum_{P\in\mathcal P^-_{q,L}}y_P\ge1,\qquad
 \sum_{P\in\mathcal P^+_U}y_P\ge1.
\tag{2.11}
\]

#### Proof

Separation makes every new positive run of length at most \(d\) cross
exactly one seam, where the collar test excludes it.  The same separation
makes every \(q\le d\) affected window belong to a unique cut and a unique
new seam, proving the occurrence-additive identity (2.8).

For larger \(q\), a selected assignment determines one literal successor at
every owner.  Hence its \(q\)-edge lower witnesses are exactly the selected
patterns in \(\mathcal P^-_{q,L}\).  Likewise its arbitrary-upper witnesses
are exactly the selected patterns in \(\mathcal P^+_U\); equivalently these
are the accepting paths of Theorem 2.2.  Equations (2.9)--(2.10) make \(y_P\)
the conjunction of the required successor choices, so (2.11) is necessary
and sufficient. \(\square\)

The path families in item 3 may be exponentially large.  Their exact lazy
form is CEGAR: materialize a candidate, replay every lower depth and every
arbitrary upper target, and add a sound disjunction of surviving or new
accepting path patterns for a missing target.  Blocking only the complete
failed permutation is always sound but weakest.  Thus separation removes
all residence and \(q\le d\) interaction terms; the path hypergraphs in
(2.11), not an unspecified seam penalty, are precisely the nonlocal residue.

## 3. The closed resource-circulation braid theorem

Let \({\cal A}\) be a collection of physically compatible braid atoms.
For an atom \(a\), let \(q_a^\pm(C)\) be its signed q1 change.  When fixed
shadow halos are additive, let \(p_a(R)\) be its signed change on a protected
fixed-shadow row \(R\).

Assume here that the atoms partition the deleted and inserted edge sets of
the final head permutation, so their q1 edit vectors add.  This holds for the
disjoint nontrivial cycles of one final permutation and for externally
composed atoms with disjoint edit supports.  If proposed atoms interact, they
must be replaced by one combined atom whose q1 vector is the literal final
\(\Delta(\pi)\) from (2.2); summing their standalone before/after vectors is
not valid.

For a selected atom vector \(x\), define
\[
 Q^\pm x=\sum_a x_aq_a^\pm,
\qquad
 Px=\sum_a x_ap_a.
\tag{3.1}
\]

### Theorem 3.1: simultaneous braid certificate

Suppose the selected atoms combine to one head permutation \(\pi\).  The
final braid is a resident shadow-preserving Johnson factor, and strictly
improves a declared hole bank, if all of the following hold:

1. Lemma 1.1 holds, and the required macro topology follows from Lemma 1.2.
2. The two q1 inequalities hold:
   \[
   Q^-x\geq-s^-,
   \qquad
   Q^+x\geq-s^+.
   \tag{3.2}
   \]
3. Every previously covered fixed target satisfies (2.5).
4. Every previously covered proper upper target satisfies Theorem 2.2.
5. Every declared hole to be repaired has a final fixed witness or an
   accepting arbitrary-upper path, as appropriate.
6. Final residence holds.
7. At least one objective hole is removed and no new objective hole is
   created.

Conversely, every final factor obtained by the head permutation satisfies
these same statements with its literal signed ledgers.  Thus, once the
physical head permutation and final accepting paths are included, the
certificate is necessary and sufficient.

#### Proof

Lemma 1.1 gives an exact spanning factor on the unchanged owner set and
Lemma 1.2 gives topology.  Equation (2.2) proves (3.2).  Theorem 2.1 proves
all fixed rows.  Theorem 2.2 proves every arbitrary upper row.  The final
run audit proves residence.  Items 5 and 7 give strict descent.  The reverse
implication reads the same literal data from any successful braid.
\(\square\)

The theorem deliberately imposes no condition on partial products of the
atoms.  Temporary q1 or shadow loss is allowed.

### Corollary 3.2: certified boundary-credit version

Suppose a later compiler supplies a finite bank \(\mathcal B\) of certified
q1-capable boundary cells.  Let \(w_{b,C}\in\{0,1\}\) assign cell \(b\) to a
compatible missing colour \(C\), with \(\sum_Cw_{b,C}\le1\).  Replacing (3.2)
in one declared palette by
\[
 \lambda_C+\Delta_C(\pi)+\sum_{b\in\mathcal B}w_{b,C}\ge1
\tag{3.3}
\]
gives an exact certificate for the **carrier-plus-boundary q1 interface**.
It does not assert that the factor alone is complete in that palette.  All
factor-internal conclusions of Theorem 3.1 remain subject to their original
rows.

#### Proof

Each certified boundary cell contributes at most its one assigned colour,
and every compatible assignment is physically realizable by hypothesis.
Thus (3.3) is exactly the old-minus-cut-plus-seam-plus-boundary occurrence
ledger. \(\square\)

## 4. Token cycles, peeling, and the exact catalyst gate

The q1 inequalities have a transparent token interpretation.  A negative
unit in row \(C\) consumes one token of colour \(C\); a positive unit returns
one.

### Lemma 4.1: one-loss/one-gain circulation

Assume every atom has q1 drift
\[
 q_a=e_{v(a)}-e_{u(a)}
\tag{4.1}
\]
on a zero-slack palette.  Draw a directed arc
\[
 u(a)\longrightarrow v(a).
\]
A selected family is q1-neutral if and only if its directed arc multigraph
is Eulerian.  Hence every nonempty neutral family is a union of directed
token cycles.

#### Proof

At a token \(C\), the total signed q1 change is indegree minus outdegree.
It vanishes at every token exactly when the selected graph is Eulerian.
Every finite Eulerian directed graph decomposes into directed cycles.
\(\square\)

With both q1 palettes, the same atom vector must be a circulation in two
token graphs simultaneously.  With several losses or gains, an atom is a
directed hyperarc and the exact condition is still the common integer
kernel (3.2).  Ordinary one-palette cycle finding is then insufficient.

### Lemma 4.2: unit-load peeling obstruction

Let \({\cal A}_0={\cal A}\).  At a peeling round, delete every atom \(a\)
for which some zero-slack q1 row \(C\) has
\[
 q_a(C)<0
 \quad\text{and}\quad
 q_b(C)\leq0\ \text{for every surviving atom }b.
\tag{4.2}
\]
Call the survivors \({\cal A}_{t+1}\).  Every q1-feasible subset of
\({\cal A}\) is contained in every survivor bank \({\cal A}_t\).  In
particular, if peeling empties the bank, no nonempty subset satisfies q1.

#### Proof

At one round, a selected atom satisfying (4.2) would make row \(C\)
negative, since no other surviving selected atom can return a unit there.
Thus no feasible subset contains that atom.  Induction over the rounds
proves the claim. \(\square\)

This is the exact meaning of the current two-round short-cycle certificate.
It is not a pairwise obstruction: the entire authenticated bank is a pointed
q1 cone.

### Corollary 4.3: catalyst necessity

If peeling empties an old bank, every feasible augmented braid using any old
atom must contain at least one atom outside that bank.  Moreover the new
atoms must return a unit to at least one exposed loss row of the selected
old closure and recursively close all debts.

For the post-triangle \(K=16\) factor, the authenticated \(1263\)-atom bank
of individually deep-safe gainful length-three through length-five circuits
peels to zero in two rounds.  Hence no subset of that bank is a nonlocal q1
braid, even before port conflicts and deep shadows are imposed.

The proof does not exclude:

- length-six or longer catalysts;
- individually non-gainful atoms;
- individually deep-unsafe atoms whose losses are restored globally; or
- a different source factor.

### Proposition 4.4: owner/diamond integer kernel

Let \({\cal D}_r\) be the bipartite graph with shores
\[
\binom{\Omega}{r-1}
\quad\text{and}\quad
\binom{\Omega}{r+1},
\]
joining \(L\) to \(U\) when \(L\subset U\) and \(|U\setminus L|=2\).
A Johnson edge is uniquely determined by its lower/upper colour pair
\((L,U)\), so it is an edge of \({\cal D}_r\).

Work on the oriented Johnson-arc universe.  For a squarefree signed edit
vector
\[
 z=1_{\rm add}-1_{\rm cut},
\]
let \(B_{\rm out}\) record arc tails, let \(B_{\rm in}\) record arc heads,
put \(B_{\rm own}=(B_{\rm out};B_{\rm in})\), and let \(B_{\cal D}\) be
lower/upper colour incidence.  Exact successor ownership and exact
two-palette q1 preservation are
\[
\boxed{
B_{\rm own}z=0,\qquad B_{\cal D}z=0.
}
\tag{4.3}
\]
With q1 slack \(s\), exact support preservation is instead
\[
B_{\cal D}z\geq-s.
\tag{4.4}
\]

#### Proof

The two owner blocks are the signed outgoing and incoming changes.  Their
vanishing preserves one outgoing and one incoming successor at every owner.
The two colour blocks are exactly the signed changes of the intersection and
union loads.
Therefore the displayed kernel and inequalities are equivalent to the
literal degree and q1 ledgers. \(\square\)

This is the correct algebraic home for a nonlocal Markov or Graver braid.
The absence of a short safe projected head cycle does not exclude a sum of
unsafe circuits lying in the common integer kernel (4.3).

### Theorem 4.5: compensation matching and simultaneous macros

Fix a selected finite atom family and take the disjoint union of the lower
and upper q1 row sets.  For every atom \(a\) and row \(C\), replace its net
integer drift \(q_a(C)\) by

- \(q_a(C)\) occurrence-labelled gain tokens if \(q_a(C)>0\); or
- \(-q_a(C)\) occurrence-labelled debt tokens if \(q_a(C)<0\).

Also create \(s_C\) initial slack tokens in row \(C\).  Then the aggregate
q1 inequalities (3.2) hold if and only if every debt token can be matched
injectively to either an initial slack token in the same row or a gain token
in the same row.

Given such a matching, draw a dependency arc \(b\to a\) whenever a debt of
atom \(a\) is matched to a gain of atom \(b\).  There is an ordering of the
atoms for which both q1 palettes are safe after every prefix if and only if
the matching can be chosen with an acyclic dependency digraph.  More
generally, for any chosen matching, its strongly connected components can be
fired simultaneously in a topological order of the condensation; both q1
palettes are safe at every macro boundary.

#### Proof

For each row \(C\), the matching exists exactly when
\[
 \sum_a(-q_a(C))^+\leq s_C+\sum_a(q_a(C))^+,
\tag{4.5}
\]
which is precisely (3.2).  The rows are disjoint, so their matchings combine.

If the dependency digraph is acyclic, fire atoms in a topological order.
Every debt at the current atom is paid by initial slack or by an unmatched
gain of an earlier provider, so the running load never drops below one.
Conversely, from any prefix-safe ordering, scan atoms in that order and
match each new debt rowwise to an unused initial slack token or an unused
gain already created.  Prefix safety guarantees that this greedy matching
never fails, and every dependency points forward in the ordering.  Finally,
in an arbitrary matching, every debt of a condensation component is paid by
slack, a gain in the same component, or a gain in an earlier component.
Firing the whole component at once therefore preserves q1 at its boundary.
\(\square\)

The SCC statement is relative to the chosen matching; it does not claim a
canonical or inclusion-minimal macro over all matchings.  It explains how a
closed nonlocal packet can exist even when no constituent atom is safe.
For additive fixed-shadow occurrence rows the same token bookkeeping may be
added.  Arbitrary-upper witnesses are different: a new accepting interval
may use several atoms jointly.  Their dependency object is a support
hypergraph of accepting paths, and prefix shadow safety is exactly the
survivor/acceptance test of Theorem 2.2 at each desired macro boundary, not an
ordinary token-cycle condition.

## 5. Exact router completion by Hoffman cuts

There is a stronger positive theorem when q1 compensation is supplied by a
prevalidated router library.

Let token vertices be exact q1 colours.  An oriented router arrow
\[
 u\longrightarrow v
\]
has signed token drift \(e_v-e_u\).  Let \(d\) be the aggregate signed drift
of the already selected service atoms, using the same incidence convention.
Let \(R\) be a directed router graph with integral arc capacities \(u_e\).
Assume that every capacity-feasible router selection is physically
compatible with the service packet and is already certified for degree,
residence, and the protected shadows.

### Theorem 5.1: token-flow absorber

There is an integral router flow \(y\), \(0\leq y\leq u\), which restores
the exact token balance
\[
 By=-d
\tag{5.1}
\]
if and only if
\[
 \sum_vd(v)=0
\tag{5.2}
\]
and, for every token set \(S\),
\[
 \boxed{
 d(S)\leq u(\delta^+(S)).
 }
\tag{5.3}
\]
Here \(B(e_{u\to v})=e_v-e_u\), and \(\delta^+(S)\) is the set of router
arcs leaving \(S\).  Complementary sets give the reverse inequalities.
Whenever a completion exists, there is an integral one.

#### Proof

Equation (5.2) is necessary because every incidence column sums to zero.
For a flow satisfying (5.1),
\[
-d(S)=y(\delta^-(S))-y(\delta^+(S)),
\]
which gives (5.3).  Conversely these are the Hoffman circulation cut
conditions after adjoining the prescribed vertex imbalances.  Directed
incidence matrices are totally unimodular, so integral capacities and
imbalances admit an integral solution. \(\square\)

Every unit of router flow changes the \(\ell_1\) imbalance by at most two.
Therefore every completion has total flow
\[
\boxed{\sum_e y_e\geq\frac12\|d\|_1.}
\tag{5.4}
\]
For unit capacities this is the same lower bound on the number of selected
router arrows.

If the service packet is already safe on the other q1 palette and the
routers are neutral there, Theorem 5.1 completes both q1 ledgers.  Otherwise
the same physical router vector must also satisfy the second literal
inequality in (3.2).  No scalar balance, and no separate choice of a second
flow, replaces those coupled rows.

This is a genuine construction lemma: once a shadow-neutral router network
with Hoffman expansion is supplied, q1 compensation is automatic and
integral.

### Corollary 5.2: service-plus-router absorber

Let a physically compatible service packet satisfy topology, residence, all
fixed lower rows, all arbitrary-upper survivor/absorber rows, and the other
q1 palette, but have imbalance \(d\) in the declared router palette.
Suppose a prevalidated router network:

1. is degree-, shadow-, and other-palette-neutral relative to that service
   packet;
2. preserves residence under every capacity-feasible integral flow; and
3. satisfies (5.2)--(5.3).

Then an integral router flow exists, and the union of the service packet and
router flow is a valid braid under Theorem 3.1.  If the service packet
strictly covers an old hole, the resulting braid is a strict descent.

#### Proof

Theorem 5.1 supplies an integral q1 repayment.  The router hypotheses leave
all other rows of Theorem 3.1 unchanged.  Applying that theorem proves the
claim. \(\square\)

## 6. Cyclic phase compression and Fourier rank

Let \(\Gamma=Z_n\) act on the factor, atoms, and target rows.  Let target
block \(O_j\) have size \(d_j\mid n\).  For a braid type \(p\), let
\[
 k_{jp}(a)
\]
be the signed final-minus-old occurrence change at target phase
\(a\in Z_{d_j}\) caused by the phase-zero atom.  Destroyed witnesses are
included.  Let \(x_{p,s}\) select translate \(s\in Z_n\).

Assume the translated supports are compatible and their fixed-window
ledgers add.  Then:

### Theorem 6.1: block-circulant orbit absorber

The exact final phase load is
\[
\boxed{
 m'_j(a)
 =
 m_j(a)
 +\sum_p\sum_{s\in Z_n}k_{jp}(a-s)x_{p,s},
 \qquad a\in Z_{d_j}.
 }
\tag{6.1}
\]
The same identity holds for literal q1 phase rows.

#### Proof

Translation by \(s\) shifts the target phase of every occurrence by \(s\)
modulo the target stabilizer.  Signed occurrence changes add over compatible
atoms.  Summing the translated signatures gives (6.1). \(\square\)

Thus the phase matrix is block-circulant.  Over the complex numbers, the
discrete Fourier transform decomposes it by characters of \(Z_n\).  If
\(\widehat k_{jp}(\chi)\) denotes the Fourier response at character \(\chi\),
then the phase-matrix rank is the sum of the ranks of the response matrices
\[
 [\,\widehat k_{jp}(\chi)\,]_{j,p}
\tag{6.2}
\]
over all characters which occur in the target blocks.  This is an exact
rank test, not an entropy heuristic.

### Corollary 6.2: full-orbit closure

If all translates of one free seed atom are selected, \(x_{p,s}=1\), every
nontrivial Fourier mode vanishes and every target phase in \(O_j\) changes
by
\[
\boxed{
 \frac{n}{d_j}\sum_{a\in Z_{d_j}}k_{jp}(a).
 }
\tag{6.3}
\]
If the atom has a nontrivial stabilizer, replace \(n\) by the number of
distinct translates.

For \(Z_{15}\), the multiplier is one on a free size-fifteen block and five
on the size-three block represented by \(46811\).

Corollary 6.2 proves the promised global cancellation mechanism for q1 and
the additive fixed-window rows.  A base atom need not preserve literal
phases.  Its full orbit is safe in those rows exactly when the orbit-averaged
signed inequalities are safe in every resource block, together with the
physical port and residence conditions.  Arbitrary-upper safety is still the
accepting-path condition of Theorem 2.2; it cannot in general be inferred
from an orbit-averaged fixed-depth signature.

## 7. The 123-row K16 phase bank and capacity

Immediately after the triangle-orbit repair, the objective rows are:
\[
\begin{array}{c|c|c}
\text{kind}&\text{representatives}&\text{physical mass}\\ \hline
\text{lower fixed }q2&
33337,33609,34069&45\\
\text{upper arbitrary rank }11&
36343,36599,39791,40623,46811&63.
\end{array}
\tag{7.1}
\]
The canonical objective mass is \(108\).

Fixed replay also has the free upper-\(q4\) block represented by \(40443\),
of mass fifteen.  Hence the stronger fixed-window bank is
\[
\boxed{45+63+15=123.}
\tag{7.2}
\]
It consists of eight free phase blocks and the one size-three block
\(46811\).  The \(q4\) block is not a canonical objective hole, because all
its targets have longer union witnesses.  It is nevertheless a valid
strong preservation/service bank for a fixed-window braid.

This is only the **initial** service bank.  A candidate cut set can destroy
previously valid witnesses and thereby create dynamic casualty rows.  Those
rows enter (2.5) and (6.1), with their literal phases, in addition to the
nine displayed blocks.  Scalar service of (7.2) alone is never a
preservation certificate.  For the canonical arbitrary-upper compiler the
initial bank is the \(108\) rows in (7.1); the optional \(q4\) block belongs
only to the stronger fixed-window formulation.

For a noninvariant physical braid, all \(123\) literal inequalities in
(7.2) must be retained.  For a full orbit packet, Corollary 6.2 collapses
them to nine scalar support rows with weights one and five.

### Lemma 7.1: universal fixed-window seam capacity

If a final factor has \(S\) new seam edges, then the number of \(q\)-edge
windows containing at least one new seam is at most \(qS\).  Consequently a
strict fixed-window repair of (7.2) satisfies
\[
\begin{aligned}
 2S_{BB}&\geq45,\\
 3S&\geq63,\\
 4S&\geq15,\\
 9S&\geq123.
\end{aligned}
\tag{7.3}
\]
In particular,
\[
\boxed{S_{BB}\geq23.}
\tag{7.4}
\]

#### Proof

In a cyclic word, one edge lies in exactly \(q\) windows of \(q\) edges; in
a path it lies in at most \(q\).  The union bound over new seams gives
\(qS\).  Every old hole needs a final witness containing a new seam.  The
lower targets contain the distinguished coordinate, so an intersection
witness cannot contain an opposite-shore state; every lower provider is a
\(BBB\) window and uses a new \(BB\) seam, where \(B\) denotes the
top-containing shore in the asymmetric-factor artifacts.  (Section 10 uses
the opposite local letter convention.)  Summing the depth-two, -three,
and -four slot bounds gives (7.3). \(\square\)

If \(S_{BB}=23\) and a repair succeeds, there are only \(46\) changed
lower-\(q2\) windows for \(45\) old holes.  After all holes are filled, the
sum of

- newly exposed lower targets which also need a new witness, and
- duplicate, wrong-rank, or otherwise unusable service slots

is at most one.  This is the sharp scalar statement; it does not assert that
the forty-five required targets admit an SDR into those slots.

For an equivariant repair, three free lower blocks require at least two
\(BB\) seam orbits, hence at least \(30\) physical \(BB\) seams.

The upper arbitrary-width problem may evade the fixed \(3S\) bound by using
longer intervals.  It cannot evade (7.4).  A seam upper colour is rank nine
and is contained in only
\[
\binom{7}{2}=21
\]
rank-eleven targets, so its arbitrary-upper eligibility is still finite.

### Post-length-eight update

The length-eight orbit discharges the free upper block represented by
\(40623\).  The current row banks are therefore:
\[
\begin{aligned}
\text{canonical objective: }&45+48=93,\\
\text{strong fixed bank: }&45+48+15=108.
\end{aligned}
\tag{7.5}
\]
The lower bound (7.4) is unchanged.

The \(123\)-row system remains the correct phase calibration for the
post-triangle source requested in the problem.  It is not the current
post-length-eight deficit.

## 8. Boundary-funded component braids

The \(k=13\) and \(k=15\) seams instantiate the same token theorem with a
boundary bank.

Assume a factor is exact in one chosen q1 palette, meaning that every colour
in that palette occurs exactly once (the lower palette in the compiler
applications), and has \(c\) physical cycles.  Cut one edge from each cycle
and join the resulting segments into one path with \(c-1\) seams.
Let \(R\) be the \(c\) distinct deleted colours in that palette and let
\(Q\) be the corresponding seam-colour multiset.

### Proposition 8.1: recycle-or-boundary law

If the compiler has at most two q1-capable boundary cells, then a necessary
condition is
\[
\boxed{|R\cap Q|_{\rm distinct}\geq c-2.}
\tag{8.1}
\]
More exactly, form a bipartite graph from the selected seams and boundary
cells to the deleted colours:

- a seam is adjacent to the cut colour equal to its q1 colour;
- a boundary cell is adjacent to the cut colours compatible with its
  endpoint halo.

The opened carrier has the declared carrier-plus-boundary q1 interface if
and only if this graph has a matching covering all \(c\) deleted colours.
This certifies only that palette interface, not simultaneous compiler
feasibility.

#### Proof

Every deleted colour had one old occurrence.  A seam restores it exactly
when the seam has that colour; a foreign or duplicated seam colour does not
restore another deleted token.  At most two unmatched colours can be placed
at the two boundary cells, proving (8.1).  The complete statement is exactly
the assignment of each missing token to a distinct seam or boundary cell,
hence bipartite matching. \(\square\)

At \(k=13\), two source components are joined by one seam and the remaining
colour is absorbed at the boundary/compiler.  The successful seam preserves
all upper shadows and leaves the exact lower compiler feasible.

At \(k=15\), two different calibrations are useful.  The nine-cycle
intermediate seam theorem uses a global donor SDR: eight seam colours
recycle eight of nine deleted colours and the last token is assigned to a
compatible boundary.  In the final exact two-cycle certificate, the foreign
seam recycles neither deleted colour; the two colours \(18553,18033\) occupy
the two boundary channels.  Individual joins are therefore not required to
be self-paying.  Both calibrations are boundary-funded instances of
Corollary 3.2.

The matching condition proves q1 only.  Common lower compiler feasibility,
all shadow survivors, residence, and endpoint chronology remain separate
conditions.

## 9. Calibration by the length-eight orbit

Every census statement in this section is scoped to the authenticated
positive-provider, positive-residence, pairwise-cut-separated directed
port-cycle catalogue.  The frozen audits do not claim complete classification
over arbitrary head permutations.

On the post-triangle factor, the exact positive-provider census proves:

- no positive q1/deep-safe single circuit through length seven;
- at length seven, the q1-pruned provider traversal finds no q1-safe circuit
  at all;
- at length eight, exactly fifteen q1/deep-safe unit-gain circuits exist.

The fifteen length-eight circuits form one free \(Z_{15}\)-orbit and use
\(120\) distinct cuts.  Their successor permutations commute.  Simultaneous
literal replay preserves both q1 palettes and positive residence, leaves
the lower deficit \(45\), and changes the upper arbitrary deficit
\[
63\longrightarrow48.
\]

For one representative, the negative q1 charges hit source colours of load
two.  Thus this particular construction is slack-funded: it spends existing
q1 multiplicity rather than demonstrating a nontrivial common token
circulation.  It nevertheless proves that the length-seven barrier is local,
not an invariant of the source factor.

Frozen artifacts:

    MATH_THEOREM_K16_ASYMMETRIC_LENGTH8_ORBIT_REPAIR_20260730.md
    scratch/k16_asymmetric_len8_orbit_repair_20260730.json
    scratch/k16_asymmetric_len8_orbit_repair_20260730.audit.json

Their factor and audit hashes are
\[
\begin{split}
&6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204,\\
&3e9c62c66d85ff6a8c242897a80dc2841eaf4fca9e908f50b8f1f5b697576e87.
\end{split}
\]

The old length-three through length-seven catalogues belong to the
pre-length-eight source.  They cannot be transferred to the new factor
without rebuilding its seam and witness tables.

### The new-source length-nine warning

The exact census was rebuilt on the length-eight-orbit factor.  It finds:

- no positive q1-safe cycle at lengths three through seven;
- \(45\) q1-safe length-eight cycles, all failing the advertised
  lower-\(q2\)/upper-\(q3\) safety test; and
- \(30\) length-nine cycles passing q1 and that narrow two-depth test.

The thirty length-nine cycles form two \(Z_{15}\)-orbits.  Their compatibility
graph has maximum packing seven.  The packing gains seven missing
upper-\(q3\) targets, but independent full replay creates
\[
14\text{ arbitrary upper-rank-10 holes}
\quad\text{and}\quad
7\text{ lower-}q3\text{ holes}.
\tag{9.1}
\]
Its ledger is
\[
\begin{array}{c|rrrr}
 &Lq2&Uq2&Lq3&Uq3\\ \hline
\text{holes after packing}&45&14&7&41.
\end{array}
\tag{9.2}
\]
Thus seven desired gains cost twenty-one new opposite-depth holes.  This is
a literal counterexample to calling preservation of only lower \(q2\) and
upper \(q3\) an all-depth braid certificate.

Theorem 3.1 already has the necessary scope: every previously covered lower
fixed target at every required depth and every arbitrary upper target at
every rank must survive or be absorbed.  A proof-safe next **standalone
single-cycle** census must go to length at least ten and include upper
\(q2\), lower \(q3\), and the remaining depths in its signed pruning.
Compound packets made from individually unsafe cycles of lengths at most
nine remain open, because their new opposite-depth debts may cancel only in
aggregate.

Frozen new-source replay:

    scratch/k16_asymmetric_len8_orbit_source_len9_full_objective_20260730.audit.json
    scratch/k16_asymmetric_len8_then_len9_maxpacking_repair_20260730.json
    scratch/k16_asymmetric_len8_then_len9_maxpacking_repair_20260730.audit.json

Their SHA-256 values are
\[
\begin{split}
&ce024402a264ff994b5b6583702e7553dd9a53703fbfeed835f2c2695662af72,\\
&81118d55bc16a7b80ae5f95355a0d4a81cdc841dad6fe839cb16501c38b36473,\\
&5ea654e46119b11f2f9e451841adfd034a2e9ba1873b8addf467f1fe66e860f4.
\end{split}
\]

## 10. The bounded-state colourful Hamilton prototype

The theorem

    MATH_THEOREM_K16_JOINT_QUOTIENT_PATH_PHASE_HISTORY_MODEL_20260730.md

gives a compact finite realization of the preceding resource-braid algebra
inside the equivariant two-rail, one-block-per-shore class.

For \(K=2R\), put \(n=K-1\) and
\[
M=\frac1n\binom nR.
\]
A quotient transition option
\[
e=(u,v;a,b,\delta)
\tag{10.1}
\]
records its source and target owner orbits, deleted and inserted labels, and
relative phase shift.  If the physical source phase is \(g\), the target
phase is \(g+\delta\).  Thus phase is part of the arc; it is not a
postselected vertex gauge.

At \(K=16\), the exact catalogue has
\[
54856
\]
selectable option arcs on \(858\) quotient owner vertices.  Positive
residence at delay three is encoded by \(2574\) history variables storing
the last three inserted coordinates in the current canonical frame.

### Theorem 10.1: dictionary with the braid theorem

Fix a baseline quotient factor \(x^0\) and a selected quotient tour \(x\).
Put
\[
z=x-x^0
\tag{10.2}
\]
on the union of their transition-option arcs.  Then:

1. quotient successor rows are the two directed systems
   \(B_{\rm out}z=0\) and \(B_{\rm in}z=0\);
2. the \(1528\) q1 label-orbit rows are the orbit-weighted quotient form of
   \(B_{\cal D}z\geq-s\); after dividing a row by its positive stabilizer
   multiplicity, these are exactly the unweighted support rows in the joint
   model;
3. the circuit/subtour rows and unit-voltage condition are the macro
   topology and one-physical-lift conditions;
4. the last-three history transition is the exact residence automaton; and
5. each selected option is one full physical edge orbit and hence one
   full-orbit column for edge-local degree and q1 resources.  A \(q\ge2\)
   shadow response belongs to a selected \(q\)-option history, not to one
   option column.

Consequently any solution of the joint quotient-history model which also
satisfies all rows in Theorem 3.1 is a literal resource-circulation braid.
Conversely, every equivariant one-block-per-shore braid in that option
catalogue with unit total voltage maps, after the allowed multiplier
normalization to voltage one, to such a colourful Hamilton solution.

#### Proof

The first two claims are the directed owner and orbit-weighted colour
incidence identities of Proposition 4.4.  Cumulative option voltages
reconstruct the physical phase;
unit total voltage makes the quotient tour traverse every physical member
of every free owner orbit.  The directed-history theorem says the last-three
state is necessary and sufficient for positive residence four.  Since one
quotient option lifts to all its translates, its edge-local resource column
is exactly the trivial-mode/full-orbit column of Corollary 6.2.  Deeper
resources are supplied by Proposition 10.2.  The soundness and completeness
statements follow. \(\square\)

This explains both the strength and the limitation of the compact model.
It handles chronology, phase, q1, residence, and Hamilton topology jointly.
Because every option is a full orbit, it does not express the nontrivial
Fourier phase schedules \(x_{p,s}\) of an arbitrary noninvariant physical
braid.  The exactly-one \(A\to B\) and one \(B\to A\) rows also restrict it
to one block per shore.

### Proposition 10.2: exact deeper-shadow extension

For a selected option tour, the last \(q\) options and their accumulated
voltage determine every fixed \(q\)-edge intersection or union window.
Therefore all required fixed lower rows through any declared depth \(H\)
can be added by a finite history product of depth \(H\).

For arbitrary upper coverage, first form the \(n\)-fold physical lift of the
selected quotient tour.  Its vertices are \((u,g)\), and a selected option
\(e=(u,v;a,b,\delta)\) enables
\[
\bigl(u,g\bigr)\longrightarrow\bigl(v,g+\delta\bigr).
\tag{10.3}
\]
For a proper upper target \(U\), put an **auxiliary** reachability automaton
on this enabled lift.  A state records the lifted owner, a start marker, a
counter at most \(W-1\), and the accumulated union \(R\subseteq U\).
Every visited physical owner must be contained in \(U\), and acceptance is
\(R=U\).  Requiring one accepting auxiliary path for each required target
orbit gives an exact finite mixed Hamilton-plus-reachability formulation for
all rows of Theorem 3.1.

#### Proof

An option and the current phase determine the literal physical transition.
Induction reconstructs the preceding \(q\) owners, so their intersection or
union is local in the declared option-history product.  The lift (10.3) is
the literal physical successor.  The auxiliary automaton is therefore
exactly Theorem 2.2, including starts at any physical phase.  It may span
several quotient laps, but the \(W-1\) counter prevents a repeated physical
owner. \(\square\)

### Corollary 10.3: finite orbit-braid prototype

Fix \(R,d,H\), a finite required target family, and one equivariant baseline
inside the two-rail option catalogue.  Assume
\[
M=C_{R-1}\ge d+1,
\tag{10.4}
\]
so the distinguished top coordinate's one-block run is resident; otherwise
add its run constraint explicitly.  Consider the finite mixed system
consisting of:

1. a cluster-Hamilton option tour with the last-\(d\) insertion histories;
2. the last-\(H\) option/voltage histories needed for the fixed lower rows;
   and
3. one enabled auxiliary path/flow in the \(n\)-fold physical lift for each
   required proper upper target orbit.

Then an equivariant braid satisfying owner degree, one-block topology, unit
voltage, positive residence, both q1 palettes, every declared lower depth,
and every declared arbitrary upper target exists **if and only if** this
mixed system is feasible.  Relative to the baseline, the projected option
incidence vector is a squarefree integral resource circulation of
Theorem 3.1.

#### Proof

Theorem 10.1 gives the bijection before deeper shadows.  Proposition 10.2
adds exact option-history recognizers for lower rows and exact physical-lift
recognizers for upper rows without changing the underlying owner choice.
Condition (10.4) handles the top coordinate; the directed histories handle
all old coordinates.  Projecting a successful tour and subtracting the
baseline preserves the directed owner rows and gives its literal signed
resource vector.  Conversely, lift any equivariant braid in the declared
class, record its local histories, and mark one physical accepting interval
for each covered upper target; these data form the required mixed
certificate. \(\square\)

The corollary is an exact finite formulation, not a polynomial-size or
satisfiability theorem.  The upper automata are auxiliary flows, not another
one-state-per-owner Hamilton product: physical phase shifts after a quotient
lap when the voltage is one.  This also explains the phase boundary cleanly:
one option column is already a full physical edge orbit and therefore
represents only the trivial Fourier mode for edge-local rows.  A braid using
selected physical translates requires the larger block-circulant system
(6.1), not this quotient specialization.

For the post-triangle \(K=16\) calibration, the strong \(123\)-row physical
bank therefore enters this full-orbit model as nine target-orbit
colour/acceptance blocks, with physical masses

\[
15,15,15,15,15,15,15,15,3.
\tag{10.5}
\]

The size-three block is not interchangeable with a free block: a generic
full \(Z_{15}\) response has the fivefold coefficient of Corollary 6.2.
After the length-eight repair, the corresponding strong bank has seven free
blocks and the size-three block.  If one instead permits a noninvariant
selection of translated packets, these compressed rows must be expanded
back to their \(123\), respectively \(108\), literal phase inequalities.

The model as presently written includes q1 and residence but deliberately
leaves the deeper products to fail-closed replay or later constraints.  The
new-source length-nine packing proves that lower \(q2\) plus upper \(q3\)
does not suffice: all lower depths and arbitrary upper ranks must be present.

This joint quotient-history master is therefore the clean finite prototype
for the general braid theorem.  A SAT or flow result for a projection of it
inherits exactly the rows actually imposed, and no others.

## 11. Reusable all-k construction lemma

The preceding results isolate one parameterized statement.

### Definition 11.1: RCBA

For a resident near-factor \(F\), let
\({\rm RCBA}(F,d,{\cal H})\) mean that there are:

1. a cut set and a head permutation satisfying Lemmas 1.1--1.2;
2. a q1 payment using initial slack and a common token circulation, with
   explicitly certified boundary cells allowed only in the terminal relative
   interface variant of Corollary 3.2;
3. phase-resolved fixed-shadow service satisfying Theorem 2.1;
4. an uncut survivor or accepting path for every required arbitrary upper
   target;
5. a final residence certificate at delay \(d\); and
6. strict reduction of the canonical hole bank \({\cal H}\), with no new
   canonical hole.

### Theorem 11.2: finite descent

Suppose a class of finite factors is closed under the boundary-free RCBA
moves, and every member with a nonempty canonical hole bank admits such a
move.  Repeated RCBA descent reaches a complete carrier after at most the
initial number of holes.  A boundary-funded relative move may instead be
used once at the terminal carrier/compiler interface; it is not an internal
factor-preserving descent step.

#### Proof

The canonical hole count is a nonnegative integer and decreases strictly at
each move.  Closure keeps every successor inside the stated class.
\(\square\)

### Corollary 11.3: exact-word interface

If the terminal carrier is a middle permutation, is upper-complete, and its
full pinned compiler \({\rm COMP}_d(T)\) is feasible, then the established
compiler theorem produces a contiguous-OR word of length
\[
\binom{k}{\lfloor k/2\rfloor}+d.
\]

Thus a uniform proof of RCBA existence for the relevant PBBS or MMM
near-factor class, together with the independent compiler condition, would
give a reusable all-\(k\) construction route.

This is a rigorous reduction, not an existence proof.  In particular:

- component connectivity alone does not imply RCBA;
- scalar orbit capacity does not imply the phase inequalities;
- q1 token flow does not imply shadow or residence safety; and
- a complete carrier does not imply the common compiler.

## 12. Sharp remaining K16 gate

For the current post-length-eight factor, the immediate theorem target is:

> Find a compatible physical or phase-selected braid which covers the three
> remaining free lower-\(q2\) blocks and the four remaining upper blocks
> \(36343,36599,39791,46811\), preserves every old critical target, satisfies
> both literal q1 inequalities, and retains positive residence.

In a strong fixed-window implementation, also preserve or restore the
\(40443\) q4 block.  In the canonical arbitrary-upper implementation, that
block needs only an accepting longer witness.

The exact algebraic search hierarchy is:

1. rebuild a signed catalyst/service catalogue on the current
   post-length-eight source; pre-length-eight length-six and length-seven
   columns do not transfer automatically;
2. select a physical or orbit-phase service packet, using the separated-port
   master of Theorem 2.3 when its hypotheses are imposed;
3. if its q1 imbalance is \(d\), seek a compatible two-palette repayment.
   Hoffman (5.3) is sufficient directly only when the routers are neutral on
   the other palette; otherwise the same router vector must satisfy the
   second palette rows as well, and two separate flow tests do not suffice;
4. impose macro monodromy, residence, every dynamic lower casualty row, and
   every arbitrary-upper accepting-path row; and
5. finish with the independent full compiler.

No theorem currently guarantees this full RCBA existence package.  Section 15
does, however, settle the abstract router-expansion and integrality step with
an exact constant.  The unresolved gate is the physical lift: the required
service/router tiles must be squarefree, mutually composable, all-depth
witness-transparent, residence-safe, and compiler-pin-transparent.

## 13. Scope and provenance

The abstract identities and conditional theorems are independent of a finite
search.  All numerical \(K=13,15,16\) calibrations, catalogue sizes, deficit
counts, and hashes depend on the listed frozen artifacts:

    MATH_K16_COMPOUND_SHORT_CYCLE_Q1_NO_GO_20260730.md
    MATH_K16_CURRENT_EXACT_FRONTIER_20260729.md
    MATH_THEOREM_K16_ASYMMETRIC_LENGTH8_ORBIT_REPAIR_20260730.md
    MATH_THEOREM_K16_JOINT_QUOTIENT_PATH_PHASE_HISTORY_MODEL_20260730.md
    MATH_THEOREM_K16_SEPARATED_PORT_PERMUTATION_MASTER_20260730.md
    MATH_THEOREM_K_FACET_DERIVATIVE_NINE_ORBIT_ABSORBER_AND_TRIANGLE_BASE_20260729.md
    MATH_THEOREM_AD_K16_ASYMMETRIC_NINE_ORBIT_SEAM_WIDTH_AND_ONECUT_NOGO_20260729.md
    MATH_K13_EXACT_1719_CERTIFICATE_20260728.md
    MATH_THEOREM_K_NINE_CYCLE_COLOURED_SEAM_MASTER_AND_CUT_KERNEL_20260729.md

The length-seven statement is scoped to the authenticated positive-provider,
positive-residence, pairwise-cut-separated port-cycle catalogue.  It is not
an architecture-wide no-go.  The global two-round peeling result is scoped
to the \(1263\) individually deep-safe gainful length-three through
length-five atoms.

No web search, local heavy computation, SAT run, or remote job was used in
preparing this theorem note.

### Dependency hashes, live-source caveat, and exact scope

The byte-level dependencies used for the finite calibrations are:

    UNPINNED-LIVE  MATH_THEOREM_K16_SEPARATED_PORT_PERMUTATION_MASTER_20260730.md
    dd404a9ab078ed7fe7ea26329adecf1527ee333fbc999adfb0558cf12105176e  MATH_THEOREM_K16_JOINT_QUOTIENT_PATH_PHASE_HISTORY_MODEL_20260730.md
    33793f75965150688a3c2acf9c6132384d537aca86c4ab86237cb551cd7e4789  MATH_K16_COMPOUND_SHORT_CYCLE_Q1_NO_GO_20260730.md
    7edfabb845715e93f7a56ca3003cf786d91c9e1fc7ccfb815277b23f0f49b5fc  MATH_K16_CURRENT_EXACT_FRONTIER_20260729.md
    6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204  scratch/k16_asymmetric_len8_orbit_repair_20260730.json
    3e9c62c66d85ff6a8c242897a80dc2841eaf4fca9e908f50b8f1f5b697576e87  scratch/k16_asymmetric_len8_orbit_repair_20260730.audit.json
    ce024402a264ff994b5b6583702e7553dd9a53703fbfeed835f2c2695662af72  scratch/k16_asymmetric_len8_orbit_source_len9_full_objective_20260730.audit.json
    81118d55bc16a7b80ae5f95355a0d4a81cdc841dad6fe839cb16501c38b36473  scratch/k16_asymmetric_len8_then_len9_maxpacking_repair_20260730.json
    5ea654e46119b11f2f9e451841adfd034a2e9ba1873b8addf467f1fe66e860f4  scratch/k16_asymmetric_len8_then_len9_maxpacking_repair_20260730.audit.json
    415891be220e7fb18ac51eaf23a2d2eef7fd5a8e0cf170f879b6ac4f591feec2  scratch/audit_joint_rail_quotient_history_model_20260730.py

The separated-port note was being edited concurrently during the final audit
and changed byte hash more than once.  No preserved copy of the version first
cited here was identified, so this dependency is deliberately not presented
as hash-closed.  Sections 14--17 use only its abstract separated-collar
statement, restated with complete hypotheses in Theorem 14.4; their proofs do
not depend on a finite separated-port artifact.

The exact logical boundary is:

- The identities and conditional portions of Sections 1--6, including
  Theorems 2.1--2.3, and the reductions in Sections 10--11 are abstract
  proofs, not finite existence claims; the numerical calibrations embedded
  in those sections still depend on the frozen artifacts.
- The separated-port theorem is necessary and sufficient only inside the
  declared \(d\)-separated assignment class; (2.8) is local only for
  \(q\le d\), while (2.11) is the exact nonlocal completion.
- The length-eight and length-nine counts are complete only for their frozen
  positive-provider, positive-residence, pairwise-cut-separated port-cycle
  catalogues, not for arbitrary head permutations or compound packets.
- The \(123\) rows are the post-triangle strong fixed-window service bank,
  \(108\) is its canonical lower-plus-arbitrary-upper bank, and \(93\) is the
  current post-length-eight canonical deficit.  Every candidate still adds
  its own dynamic casualty rows.
- The base joint quotient model is exact only for the equivariant
  one-A-block/one-B-block class with q1, unit voltage, and positive
  residence.  Deeper completeness requires the additional option histories
  and physical-lift accepting paths of Proposition 10.2.
- No remaining \(K=16\) absorber, feasible full compiler, optimal
  length-\(12873\) word, unconditional RCBA existence theorem, or all-\(k\)
  result is claimed.

The hash of this theorem note itself is intentionally recorded externally
after the final write, since embedding it here would change the hashed file.

## 14. Physical Johnson expansion and protected integral completion

The first positive existence input is intrinsic to the Johnson graph.  It is
important that the theorem is applied on the physical lift.  Orbit
identification may introduce stabilizer coefficients and need not preserve
total unimodularity.

For \(r\geq3\), put

\[
 N=\binom{2r}{r},\qquad {\cal V}=\binom{[2r]}r.
\tag{14.1}
\]

Let \({\mathbb B}_r\) be the balanced bipartite graph with left and right
copies of \({\cal V}\), in which \(X_LY_R\) is an edge precisely when

\[
 |X\mathbin\triangle Y|=2.
\tag{14.2}
\]

Thus \({\mathbb B}_r\) is the physical tail--head adjacency graph of
\(J(2r,r)\).  Relabelling the right shore by the successor of any spanning
factor does not change this graph.

### Theorem 14.1: Johnson port surplus

For every nonempty \(S\subseteq{\cal V}_L\),

\[
 \boxed{|N_{{\mathbb B}_r}(S)|
 \geq \min\{N,|S|+r-1\}.}
\tag{14.3}
\]

#### Proof

The degree is \(D=r^2\).  Two distinct vertices of \(J(2r,r)\) have
\(2r-2\) common neighbours at Johnson distance one, four common neighbours at
distance two, and none at distance at least three.  Since \(r\geq3\), the
common-neighbour count is at most \(c=2r-2\).

Write \(s=|S|\), and for \(Y\in{\cal V}_R\) put
\(d_S(Y)=|N(Y)\cap S|\).  Then

\[
 \sum_Yd_S(Y)=Ds
\tag{14.4}
\]

and

\[
 \sum_Yd_S(Y)^2
 =Ds+2\sum_{\{X,X'\}\subseteq S}|N(X)\cap N(X')|
 \leq Ds+(2r-2)s(s-1).
\tag{14.5}
\]

Cauchy--Schwarz gives

\[
 |N(S)|\geq
 \frac{D^2s}{D+(2r-2)(s-1)}.
\tag{14.6}
\]

Put \(a=(r^2-2r+2)/2\).  If \(1\leq s\leq a\), then the denominator in
(14.6) is at most \(r^3\), so

\[
 |N(S)|\geq rs\geq s+r-1.
\tag{14.7}
\]

For \(a\leq s\leq N/2\), use the Johnson eigenvalues

\[
 \theta_j=(r-j)^2-j,\qquad 0\leq j\leq r.
\tag{14.8}
\]

The largest absolute nontrivial eigenvalue is

\[
 \lambda=r(r-2)
\tag{14.9}
\]

(for \(r=3\), the negative endpoint eigenvalue has the same absolute value).
The spectral decomposition of the indicator of \(S\) yields

\[
 \|A\mathbf1_S\|_2^2
 \leq \lambda^2s+(D^2-\lambda^2)\frac{s^2}{N}.
\tag{14.10}
\]

A second application of Cauchy--Schwarz, followed by \(s/N\leq1/2\), gives

\[
 \begin{split}
 |N(S)|
 &\geq
 \frac{D^2s}{\lambda^2+(D^2-\lambda^2)s/N}\\
 &\geq
 \frac{r^2s}{r^2-2r+2}
 =s+\frac{(2r-2)s}{r^2-2r+2}
 \geq s+r-1.
 \end{split}
\tag{14.11}
\]

It remains to take \(s>N/2\).  Identify the two copies of \({\cal V}\), and
put \(T={\cal V}\setminus N(S)\).  If \(T\neq\varnothing\), no edge joins
\(S\) to \(T\), whence \(N(T)\subseteq{\cal V}\setminus S\).  Regularity first
gives \(|T|\leq N-s<N/2\), and the already proved half-range inequality gives

\[
 |T|+r-1\leq|N(T)|\leq N-s.
\tag{14.12}
\]

Therefore \(|N(S)|=N-|T|\geq s+r-1\).  If \(s+r-1>N\), (14.12) is impossible,
so \(T=\varnothing\) and \(N(S)={\cal V}\).  This proves (14.3).
\(\square\)

### Corollary 14.2: bounded seam extension

Every matching of at most \(r-1\) prescribed edges of \({\mathbb B}_r\)
extends to a perfect matching.

#### Proof

Let the prescribed matching use \(t\leq r-1\) vertices on each shore.  For
\(S\) in the residual left shore, deleting the \(t\) used right vertices
reduces \(|N(S)|\) by at most \(t\).  If \(|S|+r-1\leq N\), (14.3) leaves at
least \(|S|+r-1-t\geq|S|\) neighbours.  Otherwise (14.3) says that the old
neighbourhood is the entire right shore, and the residual neighbourhood has
size \(N-t\geq|S|\).  Hall applies.  The bipartite node--edge incidence
matrix is totally unimodular, so the completion is integral. \(\square\)

This corollary proves owner-degree completion only.  An arbitrary completion
can create a directed two-cycle and need not preserve residence, shadows,
topology, or compiler pins.  The next theorem gives the exact protected
version.

### Definition 14.3: witness-clear reservoir

Let \(F\) be an oriented simple Johnson factor whose positive coordinate runs
have length at least \(d+1\).  A set \(C\) of old transition indices is a
**witness-clear \(d\)-reservoir** for a protected certificate \({\cal P}\) if:

1. distinct indices of \(C\) have cyclic distance greater than \(d\) on
   every source component;
2. for every protected q1 colour and every protected fixed lower target,
   one literal old witnessing edge or window has transition support disjoint
   from \(C\);
3. for every protected arbitrary upper target, one literal accepting interval
   has transition support disjoint from \(C\); and
4. for every occurrence-labelled pin of a fixed feasible cyclic
   compiler-core/Hall matching, the complete envelope/core/chronology support
   certifying that pin is disjoint from \(C\).

Let \(H\subseteq C_L\times C_R\) contain diagonal retain choices and allowed
nonold seams.  It is **physically protected** if every nonold seam is
Johnson-legal and \(d\)-collar-safe, no seam reverses a retained edge outside
\(C\), and no two arcs of \(H\) are opposite orientations of one physical
undirected edge.

### Theorem 14.4: protected pin-and-complete absorber

Assume \(C\) is witness-clear, \(H\) is physically protected, and for some
integer \(h\geq0\),

\[
 |N_H(S)|\geq\min\{|C|,|S|+h\}
 \quad(\varnothing\neq S\subseteq C_L).
\tag{14.13}
\]

Let \(K\subseteq H\) be a matching of size at most \(h\).  Suppose every new
target to be served has a named literal final witness all of whose variable
seams belong to \(K\), while all of its old transitions avoid \(C\).  Then:

1. \(K\) extends to a perfect matching \(M\) of \(H\);
2. rethreading \(C\) by \(M\) is a literal simple Johnson factor with positive
   residence at least \(d+1\);
3. every object in \({\cal P}\) survives literally; and
4. every target named by the service matching \(K\) is supplied.

In particular, if \({\cal P}\) contains a full occurrence-labelled cyclic
compiler-core/Hall solution, the same matching remains feasible.  A safe
linear opening and its terminal \(d\)-suffix equations remain separate.

#### Proof

Delete the \(t=|K|\leq h\) vertices used by \(K\) on both shores.  For any
set \(S\) of residual left vertices, (14.13) leaves at least
\(|S|+h-t\geq|S|\) residual neighbours when \(|S|+h\leq|C|\).  In the other
case the old neighbourhood is the complete right shore, so its residual
size \(|C|-t\) is at least \(|S|\).  Hall and bipartite total unimodularity
give an integral residual matching, proving item 1.

Extend \(M\) by the unchanged successor outside \(C\).  Degree is exact by
the head-permutation construction, and physical protection gives simplicity.
The actual nonfixed cut set is a subset of the \(d\)-separated set \(C\).
Every new seam is collar-safe, so the separated-collar theorem gives item 2.

Every protected old witness lies wholly in retained chronology and therefore
survives unchanged.  This includes a complete accepting upper interval and
the complete support of each compiler pin, not merely its target label.
Every service witness is a path whose variable seams are fixed by \(K\);
the residual completion cannot remove those seams or its retained interior.
This proves items 3--4. \(\square\)

### Corollary 14.5: one-provider orbit lift

In Theorem 14.4 with \(|K|=1\), replace (14.13) by the following hypotheses:
a finite group acts transitively on both physical shores of \(C\), \(H\) is
invariant, and the provider edge lies in \(H\).  Then the conclusion still
holds.

Indeed, invariance makes \(H\) regular on each shore; equal shore sizes make
the two degrees equal.  A regular bipartite graph decomposes into perfect
matchings, and the provider edge belongs to one member of such an edge
decomposition.  This perfect matching may break the symmetry.  Requiring an
equivariant matching after quotienting is a different, generally non-TU,
problem.

### Corollary 14.6: alternating implementation

Let \(M_0\) be the old diagonal head matching on \(C\), and let \(M\) be the
completion from Theorem 14.4.  Then \(M_0\mathbin\triangle M\) is a disjoint
union of even alternating cycles.  Hence the protected endpoint is one
simultaneous nonlocal commutator of ordinary alternating circuits.  No
individual circuit is required to preserve \({\cal P}\); protection is a
property of the final matching and the fixed service bank.

This is the precise sense in which total unimodularity now yields a literal
trade rather than a fractional marginal.

### Lemma 14.7: protected component fusion

Let \({\mathfrak M}_K\) be the perfect matchings of \(H\) extending a fixed
service bank \(K\).  Suppose that whenever \(M\in{\mathfrak M}_K\) has more
than one fragment-monodromy component, there is an \(M\)-alternating even
cycle \(Z\subseteq H\) which avoids \(K\) and for which

\[
 M' = M\mathbin\triangle Z
\tag{14.14}
\]

has fewer fragment-monodromy components.  Then some matching in
\({\mathfrak M}_K\) has one component.  The analogous statement with the
formal closing edge of Lemma 1.2 gives one spanning path.

#### Proof

Theorem 14.4 makes \({\mathfrak M}_K\) nonempty.  Flipping \(Z\) preserves
perfect matching degree and keeps every selected edge inside \(H\); because
\(Z\cap K=\varnothing\), it also preserves every named service witness.
The witness-clear pins lie outside the whole reservoir and are unchanged.
The positive integer number of macro components decreases at every flip, so
after finitely many flips it is one.  For a path, add the formal closing edge
before counting components and delete it after the last flip.
\(\square\)

This is a genuine topology condition, not a consequence of Hall.  It is
often enough to verify a smaller two-switch statement: two selected seams in
different macro components may exchange heads through two allowed cross
arcs, and the exchange merges those components.

## 15. Spectral Johnson routing of the q1 return debt

The protected-completion theorem makes the endpoint assignment integral.
There is a second, independent integrality theorem for q1 repayment.

Let \(\Omega\) have size \(K\), fix \(1\leq s\leq K-1\), and let

\[
 {\cal C}_s=\binom\Omega s,
\tag{15.1}
\]

and replace each undirected edge of \(J(K,s)\) by both orientations, each of
integral capacity \(c\).

### Lemma 15.1: exact Johnson cut expansion

If \(N_s=\binom Ks\), then for every \(S\subseteq{\cal C}_s\),

\[
 |\partial S|
 \geq K\frac{|S|(N_s-|S|)}{N_s}
 \geq\frac K2\min\{|S|,N_s-|S|\}.
\tag{15.2}
\]

#### Proof

Here \(\partial S\) is the set of undirected cut edges, each counted once.
The degree of \(J(K,s)\) is \(s(K-s)\), and its adjacency eigenvalues are

\[
 \theta_j=(s-j)(K-s-j)-j
 =s(K-s)-j(K-j+1),
 \qquad 0\leq j\leq\min\{s,K-s\}.
\tag{15.3}
\]

Thus the Laplacian gap is exactly \(K\).  Apply the Poincare inequality to
the centred indicator of \(S\), whose squared norm is
\(|S|(N_s-|S|)/N_s\).  Its Laplacian quadratic form is the number of
undirected cut edges.  The second inequality in (15.2) is elementary.
\(\square\)

### Theorem 15.2: integral bounded-debt router

Let \(b\in\mathbb Z^{{\cal C}_s}\) satisfy

\[
 \sum_{C\in{\cal C}_s}b_C=0,
 \qquad
 \|b\|_\infty\leq\left\lfloor\frac{cK}{2}\right\rfloor.
\tag{15.4}
\]

Orient the incidence matrix by

\[
 B(\mathbf e_{u\to v})=\mathbf e_v-\mathbf e_u,
\tag{15.5a}
\]

so \(By\) is net inflow minus outflow.  There is an integral directed flow
\(y\), of capacity at most \(c\) on every oriented Johnson edge, satisfying
\(By=-b\).  It can be chosen as a union of unit directed paths with edge
congestion at most \(c\).

#### Proof

For every \(S\subseteq{\cal C}_s\), zero total sum gives

\[
 |b(S)|\leq\|b\|_\infty
 \min\{|S|,N_s-|S|\}
 \leq c|\partial S|.
\tag{15.5}
\]

These are Hoffman's cut inequalities for the bidirected capacity-\(c\)
network.  Hence a feasible real flow exists.  A directed node--arc incidence
matrix is totally unimodular, and the capacities and demands are integral,
so an integral flow exists.  Among the integral solutions choose one of
minimum total arc load.  It has no positive directed cycle, since one unit
could otherwise be subtracted around that cycle.  Standard flow
decomposition now writes it as unit source-to-sink paths. \(\square\)

The theorem is already uniform in \(K\) and \(s\).  To turn these token paths
into owner rethreadings, one needs only the following literal interface.

### Definition 15.3: protected path-composable router atlas

Fix a protected service endpoint \(F_{\rm svc}\) and a certificate
\({\cal P}\) consisting of one literal witness for every required old shadow
target, every newly gained service target whose gain is to be retained, and
every occurrence pin of one feasible compiler matching.
A capacity-\(c\) lower router atlas is **protected and path-composable** if:

1. every oriented edge \(C\to C'\) of the lower q1 Johnson colour graph has a
   literal alternating macro with lower drift
   \(\mathbf e_{C'}-\mathbf e_C\), zero upper-q1 drift, and zero change to
   \({\cal P}\);
2. any integral family of such macros of congestion at most \(c\) composes,
   through declared sockets, to one squarefree head assignment; and
3. the composed endpoint preserves the declared residence and topology
   conditions.

Define an upper atlas symmetrically.  The two atlases are **jointly
path-composable** when, for every pair of integral lower and upper path
families of congestion at most \(c\), all of their macros admit one common
squarefree head assignment which preserves \({\cal P}\), residence, and the
declared topology.  This joint property, not separate composability of the
two palettes, is what “compatible physical sockets” means below.  It is
deliberately stronger than a catalogue of marginal signed columns.

### Theorem 15.4: protected two-palette repayment

Suppose a literal service endpoint strictly improves the canonical hole bank,
preserves \({\cal P}\), and has signed q1 drifts

\[
 b^-\in\mathbb Z^{\binom\Omega{r-1}},
 \qquad
 b^+\in\mathbb Z^{\binom\Omega{r+1}}.
\tag{15.6}
\]

If capacity-\(c\) protected lower and upper atlases are jointly
path-composable and

\[
 \|b^-\|_\infty,\|b^+\|_\infty
 \leq\left\lfloor\frac{cK}{2}\right\rfloor,
\tag{15.7}
\]

then there is one literal aggregate braid which restores both q1 decks
exactly, retains the service improvement, and preserves every shadow witness
and compiler pin in \({\cal P}\).

#### Proof

Every spanning endpoint has the same number of lower and upper q1
occurrences, so each vector in (15.6) has coordinate sum zero.  Apply Theorem
15.2 separately to the two ranks and lift the two resulting path families by
the compatible atlases.  Their drifts are \(-b^-\) and \(-b^+\).  Atlas
joint transparency preserves \({\cal P}\), including the named service-gain
witness, and joint path-composability gives one literal squarefree endpoint.
\(\square\)

This theorem verifies all Hoffman cuts at once and makes the return flow
integral.  Its unproved hypothesis is purely physical: the existence of the
transparent socketed atlas.

### Corollary 15.5: complement-diagonal routing

Assume \(K=2r\), and write

\[
 \kappa(C)=\Omega\setminus C:
 \binom\Omega{r-1}\longrightarrow\binom\Omega{r+1}.
\tag{15.8}
\]

If \(b^+_{\kappa(C)}=b^-_C\), it is enough to have one synchronized atlas in
which \(C\to C'\) has joint drift

\[
 (\mathbf e_{C'}-\mathbf e_C,
   \mathbf e_{\kappa(C')}-\mathbf e_{\kappa(C)}).
\tag{15.9}
\]

The joint matrix is a row duplication of one Johnson incidence matrix, so one
flow from Theorem 15.2 repairs both palettes without losing total
unimodularity.

If, in addition, an adjacency-preserving rotation or reflection \(\sigma\)
of the carrier satisfies

\[
 T_{\sigma(i)}=\Omega\setminus T_i,
\tag{15.10}
\]

then for every contiguous interval \(I\),

\[
 \Omega\setminus\bigcap_{i\in I}T_i
 =\bigcup_{i\in I}T_{\sigma(i)}.
\tag{15.11}
\]

Thus the fixed lower tower and the corresponding fixed upper tower are
equivalent, and positive residence on the paired traces gives zero residence.
Compiler Hall does not follow from (15.11); its occurrence pins must remain
in \({\cal P}\).

## 16. Pascal halo repair by Boolean Hall

The second place where integrality had been open is the compiler halo after a
Pascal braid.  Once the chronology, cuts, promoted cores, and old retained
matching are fixed, this is again an ordinary bipartite problem.

### Lemma 16.1: degree--codegree Hall

Let \(G=(D,R;E)\) be a finite bipartite graph, with \(D\neq\varnothing\), and
put

\[
 \delta=\min_{S\in D}\deg(S),
 \qquad
 \Delta=\max_{p\in R}\deg(p).
\tag{16.1}
\]

If

\[
 \boxed{\delta\geq\Delta>0,}
\tag{16.2}
\]

then \(G\) has a matching saturating \(D\).

#### Proof

For every nonempty \(X\subseteq D\),

\[
 \delta|X|
 \leq e(X,N(X))
 \leq\Delta|N(X)|.
\tag{16.3}
\]

Thus \(|N(X)|\geq|X|\), and Hall applies.  Integrality again follows from
the bipartite incidence matrix. \(\square\)

There is a useful Boolean calibration.  Join every
\(S\in\binom{[n]}s\) to every \(P\in\binom{[n]}h\) containing it.  The left
degree and right codegree are

\[
 \delta_0=\binom{n-s}{h-s},
 \qquad
 \Delta_0=\binom hs.
\tag{16.4}
\]

Since

\[
 \binom ns\delta_0=\binom nh\Delta_0,
\tag{16.5}
\]

the full Boolean level saturates every subfamily of the \(s\)-shore whenever
\(\binom nh\geq\binom ns\).  More generally, for a compiler position \(p\)
with core \(C_p\subseteq P_p\), its codegree against residual target ranks
\({\cal R}\) is bounded by

\[
 \deg(p)\leq
 \sum_{a\in{\cal R}}
 \binom{|P_p\setminus C_p|}{a-|C_p|}.
\tag{16.6}
\]

This is the promised Boolean expansion criterion: no exponential family of
Hall inequalities remains once the two pointwise degree bounds are proved.

### Theorem 16.2: integral promoted-halo repair

Apply Theorem 6.1 of
MATH_THEOREM_AD_PASCAL_EVENT_STREAM_BRAID_AND_DUAL_GAP_20260729.md
at compiler depth \(d\).  If \(s\) old seams are cut, its promoted halo
\(R\), and the set \(D\) of targets whose old matching edges are discarded,
obey

\[
 |R|\leq s(d+2),\qquad |D|\leq|R|.
\tag{16.7}
\]

Let \(K^+\) be every position left free by the transported matching after the
core is recomputed and promoted.  Form the physical incidence graph

\[
 S\sim p
 \quad\Longleftrightarrow\quad
 C'_p\subseteq S\subseteq P'_p,
 \qquad S\in D, p\in K^+.
\tag{16.8}
\]

If the graph in (16.8) satisfies (16.2), then the transported compiler
matching extends integrally across the entire halo.  For disjoint halo
clusters it is enough to verify (16.2) in each cluster; overlapping collars
are first joined into one cluster.

#### Proof

Lemma 16.1 gives a matching \(D\hookrightarrow K^+\).  Its targets and
positions are disjoint from those of the transported old matching by the
definitions of \(D\) and \(K^+\).  Their union is the matching required in
item 6 of the protected braid theorem. \(\square\)

A halo-reserved construction, in which no old compiler edge uses \(R\), is
the special case \(D=\varnothing\).  Conversely, fractional orbit balance is
not enough if (16.8) is quotiented before rounding: short orbits can introduce
coefficients greater than one.  The matching conclusion is on the physical
lift.

### Lemma 16.3: raw Pascal endpoint expansion

Before a \(B\)-forest restricts the available endpoint slots, give every
\(U\in\binom{[2r]}{r+1}\) two labelled slots and join
\(T\in\binom{[2r]}r\) to a slot of \(U\) when \(T\subset U\).  Every left
vertex has degree \(2r\), while every right slot has codegree \(r+1\).  Hence
all rank-\(r\) endpoint labels have an integral assignment to distinct slots.

#### Proof

There are \(r\) choices for the new element of \(U\setminus T\), and two
slots for each \(U\), giving degree \(2r\).  A fixed \(U\) contains \(r+1\)
rank-\(r\) subsets.  Since \(2r\geq r+1\), Lemma 16.1 applies. \(\square\)

This proves that naked Pascal endpoint containment has no Hall obstruction.
It does not choose the labelled \(B\)-forest: after that forest leaves only
its actual endpoint slots, the restricted graph must again satisfy (16.2) or
ordinary Hall.

### Definition 16.4: protected Pascal reservoir property

Let \(C_r={\rm Cat}_r\), and consider the generalized Pascal child on

\[
 \{z\}+\binom{[2r]}r
 \quad\text{and}\quad
 \binom{[2r]}{r+1}.
\tag{16.9}
\]

Write \({\rm PPR}(r,d)\) for the following concrete statement.

1. The two sector forests can be chosen with the established exact owner and
   q1 endpoint counts and with named fragment-interior witnesses for every
   lower and arbitrary-upper target not assigned to a seam service bank.
2. The intact sector paths determine a \(d\)-witness-clear reservoir \(C\)
   and a physically protected endpoint graph \(H\).  For some \(h\), a
   service matching \(K\subseteq H\), with \(|K|\leq h\), contains a complete
   literal path or accumulated-union witness for every target whose protected
   old witnesses are cut.  The graph \(H\) satisfies the nonempty-set
   \(h\)-surplus inequality (14.13), or, in the weaker fixed-bank version,
   \(H-V(K)\) passes ordinary Hall.
3. Starting from any Hall completion of \(K\), the protected
   component-fusion hypothesis of Lemma 14.7 reaches a completion \(M^*\)
   whose fragment monodromy is one spanning cycle.  All joins of \(M^*\) are
   Johnson-legal and pass the exact residence collars, and every service or
   retained witness is disjoint from those joins except where its complete
   accepting path is explicitly fixed.
4. For this final chronology, the two requisite adjacent-depth parent
   compiler packages combine into one partial **child** compiler matching
   which saturates the entire child low-target family except a set \(D\).
   Its matched positions lie outside the promoted halos, and the physical
   halo graph (16.8) on \(D\) satisfies (16.2).
5. A declared edge \(e^*\in M^*\setminus K\) is a safe formal closing edge.
   Deleting \(e^*\) gives one spanning path while preserving every named
   fixed-lower and arbitrary-upper witness (or supplying its declared
   boundary replacement).  The two endpoint core/envelope equations, every
   nonempty-envelope condition, both q1 boundary ledgers, and the terminal
   \(d\) suffix columns required by the linear compiler theorem all hold
   literally.  The repaired matching from item 4, together with its declared
   boundary/suffix assignments, is a full occurrence-labelled linear
   \({\rm COMP}_d\) matching.

The use of arbitrary-upper accepting paths in item 2 is essential.  A
fixed-depth signature is not a substitute.

### Theorem 16.5: decorated Pascal compiler existence

If \({\rm PPR}(r,d)\) holds, there is an upper-complete middle permutation on
\([2r+1]\) with feasible full \({\rm COMP}_d\).  Consequently the established
compiler theorem gives

\[
 \boxed{\nu(2r+1)\leq
 \binom{2r+1}{r+1}+d.}
\tag{16.10}
\]

If \({\rm PPR}(r,d(2r+1))\) holds for every \(r\) beyond verified base cases,
the same inequality holds in every odd dimension; in particular it gives the
coefficient-one upper bound whenever \(d(2r+1)=o\!\left(\binom{2r+1}{r+1}\right)\).

#### Proof

Fix the two forests and the service bank.  The fixed forest interiors retain
their named witnesses, while item 2 supplies every cut-vulnerable target.
Theorem 14.4, or the explicitly stated residual Hall alternative, completes
the endpoint matching integrally without disturbing the service paths.
Lemma 14.7 and item 3 then produce \(M^*\), still preserving every named
witness, whose macro chronology is one spanning cycle.  Item 5 deletes its
formal closing edge and certifies the resulting spanning path, including all
boundary witness replacements.  Thus the resulting chronology has the exact
owner deck and the declared complete lower and upper witness banks.

Item 4 already supplies the complete child partial compiler matching,
including targets introduced by the Pascal lift.  Theorem 16.2 repairs the
remaining set \(D\) integrally.  Item 5 supplies the separate opening and
terminal conditions.  Hence the hypotheses of the exact linear compiler
theorem hold, giving (16.10).  If the data in items 1--5 are supplied by a
certificate-preserving parent-to-child construction and verified base
packages are given, the same argument is an induction on \(r\).
\(\square\)

This is one concrete all-\(r\) verification target.  Its universal rounding
steps are proved: endpoint completion, alternating-cycle realization, and
compiler repair are integral.  The missing Boolean/PBBS lemma is precisely
the construction of the witness-clear service bank and the proof of the two
restricted degree bounds after the forests and collars have been fixed.

There is also an exact interface budget under the intact-sector condition in
item 2.  The generalized construction has \(2C_r\) nonempty sector paths and
uses no extra interior cuts.  A spanning cycle uses \(2C_r\) inter-sector
joins, and deleting the formal closing edge leaves exactly \(2C_r-1\) joins
in the final path.  Therefore at most

\[
 q(2C_r-1)
\tag{16.11}
\]

fixed-depth \(q\)-window starts meet an interface, and the promoted compiler
halo has size at most

\[
 (2C_r-1)(d+2).
\tag{16.12}
\]

Since

\[
 \binom{2r+1}{r+1}=(2r+1)C_r,
\tag{16.13}
\]

the interface density is less than \(2/(2r+1)\).  These sparse counts do not
prove absorption; items 2--3 of \({\rm PPR}\) are the exact missing
chronology and Hall assertions.

If an alternative construction makes additional interior cuts and has
\(f\) actual retained fragments, the exact replacements for
\(2C_r-1\) in (16.11)--(16.12) are \(f-1\).  No smaller interface count is
then implied by the sector enumeration alone.

## 17. Exact K16 reconciliation and the remaining boundary

The new existence theorems fit, but do not solve, the authenticated K16
frontier.

### 17.1 What physical Johnson expansion proves

For \(r=8\), Theorem 14.1 gives

\[
 |N(S)|\geq\min\{12870,|S|+7\}.
\tag{17.1}
\]

Thus any seven prescribed **physical** Johnson seams which form a
vertex-disjoint matching extend to a naked head assignment.  This does not
extend a seven-orbit service bank: one free
\(Z_{15}\)-orbit already contains fifteen physical seams.  Nor does it impose
simplicity, residence, shadows, or compiler pins.  Its exact conclusion is
that small physical provider sets have no owner-degree Hall obstruction.

The authenticated length-eight endpoint has 29 components, positive
residence four, both q1 palettes, and canonical deficit

\[
 45+48=93.
\tag{17.2}
\]

Its unrestricted SAAR graph has \(810810\) nonidentity Johnson tail--head
arcs.  The three-separated collar-safe face has \(211604\) nonold seams, of
which \(5425\) are provider seams.  These counts establish neither a
witness-clear reservoir nor the surplus expansion of its protected residual
graph.  Hence they do not verify Theorem 14.4 or \({\rm PPR}\).

### 17.2 What token expansion proves

The two q1 colour graphs are \(J(16,7)\) and \(J(16,9)\).  Both have degree
\(63\) and Laplacian gap \(16\).  At unit capacity, Theorem 15.2 routes every
zero-sum drift satisfying

\[
 \|b\|_\infty\leq8.
\tag{17.3}
\]

Thus q1 token geometry is not the obstruction for the saved length-nine
signatures, whose per-row drifts have unit scale.  What is missing is a
physical atlas realizing those abstract token paths without touching the
protected all-depth and compiler witnesses.

### 17.3 Why the C9 trap is not contradicted

Every one of the thirty authenticated C9 atoms repairs one current rank-11
target but creates one lower-rank-5 hole and two upper-rank-10 holes.  Its
canonical objective therefore changes

\[
 93\longmapsto95.
\tag{17.4}
\]

The maximum compatible seven-packet changes it to \(107\).  Consequently the
C9 cut set meets every old witness of at least those new casualties; it is
not witness-clear.  The C9 catalogue also has no nonnegative exact-q1 kernel.
It therefore fails the service/transparency hypotheses before either TU
theorem is invoked.  Passing q1 and selected q2/q3 rows is insufficient.

### 17.4 Orbit and separated-port scope

The physical incidence matrices in Sections 14--16 are TU.  A quotient is a
network matrix only under the corresponding semiregularity.  If an edge
orbit has a stabilizer smaller than a vertex stabilizer, its quotient column
has coefficient greater than one.  K16's size-three target orbit, which has
fivefold response under a generic full \(Z_{15}\)-orbit, is the concrete
warning.  The conclusions above may break cyclic symmetry; an equivariant
conclusion needs a separate stabilizer-compatible proof.

Likewise, the separated-port master makes residence and fixed windows through
depth three additive.  It does not make deeper lower witnesses, arbitrary
upper accepting paths, or compiler pins local.  Those objects must be placed
literally in the protected bank of Theorem 14.4.

### 17.5 Proved/conditional boundary

The following parts are now unconditional.

1. The physical \(J(2r,r)\) port lift has additive surplus \(r-1\), and every
   prescribed matching of that size extends integrally.
2. A \(d\)-witness-clear, \(h\)-surplus reservoir turns any service bank of
   size at most \(h\) into a literal protected factor by Hall/TU.
3. Johnson token debts of sup norm at most \(cK/2\) have integral bounded-
   congestion path routings.
4. Every such endpoint difference is a union of alternating circuits.
5. The pointwise compiler inequality \(\delta\geq\Delta>0\) gives an integral
   promoted-halo repair.

The single uniform construction target is \({\rm PPR}(r,d)\), or, in the
nonrecursive language, the protected orbit-reservoir property of Theorem
14.4 together with a path-composable atlas of Definition 15.3.  What must
still be proved is the literal PBBS/Pascal atlas: one all-depth witness-clear
service bank, protected residual expansion, compatible sockets, and the
restricted compiler degree bounds.  This is an architecture-restricted
sufficient certificate and need not be necessary for an arbitrary successful
word.  Its remaining verification is nevertheless narrower than the full
word problem, because all completion and rounding steps after those literal
conditions are automatic.

No new finite artifact or search result is used in Sections 14--17.  Their
K16 numbers and the C9 statements use only the frozen dependencies already
listed in Section 13.  No local or remote search, SAT/CP solve, or web access
was used for this extension.
