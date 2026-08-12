# Exact eager rank-11 coverage from undirected turn summaries

Date: 2026-08-02

Status: exact theorem and exact authenticated-catalogue census.  No solver was
launched.  Rank 12, source/compiler, connectivity and voltage remain separate.

## 1. The three-owner union has only two labels of state

Let `u` be a selected rank-nine owner and let its two selected undirected
neighbours be `v` and `w`.  Every Johnson neighbour contributes one outside
coordinate:

\[
 x(v,u)\in v-u,
 \qquad
 x(w,u)\in w-u.                                        \tag{1.1}
\]

Therefore

\[
             v\cup u\cup w
       =u\cup\{x(v,u),x(w,u)\}.                         \tag{1.2}

It has rank 11 exactly when the two outside coordinates are different.
Neither the direction of the factor nor the identities of the deleted owner
coordinates are needed.

This observation removes the proposed 728 target automata.  The entire turn
state is an unordered pair from the eight coordinates outside `u`.

## 2. Summary variables

For every owner orbit `u` and outside coordinate `x notin u`, introduce

\[
 S(u,x)=1
 \quad\Longleftrightarrow\quad
 \text{some selected edge incident with `u` contributes `x`}. \tag{2.1}

There are

\[
                  1430\cdot8=11440                     \tag{2.2}

such variables.

Let `E(u,x)` be the set of nonfixed primary edges in this category.  If the
category contains a protected fixed edge, add the unit `S(u,x)`.  Otherwise
add the support clause

\[
              \neg S(u,x)\vee\bigvee_{e\in E(u,x)}p_e. \tag{2.3}

For every nonfixed candidate add

\[
                         \neg p_e\vee S(u,x).            \tag{2.4}

An empty support in (2.3) is the unit `not S(u,x)`.  Thus (2.3)--(2.4)
make the summary exact.  The base formula already gives degree two at every
owner; the number of true categories is consequently one or two.

For every unordered pair of different outside coordinates introduce

\[
                         Q(u;\{x,y\}).                   \tag{2.5}

There are

\[
                1430{8\choose2}=40040                  \tag{2.6}

pair variables.  Define them by the three Horn/dual-Horn rows

\[
\begin{aligned}
 &\neg S(u,x)\vee\neg S(u,y)\vee Q(u;\{x,y\}),\\
 &\neg Q(u;\{x,y\})\vee S(u,x),\\
 &\neg Q(u;\{x,y\})\vee S(u,y).
\end{aligned}                                          \tag{2.7}

Hence `Q` is true exactly for the pair of distinct exterior categories
present at the selected turn.

## 3. Orbit coverage

The rotation action of `Z_17` on rank-11 sets is free.  Indeed, 17 is prime,
so a nontrivial stabilizer would make the set invariant under the whole
17-cycle and force rank zero or 17.

For a rank-11 orbit representative `T`, add the single clause

\[
 \bigvee_{\operatorname{can}(u+\{x,y\})=T}
                         Q(u;\{x,y\}).                  \tag{3.1}

Every such clause has exactly 55 literals.  This count is structural: a
literal rank-11 set contains

\[
                         {11\choose9}=55                \tag{3.2}

rank-nine owners, and freeness preserves the count after quotienting.

There are

\[
                  {17\choose11}/17=728                 \tag{3.3}

target orbits.

### Theorem 3.1 (exactness)

On the exact owner-degree-two factor face, (2.3)--(2.7) and (3.1) are
satisfiable if and only if every physical rank-11 target occurs as the union
of three consecutive owners.

#### Proof

Given a selected factor, set every `S` from its incident selected edges and
every `Q` from the resulting pair.  Equations (2.3)--(2.7) hold.  By (1.2),
clause (3.1) is satisfied exactly when its target orbit is realized by one
three-owner turn.  Equivariance then develops that turn to all 17 literal
targets in the orbit.

Conversely, a true `Q(u;{x,y})` forces both summary categories.  Their
support clauses produce selected incident edges contributing `x` and `y`.
Since `x!=y` these are different edges, and owner degree two makes them the
actual selected turn.  Its three-owner union is `u+{x,y}` by (1.2).
Therefore every satisfied coverage clause has a literal physical witness.
`square`

The argument does not assume a connected quotient factor or nonzero voltage.
Those remain external gates, but they are irrelevant to local target-orbit
coverage.

## 4. Exact marker-58 size

The authenticated catalogue gives:

```text
summary variables                         11,440
pair variables                            40,040
total variables                           51,480

edge-to-summary channel clauses           71,700
summary support clauses                   11,150
pair-definition clauses                  120,120
rank-11 coverage clauses                     728
total clauses                            203,698
```

There are 290 summary categories forced by at least one fixed edge and 1,218
categories with no available edge, for which the support row is a negative
unit.  The remaining support clauses are ordinary long disjunctions of
incident primary variables.

If appended to the independently verified compact-Horn v3 artifact, the
combined static census would be

\[
             \boxed{366131\text{ variables},
                     2037474\text{ clauses}}.           \tag{4.1}

This includes the v3 redundant 562-blocker bank and reversal WLOG row.

## 5. Propagation and interaction with residence

The module is entirely on undirected primary variables.  A selected edge
immediately forces its exterior summary at both endpoints.  Two different
summaries force their `Q`; conversely a unit coverage clause forces a `Q`,
then its two summaries, then the support rows require incident edge providers.

The compact residence v3 module shares the same primaries but uses directed
darts and the inside-owner boundary states `B,R1,R2`.  There is no collision:

* rank-11 summaries record coordinates **outside** the middle owner;
* residence states record coordinates **inside** the owner.

Thus the modules compose conjunctively, and any rank-11 propagation into the
edge factor immediately becomes available to residence propagation after an
orientation is chosen.  No additional history product is required.

Rank 12 does not share this collapse: a four-owner union can contain three
new exterior labels whose compatibility depends on a length-three walk, not
one undirected turn.  It is intentionally left separate.  The same applies
to source/compiler incidences.

## 6. Audit

The independent geometry/count source is

```text
scratch/audit_k17_rank11_turn_summary_module_20260802.cpp
SHA256 23bf8b427716daf843f9f4c412faa0de8621c73db8886f5180056727ae573160
```

It reads the frozen v3 arc/state map, independently recovers each undirected
edge's exterior coordinate in both owner frames, reconstructs all 11,440
supports and all 40,040 pairs, and verifies 728 target orbits with exactly 55
providers each.  The H100 audit root is

```text
/home/amodo/or15/work/root_k17_rank11_turn_summary_20260802
```

This is a static exactness/census audit, not a SAT or UNSAT result.

The retained output has SHA256
`5f572de97e624ed97c84fe551e7f30b93265ea1ee18e89d055e0e76094996730`.

## 7. Frozen append build

The fail-closed append builder

```text
scratch/build_k17_compact_horn_v3_rank11_20260802.cpp
```

copied the independently verified compact-Horn v3 CNF/map as an exact prefix,
then appended the summary/support rows, pair definitions and 728 target rows.
Thus the existing canonical blocker bank and WLOG row remain inside the
prefix and are not regenerated or reordered.

Before independent replay and before any solver launch, the frozen artifact
is

```text
/home/amodo/or15/work/root_k17_compact_horn_v3_rank11_20260802/
p cnf 366131 2037474
CNF SHA256 8df50578978ad83704e14f9a7e69d7ede956bcadd41df36fda4a7f16b50bcfc8
map SHA256 73a8f94f2a0249c29ba599bd832a3d173d5e00ed773b3e610761e610600ca5dd
builder SHA256 e61aeae5ade4f2d4975b5ff10190998ceb2d6df81b025090ed65504f34f41cdd
```

The appended map rows explicitly name every `(owner,outside-coordinate)`
summary and every `(owner,unordered-pair,target-orbit)` variable.  Rank 12
and all downstream gates remain excluded.

Independent V2 stream replay then passed with no builder correction.  It
replayed the 1,833,776-clause/110,484-row v3 prefix, checked that the terminal
WLOG unit remained `204168`, and independently regenerated all 203,698 new
clauses and 51,480 new map rows.  All 283,050 positive and 243,738 negative
synthetic truth controls passed.  The independent root is

```text
/home/amodo/or15/work/qa_k17_compact_horn_v3_rank11_stream_replay_20260802_quotientaudit
source SHA256 7b56dffc8ed3abf127cbbe5a9aa5f4e02194192c4fdeffabe4ceeb88ef2c9416
audit SHA256  f058dd39973ef9fb3f222840885cb7cb852823bd9238c949149b26fb39ff39b8
```

The combined artifact is therefore solver-eligible.  No solver was launched
during construction or audit.
