# Integrated verdict on monotone-radius rotor braids

## Verdict

The local rotor theorem is correct after replacing the claimed canonical
state recurrence by a refined-state invariant.  The fractional central-band
cover and its `o(W)` reset ledger are also correct.  A safe asymptotic choice
within the proved width-order tail theorem is

\[
h=\lceil\sqrt{m\log m}\rceil,\qquad H=m-h.
\]

The construction does **not** yet prove the constant-one theorem.  The
integral statement must include per-rank incidence quotas, and its
low-duplicate form is stronger than the smallest known sufficient shadow-
coverage lemma.

Cross-depth sharing itself was already present in one fixed radius-`h`
long-run atom: a saturated radius-`h` chain exposes every shallower depth
using the same updates.  The genuinely new rotor feature is selective
truncation of the radius along one queue, which realizes the exact SCD quota
profile without extra resets.  It does not lower the cost of the weaker
missing-only OR formulation.

## Correct local theorem

For a nonincreasing radius profile (d_0\ge\cdots\ge d_{H-1}), one literal
MTF word of length

\[
H+2d_0+1
\]

exposes (H) pairwise disjoint saturated chains.  After a strict radius
drop the complete state is not the next canonical partition: stale singleton
blocks remain.  They lie after the useful chain prefix and stay harmless
under every later radius decrease.  Every chain member is a literal suffix
OR, so no extra pin theorem is needed.

## Correct fractional theorem

With (W={2m\choose m}), (N_q={2m\choose m-q}), and
(ho_q=N_q/W), use

\[
a_q=\lfloor H\rho_q+U\rfloor
\]

for one common uniform (U\in[0,1)).  This is an integral monotone profile
with (mathbb E a_q=H\rho_q).  Coordinate symmetry gives load (H/W) to
every band mask, so total atom mass (W/H) is an exact fractional cover.
Its reset mass is at most

\[
(2h+1)W/H=o(W).
\]

## Correct integral gate

For each depth and rank sign, write (T_q^\sigma,D_q^\sigma,M_q^\sigma)
for total incidence, duplicate excess, and missing masks.  Exactly

\[
M_q^\sigma=N_q+D_q^\sigma-T_q^\sigma.
\]

Hence a sufficient rotor-packing theorem must require both

\[
\sum_{q,\sigma}|T_q^\sigma-N_q|=o(W)
\]

and

\[
D_0+\sum_{q=1}^h(D_q^-+D_q^+)=o(W).
\]

Atom count plus small duplicate mass alone does not control an undersupplied
rank.  Under these corrected hypotheses, concatenation, literal central
repairs, and the established shared two-tail word do prove (W+o(W)).

## Quantitative obstruction to routine rounding

Same-row normalized pair codegrees are (Theta(m^{-2})), but adjacent-depth
nested masks have normalized codegree (Theta(m^{-1})).  A typical atom has
((\sqrt\pi+o(1))m^{3/2}) exposed masks.  Thus a black-box fixed-uniformity
nibble is not justified.

Independent rounding is decisively wrong: (W/H) independent atoms have

\[
\mathbb E\sum D_q=
  (\sqrt\pi/e+o(1))W\sqrt m,
\]

and already (mathbb E D_0=(e^{-1}+o(1))W).  The desired theorem must be a
correlated multidepth packing.

## Small exact benchmark and comparison with the weaker route

At (m=3,h=1,H=2), ten explicit atoms partition every mask in ranks
(2,3,4) exactly.  This gives the first zero-duplicate integral certificate.

At (m=4,h=1,H=3), the analogous exact benchmark has been encoded after
coordinate-symmetry reduction (864,951 variables and 2,404,043 clauses).
The first bounded exact run returned UNKNOWN; no SAT or UNSAT claim is made.

The corrected rotor lemma is sufficient but not the weakest known target.
It asks for near-bijection at every band rank—essentially a truncated SCD.
For OR coverage, nonmiddle duplicate representations cost nothing.  The
existing exact-middle MSW wreath route only asks that the summed number of
missing shadows be (o(W)), and is therefore the more economical main
target unless the extra rotor structure makes its stronger packing theorem
provable.

## Files

- `MONOTONE_RADIUS_ROTOR_BRAIDS_AUDIT.md`
- `MONOTONE_QUEUE_PACKING_CODEGREES.md`
- `ROTOR_PACKING_SMALL_EXACT.md`
- `ROTOR_PACKING_NEXT_PROMPT.md`
- `scratch/audit_monotone_radius_rotor_suffix.py`
- `scratch/verify_rotor_packing_m3.py`
