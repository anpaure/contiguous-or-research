# Independent audit of the parameter-three AGCF endpoint bank, and the exact scope of its cyclic continuation

Date: 2026-07-31  
Status: complete independent audit at `n=3`; new literal positive `n=4`
cyclic fixture; rigorous obstruction to a symmetry-preserving all-`n`
recursion.  No arbitrary-`n` AGCF existence theorem is claimed.

## 1. Verdict

The proposed parameter-three census is correct.

* There are exactly `360` unoriented complement geodesics on `[6]`.
* Exact cover of the `20` middle vertices, `15` lower turns, and `15`
  upper turns gives exactly `1,584` antipodal-geodesic Catalan fillers
  (AGCFs).
* Their endpoint pairs form exactly `72` banks, and every bank supports
  exactly `22` AGCFs.
* Every viable bank is uniquely a distinguished coordinate plus a labelled
  five-cycle.  The banks form one `S_6` orbit and have endpoint-bank
  stabilizer `D_10`.
* The canonical Dyck endpoint bank supports no AGCF.

There is a genuine next cyclic fixture at `n=4`: distinguish a hub and take
two translation orbits of regular-tournament triples on the other seven
coordinates.  A literal `14`-path AGCF exists.  Its endpoint bank has
stabilizer `D_14`, while its ordered/unoriented path factor has stabilizer
`C_7`.

This is not an all-parameter recursion.  A transitive pointed endpoint bank
at parameter `n` requires

\[
                        2n-1\mid \operatorname{Cat}_n.       \tag{1.1}
\]

At `n=5`, `9` does not divide `Cat_5=42`.  Thus the literal cyclic/dihedral
bank state must break symmetry by that stage.  The surviving general state
is a path-dependent pointed block bank with internal port/pairing/order data,
not a single odd-cycle invariant.

## 2. Independent exact-cover audit at `n=3`

Fix one canonical endpoint from each complementary pair of rank-three sets.
There are ten pairs.  A geodesic from one endpoint to its complement is
specified by independent removal and insertion orders, hence

\[
                      10(3!)^2=360.                         \tag{2.1}
\]

Every row consists of four rank-three vertices, three consecutive
intersections, and three consecutive unions.  Thus it occupies ten of the

\[
                 \binom63+\binom62+\binom64=50             \tag{2.2}
\]

resources.  A five-row exact cover is therefore literally an AGCF: it
partitions the middle level and uses every lower and upper turn exactly
once.  There is no quotient relaxation in this model.

An independent bitset implementation visits `6,481` Algorithm-X nodes and
returns

\[
       1,584\text{ covers},\qquad72\text{ banks},\qquad
       \{\text{bank load}}=\{22^{72}\}.                   \tag{2.3}
\]

This reproduces, rather than imports, the frozen classification.

## 3. Intrinsic five-cycle classification

Let `B` be an endpoint bank.  For a coordinate `h`, orient every complement
pair toward its member containing `h` and delete `h`.  This gives five
2-subsets of the other five coordinates.  Exhaustively, exactly one `h`
makes them distinct, connected, and degree two.  They are therefore the
edges of a labelled `C_5`.

Conversely, for a distinguished `h` and a labelled unoriented five-cycle
`C` on the other coordinates, define

\[
 B(h,C)=
 \left\{
   \left\{\{h\}\cup e,\ [6]\setminus(\{h\}\cup e)\right\}:
   e\in E(C)
 \right\}.                                                \tag{3.1}
\]

The independently generated `6(5-1)!/2=72` banks (3.1) agree exactly with
the 72 banks from (2.3).  Uniqueness of `h` makes the stabilizer fix `h`; on
the other five points it is precisely `Aut(C_5)`.  Directly,

\[
 |\operatorname{Stab}_{S_6}B|=10,\qquad
 \operatorname{ord}\text{-histogram}=1^1,2^5,5^4,         \tag{3.2}
\]

so the endpoint-bank stabilizer is `D_10`.

The word **endpoint-bank** matters.  A decoration/path factor on a bank need
not preserve all reflections of that bank; the group statement (3.2) is not
a claim that every one of the 22 supported AGCFs has `D_10` symmetry.

## 4. Canonical Dyck no-go

The five canonical Dyck roots are

\[
                         7,11,13,19,21.                    \tag{4.1}
\]

Their deleted representative degree sequences, sorted, are

\[
\begin{array}{c|c}
h=0,5 & 0,2,2,3,3,\\
h=1,2,3,4 & 1,2,2,2,3.
\end{array}                                                \tag{4.2}
\]

Hence this bank is not of the form (3.1), and the classification itself is
a solver-free obstruction.  Independently, restricting the exact-cover
catalogue to its `5(3!)^2=180` paths closes UNSAT in `51` nodes.  Therefore
no AGCF has the canonical Dyck endpoint transversal.

The scope is exactly the endpoint premise.  It refutes a recursion that
freezes this canonical bank; it does not refute path-dependent endpoint
selection.

## 5. A literal cyclic successor at `n=4`

Write the residual coordinates as `Z_7`, and let `h=7` be a hub.  Put

\[
                 D_1=\{1,2,3\},\qquad D_2=\{1,3,5\}.       \tag{5.1}
\]

Each `D_j` chooses one member from every pair `\{a,-a\}` and is a regular
tournament out-neighbourhood.  Take the fourteen hub endpoints

\[
                 \{h\}\cup(v+D_j),qquad
                 v\in\mathbb Z_7,\quad j\in\{1,2\}.      \tag{5.2}
\]

The following paths are written as decimal rank-four masks:

```text
142 154 216  89 113
156 180 177  51  99
184 232 226 102  71
240 209 197  77  15
225 163 139  27  30
195 198 150  54  60
135 141 172 108 120
170 166  39  23  85
212 204  78  46  43
169 153  29  92  86
210 178  58  57  45
165 228 116 114  90
202 201 105 101  53
149 147  83  75 106
```

Literal replay proves:

1. the paths contain all `70` rank-four masks exactly once;
2. every path is a four-edge geodesic from a set to its complement;
3. their `56` intersections are all rank-three masks exactly once;
4. their `56` unions are all rank-five masks exactly once;
5. the unique hub-changing edge of the path based at
   `\{h\}\cup(v+D_j)` is the swap `h <-> v`;
6. residual translation permutes the fourteen unoriented paths.

Thus this is a literal `n=4` AGCF, not just an endpoint design.  Full `S_8`
stabilizer replay gives

\[
\begin{array}{c|c|c}
 & \text{size} & \text{element-order histogram}\\ \hline
\text{endpoint bank} & 14 & 1^1,2^7,7^6,\\
\text{path family} & 7 & 1^1,7^6.
\end{array}                                                \tag{5.3}
\]

Consequently the endpoint bank is `D_14` and the path factor is `C_7`
equivariant.  The `n=3` five-cycle is therefore not an isolated numerical
accident: it is the first member of a clean hub-plus-cyclic-tournament
packet pattern, and (5.2) is its exact next member.

This fixture is distinct from the previously authenticated three-sector
`n=3 -> n=4` witness.  The latter's endpoint bank has trivial `S_8`
stabilizer and no distinguished puncture with regular triple degrees.  Thus
both a symmetric fixture and a symmetry-breaking recursive fixture exist at
`n=4`.

It is also not a literal one-tag lift in disguise.  Its aggregate
coordinate-swap multigraph has multiplicity histogram

\[
                         2^{14},4^7.                       \tag{5.4}
\]

An intact lift of the five `n=3` child paths by one fixed tag swap would use
that same coordinate pair at least five times.  Since (5.4) has maximum
multiplicity four, the cyclic fixture contains no such intact child bank;
it is a global rebundling across the putative child/residual split.

## 6. Why the cyclic packet cannot be an all-`n` recursion

Let an endpoint bank at parameter `n` contain `Cat_n` complement pairs on
`[2n]`, and fix a prospective hub `h`.  Orient each pair toward the member
containing `h` and puncture `h`.  The resulting pointed block family is

\[
                 \mathcal H_h\subseteq
                 \binom{[2n-1]}{n-1},qquad
                 |\mathcal H_h|=\operatorname{Cat}_n.      \tag{6.1}
\]

### Proposition 6.1 (transitivity obstruction)

If a group preserving `\mathcal H_h` acts transitively on the `2n-1`
non-hub coordinates, then `(2n-1) | Cat_n`.

Indeed transitivity makes every point degree equal to some integer `d`, so

\[
                  (2n-1)d=(n-1)\operatorname{Cat}_n.       \tag{6.2}
\]

But `gcd(n-1,2n-1)=1`, proving the assertion.

The same condition follows directly for a cyclic packet.  A nonidentity
translation stabilizing an `(n-1)`-subset would partition that subset into
orbits whose common nontrivial length divides both `n-1` and `2n-1`; this is
impossible.  Hence every subset orbit under `C_(2n-1)` is free, and a cyclic
invariant family has size divisible by `2n-1`.

At `n=3` and `n=4`, the divisibilities are

\[
                    5\mid5,qquad7\mid14,                  \tag{6.3}
\]

matching one and two cyclic packets.  At `n=5`, however,

\[
                    2n-1=9,qquad \operatorname{Cat}_5=42,
                    \qquad9\nmid42.                        \tag{6.4}
\]

Equivalently, a regular family of 42 four-subsets on nine points would have
total incidence `168`, which is not divisible by nine.  An independent
orbit replay finds fourteen free `Z_9` orbits on all 126 four-subsets, so no
union of cyclic packets can have size 42.

### Proposition 6.2 (clean cyclic quotient normal form)

The preceding obstruction does not discard the useful cyclic quotient in
dimensions where it is arithmetically available.  Put `q=2n-1`, assume a
residual `C_q` fixes the hub, and suppose `3` does not divide `q`.  Its action
is then free on the relevant middle, lower-turn, and upper-turn levels: the
residual subset sizes are among `n-2,n-1,n,n+1`, and their only possible
nontrivial common divisor with `q` is three.  Moreover

\[
 \operatorname{Cat}_n=
 \frac{2q}{n(n+1)}\binom{2n-2}{n-1},
 \qquad \gcd(q,n(n+1))=1,                                \tag{6.5}
\]

so integrality of `Cat_n` forces `q | Cat_n`.  Consequently a
`C_q`-invariant AGCF consists of

\[
                         t=\frac{\operatorname{Cat}_n}{q}  \tag{6.6}
\]

base path packets and all their translates.  One base packet is exactly the
following finite datum:

\[
 (D,c,\phi,\pi),                                          \tag{6.7}
\]

where `D` is an `(n-1)`-subset of `Z_q`, `c` lies outside `D`, `phi` is a
bijection

\[
       D\longrightarrow \mathbb Z_q\setminus(D\cup\{c\}),
\]

and `pi` orders the `n` swaps

\[
              \{(h,c)\}\cup\{(a,\phi(a)):a\in D\}.        \tag{6.8}
\]

Starting from `\{h\}\cup D` and executing (6.8) gives the base complement
geodesic.  Conversely every cyclic path orbit has a unique description of
this form up to translating the base point.  The translated packets form an
AGCF if and only if their quotient middle, lower-turn, and upper-turn
resources partition the corresponding quotient resource sets.  Thus
(6.7)--(6.8) is a necessary-and-sufficient finite quotient problem, not only
a heuristic template.

There are `Cat_(n-1)` residual `(n-1)`-necklace orbits, and

\[
                 t=\frac{2\operatorname{Cat}_{n-1}}{n+1}. \tag{6.9}
\]

The fixtures above realize `t=1` at `n=3` and `t=2` at `n=4`.  The
tournament-neighbourhood specialization is nevertheless only a small-base
phenomenon.  A skew difference set chooses one member of each of the
`n-1` pairs `\{a,-a\}`, so it supplies at most `2^(n-1)` packet types.  At
the next later clean test `n=9`,

\[
       t=\frac{\operatorname{Cat}_9}{17}=286>256=2^8.      \tag{6.10}
\]

Hence even where full cyclic symmetry is arithmetically allowed, arbitrary
residual necklaces—not just tournament packets—are eventually necessary.

Therefore no recursion retaining a transitive/full-cycle pointed bank can
work for every `n`.  This is a structural no-go for that symmetry, not for
AGCFs.  A viable higher recursion must export at least:

* the path-dependent pointed block bank;
* an equivariant or non-equivariant hub-port assignment;
* the internal removed/inserted pairing and order data;
* the child/residual sector interface when full cyclic symmetry breaks.

No theorem here constructs those data for arbitrary `n`.

## 7. Reproducibility ledger

The original frozen classification remains authoritative:

```text
43c01ff4e532d202282fbbbd5922e99bb149ab6e114a075844c5980a8e94e3b7
  MATH_THEOREM_CATALAN_AGCF_N3_ENDPOINT_BANK_C5_CLASSIFICATION_20260731.md
efa744ef43f4b84006f86710d386a1d970f95226820f09f50b8ab2cddce5012a
  scratch/audit_catalan_agcf_n3_endpoint_bank_cycle_classification_20260731.py
9851ffd99b8cfc396ad11cd9e5ffca4095518922ffb889b1c076d3dcf3f14c67
  scratch/audit_catalan_agcf_n3_canonical_dyck_endpoint_nogo_20260731.py
```

Independent census and higher-scope replay:

```text
5072f411b41b1ac1dec103f4b29560f3e9f0b3e478214bba0d0114c4c99094ea
  scratch/audit_k_catalan_agcf_endpoint_cycle_higher_scope_20260731.py
0eac82a3dd323b166e4955005fa1abe3be3cce9fa7a603cdbcee78c64b8ab86a
  scratch/k_catalan_agcf_endpoint_cycle_higher_scope_20260731.audit.json
```

New literal `n=4` cyclic fixture:

```text
7b371076ecee408f292a0ee90543fb0fd93c163605d5a7df8c00535d117e8070
  scratch/k_catalan_agcf_n4_two_tournament_hub_packets_20260731.witness.txt
f500e7892bc1b93dd933b57ccd14c0131d3f3f29e249b97841bd800339873c26
  scratch/audit_k_catalan_agcf_n4_two_tournament_hub_packets_20260731.py
6e03580041ff6e9fe73a0a369b97071d97d3dc5cf98c6594ea8c654d19f676ef
  scratch/k_catalan_agcf_n4_two_tournament_hub_packets_20260731.audit.json
```

The canonical payload hashes are, respectively,

```text
de50c4f823f3d3d4ad5063e6cddd29702e3c53ef486a22b02b652cafeccd2686
02537f79cc55eecc5bc56e84977ed4d78d7eaf898587a08253d03ac148641c3f
```
