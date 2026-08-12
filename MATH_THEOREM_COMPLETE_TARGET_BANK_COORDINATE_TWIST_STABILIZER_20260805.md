# A complete occurrence bank may return through a ground-set automorphism, not literal identity

**Date:** 2026-08-05  
**Method:** target-index reparametrization; no computation or search  
**Status:** unconditional transport lemma.  It enlarges the admissible
terminal stabilizer for a complete lower/upper bank.  It does not construct
a PBBS rethread realizing a nontrivial coordinate twist.

## 1. Complete banks

Let `X` be a finite ground set and let `T` be a family of target subsets
which is invariant under a permutation group `G<=Sym(X)`.  A literal word
or carrier has a **complete occurrence bank** for `T` if there is an
injection

\[
                         b:{\cal T}\longrightarrow{cal O}       \tag{1.1}
\]

into its physical interval occurrences such that

\[
                         \operatorname{val}(b(S))=S             \tag{1.2}
\]

for every `S in T`.  Occurrence addresses, interval widths, and any typed
capacity labels may be included in `O`.

## 2. Coordinate-twisted transport

### Theorem 2.1 (complete-bank automorphism lemma)

Suppose a rethread has an injective occurrence transport

\[
                         \Phi:b({\cal T})\longrightarrow{cal O}' \tag{2.1}
\]

and there is one `g in G` such that

\[
               \operatorname{val}'(\Phi(b(S)))=gS
               \qquad(S\in{\cal T}).                          \tag{2.2}
\]

Then the output has a complete occurrence bank for the original target
family `T`.  Explicitly,

\[
                         b'(U)=\Phi(b(g^{-1}U))                  \tag{2.3}
\]

witnesses `U` for every `U in T`.

If `Phi` preserves occurrence capacities and types, every matching from
targets to old bank occurrences transports to a matching on the output.

#### Proof

Since `T` is `G`-invariant, `g^{-1}U` belongs to `T`.  Equation (2.2)
gives

\[
 \operatorname{val}'(b'(U))
 =g(g^{-1}U)=U.
\]

Both `g^{-1}` on targets and `Phi` on occurrences are injective, proving
that `b'` is an occurrence injection.  Type preservation transports any
additional matching constraints. `square`

### Corollary 2.2 (all Boolean ranks simultaneously)

The theorem applies simultaneously to every rank family

\[
                         {X\choose s},qquad 0\leq s\leq|X|,     \tag{2.4}
\]

and to any union of rank families.  Hence one uniform coordinate twist
preserves a complete lower Boolean ideal, the middle owner layer, and a
complete upper Boolean filter all at once.

Complementation commutes with `g`, so a paired lower/upper bank obtained by
complementing paths is also transported simultaneously.

### Corollary 2.3 (compiler reindexing)

Suppose a strict-lower compiler matching assigns target `S` to the old cell
`b(S)`.  Under (2.2), assign target `U` to

\[
                         \Phi(b(g^{-1}U)).                       \tag{2.5}
\]

This is a complete output matching.  Thus a coordinate-twisted terminal
holonomy is harmless for the lower compiler provided the same twist acts
on the whole protected bank and `Phi` respects the physical cell
capacities.

## 3. Application to cyclic PBBS symmetry

For the cyclic PBBS factor, coordinate rotation `rho` commutes with the
forward parenthesis map and preserves every Boolean rank family (although
it need not act transitively on that family).  Therefore an output
protected bank satisfying

\[
                         D^+=\rho^sD^-                           \tag{3.1}
\]

is already complete whenever `D^-` is complete; literal target-by-target
identity is unnecessary.

This gives two distinct proof mechanisms.

1. **One-shot twisted return.**  A rethread transports the entire complete
   bank by one uniform `rho^s`; Theorem 2.1 reindexes its compiler.
2. **Orbit cancellation.**  Consecutive rotated packets satisfy the stronger
   output-to-next-input handoff and their signed currents telescope around
   a full rotation orbit.

The first mechanism needs global completeness of the transported bank but
not equality of the local triangular deck.  The second can work on a
smaller affected deck but needs literal serial handoff.

## 4. Exact boundary

The twist must be uniform.  If different occurrences use unrelated
coordinate permutations, the map on target labels need not be injective
and completeness can fail.  Likewise, equality only of rank histograms is
insufficient: (2.2) is a literal set identity after one common `g`.

The theorem also does not preserve chronology-dependent properties by
itself.  One must still prove:

1. that the target occurrence transport `Phi` is physically realizable;
2. owner simplicity and topology of the output factor;
3. residence and opening compatibility;
4. typed common-cap capacity preservation; and
5. regeneration in the next dimension.

What it removes is the unnecessarily strong demand that a complete target
bank return pointwise.  Returning through any single coordinate
automorphism is exact.
