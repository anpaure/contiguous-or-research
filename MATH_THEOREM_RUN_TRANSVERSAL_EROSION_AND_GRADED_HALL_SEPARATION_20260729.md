# Run-transversal erosion and the exact graded-Hall separation

Date: 2026-07-29

Status: unconditional structural theorem, one physical counterexample to an
automatic compiler implication, and a solver-free exhaustive census at
`k=5,7`.  This note does not change the current bound at `k=15` and is not
inserted into the shared handoff.

## 1. Binary-trace setup

Let

\[
 k=2m+1,\qquad r=m+1,\qquad W={k\choose r},\qquad N=W/k,
\]

and let `rho` be addition by one on `Z_k`.  A unit-voltage binary trace is
a cyclic word `c in {0,1}^Z_W` with

\[
 T_i=\{x\in\mathbb Z_k:c_{i-xN}=1\}.                 \tag{1.1}
\]

Assume:

1. every residue class modulo `N` contains exactly `r` ones;
2. the starts of the cyclic one-runs of `c` meet every residue class modulo
   `N` exactly once, and their ends do the same; and
3. every cyclic one-run has length at least `d+1`.

The first condition gives `|T_i|=r`.  At the transition `i -> i+1`, an
entering coordinate is exactly a `01` boundary of `c` whose left endpoint
is congruent to `i` modulo `N`, and a leaving coordinate is exactly a `10`
boundary in that residue class.  The two transversality conditions therefore
give exactly one entry and one exit at every transition.  Thus `T` is a
Johnson walk and

\[
 T_{i+N}=\rho T_i.                                     \tag{1.2}
\]

No Hamilton or shadow-coverage hypothesis is used below.

## 2. The complete erosion tower

For `0 <= q <= d`, put

\[
 I_i^{(q)}=\bigcap_{a=0}^{q}T_{i-a}.                    \tag{2.1}
\]

Write the Johnson transition as

\[
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.                \tag{2.2}
\]

### Theorem 2.1 (all shallow intersections are exact Johnson walks)

For every `0 <= q <= d`:

\[
 |I_i^{(q)}|=r-q,                                      \tag{2.3}
\]

and consecutive states of `I^(q)` are Johnson-adjacent.  More precisely,

\[
 I_i^{(q)}\setminus I_{i+1}^{(q)}=\{\alpha_i\},\qquad
 I_{i+1}^{(q)}\setminus I_i^{(q)}=\{\beta_{i-q}\}.     \tag{2.4}
\]

Moreover

\[
 I_{i+N}^{(q)}=\rho I_i^{(q)}.                         \tag{2.5}
\]

#### Proof

Consider the `q` transitions from `T_(i-q)` through `T_i`.  Their deleted
coordinates are distinct.  Otherwise a coordinate would have to be
reinserted and deleted again while occupying at most `q <= d` consecutive
carrier states, contradicting the minimum one-run length `d+1`.  Every one
of these deleted coordinates was already in `T_(i-q)`: a coordinate first
inserted inside the block and deleted before its end would again have a
positive run of length at most `q`.  Consequently

\[
 I_i^{(q)}
 =T_{i-q}\setminus\{\alpha_{i-q},\ldots,\alpha_{i-1}\},
\]

which proves (2.3).

When the window moves one step, `alpha_i` is present throughout the old
window and absent from the new endpoint.  Conversely `beta_(i-q)` is absent
just before the new window and remains present throughout it.  These two
coordinates are distinct: equality would be a run beginning at transition
`i-q` and ending at transition `i`, of length `q <= d`.  All other
coordinates have the same membership in the two intersections.  This proves
(2.4).  Finally (2.5) follows from (1.2), since rotation commutes with
intersection.  \(\square\)

There is an equivalent trace proof: replacing every one-run of `c` of
length `ell` by length `ell-q` gives the trace of `I^(q)`.  With the
end-indexed convention (2.1), a run `[a,b]` becomes `[a+q,b]`: starts are
translated uniformly by `+q` and ends remain fixed.  (For the forward-window
convention `T_i cap ... cap T_(i+q)`, starts remain fixed and ends translate
by `-q`.)  Either convention preserves both residue transversals, so the
eroded trace is itself run-transversal.

### Corollary 2.2 (the maximal erosion controller)

Put

\[
 h=r-d,\qquad P_i=I_i^{(d)}.
\]

Then `P` is a rank-`h`, unit-voltage equivariant Johnson walk.  With
`(DX)_i=X_i union X_(i+1)`, one has, pointwise,

\[
 D^jP_i=I_i^{(d-j)},\qquad |D^jP_i|=h+j
 \quad(0\le j\le d).                                  \tag{2.6}
\]

Indeed (2.4) implies

\[
 I_i^{(q)}\cup I_{i+1}^{(q)}=I_i^{(q-1)},
\]

and iteration proves (2.6).  Thus the exact ranks and Johnson chronology of
the full lower carrier tower are consequences of run transversality and
residence, not additional search gates.  Coverage of those ranks remains a
separate property.

## 3. What terminal coverage does not buy

A one-core of `P` is a word `C <= P` satisfying `DC=DP`.  Such a core always
exists (`C=P`), so core existence alone has no content.  The graded compiler
additionally needs a matching of every target

\[
 \mathcal S_h=\{S:1\le |S|\le h\}
\]

to distinct cyclic positions with

\[
 C_i\subseteq S\subseteq P_i.                          \tag{3.1}
\]

Terminal coverage `set(P) superseteq binom([k],h)` guarantees positive
envelope degree for the rank-`h` targets.  It says nothing about the total
Hall capacity or about the simultaneous stable-omission constraints needed
for smaller targets.

### Theorem 3.1 (a physical strict-spiral counterexample at `k=9`)

There is a strict equivariant carrier with

\[
 (k,r,d,h,W,N)=(9,5,2,3,126,14)
\]

which satisfies all of the following:

* it is a Hamilton Johnson cycle on the rank-five layer;
* its voltage is `4`, hence a unit modulo `9`;
* its minimum coordinate residence is `3=d+1`;
* its first lower shadow is exact;
* its terminal erosion `P` contains every rank-three target;
* `DP` contains every rank-four target; and
* its cyclic interval unions contain every target above rank five.

Nevertheless no one-core of this `P` has a graded Hall matching.  In fact
this is independent of the core:

\[
 |\mathcal S_3|
 ={9\choose1}+{9\choose2}+{9\choose3}
 =9+36+84=129>126=W.                                  \tag{3.2}
\]

The shore consisting of all low targets has Hall deficiency at least three.
Even the `d=2` appended linear collar gives only `W+d=128` source letters,
so a literal-base-row compiler remains short by one.  The known optimal word
escapes by placing one rank-three target in derivative row one.  Hence this
is a counterexample only to the automatic **graded one-core** implication,
not to `nu(9)=B(9)` or to the multirow compiler.

The fixture is the independently verified word of SHA-256

```text
0f282a2c5bb61c0ea48d49c5966eafba3ceb8a30cc40150a92764c1321c21b7c
```

whose middle carrier is `D^2A`.  It is embedded in the companion audit, so
the result does not depend on a mutable external file.

## 4. Exact tiny census

The companion solver-free audit enumerates all run-transversal trace states
at `k=5,7`, modulo cyclic translation.  It then checks Hamiltonicity, exact
first lower shadow, terminal erosion coverage, every upper cyclic interval,
and all equivariant one-core state cycles followed by physical Hall.

Its exact output is:

```text
k=5: 1 run-transversal state; 0 decorated carriers (Hamilton fails).
k=7: 195 run-transversal states; 2 decorated carriers; both admit an
     equivariant one-core with a 28/28 physical Hall matching.
k=9 fixture: every carrier gate passes; graded Hall is at most 126/129.
```

Thus the first failure is not a mysterious local core conflict: it is the
known `k=9` literal-row capacity boundary.  At `k=7`, where

\[
 {7\choose1}+{7\choose2}=28<35=W,
\]

every decorated trace in the exhaustive tiny census compiles through an
equivariant one-core.  This positive finite fact is not an all-`k` theorem.

Reproduction:

```sh
python3 scratch/audit_erosion_hall_gate_tiny_20260729.py
```

## 5. Exact conclusion for the compiler gate

The implications are therefore:

\[
 \text{run-transversal + residence}
 \Longrightarrow
 \text{exact-rank equivariant Johnson erosion tower},
\]

but

\[
 \text{all carrier shadows + terminal `P` coverage}
 \not\Longrightarrow
 \text{compiler-ready one-core/Hall pair}.
\]

For the graded route, the exact additional statement is still the stable
omission cycle plus physical Hall (or its weighted quotient form).  Outside
the literal-row capacity range, a multirow compiler is logically necessary;
no strengthening of terminal carrier coverage can remove that arithmetic
fact.
