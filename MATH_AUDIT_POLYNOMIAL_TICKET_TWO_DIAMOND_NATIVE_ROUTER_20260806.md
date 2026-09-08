# Audit of the polynomial two-diamond native router

**Date:** 2026-08-06  
**Method:** direct audit of the normalized-matching, Kruskal--Katona,
Aharoni--Haxell, and literal-occurrence steps; no computation or search  
**Verdict:** the Boolean expansion and the occurrence-disjoint rainbow
selection are correct.  The PBBS typed-cap consequence remains conditional:
containment of a logical target in an upper value is not, by itself, a
complete occurrence-labelled ticket route or an exact terminal-type
acceptance statement.

## 1. Same-rank expansion

Let

\[
 {cal X}\subseteq { [2r-1]\choose s},\qquad
 s\le r-1,\qquad 1\le |{cal X}|\le r^A.
\]

The normalized matching property does give an injection from the whole
rank-`s` layer, and hence from `X`, into the rank-`r-1` layer: all ranks up
to `r-1` are on the increasing side of the Boolean lattice.  If `Y` is
the image and `Z` is its complement family, then

\[
 {cal Z}\subseteq { [2r-1]\choose r},\qquad |{cal Z}|=|{cal X}|,
\]

and rank-`r+1` supersets of `Y` are in bijection with rank-`r-2` members of
the two-step lower shadow of `Z`.

Write `|Z|=binom(x,r)` in the Lovasz real-binomial notation.  For
`a=ceil(A)+2`, polynomial size implies `x<=r+a` for all sufficiently large
`r`.  The Lovasz Kruskal--Katona inequality gives

\[
 |\partial_{r-2}{\cal Z}|
 \ge {x\choose r-2}
 =|{cal Z}|\,{r(r-1)\over(x-r+1)(x-r+2)}
 =\Omega_A(r^2)|{cal X}|.
\]

Thus Lemma 2.1 of the theorem is correct.  Pigeonholing a mixed-rank
family among at most `r-1` nonempty lower ranks loses only one factor `r`,
so the union of its containing upper-terminal menus has size
`Omega_A(r)|X|`.  Upper surjectivity is enough at this point: choose one
literal occurrence index for each distinct upper value.

## 2. Rainbow matching constants

Clone every labelled ticket twice.  Let `mu_r=o(r)` bound the number of
labelled tickets having one value.  For a clone `c`, its candidate graph
`H_c` is a subgraph of the cyclic owner graph.  If `J` is a clone
subfamily, its underlying labelled-ticket set has size at least `|J|/2`,
and its distinct-value set `X` has size at least `|J|/(2mu_r)`.  The
preceding expansion gives

\[
 m:=\left|E\left(\bigcup_{c\in J}H_c\right)\right|
 \ge {c_A r\over2\mu_r}|J|.
\]

Every `m`-edge subgraph of a cycle has matching number at least
`(m-1)/2`.  Since `mu_r=o(r)`, uniformly over every nonempty `J`,

\[
 \nu\left(\bigcup_{c\in J}H_c\right)>2(|J|-1)
\]

for all sufficiently large `r`.  This is exactly the graph case of the
Aharoni--Haxell sufficient condition, so one obtains one edge from each
clone menu and all chosen edges are pairwise vertex-disjoint.

For index `i`, the finite interval-address footprint is

\[
 \Xi_i=\{p_i,o_i,o_{i+1},q_i\}.
\]

Vertex-disjoint owner-cycle edges separate the two owner addresses;
different indices separate the port and upper addresses; and the three
address types have different interval lengths.  Therefore the complete
footprints really are pairwise disjoint.  The clonewise `o(r)` deletion
corollary is also correct: for every clone subfamily, choose one represented
clone for each distinct value.  Their accepted union loses at most
`o(r)|X|` from the raw distinct-value union, after which the same
`mu_r=o(r)` calculation applies.  Thus the two occurrence coordinates may
have different structural-zero sets.

On the universal polarized-socket face, no Boolean expansion is needed.
The owner cycle itself has a matching of size `floor(W/2)`, exponentially
larger than a polynomial ticket bank, so two disjoint footprints per
labelled ticket can be assigned directly even with arbitrary value
multiplicity.  This is correct only when every assigned native pair is an
accepted complete socket; it is not a statement about the present PBBS
type relation.

Likewise, an injective preassignment of tickets to the `W` native ports
removes the polynomial-size restriction entirely: the pairs `(p_i,q_i)`
are already mutually disjoint.  This factor-wide corollary is a correct
conditional statement, not evidence that the PBBS ticket predicate accepts
the polarized code.  That one semantic identification remains decisive.

## 3. The semantic boundary

For a lower set `S`, the condition

\[
                         S\subseteq R_i
\]

only says that the upper value at `q_i` contains `S`.  It does **not** by
itself prove any of the following.

1. There is a physical entry occurrence for ticket `S` at `p_i`.
2. There is a complete literal claim-to-`p_i` prefix in the fixed cap,
   phase, guard, and occurrence state.
3. The terminal type of the ticket accepts `q_i` merely because its value
   contains `S`.
4. The occurrence `q_i` can retain every frozen background role while it
   terminates the new ticket.

The native diagonal theorem proves dual-role coinstantiation when the
terminal ticket has the **same declared envelope/type** `R_i` as the
already materialized upper-witness fact at `q_i`, or when a separate
complete canonical bundle explicitly certifies that role.  It does not
turn an arbitrary strict-lower target `S` into an exact witness at a cell
whose OR value is `R_i`.

The polarized-socket alternative has a different proof-safe boundary.  If
the exact target occurrences already coexist upstream, a native nested pair
may carry only the reversible occurrence-role code.  Then arbitrary native
diamonds suffice, but one must still prove that the actual terminal
predicate accepts that code, that the complete ticket record contains the
upstream occurrences, and that the frozen background and the second
occurrence system compose with the chosen pair.  The socket theorem does
not create any of those premises.

Accordingly, the exact PBBS interface still required is:

> For every logical PBBS ticket `t` and every admitted seam `i`, exhibit,
> in one fixed materialized state, a complete occurrence-labelled route
> from an entry of `t` through the native diamond to `q_i`; prove that the
> ticket's terminal type accepts the exact occurrence fact at `q_i`; and
> prove that all frozen background roles at `q_i` either use disjoint
> capacity or coinstantiate that same fact.

The two occurrence systems must additionally have global product closure
after the selected footprints are fixed.  If an external implementation
node-prices either displayed boundary source letter, disjoint interval
footprints alone are insufficient; one must use the source-free native
semantics or price those source capacities explicitly.

## 4. Proof-safe conclusion

The theorem unconditionally supplies

\[
 \boxed{\text{two pairwise occurrence-disjoint containing diamonds per
 polynomially many labelled lower-set tickets of value multiplicity }o(r).}
\]

It closes the PBBS typed-cap row only after the complete-prefix,
exact-terminal-type, background-coinstantiation, and two-coordinate product
premises above are proved.  In the current PBBS record those premises have
not yet been identified with bare containment, so no unconditional cap-rank
claim follows.
