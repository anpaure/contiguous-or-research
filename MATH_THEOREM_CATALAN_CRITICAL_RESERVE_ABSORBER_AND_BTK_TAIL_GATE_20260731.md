# Critical reserve absorption, a Boolean path absorber, and the BTK fixed-tail gate

Date: 2026-07-31  
Status: exact parameter audit, general single-pair absorber theorem, exact
cap-two Hall reduction, and solver-free `m=3` BTK fixed-tail no-go; no
all-`m` Catalan matching theorem is claimed

## 0. Verdict

The modern conflict-free matching theorems do not directly prove the
ordered-diamond matching needed here.

* In the Joos--Mubayi--Smith tripartite theorem, the required size and
  codegree exponents are mutually incompatible with the Boolean diamond
  hypergraph: the size bound forces `epsilon >= 2^(-1/3)+o(1)`, while the
  actual codegree forces `epsilon <= 1/2+o(1)`.
* In the Delcourt--Postle bipartite theorem, retaining the upper colour as
  a resource gives no degree surplus at all.  Hiding it as a conflict gives
  exactly the critical relative surplus `1/m=D^(-1/2)`, below the theorem's
  guaranteed surplus scale, and creates upper-colour conflict cliques whose
  common 2-degree is `Theta(D)`, violating every `D^(1-beta)` hypothesis.

There is nevertheless a genuine Boolean absorber.  For every lower set
`L` and every upper set `U`, whether or not `L subset U`, an explicit
alternating inclusion path of length at most `2m-1` has two states:

1. an off state covering all internal outer vertices; and
2. an on state covering the same internal vertices plus `L` and `U`.

Both states lift to pairwise middle-disjoint Johnson edges.  Thus local
outer absorption is not the missing idea.  The exact remaining theorem is
to pack a robust, resource-disjoint family of these absorbers at the
critical reserve scale and couple it to an almost-perfect outer matching;
after that, physical cycles must still be excluded or switched away.

A separate audit closes the most literal BTK rethread.  Fixing the
one-step BTK successor as the tail map and changing only the second added
coordinate is already impossible at `m=3`: all 120 upper bijections have at
most 14 distinct heads instead of the required 15.  It is also SAT-UNSAT at
`m=4,5` in the retained exact CNF model.  Consequently, an SCD rethread must
change tails as well as heads; excursion rotations confined to the head
fibres cannot be a uniform construction.

## 1. The critical three-resource formulation

Put

\[
 {\cal L}=\binom{[2m]}{m-1},\quad
 {\cal X}=\binom{[2m]}m,\quad
 {\cal U}=\binom{[2m]}{m+1},
\]

and let an ordered diamond be

\[
                  (L,U,T,H),\qquad
 L=T\cap H,\quad U=T\cup H.
\]

Suppress the upper resource `U` temporarily and regard the atoms as a
three-uniform bipartite hypergraph

\[
              G_m\subseteq {\cal L}\times{\cal X}_T\times{\cal X}_H,
\]

coloured by `U`.  The exact parameters are

\[
 \deg(L)=m(m+1),\qquad
 \deg(T)=\deg(H)=m^2,qquad
 \Delta_2(G_m)=m.                                  \tag{1.1}
\]

An `cal L`-perfect matching with distinct upper colours is an ordered
four-transversal except that its directed physical partial permutation may
contain cycles.  Because it has

\[
 N=|{\cal L}|=|{\cal U}|
\]

edges, distinct upper colours automatically mean every upper colour occurs
once.

Writing `D=m^2`, (1.1) has the exact critical form

\[
     \deg({\cal L})=(1+D^{-1/2})D,qquad
     \Delta({\cal X}_T\cup{\cal X}_H)=D,qquad
     \Delta_2=D^{1/2}.                              \tag{1.2}
\]

This is the reserve scale which a general theorem would have to reach.

## 2. Why the published black boxes stop short

### 2.1 Delcourt--Postle

Theorem 2.6 of Delcourt--Postle, *Finding an almost perfect matching in a
hypergraph avoiding forbidden submatchings* (arXiv:2204.08981), gives an
`A`-perfect matching when

\[
 d_A\ge(1+D^{-\alpha})D,\qquad d_B\le D,qquad
 \Delta_2\le D^{1-\beta},                           \tag{2.1}
\]

for constants supplied by the theorem.

There are two natural encodings, and neither meets the theorem.

1. Keep `U,T,H` as the `B`-resources.  Then the maximum `B` degree is the
   upper degree `m(m+1)`, exactly equal to the `A=cal L` degree.  The strict
   surplus in (2.1) is zero.
2. Keep only `T,H` as resources and encode repeated `U` as pair conflicts.
   Now (1.2) gives only relative surplus `D^(-1/2)`.  More decisively, one
   upper fibre is a conflict clique of order `Theta(D)`.  Two physically
   disjoint atoms in that fibre have `Theta(D)` common conflict neighbours,
   whereas Theorem 1.16 requires maximum common 2-degree at most
   `D^(1-beta)` for some `beta>0`.

The sparsification proof of Theorem 1.16 also makes the exponent mismatch
visible.  It samples at `p=D^(beta/(4g)-1)` and then invokes the logarithmic
codegree theorem with exponent `1/(20r)`, yielding a guaranteed surplus
exponent no larger than `beta/(80rg)`.  Here `r=3`, pair conflicts have
`g=2`, and (1.1) requires `beta<=1/2`; this is far below the exponent
`1/2` needed to accept the Boolean surplus.

Thus Delcourt--Postle motivates the correct reserve architecture but cannot
be cited as proving this critical instance.

### 2.2 Joos--Mubayi--Smith

Theorem 1.1 of Joos--Mubayi--Smith, *Conflict-free Hypergraph Matchings and
Coverings* (arXiv:2407.18144), can finish a `P`-perfect matching without the
Delcourt--Postle surplus, but its almost-regular first-stage hypergraph has
the simultaneous hypotheses

\[
       n\le \exp(d^{\varepsilon^3}),qquad
       \Delta_2\le d^{1-\varepsilon}.               \tag{2.2}
\]

For the full ordered-diamond hypergraph take `P=cal L` and
`Q=cal U union cal X_T union cal X_H`.  Then

\[
 d=m(m+1)=\Theta(m^2),\qquad
 \log n=\Theta(m)=\Theta(d^{1/2}),\qquad
 \Delta_2=m=\Theta(d^{1/2}).                        \tag{2.3}
\]

The size hypothesis in (2.2) forces

\[
                       \varepsilon^3\ge1/2-o(1),
\]

whereas its codegree hypothesis forces

\[
                       \varepsilon\le1/2+o(1).
\]

Since `2^(-1/3)>1/2`, no `epsilon` satisfies both for large `m`, even if
one ignores the theorem's additional small-`epsilon` restriction and the
second-stage reserve conditions.  Hence this theorem also cannot be cited
for the Boolean diamond family.

## 3. An explicit Boolean absorber for one outer pair

The failure of the black boxes is not a failure of local absorption.

### Theorem 3.1 (single-pair alternating-path absorber)

For every

\[
                 L\in\binom{[2m]}{m-1},\qquad
                 U\in\binom{[2m]}{m+1},
\]

there is an alternating path in the inclusion graph

\[
 L=L_0,U_0,L_1,U_1,\ldots,U_{s-1},L_s,U,             \tag{3.1}
\]

where `s=|L-U|<=m-1`, with the following properties.

* The odd-edge state

  \[
                 M^- =\{L_{i+1}U_i:0\le i<s\}
  \]

  covers every internal outer vertex and neither endpoint `L,U`.
* The even-edge state

  \[
       M^+=\{L_iU_i:0\le i<s\}\cup\{L_sU\}
  \]

  covers every internal outer vertex and both endpoints.
* In either state, the Boolean diamonds lift to pairwise vertex-disjoint
  Johnson edges.  In particular both ordered states are tail-injective,
  head-injective and acyclic.

The gadget has at most `m` atoms in either state and at most `2m-1` edges in
its alternating support path.

#### Proof

Write

\[
 A=L\setminus U=\{a_1,\ldots,a_s\},\qquad
 U\setminus L=\{b_1,\ldots,b_s,c,d\}.
\]

Set

\[
 L_i=L-\{a_1,\ldots,a_i\}+\{b_1,\ldots,b_i\}
\]

and

\[
                        U_i=L_i\cup L_{i+1}\cup\{c\}.
\]

Then every displayed containment in (3.1) is valid, the internal vertices
are distinct, and `L_s=U-{c,d}`.

For the edge `L_i U_i`, its two middle vertices are

\[
 Z_i=L_i\cup\{b_{i+1}\}=L_i\cup L_{i+1},\qquad
 C_i=L_i\cup\{c\}.
\]

For `L_{i+1}U_i` they are `Z_i` and `C_{i+1}`.  The final edge `L_sU` has
middle vertices `C_s` and `D_s=L_s+d`.

All `Z_i` omit both `c,d`; all `C_i` contain `c` and omit `d`; and `D_s`
contains `d` and omits `c`.  Within each family the sets are distinct.
Therefore every middle vertex in each state is distinct, proving all three
claims. \(\square\)

There are many schedules for the same pair: one may order the `a_i`, order
the chosen `b_i`, and choose the ordered held-out pair `(c,d)`.  This is the
local entropy needed by a reserve construction.

## 4. The exact robust absorber statement still missing

Theorem 3.1 reduces exact outer completion to a packing problem rather than
an invention problem.  A sufficient all-`m` reserve theorem is the
following.

> **Boolean robust reserve-packing theorem.**  There is a sparse endpoint
> template and a resource-disjoint embedding of the absorbers in Theorem
> 3.1 such that, after installing all off states, every equal pair of outer
> leftover sets of the declared reserve size can be covered by switching a
> disjoint subfamily to their on states.  The unused bulk atoms admit an
> almost-perfect matching whose entire outer leave lies in that template,
> and the combined directed physical graph is acyclic (or admits
> outer-colour-preserving cycle switches).

The local theorem proves every template edge is individually embeddable.
What remains is simultaneous resource-disjoint embedding and correlation
with the bulk leave.  This is exactly the information missing from the
published black boxes at (1.2).

If acyclicity is temporarily omitted, the theorem gives an exact outer
matching and hence a directed partial permutation with exactly
`Cat_m` unused tails and heads.  A separate Boolean cycle-switch theorem is
then sufficient.  Neither the reserve packing nor the cycle switch is
proved here.

## 5. A sharp Hall condition after a cap-two support is fixed

The forest-support Rado theorem reduces the selection to Hall.  In the
cap-two regime Hall itself has a purely componentwise form.

### Theorem 5.1 (balanced cap-two criterion)

Let `R` be a spanning physical linear forest and suppose every lower and
upper colour has occurrence degree one or two in its colour-incidence graph
`G_R`.  Then `G_R` has a perfect matching if and only if every path component
of `G_R` has one endpoint on each shore.

#### Proof

Every component of a bipartite graph of degrees one and two is a path or a
cycle.  Every even cycle has a perfect matching.  A path has a perfect
matching exactly when it has even order, equivalently when its endpoints
lie on opposite shores.  Components are independent. \(\square\)

Thus, in a cap-two construction, the exponential Hall family collapses to
one signed endpoint-balance bit per colour component.  The `m=3`
forest-support witness has profile `1^11 2^4` on each shore and exactly this
balanced-component property.

## 6. The canonical BTK tail cannot merely be recoloured at the head

Let

\[
                  \tau:\binom{[2m]}{m-1}\longrightarrow
                        \binom{[2m]}m
\]

be the one-step successor in the standard BTK symmetric-chain
decomposition.  It is injective.  Write

\[
                         \tau(L)=L+a(L).
\]

Keeping this tail map and choosing a second coordinate `b notin tau(L)`
produces

\[
 U(L)=\tau(L)+b,qquad H(L)=L+b.                    \tag{6.1}
\]

The proposed head-only rethread is therefore exactly the following sparse
rainbow matching problem:

\[
  U:\binom{[2m]}{m-1}\to\binom{[2m]}{m+1}
       \text{ is bijective},qquad H\text{ is injective}.       \tag{6.2}
\]

If (6.2) holds, the lower, upper, tail and head resources are all injective;
only directed cycles remain to be blocked.

The retained audit gives:

| `m` | result before cycle cuts | detail |
|---:|:---|:---|
| 2 | SAT and acyclic | one of two upper bijections has four heads |
| 3 | UNSAT | all 120 upper bijections enumerated; max head image 14/15 |
| 4 | UNSAT | exact 224-variable CNF |
| 5 | UNSAT | exact 1050-variable CNF |

The `m=3` row is solver-free exhaustive.  Its complete head-image histogram
over the 120 upper bijections is

```text
10^1 11^19 12^33 13^57 14^10.
```

This already disproves the fixed-tail proposal as an all-dimensional
construction.  Any successful BTK/SCD excursion rotation must alter the
one-step tails, use several SCD frames, or perform a genuinely coupled
tail/head rethread.

## 7. Artifacts and scope

The absorber identity is exhaustively replayed for every outer pair through
`m=5` by

```text
scratch/audit_boolean_single_pair_absorber_20260731.py
scratch/boolean_single_pair_absorber_m2_m5_20260731.audit.json
```

The fixed-tail model and census are in

```text
scratch/audit_btk_fixed_tail_rainbow_rethread_20260731.py
scratch/btk_fixed_tail_rainbow_rethread_m2_m5_20260731.audit.json
```

The `m=4,5` UNSAT rows are solver outputs without retained DRAT proofs and
are evidence only.  The `m=3` no-go is a complete direct enumeration and is
proof-safe.  None of these results proves or refutes the unrestricted
Catalan Linear Matching theorem, the robust reserve-packing theorem, or the
full Regenerative Shadow--Braid theorem.

