# Independent audit of the SCD multi-funnel recurrence and three-primary
# reserved-bank theorem

Date: 2026-08-01  
Audited file:
`MATH_THEOREM_OWNER_LAYER_SCD_MULTIFUNNEL_RECURRENCE_AND_THREE_PRIMARY_GATE_20260801.md`  
Verdict: **PASS with the explicit local/global and equivariance scopes stated
in the theorem.**

## 1. Common matching and socket rows

The coordinate-load identity was checked directly:

\[
 {2m-2\choose m-1}-{2m-2\choose m-2}
 ={1\over m}{2m-2\choose m-1}
 =\operatorname {Cat}_{m-1}.
\]

In the product of the two-coordinate chains

\[
 \varnothing<z_i<z_i a_i,\qquad a_i,
\]

every cover which adds `a_i` already contains `z_i`; hence all advertised
full funnels coexist in one central matching.  If `B=z_iS` and
`M(B)=a_i z_iS`, the alternate tail `A=a_iS` has
`M(A)=a_iSx`, `x\ne z_i`.  Equality of two socket colours would force
equality of their `z_i`-deleted owners `M(A)`, and then equality of their
tails.  Thus the within-funnel tail, head, owner and colour injections pass.

Distinct add-coordinate funnels cannot share a matched head under one
perfect matching.  Cross tail-tail, head-tail, provider and graphic rows
remain and are not hidden by the product construction.

## 2. Mixed-head bank

For a long central chain `R<S<L<U`, the head `azR` maps to `azS`; for a
short chain `S<L`, the head `zS` maps to `azS`.  In both cases the tail
`aS` maps to `aL`, so the socket colour is `azL`.  Coordinate signatures
separate short heads, long heads and tails.  This verifies the exact bank
size

\[
 D={2m-3\choose m-2}={m\over2}\operatorname {Cat}_{m-1}.
\]

The scalar table is:

| `m` | `c=Cat_(m-1)` | `C=Cat_m` | `D` | `(C-1-D)_+` | `I_m=C-2c` |
|---:|---:|---:|---:|---:|---:|
| 3 | 2 | 5 | 3 | 1 | 1 |
| 4 | 5 | 14 | 10 | 3 | 4 |
| 5 | 14 | 42 | 35 | 6 | 14 |
| 6 | 42 | 132 | 126 | 5 | 48 |
| 7 | 132 | 429 | 462 | 0 | 165 |
| 8 | 429 | 1430 | 1716 | 0 | 572 |

The theorem correctly does **not** promote this scalar bank to a connector
theorem.  Every omitted connector colour still needs another upper
provider, and a fixed `Q_0` still has to expose the displayed roots as its
literal free ports.

## 3. Short-core braid

For every short chain, direct substitution gives

\[
 A\to B\to C\to A,\qquad
 M(A)=aL, M(B)=azS, M(C)=zL,
\]

and all three colours equal `azL`.  The cross-block containments were
checked role by role; the only external entries are

\[
 \beta_S\to\alpha_T,\qquad
 \gamma_S\to\gamma_T
 \quad\Longleftrightarrow\quad S\subset L_T.
\]

Thus a block Hamilton path with more than two blocks must use gamma blocks.
Given `S_i subset L_(i+1)`, the literal path has:

* provider `C_i->A_i` of colour `azL_i`;
* internal connector `A_i->B_i` of the same colour; and
* cross connector `B_i->C_(i+1)` of colour `azL_(i+1)`.

There are `c` local providers, `2c` induced local components and `2c-1`
connectors.  This verifies

\[
 I_m=(C-1)-(2c-1)=C-2c
    =\sum_{i=1}^{m-2}\operatorname {Cat}_i
                       \operatorname {Cat}_{m-1-i}.
\]

The word **local** is load-bearing.  A global upper-exact extension must
avoid every declared connector port before these edges remain compatible
global connectors.

For the standard Greene--Kleitman short bank, every quotient edge strictly
decreases coordinate sum.  The repeated-level Hall cut is valid.  At
`m=4`, the displayed set `X={24,25,34}` has neighbour set contained in
`{24}`, so deficiency is at least two.

## 4. Four-funnel reserve and product obstructions

The union-reserve proof is exact: every lower set containing one of the
four coordinate pairs must map into the corresponding owner union.  The
outside-preimage allowance is therefore `|U|-|R|`.  Inclusion--exclusion
gives

\[
 S_4=4\Delta_1-6\Delta_2+4\Delta_3-\Delta_4,\qquad
 \Delta_t={2t\over m}{2m-1-2t\choose m-2t},
\]

with out-of-range binomial coefficients zero, and

\[
 2-{S_4\over c}
 ={5(m-7)(m-3)(m-2)\over
   2(2m-3)(2m-5)(2m-7)}.
\]

Hence the cross-recycling lower bound `I_m-1` for `m>=7` passes.

The sharp-coordinate relation has no directed cycle of length at most `m`:
the family of lower sets avoiding such a cycle is larger than the family
of avoiding upper sets.  This is a **directed-girth** theorem, not a proof
that the entire relation is a DAG; cycles longer than `m` remain outside
scope.

For two nested product levels, every short residual chain gives a distinct
pair of sockets sharing one lower-tail resource.  Thus at least
`Cat_(m-2)` deletions are forced.  The upper bounds

\[
 2c-\operatorname {Cat}_{m-2},\qquad
 4c-\operatorname {Cat}_{m-2}
\]

are sound.  Equality is not needed or claimed for an arbitrary convention
for decomposing product SCDs.  The comparison with `C-1` is strictly
negative from `m=22`; its signed numerator is `m^2-23m+36`.

## 5. Three-primary fixed-row reserve

Assume `m=3r+2`.  A physical order-three-fixed row is a union of `r` full
coordinate triples.  For any containing column `B=C+b` and its symbol
`A=C+alpha(B)`, both `B` and `A` uniquely recover `C` as their full-triple
core.  Therefore arbitrary choices on the fixed rows have distinct tails,
distinct symbols and no physical tail--symbol equality.

For quotient loops, core recovery gives `C+g=C`.  The row stabilizer has
order

\[
 \gcd(6r+3,3r)=3
\]

and contains the order-three subgroup `K`, so it equals `K`.  The maximal
three-free subgroup `Gamma` intersects `K` trivially; hence `g=0`, reducing
to the impossible literal equality `B=A`.  The clean-quotient and lifted
isolated-edge claims pass.

The counts also pass:

\[
 {2r+1\choose r}=(2r+1)\operatorname {Cat}_r,\qquad
 {s\over3}\operatorname {Cat}_r,\qquad
 \operatorname {Cat}_r
\]

for physical fixed rows, clean-quotient fixed vertices and residual
rotation sectors.  A relative completion must forbid the union of reserved
tails and heads in **both** residual roles.  Under that condition, the
reserved matching and residual forest are vertex-disjoint and compose.

This section is conditional on the clean equivariant quotient route.  It
does not impose a `Cat_r` lower bound on an arbitrary non-equivariant
multi-funnel construction.

## 6. Tight-pivot scope

The distinguished-source implication is exact once the component endpoints
are literal.  The proof does not construct them.  A complete joint theorem
must still:

1. put the whole predecessor phase `P_0` in the same product/nonproduct
   `M_0` which supplies the funnel relations;
2. retain `P_1` as protected providers and keep its first root free incoming;
3. avoid pivot/funnel port and upper-colour collisions;
4. complete every other upper row without consuming a declared connector
   port; and
5. solve the relative free-bulk quotient around the fixed-row reserve when
   that route is used.

No computation or asymptotic heuristic is used in this audit.
