# `k=14`: edge-orbit catalogue, exact path formulation, and linear compiler

Date: 2026-07-27

## 1. The physical catalogue and its quotient

Put

\[
V=\binom{[14]}7.
\]

Every edge of `J(14,7)` is uniquely a chain

\[
X\subset U,qquad |X|=6,quad |U|=8.
\]

Indeed, if `U\X={a,b}`, the endpoints are `X+a` and `X+b`.  Thus

\[
|E|=\binom{14}{6}\binom82=3003\cdot28=84084,
\]

which also equals `|V|*49/2`.

Let `rho` rotate the fourteen coordinates and let `c` complement both
endpoints, equivalently

\[
c(X,U)=(U^c,X^c).
\]

The exact exhaustive quotient under `<rho,c>` is:

| physical object | count |
|---|---:|
| chains / Johnson edges | 84,084 |
| quotient orbits | **3,024** |
| orbits of size 28 | 2,982 |
| orbits of size 14 | 42 |

The exceptional 42 split into:

* 10 orbits whose pure translation orbit has size 7 and whose complement
  doubles it;
* 32 translation orbits of size 14 which are self-complementary up to a
  shift.

The complete machine-readable catalogue is
`scratch/k14_edge_orbit_catalogue.json`.  Every one of its 3,024 records
contains its representative, orbit size, stabilizer flags, and every
physical member in the format

```text
[lower rank-6 colour, upper rank-8 colour, endpoint 1, endpoint 2].
```

The generator independently checks that every canonical bucket equals the
full group orbit.  Its SHA-256 is

```text
f1a4b2a4da07723f303cab296253f78f2bdb9dbb132ac53cfb59b011101ecb2a
```

### Why this is compression, not an equivariance assumption

On the rank-seven vertices the same group has orbit distribution

\[
2^1,\ 14^9,\ 28^{118}.
\]

In particular there is one alternating orbit of size two.  A translation-
invariant Hamilton cycle is impossible: an order-fourteen automorphism of a
cycle is a rotation and all of its vertex orbits have the same size.  A
translation-invariant Hamilton path is impossible a fortiori, since a path
has no automorphism of order fourteen.

Therefore a quotient solver must retain physical phases or member variables.
One integer `z_O` per orbit records only how many members are chosen and
does not determine vertex degrees.  Imposing `x_e` constant on an orbit
would delete the desired object from the search space.

## 2. Exact audit of the known 260-defect word

For the 3,434-entry word
`k14_pinnable_factor_missing260.txt`, let

\[
T=D^2A.
\]

The exact audit gives:

* `T` has length 3,432 and is a bijection onto `V`;
* all 3,431 consecutive pairs are Johnson edges;
* the endpoints have symmetric difference ten, so the path does **not**
  close to a Johnson cycle;
* all 3,003 lower `q=1` colours and all 3,003 upper `q=1` colours occur.

The two `q=1` load distributions are

\[
\begin{array}{c|rrrr}
\text{load}&1&2&3&4\\ \hline
\text{rank 6}&2589&400&14&0\\
\text{rank 8}&2598&383&21&1.
\end{array}
\]

The selected 3,431 edges occupy 2,023 of the 3,024 catalogue orbits, with
orbit-selection multiplicities

\[
1^{1056},2^{633},3^{248},4^{70},5^{11},6^5.
\]

An exhaustive contiguous-OR scan confirms the definitive defect

\[
238\text{ rank-nine masks}+22\text{ rank-ten masks}=260.
\]

The fixed central rows alone have 238 rank-nine and 31 rank-ten holes; nine
of the latter are supplied by longer upper rows.  Thus central `q=3`
coverage is a useful sufficient proxy but is strictly stronger than the
actual word objective.

## 3. Exact degree/path formulation

Use one binary variable `x_e` for every physical catalogue edge and one
binary endpoint flag `b_v` for every `v in V`.  A spanning Hamilton path is
described by

\[
\sum_v b_v=2,
\qquad
\sum_{e\ni v}x_e=2-b_v,
\tag{3.1}
\]

together with connectedness cuts

\[
\sum_{e\in\delta(S)}x_e\ge1
\quad(\varnothing\ne S\subsetneq V).
\tag{3.2}
\]

The complete `q=1` constraints are

\[
\sum_{e:\,e_\cap=X}x_e\ge1
\quad\left(X\in\binom{[14]}6\right),
\qquad
\sum_{e:\,e_\cup=U}x_e\ge1
\quad\left(U\in\binom{[14]}8\right).
\tag{3.3}
\]

For `q=2`, introduce `y_{u,v,w}` for each length-two Johnson path and impose

\[
y\le x_{uv},\quad y\le x_{vw},\quad
y\ge x_{uv}+x_{vw}-1.
\tag{3.4}
\]

Then exact central upper coverage is

\[
\sum_{u\cup v\cup w=R}y_{u,v,w}\ge1
\quad\left(R\in\binom{[14]}9\right).
\tag{3.5}

Length-three variables give the analogous rank-ten condition.  In a
degree-two connected graph the local successor pairing is unique, so these
variables encode chronology rather than an additional choice.

It is cleaner to solve the path directly.  If one instead solves a cycle and
cuts it, every `q=2` or `q=3` colour whose only witness crosses the cut is
lost.  A cycle certificate therefore needs either a cut variable with
surviving-witness constraints or multiplicity at least two for every colour
touching the chosen seam.

## 4. Exact linear residence and the fresh compiler

This is the key correction to the old cyclic compiler.  Let a proposed
middle **path** `T` have length `W` and let the desired word have length
`W+d`.  Its maximal linear erosion is

\[
P_i=\bigcap_{j=\max(0,i-d)}^{\min(i,W-1)}T_j,
\qquad 0\le i<W+d.
\tag{4.1}
\]

### Proposition 4.1

There is a set word `A` with `A_i subseteq P_i` and `D^dA=T` only if

\[
D^dP=T.
\tag{4.2}
\]

Conversely, (4.2) itself gives the set-valued preimage `A=P`; if normalized
nonzero entries are required, also require every `P_i` to be nonempty.

#### Proof

If `A_i` contributes to `T_j`, then `A_i subseteq T_j`, so `A_i subseteq
P_i`.  Hence

\[
T=D^dA\subseteq D^dP.
\]

The definition of `P` gives `D^dP subseteq T`, proving equality.  The
converse is immediate.  □

The executable `scratch/sigma_multirow_linear_compiler.py` first performs
this statewise test.  It then uses exact SAT to choose nonzero `A_i subseteq
P_i`, impose every missing middle-coordinate hit, and cover every mask below
rank seven in rows `A,DA`.  There is no cyclic wrap, no safe-cut assumption,
and no post-hoc appendix.

Calibration on the original path is SAT: 340,289 variables, 2,293,047
clauses, about one second of Kissat time, and exactly the old 260 upper
holes.

## 5. Cycle-space trades and the first genuine improvement

A 2-opt reversal removes path edges

\[
(T_i,T_{i+1}),\ (T_j,T_{j+1})
\]

and adds

\[
(T_i,T_j),\ (T_{i+1},T_{j+1}),
\]

which is symmetric difference with an alternating four-cycle in the
Johnson edge space.  For a `q=1` colour `c` of current load `ell_c`, the
move is safe exactly when

\[
\ell_c+\Delta_c\ge1
\tag{5.1}
\]

for every lower and upper colour.  All `q=2,3` changes are confined to the
two seams, so their load deltas are exact constant-size calculations.

The exhaustive one-move census around the old path is:

| class | count |
|---|---:|
| physical Johnson 2-opt moves | 7,838 |
| preserving both `q=1` covers | 382 |
| improving central upper `q=2,3` | 78 |
| exact linearly depth-two resident and improving | 13 |

The move `(i,j)=(1563,1880)` is linearly resident and reduces the **actual
full upper defect** from 260 to 258.  The fresh global compiler is SAT and
produces

```text
scratch/k14_linear_2opt_1563_1880_global.word
```

with SHA-256

```text
210a7827a80d0e8d3c6d9fc7b344c687c5d0ad9ae1a6fade9747f7ddb1521fd3
```

Independent exhaustive checks give:

* length 3,434;
* `D^2A` is exactly all 3,432 rank-seven masks once;
* every mask of rank at most eight occurs;
* the only misses are 236 rank-nine and 22 rank-ten masks.

Thus this is a genuine improvement of the fixed-length `k=14` core, not a
central-path proxy.

Putting the full compiler inside the descent loop improves it further.  At
each round the code:

1. enumerates `q=1`-safe 2-opt moves;
2. rejects every move failing `D^2P=T`;
3. orders the survivors by the actual full upper-tower defect;
4. accepts a move only after the 340,289-variable lower compiler returns
   SAT.

Four further moves are accepted, with defects

\[
258\to256\to254\to252\to\boxed{251}.
\]

The next state has five improving resident 2-opt moves, but every one is
compiler-UNSAT.  Thus 251 is an exact local minimum for this 2-opt move
class, not merely a greedy central score.  The certified word is

```text
scratch/k14_compilable_descent.word
```

with SHA-256

```text
5f49ac3cb0e136e0e41f826a930caf8f48e27a82a4294989e5fc0603b4399ff7
```

It misses exactly 229 rank-nine and 22 rank-ten masks, while every rank at
most eight remains complete.

### Larger moves and completion

At the 251 state there are five individually improving, exact-resident
2-opt moves, all compiler-UNSAT.  Exhausting the proposed two-move escape
does not help: the five intermediate states generate 189 distinct
q1-safe, exact-resident two-move paths with final defect below 251 (the best
have defect 248), and the full compiler returns UNSAT on all 189.

A genuine three-edge block transposition does escape.  The exact census from
251 is

\[
49{,}661\text{ Johnson reconnections}
\to463\text{ q1-safe}
\to70\text{ resident}
\to2\text{ improving},
\]

and both improving paths compile.  Repeating once gives a second compilable
move.  The resulting core has

\[
\boxed{249}=227\text{ rank-nine}+22\text{ rank-ten}
\]

holes.  The next block-transposition round has one 248 candidate, but its
lower compiler is UNSAT.

Starting with the known 242-entry completion suffix, a deterministic
delete-one/edit-one repair compresses the suffix to 234 entries.  The next
234-to-233 step exhausts its bounded class with no repair.  The resulting
universal word has length

\[
3434+234=\boxed{3668}.
\]

It is

```text
scratch/k14_249_complete_3668_oneedit.word
```

with SHA-256

```text
2bab8941bd66305050cdcc4d1244fcc20cecc5412c656a4ead0b187e3a463e26
```

Both independent C++ verifiers report `covered=16383/16383, missing=0`.
Thus the certified upper bound at this snapshot is

\[
\boxed{\nu(14)\le3668}.
\]

## 6. Two bounded obstructions now separated cleanly

### Old-word reversal is too rigid

Among all 7,838 central 2-opt moves, only 32 induced reversals

\[
A[i+1:j+3]\longmapsto\operatorname{rev}(A[i+1:j+3])
\]

preserve exact central ownership.  Only one of those keeps every previously
covered lower/`q=1` rank without increasing the total defect, and it leaves
the defect exactly 260.  No move in this literal lift class improves the
word.  Fresh compilation is therefore essential.

### Rank-correct intersections are not residence

An earlier 74-move descent preserved the weaker statement that every
three-middle-window intersection has rank five and reached central defects
167 and 11.  Proposition 4.1 rejects it statewise: its maximal erosion has

\[
139
\]

middle failures.  No length-3,434 depth-two word can realize that path.

After replacing that test by `D^2P=T`, a corrected greedy descent accepts 17
moves and reaches central defects 218 and 26.  Every prefix is resident, but
the full lower compiler is SAT only at prefixes 0, 1, and 2 on that greedy
route; prefixes 3 through 17 are UNSAT.  Prefix 2 again gives an actual
258-defect word.  This separates two genuinely different gates:

1. **residence:** the statewise maximal-erosion equality;
2. **lower ideal:** simultaneous SAT realization of all 6,475 lower masks.

Neither may be replaced by rank arithmetic alone.

## 7. Reproduction

```bash
python3 scratch/audit_k14_cycle_space.py

python3 scratch/search_k14_central_2opt.py

python3 scratch/sigma_multirow_linear_compiler.py \
  --source-word k14_pinnable_factor_missing260.txt \
  --two-opt 1563 1880 --k 14 --depth 2 \
  --output-word scratch/k14_linear_2opt_1563_1880_global.word

python3 scratch/search_k14_central_2opt_descent.py \
  --output scratch/k14_central_2opt_resident_descent.certificate.json

python3 scratch/compile_k14_resident_prefixes.py

python3 scratch/search_k14_compilable_descent.py

python3 scratch/search_k14_compiler_pair_moves.py \
  --compile-limit 200

python3 scratch/search_k14_block_transposition.py

python3 scratch/search_k14_append241_oneedit.py \
  scratch/k14_block_transposition_249.word \
  scratch/k14_249_append235_oneedit.txt --k 14
```

The present verdict is positive but narrow: the quotient catalogue is
correct, simple central trades contain real upper improvement, and the new
linear compiler can realize some of it.  The old 260-defect object was not a
local minimum once the compiler was allowed to move globally.  On the other
hand, residence and lower compilation reject most of the much larger
central-only gains, so a quotient SAT that omits either gate would optimize
the wrong object.
