# The queue-flush form of the PBBS two-step dynamics, the run-length conservation law, and the degenerate-tail program for Open Problem 1′

**SUPERSEDING AUDIT, 2026-09-07. Theorem Q6 is FALSE.** The primitive
height-three family `D_q=1(1100)^q0` has empty `S(D_q)` but exact planted
lifetime `3q`. The complete symbolic proof and dependency ledger are in
`scratch/PBBS_Q6_RETRACTION_AND_FIXED_HEIGHT_COUNTERFAMILY_20260907.md`.
Sections3.5-6 below are retained as a historical record, not as valid
proofs of fast-run abundance or canonical-route closure. The earlier
count-versus-packing correction does not repair the false premise.
Q1-Q3 survive; Q4's endpoint convention is corrected below. The informal
cone discussion and Proposition4.1 are not certified by this audit.
The positive-density short-run/packing question remains unresolved by
this proof chain; the independent current upper bound is unchanged.

Date: 2026-08-20 (same-day companion to
`MATH_THEOREM_RUNLENGTH_CRITERION_AND_CENTRAL_UCYCLE_EQUIVALENCES_20260820.md`).
Original status (superseded where specified above): Q1–Q5 were claimed from the exact structures of
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md` (specifically its Lemma 8.1
and Theorem 9.1, both of which carry complete proofs there); Section 5
states the identified remaining step (the cone-profile count) as a
conjecture with an explicit reduction.  All verifications against the
explicit gap-5 family of that file's Theorem 8.2 were done symbolically in
this session; no computation was used.

Setting: `N=2r+1`, middle states normalized as `0D` with `D` a Dyck word
of semilength `r`; `f` the PBBS map, `tau=phi^2` its Dyck-quotient
two-step; `h=ht(D)`.  By Theorem 9.1 of the cited file, with the unique
factorization `D=P,1,R,0,S` (split at the first up-step attaining the
global maximum and at the first return to height zero after it; `S` is
the Dyck suffix of complete arches after the first max-attaining arch):

\[
\delta(D)=|P|+1,\quad \delta(\phi D)=|R|+1,\quad
\tau D=S\,1\,P\,0\,R,\quad
u\mapsto u-d(D),\ d(D)=|S|+1 .
\]

## 1. The necklace form of a tau-step

**Theorem Q1 (two-bit necklace law).**  Realize the state as the cyclic
binary pattern on `Z_N` with the root at the unique dominant zero.  Then
one `tau`-step is exactly:

1. the root pointer jumps backward by `d(D)=|S|+1`, landing on the
   arch-end zero `0'` (the first return to height zero after the first
   maximum);
2. the vacated root position flips `0 -> 1`;
3. the first-maximum up-step position `mu` flips `1 -> 0`;
4. no other position changes.

*Proof.*  Write the necklace as `0_root P 1 R 0' S` cyclically.  The
image `tau D=S1P0R` rooted at the new root reads `0_new S 1 P 0' R`.
Rotating the original necklace to start at `0'` gives `0' S 0_root P 1 R`.
The two agree except that the letter at the old-root slot is `1` in the
image and `0` in the original, and the letter at the old first-maximum
slot is `0` in the image and `1` in the original.  The new root position
is `u-(|S|+1)`, which is `0'`.  ∎

Equivalently, on owner sets: `g(S)=S+u(S)-u(f(S))` — the entering
coordinate of a `g`-step is the vacated root; the leaving coordinate is
the deleted first-maximum letter.  This yields at once:

**Theorem Q2 (exit rule).**  Along a projected `g`-cycle, the residence
run of the coordinate that enters at a given step is exactly the queue
lifetime of the planted letter: it begins when the root vacates its
position (step 2 above) and ends at the step at which that same letter is
the first-maximum up-step of the current word (step 3).  Runs, gaps, and
`nu_H` are therefore statistics of the deterministic single-letter
consumption process, one letter consumed and one replanted per
`tau`-step.

Verification: on the explicit 3-cycle `D_0=110100(10)^t`,
`D_1=1011(01)^t00`, `D_2=(10)^t110010` of the cited file's (8.4), Theorem
Q1 reproduces `tau D_0=D_2` letter-by-letter, and Theorem Q2 gives the
planted letter of `D_1` a lifetime of exactly `2` `tau`-steps, matching
the recorded gap-5 return (its (8.8)).

## 2. Height invariance and the climbing law

**Theorem Q3 (orbit invariants and block heights).**  `ht(tau D)=ht(D)`;
in fact `ht(phi D)=ht(D)`, so the height `h` is constant along every PBBS
quotient orbit.  Moreover, under one `tau`-step `D=P1R0S -> S1P0R`, the
height of a tracked letter changes by exactly

\[
+1 \text{ if it lies in } P,\qquad
-1 \text{ if it lies in } R,\qquad
0 \text{ if it lies in } S,
\]

and the freshly planted letter enters at height `1`.

*Proof.*  In `S1P0R` the block `S` is based at height `0` (unchanged),
`P` is based at `1` after the planted divider (each letter `+1`), and `R`
is based at `h-1` after the `0` following the `P`-part, whereas in `D` it
was based at `h` (each letter `-1`).  The maximum of the image is
`max(ht(S), 1+max P\text{-profile}, (h-1)-\text{drops of }R)`; since `P`
ends at height `h-1`, the `P`-part attains `h` at its end, `S<=h` and the
`R`-part stays `<=h-1`; hence the maximum is exactly `h`.  The `phi`-step
computation in Lemma 8.1 of the cited file shows the same for `phi`.  ∎

**Theorem Q4 (run-length conservation law; endpoint corrected 2026-09-07).**
Let `T` count the subsequent updates after planting through consumption,
and let `#P,#R,#S` count only the nonconsuming updates at which the mark
lies in the respective block. Then `T-1=#P+#R+#S` and, since it is consumed at height
`h` having entered at height `1`,

\[
\boxed{\,T\;=\;h\;+\;2\#R\;+\;\#S\,.}
\]

In particular `T>=h` (a mechanistic form of the height-gap theorem,
its (16.1), with the exact excess identified), and a run of length
`T<=H` has at most `H-h` non-climbing steps in total.

*Proof.*  Immediate from Theorem Q3: final height minus initial height is
`h-1=#P-#R`; use `#P+#R+#S=T-1`. ∎

## 3. The queue-flush discipline

Each `tau`-step: locate the first positional letter attaining height `h`
(the current `mu`); the segment strictly between `mu` and the next return
to height zero (`R`) is flushed to the back of the word with heights
lowered by one; the prefix before `mu` (`P`) climbs by one; the suffix of
complete arches (`S`) rotates to the front unchanged; `mu` is consumed
and a new letter is planted at the divider.  For a tracked letter this
gives the exact trichotomy per step: **climb** (it precedes `mu`),
**swept** (it lies in `(mu,\text{arch-end}]`), **rest** (it lies in the
suffix arches).  By Theorem Q4 every swept step costs `+2` and every rest
costs `+1` against the minimal lifetime `h` (consumption included).

**Theorem Q5 (late bloomers cannot overtake).**  A letter planted at step
`t'` cannot be consumed before a letter planted at step `t<t'` while both
climb uninterruptedly: an uninterrupted climber planted at `t` reaches
height `h` at step `t+h-1`, and ties at height `h` are resolved by word
position with the current front strictly ahead; a later plant reaches `h`
strictly later.  Hence the recycled replants generated during a short run
never contribute cut-ins against it; only material with strictly positive
initial height ahead of the letter can interrupt its climb.

*Proof.*  From Theorem Q3 a climber's height at step `t+j` is `1+j`;
strictly monotone in the plant time.  A consumption requires height
exactly `h`; a letter planted later reaches `h` at a strictly later step,
so it can never be the first `h`-attainer while an earlier uninterrupted
climber is still present unless positioned before it at equal height,
which the plant order precludes for replants (each new plant enters at
the divider in front, at height `1`, and reaches `h` after the tracked
letter exits).  ∎

**Interruption source.**  Consequently a short run (`T<=H`) forces: at
all but `<=H-h+1` of its steps, no letter positioned before the tracked
letter attains height `h`.  Material ahead consists of the plant-time
suffix `S` and the suffix-arches arriving at subsequent steps; by Theorem
Q3 an arch of height `a` in this front, based at the rising divider
stack, attains `h` after `h-a` further steps.  Thus **every front arch of
height `a>=2` present at plant time triggers an interruption strictly
before the letter's earliest possible exit**, and each interruption
either costs a rest/sweep (bounded in number by `H-h+1`) or must be
absent.  A run of length `T<=H` therefore forces a *cone profile*: an
arch arriving at the front `j` steps into the run can have height at most
`j+(H-h+1)+1-ish` without violating the budget — early-arriving front
material must be flat, with the allowed height growing at most linearly
in arrival time.

## 3.5 WITHDRAWN: Q6 and the claimed canonical PBBS obstruction

The cone analysis of Section 3, pushed to completion, does not merely
constrain short runs — it *produces* them in bulk, and thereby resolves
the fate of Open Problem 1/1′ of the companion file **negatively** for
the canonical cover.

**Theorem Q6 (single-arch words exit fast).**  Let `D` be a Dyck word
with `S(D)=\varnothing` in the factorization `D=P1R0S` — equivalently,
the first arch of `D` attaining the global maximum is its last arch.
Then the letter planted at the `tau`-step from `D` climbs without any
interruption and

\[
T_{exit}(D)\;=\;h(D)+O(1).
\]

*Proof.*  At plant time the word is `1^* P 0 R`, a single active arch
with the tracked letter as its first letter and empty front.  At every
subsequent step the factorization has `S'=\varnothing` (the active arch
is the last and only arch, so there are no suffix arches), hence the new
word is again a single arch with all material other than the front
divider stack positioned after the tracked letter.  The first positional
`h`-attainer is therefore always behind the tracked letter until its own
height reaches `h`: every step is a climb (`#R=#S=0` in Theorem Q4), no
letter ahead of it exists to be consumed first (Theorem Q5 covers the
replants), and the conservation law gives `T=h-1+O(1)`, the `O(1)`
absorbing endpoint conventions.  ∎

Sanity checks: `D=111000` (`r=h=3`) has measured `T=3`; the gap-5 family
`D_1=1011(01)^t00` of the cited file's Theorem 8.2 has `S(D_1)=\varnothing`,
`h=2`, measured `T=2`.  Both match.

**Corollary Q6.1 (short-run abundance).**  Single-arch Dyck words
(`D=1D'0`) satisfy `S(D)=\varnothing` and number `Cat_{r-1}=(1/4-o(1))Cat_r`;
all but an `exp(-cH^2/r)`-fraction have height at most `H`.  Hence for
every `H` above the typical height scale — in particular at
`H=\lceil\sqrt{n\ln n}\rceil` —

\[
\boxed{\ \nu_H(P_m)\ \ge\ \Bigl(\tfrac14-o(1)\Bigr)W\ }
\]

and the hypothesis of the run-length criterion (Corollary B2 of the
companion file) is **false for the canonical PBBS cover**.  The
criterion itself remains a valid implication; its hypothesis simply
cannot be met by `P_m`.

**AUDIT CORRECTION (2026-08-20, second reader): the boxed bound
confuses counting with packing.**  `nu_H` is a maximum edge-disjoint
(repair-relevant) subfamily, not the raw count of short residence
intervals, so `(1/4-o(1))W` overlapping intervals do not directly
give `nu_H >= (1/4-o(1))W`.  Corrected statement with the same
qualitative conclusion: the `(1/4-o(1))W` single-arch intervals have
pairwise distinct starting positions in the compiled word and each
has length `< H`, so the left-to-right greedy (repeatedly take the
earliest-ending interval, discard those meeting it) discards at most
`2H` starting positions per selection, giving a DISJOINT subfamily
of size at least

    `nu_H(P_m) >= ((1/4)-o(1))·W/(2H) = Omega(W/H)`.

Since the criterion requires `nu_H = o(W/H)`, the hypothesis of
Corollary B2 REMAINS false for the canonical PBBS cover; only the
strength of the lower bound changes (`Omega(W/H)`, not `Omega(W)`).
The boxed display should be read as the interval COUNT; the packing
bound above is the load-bearing one.

**Corollary Q6.2 (two-sided closure of the erosion window for PBBS).**
Combined with the far-rank absorption threshold (Theorem A of the
companion file, `H \ge (1/2+o(1))\sqrt{n\ln n}` required) and the proved
sub-Gaussian packing window (`nu_H=o(Cat)` only for
`H=o(\sqrt{r/\log r})`, Corollary 16.2 of the cited file), Theorem Q6
shows the unbridged zone `[C\sqrt n,\ c\sqrt{n\log n}]` is not a gap in
our knowledge but a genuine obstruction for this cover: the canonical
PBBS run-length law has constant mass at scale `Theta(\sqrt r)` (the
single-arch states), so no sharper tail estimate can rescue it.  Any
erosion-architecture proof of coefficient one therefore requires either

1. an owner cycle cover whose successor map is *engineered* so that no
   positive-density family of states exits at its height scale — a run
   floor `\ge\sqrt{n\log n}`, which the pair-cell residence machinery
   (master handoff Section 5.3) reaches only at `O(\sqrt r)` and whose
   whole-cell version is 2-adically obstructed; or
2. batched sub-band repair below the Hoeffding threshold, which is
   exactly the economics of handoff conjectures 7.2.6–7.2.7 — now proved
   *necessary*, not merely convenient, for any PBBS-like cover; or
3. abandoning the erosion corner for the singleton/`ML(2m+1)` corner
   (Theorems C and D of the companion file), which has no run
   obstruction at all.

## 4. WITHDRAWN Q6-dependent conclusions (historical text)

Proved unconditionally here: the exact conservation law (Q4), the exit
rule (Q2), the invariance (Q3), the non-overtaking of replants (Q5), and
the derived necessary cone condition for short runs (Section 3).  These
replace the height-only necessary condition (its Theorem 16.1) by a
strictly stronger, time-resolved constraint: the height bound is the
`j=0` slice of the cone.

The decisive further step was Theorem Q6: pushing the cone analysis to
its `S=\varnothing` extremal did not merely bound short runs — it showed
they have positive density.  An earlier draft of this section proposed a
"cone-profile count" conjecture asserting sparsity of the short-run set
(`#{T_exit<=H} <= 4^r e^{-c r^eps}`); Theorem Q6 **refutes that
conjecture** — the single-arch family alone contributes
`Cat_{r-1}=(1/4-o(1))Cat_r` fast-exiting words.  The correct description
of the short-run set is structural, not sparse:

**Proposition 4.1 (short-run structure, two-sided; costs corrected by
hand-verification).**  Front-material costs are: a front flat (`10`)
costs one rest, incurred at the tie-step `j=h-1` (its top reaches `h`
simultaneously with the tracked letter and wins by position); a front
height-`h` arch costs `Theta(h)` rests, because its consumption debris
(head, plant, and tail) reassembles into another height-`h` arch that
returns to the front and re-interrupts on alternate steps — verified by
the exact trace of `D=111000111000` (`r=6`, `h=3`), which gives
`T_exit=6=2(h-1)+2`, i.e. gap `13`, with the rest/climb pattern
`SRSRSR`-alternating exactly as the respawn analysis predicts.  Hence
`T_exit(D)<=H` holds when `S(D)` consists of `f` flats and `k`
height-`h` arches with `f+Theta(h)k <= H-h`, and conversely a run of
length `<=H` forbids every arch of `S(D)` with height in `[2,h-1]`
outside an `O(H-h)`-window (such an arch ripens under the ladder and
sweeps the tracked letter, Section 3).  The recorded sharpness example
for the height-gap theorem (rank six, height three, gap seven) is
exactly a single-arch state: `T=h=3` with empty front, the Q6
mechanism.  The short-run set remains a positive-density, explicitly
parameterized family; the single-arch words are its empty-front core.

(The identification `#`short runs`=N·#{D: T_exit(D)<=H}` holds because
the `(phase, Dyck root)` pairs across the whole factor biject with
`Z_N x {Dyck words}`, each pair starting exactly one run, and Theorem Q2
identifies run length with exit time.)

## 5. WITHDRAWN route-closure consequences (historical text)

1. **The erosion route through canonical PBBS is closed** (Corollary
   Q6.2): no tail estimate, however clever, can meet the run-length
   criterion, because the criterion's hypothesis is false.  The prior
   question "extend the sub-Gaussian packing window (5.3) beyond
   `H=o(sqrt(r/log r))`" is now answered: that window is essentially
   sharp, and the transition to positive short-run density occurs at the
   height scale `Theta(sqrt r)`, witnessed by the single-arch states.
2. **The batched-repair economics of handoff conjectures 7.2.6-7.2.7 are
   necessary**, not merely convenient, for any cover with
   positive-density runs at its height scale; their multiscale window
   `sqrt(m log log m)` sits below the Hoeffding absorption threshold
   precisely because the run tail cannot be improved.
3. **Run-floor engineering** is the surviving erosion-side option: an
   owner cycle cover all of whose coordinate runs exceed
   `rho = sqrt(n log n)` (a "`rho`-floored cover").  The pair-cell
   machinery achieves floors `O(sqrt r)` and its whole-cell version is
   2-adically obstructed (handoff Section 5.3); crossing `sqrt(n log n)`
   needs new constructions.  Wreaths are the `rho=m` extreme, so
   `rho`-floored covers at `rho=sqrt(n log n)` are a strictly easier
   target than the wreath conjecture — a new named intermediate object.
4. **The singleton/`ML(2m+1)` corner gains priority**: it has no run
   obstruction at all (companion file, Section 9.5), and its blocking
   problem (defective covering / shift-condition Hamilton cycles) is
   untouched by today's negative result.

## 6. SUPERSEDED scope guard (historical text)

Theorems Q1-Q6 use only Lemma 8.1 and Theorem 9.1 of
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`, both fully proved there;
Theorem Q6 additionally uses Theorems Q1-Q5 of this file.  The
run-length criterion (Corollary B2 of the companion file) remains a true
implication; Theorem Q6 shows its hypothesis fails for `P_m`, so it can
only be applied to engineered `rho`-floored covers.  The exact
conjectures `nu(k)=B(k)` and the finite `k=17` problem are untouched.
The asymptotic coefficient-one conjecture remains open; its live routes
after today are batched repair (7.2.6-7.2.7), `rho`-floored covers, and
the singleton/`ML` corner.
