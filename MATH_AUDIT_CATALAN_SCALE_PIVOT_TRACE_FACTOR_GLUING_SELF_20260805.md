# Self-audit: Catalan-scale pivot trace-factor gluing

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_CATALAN_SCALE_PIVOT_TRACE_FACTOR_GLUING_20260805.md`  
**Method:** line-by-line symbolic audit; no computation, search, or solver

## 1. Pivot-window audit

The bridge starts from the `h`-state

\[
 U=(\lambda_1,\ldots,\lambda_{h-1},Q+\lambda_h)
\]

and appends

\[
 X,Q+\rho_1,\rho_2,\ldots,\rho_h,
 \qquad \varnothing\ne X\subseteq Q.
\]

After `j` shifts, `0<=j<=h`, the length-`h+1` window contains the old
tail beginning with `lambda_(j+1)`, the redundant pivot `X`, and the new
prefix through `rho_j`.  Its union is therefore

\[
 Q+\lambda_{j+1}+\cdots+\lambda_h
   +\rho_1+\cdots+\rho_j.
\]

The disjoint-label count is `(r-h)+(h-j)+j=r`.  Consecutive windows exchange
exactly `lambda_(j+1)` for `rho_(j+1)`.  There are `h+1` windows, not `h`,
because the append list has `h+1` letters.  After the final append the old
state and `X` have both shifted out, so the final `h` letters are exactly
`V`.

The ground demand is

\[
                         |Q|+2h=r+h.
\]

This is why the theorem explicitly assumes `k>=r+h`; the weaker condition
`h<r` only guarantees `X` exists.

## 2. Owner accounting

For the isolated packing theorem, the hypergraph is simple: multiple
parameterizations of the same `h+1` owner set are coalesced.  The full
symmetric group still preserves the edge family and is transitive on the
rank-`r` vertices, so all degrees really are equal.  If that degree is
`Delta` and `s=h+1`, then `s|E|=W Delta`.  A maximal matching's selected
vertex stars cover `E`, and one selected edge contributes at most
`s Delta` members to that cover.  Hence `m>=W/s^2`.  No independence or
codegree hypothesis is being smuggled into this greedy bound.

The packing theorem acts on the complete owner layer.  It does not prove
that a factor selected independently lies in the complementary vertices.

Let component `j` have `n_j` owner arcs.  There are `c-1` bridges and every
bridge has `h+1` owner arcs.  The owner-partition premise says

\[
                 \sum_{j=1}^c n_j+(c-1)(h+1)=W.
\tag{2.1}
\]

The joined word writes one initial state of `h` letters and then one letter
per owner arc.  Its length is therefore

\[
                         h+W,
\]

not `sum_j(n_j+h)` and not `W+h+(c-1)(h+1)`.  Bridge owners are precisely
the owners absent from the components.  If even one bridge owner duplicates
a component owner or another bridge owner, (2.1) fails and the theorem is
inapplicable.

## 3. Witness preservation

At a join, the preceding component's last `h` letters equal the bridge's
initial state, and the bridge's final `h` letters equal the next component's
initial state.  Hence no component source letter is altered.  Every
component flag remains on its original exact trace arc.

An upper witness which lies wholly inside one component remains a contiguous
owner interval after concatenation.  The identity

\[
      \bigcup_{i=a}^b\bigcup_{p=i}^{i+h}A_p
       =\bigcup_{p=a}^{b+h}A_p
\]

is exact.  By contrast, a witness which crossed the old cut between two
components need not survive.  This is why internal upper completeness is an
explicit premise rather than a consequence of separate component decks.

Endpoint equality is also load-bearing.  Equal owner ranks or equal unions
of endpoint states do not permit literal concatenation; the ordered `h`
letters must agree exactly.

## 4. Lower-slot ledger

There are exactly `h` proper suffix addresses on each order-`h` owner arc.
Leaving all `(h+1)(c-1)` bridge owners unflagged removes

\[
                         h(h+1)(c-1)
\]

owner-rooted flag slots.  Thus

\[
                    h(W-(h+1)(c-1))\ge\Lambda
\]

is exactly equation (4.3).  Prefix-boundary cells and any usable bridge
cells are ignored, so the ledger is conservative for a construction allowed
to use them.  It is only a raw slot count: it proves neither chain nesting,
named containment, nor literal trace compatibility.

From

\[
 dW+{d+1\choose2}\ge\Lambda,\qquad h=d+1,
\]

we obtain

\[
 hW-\Lambda\ge W-{h\choose2}.
\]

No ceiling direction is reversed.  Since `h=Theta(sqrt(r))` and `W` is
exponential, the normalized right side is `1-o(1)`.

For `k=2r`, `h^2/r -> pi/4`, so the even Catalan count `W/(r+1)` incurs
normalized charge `pi/4+o(1)`.  For `k=2r-1`,

\[
 \operatorname{Cat}_{r-1}
 ={1\over r}{2r-2\choose r-1}
 ={1\over2r-1}{2r-1\choose r},
\]

and its normalized charge is `pi/8+o(1)`.  Both constants are strictly less
than one, so the eventual inequalities are valid in their stated
asymptotic scope.  No finite threshold is claimed.

## 5. Exact logical status

The theorem is an implication from a correlated object with four protected
properties.  It does **not** infer that object from any of the following
marginals:

1. a Catalan cycle or path factor without literal trace words;
2. an unconditioned MLD lower forest;
3. the owner-disjoint pivot bank supplied in isolation by Theorem 2.2;
4. endpoint states specified only up to their union;
5. immediate-upper palette coverage without internal arbitrary-width
   witnesses; or
6. the raw capacity inequality (4.3).

The new gain is exact gluing, unconditional isolated bridge packing, and a
sharp scalar comparison.  The remaining existence statement is the
simultaneous selection of the protected trace factor on the bank complement
with the bank's exact rail endpoints.

## 6. Verdict

The pivot identities, greedy packing bound, arc count, owner partition, word
length, witness transport, and even/odd capacity asymptotics are internally
consistent.
The theorem is proof-safe with its current explicit premises.  It is not an
unconditional `B+1` or `B+O(1)` construction.
