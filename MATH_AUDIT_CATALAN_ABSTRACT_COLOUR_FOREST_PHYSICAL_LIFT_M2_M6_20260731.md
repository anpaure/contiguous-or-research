# Sparse m=2 through m=6 audit of the abstract Catalan colour forest lift

Date: 2026-07-31  
Status: explicit-quantifier, dependency-free sparse replay; diagnostics for
one deterministic forest in each dimension, not a physical no-go

## 1. Quantifiers and deterministic choices

Let (B_m) be the inclusion graph between ranks (m-1) and (m+1) of
(Q_{2m}). Put

\[
 K_m=\operatorname{Cat}_m,qquad N_m=mK_m,qquad M_m=(m+1)K_m.
\]

The abstract theorem has the quantifier form

\[
 \boxed{
 \forall m\ge2\ \exists\sigma_m\ \exists\tau_m\ \exists S_m\subseteq\tau_m:
 H_m=\sigma_m\cup S_m\text{ is a balanced spanning path forest.}}
\]

Here sigma_m and tau_m are disjoint perfect matchings of B_m,
and S_m has exactly K_m edges while omitting at least one
tau_m-edge from every alternating cycle of sigma_m union tau_m. This is
existential in the choices; it is not a
statement about every pair of matchings or every partial matching.

The finite replay fixes those existential choices completely:

1. (sigma_m) is the two-step matching of the standard left-to-right BTK
   symmetric-chain decomposition.
2. tau_m is obtained by scanning lower masks increasingly and applying
   a standard augmenting search through increasing upper masks in
   (B_m-sigma_m).
3. Alternating cycles are rotated to their least lower mask and ordered by
   that mask. The replay takes the first at most r-1 tau_m-edges of
   each (r)-cycle until exactly (K_m) edges have been selected.

Thus the computational statement is only

\[
 \forall m\in\{2,3,4,5,6\},
 \quad H_m^{\rm det}=\sigma_m^{\rm det}\cup S_m^{\rm det}
 \quad\text{has the audited properties below.}
\]

For every fixed (H\subseteq B_m), its physical lift (F(H)) is uniquely
defined: incidence (L\subset U), with (U\setminus L=\{a,b\}), lifts to
the Johnson edge

\[
                   (L+a)(L+b).
\]

The exact physical criterion is universal over fixed inputs:

\[
 \forall H\subseteq B_m,qquad
 H=G(P)\text{ for a middle Hamilton cycle }P
 \iff F(H)\text{ is connected and two-regular.}
\]

Failure of the deterministic (F(H_m^{\rm det})) therefore does not say
that every other admissible (H) fails.

## 2. Sparse abstract verification

For every m=2 through m=6, the replay checks incidence regularity, both
matchings, the alternating-cycle decomposition, and the cycle omission.
Every colour component of (H_m^{\rm det}) is then leaf-peeled. The forced
edges are exactly (sigma_m), proving both uniqueness and determinant
magnitude one without forming a dense matrix. The sign is the inversion
sign of the (sigma_m) permutation in sorted shore orders.

| (m) | (K) | (N) | (M) | colour paths | determinant | alternating-cycle lengths |
|---:|---:|---:|---:|---:|---:|---|
| 2 | 2 | 4 | 6 | 2 | -1 | 4 |
| 3 | 5 | 15 | 20 | 10 | +1 | 2,13 |
| 4 | 14 | 56 | 70 | 42 | -1 | 2,2,4,6,21,21 |
| 5 | 42 | 210 | 252 | 168 | -1 | 2,4,8,9,10,41,136 |
| 6 | 132 | 792 | 924 | 660 | +1 | (2^{12},3^3,4,8,24,29,45,649) |

The exact shore profile is (1^{N-K}2^K) in every row. No dense
determinant is formed at (m=5,6); the balanced-path leaf certificate is
the determinant proof.

## 3. The separate \(\Psi(\sigma_m)\) quantifier and the path correction

The matching statement “\(\sigma_m\) is a perfect colour matching” does not
imply that its physical lift is a union of paths. The replay therefore
audits \(\Psi(\sigma_m)\) separately, before adding \(S_m\).

| \(m\) | edges \(N\) | spanning | components | cycle rank | degree histogram | \(K\)-path forest? |
|---:|---:|---:|---:|---:|---|---|
| 2 | 4 | yes | 2 | 0 | \(1^4 2^2\) | yes |
| 3 | 15 | yes | 5 | 0 | \(1^{12}2^6 3^2\) | no |
| 4 | 56 | yes | 14 | 0 | \(1^{40}2^{20}3^8 4^2\) | no |
| 5 | 210 | yes | 42 | 0 | \(1^{140}2^{70}3^{30}4^{10}5^2\) | no |
| 6 | 792 | yes | 132 | 0 | \(1^{504}2^{252}3^{112}4^{42}5^{12}6^2\) | no |

In each replay, \(\Psi(\sigma_m)\) is a spanning forest with exactly
\(K_m\) components; every component has \(m+1\) vertices and \(m\) edges.
It is a path forest only at \(m=2\).

There is an explicit all-\(m\) branching witness. Let

\[
 E_m=\{0,2,4,\ldots,2m-2\}.
\]

For every \(j\), put

\[
 L_j=E_m\setminus\{2j\},\qquad
 U_j=E_m\cup\{2j-1\pmod {2m}\}.
\]

A direct replay of the BTK stack matching gives
\(\sigma_m(L_j)=U_j\): its first two free zero positions are precisely the
removed even position and the preceding cyclic odd position. The lifted
diamond \(\psi(L_j,U_j)\) has \(E_m\) as one middle endpoint. These \(m\)
lower rows are distinct, and every \(\sigma_m\)-edge incident with \(E_m\)
must arise from one of the \(m\) lower facets \(E_m-\{2j\}\). Therefore

\[
                         \deg_{\Psi(\sigma_m)}(E_m)=m.
\]

The complement alternating set has the same degree. This proves, without a
finite extrapolation, that the standard BTK \(\Psi(\sigma_m)\) is not a
path forest for every \(m\ge3\). The JSON freezes every incident
\((L_j,U_j)\) row for \(m=2,\ldots,6\).

## 4. Literal full-\(H\) physical-lift census

Every deterministic lift has exactly (M) physical edges on (M) middle
vertices, so its total degree is (2M). Define a middle **hole** as degree
zero and an overload unit at (X) as (max(0,deg X-2)). The exact replay
gives:

| (m) | middle degree histogram | holes | overloaded vertices | overload units | components |
|---:|---|---:|---:|---:|---:|
| 2 | (1^1 2^4 3^1) | 0 | 1 | 1 | 1 |
| 3 | (1^5 2^{10}3^5) | 0 | 5 | 5 | 2 |
| 4 | (1^{27}2^{23}3^{14}4^5 5^1) | 0 | 20 | 27 | 3 |
| 5 | (1^{104}2^{79}3^{43}4^{19}5^5 6^2) | 0 | 69 | 104 | 15 |
| 6 | (1^{387}2^{292}3^{148}4^{65}5^{21}6^{10}8^1) | 0 | 245 | 387 | 44 |

There are no degree-zero middle vertices through (m=6), but there are
degree-one deficits in every dimension. Their total deficit equals the
listed overload units, as forced by the exact average degree two.

The component sizes are also exact:

* (m=2: 6);
* (m=3: 16,4);
* (m=4: 60,5,5);
* (m=5: 168,6^{14});
* (m=6: 595,14^4,7^{39}).

Hence none of these five deterministic lifts is a spanning two-regular
cycle. At (m=2) it is connected but not regular; from (m=3) onward it
also has multiple components.

## 5. Doubled-upper local incompatibility

At a doubled upper colour (U), let its two lower neighbours be
(L_0,L_1). Their lifted Johnson edges share the middle owner needed for a
contiguous cap-two block if and only if

\[
       |(U\setminus L_0)\cap(U\setminus L_1)|=1
       \iff |L_0\cup L_1|=m.
\]

The exact compatible/incompatible counts are

| (m) | doubled (U) | compatible | incompatible |
|---:|---:|---:|---:|
| 2 | 2 | 2 | 0 |
| 3 | 5 | 3 | 2 |
| 4 | 14 | 12 | 2 |
| 5 | 42 | 28 | 14 |
| 6 | 132 | 86 | 46 |

The first literal incompatible rows, written as
`U : L0,L1 -> lifted edge 0 ; lifted edge 1`, are:

* (m=3): `0x1b : 0x09,0x12 -> 0x0b-0x19 ; 0x13-0x1a`;
  `0x36 : 0x12,0x24 -> 0x16-0x32 ; 0x26-0x34`.
* (m=4): `0x57 : 0x16,0x51 -> 0x17-0x56 ; 0x53-0x55`;
  `0xa7 : 0x07,0xa1 -> 0x27-0x87 ; 0xa3-0xa5`.
* (m=5): `0xbd : 0x35,0x8d -> 0x3d-0xb5 ; 0x9d-0xad`;
  `0xf5 : 0x35,0xd4 -> 0x75-0xb5 ; 0xd5-0xf4`;
  `0x173 : 0x131,0x152 -> 0x133-0x171 ; 0x153-0x172`.
* (m=6): `0xef : 0x2f,0xc7 -> 0x6f-0xaf ; 0xcf-0xe7`;
  `0x1db : 0x5b,0x1ca -> 0xdb-0x15b ; 0x1cb-0x1da`;
  `0x2d7 : 0x253,0x2c5 -> 0x257-0x2d3 ; 0x2c7-0x2d5`.

The complete incompatible catalogues, including both deletion-coordinate
pairs and both physical lifted edges, are frozen in the JSON. The uniform
orientation question is downstream and is not applicable to any of these
five deterministic lifts, because none first passes connected
two-regularity and all-local compatibility.

## 6. Remote \(m=4\) construction status

The nonduplicate Lane-L exact search for a different, fully physical
uniformly outgoing \(m=4\) repair reached its 900-second cap with status
`UNKNOWN`: 11,750,644 branches, 88,658 conflicts, one worker, wall time
900.003156001 seconds. It produced no candidate. This is neither SAT nor
UNSAT and supplies no mathematical obstruction.

The exact remote result is frozen locally as
`scratch/laneL_m4_directed_strong_seed20260731.remote_result.json`, SHA
`f0536b39b46980f34e068b478cd8bb3296d1fe8ba2162ab942254234d6af676c`,
canonical payload
`b1da5104172da5a9be86f5e2c041e7a61b20a4f0a7c1781d34358e5a6372335b`.
The executed producer SHA was
`d547e9e599e11d077d449ccf2c168f3ad30de15379f66535572b9d0e1b08e426`.

## 7. Scope

This audit proves a useful obstruction to the **particular deterministic
BTK plus lexicographic residual choice**, not to the abstract theorem and
not to physical realization using a different (sigma,tau,S). In
particular the observed growth (0,2,2,14,46) of local incompatibilities is
not claimed to be minimal over the choice space.

The new replay imports no producer code. Its (m=2,3,4) outputs are checked
field-for-field against the previously frozen audit, SHA
`70e0b4bf36db60e8fc60d63d252545ca6b5d088de0832b462ab8e4a9ec6c1ae6`.
The (m=5,6) stages use only sparse inclusion lists, augmenting paths,
component walks, and leaf peeling.

Artifacts:

* `scratch/audit_catalan_abstract_colour_forest_lift_m2_m6_sparse_20260731.py`,
  SHA `6720d1739de2c64b146379f2c68f01ca724ca420b83ff82dbc768d0b7bcc5a51`;
* `scratch/catalan_abstract_colour_forest_lift_m2_m6_sparse_20260731.audit.json`,
  SHA `59c4ff63f2f1d45533bea648ebed1e2869c6afc38930a85c4f70043a7b109ddd`,
  payload `f5450036e04d767bc3a305490cab6d9b81d5eefe293a11b90c3d1d5dacae18a0`;
* `scratch/catalan_abstract_colour_forest_lift_m2_m6_sparse_20260731.catalogue.tsv`,
  SHA `8437f684cfbb2fd7cb633d2a2cdd374ead1844f736224a4252949fe0d29e5539`.

No unrestricted directed-repair theorem or physical all-(m) no-go is
claimed.
