# Finite holonomy fibres: the exact universal-unit criterion

## 0. Purpose and scope

This note isolates the arithmetic row in the next fresh-pump face after the
phase-coherent `K_(2,2)` no-go.  A literal phase-split endpoint, a `C6`, or a
`C8` may export a finite menu of completed holonomies, but cap acceptance,
positive and negative history acceptance, and the private closure edge must
refer to the **same** branch.  The question here is when such a finite accepted
fibre contains a unit for every odd child modulus.

The answer is sharp.  For a dimension-independent coherent integer fibre and
a fixed carried total, universal odd-modulus success is equivalent to the
presence of one signed power of two.  A larger bounded menu does not weaken
this requirement.  In particular, a one-occurrence split is arithmetically
sufficient exactly when its accepted nonzero holonomy is dyadic; an adjacent
phase split of gain `+1` or `-1` is sufficient.  Realizing that branch with the
required Boolean, cap, history, and private-edge data is a separate geometric
problem.

No source-deck, upper-shadow, residence, topology, or compiler conclusion is
made here.

## 1. Accepted correlated fibre

Fix a terminal cap/bi-history state `s` and a private closure occurrence `e`.
Let the nonempty finite set

\[
  H(s,e)=\{h_1,\ldots,h_t\}\subset\mathbb Z                 \tag{1.1}
\]

be the coherent integer holonomies of the literal completed branches that
return to `s` and retain or regenerate `e`.  If the carried open-path total is
`w`, the completed totals are

\[
                         A(w;s,e)=w+H(s,e).                  \tag{1.2}
\]

The fibre in (1.1) is not the marginal union over different cap states,
history states, or private edges.  Such a union can combine incompatible
branches and is not a legal aperture state.

Call the correlated fibre **universally odd-unit** at `w` when for every odd
integer `N>=3`,

\[
             \text{there is }a\in A(w;s,e)\text{ with }\gcd(a,N)=1.
                                                               \tag{1.3}
\]

The same definition with all sufficiently large odd `N` is equivalent.

## 2. Exact finite-fibre theorem

### Theorem 2.1 (finite fibre iff one dyadic total)

For nonempty finite `H(s,e)` and fixed integer `w`, the following are
equivalent.

1. The correlated fibre is universally odd-unit at `w`.
2. It is odd-unit for every sufficiently large odd modulus.
3. Some completed total is a signed power of two:

   \[
                 w+h=\epsilon 2^a
       \quad\text{for some }h\in H(s,e),\quad
       \epsilon\in\{-1,+1\},\ a\ge 0.                       \tag{2.1}
   \]

#### Proof

Condition 3 implies condition 1 because every power of two is coprime to
every odd integer.  Condition 1 implies condition 2 trivially.

Suppose condition 3 fails.  For each nonzero `a_i=w+h_i`, choose an odd prime
`p_i` dividing `a_i`; this is possible because `a_i` is not a signed power of
two.  If `a_i=0`, choose any odd prime for `p_i`.  Let

\[
                         P=\prod_{i=1}^t p_i.                 \tag{2.2}
\]

Every `a_i` has a nontrivial common divisor with `P`.  Multiplying `P` by an
arbitrary odd integer gives arbitrarily large odd counterexample moduli.
Hence condition 2 fails.  \(\square\)

The theorem applies to composite moduli without change.  Indeed the
necessity proof is intrinsically composite: it puts one obstructing odd prime
for each non-dyadic branch into a single modulus.

### Corollary 2.2 (one phase-split occurrence)

Suppose the completed fresh-pump fibre over one accepted state is

\[
                              \{0,s\}.                        \tag{2.3}
\]

Starting from zero carried total, it contains a unit for every odd child
modulus if and only if

\[
                              |s|=2^a                         \tag{2.4}
\]

for some `a>=0`.  In particular, a literal adjacent-phase split `s=+1` or
`s=-1` is arithmetically sufficient.

For a general fixed carried total `w`, the two-branch fibre `\{w,w+s\}` is
universal if and only if at least one of `w` and `w+s` is a signed power of
two.

Thus the next actuator size is not determined by the number of circuit
edges.  It is the first literal face with a jointly accepted dyadic branch.
A `C6` or `C8` with many accepted branches but no dyadic completed total is
still defeated by one odd composite modulus.

### Corollary 2.3 (difference one is not enough)

The fact that two totals differ by one does not imply universal success.
For example, the consecutive fibre `\{5,6\}` has no unit modulo `15`.
What matters is an actual dyadic total, not merely a unit difference between
two branches.

Likewise, the fibre `\{0,+s,-s\}` is universal from zero exactly when `|s|`
is a power of two.

## 3. No bounded offset menu for an arbitrary carried total

### Theorem 3.1 (CRT obstruction)

Let `H` be any finite set of integer offsets.  There exist an odd modulus
`N` and an integer carried total `w` such that

\[
                     \gcd(N,w+h)>1\qquad(h\in H).             \tag{3.1}
\]

Consequently no dimension-independent bounded offset menu repairs an
arbitrary inherited voltage at every odd modulus.

#### Proof

For the distinct values `h` in `H`, choose distinct odd primes `p_h`.
The Chinese remainder theorem gives an integer `w` satisfying

\[
                          w\equiv-h\pmod {p_h}                \tag{3.2}
\]

simultaneously.  With `N=prod_h p_h`, every `w+h` is divisible by a prime
factor of `N`.  \(\square\)

This separates two inductive targets.

* A pump from a normalized zero state can be closed by one accepted dyadic
  split.
* Repair of an unconstrained inherited voltage cannot be guaranteed by any
  fixed finite menu.  The recurrence must normalize the carried voltage,
  export a dyadic branch, or allow modulus-dependent phase diversity.

## 4. Fixed-modulus menus and the Jacobsthal barrier

For an odd modulus `N`, let `j(N)` be the least positive integer such that
every interval of `j(N)` consecutive integers contains an integer coprime
to `N`.

### Proposition 4.1 (arithmetic-progression menu)

Let `s` be a unit modulo odd `N`.  The progression fibre

\[
             \{w,w+s,\ldots,w+(L-1)s\}\pmod N               \tag{4.1}
\]

contains a unit for every starting `w` if `L>=j(N)`.  Conversely, for
`s=1`, no smaller uniform `L` has this property.

#### Proof

Multiplication by `s^{-1}` permutes the units of `Z_N`, so (4.1) is the
unit-status image of a consecutive interval.  The assertion is precisely
the definition of `j(N)`; sharpness is witnessed for `s=1`.  \(\square\)

The Jacobsthal function is unbounded on odd integers.  A direct elementary
witness suffices here: for any `L`, choose distinct odd primes
`p_0,...,p_(L-1)` and use CRT to find `w` with
`w+i=0 mod p_i`; then the `L` consecutive integers beginning at `w` are all
nonunits modulo their product.  Therefore a constant-length C6/C8 phase
menu cannot replace normalization or a dyadic branch when the carried total
is arbitrary.

## 5. Modulus-dependent coherent phase formulas

A literal phase occurrence can have a formula depending on the odd modulus.
The preceding fixed-integer theorem should not be misapplied to it.  The
following covers the common affine/dyadic situation.

### Proposition 5.1 (dyadic-affine residue test)

Suppose an integer-valued branch `eta(N)` on odd `N` satisfies

\[
                 2^b\eta(N)=q(N)N+c                         \tag{5.1}
\]

with fixed `b>=0` and fixed integer `c`.  Then

\[
                 \gcd(N,\eta(N))=\gcd(N,c).                  \tag{5.2}
\]

Hence this branch is a unit for every odd `N` if and only if `c` is a
signed power of two.

#### Proof

Since `2^b` is a unit modulo odd `N`, multiplication by it does not change
the gcd with `N`.  Equation (5.1) then reduces the gcd to `gcd(N,c)`.
The final assertion follows by choosing an odd prime divisor of `c` when
one exists.  \(\square\)

For example, `eta(N)=(N+1)/2` is universally a unit because
`2 eta(N)=N+1`, so `c=1`.  Thus a modulus-dependent complement phase is not
excluded merely because its coherent integer representative is not fixed.
It must be checked through (5.1), not through branch count.

For a finite persistent menu satisfying (5.1) with constants `c_i`, the
menu is universally odd-unit if and only if some `c_i` is a signed power of
two.  The proof of Theorem 2.1 applies to the `c_i`, because multiplication
by powers of two does not affect odd-modulus unit status.

## 6. Correlated cap/history qualification

Let the full completed aperture relation be

\[
 \mathcal A_N\subseteq
   \mathcal S_{\rm in}\times\mathcal S_{\rm out}
   \times\mathbb Z_N\times\mathcal E_{\rm priv}.             \tag{6.1}
\]

An arithmetic branch is usable only when one tuple

\[
                         (s,s',\eta,e)\in\mathcal A_N        \tag{6.2}
\]

simultaneously has:

1. accepted cap-prefix current;
2. accepted positive and negative histories;
3. the declared private closure occurrence;
4. literal path/cycle topology; and
5. unit completed voltage.

Theorems 2.1 and 5.1 apply to the holonomy fibre of a **fixed compatible
state/edge relation**.  Taking the dyadic voltage from one branch, the cap
return from another, and the private edge from a third is invalid.

An accepted adjacent split with a persistent branch bit therefore exports
only constant extra state:

\[
       (\text{cap state},\text{positive history},
        \text{negative history},\text{private edge},b),
        \qquad b\in\{0,1\}.                                 \tag{6.3}
\]

The arithmetic row is then closed.  The remaining literal theorem is to
realize the `b=1` dyadic branch while the other four fields in (6.3) are
jointly accepted.

## 7. Consequence for the next Pascal actuator

The minimal `K_(2,2)` face has constant zero correction.  After adding one
phase-split endpoint/closure occurrence, the exact arithmetic decision is:

* **GO:** a jointly accepted branch has lifted holonomy `+/-2^a`, or a
  dyadic-affine formula with signed-power-of-two residue `c` in (5.1);
* **NO-GO for the dimension-uniform finite face:** every jointly accepted
  branch has an odd prime factor after reduction to its fixed coherent
  residue.  The product of one such prime per branch is an explicit
  composite counter-modulus.

Thus a literal `+/-1` branch would discharge the fresh pump with one bit of
exported phase state.  If the one-occurrence, C6, and C8 faces lack such a
branch, their larger number of choices alone cannot help.  The first
possible actuator is the first face whose **correlated accepted** holonomy
fibre contains a dyadic residue.
