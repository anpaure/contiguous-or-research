# Hostile audit of the KLP exact-rail-partition obstruction

**Date:** 2026-08-14  
**Audited source:**
`MATH_OBSTRUCTION_KLP_LOCAL_LIMIT_CANNOT_ROUND_EXACT_RAIL_PARTITION_20260814.md`  
**Verdict:** **PASS after two scope clarifications.**  The full named-owner
space has dimension exactly `W`, and the quantitative hypothesis quoted from
Kuperberg--Lovett--Peled is exact.  Therefore their theorem cannot directly
produce an exact rail partition at the natural component count.  This is an
invocation obstruction, not a nonexistence theorem for the partition.

## 1. Full lattice saturation really gives full row rank

Let `M` be the `W` by `|B|` matrix whose rail columns are their named-owner
incidence vectors.  The cited full-owner-lattice theorem proves

\[
                         M\mathbb Z^{\mathcal B}=\mathbb Z^W.     \tag{1.1}
\]

Tensoring `(1.1)` with `Q`, or simply observing that every standard unit
vector lies in the integer column span, gives

\[
                         \operatorname {rank}_{\mathbb Q}M=W.    \tag{1.2}
\]

The functions `f_A: B -> Q` are the rows of `M`, so their rational span has
dimension `W`.  No assertion that the rail columns themselves are linearly
independent is being made or needed.

This argument is valid for the same complete catalogue used by the lattice
theorem, including harmless parallel parameterizations.  A genuinely
restricted catalogue needs its own rank calculation.  The audited note now
states that caveat explicitly.

## 2. Exact KLP quantitative hypothesis

The primary arXiv source for Kuperberg--Lovett--Peled, Theorem 2.4, assumes
divisibility, bounded integer bases, transitive symmetry, and containment of
the constants.  Its displayed size condition is exactly

\[
 \min(N,|B|-N)
 \ge Cc_2c_3^2\dim(V)^6
             \log(2c_3\dim(V))^6.                   \tag{2.1}
\]

The source defines `c_2,c_3` as integers at least one.  Thus, for any KLP
space containing the named-owner rows,

\[
 \text{right side of `(2.1)`}
 \ge C W^6\log(2W)^6.                               \tag{2.2}
\]

An exact owner partition selecting `s` nonempty rails has `s<=W/2`; for
the port-rich minimum period it has `s<=W/(2q+2)`.  Therefore

\[
 \min(s,|\mathcal B|-s)\le s\le W/2,                \tag{2.3}
\]

which is incompatible with `(2.2)` for large `W`.  Notice that no estimate
of `|B|`, `c_1`, or the actual decoding constant is required.  Failure of
any other KLP hypothesis would only make the invocation less available.

## 3. Hostile scope checks

Two statements were narrowed during audit.

1. Contracting incident owner--facet data does not lower the named-owner
   row rank on the same complete catalogue.  It does not automatically
   transfer the rank calculation to a different restricted configuration
   catalogue.
2. Several natural ground-coordinate period orbits do not, by themselves,
   prove that the full abstract symmetry group of `V` is nontransitive.
   The note now says only that the natural action does not verify
   transitivity.  The dimension-versus-size contradiction remains valid
   even if transitivity is granted for free.

The proof does not say that KLP's conclusion is false at smaller `N`; it
says that Theorem 2.4 gives no guarantee there.  It also does not obstruct a
sparse constraint representation, staged nibble and absorption, or a new
local-limit theorem with a local-rank quantitative cost.

## 4. Provenance and frozen hashes

The primary source was downloaded and inspected on H100 from the arXiv
e-print `1302.4295`.  The exact theorem condition and definitions of
`c_2,c_3` were read from `full-version_final.tex`.  No local Mac computation
was used.  After final synchronization, H100 gave

| artifact | SHA-256 |
|---|---|
| audited obstruction | `baa64792edaeb35533da37d5f101eba14deb3f3205bf49fe1910026566bd5707` |
| arXiv source TeX | `e8af1a37edb6b65a8fd11aa96fb2c4aff8e203296399ba9c2a0242d077794dde` |
| downloaded arXiv e-print | `8c46325239ed8b94b8fcb39df549ed7dc6e5f9f4dd4b9989cc4c22a8c4fa74ec` |

Within this scope, the KLP obstruction is proof-complete.
