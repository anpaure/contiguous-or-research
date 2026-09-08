# Finite positive census for one resident rotating-hole collar, and the exact near-factor gate

Date: 2026-08-01  
Status: exact finite existence theorem for four calibrated dimensions; exact
general near-factor reduction.  This is not an all-dimension host theorem and
does not include the lower compiler/common cap.

## 1. Setup

Let `ML_m` be the incidence graph between ranks `m-1` and `m` of a
`(2m-1)`-element ground set.  Write

\[
                 W={2m-1\choose m}={2m-1\choose m-1}.
\]

Use the notation of the shortest resident return-rail theorem.  Thus an
oriented target atom is

\[
 e=(L,U,E,F),\qquad E=L+d_0,\quad F=L+a,\quad U=L+a+d_0,
\]

and one ternary-hex choice `(b,c)` gives the plus edges

\[
                    AF,\qquad CB,\qquad ED.
\]

Choose the rotating-hole rail

\[
 F=V_1,V_2,\ldots,V_{h+2},V_0=E
\]

from

\[
 Z=L+a+d_0+y,qquad
 (z_0,\ldots,z_{h+2})=(a,y,d_0,x_0,\ldots,x_{h-1}),
 \qquad V_i=Z-\{z_i,z_{i+1}\}.
\]

The **full terminal plus collar** is the two-path Johnson bank

\[
 {cal P}^+=
   \{AF,CB,ED\}\cup
   \{V_iV_{i+1}:1\le i\le h+2\},                    \tag{1.1}
\]

where indices on the last family are modulo `h+3`.  It is the complete
`G^+=N union R` state, not merely the return rail.

An **upper-Hamilton completion** of (1.1) is a Hamilton cycle of `ML_m`
which contains the two-incidence lift of every edge of `P+` and whose
projection to the rank-`m` shore has every rank-`m+1` set as the union of
two consecutive owners.

## 2. Finite existence theorem

### Theorem 2.1

The full terminal plus collar has an upper-Hamilton completion for

\[
                    (m,h)=(4,2),(5,2),(6,3),(7,3).       \tag{2.1}
\]

For each fixed pair in (2.1), the conclusion holds for every admissible
choice of the labelled roles in (1.1).

#### Proof

For the canonical representative use coordinates `0,...,2m-2` and put

```text
L={0,...,m-2}, a=m-1, d0=m, b=0, c=m+1, y=m+2,
(x0,...,x_(h-1))=(1,...,h).
```

The retained model for each pair selects incidence edges in `ML_m`.
Independent replay verifies all of the following directly from the selected
incidences, without trusting the labels of the generating CNF:

1. every vertex on both shores has degree exactly two;
2. the selected factor is connected, hence is one Hamilton cycle;
3. every incidence of every Johnson edge in (1.1) is selected; and
4. the unions of the two selected rank-`m` neighbours at the `W`
   rank-`m-1` vertices contain the complete rank-`m+1` layer.

The replay also checks every clause of each retained DIMACS instance against
the corresponding model.  This proves existence for the canonical
representatives.

All coordinates appearing as `L`-members, `a,d0,c,y` and the ordered
`x_i` have distinct prescribed roles; unused coordinates have no additional
structure.  The full symmetric group on the ground set is transitive on
such labelled role assignments.  Applying the corresponding coordinate
permutation to a canonical Hamilton cycle proves the last statement.  \(\square\)

The numbers in the four replays are

| `m` | `h` | vertices per shore | protected Johnson edges | required upper colours |
|---:|---:|---:|---:|---:|
| 4 | 2 | 35 | 7 | 21 |
| 5 | 2 | 126 | 7 | 84 |
| 6 | 3 | 462 | 8 | 330 |
| 7 | 3 | 1716 | 8 | 1287 |

For example, at `(m,h)=(4,2)` one completion is the following alternating
cycle of rank-three and rank-four masks:

```text
15,13,77,73,89,81,83,19,23,22,30,28,29,25,27,26,90,74,
106,98,114,82,86,70,102,100,108,104,105,97,113,49,57,41,
45,44,46,42,43,11,75,67,99,35,51,50,58,56,60,52,54,38,
39,7,71,69,101,37,53,21,85,84,116,112,120,88,92,76,78,14.
```

Its canonical roles are

```text
(A,B,C,D,E,F)=(30,46,54,39,23,15),
(V0,V1,V2,V3,V4)=(23,15,77,89,83).
```

## 3. The exact general near-factor gate

The finite theorem suggests the following precise general certificate.  It
is strictly weaker than asking a SAT solver for a Hamilton cycle at once.

Properly two-edge-colour a protected plus bank

\[
                         P=P_0\mathbin{\dot\cup}P_1
\]

and let `M0` be a perfect matching containing `P0` and avoiding `P1`.
For an incidence `e=LU` outside `M0`, define

\[
 \operatorname{up}_{M_0}(e)=M_0(L)\cup U,
 \qquad
 \lambda_{M_0}(e)=\bigl(L,M_0^{-1}(U)\bigr).            \tag{3.1}
\]

The links in (3.1) are edge-labelled directed permutation links; their
underlying graphic matroid treats opposite links as a parallel two-cycle.

### Theorem 3.1 (near-factor certificate)

Suppose there is a matching `Q subset ML_m-M0` such that

1. `P1 subset Q`;
2. `|Q|=W-s`;
3. `up_M0(Q)` covers every rank-`m+1` colour;
4. the `W-s` labelled links `lambda_M0(Q)` are graphic-independent; and
5. after deleting the endpoints of `Q`, the residual graph `ML_m-M0`
   has a perfect matching.

Then `P` is contained in an upper-surjective q1 two-factor with at most `s`
components.

#### Proof

Let `R` be the residual perfect matching and put `M1=Q union R`.  Then
`M0 union M1` is a q1 two-factor containing `P`, and condition 3 is exactly
upper surjectivity.  The components of `M0 union M1` are the cycles of the
permutation `M0^(-1) M1`.  Its edge-labelled lower-shore link graph contains
the forest `lambda_M0(Q)` of rank `W-s`.  Adding the residual links cannot
decrease graphic rank, so the permutation has at most `s` cycles.  \(\square\)

Thus the exact fixed-`H` host target is a certificate with `s=O(H)`.
Condition 5 is only an `s`-by-`s` residual Hall problem; the correlated part
is the simultaneous upper coverage and graphic independence of `Q`.

## 4. Scope and the surviving obstruction

Theorem 2.1 is finite positive evidence, not an induction.  Even with no
protected collar, existence in every dimension of a lower-perfect,
upper-surjective bounded-component factor is the unresolved ordered-diamond
or doubly-rainbow central problem.  The protected theorem cannot be inferred
from the small protected-factor/Ore--Ryser result, because that theorem sees
the two incidences at a lower vertex separately and supplies no paired-upper
or graphic-rank row.

Nor can one replace the rotating-hole hypothesis by generic typed-resource
privacy.  The authenticated four-edge protected cut in `J(5,3)` has distinct
owner, lower and upper resources and belongs to a q1 factor, but no q1
Hamilton factor contains it.  The special collar geometry is therefore a
real hypothesis.

No statement here asserts:

* global residence outside the protected collar;
* arbitrary-width upper completeness outside the immediate paired palette;
* a literal lower compiler/common cap; or
* an all-`m` upper-decorated bounded-component extension.

## 5. Frozen artifacts

Run

```text
python3 scratch/audit_rotating_hole_h1_hamilton_census_20260801.py
```

Expected status:

```text
PASS_ROTATING_HOLE_H1_UPPER_HAMILTON_CENSUS
```

Audit script:

```text
scratch/audit_rotating_hole_h1_hamilton_census_20260801.py
SHA256 6b2b54b2ecf80c025511946ed85104ce06c48f14ff902248bce8546808aff1b0
```

Audit JSON:

```text
scratch/rotating_hole_h1_hamilton_census_20260801.audit.json
SHA256 99cb4a3748ecc31017667e1e603d66f7ce536f963bb424b3fca78760f1220db2
payload 675d4109a0719d015e6bd563470f7e2c0f2da002f061113d920e4eca30ac0002
```

CNF/model pairs:

```text
m4_h2.cnf   8148cbd8d0d655cd8da4b75f11807f010c154a103654e25779d79f32e2ba8293
m4_h2.model c25f760391528a5c46db4f5770e634329ae2d263f4c8b44cf96f36a61292357f
m5_h2.cnf   ccab80ef259756d823e614f544226301496aab8b96f51f2741e1bc8bb5c68618
m5_h2.model 5c0ea7aef6339c333348c5a39829f164652f5a0ae5e07bba37fe3c96c49def57
m6_h3.cnf   0216c41f20bb6a7c24bdb7e9669dd019171d9123bd073b68f9088cd04efb71d3
m6_h3.model 94e6f2cb627b61aa63987d64200b84800764cf6725042599951b687196905cb3
m7_h3.cnf   ef31f78a6c1c2206aa0122ca109325dc7c49a347e849dfa392b61d12685b3cd3
m7_h3.model a05c43d91eeb1fb11edc83f82104222aea157e8cf520c9345af9d15bda33df15
```

They are stored under
`scratch/rotating_hole_h1_hamilton_census_20260801/`.
