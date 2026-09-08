# `RTR(7,4)`: the exact MSW--PBBS alternating-circulation gate

Date: 2026-07-29  
Lane: K  
Status: unconditional structural theorems and an exact architecture-specific
existence reduction.  `RTR(7,4)` is not claimed.

## 0. Verdict

Put

\[
 \Omega=[15],\qquad {\cal X}=\binom{\Omega}{7},\qquad
 {\cal U}=\binom{\Omega}{8},\qquad
 {\cal R}=\binom{\Omega}{6}.
\]

Let `M` be the canonical MSW middle-levels incidence factor and let `P` be
the centred PBBS incidence factor.  The following statements are proved.

1. Two-sided residence four has an exact local form.  If `p_i` is the
   two-coordinate transition label on the `i`-th projected Johnson edge,
   then residence four is equivalent to

   \[
    p_i\cap p_{i+t}=\varnothing\qquad(t=1,2,3)                 \tag{0.1}
   \]

   cyclically on every component.  Equivalently, the four labels in every
   four-edge frame are pairwise disjoint.  This condition already forces
   every component to have at least eight projected vertices.

2. Every factor obtainable by alternating circuits in `M triangle P` is
   encoded by a binary signed circulation.  Degree two is exactly the
   circulation equation; lower-turn coverage is an exact turn-atom cover;
   and (0.1) is an explicit family of width-at-most-eight linear covering
   inequalities.  Thus there is no hidden connectivity or chronology
   condition after these rows are imposed.

3. A family of nonlocal circuit packets composes safely if its change
   supports are four-frame separated, every packet is separately
   four-frame safe, and the sum of their exact turn-ledger changes leaves
   every lower target positive.  The packets themselves need not be local.

4. The MSW run arrangement is rigid.  The subgraph induced by the fifteen
   vertices of one MSW wreath is exactly a `C_15`.  Consequently every
   nontrivial turn repair must use cross-wreath edges.  More generally, if
   the MSW lower-turn map has `h` holes, every lower-complete factor has at
   least `h` cross-wreath turns, and those turns form an Eulerian interaction
   multigraph on the wreaths.  At `r=7`, the audited value `h=837` forces at
   least `837` cross-wreath turns and at least `56` affected wreaths.

5. Inside the more restrictive strict-wreath subclass, lower-turn coverage has a
   particularly simple exact form.  If `N_R` is the number of wreaths owning
   the nine rank-seven supersets of a rank-six set `R`, then

   \[
      \lambda_R=9-N_R.
   \]

   Thus strict-wreath `RTR(7,4)` is exactly the existence of a wreath
   decomposition with no rainbow nine-owner star.

6. This strict-wreath problem has a literal fractional solution with slack:
   averaging all coordinate relabelings of MSW gives weight `1/28` on every
   Johnson edge, upper load one, and lower load `9/7`.  Therefore no real
   linear or first-moment obstruction separates the run-perfect wreath face
   from lower coverage.  The remaining gap is integral collision rounding.

The sharp missing statement in this architecture is therefore a single
global binary-circulation lemma, stated in Section 7.  Failure of that lemma
would rule out only the fixed `M union P` overlay with common incidences
frozen; it would not refute unrestricted `RTR(7,4)`.

## 1. Turn selectors and transition labels

For each `U in cal U`, a selector chooses

\[
 p(U)=\{a,b\}\in\binom U2
\]

and hence the Johnson edge

\[
 e_U=\{U-a,U-b\}.                                      \tag{1.1}
\]

Assume the degree equations

\[
 \#\{x\notin X:x\in p(X+x)\}=2
 \quad(X\in{\cal X}).                                  \tag{1.2}
\]

Then the edges `(e_U)` form a spanning two-factor of `J(15,7)`, with one
edge of every upper colour `U`.  On an oriented component write

\[
 X_i,U_i,X_{i+1},U_{i+1},\ldots,
 \qquad U_i=X_i\cup X_{i+1},
\]

and put

\[
 q_i=p(U_i)=X_i\triangle X_{i+1}.                       \tag{1.3}
\]

### Theorem 1.1 (four-frame residence criterion)

The following are equivalent.

1. Every nonconstant one-run and every nonconstant zero-run of every
   coordinate has length at least four on every component.
2. For every `i` and `t in {1,2,3}`,

   \[
    q_i\cap q_{i+t}=\varnothing.                         \tag{1.4}
   \]

3. Every four consecutive transition pairs are pairwise disjoint.
4. Every projected path of at most four edges is a Johnson geodesic.

Any of these conditions forces every projected component to have length at
least eight.  Thus the separate component-length-four clause in `RTR(7,4)`
is redundant.

#### Proof

A coordinate `x` changes membership from `X_i` to `X_(i+1)` exactly when
`x in q_i`.  For a nonconstant coordinate, its cyclic run lengths are
therefore exactly the cyclic gaps between successive indices `i` for which
`x in q_i`.  All one- and zero-runs have length at least four if and only if
no two such indices have cyclic distance one, two, or three.  This is
(1.4), and it is plainly equivalent to item 3.

Along `t<=4` Johnson edges, the endpoint distance is `t` exactly when the
`2t` changed coordinates are all distinct.  This proves the equivalence
with item 4.

Finally, on a closed component every coordinate occurs an even number of
times among the `q_i`.  If the component length were at most seven, two
occurrences of some used coordinate would have cyclic distance at most
three, contradicting (1.4).  `square`

This theorem converts residence from a run-enumeration condition into a
literal four-turn exclusion system.

### Corollary 1.2 (regular transition graph and derived walks)

Write an oriented transition as

\[
 X_{i+1}=X_i-\alpha_i+\beta_i,
 \qquad q_i=\{\alpha_i,\beta_i\}.
 \tag{1.5}
\]

In every upper-exact selector, each coordinate occurs in exactly `858`
transition pairs.  Thus the multiset `(q_i)` is an `858`-regular multigraph
on the fifteen coordinate labels.

Under residence four, the lower turns

\[
 R_i=X_i\cap X_{i+1}
 \]

satisfy

\[
 R_{i+1}=R_i-\alpha_{i+1}+\beta_i,                   \tag{1.6}
\]

and every segment of at most three edges in this rank-six walk is geodesic.
Likewise the upper colours `(U_i)` form a spanning two-factor of
`J(15,8)`, whose consecutive transition label is
`{alpha_i,beta_(i+1)}`, and its segments of at most three edges are
geodesic.

#### Proof

Fix a coordinate `x` and let `t_x` count selected transitions containing
it.  There are `3003` rank-seven vertices containing `x`.  If `I_x` is the
number of selected edges with both endpoints containing `x`, degree two and
upper exactness give

\[
 6006=2I_x+t_x,
 \qquad
 3432=I_x+t_x.
\]

Hence `t_x=858`.  Formula (1.6) follows by writing
`R_i=X_(i+1)-beta_i` and `R_(i+1)=X_(i+1)-alpha_(i+1)`.
Three consecutive derived transition labels use coordinates from four
pairwise-disjoint pairs `q_i,...,q_(i+3)`, proving geodesicity.  The upper
statement is dual, and upper exactness makes its walk spanning.  `square`

## 2. The exact signed overlay circulation

View `M` and `P` as two-factors of the bipartite inclusion graph

\[
 B=B({\cal X},{\cal U}).
\]

Put

\[
 E^- = M\setminus P,\qquad E^+=P\setminus M,
 \qquad E^0=M\cap P.                                  \tag{2.1}
\]

For every `e in E^- union E^+`, choose `y_e in {0,1}`.  Interpret
`y_e=1` on `E^-` as deleting an MSW incidence, and `y_e=1` on `E^+` as
adding a PBBS incidence.  Define

\[
 F(y)=E^0
 \cup\{e\in E^-:y_e=0\}
 \cup\{e\in E^+:y_e=1\}.                            \tag{2.2}
\]

### Theorem 2.1 (alternating-circulation equivalence)

`F(y)` is a spanning degree-two incidence factor if and only if

\[
 \boxed{
 \sum_{e\in E^-\cap\delta(v)}y_e
 =
 \sum_{e\in E^+\cap\delta(v)}y_e
 \quad(v\in{\cal X}\cup{\cal U}).}                  \tag{2.3}
\]

Every binary solution of (2.3) decomposes into edge-disjoint alternating
closed trails, and toggling those trails produces `F(y)`.  Conversely every
family of alternating-circuit switches gives a binary solution of (2.3).

#### Proof

Both endpoint factors have degree two.  At a vertex `v`, (2.3) says exactly
that the number of removed selected incidences equals the number of added
incidences, proving the degree assertion.  In the selected signed support,
red and blue degrees agree at every vertex.  Pair red and blue half-edges at
each vertex and follow the pairings; this decomposes the support into
alternating closed trails.  The converse is immediate.  `square`

This is the full integral kernel of the fixed overlay.  Choosing a subset of
one previously fixed circuit decomposition is only a subcube of (2.3) and
can miss other balanced recombinations.

## 3. Exact turn and frame rows

For an incidence `e`, write its final selection indicator as

\[
 s_e(y)=
 \begin{cases}
 1,&e\in E^0,\\
 1-y_e,&e\in E^-,\\
 y_e,&e\in E^+.
 \end{cases}                                         \tag{3.1}
\]

At an upper owner `U`, equation (2.3) leaves exactly two selected facets.
For `R in cal R` with `R subset U`, let `a,b` be the two elements of
`U setminus R`.  The turn at `U` has lower colour `R` exactly when both
incidences

\[
 (U-a,U),\qquad(U-b,U)                               \tag{3.2}
\]

are selected.  If either incidence lies outside `M union P`, this turn is
unreachable in the fixed overlay.

Now take a nonbacktracking four-turn walk in `B`,

\[
 Q=(X_0,U_0,X_1,U_1,X_2,U_2,X_3,U_3,X_4),           \tag{3.3}
\]

all of whose incidences lie in `M union P`.  Call it a **bad frame** if the
four pairs

\[
 (U_i\setminus X_i)\cup(U_i\setminus X_{i+1}),
 \qquad0\le i<4,                                    \tag{3.4}
\]

are not pairwise disjoint.  Let `D^-(Q)` and `D^+(Q)` be the distinct
`E^-` and `E^+` incidences used by the walk.

### Theorem 3.1 (exact overlay formulation of `RTR`)

There is an `RTR(7,4)` selector inside the fixed `M union P` overlay with
all common incidences retained if and only if there is a binary vector `y`
satisfying all of the following.

1. The balance equations (2.3).
2. For every `R in cal R`, some `U superset R` has both incidences (3.2)
   selected.
3. For every bad frame `Q`,

   \[
    \boxed{
    \sum_{e\in D^-(Q)}y_e
    +\sum_{e\in D^+(Q)}(1-y_e)\ge1.}                \tag{3.5}
   \]

No additional component constraint is required.

#### Proof

Theorem 2.1 gives degree two and one turn at every upper owner.  Item 2 is
exactly lower-turn surjectivity.  All incidences of `Q` are selected exactly
when every old-only incidence has `y_e=0` and every new-only incidence has
`y_e=1`; (3.5) is precisely the negation of that event.  Thus item 3 forbids
exactly the bad four-turn factors.  Theorem 1.1 gives two-sided residence and
the automatic component bound.  Every implication is reversible.  `square`

Turn atoms can be linearized in the usual literal way, but Theorem 3.1 is a
mathematical equivalence and does not depend on a solver encoding.

## 4. What a fixed circuit decomposition buys

Fix a decomposition of `M triangle P` into simple alternating circuits
`C_1,...,C_t`, and toggle circuit `C_j` according to a bit `z_j`.  At an
upper owner `U`, at most two circuits occur: each occurring circuit replaces
one MSW incidence by one PBBS incidence, while `U` has only two incidences
in either factor.  Consequently:

* every reachable turn at `U` is a cylinder condition on at most two
  circuit bits;
* the literal PBBS turn at `U` is obtained by setting all local circuit bits
  to one;
* the literal MSW turn is obtained by setting all local circuit bits to
  zero;
* every bad-frame event is a conjunction of at most eight circuit literals.

The audited PBBS first-turn theorem gives each `R in cal R` between one and
three literal PBBS witnesses.  Therefore every MSW hole has a monotone
endpoint-cover requirement of the form

\[
 \bigvee_{U\in W_P(R)}\ \bigwedge_{j\in I(U)} z_j,
 \qquad 1\le|W_P(R)|\le3,\quad1\le|I(U)|\le2.      \tag{4.1}
\]

Hybrid turns may give additional witnesses; (4.1) deliberately ignores
them and is only a sufficient subfamily.  This small-width fact does not
make the problem local: one circuit bit can occur at macroscopically many
owners and frames.

There is also a sharp protection warning.  If one protects one literal PBBS
witness for each of the `5005` lower targets, those witnesses occupy `5005`
distinct upper owners, leaving only

\[
 6435-5005=1430                                      \tag{4.2}
\]

uncommitted owners.  Thus a proof based on permanently frozen literal
witnesses has only `1430` movable rows.  A genuinely global theorem should
permit witness migration through hybrid or newly created turns.

Indeed, an upper owner has only the single turn `U setminus p(U)`, so two
different lower targets cannot use the same protected owner.  For fixed
`U,R`, retaining that literal witness uniquely requires
`p(U)=U setminus R`, hence both selected incidences at `U` are frozen.  This
argument applies only to preservation of the same chosen witnesses.  It is
not an obstruction to moving a target to another owner, and no assertion is
made that `1430` movable rows are quantitatively insufficient.

## 5. A sufficient packet-composition theorem

A **circuit packet** is any binary balanced support satisfying (2.3), hence
any union of alternating closed trails.  Its size and diameter are
unrestricted.  Let `supp(Q)` be the incidence vertices touched by its
changed incidences.

Packets `Q_1,...,Q_s` are **four-frame separated** if their changed
incidence-vertex supports are pairwise disjoint and no nonbacktracking
four-turn walk in `M union P` meets the changed support of two different
packets.  In particular, no upper owner is changed by two packets.

For a packet `Q_a`, let

\[
 \Delta_a(R)=
 \#\{U:\text{the packet creates turn }R\text{ at }U\}
 -
 \#\{U:\text{the packet deletes the MSW turn }R\text{ at }U\}. \tag{5.1}
\]

### Theorem 5.1 (nonlocal safe-packet rebundling)

Suppose:

1. `Q_1,...,Q_s` are four-frame separated circuit packets;
2. toggling each `Q_a` alone in `M` satisfies the four-frame condition;
3. for every lower target `R`,

   \[
    \lambda_M(R)+\sum_{a=1}^s\Delta_a(R)\ge1.        \tag{5.2}
   \]

Then toggling all packets gives an `RTR(7,4)` selector.

#### Proof

The disjoint union of the packet circulations is balanced, so Theorem 2.1
gives degree two.  No upper row is changed by two packets, hence its turn
change belongs to exactly one ledger (5.1); (5.2) gives lower surjectivity.

If the union had a bad selected four-frame, that frame could not be wholly
MSW because MSW is four-frame safe.  It would therefore meet a changed
packet.  Four-frame separation makes that packet unique, and on the whole
frame the union agrees with the corresponding single-packet factor.  This
contradicts item 2.  Theorem 1.1 finishes the proof.  `square`

The separation hypothesis is sufficient, not necessary.  Overlapping
packets can be legal when their joint frame effects cancel; those effects
are covered exactly by Theorem 3.1.

## 6. Wreath rigidity and the forced global scale

One MSW wreath has a cyclic coordinate order

\[
 z_0,z_1,\ldots,z_{14}
\]

and vertex set

\[
 X_i=\{z_i,z_{i+1},\ldots,z_{i+6}\},
 \qquad i\in\mathbb Z_{15}.                          \tag{6.1}
\]

### Lemma 6.1 (induced-wreath rigidity)

The subgraph of `J(15,7)` induced by the fifteen sets in (6.1) is exactly
the cycle

\[
 X_0X_1\cdots X_{14}X_0.                             \tag{6.2}
\]

Consequently any spanning two-factor whose edges never join different MSW
wreath classes is the MSW factor itself.

#### Proof

Two cyclic intervals of length seven in a cyclic order of length fifteen
have intersection size six exactly when their starts differ by `+1` or
`-1`.  These and only these pairs are Johnson adjacent.  Thus the induced
graph is (6.2), whose only spanning two-regular subgraph is itself.  Apply
this independently to every wreath.  `square`

The same rigidity can be recovered from runs.  If a length-fifteen Johnson
cycle has, for every coordinate, one run of seven ones and one run of eight
zeros, write `b_i` for the coordinate entering at transition `i`.  Each
coordinate enters and leaves once, and the coordinate `b_i` leaves seven
steps later.  Hence the vertices are exactly the seven-windows in the cyclic
order `(b_i)`.  Thus exact MSW run geometry is equivalent to wreath geometry,
not a flexible reservoir of alternative internal turns.

### Theorem 6.2 (cross-wreath lower bound)

Let `h` be the number of lower-turn holes of `M`.  Every lower-turn-complete
two-factor `G` of `J(15,7)` contains at least `h` edges joining distinct MSW
wreath classes.  Contracting each wreath class, these cross edges form an
Eulerian multigraph.  If `k` is their number, at least

\[
 \left\lceil{k\over15}\right\rceil                  \tag{6.3}
\]

wreath classes are incident with them.

#### Proof

Choose in `G` one edge witnessing each MSW hole.  The chosen edges are
distinct because an edge has one lower colour.  None is an MSW edge.  By
Lemma 6.1, no non-MSW Johnson edge has both endpoints in one MSW wreath, so
all chosen edges are cross-wreath.

For one wreath class `V`, degree two in `G` gives

\[
 2|V|=2e_G(V)+|\delta_G(V)|.
\]

Thus its cross degree is even, proving the Eulerian assertion after
contraction.  A wreath contains fifteen vertices and hence has cross degree
at most thirty.  Since the total cross degree is `2k`, (6.3) follows.
`square`

The audited canonical MSW ledger at `r=7` has

\[
 h=837.                                               \tag{6.4}
\]

Therefore any `RTR(7,4)` factor obtained by rebundling the MSW vertex deck
must contain at least `837` cross-wreath turns and must affect at least

\[
 \left\lceil{837\over15}\right\rceil=56             \tag{6.5}
\]

MSW wreaths.  This proves that the needed operation is a genuinely global
rebundling, not an internal row switch or a bounded collection of fringe
repairs.  The number `837` is finite audited input; Theorem 6.2 is uniform
in `h`.

There is also a rank-six transport identity.  For every upper-perfect
factor, if `lambda_R` is the lower-turn load and `eta_R=lambda_R-1`, then

\[
 \sum_R\eta_R=1430,
 \qquad
 \sum_{R\ni x}\eta_R=572\quad(x\in\Omega).           \tag{6.6}
\]

Hence any changed-row set `K` satisfies

\[
 \sum_{U\in K}
 \left({\mathbf 1}_{R_{\rm new}(U)}
       -{\mathbf 1}_{R_M(U)}\right)=0
 \quad\text{coordinatewise}.                         \tag{6.7}
\]

In particular, a hypothetical minimum-size `837`-row repair would have to
match the aggregate coordinate-incidence vector of the `837` holes by a
submultiset of deletable MSW surplus occurrences.  This is a necessary
transport condition, not a proof that such a submultiset or chronology
exists.

## 7. The precise missing lemma

The architecture-specific remaining statement is the following.

### MSW--PBBS global frame-circulation lemma at `(15,4)` (open)

There is a binary vector on `E^- union E^+` satisfying simultaneously:

1. the signed balance equations (2.3);
2. the complete lower-turn rows of Theorem 3.1;
3. every bad-frame inequality (3.5).

Equivalently, the MSW--PBBS symmetric difference contains a globally
balanced alternating-circuit family which migrates enough turn witnesses
to cover all `837` MSW holes while leaving every four consecutive transition
labels pairwise disjoint.

This is the smallest missing lemma for the proposed MSW-versus-PBBS route:

* degree is already exact by signed circulation;
* PBBS supplies one to three literal witnesses for every lower target;
* MSW supplies a four-frame-safe endpoint;
* the component-length condition is automatic;
* first moments (6.6) have the required values.

What is not proved is the simultaneous integral choice.  Equality of the
symmetrized MSW and PBBS one-point marginals does not couple their supports.
Likewise, selecting a fixed set of literal PBBS witnesses can freeze `5005`
rows and miss the required witness migration.

Finally, this lemma is a more restrictive sufficient statement than
unrestricted `RTR(7,4)`: it forbids every incidence outside `M union P` and
freezes `M cap P`.  The converse implication is not established.
An obstruction to it is therefore architecture-specific.  A genuine
refutation of `RTR(7,4)` would need a dual invariant valid for all 28 turn
choices at every upper owner, not merely for this two-seed overlay.

## 8. The strict-wreath collision theorem

Let `C=(c_i)_(i in Z_15)` be a cyclic order of `Omega`.  Put

\[
 X_i(C)=\{c_i,c_{i+1},\ldots,c_{i+6}\}.
 \tag{8.1}
\]

The corresponding wreath is the Johnson cycle joining `X_i(C)` to
`X_(i+1)(C)`.  Its upper and lower turn colours are

\[
 U_i(C)=\{c_i,c_{i+1},\ldots,c_{i+7}\},
 \qquad
 R_i(C)=\{c_{i+1},\ldots,c_{i+6}\}.
 \tag{8.2}
\]

Call a family `D` of cyclic orders a **strict wreath decomposition** when
the sets `X_i(C)`, over `C in D` and `i in Z_15`, partition `cal X`.
Necessarily `|D|=6435/15=429`.

### Theorem 8.1 (automatic upper exactness and owner-star identity)

Every strict wreath decomposition gives a spanning two-factor satisfying
the degree rows, with components of length fifteen and coordinate run/gap
lengths exactly seven/eight.  Its upper colours are automatically exact.

For `R in cal R`, let

\[
 N_D(R)=
 \left|\left\{C\in D:
       X_i(C)=R+x\text{ for some }i\text{ and }x\notin R
       \right\}\right|
 \tag{8.3}
\]

be the number of distinct wreath owners among the nine supersets of `R`.
Then its lower-turn load is exactly

\[
             \boxed{\lambda_D(R)=9-N_D(R).}           \tag{8.4}
\]

Consequently a strict wreath decomposition proves `RTR(7,4)` if and only if

\[
                 N_D(R)\le8\qquad(R\in{\cal R}).      \tag{8.5}
\]

In words: no rank-six star may be rainbow among nine different wreath
owners.

#### Proof

Adjacent seven-windows differ by deleting `c_i` and inserting `c_(i+7)`,
so they are Johnson adjacent and have the colours in (8.2).  Each coordinate
occupies seven consecutive cycle vertices and is absent from the following
eight.  This proves degree two, component length, and residence.

Moreover

\[
       \Omega\setminus U_i(C)=X_{i+8}(C).              \tag{8.6}
\]

Thus the eight-window palette of one wreath is the complement of its
seven-window palette.  A global partition of all seven-sets therefore gives
every eight-set exactly once.

Fix `R`.  Its nine supersets are `R+x`, `x in Omega setminus R`.  One cyclic
order can own at most two of them.  Indeed, two distinct circular intervals
of length seven whose intersection has size six have adjacent starting
positions; if two owned supersets occur, their intersection is therefore
`R` and they form one edge of lower colour `R`.  Conversely every edge of
lower colour `R` is exactly such a double ownership.  Hence every owner
class in the nine-element star has size one or two.  If there are `s`
singletons and `p` pairs, then

\[
             s+2p=9,\qquad N_D(R)=s+p,
\]

while `lambda_D(R)=p`.  Eliminating `s` proves (8.4), and (8.5) follows.
`square`

Two useful exact checks follow immediately:

\[
 0\le\lambda_D(R)\le4,
 \qquad
 \sum_R N_D(R)=9\binom{15}{6}-6435=38610.
 \tag{8.7}
\]

Thus the mean owner count is `38610/5005=54/7<8`.  The obstruction is not
the average number of owners; it is the maximum-one-star requirement.
For the canonical MSW decomposition, the audited `837` missing turns are
exactly the `837` stars with `N_M(R)=9`.

### Theorem 8.2 (whole-wreath global rebundling)

Let `D_0,D_1` be any two strict wreath decompositions.  Cancel their common
wreaths and form the bipartite ownership overlay: its left vertices are the
remaining wreaths of `D_0`, its right vertices those of `D_1`, and every
seven-set not belonging to a cancelled common wreath joins its unique two
remaining owners.  Rows belonging to cancelled common wreaths remain frozen
and agreed.  For each connected overlay component `K`, let

\[
 g_K={\bf1}_{D_1\cap K}-{\bf1}_{D_0\cap K}.           \tag{8.8}
\]

Then every `g_K` lies in the integer kernel of seven-window incidence, and
for every collection `I` of overlay components,

\[
             {\bf1}_{D_0}+\sum_{K\in I}g_K            \tag{8.9}
\]

is another strict wreath decomposition.  In particular any putative
strict-wreath solution can be reached from MSW by a sequence of global
component switches which preserves degree, upper exactness, component
length fifteen, and the exact seven/eight run arrangement at every
intermediate step.

If `A_6` denotes six-window incidence, the lower ledger after (8.9) is

\[
 A_6{\bf1}_{D_0}+\sum_{K\in I}A_6g_K.                \tag{8.10}
\]

#### Proof

Every noncancelled seven-set is an overlay edge.  Its old and new owners lie
in the same connected component, so each `g_K` covers that row equally on its
two signs.  Cancelled rows have zero coefficient in every `g_K`.  This proves
`A_7g_K=0`.  Toggling any union of components therefore leaves every
seven-set covered exactly once.  Theorem 8.1 supplies all other assertions,
and (8.10) is additivity of six-window incidence.  `square`

This is a genuine residence-preserving global rebundling theorem, but not
an existence proof: it describes the exact route to a target decomposition
once that target is known.  A proper alternating cycle in the ownership
overlay need not itself be a legal move, because a wreath column cannot be
partially selected; the legal conformal packets are whole overlay
components (or unions of them).

## 9. Fractional slack and the first integral obstruction

### Theorem 9.1 (MSW orbit barycentre)

Average the edge indicators of all coordinate relabelings of the canonical
MSW wreath decomposition.  The resulting point lies in the convex hull of
literal strict-wreath factors and has

\[
 \bar x_e={1\over28}\qquad(e\in E(J(15,7))),
 \tag{9.1}
\]

middle degree two, upper load one, and lower load `9/7` at every target.

#### Proof

The symmetric group is transitive on Johnson edges.  There are

\[
 |E(J(15,7))|={6435\cdot56\over2}=180180
\]

edges, while each factor selects `6435`, giving weight `1/28`.  A middle
vertex has 56 incident edges.  The providers of one upper colour form the
28 edges between its eight facets, while the providers of one lower colour
form the 36 edges between its nine supersets.  The three loads are therefore

\[
       {56\over28}=2,\qquad {28\over28}=1,
       \qquad {36\over28}={9\over7}.
\]

Every averaged factor is a strict wreath decomposition, so the point lies
in their literal convex hull.  `square`

Thus the ordinary convex edge/load relaxation of the run-perfect
strict-wreath polytope already meets every lower-cover halfspace with uniform
slack `2/7`.  No real linear/Farkas separator in those original variables can
refute this subclass.  Lifted integer-valid inequalities and nonlinear or
statewise chronology obstructions are not excluded.

There is not even a marginal-integrality obstruction.  Every upper-exact
selector has

\[
 \sum_R\lambda_R=6435,
 \qquad
 \sum_{R\ni x}\lambda_R=2574\quad(x\in\Omega).        \tag{9.2}
\]

An explicit hole-free integral load vector satisfying (9.2) is available.
Identify `Omega` with `Z_15`.  The translation orbit of

\[
       \{0,1,5,6,10,11\}                              \tag{9.3}
\]

has size five and coordinate degree two.  Adjoin any 95 distinct free
translation orbits of six-sets; each has size fifteen and coordinate degree
six.  Their union `E` has

\[
       |E|=5+95\cdot15=1430,
       \qquad \deg_E(x)=2+95\cdot6=572.               \tag{9.4}
\]

There are 333 free orbits, so this choice is possible: the only nonfree
rank-six sets are the ten unions of two of the five three-cycles of
translation by five.  Therefore

\[
                \lambda_R^*=1+{\bf1}_{R\in E}         \tag{9.5}
\]

takes only the values one and two and satisfies (9.2).  Equation (9.5) is a
load vector, not yet a factor realization.

For two upper-exact factors let `d_R=lambda'_R-lambda_R`.  Equation (9.2)
forces

\[
       \sum_Rd_R=0,
       \qquad \sum_{R\ni x}d_R=0\qquad(x\in\Omega). \tag{9.6}
\]

Hence a unit Robin--Hood drift `e_A-e_B` is impossible unless `A=B`, and no
nonzero drift can have support at most three.  For three support cells, put
the one or two positive coefficients on one side of (9.6); every coordinate
of a negative set must then belong to every positive set with full
coefficient, forcing all support sets to coincide.

The first possible marginal drift has four cells.  With `|K|=4` and
distinct `a,b,c,d` outside `K`, one example is

\[
 e_{Kac}+e_{Kbd}-e_{Kab}-e_{Kcd}.                    \tag{9.7}
\]

The integer kernel of point-versus-six-set incidence is generated by these
hypersimplex rectangles.  The signed wreath-move lattice theorem in
`MATH_ATTACK_J_WREATH_FIBRE_MARKOV_BASIS_20260725.md` realizes the whole
rectangle lattice after abelianization at `m=7`.  It does **not** prove that
the required rectangles are simultaneously conformal, binary, or
applicable at MSW.  That statewise lifting is exactly the unresolved step.

## 10. Sharp proved boundary

Let `Omega_w` be the set of cyclic orders modulo rotation and reversal, and
let `A_j` be cyclic `j`-window incidence.  The smallest sufficient theorem
isolated by the strict-wreath route is

\[
 \boxed{
 \exists z\in\mathbb Z_{\ge0}^{\Omega_w}:
       A_7z={\bf1},\qquad A_6z\ge{\bf1}.}
 \tag{10.1}
\]

The first equation automatically makes `z` squarefree and gives 429
wreaths.  By Theorem 8.1, (10.1) is equivalent to the no-rainbow-star
condition (8.5) and proves `RTR(7,4)`.  Starting at MSW `z_0`, it is
equivalently the existence of one global signed integral rebundling

\[
 g\in\ker_{\mathbb Z}A_7,\qquad
 z_0+g\in\{0,1\}^{\Omega_w},qquad
 A_6(z_0+g)\ge{\bf1}.                                \tag{10.2}
\]

Call (10.1) the **wreath collision-rounding lemma `WCR(15,7)`**.  It is a
more restrictive sufficient statement than unrestricted `RTR(7,4)`, because
it requires a witness whose every component is a length-fifteen wreath.  The
converse implication is not established.

A monotone circuit theorem asserting that every imperfect wreath factor
admits an applicable kernel packet which strictly decreases its number of
rainbow stars would imply (10.1) by integer descent.  That assertion is
stronger than existence and is not proved.  The orbit barycentre, the
rectangle lattice, and the known positive-density two-wreath moves do not
by themselves supply conformal statewise packing.

The two live, sharply scoped missing lemmas are therefore:

1. `WCR(15,7)`, a direct run-perfect collision rounding theorem; or
2. the fixed MSW--PBBS global frame-circulation lemma of Section 7, which
   permits nonwreath intermediate geometry but restricts the edge atlas.

Either lemma proves `RTR(7,4)`.  Failure of either one alone is
architecture-specific.  No counting, parity, marginal, complement, or real
linear obstruction obtained here refutes unrestricted `RTR(7,4)`.

## 11. Inputs and audit scope

The proof uses only the following established inputs.

* `MATH_THEOREM_K16_BIRESIDENT_COMPLEMENT_DOUBLE_AND_TURN_SELECTOR_20260729.md`
  for the selector normal form and the exact target `RTR(7,4)`.
* `MSW_ATOM_FLOW.md` for the exact MSW wreath partition and its cyclic
  interval form.
* `THREAD_A_COMPOSITE_ODD_PBBS_TWO_MATCHING_SHADOW_FACTOR_20260729.md` and
  `MATH_AUDIT_PBBS_FIRST_SHADOW_THEOREM_20260726.md` for PBBS turn
  surjectivity and the load range `1,2,3`.
* `MSW_SHALLOW_DEFECT_AUDIT.md` and
  `MSW_CRITICAL_CARDINALITY_AUDIT.md` for the finite `r=7` value `837`.

An independent adversarial proof audit rederived the owner-star identity,
automatic upper exactness, overlay-component switch law, barycentre, regular
load construction, and marginal drift claims.  It found no substantive
defect after the scope corrections now stated explicitly: the two missing
lemmas are more restrictive sufficient statements, `g` is signed while its
endpoint is binary, and the Farkas conclusion concerns the ordinary convex
edge/load relaxation.

No computational search, local core enumeration, or claim of an overlay
solution is used here.
