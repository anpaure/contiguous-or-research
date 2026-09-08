# Self-audit: PR Gray recursion bi-core seam-parity obstruction

**Date:** 2026-08-05  
**Method:** independent symbolic replay of every implication in
`MATH_THEOREM_PR_GRAY_RECURSION_BICORE_SEAM_PARITY_OBSTRUCTION_20260805.md`;
no enumeration, finite search, or solver

## Verdict

**GO, with the scope restrictions in Section 5 of the theorem essential.**

The note proves an obstruction to alternately signing the **fixed published
Proskurowski--Ruskey order**.  It does not disprove a reordered PR recursion,
a different transposition Gray path, or a path cover obtained by cutting and
rejoining the PR list.

## 1. Source-recursion check

Walsh's exact transcription of the PR recursion is

\[
T(n,k)=\operatorname {flip}(T(n,k+1)^R)\circ
       \operatorname {insert}(T(n-1,k-1))
\]

for `1<k<n`, with

\[
\operatorname {first}T(n,k)=1^k010^k(10)^{n-k-1}.
\]

Applying `flip` to the first word of `T(n,k+1)` and `insert` to the first
word of `T(n-1,k-1)` gives exactly

\[
A_{n,k}=1^k0110^{k+1}(10)^{n-k-2},
\quad
B_{n,k}=1^k0010^{k-1}(10)^{n-k-1}.
\]

Their upstep sets differ only at `k+2` and `2k+3`.  This checks the seam
algebra independently of the later rank calculation.

The exceptional first word of `T(n-1,1)` is the reason `k=2` must be
treated separately.  The theorem does so; applying the generic formula at
`k=2` would be invalid.

## 2. MSW-rank check

For `k>=2`, reverse-complementing the interior of

\[
A_k=1^k0110^{k+1}
\]

gives

\[
B_k=1^k0010^{k-1}.
\]

For `k>=3`, reverse-complementing the interior of `B_k` gives `A_(k-2)`.
The primitive MSW recursion therefore gives

\[
f(k)=d_{A_k}(k+2)=i_{B_k}(k+2)=1+f(k-2).
\]

The bases `f(1)=3,f(2)=1` yield

\[
f(2a)=a,
\qquad
f(2a+1)=a+3.
\]

The other two seam ranks are both `k+2`: one comes from the first upstep
of the following `10` factor, and the other from the final deletion of the
primitive prefix `B_k` plus the leading insertion entry of `A_k`.

Thus the generic safety equivalences

\[
\text{plus}\iff f(k)>h,
\qquad
\text{minus}\iff n-k-1>h
\]

are exact, not merely sufficient.

For `k=2`, direct first-return/concatenation algebra gives the four order
lists printed in (2.9).  Their queried ranks are `(1,3;2,1)`, so the seam
is genuinely forced minus for `h>=1,n>=h+2`.

## 3. Position-parity check

Before the top seam in `T(n,k)`, the full path has traversed

\[
\sum_{j=k+1}^n a(n,j)
\]

vertices in earlier blocks and `a(n,k+1)` vertices in the first recursive
branch.  The target is the next vertex, hence

\[
J(n,k)\equiv1+\sum_{j=k+2}^n a(n,j)\pmod2.
\]

There is no off-by-one ambiguity: the first vertex of the full path has
index one, and the seam target follows all preceding vertices.

For `t=n-m`, reflection gives

\[
S(n,m)={n+t\choose t}-{n+t\choose t-1}.
\]

Modulo two this is `{n+t+1 choose t}`.  Lucas/Kummer gives oddness exactly
when `t & (n+1)=0`.  This verifies the phase oracle.

## 4. Obstruction check

When `n>=3h+2`, the seams corresponding to `t=0,...,h-1` are all forced
plus.  If the least set bit `L` of `n+1` is below `h`, then `t=0` and
`t=L` put forced-plus targets in opposite parities.  This proves the first
obstruction.

If `n+1` is a power of two, both `t=0` and `t=(n+1)-5` are disjoint from
`n+1` in binary.  The forced-plus `k=n-2` target and forced-minus `k=2`
target therefore have the same parity.  This proves the second
obstruction.

Reversing the whole path changes every target parity by the same affine
parity translation, so neither contradiction disappears.

## 5. Scope exclusions

The package does **not** prove any of the following.

1. It does not prove that the residual condition
   `2^(nu_2(n+1))>=h` with `n+1` non-power-of-two is sufficient.
2. It does not audit the `k=n-1` top seam, the joins between the large
   blocks in the full PR path, or every recursively embedded seam.  None
   of these is needed for the stated no-go.
3. It does not lower-bound the number of cuts required after arbitrary
   recursive branch reordering.
4. It does not show that the signed bi-core Dyck Gray path is impossible.
5. It prices owner/MSW-core residence only.  It says nothing about literal
   boundary letters, upper palettes, deeper shadows, or common-cap
   compilation.

Within those boundaries, every theorem statement is supported by the
displayed symbolic identities.

