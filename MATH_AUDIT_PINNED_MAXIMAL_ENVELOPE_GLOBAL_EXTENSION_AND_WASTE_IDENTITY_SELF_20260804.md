# Self-audit: pinned maximal envelope, halo patch, and waste identity

**Date:** 2026-08-04
**Method:** independent symbolic proof replay; no computation, search, or solver
**Audited theorem:**
`MATH_THEOREM_PINNED_MAXIMAL_ENVELOPE_GLOBAL_EXTENSION_AND_WASTE_IDENTITY_20260804.md`

## Verdict

**PASS with the stated halo qualification.**  The maximal-envelope
criterion and both waste identities are unconditional.  The global
`Ibc/Ica` pin-extension corollary is unconditional once the local planted
template contains the complete affected-owner halo and its local letters
respect every global owner window through that halo.  It must not be cited
for an arbitrarily clipped opening.

## 1. Maximal-envelope replay

For every feasible word `A`, each letter lies in every owner and pin label
covering its position, so `A_p subseteq E_p^Pi`.  On a declared interval
the maximal envelope is already contained in the declared label, while the
feasible subword supplies the reverse union inclusion.  Therefore the
maximal envelope itself is feasible.  No distributivity or Helly assertion
is used.

## 2. Boundary-interface replay

Let `J` be the union of pin cells and let `I_J` be exactly the owners whose
windows meet `J`.

* If `p notin H`, then `p notin J`, hence no pin prunes `E_p`.
* If an owner is not in `I_J`, its whole source window misses `J`, hence no
  pin prunes any letter of that owner window.
* Every affected owner and every pin is realized by the local word on `H`.
* The explicit inclusion `L_p subseteq E_p^Pi` is essential: it checks all
  global owner rows covering a halo position, including rows not visually
  internal to the two ray cells.

This proves that the patch does not silently lose an owner at either halo
boundary.  A local template checked only on `J`, or only against its two
central coatom blocks, would be insufficient.  The corollary therefore
requires the complete owner-of-source halo or a separate clipped-boundary
verification.

## 3. Resident Johnson envelope replay

At source position `p`, at most `d+1` consecutive owners contribute to the
intersection.  Starting with rank `r`, at most one element is deleted at
each of at most `d` transitions, so the intersection rank is at least
`r-d>0`.

For a coordinate run `[alpha,beta]`, the safe source interval is

\[
 [0,\beta]\quad(\alpha=0,\ \beta<W-1),
 \qquad
 [\alpha+d,\beta]\quad(0<\alpha\le\beta<W-1),
\]

with the evident right-boundary extensions when `beta=W-1`.  Residence
ensures `alpha+d<=beta` for an internal run.  For every owner index
`i in [alpha,beta]`, this safe interval meets `[i,i+d]`.  Hence every owner
coordinate appears in some maximal-envelope letter of its owner window.

## 4. Fixed-word and waste replay

Every interval of length at most `d` in a word of length `W+d` is contained
in at least one of the `W` intervals of length `d+1`.  Therefore its value
has rank at most `r`.  The total number of short cells is

\[
 \sum_{j=1}^d(W+d-j+1)
 =dW+\binom{d+1}{2}=\Lambda+\sigma.
\]

For the unpinned identity these cells partition into:

1. one first occurrence for each of `Lambda-M` present lower targets;
2. `D` duplicate lower occurrences; and
3. `R` rank-`r` cells.

This gives `M=D+R-sigma` exactly.

After deleting `p` forced target/cell pairs, there are
`Lambda-p+sigma` cells and `Lambda-p` residual targets.  The remaining
cells partition into first residual occurrences, residual duplicates,
extra occurrences of forced values, and rank-`r` cells.  This gives

\[
 M^\Pi=D^\Pi+Q^\Pi+R^\Pi-\sigma.
\]

No sign, endpoint, or multiplicity term is missing.

## 5. Scope exclusions

The theorem does not prove:

* a complete strict-lower deck;
* integral one-copy coloured Euler/trace rounding;
* global planting of the expanded packet in the protected carrier;
* arbitrary-width upper coverage or regeneration; or
* feasibility of retained typed route interiors.

It proves that, in the direct one-phase final model, the lower obstruction
after global inverse extension is exactly the excess literal waste above
the scalar slack, not a further occurrence-Hall system.
