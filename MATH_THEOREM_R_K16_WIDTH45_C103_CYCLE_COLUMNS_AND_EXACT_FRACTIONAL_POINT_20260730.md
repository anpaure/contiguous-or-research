# K16 WIDTH45 count-103 faces: exact cycle columns and a rational branch-B point

Date: 2026-07-30  
Lane: R  
Status: **exact structural reduction and independently replayed rational point; no binary construction**

> **Subsequent resolution.**  The exact rational point and interface theorem
> in this note remain valid, but the integral frontier in Sections 0 and 7
> has since been closed by complete safe-cycle enumeration.  Branches A, B
> and C are all impossible in the frozen catalogue; see
> `MATH_THEOREM_R_K16_WIDTH45_C103_COMPLETE_SAFE_CYCLE_EXCLUSION_20260730.md`.

## 0. Result

For the frozen K16 length-eight seam catalogue, the scale-four identity and
the three tight GF(2) locks leave exactly two count-103 ledgers:

* **A:** exact-once service of all 93 targets and total scale-four slack four;
* **B:** one additional price-three service unit and total scale-four slack
  one.

Both have exact arc and cycle-column formulations below.  In the Boolean
capacity-one model, A uses only the 171,711 cycle-eligible arcs of the
slack-at-most-four graph.  B uses only the 1,681 cycle-eligible arcs of the
slack-at-most-one graph; equivalently, it has one of 43 slack-one seams with
a tight directed return, one of 30 price-three repeat targets, and otherwise
tight arcs.

The principal constructive result is an exact rational point on face B:

```text
cycle columns                         82
positive seam coordinates            602
positive price-three excess rows      14
total seam mass                      103
weighted physical service            411
raw/effective slack                     1
activation loss                         0
maximum port mass
  862757397907898073753 / 1271875625330783139064 < 1
maximum cyclic Sep5 window mass         1
WIDTH5 activators                   150, all set to w_e=x_e
common denominator LCM
  3815626875992349417192
```

An independent fail-closed checker reparses all 211,604 seams and verifies
the 82 directed simple cycles, endpoint balance, capacity, all 12,870 Sep5
rows, all 150 upper activator rows, all 450 collateral rows, all 150 lower
activator rows, all 93 target rows, and the physical scale-four identity.

Consequently **no linear/Farkas obstruction using only these rows can exclude
branch B**.  The two exact CP-SAT branch-B models are infeasible only at the
Boolean level and have no proof log.  The surviving obstruction is therefore
integral unless a stronger physical row is added.

No K16 carrier or word is constructed here.

## 1. Frozen arc data

Let (P) be the 12,870 transition ports and (E) the 211,604 directed
seams.  For (e=(u,v)), let

* (h_{te}\in\{0,1\}) be the authenticated WIDTH45 service incidence of
  target (t);
* (a_t\in\{3,4,6,8\}) be the scale-four target price;
* (Phi:P\to\{0,\ldots,7\}) be the exact port potential; and
* 
  \[
  s_e=4+\Phi(v)-\Phi(u)-\sum_t a_t h_{te}\in\{0,\ldots,11\}
  \tag{1.1}
  \]
  be the exact integral slack.

The prices sum to 408.  For a nonnegative balanced arc vector (x), put

\[
d_p=\sum_{e\in\delta^+(p)}x_e
    =\sum_{e\in\delta^-(p)}x_e,
\qquad
\mu_t=\sum_e h_{te}x_e .
\tag{1.2}
\]

Potential telescoping gives the exact identity

\[
4\sum_e x_e=\sum_t a_t\mu_t+\sum_e s_ex_e.
\tag{1.3}
\]

Capacity one and global cyclic Sep5 are

\[
0\le d_p\le1,
\qquad
\sum_{j=0}^{4}d_{p+j}\le1
\tag{1.4}
\]

for every source-cycle position (p), with indices cyclic inside its frozen
source component.

## 2. Exact ledgers

### Theorem 2.1 (complete count-103 classification after the tight lock)

Let (x\in\{0,1\}^{E}) be endpoint-balanced, let every target be serviced,
and suppose (sum_e x_e=103).  The scale-four excess identity is

\[
4=R+S,
\quad
R=\sum_ta_t(\mu_t-1),
\quad
S=\sum_es_ex_e.
\tag{2.1}
\]

The only arithmetical cases are

\[
(R,S)=(0,4),(3,1),(4,0).
\tag{2.2}
\]

The three audited tight GF(2) locks eliminate ((4,0)).  Hence A and B are
the only surviving ledgers.

#### Face A

\[
\mu_t=1\quad(t\in T),
\qquad
\sum_es_ex_e=4.
\tag{2.3}
\]

Equation (1.3) makes (sum_ex_e=103) redundant.  Because (x) is Boolean,
every selected seam has (s_e\le4), and the positive slacks have one of the
five partitions

\[
[4], [3,1], [2,2], [2,1,1], [1,1,1,1].
\tag{2.4}
\]

Every positive edge of a nonnegative balanced flow lies on a directed cycle.
Thus A may delete all arcs outside cyclic SCCs of the graph (E_{\le4}).
The exact census is

```text
arcs with slack <=4             171816
cycle-eligible arcs             171711
largest SCC                      12855
```

The positive-slack seams in A need not individually have tight returns:
several positive seams can jointly close paths through the tight SCC
condensation.

#### Face B

There is a unique price-three target (r) with

\[
\mu_t=1+\mathbf1_{t=r},
\qquad
\sum_es_ex_e=1.
\tag{2.5}
\]

Thus exactly one selected seam has slack one and every other selected seam
is tight.  That seam must have a directed return through tight arcs.  Exactly
43 of the 9,484 slack-one seams do; 30 have no service hit and 13 have one
hit.  There are 30 possible price-three repeat targets, hence 1,290
slack-seam/repeat-target prebranches.

Equivalently, every B solution lies in the cyclic SCC bank of (E_{\le1}):

```text
arcs with slack <=1              17226
cycle-eligible arcs               1681
```

The 1,681-arc bank is the cleanest exact Boolean master.  The alternative
7,742-tight-plus-43-return bank is equivalent only because a Boolean B point
has exactly one slack-one seam.

### Fractional pruning warning

The branch-specific slack cutoffs are **not** valid for the full continuous
polytope: an arc with (s_e>4), or (s_e>1), may occur with a small
fractional coefficient.  The full graph has one cyclic SCC of size 12,855
and 15 singleton SCCs; its safe continuous SCC pruning retains 211,469 of
211,604 arcs.

The exact rational point in this note happens to lie inside the smaller
1,681-arc B bank.  This makes it valid for the full relaxation as well.

## 3. Minimal cycle-column formulation

### Lemma 3.1 (complete simple-cycle decomposition)

Every nonnegative balanced flow on a finite directed graph has a finite
decomposition

\[
x=\sum_{C\in\mathcal C}\lambda_C\chi_C,
\qquad \lambda_C>0,
\tag{3.1}
\]

where each (C) is a directed simple cycle.  Repeatedly follow positive
arcs until a vertex repeats and subtract the minimum residual flow on the
resulting simple cycle.

If (x) is Boolean and (d_p\le1), its support is a vertex-disjoint union
of directed cycles, and the decomposition has coefficients one.

First impose the direct-activation subface (w_e=x_e) for the 150 WIDTH5
occurrences.  This contains every Boolean global-Sep5 point and contains the
exact fractional point below.  For a cycle (C), define

\[
\ell_C=|C|,
\quad
\sigma_C=\sum_{e\in C}s_e,
\quad
\eta_{tC}=\sum_{e\in C}h_{te},
\tag{3.2}
\]

and

\[
q_{pC}=\mathbf1_{p\in V(C)},
\qquad
w_{pC}=|V(C)\cap\{p,p+1,\ldots,p+4\}|.
\tag{3.3}
\]

Balance is then automatic.  The common capacity/Sep5 rows are

\[
\sum_Cq_{pC}\lambda_C\le1,
\qquad
\sum_Cw_{pC}\lambda_C\le1.
\tag{3.4}
\]

Face A is

\[
\sum_C\eta_{tC}\lambda_C=1\ (t\in T),
\qquad
\sum_C\sigma_C\lambda_C=4.
\tag{3.5}
\]

Face B introduces (z_t\ge0) on the 30 price-three targets:

\[
\sum_C\eta_{tC}\lambda_C=1+z_t,
\quad
\sum_{a_t=3}z_t=1,
\quad
z_t=0\ (a_t\ne3),
\quad
\sum_C\sigma_C\lambda_C=1.
\tag{3.6}
\]

For a Boolean solution (z) is a unit vector.  In the continuous relaxation
it may distribute the one unit over several price-three targets.  In both
faces (1.3) implies

\[
\sum_C\ell_C\lambda_C=103.
\tag{3.7}
\]

For integral A and B, (mathcal C) may be restricted respectively to simple
cycles of (E_{\le4}) and (E_{\le1}).  For the unrestricted continuous
model, cycles using larger-slack arcs must be retained.

## 4. WIDTH5 activators in a fractional point

For each of the 150 authenticated width-five occurrences, let (e=(u,v)),
let (Z_e) be its three collateral cut positions, and introduce (w_e):

\[
0\le w_e\le x_e,
\quad
w_e+d_z\le1\ (z\in Z_e),
\quad
w_e\ge x_e-\sum_{z\in Z_e}d_z.
\tag{4.1}
\]

The phrase “Sep5 forces (w=x)” is literally true for Boolean selected
seams, but need not mean uniqueness at a fractional point.  Nevertheless

\[
w_e=x_e
\tag{4.2}
\]

is always a feasible fractional choice here.  Each collateral position lies
in a Sep5 window with (u) or (v); nonnegativity and balance give

\[
x_e\le d_u,\qquad x_e\le d_v,
\tag{4.3}
\]

so (1.4) gives (x_e+d_z\le1).  Thus (4.2) satisfies all four row types in
(4.1).  The exact point supplies all 150 values explicitly and the
independent checker verifies them rather than inferring them.

For a general activator choice the physical slack is

\[
s_e^{\rm eff}x_e=s_ex_e+
   a_{t(e)}(x_e-w_e)
\tag{4.4}
\]

on a WIDTH5-only seam.  In the point below (w=x), so activation loss is
zero and effective slack equals raw slack.

## 5. Exact rational branch-B point

### Theorem 5.1

The capacity-one, global-Sep5, complete-activator continuous relaxation of
face B is nonempty.

### Proof certificate

The point file contains 82 exact rational simple-cycle columns.  Expanding
them gives 602 positive seam masses.  Fourteen price-three excess variables
are positive and sum to one.  The exactifier obtains these values from a
96-by-96 integer system consisting of all 93 service rows, the slack row,
the count row, and the unique active Sep5 row `(component=14,start=33)`.
Its determinant has absolute value

```text
45787522511908193006304.
```

The common denominator LCM is

```text
3815626875992349417192.
```

The independent checker reconstructs the raw ledger and returns

```text
status                              PASS_EXACT_PHYSICAL_POINT_REPLAY
columns                             82
positive seams                      602
seam mass                           103
weighted raw service                411
weighted physical service           411
activation loss                       0
raw slack                              1
effective slack                        1
service surplus                        3
cyclic Sep5 violations                 0
```

The cycle-length histogram is recorded in the checker artifact; lengths
range from 2 to 135.  Every coefficient and activator is serialized as an
integer or rational string; JSON floats are rejected by the independent
checker.  This proves the theorem.  QED.

### Proposition 5.3 (the 82-column Boolean support is insufficient)

Regard the 82 exact rational cycles as a restricted Boolean column
catalogue, and impose port capacity, all 12,870 cyclic Sep5 rows, all 93
service rows, count 103, branch-B slack one, and one price-three repeat.
Before solving, the exact integral filters leave only eight columns:

```text
raw rational columns                              82
accepted integral columns                          8
rejected for an internal Sep5 conflict             44
rejected for impossible target multiplicity        73
rejected for branch-B slack above one               37
rejected for length above 103                        1
```

The rejection categories overlap.  The eight retained columns provide no
occurrence of 33 of the 93 targets, so the restricted master is infeasible
immediately.  CP-SAT records zero branches and zero conflicts because the
empty provider row is installed explicitly.

This is **not** a global branch-B obstruction.  It says only that a cycle
decomposition chosen to exactify the fractional edge flow is a poor Boolean
basis: 74 of its 82 cycles are individually unusable.  Any constructive
continuation must price Sep5-safe directed cycles directly in the global
branch-B arc bank, rather than decomposing this same 602-seam flow again.

### Corollary 5.2 (no current-row LP obstruction for B)

No Farkas certificate formed only from endpoint balance, port capacity,
global Sep5, the 93 service rows, the scale-four slack row, and the 150
activator rows can exclude face B: the exact rational point satisfies all of
them.

This does not contradict the two CP-SAT presolve `INFEASIBLE` results.  Those
are Boolean models.  They currently have no DRAT/LRAT proof or independently
checkable linear-combination core, so they remain solver evidence of an
integrality gap, not a theorem excluding B.

## 6. Candidate and replay contract

An exact arc-form candidate may instead specify a common denominator (D>0)
and integer numerators (X_e,Z_t,W_e).  A fail-closed replay must verify:

1. every seam id, endpoint, hit set, slack, occurrence and source hash;
2. (X_e\ge0), endpoint balance, and (d_p\le D);
3. every cyclic Sep5 window has cut mass at most (D);
4. all 150 activator rows
   \(0\le W_e\le X_e\), (W_e+C_z\le D), and
   (W_e\ge X_e-\sum_zC_z);
5. A: every physical target load is (D) and effective slack is (4D);
6. B: target load is (D+Z_t), (Z_t\ge0) only for price-three targets,
   (sum_tZ_t=D), and effective slack is (D);
7. (sum_eX_e=103D); and
8. either an exact simple-cycle decomposition, or an independently rebuilt
   decomposition obtained by repeatedly peeling a minimum positive directed
   support cycle.

When the candidate uses (W_e=X_e), as the retained point does, activation
loss is zero and raw slack equals effective slack.

The retained point uses the checker-native schema

```text
point.columns[] = {
  seam_ids: [ordered directed simple cycle],
  coefficient: "numerator/denominator"
}

point.occurrence_activators[] = {
  binary_seam_id,
  target,
  split,
  required_zero_cut_indices: [three exact ports],
  value: "numerator/denominator"
}
```

## 7. Scope and remaining gate

The reduction and point are source-relative to the frozen WIDTH45 isolated-
seam catalogue.  They omit reverse-edge constraints, q1, survivor rows,
other deeper shadows, connectedness, COMP3, boundary absorption, and literal
word verification.

The exact remaining A/B question is Boolean.  For B, a proof must explain
why the exact rational cycle mixture cannot be rounded to vertex-disjoint
cycles while retaining service, one slack unit, and Sep5.  For A, neither a
binary point nor a certified obstruction is presently known.

## 8. Frozen artifacts

```text
Floating source point:
scratch/k16_width45_c103_branchB_fractional_20260730.audit.json
  SHA-256 992e6e54623b0d9af103e80eb809354b7716d6479290fbcc5cd3d7d60e85afeb
scratch/k16_width45_c103_branchB_fractional_20260730.tsv
  SHA-256 7a840d4c41e5a4a0dc489fa17d5e2bef7109da2c06db0183c9825fdae5272f77

Exactifier:
scratch/exactify_k16_width45_c103_branchB_fractional_20260730.py
  SHA-256 f4bc999d5249a50ad3a1f55cd445e6d0b25cd1189d84d9a9f6c999e5c1dbb43c
scratch/k16_width45_c103_branchB_exact_fractional_point_20260730.json
  SHA-256 2fd6dec37213daa697b90c239cf9183099f13343dfa6f8fe4c054724e70f726b
  payload 288b7bbb36da9e76e66e3be150fe66691ca51919ef58a9406a30829bf1f5521a
scratch/k16_width45_c103_branchB_exactification_20260730.audit.json
  SHA-256 e932f5f61f8fcdf32bfb5de833bd6209d29692adb8ba604c4de3b8a3d44569bf
  payload 18d62c30560801b654aeda8172bb6a51f000d7fea218dc00a09c532700d181da

Independent fail-closed checker (after the nonmutating zero-mass lookup fix
and enforcement of the declared branch-B ledger):
scratch/audit_r_k16_width45_c103_cycle_column_point_20260730.py
  SHA-256 f8505ca395c349352d212b2c0d1c7e23ca46f26d99d70339f9db6be85c61dd0c
scratch/k16_width45_c103_branchB_exact_fractional_point.independent.v2.audit.json
  SHA-256 5595eb7c5463f8e7d414db01c66bc651ab14ccc743b7bad3799a3e0764b0b0cc
  payload d2133732e64fccc3d31c4d0787d779a52741dcbd1943db4768f3f4876801c526

Restricted 82-cycle Boolean master:
scratch/solve_r_k16_width45_c103_restricted_cycle_column_master_20260730.py
  SHA-256 a3c1628f13873c3eb0b4b6cd1628cd55647c05fdcee6b198d6dad4b87e8a280e
scratch/k16_width45_c103_branchB_restricted82_master_20260730.audit.json
  SHA-256 cad6b7ba98968639a74a7b8d1c6c22d3911aced25d5f7c1f925916d7626e13dd
  payload 2d7d9d2245845f2715f754ea4c1507e0e27278cc2fda1dbf283da675ae8c7303
```

The exactifier used one H100 CPU, 115,612 KiB maximum RSS and 2.80 seconds
wall time under a 1.5 GiB address-space cap.  The independent replay used one
H100 CPU, 107,092 KiB maximum RSS and 0.95 seconds under a 768 MiB cap.
