# Independent audit: pinned maximal envelopes, global halo extension, and waste identities

**Date:** 2026-08-04  
**Method:** independent pure-mathematical proof replay; no computation,
search, or solver  
**Audited theorem:**
`MATH_THEOREM_PINNED_MAXIMAL_ENVELOPE_GLOBAL_EXTENSION_AND_WASTE_IDENTITY_20260804.md`  
**Audited SHA-256:**
`f89a928ca6f246a1b274c86638bf95e9966953f31833ef13b6e9f5ef7f1c212c`

## Verdict

**INDEPENDENT GO with the theorem's complete-halo qualification.**  The
maximal-envelope criterion, halo patch, resident-Johnson inverse theorem,
and both waste identities are exact.  No source correction was required.
The `Ibc/Ica` corollary does not apply to a clipped opening unless every
owner row meeting the clipped halo is checked separately.

## 1. Maximal pinned envelope

Every feasible letter at position `p` is contained in every owner and pin
label whose interval contains `p`; hence it lies in `E_p^Pi`.  On a
declared owner or pin interval, the envelope is already contained in the
declared label.  A feasible subword supplies the reverse union inclusion,
so the envelope union is squeezed to exactly that label.  Conversely, the
displayed nonemptiness and union equalities say directly that the maximal
envelope is feasible.  No Helly, distributivity, or independent pin-choice
claim is hidden in the proof.

## 2. Complete-halo boundary replay

Let `J` be the union of pin addresses, let `I_J` be all owner windows
meeting `J`, and let

\[
 H=J\cup\bigcup_{i\in I_J}I_i.
\]

If `p notin H`, then `p notin J`, so no pin changes its envelope.  If an
owner is unaffected, its whole source window misses `J`, and every envelope
letter on that window remains unpinned.  On an affected owner or pin, the
local word is contained in the global pinned envelope and has the required
union, which again gives the squeeze equality.

The inclusion `L_p subseteq E_p^Pi` on **all** of `H` is essential.  It
checks global owner rows crossing either local boundary.  A template known
only on the visible ray intervals, or only on the two central coatom
blocks, does not meet the hypothesis.  The source states this boundary
condition correctly.

## 3. Boundary-run intervals in Theorem 3.1

The owner indices whose windows contain source position `p` are

\[
 [\max(0,p-d),\min(W-1,p)],
\]

an interval of at most `d+1` owners.  At most one coordinate is deleted at
each of at most `d` transitions, so their intersection has rank at least
`r-d>0`.

For one coordinate run `[alpha,beta]`, membership in the envelope at `p`
is equivalent to the displayed owner-index interval being contained in
`[alpha,beta]`.  This gives exactly

\[
 P_x=[\ell_x,u_x],\qquad
 \ell_x=\begin{cases}0,&\alpha=0,\\ \alpha+d,&\alpha>0,
 \end{cases}
 \quad
 u_x=\begin{cases}W+d-1,&\beta=W-1,\\ \beta,&\beta<W-1.
 \end{cases}
\]

For an internal run, residence gives `alpha+d<=beta`.  For a left boundary
run, `ell_x=0`; for a right boundary run, `u_x=W+d-1`.  Therefore, for
every owner `i in [alpha,beta]`, the owner window `[i,i+d]` meets `P_x`.
Every coordinate of every owner is consequently supplied by some maximal
envelope letter.  This verifies both boundary cases and the interior case;
there is no missing wrap or off-by-one term.

The aligned-phase corollary is then valid exactly when the expanded packet
contains this entire affected-owner halo and its local antecedent respects
every global owner window through it.

## 4. Unpinned waste identity

In a word of length `W+d`, the number of interval addresses of lengths
`1,...,d` is

\[
 \sum_{j=1}^d(W+d-j+1)
 =dW+\binom{d+1}{2}=\Lambda+\sigma.
\]

Every such interval lies in a length-`d+1` owner window, so its nonempty OR
has rank at most `r`.  The short cells partition into

* one occurrence for each of the `Lambda-M_A` present strict-lower values;
* `D_A` duplicate strict-lower occurrences; and
* `R_A` rank-`r` occurrences.

Equating the partition size with `Lambda+sigma` gives

\[
                         M_A=D_A+R_A-\sigma
\]

with the stated signs.

## 5. Pinned waste identity

For an exact partial matching of size `p` whose cells lie in the short-cell
bank, deleting its distinct target and cell shores leaves
`Lambda-p+sigma` cells and `Lambda-p` residual targets.  The remaining
cells partition into first residual occurrences, residual duplicates,
extra occurrences of forced target values, and rank-`r` occurrences.
Therefore

\[
 M_A^\Pi=D_A^\Pi+Q_A^\Pi+R_A^\Pi-\sigma.
\]

In one fixed literal word, a cell has one OR value.  Hence forced cells have
no residual-target edge, occurrence fibres of distinct values are disjoint,
and the residual matching deficiency is exactly the number `M_A^Pi` of
absent residual values.  The criterion

\[
 D_A^\Pi+Q_A^\Pi+R_A^\Pi\le\sigma+C
\]

is therefore equivalent to terminal lower deficiency at most `C`.

## 6. Exact scope

The theorem removes inverse-fibre search and post-word Hall; it does not
construct the required low-waste one-copy antecedent.  It also does not
plant the expanded packet globally, prove arbitrary-width upper coverage,
preserve typed route interiors, round the fractional trace circulation, or
regenerate the terminal state.  The remaining lower problem is exactly
integral owner-coloured trace/Euler realization with bounded literal waste.
