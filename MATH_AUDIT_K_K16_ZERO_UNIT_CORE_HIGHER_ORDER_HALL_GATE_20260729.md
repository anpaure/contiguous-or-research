# K16 zero-unit-core overlay: UNSAT metadata audit and the higher-order Hall gate

Date: 2026-07-29  
Lane: K  
Status: frozen metadata audited; exact higher-order reduction proved  
Scope: fixed q1 endpoint \(Q\), fixed resident endpoint \(R\), inherited short-run rows

## 1. Audited verdict

The frozen result

```text
scratch/k16_zero_full_unit_core_overlay_solve_20260729.json
SHA-256 6995f5d2d6e2b10385cd2d342b39fc93d10b3455437b27f26048890dbdb4902b
```

is structurally consistent with the exact initial fixed-overlay model between

```text
Q = scratch/k16_q1_endpoint_resume1_zero_full_unit_cores_20260729.json
R = scratch/k16_pbbs_oriented_noaa_softq1_resume1_20260729.json.
```

The reconstructed dimensions are:

| object | count |
|---|---:|
| common physical edges | 391 |
| resident-only red variables | 12,479 |
| q1-only blue variables | 12,479 |
| literal decision variables | 24,958 |
| serialized model variables | 24,959 |
| endpoint-degree rows | 12,867 |
| lower-q1 rows | 11,440 |
| upper-q1 rows | 11,440 |
| distinct inherited motif rows | 2,250 |
| total constraints | 37,997 |

The extra serialized variable is model-internal; the mathematical system has
exactly the two 12,479-variable shores.  The row identity is

\[
12867+\binom{16}{7}+\binom{16}{9}+2250=37997.
\]

Every inherited motif has at least one blue candidate and all 2,250 candidate
signatures are distinct.  The model binds both q1 palettes.  The endpoint has
four physical components, zero q1 holes on both shores, and 2,250 short runs.

The unit-propagation fixpoint has score

\[
(0,0,0,2250,4)
\]

and variable-state histogram

\[
22622\text{ unassigned},\qquad2029\text{ forced zero},qquad307\text{ forced one}.
\]

The frozen CP-SAT result reports `INFEASIBLE` at iteration zero, before any
dynamic CEGAR row is added.  Thus the reported contradiction concerns exactly
degree balance, both q1 palettes, bounds, and all inherited motif rows.

### Proof-scope caveat

The result and its 220-byte log contain no assumption core, proof trace, or
independently checkable Farkas/branch certificate.  The result also does not
record the serialized-model SHA, although all of its input hashes and counts
agree with the frozen build report.  This local audit verifies all available
hashes, dimensions, row counts, and status linkage; it does **not** rerun
CP-SAT or independently prove the `INFEASIBLE` status.  Accordingly:

- operationally, the fixed-overlay model is solver-certified UNSAT;
- theorem-level use should wait for a guarded core plus an independently
  checkable linear or integer certificate.

The serialized model is frozen at

```text
scratch/k16_resume1_zero_fullunit_overlay_circulation_build_20260729.model.pb
SHA-256 c2a5cf5e56dfbc6cebe021a92fa46c8999ec6206a9649d8d37e3c8466217e1ec.
```

## 2. What zero unit cores does and does not say

Let \(A=R\setminus Q\) be the red shore and \(B=Q\setminus R\) the blue
shore.  For \(f\in A\), write \(a_f=1\) when the resident edge is inserted;
for \(e\in B\), write \(b_e=1\) when the q1 edge is deleted.

The base overlay system is

\[
\sum_{f\in A(v)}a_f-\sum_{e\in B(v)}b_e=0
\quad(v\text{ a middle vertex}),
\tag{2.1}
\]

and, for every lower or upper q1 colour \(c\),

\[
\sum_{e\in B_c}b_e-sum_{f\in A_c}a_f\le s_c,
\qquad s_c=\mu_Q(c)-1.
\tag{2.2}
\]

For a short-run motif \(M\) with closure \(C_M\), the inherited residence row
is

\[
\sum_{e\in C_M\cap B}b_e\ge1.
\tag{2.3}
\]

The all-zero assignment satisfies (2.1)--(2.2), so the base system is
nonempty.  Zero peeled unit cores means only that repeated unit minimization
of the signed rows does not derive a contradiction.  It does not imply that
(2.1)--(2.3) are jointly feasible.

In the circuit-hypergraph notation of the companion audit, the reported UNSAT
asserts

\[
\mathscr C_R(Q)\ne\varnothing,
\qquad
\Delta_R(Q)=\tau(\mathscr C_R(Q))\ge1.
\tag{2.4}
\]

It does not determine the size of a minimal circuit, the transversal number,
or the exact deficiency.  A single motif can in principle have a non-unit
extension obstruction, so “higher-order” refers to the proof mechanism, not
automatically to the number of motif rows.

## 3. Exact fractional Hall/min-cut theorem

The first decisive audit is whether the LP relaxation is already infeasible.
This admits an exact weighted Hall formulation.

Let \(P_R(Q)\) be the compact polytope obtained from (2.1)--(2.2) and

\[
0\le a_f,b_e\le1,
\]

without motif rows.  Let \(H\) be the motif-versus-blue-edge matrix

\[
H_{M,e}=\mathbf1[e\in C_M].
\]

The LP residence system asks for \((a,b)\in P_R(Q)\) with

\[
Hb\ge\mathbf1.
\tag{3.1}
\]

For a nonnegative motif weight vector \(\alpha\), define the induced blue-edge
weight

\[
w_\alpha(e)=\sum_{M:e\in C_M}\alpha_M.
\tag{3.2}
\]

### Theorem 3.1 (weighted Hall separation)

The LP system (3.1) is feasible if and only if, for every
\(\alpha\in\mathbb R_{ge0}^{\mathcal M}\),

\[
\boxed{
\max_{(a,b)\in P_R(Q)}
   \sum_{e\in B}w_\alpha(e)b_e
\ \ge\ 
\sum_{M}\alpha_M.}
\tag{3.3}
\]

#### Proof

If \(Hb\ge\mathbf1\), then for every \(\alpha\ge0\),

\[
\sum_e w_\alpha(e)b_e
=\alpha^THb
\ge\alpha^T\mathbf1.
\]

Conversely, suppose (3.1) is infeasible.  The image

\[
Y=\{Hb:(a,b)\in P_R(Q)\}
\]

is compact and convex, and it is disjoint from the closed dominant orthant

\[
D=\{y:y\ge\mathbf1\}.
\]

Strong separation gives a vector \(\alpha\) with

\[
\sup_{y\in Y}\alpha^Ty<\inf_{z\in D}\alpha^Tz.
\]

The right-hand infimum is finite only when \(\alpha\ge0\), in which case it
equals \(\alpha^T\mathbf1\).  This is the strict reverse of (3.3). \(\square\)

Thus an LP-level obstruction is exactly a weighted family of motif demands
whose total demand exceeds the maximum compatible blue deletion weight.  This
is the correct higher-order Hall statement; it allows many motifs to share a
deletion edge and retains all endpoint and palette coupling.

### Dual Hall-price form

The maximum in (3.3) has a finite linear-programming dual.  Give every middle
vertex a free potential \(\pi_v\), every enforced q1 colour a nonnegative
price \(\lambda_c\), and every red or blue variable a nonnegative upper-bound
slack \(u_g\).  The dual constraints are

\[
\pi_x+\pi_y-\lambda_{\ell(f)}-\lambda_{u(f)}+u_f\ge0
\quad(f=xy\in A),
\tag{3.4}
\]

\[
-\pi_x-\pi_y+\lambda_{\ell(e)}+\lambda_{u(e)}+u_e
\ge w_\alpha(e)
\quad(e=xy\in B),
\tag{3.5}
\]

with objective

\[
\operatorname{cost}(\pi,\lambda,u)
=\sum_c s_c\lambda_c+sum_{g\in A\cup B}u_g.
\tag{3.6}
\]

Consequently any rational data satisfying (3.4)--(3.5) and

\[
\operatorname{cost}(\pi,\lambda,u)<\sum_M\alpha_M
\tag{3.7}
\]

is an independently checkable fractional Hall certificate.  Since all model
coefficients are integral, rational data may be cleared to an integer
certificate.  Equation (3.6) is a generalized min-cut: endpoint potentials
route degree balance, palette prices charge protected colours, and \(u_g\)
pays for saturated physical edges.  It is not in general an ordinary
single-source graph cut.

## 4. Fractional-versus-integral dichotomy

The frozen CP-SAT artifact does not reveal which of the following cases holds.

### Case F: LP infeasible

Then Theorem 3.1 supplies \(\alpha,\pi,\lambda,u\) satisfying (3.4)--(3.7).
The support of \(\alpha\) is a higher-order fractional Hall core.  It can be
made inclusion-minimal by guarding motif rows and deleting assumptions while
retaining LP infeasibility.  This yields a short, solver-independent theorem.

### Case I: LP feasible but the binary system infeasible

Then no nonnegative motif weighting can violate (3.3), and no Farkas
combination of the present linear rows proves UNSAT.  The obstruction is
integral: parity, an odd-set inequality, or a higher Chvatal--Gomory cut is
required.  An assumption core still identifies relevant motif rows, but it is
not a Hall cut until an integer certificate is supplied.

This dichotomy prevents an unjustified claim that every CP-SAT core is a
min-cut.  The LP status is the first missing bit.

## 5. Minimal guarded-core protocol

The exact next model should leave degree, q1, and bounds hard and guard only
the inherited motif rows:

\[
\sum_{e\in C_M\cap B}b_e\ge g_M,
\qquad g_M\in\{0,1\},
\]

with every \(g_M\) assumed true.  The proof-safe protocol is:

1. extract a sufficient assumption core \(S\subseteq\mathcal M\);
2. deletion-minimize \(S\);
3. solve the LP relaxation on \(S\);
4. in Case F, export a rational dual ray satisfying (3.4)--(3.7);
5. in Case I, export an odd-set/CG or complete branch certificate;
6. independently replay the final certificate from the frozen edge lists.

The present artifact has no assumptions and therefore cannot identify \(S\).

## 6. Exact implication for moving the resident endpoint

The UNSAT result is architecture-specific.  It rules out only switches inside
the fixed union \(Q\cup R\).  It does not rule out a different resident
factor \(R'\), an exterior edge, or a joint move of both endpoints.

Once a fractional certificate is known, however, it gives an exact exclusion
test for resident moves.  Keep \(Q\), \(\alpha\), \(\pi\), and \(\lambda\)
fixed and define

\[
c_R(xy)=\max\{0,\lambda_{\ell(xy)}+\lambda_{u(xy)}-\pi_x-\pi_y\},
\tag{6.1}
\]

\[
c_B(xy)=\max\{0,w_\alpha(xy)+\pi_x+\pi_y
 -\lambda_{\ell(xy)}-\lambda_{u(xy)}\}.
\tag{6.2}
\]

For any candidate resident factor \(R'\), put

\[
\mathcal C(R')=
\sum_c s_c\lambda_c
+\sum_{f\in R'\setminus Q}c_R(f)
+\sum_{e\in Q\setminus R'}c_B(e).
\tag{6.3}
\]

Equations (6.1)--(6.2) are the least edge slacks making the same dual
potentials feasible for the new overlay.  Therefore:

### Corollary 6.1 (resident exclusion by certificate price)

If

\[
\mathcal C(R')<\sum_M\alpha_M,
\tag{6.4}
\]

then the LP overlay for \((Q,R')\) is infeasible, hence the binary overlay is
infeasible.

Thus any successful resident move must cross the dual price threshold, or
invalidate the motif weighting by moving \(Q\).  This converts a future Hall
certificate into a quantitative resident-endpoint design constraint.

In Case I, only the weaker locality statement is presently valid: a resident
move that leaves the complete constraint submatrix of an independently
verified integer circuit unchanged cannot repair it.  Without the core, no
particular resident edge is yet proved necessary.

## 7. Sharp remaining boundary

What is proved here:

- the frozen model and result metadata match the exact fixed-overlay system;
- zero unit cores coexist with a reported full-model UNSAT;
- exact LP feasibility is equivalent to all weighted Hall inequalities
  (3.3);
- a fractional obstruction has the explicit dual price form (3.4)--(3.7);
- such a certificate quantitatively excludes resident endpoints by (6.3).

What remains open:

- an independently checkable core or proof of the frozen CP-SAT status;
- whether the obstruction is fractional or purely integral;
- the exact circuit support and exact deficiency \(\Delta_R(Q)\);
- a resident move crossing the eventual certificate support or price.

The smallest decisive computation is therefore not another local unit-core
beam.  It is a guarded motif-core extraction followed by one LP feasibility
test and certificate export.

## 8. Lightweight audit artifacts

Script:

```text
scratch/audit_k16_zero_unit_core_overlay_unsat_metadata_20260729.py
SHA-256 68dd876b04f36e075074834a58898eb13aa93ff46a83ec464b86cd2b1ad6248e
```

Output:

```text
scratch/k16_zero_unit_core_overlay_unsat_metadata_20260729.audit.json
SHA-256 554af332041a910f9598b2c3ff9fca553f0cec2a1387f7ffc68cb730b9496194
```
