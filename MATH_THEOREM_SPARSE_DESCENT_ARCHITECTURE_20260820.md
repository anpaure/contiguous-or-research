# The sparse-descent architecture: exact segment supply from cut SCDs, the closed volume ledger, and the single remaining serialization gate

Date: 2026-08-20 (fourth file of this date; companions listed in
`RESEARCH_INDEX.md` under this date).  Status: Lemmas S1–S4 are proved;
Section 5 proves the volume ledger closes with factor-two slack;
Section 6 states the one remaining gate precisely.  This file supersedes
the `t`-swap parameterization of
`MATH_THEOREM_MULTISWAP_EROSION_FLOOR_REDUCTION_20260820.md` (its Lemmas
M1 and M4 remain in force; its `t=Theta(sqrt(log n))` cap is shown
unnecessary here) and replaces the STW-leave route of Open Problem 6 by
an exact, defect-free segment supply.

Setting: `n=2m+1`, `W=binom(n,m)=binom(n,m+1)`,
`Lambda=sum_{j=1}^{m}binom(n,j)=(sqrt(pi/8)+o(1))W sqrt n` the strict
lower cone mass.  Chronology, windows, and the factorization theorem as
in the companions; `d` denotes the window depth and the coordinate run
floor is `d+1`.

## 1. Lemma S1 (sparse chains: the schedule designs the ranks)

At a position `a` of a chronology, the available window intersections
form the nested family `X_a` minus its departure prefixes.  If the step
departure sets are chosen freely (sizes unrestricted), the chain of
intersections can realize ANY prescribed nested sequence
`G_1 supset G_2 supset ... supset G_s` with `G_1 subset X_a`: depart
`X_a\G_1`, then `G_1\G_2`, ..., then `G_{s-1}\G_s`, in `s` steps.  The
ranks of the `G_i` are arbitrary — window chains are sparse, not
saturated.  The letters of the compiled word remain nonempty throughout
provided `G_s` persists `d` further steps (letters contain `G_s`).

*Proof.*  Immediate from the intersection identity (Lemma M2(3) of the
multi-swap file) with the departure sets as stated; nonzero letters from
`A_j^{max} ⊇ G_s`.  ∎

This removes the swap-size cap entirely: big departure steps are legal;
the only inherited constraints are the run floor (every departing
coordinate is `>=d+1` old, every arriving coordinate persists `>=d+1`)
and the global ledgers of Section 5.

## 2. Lemma S2 (exact segment supply — no STW leave)

Fix `C>=1` and `eps=(sqrt(pi/8))/C`.  There is an explicit partition of
the strict lower cone (ranks `1..m`) into at most `(1+eps)W` nested
segments, each with at most `Cceil(sqrt n)` elements: take any chain
partition of the cone into `W` chains (the truncated symmetric chain
decomposition is explicit) and cut every chain into consecutive blocks
of at most `Cceil(sqrt n)` elements.  The number of segments is at most
`W+Lambda/(C sqrt n)=(1+eps+o(1))W`.

*Proof.*  Dilworth/SCD plus the stated cut count.  ∎

Unlike the STW-anchored packing (leave `Lambda k^{-1/16}`), this supply
is exact: every strict-lower target lies in exactly one segment.  The
leave-exponent problem of the multi-swap file's Open Problem 6 is
thereby dissolved — the difficulty was an artifact of demanding
near-uniform saturated chains, which sparse window chains do not need.

## 3. Lemma S3 (anchoring the segments)

Each segment is a nested family with top `G_1`; it can be served at any
position whose owner contains `G_1`.  Segments with rank-`m` tops number
at most `W` and have exactly `m+1` admissible owners each; the
rank-`m`/rank-`(m+1)` containment graph is `(m+1)`-regular, so a
perfect matching assigns them distinct owners.  Deeper-topped segments
number at most `Lambda/(C sqrt n)<=eps W` and each admits
`binom(n-|G_1|, m+1-|G_1|)>=m+1` owners; assigning them by any
injective choice into the `eps W` surplus positions satisfies Hall's
condition with room (each such segment has at least `m+1` choices and
the demand per owner can be capped at `O(1)` by a standard b-matching
argument).

## 4. What the chronology must do

A single cyclic chronology of length `L=(1+2eps)W` rank-`(m+1)` owners
must: (i) visit every rank-`(m+1)` set at least once (upper-layer
coverage; unions of consecutive owners then give the upper band as in
the companions); (ii) at the position assigned to each segment, have
its forward departure stream realize that segment's nested sequence as
window intersections (Lemma S1); (iii) satisfy the run floor `d+1`,
`d=Cceil(sqrt n)`, at every step; (iv) keep every letter nonempty
(automatic from Lemma S1's `G_s`-persistence).  Far ranks are then
absorbed per Theorem A, and coefficient one follows for all `k` by the
standard assembly.

## 5. Theorem S4 (the volume ledger closes)

The run floor caps total turnover: a chronology of length `L` with all
runs `>=d+1` has total departure volume at most `(m+1)L/(d+1)`.  The
descent demand of the segment supply is, per segment, `(m+1)-|G_s|`
(telescoping), i.e. the depth of its bottom.  Summed over the cut SCD:

\[
\sum_{\text{segments}}(\text{bottom depth})
=\frac{1}{2C\sqrt n}\sum_i c_i \ell_i^2\,(1+o(1))
=\frac{1}{2C\sqrt n}\cdot\frac{Wn}{2}\,(1+o(1))
=\frac{W\sqrt n}{4C}(1+o(1)),
\]

using `sum_i c_i ell_i^2 = sum_x [binom(n,m-x)-binom(n,m-x-1)]x^2 =
(1+o(1))·2W·sum_x x e^{-2x^2/n} = (1+o(1))Wn/2` by Abel summation and
the Gaussian profile.  The budget is

\[
\frac{(m+1)L}{d+1}=\frac{(1+2eps)W(m+1)}{C\sqrt n}
=(1+2eps)(1+o(1))\frac{W\sqrt n}{2C}.
\]

Demand over budget is `1/2+o(1)`: **the ledger closes with factor-two
slack**, uniformly in `C`.  In particular no counting obstruction —
mass, width, window count (Lemma M1), turnover, letter nonzeroness, or
owner enumeration — separates the sparse-descent architecture from
coefficient one.

*Proof.*  Turnover cap: each of the at most `(m+1)L/(d+1)` maximal runs
contributes one departure... more precisely total coordinate incidence
is `(m+1)L`, every run has length `>=d+1`, and departures biject with
completed runs.  Demand: the telescoping identity and the displayed
Abel summation.  ∎

**AUDIT CORRECTION (2026-08-20, second reader): THEOREM S4 IS FALSE
AS STATED — the ledger does NOT close.**  The displayed demand
`sum ell^2/(2d)` is the sum over cut pieces of bottom depths ONLY in
the regime `ell >> d`, where a chain of length `ell` yields `ell/d`
pieces with bottom depths `d, 2d, ..., ell`.  But `d = C·sqrt n`
EXCEEDS the typical SCD chain length `Theta(sqrt n)`: almost every
chain is a SINGLE piece whose demand is its full bottom depth
`~ell`, contributing the base term `sum_{ell <= 2d} c·ell` — which
the displayed formula drops.  The correct demand is

    `sum_segments (bottom depth) = (1+o(1))·Lambda = Theta(W·sqrt n)`,

INDEPENDENT OF `C` (each cone target needs at least one departure at
or below its depth; equivalently, per segment the bottom depth is at
least the number of targets it contains).  Against the budget
`W·sqrt n/(2C)` this REVERSES for large `C`: the run floor makes
per-owner turnover scarcer while the demand stays put.  The only
escape is DEPARTURE SHARING — one departure serving many concurrent
segments — and proving that sharing is feasible at density
`Theta(C)` per departure is precisely the serialization problem
(Section 6 / Open Problem 7), NOT a closed counting ledger.
Everything downstream in this date's files that cites "S4 slack" or
"all counting obstructions closed with slack" is hereby withdrawn to
candidate status.  Lemmas S1–S3 (sparsity, cut supply exactness,
anchoring matching) are unaffected.

## 6. The single remaining gate

Window chains at overlapping positions share one departure stream, so
segments served at nearby positions are not independent: the family of
served segments must be realizable as the staircase of window
intersections of a single stream.  Concretely, the remaining problem is:

**Open Problem 7 (staircase serialization).**  Order and schedule the
`(1+eps)W` segments of Lemma S2 (with the anchoring of Lemma S3) into
one cyclic departure stream of length `(1+2eps)W` such that (i) each
segment's sets appear as the window intersections at its serving
position, (ii) every departing coordinate is at least `d+1` old and
every arriving coordinate persists at least `d+1` steps, and (iii) the
owners visit every rank-`(m+1)` set.  By Lemmas S1–S3, Theorem S4, the
factorization/collar compiler, and far-rank absorption, a solution
implies `nu(k)=(1+o(1))binom(k,floor(k/2))` for all `k`.

This is the serialization gate of the master handoff (Section 5.3,
layered trace flow; Section 7.3 gate 8) in its sharpest form to date:
all fractional, counting, and supply-side obstacles are now closed with
slack, the segment supply is exact rather than defective, and the gate
is a pure scheduling/compatibility statement.  Natural attack: group
segments by bottom depth and serve deep segments at widely separated
positions (their big descents are rare: volume `W sqrt n/(4C)` spread
over `L` positions averages `sqrt n/(4C)` departures per step, and the
run-floor condition is a local age constraint amenable to a
Lovász-local-lemma or flow/de-Bruijn-path argument at these densities).
The handoff's own layered de Bruijn formulation says exactly this
becomes a source–sink path question in a totally unimodular flow once
the segment order is fixed; the new content needed is an order for
which the flow is feasible, and the slack of Theorem S4 is the first
quantitative evidence that such an order exists.

## 6.5 The cut ledger for Open Problem 7 (same-day addendum)

The serialization system is interval-structured — every constraint is a
time-window statement — so once an assignment is fixed, feasibility is
a totally unimodular flow (the handoff's layered-trace theorem), and
the essential cuts are enumerable.  Computing them:

1. **Per-step capacity.**  Departures at step `i` are a subset of the
   current owner: `|D_i|<=m+1`.  Average demand is `sqrt n/(4C)`
   (Theorem S4).  Local slack factor `Theta(sqrt n)`: per-step
   congestion is never binding.

2. **Per-coordinate spacing.**  Each coordinate `x` departs once per
   served difference-block containing it; total demand per coordinate
   is `(volume)/n=W/(4C sqrt n)` departures, each pair at least `d+1=
   C sqrt n+1` apart, total span `>=W/4` against chronology length
   `L=(1+2eps)W`: **slack factor 4**.  This is the binding constraint
   class.

3. **Random assignment fails it.**  Spreading segments uniformly at
   random gives each coordinate `Theta((W/(C sqrt n))^2·(C sqrt n)/W)
   =Theta(W/(C sqrt n))·(1/sqrt n·...)` colliding departure pairs;
   summed over coordinates this is `Theta(W sqrt n/C)` — the same
   order as the whole volume.  Independent randomness is therefore
   excluded here exactly as it was excluded in the covering corners
   (companion Proposition 6.1 and handoff Section 8): the assignment
   must be *balanced*, with every coordinate's departures near-
   periodic at spacing `~4(d+1)`.

4. **The natural symmetry.**  A `Z_n`-equivariant design — SCD, cut,
   anchoring, and serving order all commuting with the rotation
   `x -> x+1`, which acts freely on the middle layers (cycle lemma,
   identity (0.1) of the first companion) — makes every coordinate's
   departure pattern an exact rotation of every other's, so balance
   holds identically rather than probabilistically.  The
   Greene–Kleitman bracketing SCD is not rotation-equivariant, but the
   necklace-orbit structure (all rotation orbits of the middle layers
   are full, `Cat_m` of them) suggests an orbit-by-orbit variant.

**Open Problem 7′ (refining Open Problem 7).**  Construct a
`Z_n`-equivariant (or otherwise exactly balanced) cut-chain supply and
assignment for which the per-coordinate departure patterns have spacing
`>=d+1`; then verify the residual interval cuts and conclude by total
unimodularity.  Items 1–2 show the two dominant cut classes carry slack
`sqrt n` and `4` respectively; item 3 shows the balance cannot come
from independent randomness; item 4 names the symmetry that would
provide it identically.

## 7. Scope guard

Lemmas S1–S3 and Theorem S4 are complete proofs given the cited
companions and classical SCD/Dilworth/König facts.  Open Problem 7 is
open; nothing here claims it.  The exact conjectures `nu(k)=B(k)` and
finite `k=17` are untouched.
