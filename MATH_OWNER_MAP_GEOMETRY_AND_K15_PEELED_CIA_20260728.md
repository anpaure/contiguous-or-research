# Owner-map geometry, the Hall-only counterexample, and the peeled k=15 CIA channel

Date: 2026-07-28

## 1. Verdict

The normalized optimal words do not come from an ordinary Hall matching or
from a canonical SCD-local owner rule.  Both obvious constructions fail for
small exact reasons:

* an ordinary row-major maximum matching is already globally unrealizable at
  `k=7`, on three targets and two positions; and
* only 16--26% of the normalized owners through `k=14` use their canonical
  Greene--Kleitman middle owner.

The positive conclusion is at `k=15`.  Degree-one peeling of the frozen
Hall-29 DM graph removes 1489 forced owner pairs in three perfectly graded
rounds and leaves an exact `35 targets / 6 cells` residual, still of
deficiency 29.  Freezing those forced owners and allowing only baseline
defect-at-most-one repairs gives a proof-safe positive architecture with
only 4057 fixed-target options.  It uses no target selectors, target-bit
variables, or target `AddElement` constraints.

This is not a Hall-zero proof.  It is a substantially smaller exact search
lane whose SAT solutions are genuine DM-shore matchings.

## 2. The obvious Hall rule fails at k=7

For a fixed middle row `T` and maximal erosion `P`, a target `X` is locally
eligible for a short cell `J` when

\[
 M_J\subseteq X\subseteq E_J:=\bigcup_{p\in J}P_p,
 \qquad P_p\cap X\ne\varnothing\quad(p\in J),            \tag{2.1}
\]

where `M_J` is the complete-carrier mandatory core.  The raw word gives a
perfect matching in this graph.  It is tempting to take an arbitrary perfect
matching and invoke the full-witness theorem afterwards.

That implication is false.  In the normalized `k=7` word, row-major
Hopcroft--Karp chooses the three locally valid and cell-distinct pairs

\[
  7\mapsto[1,2],\qquad 1\mapsto[1],\qquad4\mapsto[2].    \tag{2.2}
\]

Here masks use zero-based bits.  The two singleton owners omit coordinate
one, so their negative windows forbid that coordinate at positions one and
two.  Consequently the assigned interval for mask `7={0,1,2}` realizes
only mask `5={0,2}`.

Thus the static candidate graph has a complete matching but the assignment
violates the global coordinate criterion.  This is a three-target exact
counterexample to each of the following rules:

1. arbitrary Hall matching;
2. row-major Hall matching;
3. independent per-target choice of a locally admissible cell.

The same deterministic rule has the following failures on the raw-derived
fixed points:

| `k` | static candidate edges | bad assigned targets | damaged middle cells |
|---:|---:|---:|---:|
| 6 | 35 | 0 | 0 |
| 7 | 127 | 6 | 1 |
| 8 | 204 | 4 | 1 |
| 9 | 637 | 9 | 3 |
| 10 | 1261 | 18 | 6 |
| 11 | 3105 | 46 | 13 |
| 12 | 7656 | 121 | 50 |
| 13 | 19342 | 246 | 40 |
| 14 | 51648 | 700 | 282 |

This reconciles the successful static Hall audits with the need for the
subsequent compiler SAT: Hall controls distinct cells, while negative-window
blocking controls simultaneous realizability.

## 3. Why a standard SCD owner rule also fails

For each lower target `X`, compute its canonical Greene--Kleitman rank-`r`
owner `g(X)`.  If `X` is realized on the short cell `[s,s+h]`, then its
physical central owners are exactly the middle windows with starts

\[
  \max(0,s+h-d)\le i\le\min(s,W-1).                      \tag{3.1}
\]

Call the assignment SCD-native if `g(X)=T_i` for one of these starts.

| `k` | native | exported | native fraction |
|---:|---:|---:|---:|
| 6 | 10 | 11 | 0.476 |
| 7 | 24 | 39 | 0.381 |
| 8 | 34 | 58 | 0.370 |
| 9 | 65 | 190 | 0.255 |
| 10 | 77 | 308 | 0.200 |
| 11 | 203 | 820 | 0.198 |
| 12 | 348 | 1237 | 0.220 |
| 13 | 650 | 3445 | 0.159 |
| 14 | 1101 | 5374 | 0.170 |

The optimal compilers globally rematch most lower targets away from their
canonical SCD owner.  This is stronger empirical behavior than the proved
SCD-local overload theorem: that theorem forces at least

\[
 E_{k,d}-\binom{d+1}{2}
\]

exports, while the actual normalized maps export a much larger majority.
There is therefore no contradiction.  The raw solutions evade the theorem
by doing exactly what it says a successful compiler must do: bulk nonlocal
pin rematching, not seam-local SCD repair.

## 4. Containment cores and negative-window sparsity

The owner map is nevertheless highly structured.

1. Every owner through `k=14` lies in its nominal rank row or one row later,
   apart from the small boundary ramp.
2. The containment core `M_J` is usually close to its target, but it does not
   determine it.  At `k=14`, only 70 of 6475 owners have target equal to the
   core; 2946 have target rank three above the core.
3. At the canonical fixed point, every omitted erosion incidence is explained
   by a selected negative interval.  Suppression multiplicity stays tiny:

| `k` | omitted incidences killed once | twice | three times |
|---:|---:|---:|---:|
| 6 | 8 | 0 | 0 |
| 7 | 10 | 2 | 0 |
| 8 | 12 | 0 | 0 |
| 9 | 54 | 6 | 0 |
| 10 | 67 | 0 | 0 |
| 11 | 80 | 3 | 2 |
| 12 | 393 | 0 | 0 |
| 13 | 498 | 32 | 0 |
| 14 | 1721 | 422 | 0 |

So the compiler is global in *where* targets move but sparse in the final
coordinate dependencies.  This suggests conflict-directed owner repair,
not SCD-chain allocation and not independent matching.

## 5. Exact one-owner CIA encoding for a fixed carrier

For every locally eligible pair `(X,J)`, introduce one owner Boolean
`y_XJ`.  Impose one owner per target and at most one target per cell.  For
each source position and coordinate introduce `z_px`, meaning that the
coordinate survives all selected negative windows at that position.

The exact fixed-carrier conditions are

\[
 y_{XJ}=1, x\notin X, p\in J\Longrightarrow z_{px}=0,  \tag{5.1}
\]

\[
 y_{XJ}=1, x\in X\Longrightarrow
       \sum_{p\in J}z_{px}\ge1,                         \tag{5.2}
\]

and

\[
 sum_{p=i}^{i+d}z_{px}\ge1\qquad(x\in T_i).           \tag{5.3}
\]

Together with `z_px=0` for `x\notin P_p` and nonzero source positions,
these are exactly the fixed-middle CIA conditions.  There is one sparse
owner variable per candidate edge, not one target selector per physical
cell.

For the Hall-29 carrier the complete lower graph has only 133,534 candidate
edges.  The canonical DM shore alone has:

```text
1524 targets
1495 neighbouring cells
6322 candidate edges
96,570 position-coordinate blocker variables
161,443 negative-owner implications
35,525 positive-owner constraints
51,480 middle-carrier constraints
```

The fixed carrier cannot be layered with CIA because it already fails the
ordinary matching gate by 29.  Equations (5.1)--(5.3) become relevant only
after a carrier edit reaches Hall zero.

## 6. Degree-one peeling exposes the true Hall-29 kernel

In a bipartite matching instance, if a live target has a unique live cell and
no other live degree-one target demands that same cell, the edge is forced in
every saturating matching.  Remove the target and cell and repeat.  This
preserves matching feasibility and deficiency exactly.

On the canonical Hall-29 shore the peeling is perfectly rank graded:

| round | forced pairs | target rank | cell depth | colliding singleton cells |
|---:|---:|---:|---:|---:|
| 1 | 1013 | 7 | 2 | 6 |
| 2 | 395 | 6 | 1 | 6 |
| 3 | 81 | 5 | 0 | 6 |

Thus 1489 of the 1524 owners are forced.  The residual is

\[
 \boxed{35\text{ targets},\quad6\text{ live cells},\quad
        35-6=29.}                                       \tag{6.1}
\]

Its rank profile is

\[
 4^9\,5^1\,6^{17}\,7^8.
\]

The six live cells are all depth two.  Each is the sole live option of one
rank-six and one rank-seven target, so the current residual has twelve edges
arranged as six forced collisions; the other 23 targets have residual degree
zero.

This 35/6 object is a **conditional matching kernel**, not an unconditioned
35-target Hall shore.  The 1489 deleted cells may also neighbor residual
targets in the original graph.  Therefore one must not claim that the plain
35-target neighborhood has size six.  The kernel is exact only after the
1489 forced owner reservations are retained.

## 7. A 4057-option positive carrier architecture

Freeze the 1489 peeled owner pairs.  Exclude their cells.  For each residual
target retain every other physical cell whose Hall-29 candidate defect is at
most one, where

\[
 \delta(X,J)=|X\setminus E_J|+|M_J\setminus X|
 +|\{p\in J:P_p\cap X=\varnothing\}|.                   \tag{7.1}

This gives:

```text
35 residual targets
4057 target-cell options
3183 distinct option cells
12 currently exact options
3807 missing-one options
238 mandatory-one options
```

The seven original zero-candidate targets alone have 197 defect-one options;
each has minimum defect exactly one.

On a dynamically selected carrier, recompute the full exact predicate (2.1)
for every frozen pair and selected option.  Require one option per residual
target and at most one residual target per cell.  Any satisfying carrier then
contains the explicit matching

\[
 1489\text{ frozen pairs}+35\text{ residual pairs}
\]

of the complete 1524-target DM shore.  This is a proof-safe positive
certificate.  It is sufficient-only because a valid repair might change a
frozen owner or require a baseline defect-two option.

The channel has 4057 guarded owner Booleans and 93,687 fixed-mask fit clauses
(26,245 frozen and 67,442 guarded).  It has zero target selectors, zero
target-bit variables, and zero target `AddElement` constraints.  It can be
placed on the existing exact 19,311-cell global order channel.

This is materially smaller than the unrestricted fixed-shore consumer whose
single pair run reached roughly 130 GiB RSS.

## 8. Artifacts

Raw owner geometry:

```text
scratch/analyze_raw_fixedpoint_owner_geometry.py
SHA-256 442de70fae1dff0e62ee0bbd87adf1a40e359d6a45b28d3b160ebc64afa6794f

scratch/raw_fixedpoint_owner_geometry_audit.json
SHA-256 281130c16e155e5835f660296f6964df21f9face90d8b39d060542f32f1565b2
```

Hall-29 peeling and option atlas:

```text
scratch/analyze_k15_h29_one_owner_cia.py
SHA-256 23bfb126ae1b61f4023b32bd9295096687aa5069011fe594fb2d70d756848de3

scratch/k15_h29_one_owner_cia_audit.json
SHA-256 721a67896e5f992945cb0adabcb47fff94cdfe1c2d993b347270b03a1b7f35f4
```

CP-SAT channel:

```text
scratch/k15_compact_owner_channel.py
SHA-256 2b56ee60b3cebc77b4b8b0c1bdf9e0bf661f9623275c10cbd6b994d56d52e54d
```

Call

```python
add_compact_owner_architecture(model, order_channel, audit_path)
```

after constructing
`add_compact_order_channel(..., global_compiler=True)`.

