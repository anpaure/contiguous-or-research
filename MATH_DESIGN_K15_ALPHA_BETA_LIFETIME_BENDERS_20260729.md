# Exact `alpha/beta` lifetime master and compiler decomposition at `k=15`

Date: 2026-07-29

Status: exact finite formulation and search design.  The representation is
proved equivalent to the strict-spiral run-transversal normal form and has
been replayed exactly on the authoritative resident `k=15` seed.  It does
**not** produce a new `k=15` word by itself.

Reproducible audit:

```text
scratch/audit_k15_alpha_beta_lifetimes_20260729.py
scratch/k15_alpha_beta_lifetime_audit_20260729.json
```

## 1. Parameters and event notation

At `k=15` put

\[
 r=8,\qquad d=3,\qquad W={15\choose8}=6435,\qquad N=W/15=429.
\]

Let `T_i` be a cyclic Johnson carrier and orient edge `i` from `T_i` to
`T_(i+1)`.  Write

\[
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.
\tag{1.1}
\]

For a strict spiral of unit voltage `v`, it is enough to store the quotient
symbols

\[
 a_j=\alpha_j,\qquad b_j=\beta_j\qquad (j\in\mathbb Z_N),
\]

because at physical edge `j+sN`

\[
 \alpha_{j+sN}=a_j+sv,\qquad
 \beta_{j+sN}=b_j+sv\pmod k.
\tag{1.2}
\]

Thus the physical deletion/insertion chronology has only `2N=858`
finite-domain decisions, rather than `W=6435` unconstrained binary trace
decisions.  A unit voltage may be gauged to `v=1`, also for composite
`k=15`.

## 2. Exact lifetime theorem

For each quotient insertion orbit `j`, follow the inserted coordinate until
its next deletion.  Call the number of carrier states in that positive run
`ell_j`.  Equivalently, if `h=j+ell_j` is unwrapped, then

\[
 a_{h\bmod N}+\left\lfloor h/N\right\rfloor v=b_j\pmod k.
\tag{2.1}
\]

### Theorem 2.1 (event/lifetime equivalence)

The quotient data `(a,b)` lift to a cyclic rank-`r` strict Johnson trace if
and only if:

1. `a_j != b_j` for every `j`;
2. on one (equivalently every) coordinate, deletion and insertion events
   alternate cyclically;
3. matching every insertion to the next deletion induces a permutation of
   the `N` deletion orbits; and
4. `sum_j ell_j = rN`.

The carrier is residence-legal at depth `d` if and only if

\[
                         \ell_j\ge d+1\quad\hbox{for every }j.
\tag{2.2}
\]

Under these conditions the carrier is reconstructed uniquely.

#### Proof

Alternation uniquely determines the binary incidence trace of each
coordinate.  Equation (1.2) makes all coordinate traces translates, so it
is enough to check coordinate zero.  There is one insertion orbit over each
edge residue.  The deletion-orbit permutation gives one deletion orbit over
each residue.  Hence every physical edge deletes exactly one coordinate and
inserts exactly one different coordinate, so rank is constant.  The total
coordinate-zero occupation is `sum ell_j`; equivariance therefore makes the
constant rank `(sum ell_j)/N`, which is `r` exactly in (4).  Conversely a
strict Johnson trace has alternating events, uniquely matched next
deletions, and the incidence count gives (4).  A positive coordinate run of
length `ell_j` is precisely its residence interval, proving (2.2).  □

The matching in this theorem should **not** be represented by `N^2`
Boolean variables.  It is the deterministic next-deletion matching and is
audited in linear time.

## 3. A still smaller run-schedule master

The `alpha` symbols can be derived, so the minimal useful decision form has
only a start sheet and a lifetime for each run.

Let `u_j in Z_k` and define the physical edge on which coordinate zero is
inserted by run `j` as

\[
                         s_j=j+Nu_j.
\tag{3.1}
\]

In the `(a,b)` convention,

\[
                  u_j=-b_jv^{-1}\pmod k.
\tag{3.2}
\]

The coordinate is present in states

\[
                 s_j+1,s_j+2,\ldots,s_j+\ell_j\pmod W.
\tag{3.3}
\]

The following constraints are exact:

1. the `N` cyclic arcs (3.3) are pairwise disjoint and successive arcs have
   at least one zero state between them;
2. `ell_j >= d+1`;
3. `sum ell_j = rN`;
4. the end residues
   
   \[
                     \pi(j)=j+\ell_j\pmod N
   \tag{3.4}
   \]
   
   are all different.

The start residues are automatically all different because `s_j mod N=j`.
Condition (3.4) is exactly the deletion-transversal condition.  If
`e_j=s_j+ell_j` and `q_j=floor(e_j/N) mod k`, then deletion symbols are
derived by

\[
                  a_{e_j\bmod N}=-q_jv\pmod k.
\tag{3.5}
\]

This is the run-transversal `c`-space normal form expressed without the
`W` raw bits.  The binary trace is recovered by setting `c_p=1` precisely
on the arcs (3.3), and

\[
 x\in T_i\quad\Longleftrightarrow\quad
 c_{i-xv^{-1}N}=1.
\tag{3.6}
\]

### Best compact form: two cyclic compositions

There is no need even for `NoOverlap`.  Index the coordinate-zero runs in
their physical cyclic order, use time/coordinate rotation to put the first
insertion at edge zero, and let

```text
life[t] >= d+1     positive-run length
gap[t]  >= 1       zero-run length following it
pos[0]   = 0
pos[t+1] = pos[t] + life[t] + gap[t]
```

Then the exact CP-SAT skeleton is

```text
sum(life) = r*N
sum(gap)  = (k-r)*N
pos[N]    = W
startres[t] = pos[t] mod N
endres[t]   = (pos[t] + life[t]) mod N
AllDifferent(startres)
AllDifferent(endres)
```

This is just `429` positive lifetimes plus `429` positive gaps, two fixed-sum
composition constraints, and two `AllDifferent(429)` constraints.  Pairwise
disjointness, alternation, and the next-deletion matching are now true by
construction.

The event symbols are recovered without choices.  If run `t` starts at
`p=pos[t]`, put `j=p mod N` and `s=floor(p/N)`; then

\[
                         b_j=-sv\pmod k.
\tag{3.7}
\]

If it ends at `e=p+life[t]`, put `h=e mod N` and
`q=floor(e/N) mod k`; then

\[
                         a_h=-qv\pmod k.
\tag{3.8}
\]

This removes the explicit lifetime permutation **and** all interval
disjunctions.  It is substantially smaller in *decision dimension* than the
raw `c` model.  It is not automatically a smaller monolithic CNF once all
shadow membership literals are channelled; see Section 6.

## 4. What remains in the carrier master

The schedule constraints prove rank, Johnson adjacency, residence, and the
rank of the first lower shadow.  They do not prove orbit injectivity or
deeper coverage.  After reconstructing `T`, the exact carrier oracle checks:

1. the `N` middle representatives are pairwise rotation-inequivalent;
2. the `N` adjacent intersections are pairwise rotation-inequivalent;
3. the required lower window intersections (`q=2` eagerly at `k=15`, and
   the terminal depth in the compiler interface) cover their target orbits;
4. consecutive unions cover every upper target; and
5. at least one linear cut preserves every cyclic witness needed by the
   final path.

Residence makes the shadow evaluator especially cheap.  For `q<=d`,

\[
 \bigcap_{t=0}^{q}T_{i+t}
   =T_i\setminus\{\alpha_i,\ldots,\alpha_{i+q-1}\},
\tag{4.1}
\]

while for every `q`, without an extra hypothesis,

\[
 \bigcup_{t=0}^{q}T_{i+t}
   =T_i\cup\{\beta_i,\ldots,\beta_{i+q-1}\}.
\tag{4.2}
\]

Similarly, the interior depth-`d` erosion envelope is

\[
 P_i=T_i\setminus\{\beta_{i-d},\ldots,\beta_{i-1}\}.
\tag{4.3}
\]

Thus the expensive-looking window tower reduces to short deletion/insertion
prefixes once the run schedule is legal.  A C++ LNS can update these ledgers
only near changed run boundaries.

All checks are finite bit-mask audits.  Reconstructing the full physical
carrier costs `O(kW)` elementary operations, under `10^5` at `k=15`.

A failed orbit `O` gives the exact disjunctive requirement

\[
 \bigvee_{j,\phi}
 \left(\bigcap_{t=0}^{q}T_{j+t}=\rho^\phi O\right)
\tag{4.4}

for a lower window, and the analogous union condition for an upper window.
There are three implementation choices:

* block the complete `(life,gap)` candidate (proof-safe, weakest CEGAR cut);
* channel only the interval-membership facts touched by (4.1), then add the
  exact selector disjunction; or
* retain global `c_p` channel variables for shadow clauses while branching
  primarily on `(life,gap)`.

The third is likely the most practical exact SAT hybrid.  The first is the
smallest master.  A purported local no-good on only the runs currently
covering a failed mask is generally **not sound**: a presently absent run
can move into the window and repair it without changing those positive
runs.

## 5. Compiler subproblem and proof-safe Hall cuts

Choose a cut and let `T_0,...,T_(W-1)` be the resulting linear carrier.
For source position `i`, define its maximal erosion envelope

\[
 P_i=\bigcap_{j=\max(0,i-d)}^{\min(i,W-1)}T_j.
\tag{5.1}
\]

At two-sided interior positions every feasible source letter obeys

\[
 F_i:=\{\alpha_i,\beta_{i-d-1}\}\subseteq A_i\subseteq P_i.
\tag{5.2}
\]

At the `O(d)` boundary positions use the exact one-sided tower implications;
for the cheap necessary Hall screen it is also sound simply to put
`F_i=emptyset` there.  This weakens the screen but cannot reject a feasible
compiler.

For every short cell `c=(i,j)`, `0<=j<d`, put

\[
 M_c=\bigcup_{t=i}^{i+j}F_t,
 \qquad
 U_c=\bigcup_{t=i}^{i+j}P_t.
\tag{5.3}
\]

If the cell realizes lower target `S`, necessarily

\[
                         M_c\subseteq S\subseteq U_c.
\tag{5.4}

This gives a carrier-dependent bipartite eligibility graph: left vertices
are all lower targets and right vertices are the `d(W+d)-C(d,2)=19311`
short cells.  Every exact compiler induces a matching saturating all

\[
                   \Lambda=\sum_{s=1}^{7}{15\choose s}=16383
\]

left vertices.  Therefore maximum matching is a fast **necessary** compiler
oracle.

Suppose its alternating-reachability certificate gives a deficient target
set `X`, current neighborhood `B=N(X)`, and defect

\[
                         \delta=|X|-|B|>0.
\]

For a future carrier define

\[
 z_c^X=1\quad\Longleftrightarrow\quad
 \exists S\in X:\ M_c\subseteq S\subseteq U_c.
\]

Then the proof-safe Benders cut is

\[
                 \sum_{c\notin B}z_c^X\ge\delta.
\tag{5.5}

The equivariant quotient version gives capacity `k` to an ordinary position
orbit and uses the exact smaller weights for the exceptional target orbits.
For a quotient defect `Delta`, the weaker block cut requires at least
`ceil(Delta/k)` new eligible position orbits.

Passing (5.5) is not sufficient.  Source bits at different cells are coupled
by the tower equations `D^d A=T`.  The exact second compiler tier is the
bit-level subproblem already implemented by `sandwich2.py`:

```text
x[i,t] is allowed only for t in P_i
OR_{q=i..i+d} x[q,t] = 1 for every t in T_i
every source letter is nonempty
every lower target selects a short interval whose source OR equals it
```

An UNSAT exact compiler may safely block the full carrier interface
`(P_i,F_i)`.  A stronger logic-based Benders implementation attaches
assumptions to the derived envelope/eligibility facts, extracts an UNSAT
core, and blocks only that core.  A plain Hall failure should always be
returned as (5.5), because it is smaller and mathematically interpretable.

## 6. Recommended exact search architecture

```text
MASTER (CP-SAT or C++ LNS)
    decide life[0..N-1], gap[0..N-1] in cyclic run order
    enforce the two sums and start/end residue permutations

REALIZABILITY ORACLE (O(kW))
    reconstruct c and T
    verify event alternation and exact alpha/beta replay
    verify middle/q1 orbit injectivity
    on failure: exact selector cut or full (life,gap) no-good

SHADOW ORACLE (bit masks, O(kW))
    audit lower q2 and all upper unions
    add missing-orbit selector cuts

CUT ORACLE
    try inequivalent linear cuts
    reject cuts that lose a unique upper/lower witness

HALL ORACLE (flow/matching)
    construct (5.4), run Hopcroft--Karp/min-cut
    on defect: add (5.5)

EXACT COMPILER (CP-SAT)
    solve the tower + simultaneous short-interval host problem
    on UNSAT: add an assumption-core interface cut

FINAL VERIFIER
    emit A of length 6438 and exhaust all 2^15-1 targets
```

The separation is important.  No `N^2` lifetime matching is needed, and the
large exact compiler is called only on shadow-complete carriers that pass a
cheap Hall screen.

## 7. Exact replay on the authoritative `k=15` seed

The audit gives:

```text
quotient insertion symbols                    429
quotient deletion symbols                     429
derived lifetime matching                     a permutation of 429
ordered-run start/end residues                two permutations of 429
minimum / maximum lifetime                    4 / 32
sum lifetimes                                 3432 = 8*429
sum zero gaps                                 3003 = 7*429
event-alternation violations                  0
carrier reconstructed from runs               exact, all 6435 states
forced-port ranks                             1^112 2^317
```

The `112` singleton ports are exactly the `112` minimum lifetimes: by (5.2),
`|F_i|=1` precisely when the insertion at `i-d-1` is deleted at `i`, i.e. a
run has the minimum legal lifetime `d+1=4`.

The replay does not change the seed's known failures: it still has `47`
missing lower-q2 orbits and `165` missing terminal physical targets.  It
does prove that those failures live entirely in the shadow arrangement,
not in hidden carrier realizability.

## 8. Relation to Claude's newest `cword.py`

The newest substantive file in
`/Users/amir.nuriyev/Downloads/opusproblem/work` is `cword.py` (mtime
2026-07-29 06:21:47, SHA-256
`0115066efb869d05c4a8c5a5bc3709d5c222f150ff181b6e4b934b8d55133097`).
It correctly implements the run-transversal `c`-space constraints and lazy
middle/q1/q2/upper cover selectors.  The present theorem is the compressed
event/run form of that same model:

```text
c-space:          6435 primary binary trace variables
run schedule:      429 lifetimes + 429 following gaps
```

The compression is most valuable for a C++ LNS or logic-based Benders
master.  `cword.py` remains convenient for monolithic shadow clauses, since
set membership is already a literal there.  Its apparently minimal
`extract_cw()` gauge is in fact correct: coordinate zero is fixed by the
multiplier gauge, and reconstructing with `v=1` merely relabels every other
coordinate.  This was checked directly on the saved voltage-two `k=11`
carrier (`jv=0`, no middle or q1 orbit missing).

An independent import of the three frozen atlas traces through `cword.py`
gave:

```text
case   true voltage   Johnson  residence  middle/q1 missing  q2 missing  upper missing
k=9         4             0        0             0/0              0            0
k=11        2             0        0             0/0              0            0
k=15        1             0        0             0/0             47           95
```

So the new code is a real model collapse and calibrates correctly on both
known strict optima.  It has not emitted a new `k=15` carrier: the frozen
seed remains exactly at the already known `47+95` decoration deficit.

## 9. Honest boundary

This formulation removes a large amount of accidental search state.  It
does not remove the substantive obstacle: selecting the two transversal
event permutations and the lifetime composition so that all lower/upper
shadows and the common lower compiler agree.  In particular, the Hall cut
(5.5) is only a necessary master cut; the exact tower compiler remains the
final integral subproblem.
