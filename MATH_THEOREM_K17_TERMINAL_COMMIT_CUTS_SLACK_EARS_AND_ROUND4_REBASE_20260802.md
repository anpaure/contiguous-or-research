# K17 terminal-commit cuts, slack ears, and the live residence rebases

Date: 2026-08-02  
Status: **exact terminal-cut and bounded-state theorems; one authenticated
five-circuit accepting packet; no uniform regenerative-expansion theorem**

## 0. Result

There are three distinct statements, and the frozen data support all three.

1. Terminal cap completeness has an exact cut description.  In the
   unit-transfer projection, a prescribed tight-cap move closes by either a
   directed return ear or a path from a cap with positive slack.  The minimum
   cap-only packet size is an exact shortest-path quantity.
2. The all-tight directed `C4` remains the sharp obstruction to a universal
   three-primitive theorem.  The recovered C14 endpoint switch and the
   authenticated C16 and latest C10 winners do **not** defeat that
   obstruction: their cap projections are slack-fed paths, not tight cycles.
3. There is nevertheless an exact historical instance-level bounded accepting
   packet.  The symmetric difference from the authenticated C16 factor to the
   3,502-run factor is the disjoint circuit packet

   \[
                    C_6+C_8+C_{10}+C_{12}+C_{10},             \tag{0.1}
   \]

   with 23 changed quotient rows.  Its simultaneous terminal commit preserves
   every immediate factor gate and changes the exact current blocker-orbit
   count

   \[
                       216\longrightarrow206.                 \tag{0.2}
   \]

   Thus it is a negative accepting path of length five in the root-active
   batch builder.  No claim is made that its first four prefixes are feasible
   commits.

The 3,502-run factor scores `198` on the old 413-row blocker bank, but exact CEGAR
adds eight canonically new rows.  The authoritative bank is therefore 421,
not the invalid raw-text union 585, and the factor scores `206` on it.  It is a
positive control across the old `B=200` face and simultaneously a
`NEED_CEGAR` factor; it is not resident and is not a word.

The live dominant endpoint has since moved to 2,754 short positive runs.  It
passes the same immediate factor gates and has upper-hole vector
`(1853,357,0)` at ranks 11--13, but it remains nonresident.  Canonical
separation against the supplied 445-bank gives 20 new rows, the 465-row union,
and score 162.  Section 9 is the authoritative live rebase; the C16-to-3502
packet remains the audited bounded-path fixture.

## 1. Exact terminal-commit model

Let `E` be the literal option rows, and let `F subset E` be the incumbent.
For a terminal packet `P`, write

\[
 R_P=F\setminus F^P,\qquad G_P=F^P\setminus F.               \tag{1.1}
\]

All quantities below are computed from the literal terminal row set `F^P`.
They are not sums of marginal scores cached on isolated primitives.

Let `R`, `O`, and `U` be respectively the facet rows, owner vertices, and
required rank-ten cap targets.  With binary terminal variables `x_e`, the
immediate factor rows are

\[
\begin{aligned}
 \sum_{e\in E(r)}x_e&=1 &&(r\in R),\\
 \sum_{e\in E(o)}x_e&=2 &&(o\in O),\\
 x_e&=1 &&(e\text{ protected}),\\
 \sum_{e:U\subset e}x_e&\ge1 &&(U\in\mathcal U).             \tag{1.2}
\end{aligned}
\]

The quotient formulation may subtract fixed protected incidences from the
right sides; this is algebraically the same system.

Once the degree rows in (1.2) hold, quotient connectedness is exactly

\[
              x(\delta_O(S))\ge2
       \quad(\varnothing\ne S\subsetneq O).                  \tag{1.3}
\]

Indeed a degree-two undirected graph is connected if and only if it has no
zero edge cut, and all of its cuts have even cardinality.  Physical
connectedness additionally requires the voltage subgroup of each quotient
component to generate the deck group.  For the frozen single quotient cycles
over `Z17`, this reduces to nonzero total voltage.

### Theorem 1.1 (exact palette inequalities)

For a target `U`, put

\[
 \mu_F(U)=|\{e\in F:U\subset e\}|,
 \quad d_P(U)=|\{e\in R_P:U\subset e\}|,
 \quad g_P(U)=|\{e\in G_P:U\subset e\}|.                    \tag{1.4}
\]

Then `F^P` covers every required target if and only if

\[
             d_P(U)-g_P(U)\le \mu_F(U)-1
             \qquad(U\in\mathcal U).                         \tag{1.5}
\]

Equivalently, for every \(S\subseteq\mathcal U\),

\[
 \sum_{U\in S}(d_P(U)-g_P(U))
 \le \sum_{U\in S}(\mu_F(U)-1).                              \tag{1.6}
\]

The family (1.6) is exact because it contains all singleton inequalities;
summing (1.5) proves every other member.

There is also an exact exposure form.  Let

\[
 \mathcal E_P=\{U:\operatorname{Occ}_F(U)\subseteq R_P\}.    \tag{1.7}
\]

Since the incumbent has no cap holes,

\[
       F^P\text{ cap-complete}
       \quad\Longleftrightarrow\quad
       \mathcal E_P\subseteq\operatorname{supp}(G_P).        \tag{1.8}
\]

Proof.  The terminal load is exactly
`mu_F(U)-d_P(U)+g_P(U)`, which proves (1.5).  A target outside
`E_P` retains an unchanged old witness.  A target in `E_P` has lost every old
witness and therefore needs a witness in `G_P`, proving (1.8).  \(\square\)

On overlapping proposals, `R_P` and `G_P` must first be formed from the
terminal row map.  For a pair, the exact correction to isolated columns is
the overlap square

\[
 \mu^{12}_U-\mu^1_U-\mu^2_U+\mu^0_U,                         \tag{1.9}
\]

with the usual pair and triple Möbius corrections for three proposals.

### Exact blocker rows

For a purely negative blocker `c` with support `S_c`, define

\[
 r_c(x)=\mathbf 1[S_c\subseteq\operatorname{supp}x].          \tag{1.10}
\]

Its exact binary linearization is

\[
 r_c\le x_e\ (e\in S_c),
 \qquad
 r_c\ge \sum_{e\in S_c}x_e-|S_c|+1.                         \tag{1.11}
\]

For a fixed bank `A`, let `b_A(x)=sum_(c in A) r_c(x)`.  Relative to the
incumbent, define the killed and born rows

\[
\begin{aligned}
 K_A(P)&=\{c:r_c(F)=1,\ r_c(F^P)=0\},\\
 N_A(P)&=\{c:r_c(F)=0,\ r_c(F^P)=1\}.
\end{aligned}                                                \tag{1.12}
\]

Then the exact terminal identity is

\[
       b_A(F^P)-b_A(F)=|N_A(P)|-|K_A(P)|.                    \tag{1.13}
\]

For example, a terminal commit from C16 to `A413 <= 200` must satisfy

\[
                        |K|-|N|\ge13.                         \tag{1.14}
\]

No sum of primitive blocker deltas may replace (1.13): each `r_c` is an AND
monomial, and two circuits may jointly kill or jointly create it.

### Theorem 1.2 (terminal compound criterion)

Let `Q_1,...,Q_m` be root-active alternating circuits whose simultaneous
literal rewrite is well-defined.  Their batch is a negative accepted packet
if and only if its one terminal row set satisfies (1.2), (1.3), the voltage
test, every declared downstream return row, and

\[
                \Phi(F^{Q_1\cup\cdots\cup Q_m})<\Phi(F).      \tag{1.15}
\]

For blocker potential, (1.15) is exactly `|K|>|N|`; for weighted residence
tokens, it is the corresponding weighted set difference.  None of the
singletons is required to be a feasible commit.

Proof.  Root activity and compatibility define one terminal row set.  The
displayed rows are respectively exact facet/owner/protection, cap, topology,
lift, downstream, and objective conditions.  They are therefore necessary
and sufficient.  Intermediate prefixes are builder states, not commits.
\(\square\)

## 2. Cycle space gives a bounded pending path

The terminal criterion becomes useful when combined with the exchange-cycle
decomposition.

### Theorem 2.1 (cycle-space batch augmentation)

Suppose `F` and `F'` choose one option on every facet, have the same owner
degrees, and every changed old/new option pair retains one owner endpoint.
Orient the changed facet from its removed owner to its added owner.  The
resulting directed multigraph is Eulerian and hence decomposes into directed
circuits

\[
                         Q_1+\cdots+Q_m.                      \tag{2.1}
\]

If the circuit bank contains these root-active circuits, a terminal-only
pending builder (or one whose declared prefix-debt budget contains these
partial unions) has a path of `m` circuit additions from `F` to the terminal
row set `F'`.
If `F'` passes Theorem 1.2 and has lower potential, this is a negative
accepted path of length `m`, even if every proper prefix is blocked.

Proof.  Equal terminal owner degrees imply that each owner has equal removed
and added multiplicity, so the oriented difference is Eulerian.  Eulerian
decomposition gives (2.1).  Adding its circuits as pending columns reconstructs
the full difference.  Only the final node is committed, and Theorem 1.2 then
applies.  \(\square\)

For ordinary perfect matchings, the same statement is the familiar
decomposition of a symmetric difference into alternating even cycles.  The
theorem is a cycle-space statement, not an assertion that all intermediate
graphs remain factors.

## 3. Exact cap circulation and the ear bound

Assume a primitive transfers one cap unit from `u` to `v`; orient it
`u -> v`.  Let `y` be a selected arc set and put

\[
                         b_F(U)=\mu_F(U)-1.                   \tag{3.1}
\]

Then (1.5) becomes

\[
 \partial y(U):=y(\delta^+(U))-y(\delta^-(U))\le b_F(U),     \tag{3.2}
\]

and summing over a shore gives

\[
 y(\delta^+(S))-y(\delta^-(S))\le b_F(S).                    \tag{3.3}
\]

This is an integral network-flow projection.  It omits row conflicts,
protection, topology, voltage, and trace cost.

### Theorem 3.1 (tight causal arc and shortest ear)

Let `q:u -> v` be prescribed, with `b_F(u)=0`.  Assume the cap arcs are
otherwise independently and jointly selectable.  The minimum cap-safe packet
containing `q` has cardinality

\[
 1+\min\left\{
      \operatorname{dist}(v,u),
      \min_{s:b_F(s)>0}\operatorname{dist}(s,u)
    \right\},                                                \tag{3.4}
\]

where an absent path has infinite distance.

Proof.  Decompose a minimum feasible unit arc set into directed cycles and
paths from positive-divergence vertices to negative-divergence vertices.
The component containing `q` is either a cycle, whose remainder is a
`v -> u` path, or a path whose source `s` has positive divergence.  By (3.2),
the latter requires `b_F(s)>0`, and its prefix before `q` is an `s -> u`
path.  Removing all unrelated components gives the lower bound.  Conversely,
a return path plus `q` is a circulation, while a slack-source path followed
by `q` has positive divergence only at an allowed slack source.  \(\square\)

Thus a packet of at most `L` exists in the cap projection exactly when one
of the two distances in (3.4) is at most `L-1`.

### Corollary 3.2 (sharp tight-C4 obstruction)

For four tight caps and only the arcs

\[
 U_0\to U_1\to U_2\to U_3\to U_0,                           \tag{3.5}
\]

the only cap-safe selections are the empty set and all four arcs.  Hence no
nonempty packet of at most three primitives closes.  A one- or two-arc
return/supply ear bypasses it at budget three exactly as prescribed by
(3.4).

More generally a tight directed `C_(L+1)` rules out every universal
`L`-packet theorem based only on cap completeness and bounded degree.  Giving
the full long cycle negative abstract cost shows that a negative long packet
may coexist with the short obstruction.  This is a cap-projection
counterexample, not a new literal K17 factor.

The joint-selectability assumption in Theorem 3.1 is essential.  A formal
two-arc cap return can request incompatible alternatives in one terminal
facet row, or its terminal owner graph can have a zero cut or bad voltage.
Therefore a short cap ear is not by itself a literal accepting path.

## 4. Exact bounded-state / min-cost-circulation theorem

For a fixed incumbent `F`, support bound `H`, circuit budget `L`, and declared
debt bounds, build a layered graph `B_L(F)` as follows.

* A node stores the layer and the complete pending literal row delta.  Any
  cap, port, component, voltage, or trace summary used to merge nodes must be
  proved sufficient; otherwise the literal delta remains part of the state.
* A layer arc is materialized for every compatible root-active circuit in the
  declared bank.
* A commit arc is materialized exactly when the terminal row set passes
  (1.2)--(1.3),
  cap and voltage replay, blocker indicators (1.11), and every declared
  downstream return row.  Give this arc cost `Phi(F')-Phi(F)` and all
  accumulation arcs cost zero.
* Add a zero-cost reset arc from the committed node to the root.

### Theorem 4.1 (negative return or dual certificate)

For this complete materialization, there is a negative accepted packet using
at most `L` circuits if and only if the augmented builder contains a negative
directed cycle through the reset arc.  Equivalently, the minimum-cost unit
circulation using one reset arc has negative value.

Because the builder is a network, its unit-flow polytope is integral.  If no
negative cycle exists, there is a Bellman--Ford/Farkas potential `pi` such
that

\[
                   \pi(v)-\pi(u)\le c(u,v)                   \tag{4.1}
\]

for every materialized arc.  Summing (4.1) around a cycle proves that every
packet encoded by this complete builder has nonnegative cost.  On a reset arc
`a -> root`, (4.1) reads
`pi(a) >= pi(root)`, exactly the accepting-state inequality in the frozen
closed-packet theorem.  If no accepting node is reachable, the reachable-set
boundary is the corresponding cut certificate.

Proof.  Layer arcs strictly increase depth, so every directed cycle contains
one commit/reset return and encodes exactly one terminal packet.  Its cost is
the telescoping terminal potential difference.  Integral min-cost circulation
duality gives the alternative (4.1); it is also the standard no-negative-cycle
Bellman--Ford theorem.  \(\square\)

This is the exact bounded-state formulation requested by the frozen
closed-packet theorem.  A dual computed on a truncated circuit bank, a cap
projection, or incomplete trace summaries certifies only that materialized
subproblem.

## 5. Recovered C14 and authenticated C16 ear structure

The recovered raw-C14 owner circuit is

\[
 767\to2687\to3199\to3263\to3325\to5373\to1407\to767.       \tag{5.1}
\]

Its seven recovered variable replacements are

```text
38->44, 286->304, 3178->3183, 5528->5530,
5759->5763, 1328->1331, 1343->1336.
```

These seven pairs are embedded recovered endpoint-difference constants.  The
new audit checks their internal owner/cap consistency against the raw-C14
model and reconstructs the predecessor, but it does not compare that
predecessor to a separately frozen C12 sparse model.  Accordingly the C14
ear decomposition below is conditional on this recovered patch; the C14
endpoint and aggregate census remain independently authenticated.

Its cap transfers decompose into slack-source paths of lengths

\[
                              1,2,4.                          \tag{5.2}
\]

Every net source has base load two.

The clean-C14 to C16 winner is the owner circuit

\[
 8831\to9977\to9721\to9407\to13495\to23373\to23381
 \to10875\to8831,                                           \tag{5.3}
\]

with eight variable replacements

```text
18155->18174, 20219->20217, 1140->1139, 19896->19912,
14575->14574, 23461->23462, 24193->24178, 18231->18219.
```

Its cap transfers decompose into slack-source paths of lengths

\[
                              1,3,4,                          \tag{5.4}
\]

again with all net sources at load two.  In particular, neither winner has a
tight cap-dependency cycle.  They instantiate the slack-source branch of
Theorem 3.1; they do not contradict Corollary 3.2.

The authenticated endpoint summaries remain

```text
C14 after C12:      3,829,899 simple; 856 cap-safe; 271 connected;
                    13 improving-one; best 3,774
C16 after clean C14: 36,989,415 simple; 2,313 cap-safe; 693 connected;
                     51 improving-one; best 3,672
```

and its exact endpoint has `2057+1615=3672` positive short runs, all 19,448
caps, 3,944 protected edges, and one physical cycle.  The C14 full
materialized catalogue is absent locally, and the C16 candidate TSV is
truncated after 542 complete rows plus one partial row; the census audit and
winning patch are intact.  No new catalogue-completeness claim is made here.

## 6. The authenticated five-circuit accepting packet

Canonical comparison of the C16 and floor-3502 sparse models gives 23 removed
and 23 added residual options.  The exact owner-exchange decomposition is

\[
\begin{array}{rcl}
 C_6&:&5113\to8831\to9023\to5113,\\
 C_8&:&5743\to5839\to13945\to13933\to5743,\\
 C_{10}&:&3005\to4025\to16037\to22901\to19373\to3005,\\
 C_{12}&:&7767\to7795\to8049\to12789\to13991\to13487\to7767,\\
 C_{10}&:&6891\to6905\to13747\to9655\to9687\to6891.
\end{array}                                                  \tag{6.1}
\]

The first four circuits are exactly the C16-to-floor-3553 terminal delta.  The
last `C10` is the fully catalogued floor-3553-to-floor-3502 move.  Its complete
local `C10/C12` census is

| shell | simple | cap-safe | connected | improving-one |
|---|---:|---:|---:|---:|
| `C10` | 50,748 | 113 | 42 | 2 |
| `C12` | 415,194 | 283 | 84 | 4 |

and the promoted `C10` changes `3553 -> 3502`.  Its cap projection consists
of four slack-source paths of lengths `1,1,1,2`, all starting at load-two
caps.

Separate endpoint factor replays certify exact facets, owners, caps,
protected edges, nonzero voltage, and one physical cycle.  Let
\(\mathcal B(F)\) denote the canonical set of exact current blocker support
signatures.  The frozen sets obey

\[
 |\mathcal B(F_{16})|=216,\qquad |\mathcal B(F_{3502})|=206,
 \qquad |\mathcal B(F_{16})\cap\mathcal B(F_{3502})|=198.    \tag{6.2}
\]

Thus terminal acceptance is supplied by the separate factor/voltage/residence
replays, while the new deterministic audit supplies the five-circuit
decomposition and blocker-signature arithmetic.  Neither artifact is being
used outside its stated scope.

Hence the simultaneous packet removes 18 current support signatures and
introduces 8.  Independently, each endpoint has one exact `Z17` orbit per
current signature, so the two residence audits give

\[
                 216-18+8=206,
 \qquad 17(216-206)=170.                                    \tag{6.3}
\]

By Theorem 2.1 this is an accepted path of five macro circuits and support 23
in the terminal-only pending builder.  Equation (6.3) is its exact negative
terminal cost.  It is an instance theorem only: the frozen local artifacts do
not certify feasibility, topology, or a particular finite debt bound for each
of the first four prefixes.

## 7. Canonical round-four CEGAR reconciliation

The old bank `A413` and the new exact current set have

\[
 |A_{413}|=413,\qquad |\mathcal B(F_{3502})|=206,\qquad
 |A_{413}\cap\mathcal B(F_{3502})|=198.                     \tag{7.1}
\]

Thus the canonical union is

\[
                         |A_{421}|=421,                       \tag{7.2}
\]

with five new ternary and three new quaternary rows.  The eight literal
vectors are

```text
-34901 -32071 -14544 -11678 0
-32418 -27557 -9194 -8831 0
-22900 -12851 -5223 0
-19024 -2712 -2193 0
-18679 -18659 -18174 0
-18103 -3969 -545 0
-18058 -8758 -952 0
-15156 -14597 -9518 -4293 0
```

Literal order inside a clause is immaterial.  Comparing raw text lines before
canonicalizing each literal vector produces a false 585-row union and must be
rejected.  The authoritative canonical file has SHA-256

```text
8caaf19d74b161146e312a99e6e25d46d8e2e67b9e20785a4382bd066dc28106
```

The exact scores are

| factor | `A413` | `A421` | exact current signatures/orbits |
|---|---:|---:|---:|
| C16 | 213 | 214 | 216 |
| floor 3502 | 198 | 206 | 206 |

Seven of the eight support signatures introduced relative to C16 are
canonical new rows; the eighth was already in `A413`.  Conversely, one
canonical new row was already falsified by C16.  This explains why
set-difference counts and fixed-bank score differences are not
interchangeable.

Consequently the new factor crosses the old `A413, B=200` face with two units
of slack, but after exact separation it violates 206 rows of `A421`.  The
first strict round-four bound is 205; reaching `A421 <= 200` needs a further
net repair of at least six rows.  None of these blocker scores is a residence
certificate.

## 8. What regenerated, and what did not

The quotient cap-load histograms are

| checkpoint | load 1 | load 2 | load 3 | load 4 | load 5 | slack caps |
|---|---:|---:|---:|---:|---:|---:|
| raw C14 / clean C14 / C16 | 988 | 90 | 6 | 56 | 4 | 156 |
| floor 3553 / floor 3502 | 986 | 93 | 5 | 57 | 3 | 158 |

The total excess cap mass is fixed, but the C16-to-floor-3553 four-circuit
subpacket spreads it over two additional cap orbits.  The final C10 preserves
that distribution.
This is genuine **accessible slack-source regeneration**, not creation of new
total cap mass.

The downstream deck does not improve monotonically:

| checkpoint | rank-11 holes | rank-12 holes | rank-13 holes |
|---|---:|---:|---:|
| C16 | 1,836 | 408 | 17 |
| floor 3502 | 1,802 | 425 | 17 |

Ranks 14 and above remain complete.  The packet gains rank-11 coverage and
residence while paying rank-12 debt.  A regenerative class must therefore
state its admissible debt vector; cap slack alone is not a closed invariant.

## 9. Live dominant endpoint: 2,754 and locally canonicalized `A465`

The current dominant authenticated factor is

```text
scratch/r2_k17_residence_master_round1_20260802/final2754/
  after_c14_2754_single/final2754.factor.tsv
```

with sparse model `round000.model`.  Exact replays give

\[
 2754=1377\text{ length-two runs}+1377\text{ length-three runs}
     =162\cdot17.                                            \tag{9.1}
\]

It has all 24,310 rank-eight facets and rank-nine owners, all 19,448
rank-ten caps, 3,944 protected edges, one quotient component with nonzero
voltage, and one physical cycle.  It is nevertheless nonresident.

The factor, model, and supplied canonical 445-bank have respective SHA-256
values

```text
fac9ad6c29f39a89c9cdce4e88f231e5f73725535e6e1aea47aeb3f43aaaddc7
edc937949e741382fbf53cb80f1d32aa9c7d7f008f60894682ecac0b1e7747a7
e151ccd9327d66430e7c0c08f601b49c8e4f7c632871f68ca2c3d604b5b63c15
```

The supplied 445-row bank scores 142 on this model.  Canonical comparison
with the 162 exact current support signatures gives

\[
 |A_{445}\cap\mathcal B(F_{2754})|=142,\qquad
 |\mathcal B(F_{2754})\setminus A_{445}|=20,\qquad
 |A_{465}|=465.                                              \tag{9.2}
\]

The 20 new rows have arity histogram

\[
                         1^2\,2^1\,3^5\,4^{12},              \tag{9.3}
\]

and are retained literally in

```text
scratch/k17_final2754_cegar_rebase_20260802.novel20.cnf
```

The factor scores 162 on the deterministic locally canonicalized `A465`;
the first strict bound is 161.
Thus it still satisfies `B=200`, now with 38 rows of slack, while having
2,754 prohibited short runs.  Even after current-row separation, `B=200` is
a search proxy and not a residence criterion.

The complete one-endpoint-retaining directed single-circuit catalogue at this
endpoint contains 1,922 `C6` and 6,159 `C8` circuits.  Respectively 78 and 53
are cap-safe, and 43 and 23 are one-component physical candidates, but none
improves the positive-short-run primary.  This closes only the stated single
`C6/C8` face; it says nothing about pairs, longer circuits, or general
compound packets.

The new upper ledger is Pareto-incomparable with floor 3502:

| checkpoint | rank-11 holes | rank-12 holes | rank-13 holes |
|---|---:|---:|---:|
| floor 3502 | 1,802 | 425 | 17 |
| final 2754 | 1,853 | 357 | 0 |

Ranks 13 through 17 are complete at final 2754.  Residence, rank 12, and
rank 13 improve, while rank 11 pays 51 additional holes.  The quotient cap
load histogram is

\[
                  1^{984}2^{97}3^3 4^{57}5^3,               \tag{9.4}
\]

so 160 cap orbits have positive slack.  This continues the observed spreading
of fixed cap surplus, but it is not a proof of lifted expansion.

No source-factor row, opening, or source audit accompanies this endpoint.
The verifier and deep-upper scopes explicitly exclude source and compiler
claims.  The exact history from floor 3502 to final 2754 is also not rebound
here as one prefix-feasible packet; this section authenticates the endpoint,
the current blocker separation, the short single-circuit face, and the upper
ledger only.

## 10. Exact additional expansion hypothesis

Define `chi_D(F,F')` to be the minimum number of compatible root-active
alternating circuits whose pending union changes `F` to `F'` while respecting
the declared pending-debt budget `D`; set it to infinity if no such
representation exists.  Let `C` be a class defined by literal terminal gates
and downstream budgets.

### Lifted terminal cycle expansion `LTCE(C;L,H,D,epsilon)`

For every `F in C` with `Phi(F)>0`, there is `F' in C` such that

\[
 \chi_D(F,F')\le L,qquad
 |F\setminus F'|\le H,qquad
 \Phi(F')\le\Phi(F)-\epsilon.                               \tag{10.1}
\]

All cap cuts, row compatibility, topology, voltage, blocker births, and
declared downstream returns are part of membership in `C` or of the full
lift defining `chi_D`.

### Theorem 10.1 (regenerative descent)

If `Phi` is a nonnegative integer, `epsilon >= 1`, and `LTCE` holds, repeated
terminal commits reach `Phi=0` in at most

\[
                         \lceil\Phi(F_0)/\epsilon\rceil       \tag{10.2}
\]

steps while remaining in `C`.

Proof.  Each commit remains in `C`, so (10.1) reapplies, and the integer
potential decreases by at least `epsilon`.  A positive terminal value would
admit another decrease, so termination occurs only at zero.  \(\square\)

For the complete root-active circuit bank, `LTCE` is necessary and sufficient
for the bounded batch builder: it is exactly the assertion that every
positive state has an accepted return of cost at most `-epsilon` within the
declared support and debt bounds.  For integer `Phi` and `epsilon=1`, this is
equivalent to a negative accepted return.  Theorem 4.1 supplies either the
required return or an auditable potential/cut certificate for the complete
materialized builder.

The frozen data verify only the single-state inequalities

\[
 \chi_\infty(F_{C16},F_{3502})\le5,\qquad H=23,\qquad
 |\mathcal B(F_{3502})|\le|\mathcal B(F_{C16})|-10,          \tag{10.3}
\]

where `chi_infinity` denotes the terminal-only builder with no claimed finite
prefix-debt bound.  The slack-cap count increases `156 -> 158`.  These facts
do not bound the supremum of `chi_D` over all positive factors.  A uniform
theorem cannot be
deduced from cap degree, cap completeness, or slack count alone: slack sources
may be unreachable in the lifted compatibility graph, and Corollary 3.2 gives
arbitrarily long all-tight returns.  The exact missing hypothesis is therefore
bounded **negative return in the full lifted cycle space**, not merely a short
cycle or an expander condition in the cap projection.

## 11. Heptagonal reserve/history refinement of `LTCE`

The heptagonal circulation theorem supplies a concrete candidate family for
the abstract return in Section 10, but it also identifies two state
coordinates which cannot be projected away.

For every physical cap `U`, write

\[
                         s_F(U)=M_F(U)-1.
\]

A compound row exchange gives a cap-transfer multigraph `D`, oriented from
each old cap to its replacement cap.  Its exact terminal cut is

\[
 \operatorname{out}_D(S)-\operatorname{in}_D(S)
                  \le \sum_{U\in S}s_F(U)                 \tag{11.1}
\]

for every cap shore `S`; singleton shores are equivalent to the full family.
The total reserve `sum_U s_F(U)` is invariant.  Decomposing `D` into cycles
and paths shows that every path consumes one duplicate-cap reserve at its
initial cap and replants one at its terminal cap.  This is the exact
“balanced backup” ledger.  It preserves support, whereas cap-multiset
equality would additionally require zero drift at every cap.

For an actually ordered packet, with the second step evaluated
state-relatively after the first, this terminal ledger refines to the exact
product

\[
 (z_A,\beta_A,\mathbb W_A)(z_B,\beta_B,\mathbb W_B)
 =\bigl(z_A+z_B,\max\{\beta_A,\beta_B-z_A\},
              \mathbb W_B\otimes\mathbb W_A\bigr),       \tag{11.1a}
\]

where `beta` is maximum prefix cap debt and `mathbb W` is the signed paired
old/new socket relation with weight `C_new-C_old`, including whole-component
drift.  On a disjoint/additive literal ledger, an atomic
terminal union has cap requirement `(-z_A-z_B)_+`.  If the supports overlap,
one must replay the final symmetric difference and use
`(-z_(A triangle B))_+`; primitive deltas need not add.  Conceptual prefixes
must not introduce an artificial cap obligation.  Regeneration further
requires the output reserve vector, not merely its total mass, to return to
the declared state class.

The authenticated `2,822 -> 2,754` `C14` has holonomy `5 mod 17`.  It uses
three quotient path starts at old load-two cap-orbit representatives
`13783,27447,28075` and plants the three new terminal load-two representatives
`13727,28331,43755`.  Hence it is the nontrivial support-preserving mode
predicted by (11.1), not the fixed-label cap-multiset rotor.

The second indispensable coordinate is the complete labelled boundary
history of the seven retained paths: forward and reverse positive/zero
absolute capped-age matrices, endpoint frames and connector labels, capped
lengths, and constant-coordinate cores.  The aggregate drift
\(B_2(\mathcal H)-B_1(\mathcal H)\) is exact for a closed co-oriented replay, but
it is not a recursive socket under a later reversal or connector.  At fixed
depth, a protected Pascal state must export the full bi-history
relation, or the audited positive pivot reset with its triangular input
domain plus a separately supplied literal deletion-history dual/reversed
reset and its own domain.  Under `d -> d+1`, it must additionally export the
new oldest labels, retain the longer bi-history, or supply certified resets
at the new depth; no transition-compatible depth section is available.

After a cap `U` and two depth-`d` collars are transported into one frame,
assume their positive endpoint labels satisfy
`I^+ union D^+ subseteq U`, their dual negative labels avoid `U`, and the
two old cross-collar inequalities pass.  With
`W=U setminus (I^+ union D^+)`, the exact same-cap connector menu is

\[
 |W|(|W|-1)\ge (|U|-2d)(|U|-2d-1),                       \tag{11.1b}
\]

when `|U|>=2d+1`.  Thus local backup connectors are quadratic in the central
regime once endpoint separation and the two old cross-collar inequalities
pass.  What remains open is placing those owners/facets, the heptagon ears,
the topology, and the Pascal opening in one selected factor; marginal
connector abundance does not perform that joint embedding.

Accordingly the proof-safe specialization of `LTCE` is the balanced
cap/history host-spread hypothesis of
`MATH_THEOREM_BALANCED_CAP_BACKUP_AND_BOUNDARY_HISTORY_REGENERATION_20260802.md`:
each rooted task has `Omega(k^7)` **physically exposed** accepted macro-tickets,
each ticket uses `O(Ld)` nonanchor cap/history/protected resources (including
capped-length and whole-component/core tokens, unless all evaluated
components are longer than `d`), and each such resource has load `O(k^6)` in
every other rooted atlas.  The private anchor banks are assumed pairwise
compatible/disjoint.  The resulting greedy cut is

\[
                         (H-1)aLCd<ck,                    \tag{11.2}
\]

which selects one disjoint ticket for each of `H` tasks and, when the state
regenerates, implies integer descent.  The central-regime phasewise
prospective count `Theta(k^7)` and the twisted seven-run count do not prove
physical exposure, history acceptance, core-token load, or backup
distribution.  Those joint spread rows—not raw central supply—are the
remaining expansion hypothesis.

## 12. Frozen artifacts and scope lock

The deterministic audit and its outputs are

```text
MATH_THEOREM_BALANCED_CAP_BACKUP_AND_BOUNDARY_HISTORY_REGENERATION_20260802.md
MATH_THEOREM_A_HEPTAGONAL_CAP_BACKUP_AND_BIHISTORY_TICKET_INTERFACE_20260802.md
MATH_THEOREM_K_CAP_BACKUP_HISTORY_TICKET_MONOID_AND_HEPTAGON_HOST_GATE_20260802.md
MATH_THEOREM_K_HEPTAGON_CAP_HOLONOMY_BACKUP_AND_HISTORY_TICKET_INTERFACE_20260802.md
scratch/audit_k17_terminal_commit_ear_round4_20260802.cpp
scratch/k17_terminal_commit_ear_round4_20260802.audit.json
scratch/k17_terminal_commit_ear_round4_20260802.novel8.cnf
scratch/audit_k17_final2754_cegar_rebase_20260802.cpp
scratch/k17_final2754_cegar_rebase_20260802.audit.json
scratch/k17_final2754_cegar_rebase_20260802.novel20.cnf
scratch/k17_final2754_cegar_rebase_20260802.cumulative465.cnf
```

Principal inputs are

```text
scratch/ad_k17_upper_component_cegar_20260802/cumulative413.authoritative.blocks.cnf
scratch/r2_k17_residence_master_round1_20260802/c16_escape001/
scratch/p_k17_physical_deadline_master_20260802/c10_escape_from3553_cegar/
scratch/k17_upper_decorated_longrun_circuit_20260802/seed3502/
scratch/r2_k17_residence_master_round1_20260802/final2754/
```

The canonical 421-row bank and floor-3502 sparse model were copied from the
authenticated remote freeze into the local CEGAR directory and rebound by
SHA-256 before use.  The supplied canonical 445-bank and final-2754 model
were rebound in the same way.  Both audits canonicalize literal vectors
before all set operations.

No new exhaustive C14/C16 enumeration was performed.  No residence
completion, deeper-upper completion, source factor, compiler, universal word,
or final construction is claimed.
