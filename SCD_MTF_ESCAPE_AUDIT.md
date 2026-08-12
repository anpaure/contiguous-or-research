# Independent audit of `SCD_MTF_ESCAPE_RESEARCH.md`

## Verdict

The central-square obstruction is correct.  Its quantifiers are as strong as
claimed: it excludes an update between **every pair** of exposing states in
the indicated direction, rather than merely excluding a canonical exposure.
Both directional arguments correctly invoke the exact existential
quotient-chain criterion.

The global consequence is also correct, but its exception count is one unit
looser than necessary.  In a directed vertex-disjoint path system, every
projection edge that can possibly be an MTF transition enters one of the
`K` singleton-chain vertices or the unique empty-minimum chain.  Hence there
are at most

\[
                             K+1
\]

compatible traversed edges, not merely `K+2`.  The displayed
`W-2K-2` incompatibility bound is therefore valid but conservative; it
strengthens to `W-2K-1`.

The claimed `2W-o(W)` cost is a valid **lower bound for the explicitly
restricted direct chain-by-chain scheme**.  It is neither a construction of
length `2W+o(W)` nor a lower bound for the unrestricted OR problem.  One
sentence should also be read optimistically rather than literally: an
existentially compatible adjacency *may* cost one update after choosing
suitable endpoint states, but arbitrary preassigned exposing states need not
realize that one-step transition, and pairwise witnesses need not compose.
This only makes the lower bound stronger and does not damage it.

Finally, Proposition 3 correctly extends the central forest to a saturated
minimum-width chain partition.  The normalized-matching argument does **not**
show that the resulting chains are symmetric.  Consequently it is not, on
the proof given, an extension to an SCD.  The manuscript itself mostly uses
the accurate phrase “saturated partition”; any handoff summary calling it an
SCD extension must be corrected.

## 1. Audit of the inherited state-fiber statements

Write a saturated chain as

\[
C=(B\subset B+e_1\subset\cdots\subset B+e_1+\cdots+e_h).
\]

The cited fiber theorem says that every ordered-partition state exposing `C`
has the form

\[
  (\mathcal P(B),\{e_1\},\ldots,\{e_h\},\mathcal Q(Z(C))),
\]

where the first and last pieces are arbitrary ordered partitions of the
chain minimum and the complement of the chain top.  Thus the theorem does
not silently collapse either endpoint to one block.

For a target chain `D` of nonempty minimum `A`, the exact existential
one-update theorem is

\[
  \exists\Pi\in F(C),\ X\ne\varnothing:
       M_X(\Pi)\in F(D)
  \quad\Longleftrightarrow\quad
  C-A\text{ and }D-A\text{ are cross-nested}.
\]

This equivalence already quantifies over the entire predecessor fiber and
over every legal update.  Therefore proving that two displayed members of
the quotient chains are incomparable really does exclude all exposing-state
choices.  The use of this theorem in Theorem 1 is legitimate.

The empty-minimum case is genuinely different: its admissible anchor is the
first singleton increment.  Treating the unique empty-minimum chain as an
exception is therefore necessary unless that anchored quotient is audited
separately.

## 2. Line audit of Theorem 1

Let

\[
 S\subset T=S+a\subset U=S+a+b
\]

belong to `C`, and let `T'=S+b` belong to the disjoint chain `D`.

### Reverse direction `D -> C`

If the target minimum `B=min(C)` is nonempty, then `B subseteq S`.  Hence the
two quotient-chain members

\[
 T'-B=(S-B)+b,\qquad T-B=(S-B)+a
\]

are distinct and have equal cardinality.  They are therefore incomparable.
The exact quotient-chain criterion rules out `D -> C` for all predecessor
and successor exposing states.  No symmetry, canonical ordering, or endpoint
block choice is used.

### Forward direction `C -> D`

Let `A=min(D)` be nonempty and suppose `D` continues from `T'` to a cover
`V`.  Necessarily `A subseteq T'`.

* If `b notin A`, then `A subseteq S`, and `T-A` and `T'-A` are distinct
  equal-size quotient members.  Cross-nesting fails.
* If `b in A`, write `A=A_0+b` with `A_0 subseteq S`.  Then
  \[
     T'-A=S-A_0,\qquad T-A=(S-A_0)+a.
  \]
  Since `V` covers `T'`, `V-A` is another set one cardinality above
  `T'-A`.  If the two quotient chains were cross-nested, the equal-size sets
  `V-A` and `T-A` would have to coincide.  Because `A subseteq V`, adding
  `A` back gives
  \[
       V=(T-A)\cup A=T\cup\{b\}=U,
  \]
  contradicting disjointness of `C` and `D`.

The phrase “the same common quotient chain” is stronger wording than needed:
cross-nesting merely says the union of the two quotient chains is a chain.
That is sufficient, since a set-chain has at most one member of any fixed
cardinality.  The proof is sound.

### Exact scope

The local theorem applies to arbitrary disjoint saturated chains containing
the stated central diamond.  The later global exception count additionally
uses the SCD facts that every non-singleton chain contains such a triple,
exactly `K` middle chains are singletons, and exactly one chain contains the
empty set.  It should not be exported without those global hypotheses to an
arbitrary saturated chain cover whose middle chains may terminate early.

## 3. Directional exception count

For every non-singleton SCD chain `C`, let `e_C` have functional orientation

\[
                         C\longrightarrow h(C).
\]

The two directions have the following necessary conditions.

* A functional-forward traversal `C -> h(C)` can be compatible only if its
  head `h(C)` is a singleton chain or the unique empty-minimum chain `L`.
* A reverse traversal `h(C) -> C` can be compatible only if `C=L`.  Its head
  is again `L`.

Thus **every** potentially compatible traversed projection edge has its head
in the same exceptional vertex set

\[
             \{\text{the `K` singleton chains}\}\cup\{L\}.
\]

A directed vertex-disjoint path system has indegree at most one at every
vertex.  It follows immediately that

\[
             \#\{\text{compatible traversed projection edges}\}
             \le K+1.                                      \tag{A.1}
\]

This also handles the edge owned by `L`: when traversed in reverse it enters
`L`, so it cannot coexist with a different traversed arc entering `L`.
There is no need for a separate extra unit.

The manuscript's `K+2` is still a true upper bound, merely non-sharp.  Its
explanation that the extra unit avoids case distinctions is safe, but the
clean head-count (A.1) removes those case distinctions altogether.

For a linear forest, the `C=W-K` edges therefore include at least

\[
  C-(K+1)=W-2K-1                                      \tag{A.2}
\]

one-step-incompatible adjacencies.  The manuscript's
`W-2K-2` ledger is valid but can be improved by one.  In dimension fourteen,
this changes the displayed lower count from `2572` to

\[
                    3432-2\cdot429-1=2573.
\]

The claim that a final functional edge entering a singleton chain is truly
compatible is also correct.  For a singleton target of minimum `T'`, the
target quotient is just `{emptyset}`, which is cross-nested with every source
quotient; updating by `T'` supplies a witness.

## 4. Linear-forest ledger and direct-walk cost

A spanning linear forest on `W` vertices with `C=W-K` edges has exactly `K`
components.  Under the functional orientation, every non-singleton chain has
outdegree one and every singleton chain has outdegree zero.  Edge colors are
unique, so no projection edge is owned twice; an underlying forest cannot
contain a directed cycle.  Each component consequently has exactly one
singleton sink.

Using the sharpened count (A.2), the internal forest transitions cost at
least

\[
 (W-K)+(W-2K-1)=2W-3K-1                         \tag{A.3}
\]

updates: every adjacency costs at least one, and every incompatible one
costs at least one additional update.  Joining the `K` path components in a
prescribed chain-by-chain traversal costs at least `K-1` more updates, since
one ordered-partition state cannot expose two distinct middle sets.  Hence
the total number of updates between the `W` assigned chain visits is at
least

\[
                         2W-2K-2.                \tag{A.4}
\]

The manuscript's `2W-2K-3` is the corresponding valid conservative bound
obtained from `K+2`.

Since `K=W/(m+1)`, both versions are

\[
                         2W-o(W).
\]

This accounting is valid only under all of the scheme restrictions stated
in Section 5:

1. every SCD chain has a designated visit;
2. the visits occur in the orders prescribed by the projection paths; and
3. the walk must pass from one such chain exposure to the next, with any
   repair updates charged between those visits.

The argument is a lower bound for that scheme.  It does not show that two
updates always suffice for an incompatible adjacency, so it gives no
`2W+o(W)` upper construction.  It also does not constrain a state-aware tour
that abandons the projection order, uses an auxiliary exposure as a useful
visit in its own right, or selects unrelated cross-chain arcs.

The sentence “a one-step-compatible adjacency costs one update” should be
understood as an optimistic charge.  Existential pairwise compatibility
only guarantees that *some* predecessor/successor fiber pair realizes one
update.  A globally preselected state for the shared chain need not realize
both neighboring existential arcs, because pairwise quotient witnesses need
not compose.  For the lower bound one may safely charge every compatible gap
only one update anyway.

## 5. Audit of Proposition 3

The central construction is correct.  Orient each path toward one endpoint.
Every oriented edge `T -> T'` contributes

\[
 T\cap T'\subset T\subset T\cup T'.
\]

The rainbow meet and join conditions use every rank-`(m-1)` and
rank-`(m+1)` set exactly once.  The oriented tails use every middle vertex
except one terminal vertex per path.  Since there are `K` paths, the
remaining `K` middle sets are singleton chains.  Thus the three central
levels are partitioned into `C` triples and `K` singletons.

The normalized-matching extension is also correct as a construction of a
saturated partition:

* for every `r<m-1`, choose an inclusion matching from rank `r` to rank
  `r+1` saturating rank `r`;
* their union is a family of vertex-disjoint saturated lower chains, each
  terminating at a unique rank-`(m-1)` set;
* dually, choose matchings on the upper half to obtain one saturated upper
  chain beginning at every rank-`(m+1)` set;
* attach the corresponding lower and upper chains to the central triples.

There are exactly `C+K=W` resulting chains, so this is a minimum-width
saturated chain partition of the Boolean lattice.

What is **not** proved is symmetry of those chains.  Independent normalized
matchings do not ensure that the bottom rank of the lower extension and the
top rank of the upper extension sum to `2m` for each prescribed central
triple.  Extending an arbitrary rainbow linear forest to an actual symmetric
chain decomposition would require an additional coupled extension theorem.
No such theorem appears in the manuscript.

This distinction does not affect the MTF obstruction.  In the constructed
partition, every one of the `C` non-singleton central chains contains its
central triple, the other `K` chains are middle singletons, and exactly one
chain has empty minimum.  Those are precisely the hypotheses used in the
`K+1` compatibility count; symmetry is unnecessary.

## 6. Claim-by-claim status

| Claim | Audit status | Precise scope/correction |
|---|---|---|
| Fiber description covers arbitrary endpoint partitions | proved | Full exposing-state fiber, not canonical states only. |
| Nonempty-target quotient-chain criterion | proved/inherited | Exact existential criterion over every source exposure and update. |
| Reverse central-square barrier | proved | Requires nonempty minimum of the owner/target chain. |
| Forward central-square barrier | proved | Requires nonempty target minimum and a successor above the alternate middle set. |
| Only singleton targets and the empty-minimum chain evade the forward SCD screen | proved | “Evade” means not ruled out, not necessarily compatible. |
| Only the empty-minimum owner evades the reverse SCD screen | proved | Again only a necessary exception. |
| At most `K+2` usable path edges | true but loose | Sharpen to `K+1` by counting exceptional heads. |
| At least `W-2K-2` incompatible forest edges | true but loose | Sharpen to `W-2K-1`. |
| Direct prescribed-order cost is `2W-o(W)` | proved as a lower bound | Not an upper bound and not a statement about unrestricted `nu(2m)`. |
| Rainbow linear forest extends by normalized matchings | proved | Extension is a saturated minimum-width chain partition. |
| Rainbow linear forest extends to an SCD | not proved | Symmetry requires a further coupled lower/upper extension theorem. |
| Barrier survives the normalized-matching extension | proved | It uses central triples, singleton count, and the unique empty-minimum chain, not symmetry. |

## 7. Safe theorem ledger for reuse

The following version can be handed off without qualification.

> Let an SCD of `B_(2m)` induce its two-sided central projection, and let a
> directed vertex-disjoint path system use projection edges in arbitrary
> traversal directions.  Then at most `Cat_m+1` traversed edges are
> existential one-step MTF transitions between the full exposing-state
> fibers of their endpoint chains.  Consequently, if the projection is a
> spanning linear forest, at least
> \[
>   \binom{2m}{m}-2\operatorname{Cat}_m-1
> \]
> of its internal adjacencies require at least two MTF updates.  Any direct
> traversal that visits the chains in those path orders therefore uses at
> least
> \[
>   2\binom{2m}{m}-2\operatorname{Cat}_m-2
> \]
> updates between designated chain visits.  This is a framework-specific
> obstruction, not a lower bound for the unrestricted OR-array problem.

> A two-sided rainbow spanning linear forest does canonically determine the
> three central levels of a minimum-width saturated chain partition, and
> normalized inclusion matchings extend it to the whole Boolean lattice.
> This extension need not be symmetric; nevertheless the same MTF barrier
> applies because its proof only uses the central triples and exceptional
> middle singleton/empty-minimum chains.

