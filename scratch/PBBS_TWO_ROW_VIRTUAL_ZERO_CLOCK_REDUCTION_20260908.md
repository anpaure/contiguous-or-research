# Two-row virtual-zero clocks and the exact phase-count reduction

2026-09-08. Pure proof; no computation. This is a positive reduction of the physical eligible-label gate to an original-row-one query function and its geometric comparison under the same actual deeper environment. It does not prove divergence of that function. Root full-file audit: PASS. Independent cover-selectors full-file audit: PASS, with the no-wrap and threshold clarifications incorporated below. The growing-query theorem used in Section 7 has separately passed both full audits.

The exact clock and indexing inputs are the accepted notes

- `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_gaussian_clock_genealogy_structural_audit.md`, Sections 2–4;
- `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_finite_layer_zero_triangle_incidence_fibre.md`;
- `/Users/amir.nuriyev/.codex/worktrees/e333/problem/research_round1/pbbs_original_array_shift_cocycles.md`, Sections 1–3;
- `PBBS_SAME_PARTICLE_SHORT_TRACE_MULTIPLICITY_20260907.md` and `PBBS_TOP_ZERO_ALL_SHORT_OVERLAP_REDUCTION_20260908.md`.

## 1. Base incidence, partner cutoff, and the exact fibre

Fix constants `0<c<=C<infinity` before sending `r` to infinity. Write

\[
 H_c=\lfloor c\sqrt r\rfloor,\quad H_C=\lfloor C\sqrt r\rfloor,
 \quad G_C=2H_C+1.
\]

The BASE incidence is that of the original family

\[
 F_{0,c}=\{\mathrm{GOOD},\ T\le H_c,\ Z_{0,0}=0\},
 \qquad \mu_{0,c}=\mathbb E[(T+2)\mathbf1_{F_{0,c}}]=\Theta_c(1).
\]

After weighting a root by `(T+2)1_(F_(0,c))`, sample its edge offset `j` uniformly from `{0,...,T+1}`. Keep this base law throughout; it is not replaced by incidence at cutoff `C`.

Use the accepted depth-two safe base event, so the original triangle satisfies

\[
 Z_{0,0}=Z_{1,0}=Z_{1,-1}=0,
\]

the profile has `h>=4`, and the finite-layer fibre domain holds. Further restrict only the exposed profile to

\[
 \boxed{G_C+1<\min(n_1,n_2),\qquad n_s=2r_s+1.} \tag{1}
\]

For every fixed `c,C`, these restrictions have base-incidence probability tending to one. The triangle and safe-depth assertion is the accepted fixed-`S=2` bound. The extra inequality follows from original-depth profile concentration under actual incidence: `n_1/r -> 1` and `n_2/r -> 2/3`, whereas `G_C=O_C(sqrt r)`. Thus (1) does not introduce an unproved persistence or dynamical condition. The strict margin also excludes a circumference-minus-one C-clock alternative.

Expose

\[
 E_2=(\text{entire profile, all original rows }s\ge2,\ j).
\]

On every feasible environment in this safe event, the accepted fibre says:

- row zero has its coordinate zero fixed to zero and is otherwise a uniform weak composition of `ell_0` into `p_0-1` labelled parts;
- row one has coordinates `0,-1` fixed to zero and is otherwise a uniform weak composition of `ell_1` into `p_1-2` labelled parts;
- these two rows are conditionally independent, where `p_s=n_(s+1)`.

The environment retains its actual conditioned base-incidence distribution. Its feasibility includes the short base clock and sampled-offset test. On the triangle-zero fibre the base clock is the chronological `C_2 C_2 T_2` word from time zero, entirely determined by `E_2`; no new lifetime conditioning on free row-one values is needed.

## 2. Signed original trajectories and virtual-zero intervals

Let `lambda_s(t)` be the omitted physical site in the ORIGINAL fixed-site process of `D_s=partial^s D`, before the update at integer time `t`. Negative times use the inverse finite permutation on the same original labelled orbit. All levels use this same signed physical time, and `lambda_s(0)=0`.

The exposed rows determine the complete original `D_2` and its signed trajectory `lambda_2`. They do not determine `lambda_1`; the algorithm below will not request it.

At a physical phase whose selected site is `i`, C means the first later selection of site `i-1`, and T means the first later selection of the same site `i`. Their physical durations are positive even and odd integers respectively. Define the virtual-zero endpoint at a birth phase `t_d=2d` as the endpoint of the chronological `C_1 T_1` word beginning at `t_d`. Equivalently, it is the second strictly later selection of `lambda_1(t_d)-1`. Denote its physical gap by `g_0(d)` and put

\[
 T_0(d)=\frac{g_0(d)-1}{2},\qquad
 R_0(d)=d+T_0(d)+1,\qquad
 J_d^*=[d,R_0(d)]\cap\mathbb Z. \tag{2}
\]

Both endpoints of this edge interval are included. These virtual objects are defined from the original `D_1` trajectory, independently of every top-row gap. They are not asserted to be the actual lifetimes of births whose top-row gaps are positive.

The height floor holds without an additional test:

\[
 \boxed{T_0(d)\ge h.} \tag{3}
\]

Indeed `C_1>=2`, while its following reached `T_1` has physical duration at least `2(h-1)+1`: every reached level-one root has height `h-1`. Thus `g_0(d)>=2h+1`. The parity of C and T makes `g_0(d)` odd.

If the original top gap at label `i=lambda_1(2d)` is zero and `T_0(d)<=H_C<r`, the original predecessor-count theorem identifies the virtual endpoint with the actual top-level return. The full spatial-lap alternative needs at least `n_0=2r+1` physical time and cannot occur within `G_C`. Conversely every top-zero actual short birth has this virtual endpoint. This is the exact connection with the partner family `F_(0,C)`.

## 3. Exact two-query replay theorem

For every signed integer `d`, put

\[
 b_d=\lambda_2(2d)\pmod{p_1},\qquad
 u_d=Z_{1,b_d},\qquad v_d=Z_{1,b_d-1}. \tag{4}
\]

All indices are original persistent labels. The two-query leaf word is

\[
 \boxed{(C_2T_2^{2u_d})(C_2T_2^{2v_d+1}).} \tag{5}
\]

Replay it chronologically on the ONE exposed `D_2` orbit starting at physical time `2d`. An exponent zero means that the corresponding T block is empty. No clock is restarted at a freshly rooted or independently sampled state.

### Theorem 1

Under (1), replay (5) exactly decides whether `T_0(d)<=H_C`, and gives the exact virtual endpoint whenever this holds. Replay may stop and reject as soon as its cumulative physical duration exceeds `G_C`. It need not identify an unrestricted long virtual endpoint through an invalid no-wrap expansion.

**Proof of the two labels.** The original selection cocycle for row one is `kappa_1(t)=lambda_2(t)`. Therefore the initial C1 query at time `2d` is exactly `Z_(1,b_d)`. The one-level clock partition gives `C_1 -> C_2 T_2^(2u_d)`. Its first child C changes the selected level-two site from `b_d` to `b_d-1`; every following child T returns to that same selected site. Hence completion of this C1 node leaves selected level-two label `b_d-1`. The next parent T1 consequently queries `Z_(1,b_d-1)` and expands as the second block in (5). This reasoning remains valid when `u_d>0` and at negative starting times. It needs neither an absolute level-one site nor a cumulative original gap sum.

**Forward cutoff implication.** If the actual virtual C1T1 word has duration at most `G_C`, its whole horizon satisfies the source no-wrap hypothesis at both levels. The two one-level partitions are therefore exact, and (5), with these original labels, has the same endpoint.

**Reverse cutoff implication.** If candidate (5) finishes within `G_C`, group its first block into C1 and its second into T1. Every child interval lies inside this same short horizon. Condition (1) excludes the wrap alternatives in each reverse grouping, so both are actual parent clocks. Their concatenation is exactly the virtual C1T1 word. Thus a candidate exceeding the cutoff cannot conceal a virtual endpoint within it: the forward implication would force equality. These arguments use time differences only and apply across physical time zero as well. `square`

## 4. Commutation and a count interval depending only on adjacent sums

The endpoint maps C and T commute exactly. To see this, begin at any selected site `i`. Strict alternation of selections of `i` and `i-1` gives the order

\[
 t<\text{first later }(i-1)<\text{first later }i
   <\text{second later }(i-1).
\]

Both CT and TC end at that second later predecessor selection, in the same physical state. Repeated adjacent swaps therefore preserve the endpoint of any finite C/T word. This endpoint statement does not declare the intermediate clock roots independent.

Consequently (5) has the same endpoint as

\[
 \boxed{C_2^2T_2^{2w_d+1},\qquad
 w_d=Z_{1,b_d}+Z_{1,b_d-1}.} \tag{6}
\]

Let `a_d` be the first later selection time of `b_d-1` in `lambda_2`, starting after `2d`; this is the first C2 endpoint. The endpoint of (6) is the `(2w_d+2)`-nd selection of `b_d-2` **strictly after `a_d`**. Visits of that label before `a_d` are not counted.

For an integer `l>=0`, define the exposed count

\[
 B_d(l)=\#\{t\in\mathbb Z:a_d<t\le2d+2l+1,
                    \ \lambda_2(t)=b_d-2\pmod{p_1}\}, \tag{7}
\]

with value zero when the upper endpoint is at or before `a_d`. Both the strict lower endpoint and inclusive upper endpoint in (7) are part of the definition.

For candidate phases

\[
 \mathcal D_C=\{j-H_C-1,\ldots,j\},\qquad
 L_d=\max(h,j-d-1,1), \tag{8}
\]

set the following integer interval to be empty if `L_d>H_C` or its endpoints are reversed:

\[
 \boxed{I_d^{(2)}=
 \left[\left\lfloor\frac{B_d(L_d-1)}2\right\rfloor,
       \left\lfloor\frac{B_d(H_C)}2\right\rfloor-1\right]
       \cap\mathbb Z.} \tag{9}
\]

Every item in (8)–(9), including `b_d`, `a_d`, and the count function, is measurable from `E_2`. Theorem 1, parity, and the order-statistic description above give the exact test

\[
 \boxed{\{T_0(d)\le H_C,\ j\in J_d^*\}
       \quad\Longleftrightarrow\quad w_d\in I_d^{(2)}.} \tag{10}
\]

To check the endpoints explicitly, the upper cutoff requires
`B_d(H_C)>=2w_d+2`. The lower lifetime requirement `T_0(d)>=L_d` requires that the designated odd endpoint occur strictly after `2d+2L_d-1`, equivalently `B_d(L_d-1)<=2w_d+1`. These two inequalities are precisely (9). The overlap requirement is `T_0(d)>=j-d-1`; (3) supplies the height floor already included in `L_d`. Thus (10) retains the deletion boundary `j=R_0(d)` and insertion boundary `j=d`.

A related general identity is useful only when the actual one-level no-wrap clock partition is valid throughout the parent word: a chronological parent word with `a` C nodes and `b` T nodes queries its first `a+b` original incoming coordinates and expands, after commuting child endpoint maps, to `C^(a+b) T^(b+2 sum z)`. Its chronological starting indices still have to be justified in the actual phase. Endpoint commutation alone does not authorize expansion of a long parent word, or remove the indexing or conditioning obligation.

## 5. Deterministic query union and the actual conditional law

Define the exposed index union

\[
 \boxed{Q_C(E_2)=\bigcup_{d\in\mathcal D_C}\{b_d,b_d-1\}
               \subseteq\mathbb Z_{p_1}.} \tag{11}
\]

It is chosen before reading any free row-one value, and

\[
 |Q_C(E_2)|\le2(H_C+2). \tag{12}
\]

Query each free coordinate of this union once, retain its value, and reuse it in every test (10). Coordinates `0,-1` return their forced zeros. Repeated phases and coincident labels create shared variables, not independent replicas. No row-zero coordinate is queried.

The virtual eligible phase count is therefore the exact function

\[
 \boxed{N_{c\to C}=
 \sum_{d\in\mathcal D_C}\mathbf1_{
 Z_{1,b_d}+Z_{1,b_d-1}\in I_d^{(2)}}.} \tag{13}
\]

The subscript records its BASE incidence law at `c` and its partner cutoff `C`. It is measurable from `E_2` and at most `2(H_C+2)=O_C(sqrt r)` original row-one queries.

Conditional on every feasible `E_2` on the safe event, these queries read the exact uniform composition of `ell_1` into `p_1-2` free coordinates described in Section 1. The environment is not reweighted or replaced. At `d=0`, `b_0=0` and the two forced row-one values are zero; feasibility of `E_2` makes the base phase eligible. Since `C>=c`, increasing the partner cutoff retains that eligibility.

## 6. Exact comparison with distinct eligible top labels

Let

\[
 k_{c\to C}=\#\{i\in\mathbb Z_{p_0}\setminus\{0\}:
 \exists d\in\mathcal D_C,\ \lambda_1(2d)=i,
 \ T_0(d)\le H_C,\ j\in J_d^*\}. \tag{14}
\]

This is the original distinct-label gate, with the larger partner cutoff allowed. The algorithm does not need to compute the individual labels in (14).

### Theorem 2

Pointwise on the safe base-incidence event,

\[
 \boxed{k_{c\to C}+1\le N_{c\to C}\le k_{c\to C}+2.} \tag{15}
\]

In particular, divergence in base-incidence probability of these two quantities is equivalent, for each fixed `c,C`. At `C=c`, `k_(c->c)` is exactly `k_0` in the top-zero overlap reduction.

**Proof, including interval boundaries.** Fix an original level-one physical label `i`. Enumerate its even selection times bi-infinitely as

\[
 \ldots<2d_{-1}<2d_0<2d_1<\ldots.
\]

Such an enumeration exists by the full-label property and finite invertibility. Consecutive selections of the same label are separated by odd physical times, so its even selections are every second selection. Starting at `2d_k`, strict alternation puts the second later selection of `i-1` after the intervening odd-time selection of `i` and strictly before its next even selection `2d_(k+1)`. The first later predecessor selection has even relative time; the next same-predecessor gap is odd. Thus this second predecessor selection is at an odd absolute time `t_k^*`, and its virtual edge endpoint satisfies

\[
 \boxed{d_k+1\le r_k^*:=(t_k^*+1)/2\le d_{k+1}.} \tag{16}
\]

This is a direct fact about the virtual-zero intervals `[d_k,r_k^*]`. It does not require pretending to set all actual top-row gaps to zero, or altering any composition.

If `d_m<j<d_(m+1)`, only interval `m` can cover `j`: all preceding intervals end no later than `d_m`, and all following ones start no earlier than `d_(m+1)`. If `j=d_m`, only intervals `m-1` and `m` can cover it. The former contributes only when its inclusive right endpoint equals `j`; the latter includes its left endpoint `j`. This is the only possible doubling.

The equality `j=d_m` for a label can occur only for the unique currently selected label `i=lambda_1(2j)`. Hence every other label contributes at most one eligible phase, and the current label contributes at most two. Restricting to phases in `mathcal D_C` and lifetimes at most `H_C` only removes intervals and preserves the bound.

The eligible label set includes the original base label zero, because the sampled base interval covers `j` and its lifetime is at most `H_c<=H_C`. Thus the number of distinct eligible labels is exactly `k_(c->C)+1`. Each contributes at least one phase, and at most one extra phase is possible globally. This proves (15). Negative birth indices and intervals crossing time zero are covered by the same bi-infinite ordering argument. For large `r`, `H_C+2` is below the physical cycle period, so the candidate window has no duplicate representatives of one physical birth. `square`

More precisely, (15) gives the shifted lower-tail brackets

\[
 \mathbb P(N_{c\to C}\le m+1)
 \le\mathbb P(k_{c\to C}\le m)
 \le\mathbb P(N_{c\to C}\le m+2) \tag{17}
\]

under the safe conditioned base law, for every deterministic threshold `m`, including a threshold depending on `r`. Under the full base-incidence law, an `o(1)` safe-exception error may be added to these brackets. Divergence in probability is therefore equivalent, but arbitrary moving lower-tail thresholds cannot be equated without their additive shifts. The exact function (13) tests the phase count without reconstructing absolute top-label indices. This is a reduction, not a proof that either count diverges.

## 7. Proved growing-query transfer under the same actual environment

The independently audited theorem in `PBBS_GROWING_ADAPTIVE_GAP_QUERY_FRESHNESS_20260908.md`, especially its actual-incidence estimate (8), applies to (11)–(13). The number of free row-one requests is at most `M=2(H_C+2)=O_C(sqrt r)`, and their indices are `E_2`-measurable.

Define the comparison counter by first sampling `E_2` with its SAME actual base-incidence marginal. Conditional on that environment, set `G_0=G_{-1}=0`, assign independent marks to the other distinct indices of `Q_C(E_2)` with

\[
 \mathbb P(G_i=a\mid E_2)=\frac89\left(\frac19\right)^a,
 \qquad a=0,1,2,\ldots, \tag{18}
\]

and cache every repeat of an index. Thus `Geom(1/9)` here denotes the geometric law on the nonnegative integers with ratio `1/9`. Apply the exact same function as in (13):

\[
 \widetilde N_{c\to C}
 =\sum_{d\in\mathcal D_C}
   \mathbf1_{G_{b_d}+G_{b_d-1}\in I_d^{(2)}}. \tag{19}
\]

### Corollary 3

For every fixed `0<c<=C<infinity`, the joint laws under this common environment marginal satisfy

\[
 d_{\mathrm{TV}}\bigl(\mathcal L(E_2,N_{c\to C}),
                         \mathcal L(E_2,\widetilde N_{c\to C})\bigr)
 =o(1). \tag{20}
\]

On the accepted safe event, the mean conditional total variation is
`O_(c,C)(r^(-1/4) sqrt(log r))` plus the profile-tail error. Restoring the safe exceptions adds `o(1)`. This is an averaged conditional estimate, equivalently a joint estimate with the common actual `E_2` marginal; it is not claimed uniformly over every feasible environment.

**Proof.** Conditional on a safe feasible environment, the actual free marks form a uniform weak composition of `ell_1` into `P_1=p_1-2` labelled parts. Original-depth profile concentration under the actual incidence law gives `P_1` of order `r` and mean-matched geometric ratio

\[
 q_{1,r}=\frac{\ell_1}{\ell_1+P_1}
       =\frac19+O\!\left(\sqrt{\frac{\log r}{r}}\right)
\]

outside a profile event of arbitrarily small polynomial probability. The growing-query theorem compares at most `M` fresh individual requests with cached independent geometric replies. Its mean conditional error is bounded by

\[
 O_{c,C}\!\left(\frac{M+\log r}{r}
           +\sqrt{\frac{M\log r}{r}}\right)
\]

plus that profile error. With `M=O_C(sqrt r)`, this is the stated rate. The index union, the intervals `I_d^(2)`, and the finite function (13) are already determined by the environment and these replies. Data processing therefore proves (20) on the safe event. Assigning the same arbitrary output on its complement and then restoring the original count costs at most the safe-exception probability, which tends to zero. `square`

In particular, under the stated base-incidence laws,

\[
 k_{c\to C}\xrightarrow{\mathbb P}\infty
 \quad\Longleftrightarrow\quad
 N_{c\to C}\xrightarrow{\mathbb P}\infty
 \quad\Longleftrightarrow\quad
 \widetilde N_{c\to C}\xrightarrow{\mathbb P}\infty. \tag{21}
\]

The first equivalence uses (15), with its safe-exception error, and the second uses (20). Formula (20) also compares every event depending on `(E_2,N)` with the same event for `(E_2,tilde N)`, including arbitrary moving count thresholds; the comparison with `k` still requires the shifts in (17).

The actual row-one marks remain a conditional uniform composition. The independent geometric marks define the comparison counter only. They do not reconstruct an entire independent-geometric array as a valid PBBS root, assign an unweighted law to `D_2`, or condition again on an oracle base lifetime. Base eligibility is already preserved by exposed feasibility and the forced zeros.

The remaining gate is abundance of the feasible virtual phases in the actual deeper environment, expressed equivalently by divergence of (19). This note proves the finite-query interface and the equivalences (20)–(21), not that divergence, an occupied-support estimate, a packing improvement, or coefficient one.
