# CC audit: all 1,024 C106 signatures escape the S662 lattice at radius at least two

Date: 2026-07-30  
Status: **proved, solver-free, for the frozen source-relative seam catalogue**

## 0. Verdict and scope

Let \(S\) be the 662-seam support of the exact `SSSSS` fractional C106
point.  None of the authenticated \(4^5=1024\) C106 lock signatures admits
an integral balanced circulation wholly on \(S\).  This remains true even if
support coefficients are allowed to be signed and port capacity is omitted.

There is moreover one exact cyclic congruence, common to all 1,024
signatures, whose corrected coefficient is zero on every seam of \(S\).  An
exhaustive raw-ledger replay proves that no single outside seam of allowable
slack can supply the required signature residue.  Consequently:

> **All-signature radius-two escape theorem.** Every binary balanced C106
> service solution in the frozen catalogue uses at least two seam IDs outside
> \(S\), independently of its lock signature.

This is an escape theorem, not a C107 lower bound.  In general, a C106
solution using two or more outside seams is not excluded.  Separation, q1, reverse-edge,
residence, survivor, deeper-shadow and literal-word rows are not used.  No
unrestricted-K16 claim is made.

For the all-slack signature `SSSSS`, the radius-two packet has also been
closed exactly.  The combined parity/mod-457 portal interface leaves 208
outside-seam pairs, and complete signed-lattice membership rejects all 208.
Thus an `SSSSS` solution must use at least three seams outside `S`.  This
sharpening is support-relative and still does not exclude `SSSSS` globally.

## 1. Frozen lineage

The deterministic audit uses:

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

scratch/k16_direct_cycle_dual_exact_20260730.audit.json
SHA-256 29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d

scratch/k16_floor106_s5_pdlp_20260730.json
SHA-256 e934799a0f881163e621236a530b4127253a4b032653eeb21876f40e81fad00a

scratch/k16_floor106_authenticated_frozen_20260730/MANIFEST.json
SHA-256 37c39639910a3ba02896e2fb9163c70c82e63e779e9213c10e4075b41100a05d
```

The checker and result are:

```text
scratch/audit_cc_k16_c106_all1024_support662_lattice_escape_20260730.py
SHA-256 cefd0a3be53bb25703444d06122a5ea06946be70d44647edc8f71bdc875b769f

scratch/cc_k16_c106_all1024_support662_lattice_escape_20260730.audit.json
SHA-256 d2470bbb431bb9a636e7bbc6f499661dd16b0c631d57281c1dff9eae447fe6b4
payload 44ed046c10ccdd79d766b2396d78c8548923e95616eb28d0a0b9e600501b46dc
```

A fresh H100 replay to a distinct path was byte-identical to the displayed
audit JSON:

```text
scratch/root_k16_c106_all1024_support662_lattice_escape_h100_v2_20260730.audit.json
SHA-256 d2470bbb431bb9a636e7bbc6f499661dd16b0c631d57281c1dff9eae447fe6b4

scratch/all1024_escape_replay_v2.stdout.txt
SHA-256 363b6d427b5f6f5705b5d22164582d2a571b581fed2cb14dd214d64da7271837

scratch/all1024_escape_replay_v2.resource.txt
SHA-256 e56f301f2da26199838e1161d7231fee63e7f978e045d2199443125d0f07acd8
```

That run used one CPU, a 2 GiB address-space cap, 5.88 seconds wall time and
120,180 KiB maximum RSS.  The checker is self-contained apart from the four
hash-pinned data inputs; it does not import the contemporaneously evolving
radius-one checker.

## 2. The exact integral support lattice

For a seam \(e\), define its 94-coordinate feature column

\[
 \chi(e)=\bigl((1_{t\in H(e)})_{t\in\mathcal T},1\bigr),              \tag{2.1}
\]

where the last coordinate records selected mass.  The support graph has 662
edges, 571 vertices and three weak components, hence circulation dimension

\[
                         662-571+3=94.                                \tag{2.2}
\]

Choose the deterministic breadth-first spanning forest used by the audit.
For every nonforest chord \(c_j:u\to v\), let \(\gamma_j\) be \(c_j\) plus the
signed forest path from \(v\) to \(u\).  The 94 vectors \(\gamma_j\) form a
\(\mathbb Z\)-basis of the full integral circulation lattice on \(S\): after
subtracting \(x_{c_j}\gamma_j\) for all chords, an integral circulation is
supported on a forest and must vanish.

Form the integer matrix

\[
             A_{ij}=\chi_i(\gamma_j),\qquad A\in\mathbb Z^{94\times94}. \tag{2.3}
\]

Rows are the 93 targets in increasing numerical order followed by count.
The audit hashes the full matrix as

```text
d86d2eb1d71afbfb5663af2710118e7a3caf877999a3e619ad194f68d619d032
```

and fraction-free Bareiss elimination gives

\[
 \det A=-7,452,780,650,347,681,984,140,640\ne0.                \tag{2.4}
\]

For a lock word \(\alpha\in\{S,0,1,2\}^5\), let
\(d_\alpha\in\mathbb Z^{94}\)
have target coordinate one, increased to two at each digit-selected repeat,
and last coordinate 106.  An integral support circulation with signature
\(\alpha\) would give an integer vector \(z\) satisfying

\[
                              Az=d_\alpha.                             \tag{2.5}
\]

Thus membership of \(d_\alpha\) in the exact lattice \(A\mathbb Z^{94}\) is
a necessary condition even before nonnegativity or capacity.

## 3. Complete 1,024-signature lattice classification

The ranks are

\[
 \operatorname{rank}_{\mathbb F_2}A=90,
 \qquad
 \operatorname{rank}_{\mathbb F_5}A=93.                              \tag{3.1}
\]

The audit constructs four exact mod-two left annihilators and one exact
mod-five left annihilator.  Applying them to all 1,024 right-hand sides gives:

| slack \(R\) | signatures | pass mod 2 | pass mod 5 | pass both |
|---:|---:|---:|---:|---:|
| 0 | 243 | 16 | 39 | 2 |
| 1 | 405 | 22 | 77 | 2 |
| 2 | 270 | 18 | 69 | 5 |
| 3 | 90 | 8 | 20 | 2 |
| 4 | 15 | 0 | 4 | 0 |
| 5 | 1 | 0 | 1 | 0 |

The union of these congruences rejects 1,013 signatures.  Exactly eleven
survive both small-prime tests:

```text
SS12S  S1S22  S2221  0SS2S  01020  01122
1110S  112SS  2S0S0  2S1S2  2S21S
```

Here a digit gives the zero-based target position in its frozen lock triple.
Exact rational Gauss-Jordan elimination then solves (2.5) for those eleven.
Their cycle-coordinate denominator LCMs are:

```text
D  = 46579879064673012400879:
     SS12S, 0SS2S, 01020, 01122, 112SS, 2S21S

2D = 93159758129346024801758:
     S1S22, S2221, 1110S, 2S0S0, 2S1S2
```

Every denominator is greater than one.  Hence none of the eleven has an
integer cycle-coordinate vector.  Together with the modular rejection of the
other 1,013, this proves that the number of integral support-compatible lock
signatures is exactly zero.

The audit stores a SHA-256 digest of every 94-coordinate exact solution and
replays \(Az=d_\alpha\) entry by entry.  Several coordinates are also
negative, but the stronger point here is that integrality already fails.

## 4. One universal global escape congruence

The support-lattice calculation lifts to a full-catalogue cut, rather than
remaining merely a support-local rank test.

Let \(\lambda^T\) be row zero of \(A^{-1}\).  After clearing and primitively
normalizing denominators, the audit obtains an integer vector
\(a\in\mathbb Z^{94}\) modulo

\[
                    M=232,899,395,323,365,062,004,395,          \tag{4.1}
\]

with

\[
                         a^T A\equiv0\pmod M.                         \tag{4.2}
\]

The exact coefficient vector is embedded in the audit JSON; its digest is

```text
37630781cb2949be6bb86a930987cf3bae602f0ed3d193217ff753181d42456b
```

For any catalogue seam define

\[
 L(e)=a_{\rm count}+\sum_{t\in H(e)}a_t\pmod M.                       \tag{4.3}
\]

Equation (4.2) says that \(L\) has zero sum on every integral support cycle.
The audit therefore constructs a vertex potential \(p\) on each of the three
support components such that

\[
                         L(e)=p(v)-p(u)\pmod M                         \tag{4.4}
\]

for every \(e:u\to v\) in \(S\).  Extend \(p\) by zero off the 571 support
vertices and set

\[
              \rho(e)=L(e)-p(v)+p(u)\pmod M.                          \tag{4.5}
\]

Then \(\rho(e)=0\) on all 662 support seams.  For every full-catalogue
integral balanced circulation with signature \(\alpha\), endpoint balance
cancels the potential and gives the exact congruence

\[
                 \boxed{\sum_e\rho(e)x_e\equiv
                    r_\alpha:=a^Td_\alpha\pmod M}.                    \tag{4.6}
\]

The support-potential and all-signature residue maps have hashes

```text
support gauge     8e24bc1e68bc4f963adf630fd929333902e66bced03d2ce8cffe1ad070dba75c
signature residue aa7f7bbabd72b63be443a13f280bd2be83c741ec720f548cafc944a13d2f0263
```

Crucially,

\[
                             r_\alpha\ne0\pmod M                      \tag{4.7}
\]

for every one of the 1,024 authenticated signatures.  Thus (4.6) is a
signature-independent cut template: only its known right-hand side changes
with the five lock digits.  It forces every C106 solution to leave \(S\).

### 4.1 Radius one is impossible for every signature

Suppose a binary solution uses exactly one outside seam \(e\).  The remaining
support flow can balance it only if both endpoints of \(e\) lie in the same
support component.  Nonnegative direct slack also forces
\(s(e)\le R(\alpha)\).  Finally (4.6) forces

\[
                              \rho(e)=r_\alpha.                        \tag{4.8}
\]

The checker evaluates (4.8) on all 211,604 raw seam records for every
signature.  The number of qualifying seams is zero in every slack layer:

| \(R\) | signatures | signatures with one-seam candidate | total candidate pairs |
|---:|---:|---:|---:|
| 0 | 243 | 0 | 0 |
| 1 | 405 | 0 | 0 |
| 2 | 270 | 0 | 0 |
| 3 | 90 | 0 | 0 |
| 4 | 15 | 0 | 0 |
| 5 | 1 | 0 | 0 |

This proves the all-signature radius-two escape theorem stated in Section 0.
It strictly extends the earlier 33-target `SSSSS` parity escape cut: the new
cut covers every lock word and its exact residue eliminates all one-column
escapes without invoking a SAT/CP solver.

## 5. Proof-guided exact construction after the escape theorem

The same lattice gives a finite constructive master with no ambiguity about
cycle closure.

Fix a signature \(\alpha\) and a proposed binary outside packet
\(F\subseteq E\setminus S\).  Put

\[
 b_F(v)=\operatorname{out}_F(v)-\operatorname{in}_F(v).               \tag{5.1}
\]

For \(F\) to be completable using support seams, it is necessary and
sufficient at the balance level that:

1. \(b_F(v)=0\) for every vertex outside the support vertex set;
2. \(\sum_{v\in W}b_F(v)=0\) for each of the three support components \(W\).

When these hold, the frozen spanning forest has a unique signed integral flow
\(q_F\) with divergence \(-b_F\).  Every support completion is uniquely

\[
                         x_S=q_F+Cz,                                  \tag{5.2}
\]

where the columns of \(C\) are the 94 fundamental cycles.  Target service and
count reduce to the single square system

\[
             Az=d_\alpha-\chi(F)-\chi(q_F).                           \tag{5.3}
\]

Since \(A\) is invertible, (5.3) has one exact rational candidate.  Therefore
\(F\) extends to a reduced C106 witness if and only if:

* the candidate \(z\) is integral;
* \(q_F+Cz\in\{0,1\}^{S}\);
* the union with \(F\) obeys outgoing port capacity one.

Balance then gives incoming capacity, and the direct identity makes the
declared slack row automatic from exact service and count.  This is an exact
necessary-and-sufficient test for the face whose outside set is \(F\), not a
heuristic rounding rule.

The all-signature construction search should therefore begin at \(|F|=2\),
never at radius zero or one.  For `SSSSS`, Section 6 raises the starting radius
to three.  Candidate packets can be indexed before any exact solve by

\[
 \sum_{e\in F}s(e)\le R(\alpha),\qquad
 \sum_{e\in F}\rho(e)\equiv r_\alpha\pmod M,                          \tag{5.4}
\]

together with the two boundary conditions above.  For two seams this is a
residue-join/portal-pair enumeration; (5.3) then supplies a deterministic
proof-producing accept/reject calculation.  Any accepted packet must still
be replayed from raw seam IDs before adding the physical rows omitted here.

## 6. SSSSS radius-two packet theorem

The simple 33-target parity row and the mod-457 support separator can be
combined by the Chinese remainder theorem into a residue $q(e)\pmod{914}$.
Every support seam has $q(e)=0$, while the exact `SSSSS` right-hand side has
total residue one.

Contract the three connected components of `S`, leaving every other port as
its own singleton quotient class.  Among the 210,763 outside seams of direct
slack at most five, two selected seams can have a support-balanced boundary
only in one of two ways:

1. both quotient arcs are loops; or
2. they are opposite arcs between the same two distinct quotient classes.

Imposing distinct raw tails and heads, total slack at most five, and
$q(e)+q(f)=1\pmod{914}$ leaves exactly 208 unordered pairs:

```text
204 quotient-loop pairs
  4 directed quotient two-cycles
pair-set SHA-256 55d24bcc086ceea1941759958cbac79b8212a272e7ee2a34f1cf51b67cd696a7
```

An independent explicit replay obtains the same pair set.  For each pair
$F=\{e,f\}$, correct its boundary with the fixed support forest as in
(5.2), and let $b_F$ be the remaining 93-service-plus-count vector in
(5.3).  Complete membership in $A\mathbb Z^{94}$ is tested at every prime
power dividing the determinant:

\[
 32,\ 5,\ 457,\ 63079,\ 33852407,\ 47731799.
\]

The first-failure census is

```text
mod 32:    198 pairs
mod 5:       8 pairs
mod 63079:   2 pairs
survivors:   0 pairs
```

These congruences test the full signed support lattice, already relaxing
support nonnegativity, support binarity and support port capacity.  Hence no
two-outside-seam `SSSSS` packet can complete on `S`.  Together with the
support-only and radius-one results:

> **SSSSS radius-three escape theorem.** Every binary balanced exact-service
> `SSSSS` solution uses at least three seams outside the frozen support `S`.

The exact artifacts are:

```text
scratch/build_ad_k16_c106_sssss_crt914_radius2_interface_20260730.py
SHA-256 a7460f69f305d3a363f7b3d557f615999dde994979d6e51847f1c0b3898093c0

scratch/ad_k16_c106_sssss_crt914_radius2_v2_20260730.audit.json
SHA-256 9dce75365e9ce98cd16f8096ea206803e8f83326919cc7b4e01e41ebcc62f4ff
payload adb22c4a988aa28b21545a5fed645ebe7ea43a740878dffa46e14820d3f417b1

scratch/ad_k16_c106_sssss_crt914_outside_slack5_v2_20260730.tsv
SHA-256 da46d259648bf01db3b678cfafca857a49cac79c47f05e5abb3de90b457bb69e

scratch/ad_k16_c106_sssss_crt914_radius2_pairs_replay_20260730.audit.json
SHA-256 bd33a7a86c27aa45cbc6d9178165e90b065fb633309fa75478a8707820a3c26c

scratch/provider56_audit_k16_c106_sssss_crt914_radius2_lattice_20260730.py
SHA-256 e1de952e5094b3b54b2fee261b8d0a334652fc4c71cf811c9066cd5696b10fc4

scratch/provider56_k16_c106_sssss_crt914_radius2_lattice_20260730.audit.json
SHA-256 a84b4e07f8002d4f723c9ff476977f82ccd9568a575551e03b4f76a1584643f1
payload b36c2c0d658b2e0bc42ee515a085b3e5b927caa741de74fc25db643637b1787b

scratch/provider56_k16_c106_sssss_crt914_radius2_lattice_20260730.resource.txt
SHA-256 0bbfd1006d7bbca08fc90def60b2c94d5646248a297c59572827f8440eab933a
```

The final audit used one H100 CPU, a 2 GiB address-space cap, 3.93 seconds
wall time and 241,236 KiB maximum RSS.

### 6.1 Pure GF(2) does not survive the first portal expansion

An exact follow-up census tested the `SSSSS` parity system consisting of
endpoint balance, exact-once target service, count 106 and slack five.  On
the 662 support seams its column rank is 658 and adjoining the right-hand
side raises the rank to 659, recovering a parity obstruction.  But the
obstruction disappears as soon as the allowed seam set is enlarged:

| seam set | eligible seams | column rank | augmented rank | GF(2) feasible |
|---|---:|---:|---:|---|
| `S` | 662 | 658 | 659 | no |
| endpoints both in the 571 support vertices | 1,317 | 664 | 664 | yes |
| at least one endpoint in the support vertices | 16,481 | 8,170 | 8,170 | yes |

Thus neither the induced nor incident one-hop expansion admits another pure
GF(2) separation of this complete parity system.  The radius-three theorem
above genuinely uses the two-column portal topology and the integer support
lattice; it cannot be replaced by a parity-only expansion argument.  This
positive parity feasibility supplies no nonnegative, capacity-one or
physical circulation.

```text
scratch/explore_ad_k16_c106_sssss_incident_gf2_20260730.py
SHA-256 665963f0a4be2a80b9624eea550869a79c28e6f72889ba648dc97a0650718536

scratch/threadB_k16_c106_sssss_incident_gf2_20260730.audit.json
SHA-256 46fc83471f44c368ed9a352c0042c40f32d6f58b3a86fe62db08162baf509b25
payload d225fcfc7d038c530693aa4c717350c6bb481545a1e14be51a01c6abc96bc38b

scratch/threadB_k16_c106_sssss_incident_gf2_20260730.resource.txt
SHA-256 62e75aab4f3e85ddaacf389f97a6ad9749a7652cf5bb9ce6573154764d9ef6ef
```

The capped H100 run used one CPU, a 2 GiB address-space cap, 3.34 seconds
wall time and 741,120 KiB maximum RSS.

## 7. Exact boundary

Proved:

1. zero of the 1,024 C106 signatures lies in the integral circulation lattice
   of the frozen S662 support;
2. a single exact modulo-\(M\) cohomology cut forces every signature to use an
   outside seam;
3. no binary signature can use exactly one outside seam, so every reduced
   C106 witness has escape radius at least two;
4. the `SSSSS` signature has escape radius at least three;
5. equations (5.1)--(5.3) give an exact finite completion test for every
   proposed outside packet.

Not proved:

* infeasibility or feasibility after two or more outside seams for the other
  1,023 signatures, or after three or more outside seams for `SSSSS`;
* a capacity-one C106 circulation in the full catalogue;
* any physical separated-port or literal-word C106 construction;
* a source-relative lower bound of 107.
