# K16 H1 joint13: strongest audited closure package

Date: 2026-07-30  
Lane: AD  
Status: **exact on the frozen thirteen-cell support; feasibility UNKNOWN**

## 1. Scope

Fix the authenticated length-12,873 word

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
```

and permit arbitrary nonzero reassignment only at

```text
{0,1} | {4486,4487,4488,4489} | {6438,6439,6440} |
{12869,12870,12871,12872}.
```

The complement is frozen and there is no edit-cardinality budget.  Safe-gap
localization leaves 55 residual targets and 29 one-block interval charts per
target.  Every residual target contains coordinate 6.  Nothing below is a
normalization of an arbitrary length-12,873 word into this support.

This note synthesizes three independently audited exact reductions.  It does
not report or rely on any SAT-solver result.

## 2. Exact union-blocker theorem

Choose one chart \(\alpha_T=(T,b,I_T,N_T)\) for each residual target.  For a
noncommon coordinate \(q\), put

\[
 U_{b,q}=\bigcup_{T:b(T)=b,\ q\notin T}I_T.
\]

Then the frozen support is feasible if and only if

\[
 I_T\setminus U_{b(T),q}\ne\varnothing
 \qquad(T,\ q\in N_T\setminus\{6\}).                       \tag{2.1}
\]

Necessity follows because a cell supplying \(q\) to a literal \(T\)-witness
cannot lie in a selected witness of a target omitting \(q\).  Conversely,
assign each cell the intersection of all selected targets crossing it.
Condition (2.1) supplies every residual need, and common bit 6 makes every
nonempty intersection nonzero; an unused cell takes `0xffff`.

Equivalently, introduce existential supply bits \(X_{p,q}\).  A chart is
admissible exactly when it blocks \(X_{p,q}\) on its interval for every
\(q\notin T\), while every \(q\in N_T\setminus\{6\}\) is supplied somewhere
on that interval.  For a fixed local supply pattern \(X_b\), let
\(S_b(X_b)\) be the targets admitting a chart in block \(b\).  Feasibility is
exactly the four-way join

\[
 S_0(X_0)\cup S_1(X_1)\cup S_2(X_2)\cup S_3(X_3)=R.          \tag{2.2}
\]

Thus targets become independent once the four local supply patterns are
fixed; there is no cell-capacity constraint.

Every failed demand has an inclusion-minimal blocker cover of at most
\(|I_T|\le4\) selected charts.  Hence the chart-only master has 275 binary
code bits, 181 invalid-code rows, and an exact lazy separator returning one
no-good on at most five chart assignments, or at most 25 code literals.
The finite family of all such cuts is an exact projection; the 181-row
initial master alone is not a complete static CNF.

## 3. Exact meet/OR proxy theorem

Let \(\mathcal F\) be the meet closure of the 55 residual targets, including
the empty meet `0xffff`.  It has exactly 216 states.  For target \(T\) and
width \(w\), define

\[
 \mathcal U_w(T)=\left\{\bigvee_{j=1}^w(T\cap C_j):C_j\in\mathcal F\right\}.
\]

Every canonical selected-chart OR belongs to this family.  The family is a
safe independent-cell overapproximation and has at most 440 states here.

For chart need \(N\), let `Good` be the states containing \(N\), `Bad` the
others, and let \(E\) be the noncommon coordinates in the intersection of
all good states.  Choose a minimum-cardinality \(G\subseteq E\), breaking
ties lexicographically, such that every bad state omits at least one member
of \(G\).  Then, on all of
\(\mathcal U_w(T)\),

\[
                         N\subseteq V\iff G\subseteq V.       \tag{3.1}
\]

The forward implication uses \(G\subseteq\bigcap\mathrm{Good}\); the reverse
uses the bad-state hitting condition.  Proxy coordinates need not belong to
the formal need.

Across 445 distinct \((T,w,N)\) types, (3.1) reduces 10,301 durable rows to
5,465.  Exhaustive enumeration of 2,336 inclusion-minimal positive proxy
clauses proves that no nonsingleton positive clause saves another row or
literal in this chartwise independent-cell language.  The resulting durable
family is therefore clause-minimal in that explicitly stated language.

Availability `(flat=2, bit=8)` then has no durable occurrence.  Existentially
projecting its 51 forward definitions and one reverse definition gives the
exact canonical-occupancy projection

```text
1129 variables, 12670 clauses, 46661 literals.
```

The reverse canonical availability rows for the retained variables are
essential to this particular projection theorem.

## 4. Exact chart canonicalizations

For two supply predicates of the same target, strict implication occurs
exactly when the implied chart has common-bit-only need and its interval is
properly contained in the implying interval.  There are 30 ordered strict
implications and exactly 16 dominated charts.  Contracting them leaves 1,579
charts, an antichain under target-local single-chart implication.

A separate safe-follower rule applies when \(S\subsetneq T\) and
\(N(T,J)\subseteq N(S,J)\): conditional on selecting \(S\) on \(J\), target
\(T\) may select the same chart without changing any canonical cell or
destroying another witness.  A deterministic strict-containment forest has
36 edges and 150 triggers.  Its 358 implication clauses eliminate 4,200
local parent/child chart pairs (28 alternative child charts for each of 150
triggered parent charts) and give the optional model

```text
1129 variables, 13028 clauses, 47909 literals.
```

These follower clauses preserve existence by canonical representative
selection; unlike the primary projection, they do not preserve every
occupancy assignment.

## 5. Strongest composed static CNF

The supply-code and proxy reductions compose without reverse supply rows.
If \(X_{p,q}=1\), the omitter rows ensure that every selected target crossing
\(p\) contains \(q\), so the canonical cell contains \(q\).  Supplying every
proxy bit therefore puts \(G\) in the canonical chart OR, and (3.1) supplies
the full original need.  Conversely, a physical solution may set supplies
to its full canonical coordinate membership.

After the 16 chart contractions, this yields

```text
469 variables
28233 clauses
174662 literals
```

with exact clause ledger

```text
invalid chart codes              181
selected proxy supplies         5465
selected omitters block supply 22587.
```

The 469-variable model and the 1,129-variable projection are complementary
Pareto reductions: the former uses information-minimal five-bit indices in
the explicit one-codeword-per-chart representation, while the latter has
substantially fewer clauses and literals and retains exact canonical
availability equalities.  No lower bound for arbitrary extended
formulations is claimed.

## 6. Frozen artifacts

The primary theorem reports are

```text
MATH_THEOREM_AD_K16_H1_FOURPORTAL_SUPPLY_UNION_NORMAL_FORM_20260730.md
SHA-256 d166fb7ba04c8b9cf2ebec0d8e8b58085bb97c4a2f5f0957163b66e29e920f81

MATH_THEOREM_AD_K16_H1_JOINT13_PROXY_ORCLOSURE_AND_SAFE_FOLLOWERS_20260730.md
SHA-256 a0ef6dd0476df5760f705c0c35b93037b7f3cac7057a5976b5804423a37cb38f

MATH_THEOREM_AD_K16_H1_FOURPORTAL_PROXY_SUPPLY_COMPOSITION_20260730.md
SHA-256 813d5745c2aa3dcdf4eb9e9aa405b23bb67cd147ae15d2338f31075904fcb556
```

The current composed static low-variable model is

```text
scratch/build_ad_k16_h1_fourportal_joint13_proxy_supplycode_cnf_20260730.py
SHA-256 c1476781fd1fac7ef3b5960720a6bab3a47693ec5d5f6237fdee3c6201bc090a

scratch/ad_k16_h1_fourportal_joint13_proxy_supplycode_20260730/model.cnf
SHA-256 f03c8c3e38caf4d4f47bb7ae4569e07526afdd7689acc2c1b32b8dfd71ab488e

scratch/ad_k16_h1_fourportal_joint13_proxy_supplycode_20260730/model.map.json
SHA-256 f5f50ec0563adb1175500ef1426144f753dd72ed37f360f787ebb840feeb5ed8
payload SHA-256 7ff2f7a17a45b40360b7e29a004365b7f7031b169188cb58e85ddf2d1e6c8698

scratch/ad_k16_h1_fourportal_joint13_proxy_supplycode_20260730/model.independent_audit.json
SHA-256 331f1d7d56c18c6c639c8abf27b9e177c692a012b9a20e6878b4397efb025c76
payload SHA-256 72be9126c4233d3d18c3008a2751774c52db46410c9ba2aa599d2a6658b774f1

scratch/decode_verify_ad_k16_h1_fourportal_joint13_proxy_supplycode_20260730.py
SHA-256 cbb9e235d8e71b144caf3e69f659f40f3f3651b107366f652a342d35ef88ffe4

scratch/audit_ad_k16_h1_fourportal_joint13_proxy_supplycode_independent_20260730.py
SHA-256 3fb075e588405b8bf3d6a28f602c6b382400503548a7c17aef799ba8b1069ea1
```

The low-clause model and its audit are

```text
scratch/ad_k16_h1_joint13_proxyclosure_reduced_20260730/model.cnf
SHA-256 c59418fd0a01a9f5275c9c067c97d051b8ddc7bff02110e91b8c127cc8546683

scratch/ad_k16_h1_joint13_proxyclosure_reduced_20260730/model.independent_audit.json
SHA-256 d8c7d189daf2bd705c07873f40cd0c197e3a674f3159842d0c732b17f7e145f8
payload SHA-256 704166a9517cc6ddc6244c93123f9d7ec90899520a86a01596d511092c4e3dae
```

Both independent auditors reconstruct their complete ordered clause streams.
The composed audit was replayed separately and reproduced byte-for-byte.  A
fail-closed decoder checks a complete SAT assignment, every CNF clause, every
full original need, and all 65,535 literal targets before writing a word.

## 7. Exact boundary

No new model produced in this package was submitted to a solver, and the
pre-existing H100 run was not duplicated or touched.  These are exact support-restricted reductions,
not SAT or UNSAT certificates.  Their disposition is **UNSOLVED/UNKNOWN**.
They neither construct a length-12,873 word nor exclude edits outside the
thirteen cells.  The global bracket remains

\[
                         12873\le\nu(16)\le12874.
\]
