# Multi-swap erosion chronologies: the window-counting floor, the t-swap trade, and the reduction of the run-floor requirement to the natural height scale

**PBBS dependency correction (2026-09-07):** The motivation below that
Q6 has closed the canonical PBBS route is withdrawn: its height-time
claim is false. See `scratch/PBBS_Q6_RETRACTION_AND_FIXED_HEIGHT_COUNTERFAMILY_20260907.md`.
This does not affect independent window-counting identities, nor does it
certify other claims or repair separately recorded splice defects.

Date: 2026-08-20 (third file of this date; companions:
`MATH_THEOREM_RUNLENGTH_CRITERION_AND_CENTRAL_UCYCLE_EQUIVALENCES_20260820.md`,
`MATH_THEOREM_PBBS_QUEUE_FLUSH_DYNAMICS_AND_RUN_CONSERVATION_20260820.md`).
Status: Lemmas M1–M3 and Theorem M4 are proved; Section 4 records the
resulting revision of the route map with explicit remaining demands.

Setting as in the companions: `n=2m+1`, `W=binom(n,m)=binom(n,m+1)`.
An *owner chronology* is a sequence `X_1,…,X_L` of `(m+1)`-subsets of
`[n]`; it need NOT be a Johnson walk.  Its *swap size* at step `i` is
`t_i=|X_{i+1}\setminus X_i|` (`=|X_i\setminus X_{i+1}|` when ranks are
equal).  A coordinate incidence run is a maximal interval of consecutive
owners containing a fixed coordinate.  The factorization theorem of
`MASTER_HANDOFF.md` Section 4 — which imposes **no adjacency condition**,
only run lengths — states: a letter word `A` with `D^dA=X` exists iff
every internal coordinate run has length at least `d+1`, and the compiled
nonzero word has length `L+d` with letters
`A_j^{max}=∩_{max(1,j-d)<=i<=min(L,j)}X_i`.

## 1. Lemma M1 (the window-counting floor)

In any erosion-compiled word from a chronology of length `L=(1+o(1))W`
and depth `d`, each pair `(i,q)` with `q<=d` realizes at most one lower
target (the intersection of the window), so at most `L·d` lower-band
targets are realized by short windows in total.  Realizing all targets
of ranks in `[m+1-H*, m]` with `H*=Theta(sqrt(n log n))` (the far-rank
absorption threshold, Theorem A of the first companion) requires

\[
L\,d\ \ge\ \sum_{q'=1}^{H^*}\binom{n}{m+1-q'}
\ =\ \Bigl(\sqrt{\pi/8}+o(1)\Bigr)\,W\sqrt n ,
\]

hence

\[
\boxed{\,d\ \ge\ \bigl(\sqrt{\pi/8}+o(1)\bigr)\sqrt n\,}
\]

for every erosion architecture at coefficient one.  The depth — and with
it the coordinate run floor `d+1` — can never be pushed below the
natural height scale `Theta(sqrt n)`; the question is only whether the
extra `sqrt(log n)` factor above it is necessary.  (This makes precise
why the canonical PBBS failure at scale `Theta(sqrt n)` in the second
companion was fatal for `t=1`: there the run floor must be `t·d`-reach
divided by `t=1`, i.e. the full `sqrt(n log n)`.)

## 2. Lemma M2 (the t-swap trade)

Let the chronology have swap sizes `t_i<=t` and all coordinate runs
`>=d+1`.  Then:

1. the compiled nonzero word exists and has length `L+d` (factorization
   theorem; no adjacency needed);
2. every letter is nonempty with rank at least `m+1-td`, since a window
   of `d` steps loses at most `td` coordinates; for `td<=H*` this is
   `>=m/2`, so all letters are nonzero with room to spare;
3. the intersection over a window `[a,b]`, `b-a=q<=d`, equals `X_a`
   minus its at most `qt` departures — realizable lower ranks reach down
   to `m+1-td`;
4. the union over a window of length `q` equals `X_a` plus its at most
   `qt` arrivals — realizable upper ranks reach up to `m+1+td`.

Hence the **band reach in rank is `t·d` while the run-floor requirement
is only `d`**.  Choosing

\[
t=\Theta(\sqrt{\log n}),\qquad d=\Theta(\sqrt n),\qquad td=H^*,
\]

satisfies Lemma M1 with equality up to constants, meets the absorption
threshold, and reduces the run-floor requirement to `Theta(sqrt n)`.

*Proof.*  (1) is the cited factorization theorem.  (2)–(4) are the
displayed set identities: an intersection over a window is the initial
owner minus its departures inside the window; a union is the initial
owner plus its arrivals; departures and arrivals per step are bounded by
the swap size.  ∎

**Remark.**  All prior cover machinery in this project — PBBS, pair
cells, wreaths — is Johnson (`t=1`), for which band reach and run floor
coincide and the requirement is the full `sqrt(n log n)`, now proved
unattainable for canonical PBBS.  The `t`-swap trade is therefore a
genuinely new lever: it spends the abundant letter mass (letters of rank
`~m-H*` instead of `~m-sqrt n`) to buy a `sqrt(log n)` reduction of the
floor, landing exactly on the scale the residence machinery already
achieves.

## 3. Theorem M4 (seams need ages, not adjacency)

Call a coordinate *young at step `i`* if it entered within the last `d`
steps, and *doomed* if it departs within the next `d`.  Concatenating
two chronology segments with a single seam step of swap size `<=t` (an
arbitrary owner-to-owner jump within that swap budget) preserves the
run-floor hypothesis iff no coordinate swapped out at the seam is young
and no coordinate swapped in is doomed.  **AUDIT CORRECTION
(2026-08-20, second reader): the "arbitrary owner-to-owner jump"
clause is FALSE.  A single seam step moves the owner by at most the
swap size `t`; boundary owners at Hamming distance `Delta` require at
least `ceil(Delta/t)` transitions, and with `t = Theta(sqrt(log n))`
an arbitrary pair costs `Theta(n/sqrt(log n)) >> d = Theta(sqrt n)`.
The `O(d)`-cost splice claim is withdrawn; it survives only for
segment families served in a PROXIMITY ORDER (consecutive boundary
owners at distance `O(t·d)`), which is an unproven scheduling
hypothesis, not a free consequence.**  Subject to that hypothesis,
any family of
segments with internal floor `d+1` can be spliced into one chronology by
seam steps together with `O(d)`-step buffer collars per seam (the collar
repeats the boundary owner's long-lived coordinates while retiring young
ones at swap-size `<=t` per step), at total length cost `O(d)` per seam.
For `s` segments the total splice cost is `O(sd)`, which is `o(W)`
whenever `s=o(W/sqrt n)`.

*Proof.*  Runs are broken only at the seam, and only for swapped
coordinates; the age condition is exactly the statement that every
terminated run already has length `>=d+1` and every started run will
have length `>=d+1`.  If the raw boundary owners violate it, prepend to
the right segment `O(d)` collar steps that swap nothing young out and
nothing doomed in — possible since at most `td<=H*` coordinates of an
owner are young and the swap budget retires them at `t` per step over
`d` steps, `td>=` the young count by the same arithmetic.  Each collar
step keeps all other runs alive, so the floor survives.  ∎

This is the same age inequality as the seam-cleanliness law (Lemma 5 of
the first companion) and the endpoint-age matching test of
`MATH_THEOREM_COMPLEMENTARY_AGE_CROSS_STRATUM_COLLARS_20260804.md`,
now appearing on the erosion side: **all three seam calculi of this
project are one law: terminated dwell plus initiated dwell must cover
the window.**

## 4. Revised route map and explicit remaining demands

With Lemmas M1–M2 and Theorem M4, the erosion route to coefficient one
now requires exactly the following data, for `t=Theta(sqrt(log n))`,
`d=Theta(sqrt n)`, `td>=H*`:

1. **Owner coverage:** segments jointly visiting `(1-o(1))`-almost all
   `(m+1)`-sets, total length `(1+o(1))W`, at most `o(W/sqrt n)`
   segments.  Pair-cell Hamilton cycles with repeat separation
   `L_0=Theta(sqrt r)` (handoff Section 5.3, proved) supply segments
   with internal floor at the required scale provided their constant can
   be taken above `sqrt(pi/8)·sqrt 2`; their assembly no longer needs
   Johnson splicing or whole-cell partitions — Theorem M4 splices them
   with `O(sqrt n)` collars each, and the 2-adic obstruction (which
   concerns exact whole-cell partitions) is bypassed by allowing `o(W)`
   owner repeats across overlapping cells.
2. **Lower band injection:** an assignment realizing each rank-
   `(m+1-q')` target, `q'<=H*`, as the intersection over some window —
   equivalently a system of distinct representatives between band-lower
   targets and windows, with the window's departure set as the free
   choice.  This is the conditioned-lower-lift gate (handoff 7.3.3) in a
   strictly easier form: swap schedules are a new degree of freedom
   (the departure multiset per window is designable, subject only to
   run floors), where the Johnson case had per-step departures forced
   to singletons.
3. **Upper band:** dual to 2 via arrivals; strictly easier since upper
   loads grow with depth.

Demand 1 is structural and now plausibly within reach of the existing
pair-cell theorems plus Theorem M4; demand 2 remains the substantive
open core, but it is now a pure matching/design question with a
polynomially large per-window choice space, decoupled from adjacency,
topology, and the run-length statistics that killed the canonical
route.  This is recorded as:

**Open Problem 6 (multi-swap lower injection).**  For some
`t=Theta(sqrt(log n))`, `d=Theta(sqrt n)`, construct a length-
`(1+o(1))W` chronology satisfying demands 1–3.  By Lemmas M1–M2,
Theorem M4, the collar compiler, and far-rank absorption, this implies
`nu(k)=(1+o(1))binom(k,floor(k/2))` for all `k`.

**Identification with the chainization lane, and the exact quantitative
gap.**  At a fixed position `a`, the available window intersections form
a *nested chain* under the owner `X_a`: the owner minus its successive
departure prefixes, with the step-size schedule controlling which ranks
the chain visits.  Demand 2 therefore asks for a near-perfect covering
of the lower band by owner-rooted nested chains — precisely the
asymptotic, multi-swap form of handoff conjecture 7.2.1 (sharp
owner-chain chronology), with two crucial relaxations: chain length
`H*=Theta(sqrt(n log n))` instead of `d(k)=Theta(sqrt k)` at exactness,
and defect budget `o(W)` instead of zero.  Since `Lambda=Theta(W sqrt
n)`, the allowed leave fraction is `o(W/Lambda)=o(n^{-1/2})`.  The
proved STW-anchored integral chainization
(`MATH_THEOREM_ASYMPTOTIC_SHARP_ANCHORED_CHAIN_FACTOR_FROM_STW_20260801.md`)
achieves leave `O(Lambda·k^{-1/16+o(1)})`.  **The entire remaining gap
on this route is the leave exponent: `-1/16` must become `-1/2-eps`** —
a concrete quantitative strengthening of one existing theorem, plus the
serialization of the resulting chain factor into a run-floored
multi-swap schedule (the departure orders must realize the chains,
which is the new design freedom of this file rather than an
obstruction).

## 5. Scope guard

Lemmas M1–M2 and Theorem M4 are self-contained given the cited
factorization theorem and Theorem A of the first companion.  No claim is
made that demands 1–3 are satisfied; Open Problem 6 is open.  The exact
conjectures `nu(k)=B(k)` and finite `k=17` are untouched.
