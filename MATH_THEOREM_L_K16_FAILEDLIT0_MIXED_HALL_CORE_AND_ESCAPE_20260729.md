# The detector-zero overlay has a real-linear mixed-Hall obstruction

Date: 2026-07-29  
Status: proved, solver-free Farkas certificate for the guarded core; two
literal degree- and q1-safe certificate-breaking moves exhibited.  No claim
that either move completes residence or the full word.

## 1. Exact verdict

Let

```text
Q = scratch/k16_q1_endpoint_resume1_failedlit0_20260729.json
R = scratch/k16_pbbs_oriented_noaa_softq1_resume1_20260729.json.
```

The target `Q` is a literal spanning physical factor with both q1 palettes
complete, two components of lengths 13 and 12,857, and 2,222 inherited short
runs.  Against the fixed resident factor `R`, put

\[
 A=R\setminus Q,\qquad B=Q\setminus R.
\]

There are 391 common physical edges and

\[
                         |A|=|B|=12479.                       \tag{1.1}
\]

For `f in A`, let `a_f` select the red addition; for `e in B`, let `b_e`
select the blue deletion.  All variables below are merely nonnegative real
numbers.  Thus every contradiction proved below is an LP/Farkas
contradiction and does not use Boolean parity or branching.

The guarded core

```text
scratch/k16_failedlit0_guarded_q1_motif_core_20260729.json
```

contains 8 lower-q1 rows, 13 upper-q1 rows, and one length-two motif row;
all degree equalities are hard.  Only nine degree equalities are needed.  The
21 palette rows and those nine equalities imply the one-row projected
endpoint separator

\[
 \boxed{
 b_{11795}+b_{11796}+b_{11821}\le0.}                          \tag{1.2}
\]

The motif row requires the same left side to be at least one.  Hence the
guarded subsystem, the LP relaxation of the full overlay, and therefore the
binary full overlay are all infeasible.  This independently proves the
fixed-overlay `INFEASIBLE` conclusion; the stored CP-SAT status is no longer
the proof.

## 2. Frozen provenance

```text
Q endpoint
  SHA-256 17bd05a0bb0da228e580d65bdec27ce04589072baecb8575e0623fc4ea4343b8

guarded core
  SHA-256 2f8031fff879faf42b80a169aee2f0a0f5a2484987c5fe625c20fc5bf945c238

canonical physical R/Q endpoint reconstruction
  scratch/k16_resident_resume1_q1_canonical_physical_endpoints_20260729.json
  SHA-256 fbd182aff3117581c7cf5216e33a30db3309da23c8d570275114e5a6165985e9

full-overlay result
  SHA-256 4fd0b2d2a15326b9ecfa5c1b939f835814ca2d5303268268ad1ea639e33fdcf2

serialized full-overlay model
  SHA-256 30cc26ba1586c259407ad5286026707960f6fda5e131d6e16313a32759d9852b

resident endpoint
  SHA-256 d28491b708d5a83e8abcde20fda8ad523cd58f9c662f46ae2d9c2507ba73e951

catalogue digest
  e5ffa02199834c476f45b314b2eacfbaa1866a74895cc0aa4e12744c8d157ff3
```

The core has one blue provider in every q1 row and at most one red provider.
Every source load is one.  Consequently each row is exactly `b_i<=a_j`, or
`b_i<=0` when the red provider is absent.

## 3. Complete physical provider table

The rows reconstructed from the two physical shores are:

| row | blue removal | red replacement |
|---|---|---|
| `L18526` | `b4006=(18558,26718)` | none |
| `L47652` | `b10117=(47660,47780)` | `a10025=(47908,64036)` |
| `L51230` | `b10718=(51358,59422)` | `a10650=(51262,59422)` |
| `L57614` | `b11849=(58126,58638)` | none |
| `L57870` | `b11795=(57902,57998)` | `a11797=(57871,59918)` |
| `L57894` | `b11827=(58022,59942)` | `a11806=(57902,61990)` |
| `L59406` | `b12127=(59918,63502)` | `a12057=(59422,60430)` |
| `L61988` | `b12319=(61990,62052)` | `a12345=(61989,64036)` |
| `U27742` | `b5891=(26718,27678)` | none |
| `U47645` | `b9749=(45597,47644)` | none |
| `U47676` | `b10030=(47164,47660)` | `a9991=(47644,47668)` |
| `U47772` | `b3328=(15004,47644)` | none |
| `U58254` | `b11821=(57998,58250)` | `a10338=(50062,58126)` |
| `U59486` | `b12037=(59422,59478)` | `a5686=(26718,59478)` |
| `U59950` | `b12126=(59918,59948)` | `a10798=(51758,59942)` |
| `U61998` | `b11796=(57902,61994)` | `a11806=(57902,61990)` |
| `U62118` | `b9796=(45734,61990)` | none |
| `U62222` | `b9815=(45838,58126)` | `a11867=(58126,62214)` |
| `U64038` | `b11579=(55846,59942)` | none |
| `U64044` | `b12455=(64036,64040)` | `a9993=(47660,61996)` |
| `U65060` | `b12456=(64036,65028)` | none |

The motif is

\[
 M=\{b_{11795},b_{11796},b_{11821}\},                        \tag{3.1}
\]

with physical closure

\[
 (57902,57998),\quad(57902,61994),\quad(57998,58250),         \tag{3.2}
\]

and requires

\[
                  b_{11795}+b_{11796}+b_{11821}\ge1.         \tag{3.3}
\]

## 4. Nine-socket proof over the reals

All omitted variables in the following equalities are nonnegative.

### 4.1 Right socket forces `a11806=0`

The no-provider rows give

\[
 b_{3328}=b_{9749}=b_{9796}=b_{12456}=0.                     \tag{4.1}
\]

At endpoint 47644, degree balance is

\[
 a_{8352}+a_{9991}=b_{3328}+b_{9749}=0,
\]

so `a9991=0`, and `b10030<=a9991` gives `b10030=0`.

At 47660,

\[
 a_{9960}+a_{9993}=b_{10030}+b_{10117},
\]

and `b10117<=a10025`; hence `a9993<=a10025`.

At 64036,

\[
 a_{10025}+a_{12345}=b_{12455}+b_{12456},
\]

while `b12455<=a9993`.  Therefore

\[
 a_{10025}+a_{12345}\le a_{9993}\le a_{10025},
\]

so `a12345=0` and then `b12319=0`.

Finally, at 61990,

\[
 a_{9710}+a_{11806}=b_{9796}+b_{12319}=0.                   \tag{4.2}
\]

Thus `a11806=0`; the two mixed palette links give

\[
                         b_{11796}=b_{11827}=0.               \tag{4.3}
\]

### 4.2 Left socket forces `b11795=0`

The two anchors at 26718 satisfy

\[
 b_{4006}=b_{5891}=0.
\]

Degree balance there gives `a5686=0`, hence `b12037=0`.  At
59422,

\[
 a_{10650}+a_{12057}=b_{10718}+b_{12037}le a_{10650},
\]

so `a12057=0` and `b12127=0`.

At 59942, using (4.3),

\[
 a_{10798}+a_{12168}=b_{11579}+b_{11827}=0,
\]

because `b11579=0`.  Thus `a10798=0` and `b12126=0`.

At 59918,

\[
 a_{10793}+a_{11797}=b_{12126}+b_{12127}=0.
\]

Therefore `a11797=0`, and the `L57870` row gives

\[
                             b_{11795}=0.                     \tag{4.4}
\]

### 4.3 Third socket forces `b11821=0`

At 58126,

\[
 a_{10338}+a_{11867}=b_{9815}+b_{11849}\le a_{11867},        \tag{4.5}
\]

using `b9815<=a11867` and the no-provider row `b11849=0`.
Hence `a10338=0`, and the `U58254` row gives

\[
                             b_{11821}=0.                     \tag{4.6}
\]

Equations (4.3), (4.4), and (4.6) contradict (3.3).

## 5. Collapsed integer Farkas certificate

The separator is already a pure rank-two endpoint-capacity Hall row.  Give
weight two to the eight colours

\[
 \mathcal T=\{L47652,L61988,U47645,U47676,U47772,
               U62118,U64044,U65060\},                       \tag{5.1}
\]

weight one to the other thirteen core colours, and zero to all other q1
colours.  Give endpoint weight two at

\[
                  47644,47660,61990,64036,                   \tag{5.2}
\]

weight one at

\[
                  26718,59422,59942,59918,58126,             \tag{5.3}
\]

and zero elsewhere.  For every one of the 12,479 resident-only red seams
`f=uv`, exact replay gives

\[
       \lambda_{\ell(f)}+\lambda_{u(f)}\le w_u+w_v.           \tag{5.4}
\]

Exactly twelve red columns have nonzero resource price, and all twelve are
tight.  The double-colour seam `a11806=(57902,61990)` carries `L57894` and
`U61998`, so its price is `1+1=2=w_61990`.

Expanding the globally valid mixed-Hall row in the 12,479 blue deletion
variables cancels every coefficient except

\[
 b_{11795},\quad b_{11796},\quad b_{11821},                   \tag{5.5}
\]

each with coefficient one.  This gives (1.2) directly.  Dividing every
weight by two gives the bounded normalization `0<=lambda<=1`; the normalized
violation margin against the motif is `1/2`.

The same row has the following transparent socket expansion.

The proof above is equivalently the single incidence-counted inequality

\[
\begin{aligned}
 b_{11795}+b_{11796}+b_{11821}
 \le{}&b_{11579}+b_{4006}+b_{5891}+b_{11849}\\
 &+2(b_{9796}+b_{3328}+b_{9749}+b_{12456}).                  \tag{5.6}
\end{aligned}
\]

The eight right-side variables are precisely the no-red-provider q1 rows,
so the right side is zero.  This proves (1.2).

For a literal row-sum replay, use:

- coefficient one on the six non-anchor left-socket q1 links and its four
  degree equalities at `26718,59422,59942,59918`;
- coefficient one on the two non-anchor third-socket q1 links and the degree
  equality at `58126`;
- coefficient one on `U61998`, namely `b11796<=a11806`;
- coefficient two on the four non-anchor right-socket q1 links and on the four
  degree equalities at `47644,47660,64036,61990`;
- coefficient one on the nonnegativity rows for
  `a5685,a12168,a10793`;
- coefficient two on the nonnegativity rows for
  `a8352,a9960,a9710`.

Every non-motif variable cancels, leaving (5.6).  Add the motif row

\[
          -b_{11795}-b_{11796}-b_{11821}\le-1
\]

with coefficient one.  Also add the no-provider rows for
`b11579,b4006,b5891,b11849` with coefficient one and those for
`b9796,b3328,b9749,b12456` with coefficient two.  The result is the integer
Farkas contradiction

\[
                              0\le-1.                         \tag{5.7}
\]

This proves **LP infeasibility**, not merely integral infeasibility.  The
guarded artifact reports that every 21-of-22 guarded-row deletion is
integer-feasible, but it stores no primal witnesses.  Thus its guarded
support minimality remains solver-backed; (5.7), in contrast, is entirely
solver-free.

## 6. Polynomial mixed-Hall separator for any physical overlay

The preceding certificate is one sparse instance of the general polynomial
oracle.  For motif weights `alpha_M>=0`, lower/upper q1 prices
`lambda_c>=0`, free endpoint potentials `pi_v`, and nonnegative unit-bound
slacks `u_g`, require for every red edge `f=xy`

\[
 \pi_x+\pi_y-\lambda_{\ell(f)}-\lambda_{u(f)}+u_f\ge0,       \tag{6.1}
\]

and for every blue edge `e=xy`

\[
 -\pi_x-\pi_y+\lambda_{\ell(e)}+\lambda_{u(e)}+u_e
 \ge\sum_{M:e\in C_M}\alpha_M.                             \tag{6.2}
\]

Put `s_c=mu_Q(c)-1`.  A strict inequality

\[
 \boxed{
 \sum_M\alpha_M>
 \sum_cs_c\lambda_c+
 \sum_{g\in A\cup B}u_g}                                   \tag{6.3}
\]

is an exact rational Farkas certificate for fractional infeasibility of the
motif-plus-degree-plus-both-q1 overlay.  Conversely, if that fractional
overlay is infeasible, such weights exist.  This is one explicit linear
program over the stored physical catalogue, not an enumeration of overlay
cuts.

For the whole detector-zero endpoint its dimensions are:

| object | count |
|---|---:|
| motif weights | 2,222 |
| lower q1 prices | 11,440 |
| upper q1 prices | 11,440 |
| active endpoint equalities | 12,867 |
| red unit slacks | 12,479 |
| blue unit slacks | 12,479 |

The 22-row certificate collapses this to one motif weight, 21 nonzero q1
prices, nine nonzero endpoint sockets, and six nonnegativity payments, with
integer weights only `1` and `2`.  A verifier need not import CP-SAT or an LP
solver: it rebuilds the two shores, checks (5.6), and checks the positive
unit margin in (5.7).

## 7. Exact escape operations

### 7.1 A single catalogue edge that breaks the proof

The sparsest violation of the dual column condition is

\[
                         e_0=(11358,19550).                   \tag{7.1}
\]

It is a physical Johnson edge with upper colour 27742 and is absent from
both `Q` and `R`.  Both endpoints have dual price zero, whereas
`lambda_(U27742)=1`.  Hence

\[
 \lambda_{\ell(e_0)}+\lambda_{u(e_0)}=1
 >w_{11358}+w_{19550}=0,                                    \tag{7.2}
\]

so admitting this one red column invalidates (5.4) and changes the protected
`U27742` row from `b5891<=0` to `b5891<=a_(e_0)`.

There is also a lower-colour escape with known quotient identity.  The
physical Johnson edge

\[
                         f=(18527,18558)                      \tag{7.3}
\]

has lower colour 18526 and upper colour 18559.  It is absent from both `Q`
and `R`.  In the quotient catalogue it is loopless edge ID 3302, between
quotient nodes 63 and 118, and is off the frozen r147 source.

Adding `f` to the allowed red catalogue changes the first anchor from

\[
                    b_{4006}\le0
 \quad\text{to}\quad b_{4006}\le a_f.                        \tag{7.4}
\]

The collapsed proof then has an unpaid `a_f` term and no longer yields
(5.6).  This is an exact certificate escape, but not yet a balanced factor
move: incidence at 18527 and 26718 still has to be routed.

### 7.2 A literal q1-perfect radius-two escape

A fully balanced and q1-complete way to destroy a zero anchor is the
following two-edge trade on `Q`:

\[
\begin{array}{ll}
\text{delete}&(25662,27678),\ (25694,25722),\\
\text{add}&(25662,25722),\ (25694,27678).                    \tag{7.5}
\end{array}
\]

Both added edges are outside the current `Q`.  The four endpoints occur once
on each shore, so degree two is preserved.  The exact q1 load changes are

\[
\begin{array}{c|ccc}
\text{lower}&25630:1\to1&25658:1\to2&25690:2\to1\\
\text{upper}&25726:1\to1&27710:2\to1&27742:1\to2.
\end{array}                                                   \tag{7.6}
\]

Hence no lower or upper q1 hole is created.  The new edge
`(25694,27678)` supplies a second source occurrence of the formerly
no-red-provider upper colour 27742.  Therefore the anchor row
`b5891<=0` used in (5.6) disappears after rebuilding the overlay, and the
certificate cannot transport.

A second literal option is

\[
\begin{array}{ll}
\text{delete}&(57487,57615),\ (57550,57742),\\
\text{add}&(57487,57550),\ (57615,57742),                    \tag{7.7}
\end{array}
\]

with loads

\[
\begin{array}{c|ccc}
\text{lower}&57359:3\to2&57486:1\to1&57614:1\to2\\
\text{upper}&57551:1\to2&57743:1\to1&57806:2\to1.
\end{array}                                                   \tag{7.8}
\]

This removes the `b11849<=0` anchor instead.  Both moves preserve only the
currently asserted middle degree and q1 completeness.  Residence, new motif
closures, topology, failed-literal banks, and the rebuilt full overlay must
still be audited.  They are certificate escapes, not claimed solutions.

## 8. Sharp boundary

Proved:

- the 22 guarded rows contain a real-linear, integer-weight Farkas
  contradiction;
- only nine of the 12,867 degree rows are needed;
- the weights (5.1)--(5.5) expand exactly to the projected separator (1.2);
- the full fixed `Q`--`R` overlay is therefore impossible independently of
  CP-SAT;
- (6.1)--(6.3) give the polynomial exact fractional separator for any future
  physical overlay; and
- (7.5) and (7.7) are literal degree/q1-safe moves that invalidate this
  particular certificate.

Not proved:

- solver-free inclusion-minimality of the 22 guarded rows;
- feasibility of either escaped overlay;
- residence or all-depth coverage after either move; or
- any conclusion outside the fixed physical endpoint architecture.

## 9. Permanent solver-free replay

```text
scratch/audit_k16_failedlit0_mixed_hall_farkas_20260729.py
  SHA-256 3e6b0d27d369a2962c886230822e355c99e0592b2d5c9315039b61d16524b4b4

scratch/k16_failedlit0_mixed_hall_farkas_20260729.audit.json
  SHA-256 895323f21d529435957f0bdefe6121129e3b89a234851720dacdd4dab471c9f6
```

The verifier uses only the Python standard library.  It rebuilds all 12,479
red and blue shore edges, checks the complete 21-row provider table, checks
all 12,479 mixed-Hall red-column inequalities, reconstructs the three-term
blue expansion, sums the integer Farkas proof, and audits both q1-perfect
escape trades.  Its status is

```text
PASS_SOLVER_FREE_LP_INFEASIBILITY
```

All reconstruction and auditing for this note used small JSON/text passes and
exact hand algebra.  No local SAT, LP, C++, sustained Python, or process
management was used.
