# Endpoint-Markov AGCF recursion, paired-port Hall, and an explicit nontransitive parameter-five filler

Date: 2026-07-31  
Status: exact all-parameter recursion equivalence; exact
partition--graphic--transversal criterion; explicit independently replayed
`n=4 -> n=5` construction.  No all-parameter transition-supply theorem is
claimed.

## 0. Results

Three points settle the immediate endpoint-bank question.

1. **The central transition is endpoint-Markov.**  After the parent is known
   to be an AGCF, its internal path chronology does not determine the
   residual resource face.  The face depends only on one chosen endpoint
   from each complementary endpoint pair.  Equivalently, orientation rows
   plus residual path rows form one exact-cover instance depending only on
   the endpoint bank.
2. **The remaining component-routing condition is ordinary Hall.**  Once
   three exact directed sector forests and their port banks are fixed, the
   opaque “one complementary reset per augmented cycle” row is equivalent
   to a perfect matching in one paired two-containment graph.
3. **The new cyclic `n=4` child extends.**  There is an explicit
   nontransitive `C_7`-equivariant AGCF at `n=5`, consisting of the two
   inherited child orbits and four residual path orbits.  It covers all
   `252` middle vertices, all `210` lower turns, and all `210` upper turns
   once.

The new `n=5` construction also proves that the Catalan type histogram
`C_a C_b C_c` is not forced by exact recursion.  Only its zeroth and three
first-moment ledgers are forced.

For the asymptotic construction, the arbitrary-`Q` theorem supplies the
`P-o(P)` forest bodies after a path-dependent state is chosen.  The planted
`C6` bank supplies enough raw gain-one packets, but it composes only under
three separate exact cut systems: protected common-basis rank, private-ear
Rado rank, and the paired-port Hall cuts proved here.  Raw packet cardinality
alone implies none of them.

## 1. The weakest central recursive state

Let `G` be an AGCF on a `2n`-set `Omega`.  Write its complementary endpoint
bank as

\[
 \mathcal B(G)=
 \bigl\{\{s_P,\overline{s_P}\}:P\in\operatorname{comp}(G)\bigr\}.
                                                               \tag{1.1}
\]

The bank has `C_n` pairs.  The weakest central transition state is

\[
                         (\mathcal B,E),                         \tag{1.2}
\]

where `E` chooses one member of each pair.  The actual parent paths remain
the payload used to materialize the inherited child paths; they are not
needed to define the residual resource face.

This distinction is only central.  A protected physical/common-cap
transition may still need the whole oriented parent because its tail/head
injections, occurrence graphs, residence state, and compiler guards depend
on physical chronology.

## 2. Endpoint-Markov exact-cover theorem

Adjoin coordinates `c,z`.  For each parent component `P`, introduce one
private token `tau_P`.  Before choosing `E`, use the following full typed
resource banks, with fixed tags shown explicitly:

\[
\begin{array}{lll}
V_0=\binom\Omega{n+1},&
V_1=z+\binom\Omega n,&
V_2=c+z+\binom\Omega{n-1},\\
L_0=\binom\Omega n,&
L_1=z+\binom\Omega{n-1},&
L_2=c+z+\binom\Omega{n-2},\\
U_0=\binom\Omega{n+2},&
U_1=z+\binom\Omega{n+1},&
U_2=c+z+\binom\Omega n.
\end{array}                                                   \tag{2.1}
\]

For `e` in the endpoint pair of `P`, add the four-resource orientation row

\[
 q(P,e)=\{\tau_P,\ z+e\in V_1,\ e\in L_0,\ c+z+e\in U_2\}.
                                                               \tag{2.2}
\]

Also add one row for every complement geodesic whose tag trace is

\[
                  00\cdots00,\quad 01\cdots01,\quad 11\cdots11, \tag{2.3}
\]

recording its `n+2` middle, `n+1` lower, and `n+1` upper resources.

### Theorem 2.1 (endpoint-Markov recursion)

An exact cover of all resources (2.1) and all child tokens by rows
(2.2)--(2.3) is equivalent to an AGCF at parameter `n+1` in the exact
three-sector recursive face.  Feasibility and the set of attainable next
endpoint banks depend on the parent only through `B(G)`.

#### Proof

The token columns choose exactly one endpoint `e_P` from every parent pair.
Orient the old component from \(\overline{e_P}\) to \(e_P\) and extend it to

\[
 c+\overline{e_P},\ldots,c+e_P,z+e_P.                       \tag{2.4}
\]

Because the parent is an AGCF, its internal edges consume the complete
`c`-copies of the old middle, lower, and upper levels, independently of its
internal pairing/order.  The last edge of (2.4) additionally consumes
exactly the three non-token resources in (2.2).  Hence the uncovered face is
determined only by the chosen endpoints.

Exact coverage by (2.3) gives every remaining middle vertex and both turn
palettes once.  Every row is already a monotone-tag complement geodesic, so
the union is an AGCF.  Conversely, deleting the inherited child paths from
any recursive-face child exposes precisely the residual rows (2.3), while
each deleted final tag edge gives the corresponding row (2.2).  This proves
both directions. \(\square\)

If the residual paths start at `A_1,...,A_K` in rank `n+1`, the output bank
is explicitly

\[
\boxed{
 \mathcal B'=
 \{\{c+\bar e,z+e\}:e\in E\}
 \mathbin{\dot\cup}
 \{\{A_i,c+z+(\Omega\setminus A_i)\}:1\le i\le K\}.
}                                                              \tag{2.5}
\]

Thus (2.2)--(2.3) defines a finite directed relation on endpoint banks.  A
hub, Dyck representative, or transitive group is not part of its definition.

Put

\[
 M=\binom{2n}{n},\quad N=\binom{2n}{n-1},\quad
 P=\binom{2n}{n-2},\quad K=N-P=C_{n+1}-C_n.                  \tag{2.6}
\]

The mixed exact cover has

\[
 3M+4N+2P+C_n=4C_n+(3n+4)K                              \tag{2.7}
\]

columns counted with types.  It chooses `C_n` orientation rows and `K`
residual rows.

## 3. Exact port-decorated forest state

The path rows can be cut at their two tag seams.  The resulting sector
forests have `N` vertices, `P` edges, and `K=N-P` components apiece.  Strip
the fixed tags and orient their components as

\[
 T_i:A_i^0\longrightarrow A_i^1,\qquad
 M_j:X_j^0\longrightarrow X_j^1,\qquad
 B_k:L_k^0\longrightarrow L_k^1.                         \tag{3.1}
\]

Here `T,M,B` lie respectively in old ranks `n+1,n,n-1`.  Write `I(F)` and
`U(F)` for the sets of internal intersection and union colours of a forest.

The exact port-decoration equations are

\[
\begin{aligned}
 I(T)\mathbin{\dot\cup}\{X_j^0\}&=\binom\Omega n\setminus E,
 &U(T)&=\binom\Omega{n+2},\\
 I(M)\mathbin{\dot\cup}\{L_k^0\}&=\binom\Omega{n-1},
 &U(M)\mathbin{\dot\cup}\{A_i^1\}&=\binom\Omega{n+1},\\
 I(B)&=\binom\Omega{n-2},
 &U(B)\mathbin{\dot\cup}\{X_j^1\}&=\binom\Omega n\setminus E.
\end{aligned}                                                \tag{3.2}
\]

Thus the component orientations are not cosmetic.  Their four seam-port
banks are exactly the four palette leaves of the internal forests.

Choose a bijection `kappa` between top and bottom components such that

\[
                         L_{\kappa(i)}^1=\Omega\setminus A_i^0. \tag{3.3}
\]

This is the outer complementary tube matching.  Once it is fixed, define the
paired-port router `H_kappa` between outer tubes `i` and middle components
`j` by

\[
 i\sim j
 \quad\Longleftrightarrow\quad
 X_j^0\subset A_i^1
 \quad\hbox{and}\quad
 L_{\kappa(i)}^0\subset X_j^1.                              \tag{3.4}
\]

### Theorem 3.1 (paired-port Hall equivalence)

The port-decorated forests (3.1)--(3.3) assemble into the required residual
factor if and only if `H_kappa` has a perfect matching, equivalently

\[
                 |N_{H_\kappa}(S)|\ge |S|
                 \qquad(S\subseteq[K]).                       \tag{3.5}
\]

The exact routing deficiency is

\[
 \delta_{\rm route}=K-\nu(H_\kappa)
 =\max_{S\subseteq[K]}\bigl(|S|-|N_{H_\kappa}(S)|\bigr).     \tag{3.6}
\]

#### Proof

Necessity follows by cutting every residual path at the two seams.  Its
middle component supplies one edge of `H_kappa`, and disjoint paths use all
middle components once.

Conversely, let `pi` be a perfect matching of `H_kappa`.  Concatenate

\[
 T_i,\quad
 A_i^1-(z+X_{\pi(i)}^0),\quad
 z+M_{\pi(i)},\quad
 (z+X_{\pi(i)}^1)-(c+z+L_{\kappa(i)}^0),\quad
 c+z+B_{\kappa(i)}.                                      \tag{3.7}
\]

The two containments in (3.4) make the seams Johnson edges.  Equations
(3.2) make both turn palettes exact, and (3.3) makes the outer endpoints
complementary.  The concatenated paths partition all sector vertices.

Their total number of physical edges is

\[
                        3P+2K=3N-K=(n+1)K.              \tag{3.8}
\]

Every path joins complementary `(n+1)`-sets and therefore has at least
`n+1` Johnson edges.  Equality in (3.8) forces every one of the `K` paths to
have exactly `n+1` edges, hence to be a geodesic.  Hall's theorem and the
deficiency formula give (3.5)--(3.6). \(\square\)

This is the promised sharp Hall/matroid condition.  The endpoint choice is
a base of a partition matroid, the three internal edge sets are graphic
independent sets satisfying the palette partitions, and the final router is
one transversal matroid of full rank.  Separate one-sided seam matchings do
not imply (3.5).

## 4. Exact specialization at `n=4 -> n=5`

For the new cyclic parameter-four parent,

\[
 C_4=14,\qquad N=56,\qquad P=28,\qquad K=28.                 \tag{4.1}
\]

Thus a completely nonsymmetric transition certificate consists of one
endpoint from each of 14 parent pairs, three directed 28-edge forests on 56
vertices, the six partitions (3.2), an outer complement pairing, and one
`28 x 28` router passing (3.5).

The direct mixed exact-cover form has

\[
 504\text{ typed resources},\qquad 28\text{ orientation rows},\qquad
 403{,}200=\binom85\frac{(5!)^2}{2}\text{ residual rows}.     \tag{4.2}
\]

Every solution selects 14 orientation rows and 28 residual rows.  No type
quota beyond exact resource coverage belongs to the weakest problem.

The previously running local/remote sources do not test the new cyclic
bank: their two endpoint arrays are older fixtures, only three of whose 14
pairs occur in the cyclic bank.  Their unrestricted, quota, and DLX runs all
ended `UNKNOWN` by timeout.  Moreover their optional quota mode is strictly
stronger than AGCF recursion and is refuted by the construction below.

## 5. The `C7` quotient reduction

Retain only the inherited residual rotation

\[
                         \tau=(0\ 1\ 2\ 3\ 4\ 5\ 6),           \tag{5.1}
\]

fixing the old hub `7` and the new tags `8,9`.  The parent has two path
orbits.  Orient both so the terminal endpoints contain the old hub.

After deleting the inherited child resources, the residual quotient has

\[
\begin{array}{c|c}
\text{resource type}&\text{number of }C_7\text{ orbits}\\ \hline
\text{middle}&8+8+8=24,\\
\text{lower}&8+8+4=20,\\
\text{upper}&4+8+8=20.
\end{array}                                                \tag{5.2}
\]

Hence it has 64 resource orbits.  One residual path contains 16 resources.
Its seven translates are pairwise resource-disjoint exactly when those 16
resources lie in distinct quotient orbits.  Consequently:

### Corollary 5.1 (four-row quotient criterion)

A `C7`-equivariant child exists in this orientation face if and only if four
orbit-simple residual path rows partition the 64 quotient resources.

If their tag-block types are `(a_i,b_i,c_i)`, exact coverage forces

\[
              \sum_{i=1}^4a_i=\sum_{i=1}^4b_i
              =\sum_{i=1}^4c_i=4.                         \tag{5.3}
\]

The output then has six path orbits, hence 42 paths.  It is nontransitive:
it retains `C7`, rather than seeking the impossible transitive `C9` bank.

## 6. Explicit nontransitive `n=5` AGCF

Take all seven translates under (5.1) of the following six base paths:

\[
\begin{aligned}
&(369,345,472,410,398,654),\\
&(341,279,295,422,426,682),\\
&(31,61,188,684,936,992),\\
&(55,179,211,721,713,968),\\
&(151,535,566,818,866,872),\\
&(171,555,617,632,880,852).
\end{aligned}                                               \tag{6.1}
\]

The first two are the reversed cyclic parent orbits, lifted through the
`c`-rail and extended by the final `c -> z` swap.  The remaining four are
residual path orbits.  Their quotient supports have order 16, are pairwise
disjoint, and partition the 64 resources in (5.2).

### Theorem 6.1

The 42 paths generated by (6.1) form an AGCF at parameter five.

#### Proof

Independent literal replay gives

\[
\begin{array}{c|c|c}
\text{rank/resource}&\text{occurrences}&\text{distinct/full}\\ \hline
5\text{ middle}&252&252/252,\\
4\text{ lower}&210&210/210,\\
6\text{ upper}&210&210/210.
\end{array}                                                \tag{6.2}
\]

Every path has six rank-five vertices, five Johnson edges, complementary
endpoints, and one flip of every coordinate.  Therefore each is a complement
geodesic, and (6.2) is exactly the AGCF definition. \(\square\)

The residual types are

\[
 (2,0,1),\quad(2,1,0),\quad(0,1,2),\quad(0,2,1),             \tag{6.3}
\]

each with physical multiplicity seven.  Thus

\[
 \sum x_{abc}=28,qquad
 \sum ax_{abc}=\sum bx_{abc}=\sum cx_{abc}=28,               \tag{6.4}
\]

but every canonical `C_aC_bC_c` quota at sum three is violated.  Equation
(6.4), not the Catalan histogram, is the forced type ledger.

Both the endpoint-pair bank and the unoriented path family have exact
stabilizer `C7`, with element-order histogram `1^1,7^6`.  An
orientation-free pair invariant first separates the coordinate classes as

\[
                       7+2+1,                                \tag{6.5}
\]

and the remaining `2(7!)` permutations leave only the seven rotations.  In
the exported orientation, first-endpoint coordinate degrees are

\[
                       26^7,14,14,0,                          \tag{6.6}
\]

so the state is visibly nontransitive.

For the displayed sector orientation, the outer complement graph and the
paired-port router in Theorem 3.1 are both the identity matching on 28
vertices.  This is a leaf-peelable exact base, but it has no router reserve:
every one of its 28 Hall edges is essential.

## 7. Symmetry must break again

The inherited `C7` is not a viable all-parameter state.  At parameter six it
moves seven coordinates and fixes five.  It fixes no rank-six set: an
invariant set would contain either zero or seven moving coordinates, while
the five fixed coordinates cannot supply a six-set.  Hence it fixes no
middle vertex.

A parameter-six complement geodesic has seven vertices.  If a path were
setwise fixed by `C7`, the induced order-seven action would be an
automorphism of a path graph, whose automorphism group has order at most two.
Thus every path orbit is free.  But

\[
                         C_6=132\not\equiv0\pmod7.              \tag{7.1}
\]

Therefore no `C7`-invariant parameter-six AGCF exists.  The next transition
must break even the inherited subgroup.  This is why the recursive state is
endpoint-Markov, not group-Markov.

## 8. Integration with arbitrary `Q` and planted `C6`

The exact quantifier order is

\[
 \mathcal B\longrightarrow E,\mathcal A
 \longrightarrow Q\longrightarrow\text{bulk forests}
 \longrightarrow\text{packet completion}\longrightarrow H_\kappa.
                                                               \tag{8.1}
\]

Here `A` is a selected planted packet bank.  Let `R(A)` be its puncture-risk
set in the common ground `Xi` of the two strict common-basis matroids of rank
`q`, and put `Xi_A=Xi\setminus R(A)`.  A basis protecting the bank exists
if and only if Edmonds' cuts hold:

\[
 r_1(S)+r_2(\Xi_{\mathcal A}\setminus S)\ge q
 \qquad(S\subseteq\Xi_{\mathcal A}).                         \tag{8.2}
\]

Once such a `Q` is fixed, the arbitrary-`Q` theorem supplies `P-o(P)`
physical linear-forest bodies uniformly.  It does not align their leaves,
ports, or final router.

Suppose the remaining typed leave is a matching of planted target atoms and
each target `d` has a menu `Sigma_d` of resource-private activations.  Assume
each option suppresses, after contracting the bulk forest, to one quotient
ear and has one fixed declared port effect.  Let `M_ear` be the direct sum of
the relevant contracted graphic matroids.  Rado's theorem gives the exact
private-ear condition

\[
 r_{M_{\rm ear}}\!\left(\bigcup_{d\in J}\Sigma_d\right)
       \ge |J|\qquad(J\subseteq D).                           \tag{8.3}
\]

After (8.3) fills the exact palette/port leaves, Theorem 3.1 says that the
only remaining central topology row is (3.5).

Thus, on the protected slot-separable single-ear face, the complete finite
cut package is

\[
                 \boxed{\text{common-basis (8.2)}
                 +\text{Rado (8.3)}+\text{router Hall (3.5)}.} \tag{8.4}
\]

The raw suspended-hex theorem supplies more than `P/54` pairwise-private
packets, the correct scalar scale for an `o(P)` leave.  It does not prove
(8.4).  A fixed disjoint packet bank is only a partial bijection between
lower and upper targets, and sparse count-neutral cycles preserve both outer
leave sets pointwise.  Hence target alignment must be present before those
rerouters act.  Outside the slot-separable one-ear face, the exact target row
is a four-uniform matching condition and (8.3) alone is unsound.

Occurrence-reserve, residence, deep-shadow, and downstream compiler guards
remain separate exported conditions.  The present theorem advances the
central AGCF recursion and replaces its opaque topology row by Hall; it does
not by itself prove `nu=B`.

## 9. Exact remaining all-parameter lemma

Starting from the authenticated bases through parameter five, choose along
one endpoint-Markov chain:

1. an endpoint orientation and planted packet subbank;
2. a protected common basis satisfying (8.2);
3. arbitrary-`Q` bulk forests whose full typed leave is target-aligned;
4. private packet choices satisfying (8.3); and
5. completed port-decorated sector forests satisfying (3.5), together with
   the separately declared occurrence/compiler guards.

This statement is existential along one chain.  It does not require every
parent, every common basis, a fixed Dyck bank, or a transitive bank.  The
direct Joos--Mubayi--Smith black box cannot supply it, and the endpoint
classifications show why symmetry is not an admissible replacement.

## 10. Reproducibility and source scope

The new compact construction and independent replay are

```text
scratch/k_catalan_agcf_n5_c7_child_extension_20260731.witness.txt
scratch/audit_k_catalan_agcf_n5_c7_child_extension_20260731.py
scratch/k_catalan_agcf_n5_c7_child_extension_20260731.audit.json
```

Their SHA-256 hashes are

```text
witness  fe94bf1a61c4ff9dc1445764fef0bac2ea20d6f68acbac269c914f326b71cb55
replay   50d78086b2707f6b7b637cb88b50ea8c6872c7ca8aa8a98e4d9655be130e4060
audit    6f039959520ea9d585c272114019819e6804e9ea06b12f35193bac1fd514e602
payload  a739c443afaa6d81bcc508aa12f5bb2870e911fa5990037e60e7e7fc048d212e
```

A second clean-room reconstruction from the six displayed base paths
independently checked the middle and turn partitions, all three sector
forests, both identity routers, and the exact `C7` stabilizer.  Thus the
literal paths, rather than the quotient search that found them, are the
load-bearing certificate.

The parent is the frozen cyclic `n=4` witness of SHA
`7b371076ecee408f292a0ee90543fb0fd93c163605d5a7df8c00535d117e8070`.

The older exact-cover sources

```text
scratch/search_catalan_antipodal_three_sector_n4_to_n5_dlx_20260731.cpp
scratch/solve_catalan_antipodal_three_sector_n4_to_n5_cpsat_20260731.py
```

have SHAs

```text
7f1ede69d21726678c418109890acd370d29664f0799ddf09124c1561c65be98
638458cecdc214b28a869296aaa598d7783cba359e57ead49220860fe03f3724
```

and use older endpoint arrays, not the new cyclic bank.  Their remote
timeout verdict is `UNKNOWN`, not `UNSAT`.  The separate direct-edgewise
chain is authenticated through `n=6`; its `n=7` Kissat process was still
active when polled.  Neither fact is used in Theorems 2.1, 3.1, or 6.1.
