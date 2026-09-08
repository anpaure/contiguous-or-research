# Colorful facet-socket paths: exact Hall cuts, sufficient dispersion, and the PBBS wedge obstruction

Date: 2026-07-31  
Lane: AD, general mathematics  
Status: proved graph/transducer theorems and proved counting obstructions.
No residence, lower-`q1` restitution, lower compiler, or coefficient-one
claim is made.

## 0. Verdict

The remaining fixed-width upper-socket quantifier has an exact finite
formulation.  It is not an ordinary component-level Hall problem.

1. For a fixed component order, existence of a colorful linear socket chain
   is exactly nonvanishing of a Boolean product of facet transducers.
2. Globally, the exact integral formulation is the usual selected-path
   degree system plus one rooted connectivity/subtour inequality for every
   proper set of component colours.  Those inequalities are separable by a
   directed minimum cut.  Omitting them leaves precisely a path together
   with directed subtours.
3. Three useful sufficient criteria are proved:

   * ordered live-bank expansion;
   * a rooted robust-quotient Dirac criterion;
   * Hall cycle cover plus compatible two-cycle switches.

4. Projecting away the opening state is genuinely unsound.  There is a
   three-colour chamber obstruction in which the component projection is
   complete, every option has neighbours in `b-2` other colours, and every
   proper subfamily has a colorful path, but no full colorful path exists.
   The obstruction is realizable by local wedge fragments in `J(9,5)`.
5. At odd middle rank `k=2m+1`, `r=m+1`, the complete upper-`q1` deck has
   only

   \[
        {2W\over m+2},\qquad W={2m+1\choose m+1},
   \]

   units of adjacent-repeat overload.  Therefore a full-rotation,
   unit-voltage factor has at most

   \[
        {2\operatorname{Cat}_m\over m+2}
   \]

   wedge-bearing components.  A linear all-wedge socket chain may use one
   arbitrary safe root, but all other components must be wedge-bearing.
   Thus a `Theta(Cat_m)`-component unit-voltage multi-spiral cannot satisfy
   this socket quantifier.  A dense Dirac criterion is even more restrictive:
   it can apply only after reduction to `O(sqrt(Cat_m))` invariant
   components.

The exact surviving asymptotic gate is a **sparse, option-level
facet-dispersion/rotation theorem after component reduction**, or a stronger
seam theorem that permits nonwedge destination cuts.  PBBS all-depth support
and multi-spiral residence do not currently imply this gate.

## 1. Directed opening graph

Let `F` be a spanning directed cycle factor of `J(k,r)`, with vertex-disjoint
simple components of length at least three,

\[
                       C_1,\ldots,C_b.                 \tag{1.1}
\]

Fix, once and for all, one directed fixed-width witness for every protected
upper target and assign that witness to its provider component.  This is the
assigned tower required by the fixed-width facet-seam theorem.

### 1.1 Root openings and socketable openings

A directed opening `x` of `C_i` is obtained by cutting one directed cycle
edge and retaining the resulting directed path.  Write

\[
                         S(x),\quad E(x)              \tag{1.2}
\]

for its start and end.  Let `R_i` be the openings whose cut is **safe at the
root**: every selected fixed-width witness assigned to `C_i` avoids that cut.
The opening in `R_i` need not be a wedge opening.

A socketable opening `p` is a signed right-wedge opening.  Thus for some
wedge centre `A`, with two cyclic neighbours `L_A,R_A`, one chooses one
neighbour as `S(p)` and puts

\[
 E(p)=A,
 \qquad
 U(p)=L_A\cup A=A\cup R_A,
 \qquad |U(p)|=r+1.                                  \tag{1.3}
\]

Let `O_i` be the socketable openings of `C_i`.  Both signs at one wedge
centre have the same endpoint `A` and the same union `U`, but different
service/start facets.

The input facets accepted by `p` are

\[
 \begin{aligned}
 I(p)
   &=\{B\in {[k]\choose r}:B\cup S(p)=U(p)\}\\
   &= {U(p)\choose r}\setminus\{S(p)\}.
 \end{aligned}                                      \tag{1.4}
\]

Hence `|I(p)|=r`.  Two members of `I(p)`, namely `E(p)` and the opposite
wedge neighbour, already lie on the destination component.  Consequently
at most `r-2` accepted facets can lie on other components.

### Definition 1.1 (opening graph)

The coloured directed opening graph has colour classes

\[
                         V_i=R_i\cup O_i.             \tag{1.5}
\]

There is an arc

\[
                         x\longrightarrow p
 \quad\Longleftrightarrow\quad
                         E(x)\in I(p),                \tag{1.6}
\]

where `x` and `p` have different component colours and `p` is socketable.
Equivalently,

\[
                         E(x)\cup S(p)=U(p).          \tag{1.7}
\]

Vertices in `R_i\setminus O_i` have no incoming role and may occur only as
the first vertex.  A **safe colorful linear socket path** is a directed path
containing exactly one vertex of every component colour, whose first vertex
lies in its safe set `R_i`.

### Proposition 1.2 (upper-tower implication)

Every safe colorful linear socket path gives a literal concatenation of the
opened component paths which preserves every selected fixed-width upper
witness, simultaneously at every protected depth.

#### Proof

The root cut preserves every witness assigned to the first component by the
definition of `R_i`.  Every later component is opened at a wedge flank, and
its incoming arc is exactly the facet identity (1.7).  The fixed-width
facet-seam theorem therefore replaces every assigned witness crossing that
cut by a seam-crossing witness of the same width and union.  Witnesses not
crossing a cut remain literal internal intervals.  Apply this independently
to the assigned witness of every target.  \(\square\)

This implication concerns upper witnesses only.  It says nothing about the
new seam's coordinate runs, the cut lower-`q1` colours, or a common lower
compiler.

The graph is exact **relative to the fixed assigned tower**.  If the witness
assignment is allowed to depend on the root component, construct one
root-labelled graph for each such assignment (or retain the assignment as
part of the safe-root label) and take their disjunction.  Collapsing two
different assignment labels merely because their cuts have the same endpoint
is not an upper-safety equivalence.  Once the label is fixed, however, the
endpoint alone is the complete socket-transition state used below.

## 2. Exact facet transducer and fixed-order theorem

For a component `C_i`, define its endpoint transducer

\[
 T_i(B)=\{E(p):p\in O_i,\ B\in I(p)\},               \tag{2.1}
\]

and extend it to sets by `T_i(X)=union_(B in X) T_i(B)`.  Define the safe
root endpoint set

\[
                         Q_i=\{E(x):x\in R_i\}.       \tag{2.2}
\]

### Theorem 2.1 (exact Boolean-product criterion)

Fix a permutation `sigma` of the `b` component colours.  Put

\[
 X_1=Q_{\sigma(1)},
 \qquad
 X_t=T_{\sigma(t)}(X_{t-1})\quad(2\le t\le b).       \tag{2.3}
\]

There is a safe colorful socket path in component order `sigma` if and only
if

\[
                              X_b\ne\varnothing.      \tag{2.4}
\]

Equivalently, if `M_ij` is the Boolean incidence matrix of socket arcs, then

\[
 \mathbf 1_{R_{\sigma(1)}}^{\mathsf T}
 M_{\sigma(1),\sigma(2)}\cdots
 M_{\sigma(b-1),\sigma(b)}\mathbf 1\ne0             \tag{2.5}
\]

over the Boolean semiring.

#### Proof

Induct on `t`.  The set `X_t` is exactly the set of endpoint labels attainable
after a compatible chain through the first `t` colours.  This is true at
`t=1` by (2.2).  If it is true at `t-1`, an endpoint `A` is attainable at
step `t` exactly when some attainable input endpoint `B` belongs to the
accepted-facet set of a socketable opening on `C_(sigma(t))` with endpoint
`A`; this is exactly `A in T_(sigma(t))(X_(t-1))`.  Thus (2.3) is both
sound and complete.  Backtracking the successful relations gives the actual
openings.  \(\square\)

The endpoint is a sufficient state: an opening's compatibility with the next
component depends only on its endpoint, while its compatibility with the
previous component is already certified by the transition that produced it.

### Corollary 2.2 (ordered live-bank dispersion)

Fix an order `sigma`, endpoint banks `D_(sigma(t))`, and integers
`a_t>=1`.  Suppose

\[
 |Q_{\sigma(1)}\cap D_{\sigma(1)}|\ge a_1,           \tag{2.6}
\]

and, for every `2<=t<=b` and every
`X subseteq D_(sigma(t-1))` with `|X|>=a_(t-1)`,

\[
 |T_{\sigma(t)}(X)\cap D_{\sigma(t)}|\ge a_t.        \tag{2.7}
\]

Then a safe colorful socket path exists in order `sigma`.

#### Proof

Intersect each set in the recursion (2.3) with the declared live bank.
Equations (2.6)--(2.7) inductively keep at least `a_t` attainable endpoints,
so the final set is nonempty.  Apply Theorem 2.1.  \(\square\)

This is a genuine option-level Hall/dispersion condition.  It permits sparse
graphs and is the scale-correct form to seek in PBBS.  Pairwise component
degree does not imply (2.7).

## 3. Exact global Hall formulation

The next theorem identifies exactly what ordinary successor Hall omits.
Use the opening graph of Definition 1.1.  For each opening vertex `v`, let
`x_v` select it, `a_v` mark it as the first vertex, and `e_v` mark it as the
last vertex.  For every socket arc `uv`, let `y_uv` select it.  All variables
in this section are binary.

Impose

\[
 \sum_{v\in V_i}x_v=1                              \tag{3.1}
\]

for every colour `i`,

\[
 \sum_v a_v=\sum_v e_v=1,
 \qquad a_v\le x_v,\quad e_v\le x_v,               \tag{3.2}
\]

with `a_v=0` for `v notin R_(colour(v))`, and the degree equations

\[
 \sum_{u:uv\in A}y_{uv}=x_v-a_v,
 \qquad
 \sum_{w:vw\in A}y_{vw}=x_v-e_v.                   \tag{3.3}
\]

For a component-colour set `I`, write `E[I]` for arcs whose two endpoint
colours lie in `I`.

### Theorem 3.1 (rooted component-subtour theorem)

The integral solutions of (3.1)--(3.3) are a selected safe-rooted directed
path together with zero or more vertex-disjoint directed cycles.  They are
exactly the safe colorful spanning paths after adding, for every nonempty
proper component set `I`,

\[
                    \sum_{uv\in E[I]}y_{uv}\le |I|-1.            \tag{3.4}
\]

Using (3.3), (3.4) is equivalently the rooted entering cut

\[
 \sum_{\substack{uv\in A:\ 
                  \operatorname{col}(u)\notin I,
                  \operatorname{col}(v)\in I}}y_{uv}
       +\sum_{\operatorname{col}(v)\in I}a_v\ge1.                \tag{3.5}
\]

The family (3.5) is separable, including at fractional points, by at most
`b` directed minimum-cut computations after adding a super-root whose arc
into colour `i` has capacity `sum_(v in V_i)a_v` and forcing one colour at
a time to lie on the nonempty side of the cut.

#### Proof

Equations (3.1)--(3.3) give every selected noninitial vertex indegree one,
every selected nonterminal vertex outdegree one, one unit of positive
imbalance at the start, and one unit of negative imbalance at the end.
Thus the selected arcs decompose into one start-to-end path and directed
cycles.  A directed cycle whose component-colour set is `I` uses exactly
`|I|` arcs in `E[I]` and violates (3.4).  Conversely, the subgraph induced
by any proper colour set on one directed path is a disjoint union of path
segments and contains at most `|I|-1` arcs, so a colorful spanning path
satisfies every row.

Summing the indegree equation in (3.3) over the one selected vertex of every
colour in `I` gives

\[
 \sum_{uv\in E[I]}y_{uv}+y(\delta^-(I))=|I|-a(I),                \tag{3.6}
\]

which makes (3.4) and (3.5) equivalent.  The latter is the standard cut
capacity from a super-root to `I`; minimizing it over proper nonempty `I`
is a directed min-cut separation.  \(\square\)

Thus an ordinary successor matching, and hence ordinary Hall inequalities,
settles only the degree/cycle-cover layer.  The exact missing inequalities
are the rooted connectivity cuts (3.5), not another rankwise marginal.

## 4. Three positive graph criteria

### 4.1 Robust quotient and a rooted Dirac theorem

Choose a nonempty live set `D_i subseteq O_i` for every nonroot component.
Define the robust directed component relation

\[
 i\Rightarrow j
 \quad\Longleftrightarrow\quad
 \text{every }x\in D_i\text{ has a socket successor in }D_j.     \tag{4.1}
\]

Let `M` be its mutual graph: `{i,j}` is an edge of `M` exactly when both
`i=>j` and `j=>i` hold.

### Theorem 4.1 (rooted robust Dirac criterion)

Choose a root colour `rho`, a safe root opening `x_0 in R_rho`, and a
nonroot colour `j_0` with a socket arc from `x_0` to some member of `D_j0`.
Put `n=b-1`.

* If `n=1`, this one root arc is sufficient.
* If `n=2`, suppose the two nonroot colours are adjacent in `M`.
* If `n>=3`, suppose the mutual graph on the nonroot colours satisfies

  \[
                   \delta(M)\ge \left\lceil{n\over2}\right\rceil.          \tag{4.2}
  \]

Then a safe colorful socket path exists.

#### Proof

For `n>=3`, the classical Dirac argument is included for completeness.
Condition (4.2) makes `M` connected: two components would each have more
than `n/2` vertices.  Take a longest path
`v_1,...,v_l`.  Every neighbour of either endpoint lies on the path.  The
sets

\[
 \{i:v_1v_{i+1}\in E(M)\},
 \qquad
 \{i:v_iv_l\in E(M)\}
\]

are subsets of `{1,...,l-1}` and have total size at least `n>=l`; hence they
intersect.  The corresponding two chords close a cycle through all `l`
path vertices.  If `l<n`, connectivity supplies an edge from outside that
cycle and hence a longer path, a contradiction.  Therefore `M` has a
Hamilton cycle.

Rotate this cycle so that it starts at `j_0` and delete its closing edge.
Choose the already available successor of `x_0` in `D_j0`.  At each later
step, (4.1) supplies a compatible option in the next colour for the option
already chosen.  This greedily lifts the component path to an opening path.
The cases `n=1,2` are immediate.  \(\square\)

The universal quantifier in (4.1) is essential for greedy lifting.  An
existential component arc does not remember whether the same intermediate
opening can receive the preceding socket and supply the next one.

### 4.2 Hall plus rotation/exchange

Let `H` be a robust directed component graph on the nonroot colours.

### Theorem 4.2 (Hall--two-switch criterion)

Suppose

\[
                         |N_H^+(X)|\ge|X|            \tag{4.3}
\]

for every component set `X`.  Hall's theorem gives a directed cycle cover
`f`.  Suppose further that **every** directed cycle cover of `H` with at
least two cycles has vertices `x,y` in different cycles such that

\[
                         x\to f(y),\qquad y\to f(x). \tag{4.4}
\]

Then `H` has a directed Hamilton cycle.  If a safe root has an arc into the
declared live bank of one of its colours, the cycle can be rotated there and
lifted to a safe colorful linear socket path.

#### Proof

Hall gives a perfect successor matching, hence a cycle cover because the
graph has no component loops.  Under (4.4), delete `x->f(x)` and `y->f(y)`
and add the two crossed arcs.  The two old cycles become one directed cycle;
all indegrees and outdegrees remain one.  Repeating reduces the number of
cycles until a Hamilton cycle remains.  Robustness lifts it exactly as in
Theorem 4.1.  \(\square\)

This is the precise rotation-extension supplement missing from projected
Hall.  It may hold in a sparse graph even when Dirac density is impossible.

### 4.3 Product palettes

For each nonroot component, suppose there are nonempty input and output
palettes `P_i^-` and `P_i^+` such that

\[
 P_i^-\times P_i^+
 \subseteq
 \{(B,A):A\in T_i(B)\}.                             \tag{4.5}
\]

Define a palette-overlap arc `i->j` when

\[
                         P_i^+\cap P_j^-\ne\varnothing.           \tag{4.6}
\]

For a root, replace `P_rho^+` by its safe endpoint palette.  Any rooted
Hamilton path in this overlap graph lifts to a colorful socket path: at
each intermediate component choose its incoming and outgoing seam labels
independently inside the rectangle (4.5).  Consequently Theorems 4.1 or 4.2
may be applied to the smaller palette-overlap graph.

Equation (4.5) is a strong but usable local dispersion statement.  Merely
having many input labels and many output labels separately is insufficient;
the same opening transducer must couple them.

## 5. Sharp projection obstructions

### Theorem 5.1 (chamber obstruction)

For every `b>=3` there is a coloured directed opening graph with the
following properties:

1. every option is safe;
2. the existential component projection is complete and bidirected;
3. every option has in- and out-neighbours in exactly `b-2` other colours;
4. every prescribed ordering of every proper component subfamily has a
   compatible colorful path;
5. no colorful path uses all `b` colours.

#### Proof

For every `j in [b]`, form a chamber `H_j` containing one option of every
colour except `j`.  Put all bidirected arcs between distinct colours inside
one chamber and no arcs between different chambers.  Any ordered proper
colour set omits some `j`, so it can be routed inside `H_j`.  Every directed
path remains in its initial chamber and hence omits that chamber's missing
colour.  The other assertions are immediate.  \(\square\)

Thus the worst-case option-level colour-degree threshold

\[
                         \delta^+_{\rm col}\ge b-1                \tag{5.1}
\]

is sharp: (5.1) permits greedy routing through the remaining colours in any
order, whereas Theorem 5.1 fails at `b-2`.  Notice that the component
projection in the counterexample already has maximum possible degree.

The smallest component count is `b=3`.  This is not only an abstract graph
artifact.  Put `r=5`, `k=9`, and choose three six-sets with complements

\[
 \{1,2,3\},\qquad \{1,4,5\},\qquad \{2,4,6\}.        \tag{5.2}
\]

Their pairwise intersections have size four.  In the six-set assigned to
chamber `j`, partition its six facets into two triples, one for each other
colour, and order each triple as predecessor--centre--successor.  Each
triple is a legal wedge fragment with that six-set as its common union.
The two fragments in one chamber socket reciprocally.  No facet from one
chamber is contained in another chamber's six-set because their intersection
has size only four.  All eighteen local middle vertices are distinct.
This realizes the chamber incidence inside `J(9,5)`.  Completion of these
fragments into a prescribed global spanning factor is not asserted.

### Proposition 5.2 (Hall without connectivity)

Ordinary successor Hall can fail with only four singleton colour classes:

\[
                         1\leftrightarrow2,
 \qquad                 3\leftrightarrow4.          \tag{5.3}
\]

The successor bipartite graph has a perfect matching, but there is no
spanning path.  Four is minimal in the loopless singleton-option model,
because a cycle cover on at most three vertices is a single cycle and
deleting one edge gives a spanning path.  The two cycles in (5.3) are
exactly what the rows (3.4)--(3.5) remove.

## 6. Exact facet-incidence budget

Let `Z_d` be the wedge centres on component `C_d`.  For distinct colours
`c,d`, define

\[
 I_{cd}=\#\{(B,A)\in Z_c\times Z_d:B\subset U_A\}.   \tag{6.1}
\]

### Theorem 6.1 (socket multiplicity and external-facet capacity)

The number of signed opening arcs from `C_c` to `C_d` is exactly

\[
                              4I_{cd}.               \tag{6.2}
\]

Moreover,

\[
 \sum_{c\ne d}I_{cd}\le(r-2)|Z_d|.                 \tag{6.3}
\]

#### Proof

For every incidence `(B,A)`, there are two source orientations at `B` and
two destination orientations at `A`.  The source endpoint is `B` under
either source orientation.  Because `B` is on another component, it differs
from both destination service facets, and `B subset U_A` is equivalent to
the facet-socket identity.  This gives exactly four arcs and proves (6.2).

For a fixed destination centre `A`, the three distinct facets
`A,L_A,R_A` of `U_A` already lie on `C_d`.  Only the remaining `r-2` facets
can be wedge centres on other components.  Sum over `A in Z_d`.  \(\square\)

Formula (6.2) counts wedge sources.  For a genuinely arbitrary safe root,
let `s_c(B)` be the number of safe directed openings of `C_c` ending at the
vertex `B` (normally `0`, `1`, or `2`).  The exact safe-root arc count into
the wedge openings of `C_d` is instead

\[
 2\sum_{A\in Z_d}\ 
   \sum_{\substack{B\in V(C_c)\\B\subset U_A}}s_c(B).             \tag{6.4}
\]

The factor two is the destination orientation.  Restricting (6.4) to
wedge centres `B in Z_c` recovers the corresponding safe subset of (6.2).

## 7. Odd-middle overload and the PBBS/multi-spiral obstruction

Assume now

\[
                         k=2m+1,\qquad r=m+1,\qquad m\ge2,         \tag{7.1}
\]

and put

\[
 W={2m+1\choose m+1}=(2m+1)\operatorname{Cat}_m.    \tag{7.2}
\]

Every directed factor edge has upper-`q1` colour `A_i union A_(i+1)`, an
`(r+1)`-set.  Let `mu_U` be the load of colour `U`.

### Lemma 7.1 (adjacent-repeat overload)

Suppose every upper-`q1` colour occurs and no component has a constant
upper-`q1` colour word.  If

\[
                         D=\sum_d|Z_d|              \tag{7.3}
\]

is the number of wedge centres, then

\[
 \begin{aligned}
 D
 &\le {k\choose r}-{k\choose r+1}\\
 &= {2W\over m+2}.                                  \tag{7.4}
 \end{aligned}
\]

Without the nonmonochromatic hypothesis, the right side must be increased
by at most the number of monochromatic components.

#### Proof

For a fixed colour `U`, decompose its occurrences in all cyclic edge-colour
words into maximal proper runs.  A run of length `a` gives `a-1` wedges.
Because `mu_U>=1`, the total for that colour is at most `mu_U-1`.  Summing
and using `sum_U mu_U=W` proves the first line.  Finally

\[
 {2m+1\choose m+2}={m\over m+2}W,                  \tag{7.5}
\]

which proves the second.  A monochromatic cyclic component contributes one
more adjacent equality than the corresponding linear-run count.  \(\square\)

### Theorem 7.2 (stabilizer-weighted wedge bound)

Let cyclic coordinate rotation act on the factor components, and let `h_d`
be the order of the setwise stabilizer of `C_d`.  Under the hypotheses of
Lemma 7.1, every wedge-bearing `C_d` contains at least `h_d` wedges, and

\[
                  \sum_{d:Z_d\ne\varnothing}h_d
                     \le {2W\over m+2}.             \tag{7.6}
\]

In particular, if every physical component is a unit-voltage quotient lift
and hence is preserved by all `k` rotations, then

\[
 b_{\rm wedge}
     \le {2W\over k(m+2)}
     ={2\operatorname{Cat}_m\over m+2}.             \tag{7.7}
\]

#### Proof

The stabilizer orbit of one wedge centre remains in the same component and
consists of wedge centres.  Rotation acts freely on rank-`r` vertices:
if a nonidentity rotation fixed an `r`-set, that set would be a union of
cycles of a nontrivial divisor of `k`, forcing that divisor to divide `r`,
contrary to

\[
                         \gcd(2m+1,m+1)=1.           \tag{7.8}
\]

Thus the orbit has size `h_d`.  Sum over wedge-bearing components and apply
Lemma 7.1.  For a unit-voltage lift `h_d=k`, yielding (7.7).  A
full-rotation-invariant component cannot be monochromatic: its sole colour
would then be invariant under the one-step cyclic shift, impossible for a
nonempty proper subset.  \(\square\)

### Corollary 7.3 (linear all-wedge obstruction)

A safe linear socket chain may use an arbitrary cut only on its first
component.  All `b-1` later components must be wedge-bearing.  Consequently
a unit-voltage factor satisfying Lemma 7.1 can have such a chain only if

\[
                 b-1\le {2\operatorname{Cat}_m\over m+2}.        \tag{7.9}
\]

An all-wedge cyclic chain has the same inequality with `b` in place of
`b-1`.  Hence a `Theta(Cat_m)`-component unit-voltage multi-spiral fails the
wedge-existence quantifier before any Hall or chronology issue is reached.

For a quotient cycle of voltage `v`, let `g=gcd(k,v)`.  Its `g` physical
lifts have stabilizer order `k/g`; if an actual physical lift, including its
voltage-wrap seam, is wedge-bearing, equivariance makes all `g` lifts
wedge-bearing and their stabilizer weights total `k`.  Thus the number of
wedge-bearing quotient cycles is also at most
`2 Cat_m/(m+2)`, provided q1 completeness and the nonmonochromatic physical
component hypothesis are retained.  This does not bound the number of
physical lifts without controlling the voltages.

The current PBBS theorem supplies only the upper bound
`b<=Cat_m` on its number of physical components; it does not assert
`b=Theta(Cat_m)`, nor does it make every physical component unit-voltage.
Accordingly (7.9) does not refute the actual PBBS factor.  It refutes the
proposed normalization to a Catalan-scale family of individually
unit-voltage wedge-opened components and identifies the voltage/component
reduction that a positive PBBS theorem must still provide.

### Corollary 7.4 (dense Dirac obstruction)

Assume the physical components in the nonroot core are individually
unit-voltage and full-rotation invariant.  Write

\[
                         t_d={|Z_d|\over k}.          \tag{7.10}
\]

The quotient incidence `j_cd=I_cd/k` is integral and (6.3) gives

\[
                         \deg^-(d)\le(r-2)t_d.       \tag{7.11}
\]

If a mutual Dirac core has `n=b-1` colours, then

\[
 \begin{aligned}
 n\left\lceil{n\over2}\right\rceil
 &\le (r-2)\sum_dt_d\\
 &\le {2(r-2)\over m+2}\operatorname{Cat}_m
  ={2(m-1)\over m+2}\operatorname{Cat}_m.          \tag{7.12}
 \end{aligned}
\]

In particular `n<2 sqrt(Cat_m)`.  Therefore the dense Dirac criterion cannot
apply at `b >> sqrt(Cat_m)`.  This is a no-go only for dense Dirac; a sparse
Hamilton path of degree `O(m)` is not excluded.

#### Proof

The cyclic action on incidence pairs is free by (7.8), so `k` divides
`I_cd`.  Every incoming component neighbour consumes at least one quotient
incidence.  Sum the Dirac lower degree over the `n` core colours and use
(6.3), then use (7.4) divided by `k`.  The final strict inequality follows
from the displayed bound.  \(\square\)

## 8. Exact finite interpretation

### 8.1 `k=13`

The authenticated two-component factor has lengths `1547+169`.  The
maximum-flexibility audit finds

\[
 130+52=182                                             \tag{8.1}
\]

oriented assignment-safe, all-upper one-seam splices across the two possible
root orders.  These two summands are the maximum-flexibility order counts.
Separately, the stricter distinguished all-wedge socket convention has `52`
chains; that `52` is not being identified with the second summand in
(8.1).  In wedge-centre incidence coordinates,

\[
 I_{\rm big,small}=26=2k,
 \qquad
 I_{\rm small,big}=0.                                \tag{8.2}
\]

Thus `4I=104` signed all-wedge socket arcs exist in one direction and none
in the other; imposing the distinguished safe-root restriction leaves the
reported `52` chains.  The larger `182` census is valid for `b=2`, where
the root may be an arbitrary safe cut.  It must not be interpreted as a
dense bidirectional internal socket graph for a multi-component chain.

The exact two-colour theorem is simply nonemptiness of one transition
`T_j(Q_i)`, and the `182` census proves that upper-only statement many times.
It does not certify residence, the two lower cut colours, or the common
lower Hall system.

### 8.2 `k=15`

The authenticated factor has lengths `6390+45`.  The large component has
`330` wedges; the length-`45` component has zero.  Hence the latter has an
empty socketable-opening colour class, even though the factor is resident
and fixed-width complete at every upper depth.  This alone rules out an
all-wedge path and the order with the large component as root.  In the
opposite order, the exact maximum-flexibility audit finds `120` facet
sockets from an arbitrary small-component root into a large-component
wedge, but every one of the `45` physical small cuts is provider-forbidden:
`90` chronologies miss one depth-three target and `30` miss one depth-one
and one depth-three target.  Thus the audited selected-tower graph has no
safe colorful path in either order.  This is the smallest current concrete
demonstration that all-depth support plus multi-spiral/residence data do not
imply the facet-socket quantifier.

## 9. Precise remaining theorem

The following statement would now suffice for the upper chronology after a
component reduction, and is not proved.

> **Sparse facet-transducer dispersion lemma (open).**  For the chosen
> PBBS or multi-spiral factor after premerging, there is a component order
> `sigma`, a declared safe root endpoint bank, and live endpoint banks such
> that the ordered expansion inequalities (2.6)--(2.7) hold; equivalently,
> the Boolean product in Theorem 2.1 is nonzero.  An alternative sufficient
> certificate is a robust quotient satisfying Theorem 4.2, with every
> two-switch realized at common intermediate wedge centres.

What is already known does not prove this lemma:

* PBBS all-depth support controls target witnesses, not the distribution of
  wedge facets among component colours.
* Rotation equivariance makes each nonzero incidence occur in a large orbit,
  but all members of that orbit join the same ordered pair of component
  colours.  Multiplicity is not dispersion.
* Multi-spiral lifetime and residence equations do not force a wedge on each
  component; the `k=15` length-`45` component is a direct counterexample.
* Projected pairwise Hall or Dirac statistics do not couple the incoming and
  outgoing socket at the same intermediate opening; Theorem 5.1 shows the
  resulting chamber obstruction.

Even if the open lemma is proved, three independent gates remain:

1. residence across every new seam;
2. restitution or boundary absorption of the lost lower-`q1` colours;
3. feasibility of one common lower compiler/Hall assignment for the final
   literal chronology.

No implication among these three gates is asserted here.

## 10. Audit provenance

The incidence, overload, stabilizer, arbitrary-voltage, and Dirac-budget
calculations were independently audited in

```text
THREAD_AD_PBBS_MULTISPIRAL_FACET_SOCKET_DISPERSION_BUDGET_20260731.md
```

The exact Boolean-product theorem, rooted Dirac lifting, Hall--two-switch
criterion, component-subtour cuts, and chamber obstruction were separately
derived by independent proof audits before integration into this note.
