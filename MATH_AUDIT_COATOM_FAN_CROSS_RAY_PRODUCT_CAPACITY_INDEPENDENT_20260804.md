# Independent audit: coatom-fan cross-ray product capacity

**Date:** 2026-08-04  
**Method:** independent symbolic interval replay; no computation, search, or
solver  
**Source theorem:**
`MATH_THEOREM_COATOM_FAN_CANONICAL_DIAMOND_BUNDLE_AND_HALO_GATE_20260804.md`  
**Source SHA-256:**
`0810322ef88e7337f225cc36a33c1b2f7ee9614d9b522257dab1fcf995f3ae01`

## Verdict

**GO as an isolated literal occurrence and product-capacity theorem.**

The construction genuinely evades the constant-envelope rank-one
obstruction.  It does not replicate or route through the common union
envelope `U`; instead, ticket `j` is assigned to its own native diamond

\[
                         p_{j-1},o_{j-1},q_{j-1}.
\]

All `d-1` upstream prefix/suffix witness pairs and all `d-1` downstream
owner/q1 socket pairs are occurrence-distinct.  Thus the bundle bank has
real product capacity before type acceptance.

The polarized terminal type is **not automatic**.  The exact remaining
local premise is one complete cap/phase/guard state which accepts

\[
 (O_{j-1},\text{prefix polarity}),
 qquad
 (Z,\text{suffix polarity})

\]

as the terminal code for the upstream incomparable pair `(X_j,Y_j)`, while
retaining those two exact literal witnesses.  Ambient inverse-halo planting,
background disjointness, and regeneration also remain open.

## 1. Rotor and witness replay

With `n=d+2`, source position `p` carries `C+f_(p+1 mod n)`.  Every owner
window has `n-1` consecutive residues and therefore omits exactly `f_i`,
giving owner `O_i=Z-f_i`.

For `1<=j<d`,

\[
 x_j=[d+2,d+j+1],\qquad y_j=[j,d-1]
\]

have values

\[
 X_j=C\cup F[1,j],\qquad Y_j=C\cup F[j+1,d].
\]

The two address ranges are disjoint, and their lengths are at most `d-1`.
All `x_j,y_j` are therefore pairwise distinct literal target occurrences.

## 2. Native socket replay

At `i=j-1`, the native intervals have lengths

\[
 |p_i|=d,qquad |o_i|=d+1,qquad |q_i|=d+2,
\]

and values

\[
 Z-\{f_i,f_{i+1}\}\subset O_i\subset Z.
\]

As `j` varies, the starts of `p_(j-1),o_(j-1),q_(j-1)` vary injectively.
Different native families have different lengths, and all native lengths
exceed all upstream witness lengths.  Hence every finite coordinate in

\[
 \mathcal B_j=(x_j,y_j;p_{j-1},o_{j-1},q_{j-1})
\]

is disjoint from every finite coordinate of `mathcal B_(j')` for
`j\ne j'`.
The two terminal coordinates within a bundle are also distinct.  This is
an actual paired-capacity bank, not two marginal matchings and not one
shared socket with different state labels.

## 3. Reconciliation with the envelope multiplicity no-go

The envelope theorem proves that the alternative factorization

\[
 (X_j,Y_j)\longrightarrow U\longrightarrow q_U
\]

has rank one because every `j` shares the same `U` occurrence and q1
terminal.  The coatom fan uses

\[
 (X_j,Y_j)\rightsquigarrow(p_{j-1},o_{j-1},q_{j-1}),
\]

whose native values vary with `j`.  It is therefore exactly the “different
injective typed factorization” left open by that no-go, not a contradiction
and not a hidden capacity alias.

## 4. Exact remaining premises

The interval geometry proves occurrence supply, native Hasse type, and
capacity disjointness.  It does not prove:

1. that the external terminal predicate accepts the polarized native code;
2. that the isolated inverse equals the restriction of the full packet
   inverse on its `d`-position left and right halos;
3. that the transported background avoids every displayed occurrence; or
4. that the same slot is regenerated in the next child.

These are the only qualifications added by this audit.  No multiplicity or
two-coordinate capacity obstruction remains inside the isolated coatom fan.
