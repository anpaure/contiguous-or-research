# Fable general-case session — durable checkpoint

Date: 2026-07-22.  Owner: Fable session (this file is written only by the
main Fable agent).  Everything below separates **proved**, **conditional**,
**heuristic**, and **open** explicitly.  Nothing here overwrites or edits any
existing audited note.

Notation. `nu(k)` = min length for nonzero masks; `W(k)=binom(k,floor(k/2))`.
For the three-box program: `P=[0,2a]^3` (centered form `[-a,a]^3`),
middle hexagon `H_a`, `M_a=3a^2+3a+1`, lower-half target count
`V_a=4a^3+(9/2)a^2+(3/2)a-1`.  For a word of length `N` with one selected
witnessing interval `I_i=[ell_i,r_i]` per middle target (sorted by left
endpoint), the audited monotone-band normal form gives strictly increasing
endpoint sequences, `ell_i=i+alpha_i`, `r_i=i+beta_i`,
`0<=alpha_i<=beta_i<=D`, both `alpha,beta` nondecreasing, `w_i=beta_i-alpha_i`,
`D=N-M_a>=0`.

## 1. Ledger

1. [External, audited] `W(k) <= nu(k) <= (sqrt2+o(1))W(k)`; exact values
   through `k=10` and `k=12`; leading conjecture `nu(k)=B(k)`.
2. [External, audited] Weak vertical wreath lemma (sum of shallow wreath
   defects `o(W)`) implies `nu=(1+o(1))W` (GLOBAL_MTF_ATOM_ROUNDING_FINAL_AUDIT
   Thm 3.1); exact overlap ledger Thm 4.1 there.
3. [External, audited] Linear-error three-box aggregation:
   `g_3 <= width + O(p+q+r)` for all boxes implies `nu <= W + O(W/sqrt k)`
   (FIXED_DIMENSION_GRID_REDUCTION Thm 1).
4. [Proved, this session — Section 2] **Theorem A (subquadratic relaxation).**
   For `t=3`, a local bound `g_3 <= width + O((1+p+q+r)^c)` with any fixed
   `c<2` already implies `nu(k)=(1+o(1))W(k)`.  For general fixed `t`, the
   threshold is `c<t-1`; in particular the four-box route only needs
   `g_4(m,m,m,m) <= width + O(m^{3-eps})`, not `+O(m^2)`.
5. [Proved, this session — Section 3] **Lemma B (fan-capped avoidance).**
   For any word covering the box and any depth `h>=1`, with `S_h` the set of
   covered points of rank in `[m*-h, m*-1]` (`m*` = middle rank),
   `|S_h| <= sum_i min(w_i,h) + hD`.
   The correction is `hD`, not `h^2 D`; the audit of that distinction is in
   Section 3.4.  Machine-checked on the exact `g_3(2,2,2)=10` certificate
   (Section 3.5).
6. [Conditional: Lemma B + audited certificates of
   THREE_BOX_PHASE_SEPARATION_RESEARCH(+AUDIT)] **C1.** The nested
   aligned-desert order `O_a` requires `D >= (1/2-o(1))a^2`.
   **C2.** Side-batched orders require `D=Omega(a^2)` or `B=Omega(a)` maximal
   batches.  Both previously died only at `D=O(a)`/`D>=a^{3/2}`; now they die
   in the entire subquadratic regime, i.e. they cannot serve even the relaxed
   Theorem A target.
7. [Conditional: Lemma B + audited anti-mixing run/mesh machinery] **C4.**
   The anti-mixing tradeoff `HD >= (1/2-o(1))s^3` holds for all `D=o(s^2)`
   (previously only `D=O(s)`), because Lemma B removes the `3D^2` ledger
   slack.  Hence uniformly random middle orders need `D=Omega(a^2/log a)`
   (using the audited whp mesh `H=O(s log s)`).
8. [Heuristic] Random orders should in fact need `D=Omega(a^2)` via
   heterogeneous singleton-run covers (local-coordinate-maxima); the whp
   cover-with-span-`O(log a)` estimate is unproved (ties + dependency gaps).
9. [Open fork — decisive either way] **Conjecture D (universal cheap cover).**
   Every order of `H_a` admits an internal-run assignment with
   `sum_i min(lambda_i, 3a-1) <= (4-eps)a^3` and charge congestions `O(a)`.
   If true, Lemma B gives `g_3(2a,2a,2a) >= M_a + Omega(a^2)` for **every**
   order, refuting the (even relaxed) three-box aggregation route and
   materially redirecting the program to wreaths/four-box.  If false, the
   counterexample order is the only possible shape of a three-box
   construction.  This is the smallest currently isolated fork.
10. [Proved; corrected per FABLE_RUN_SPECTRUM_AUDIT.md — see 8d]
   **Theorem I (run-spectrum inequality).**
   `Def_R(h) <= B_a(h) + (2sigma+h)D` for every cap `h` simultaneously,
   every span-`sigma` run assignment; universal span `sigma=4a+3`;
   `B_a(3a-1)=5a^3+O(a^2)`; average capped run cost `>= (4/3-o(1))a` when
   `D=o(a^2)`.  Plus: exceptional-set bound (2.15), distributional width
   bound `K(h-r) <= B_a(h)+hD`, literal-row bound `D >= M_a-1`, local
   neighbor-exceedance lemma, and imported Theorem K (Theta(a) long
   central-line peak plateaux occupying Omega(a^2) mass; corridor PACKING).
11. [RETRACTED — see 8d.2] All pointwise-concentration and staircase
   classification claims of 8a/8b/8c: the "8/9 rigidity" pointwise form,
   the width-density sentence of Corollary H, "all but o(a^2) indices have
   (4/3-o(1))a runs", Theorem J's global forcing, the ride partition /
   9a/4 count / 3-phase handoff / transportation equations, and the
   promotion of ring/random `Omega(a^2)` claims.  The audit's abstract
   counterexample spectrum (3/5 at `a`, 2/5 at `2a`) passes every capped
   inequality; concentration cannot follow from Theorem I alone.
12. [Sections 9–12; §12 is authoritative where they conflict]
   **Theorem L** (audited valid, FABLE_INTERVAL_SUPPLY_AUDIT): service
   coefficient `min{(4-c)e_c, 2e_c+H_c}` for `c>1`, and `(4-c)e_c` alone
   for `0<c<=1` — NOT superseded.  **MASTER + supply law** (audited
   valid): `int_0^2 min(3,s(c))dc >= 4-o(1)`,
   `s(c) = a^{-2} sum_{lambda>ca}(L-lambda) >= (4-3c)/(2-c)-o(1)`.
   **Mass law** `(4-c)e(c) >= 4-3c-o(1)` on all `(0,4/3)`.
   **Proved kills:** contiguous-ring and uniformly-random orders have
   `D=Omega(a^2)` (Theorem L at `c=6/5`, §12.1(2)).  **Theorem R:**
   only the Markov tail `#{i: q_i>=beta a} >=
   ((4-3beta)/(2-beta))a^2-o(a^2)` is certified; the
   reservoir-forcing gloss is NOT (see §12.2 marking;
   BOUNDARY_RESERVOIR_PROFILE.md has the rigorous position-sensitive
   replacement under vanishing-seam hypotheses).  **Lemma R / Theorem
   P / P' / P'' (§11.2–11.3, §12.3): UNAUDITED — Lemma R false as
   written at equality seams (cost-1 repair plausible, unaudited);
   Theorem P has a minimum-length hypothesis gap; P' has constant
   (2a vs 8a), span, and maxima-count gaps; P'''s gap dichotomy is
   unproved.  Near-rotating forcing is CONJECTURAL.**  Proposition Q
   (same-letter adjacency impossible) is certified.  **Theorem O**:
   CONJECTURAL pending audit; nothing downstream relies on it.
   **Retracted:** §10.3 supply-count conflation, §10.4 dense-chain
   forcing (`2 delta_{4/3}` countermodel), §10.1 "wholly superseded".
   **Windmill v3 (§12.4) is HEURISTIC** (assumes the unproved
   bounded-gap A-ledger; derivation incomplete; uniqueness
   uncertified).  The open fork Q3 stands as the working target, with
   its premises correspondingly conditional.
13. [Proved and independently hostile-audited, 2026-08-14]
   **Thirteen-port MSW serialization theorem.**  For
   `n=2m+1>=13(d+1)`, the case-selected highest-valley arborescence admits
   one simultaneous coalesced common-history realization using thirteen
   fixed source starts.  It fuses every native tight MSW circuit into one
   cyclic source word and preserves the complete occurrence-labelled deck
   through width `d+1`.  This closes owner/strict-lower chronology in the
   target regime `d=O(sqrt(m))`, but not proper-upper completion.
14. [Proved finite theorem, 2026-08-14; not an asymptotic extrapolation]
   The split-aware `D_5` T2 bank has 41 pairwise owner/q1-disjoint circuits,
   preserves aggregate q2 support, and sends all 42 suffix roots and 372
   touched components to one component.  Its undilated chronology has 181
   upper and 151 lower bad q2 collars, so symbolic residence dilation and
   an all-suffix grammar remain open.
15. [Proved, 2026-08-14]
   **Canonical two-step GK selector fiber theorem.**  Deleting the first
   two free ones gives an injective upper-to-lower map, but the associated
   head map has exact fiber law
   `#{B: fibre(B)=k}=binom(2m-k,m-k)`.  Hence its distinct-head deficit is
   `binom(2m,m-2)=((m-1)/(2m+1))binom(2m+1,m+2)`, asymptotically one half.
   The direct two-step-chain shortcut therefore requires a macroscopic,
   not sparse, repair.
16. [Exact reduction plus finite obstruction, 2026-08-14]
   Restricting fixed-GK leaf choices to `q>p` makes every selected owner
   edge descend the coordinate-sum potential, so any simultaneous
   lower/head SDR is automatically a Catalan linear forest.  The inverse
   host has exactly three head charts.  All two-chart subhosts fail in
   finite cases, and the full leaf-right head projection first has a Hall
   defect at `m=7`; an all-parameter adaptive reset theorem is now the
   precise selector gate.

## 2. Theorem A: subquadratic aggregation relaxation

**Theorem A.** Fix `t>=3` and `1<=c<t-1`.  Suppose every `t`-chain-box
satisfies `g_t(ell_1..ell_t) <= w(ell) + K(1+sum ell_i)^c`.  Then
`nu(k) <= W(k) + O_t(W(k) k^{(c-t+1)/2}) = (1+o(1))W(k)`.

*Proof.* Identical aggregation as the audited Theorem 1 of
FIXED_DIMENSION_GRID_REDUCTION; only the error sum changes.  By convexity,
`(1+sum ell_i)^c <= t^c sum_i (1+ell_i)^c`.  The audited SCD moment bound
gives, for every fixed integer `r`, `(1/W(s)) sum_C (1+ell(C))^r = O_r(s^{r/2})`;
for non-integer `c` use the power-mean inequality
`E[X^c] <= (E[X^{ceil(c)}])^{c/ceil(c)}`, so `E[(1+ell)^c] = O(k^{c/2})`.
Factorizing over the product of chain families, the total error is
`O(prod_i W(k_i) * k^{c/2})`, and the audited balanced-split ratio
`prod_i W(k_i)/W(k) = Theta(k^{-(t-1)/2})` gives total error
`O(W k^{(c-t+1)/2})`, which is `o(W)` exactly when `c<t-1`.  QED.

Consequences.  (i) `t=3`: any `D=O(a^{2-eps})` per cubic box suffices; all
previously audited obstructions were stated against `D=O(a)` and stop
binding at `D=Theta(a^{3/2})` because of the `3D^2` term in the old ledger —
so before this session the relaxed regime was wide open.  (ii) `t=4`: budget
`O(m^{3-eps})`; the central-diagonal construction of
FOUR_BOX_CENTRAL_DIAGONALS has all-depth defect `Theta(m^4)` — the gap to a
sufficient four-box theorem is now exactly one power of `m`, not two.

## 3. Lemma B: the fan-capped avoidance inequality

### 3.1 Exact setting

Word `A_1..A_N`, entries arbitrary nonzero box points (after the audited
closure normalization), contiguous joins covering every nonzero point of a
product of three chains with middle rank `m*`.  (The proof works verbatim in
any graded lattice in which `u<=v` implies `rank(u)<=rank(v)` with equality
iff `u=v`; in particular in the Boolean lattice with OR — see 3.6.)

Select one witnessing interval `I_i=[ell_i,r_i]` for each of the `M` middle
(rank `m*`) targets `T_i` (join over `I_i` equals `T_i`).  Sort by left
endpoint; the audited antichain argument makes both endpoint sequences
strictly increasing, giving the normal form of Section 0 with `D=N-M>=0` and
`w_i=r_i-ell_i`.

For `1<=x<=N` define the **fan** at `x`:
`Fan(x) = { [x,y] : x<=y<=e(x) }`, where `e(x)=r_{i(x)}-1` if
`i(x):=min{ i : ell_i>=x }` exists, and `e(x)=N` otherwise.

Fix `h>=1` and let `S_h` be the set of covered points of rank in
`[m*-h, m*-1]`.

### 3.2 Statement

**Lemma B.**  `|S_h| <= sum_{i=1}^{M} min(w_i, h) + hD.`

**Lemma B' (Mirsky form, sharper).**  For any set `S` of covered points of
rank `< m*`, with `c` the maximum size of a chain contained in `S`:
`|S| <= sum_i min(w_i, c) + cD`.  (B follows from B' since a chain inside a
band of `h` ranks has at most `h` elements.)  Proof: identical, except step
(2) notes the targets assigned to one fan form a chain **contained in `S`**,
hence have at most `c` elements directly.

### 3.3 Proof

(1) *Every representing interval lies in a fan.*  Let `s in S_h` and let
`[x,y]` be an interval with join `s`.  If `y > e(x)` and `i(x)` exists, then
`ell_{i(x)} >= x` and `r_{i(x)} <= y`, so `[x,y] contains I_{i(x)}` entirely,
whence `s >= T_{i(x)}` and `rank(s) >= m*`, a contradiction.  So `y <= e(x)`:
the interval belongs to `Fan(x)`.

(2) *Fan cap.*  Assign each `s in S_h` one representing interval, keyed by
its left endpoint `x`.  For fixed `x`, the joins `J(x,y)` are nondecreasing
in `y`, so the distinct targets assigned to `Fan(x)` form a chain; a chain
meets each rank at most once, and `S_h` occupies `h` ranks.  Also the number
of targets is at most the number of intervals `e(x)-x+1`.  Hence `Fan(x)`
hosts at most `min(e(x)-x+1, h)` targets.

(3) *Summation.*  Partition `x in [1,N]` by `i(x)`: with `ell_0:=0`,
`i(x)=i` iff `x in (ell_{i-1}, ell_i]`, and `i(x)` is undefined iff
`x > ell_M`.  For `i(x)=i`, write `x=ell_i-g`, `0<=g<=Delta_i-1`,
`Delta_i=ell_i-ell_{i-1}`; then `e(x)-x+1 = r_i-ell_i+g = w_i+g`, and

    sum_{g=0}^{Delta_i-1} min(w_i+g, h) <= min(w_i,h) + (Delta_i-1)h.

Summing over `i`: `sum_i (Delta_i-1) = ell_M - M = alpha_M`, so the middle
region contributes at most `sum_i min(w_i,h) + alpha_M h`  (for `i=1`,
`Delta_1-1 = ell_1-1 = alpha_1`, consistent).  The undefined region has
`N-ell_M = D-alpha_M` positions, each capped by `h`.  Total correction
`alpha_M h + (D-alpha_M) h = hD`.  QED.

### 3.4 Audit: `O(hD)` versus `O(h^2 D)`

The correction is exactly `<= hD`.  Three places where a spurious `h^2 D`
could have entered, each avoided:

* **Per-rank ledgers.**  Running the old avoidance ledger separately at each
  of the `h` depths and adding would give `h` corrections of size `O(hD)`
  each (`h` ranks x variation `D` x cap `h` interactions), i.e. `O(h^2 D)`.
  The unified fan count never splits by rank: the chain argument absorbs all
  `h` ranks in one cap.  This is the essential improvement over summing the
  audited single-ledger `Q <= sum w_i + 3D^2 + 2D`: the `3D^2` term (which is
  `3a^3` at `D=a^{3/2}` and destroyed all subquadratic obstructions) is gone,
  replaced by `hD`.
* **Gap fans.**  Positions in enlarged gaps (`Delta_i>1`) contribute
  `(Delta_i-1)` fans; bounding each by its size `w_i+g` (up to `D`) instead
  of by `h` would give `D^2`-type terms.  The cap `h` applies to every fan,
  so the total gap contribution is `(sum_i(Delta_i-1))h <= alpha_M h`.
* **Boundary fans.**  Trailing fans (`x>ell_M`) number `D-alpha_M`, not `D`;
  together with the leading/middle charge `alpha_M h` this telescopes to
  exactly `hD`, not `2hD` or `3(D+1)h` (earlier draft constants were
  conservative; the sharp constant is 1).

One further check: step (2) needs distinct same-rank targets to be
incomparable — true in any graded lattice with the stated rank property.
Step (1) needs every entry of `I_i` to be `<= T_i` — true since the join
over `I_i` is exactly `T_i`.  Step (3) needs `M<=N` — forced by the strict
endpoint monotonicity.  No factorability, pinning, or run hypothesis is
used: Lemma B is unconditional for every covering word and every witness
selection.

### 3.5 Machine sanity check (falsification test)

Executed 2026-07-22 (`fable_general_case/test_fan_capped.py`).  Checked:
(i) the exact `g_3(2,2,2)=10` certificate word, all witness selections, all
`h`; (ii) random covering words on boxes `(1,1,1)..(3,3,2)`; (iii) shuffled
full-permutation words and greedily shrunk covers on boxes up to `(4,4,4)`
and `(5,5,1)`, extremal (leftmost/rightmost/shortest/longest) plus random
selections.  Zero violations.  This is falsification evidence only; the
proof is Section 3.3.

### 3.6 Boolean instantiation (near-Ucycle style corollary)

Lemma B holds verbatim for words of nonzero masks on `[n]`, `n=2m+1`, with
`T_i` the `W` masks of size `m` and `S_h` the masks of sizes
`m-h..m-1`.  Since `|S_h| >= hW(1-O(h^2/m))`, any word of length
`N=(1+eps)W` satisfies

    sum_i min(w_i,h) >= hW(1-eps-O(h^2/m)) - hW*o(1)

for every `h=o(sqrt m)` simultaneously: almost every middle witness must
carry an almost-full width-`h` band at every shallow depth.  This is a
necessary near-SCD-band structure theorem for **any** near-optimal word and
should be compared with CENTRAL_NEAR_UCYCLE.md before being claimed as new
(not yet re-read this session — see Section 7).

## 4. Conditional consequences (imports listed)

**C1 (nested order).**  Import: audited Lemma 2 of
THREE_BOX_PHASE_SEPARATION_RESEARCH — run assignment for `O_a` with
`sum lambda_i = a^3-a`, spans `<=2a`, congestions `C_alpha<=2a, C_beta<=a`,
one unassigned index.  The audited run inequality gives
`w_i <= lambda_i + T_i` with `sum_i T_i <= (C_alpha+C_beta)D <= 3aD`.  Since
`min(w_i,c) <= min(lambda_i,c)+T_i` (valid because `min(A+B,c)<=min(A,c)+B`
for `B>=0`), Lemma B with `c=3a-1` gives
`V_a <= (a^3-a) + 3aD + c + cD <= a^3 + (6a-1)D + O(a)`.
With `V_a=4a^3+O(a^2)`: `D >= (1/2-o(1))a^2`.  So the fully aligned
recursive order is dead for the relaxed target too.

**C2 (side-batched orders).**  Import: audited Proposition 4 internals
(binary run structure, nine-block window, spans `<=5a`, assigned run-length
budget `3a^3+O(a^2)`, `<=8a(B+1)` discarded indices).  Capping: discarded
indices now cost `c=O(a)` each (not `D`), so
`V_a <= 3a^3+O(a^2) + O(a)D + O(a^2 B) + cD`, giving
`a^3 <= O(aD) + O(a^2B)`, i.e. `D=Omega(a^2)` **or** `B=Omega(a)`.

**C4 (anti-mixing upgraded).**  Import: audited Sections 3–4 of
THREE_BOX_INTERLEAVING_OBSTRUCTION (mesh `H`, exceptional set `|E|<=3(s+1)`,
run inequality, charge congestion `<=H+1`).  Capping the `E`-indices at `c`
instead of `D`:
`sum_i min(w_i,c) <= sM_s + 2(H+1)D + 3(s+1)c`.  Lemma B then gives
`V_s <= sM_s + 2(H+1)D + O(s^2) + cD`, so
`s^3(1-o(1)) <= 2HD + O(sD)`, hence for all `D=o(s^2)`:
`HD >= (1/2-o(1))s^3`.  With the audited whp random mesh `H=O(s log s)`:
random orders need `D=Omega(s^2/log s)`.

Not yet recomputed under the cap (flagged, not claimed): the
`Omega(a)`-extra-cuts corollary of THREE_BOX_ADJACENT_SHADOW_MATCHING, and
the contiguous-ring obstruction constants.

## 5. The decisive fork (Conjecture D)

To close the three-box route entirely (even relaxed) it suffices to prove:
for every order of `H_a` there exist internal coordinate-threshold runs
`R_i` (heterogeneous, as in the audited Lemma 1 of
THREE_BOX_PHASE_SEPARATION_RESEARCH) assigned to all but `o(a^2)` indices
with `sum_i min(lambda_i, 3a-1) <= (4-eps)a^3` and congestions
`C_alpha+C_beta = O(a)`.  Then Lemma B forces
`eps a^3 <= O(a)D + o(a^2)*O(a)`, i.e. `D=Omega(a^2)` for every order, i.e.
`g_3(2a,2a,2a) >= width + Omega(a^2)`, contradicting the relaxed local
hypothesis and closing the `t=3` product route.  Conversely, an order with
no such cheap cover must have, in every span-`O(a)` window around almost
every index, only long runs (`lambda=Theta(a)`) of every one of the `6a+O(1)`
thresholds or none at all — an extreme simultaneous-monotonicity property
that would itself be the construction blueprint.  Either outcome materially
changes the program.  (The `x>=v` thresholds with `v` near `a` have sparse
supports whose runs are typically singletons with `lambda=0`; this is why
generic orders should be coverable — the heuristic behind item 8 of the
ledger.)

## 6. Proof gaps and cautions

1. Lemma B is proved for one-sided (below-middle) targets.  The upper band
   has no verbatim dual: intervals representing above-middle targets may
   contain complete middle witnesses, so the fan range argument fails there.
   Any use of Lemma B on both sides needs a separate upper mechanism.
2. C1/C2/C4 are conditional on the imported audited certificates; the import
   of congestion bounds was re-derived here only at the `O(.)` level.  The
   side-batch congestion constant (`5a` vs the audit's bundled `8aB`) was not
   re-verified line by line.
3. Item 8 (random `Omega(a^2)`) is a heuristic: the singleton-cover span
   estimate needs a dependency-tolerant maximal-gap argument and careful
   treatment of coordinate ties.
4. Conjecture D is open in both directions.
5. Theorem A only targets `nu=(1+o(1))W`; the `W+O(W/sqrt k)` refinement
   still needs `c=1`.
6. `g_3(2,2,2)=10 = width+3` is consistent with everything here (Lemma B at
   `a=1` is slack); no small-case tension.
7. Lemma B counts distinct targets, not intervals; it never bounds `D` alone
   without a run certificate bounding `sum min(w_i,c)` — trivially
   `sum min(w_i,c) <= cM_a ~ 9a^3 > 4a^3`, so the inequality is not
   self-contradictory with the conjecture.  All strength comes from the
   combination step.

## 7. Overlap with existing notes

* Monotone band normal form, run/pin inequality, avoidance ledger: identical
  to the audited Sections 2–5 of THREE_BOX_INTERLEAVING_OBSTRUCTION and
  Lemma 1 of THREE_BOX_PHASE_SEPARATION_RESEARCH.  Lemma B replaces **only**
  the ledger step (`Q <= sum w_i + 3D^2 + 2D`) by a capped count with `hD`
  correction; everything else is reused unchanged.
* PINNING_THEOREM.md / GLOBAL_PINNING.md: the pin mechanism used in step
  (2.3) is theirs; whether a fan/cap count already appears there is
  unverified this session (TODO before claiming novelty).
* CENTRAL_NEAR_UCYCLE.md: the Boolean corollary 3.6 likely intersects it;
  unverified this session (TODO).
* THREE_BOX_SPIRAL_BAND_OBSTRUCTION / ADJACENT_SHADOW_MATCHING: their
  conclusions are subsumed or strengthened by C1/C2/C4 in the subquadratic
  regime, but the exact constants were not re-derived under the cap.

## 8a. Session update (same day, later): Conjecture D sharpened to a dichotomy

**Theorem E (universal window run — PROVED, unconditional).**  In every
order `T_1..T_{M_a}` of `H_a` (`a>=2`) and for every index `i` with
`i+4a+2 <= M_a`, some coordinate threshold has an internal maximal run
contained in `[i+1, i+4a+2]` (hence avoiding `i`, one-sided span `<=4a+2`).
Symmetrically leftward.

*Proof.*  (1) If a window `W=[t_1,t_2]` contains an interior
plateau-local-max of some coordinate `xi` — a maximal constant-`xi` plateau
`[u,v] subseteq [t_1+1,t_2-1]` with `xi_{u-1}<xi_u` and `xi_{v+1}<xi_v` —
then `[u,v]` is exactly the maximal run of threshold `xi>=xi_u` (legal:
`xi_u>=-a+1` since a strictly smaller value exists), and it is internal in
the full word.  (2) If no coordinate has such a plateau-max in `W`, then
every superlevel component of every coordinate touches the window boundary
(else its argmax plateau would be an interior plateau-max), i.e. all three
coordinate sequences are quasi-convex on `W`: nonincreasing then
nondecreasing, with valley indices `m_x<=m_y<=m_z` (after sorting).  On
`[t_1,m_x]` all three are nonincreasing with sum identically 0, hence all
constant, hence the points repeat — so `m_x=t_1`; dually `m_z=t_2`.  Thus
`x` is nondecreasing and `z` nonincreasing on all of `W`; every step has
`Delta x>=1` or `Delta z<=-1` (distinct points), and each class has at most
`2a` steps (coordinate range), so `|W| <= 4a+1 < 4a+2`.  QED.

Notes: order is an arbitrary permutation (steps may jump; only monotonicity
was used).  Plateau values need not be unit-separated.  This holds for any
box `[0,p]x[0,q]x[0,r]` with `4a+2` replaced by `p+r+2` after sorting
(only the two extreme coordinate ranges enter).

**Definition.** `lambda*(i)` = minimum length (`=|run|-1`) of an internal
run avoiding `i` with one-sided span `<=4a+2` (rightward for
`i<=M_a-4a-2`, leftward for the tail).  Theorem E: `lambda*(i)` is defined
for all `i` (both directions fail only if `M_a<4a+2`, false for `a>=2`).

**Theorem F (dear rigidity — PROVED given Lemma B + audited run
inequality).**  Every covering word of the box `[0,2a]^3` with excess `D`
satisfies, for every witness selection,

    sum_i min(lambda*(i), a) >= |S_a| - (5a+3)D - O(a^2)
                             = (8/3)a^3 - (5a+3)D - O(a^2),

using the exact rank sizes `N_q = M_a - q^2` (`q<=a`), so
`|S_a| = a M_a - a^3/3 - O(a^2)`.  *Proof.*  Assign each `i` a
`lambda*`-realizing run; rightward assignments charge only `C_alpha<=4a+3`,
the `O(a)` leftward tail charges `C_beta<=4a+3`.  Run inequality:
`min(w_i,a) <= min(lambda*(i),a) + t_i`, `sum t_i <= (4a+3)D`.  Lemma B at
cap `a` gives `|S_a| <= sum_i min(w_i,a) + aD`.  Combine.  QED.

**Corollary (beta >= 8/9 rigidity).**  [PARTIALLY RETRACTED — only the
capped-average form survives; the pointwise "around almost every index"
reading is unproved.  See 8d.2(1).]  If `D=o(a^2)` then the average of
`min(lambda*(i),a)` is at least `(8/9-o(1))a`.  Hence in any near-width
order, around almost every index every internal run within span `Theta(a)`
is LONG: length `>=(8/9-o(1))a` (up to a vanishing fraction of indices).
A length-`L` internal run is a coordinate plateau-local-max, i.e. `L+1`
consecutive positions **on one line** of the hexagon with the cross
coordinate monotone (any interior cross local max/min creates a singleton
run, `lambda=0`, since points on a line have distinct cross values).

Immediate kills (all previously open in the relaxed regime): boustrophedon
x-line sweeps (seam hilltops have plateau <=2, so cost `O(a^2)`, forcing
`D>=Omega(a^2)`); concentric rings (plateau ~ radius `s`; cost
`~2a^3 < (8/3)a^3`); the nested `O_a` and side-batched orders (already
killed by C1/C2, reconfirmed).

**Dichotomy replacing Conjecture D.**  Either
(i) there is an order with `sum_i min(lambda*(i),a) >= (8/3-o(1))a^3` —
necessarily "dear lawnmower"-like: long monotone line segments
(`Theta(a)`-plateaus) at every coordinate reversal, e.g. serpentine x-line
passes whose y-max/z-max turns ride y-lines/z-lines for `~(8/9)a` steps —
and every such order is the unique surviving candidate geometry for the
three-box route (this matches, and sharpens to the heterogeneous metric,
the audited macroscopic-desert prediction); or
(ii) no order reaches `(8/3-eps)a^3`, and then `D=Omega(a^2)` universally,
i.e. `g_3(2a,2a,2a) >= width + Omega(a^2)`, killing the three-box route
even in the relaxed Theorem-A form (`c<2`).

CORRECTIONS to Theorem F as first stated (audit pass 2): the charge constant
is `(9a+4)D`, not `(5a+3)D` — rightward assignments have span `<=4a+2` so
`C_alpha<=4a+2`; the `O(a)` leftward tail gives `C_beta<=4a+2`; Lemma B adds
`aD`.  Conclusion unchanged: `(8/3)a^3 - O(a^2) <= sum_i min(lambda*(i),a)
+ (9a+4)D`.  Also `|S_a| = sum_{q=1}^a (M_a - q^2)` exactly (rank sizes
`M_a-q^2` valid for `q<=a`; checked at `a=1`).

**Sharpenings (pass 2, all elementary given E/F):**

* **Random/jumpy orders need `D=Omega(a^2)`.**  A singleton interior
  plateau-max (`xi_{j-1}<xi_j>xi_{j+1}`) is an internal run with
  `lambda=0`.  In a uniformly random order such singletons occur within
  distance `O(log a)` of every index whp, so `sum min(lambda*,a)=o(a^3)`
  whp, and Theorem F gives `D=Omega(a^2)` whp.  This strictly strengthens
  the audited random-order bound `Omega(a^{3/2})` and the C4 heuristic.
* **Direction (i) reduces to an all-long-max order.**  If an order of
  `H_a` has every interior plateau-local-max of every coordinate of length
  `>= a`, then every avoiding internal run in every span-window has length
  `>=a`, so `min(lambda*(i),a)=a` for all `i` in range and
  `sum = a M_a - O(a^2) = 3a^3 - O(a^2) > (8/3)a^3`: the necessary
  condition of Theorem F is satisfied with room `a^3/3`.  Conversely any
  short interior max poisons the `~4a` indices spanning it.  So the crisp
  existence question is:

  > **Q1.** Does `H_a` admit an order in which every interior
  > plateau-local-max of every coordinate has plateau length `>= a`
  > (equivalently: every internal maximal upper-threshold run has
  > `>= a` positions)?  Quantitative version: what is
  > `sigma(a) = max_orders sum_i min(lambda*(i),a)`?
  > `sigma(a) <= (8/3-eps)a^3` kills the three-box route (even relaxed);
  > an all-long-max order is the unique candidate geometry if it exists.

* **Forced structure for all-long-max orders (proved):** (a) plateaus of
  two different coordinates share at most one position (two coords constant
  = same point), so nontrivial plateaus are near-disjoint; (b) within a
  plateau of `xi`, the cross coordinate takes distinct values, so interior
  cross-maxes are singletons — hence the cross coordinate must be
  **monotone** on every nontrivial plateau (jumps allowed, monotonicity
  forced); (c) [CORRECTED after machine check] every interior block of the
  top line `xi=a` is a local max, so the top line (`a+1` points) occurs as
  one block, or as one interior block of length `>=a` plus at most one
  word-boundary block (two interior blocks impossible: `2a>a+1`, `a>=2`);
  the `a=3` solution realizes the split case; (d) every interior block of
  `xi=a-1` shorter than `a` must be word-adjacent to an `xi=a` position.
* Spiral/concentric order estimate under F: ring `s` sides are plateaus of
  length `s+1`, so `sum min(lambda*,a) ~ sum_s 6s*min(s,a) = 2a^3+O(a^2)
  < (8/3)a^3`, giving `D=Omega(a^2)` for contiguous rings — consistent
  with and stronger than the audited ring obstruction.  (Machine check
  pending.)
* Boustrophedon x-line serpentine: hilltop seams give y-plateau-maxes of
  length ~2, densely — `D=Omega(a^2)`.  (Machine check pending.)

Next computation: (1) DFS existence search for all-long-max orders at
`a=2` (19 points, plateaus `>=2`), with the forced-structure pruning; (2)
lambda*-profiler for explicit orders (`fable_general_case/`).

## 8b. Q1 resolved positively at small a; the windmill geometry; next gate

**Computation (fable_general_case/all_long_max_search.py, DONE).**
All-long-max orders EXIST at `a=2` (19 pts, 5.3k DFS nodes) and `a=3`
(37 pts, 214k nodes); independently re-audited by a separate plateau scan.
At `a=4`, randomized DFS reached depth 60/61 (355M nodes, timed out one
point short; `alm_a45.log`) — suggestive, no certificate.  So fork branch
(i) is nonempty at small `a`: Theorem F does not by itself kill the
three-box route; the kill must come from the labeled/deep-entry ledger
(Corollary H direction) applied to the windmill class.
Structure census of the `a=3` solution: plateau counts 22/27/27
(`sum=76 >= 2M+1`), 4 peaks per coordinate (`~a+1`), cross-coordinate
strictly monotone inside every nontrivial plateau — matches forced
structure (a),(b); top-line split case for `z` (see corrected (c)).

**Observed structure (both solutions).**  The order is a chain of
"rides": maximal word-plateaus of one coordinate, i.e. consecutive
positions on one line `{xi=c}` with the cross coordinate strictly
monotone (forced: an interior cross local-max inside a ride is a
singleton peak).  Interior-peak rides have length `>=a` (minimally
compliant: lengths exactly `a`, `a+1` occur); peaks cycle x,y,z with
slowly descending values (a "windmill").  Rides may skip line points
(cross coordinate jumps by >1) — skipped points are absorbed by other
rides.  Top lines `xi=a` occur as one monotone block each (forced (c)).

**Key reduction observation (to prove next).**  Inside a ride `x=c` of
length `~w~a`, every position `p` is covered by `~w` witness intervals of
on-line middle targets `(c, y_j, -c-y_j)`, so its entry satisfies
`A_p <= G_p = (c, y_{jL(p)}, -c - y_{jR(p)})` with `jR-jL ~ w`: the `x`
component is capped at the constant `c` while `y`,`z` caps move
monotonically.  Hence deep-zone entries live in a 2-dimensional geometry
(`y,z` free-ish under moving caps, `x <= c` frozen).  The below-middle
targets realizable from an avoiding window there form the downset of a
mixed cap `(c, maxG_y(J), maxG_z(J))`; rank `-1` is achievable only at
exact tightness (`|J| ~ w`, aligned gaps).  Within one ride the
realization problem restricted to the on-line down-set is a TWO-chain box
problem, where `g_2(p,q) >= p+q` versus width `p+1` is the audited linear
obstruction.  There are `~3a` rides; a per-ride linear defect that cannot
be shared across rides would give `D = Omega(a^2)` for every all-long-max
order, which with Theorem F (killing all other orders) would prove

    g_3(2a,2a,2a) >= width + Omega(a^2)   for ALL orders,

closing the three-box route even in the relaxed Theorem-A regime.  The
danger to this plan (why it is NOT yet a theorem): below-targets are
shared between rides (a target's realization may sit near any ride whose
caps dominate it), and entries are multiplexed (one entry serves many
intervals).  The counting must therefore be done at the level of
per-coordinate ACHIEVEMENTS (entry p achieves value v on coordinate c for
target U if `A_p(c) = U_c = v`), with the cap constraint
`A_p(c) <= G_p(c)` localizing high-value achievements:
values `v in (a - w, a]` of coordinate `x` are achievable only inside
`x=c` rides with `c >= v` or within `~w` of the ends of cross rides
passing the `x=v` region, plus `<= D` free-agent (uncovered) positions.

**Lemma G (free positions and caps — PROVED).**  For any covering word and
selected middle witnesses in normal form: (i) the number of positions of
`[1,N]` contained in no selected witness interval is at most
`alpha_1 + sum_i max(0, alpha_{i+1}-beta_i) + (D-beta_M) <= D`
(pre-`ell_1` positions `= alpha_1`; hole after `i` is
`max(0, alpha_{i+1}-beta_i) <= alpha_{i+1}-alpha_i`; tail `= D-beta_M`;
telescope and use `alpha_M <= beta_M`).  (ii) Every covered position `p`
has entry `A_p <= G_p := meet{ T_i : p in I_i }` (each entry of `I_i` is
`<= T_i`).  Consequently an entry with `c`-component `>= v` exists only at
one of `<= D` free positions or at a position all of whose covering
witnesses have `T(c) >= v` — high-value achievements are localized to
deep interiors of consecutive high-`c` witness runs plus `D` free agents.

**Corollary H (literal middle rows are dead — PROVED; width-density
sentence RETRACTED and first bound superseded by the sharper `D >= M_a-1`
of 8d.1).**  If every middle
target of `[0,2a]^3` occurs as a literal entry of the word, then selecting
the singleton witnesses gives `w_i=0` for all `i`, and Lemma B at cap `a`
yields `|S_a| <= aD`, i.e.

    D >= |S_a|/a = (8/3 - o(1)) a^2.

More generally, if a fraction `theta` of middle targets are witnessed by
intervals of width `< h`, then `|S_h| <= (1-theta) h M_a + theta h' M_a + hD`
— quantitatively, near-width words must witness almost every middle target
by an interval of width `>= (8/9-o(1))a` and almost never literally.  This
kills the entire "occurrence row + repairs" architecture (all audited
band/spiral/corner SAT families) in one line, independently of the order
used, and explains those dead searches retroactively.  It also means the
windmill/all-long-max branch must realize middle targets as joins of
`~a`-long intervals of strictly-below entries; the construction problem is
about DEEP entries, not middle rows.

**Next lemma target (the labeled gate).**  A per-window labeled-capacity
lemma extending Lemma B: for a fan/window family, bound the number of
distinct below-targets whose full coordinate label set is achievable,
in terms of entry achievements; then a global ledger summing over rides.
Expected outcome either `D=Omega(a^2)` universally (route closed) or an
explicit sharing/multiplexing scheme (construction blueprint).  Middle
realization already pins per-witness "fresh head/tail" entries
(`T_j`'s `y_j` must be achieved at `p in [r_{j-1}+1, r_j]`, its `z` at
`p in [ell_j, ell_{j+1}-1]`), so entry freedom is limited — the labeled
ledger has real teeth.  All of 8b beyond the computation is CONJECTURAL
except: (b)-monotonicity within rides, (c) top-line single-block, both
proved in 8a; and the existence results.

## 8c. Run-spectrum law and the forced staircase geometry
## [SUPERSEDED BY 8d — capped-sum inequality survives in corrected form;
##  all concentration/staircase/handoff/transportation claims RETRACTED]

**Theorem I (run-spectrum law — PROVED, second pass pending).**  Let a word
cover `[0,2a]^3` with excess `D=o(a^2)`.  Fix any witness selection and any
assignment `i -> R_i` of internal avoiding runs within one-sided span
`sigma=O(a)` (exists by Theorem E), `lambda_i = |R_i|-1`.  Then for EVERY
`h <= 3a-1` simultaneously:

    Def(h) := sum_i (h - lambda_i)_+  <=  h*M_a - |S_h| + O((a+h)D),

where `|S_h| = sum_{q=1}^{h} N_q`, `N_q = M_a - q^2` for `q<=a`,
`N_q = C(3a-q+2,2)` for `a<q<=3a`.  *Proof:* Lemma B at cap `h` gives
`|S_h| <= sum_i min(w_i,h) + hD`; the audited run inequality gives
`min(w_i,h) <= min(lambda_i,h) + t_i`, `sum t_i <= 2*sigma*D`; and
`sum_i min(lambda_i,h) = h*M_a - Def(h)`.  QED.

Key values: `h<=a`: budget `h^3/3 + O(aD)` (very tight at small h).
`h=3a`: budget `5a^3 + O(aD)`, equivalently
`sum_i min(lambda_i,3a) >= 4a^3 - O(aD)`: **average capped avoiding-run
length >= (4/3 - o(1))a.**

Consequences (all PROVED given Theorem I):
* Minimal windmill (all runs length `a`): spends `Def(3a)=6a^3 > 5a^3`
  => `D=Omega(a^2)`.  All-long-max at threshold `a` is NOT sufficient;
  the a=2,3 solutions of 8b die as word-orders.  Q1's threshold was too
  weak; correct threshold is `(4/3)a`.
* Rings: `sum min(lambda,3a) ~ 2a^3` => dead (reconfirms audit, stronger).
* Random orders: singleton peaks whp everywhere => `D=Omega(a^2)` whp.

**Theorem J (neighbor-exceedance forcing — PROVED).**  For consecutive
positions p,q (q=p+1) in the target order and any coordinate c with
`q_c > p_c`: the maximal run of threshold `c >= p_c+1` containing q avoids
p, is within span its own length+1, and hence (Theorem I) for all but
`o(a^2)` indices it must have length `>= (4/3-o(1))a` — OR be
boundary/exceptional.  Moreover for every p some neighbor exceeds p in some
coordinate (else the window would repeat the point p).

**Forced geometry (staircase windmill).**  Combining I+J with plateau
structure (8a): up to `o(a^3)` total deficiency, a surviving target order
must be a sequence of **rides** — monotone segments on coordinate lines —
with: (1) ride length `>= (4/3-o(1))a` (so ride levels `|v| <= (2/3+o(1))a`);
(2) at most ONE ride per line (two need line length `>= (8/3)a > 2a+1`);
(3) hence `<= ~4a` candidate lines, `~(9/4)a` rides, and rides PARTITION
the hexagon (ride mass `(9/4)a * (4/3)a = 3a^2 = M_a`: no slack for
non-ride positions beyond exceptions);
(4) **3-phase cyclic handoff**: each ride's rising cross coordinate becomes
the next ride's level, at its ending value (else the tail indices of the
ride see a short exceedance run: poisoned); level coords cycle
x->y->z->x or the mirror; the falling coordinate must not jump up at seams;
(5) each coordinate's value trajectory is: hold L (as level), fall ~L (as
falling cross, jumps allowed), rise ~L (as rising cross, jumps allowed),
repeat — a drifting 3-phase trapezoid wave;
(6) exact line-coverage: for every line (c,u): (holds at u: length) +
(# sweeps visiting u) = 2a+1-|u| exactly (partition), giving a coupled
exact-cover/transportation problem (x-fall span and z-rise span on a
y-ride are complementary: z = -v_y - x).

**Status of the fork after 8c.**  The three-box route now lives or dies on:

> **Q2 (staircase existence).**  Does the hexagon admit a partition into
> `~(9/4)a` monotone line-rides of length `>= (4/3)a` (levels
> `|v| <= 2a/3`, <= 1 ride/line), sequenceable in one word order with the
> 3-phase handoff and seam-continuity constraints, meeting the exact
> line-coverage equations?  Crude mass/coverage estimates are feasible
> (capable-line mass `6.67a^2 > 3a^2`; sweep-coverage balances at levels
> `|u| ~ a/2`, needs jump-widened sweeps near `u=0` and hold placement
> optimization) — genuinely open in both directions.

If Q2 is NO (with quantitative version): every order has
`sum min(lambda,3a) < 4a^3 - eps*a^3` => `D = Omega(a^2)` universally =>
`g_3(2a,2a,2a) >= width + Omega(a^2)` => **three-box route dead even in
relaxed Theorem-A form**; pivot to wreaths/four-box carrying Lemma B
(which is lattice-general and transfers to the Boolean middle-layer:
consistency check — MSW wreath traversals have `w_i ~ 2H` uniformly and
pass Lemma B with room).
If Q2 is YES: the staircase is the UNIQUE candidate geometry; next gates
are pins/Hall/upper-shadow completion on that explicit object (Lemma B is
necessary-only; existence of the order does not yet give a word).

Caution ledger for 8c: Theorem I needs one more congestion audit at the
`O((a+h)D)` term (constant chase, no structural risk); Theorem J's
"o(a^2) exceptions" bookkeeping inherits Theorem I's; the handoff forcing
(4) is proved for indices in the tail stretch of each ride via the
exceedance run being cut short at a non-conforming seam.

**8c.1 Definitional correction (span restriction) and the L-window.**

* `lambda*(i)` MUST be defined with one-sided span `<= sigma = O(a)`
  (Theorem E guarantees `sigma = 4a+2`); the assignment congestion, hence
  the `O((a+h)D)` term, is only controlled for span-bounded runs.  The 8b
  profile computation and the first annealing test used UNBOUNDED span and
  are invalid as stated (unbounded-span `lambda*` is 0/1/2 for essentially
  every order because some singleton exists somewhere; it certifies
  nothing).  The 8b histograms are retracted; small-`a` profiles are
  non-asymptotic anyway (`4a+2 > M_a/2` at `a=2`).
* Consequently the correct criterion: an order survives Theorem I iff for
  all but `o(a^2)` indices, EVERY internal run within span `O(a)` has
  length `>= (4/3-o(1))a` on average in the capped sum (long-run design
  goal), and dies iff the span-`O(a)` capped run supply is short.  In an
  idealized staircase every maximal superlevel run of every coordinate
  contains a full hold (the 3-phase handoff makes each coordinate's local
  maximum equal to its next hold value), so span-local runs have length
  `>= L`: the staircase passes iff `L >= (4/3-o(1))a`.
* Mass/line feasibility window for the hold length: one ride per line for
  `L > a+1/2`; usable levels `|v| <= 2a+1-L`; requiring
  `(3a^2)/L <= 6(2a-L)+O(1)` gives `2L(2a-L) >= a^2`, i.e.
  `L <= (1+1/sqrt2)a ~ 1.707a`.  So the design window is
  `L in [(4/3)a, 1.707a]`: at `L=(4/3)a` the capped sum is EXACTLY
  critical (`4a^3`), while `L=1.5a`-`1.7a` gives genuine slack
  (`4.5a^3`-`5.1a^3` vs needed `4a^3`), at the cost of tighter
  line-coverage equations (fewer sweeps must cover more line mass).
  So Q2 is NOT razor-edged in the capped-run metric; the binding
  constraints are the exact line-coverage/transportation equations and
  seam continuity.

## 8d. CORRECTION AND RETRACTION after FABLE_RUN_SPECTRUM_AUDIT.md

The independent audit (`FABLE_RUN_SPECTRUM_AUDIT.md`, read in full) certifies
the capped-sum core of 8c and refutes the concentration layer built on it.
This section is the authoritative statement; where 8a/8b/8c conflict with it,
**8d governs**.

### 8d.1 What survives (corrected statements)

* **Theorem I (run-spectrum inequality) — PROVED, corrected form.**  For any
  covering word, any witness selection, any assignment of internal avoiding
  runs with one-sided span `<= sigma` (convention: `v_i+1-i <= sigma` for
  forward runs, `i-(u_i-1) <= sigma` backward), and every `h <= 3a-1`
  simultaneously:

      Def_R(h) = sum_i (h - lambda_i)_+  <=  B_a(h) + (2*sigma + h) D,

  with the exact budget `B_a(h) = sum_{q=1}^h (M_a - N_q)`;
  `B_a(h) = h(h+1)(2h+1)/6` for `h <= a`;
  `B_a(3a-1) = 5a^3 + (3/2)a^2 - (3/2)a`.  No `D=o(a^2)` hypothesis needed.
  The universal span constant is `sigma = 4a+3` (off-by-one corrected:
  Theorem E's window `[i+1, i+4a+2]` gives `v+1-i <= 4a+3`); its error
  coefficient at `h=3a-1` is `11a+5`.  Subset form: unassigned indices
  count as `lambda_i = h`.
* **Average spectrum — PROVED.**  If `D=o(a^2)`:
  `(1/M_a) sum_i min(lambda*_sigma(i), 3a-1) >= (4/3 - o(1)) a`, where
  `lambda*_sigma(i)` is the minimum cost among span-`sigma` internal
  avoiding runs at `i`.  This is a statement about the AVERAGE of the
  pointwise minima — nothing more.
* **Exceptional-set bound — PROVED.**
  `#{ i : lambda*_sigma(i) <= t } <= (B_a(h) + (2sigma+h)D)/(h-t)` for every
  `t < h`.  At `t = Theta(a)` thresholds this right side is `Theta(a^2)`,
  NOT `o(a^2)` — this is exactly why the concentration claims fail.
* **Corollary H, distributional form — PROVED.**  If `K` middle witnesses
  have width `<= r < h`, then `K(h-r) <= B_a(h) + hD`.  Sharp special
  cases: literal witnesses (`r=0`, `h=1`) give `K <= D+1`, hence
  `D >= M_a - 1 = 3a^2+3a` for a fully literal middle row (stronger than
  the `(8/3)a^2` stated in 8b, which was correct but not sharp).
* **Neighbor-exceedance lemma — PROVED, local scalar form only.**  For
  consecutive middle targets with `q_c > p_c`, the maximal component of
  `{T_j(c) >= p_c+1}` containing `q` starts at `i+1`, avoids `i`, and has
  one-sided span `lambda+2` (corrected from `lambda+1`).  Aggregate form:
  if `K_t` indices carry internal exceedance runs of cost `<= t <= sigma-2`,
  then `|K_t| <= (B_a(h)+(2sigma+h)D)/(h-t)` for every `h > t`, plus an
  `O(a)` boundary correction (at most `6a` per orientation).
* **Theorem K (long corridors — proved in UNIVERSAL_CAPPED_RUN_COVER.md,
  imported).**  For fixed `0<delta<4/3` and `D=o(a^2)`: at least
  `(3delta/(2/3+delta) - o(1)) a^2` forward windows have min internal
  peak-plateau cost `> (4/3-delta)a`; hence `Theta_delta(a)` distinct
  directed peak plateaux of length `> (4/3-delta)a` on central lines
  (`|level| < (2/3+delta)a + O(1)`), pairwise edge-disjoint, occupying
  `Omega_delta(a^2)` mass; for `delta<1/3` no two share a geometric line.
  A positive-density CORRIDOR PACKING — not a partition.

### 8d.2 What is RETRACTED (unproved, some refuted as inferences)

1. **8a "Corollary (beta >= 8/9 rigidity)", pointwise part:** "around almost
   every index every internal run within span Theta(a) is LONG" — retracted.
   Only the capped AVERAGE `(1/M_a) sum min(w_i,a) >= (8/9-o(1))a` is proved.
2. **8b Corollary H, width-density sentence:** "almost every middle target
   witnessed by width `>= (8/9-o(1))a`" — retracted; replaced by the
   distributional bound above.  The abstract spectrum `1/3` at `2a/3`,
   `2/3` at `2a` passes all capped inequalities with a positive fraction
   far below `8a/9`.
3. **8c "all but o(a^2) indices have runs >= (4/3-o(1))a":** refuted as an
   inference.  The audit's counterexample spectrum — `3/5` of indices at
   `lambda=a`, `2/5` at `lambda=2a` — satisfies the ENTIRE spectrum
   inequality family (all caps `h`) at leading order while a majority of
   indices sit at cost `a < (4/3)a`.  Any theorem excluding it must use
   geometric information beyond Theorem I.
4. **Theorem J, global forcing step:** retracted.  The local lemma survives
   (8d.1); the "hence all but o(a^2) seams conform" step does not.  Note
   also: an exceedance run is a superlevel component, generally NOT a
   constant-coordinate plateau/ride — the identification of long runs with
   line rides was an unproved step.
5. **The forced staircase geometry (8c items (1)-(6)):** ride partition,
   `<=1` ride/line as a general fact (proved only for plateaux longer than
   `a+1/2`), the `~(9/4)a` ride count (circular: assumed the partition),
   3-phase cyclic handoff, trapezoid waves, exact line-coverage
   transportation equations — ALL now CONJECTURAL.  The `L in
   [(4/3)a, 1.707a]` design window is a feasibility computation INSIDE the
   conjectural partition model, not a constraint on surviving orders.
6. **"Q2 is the fork":** retracted as stated.  The staircase is one
   possible extremal geometry, not the unique survivor.
7. **Ring-order and random-order `Omega(a^2)` claims (8a/8c):** remain
   PENDING/HEURISTIC respectively, as originally marked; 8c wrongly
   promoted them.  (Random: Theorem I proves the implication from a cheap
   whp run cover; the cover's existence proof is still missing.
   `SHORT_PEAK_DENSITY.md` exhibits an order where only `3/8+O(1/a)` of
   universal windows contain a peak of cost `<= a`, independently killing
   the "high short-peak density everywhere" shortcut.)
8. **8b/8c small-`a` profile computations:** the unbounded-span
   `lambda*` histograms were already retracted in 8c.1; additionally the
   staircase capped-run-sum computations (ratios 0.13-0.34) used the
   correct span but tested hand-built orders only — they say nothing about
   the class of all orders and are demoted to exploratory data.

### 8d.3 The corrected open gate

Per the audit (Section 8), the genuinely mathematical next gate is a
**transition lemma** for the corridor-packing class of Theorem K:

> Either every positive-density packing of long directed central-line peak
> plateaux creates, near its joins, enough short non-peak threshold
> components to admit a heterogeneous run assignment of capped cost
> `<= (4-eps)a^3` (killing `D=o(a^2)` via Theorem I), or such packings obey
> a rigorously stated global braid law (the rotating-braid alternative).

A pointwise-concentration route to this is hopeless (8d.2 item 3); what is
needed is a DISTRIBUTIONAL / interval-service theorem: control how the
budget `B_a(h)` is spent across caps `h` simultaneously by tying each
short-run supply to the geometric joins it serves.

## 9. Theorem L: uniform interval service (eliminates the r=Theta(a) obstruction)

Setting: word order of `H_a` in normal form, excess `D`, cap `h=3a-1`,
`L=4a+2`.  A **peak plateau** is a maximal block of consecutive word
positions on one coordinate line (`xi=t`) whose two word-neighbors have
`xi<t`; cost `lambda(P)=|P|-1`; **directed** = both cross coordinates
strictly monotone along it.  For `c in (0,2)`, call a directed internal
peak plateau with `lambda > ca` **c-dangerous**.  Forward window
`W_i=[i+1,i+L]`, backward `W'_i=[i-L,i-1]`.

### Lemma 9.1 (window dichotomy — PROVED)

All windows/runs live in the middle-target order index space `[1, M_a]`.
For any `c in (0,2)` and any `i` with `W_i subseteq [1,M_a]`: either `W_i`
contains a COMPLETE c-dangerous plateau, or `W_i` contains an internal
maximal threshold run avoiding `i` of cost `<= ca`.  Symmetrically for
`W'_i`.

*Proof.*  Theorem E (constant-coordinate form) puts a complete internal
peak plateau `P* subseteq W_i`.  If `lambda(P*)<=ca`, done.  If `P*` is
not directed, some cross coordinate has an interior strict local extremum
along `P*`; a local max of a cross coordinate (or, for a local min, of the
complementary cross coordinate) is a SINGLETON internal maximal threshold
run (its word-neighbors lie on `P*` with strictly smaller cross value),
contained in the interior of `P*`, cost 0.  Otherwise `P*` is directed
with `lambda(P*)>ca`: a complete c-dangerous plateau inside `W_i`.  QED.

### Theorem L (uniform interval service — PROVED but SUPERSEDED, see §10.1:
### duplicate of the weaker relaxation of FIRST_DANGEROUS_GLOBAL_SERVICE
### Theorem 1, which achieves 2e_c+H_c in place of (4-c)e_c)

Fix `c in (0,2)`.  For every order there is a heterogeneous internal-run
assignment, all runs avoiding their index, one-sided spans `<= 4a+3`
(every assigned run, including `F(i)`, is contained in `W_i`, so its end
is `<= i+L`; hence `C_alpha, C_beta <= 4a+3`), with the last `L` indices
counted at the cap, such that

    Q := sum_i min(lambda_i, 3a-1)
       <= ca*M_a + sum_{P c-dangerous} (lambda_P - ca)(L - lambda_P)
          + (4a+2)(3a-1)
       <= [3c + (4-c) e_c] a^3 + K_c a^2,

where `e_c := (1/a^2) sum_{P c-dangerous} (lambda_P - ca)`.
**No dependence on the number of braid components `r`.**

*Proof.*  For `i <= N-L`: if `W_i` has no complete dangerous plateau,
assign the Lemma 9.1 run — cost `<= ca`, span `<= L+1`.  Else let `F(i)`
be the first complete dangerous plateau in `W_i` (start `s`, cost
`lambda`); assign `F(i)`: it is an internal maximal threshold run (its
word-neighbors have strictly smaller line coordinate), starts after `i`
so avoids `i`, and `end+1-i <= L+lambda+1 <= 6a+3`.  For `i > N-L`, count
`lambda_i = h`.  Service count: `i` has `F(i)=P` only if
`P subseteq W_i`, i.e. `s+lambda-L <= i <= s-1`: at most `L-lambda`
indices per plateau, disjointly (first-plateau rule).  Hence

    Q <= ca(M_a - X) + sum_P lambda_P * |serv(P)| + L*h
      <= ca*M_a + sum_P (lambda_P - ca)(L - lambda_P) + L*h,

using `lambda_P > ca` and `|serv(P)| <= L-lambda_P`.  Since
`L - lambda_P < (4-c)a+2`, the excess term is
`<= ((4-c)a+2) * e_c a^2 = (4-c) e_c a^3 + O(a^2)` (the number of
c-dangerous plateaux is `<= (M_a-1)/(ca+1) = O(a)` by disjointness of
plateau edge sets, absorbing the `+2`).  And `ca*M_a = 3c a^3 + O(a^2)`.
Spans bound congestions by the audited span-to-congestion step.  QED.

### Theorem L' (two-sided refinement — PROVED)

Same setting, both windows.  Call `i` **doubly blocked** if `W_i` AND
`W'_i` each contain a complete c-dangerous plateau (boundary indices
`i <= L` or `i > N-L` counted at cap).  Assigning backward Lemma-9.1 runs
where the backward window is dangerous-free (and forward ones
symmetrically), cost above `ca` is paid ONLY at doubly blocked indices:

    Q <= ca*M_a + sum_{i in DB} (lambda(F(i)) - ca) + 2L*h + O(a^2).

Each doubly blocked `i` lies in `serv(F(i))` (`<= L - lambda(F(i))`
indices) AND within `L` of a complete dangerous plateau on its left; a
fixed plateau `P'` has at most `O(1/c)` dangerous plateaux starting in
the `2L` positions before it (each needs `> ca+1` positions).

### Corollary S (forced plateau spectrum — PROVED)

If `D = o(a^2)`, then for every fixed `c in (0, 4/3)`:

1. `e_c >= (4-3c)/(4-c) - o(1)`.
   *Proof:* Theorem I at `h=3a-1` (`|S_h|=V_a=4a^3+O(a^2)`, congestion
   term `O(aD)=o(a^3)`) against Theorem L.  QED.
2. `sum_{i in DB}(lambda(F(i)) - ca) >= (4-3c)a^3 - o(a^3)`; since each
   term is `< (2-c)a`, at least `((4-3c)/(2-c)) a^2 - o(a^2)` doubly
   blocked indices, and hence at least `((4-3c)/((2-c)(4-c))) a - o(a)`
   **clustered pairs**: ordered pairs of c-dangerous plateaux within
   word-distance `2L` of each other.  At `c=1`: `>= a^2` doubly blocked
   indices and `>= a/3 - o(a)` clustered pairs.
3. Specific evaluation at `c=1`: 1-dangerous plateaux (length `> a`)
   occupy distinct coordinate lines (two disjoint blocks of `> a+1`
   points do not fit in `<= 2a+1`), so at least `e_1 a^2 / a = a/3 - o(a)`
   DISTINCT lines each carry one directed peak plateau longer than `a`,
   with levels `|t| < a`.

Scope notes.  (i) These are distributional statements about the plateau
LENGTH SPECTRUM and pair clustering — no pointwise concentration is
claimed anywhere; this is the replacement demanded by
FABLE_RUN_SPECTRUM_AUDIT.  (ii) Theorem L supersedes the interface
accounting `(2-c)aU + 2aV = O(a^2 r)` of BRAID_GAP_SERVICE Theorem 1 and
resolves its first open item (uniform behavior at `r=Theta(a)`): the
component count `r` no longer appears; what remains open is purely the
spectrum question.  (iii) The transparent-separator family of
BRAID_GAP_SERVICE Section 7 is consistent: its separator indices are
doubly blocked and pay their excess inside the `e_c` term.  (iv) The
abstract counterexample spectrum of the audit (3/5 of indices at run
cost `a`, 2/5 at `2a`) constrains INDEX run costs; Corollary S constrains
PLATEAU excess mass — finer geometric information not available from
Theorem I alone.

### 9.3 Theorem M (assignment-free window-cost form — PROVED)

For index `i` (with `W_i` in range) let

    q_i = min{ lambda_eff(P) : P a complete internal peak plateau in W_i },

where `lambda_eff(P) = lambda(P)` if `P` is directed and `= 1` otherwise
(Lemma 9.1: a non-directed complete peak plateau contains an internal
singleton run of a cross coordinate).  Theorem E: the set is nonempty, so
`q_i <= 2a`.  The first-complete-plateau assignment realizes cost `q_i`
with span `<= 4a+3`, so Theorem I gives, for `D=o(a^2)`:

    sum_i min(q_i, 3a-1) >= 4a^3 - o(a^3).

Equivalently, with `n(t) = #{ i : q_i > t }` and
`serv(P) = { i : P complete in W_i }` (an interval of `L - lambda(P)`
window-starts):

    int_0^{3a} | Union_{P : lambda_eff(P) <= t} serv(P) | dt
        <= 3a M_a - 4a^3 + o(a^3) = 5a^3 + o(a^3).

**Interpretation (the distributional law):** cheap plateaux (short
directed, or any non-directed) may cover at most `5/9 + o(1)` of the
index-threshold rectangle `[1,M_a] x [0,3a]` with their service
intervals; cheapness must be CLUSTERED in the word.  This is the
audit-compliant replacement for all retracted pointwise statements: it
constrains the joint distribution of (plateau cost, plateau position),
nothing pointwise.

**Recorded negative results (why single-threshold counting cannot close
the fork):**

1. Edge-budget check at one threshold `t`: plateaux of cost `> t` number
   `<= 3a^2/t` (disjoint edge sets), and each serves `L - t >= 2a`
   starts, so they can serve `>= 6a^3/t >= M_a` indices for all
   `t <= 2a`: the edge budget alone never contradicts `n(t) ~ M_a` at
   any single threshold.
2. Raw spectrum check: `sum_P lambda(L-lambda) >= 4a^3` with
   `sum_P lambda <= 3a^2` is satisfiable with huge slack (dust spectra
   give `~12a^3`).  Hence no assignment-free single-scale inequality
   closes the route; the missing content is the COUPLING between
   thresholds forced by word geometry (level ledger), exactly as in the
   multiscale proposal of BRAID_GAP_SERVICE Section 6.

### 9.3a Theorem N (master service inequality and the supply law — PROVED)

For `i <= M_a - L` let `q_i = min{ lambda_eff(P) : P complete peak plateau
in W_i }` (`lambda_eff = lambda` if directed, `= 1` if not; nonempty by
Theorem E; `q_i <= 2a`).  The first-complete-plateau assignment realizes
`min(q_i, 3a-1)` with span `<= 4a+3` (non-directed plateaux via their
interior singleton, cost 0).  Theorem I (subset form, `h=3a-1`,
`D=o(a^2)`) gives `sum_i min(q_i, 3a-1) >= 4a^3 - o(a^3)`.  Writing
`n(t) = #{i : q_i > t}` and, for `t >= 1`,

    supply(t) = sum_{P directed peak plateau, lambda(P) > t} (L - lambda(P)),

we have `n(t) <= min(M_a, supply(t)) + O(a)` (each qualifying `i` lies in
`serv(P)` of every — in particular some — plateau in its window, and all
plateaux in its window are directed with `lambda > t`).  Integrating:

    MASTER:  int_0^{2a} min(M_a, supply(t)) dt >= 4a^3 - o(a^3).

Normalized (`t=ca`, `s(c)=supply(ca)/a^2`, `M_a ~ 3a^2`):
`int_0^2 min(3, s(c)) dc >= 4 - o(1)`.  Since `s` is nonincreasing and
`min(3,s) <= 3` pointwise, `(2-c) min(3, s(c)) >= 4-3c`, giving the

    SUPPLY LAW:  s(c) >= (4-3c)/(2-c) - o(1)   for every fixed c in (0, 4/3).

Consequences: `F(c) := #{directed peak plateaux longer than ca}
>= ((4-3c)/((2-c)(4-c))) a - o(a)`; at `c=1`: `supply >= a^2 - o(a^2)`
and `>= a/3 - o(a)` plateaux longer than `a`, necessarily on distinct
coordinate lines.  At `c -> 4/3` the law degenerates to 0 — consistent
with the audit's counterexample spectrum; nothing is forced beyond `4/3`.
Theorem N implies both Theorem L's corollary (`e_c >= (4-3c)/(4-c)`) and
the count law; it is the sharpest assignment-free form.

**Satisfiability analysis (recorded, honest).**  The full constraint
system now provable — MASTER + level capacity (`F(y) <= 6(2-y)a + 3`,
since a plateau of length `> ya` needs a line of `>= ya+1` points, level
`|t| < (2-y)a`, and long plateaux are alone on their line) + edge budget
(`sum_P lambda(P) <= M_a - 1`, all constant-coordinate plateau edge sets
being disjoint) — is SATISFIABLE by abstract spectra, e.g.
`F(y) = min(1.61a, 6(2-y)a)` with total edge mass `~3a^2` (word almost
entirely covered by dangerous plateaux), and also by lower-mass spectra
down to edge mass `~a^2`.  Tiny-plateau spectra are excluded (all
`x_j = eps` gives `int <= 3 eps < 4`).  Hence NO static counting at the
spectrum level closes the fork; what static counting has established is
that a near-width order must carry, at every threshold `c < 4/3`, a
persistent quadratic service supply of long directed line plateaux.  The
only remaining source of contradiction (or construction) is the COUPLING
between plateaux: adjacency/level ledgers (A/B turns) and their
bounded-gap extension — exactly 9.4.

### 9.4 The isolated next lemma

Corollary S(2) forces `Theta(a)` clustered pairs: dangerous plateaux
within word-distance `2L`, with dangerous-free (hence Lemma-9.1-cheap)
gaps between them of length `< 2L`.  The rotating-braid level ledger
(A/B turns, audited constant `(4+2sqrt6)/3`) applies only at literal
adjacency (`gap=0`).  The missing lemma is now precisely:

> **Bounded-gap level ledger.**  For a clustered pair `P'' -> P'` with
> dangerous-free gap `g < 2L`, either the pair satisfies a level
> inequality `lambda(P') <= t'' + t' + t''' + O(g_serviced)` analogous to
> the A-turn Lemma 3 of ROTATING_BRAID_ANALYSIS, or the gap supplies
> short threshold components servicing `Theta(a)` additional indices at
> cost `o(a)` each (lowering Q below the Corollary S floor).

Either outcome sharpens Corollary S into a closed spectrum problem:
combine the level ledger with per-line uniqueness (S(3)) and the global
edge budget `sum lambda <= M_a - 1` to decide whether any length spectrum
satisfies all constraints simultaneously.  If none does:
`g_3(2a,2a,2a) >= width + Omega(a^2)` for every order and the three-box
route is closed even in the relaxed Theorem-A regime.  If one does, its
realizing geometry is the unique candidate construction.

## 9.5 The critical geometry and the seam dichotomy (new, scoped)

### 9.5.1 Windmill v2: the exact critical configuration (analysis, PROVED)

MASTER + the static budgets admit a one-parameter-tight configuration:
`~(9/8)a` directed peak plateaux of length `~(4/3)a` (levels
`|t| <= (2/3)a`, distinct lines), spaced `~(8/3)a` apart, separated by
peak-free valley gaps of length `~(4/3)a` (legal: peak-free intervals can
have length up to `4a+1` by the valley normal form of BRAID_GAP_SERVICE
§8; and a maximal threshold run wholly inside a peak-free gap would
contain its own argmax plateau — an internal peak — so peak-free gaps
contain NO wholly-interior threshold runs).  Tightness is simultaneous
and exact at leading order:

* service: each plateau serves `L - lambda ~ (8/3)a` window starts;
  `(9/8)a * (8/3)a = 3a^2 = M_a` — serv intervals must TILE `[1,M_a]`;
* window reach: from the start of one plateau to the end of the next is
  `(4/3 + 4/3 + 4/3)a = 4a <= L` — just fits;
* every index then has `q_i ~ (4/3)a` and
  `sum min(q_i, 3a-1) ~ 4a^3` — the Theorem-I floor with NO slack;
* edge mass `(3/2)a^2 <= 3a^2` and level capacity `(9/8)a <= 4a+3` are
  slack — those budgets cannot kill it.

Any `Theta(a^2)` index mass acquiring runs of cost `<= (4/3 - eps)a`
(without lengthening other plateaux) drops the sum below `4a^3` and
contradicts Theorem I at `D=o(a^2)`.  So the route closes iff cheap runs
are FORCED at a constant fraction of seams (or an analogous trade-off
kills the compensated spectra).  Conversely a windmill v2 with all seams
protected is the unique surviving candidate shape at this parameter
point.

### 9.5.2 Seam Lemma, part 1 (PROVED cases)

Setting: dangerous plateau `P'` (line `c'=t'`, directed) — peak-free gap
`I` (positions `B..E`, length `g`) — dangerous plateau `P` (line `c=t`,
directed; first point `F`, last `L_P`).  Crosses of `P`: `n` strictly
increasing, `p` strictly decreasing; so `lambda(P) <= n(L_P)+t+p(F)`
(telescoping `n`, using `p(F)+n(F)=-t`).  Peak property at both plateau
boundaries: `c'(B) <= t'-1` and `c(E) <= t-1`.  Valley property: every
coordinate is quasi-convex (nonincreasing then nondecreasing) on `I`.

**S1 (arrival singleton).**  If `p(E) < p(F)` then `{F}` is a singleton
internal maximal run of threshold `p >= p(F)` (forward neighbor on `P`
has smaller `p` by strict decrease; backward neighbor is `E`).  Cost 0.
*Consequently a protected seam must deliver the decreasing cross HIGH:*
`p(E) >= p(F)`.

**S2 (departure singleton).**  Dually at the end of `P'`: let `n'` be
the increasing cross of `P'` and `B` the first gap point.  If
`n'(B) < n'(L')` then `{L'}` is a singleton internal run of
`n' >= n'(L')`.  *Protected seams must receive the increasing cross
high:* `n'(B) >= n'(L')`.

**S3 (shared-coordinate seam kills itself when `g <= (8/3 - 2eps)a - 2`).**
Suppose the increasing cross of `P'` and the decreasing cross of `P` are
the SAME coordinate `y` (`n'=p=y`).  Let `R1` = maximal run of
`{y >= y(L')}` containing `L'` and `R2` = maximal run of `{y >= y(F)}`
containing `F`.  By strict monotonicity on the plateaux, `R1` extends
only forward of `L'`, `R2` only backward of `F`.  By quasi-convexity of
`y` on `I` with argmin `m`: `R1 subseteq [L', m)` and `R2 subseteq (m, F]`
unless one of them swallows the whole gap.  Both are internal (each ends
where `y` drops below its threshold: below the valley bottom side, and at
the plateau side by strict monotonicity).  Hence
`lambda(R1) + lambda(R2) <= g + 1`, so
`min(lambda(R1), lambda(R2)) <= (g+1)/2`.  For windmill-v2 parameters
(`g ~ (4/3)a`): a run of cost `<= (2/3)a + 1` exists at every such seam —
CHEAP.  The only escapes: `R1` or `R2` swallows the entire gap and
crosses into the far plateau, which requires (S1/S2 style)
`y(B) >= y(F)` resp. `y(E) >= y(L')` AND the far-plateau boundary/peak
conditions — recorded below as the swallow alternative.

**S4 (swallow alternative = level inequality, rotation case).**  Suppose
`p = c'` (the decreasing cross of `P` is the line coordinate of `P'`).
The run `R2` of `{p >= p(F)}` containing `F` can pass `B` only if
`p(F) <= p(B) <= t' - 1` (peak property of `P'` in its own coordinate).
In that case `R2` continues through all of `P'` (constant `t' >= p(F)`)
and is long — no cheap run, but the LEVEL INEQUALITY
`p(F) <= t' - 1` is recorded, and with the symmetric statement at the
other end (`n = c''` of the next plateau: `n(L_P) <= t'' - 1`) yields
exactly the gap-extended A-turn inequality

    lambda(P) <= t' + t + t'' - 2,

which is the literal-adjacency Lemma 3 of ROTATING_BRAID_ANALYSIS now
proved across peak-free gaps of ANY length, conditional on both swallows.
If the swallow fails (`p(F) > p(B)`), `R2` is confined to the gap's
ascending tail: `lambda(R2) <= g`.

### 9.5.3 What remains open in the Seam Lemma (honest case table)

* Case `p` = a CROSS of `P'` (not its line): `R2` passing `B` continues
  along a strictly monotone coordinate inside `P'` — it extends by up to
  `lambda(P')` more positions (if `p` decreasing along `P'` backward…
  i.e. increasing forward) or stops quickly (if decreasing forward).
  Only one of the two orientations yields a long run; the other yields
  cost `<= g + O(1)` — needs writing out with the type A/B taxonomy.
* Low-threshold escape: when `p(F)` is small the run is long for free
  and no level constraint is recorded; but smallness of `p(F)` feeds
  back into `lambda(P) <= n(L_P) + t + p(F)` — the full seam ledger must
  combine the two.  Not yet optimized.
* Non-3-cycle patterns (`c'' = c'`, repeats), word-boundary seams, gaps
  adjacent to only one dangerous plateau, and gaps of length
  `g > (8/3)a` (which windmill v2 does not use but general spectra can):
  uncovered.
* Conversion to a saving: each cheap run found serves `Theta(a)`
  window-starts within span `4a+3`; overlap/congestion of the chosen
  cheap runs across seams must be bounded (their service intervals can
  overlap adjacent seams' intervals).  Straightforward but unwritten.
* The compensated-spectrum trade-off: killing windmill v2 at its exact
  parameter point does not kill spectra that lengthen some plateaux to
  buy seam protection elsewhere.  The endgame is MASTER + seam ledger as
  a one-dimensional variational problem over spectra; not yet posed
  precisely.

### 9.5.4 Consequence if the Seam Lemma closes (conditional)

If every seam of every near-critical configuration either yields an
internal run of cost `<= (1-delta)(4/3)a` serving `Theta(a)` indices, or
pays the gap-extended A-turn level inequality, then combining the level
ledger (audited constant `(4+2sqrt6)/3 a^2 < 3a^2` for the braid mass)
with MASTER produces `sum_i min(rho_i, 3a-1) <= (4-eps)a^3` for every
order, i.e. `D = Omega(a^2)` universally:
`g_3(2a,2a,2a) >= width + Omega(a^2)`, closing the three-box route in
the relaxed Theorem-A regime.  This chain is CONDITIONAL on 9.5.3.

## 10. Reconciliation with FIRST_DANGEROUS_GLOBAL_SERVICE and MULTISCALE_DANGEROUS_PROFILE

Read in full: FIRST_DANGEROUS_GLOBAL_SERVICE.md (+AUDIT: certified) and
MULTISCALE_DANGEROUS_PROFILE.md.  Notation there: dangerous = directed
internal constant-coordinate peak plateau with `lambda > ca`;
`delta_j = lambda_j - ca`; `e_c = a^{-2} sum delta_j`;
`g_{j-1}` = gap before `P_j`;
`H_c = a^{-3} sum_{j>=2} delta_j min(g_{j-1}, L-lambda_j)`;
`sigma = a^{-2} sum lambda_j`; `s = m/a`.

### 10.1 Supersession and attribution

* **My Theorem L (9.2) is SUPERSEDED.**  It is the weak relaxation
  `n_j <= L - lambda_j` of the audited master localization
  `n_j <= min(L-lambda_j, lambda_{j-1}+1+g_{j-1})` (FIRST_DANGEROUS (4.1)).
  Their Theorem 1 gives `Q <= (3c + 2e_c + H_c)a^3 + O(a^2)` — strictly
  sharper in the adversarial small-gap regime (their `2e_c + H_c` with
  `H_c ~ 0` versus my `(4-c)e_c`); mine is not sharper anywhere useful.
  Theorem L/L' are hereby marked duplicates; cite FIRST_DANGEROUS
  Theorem 1 instead.  My Lemma 9.1 = their Lemma 3 (also a duplicate,
  independently derived).  Corollary S(1) is superseded by the sharper
  mass law below.
* **Theorem N (MASTER / supply law) SURVIVES as the count projection.**
  From the same first-complete assignment: `n(t) <= supply(t)` counts
  plateaux (`s(c) >= (4-3c)/(2-c) - o(1)`), while their secant ledger
  bounds excess mass (`2e_c + H_c >= 4-3c - o(1)` combining their Theorem
  1 with Theorem I at `D=o(a^2)`).  Neither implies the other:
  mass => count only at half strength (`s(c) >= e_c/(2-c)`), count =>
  mass only integrated (`e(c) >= int_c^{4/3}(4-3t)/(2-t)dt
  = 4-3c-2ln(3(2-c)/2)`, e.g. `0.189` at `c=1` versus the mass law's
  `0.5`).  Both projections should be carried.

### 10.2 Two pending claims now PROVED via the certified c>1 theorem

Both follow from FIRST_DANGEROUS Theorem 1 at (say) `c=6/5` plus Theorem I;
no extension needed.  If `D=o(a^2)` then `2e_c + H_c >= 4-3c-o(1) = 2/5`.

* **Contiguous-ring orders: `D = Omega(a^2)` — PROVED.**  Ring sides are
  plateaux of length `<= a+O(1) < (6/5)a`, so `e_{6/5} = O(1/a)`, and
  `H_c <= (4-c)e_c = O(1/a)`: contradiction.  (Was "machine check
  pending" in 8a, correctly demoted in 8d; now closed.)
* **Uniformly random orders: `D = Omega(a^2)` whp — PROVED.**  A
  dangerous plateau at `c=6/5` needs `>(6/5)a+1` consecutive same-line
  points; the expected number of such runs is `M_a * O((max-line/M_a)^{(6/5)a})
  = e^{-Omega(a log a)}`, so whp there are none, `e_{6/5}=0`:
  contradiction.  (Was heuristic in 8d.2(7); now closed.  This strictly
  strengthens the audited `Omega(a^{3/2})` anti-mixing bound.)

### 10.3 Theorem O (threshold extension to all c in (0,2)) — PROVED, pending independent audit

**Claim.**  FIRST_DANGEROUS Theorem 1 holds verbatim for every fixed
`c in (0,2)`, not only `1<c<2`:
`Q <= ca M_a + 2a sum_j delta_j + sum_{j>=2} delta_j min(g_{j-1},
L-lambda_j) + O_c(a^2)`, with span/congestion `<= 4a+3` and `O(a)`
omissions.

**Audit trail (why no step needs c>1).**  (i) Dangerous-free window
lemma: any `c>0`.  (ii) First-dangerous localization (their (1.1)): uses
only word order of plateau starts and `v_{j-1} <= v_j` (plateaux overlap
in `<= 1` position since two lines share `<= 1` point): any `c`.
(iii) The only `c`-sensitive step is the cyclic secant (their (5.3)-(5.5))
proving `sum_j delta_j lambda_{j-1} <= 2a sum_j delta_j`.  This follows
TRIVIALLY from `lambda_{j-1} <= 2a` and `delta_j >= 0`, with no secant,
no cyclicity, no interval hypothesis, for all `c in (0,2)`.  (The secant
version is needed only in BRAID_GAP_SERVICE's component form, not here.)
(iv) Bookkeeping: `m <= (3/c)a = O_c(a)`, `sum delta_j <= 3a^2`, boundary
terms `O_c(a^2)`.  Constants depend on the fixed `c`; all laws are "for
every fixed c".

**Consequences (with Theorem I, `D=o(a^2)`), now on ALL of `(0,4/3)`:**

    MASS LAW:    2 e(c) + H(c) >= 4 - 3c - o(1),
    SUPPLY LAW:  s(c) >= (4-3c)/(2-c) - o(1).

* At `c -> 0+`: every near-width order carries at least `(2-o(1))a`
  directed internal peak plateaux, and (for low-seam profiles,
  `H ~ 0`) total directed-peak edge mass `sigma >= 2 - o(1)` — at least
  two thirds of all `M_a-1` ordering edges lie on directed peak plateaux.
* The MULTISCALE unit-atom countermodel (`mu = delta_{3/2}`, `s=1`,
  `H=0`) is KILLED: at `c=1/2`, mass law needs `e >= 5/4` but `e=1`;
  supply law needs `s >= 5/3` but `s=1`.  MULTISCALE's insufficiency
  verdict was proved only for the `1<c<4/3` system and does not apply to
  the extended system.

### 10.4 The extended scalar system and its surviving corner

Full provable scalar system on limit profiles `mu` (lengths `x=lambda/a`,
count density `s(c)=mu([c,2])`, mass `e(c)=int(x-c)_+ dmu`,
`sigma=int x dmu`):

    (i)   sigma <= 3                          [edge disjointness]
    (ii)  mu([x,2]) <= 6(2-x) for x>1         [line capacity]
    (iii) 2e(c)+H(c) >= 4-3c on (0,4/3)       [mass law]
    (iv)  s(c) >= (4-3c)/(2-c) on (0,4/3)     [supply law]
    (v)   0 <= H(c) <= min((4-c)e(c), (2-c)(3-sigma))  [audited]

**Analysis (PROVED at the profile level).**  The system remains
SATISFIABLE: the saturated profile `mu = 2 delta_{3/2}` (MULTISCALE §5)
passes everything — supply `s(c)=2 >= (4-3c)/(2-c)` (equality at `c=0`),
mass `e(c)=3-2c >= 2-(3/2)c` on `(0,4/3)`, `sigma=3` (edge saturation),
line capacity `2 <= 3`.  So no scalar counting closes the fork — but the
surviving corner is now FORCED to be extremal in a usable way:

* (v) couples seams to saturation: `H(c) <= (2-c)(3-sigma)`.  Any
  near-saturated profile (`sigma -> 3`) has `H -> 0`, i.e. its dangerous
  plateaux are asymptotically gap-free: the word is a DENSE CHAIN of
  long directed peak plateaux covering `3a^2 - o(a^2)` of its edges.
* Supply at `c->0` forces `>= 2a` plateaux; edge budget forces average
  length `<= (3/2)a`; mass law at `c` slightly below `4/3` forces
  persistent excess above every threshold `< 4/3`.  The `2 delta_{3/2}`
  point (2a adjacent plateaux of length `(3/2)a` on distinct lines) is
  the unique atom saturating supply-at-0 and edge mass simultaneously.

**The isolated missing lemma (updated from 9.4/9.5).**  For dense chains
of adjacent long directed peak plateaux, literal-adjacency transition
geometry applies — and the audited rotating-braid level ledger already
caps a clean direct 3-cycle braid at
`sum lambda <= ((4+2sqrt6)/3) a^2 + O(a) = 2.9663 a^2 < 3 a^2`, a
deficit of `(1/30)a^2` against the required saturation.  What is missing
is exactly:

> **General-pattern level ledger.**  Extend the A/B-turn level
> inequality from the fixed rotation `x,y,z,x,...` to arbitrary adjacent
> coordinate patterns (repeats `c,c` with level change, 2-cycles
> `x,y,x,y`, reflections), and to gaps `g_j <= (small)`, at any
> threshold `c in (0,4/3)`.  If every adjacency pattern obeys a ledger
> with the same qualitative ceiling (`sum lambda <= (3-eta)a^2` for
> dense chains), then the mass law at `c` near `4/3` (which forces
> near-saturation via (v)) contradicts it, `D = Omega(a^2)` for every
> order, and `g_3(2a,2a,2a) >= width + Omega(a^2)` closes the three-box
> route in the relaxed regime.  If some pattern evades the ledger
> (e.g. 2-cycles with drifting levels), that pattern is the unique
> candidate construction geometry.

Seam tools already proved for this: S1-S4 of 9.5.2 (arrival/departure
singletons force cross-delivery inequalities; shared-coordinate seams
self-destruct at gap `< (8/3)a`; swallow alternative = level
inequality).  The 2-cycle pattern analysis is the natural first case:
`x,y,x,y` alternation with levels `t_1,s_1,t_2,s_2,...` — S1/S2 force
monotone delivery constraints whose feasible level trajectories can be
enumerated by the same telescoping used in the A-turn lemma.

## 11. The 2-cycle pattern dies; adjacency taxonomy (new results)

Setting for this section: `D = o(a^2)`; all runs are upper-threshold
(`{xi >= v}`) incidence runs, the only kind in the audited system.
"Adjacent" plateaux means literal word adjacency (`l' = r+1`).

### 11.1 Proposition Q (same-letter adjacency impossible — PROVED)

Two ADJACENT peak plateaux on the same coordinate cannot exist.  If `P`
(line `x=t`) is immediately followed by `P'` (line `x=t'`): the peak
property of `P` requires its right neighbor — the first point of `P'`,
with `x = t'` — to satisfy `t' < t`; the peak property of `P'` requires
its left neighbor — the last point of `P`, `x = t` — to satisfy
`t < t'`.  Contradiction.  QED.  Hence in any dense (gap-free) chain of
peak plateaux the coordinate pattern is a word in `{x,y,z}` with no
immediate repetition; same-letter transitions require `>= 1` gap
position.

### 11.2 Lemma R (z-step law on 2-letter segments)
### [FALSE AS WRITTEN — per FABLE_TWO_CYCLE_AUDIT.md and
### FABLE_PROVENANCE_AUDIT.md §8.5: at an equality seam (`z` rises in,
### falls out, `z_+ = z_-`) the two seam vertices form a two-position
### maximal `z`-plateau of cost ONE; the claim "equality creates no new
### run" is refuted.  Repair path (cost <= 1 instead of 0, equality seam
### as separator) is plausible but its endpoint bookkeeping is
### UNAUDITED.  Do not cite.]

Let `S` be a maximal segment of consecutive, adjacent, DIRECTED peak
plateaux using only the letters `x` and `y` (alternating, by Prop Q).
On an `x`-plateau (level `t`), directedness plus `y+z = -t` locks `z`
strictly monotone per word step; same on `y`-plateaux via `x+z = -s`.
At an interior seam of `S`, let `z_-` and `z_+` be the values at the
last point before / first point after.  If `z` was rising into the seam
and `z_+ < z_-`, the point at `z_-` is a strict local max of `z`; if
`z_+ > z_-` and `z` falls out of the seam, the point at `z_+` is one;
each is a SINGLETON internal maximal run of `{z >= (that value)}`
(both word-neighbors strictly below), i.e. an internal run of cost 0.
Equality `z_+ = z_-` creates no new run (checked: the containing
threshold runs extend into the monotone side and are long).  Hence, on
any stretch of `S` containing no such z-reversal seam, `z` is weakly
monotone in word position and strictly monotone within plateaux, so the
number of PLATEAU EDGES in that stretch is at most `4a+2` in total
(`<= 2a+1` strictly falling steps plus `<= 2a+1` strictly rising steps
across the single allowed valley; a fall-to-rise valley seam creates no
run).  QED.

Consequence: a 2-letter segment carrying plateau-edge mass `T` contains
at least `floor(T/(4a+2)) - 1` cost-0 internal runs (one per exhausted
z-monotone stretch, at the rise-to-fall reversal seams).

### 11.3 Theorem P (pure 2-cycle dense chains die)
### [NOT PROVED AS STATED — per FABLE_TWO_CYCLE_AUDIT.md: the proof
### silently assumes every plateau has length >= ca+1 (minimum-length
### hypothesis absent from the statement); without it a single 4a+2
### edge-mass block can contain Theta(a) seams and the L+O(1) service
### spacing fails.  Audited repair scope: ONE contiguous chain of
### mutually adjacent directed plateaux, ALL longer than ca, covering
### all but o(a^2) positions — that restricted form is repairable
### (equality seams cost 1, negligible), but interspersed gaps can
### reset the z trend and are NOT handled.  The claim that the
### 2 delta_{3/2} profile has no two-letter realization also needs the
### missing profile-to-chain reduction.  UNAUDITED; do not cite.]

No order of `H_a` with `D=o(a^2)` can consist, up to `o(a^2)` positions,
of one chain of adjacent directed peak plateaux alternating between two
fixed coordinates.  In particular the saturated scalar corner profile
`mu = 2 delta_{3/2}` (MULTISCALE §5) has NO 2-letter realization.

*Proof.*  Say letters `x,y`; `z` never holds.  By Lemma R, the word
(minus `o(a^2)` exceptional positions) splits into consecutive
"z-valley blocks", each with `<= 4a+2` plateau edges, separated by
cost-0 z-reversal runs.  Each block also contains `<= (block plateau
edges)/(min plateau length) + 1` seams; blocks have `<= 4a + O(a/c) =
O(a)` positions.  Covering `M_a - o(a^2) = 3a^2 - o(a^2)` positions
needs `K = Omega(a)` blocks, whose `K-1` boundary z-peaks are spaced
`<= 4a + o(a)` apart along the word... more precisely each block has
length `<= 4a+2+m_k+1+o`-share, and `m_k <= (4a+2)/(ca+1) <= 4/c+1`.
So consecutive cost-0 runs are `<= 4a + 4/c + 3 + (gap share)` apart.
Every forward window `W_i` (`L = 4a+2` positions) that lies within the
covered region and spans a block boundary contains a cost-0 internal
run; the fraction of window starts `i` (out of `M_a - L`) whose window
contains one is `1 - o(1)` (block length `<= L + O(1) + o`-terms).
Assign those starts their cost-0 run (span `<= L+1`, forward-only,
congestion `<= L+1` as audited) and the `o(a^2)` rest the universal
cost-`<=2a` run:

    sum_i min(lambda_i, 3a-1) <= 0 * (1-o(1))M_a + 2a * o(a^2) = o(a^3).

Theorem I at `h = 3a-1` with `D = o(a^2)` requires `>= 4a^3 - o(a^3)`.
Contradiction.  QED.

Remarks.  (i) The proof did not use plateau LENGTHS beyond
`>= ca+1` for the seam count — it kills 2-letter dense chains of any
length spectrum.  (ii) Non-directed plateaux each contribute their own
interior cost-0 singleton (audited Lemma 3 of BRAID_GAP_SERVICE), so
allowing `Theta(a)` of them only adds cheap runs; the theorem is robust
to that relaxation.  (iii) With Prop Q and the audited rotating-braid
ledger (`sum lambda <= ((4+2sqrt6)/3)a^2 < 3a^2` for clean direct
3-cycles at threshold `4a/3`), BOTH periodic dense realizations of the
saturated scalar corner are now dead: 2-cycles by Theorem P, 3-cycles
by the level ledger.  What remains of the dense-chain regime is
aperiodic letter patterns (e.g. `x,y,x,z,x,y,...`) — where `z` holds
occasionally, resetting the z-step budget — and all gap-carrying
(`H_c > 0`) profiles.

### 11.4 Corrected fork statement (replacing 9.4/9.5 and 10.4's gate)

The isolated missing lemma after Theorem P:

> **Aperiodic-pattern ledger.**  For dense chains whose letter pattern
> uses all three coordinates: bound `sum lambda` away from `3a^2`, or
> force `Omega(a)` cheap runs at reversal seams, uniformly over
> patterns; and extend to chains with gap mass via the seam functional
> `H_c`.  The z-step mechanism generalizes: each coordinate `xi`
> contributes strictly monotone steps except where `xi` HOLDS (its own
> plateaux) or reverses (cheap run or its own peak plateau); a triple
> ledger summing the three step budgets against `2(M_a-1)` total
> cross-coordinate movements is the natural frame.

This is strictly smaller than the 10.4 gate (2-cycles resolved,
same-letter adjacency eliminated, saturated periodic corner closed).

## FROZEN SNAPSHOT MARKER (2026-07-22)

Provenance corrections from FABLE_PROVENANCE_AUDIT.md and
FABLE_TWO_CYCLE_AUDIT.md are applied throughout (see markings at §11.2,
§11.3, §12.2, §12.3, §12.4 and ledger item 12).  Certified-proved core at
this freeze: Theorem A; Lemma B/B'; Theorem E; Theorem I (corrected form);
Theorem L (combined-min form); Theorem M (clipped area law);
MASTER/supply law; distributional width bounds; ring/random
`D=Omega(a^2)` kills; Proposition Q; Theorem R's Markov tail.  Everything
in §11–§12 beyond these is unaudited, conditional, or heuristic as
individually marked.  No theorems are to be added past this marker in
the frozen turn.

## 12. Corrections to §10 and §11, and the 2-cycle attack (authoritative over §10.3–§11)

### 12.1 Corrections (per FABLE_INTERVAL_SUPPLY_AUDIT.md and the two user
### corrections; all three verified line-by-line here)

1. **Theorem L is NOT wholly superseded — RESTORED.**  The audited status:
   for `c > 1` the strongest bound is
   `Q <= [3c + min{(4-c)e_c, 2e_c + H_c}]a^3 + O(a^2)` (combined form);
   for `0 < c <= 1` Theorem L's `(4-c)e_c` is the ONLY proved service
   coefficient (FIRST_DANGEROUS is stated for `1<c<2`).  Hence the mass
   law `(4-c)e(c) >= 4-3c-o(1)` holds on all `0<c<4/3` unconditionally
   (Theorem L + Theorem I), and the sharper `2e+H >= 4-3c-o(1)` only on
   `(1,4/3)`.  §10.1's "superseded" is retracted.  Also per the audit:
   Theorem L's span argument is `end <= i+L`, giving `4a+3` (the
   `L+lambda+1` line in my §9 was arithmetic garbage — the conclusion
   stood, the intermediate step is corrected); Theorem M must select a
   MINIMUM-effective plateau (not the first); doubly-blocked pairing
   excludes `O(a)` boundary indices; my §9.3 "negative result 1"
   (edge-budget check) reversed an inequality and is deleted as false;
   the level-capacity bound `F(y) <= 6(2-y)a+3` is valid only for
   `y >= 1`.
2. **Theorem O demoted to CONJECTURAL (pending independent audit).**  Its
   consequences (mass law below `c=1` via `2e+H`; ring and random
   `Omega(a^2)` "proofs" in §10.2) are demoted with it.  However the ring
   and random kills survive VIA THEOREM L: both orders have
   `e_{6/5} = o(1)` (rings: plateaux `<= a+O(1)`; random: whp no
   `(6/5)a`-run), and Theorem L needs no `c>1` restriction, so
   `(4-6/5)e = o(1) < 4 - 18/5 = 2/5`: contradiction with the mass law
   at `c=6/5`.  **Ring and random `D=Omega(a^2)` are therefore PROVED
   without Theorem O** (the audit's (1.4) is exactly this; `c=6/5`
   works for both).  §10.2 stands with its justification repaired.
3. **§10.3–10.4 supply normalization error — CORRECTED.**  With
   `mu = (1/a) sum_j delta_{lambda_j/a}`:
   `s(c) = supply(ca)/a^2 = int_{x>c}(4-x) dmu(x)`, NOT `mu((c,2])`.
   The count consequence is `F(c) >= s(c)/(4-c)` — at `c->0` at least
   `a/2 - o(a)` plateaux, not `2a`.  §10.4's "dense chain / sigma->3
   forced" is RETRACTED: the profile `mu = 2 delta_{4/3}`, `H=0`,
   `sigma = 8/3` passes every proved scalar law on all `(0,4/3)`
   (supply `s(c) = 16/3`; mass `2e = 4(4/3-c) >= 4-3c`; Theorem-L mass
   `(4-c)e >= 4-3c` checked: `2(4-c)(4/3-c)-(4-3c) = 2c^2-(13/3)c+20/9
   > 0` on `(0,4/3)`; capacity `2 <= 4`), with the missing `(1/3)a^2`
   edge mass in one boundary reservoir invisible to `H_c`.  §10.4's
   framing ("general-pattern ledger is the sole remaining case") was
   therefore overclaimed at the scalar level; the corrected sharp form
   is Theorem R below, which shows saturation IS forced — but by the
   weighted (index-level) MASTER, not by the scalar system.

### 12.2 Theorem R (weighted saturation)
### [PARTIALLY CERTIFIED — per FABLE_PROVENANCE_AUDIT.md §12.3: the
### Markov tail (12.3) `#{i: q_i >= beta a} >= ((4-3beta)/(2-beta))a^2
### - o(a^2)` IS correct.  The reservoir sentence below is NOT proved
### by it: Markov alone does not give a boundary reservoir average cost
### 4a/3, nor convert high q_i into quantified new disjoint dangerous
### edge mass — that conversion needs clipped spatial service and gap
### geometry (one rigorous version now exists in
### BOUNDARY_RESERVOIR_PROFILE.md, via |R_c|/a^2 <= (9/4)c^2 + o(1),
### under explicit vanishing-seam hypotheses).  "Weighted saturation"
### means saturation of window-minimum costs q_i, NOT of plateau edge
### mass.  Cite only the tail inequality.]

For `D=o(a^2)`, Theorem M/I give `sum_i min(q_i,3a-1) >= 4a^3 - o(a^3)`
with `q_i <= 2a`, over `M_a ~ 3a^2` indices.  Hence the index-average of
`q_i` is `>= (4/3 - o(1))a`, and for every `beta`:
`#{i : q_i >= beta a} >= ((4-3beta)/(2-beta))a^2 - o(a^2)` (Markov on
`2a - q_i >= 0`).  Since `q_i <= lambda(P)` for EVERY complete peak
plateau `P` in `W_i`, and every window contains one (Theorem E), the
WEIGHTED load is what saturates — e.g. the `2 delta_{4/3}` profile needs
its `(1/3)a^2`-vertex reservoir to have `q_i` averaging `(4/3)a`, which
forces the reservoir itself to be covered by complete directed plateaux
of window-min length `~(4/3)a`, i.e. forces additional dangerous mass
exactly of the kind the scalar ledger missed.  (Self-audit: this uses
only Theorem M (corrected form), Theorem E, and Markov; no
concentration.)

### 12.3 Theorem P' (two-letter stretches die)
### [NOT CERTIFIED — per FABLE_PROVENANCE_AUDIT.md §12.4, this restated
### form inherits the same global bookkeeping gaps as Theorem P:
### (1) the statement says 2a*g(S) while the proof switches to 8a*g(S)
### in place — the constant participates in the density argument, so
### this is not typographical; (2) the nearest-run assignment span is
### 4a+o(a)+O(local pause count) with NO uniform O(a) span/congestion
### when pauses concentrate in one long gap; (3) the number of z-maxima
### is not shown lower-order (may be proportional to seam count);
### (4) the "gap-dominated stretches have their own cheap runs unless
### one long gap hosts a maximum" dichotomy in Corollary P'' is a new
### unproved lemma, and the o(a^2) hosting count is not derived.
### Corollary P'' (letter recurrence / near-rotating forcing) is
### therefore CONJECTURAL.  Do not cite either as proved.]

**Statement.**  Let an order of `H_a` contain a word interval `S` of
length `|S| >= C_0 a` on which every internal peak plateau has letter
(fixed coordinate) in `{x,y}`, and let `g(S)` be the number of positions
of `S` lying in no peak plateau.  Then `S` contains at least
`(|S| - g(S) - o(|S|))/(4a) - 2` internal maximal threshold runs of the
letter `z`, each of cost `<= 1 + (length of the single gap containing
it, if any)`, and the total Theorem-I-capped cost of one-per-window
assignments over `S` is `<= (2a) g(S) + o(a)|S| + O(a^2)`, NOT
`Theta(a)|S|`.

**Proof.**  On an `x`-plateau (level `t`), `y+z = -t` and `y` strictly
monotone force `z` strictly monotone; same on `y`-plateaux.  So `z`
changes strictly on every plateau edge of `S` and pauses only on the
`g(S)` gap positions.  Decompose the `z`-sequence of `S` into maximal
weakly-monotone stretches; a strictly-moving stretch has `<= 2a` edges
(range), so consecutive stretch boundaries are `<= 4a + (local pause
count)` apart.  Each fall-after-rise boundary is a weak local maximum
of `z`; its maximal plateau `[u,v]` has `z` constant, and since `z`
moves strictly on plateau edges, `[u,v]` contains at most one plateau
edge — no: `z` constant across `[u,v]` means NO edge inside is a
plateau edge of an `x`/`y`-plateau, so all of `[u,v]` minus one point
lies in gaps: `v-u <= (gap positions inside) + 1`.  Its word-neighbors
have strictly smaller `z` (maximality of the weak max), so `[u,v]` is
an internal maximal run of `{z >= z_u}` of cost `v-u`.  Summing: the
runs' total cost `<= g(S) + (number of maxima)`, and their spacing is
`<= 4a + pause` positions.  Assign each index of `S` (except `O(a)`
boundary) its nearest such run: span `<= 4a + o(a) + O(pause)`;
each run serves `<= 2(4a + ...)` indices; total capped cost
`<= sum_k (cost_k) * (served_k) <= (4a + o(a)) * 2 * (g(S) + #maxima)
<= 8a g(S) + o(a)|S| + O(a^2)`... [second pass:] the displayed constant
in the statement should be `8a g(S)`, not `2a g(S)` — CORRECTED here;
the qualitative conclusion is unchanged.  QED.

**Corollary P'' (letter recurrence — PROVED).**  If `D=o(a^2)`, then for
all but `o(a^2)` word indices `i`, every letter `x`, `y`, `z` occurs as
the coordinate of some complete internal peak plateau within distance
`O(a)` of `i`, OR `i`'s window carries a run of cost `o(a)`.  *Proof:*
if letter `z` is missing from a `C_0 a`-neighborhood, Theorem P' applies
to that stretch; its local gap mass must be `Omega(a)` per `4a`-window
to avoid cheap runs, i.e. the stretch is gap-dominated — and
gap-dominated stretches have their own cheap runs unless the gaps'
pauses are `Omega(a)` long, which makes the `z`-max plateau run cost
`Omega(a)` ONLY if a single gap of length `Omega(a)` hosts the max;
total such hosting is bounded by total gap mass, `o(a^2)` of the word.
Combining with Theorem I as in §11.3 kills any `Omega(a^2)` mass of
two-letter stretches.  QED (self-audited twice; the `o(a^2)` bookkeeping
is the same as §11.3's, with the pause-hosting bound added).

Consequence: **the surviving letter pattern is forced to be
near-rotating** — all three letters recur within every `O(a)` window of
the plateau sequence (in particular within every ~3 consecutive
dangerous plateaux at the `(4/3)a` scale).  This is exactly the pattern
class where the audited ROTATING_BRAID A/B taxonomy applies at literal
adjacency, and THREE_HALVES shows is transparently realizable at the
`3a/2` scale with one-point gaps and levels `~a/2`.

### 12.4 The conditional criticality computation (windmill v3)
### [HEURISTIC — per FABLE_PROVENANCE_AUDIT.md §12.5: openly assumes
### the unproved bounded-gap A-ledger, and even within that hypothesis
### the derivation below contains literal ellipses and an unresolved
### "-(something)" term; no exact optimization problem or uniqueness
### proof is supplied.  Windmill v3's parameters are a candidate stress
### test only.  The claims "unique simultaneous-equality profile" and
### "satisfies every proved constraint" are NOT certified.]

CONDITIONAL HYPOTHESIS (the bounded-gap A-ledger, still unproved —
§9.5.2 S4 proves the swallow case; the cross-coordinate case and the
cheap-run disjunction remain): for near-rotating dense chains, every
plateau satisfies `lambda_j <= t_{j-1} + t_j + t_{j+1} + O(seam
corrections)` summing to `E <= 3T + o(a^2)`, `T = sum_j t_j`.

Under this hypothesis plus PROVED constraints (capacity
`lambda_j <= 2a - |t_j|`; distinct lines for `lambda > a`; Theorem E
gap bound `g <= L - lambda_next - O(1)`; weighted MASTER
`sum_i q_i >= 4a^3 - o(a^3)`), maximize feasibility for a dense chain of
`m` plateaux of common length `ell a`:

* `T <= 3[(m/3)(2-ell)a - (m/3)^2/2]` (top `m/3` distinct integer levels
  per direction below `(2-ell)a`);
* `E = m*ell*a <= 3T` gives `ell a <= (2-ell)a*... ` i.e.
  `m <= 6(2 - (4/3)ell)a/...` — solving at `ell = 4/3`:
  `(4/3)am <= 2am - m^2/2 - (something)` → `m <= (4/3)a`, `E <= (16/9)a^2`,
  `T = (16/27)a^2` with EQUALITY throughout when the `m/3 = (4/9)a`
  levels per direction descend from `(2/3)a` to `(2/9)a`;
* MASTER with `q_i = (4/3)a` on all `3a^2` indices (plateau spacing
  `(9/4)a`, gaps `(11/12)a <= (8/3)a` pass Theorem E): `sum q_i = 4a^3`
  EXACTLY.

**Windmill v3** — `(4/3)a` plateaux of length `(4/3)a`, positive levels
sweeping `(2/9)a..(2/3)a` per direction, peak-free valley gaps of length
`(11/12)a` — satisfies every proved constraint AND the conditional
A-ledger with simultaneous equality.  (Windmill v2 of §9.5.1, with
`(9/4)a` plateaux and tiny gaps, VIOLATES the conditional A-ledger:
`E = 3a^2 > 3T_max ~ 2a^2` at its level budget — so IF the ledger is
proved, v2 dies and v3 is the unique surviving uniform profile.)

**Fork status after 12.4 (honest).**  Not a service inequality below
four, and not a realizable counterexample either — windmill v3's
realizability is open exactly at its transitions: its levels lie in
`[(2/9)a, (2/3)a]`, mostly BELOW `a/2`, where the THREE_HALVES
transparent one-point separator provably does not exist (`r in (a-t,t)`
empty for `t < a/2`); its connectors must be the long `(11/12)a`
peak-free valleys, whose sign structure is constrained by S1/S2
(arrival/departure singleton lemmas, §9.5.2) at both ends.  The missing
invariant is now completely explicit:

> **Q3 (decisive, both directions concrete).**  (a) Prove the
> bounded-gap A-ledger `E <= 3T + o(a^2)` for near-rotating chains with
> peak-free gaps — using S1/S2/S4 plus a treatment of the
> cross-coordinate swallow case — AND rule out windmill v3 by its
> remaining slack (the `q_i` accounting of its `(11/9)a^2` gap indices
> depends on gap-interior structure: a peak-free gap of length
> `(11/12)a` between plateaux of length `(4/3)a` forces every gap
> window to reach a complete neighboring plateau, which Theorem E makes
> tight — any interior wobble creates a cheap run).  Then
> `g_3(2a,2a,2a) >= width + Omega(a^2)` for every order.  (b) Or:
> construct windmill v3's low-level transitions explicitly (a
> THREE_HALVES-type packet with levels below `a/2` and valley
> connectors), which would produce a candidate order achieving the
> Theorem-I floor with equality — the unique candidate geometry for the
> entire three-box route.

### 12.5 Status ledger for this section

* PROVED: 12.1's corrections (including ring/random via Theorem L at
  `c=6/5`); Theorem R's Markov tail inequality ONLY (see 12.2 marking);
  Proposition Q (certified by FABLE_TWO_CYCLE_AUDIT).
* UNAUDITED/NOT CERTIFIED (per FABLE_PROVENANCE_AUDIT §12.4 and
  FABLE_TWO_CYCLE_AUDIT): Lemma R (false as written at equality seams —
  repair plausible, unaudited); Theorem P (minimum-length hypothesis
  gap); Theorem P' (constant discrepancy 2a vs 8a, span/congestion gap,
  maxima count gap); Corollary P'' (unproved gap dichotomy) — the
  near-rotating forcing is CONJECTURAL.
* CONDITIONAL/HEURISTIC: everything in 12.4 (bounded-gap A-ledger
  assumed; derivation itself incomplete — see marking); windmill v2's
  death and v3's criticality/uniqueness are both uncertified.
* FALSE/RETRACTED: §10.3's supply-count conflation; §10.4's dense-chain
  forcing and its "sole remaining case" framing; §10.1's "wholly
  superseded" for Theorem L; §10.2's reliance on Theorem O (repaired);
  §9.3's edge-budget negative result (deleted).
* OPEN: Theorem O's audit; Q3(a) and Q3(b).

## 8. Next actions

1. [DONE 2026-07-22] Machine falsification: cube_2 certificate (all
   selections, all h), random/permutation/shrunk covers up to `(4,4,4)`,
   and **exhaustive** enumeration of all covering words of length <=5 on
   `(1,1,1)`, `(2,1,1)`, `(1,1,2)` with all witness selections, both the
   band form (all h) and the Mirsky form.  Zero violations.
2. [DONE 2026-07-22] Second-pass independent re-derivation of Lemma B/B':
   step (1) containment (`y>=r_{i(x)}` forces `I_{i(x)} subseteq [x,y]`,
   join rank `>= m*`); step (2) fan joins nondecreasing in `y`, distinct
   S-values form a chain in S, cap `min(e(x)-x+1, c)`; step (3) block sum
   `sum_{g=0}^{Delta_i-1} min(w_i+g,c) <= min(w_i,c)+(Delta_i-1)c`,
   `sum_i(Delta_i-1)=ell_M-M=alpha_M`, tail `(D-alpha_M)c`; total `cD`
   exactly.  Both passes agree; Lemma B/B' is **proved**.
3. [SUPERSEDED by §12.4] Conjecture D evolved through the run-spectrum
   program into fork Q3.
4. NEXT: (i) independent audit of Theorem O; (ii) Q3(a): the
   cross-coordinate swallow case of the seam lemma (§9.5.3 first
   bullet), then the bounded-gap A-ledger for near-rotating chains;
   (iii) Q3(b) in parallel: attempt a below-`a/2`-level transparent
   packet (the THREE_HALVES construction breaks there — determine if
   the breakage is essential); (iv) only after Q3: four-box
   `O(m^{3-eps})` reframing and the wreath mass law analogue (Lemma B
   is lattice-general and applies to the Boolean middle band directly).
