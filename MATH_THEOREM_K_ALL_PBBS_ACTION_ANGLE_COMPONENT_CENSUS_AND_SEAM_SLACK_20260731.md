# Exact PBBS component census, odd periods, and the seam/slack interface

Date: 2026-07-31

Status: exact PBBS action--angle formula specialized to the critical-density
odd case, with an independent literal replay through `m=10`.  The resulting
component counts and parity theorem are unconditional subject to the standard
exact `sl_2` periodic-BBS action--angle correspondence already used by the
repository's homomesy audit.  The final protected-opening problem is not
solved here.

The permanent arithmetic checker is

```text
scratch/audit_pbbs_action_angle_component_census_20260731.py
scratch/pbbs_action_angle_component_census_20260731.audit.json
```

It enumerates integer partitions and internal symmetries, not Boolean states.

## 1. What is being counted

Put

\[
 n=2m+1,\qquad W=\binom{n}{m}=n\operatorname{Cat}_m.
\]

Let `p` be the canonical cyclic-parenthesis/PBBS permutation of the rank-`m`
subsets.  Write

\[
 c_m=\#\{\text{cycles of }p\}.
\]

The complemented two-extension factor from
`MATH_THEOREM_K_ALL_PBBS_BALANCED_SURJECTIVE_TWO_EXTENSION_20260731.md`
has the same number of components: on a `p`-cycle of length `P`, its
monodromy is `p^2`, and all PBBS periods below are odd.  Thus `gcd(P,2)=1`.

The observed sequence is therefore exactly

\[
 \boxed{c_m=1,2,3,6,12,26,73,146,360,1408,2412,10204,\ldots.}
\]

It is neither a guessed recurrence nor merely a state-space census.  Section
2 gives an exact finite action--angle sum for every `m`.

## 2. The exact action--angle sum

Fix a soliton partition `lambda` of `m`.  Let

\[
 J_1<\cdots<J_g
\]

be its distinct part sizes and let `a_i` be the multiplicity of `J_i`.  Define
the vacancy numbers

\[
 q_i=n-2\sum_{j=1}^g\min(J_i,J_j)a_j.                 \tag{2.1}
\]

At critical density every `q_i` is a positive odd integer, and the last one
is `q_g=1`.

For each vector of internal symmetry orders

\[
 \gamma_i\mid\gcd(a_i,q_i),                            \tag{2.2}
\]

form the integer matrix

\[
 (F_\gamma)_{ij}
 =\frac{\delta_{ij}q_i+2\min(J_i,J_j)a_j}{\gamma_j}.
                                                               \tag{2.3}
\]

The number of exact-symmetry arrays in the `(a,q)` block is

\[
 L_\gamma(a,q)=
 \sum_{\substack{\beta:\ \gamma\mid\beta\mid\gcd(a,q)}}
 \mu(\beta/\gamma)
 \binom{(q+a)/\beta-1}{a/\beta-1}.                    \tag{2.4}
\]

Consequently the number of identical tori of this type is

\[
 M(\lambda,\gamma)
 =\prod_{i=1}^g
   \frac{L_{\gamma_i}(a_i,q_i)}{a_i/\gamma_i}.         \tag{2.5}
\]

On every such torus, PBBS is translation by

\[
 h_\infty=(J_1,\ldots,J_g)^\mathsf T
 \quad\text{in}\quad
 \mathbb Z^g/F_\gamma\mathbb Z^g.                    \tag{2.6}
\]

Let `F_gamma[i]` denote `F_gamma` with column `i` replaced by `h_infinity`.
The exact order of that translation is

\[
 P(\lambda,\gamma)
 =\operatorname{lcm}_{i=1}^g
 \frac{|\det F_\gamma|}
      {\gcd(|\det F_\gamma|,|\det F_\gamma[i]|)}.     \tag{2.7}
\]

The torus has `|det F_gamma|` points, so it contains

\[
 \frac{|\det F_\gamma|}{P(\lambda,\gamma)}            \tag{2.8}
\]

PBBS cycles.  Summing gives the promised exact formula

\[
 \boxed{
 c_m=\sum_{\lambda\vdash m}\ \sum_\gamma
 M(\lambda,\gamma)
 \frac{|\det F_\gamma|}{P(\lambda,\gamma)}.}          \tag{2.9}
\]

This is computationally small compared with the Boolean layer: it ranges
over partitions of `m` and divisor vectors.  For example it computes the
`k=39` count while avoiding all `binom(39,19)` physical states.

At critical density the determinant itself has the useful product form

\[
 \boxed{
 |\det F_\gamma|
 =\frac{n\prod_{i=1}^{g-1}q_i}{\prod_{i=1}^g\gamma_i}.} \tag{2.10}
\]

This follows by taking consecutive row differences in the `min` matrix (or
from the standard `sl_2` period-matrix determinant formula); the last
vacancy is `q_g=1`.  The audit checks (2.10) sector by sector as an additional
integer identity.

### Proof and dependency label

For the `sl_2` periodic BBS, the exact inverse-scattering theorem decomposes
each soliton level set and symmetry sector into the tori
`Z^g/F_gamma Z^g`, with multiplicity (2.5), and linearizes `T_infinity` as
(2.6).  Equations (2.3)--(2.5) are the specialized torus-size/multiplicity
formula, including the Moebius inversion for exact internal symmetry.
Equation (2.7) is Cramer's rule for the least positive `P` with
`P h_infinity in F_gamma Z^g`.  A translation of order `P` partitions a
group of size `|det F_gamma|` into the number of cycles in (2.8).  Summing
over the disjoint action variables and symmetry sectors proves (2.9).

This note does not use the generic-period conjecture from the early Bethe
ansatz paper.  It uses the exact `sl_2` action--angle decomposition, the same
periodic-BBS framework underlying
`PBBS_COORDINATE_HOMOMESY_AUDIT_20260724.md`.

## 3. Every PBBS period is odd

### Theorem 3.1

For `n=2m+1` and weight `m`, every cycle length `P` of the canonical PBBS
permutation is odd.  More precisely,

\[
 P=n\ell\qquad\text{with `ell` odd}.                   \tag{3.1}
\]

#### Proof

All vacancy numbers `q_i` in (2.1) are odd.  Every `gamma_i` in (2.2) is
therefore odd.  Reducing (2.3) modulo two gives

\[
 F_\gamma\equiv I_g\pmod2.                             \tag{3.2}
\]

Thus `det F_gamma` is odd.  Formula (2.7) shows that the translation order
`P` divides an lcm of divisors of this odd determinant, so `P` is odd.

The independently audited site-homomesy theorem gives `n | P`: over a
period, each coordinate is occupied `Pm/n` times, and `gcd(n,m)=1`.
Since `n` is odd, the quotient `ell=P/n` is odd as well. `square`

This proves, rather than extrapolates, the parity seen in every finite
census.  It also sharpens the component statement in the balanced
two-extension theorem: `p^2` has exactly the same cycles as `p`, not merely
at most `Cat_m` of them.

## 4. A factor-three bound with an explicit exceptional term

Let

\[
 a_m=\#\{\text{PBBS cycles of the minimum possible length }n\}.
\]

Equivalently,

\[
 a_m=\frac{|\operatorname{Fix}(p^n)|}{n},             \tag{4.1}
\]

and (2.9) computes it by retaining only the sectors for which
`P(lambda,gamma)=n`.

If the normalized cycle lengths are `ell_1,...,ell_{c_m}`, homomesy gives

\[
 \sum_i\ell_i=\operatorname{Cat}_m.                   \tag{4.2}
\]

By Theorem 3.1 they are odd.  Hence every nonminimal one is at least three,
and

\[
 \operatorname{Cat}_m
 \ge a_m+3(c_m-a_m).
\]

Therefore

\[
 \boxed{c_m\le
 \frac{\operatorname{Cat}_m+2a_m}{3}.}                \tag{4.3}
\]

This is a genuine improvement over the old bare Catalan bound whenever
minimum cycles are sparse.  The audit finds

```text
m          1  2  3  4  5  6  7   8   9    10   19
a_m        1  2  2  3  3  4  5   6   5    10   40
c_m        1  2  3  6 12 26 73 146 360  1408 26478632
```

The data strongly suggest that `a_m` is subexponential, which would make
`c_m <= (1/3+o(1)) Cat_m`.  This note does **not** claim that asymptotic:
a uniform bound on (4.1) remains a clean action--angle subproblem.

### Two infinite minimum-period families

The exceptional term is structured rather than arbitrary.

First, for every divisor `u | m`, take the rectangular soliton partition

\[
 \lambda=(u^{m/u}).                                    \tag{4.4}
\]

It has one vacancy number, equal to one.  Its torus has size `n`, and PBBS
translation is by `u`; because `gcd(n,u)=1`, this is one `n`-cycle.  Hence

\[
 a_m\ge \tau(m).                                      \tag{4.5}
\]

There is a larger family explaining the conspicuous entries at
`m=7,10,13,16,19,...`.  Fix `a,t>=1`, put

\[
 s=2a+1,\quad v=3a+1,\quad
 m=st+v,quad n=s(2t+3),                               \tag{4.6}
\]

and take

\[
 \lambda=(v,s^t).                                     \tag{4.7}
\]

Its two vacancy numbers are `(s,1)`.  For every allowed internal symmetry
`gamma | gcd(s,t)`, direct substitution in (2.3)--(2.7) gives PBBS period
exactly `n`.  Therefore the entire level set is a union of minimum cycles.
The critical-density fermionic count is

\[
 |\mathcal P_{n,\lambda}|
 =n\binom{s+t-1}{t},
\]

so this one sector contributes

\[
 \boxed{\binom{s+t-1}{t}=\binom{t+2a}{2a}}            \tag{4.8}
\]

to `a_m`.

For `a=1`, (4.8) gives `3,6,10,15,21,36,...` from the partitions

\[
 (4,3),\ (4,3,3),\ (4,3,3,3),\ldots,
\]

exactly matching the action--angle census.  Taking `t` comparable with
`a` shows that `a_m` is at least `exp(Omega(sqrt(m)))` on an infinite
subsequence.  Thus a polynomial bound on the exceptional term is false.
The natural sharpened target is

\[
 \boxed{a_m=\exp(O(\sqrt m\log m))\ ?}                 \tag{4.9}
\]

which is compatible with the divisor-vector formula and would still make
the exception negligible against `Cat_m`.  Equation (4.9) is a conjectural
action--angle counting target, not a theorem of this note.

## 5. Exact finite census

The action--angle output is:

| `m` | `k=2m+1` | `Cat_m` | `c_m` | `a_m` | `c_m/Cat_m` |
|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 1 | 1 | 1 | 1.000000 |
| 2 | 5 | 2 | 2 | 2 | 1.000000 |
| 3 | 7 | 5 | 3 | 2 | 0.600000 |
| 4 | 9 | 14 | 6 | 3 | 0.428571 |
| 5 | 11 | 42 | 12 | 3 | 0.285714 |
| 6 | 13 | 132 | 26 | 4 | 0.196970 |
| 7 | 15 | 429 | 73 | 5 | 0.170163 |
| 8 | 17 | 1430 | 146 | 6 | 0.102098 |
| 9 | 19 | 4862 | 360 | 5 | 0.074044 |
| 10 | 21 | 16796 | 1408 | 10 | 0.083829 |
| 11 | 23 | 58786 | 2412 | 4 | 0.041030 |
| 12 | 25 | 208012 | 10204 | 11 | 0.049055 |
| 13 | 27 | 742900 | 31142 | 17 | 0.041920 |
| 14 | 29 | 2674440 | 49452 | 8 | 0.018491 |
| 15 | 31 | 9694845 | 139123 | 6 | 0.014350 |
| 16 | 33 | 35357670 | 848904 | 24 | 0.024009 |
| 17 | 35 | 129644790 | 3021452 | 33 | 0.023306 |
| 18 | 37 | 477638700 | 3250840 | 8 | 0.006806 |
| 19 | 39 | 1767263190 | 26478632 | 40 | 0.014983 |
| 20 | 41 | 6564120420 | 27962514 | 11 | 0.004260 |

For `m<=10`, the script independently constructs every state, applies the
literal cyclic `10` matching, and compares the entire normalized-period
histogram—not only `c_m`.  The two computations agree exactly.

## 6. Staircase slack at the first critical odd dimensions

For odd `k`, put

\[
 r=(k+1)/2,\quad W=\binom{k}{r},\quad
 \Lambda=2^{k-1}-1,
\]

and

\[
 s(k)=d(k)W+\binom{d(k)+1}{2}-\Lambda.                \tag{6.1}
\]

This is the scalar slack in the deadline lower bound at length `B(k)`.
Opening `c_m` cycles into paths and placing them in one chronology uses
`c_m-1` intercomponent seams.  The first critical cases are:

| `k` | `d(k)` | `s(k)` | canonical PBBS `c_m` | `s(k)-(c_m-1)` |
|---:|---:|---:|---:|---:|
| 9  | 2 | 0 | 6 | -5 |
| 21 | 3 | 9579 | 1408 | 8172 |
| 39 | 4 | 815150707 | 26478632 | 788672076 |

This explains one real distinction.  At `k=9`, even the scalar seam bill
does not fit the equality slack; the known optimum necessarily uses a more
singular architecture.  At `k=21` and `k=39`, the canonical PBBS component
bill is already far below the total scalar slack.  The `k=39` comparison is
now a theorem-sized arithmetic calculation, not an extrapolation from small
`m`.

### The important non-implication

The positive last column at `k=21,39` does **not** prove that the PBBS factor
compiles at the bound.  If one edge is cut from each component, let `R` be
the `c_m` deleted lower-`q1` colours and let `Q` be the colours of the
`c_m-1` new seams.  The exact boundary theorem gives

\[
 |R\setminus Q|\le2,                                  \tag{6.2}
\]

not merely `c_m-1 <= s(k)`.  Thus at least `c_m-2` deleted colours must be
recycled by the seam palette, unless a different literal mechanism is used.
The staircase slack lives across all lower rows; at rank `r-1`, the usual
flat compiler has only two outer boundary chains.

The component census therefore narrows the all-`k` task but does not close
it:

* numerically, the canonical PBBS factor is cheap enough after `k=9` in the
  first critical cases;
* combinatorially, one still needs protected factor switches reducing it to
  one or two components, or a global seam system satisfying (6.2);
* residence and the common lower Hall compiler remain independent gates.

## 7. Consequence for the `B(k)+O(1)` program

The raw all-depth support problem is already solved by PBBS.  The exact
formula (2.9) shows that its topology is also explicitly enumerable.  The
remaining theorem is not “prove there are few enough components” in a
scalar sense.  It is one of the following stronger correlation statements:

1. **protected component collapse:** move inside the q1-exact/all-depth
   factor fibre to at most two resident components;
2. **palette-recycling braid:** order/open all `c_m` components so that all
   but at most two cut colours return as seam colours;
3. **non-flat absorption:** replace the two-boundary compiler by a different
   architecture that converts the global scalar slack into rank-`r-1`
   capacity.

The action--angle census is useful in all three lanes: it gives the exact
number and period distribution of the packets that must be collapsed,
recycled, or absorbed, without a Boolean-layer search.

## 8. Scope

Proved here:

* the exact formula (2.9), conditional only on the standard exact `sl_2`
  PBBS action--angle theorem;
* oddness of every PBBS orbit and normalized orbit length;
* equality of the PBBS and contracted-factor component counts;
* the factor-three inequality (4.3);
* exact component counts through `m=20`, with independent full-state replay
  through `m=10`;
* the exact `k=9,21,39` scalar seam/slack comparison.

Not proved:

* a closed scalar recurrence for `c_m`;
* a uniform asymptotic bound on `a_m`;
* protected merging, residence, safe opening, or compiler feasibility;
* `nu(k)=B(k)` or `B(k)+O(1)` from the PBBS factor alone.
