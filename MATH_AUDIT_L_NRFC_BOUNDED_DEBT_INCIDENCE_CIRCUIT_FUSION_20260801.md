# Independent audit: Lane-L NRFC bounded-debt incidence-circuit fusion

Date: 2026-08-01  
Audited file:
`MATH_THEOREM_L_NRFC_BOUNDED_DEBT_INCIDENCE_CIRCUIT_FUSION_20260801.md`  
Verdict: **PASS, conditional theorem with exact finite scope**.

## 1. Algebraic replay

Let `Delta_j=mu_j-mu_(j-1)`.  Direct summation gives

```text
mu_q=mu_0+sum_j Delta_j.
```

For every coordinate with `mu_0>=1`, terminal absence implies the summed
delta is at most `-1`.  Hence missing-colour count is at most the negative
`l_1` mass.  If `mu_0=1` pointwise, terminal nonnegative integrality makes
this an equality.  Lemma 1.1 is exact.

For a merge forest, expand every row

```text
Delta_j=pi(parent_j)-sum pi(children_j)+epsilon_j.
```

Every internal nonroot component has coefficient `+1-1=0`; leaves have
coefficient `-1`, roots coefficient `+1`.  This proves (2.2).  The negative
part obeys `(x+y)_-<=x_-+y_-` coordinatewise, so (2.3)--(2.4) have the
correct signs and constants.

For the port version,

```text
sum_j(phi(t_j)-phi(s_j))=sum_v d(v)phi(v).
```

Compatible-chain cancellation gives at most one end-minus-start term per
chain.  The two bounds

```text
K max_(x,y)||(phi(y)-phi(x))_-||_1,
P sum_v |d(v)|
```

are therefore both valid.  If there are `J` broken joins, at most `J+1`
open chains remain and `sum|d|<=2(J+1)`, proving the displayed coarse
constant.  Closed chains contribute zero.  The closed-walk criterion in
Proposition 3.2 is the standard path-independence proof for an exact
one-coboundary and is correct over the free abelian palette group.

## 2. Necessity checks

Proposition 4.1 conserves palette mass in every move:

```text
Delta_i=1_q-1_(t_i).
```

The final load of `q` is `c`, while `c-1` distinct targets disappear.  Each
edge admits a bounded endpoint potential, but the star has `c-1` unmatched
port chains.  Thus bounded per-edge debt, resource disjointness, a spanning
tree, and bounded endpoint vectors do not imply bounded terminal debt.

Proposition 4.2 is stronger in a different direction.  With baseline load
two on cyclic targets, each payload

```text
2 1_q-1_(t_i)-1_(t_(i+1))
```

has zero standalone coverage debt and conserves occurrence mass.  The full
packet deletes both providers of every `t_i`.  This validates the warning
that standalone palette-safe rows are not compositional.  The proposition
is explicitly an abstract transition-system counterexample, not a claimed
Boolean incidence construction.

The three independent quantitative hypotheses are real:

* unbounded port potential can encode linearly many distinct losses along
  one compatible path;
* bounded potentials with unbounded port divergence can encode them on a
  star;
* bounded residual on each edge can still have unbounded total residual.

## 3. Literal-scope audit

The theorem correctly requires statewise payloads.  Frozen deltas may be
added only for disjoint complete affected-centre closures or after a
context-independence proof.  It also requires the actual component merge
row before applying the cocycle.  A tight word-fibre cut with no live edge
is therefore not bypassed.

Corollary 2.2 retains the literal NRFC age-cell recurrence as a hypothesis.
It does not infer owner/flag colouring from rank counts.  Residence, q2,
deeper shadows, upper witnesses, and common cap remain outside unless put
into the hard circuit guards.  This is the correct implication direction.

## 4. Independent finite `k=17` replay

The finite calibration is bound to seed SHA

```text
a3f9eac037ae66a460349b12d578a31222afe1a7d168da641e77967a44ddbab3.
```

The C6 row is independently replayed in

```text
scratch/threadA_k17_complement_dual_age_local_replay_20260801/
  switch75_265_219.audit.json
SHA 7e180f3b5c1a5a13206916f98ce9f727d0d1085b2ece62a49aaf54f768ea4ec5.
```

It preserves both immediate quotient-q1 palettes but leaves physical
components `24293+17`.  Its full signed load delta is nonzero, so the note
correctly does not call it a zero-payload compositional macro.

The C12/C16 factor TSVs are independently reconstructed in

```text
scratch/k17_dual_splice_dev5_independent_20260801/
  independent_replay.audit.json
SHA 3edce35e7429b89255029b4a3c0fbc7bf78a6f24b4261cc20ebf50884152a437.
```

The replay verifies all selected incidences in all 17 phases, both perfect
matching rows, quotient and physical components, voltages, and immediate
rank-10/rank-7 load counters.

* C12 factor SHA
  `f1d21146512662a54ad0c3811b8a4c901e738c6e3e7c2f42e835017c662134c0`:
  `A` is one voltage-15 1430-cycle; the physical factor is two
  12155-cycles; holes are upper `0x03e4f` and lower `0x00d87`.
* C16 factor SHA
  `c082621d6444dc2283675882557d0240babb989f2d31847eb198fbe8b4612587`:
  one voltage-9 quotient cycle and one 24310-cycle physical lift; upper
  holes none; lower holes `0x00e0f,0x01547`.

These are missing quotient-colour orbits.  The finite audit supplies no q2,
deep-shadow, C12/C16 residence, common-cap, compiler, or all-parameter
potential certificate.  The note states exactly this scope.

## 5. Final verdict

The reusable result is the conditional bounded-root/compatible-port
telescoping theorem.  The exact missing all-parameter statement is a
prospectively selected NRFC-labelled circuit merge tree with one of those
cancellation structures and a bounded terminal repair bank.  The finite
C16 row proves only that connected debt two occurs in one authenticated
`k=17` catalogue.

