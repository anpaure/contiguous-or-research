# Thread D: exact MMM global-switch c-space/Benders integration

**Date:** 2026-07-29  
**Status:** proved finite-state reduction and audited negative/weak-Pareto result; no compiler-ready (k=15) carrier and no output word claimed.

## 1. The two move classes are different objects

An MMM parallel-edge switch is not a local edit of the binary trace.  It keeps the unlabelled quotient factor but changes the voltage accumulated while that quotient circuit is lifted through the (k) sheets.  A run-end 3-cycle, by contrast, fixes all run starts and cyclically permutes three run-end residue classes, with integer lifts chosen to preserve total length.  They do not commute in general.

The proof-safe master therefore uses complete reconstructed traces as states.  It never assigns independent Boolean variables to the changed trace columns of an MMM switch, and it never accepts a run-end circuit merely because its scalar run algebra is legal.

## 2. Exact parallel-edge shear

Let (U_0,ldots,U_{N-1}) be the directed quotient order of a connected factor.  Write the old unit voltage as (v\in\mathbb Z_k^\times).  If the selected parallel edges change their signed voltage by increments (epsilon_e), put

\[
E=\sum_e\epsilon_e,\qquad
B_j=\sum_{e\text{ before }U_j}\epsilon_e,
\qquad v'=v+E.
\]

Assume (v'\in\mathbb Z_k^\times).  Aligning the old and new lifts at (U_0), their coordinate-zero traces obey

\[
c'_{j+tN}=c_{j+(a t+b_j)N},\qquad
a=v'v^{-1},\quad b_j=B_jv^{-1}\pmod k.                 \tag{2.1}
\]

Indeed, before the quotient prefix ending at (U_j), the new sheet is the old sheet plus (B_j); after one quotient revolution their relative sheet displacement gains (E).  Solving for the old phase in terms of the new phase gives (2.1).  Thus the change is a piecewise-affine sheet shear across entire (N)-columns.

A parallel choice has the same lower and upper quotient endpoints.  Since a unit-voltage lift visits every sheet exactly once over each quotient vertex and each quotient edge, it preserves the complete middle orbit histogram and complete lower-(q=1) histogram.  It need not preserve residence, any deeper intersection, an arbitrary-width upper union, or the compiler Hall graph.

For the audited (k=15) switch at selector 175,

\[
(1807,7,12)\longrightarrow(1807,11,12),\qquad
v:1\longrightarrow8,
\]

and

\[
a=8,\qquad b_j=0\ (0\le j<381),\qquad b_j=7\ (381\le j<429).
\]

This accounts for 3,092 changed trace bits and 406 removed plus 406 added run starts and ends.  The normalized voltage-one target IDs must be returned to the raw physical gauge by the coordinate relabelling (x\mapsto8x\pmod {15}); comparing target IDs without this conjugation is invalid.

## 3. Exact run-end 3-cycle lemma

Choose a zero gap as cyclic origin and unwrap the (N) one-runs as

\[
[s_i,e_i],\qquad s_i+d\le e_i\le s_{i+1}-2.
\]

For a 3-cycle (sigma) on run indices, prescribe

\[
e'_i=e_{\sigma(i)}+Nz_i.
\]

Define

\[
L_i=\left\lceil\frac{s_i+d-e_{\sigma(i)}}N\right\rceil,
\qquad
U_i=\left\lfloor\frac{s_{i+1}-2-e_{\sigma(i)}}N\right\rfloor.
\]

Then a legal lift exists exactly when there are integers (z_i\in[L_i,U_i]) with (sum_i z_i=0), equivalently

\[
\sum_iL_i\le0\le\sum_iU_i.                              \tag{3.1}
\]

The bounds are exactly the residence and nonempty-gap inequalities.  The endpoint residues are permuted, the starts are fixed, and (sum e'_i=sum e_i).  Consequently every residue-class sum, the one-start/one-end transversals, class rank, Johnson adjacency, and the lower derivative ranks through depth (d) are preserved.

This does **not** preserve the middle or lower-(q=1) decks automatically.  For each orbit (O), the exact acceptance signatures are

\[
\Delta^M_O=\#\{j:\operatorname{can}(T'_j)=O\}
            -\#\{j:\operatorname{can}(T_j)=O\},
\]

\[
\Delta^{q1}_O=\#\{j:\operatorname{can}(T'_j\cap T'_{j+1})=O\}
             -\#\{j:\operatorname{can}(T_j\cap T_{j+1})=O\}.       \tag{3.2}
\]

The circuit is collision-neutral if and only if both signed vectors vanish.  Multiplicities in (3.2) are essential; support-only lost/gained sets cannot certify cancellation.

The companion verifier enumerates every arithmetic circuit, reconstructs every changed physical middle and (q1) deck, and compares the sparse signature with that full replay.  It gives:

| case | legal circuits | neutral singles | signed types | inverse signed pairs |
|---|---:|---:|---:|---:|
| (k=9) | 27 | 0 | 27 | 0 |
| (k=11) | 131 | 0 | 131 | 0 |
| (k=15) | 4,037 | 0 | 4,037 | 0 |

For (k=15), the nearest circuit still creates 15 duplicate middle positions and 30 duplicate (q1) positions.  The absence of inverse signatures excludes a pair only when the two literal effects commute and their (q1) halos are disjoint.  Overlapping moves have quadratic (q1) cross terms and require reconstruction of the final trace.

A separate exact meet-in-the-middle check strengthens the additive statement: among all `8,146,666` unordered pairs, no pair is an inverse and no pair sum is the negative of a third catalogue signature.  Hence no collection of one, two, or three distinct catalogue moves has zero signed middle+(q1) sum.  In the commuting, pairwise-(q1)-support-disjoint submaster, every nonempty admissible composition therefore has arity at least four.  This still says nothing about nonlinear overlapping sequential moves.

## 4. Exact finite-state master

For each completely reconstructed unit state (s), let (y_s\in\{0,1\}).  The finite-state interface installs

\[
\sum_s y_s=1,\qquad
c_p=\sum_{s:c^s_p=1}y_s\quad(0\le p<W).                  \tag{4.1}
\]

For every middle orbit (R) and lower-(q1) orbit (L), define literal multiplicities

\[
\mu_s(R)=\#\{j<N:\operatorname{can}(T^s_j)=R\},
\]

\[
\lambda_s(L)=\#\{j<N:\operatorname{can}(T^s_j\cap T^s_{j+1})=L\}.
\]

The exact signature system is

\[
\sum_s\mu_s(R)y_s=1\quad\text{for every }R,
\qquad
\sum_s\lambda_s(L)y_s=1\quad\text{for every }L.         \tag{4.2}
\]

At (k=15), (4.2) is 858 integral rows.  These are full derived-column equations.  A single-column exclusion is not a valid replacement.

The executable hook `install_portfolio_cp_sat_rows()` is called after `SoundCspaceMaster.build_model`.  It first performs the full pinned deep replay, then installs 15 state variables, one one-hot row, 6,435 literal trace-link rows, and all 858 equations (4.2).  Residence, lower/upper separation, and the compiler remain the base master's exact CEGAR/Benders gates.  A shallow payload check is only an integrity regression; proof-safe installation always uses the deep replay.

The 4,037-state frozen single-3-cycle class has no state satisfying (4.2), so the exact class row is

\[
\sum_{s\in\mathcal C_3}y_s=0.                            \tag{4.3}
\]

Equation (4.3) has only this frozen one-move scope.  After an MMM shear, the run boundaries change globally (406 of 429 in the audited switch), so its 3-cycle catalogue must be regenerated.

For the frozen additive submaster restricted to at most three distinct, commuting, pairwise-(q1)-support-disjoint moves, the stronger exact bounded-class cut forces every move variable to zero.  It is not installed against overlapping sequential compositions.

## 5. Event-stream master, all-width oracle, and compiler feedback

On every physical Johnson edge write

\[
T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.
\]

The master derives these physical deletion and insertion events and imposes

\[
L_i^{(q)}=T_i\setminus\{\alpha_i,\ldots,\alpha_{i+q-1}\},
\qquad
U_i^{(q)}=T_i\cup\{\beta_i,\ldots,\beta_{i+q-1}\}.       \tag{5.1}
\]

These are exact prefix identities even when an event repeats.  Short one- and zero-run histograms additionally impose the coefficient-exact rank ledgers

\[
\sum_i\bigl(|L_i^{(q)}|-(r-q)\bigr)
=\sum_x\sum_s(q-s)^+R_x^+(s),
\]

\[
\sum_i\bigl((r+q)-|U_i^{(q)}|\bigr)
=\sum_x\sum_s(q-s)^+R_x^-(s).                            \tag{5.2}
\]

The compiler's retained erosion is backward-looking,

\[
P_i^{(q)}=\bigcap_{a=0}^qT_{i-a}.
\]

The exact positionwise bridge is

\[
L_i^{(q)}=P_{i+q}^{(q)}.                                 \tag{5.3}
\]

The payload verifies (5.3) at every physical position and every audited depth; equality of support-hole sets alone would not certify the shift.

Every event is indexed by a physical transition and a physical coordinate.  The implementation does not treat any Claude map \(\mathbb Z_N\to\mathbb Z_k\) as injective or as a permutation.

For a fixed quotient start, let \(d_x\) be the cyclic distance from the translated trace position of coordinate \(x\) to its next insertion/one.  Starting with the current middle set and adding all coordinates tied at each successive value of \(d_x\) enumerates exactly the distinct insertion prefixes, hence the unions of **all** consecutive intervals from that start.  Strict equivariance reduces the start positions to one quotient period.  This is the retained all-width oracle; widths 2 through 8 are diagnostic only.

For rank \(r+1\), the oracle specializes to the adjacent-edge identity \(S=T_i\cup T_{i+1}\).  Higher ranks retain the arbitrary-width insertion-prefix recurrence.

Each finite state is processed in this order:

1. exact middle and \(q1\) signatures;
2. exact owner circuit, residence, erosion normal form, and the bridge (5.3);
3. deletion-prefix lower rows and the coefficient-exact rank ledgers before depth \(d\);
4. exact arbitrary-width upper rows;
5. only then the exact one-core, weighted quotient Hall, physical matching, safe cut, and literal compiler verifier.

At a pre-compiler failure the payload emits exact target-row digests.  The one-core, weighted Hall, physical matching, and safe-cut problem remains an exact Benders subproblem.  An `UNKNOWN` compiler result emits no cut.  A proved fixed-carrier compiler failure may exclude the complete \(c\)-assignment; no partial selector or local-switch overcut is inferred.

## 6. Complete five-menu result

The exact menu voltage is

\[
v(y)=9+14y_0+7y_1+10y_2+12y_3+12y_4\pmod {15}.          \tag{6.1}
\]

Of the 32 assignments, 15 are unit-voltage circuits and 17 are excluded by (6.1).  All 15 have exact middle and (q1) decks.  Only two are residence-clean:

| state | (q2) holes | (q3) holes | exact all-width upper holes |
|---|---:|---:|---:|
| `00101` | 47 | 11 | 95 |
| `01101` | 47 | 12 | 94 |

Thus the complete fixed-factor parallel portfolio gives a weak (q2)-neutral/upper-improving move, but no strict (q2)-and-upper improvement.  The upper gain has a (q3) counterterm.  No state reaches the compiler gate, because all retain at least 47 lower-(q2) holes.

The exact load change at (q2) is (+e_{1295}-e_{1671}), so the missing set is unchanged.  At (q3) it is

\[
+e_{271}-e_{647}+e_{901}-e_{1159},
\]

creating hole 1159.  The unrestricted upper support gains exactly rank-nine orbit 1951 and loses none.

The zero-run rank-capacity ledger improves simultaneously.  The physical upper-rank deficit changes by

| depth \(q\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| \(\Delta E_q^+\) | 0 | -15 | -30 | -45 | -45 | -30 | -15 |

for total change \(-180\).  This is an exact insertion-prefix capacity improvement, not a claim that the hole objective is monotone under the run potential.

## 7. Artifacts, hashes, and runtime

| artifact | SHA-256 |
|---|---|
| `scratch/threadD_mmm_switch_cspace_benders.py` | `e0df0c4435c22960503dd5b29986bb1793fe7e721cf60ae488f11af16e0d70f4` |
| `scratch/test_threadD_mmm_switch_cspace_benders.py` | `64295e9f3ccffbfcfcba838b41c80ff4129725fd255f3f56f16f66eaff16cf88` |
| `scratch/threadD_mmm_switch_cspace_benders_20260729.audit.json` | `31ec15e992385dc02809e55afcad112d13bc01d04f31e831372dc8afe5d63670` |
| `scratch/audit_threadD_mmm_portfolio_cp_sat_hook.py` | `6a39a361609c60a4bf0d761c3a091fab813f9a81433b2cf46dc04f010444ccdb` |
| `scratch/threadD_mmm_portfolio_cp_sat_hook_20260729.audit.json` | `be2a1c683d9670edb8a32a99687e36f48cd470ef119bccff06129fb3fc0adb42` |
| `scratch/audit_strict_spiral_three_run_cycles_20260729.py` | `3a490101dc0d79d6ed504d954e4604150d2df1af7ea5f4f6f1c44a5ee2400165` |
| `scratch/strict_spiral_three_run_cycle_audit_20260729.json` | `bbeadffb2669c95f09924a941959c80ad51e3a5c76c30a541252da325aad4e31` |
| parallel-switch regression source | `323601c0edbcd5a209b9ba99432fd63347dd3d708b8ad03515f4b6a083427289` |
| frozen (k=15) fixture | `4482c3d448b3e314f89cc0c6e3f04a950e12a9e97ceb680da0478a00f2f4ee10` |
| event-stream theorem (prose, not an executable pin) | `da7f9837cb6bb0d145f499c4e3adf8aec62d3c18b87ea9e920cfc3702f99067b` |
| event-stream audit source | `8f592dc49682bcb6d896e9a79df0ac6dc8bd8b0e5b13990a62053719fb844c80` |
| event-stream audit JSON | `4580f1df6c5316ae39216496c766e50e54c28ffa4b0b4932b20a60f3971f1270` |
| arity-four lower-bound theorem | `3c1c02bdffb93c621b8e43714901ea9d0709c5bb5fbc595fa3eb7650a796d4ba` |
| three-cycle signature catalogue | `cbae9665d9f882360ee7ae61acf1c1e78e33abefb21d33873b56554beab56d90` |
| arity meet-in-the-middle result | `324eec348c33b7eaeb49ad72b68de56900f1b0d5dcdd4d7c2e7eb5f4da693327` |

The retained payload is 1,321,629 bytes and contains all 15 literal \(c\)-traces, the 858 signature rows, deletion/insertion stream hashes, coefficient-exact run-deficit ledgers, the shifted erosion bridge, the arity-three finite-class certificate, target-cut digests, and reconstruction hashes.  Its internal canonical payload digest is `81c41a02f689c5f6f851757bb42372feba50fe3500c5febde464eac8ca89d974`.

On one H100 **CPU** core (`taskset -c 63`, `nice -n 10`; no GPU):

- exact three-cycle census: 25.62 s;
- complete event-stream portfolio build: 17.57 s;
- deep-replay plus executable CP-SAT hook smoke: 19.08 s total;
- CP-SAT solve inside that smoke: 0.176 s, 6,450 variables, 7,294 constraints, one worker;
- seven retained unit tests: 0.430 s remotely and 0.154 s locally.

No annealing, SAT, CP-SAT, or blind local search was run.  No compiler-ready carrier and no length-6438 word is claimed.

## 8. Sharp remaining gate

The frozen additive, support-disjoint three-cycle neighborhood is excluded through arity three.  Any nonempty additive neutral bundle, if one exists, has arity at least four; the other surviving possibilities are a genuinely nonlinear overlapping endpoint permutation or a sequence in which each global MMM shear is followed by regeneration of the legal run-end circuit catalogue.  In every case the **final** trace must satisfy (4.2), the deletion/insertion prefix system (5.1), the coefficient-exact rank ledgers (5.2), the shifted erosion bridge (5.3), and the exact compiler Benders subproblem.  Neither signed signatures nor upper deltas may be added across overlapping/noncommuting moves without literal final-trace replay.
