# K17 exact incidence-cycle and complement-dual companions

## 1. Scope

This note records three independent companions to the compact K17
rank-8/rank-9 incidence master.

1. An exact rooted matching-split encoding of quotient connectedness, with
   an optional exact nonzero-voltage layer.
2. A smaller sufficient-subclass master in which the second incidence
   matching is the complement dual of the first.
3. The search-facing direct owner-arc formulation of that complement-dual
   subclass, with clean `A`-subtour separation.

Neither construction fixes the age-type order.  In particular, neither an
`e55`-fixed UNSAT result nor a complement-dual UNSAT result would imply
global UNSAT.  The unrestricted free-type companion remains load-bearing.

Write `N=1430` and let `G=(O,F;E)` be the 9-regular quotient incidence
multigraph between rank-9 owner orbits and rank-8 facet orbits.  Thus
`|O|=|F|=N` and `|E|=12870`.

## 2. Exact one-cycle companion

### Theorem 2.1

Let `x` be a selected spanning degree-two incidence factor.  The following
are equivalent.

1. `x` is one alternating cycle through all owner and facet vertices.
2. There are disjoint perfect matchings `D,H subseteq x` whose union is
   `x`, and the owner permutation

   \[
                         \sigma=H^{-1}D
   \]

   is one cycle.
3. In addition to such `D,H`, there are 11-bit integers `r(o)` satisfying

   \[
       r(o_0)=0,\qquad r(o)>0\ (o\ne o_0),\qquad
       r(\sigma(o))=r(o)+1
   \]

   on every selected dart whose head is not `o_0`, with no binary
   overflow.

Here `o_0` is owner orbit 0.  Requiring the selected `D` incidence at
`o_0` to have smaller incidence ID than the selected `H` incidence removes
exactly the global `D/H` reversal symmetry.

#### Proof

A connected bipartite degree-two graph is an alternating cycle, and its
two parity classes are disjoint perfect matchings.  Conversely, two
disjoint perfect matchings form a disjoint union of alternating cycles;
these are precisely the cycles of `sigma`.

For (2) implies (3), orient the unique cycle from `o_0` and assign the
successive ranks `0,1,...,N-1`.  They fit in 11 bits.  Conversely, every
component of a permutation is a directed cycle.  A component avoiding
`o_0` would make the ordinary integer rank increase strictly around a
closed directed cycle, impossible.  Hence every owner belongs to the
component of `o_0`, so `sigma` is one cycle.  The two alternating
colourings are exchanged by `D<->H`; because the two root incidences are
distinct, exactly one satisfies the incidence-ID inequality.  `square`

The implementation does not introduce ordered-dart variables.  For a
potential dart consisting of a `D` incidence `e=(o,f)` and an `H`
incidence `h=(o',f)`, every binary increment clause is guarded directly by
`D_e AND H_h`.  Prefix-carry variables are shared by all darts leaving the
same owner.

### Primitive physical voltage

If the incidence shifts of `e,h` are `s,t`, the dart voltage is `s-t`
modulo 17.  Give each owner a one-hot phase `g(o) in Z_17`.  For a selected
dart not entering the root impose

\[
                 g(o')=g(o)+s-t \pmod {17}.
\]

Set `g(o_0)=0`.  On the unique closing dart entering `o_0`, forbid the one
tail phase that would make the total voltage zero.  The quotient factor is
already one cycle, so these clauses are satisfiable exactly when its total
voltage is nonzero.  Since 17 is prime, this is equivalent to the physical
lift being one cycle on all `17N=24310` owners.

### Exact scale

For the rank10-only base (`64350` variables, `421564` clauses), the exact
quotient-cycle companion has

\[
                 121550\text{ variables},\qquad
                 5155518\text{ clauses}.
\]

Adding primitive voltage gives

\[
                 145860\text{ variables},\qquad
                 7100357\text{ clauses}.
\]

The geometry has `102960` ordered distinct incidence pairs at facets,
including 16 quotient loops; 70 nonloop pairs enter the chosen root and
`102874` pairs receive guarded rank increments.  The independent audit
checked all `2^22=4194304` input/output rows of the 11-bit increment,
every permutation through order 8 (`46232` total), and all `17^3=4913`
three-dart voltage words.

## 3. Complement-dual one-matching restriction

Let `C` denote set complementation, exchanging the owner and facet shores.
For a quotient incidence

\[
 e=(O,F,s),\qquad \rho^sF\subset O,
\]

write

\[
 C(F)=\rho^aO',\qquad C(O)=\rho^bF'.
\]

Then physical complementation sends `e` to the quotient incidence

\[
                         \bar e=(O',F',b-s-a).       \tag{3.1}
\]

The exact census gives a fixed-point-free involution on the 12870
incidence orbits: 6435 complementary pairs.

### Theorem 3.1

Choose one incidence perfect matching `D` from owners to facets and define

\[
                    H=C D^{-1} C.
\]

On incidence variables this is exactly

\[
                         H_e=D_{\bar e}.             \tag{3.2}
\]

If `D_eD_(bar e)=0` for every `e`, then

\[
                         x_e=D_e\lor D_{\bar e}      \tag{3.3}
\]

is a spanning degree-two incidence factor.  Conversely, every factor in
this complement-dual subclass has the form (3.3).

#### Proof

Formula (3.1) follows by complementing the physical edge
`rho^g O -- rho^(g+s)F`: its new owner is
`rho^(g+s)C(F)=rho^(g+s+a)O'`, while its new facet is
`rho^g C(O)=rho^(g+b)F'`; their relative shift is `b-s-a`.

Complementation maps the nine-edge star of any owner bijectively to the
nine-edge star of one facet, and maps each facet star to one owner star.
Therefore a perfect matching `D` induces a perfect matching `H` by (3.2).
The pairwise inequalities make them edge-disjoint, so their union has
degree two at every vertex.  The reverse implication is merely the
definition of the restricted subclass.  `square`

The separate master keeps selected support variables `x_1,...,x_12870`
and the `51480` rank-10 turn variables in exactly the same order as the
unrestricted rank10-only outer master.  The complete `inc`/`turn` semantic
map prefix is byte-identical, so incidence and turn replay is unchanged.
It eagerly enforces every rank-10 orbit row.  Its exact size before lazy
cuts is

\[
                   77220\text{ variables},\qquad
                   312884\text{ clauses}.
\]

This is a prospective sufficient lane only.  It is not an argument that an
arbitrary admissible incidence factor can be made complement-dual.

### The parity law and the correct constructive target

Define the owner permutation

\[
                            A=C D.
\]

Because `H=C D^(-1) C`, the owner successor induced by the degree-two
factor `x=D union H` is

\[
                     H^{-1}D=C D C D=A^2.           \tag{3.4}
\]

Consequently a complement-dual factor can never be one quotient cycle
when `A` is a 1430-cycle: `A^2` has exactly
`gcd(1430,2)=2` cycles, each on 715 owners.  This is not a defect in the
construction.  The correct seed is an `A`-Hamilton cycle followed by a
separate two-component switch catalogue.

The optional `--exact-A-cycle` layer imposes a rooted 11-bit order directly
on `A`.  It has

\[
                  108680\text{ variables},\qquad
                  912557\text{ clauses}.
\]

Its decoder exports the `A` order, the two 715-owner `x` cycles, their
voltages, and every unused incidence crossing the two components.  The old
ordinary separator must **not** be fed to this lane: its connectivity cuts
ask `x` to be one cycle and contradict (3.4).  Any lazy run starts with a
clean bank of `A`-subtour cuts over the `D`/`A` variables.

## 4. Direct owner-arc master

The complement-dual equations admit a smaller formulation in which `D`
and `x` are not primary search variables.  For a rank-9 owner `a` and a
label `n in a`, take the directed odd-graph arc

\[
                         a\longrightarrow C(a)+n.   \tag{4.1}
\]

There are nine incoming and nine outgoing arcs at each owner, hence 12870
arc variables.  If the selected incoming arc has label `p` in the current
owner gauge and the outgoing arc has label `n`, edge-disjointness is simply
`p != n`, and the two immediate turn colours are

\[
              U(a;p,n)=C(a)+\{p,n\},\qquad
              L(a;p,n)=a-\{p,n\}.                  \tag{4.2}
\]

Thus 36 unordered turn variables per owner, or 51480 total, linearize both
palettes.  The present master eagerly covers every rank-10 orbit; it maps
the lower rank-7 turn exactly but leaves that row to the downstream model.

The lazy direct master has

\[
                  64350\text{ variables},\qquad
                  325754\text{ clauses},
\]

and the exact-order version has

\[
                  95810\text{ variables},\qquad
                  925391\text{ clauses}.
\]

The custom separator uses only valid `A`-boundary clauses.  Once `A` is
one quotient cycle it computes its voltage; zero voltage is blocked by the
exact selected-cycle clause, while nonzero voltage is accepted.  On PASS it
reconstructs `D`, `H`, and the two `A^2` cycles and writes the cross-component
incidence catalogue.  Residence, the deletion spine, age-type assignment,
and deeper opening remain deliberately downstream.

## 5. Authenticated artifacts

- `scratch/build_k17_age_incidence_exact_cycle_companion_20260801.cpp`
  (`c418a7b51fde2ca07a7abab0c23805339ecd391ebdd7858713e969d13e269c74`)
- `scratch/audit_k17_age_incidence_exact_cycle_companion_20260801.cpp`
  (`8351fab74223923f54bc45fec4cc138226134e8428f74fd827d0f228fa4ea883`)
- `scratch/k17_age_incidence_exact_cycle_companion_20260801.audit.json`
  (`b2ae39dd2d23cf74d275a4176a994ec8daa64c7a31b06068dbd9324992decb95`)
- `scratch/build_k17_age_complement_dual_matching_master_20260801.cpp`
  (`66f764f7257a5335f5d65bd32d2109db066347e7ad283a240b2253f4b63bcf23`)
- `scratch/audit_k17_age_complement_dual_matching_master_20260801.cpp`
  (`d5c2e202719d984b47dfbe4f4211cc9afa40b64aee83b6c83bde983cefc37e39`)
- `scratch/decode_k17_age_complement_dual_matching_master_20260801.cpp`
  (`355d97a29fa1cd843be4e34055951e0dd962e15063879c79f5235595a1933ad9`)
- `scratch/k17_age_complement_dual_matching_master_20260801.audit.json`
  (`7eee5ad5d6fb814a54eec8dcd8d7854af5fcce6202e7734f577371913c38c045`)
- `scratch/build_k17_age_direct_A_cycle_master_20260801.cpp`
  (`b746baf534e2a1b4be1a5e0e7a37829c821e76a94e587e6bb61c9b41d0465d27`)
- `scratch/separate_decode_k17_age_direct_A_cycle_master_20260801.cpp`
  (`a32b8935e714e8dfbb48ce9a9f97b6769713addea251ee3351c4888684f52086`)
- `scratch/audit_k17_age_direct_A_cycle_master_20260801.cpp`
  (`aa0eb5dcd9b6cd8ac78163cfeb318c7cda00b48ef2b373dfa75ccb5d0368017d`)
- `scratch/k17_age_direct_A_cycle_master_20260801.audit.json`
  (`6707ffa234544bcef286871ad1c85ac780b17a8cf83b63d01c978fa5290d3bc6`)

The complement-dual audit checked all `218790=17*12870` physical phase
incidences, the involution and star-duality identities, the DIMACS header
and literal range, and byte equality of the separator-visible semantic
prefix.  No SAT solve was run in this audit.

The independent direct audit checked all 218790 physical phase-arcs,
both identities (4.2), all 1144 available upper and lower turn orbits, and
the exact DIMACS arithmetic in lazy and exact-order modes.  No SAT solve
was run.  In particular, there is no result from which global UNSAT could
be inferred.
