# Random diamond matchings: the canonical-triple LLL barrier

Date: 2026-07-31  
Status: exact event/dependency counts, a solver-free (m=3) lopsided-LLL
counterexample and complete cycle-shift census.  No all-(m) Catalan
linear matching theorem is claimed.

## 0. Verdict

Let (P) be a uniformly random perfect matching of the diamond graph
(B_m).  Splitting the event

\[
                  d_{\Psi(P)}(X)\ge3
\]

into canonical three-edge events does **not** put the problem in the
ordinary local-lemma regime.

There are

\[
 t_m=6\binom m3^2
\]

canonical triples at one middle vertex.  A fixed event has

\[
                 (3+o(1))m^6
\]

locally conflicting events.  Thus even the optimistic independent-edge
probability (d^{-3}\sim8m^{-6}) gives (pD\to24), whereas the symmetric
LLL needs (epD\le1).  It misses by the constant (24e\), not by a
logarithm or a loose power.

Worse, the usual assertion that disjoint endpoint events may be omitted
from a lopsided dependency graph is false for the uniform matching measure
on (B_m).  At (m=3) two endpoint-disjoint canonical events centred at
complementary middle sets are negatively correlated.  Conditioning on the
complement of one therefore *increases* the probability of the other.

The exact (m=3) census also separates cap two from acyclicity.  Conditional
on cap two, (85.11\%\) of matchings are already forests.  Nevertheless,
among the cyclic cap-two matchings only (26.48\%\) admit either canonical
whole-cycle shift which lowers the cycle count.  Consequently neither
"random perfect matching + local LLL" nor "cap two + always shift open the
cycles" is a proved route.  A correlated factorization or a compound
alternating switch is genuinely additional content.

## 1. Canonical overload triples

Use the notation

\[
 \mathcal L=\binom{[2m]}{m-1},\quad
 \mathcal X=\binom{[2m]}m,\quad
 \mathcal U=\binom{[2m]}{m+1},\quad
 d=\binom{m+1}{2}.
\]

For (X\in\mathcal X), every diamond whose lift is incident with (X)
has the form

\[
 e_{a,b}=\bigl(X-a,X+b\bigr),\qquad
             a\in X,\quad b\notin X.                 \tag{1.1}
\]

These (m^2) diamonds form an (m\)-by-(m) grid.  A perfect matching of
(B_m) restricts to a partial matching in this grid: selected cells have
distinct (a)-rows and distinct (b)-columns.

### Lemma 1.1 (exact canonical-event count)

The event (d_{\Psi(P)}(X)\ge3) occurs if and only if (P) contains one
of

\[
 \boxed{t_m=\binom m3^2,3!
             ={(m)_3^2\over6}}                       \tag{1.2}
\]

canonical triples centred at (X).

#### Proof

Choose three selected grid cells.  Matching compatibility says that their
three rows and columns are distinct.  Thus one chooses three rows, three
columns and a bijection between them.  Conversely any physical degree at
least three contains such a choice. \(\square\)

The action of (S_{2m}) is transitive on canonical triples.  Hence their
probability under the uniform perfect-matching measure is a common number

\[
 p_m={\operatorname {per} A_{-R,-C}\over
             \operatorname {per} A},                 \tag{1.3}
\]

where (A) is the bipartite adjacency matrix and (R,C) are the three
lower and three upper endpoints of a fixed triple.  Formula (1.3) is exact;
it is **not** replaced below by an independence assumption.

## 2. The exact local dependency ledger

### Lemma 2.1 (events through one edge and one shore vertex)

The number of canonical events containing a fixed diamond edge is

\[
 h_m=4\binom{m-1}{2}^2
     =(m-1)^2(m-2)^2.                                \tag{2.1}
\]

The number containing a fixed vertex of either shore of (B_m) is

\[
 q_m=d h_m.                                          \tag{2.2}
\]

#### Proof

A diamond has two physical middle endpoints.  At either one, retain its
grid cell, choose two of the other (m-1) rows, two of the other (m-1)
columns, and one of the two bijections.  This proves (2.1).  Every shore
vertex has (d) incident diamonds, and a canonical triple uses only one of
them, proving (2.2). \(\square\)

Call two canonical events *conflicting* when the union of their diamond
edges is not a matching of (B_m).  Fix an event (E).  At each of its six
shore endpoints there are (q_m-h_m) events choosing a different incident
edge and hence conflicting with (E).

### Lemma 2.2 (conflict degree)

If (D_m^{\rm conf}) is the number of canonical events conflicting with a
fixed event, then

\[
             D_m^{\rm conf}=3m^6+O(m^5).             \tag{2.3}
\]

More explicitly,

\[
 6(q_m-h_m)-15R_m\le D_m^{\rm conf}\le6(q_m-h_m),    \tag{2.4}
\]

where one may take

\[
 R_m=h_m+2dm(m-2)^2=O(m^5).                          \tag{2.5}
\]

#### Proof

The upper bound is the union bound over the six endpoints.  For two fixed
shore vertices, first choose the event edge at the first vertex.  There
are (d) choices and at most two possible physical centres.  Unless this
is the common edge of the two vertices, the edge at the second vertex has
at most (m) choices, after which the third row and column have at most
((m-2)^2) choices.  The common-edge case contributes at most (h_m).
Thus any pairwise intersection has size at most (2.5), and the first two
terms of inclusion--exclusion give the lower bound.  Substitution of
(d=m(m+1)/2) and (2.1) gives (2.3). \(\square\)

### Corollary 2.3 (the symmetric-LLL constant barrier)

The symmetric LLL would require approximately

\[
 p_m\le {1\over eD_m^{\rm conf}}
       ={1+o(1)\over3e,m^6}.                         \tag{2.6}
\]

The optimistic independent-edge calibration is

\[
 d^{-3}={8+o(1)\over m^6},
 \qquad d^{-3}D_m^{\rm conf}=24+o(1).                \tag{2.7}
\]

Therefore a symmetric canonical-event LLL needs the events to be roughly
(24e\) times rarer than the independent-edge scale.  This is a barrier to
that proof scheme, not a proof that a cap-two matching does not exist.

Generic permanent bounds do not repair (2.6).  Van der Waerden below and
Bregman above only give

\[
 p_m\le
 { (d!)^{(N-3)/d}\over d^N N!/N^N},                 \tag{2.8}
\]

whose excess factor over (d^{-3}) is exponential in
(N\log d/d).  Thus a useful estimate for (1.3) itself would already need
substantial Boolean-graph structure.

## 3. The proposed lopsided graph is not valid

A negative dependency graph for bad events must satisfy

\[
 \Pr(E\mid\bigcap_{F\in S}\overline F)\le\Pr(E)      \tag{3.1}
\]

whenever (S) contains only non-neighbours of (E).  For random
permutations on a complete bipartite graph, canonical conflict graphs have
the needed property.  It cannot simply be imported to an arbitrary
allowed-edge graph.

### Theorem 3.1 (exact (m=3) lopsided counterexample)

The graph (B_3) has exactly

\[
                         3,013,854
\]

perfect matchings.  Let (E) be the canonical triple at (X=123)

\[
\begin{array}{lll}
23\mapsto1234,&13\mapsto1235,&12\mapsto1236,
\end{array}                                           \tag{3.2}
\]

and let (F) be the endpoint-disjoint triple at (\bar X=456)

\[
\begin{array}{lll}
56\mapsto1456,&46\mapsto2456,&45\mapsto3456.
\end{array}                                           \tag{3.3}
\]

Then

\[
 \Pr(E)={42,984\over3,013,854}
        ={7164\over502309},                           \tag{3.4}
\]

while

\[
 \Pr(E\cap F)={448\over3,013,854}
              ={224\over1506927}
              <\Pr(E)^2.                              \tag{3.5}
\]

Consequently

\[
 \Pr(E\mid\overline F)
 ={21268\over1485435}
 >{7164\over502309}=\Pr(E).                           \tag{3.6}
\]

Thus neither endpoint overlap nor matching conflict alone is a valid
lopsided dependency graph for these events.

#### Proof

The displayed endpoint sets are disjoint, so the events are compatible
and are nonadjacent in both proposed local graphs.  Equations
(3.4)--(3.5) follow by exact permanent enumeration of the (15\)-by-(15)
allowed-edge matrix and its two conditioned minors.  Equation (3.6) is
algebra.  The audit cited below independently enumerates every perfect
matching. \(\square\)

For a fixed (E), exactly (53) canonical events are incompatible with
it.  All six canonical events centred at (\bar X) satisfy the strict
inequality (3.5), so any valid lopsided dependency graph must give (E)
degree at least (59).  The optimal symmetric criterion at degree (59)
is

\[
 {59^{59}\over60^{60}}=0.00618292\ldots,
\]

whereas (3.4) is (0.01426214\ldots).  Hence the symmetric lopsided LLL
fails already in the first nontrivial dimension by a factor (2.306\ldots).

This does not rule out an asymmetric or resampling argument with a richer
state.  It does rule out the advertised local dependency graph and shows
that its missing correlation theorem cannot be treated as routine.

## 4. What happens to cycles after cap two

The same exhaustive audit gives

\[
\begin{array}{c|r}
\text{all perfect matchings}&3,013,854\\
\text{cap-two matchings}&538,764\\
\text{linear forests}&458,544\\
\text{cap two with one cycle}&73,116\\
\text{cap two with two cycles}&7,104.
\end{array}                                           \tag{4.1}
\]

Thus

\[
 \Pr(\text{forest}\mid\text{cap two})
        ={458544\over538764}=0.8511036\ldots,          \tag{4.2}
\]

and the conditional expected number of cycles is

\[
 {73116+2(7104)\over538764}=0.1620821\ldots.           \tag{4.3}
\]

This is encouraging finite evidence that topology is cheaper than cap
two.  It does not make the canonical forward/backward cycle shifts
universal.  Trying both signs on every cycle gives

\[
\begin{array}{c|r|r}
\text{old cycles}&\text{some shift lowers cycle count}&
                         \text{both signs locked on every cycle}\\ \hline
1&18,216&54,900\\
2&3,024&4,080.
\end{array}                                           \tag{4.4}
\]

Only (21,240/80,220=26.48\ldots\%\) of cyclic cap-two matchings admit
a canonical whole-cycle shift which lowers the cycle count.  A compound
alternating circuit can still repair some locked examples, as the existing
switch theorem records; (4.4) says that exact cycle shifts are not the
automatic final step of a random proof.

For comparison, ignore all Boolean containment and take a uniformly random
partial permutation with (N=M-K) arcs on (M=(m+1)K) vertices.  Its
expected number of directed cycles is exactly

\[
 \sum_{\ell=1}^{N}{(N)_\ell\over\ell(M)_\ell}
       =\log(m+1)+o(1).                               \tag{4.5}
\]

Indeed there are ((M)_\ell/\ell) directed (\ell)-cycles, and any one
is present with probability ((N)_\ell/(M)_\ell^2).  The reference model
therefore predicts a logarithmic, not zero, cycle residue.  Deleting one
edge per cycle would be harmless for a bounded-defect theorem, but exact
palette-preserving opening remains an integral correlation requirement.

## 5. Consequence for the all-(m) programme

The random-perfect-matching lane has a precise disposition.

1. A uniform matching has the right one-edge marginals, but no justified
   local lopsidependency relation.
2. Even after granting ideal (d^{-3}) triple probabilities, the
   canonical symmetric LLL loses by the constant (24e).
3. Sampling a random colour from a fixed one-factorization supplies only
   one global random variable.  Sampling a random factorization would
   require exactly the still-open simultaneous balancing theorem.
4. If a two-balanced factorization is constructed by another method, one
   should search directly for a forest colour or use compound alternating
   circuits.  Canonical cycle shifts alone are not enough.

Accordingly the best target remains the direct ordered four-transversal,
or an integral simultaneous-colouring theorem.  The LLL can plausibly
re-enter only after an iterative nibble has changed the bad-event scale,
not at the raw perfect-matching level.

## 6. Reproducibility

Run

```text
python3 scratch/audit_catalan_random_matching_lll_m3_20260731.py
```

It writes

```text
scratch/catalan_random_matching_lll_m3_20260731.audit.json
```

and checks every number in (3.4)--(4.4) by literal enumeration.

