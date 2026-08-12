# `k=17` q1 cores: socket quotient, minimal fan obstructions, binary 2-SAT, and finite refinement

Date: 2026-08-01  
Status: exact abstract classification, exact decoding of the authenticated
dense-bank fan cores, an exact functional-Hall potential, and a finite
termination theorem for monotone pure refinement.  The live
fixed-cardinality provider-gain CEGAR is proved to stall, and the complete
zero-265-preserving one-for-one single-recut face at round 02 is proved
q1-UNSAT.  The 65 compatible pairs drawn from the twelve visible escape
recuts are also proved q1-UNSAT.  A later complete anchor generator includes
the synergistic activations: it has 169,426 joint-zero-265-clean banks, and
all 49 banks which compensate one of the seven dirty central anchors are
independently DRAT-UNSAT.  The remaining 169,377 banks all contain an
individually clean anchor and require retained-core screening or a fresh q1
build.  No termination theorem is obtained for the full two-recut face, added
pure refinement, alternative base cuts, or circuit rethreads.  This note does not
make the frozen bank q1-feasible, prove connectedness or exact residence, or
prove `nu(17)=24313`.

## 1. The orientation variables are an extended formulation

Let there be `n` physical pieces.  Each piece has two physical sockets, so
the socket set `V` has size `2n`.  Let `J` be the fixed perfect matching that
joins the two sockets belonging to the same piece.  A legal physical seam is
an edge `e=uv` between sockets of distinct pieces.  It has one selected
lower-q1 colour

\[
                         \gamma(e)\in\mathcal C,
             \qquad |\mathcal C|=n.                         \tag{1.1}
\]

The relaxed residence predicate used by the dense bank is symmetric on
physical sockets.  The two directed occurrences of one physical seam are
obtained by reversing the alternating piece/seam cycle containing it.

### Theorem 1.1 (exact socket quotient)

An orientation-consistent q1 cycle cover using every selected colour once
is equivalent to a set `M` of physical seams satisfying

\[
 \deg_M(v)=1\quad(v\in V),\qquad
 |M\cap\gamma^{-1}(c)|=1\quad(c\in\mathcal C).              \tag{1.2}
\]

Equivalently, it is a rainbow matching containing one edge of every colour.

#### Proof

Forget the directions in a directed cover.  Its incoming/outgoing seam at a
piece uses its two different physical sockets, so every socket has degree
one and every colour is used once.

Conversely, `J union M` is 2-regular and alternates fixed piece edges with
seam edges.  Orient each of its cycles.  This chooses one common orientation
of every piece and supplies its one incoming and one outgoing seam.  Colour
exactness is unchanged.  Finally, a matching with one edge of each of the
`n` colours has `n` disjoint two-ended edges, so it automatically saturates
all `2n` sockets.  \(\square\)

Thus the orientation Booleans in the 891,633-variable formula are useful
bookkeeping, but they do not define an additional q1 obstruction after the
physical quotient is taken.

There is an equally exact hypergraph formulation.  Make the 3-uniform
hypergraph

\[
 \mathcal H=\bigl\{\{u,v,\gamma(uv)\}:uv\in E(S)\bigr\}
 \quad\hbox{on}\quad V\mathbin{\dot\cup}\mathcal C.         \tag{1.3}
\]

Then (1.2) is precisely a perfect matching of `H`.  Each hyperedge uses two
socket resources and one colour resource.

## 2. The exact family-to-socket Hall cut

For `F subset C`, write `E_F` for the physical seams whose colour lies in
`F`.

### Theorem 2.1 (socket-cover obstruction)

If `X subset V` meets every edge of `E_F`, then every q1 solution satisfies

\[
                              |F|\le |X|.                    \tag{2.1}
\]

If `(F,X)` is inclusion-minimal in `F` among violations of (2.1), then

\[
                              |F|=|X|+1.                     \tag{2.2}
\]

In particular, a minimal violation with one socket is exactly two nonempty
colour families all of whose candidate edges use the same socket.

#### Proof

The selected edges of colours in `F` are pairwise socket-disjoint.  Since
each meets `X`, charge it to one of its ends in `X`.  The charges are
distinct, proving (2.1).  Equivalently, summing the socket equations over
`X` dominates the sum of the colour equations over `F`.

If a minimal violation had `|F| >= |X|+2`, removing any one colour would
leave a violation covered by the same `X`, contrary to minimality.  This
proves (2.2).  With `|X|=1`, (2.2) gives `|F|=2`, and the remaining statement
is just the definition of a one-vertex edge cover.  \(\square\)

Call the `|X|=1` case a **primal fan**.  It is a pair obstruction, so positive
degree of every individual socket and colour cannot detect it.

There is a dual inequality which also accounts for seams internal to the
socket set.  Let

\[
 \Gamma(Y)=\{\gamma(e):e\cap Y\ne\varnothing\},
 \qquad \nu(Y)=\text{matching number of }S[Y].             \tag{2.3}
\]

### Theorem 2.2 (dual socket-colour capacity)

Every q1 solution satisfies

\[
                         |\Gamma(Y)|+\nu(Y)\ge |Y|
                         \qquad(Y\subseteq V).               \tag{2.4}
\]

#### Proof

Let `m` selected seams have both ends in `Y`.  The selected matching
saturates `2m` sockets of `Y` internally and the remaining `|Y|-2m` sockets
with crossing seams.  Thus exactly `|Y|-m` selected seams meet `Y`.  Their
colours are distinct and belong to `Gamma(Y)`, while `m<=nu(Y)`.  Hence

\[
             |\Gamma(Y)|\ge |Y|-m\ge |Y|-\nu(Y).
\]

This is (2.4).  \(\square\)

If `Y` is independent, `nu(Y)=0`; a matching saturating `Y` uses `|Y|`
different edges and therefore `|Y|` different colours.  The inequality
reduces to

\[
 \bigl|\{\gamma(e):e\cap Y\ne\varnothing\}\bigr|\ge |Y|.   \tag{2.5}
\]

For `|Y|=2`, failure means that two nonadjacent socket requirements can only
be discharged through one colour.  This is the role-reversed **dual fan**.

The second decoded dense-bank core is a dual fan after its forced rows have
been resolved: two surviving socket requirements force two seams of lower
mask `15635`, whose colour capacity is one.  This is a statement about the
resolved core, not a claim that the corresponding raw sockets have degree
one in the full atlas.

## 3. The first and third cores are the same quotient obstruction

The first authenticated core in
`MATH_THEOREM_K17_DENSE_ZERO265_Q1_BOWTIE_UNSAT_CORE_20260801.md`
has two colours, lower masks `18782` and `19038`.  After pairing reverse
directed seams, each colour has one physical candidate edge and both edges
use the same physical socket of piece `1330`.  It is Theorem 2.1 with

\[
 F=\{18782,19038\},\qquad X=\{\text{the exposed socket of piece }1330\}.
                                                                    \tag{3.1}
\]

The third decoded core has central piece `3044` and the following directed
seams:

```text
colour 6946, lower mask 114240
  3044- -> 4159-      (107083)
  3044- -> 5047-      (107084)
  4159+ -> 3044+      (140525)
  5047+ -> 3044+      (167387)

colour 6928, lower mask 113224
  3044- -> 5099+      (107085)
  5099- -> 3044+      (168815)
```

Let `sigma` be the physical socket of piece `3044` exposed as the tail of
`3044-` and as the head of `3044+`.  The reverse directed pairs quotient to
three physical edges:

\[
 \begin{array}{c|c}
 114240&\sigma\! -\! s_{4159},\quad\sigma\! -\! s_{5047}\\
 113224&\sigma\! -\! s_{5099}.
 \end{array}                                                   \tag{3.2}
\]

Every candidate of both colours meets `sigma`, so

\[
       F=\{114240,113224\},\qquad X=\{\sigma\},
       \qquad |F|=2>|X|=1.                                    \tag{3.3}
\]

Therefore the third six-directed-seam core is not a new obstruction
species.  It is the same primal fan as the first four-directed-seam bow tie;
one colour merely has two physical leaves instead of one.  In particular,
both cores are already infeasible in the fractional q1 equations.  They are
not hidden parity failures.

### Corollary 3.1 (exact local repair criterion)

A pure refinement destroys a fixed primal-fan certificate `(F,{sigma})` if
it creates, for at least one colour in `F`, a candidate physical edge not
incident with `sigma`.  Refinements which add only candidates through
`sigma` cannot destroy that certificate.

Because old socket edges persist under pure refinement, once this particular
certificate is destroyed it never reappears with the same `(F,{sigma})`.
This only kills the named core; another core may remain, exactly as happened
after the first dense-bank repair.

## 4. Complete solution of the binary-colour face

The full rainbow socket problem is not 2-SAT, but every residual face on
which each colour has at most two physical candidates is.

### Theorem 4.1 (binary-colour 2-SAT)

Assume

\[
                         1\le |E_c|\le2
                         \quad(c\in\mathcal C).             \tag{4.1}
\]

Introduce one Boolean `z_c` for every two-candidate colour; a one-candidate
colour is a unit choice.  For every two candidate edges of distinct colours
which share a socket, add the clause forbidding those two choices.  The
resulting 2-CNF is satisfiable if and only if the q1 rainbow socket matching
exists.

#### Proof

An assignment chooses exactly one edge of every colour.  The binary clauses
say exactly that no two chosen edges share a socket.  Thus a satisfying
assignment selects `n` disjoint physical edges.  They have `2n` distinct
ends and hence cover all `2n` sockets.  Conversely, a q1 solution supplies
the Boolean choices and violates no conflict clause.  \(\square\)

Consequently, on this face UNSAT is equivalent to the existence of a literal
whose two signs lie in the same strongly connected component of the
implication graph.  Every minimal UNSAT core contains the standard
implication **bicycle**: a path from a literal to its negation and a path
back.  Primal and dual fans are the shortest unit-propagating degenerations
of this classification.

This gives a proof-safe core workflow:

1. quotient reverse directed seams to physical socket edges;
2. separate primal and dual fan cuts first;
3. if the surviving core has at most two candidates per colour, replace its
   general SAT encoding by the exact implication graph;
4. retain the full exact-cover/Benders formulation only for colours with
   three or more live physical candidates.

The current full atlas has high-degree colours, so Theorem 4.1 classifies its
small decoded cores, not the whole 7,612-colour instance.

## 5. Why ordinary matching or matroid parity does not close the full row

Dropping colours from (1.2) leaves ordinary perfect matching.  Keeping
colours changes the object to a rainbow perfect matching, equivalently the
3-uniform exact cover (1.3).

This distinction is structural:

* Socket-disjoint edge sets are not the independent sets of a matroid.  On
  the path with edges `a=12`, `b=23`, `c=34`, the matchings `{b}` and
  `{a,c}` violate exchange: neither element of the larger matching can be
  added to the smaller one.
* Ordinary graph matching can be written as matroid parity in a partition
  matroid on endpoint-incidence copies.  Adding one colour resource to each
  selectable pair turns it into a three-element object.  This is matroid
  3-parity (or matroid parity with an additional partition constraint), not
  ordinary polynomial-time matroid parity.
* On a bipartite socket graph with shores `X,Y`, assigning colour `z` to edge
  `xy` identifies a seam with a triple `(x,y,z)`.  A rainbow perfect matching
  is exactly perfect three-dimensional matching.  The positive-degree
  assumption is only removal of singleton zero rows and does not change
  that general expressive class.

Therefore the undirected socket quotient alone does **not** reduce the full
problem to ordinary matching, 2-SAT, matroid intersection, or standard
matroid parity.  Such a reduction would need an additional theorem using
the Boolean-intersection and residence structure of the Johnson-generated
atlas.  No such exchange theorem is presently proved.  This paragraph is
not a hardness proof for the exact `k=17` Johnson subclass; it identifies why
the generic algorithms do not follow merely from taking the socket quotient.

## 6. A finite pure-refinement termination bound

There is nevertheless an unconditional q1-only termination theorem.

### Theorem 6.1 (full-refinement termination)

Let a lower-rainbow factor have `W` owners and let its current segmentation
have `p` pieces.  Assume every remaining internal factor gap may be refined.
Repeated pure refinement reaches a q1-feasible socket system after at most

\[
                              W-p                              \tag{6.1}
\]

additional cuts.

#### Proof

Each cut increases the piece count by one.  At `p=W`, every piece is a
singleton owner.  Select as seams all original factor adjacencies.  At each
new internal socket this is the canonical seam supplied by refinement.  The
factor is lower-rainbow, so these seams use every lower-q1 colour exactly
once; and the original factor cycles use every singleton piece socket once.
They are therefore a rainbow socket perfect matching.

Equivalently, the canonical transparent-refinement lift contracts every new
canonical seam and recovers the preceding segmentation.  No refinement can
destroy a q1 solution, and full refinement has the explicit solution just
described.  \(\square\)

For the frozen dense bank,

\[
                         W=24310,\qquad p=7612,
\]

so the raw bound is `16698` further cuts.  This is a finiteness theorem, not
a useful optimal-construction bound.  Full singleton refinement reconstructs
the old factor cycles and need not satisfy exact cyclic residence,
connectedness, the deeper upper deck, or the terminal compiler.  Protected
uncut gaps also require replacing (6.1) by the number of cuts in a certified
allowed terminal refinement.

## 7. Consequence for the dense-bank CEGAR

The first and third exact cores should be priced as the linear socket-cover
cut

\[
        \sum_{c\in F}\sum_{e\in E_c}x_e=|F|
        \ \le\
        \sum_{v\in X}\sum_{e\ni v}x_e=|X|,                 \tag{7.1}
\]

not as opaque directed-orientation conflicts.  For both, `|F|=2` and
`|X|=1`.  A pricing move must expose an off-central provider for one named
colour.  The second core should instead be priced on its dual two-socket,
one-colour fan after forced-row contraction.

The exact q1 CEGAR can therefore permanently learn these quotient cuts and
use binary implication cores whenever the residual colour degrees fall to
two.  What remains genuinely global is the high-degree rainbow matching;
after that, connectedness, exact residence, all-width upper coverage, and
the compiler are still separate gates.

## 8. The `114930` core is another dual fan, not a provider-shortage core

The next decoded core has sole named lower mask `114930`, colour index 6961,
and incumbent directed-provider degree `80`.  Its directed seams quotient as
follows.  Put

\[
 s=L(3669),\qquad t=L(3670),                              \tag{8.1}
\]

where `L(P)` is the socket exposed as the tail of `P-` and the head of `P+`.
Every physical candidate in the core joins either `s` or `t` to one of

\[
 R(1827),L(2198),L(3370),L(3671),R(3671),
 L(5585),R(5585),L(7423).                                \tag{8.2}
\]

There is no `st` edge, and every displayed edge has the same colour 114930.
The retained core has 139 original clauses and 45 DRAT lemmas (1,851
resolution steps, no RAT lemma).  Its only central orientation variables are
those of pieces 3669 and 3670 (piece 7423 appears in a leaf implication), and
no rank-ten coverage row occurs in the core.

If piece 3669 takes orientation zero, its forced outgoing row uses a 114930
seam at `s`; if it takes orientation one, its forced incoming row uses a
114930 seam at the same physical socket `s`.  Hence either orientation forces
one 114930 seam at `s`.  The identical argument applies to `t` for piece
3670.  Since there is no `st` seam, these are two different selected seams,
while the colour AMO permits at most one.

Thus `s` and `t` are two independent socket requirements whose surviving
colour neighbourhood is the singleton `{114930}`.  It is exactly the dual
fan (2.4):

\[
                         |Y|=2>1=|N_{\mathcal C}(Y)|,
                \qquad Y=\{s,t\}.                         \tag{8.3}
\]

This decoding changes the right pricing target.  Adding another 114930 edge
from `s` or `t` to an outside leaf does not help: colour capacity is still
one and the two central sockets still require two seams.  The certificate is
destroyed only by at least one of the following:

1. a legal 114930 seam `st`, which covers both central sockets with its one
   permitted colour occurrence;
2. a legal seam of some other colour at `s` or `t`;
3. a rethread which changes one of the two forced socket roles.

The first census scanned all `16667` one-coordinate substitutions which
replace the chosen extra cut by another allowed candidate inside the same
already-split base piece.  It does not scan every possible added cut,
base-cut change, second cut, or two-piece rethread.  Exactly `13043` preserve
the complete zero-265 local ledger, and none has directed 114930 degree
greater than 80.  Provider identities were not compared.  **That degree
statement alone is not a radius-one q1 UNSAT
theorem**, because item 2 can break the dual fan without changing the
114930 degree.  A subsequent exact enumeration of the different-colour
incidence mode finds precisely 12 of the 13043 clean children with a
non-114930 seam at `s` or `t`; every one has zero direct `st` seam of colour
114930.  An independent occurrence-level replay supplies, for every one of
the 12, a surviving opposite 114930 arm with a distinct outside socket.
Thus all 12 genuinely destroy the *local* dual-fan certificate.  Complete
rebuilt q1 formulas for the 12 banks are nevertheless all UNSAT, and all 12
text proofs are independently DRAT-verified.  The other 13031 clean children
retain the dual fan literally.  Therefore the fixed one-for-one
single-recut face is closed, although the local one-colour certificate by
itself is not stable.

No unrestricted C6/C8 necessity follows.  A second recut, an added pure
refinement cut, a cut relocation outside the fixed face, or a larger circuit
may leave that face and realize a different global exchange.

The exact reason two cuts can be genuinely necessary follows directly from
the socket-age criterion.

### Theorem 8.1 (two-lock activation criterion)

Let a raw Johnson seam `e=st` join endpoint owners

\[
 A=C\cup\{p\},\qquad B=C\cup\{q\}.
\]

Let `a_s`, `a_t` be the inward endpoint ages, and suppose the canonical
endpoint-singletonizing cuts `b(s),b(t)` are both allowed.  Among these two
cuts, the minimum number required to make `e` resident-legal is two if and
only if

\[
                         a_s(p)<d+1
             \quad\hbox{and}\quad
                         a_t(q)<d+1.                         \tag{8.4}
\]

If (8.4) fails and `e` is not already legal, one of the two cuts suffices.

#### Proof

Cutting `b(s)` makes every coordinate present at socket `s` have age
`infinity`.  It therefore repairs the deleted-coordinate condition for `p`
and every common-coordinate sum

\[
                         a_s(x)+a_t(x)\ge d+1\quad(x\in C),
\]

but it does not change the opposite exclusive condition `a_t(q)>=d+1`.
Symmetrically, cutting `b(t)` repairs the inserted-coordinate condition for
`q` and all common sums, but not `a_s(p)>=d+1`.

Hence both cuts are necessary exactly when both exclusive conditions fail;
then the two cuts together make all relevant ages infinite and are
sufficient.  If at most one exclusive condition fails, cut its own end; if
only common sums fail, either end works.  \(\square\)

Call a raw seam satisfying (8.4) **two-locked**.  The theorem gives the
smallest exact two-cut provider test; no C6/C8 search is needed to formulate
it.

### Corollary 8.2 (smallest exact primal-fan core-breaking condition)

Let a decoded q1 core have a tight socket set `X` for a named colour family
`F`, as in Theorem 2.1.  A two-cut endpoint-singletonization breaks that
specific certificate by provider addition if and only if there are

* a colour `c in F`;
* a raw candidate seam `e=st` of colour `c` with `e cap X` empty;
* two allowed endpoint cuts `b(s),b(t)`;
* both exclusive ages short as in (8.4);

and the simultaneous pair of cuts preserves whatever protected local rows
are imposed by the construction face.

The first three bullets identify an off-tight provider and the fourth says
why it is absent from every one-cut atlas but present after the pair.  Once
created, refinement monotonicity preserves it permanently.

This corollary applies directly to the primal fans of Sections 3, but 114930
is the dual fan (8.3).  Its smallest exact two-cut audit must instead test:

* two-locked raw seams of a colour other than 114930 at `s` or `t`;
* a two-locked raw `st` seam of colour 114930; and
* two-cut role relocations which remove `s` or `t` from the forced shore.

Only if all three catalogues are empty (or exactly replayed no-go) is it
justified to promote this core to a genuine C6/C8 or higher exchange target.

### Retained round-02 evidence

Remote root:

```text
/home/amodo/or15/work/laneL_k17_dense_persistent265_20260801/cegar
```

```text
round02.core.cnf
  SHA-256 354e3aef1fa6512c29409656a7ab93c1049759f33b9bd2852830cb77ce54f56f
round02.core.seams.tsv
  SHA-256 e677dc6af4f760bd9e42d3cf320775e77992edab257a270a15ee724475305a8f
round02.dratcheck.out
  SHA-256 698ffa6045b26dd64ab110054c186053f6a49d7c444fa269aad2c24eb0161229
round02.scan.out
  SHA-256 b2fc1aeb830ed5fd4cc34ba672a6cf6354a4dbd0d3a2804588acad3ee45ef61c
```

## 9. Exact functional-Hall defect

The physical deficiency in Section 6 is the cleanest invariant under pure
refinement.  For a fixed-cardinality cut replacement it is also useful to
retain the exact directed functional-Hall form.

For a cut bank `C`, let `P(C)` be the integral orientation/head--colour
master from
`MATH_THEOREM_COLORED_ENDPOINT_FUNCTIONAL_HALL_AND_PARITY_OBSTRUCTION_20260801.md`.
For `(z,u) in P(C)` and a family `X` of oriented tail states, let `A_X(C)`
be the selected head--colour columns having a legal predecessor in `X`, and
put

\[
 d_C(z,u)=
 \max_X\left(
   \sum_{v\in X}z_v-
   \sum_{a\in A_X(C)}u_a
 \right)_+ .                                             \tag{9.1}
\]

Define

\[
              \delta_{\rm FH}(C)=
              \min_{(z,u)\in P(C)}d_C(z,u),              \tag{9.2}
\]

with value `infinity` when the master itself is infeasible.

### Theorem 9.1 (exact q1 score)

The bank `C` has an orientation-consistent coloured q1 cycle cover if and
only if

\[
                         \delta_{\rm FH}(C)=0.             \tag{9.3}
\]

For a finite family `Q` of admissible one-cut children, every child is q1
infeasible if and only if

\[
                         \min_{C'\in Q}
                         \delta_{\rm FH}(C')>0.            \tag{9.4}
\]

#### Proof

For fixed `(z,u)`, Hall's theorem says that the maximum predecessor matching
misses exactly `d_C(z,u)` selected tails.  Optimizing over the integral
orientation/head--colour master proves (9.3).  Taking the minimum over the
finite child family proves (9.4).  \(\square\)

Thus provider degree, number of decoded cores, singleton support and three
pairwise projection ranks are not termination potentials.  A one-cut move
is certified strict progress only when it lowers the global quantity in
(9.2), or lowers an independently proved well-founded refinement potential.
Destroying the returned DRAT core is not enough.

### Theorem 9.2 (exact all-Hall-shore progress test)

Fix one integral functional master and write `B,B'` for its predecessor
graphs before and after a cut replacement.  For a head family `Y`, put

\[
 d(Y)=|Y|-|N_B(Y)|,qquad D=\max_Y d(Y),                 \tag{9.4a}
\]

and

\[
 \kappa(Y)=
 |N_{B'}(Y)\setminus N_B(Y)|-
 |N_B(Y)\setminus N_{B'}(Y)|.                           \tag{9.4b}
\]

Then, for every integer `a>=0`,

\[
 \nu(B')\ge n-D+a                                      \tag{9.4c}
\]

if and only if

\[
 \boxed{\ \kappa(Y)\ge d(Y)-D+a
             \quad\hbox{for every }Y.\ }               \tag{9.4d}
\]

#### Proof

The exact neighbour identity is

\[
 |Y|-|N_{B'}(Y)|=d(Y)-\kappa(Y).
\]

Taking the maximum over `Y` and applying the Hall-deficiency formula gives
(9.4c)--(9.4d).  \(\square\)

In particular, a one-unit increase must gain one neighbour on **every**
old maximum-deficiency shore and obey the corresponding nonloss inequalities
on every near-critical shore.  Adding a provider for one returned core is
only one necessary local test.  This all-shore criterion is the exact
proof-level explanation for core hopping in the live sequence.  When the
cut also changes the orientation/head--colour master, Theorem 9.1 requires
optimizing this test over the new integral master; no single frozen shore is
then sufficient.

### Theorem 9.3 (guided pure-refinement potential)

Let

\[
 \delta_3(C)=p(C)-\nu_3(C),                              \tag{9.5}
\]

where `nu_3(C)` is the maximum matching rank in the physical
socket--socket--colour hypergraph.  On the hereditary pure-refinement face,
let

\[
 \lambda(C)=\min\{|D|:\delta_3(C+D)<\delta_3(C)\},       \tag{9.6}
\]

where `D` ranges over commuting bundles of allowed additional cuts; set
`lambda(C)=infinity` if no such bundle exists.

If `lambda(C)` is finite and `D` is a minimum witness, then for every
`g in D`,

\[
 \delta_3(C+g)\le\delta_3(C),                            \tag{9.7}
\]

and, when equality holds,

\[
 \lambda(C+g)\le\lambda(C)-1.                            \tag{9.8}
\]

Consequently the lexicographic potential

\[
                         (\delta_3,\lambda)               \tag{9.9}
\]

strictly decreases when the next cut is chosen from a minimum improving
bundle.  If every remaining internal factor gap is allowed, full refinement
makes `lambda` finite at every positive-defect state, so guided one-cut
addition terminates at q1 feasibility.

#### Proof

Here a pure cut adds two new private socket resources, one new private colour
resource, and their disjoint canonical triple; every old triple persists.
The canonical triple of `g` therefore extends a maximum old matching,
proving (9.7).  If
the deficiency does not fall, the commuting bundle `D-{g}` still reaches
`C+D`, whose deficiency is strictly below the current value.  It therefore
witnesses (9.8).  Full singleton refinement has deficiency zero by Theorem
6.1.  \(\square\)

This theorem permits neutral preparatory cuts; it does not say that the
current core has a one-cut rank improvement.  More importantly, replacing
one selected cut by another can delete old atoms and sockets.  Equations
(9.7)--(9.9) therefore do **not** apply to the live 7,612-piece
fixed-cardinality CEGAR without a separate persistence proof.

The need for a neutral preparation is sharp even abstractly.  On sockets
`1,2,3,4`, let

\[
 E_c=\{12,34\},\qquad E_d=\{13,24\}.                    \tag{9.10}
\]

The rainbow matching deficiency is one.  Let one pure cut expose `c`-edge
`14` and a second expose `d`-edge `23`, each with its private canonical
split atom.  Neither one-cut child lowers the deficiency, while the two-cut
child selects `14` and `23` and has deficiency zero.  All socket and colour
singleton rows remain nonzero throughout.  Hence no theorem can require a
strict rank drop at every individual cut.

## 10. What the live provider-gain CEGAR actually proves

In this census, **zero-265-preserving** means that literal rebuild leaves all
five local counts zero: deleted-lower-colour zeros, outgoing-piece zeros,
incoming-piece zeros, common-orientation-piece zeros, and immediate-upper
rank-ten zeros.  The name recalls the original `187+78` support debt; it is
not a claim about global q1 feasibility.

The authenticated tail of the Lane L sequence is:

| round | bank SHA prefix | named core masks | baseline degrees | zero-265-preserving replacements | strict named-degree gains | chosen replacement |
|---:|---|---|---:|---:|---:|---|
| 00 | `0e3a5873` | `114874,114930` | `2,50` | 13,055 | 11 | `1685:9129->9128` |
| 01 | `401fe41f` | `114874,114930` | `2,66` | 13,043 | 9 | `913:4918->4922` |
| 02 | `48670b1b` | `114930` | `80` | 13,043 | 0 | none |

All three bank formulas are DRAT-verified UNSAT.  Their retained cores use,
respectively, `113/35`, `137/54`, and `139/45` original clauses/lemmas.
The round-02 proof is the dual fan decoded in Section 8.

### Theorem 10.1 (provider-gain rule stalls)

Consider the rule which, after receiving a core with named colour `c`, is
allowed to move only to a zero-265-preserving one-cut replacement having
strictly larger raw provider degree for `c`.  On authenticated round 02 this
rule has no legal successor although the incumbent is q1-UNSAT.

#### Proof

The exact scan rebuilds all 16,667 one-cut replacements, retains the 13,043
with the complete zero-265 local ledger, and reports no child with provider
degree greater than the incumbent value 80.  The incumbent's verified DRAT
proof establishes q1-UNSAT.  \(\square\)

This refutes termination for the **provider-gain rule**.  By itself it does
not prove that every one-cut child is q1-UNSAT, nor even that the physical
114930 provider set is unchanged: a count-neutral deletion and insertion
may replace one provider by another.  The separate complete single-recut
audit below is load-bearing for the stronger fixed-face no-go.

## 11. Exact socket escape from the round-02 dual fan

Work after contracting the forced rows used in the round-02 proof.  Let

\[
                         Y=\{s,t\}
       =\{L(3669),L(3670)\},qquad c=114930.              \tag{11.1}
\]

In the retained core, `s,t` are independent mandatory sockets and every
surviving incident edge has colour `c`.  For a rebuilt one-cut child, first
redo the forced contraction and delete all already consumed socket and
colour resources.

### Theorem 11.1 (two-socket escape criterion)

If `s,t` remain mandatory residual sockets, the displayed dual-fan
certificate is destroyed exactly when the residual star contains either

1. one available edge `st` of any unused colour; or
2. two edges `su` and `tv` with `u!=v`, distinct available colours, and no
   used socket or colour resource.

It is also destroyed if the rebuilt forcing no longer leaves both `s,t` as
mandatory residual sockets.

#### Proof

An `st` edge saturates both sockets with one allowed colour.  In the absence
of such an edge, any matching saturating `s,t` must use one incident edge at
each socket.  Socket disjointness forces distinct outside endpoints and
rainbow exactness forces distinct colours, giving item 2.  Conversely either
displayed pattern is a resource-disjoint local matching saturating `Y`.
If the forced roles change, (11.1) is no longer the residual demand and the
old certificate is inapplicable.  \(\square\)

### Corollary 11.2 (exact persistence outside the escape cone)

Suppose a rebuilt child leaves `s,t` as mandatory residual sockets, creates
no available `st` edge, and leaves every available residual edge incident
with `s` or `t` coloured `c`.  Then arbitrary changes to seams not incident
with `s` or `t` preserve the dual-fan obstruction.

#### Proof

Any matching saturating the two independent sockets must use two distinct
incident edges.  Both have colour `c`, contradicting colour capacity one.
Deleting old arms only shrinks the two stars and cannot repair the
inequality; edges disjoint from `{s,t}` never enter it.  Consequently a
move elsewhere can invalidate this literal certificate only by creating an
`st` edge, creating a non-`c` incident arm, or changing one of the two forced
socket roles.  \(\square\)

Accordingly an exact one-cut socket-escape audit must test three things for
every zero-265-preserving child:

* count-neutral as well as count-increasing changes to the 114930 edge set,
  especially a new `st` edge;
* every newly available non-114930 edge at `s` or `t`, together with a
  disjoint opposite 114930 arm; and
* changes in the unit/forced rows which expose different socket roles.

The original named-degree scan tests none of these exhaustively.  Passing one of
them only kills the named dual-fan proof; Theorem 9.1 must still be evaluated
to certify q1 feasibility.

The independent socket-role scan tests direct-114930 incidence and the
presence of a different-colour incidence on the fixed round-02 roles.  Among
all `16667` replacements it again finds `13043` zero-265-clean children and
exactly 12 different-colour incidences.  Their direct-114930 `st` count is
zero.  Hence the one-colour premise of round 02 is **not** cut-stable and
cannot support a C6/C8 lower bound.  Independent owner-mask replay verifies
that each row has a disjoint surviving opposite 114930 arm, so all 12 have
local rank two.  Complete q1 formulas for all 12 escape banks are nevertheless
DRAT-verified UNSAT; the other 13031 clean children retain the dual fan.
Equivalently, for the finite family `Q` of zero-265-preserving one-for-one
single recuts,

\[
       \min_{C'\in\mathcal Q}\delta_{\rm FH}(C')>0.       \tag{11.2}
\]

No numerical value of this minimum deficiency is asserted.

The nine recuts of the two central lock pieces give a useful direct
cross-check.  Exactly one is zero-265-clean:
`1834:9924->9923`; it retains the dual fan and its complete q1 formula is
DRAT-verified UNSAT.  The other eight fail a local rebuild row.  Seven have
a lower-colour zero, while `1835:9933->9932` has a zero tail state, a zero
head state and a zero common-orientation row; its separately emitted q1
formula is also DRAT-verified UNSAT, but it is not a clean child.  The point
of this nine-row ledger is that no literal recut of either lock piece was
overlooked.  All nine were already included in the complete 16667-row
partition.  Thus q1 radius one is closed on this fixed replacement face,
although the residual cores of the 12 local escapes may differ.

## 12. Hamming-two pricing and when a C6 conclusion would become valid

Let `E` be the twelve one-recut moves which individually create a local
non-114930 socket escape.  There are `binom(12,2)=66` formal unordered pairs.
Two members of `E` are alternative replacements of the same old cut in base
2251 and cannot coexist, leaving exactly 65 compatible pairs.  Literal
composition and replay shows that every one of the 65 preserves the complete
zero-265 ledger and has a distinct rebuilt socket-atlas signature.

### Theorem 12.1 (independent-arm depth-two shell)

Every q1 formula obtained by applying one compatible pair from `E` to the
round-02 bank is UNSAT.  Hence two individually visible socket-escape moves
do not repair q1, even when they address opposite central sockets and carry
different colours.

This is not an exhaustion of the Hamming-two face.  In particular it does
not test

* one visible escape together with an arbitrary neutral blocker-rerouting
  recut;
* two recuts `g,h` for which neither singleton changes the socket graph but
  a joint seam satisfies

  \[
   e\in E(H_{g,h})\setminus
        \bigl(E(H_g)\cup E(H_h)\cup E(H)\bigr);          \tag{12.1}
  \]

* a pair which rescues a singleton local-zero failure, a central-role pair,
  an added pure cut, or a non-cut circuit rethread.

The second bullet is exactly the synergistic two-lock phenomenon of Theorem
8.1.  Thus the 65-pair result closes the **independent-arm shell**, not
two-cut activation in general.

#### Proof

The pair census applies all 66 formal pairs to the literal cut assignment.
It rejects the unique same-base pair and rebuilds the other 65, all with
zero five-component local score.  The complete orientation/socket/colour q1
formula returns UNSAT for each rebuilt bank, and all 65 text proofs are
independently DRAT-verified.  The listed exclusions are not members of this
finite pair family.  \(\square\)

### 12.2 Four residual core-price classes

The newly trimmed escape-child cores (a later pricing reduction, not the
earlier raw DRAT-core bundle) have only four principal lower-mask patterns.
The files `core.seams.tsv` are headerless, so the reported counts
`6,28,29,36` are the actual directed seam-row counts.  Physical pricing is
done only after reverse-pairing and forced-row contraction.

| first-child indices | directed lower-mask multiplicities | seam rows | price class |
|---|---:|---:|:---:|
| `e00` | `118996:6` | `6` | `A` |
| `e06` | `14820:6` | `6` | `B` |
| `e11` | `87145:36` | `36` | `C` |
| `e01,e02,e03,e04,e07,e08,e09,e10` | `115308:28` | `28` | `D` |
| `e05` | `115308:28,117348:1` | `29` | `D+pendant` |

Thus the primary named-core price of nine children is the same class `D`;
the extra `117348` row of `e05` is a side guard, not a fifth primary
price class.  This is a compression of the **named physical core row**, not
an identification of the twelve full cut banks.  Exterior socket resources,
the lower-colour bank and other Hall shores can still differ.

The physical quotient identifies the forced dual fan in every class.  The
following are labelled socket masks, not mutable piece indices.

| class | locked sockets (forced pieces) | core colour | quotient arms | direct-seam upper label |
|:---:|---|---:|---|---:|
| `A` | `127188` (`p1507`), `119028` (`p2078`) | `118996` | path `119508-127188-119004-119028` (3 reverse pairs) | `127220` |
| `B` | `14821` (`p3505`), `14828` (`p3789`) | `14820` | path `15844-14821-15332-14828` (3 reverse pairs) | `14829` |
| `D` | `115310` (`p3924`), `119404` (`p7179`) | `115308` | owner-mask `K_{2,5}`, physical `K_{2,7}` (14 reverse pairs) | `119406` |
| `C` | `87147` (`p1790`), `119913` (`p6616`) | `87145` | owner-mask `K_{2,6}`, physical `K_{2,9}` (18 reverse pairs) | `119915` |

For the locked pair `Y={s,t}` in each row,

\[
             \nu(S[Y])=0,\qquad \Gamma(Y)=\{c\},\qquad
             |\Gamma(Y)|+\nu(S[Y])=1<2=|Y|.             \tag{12.2a}
\]

Thus all twelve trimmed cores are literal instances of the dual-fan cut in
Theorem 2.2.  In `e05` the extra directed pendant of colour `117348` joins
`117356` to `125540` and misses both locked sockets, so it does not change
(12.2a).  Within a labelled class the local breaker oracle is consequently
exact: add a non-core-colour arm at one lock while retaining a
resource-disjoint core-colour arm at the other; add the displayed direct
lock-to-lock seam; or relocate a locked role.  Same-core-colour spoke growth
and edits confined to the `e05` pendant cannot break this certificate.

For a class `alpha`, let `Q_alpha` be its forced, reverse-paired physical
socket/colour core.  For a candidate joint recut set `P`, define the local
price

\[
 r_\alpha(P)=
 \nu\bigl(Q_\alpha\cup A_\alpha(P)\bigr)-\nu(Q_\alpha), \tag{12.2}
\]

where `A_alpha(P)` contains only newly available physical triples after all
consumed sockets and colours are deleted.  Two first children admit a shared
second-recut price exactly when their labelled cores and the complete maps
`P -> A_alpha(P)` agree.  Equality of the retained mask and seam count alone
is necessary but not sufficient for this stronger response equivalence.

### Theorem 12.2 (two-resource activation for noncentral recuts)

Anchor a forced core socket by its owner occurrence.  Let `g,h` be recuts in
two distinct noncentral base pieces.  For a raw central--leaf seam `e`, write

* `G_e(D)=1` when, after forced contraction, every **non-colour** availability
  predicate for `e` is legal in child `D`: endpoint roles and owners,
  Johnson/residence, survival of the leaf socket, and every fixed local
  resource guard, but not the selected-lower-colour test; and
* `K_e(D)=1` when `gamma(e)` belongs to the selected lower-colour bank of
  `D`.

Assume these non-colour predicates are leaf-local: with the anchored central
role fixed, a noncentral recut can change `G_e` only when it changes the base
piece containing the leaf occurrence.  This is exactly the locality used by
the literal round-02 socket atlas.  Because `G_e` is the complete
non-colour predicate, (12.3) remains an identity without leaf-locality, but
the one-mover conclusion (12.4) can then fail: jointly activated non-colour
guards require their own interaction columns in addition to the joint-debt
ledger below.

Then

\[
       e\in E(H_D) \quad\Longleftrightarrow\quad
       G_e(D)K_e(D)=1.                                  \tag{12.3}
\]

If `e` occurs in the joint child `C_{gh}` but in neither singleton child,
then, after possibly exchanging `g,h`,

\[
 G_e(C_g)=1,qquad K_e(C_g)=0,qquad
 \gamma(e)=n_h\in K(C_{gh})\setminus K(C_g),            \tag{12.4}
\]

where `n_h` is the lower colour inserted by recut `h`.  In words: `g` is the
geometry mover and `h` is the colour supplier.  Such a seam is invisible in
both singleton socket graphs.

#### Proof

A noncentral recut changes the stipulated non-colour availability predicates
only in its own base piece.  With the anchored central state fixed, those
predicates for a changed central--leaf seam can therefore depend on at most
one of `g,h`.  Once they hold, membership in the contracted residual atlas is
exactly the selected-colour guard, proving (12.3).  If availability and
colour were already present together in either singleton, `e` would occur
there.  Otherwise the
recut changing the leaf supplies geometry while the other recut must supply
the missing selected colour, which is (12.4).  \(\square\)

A cross-activated arm is only one necessary resource.  It repairs the local
two-socket demand only if the opposite lock retains an arm with a distinct
outside socket and a distinct colour, as in Theorem 11.1; full q1 feasibility
still requires extension to a complete resource matching.  Thus (12.4) is
an exact candidate-generation theorem, not a sufficiency claim.

The exclusion from a visible-singleton list is sharp even abstractly.  Start
with fan arms `sx(c),ty(c)`.  Let `g` make a raw arm `su(d)` non-colour-legal
without selecting `d`, and let `h` select `d` without changing `u`.  Neither
singleton gains an actual socket edge, but the joint child gains `su(d)`.
If `u!=y` and `ty(c)` survives, the pair is a local rainbow saturation of
`s,t`.  This example proves that a singleton-escape anchor cannot be complete
without an independent Boolean theorem excluding the product activation.

For every raw seam, (12.3) gives a Cartesian geometry--colour activation
table.  The exact core-guided Hamming-two master must therefore contain four
types of columns:

1. unary arms already present in a singleton child;
2. cross columns `G_{alpha,e} x K_{gamma(e)}` from (12.4);
3. literal central-base/forced-role changes; and
4. joint local-debt compensation columns for pairs whose singleton child is
   not zero-265-clean.

The previously proposed 21-anchor set (nine central recuts plus twelve clean
singleton escapes) is complete only after excluding columns 2 and 4.  The
65-pair theorem tests only pairs drawn from column 1.  It says nothing about
the two-resource columns of Theorem 12.2.

### Corollary 12.3 (proof-safe shared pricing, but no recut potential)

The twelve first children require only four primary local price rows, with
one pendant guard for `e05`.  A second-recut CEGAR may share a row across a
class by using its labelled physical quotient and the full unary/cross/role/
debt response table above.  After satisfying that local row it must still
evaluate `delta_FH` from Theorem 9.1; killing a class does not prevent the
next exact core from lying in another class.

Consequently neither the number of distinct retained masks nor the number
of repaired price classes is a monotone termination potential for
one-for-one recuts.  Finite exact pair enumeration with learned no-goods is
a decision procedure, but the only proved constructive monotone potential
in this note remains `(delta_3,lambda)` on pure refinement.

The labelled-quotient qualification is sharp.  Take two one-colour dual
fans with the same colour and the same number of seam literals, but forced
socket pairs `{s,t}` and `{u,v}`.  A recut which supplies a new noncore-colour
arm only at `s` can break the first fan and leaves the second unchanged.
Thus retained mask and multiplicity alone cannot define an exact shared
second-recut class; the forced socket owners and the complete recut-response
map in (12.2)--(12.4) are indispensable.

The rank-eight/rank-nine Boolean incidence graph has no 4-cycle: two
distinct rank-eight sets have at most one common rank-nine superset, namely
their union.  Therefore every nontrivial closed degree-preserving factor
exchange decomposes into alternating cycles of length at least six.

This does **not** make C6 or C8 necessary at round 02.  The exact result is
that a successful zero-265 bank has Hamming distance at least two inside the
fixed one-for-one replacement face.  Two recuts and an added pure cut are
not closed factor exchanges.  Only after those resegmentation faces are
excluded may one conclude, within the *separate* class of closed
degree-preserving exchanges, that the next move has support at least C6.
Nothing presently forces C8 rather than C6.  The three named C6/C8 attempts
already audited as UNSAT are three scoped points, not an exhaustion of that
class.

## 13. Audited artifact scope

The local manifest

```text
scratch/l_k17_dense_q1_cegar_20260801/manifest.tsv
SHA-256 9591f41014fd9cd1e842e7db98fd50d5f0b44cedee1583570edbc56e3230a45e
```

binds all three bank/CNF/proof/core/scan families.  In particular,

```text
round00.bank.tsv  0e3a58738722f8a1c6cf2e58292a1b6a411269b7ecd1536c8adcaf587d91f8a4
round01.bank.tsv  401fe41f2db6351c4fc8ce7697d241d6a9b285fa608326617837c24c7694e3e3
round02.bank.tsv  48670b1bf5388ed4c8f47a408e4659c145ec26dc3d6a6bb31cd379a1e70ad649
```

and the round-02 core/proof check are exactly the hashes retained at the end
of Section 8.  No solver was rerun for this theorem audit.

The corrected radius-one socket and full-q1 audit is

```text
scratch/search_l_k17_round02_dualfan_socket_escape_20260801.cpp
  SHA-256 76421ec6df9450bb962859c29f060778ad66caa616bdc3b210e1c8d3f2eaabac
scratch/threadD_k17_mask114930_core_20260801/round02.socket_escape_v2.tsv
  SHA-256 88893f08ea810662df0ef44be9d227ad53ff19485f27034d8827c6083f6b29ef
scratch/threadD_k17_mask114930_core_20260801/round02.socket_escape_v2.out
  SHA-256 3bdaa40f39c8af0384c39825547f679c269b05db75665c5bc094af90a9f9eb49
scratch/threadD_k17_mask114930_core_20260801/round02.socket_escape_v2.replay.audit.json
  SHA-256 acd445b17f288de6d60f51b9b95b8bbd2868f2589f321501e5f8b6e4222427d4
scratch/l_k17_dense_q1_cegar_20260801/summary.tsv
  SHA-256 9e80b335755f7abe60a69420147717a3c1aed64b8dc8f0a4689bdb71f2023464
scratch/l_k17_dense_q1_cegar_20260801/proof_manifest.tsv
  SHA-256 95150d58c3cb0782468bd1572ca8e34c117de7e70c7c80200cc3719c8321dbff
scratch/k17_round02_dualfan_radius1_20260801/summary.tsv
  SHA-256 a5a5685ba78d6a979ea667447fba7165a61a84b589ebe6f370c6f579883332de
scratch/k17_round02_dualfan_radius1_20260801/core_piece_drat_summary.tsv
  SHA-256 e2ec901aa6afff7a5d64023f3400ae8c361a12798faf9f1b5b32bebf2a7740ce
scratch/k17_round02_dualfan_radius1_20260801/escape_pairs.tsv
  SHA-256 7b2edd1557f4fe94e6c88acdc362ffb18b88cd21f8bf6e03eb3699f5c89556b7
scratch/k17_round02_dualfan_radius1_20260801/escape_pairs.audit.json
  SHA-256 fe5fb127e9d405574f9e1b7da7f2cc7fcdb98794ce0a881e6497819099123b70
scratch/k17_round02_dualfan_radius1_20260801/escape_pairs.q1_summary.tsv
  SHA-256 b2cdcece539162e9a0eee4ad4ebcdfc0597cc075e0b8732674511753add8a39b
scratch/k17_round02_dualfan_radius1_20260801/escape_pairs.drat_summary.tsv
  SHA-256 006c2c09177248228cf40a20d78472ee28abcc581c95308050546f3db6a1f3f3
scratch/k17_round02_dualfan_radius1_20260801/escape_core_mask_classes.audit.tsv
  SHA-256 ac0a55728381ad5493c5174093e9647533d1088dc5d35fcc0987efcacce42c2b
scratch/k17_round02_dualfan_radius1_20260801/escape_core_summary.root.tsv
  SHA-256 d1336ed1131393f5bdfe10556718af7a5ddf838a1880ad36029ab643689998e3
scratch/k17_round02_dualfan_radius1_20260801/escape_core_drat_summary.root.tsv
  SHA-256 39a4f41f4d2ecae4ad6273f86eed6de92d95dc6639e0f0355738265f3368f9c0
```

The occurrence replay authenticates the 12 local rank-two escapes; the
summary and proof manifest authenticate their separate full-q1 UNSAT
verdicts.  The complete fixed-face theorem is
`MATH_THEOREM_L_K17_ROUND02_DUALFAN_COMPLETE_SINGLE_RECUT_NOGO_20260801.md`.
None of these artifacts certifies topology, assembled residence, deeper
shadows, or compiler feasibility.

## 14. Later fixed-face closure of dirty-single compensation

The complete final-net anchor theorem subsequently replaced the conditional
21-anchor shortcut above.  On the same fixed distinct-base, one-for-one
Hamming-two face it proves that every breaker contains one of nine central
or twelve visible anchors, even when one recut creates raw socket geometry
and the other selects its lower colour.  Its exact product contains

\[
 349642\text{ compatible banks},\qquad
 169426\text{ joint-zero-265-clean banks}.               \tag{14.1}
\]

The role-changing central anchor `1835:9933->9932` has no jointly clean
partner.  Each of the seven locally dirty central anchors
`1834:9924->9925,...,9931` has exactly the same seven compensators.  These
are 49 distinct final banks.

### Proposition 14.1 (dirty-central compensation is closed)

Every one of those 49 banks is q1-UNSAT.  The canonical replay regenerates
the complete bank/CNF/maps byte for byte, obtains Kissat exit 20 on every
row, and verifies every proof independently with `drat-trim`.

Consequently the fixed-face residual is

\[
                       169426-49=169377,                 \tag{14.2}
\]

and every residual bank contains at least one of the thirteen individually
clean anchors: the twelve visible escapes or the clean central-state move
`1834:9924->9923`.

#### Proof

The complete anchor census supplies the seven-by-seven dirty-central
incidence and proves that there are no other jointly clean banks supported
only by a dirty central anchor.  The proof manifest contains 49 rows with 49
distinct bank, CNF and proof hashes; every row records a canonical rebuild,
UNSAT verdict and verified DRAT proof.  Subtraction gives (14.2), while the
anchor column of every remaining census row lies in `0,...,12`.  \(\square\)

This proposition closes dirty-single compensation only.  It does not prove
that the 169,377 residual banks are q1-feasible or q1-infeasible.  The
proof-safe next filter is occurrence-labelled semantic core persistence:
retain complete effective positive-row provider sets, resource clauses and
named blockers, including geometry--palette and two-endpoint cross atoms.
The frozen 13-profile filter certifies 164,323 residual banks UNSAT and
promotes 5,054 to fresh exact q1 rebuilding.  `EXACT_BUILD` is inconclusive,
not a feasibility verdict.  Only rejection of all 5,054 would prove that
Hamming radius two fails inside this one-for-one face; it would imply no
unrestricted Hamming-three, C6/C8/q4 or global `k=17` conclusion.

The proof-grade compact bundle is

```text
scratch/threadD_k17_round02_dirtycentral49_q1_20260802/proof_manifest.tsv
  SHA-256 7959c9ce00d855cd187fe24e770e785f908dee5106cef8daf75480a75d55c0b6
scratch/threadD_k17_round02_dirtycentral49_q1_20260802/theorem.audit.json
  SHA-256 bf468abc0fd076613c81b21468f23e8e947e153eeff3d85e4bb52b15705e32f9
scratch/threadD_k17_round02_dirtycentral49_q1_20260802/THEOREM_SCOPE.txt
  SHA-256 bcda315af6bff664e7cb4a29df52479af4218e0008423a2a537bfa12316ca81d
```

The full remote bundle's `artifacts.sha256` has SHA-256
`52eba4e2c2869b5b04324062f3959f733e464338d6ce8de577aaaf5b25d89ca9`.
The independent scope and persistence audit is
`MATH_AUDIT_K_K17_DIRTY_CENTRAL49_Q1_AND_CORE_PERSISTENCE_FRONTIER_20260802.md`.
