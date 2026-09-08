# Cyclic coboundary and paired-orbit criteria for zero nonpump background charge

Date: 2026-08-02  
Lane: K, prospective twisted-pump host  
Status: unconditional charge calculus, an exact matching-fibre obstruction,
and two sufficient zero-charge host criteria.  The residual Ore--Ryser,
history, topology, deep-shadow, and compiler rows remain separate.

## 0. Outcome

The prospective host in
`MATH_THEOREM_K_C6_UNIT_PUMP_SEVEN_EAR_PROSPECTIVE_PLANTING_20260802.md`
has one remaining scalar row

\[
 \sigma_{\rm bg}
 =\sum_{F\ne P_P}\lambda(F)
   +\sum_e x_e\delta(e)-\delta(e_o)=0.                 \tag{0.1}
\]

This row can be incorporated exactly into the contracted fragment graph.
If a join `e:F->G` is selected, put

\[
 \omega(e)=\delta(e)
  +\mathbf 1_{F\ne P_P}\lambda(F)
  -\mathbf 1_{F=P_P}\delta(e_o).                       \tag{0.2}
\]

Every feasible rooted cycle uses exactly one outgoing join from every
fragment, including `P_P`, and therefore

\[
                         \sigma_{\rm bg}=\sum_e x_e\omega(e). \tag{0.3}
\]

There are two proof-safe ways to make (0.3) automatic.

1. **Coboundary fibre.**  Restrict the accepted join graph to a support on
   which

   \[
                  \omega(F,G)=a(F)+b(G),
   \qquad \sum_Fa(F)+\sum_Gb(G)=0.                      \tag{0.4}
   \]

   Then every perfect fragment matching has charge zero.  The coherent
   cyclic-lift specialization is

   \[
                  \omega(F,G)=\phi(G)-\phi(F),          \tag{0.5}
   \]

   with one common **integer** lift of `phi`.  A congruence modulo the cover
   order proves only zero residue, not zero integer background charge.

2. **Paired orbit fibre.**  Let an involution pair every residual fragment
   and every residual edge, preserve the degree demands, and negate
   `omega`.  Any factor which is a union of paired edge orbits has charge
   zero.  If the paired quotient graph is `D`-regular bipartite and the
   residual demand is the constant `h<=D`, such an `h`-factor exists.  It can
   be required to contain any prescribed quotient edge.  Hence one
   prescribed orbit of two Boolean-hex partner edges can be built into the
   zero-charge factor.

These criteria are genuinely additional structure.  No degree, codegree,
or expansion hypothesis by itself can force zero charge: even in a regular
bipartite graph of arbitrarily large degree and codegree at most one, put
weight one on every edge incident with one fixed left vertex and zero on
all other edges.  Every perfect matching has charge one.  This is the
minimal frozen-charge obstruction.

The results below concern charge and factor support only.  They do not
prove the six directed-history tests for the eventual Boolean hex, and they
do not replace the residual Ore--Ryser criterion on a nonuniform demand
table.

## 1. Contracted charge cochain

Let `mathcal F` be the fixed fragment set in one prospective host state.
Use a left copy `mathcal F_out` and a right copy `mathcal F_in`.  An accepted
join `e:F->G` is an edge from `F_out` to `G_in`.  A perfect matching is
exactly one outgoing and one incoming join at every fragment; the separate
root/order row decides whether it is the required one-cycle chronology.

### Lemma 1.1 (exact contraction)

For every perfect fragment matching `M`,

\[
 \sum_{e\in M}\omega(e)
 =\sum_{F\ne P_P}\lambda(F)
   +\sum_{e\in M}\delta(e)-\delta(e_o).                 \tag{1.1}
\]

Hence `M` has zero contracted charge if and only if it satisfies the
background row (0.1).

#### Proof

Every fragment is the tail of exactly one selected join.  Thus the second
term of (0.2), summed over `M`, is exactly the first sum on the right of
(1.1).  Exactly one selected edge has tail `P_P`, so the last term of
(0.2) contributes `-delta(e_o)` once.  The remaining terms are the selected
join gains.  \(\square\)

This is why the pump normalization in (0.2) is load-bearing.  Applying an
unadjusted edge-voltage test to the residual join graph shifts the desired
fibre by `delta(e_o)`.

## 2. Coboundary criterion and exact fibre invariant

### Theorem 2.1 (additive-potential zero-charge theorem)

Suppose the accepted join support admits integer functions `a` on
`mathcal F_out` and `b` on `mathcal F_in` such that (0.4) holds on every
accepted edge.  Then every perfect matching of that support has the same
charge

\[
             \sum_F a(F)+\sum_G b(G).                    \tag{2.1}
\]

In particular, if the sum is zero, every rooted Hall solution in this
support satisfies `sigma_bg=0`.

The cyclic coherent-lift condition (0.5) is a sufficient special case.

#### Proof

Every perfect matching uses each left fragment and each right fragment
exactly once, so

\[
 \sum_{(F,G)\in M}\omega(F,G)
 =\sum_Fa(F)+\sum_Gb(G),
\]

independently of `M`.  With `a(F)=-phi(F)` and `b(G)=phi(G)`, the two sums
cancel termwise over the common fragment index set.  Apply Lemma 1.1.
\(\square\)

For a bipartite residual `b`-factor rather than a fragment perfect
matching, the same proof gives the weighted form

\[
 \sum_{e\in H}\omega(e)
 =\sum_{u\in L}b(u)a(u)+\sum_{v\in R}b(v)b'(v).          \tag{2.2}
\]

Thus an additive potential closes charge exactly when the right side of
(2.2) is zero.  It says nothing about whether the `b`-factor exists.

### Theorem 2.2 (alternating-cycle characterization)

Assume the accepted bipartite support has at least one `b`-factor.  The
charge is constant on its entire `b`-factor fibre if and only if every
feasible alternating cycle has signed charge zero:

\[
              \chi(C)=\sum_{e\in C^+}\omega(e)
                       -\sum_{e\in C^-}\omega(e)=0.     \tag{2.3}
\]

On each connected support component, vanishing on every alternating cycle
is equivalent to an additive representation `omega(u,v)=a(u)+b'(v)`.
Consequently a nonzero value in (2.2) is a complete obstruction inside
that fixed support: no change of Hall matching can reach charge zero.

#### Proof

The symmetric difference of two `b`-factors is an Eulerian bipartite
multigraph and decomposes into alternating even cycles.  The charge
difference is the sum of their signed charges.  Conversely, switching one
feasible alternating cycle preserves every degree and changes charge by
(2.3).  This proves the first assertion.

For the second, choose one spanning tree in a connected support and define
`a,b'` successively along it.  Every nontree edge closes an even cycle; its
alternating sum is zero exactly when the same additive equation holds on
that edge.  \(\square\)

Theorem 2.2 is a useful fail-closed audit: compute one factor charge and
the charges of a cycle-space basis.  If the basis charges all vanish and
the factor charge is nonzero, the present support is theorem-dead and an
edge outside it is necessary.

## 3. Paired cyclic-orbit construction

The coboundary face is not the only exact route.  A charge-reversing orbit
pair also cancels without choosing a special matching inside each pair.

Let `G=(L,R;E)` be a residual bipartite graph.  Suppose there is a
fixed-point-free involution `iota` which preserves `L` and `R`, satisfies

\[
                 b(\iota v)=b(v),\qquad
                 \omega(\iota e)=-\omega(e),            \tag{3.1}
\]

and sends every legal resource-labelled edge to another legal edge.  Assume
every edge orbit has size two and projects without a folded endpoint.  Let
`bar G=G/iota`; selecting one quotient edge means selecting both edges of
its orbit.

### Theorem 3.1 (paired-orbit factor)

Every quotient `b`-factor of `bar G` lifts to an `iota`-invariant
`b`-factor of `G` with total charge zero.

If `bar G` is `D`-regular bipartite and `b` is the constant `h` with
`0<=h<=D`, such a factor exists.  For `h>=1` it can be chosen to contain
any prescribed quotient edge.

#### Proof

A quotient edge orbit contributes one incident physical edge at each of
the two vertices in either endpoint orbit.  Quotient degree `b` therefore
lifts to physical degree `b`.  Equation (3.1) cancels the two edge charges
in every selected orbit.

A `D`-regular bipartite multigraph decomposes into `D` perfect matchings.
The union of any `h` of them is an `h`-factor.  To include a prescribed
edge, use a one-factorization containing it and select its colour together
with any other `h-1` colours.  \(\square\)

The theorem extends verbatim to a free cyclic action by pairing orbit
classes `s` and `-s`; self-opposite classes must have charge zero.  For an
odd cover order there is no nonzero self-opposite class.

### Corollary 3.2 (prepared Boolean-hex partner orbit)

Suppose a quotient edge `bar f` lifts to two old host edges
`f,iota(f)` which, together with the chosen nonprivate pump edge, form the
old side of one coherent physical Boolean hex.  If `bar f` lies in the
regular quotient support of Theorem 3.1, the zero-charge factor may be
chosen to contain both partner edges.

If those two edges lie on distinct nonpump components exchanged by
`iota`, then their component voltages are opposite.  The coherent hex
therefore preserves total charge and leaves the pump as the sole unit
voltage source.

#### Proof

Force `bar f` into the quotient factor using Theorem 3.1.  Its lift contains
both partners and has zero total charge.  Charge reversal gives opposite
component voltages.  The coherent Boolean-hex identity has switch charge
zero, so the fusion preserves their zero sum.  \(\square\)

The distinct-component condition is a topology row.  The six positive and
negative collar tests are history rows.  Neither follows from this
corollary.

## 4. Degree/codegree cannot replace charge structure

### Proposition 4.1 (complete frozen-charge obstruction)

For every `D>=1` there is a `D`-regular bipartite graph, with pair codegree
at most one if desired, such that every perfect matching has charge one.
More generally every constant-`h` factor has charge `h`.

#### Proof

Choose an integer `N>2^D` and the difference-Sidon set

\[
                         S=\{1,2,4,\ldots,2^{D-1}\}
                         \subseteq\mathbb Z/N.
\]

Join `x` on the left to `x+s` on the right for `s in S`.  This is a
`D`-regular bipartite graph.  Two different left vertices have at most one
common neighbour, since an equality between two ordered differences of
powers of two has the same least two-adic valuation and hence the same two
exponents; the choice of `N` prevents wraparound.  The same holds on the
right.  Fix one left vertex `u_0` and give weight one
to every edge incident with `u_0`, weight zero to every other edge.  Every
perfect matching uses exactly one edge at `u_0`, and every `h`-factor uses
exactly `h`.  \(\square\)

The weights are already additive: take `a(u_0)=1`, all other potentials
zero.  Thus all alternating-cycle charges vanish.  Expansion, large
minimum degree, and small codegree cannot alter the nonzero constant fibre.
One must either normalize the additive constant to zero, use a
charge-reversing orbit factor, or introduce an alternating circuit with
nonzero charge.

### Proposition 4.2 (minimal arithmetic obstruction outside a frozen fibre)

Fix one `b`-factor `H_0`, and let `g` be the greatest common divisor of the
signed charges of all feasible alternating cycles in its exchange
component.  Every reachable factor has charge congruent to
`sigma(H_0)` modulo `g`.  Hence

\[
                         g\nmid \sigma(H_0)               \tag{4.1}
\]

is an exact obstruction to reaching charge zero by those exchanges.

#### Proof

Every exchange changes charge by an integer sum of alternating-cycle
charges.  \(\square\)

Divisibility is necessary, not sufficient: compatible cycles may overlap
and their usable multiplicities are bounded.

## 5. Exact interface with the 2648K host

The prospective host can now be separated into three logically independent
rows.

1. **Residual owner/lower factor.**  Restrict the physical incidence graph
   to the desired coboundary or paired-orbit support and solve the residual
   degree/resource problem.  For a general nonuniform table this is still
   exactly the Ore--Ryser system already stated in the 2648K notes.  The
   charge theorem does not imply it.
2. **Background charge.**  On the contracted fragment graph, use (0.2).
   Either certify (0.4) with zero constant, or construct the paired quotient
   factor of Theorem 3.1.  If all alternating-cycle charges vanish but the
   audited constant is nonzero, the support is closed by Theorem 2.2.
3. **Hex/history/topology.**  Force one quotient partner orbit as in
   Corollary 3.2.  Then separately verify distinct old components and all
   six directed-history collars.  These tests must not be absorbed into a
   marginal degree or charge claim.

Thus the weakest new all-dimension host statement is no longer “large
degree implies a zero-charge completion.”  It is the following explicit
Boolean/cyclic target:

> after the protected pump and seven-ear banks are fixed, the accepted
> residual support contains either (i) an integer-lift coboundary factor
> face with normalized constant zero, or (ii) a charge-reversing paired
> orbit quotient with a factor containing one coherent pump-partner edge
> orbit.

No such support is constructed here for every dimension.  The theorem
identifies both an exact sufficient structure and the minimal obstruction
which any proposed degree/codegree proof must defeat.
