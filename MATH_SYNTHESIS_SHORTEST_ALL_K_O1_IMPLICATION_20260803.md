# Shortest honest all-dimensional implication for `B(k)+O(1)`

**Date:** 2026-08-03  
**Status:** synthesis and conditional implication only.  The correlated
construction theorem isolated below is **not proved**.  Consequently this
note proves no new upper bound for `nu(k)`.

## 0. Verdict

The newest results separate into three logically different classes.

1. **Necessary shadows.**  They constrain every near-optimal word, but do
   not construct one.
2. **Exact transfer theorems.**  They turn one fully materialized literal
   certificate into a bounded-defect compiler, but do not materialize the
   certificate.
3. **Abstract positive existence.**  The required immediate-upper palette
   exists and is reachable in its row-margin fibre, but its occurrence-level
   realization is still open.

After making that separation, the shortest current implication is

```text
one compatible protected dense-diagonal spine
  + one-copy Ferrers/background physicalization
  + one same-state two-coordinate bounded-overload compiler
  + literal odd regeneration and even taps
  -> uniformly bounded terminal target set
  -> nu(k) <= B(k) + O(1).
```

The single missing statement is the existence of the object on the first
four lines with every persistent choice coinstantiated in one auxiliary
state and every dimension-specific terminal certificate internally
materialized.  Separate existence of its rows is not enough; the odd
transition, odd terminal, and adjacent even tap are not literally one word.

## 1. Necessary results: what an additive word would force

Put

\[
 r=\left\lceil{k\over2}\right\rceil,
 \qquad W={k\choose r},
 \qquad
 \Lambda=\sum_{s=1}^{r-1}{k\choose s},
\]

and let `d=d(k)` be least with

\[
 dW+{d+1\choose2}\ge\Lambda,
 \qquad B(k)=W+d.
\]

### 1.1 Architecture-free unit vacancy

Every universal word of length `W+e` partitions the strict lower ideal into
`W+e` literal endpoint chains, each of size at most `e`.  If `e=d+C`, the
total vacancy in those chains is

\[
 V_C=(dW-\Lambda)+CW+(d+C)^2
      <(C+1)W+O_C(k).
\]

Thus `B(k)+C` forces bounded average vacancy at unit-chain scale.  This is
architecture-free, but the chains are not anchored at the `W` middle
owners and need not obey one sliding suffix cocycle.

### 1.2 The dense Ferrers projection

On the cyclic depth-`d` dense-factor face, let `gamma_d(k)` be the minimum
number of strict-lower targets deleted so that the rest partitions into `W`
owner-anchored chains of size at most `d`.  For even `k`, complementation
identifies this exactly with deletion from the truncated upper half into
`W` chains of size at most `d+1`, one middle set per chain.

Its fractional relaxation is completely solved:

\[
 \gamma_d^*(k)=(\Lambda-dW)_+.
\]

If a literal dense factor misses `c` named targets and its triangular
boundary represents at most `b_partial` targets, then

\[
 \gamma_d(k)\le c+b_{\partial}.
\]

Since `b_partial=O(d^2)=O(k)=o(W)`, even an `o(W)` dense named-target
rounding would prove `gamma_d(k)=o(W)`.  This is a necessary projection of
that architecture, not a sufficient physical construction: after static
chainization, the sliding Ferrers cocycle and simultaneous interval closure
remain.

### 1.3 Why a generic nibble is not the missing proof

For the symmetric owner-plus-flag atom law, all codegrees are known exactly.
Any `o(W)`-defect law lies on the critical surface

\[
 \rho_2\ge{1-o(1)\over r},
 \qquad K=\Omega(\sqrt r),
 \qquad K^2\rho_2\ge{\pi\over4}-o(1).
\]

Therefore the standard growing-uniformity nibble hypotheses do not apply.
This is not a nonexistence theorem.  It says that the first open lower row
requires Boolean flag switching/absorption at unit-chain precision, rather
than black-box degree-codegree rounding.

These three results are diagnostic and necessary.  None points in the
upper-bound direction by itself.

## 2. Sufficient transfer results that are genuinely closed

### 2.1 Abstract protected Catalan target

For every `m>=3`, there is a simple family `D` of `Cat_m` rank-`(m+1)`
colours with coordinate degree `2 Cat_(m-1)`.  It can avoid any protected
colour bank of size `<(m-1)/2`.  Hence

\[
                    1+\mathbf 1_D
\]

is a cap-two, upper-surjective palette with exactly the current of two
edge-disjoint middle-levels matchings.  Abstract Ryser switches reach this
target while fixing all protected occurrence rows when their colours are
pairwise distinct and the resulting distinct protected-colour bank has size
`<(m-1)/2`.

What is closed is the **target palette and row-margin transport**.  A
literal colour-tail-head selector, Boolean `C6` realization of the Ryser
path, and neutral `C8` component tree are not supplied.

### 2.2 Literal diagonal `q1` routing

For a cyclic flat factor with

\[
 T_i=\bigcup_{h=i}^{i+d}A_h,
 \qquad
 P_i=\bigcup_{h=i+1}^{i+d}A_h=T_i\cap T_{i+1},
\]

where the `T_i` and `P_i` enumerate their two middle-level shores, the
literal routes

\[
 P_i\xrightarrow{A_i}T_i,
 \qquad
 P_i\xrightarrow{A_{i+d+1}}T_{i+1}
\]

form an addressed spanning two-factor.  Either orientation is an explicit
pairwise-disjoint full linkage after one compatible unused terminal socket
is attached to each owner occurrence; the union of both orientations has
zero normalized raw overload.

Thus the chronological occurrence map, semantic prefix identities, and
degree-two route packing are closed **once the q1-exact row and compatible
unused sockets exist**.  The theorem does not create those sockets and does
not infer q1 exactness from flatness.

### 2.3 Terminal Rado and overload algebra

After one complete cap/guard/occurrence state, transported background, and
cross-coordinate capacity allocation are fixed, the two occurrence
coordinates give Rado matroids `R_0,R_1` on the common logical ticket set.
Under global product closure, their exact common deficiency is

\[
 \delta=
 \max_{J_0\cap J_1=\varnothing}
 \left(
 |J_0|-r_{N_0}(A_0(J_0))
 +|J_1|-r_{N_1}(A_1(J_1))
 \right).
\]

Structural zeros separate exactly.  Hence background omission `beta`,
structural-zero set `Z`, and coordinate defects `k_0,k_1` give

\[
              \delta_{\rm total}\le
              \beta+|Z|+k_0+k_1.                 \tag{2.1}
\]

The physical suffix certificate can be strictly weaker than a preselected
disjoint router.  For an endpoint-balanced path pseudoflow,

\[
 N-r_\Gamma(P)
 \le\lfloor\Omega_{\rm cut}\rfloor
 \le\lfloor\Omega_{\rm tot}\rfloor .             \tag{2.2}
\]

For a balanced degree-`h` addressed semantic factor with raw path
multiplicities `ell(a)`, it is enough that

\[
 k_p\le
 \left\lfloor {1\over h}
   \sum_a(\ell(a)-h c(a))_+\right\rfloor .          \tag{2.3}
\]

Endpoint-star locality makes (2.3) zero.  The diagonal `q1` theorem is the
canonical `h=2`, zero-overload realization after its sockets are supplied.

Equations (2.1)--(2.3) close the **transfer algebra**.  They do not produce
the occurrence menus, cap, sockets, transported phase, or product closure.

### 2.4 Terminal repair and spine implication

A literal scaffold of length `B(k)+c` missing a set `H` becomes universal
after appending a repair word of length at most `|H|`.  One compatible odd
spine with even terminal taps and uniformly bounded total terminal charge
therefore implies `nu(k)<=B(k)+O(1)`.  The charge is paid only at the
requested terminal dimension; it is not exported down the spine.

This implication and its quantifier order are closed.  Existence of the
spine is not.

## 3. One minimal correlated construction theorem

The following statement packages exactly the rows which still have to be
coinstantiated.  It is weaker than a left-total induction theorem: one
selected infinite spine suffices.

### Protected dense-diagonal spine theorem `PDDS(C)`

There exist `m_0`, an absolute constant `C`, and one compatible sequence of
odd auxiliary states `g_m` with even terminal taps such that, for every
`m>=m_0`:

* there is one dimension-appropriate odd transition `g_m -> g_(m+1)`;
* there is an odd terminalization of `g_m` in dimension `2m+1`; and
* there is an even terminalization of `g_m` in dimension `2m+2`.

Every persistent choice shared by two of these certificates is fixed in
`g_m` or bundled into their common transition datum.  Each terminal
certificate has one internally consistent materialization in its own
dimension; the three certificates are not asserted to be the same literal
word.  They satisfy the following.

1. **One-copy protected owner chronologies.**  Every odd/even terminal
   branch has a dimension-appropriate literal scaffold of true excess at
   most `C` over its own `B(k)`, using every required middle owner once and
   covering every upper target with the required residence/envelope and
   protected export rows.  On the **odd equal-shore branch**, its
   chronological `q1` row is exact and occurrence-labelled, and its
   immediate-upper palette is a simple protected-avoiding `1+1_D` Catalan
   target realized by actual colour-tail-head occurrences; the protected
   colours are pairwise distinct and their bank has size `<(m-1)/2`.  Its
   owner graph has one legal opening/component.  On the **even branch**,
   PDDS assumes the corresponding dimension-appropriate literal
   owner/upper chronology and legal opening directly; it does not attribute
   the odd equal-shore q1/Catalan form to the closed diagonal or Catalan
   theorems.

2. **One-copy lower physicalization.**  On the odd dense-diagonal branch,
   the cyclic Ferrers cells and exact triangular boundary cells carry one
   common literal candidate incidence system for every strict-lower named
   target.  Every admitted cell obeys the sliding suffix cocycle and
   simultaneous coordinate interval closure.  The actual injective
   target-to-cell selection is part of Row 3; after that selection, grouping
   its cyclic cells by endpoint gives the required integral owner-chain
   atoms.  Each even terminal instead supplies its own dimension-appropriate
   literal lower candidate system and actual interval cells under Row 3; no
   odd Ferrers normal form is inferred for it.  In every branch no
   target/rank-marginal convex combination or repeated-owner circulation is
   used.

3. **One common occurrence compiler.**  In one fixed cap state, use one
   common logical ticket ground set and one declared target/background
   partition.  Choose explicitly either frozen private background routes or
   the adaptive-contraction model in each coordinate.  After one fixed
   compensation/background choice, every remaining logical ticket has its
   complete physical menu in both occurrence coordinates.  The balanced
   claim-to-port factors have edge-private, port-complete,
   capacity-faithful prefixes whose interiors are disjoint from the suffix
   network and the frozen compensation capacities (or the construction
   proves the direct all-subset Rado ranks instead).  All shared capacities
   are allocated, every terminal is typed, and global product closure holds.
   Define `k_p` either by the actual all-subset rank bound
   `r_(N_p)(A_p(J))>=|J|-k_p` for every ticket subset `J`, or by a literal
   endpoint-balanced pseudoflow whose normalized cut-overload theorem proves
   that bound.  The complete exceptional charge obeys

   \[
        \beta+|Z|+k_0+k_1\le C.                    \tag{3.1}
   \]

   In the literal diagonal subcase, it is enough to attach one compatible
   unused socket per routed owner in each occurrence coordinate, which gives
   `k_0=k_1=0`.

4. **Literal regeneration.**  The odd transition exports the next odd
   auxiliary state with every declared boundary, occurrence, history,
   residence, provider, and compiler coordinate revalidated.  The even tap
   and both terminal certificates have both true scaffold excess at most
   `C` and exceptional bound (3.1).  Terminal omissions and repair cells are
   not exported as fresh debt.

Then

\[
                         \boxed{\nu(k)\le B(k)+O(1)}.
\]

### Proof of the conditional implication

Row 1 supplies all middle and upper targets and the legal physical
chronology.  Rows 2 and 3 give one lower target-cell compiler.  More
precisely, (2.2)--(2.3) bound the two marginal suffix coranks by `k_0,k_1`,
and the two-coordinate Rado theorem plus product closure bounds the complete
lower/terminal omission set by (3.1).  Therefore each terminal scaffold has
length at most `B(k)+C` before repair and misses at most `C` named targets.
Appending those masks gives length at most `B(k)+2C`.

Row 4 makes the odd certificates one compatible infinite spine and supplies
the adjacent even dimensions.  The finitely many smaller dimensions are
absorbed by enlarging the constant.  This proves the displayed conditional
conclusion.  `square`

The two occurrences of `C` in the coarse bound are intentionally not
optimized; `PDDS(C)` is an additive-constant theorem, not a proposed sharp
coefficient.

## 4. Exact open rows after the synthesis

The conjecture is therefore not waiting on another scalar inequality.  The
remaining rows are:

1. **Critical integral lower rounding.**  Prove a Boolean-specific
   owner-flag matching with static leave at most the triangular
   `O(d^2)` boundary plus `O(1)` terminal targets, then lift it to the
   sliding Ferrers cocycle and simultaneous interval closure.  Even the
   weaker `o(W)` static leave is presently open.  The fractional SDR,
   fractional chain atoms, and stationary pull clock do not do this.
2. **Occurrence-level owner selector and topology.**  Realize the simple
   Catalan target by one cap-two colour-tail-head selector, literal protected
   `C6` switches, and a compatible neutral `C8` tree/opening, while retaining
   the all-width upper deck and residence.  Row-fixed Ryser is only the
   abstract matrix path.
3. **Same-state sockets and product closure.**  Materialize the two
   occurrence-coordinate port systems after compensation with either the
   diagonal unused-socket injection or bounded normalized overload.  Bound
   structural zeros and background loss, authenticate transported phase 1,
   and prove global product closure.  An abstract two-factor plus a matching
   cannot imply this row.
4. **Regeneration.**  Export the accepted child as the next admissible odd
   state with fresh child-local occurrence catalogues and provide both parity
   taps.  Per-dimension marginal existence or `O(1)` fresh loss per step is
   insufficient.

These four rows must be solved together because the lower chains determine
physical cells, the owner selector determines occurrence addresses, the cap
determines which sockets survive, and regeneration determines which of
those choices remain legal in the next dimension.

## 5. Closed-versus-open ledger

| Item | Exact status |
|---|---|
| Architecture-free endpoint-chain vacancy | **Closed necessary theorem**; no upper construction |
| Dense `gamma_d` complement reduction | **Closed necessary projection** on the dense face |
| Fractional owner-chain optimum | **Closed**; integral named-target rounding open |
| Critical flag codegree calculation | **Closed obstruction to black-box nibble**; no nonexistence claim |
| Simple protected Catalan duplicate target | **Closed abstract existence** |
| Row-fixed Ryser transport | **Closed abstract transport**; literal `C6` lift open |
| Diagonal `q1` incidence and two routing phases | **Closed conditional literal theorem**; q1 row and unused sockets open |
| Two-coordinate Rado/Edmonds formula | **Closed exact transfer theorem**; occurrence lift/product closure open |
| Private-router and overload bounds | **Closed exact transfer theorems**; bounded-overload catalogue open |
| Terminal repair and bounded-charge-spine implication | **Closed**; compatible spine existence open |
| `nu(k)<=B(k)+O(1)` | **Open** |

## 6. Authoritative inputs

- `MATH_THEOREM_ARCHITECTURE_FREE_ENDPOINT_CHAIN_UNIT_SLACK_20260803.md`
- `MATH_THEOREM_DENSE_FERRERS_UNIT_SCALE_CHAIN_DELETION_BARRIER_20260803.md`
- `MATH_THEOREM_FRACTIONAL_CHAIN_ATOM_CODEGREES_AND_CRITICAL_NIBBLE_BARRIER_20260803.md`
- `MATH_THEOREM_PROTECTED_SIMPLE_CATALAN_TARGET_AND_ROW_FIXED_RYSER_20260803.md`
- `MATH_THEOREM_DIAGONAL_Q1_LITERAL_TWO_FACTOR_ROUTER_20260803.md`
- `MATH_THEOREM_TERMINAL_COMMON_CAP_TWO_CROSS_RAY_RADO_GAMMOID_V2_20260803.md`
- `MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md`
- `MATH_THEOREM_BOOLEAN_INCIDENCE_OVERLOAD_SUFFIX_ROUTER_20260803.md`
- `MATH_THEOREM_UNIFORM_COINSTANTIATED_BOUNDED_CHARGE_RESET_SPINE_REDUCTION_20260803.md`

The unversioned first common-cap draft is formatting-failed lineage and must
not be cited.
