# Necklace SCDs do not lift orbit-by-orbit to bridge-one packets

Date: 2026-07-26

## 0. Outcome

The quotient Boolean poset \(B_n/C_n\) is known to have an explicit
symmetric-chain decomposition.  This was proved for all \(n\), with an
explicit Lyndon-word lowering map, by Hersh and Schilling, *Symmetric
chain decomposition for cyclic quotients of Boolean algebras and relation
to cyclic crystals*, IMRN 2013, doi:10.1093/imrn/rnr254; see also Dhand,
*Symmetric Chain Decomposition of Necklace Posets*, EJC 19 (2012), P26.

That theorem is relevant to the promotion-ring programme, but its direct
lift does **not** supply the required bridge-one chronology.  The
obstruction occurs already at the middle owners and is independent of all
outer-collar choices.

Let \(\tau=(0\ 1\ \cdots\ n-1)\).  Among the
\(\binom n{\lfloor n/2\rfloor}\) middle masks, all but

\[
                         n^3 2^{n/2}=o\!\left(\binom n{\lfloor n/2\rfloor}\right)
\tag{0.1}
\]

have no Johnson-adjacent nontrivial rotation \(\tau^dX\).  Every
bridge-one rotor or owner-changing promotion joins equal or
Johnson-adjacent middle owners.  Consequently, in the direct lifted
necklace construction, \(W-o(W)\) middle states have no bridge-one
neighbour inside their own rotation orbit, under **any** choice of
collars.

Thus a path cover restricted to the obvious cyclic orbits has

\[
                         p\ge W-o(W),
\tag{0.2}
\]

far above the required \(o(W/H)\).  Cyclic quotient symmetry is not the
missing packet chronology.  A necklace SCD could still be useful after a
new positive-density system of cross-orbit bridge edges; this note does
not obstruct such rewiring.

## 1. Rotation adjacency

Identify a subset \(X\subseteq\mathbb Z_n\) with its binary cyclic word.
Fix \(1\le d<n\), and put

\[
                         g=\gcd(d,n).
\tag{1.1}
\]

The permutation \(x\mapsto x+d\) has \(g\) cycles.  Along each such
cycle, the number of transitions from \(1\) to \(0\) equals the number
from \(0\) to \(1\).  Moreover

\[
 {1\over2}|X\mathbin\triangle(X+d)|
\tag{1.2}
\]

is the total number of \(1\)-to-\(0\) transitions over those cycles.
Therefore

\[
 |X\mathbin\triangle(X+d)|=2
\tag{1.3}
\]

if and only if exactly one \(d\)-cycle is nonconstant, its ones form one
proper cyclic interval on that cycle, and every other \(d\)-cycle is
constant.

Put \(\ell=n/g\).  For one fixed \(d\), choose the exceptional cycle in
\(g\) ways.  A nonempty proper cyclic interval in a labelled
\(\ell\)-cycle is specified uniquely by its start and its length in
\(\{1,\ldots,\ell-1\}\), so there are exactly \(\ell(\ell-1)\) choices.
The constant values on the other \(g-1\) cycles can be chosen in
\(2^{g-1}\) ways.  Thus, before imposing a rank condition, the exact
fixed-\(d\) census is

\[
 g\ell(\ell-1)2^{g-1}=n(\ell-1)2^{g-1}.
\tag{1.4a}
\]

The middle-rank census is at most this, and hence at most

\[
                         n^2 2^{g}.
\tag{1.4}
\]

For every nontrivial \(d\), one has \(g\le n/2\).  Taking the union over
the fewer than \(n\) values of \(d\), and absorbing the extra polynomial
factor, gives

\[
 \#\{X:\exists d\ne0,\ |X\triangle(X+d)|=2\}
 \le n^3 2^{n/2}.
\tag{1.5}
\]

Since

\[
 \binom n{\lfloor n/2\rfloor}=\Theta(2^n/\sqrt n),
\tag{1.6}
\]

the ratio in (1.5) tends to zero exponentially.

For \(d=1\), the characterization is especially simple: (1.3) holds
exactly when \(X\) is one nonempty proper cyclic interval.  The larger
gcd cases merely allow full \(d\)-cycles plus one interval in one
exceptional cycle.

## 2. Bridge-one projection to the middle layer

For the bridge application take \(n=2m\); Section 1 was stated for general
\(n\) because the rotation census itself does not require evenness.
A complete radius-\(H\) state has the form

\[
                         \omega=(L;z_1,\ldots,z_{2H};R),
\tag{2.1}
\]

with middle owner

\[
                         X(\omega)=L\cup\{z_1,\ldots,z_H\}.
\tag{2.2}
\]

The exact bridge-one successor list consists of identities, rotors, and
promotions.  Checking every promotion position explicitly, a rotor with
incoming residual element \(y\), and a promotion at position \(j\), have
target owners

\[
 X_{\rm rotor}=X-z_H+y,
 \qquad
 X_{\rm promotion}=\begin{cases}
 X,&1\le j\le H,\\
 X-z_H+z_j,&H<j\le2H.
 \end{cases}
\tag{2.3a}
\]

Indeed, the promoted element \(z_j\) enters the new lower block while the
displaced lower element becomes the first singleton.  For \(j\le H\)
these changes cancel in the owner; for \(j>H\) they replace precisely
\(z_H\) by \(z_j\).  Thus identities and early promotions preserve \(X\),
whereas every owner-changing rotor or late promotion replaces one element
of \(X\) by one element outside \(X\).  Consequently

\[
 \omega\longrightarrow\omega',\quad X(\omega)\ne X(\omega')
 \quad\Longrightarrow\quad
 |X(\omega)\triangle X(\omega')|=2.
\tag{2.3}
\]

Now lift a quotient-chain decomposition of \(B_n/C_n\).  Away from the
periodic necklaces, each quotient middle owner lifts to its full orbit

\[
                         X,\tau X,\ldots,\tau^{n-1}X.
\tag{2.4}
\]

Any path edge which stays inside this obvious lifted orbit has endpoints
\(X\) and \(\tau^dX\) for some \(d\ne0\).  On a free orbit these owners are
distinct, so equation (2.3) makes (1.3) necessary.  The direct lifted SCD
has one selected middle state for each middle owner; hence an
owner-preserving identity or early promotion cannot create an edge between
two different rotations.  This condition involves only the middle owners;
changing the lower block, outer residual block, or collar ordering cannot
create the missing edge.

A word fixed by a nonidentity rotation has a period \(s\) which is a
proper divisor of \(n\), and there are at most \(2^s\) words of period
dividing \(s\).  Thus periodic middle necklaces contribute at most

\[
 \sum_{\substack{s\mid n\\s<n}}2^s\le n2^{n/2}=o(W)
\tag{2.5}
\]

masks.  Equations (1.5)--(2.5) therefore show that \(W-o(W)\) lifted
middle states have no nontrivial within-orbit bridge-one neighbour.
Every such state is an isolated path component if only the cyclic-orbit
edges are used.  More explicitly, for that restricted graph every path
cover satisfies

\[
 p\ge W-n^3 2^{n/2}-n2^{n/2}=W-o(W),
\tag{2.6}
\]

proving (0.2).  This conclusion uses no assertion about bridge edges to a
different middle necklace orbit.

## 3. Relation to the explicit necklace lowering map

Hersh--Schilling rotate a binary word to its Lyndon representative,
cyclically bracket \(01\)-pairs, and move down a quotient chain by changing
the rightmost unmatched \(1\) to \(0\), with the lower-half rule obtained
by undoing the most recently created pair.  This proves nested quotient
chains, but it makes no assertion that two rotated lifts of one chain have
Johnson-adjacent middle members.  Equations (1.3)--(1.5) show that such an
assertion would be false on almost every middle orbit.

The obstruction is therefore not a defect in the quotient SCD theorem.
It is exactly the additional residence/bridge condition which quotient
order forgets.

## 4. Boundary

Proved:

1. an exact characterization and exponential census of masks having a
   Johnson-adjacent nontrivial rotation;
2. collar-independent failure of within-orbit bridge edges on
   \(W-o(W)\) lifted middle states; and
3. failure of the direct orbit-by-orbit necklace path cover.

Not proved:

1. failure of cross-orbit bridge edges between different necklace
   chains;
2. failure of a dense rewiring of the lifted necklace SCD; or
3. the coefficient-one theorem.

Accordingly the necklace SCD is a possible source of globally nested
chains, but not a ready-made cyclic packet factor.  Any use of it must add
a new positive-density cross-orbit routing theorem.
