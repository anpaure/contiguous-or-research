# Audit of the owner-level `Q_8` carousel and its `CPM/EMSF` boundary

Date: 2026-07-26

Method: independent pure-mathematics audit.

Audited report:
`MATH_ATTACK_K_Q8_OWNER_CAROUSEL_CPM_EMSF_BOUNDARY_20260726.md`.

## Verdict

PASS after the scope corrections incorporated in the audited report.

1. The phase splice

   \[
   R(x)=P^{(i)}(x)\qquad(x\in C_i)
   \]

   is a bijection.  Every shore maps `C_i` bijectively to `C_(i+1)`.
   Independent recomputation gives the first-half directions

   \[
   R(-c),L(-c'-2),R(1-c),L(-c'-1),
   R(2-c),L(-c'),R(3-c),L(1-c'),
   \]

   so every component is an isometric `C_16` and the 256 owners split into
   sixteen cycles.

2. The relative predecessor/successor interface is legitimate for the
   standard carousel because every shore uses the same reference factor.
   It must not be transferred to independently conjugated reference gauges.

3. The sparse carrier has sixteen cycles of length `16(L+1)`, hence exactly
   `256(L+1)` owners.  At depth `q<=L`, the sixteen seam collars are
   disjoint and exactly `16q` starts per macrocycle meet a seam.  Counting
   the lower and upper signs gives the aggregate quarantine bound

   \[
   {G H(H+1)\over L+1}.
   \]

   No extra orientation factor is present.  The condition `L>>H^2` is only
   a sufficient condition for occurrence-by-occurrence quarantine, not a
   lower bound on actual holes.

4. Raw macrocycle isometry holds for every `L`.  A literal inherited
   parity-indexed payload certificate needs even `L` or an explicit phase
   reset.  The carrier is not a full `2^r`-owner packet and therefore is not
   itself a `CPM` option.

5. The transverse matchings have the verified formal properties

   \[
   K(W_0)\cap K(W_1)=\{0,\mathbf1^8\},
   \qquad \langle B_0,B_1,B_2\rangle\text{ primitive}.
   \]

   They do not form a literal owner carousel.  Their natural Hamilton
   bipartitions are

   \[
   \{0,2,4,6\}\quad\text{and}\quad\{0,1,4,6\},
   \]

   and their conjugated reference factors differ.  Equality of an abstract
   port involution therefore does not identify the actual owner ports.

6. The `4L+8` minimal-quartet rail is an exact owner 2-factor, but its
   Hamilton shore has exactly one repeated lower and one repeated upper
   depth-one trace.  For `2<=q<=L`, the two mixed collars contribute exactly
   `q-1` wrong-rank windows in the affected sign.  This proves the claimed
   no-go for the minimal-collar compiler architecture.

7. With `K` owner-disjoint rail carriers in a completion on `W` owners,

   \[
   M_1^-+M_1^+\ge
   \left[2K-{2W\over m+1}\right]_+.
   \]

   Exact depth-one coverage at positive carrier density forces
   `L=Omega(m)`.  The report correctly does not promote this to a `CPM`
   contradiction, because `CPM` permits `o(W)` holes.

8. The bottom-wire theorem is correctly restricted to finite substitutions
   with one literal reference factor, one common phase decoder, and
   kernel-compatible interfaces.  In that category all accumulated labels
   lie in the same phase-kernel normalizer.  A different-kernel gauge
   transition remains outside the theorem and is precisely the open
   primitive.

The report's final implication scope is therefore exact: the standard
owner carousel and sparse carrier are proved; the minimal mixed-collar
escape is closed; a common-gauge, different-kernel, multidepth-decoded
owner transition remains open; and no constant-one conclusion is claimed.

