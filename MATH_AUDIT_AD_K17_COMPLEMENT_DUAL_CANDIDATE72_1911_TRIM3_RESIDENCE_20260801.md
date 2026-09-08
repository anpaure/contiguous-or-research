# Exact complement-dual splice chronology, residence, and trim3 audit for K17

Date: 2026-08-01  
Lane: AD  
Status: **PASS, scoped negative candidate audit**

## 1. Scope

This note integrates the authenticated complement-dual seed

```text
/dev/shm/root_k17_complement_dual_deep17931_20260801/best.tsv
SHA256 a3f9eac037ae66a460349b12d578a31222afe1a7d168da641e77967a44ddbab3
```

and the two new full-factor candidates in

```text
/dev/shm/root_k17_complement_dual_deep17931_20260801/
  dual_splice_dev5_20260801/
```

with the exact source-3-trimmed all-width upper-opening oracle.  The result is
not a K17 construction:

- candidate 72 has no single factor chronology and fails residence on each
  physical component;
- candidate 1911 has a connected primitive chronology, but it has two lower
  palette holes, fails depth-3 residence, and has no trim3-safe upper opening.

The generalized lower compiler, suffix/deletion state, literal source cells,
and common-cap matching are outside this audit.

## 2. Exact chronology input theorem

An incidence orbit is a tuple

\[
e=(o(e),f(e),s(e)),
\]

whose phase-\(g\) physical copy is

\[
\rho^g o(e)\supset \rho^{g+s(e)}f(e).
\]

Let \(D,H\) be two owner/facet-perfect, edge-disjoint incidence matchings.
For the forward orientation define

\[
o_{i+1}=o\!\left(H_{f(D_{o_i})}\right),\qquad o_0=0,
\]

and put

\[
d_i=D_{o_i},\quad h_i=H_{f(d_i)},\quad
v_i=s(d_i)-s(h_i)\pmod {17},
\]

\[
p_0=0,qquad p_i=\sum_{j<i}v_j\pmod {17},qquad
V=\sum_{i=0}^{1429}v_i\pmod {17}.
\]

The reverse orientation is obtained by exchanging the traversal roles of
\(D\) and \(H\).  It must be reconstructed rather than inferred, because
opening and trim chronology are directional.

### Theorem 2.1 (exact accepted chronology)

Suppose the forward traversal visits all 1,430 owner and facet orbits once,
closes after 1,430 steps, and \(V\ne0\).  Then its physical lift is

\[
T_{qN+i}=\rho^{qV+p_i}o_i,
\qquad N=1430,quad 0\le q<17,
\]

and contains all 24,310 rank-nine owners and all 24,310 rank-eight Johnson
edge colours once.  The phase-zero copy of quotient position \(i\) is on lap

\[
q_i=-p_iV^{-1}\pmod {17},
\]

so its physical cut and emitted source-P start are

\[
c_i=1430q_i+i,qquad e_i=c_i-2\pmod {24310}.
\]

#### Proof

At a quotient step, the common physical facet has phase
\(qV+p_i+s(d_i)\).  The head owner therefore has phase
\(qV+p_i+s(d_i)-s(h_i)=qV+p_{i+1}\), proving the lift formula by induction.
Because 17 is prime and \(V\ne0\), the 17 lap phases are all distinct.  Each
quotient owner and facet occurs once, so the lift is bijective on both physical
layers.  Solving \(qV+p_i=0\) gives the root formula.  The offset \(-2\) is
the frozen source-to-owner trim3 convention.  The checker independently
replays every incidence and does not rely on this proof alone.  ∎

The emitted chronology table contains

```text
candidate orientation position
owner_id owner_rep facet_id facet_rep
tail_incidence tail_shift head_owner_id head_rep head_incidence head_shift
step_voltage phase_prefix d_var h_var turn_var root_var
```

Every variable is rebound to the frozen host and opening maps.

## 3. Exact residence and upper-opening tests

For a physical Johnson step put

\[
\alpha_i=T_i\setminus T_{i+1},\qquad
\beta_i=T_{i+1}\setminus T_i.
\]

Depth-3 positive residence is checked in both equivalent forms:

1. for every \(i\), the four labels
   \(\alpha_i,\alpha_{i+1},\alpha_{i+2},\alpha_{i+3}\) are distinct and all
   belong to \(T_i\);
2. every cyclic coordinate one-run has length at least four.

Zero-run statistics are reported separately and are not silently added to the
positive-residence gate.

For an owner witness with first-growth interval \([a,b]\), the corresponding
source interval is \([a,b+3]\).  Its exact source-3-trimmed interior is the
ordinary owner-edge interval

\[
[a,b).
\]

There is no second subtraction of three.  The oracle enumerates first future
arrivals of the at most eight absent coordinates, hence at most
\(8W=194480\) events, and tests all 1,430 normalized roots at physical ranks
10 through 16; rank 17 is automatic.

## 4. Fail-closed checker

The source is

```text
scratch/audit_ad_k17_complement_dual_trim3_splice_candidate_20260801.cpp
SHA256 b35fbc48d22043d3102f36b33654c7f37f43441698acb1f29fac3ca16a692da1
```

It accepts:

- the authenticated seed alone;
- a literal D- or H-side support-two rectangle row;
- a complete 2,860-row D/H factor TSV.

It strictly parses every number, rebuilds the canonical \(Z_{17}\) incidence
atlas, binds all used incidence/turn/opening variables, rejects variable
aliasing, verifies matching perfection and disjointness, and reconstructs both
orientations.  Malformed input returns exit 1 and truncates every semantic
output to its header.  A mathematically valid but rejected candidate returns
exit 3.  Only an accepted candidate can populate `.selected.tsv`; a rejected
connected chronology is available only as explicitly named
`.diagnostic_selected.tsv`.

The direct support-two rectangle face of this seed remains empty: on both D
and H sides there are 1,429 cross-component pairs, seven pairs supporting each
individual crossed leg, but zero pairs supporting both legs.  Candidates 72
and 1911 are longer assignment-cycle changes, not counterexamples to that
no-go.

The H100 build was warning-free:

```text
g++ -std=c++20 -O3 -DNDEBUG -Wall -Wextra -Wpedantic
```

The binary SHA is
`13325e1fdf6b82ea95d1fddc3a99ff4567a01a4752287324f973e0d2eeb88637`.
Seed-only replay used 18 MiB RSS.  The malformed-geometry and trailing-junk
numeric regressions both returned exit 1 with header-only outputs.

## 5. Candidate 72

Inputs:

```text
candidate72.factor.tsv
SHA256 f1d21146512662a54ad0c3811b8a4c901e738c6e3e7c2f42e835017c662134c0

candidate72.source.json
SHA256 70e266c7a1b5bc3ac245fd94b3b68ddfe8162172692cbfb45b24ba4660afe608
```

The factor changes six D owner rows and six H owner rows.  Literal replay gives

\[
\text{component lengths}=(715,715),\qquad
\text{voltages}=(15,15).
\]

Thus both physical components are primitive 12,155-owner cycles, but there is
no single 24,310-owner quotient chronology.  The immediate palettes have
1,143 colours on each shore, with exact missing representatives

\[
U_{10}:15951=\texttt{0x03e4f},qquad
L_7:3463=\texttt{0x00d87}.
\]

Componentwise residence is also negative:

| component | min one-run | length-2 runs | length-3 runs | spine |
|---:|---:|---:|---:|:---:|
| 0 | 2 | 544 | 1,615 | no |
| 1 | 2 | 646 | 1,496 | no |

The exact status is `REJECT_NOT_ONE_QUOTIENT_CYCLE`, exit 3.  A trim3 root
scan would require inventing a join and is therefore correctly not performed.

## 6. Candidate 1911

Inputs:

```text
candidate1911.factor.tsv
SHA256 c082621d6444dc2283675882557d0240babb989f2d31847eb198fbe8b4612587

candidate1911.source.json
SHA256 d719fb01468188d827659d523677414cfb7b9244d5af567c42a87137bf19110b
```

The factor keeps D fixed and changes exactly eight H owner rows.  It has one
1,430-orbit quotient cycle of voltage 9; the reverse chronology has voltage 8.
Both orientations lift bijectively to all 24,310 owners and lower edge colours.
The upper rank-ten palette is complete, while the lower rank-seven palette has
exactly two holes:

\[
3599=\texttt{0x00e0f},qquad
5447=\texttt{0x01547}.
\]

The full physical residence ledger is

```text
minimum positive run       2
positive runs of length 1  0
positive runs of length 2  1173
positive runs of length 3  3179
exact length-4 runs        2431
minimum zero run           1
zero runs length 1/2/3     1207 / 3179 / 2363
```

Hence the deletion spine fails.

The exact upper scan has 170,170 first-growth events in either orientation and
no safe root.  The two best normalized roots are:

| orientation | quotient root | physical cut | emitted P start | rank-10 load | holes r10..r16 |
|---:|---:|---:|---:|---:|:---|
| 0 | 0 | 0 | 24,308 | 2 | (0, 1666, 323, 0, 0, 0, 0) |
| 1 | 5 | 18,595 | 18,593 | 2 | (0, 1666, 323, 0, 0, 0, 0) |

Thus the best trim3 upper deficit is 1,989, wholly at ranks 11 and 12.
Ranks 10 and 13 through 16 have no hole at these roots, and rank 17 is
automatic.  The integrated report contains 2,860 root rows and 337,600
nonzero phase-core rows.

The checker status is `REJECT_OUTER_PALETTE`, exit 3.  This status names the
first global factor gate; the report simultaneously proves independent
residence and deep-opening failures, so merely repairing the two lower holes
does not finish this chronology.

## 7. Independent decisive-step audit

The previously frozen oracle

```text
scratch/audit_ad_k17_incidence_trim3_upper_opening_oracle_20260801.cpp
SHA256 33360fe78e64ed35886c9c0bda88987b6a75c05949289ab8d875653578ddbea9
```

was compiled separately and run on candidate 1911's map-bound diagnostic
chronology.  It independently returned

```text
CUT_NO_TRIM3_UPPER_SAFE_ROOT
voltage 9
rank10 orbit holes 0
safe roots 0
best holes 1989
best r10..r16 = 0,1666,323,0,0,0,0
lazy phase-core clauses 1281
```

Its audit SHA is
`c88f9deeddab692b2534b8c44728af046530389df40c1574ac07c64370d3f22b`;
its phase-core SHA is
`fb4270c360eb23ada26e7b7a1ec7d57d84285df330edfff0bd6505cf5f163c23`.
An independent code/ledger audit separately reconstructed both factor TSVs,
their palettes, components, voltages, physical run ledgers, all 2,860 root
rows, and all 337,600 integrated phase-core rows, and found no mismatch.

## 8. Exact remaining boundary

Candidate 1911 is a useful connected, primitive, upper-q1-exact chronology,
but it is not a near-positive trim3 carrier in the literal sense: it needs
simultaneous lower-palette, residence, rank-11, and rank-12 regeneration.
Candidate 72 is useful only as a strict-dual/A-Hamilton structural witness;
its actual factor remains disconnected and nonresident.  No accepted splice,
positive trim3 certificate, compiler completion, or K17 word is claimed.

All frozen local artifacts and the remote lazy CNF hash are listed in

```text
scratch/ad_k17_complement_dual_trim3_splice_20260801/run_manifest.json
```
