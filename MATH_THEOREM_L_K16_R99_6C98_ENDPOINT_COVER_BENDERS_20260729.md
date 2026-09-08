# The `6c98` exact-add conflict is a four-colour endpoint-cover Hall cut

Date: 2026-07-29  
Status: proved, solver-free structural certificate and globally valid projected
Benders row.  This does **not** close either radius-99 branch.

## 1. Exact setting

Let `F_0` be the frozen loopless 858-edge quotient factor in
`scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json`.  For
`h in F_0`, let `x_h` indicate deletion of `h`; for a loopless off-source
seam `a`, let `y_a` indicate insertion.  Write `iota_v(e)` for endpoint
incidence, so it is `0` or `1` here (and would be `2` for a loop).  Exact
degree restoration is

\[
 \sum_{a\notin F_0}\iota_v(a)y_a
 =b_x(v):=\sum_{h\in F_0}\iota_v(h)x_h              \tag{1.1}
\]

at every quotient vertex `v`.

Each seam has exactly one upper-q1 colour.  If an upper colour `c` has the
unique source provider `e(c)`, its exact coverage row is

\[
 (1-x_{e(c)})+\sum_{a\in A(c)}y_a\ge1,
 \qquad\text{hence}\qquad
 \sum_{a\in A(c)}y_a\ge x_{e(c)},                  \tag{1.2}
\]

where `A(c)` is the set of loopless off-source providers of `c`.

The infeasibility theorem and projected rows below concern only this exact
quotient degree/q1 projection; they do not impose connectivity, voltage,
residence, or deeper shadows.  The separate 713-cut strengthening in Section
5 additionally conditions on the 147 frozen source-motif rows, exactly as
stated there.

## 2. General endpoint-cover projection theorem

### Theorem 2.1 (same-palette endpoint-cover Hall row)

Let `T` be any set of upper colours having unique source providers `e(c)`.
Let `P` be any quotient-vertex set meeting every edge of

\[
                     \bigcup_{c\in T}A(c).          \tag{2.1}
\]

Then every integral or fractional cut/add completion satisfying (1.1) and
the upper-q1 rows satisfies

\[
 \boxed{
 \sum_{c\in T}x_{e(c)}
 \le \sum_{v\in P}b_x(v)
 =\sum_{h\in F_0}
       \bigl|\operatorname{ends}(h)\cap P\bigr|x_h .}      \tag{2.2}
\]

Endpoint incidence, including coefficient two when both endpoints lie in
`P`, is essential.  Parallel seam IDs remain separate.

#### Proof

Sum (1.2) over `c in T`.  Provider sets for distinct upper colours are
disjoint because upper colour is a function of the seam.  Every counted
provider meets `P`, so its selected value can be charged to at least one of
its endpoint incidences in `P`.  Thus

\[
 \sum_{c\in T}x_{e(c)}
 \le \sum_{c\in T}\sum_{a\in A(c)}y_a
 \le \sum_{v\in P}\sum_{a\notin F_0}\iota_v(a)y_a.
\]

Apply (1.1) and expand `b_x(v)`.  No integrality was used.  This proves
(2.2).  ∎

The same proof works for lower colours.  It is not tied to radius 99 or to
one of the retain/delete branches.

### Corollary 2.2 (explicit-catalogue polynomial fractional separator)

For a candidate fractional cut `x in [0,1]^{F_0}`, put

\[
 p_c=x_{e(c)},\qquad
 d_v=\sum_{h\in F_0}\iota_v(h)x_h.
\]

Over all source-unique colours of one palette, solve the linear program

\[
 \max\left\{\sum_c p_ct_c-\sum_vd_vw_v:\quad
 0\le t_c\le1,\ 0\le w_v\le1,\
 t_c\le w_u+w_v\ \text{for every }a=uv\in A(c)\right\}.       \tag{2.3}
\]

This is a prize-collecting simultaneous fractional vertex-cover LP (an
ordinary fractional vertex cover after fixing `t_c=1` on a chosen `T`).  Its
size is polynomial in the explicitly listed colour/provider catalogue; no
polynomial-in-`k` claim is made for an implicit exponentially large
catalogue.

If its value is positive, the fixed optimal weights give the violated valid
row

\[
             \sum_vw_vb_x(v)\ge\sum_ct_cx_{e(c)}.             \tag{2.4}
\]

Indeed, multiply (1.2) by `t_c`, sum, and charge a provider `uv` by
`w_u+w_v`.  The weights may be chosen at the candidate, but once frozen they
define the globally valid linear row (2.4).  Bounds `w_v<=1` lose nothing:
replace `w_v` by `min(w_v,1)`; any clipped provider pair still has weight at
least `1>=t_c`, and the nonnegative cost cannot increase.  Every integral
endpoint-cover row occurs by taking `t=1_T,w=1_P`, so a nonpositive LP optimum
certifies all such rows; a positive fractional optimum emits a valid weighted
row, not necessarily an integral cover.  This family strictly extends the
earlier canonical portal-union maximum-closure separator.

In fact, this LP is exact for the fractional one-palette endpoint-capacity
packing relaxation

\[
 \sum_{a\in A(c)}y_a\ge x_{e(c)},\qquad
 \sum_a\iota_v(a)y_a\le d_v,
 \qquad y\ge0.                                                \tag{2.5}
\]

Necessity is the charging proof above.  If (2.5) is infeasible, Farkas gives
nonnegative `t,w` with `t_c<=w_u+w_v` on every provider and positive value in
(2.3); scale so `max_c t_c=1` and clip `w_v` at one.  Thus (2.3) has positive
optimum if and only if (2.5) is infeasible.  This exactness concerns the
capacity relaxation only: it does not require every freed endpoint degree to
be filled and does not imply an integral provider choice.  The simultaneous
lower/upper extension and the exact equality dual are proved in
`MATH_THEOREM_L_GLOBAL_ENDPOINT_CAPACITY_HALL_FARKAS_20260729.md`.

Strictness already occurs on the loopless source six-cycle
`0-1-4-2-3-5-0`: cut source edges `01,23` and give two colours sole
replacement providers `12,13`.  Their canonical outside-base portal union is
`{1,2}` and has capacity two, equal to demand.  The endpoint cover `{1}` hits
both providers and has capacity one, so (2.3) has positive value one.

This remains only a one-palette degree/q1 projection.  It does not
characterize cross-palette coupling, the full seam-recourse polytope,
connectivity, residence, or deeper shadows.

## 3. The four-colour structural conflict

The frozen exact-add CNF for delete cut `6c98` has 198 distinct exposed
endpoints, each of cut degree one.  The externally shrunk q1 core contains
the four upper colours

\[
 T=\{(1,1883),(1,1907),(1,3255),(1,5939)\},          \tag{3.1}
\]

whose unique source providers are, respectively,

\[
                    4742,\ 22511,\ 23229,\ 24034.    \tag{3.2}
\]

All four source providers are deleted by `6c98`.  Restricting the complete
off-source seam bank to the 198 exposed endpoints gives exactly

\[
\begin{array}{c|l}
 (1,1883)&4737,4740,18552,18555,21385\\
 (1,1907)&18171,18172\\
 (1,3255)&21408,21411\\
 (1,5939)&22529,22530.
\end{array}                                                    \tag{3.3}
\]

This already gives a direct contradiction.  A provider of colour 3255 uses
vertex 576, and a provider of colour 5939 uses 611.  The 1907 provider
cannot then use 611, so it uses 617.  Every 1883 provider uses 576 or 617.
Since every exposed endpoint has capacity one, the fourth colour cannot be
served.

The four-row local contradiction is inclusion-minimal in those rows.  After
omitting the named row, the following three demanded colours have disjoint
provider edges:

\[
\begin{array}{c|l}
 \text{omit }1883&18172,21408,22529\\
 \text{omit }1907&4740,21408,22529\\
 \text{omit }3255&4737,18172,22529\\
 \text{omit }5939&4740,18171,21408.
\end{array}                                                    \tag{3.4}
\]

This certifies minimality of the local four-colour matching obstruction; it
does not by itself assert a full 198-endpoint completion for each
core-minus-one case.

## 4. Globalizing the conflict

For the four colours in (3.1), the complete provider graphs are `K_9` on the
following quotient-node sets:

\[
\begin{aligned}
V_{1883}&=\{92,485,499,541,576,606,615,617,619\},\\
V_{1907}&=\{97,490,502,546,581,611,617,620,623\},\\
V_{3255}&=\{208,521,576,600,638,751,754,757,758\},\\
V_{5939}&=\{403,611,663,667,739,759,761,832,852\}.
\end{aligned}                                                  \tag{4.1}
\]

Deleting the unique source provider removes, respectively, the edges

\[
 92\!-!499,\quad611\!-!617,\quad638\!-!754,
 \quad663\!-!739.                                             \tag{4.2}
\]

Thus there are exactly `4*35=140` off-source providers.  The only pairwise
block overlaps are

\[
 V_{1883}\cap V_{1907}=\{617\},\quad
 V_{1883}\cap V_{3255}=\{576\},\quad
 V_{1907}\cap V_{5939}=\{611\}.                               \tag{4.3}
\]

Define

\[
\begin{aligned}
P=\{&97,208,403,485,502,521,541,546,576,581,600,606,611,615,617,\\
    &619,620,623,667,751,757,758,759,761,832,852\}.
\end{aligned}                                                   \tag{4.4}
\]

Equivalently, its four blockwise pieces are

\[
\begin{aligned}
V_{1883}\setminus\{92,499\},\quad
V_{1907}\setminus\{490\},\quad
V_{3255}\setminus\{638,754\},\quad
V_{5939}\setminus\{663,739\}.
\end{aligned}                                                   \tag{4.5}
\]

Hence `P` meets all 140 alternatives.

The cover has minimum cardinality 26.  Its complement in the 33-node union
is the independent set

\[
               \{92,499,490,638,754,663,739\}.                 \tag{4.6}
\]

Conversely, each block is `K_9-e`, so an independent set meets it in at most
two vertices.  If an independent set avoids the three shared vertices, its
1907-block contribution is at most one and the other three contributions
are at most two, giving at most seven.  If it uses 576, that vertex is
universal in both incident blocks; if it uses exactly one of 611 and 617,
that vertex is universal in the other incident block and has no permitted
1907 mate; if it uses both 611 and 617, no further 1907, 1883, or 5939
vertex is possible.  These cases give at most seven.  Thus `alpha=7` and
`tau=33-7=26`.

Apply Theorem 2.1.  Every exact or fractional completion of the frozen source
obeys

\[
\boxed{
 \sum_{h\in F_0}|\operatorname{ends}(h)\cap P|x_h
 \ge x_{4742}+x_{22511}+x_{23229}+x_{24034}.}                  \tag{4.7}
\]

At `6c98`, only cut edge 18158 contributes one unit on the left and cut edge
22511 contributes two.  Therefore (4.7) reads

\[
                         3\ge4,                                \tag{4.8}
\]

which is false.  This is a solver-free proof that the frozen exact-add
degree-plus-both-q1 model is infeasible.  CaDiCaL's 0.011-second UNSAT is now
only corroborating discovery evidence, not the proof.

## 5. Exact projected master row and strict generalization

The capacity side of (4.7) has 49 nonzero source-edge coefficients: 46 are
one and three are two; the other 809 source edges have coefficient zero.
After moving the four demand terms left, the normalized row has 52 nonzero
coefficients, with histogram

\[
                         1^{47},\quad2^2,\quad(-1)^3.           \tag{5.1}
\]

Its value at `6c98` is `-1`.  The complete coefficient list is reconstructed
from the catalogue, not copied, by the permanent audit below.

The row provably excludes more than the one discovery cut.  Edge 18085 is a
cut edge of row coefficient zero and is not the unique `6c98` hitter of any
of the 147 source-residence motifs.  There are exactly 712 uncut source edges
of row coefficient zero.  Replacing 18085 by any one of them leaves a
99-edge delete-branch cut, still hits all 147 motifs, and retains row value
`-1`.  Consequently (4.7) excludes at least

\[
                            1+712=713                           \tag{5.2}
\]

distinct motif-hitting radius-99 cuts.  This count makes no claim that those
712 alternatives satisfy every other master row.

The row is valid in both retain and delete branches.  The proof-carrying
CEGAR driver installs it as an eager Hall row in both branches; it is not
mislabelled as a joint-hypergraph cover row.

## 6. Replay and evidentiary boundary

Canonical production-row replay:

```text
scratch/audit_k16_r99_6c98_fourcolour_endpoint_cover_cut_20260729.py
scratch/k16_r99_6c98_fourcolour_endpoint_cover_cut_20260729.audit.json
```

Its source/artifact hashes are

```text
audit source  583e4db542ae4f0d4731e052eb6699e22b3419e424b47027796032134ae897e4
audit JSON    aacf3b7960201815404596a4fc124e99173d38b757b347ede0b240142ecbbd3d
row object    39ba4675a95d4c4309a5615ed73b6762bbf5cabe21dc900607ad3272d4ff76ec
payload       0739a85af177bb932505147c77d4664e5a7e5b3cb09d96b027529af532ba5ad2
```

The richer independent structural replay, including minimum-cover structure,
the local forcing witnesses, and the 713-cut family, is

```text
scratch/audit_k16_r99_fixed_delete_6c98_upper4_hall_benders_20260729.py
scratch/k16_r99_fixed_delete_6c98_upper4_hall_benders_20260729.audit.json
```

The replay verifies the four complete `K_9` provider graphs, all 140
off-source provider edge IDs, the 26-node cover, coefficient multiplicities,
the local forced pattern, the four local core-minus-one matchings, the
`3<4` evaluation, and all 713 one-swap excluded cuts.  Current hashes are

```text
audit source  f7689dae2a5acedb976492be4ef5be856de0316f57d9ca21a7e37b0abaf1d963
audit JSON    454ee0376e39c8bf3688c6e707220a6a2de4f2b36532078b25e39f4168cf3990
payload       035e9b9ef2ffc6549f2259e4b95688fc7cd11c9163600d6942c29d32821357f4
signed list   35770364d98f106d480240f5e49f55f52d668264793fbfea3e7d5e26fbbf973e
```

The corrected solver-free production-size ledger is

```text
scratch/audit_threadD_k16_r99_benders_static_size_20260729.py
  SHA 3ce97dd168686eba933163f48da99740cd41793800dbefffc4799e403d39bc52
scratch/threadD_k16_r99_benders_static_size_20260729.audit.json
  SHA f7b652c35a70f643a54f6f809006ab35ea268b49dd43fcd74084ca081e4d0af1
  payload 9b8a3b9b3ced67d7af094993703a220a62387ead462fcb6f6fd2b658ffea4f73
```

It records one four-colour endpoint row and no redundant joint-cover rows:
the retain/delete masters have `21,645` variables and `3,691/3,692` linear
constraints.  The full recourse models retain `27,428` variables and
`2,387` branch-free constraints.

Current integration hashes are

```text
production driver  5f700eeca6b36385378c5a6595ab7838b67606e1cdf2215dcc46c0c1b02c4e84
result auditor     0cb576e930ff1a9603ce1b8e1af3a23807e8ec01ab202a7ce641297b766772bc
16-test suite      340a5cf2992859619d29eaa206657ff8d41a7d3369c30ce46356e08dd97a44d2
```

The auditor self-test and all sixteen lightweight regressions pass.  The
historical low-memory launch bundle is pre-pivot and is explicitly barred in
`scratch/K16_R99_RECOVERY_COMMANDS_20260729.md` until its manifest is rebuilt.

Frozen discovery inputs include

```text
source        d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8
cut artifact  b66a9f72fd6b7a03a57f3adc0a804fd9b75f95d9d36db6b3c733c78350ebdc01
cut list      6c98aa96b824b580be70fb9bab617e80fef233b4bf11b33a7a83adce5d9c39b4
CNF           fbcbace828f3aad11e61291e4244a51a23adedee384182a8ec5ea26eefc67dfc
```

The four-row core JSON records external SAT/UNSAT outcomes but no formal
proof or core-minus-one assignments.  No conclusion here relies on those
outcomes.  The proved conclusion is exactly: `6c98` has no loopless exact
degree-plus-both-q1 completion, and every feasible cut/add projection must
satisfy (4.7).  Radius 99, the delete branch, and `B(16)=12873` all remain
open.
