# Independent audit: heptagonal cap circulation, holonomy, and backup scope

**Date:** 2026-08-02  
**Audited source:** `MATH_THEOREM_HEPTAGONAL_CAP_CIRCULATION_AND_PROSPECTIVE_ABUNDANCE_20260802.md`  
**Verdict:** PASS for the literal phasewise `C14`, the quotient cap ledger, the rooted prospective count, and the finite `k=17` backup certificate, with the scope qualifications in Section 7.

## 1. Literal `C14` calculation

Write `C=X\{a,b,c}` and

\[
(H_0,\ldots,H_6)=(abc,abp,apq,pqs,cps,cpt,bct).
\]

The consecutive intersections, including the wrap, are

\[
ab,ap,pq,ps,cp,ct,bc.
\]

They are seven distinct pairs.  Hence

\[
x_i=C\cup H_i,\quad f_i=C\cup(H_i\cap H_{i+1}),\quad
y_i=f_i\cup\{z\}
\]

have ranks `r,r-1,r`, respectively, and both `x_i` and `x_{i+1}` meet
`y_i` in exactly `f_i`.  The moving incidence symmetric difference is

\[
x_0f_0x_1f_1\cdots x_6f_6x_0,
\]

a simple `C14`; the fixed `z` separates every retained owner from every
moving owner.  Finally

\[
x_i\cup y_i=C\cup H_i\cup\{z\},\qquad
x_{i+1}\cup y_i=C\cup H_{i+1}\cup\{z\}.
\]

Thus the new cap list is exactly the cyclic shift of the old cap list.  This
proves literal degree preservation and cap-*multiset* preservation, not only
support preservation.

## 2. Quotient holonomy and cap balance

For quotient increments `a_i`, one lap advances phase by

\[
h=\sum_i a_i\pmod m.
\]

On a free developed phase set this permutation has `gcd(m,h)` cycles, so
each developed moving circuit has length `tm/gcd(m,h)`.  For a cap orbit
`O`, direct deletion/insertion accounting gives

\[
M'(O)=M(O)-\mu^-(O)+\mu^+(O).
\]

Equality of the developed old and new cap multisets is equivalent to a
matching of quotient cap entries by orbit, equivalently to a row permutation
and phase shifts as stated in equation (1.15).

For the sequential matching `V_i=rho^{a_i}U_{i+1}`, uniqueness of the extra
coordinate outside the moving owner forces

\[
z_i=rho^{a_i}z_{i+1}.
\]

Multiplication around the circuit gives `z_0=rho^h z_0`.  Under a free
coordinate action this rules out the naive fixed-label sequential cap rotor
when `h` is nonzero.  Therefore a coprime-voltage development genuinely
needs a nonsequential cap permutation, duplicate-cap slack, or a compound
terminal repayment.

## 3. Counts

For fixed `(X,a)`, the seven free roles are chosen in

\[
(r-1)(r-2)(k-r)_4(k-r-4)
\]

ways.  This is `Theta(k^7)` in the central regime.  Fixing any nonanchor
owner/facet/cap/row token fixes at least one of those seven roles; the stated
`O(k^6)` central-token load follows by a finite role-pattern union bound.

For a coprime step `h`, a rank-`r` cyclic word with exactly `s` positive runs
is counted by

\[
\frac{k}{s}{r-1\choose s-1}{k-r-1\choose s-1}.
\]

Fixing one run-boundary coordinate removes the factor `k/s`, giving, at
`s=7`,

\[
{r-1\choose6}{k-r-1\choose6}.
\]

Ordering the seven deletions and seven insertions contributes `(7!)^2`.
Each of seven retained rows has `k-r-1` raw outside-extension choices before
the finite literal simplicity exclusions.  Consequently the advertised

\[
{r-1\choose6}{k-r-1\choose6}(7!)^2\,\Omega(k)^7
\]

is a valid *prospective raw socket* count.

At `k=17,r=9`, the literal formula gives `376320`; the frozen atlas reports
the same count.  The run formulas give `476` seven-run owners and `196`
through the fixed boundary coordinate, again matching the audit.  The four
audited central token types have maximum nonanchor load `47040`.

## 4. Independent finite cap-backup replay

Reading the seven quotient rows of `longrun2754.trace.tsv` gives arc-voltage
sum

\[
10+12=22=5\pmod {17}.
\]

The four cap orbits retained on both sides are

\[
15083,15979,23915,23979.
\]

The three net-removed cap orbits are

\[
13783,27447,28075,
\]

and all three have incumbent load exactly two.  They are replaced by

\[
13727,28331,43755.
\]

Thus the phrase "three load-two cap backups" is correct as an orbit-load
ledger: one copy of each removed orbit survives.  It does **not** assert
that three independently planted physical backup packets have already been
constructed.

The frozen replay also gives one developed moving circuit of length
`7*17=119`, one factor component before and after, exact immediate-upper
support, and per-coordinate short-run/deficit drift `(-4,-6,-4,-6)`.

## 5. Correct recurrence interface

A protected Pascal/pull-ear state that uses these circuits must export at
least

\[
(h,\partial_{\rm cap},\mathcal H,\mathcal P),
\]

where `h` is holonomy, `partial_cap(O)=mu^+(O)-mu^-(O)`, `mathcal H` is the
two-polarity boundary-history transfer state, and `mathcal P` records the
private owner/facet/occurrence resources.  A packet is cap-admissible against
the incumbent cap-load vector `M` exactly when

\[
M(O)+\partial_{\rm cap}(O)\ge 1
\]

for every protected cap orbit.  Equivalently, its duplicate-slack vector
`s=M-1` must satisfy `s+partial_cap>=0`; a declared terminal compound may
instead carry and repay the negative entries.  The fixed-`z` phasewise atlas has
`partial_cap=0`; the authenticated `h=5` packet has three `-1` entries paid
by three load-two reserves.

This identifies balanced duplicate-cap backup planting plus compatible
boundary histories as the next interface.  Raw central `C14` supply is no
longer the bottleneck.

## 6. Artifact authentication

The hashes embedded in the theorem agree with the files presently in the
repository:

```text
c4dadda7fdfce8092a2a3fdf2b43f2a7c351674f464675b8cd626180c6ac8e65
  scratch/audit_heptagonal_cap_circulation_atlas_20260802.cpp
2b58e7b2de4009198f5a2acf29f7b55ba76af51d5426f056c3b32c655a97f35b
  scratch/k17_upper_decorated_longrun_circuit_20260802/heptagon_atlas_k17_r9.audit.json
46dda4f08412ecd06b58885d50c65e4b7227b7d5952a2acb3184af0c17a92ec3
  scratch/k17_upper_decorated_longrun_circuit_20260802/longrun2754.audit.json
31aa36f6fc4a2be2dfaf03819dd81cbd5df0bd626949f6641a6a78fb81f38eea
  scratch/k17_upper_decorated_longrun_circuit_20260802/longrun2754.trace.tsv
092ffad06b367b8e6c21f8a913fdd6529a1415b28aa69d8d4811a83664473e44
  scratch/k17_upper_decorated_longrun_circuit_20260802/longrun2754.moving_cycles.tsv
```

## 7. Exact scope qualifications

1. The `Theta(k^7)` theorem is cap-exact for the literal phasewise
   fixed-`z` `C14`.  It does not make that family coprime-voltage.
2. The larger twisted-run expression in Section 3 counts prospective
   geodesic socket data.  It does not by itself prove pairwise-distinct free
   quotient owner/facet/cap orbits, cap closure, an exposed incumbent host,
   or an accepting history.
3. The quotient circuit formulas require the quotient representatives to
   form the asserted circuit (in particular, no unintended orbit
   identifications).  Individual stabilizer-freeness alone would not imply
   that condition, but it is part of the phrase "quotient endpoint
   circuit" in the theorem's premise.
4. Only the central-token `O(k^6)` load is unconditional.  The corresponding
   load bound for all history/occurrence resources is explicitly still a
   hypothesis.
5. No source antecedent, deeper-upper completion, lower compiler, or
   all-dimensional host/regeneration theorem follows from this audit.
