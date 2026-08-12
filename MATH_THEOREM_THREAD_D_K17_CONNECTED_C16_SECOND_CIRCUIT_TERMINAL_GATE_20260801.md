# Thread D: exact terminal gate after the connected `H`-`C16` near-winner

Date: 2026-08-01  
Status: exact algebra and independently replayed input certificate.  This note
does not claim that a repairing second circuit exists.  It identifies the
smallest complete finite search and the exact terminal inequalities it must
satisfy.

Finite-search update: the subsequent note
`MATH_THEOREM_THREAD_D_K17_CONNECTED_DEBT2_SECOND_CIRCUIT_AND_PAIRED_SWITCH_GATE_20260801.md`
executes this gate and closes every simple one-side circuit through support
`11` (`C22`).  The present note remains the topology/compound-rectangle proof.

## 0. Audited state

Start with incidence perfect matchings `D,H` between the 1,430 quotient
rank-nine owners and rank-eight facets.  Regard both matchings as maps from
owners to facets and put

\[
                         \pi=H^{-1}D.                 \tag{0.1}
\]

The frozen first move is the `H` assignment circuit of support eight
(bipartite length 16)

\[
 (425,395,396,665,650,608,157,135),                  \tag{0.2}
\]

with old incidence IDs

\[
 (3829,3559,3567,5988,5854,5477,1415,1216)          \tag{0.3}
\]

and new incidence IDs

\[
 (3826,3558,3569,5989,5856,5478,1417,1219).         \tag{0.4}
\]

Independent reconstruction of all 2,860 matching rows gives

\[
 c(\pi)=1,\qquad |\pi|=1430,\qquad V(\pi)=9\pmod {17}.             \tag{0.5}
\]

Hence its physical lift is one 24,310-cycle.  The rank-ten palette is
complete, with load histogram

\[
                    1^{878}2^{247}3^{18}4^1,          \tag{0.6}
\]

and the rank-seven palette has histogram

\[
                    0^2 1^{874}2^{249}3^{18}4^1.     \tag{0.7}
\]

Its two holes are

\[
                    h_0=0x00e0f,\qquad h_1=0x01547.  \tag{0.8}
\]

The old complement-dual `A^2` identity survives on exactly 1,422 rows, as
it must: the first circuit changed precisely eight `H` rows.  Thus the state
is genuinely non-dual, and upper and lower palettes must be audited
separately.

## 1. State-relative palette derivative

For an incidence edge pair meeting at an owner, write `L(d,h)` for its
aligned rank-seven intersection orbit.  For a pair meeting at a facet,
write `U(d,h)` for its aligned rank-ten union orbit.  These are the literal
`lower_turn` and `upper_turn` maps, including stored shifts; quotient set
intersection or union without gauge alignment is not a substitute.

Let `mu_r(T)` be the current load of target `T` on shore `r`.  For any
second matching circuit, let `O_r` and `N_r` be the multisets of old and new
turns on that shore, and define

\[
 \Delta_r(T)=N_r(T)-O_r(T).                           \tag{1.1}
\]

### Theorem 1.1 (exact terminal palette row)

The second circuit preserves both complete palettes, repairing the two
rank-seven holes, if and only if

\[
                     \mu_r(T)+\Delta_r(T)\ge 1       \tag{1.2}
\]

for every target on both shores.

Equivalently, for every currently covered target its net deletion is at
most its reserve

\[
       O_r(T)-N_r(T)\le \rho_r(T):=\mu_r(T)-1,        \tag{1.3}
\]

while on the lower shore

\[
                     N_7(h_j)\ge1\quad(j=0,1).       \tag{1.4}
\]

Here `O_7(h_j)=0`, since an absent target cannot be deleted.

#### Proof

Only turns incident with changed matching edges can change.  Removing their
old occurrences and inserting their new occurrences gives (1.1) exactly,
with multiplicity.  A palette is complete precisely when every final load
is positive.  This is (1.2); separating zero and positive current loads
gives (1.3)--(1.4).  \(\square\)

This is the exact **two-circuit** derivative as well.  If the first circuit
has derivative `Delta_1` and the second is evaluated in the state produced
by it, then

\[
                    \mu_2=\mu_0+\Delta_1+\Delta_2.   \tag{1.5}
\]

What is invalid is adding a precomputed baseline column for the second
circuit when the two supports interact.  In that case its old turns have
changed.  One must either compute `Delta_2` relative to the first state or
reconstruct the terminal turns directly.  No intermediate palette
completeness is needed for an atomic two-circuit packet.

## 2. Exact `H`- and `D`-circuit ledgers

Let `u_0,...,u_(t-1)` be distinct owners, indices modulo `t`.

### 2.1 `H` circuit

Put `f_i=H(u_i)`.  Suppose there is a chosen incidence

\[
                         e_i:u_i\longrightarrow f_{i+1}.          \tag{2.1}
\]

Replacing `H(u_i)` by `e_i` is exactly the assignment cycle
`sigma=(u_0 ... u_(t-1))`:

\[
                         H'=H\sigma,qquad
                         \pi'=\sigma^{-1}\pi.          \tag{2.2}
\]

Its complete local turn multisets are

\[
\begin{aligned}
 O_7&=\{L(D(u_i),H(u_i)):i\},&
 N_7&=\{L(D(u_i),e_i):i\},\\
 O_{10}&=\{U(D^{-1}(f_i),H(u_i)):i\},&
 N_{10}&=\{U(D^{-1}(f_i),e_{i-1}):i\}.              \tag{2.3}
\end{aligned}
\]

The selected new incidences must exist literally and be distinct from the
corresponding `D` edges.

### 2.2 `D` circuit

Put `f_i=D(u_i)` and choose incidences

\[
                         e_i:u_i\longrightarrow f_{i+1}.          \tag{2.4}
\]

Then

\[
                         D'=D\sigma,qquad
                         \pi'=\pi\sigma,              \tag{2.5}
\]

and

\[
\begin{aligned}
 O_7&=\{L(D(u_i),H(u_i)):i\},&
 N_7&=\{L(e_i,H(u_i)):i\},\\
 O_{10}&=\{U(D(u_i),H^{-1}(f_i)):i\},&
 N_{10}&=\{U(e_{i-1},H^{-1}(f_i)):i\}.              \tag{2.6}
\end{aligned}
\]

Again the new incidences must be literal and avoid the opposite matching.
Equations (2.3) and (2.6), followed by (1.2), include every cross term.

## 3. Exact topology and the odd-support law

The usual sign test is necessary but not sufficient.  There is nevertheless
an exact order test requiring no factor reconstruction.

List the selected owners as `v_0,...,v_(t-1)` in their cyclic order on the
current Hamilton cycle `pi`.  Let `alpha` be the permutation of
`Z/tZ` determined by

\[
                         \sigma(v_j)=v_{\alpha(j)},                \tag{3.1}
\]

and let `s(j)=j+1`.

### Theorem 3.1 (segment-contraction criterion)

For an `H` circuit, the number of cycles after the switch is the number of
cycles of

\[
                         \Phi_H=\alpha^{-1}s.         \tag{3.2}
\]

For a `D` circuit, it is the number of cycles of

\[
                         \Phi_D=s\alpha.              \tag{3.3}
\]

Consequently the second circuit preserves quotient Hamiltonicity exactly
when the relevant `Phi` is a `t`-cycle.

#### Proof

For (3.2), contract each old `pi` segment starting at `v_j` and ending just
before `v_(j+1)`.  Left multiplication by `sigma^{-1}` reconnects its end
to `sigma^{-1}(v_(j+1))=v_(alpha^{-1}(j+1))`.  Thus the contracted successor
is (3.2).

For (3.3), starting at `v_j`, the new map `pi sigma` jumps to the old
successor of `v_(alpha(j))` and follows that old segment until
`v_(alpha(j)+1)`.  The contracted successor is `s alpha`.  Contraction does
not change component count.  \(\square\)

Because a 1,430-cycle is an odd permutation,

\[
 \operatorname{sgn}(\pi')=
 (-1)^{t-1}\operatorname{sgn}(\pi)                 \tag{3.4}
\]

must again be odd.  Hence a **single second assignment circuit must have
odd support `t`**.  The smallest possibility is therefore support three,
that is a quotient `C6`; supports four, six, and eight are excluded by
topology alone in the connected state.

For `t=3`, the order test is especially sharp.  If `v_0,v_1,v_2` occur in
that order around `pi`, then

* an `H` circuit preserves one cycle exactly in the reverse order
  `sigma=(v_0 v_2 v_1)`; the forward order splits it into three;
* a `D` circuit preserves one cycle exactly in the forward order
  `sigma=(v_0 v_1 v_2)`; the reverse order splits it into three.

Thus the minimum exact search is not an arbitrary C6 census: only one of
the two cyclic orders for each selected triple can survive topology.

## 4. Voltage and physical lift

Let `s(e)` denote the stored shift of an incidence.  From the current
voltage `V=9`, an `H` circuit has

\[
 V'=9+\sum_i s(H(u_i))-\sum_i s(e_i)\pmod {17},       \tag{4.1}
\]

whereas a `D` circuit has

\[
 V'=9-\sum_i s(D(u_i))+\sum_i s(e_i)\pmod {17}.       \tag{4.2}
\]

Once Theorem 3.1 gives one quotient cycle, its physical lift is one cycle
if and only if `V'!=0`, since 17 is prime.

The assignment circuit itself need not have zero voltage.  Zero assignment
voltage means 17 parallel literal `C_(2t)` switches; nonzero voltage means
one longer translation-linked physical alternating circuit.  Both are
matching-exact when the complete incidence orbits are switched.

## 5. The smallest complete repair gate

Combining the preceding sections gives a duplicate-free exact test.

### Corollary 5.1 (second-C6 iff test)

A single second circuit repairs the connected C16 near-winner with minimum
support if and only if there are three owners and one of the two sides
`H,D` such that:

1. the three cyclically reassigned literal incidences exist and avoid the
   opposite matching;
2. their order is the unique Hamilton-preserving order stated after
   Theorem 3.1;
3. the three new lower turns include both `0x00e0f` and `0x01547`;
4. the six state-relative turn multisets (2.3) or (2.6) satisfy all reserve
   rows (1.2), on both shores;
5. the voltage (4.1) or (4.2) is nonzero;
6. any protected comparator/boundary incidence is either outside the
   support or is reproduced with the identical typed signature.

These conditions are jointly necessary and sufficient for a connected,
immediate-palette-exact physical factor.  Residence, deeper shadows, and
the compiler remain separate terminal tests.

A complete finite enumeration may anchor one new lower turn at `0x00e0f`,
walk the directed assignment graph until it closes after three steps, and
then require a new turn at `0x01547`.  Every repair contains such an anchor,
so this loses no solutions.  Rotation by the least incidence ID removes
only cyclic duplicates; reversal must not be identified because it changes
both topology and turn labels.

If no C6 passes, the next single-circuit supports are five and seven
(quotient C10 and C14).  Even supports need not be enumerated.

## 6. Smallest two-rectangle alternatives

A compound second move can instead use two assignment rectangles.  Let
`eta` be the product of the owner transpositions applied on `H`, and `tau`
the product of those applied on `D` (the identity if that side is unused).
The exact terminal successor is

\[
                         \pi'=\eta^{-1}\pi\tau.       \tag{6.1}
\]

Two transpositions have even total sign, so parity now permits a Hamilton
cycle.  There are three cases.

* For one `D` and one `H` rectangle, `pi tau` has two cycles, and (6.1) is
  Hamilton exactly when the two endpoints of `eta` lie in different cycles
  of `pi tau`.
* For two `D` rectangles, the first splits `pi`; the second must have its
  endpoints in the two different resulting cycles.
* For two `H` rectangles, the first left transposition likewise splits
  `pi`; the second must have its endpoints in the two different resulting
  cycles.

These are exact interlacing tests.  If the two transpositions on one side
share one owner, their product is a 3-cycle and the move is already the C6
case of Corollary 5.1.  Disjoint transpositions give the genuinely new
support-four compound class.

For this mixed packet the isolated H- and D-rectangle palette columns are
not generally additive.  Direct terminal formulas are

\[
\begin{aligned}
 L'_o&=L(D(\tau(o)),H(\eta(o))),\\
 U'_f&=U(\tau^{-1}D^{-1}(f),\eta^{-1}H^{-1}(f)).     \tag{6.2}
\end{aligned}
\]

All affected occurrences must be recomputed from (6.2) and tested by
(1.2).  Thus C6 is the smallest **single-circuit** gate, while two
interlacing rectangles are the other smallest compound gate.  Neither is
excluded here.

## 7. Scope and reproducibility

Authoritative inputs:

* `scratch/k17_dual_splice_dev5_independent_20260801/seed17931.minimum_debt_assignment_cycle.factor.tsv`, SHA
  `c082621d6444dc2283675882557d0240babb989f2d31847eb198fbe8b4612587`;
* `scratch/k17_dual_splice_dev5_independent_20260801/seed17931.minimum_debt_assignment_cycle.json`, SHA
  `d719fb01468188d827659d523677414cfb7b9244d5af567c42a87137bf19110b`;
* independent replay program
  `scratch/k17_dual_splice_dev5_independent_20260801/audit_factor_tsv.py`.

The replay reads every incidence row, reconstructs both perfect matchings,
all quotient and physical components, and both literal palette counters.
No search is used in this note.  In particular, the existence of the C6,
C10, C14, or mixed repair is still open.
