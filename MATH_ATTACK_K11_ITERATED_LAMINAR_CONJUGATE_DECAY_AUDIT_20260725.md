# Independent audit: K11 iterated laminar conjugate decay

Date: 2026-07-25

Audited file:

\[
\texttt{MATH\_ATTACK\_K11\_ITERATED\_LAMINAR\_CONJUGATE\_DECAY\_20260725.md}.
\]

Three independent audits were used:

1. a Catalan/TU/constants audit of Sections 1--3 and the added shifted-bit
   theorem;
2. a covariance, shielding, routing, and scope audit of Sections 4--8;
3. a full adversarial pass over all theorem statements and implication
   boundaries.

## Verdict

PASS after the corrections recorded below. No substantive mathematical
defect remains in the current report.

The unconditional output is:

* literal geometric exhaustion of the native atlas;
* one further literal shifted carrier bit;
* covariance and transported-cube normal form;
* exact shielding equivalence;
* an exact pathwise control-block loss theorem;
* an aligned-packet round lower bound.

The global \(o(W)\) endpoint remains conditional. The report does not claim
constant one.

---

## 1. Native Catalan and TU ledger

The exact ratio

\[
 \frac{C_{m-2}}{C_m}
 =\frac{m(m+1)}{4(2m-1)(2m-3)}
 \longrightarrow\frac1{16}
\]

is correct. Restricting a laminar cylinder family to \(Q_t\) preserves
laminarity. With the box constraints
\(x\in[0,1]^{Q_t}\), stacking the incidence matrix and its negative with
\(I,-I\) is totally unimodular. Thus the integral half-selection used in
Theorem 2.1 is valid.

The recurrence

\[
 |Q_{t+1}|\le\left\lceil|Q_t|/2\right\rceil
\]

gives

\[
 |Q_t|\le\left\lceil C_{m-2}/2^t\right\rceil.
\]

Pairwise disjoint invariant \(2n\)-root blocks prove exact persistence.
The ledgers

\[
 2C_{m-2}=\left(\frac18+o(1)\right)B
\]

and

\[
 (2n-4)C_{m-2}
 =\left(\frac18+o(1)\right)W
\]

have no missing factor two.

The tagged charge is

\[
 2\sum_{q=1}^{H}C_qC_{m-q-2}
 \le2C_{m-1},
\]

and

\[
 \frac{2C_{m-1}}W
 =\frac{m+1}{(2m-1)(2m+1)}
 =o(1).
\]

The terminal all-one native signing is not a cumulative discrepancy-one
signing; the report states this correctly.

Each native aligned packet has two positive first-shadow cells, so native
exhaustion fills at most \(2C_{m-2}=o(W)\) holes. This does not depend on
the order of the native switches.

---

## 2. The shifted first-bit theorem

For

\[
 s=\left\lceil3H/4\right\rceil,\qquad
 M_s=m-s-2,
\]

the hypothesis \(H\ge3\) ensures \(s\ge3\). This condition is essential:
for \(s=1,2\), shifted rows can fall back into the native initial-run
classes.

For \(s\ge3\), shifted indices begin with \(111\), while native packet rows
begin with \(1100\) or \(1010\). The row families are disjoint in the exact
factor; their invariant ownership blocks are therefore root-disjoint.
Every shifted \(\tau_s\)-cell survives any native preparation verbatim.

The shifted suffix cylinders are laminar. The common TU half-selection gives
tagged loads

\[
 \left\{\left\lfloor C_q/2\right\rfloor,
 \left\lceil C_q/2\right\rceil\right\}
\]

for every displayed \(q,V\), and the full-atlas constraint switches
\(C_{M_s}+O(1)\) rows.

For both parities of \(C\),

\[
 \binom{\lfloor C/2\rfloor}{2}
 +\binom{\lceil C/2\rceil}{2}
 =\left\lfloor\frac{(C-1)^2}{4}\right\rfloor
 \le\frac12\binom C2.
\]

Thus Theorem 2.2 is exact. Its scope is one surviving menu bit; it proves no
second noncommuting bit.

---

## 3. Hereditary clean-cover theorem

The stopping threshold \(r_\star\) is necessary: a two-row atlas cannot
cover a one-row residual. The current definition quantifies over every
admissibly reachable pair \((F,R)\) above \(r_\star\), avoiding both the
singleton obstruction and a circular schedule quantifier.

Disjoint \(2n\)-root blocks imply that at most \(B/2\) cells are ever
selected. Hence

\[
 \text{switched rows}\le B,\qquad
 \text{tagged charge}\le HB=\frac HnW.
\]

For \(H\le A\sqrt m+1\), this is \(O_A(W/\sqrt m)=o(W)\).

The density

\[
 p_m=\frac{2\lfloor C_{m-2}/2\rfloor}{C_m}
 \longrightarrow\frac1{16}
\]

satisfies \(p_m\ge1/17\) eventually. Therefore

\[
 (1-1/17)^{\lceil17\log m\rceil}\le m^{-1},
\]

which gives \(B/m\) residual rows and \(W/m\) residual roots under the
stated hereditary hypothesis.

This theorem controls middle-owner and source-tag mass. It does not control
untagged collateral action and does not by itself imply \(J_A=o(W)\).

---

## 4. Covariance and static renewal ceiling

The covariance identity

\[
 \mathcal P_{g\sigma g^{-1}}(gF)
 =g\mathcal P_\sigma(F)
\]

is exact. It transports the atlas and residual set together, so relative
whole-cell coverage is unchanged.

Under the deliberately restricted operation set of global relabellings plus
transported native toggles, induction gives the normal form

\[
 gF_\varepsilon.
\]

This says nothing about genuinely recomputed components in a mixed factor,
as the report notes.

The admissible residual retaining one row of each native cell and every
background row has

\[
 W-nC_{m-2}
 =\left(\frac{15}{16}+o(1)\right)W
\]

roots but contains no complete native cell. This is a valid whole-row
counterexample to a bare density-to-cell-containment inference.

The static contextual matching constants

\[
 \nu(\mathfrak M_m)
 =\left(\frac{11}{72}+o(1)\right)B,
\]

\[
 2\nu
 =\left(\frac{11}{36}+o(1)\right)B
\]

are correctly scoped to transported static cells.

---

## 5. Shielding and seams

For a fixed union \(Z\) of row-root blocks and one colour \(\sigma\), the
following equivalence is sound:

\[
 \text{componentwise }Z/Z^c\text{ separation}
 \iff \text{no crossing owner edge}
 \iff \sigma Z=Z.
\]

Equivalently, the rowwise prescription fixing \(Z\) and conjugating all of
\(Z^c\) is constant on complete components exactly under this invariant.

A seam crossing \(Z,Z^c\) therefore obstructs either nonconstant global
indicator orientation. It does not necessarily obstruct a packet-only bit
when the outside endpoint is unconstrained.

If one fixed \(Z\) is invariant under every generator of an
\(S_n\)-generating menu, transitivity on
\(\binom{[n]}m\) forces \(Z\) to be empty or full. This does not cover a
dynamic \(Z\), a proper subword, a subgroup, or setwise motion of frozen
rows.

With nonzero boundary one may still switch pure-\(Z^c\) components while
keeping mixed components old. The theorem obstructs conjugating all of
\(Z^c\), not partial progress.

---

## 6. Control blocks and geometric routed survival

The block-uniform policy has exact loss

\[
 L_t=
 \sum_{Q\ {\rm unforced}}\min\{n_0(Q),n_1(Q)\}
 +\sum_{Q\ {\rm forced}}n_1(Q).
\]

All quantities must be recomputed on the current survivor set after every
actual fresh cut. Under that pathwise quantifier,

\[
 N_t=N_{t-1}-L_t
\]

is exact.

Forcing a discarded packet's two current rows to zero for the remainder of
the route word preserves its coherence. Retrying it later is conditional on
its being a legal current candidate and on including every accumulated
forced row.

The connector example only shows that block-uniform routing is nonoptimal
when failed connectors may be sacrificed permanently. It does not refute
the retryable-coherence policy.

For pairwise row-disjoint candidates wholly inside the unresolved row set,
a \(p\)-fraction candidate cover and \(\gamma\)-fraction route survival
give

\[
 |R_r|_{\rm row}\le(1-p\gamma)^rB.
\]

With \(p\ge1/17\) and \(\gamma\ge1/16\), the constant is

\[
 p\gamma\ge1/272,
\]

so \(\lceil272\log m\rceil\) rounds leave at most \(B/m\) rows.

The seam-loss estimate

\[
 L_t\ge s/(2n)
\]

is correct only for distinct unordered seams of one colour whose two
endpoints are active packet cells and which cross the current route bit.
K10's aggregate seam theorem does not verify those hypotheses.

---

## 7. Local-round speed limit

The round lower bound is valid for aligned first-shadow trades having
exactly two positive cells:

\[
 M_1(F_{t-1})-M_1(F_t)\le2r_t,\qquad
 r_t\le B/2.
\]

Thus

\[
 M_1(F_0)-M_1(F_T)\le BT,
\]

and a fixed \(\delta W\) defect followed by an \(o(W)\) endpoint forces

\[
 T\ge(\delta-o(1))n.
\]

This does not cover nonlocal components or high-footprint two-row
components. The report now states that exact scope.

---

## 8. Final implication scope

The report proves two conditional decay mechanisms:

* direct hereditary current-cell renewal, with \(17\log m\) rounds;
* candidate cover plus routed survival, with rate \(1-p\gamma\).

Neither is supplied by K10's seam count. Source-tag decay also does not
control collateral untagged rows.

A final conclusion \(J_A=o(W)\) requires a separate fresh overlay satisfying
K10's charged common-TU/off-residue hypotheses. If earlier routed rows must
remain fixed through that last signing, the common-TU system must include
their forced-zero constraints.

Therefore the precise surviving gate is hereditary fresh-component
regeneration with pathwise control-block survival and cumulatively
\(o(W)\) collateral charge, followed by the charged common-TU feasibility.
No unconditional constant-one conclusion is asserted.
