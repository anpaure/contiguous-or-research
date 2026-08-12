# Independent audit: finite holonomy fibre arithmetic

## 1. Claims audited

This audit rederives, without using any Boolean carrier assumption, the
number-theoretic claims in
`MATH_THEOREM_K_FINITE_HOLONOMY_FIBRE_UNIVERSAL_UNIT_CRITERION_20260802.md`.

The audited objects are a finite set of coherent integer completed totals
`A`, odd moduli `N>=3`, and the predicate

\[
                            \exists a\in A:\gcd(a,N)=1.       \tag{1.1}
\]

## 2. Universal finite-fibre criterion

If `A` contains `+/-2^r`, (1.1) holds for every odd `N` because an odd
integer has no factor two.

Conversely, if `A` contains no signed power of two, associate to each
nonzero `a` one odd prime factor `p_a`; associate any odd prime to `a=0`.
The odd composite modulus

\[
                               N=\prod_{a\in A}p_a            \tag{2.1}
\]

makes every member of `A` a nonunit.  This proves both necessity and the
claimed explicit adversarial modulus.  Repeated primes or duplicate totals
do not affect the argument.

Multiplying (2.1) by arbitrary odd factors gives arbitrarily large
counterexamples, so restricting to all sufficiently large odd moduli does
not change the criterion.

## 3. One-split and composite checks

For a zero-base fibre `\{0,s\}`, zero is never a unit modulo `N>1`, so the
test is exactly `gcd(N,s)=1`.  This holds for every odd `N` exactly when `s`
has no odd prime factor, namely `|s|=2^r`.

The consecutive pair `\{5,6\}` fails modulo `15`:

\[
                       \gcd(5,15)=5,\qquad\gcd(6,15)=3.       \tag{3.1}
\]

Thus a difference-one assertion would be false for composite moduli.

For `\{0,+s,-s\}`, both nonzero branches have the same gcd with every
modulus, so adding the opposite orientation does not strengthen the unit
test.

## 4. Arbitrary-base CRT check

For finite offsets `H`, choose pairwise-distinct odd primes `p_h` and solve
`w=-h mod p_h` by CRT.  With `N=prod_h p_h`, each `w+h` is a nonunit.
There is no compatibility issue because the prime moduli are pairwise
coprime.  Hence no fixed bounded offset menu is universal over both `w` and
odd `N`.

This also gives the elementary unbounded-Jacobsthal witness by taking
`H={0,1,...,L-1}`.

## 5. Dyadic-affine check

If `2^b eta(N)=q(N)N+c`, then

\[
 \gcd(N,\eta(N))
 =\gcd(N,2^b\eta(N))
 =\gcd(N,q(N)N+c)
 =\gcd(N,c),                                                \tag{5.1}
\]

where the first equality uses oddness of `N`.  For
`eta(N)=(N+1)/2`, equation (5.1) gives gcd one exactly.  This confirms that
modulus-dependent phase formulas require residue auditing and are not ruled
out by the fixed-integer obstruction.

## 6. Correlation scope

The arithmetic proof applies after fixing one compatible cap state,
positive history, negative history, and private edge.  It does not license
unioning incompatible branch marginals.  Consequently it proves neither
existence of a literal phase-split gadget nor its residence, upper-deck,
source, topology, or compiler properties.

## 7. Verdict

All arithmetic and composite-modulus claims pass.  The exact next literal
test is whether the one-occurrence/C6/C8 correlated accepted fibre contains
a dyadic branch (or a dyadic-affine branch with dyadic residue).  Branch
count, pairwise difference, and gcd of all branch values are insufficient
substitutes.

