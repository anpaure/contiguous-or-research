# Audit of the SCD `a`-current phase count versus the GK aligned-C collision count

Date: 2026-08-01  
Lane: K / four-row SCD phase forest / rooted connector cuts  
Status: exact symbolic audit.  The GK collision variable and the variable in
the `a`-connector current are different.

## 0. Result

Put

\[
 c=\operatorname {Cat}_{m-1},\qquad
 E={2m-3\choose m-3},\qquad
 J={2m-3\choose m-4},\qquad I=E-J,
\]

and let

\[
 A=A_C,qquad d_s=D_{\rm short},\qquad d_\ell=D_{\rm long}
\]

be the numbers of aligned-long-C, short-D, and long-D choices among the
`E` missing `aU` target rows.  Thus

\[
                         A+d_s+d_\ell=E.                 \tag{0.1}
\]

The exact distinction is

\[
 \boxed{q_{\rm GK}=A,\qquad q_{\kappa_a}=A+d_s.}          \tag{0.2}
\]

Indeed, the GK collision map is the underlying aligned-C head map

\[
                   \psi(R)=R+x,                           \tag{0.3}
\]

whose physical auxiliary row is `azS -> az psi(R)` and whose rooted lower
tail is `azR`.  A short-D auxiliary row is instead

\[
                   zS\longrightarrow zL.                 \tag{0.4}
\]

The rows have different `{a,z}` signatures on their rooted lower tails and
physical heads, so (0.4) is not a point of the map in (0.3).  In contrast,
both rows improve the directed `a`-connector cut, by two different
mechanisms.

For every exact-upper, lower-injective selection in the ordinary flexible
phase grammar,

\[
 \boxed{
 H_a=E-A,\qquad
 t_a=c-d_s,\qquad
 S_a=c+d_s,\qquad
 \kappa_a=c-E+A+d_s+1.}                                  \tag{0.5}
\]

These identities remain valid after adding any number of the audited
first-stage short-chain `h` provider rethreads: such a rethread changes
neither the `a`-hole count nor the `a`-source count.

## 1. Literal phase rows

The fixed four-row incidence matching is

\[
\begin{array}{c|cc}
\text{lower root}&\text{long chain}&\text{short chain}\\ \hline
azR&azS&-\\
zS&zL&azS\\
aS&aL&aL\\
L&U&zL.
\end{array}                                               \tag{1.1}
\]

This is recorded in
`MATH_THEOREM_R_FOUR_ROW_SCD_CPHASE_ACYCLIC_BRANCHING_AND_DIAGONAL_HALL_CUT_20260801.md`,
lines 94--127.  The three possible `aU` auxiliary rows are recorded in
`MATH_THEOREM_THREAD_D_SCD_FLEXIBLE_DETACHMENT_POTENTIAL_SCOPE_20260801.md`,
lines 94--116:

\[
\begin{array}{c|c}
\text{phase}&\text{physical auxiliary arrow}\\ \hline
\text{long aligned C}&azS\to az(R+x),\\
\text{long reversed D}&zL\to azS,\\
\text{short D}&azS\to zL.
\end{array}                                               \tag{1.2}
\]

In rooted-lower notation these auxiliary tails are respectively `azR`,
`zS`, and `zS`.  Hence the map on long chain bottoms

\[
                              \psi(R)=R+x               \tag{1.3}
\]

counts aligned-C rows only.  Neither D row belongs to its domain, and the
short-D physical head lacks `a`, unlike every aligned-C physical head.
Consequently an image bound for (1.3) is an upper bound on `A`, not on
`A+d_s`.

There is also a literal finite refutation of the conflated reading.  The
authenticated `m=9` forest reports

\[
                         A=1974,\qquad d_s=1133.
\]

Thus `A+d_s=3107`, while the aligned-C image size is

\[
 E-K=5005-{14\choose5}=3003,
 \qquad K={2m-4\choose m-4}.
\]

The PASS line is
`scratch/h2_k17_m9_scd_multiblock_upper_20260801/phase_m9.root.audit.stdout`.
It is consistent with `A<=E-K` and incompatible with
`A+d_s<=E-K`.

## 2. Exact `a`-hole and source ledger

The unused-lower signature ledger is

\[
\begin{array}{c|c}
\text{signature in }\{a,z\}&\text{number}\\ \hline
\varnothing&c,\\
a&0,\\
z&c-J+A,\\
az&E-A.
\end{array}                                               \tag{2.1}
\]

See
`MATH_THEOREM_THREAD_D_SCD_PHASE_FOREST_ENDPOINT_COCYCLE_AND_Z_CONNECTOR_CUT_20260801.md`,
lines 120--152.  The only unused roots containing `a` are therefore the
`azR` roots left by D choices, proving

\[
                               H_a=E-A.                   \tag{2.2}
\]

For a hole `K`, write `M_0(K)=K+e(K)` and put

\[
                     t_a=|\{K\in H:e(K)=a\}|.             \tag{2.3}
\]

By (1.1), the roots with `e(K)=a` are exactly `zS` on short central
chains, because

\[
       M_0(zS)=azS\quad\hbox{on a short chain},            \tag{2.4}
\]

whereas on a long chain `M_0(zS)=zL=zS+x`.  The other possible holes have
`M_0(L)=zL` on a short chain and `M_0(azR)=azS` on a long chain, so their
added coordinates are `z` and `rho`, not `a`.

There are exactly `c` short chains.  A short-D option consumes exactly its
own rooted auxiliary tail `zS`; see the phase table cited above, and the
literal semantic check in
`scratch/audit_scd_global_seed_detachment_sat_models_20260801.cpp`, lines
205--238.  Tail/provider capacity makes the consumed short roots distinct.
No all-`G` option can consume a short `zS`: its two permitted
auxiliary physical owners contain no `a`, whereas (2.4) contains `a`.  This
is also explicit in the semantic checker
`scratch/audit_scd_global_seed_detachment_sat_models_20260801.cpp`, lines
241--274.  Long-D rows consume long `zS` roots.  It follows that exactly
`c-d_s` short `zS` roots remain holes, so

\[
                               t_a=c-d_s.                 \tag{2.5}
\]

The universal endpoint identity

\[
                  S_q=2c-t_q                             \tag{2.6}
\]

is proved in the phase-forest note cited above, lines 158--180.  Equations
(2.2), (2.5), and (2.6) now give all of (0.5).

As an independent executable check, lines 171--181 of
`scratch/audit_threadD_scd_swapped_phase_components_20260801.py` assert
exactly

\[
                     \kappa_a=c-E+A+d_s+1                \tag{2.7}
\]

against each reconstructed saved forest.

## 3. Consequences of the exact aligned-C image count

Assume the independently proved GK image bound

\[
                       A\le E-K,
 \qquad K={2m-4\choose m-4}.                              \tag{3.1}
\]

There are only `c` short providers, hence `d_s<=c`; also (0.1) gives
`A+d_s<=E`.  Therefore

\[
 A+d_s\le \min\{E,E-K+c\},                               \tag{3.2}
\]

and (0.5) yields the sharpest bound supplied by these rows alone:

\[
 \boxed{\kappa_a
 \le c+1-\max\{0,K-c\}.}                                 \tag{3.3}
\]

Since

\[
 {K\over c}={(m-2)(m-3)\over2(2m-3)},                    \tag{3.4}
\]

one has `K>c` for every `m>=8`, and then

\[
                         \kappa_a\le2c-K+1.              \tag{3.5}
\]

In particular `K>2c+1` for every `m>=12`, so the `a` cut alone is
universally negative in that range inside this fixed-GK grammar.

## 4. First-stage `h` rethreads and neutral conjugate transfer

Let `p<=c` be the number of audited first-stage short-chain provider
rethreads.  Their exact effect is

\[
               \Delta\kappa_z=p,\qquad \Delta\kappa_a=0. \tag{4.1}
\]

The `z` statement is the corrected one-unit ledger in
`MATH_AUDIT_R_SCD_PHASE_DETACHMENT_SAT_AND_CONNECTOR_GATE_20260801.md`,
lines 526--565.  For `a`, the rethread exchanges an old and a new lower tail
both avoiding `a`, and an old and a new physical source both avoiding `a`;
the ordinary short-D second stage, if selected, has already been counted in
`d_s`.

Since the ordinary forest has `kappa_z=1-I`, (0.5) and (4.1) give

\[
 \kappa_a+\kappa_z
   =c-E-I+2+A+d_s+p.                                      \tag{4.2}
\]

Using (3.1), `d_s<=c`, and `p<=c`,

\[
 \boxed{\kappa_a+\kappa_z\le3c-I-K+2.}                    \tag{4.3}
\]

Moreover

\[
 {K+I-3c\over c}
 ={m^3-8m^2-21m+48\over2(2m-3)(m+1)}.                    \tag{4.4}
\]

At `m=10`, `K+I-3c=494`, and the right side of (4.3) is `-492`.
The rational coefficient in (4.4) is positive and increasing thereafter;
hence (4.3) is strictly negative for every `m>=10`.

Finally, every neutral common-`M_0` conjugate component switch satisfies

\[
                 \Delta\kappa_a+\Delta\kappa_z=0,         \tag{4.5}
\]

as proved in Section 11, lines 577--612, of the phase-detachment audit.
Consequently such switches cannot escape the negative-sum obstruction in
(4.3).

## 5. Scope

The proved formulas and bounds concern:

1. the standard GK fixed-`M_0` flexible phase catalogue;
2. the audited first-stage `h` provider rethreads, at most one per short
   chain; and
3. neutral conjugate switches for which (4.5) applies.

They do not obstruct a prospective SCD or owner matching, a non-GK
head-injective factor, a packet with positive total two-coordinate current,
or a support-first construction outside this phase fibre.
