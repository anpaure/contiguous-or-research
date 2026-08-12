# The \(BA\)-orbit matching--circulation intersection: owner parity and the first-annulus no-go

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad L=m(m+1).
\tag{0.1}
\]

Throughout, \(m\ge2\). The odd-case statements below impose their
stronger displayed lower bounds on \(m\).

For a permutation state \(\pi=(x_1,\ldots,x_n)\), let

\[
 \kappa(\pi)=\{x_1,\ldots,x_m\}
\tag{0.2}
\]

be its middle owner. Use the two rotors

\[
 A(x_1,\ldots,x_n)
   =(x_2,\ldots,x_{n-1},x_1,x_n),
\]

\[
 C=BA,\qquad
 C(x_1,\ldots,x_n)
   =(x_3,\ldots,x_{n-1},x_1,x_n,x_2).
\tag{0.3}
\]

In the canonical nested-star atom system, if \(S\) is the set of atom
source states, exact de Bruijn balance is

\[
                         S=C(S),
\tag{0.4}
\]

and the selected owner occurrences are

\[
 \{\!\{\kappa(e):e\in S\}\!\}
 \mathbin{\dot\cup}
 \{\!\{\kappa(Ae):e\in S\}\!\}.
\tag{0.5}
\]

The matching--circulation intersection has a sharp parity dichotomy.

### Theorem A (even \(m\): the integral intersection is empty)

If \(m\) is even, then for every \(C\)-orbit \({\cal O}\),

\[
 \{\!\{\kappa(e):e\in{\cal O}\}\!\}
 =
 \{\!\{\kappa(Ae):e\in{\cal O}\}\!\}.
\tag{0.6}
\]

Consequently every \(C\)-invariant source set has a coordinatewise even
owner-incidence vector. No nonempty such set satisfies owner capacity
one, even if arbitrary owner rows may be left empty. More quantitatively,
if \(\ell_X\) is its owner load, then

\[
                       \sum_X|\ell_X-1|\ge W.
\tag{0.7}
\]

Thus the exact fractional point in the atom theorem has no Boolean
rounding at all on the even-\(m\) subsequence. This is a linear parity
gap, not a divisibility residue.

### Theorem B (odd \(m\): exact owners force a linear first-annulus hole)

Let \(m\ge3\) be odd. Every individual alternating \(C\)-component has
\(2L\) distinct middle owners. However, its \(2L\) rank-\((m-1)\)
lower-prefix occurrences have support exactly \(L\): every supported
target has load two.

Hence any owner-capacity-one union of \(q\) full \(C\)-components covers
\(G=2qL\) middle owners but at most \(G/2\) rank-\((m-1)\) targets. Since

\[
 N_1=\binom n{m-1}=\frac{m}{m+2}W,
\]

its first lower-shadow hole count obeys

\[
 \boxed{
 M_1^-\ge N_1-\frac G2
 =\frac{m-2}{2(m+2)}W+\frac{W-G}{2}.}
\tag{0.8}
\]

In particular, an exact owner cover has

\[
 M_1^-\ge
 \frac{m-2}{2(m+2)}W
 =\left(\frac12-o(1)\right)W.
\tag{0.9}
\]

Thus even a successful odd-\(m\) rounding of the matching--circulation
rows would fail the Gaussian annulus already at depth one.

### Theorem C (no fixed-offset packet; no arbitrary rematching for \(m\ge5\))

For every \(m\ge3\), three distinct \(BA\)-orbits cannot be bundled by
equal phases, even with fixed phase offsets, into canonical nested-star
triples. For every \(m\ge5\), this remains impossible after arbitrary
phase rematching between the three orbits.

Therefore the smallest proposed explicit orbit packet does not exist.

Together, Theorems A and B close the strictly alternating
\(BA\)-orbit/nested-star architecture as a constant-one
Gaussian-annulus compiler for both parities of \(m\). They do not
obstruct general rotor circulations with nonalternating \(B\)-run
lengths, nor do they disprove the constant-one conjecture.

## 1. Orbit geometry

Write the pullback action of \(C\) on coordinate positions as

\[
 (C\pi)_j=\pi_{c(j)}.
\]

From (0.3),

\[
 c=(1,3,5,\ldots,2m-1)
   (2,4,6,\ldots,2m,2m+1).
\tag{1.1}
\]

The two cycles have coprime lengths \(m\) and \(m+1\). Since every state
has distinct labels, every \(C\)-orbit has the full length

\[
                         |{\cal O}|=L=m(m+1).
\tag{1.2}
\]

Let

\[
 P=\{1,\ldots,m\},\qquad Q=\{2,\ldots,m+1\}.
\tag{1.3}
\]

The owner \(\kappa(\pi)\) reads the labels in footprint \(P\), while
\(\kappa(A\pi)\) reads those in footprint \(Q\). Thus

\[
 \kappa(C^t\pi)=x_{c^tP},\qquad
 \kappa(AC^t\pi)=x_{c^tQ}.
\tag{1.4}
\]

The source owner map is injective on every \(C\)-orbit. Indeed,
\(P\) meets each cycle of (1.1) in a nonempty proper cyclic interval.
A power \(c^t\) stabilizing \(P\) must induce the zero rotation on both
cycles, hence

\[
 t\equiv0\pmod m,\qquad t\equiv0\pmod{m+1}.
\]

Therefore \(t\equiv0\pmod L\). The same argument applies to \(Q\).

The two state shores \({\cal O}\) and \(A{\cal O}\) are disjoint.
Otherwise \(A\pi=C^t\pi\) for some state \(\pi\); distinct labels would
give equality of the position permutations \(A=C^t\). Every \(C^t\)
preserves the two cycles in (1.1), while \(A\) does not.

## 2. Even-\(m\) owner parity

Assume

\[
                         m=2r.
\]

On the length-\(m\) position cycle in (1.1), \(Q\cap C_0\) is the
one-step translate of \(P\cap C_0\). On the length-\((m+1)\) cycle,
the two intersections agree. Thus the phase displacement \(s\) taking
\(P\) to \(Q\) satisfies

\[
 s\equiv1\pmod m,\qquad s\equiv0\pmod{m+1}.
\tag{2.1}
\]

The exact solution is

\[
                         s=m+1,
\tag{2.2}
\]

so

\[
                         c^{m+1}P=Q.
\tag{2.3}
\]

Equations (1.4) and (2.3) give, phase by phase,

\[
 \boxed{
 \kappa(AC^t\pi)=\kappa(C^{t+m+1}\pi).}
\tag{2.4}
\]

Translation by \(m+1\) permutes the \(L\) phases. This proves (0.6).

Now let \(S=C(S)\). It is a disjoint union of full \(C\)-orbits, and
summing (2.4) over them gives

\[
 \sum_{e\in S}
 \bigl({\bf e}_{\kappa(e)}+{\bf e}_{\kappa(Ae)}\bigr)
 =
 2\sum_{e\in S}{\bf e}_{\kappa(e)}.
\tag{2.5}
\]

All coordinates are even. Hence capacity

\[
 0\le\ell_X\le1
\]

forces \(\ell_X=0\) for every \(X\), and therefore \(S=\varnothing\).
Different activated orbits cannot cancel the obstruction because every
incidence is nonnegative.

For the quantitative statement, write \(\ell_X=2d_X\). Every
nonnegative even integer has distance at least one from \(1\), whence

\[
 \sum_X|\ell_X-1|
 =\sum_X|2d_X-1|
 \ge W.
\]

One activated orbit supplies \(2L\) owner occurrences paired into \(L\)
equal-owner pairs by (2.4). Any occurrence-level capacity-one repair must
delete at least one member of every pair, hence at least \(L\) occurrences
per orbit. Breaking the orbit also breaks exact flow, so this lower bound
is valid before charging any circulation repair.

This proves Theorem A.

## 3. Odd-\(m\) middle owners and the first lower prefix

Assume

\[
                         m=2r+1\ge3.
\]

The intersection-size vectors of \(P,Q\) with the two position cycles
\((C_0,C_1)\) in (1.1) are

\[
\begin{array}{c|cc}
 &C_0&C_1\\ \hline
 P&r+1&r\\
 Q&r&r+1.
\end{array}
\tag{3.1}
\]

Powers of \(C\) preserve these two cardinalities. Therefore the source
and successor middle-owner orbits are disjoint. By Section 1 each has
size \(L\), proving that one alternating component has \(2L\) distinct
middle owners.

Now set

\[
 s=m-1=2r,
\qquad
 P_s=\{1,\ldots,s\},\qquad
 Q_s=\{2,\ldots,s+1\}.
\tag{3.2}
\]

These are the rank-\((m-1)\) lower-prefix footprints on the source and
successor shores. Their intersection-size vectors with \(C_0,C_1\) are
both \((r,r)\). More precisely, on \(C_0\), \(Q_s\) is the one-step
translate of \(P_s\), while on \(C_1\) the two footprints agree. The
same Chinese-remainder calculation as (2.1)--(2.2) gives

\[
                         Q_s=c^{m+1}P_s.
\tag{3.3}
\]

Thus the two length-\(L\) prefix orbits coincide. Their common orbit has
length \(L\), since both footprint intersections are nonempty proper
cyclic intervals. Consequently the \(2L\) occurrences in one component
have load exactly two on \(L\) targets and zero elsewhere.

Take any owner-capacity-one family of \(q\) full alternating components.
Their middle-owner blocks are disjoint, so

\[
                         G=2qL.
\tag{3.4}
\]

Each component supports only \(L\) first-lower targets, and overlaps
between different components can only decrease the union. Hence total
support is at most

\[
                         qL=\frac G2.
\tag{3.5}
\]

Subtracting (3.5) from

\[
 \binom n{m-1}=\frac{m}{m+2}W
\]

proves (0.8)--(0.9), and therefore Theorem B.

The obstruction is internal to each orbit block. It does not arise from
random overlap between different chosen components and cannot be repaired
by a better owner-block matching theorem.

## 4. No diagonal three-orbit atom packet

For a canonical nested-star atom, its three source states have a common
ordered suffix in the position interval

\[
                         J=\{m+2,\ldots,2m\}.
\tag{4.1}
\]

This interval has length \(m-1\) and meets both cycles of \(c\) whenever
\(m\ge3\). Therefore

\[
                         \bigcup_{t\in\mathbb Z_L}c^tJ=[n].
\tag{4.2}
\]

Suppose three states \(\pi_1,\pi_2,\pi_3\) had the property that

\[
 C^t\pi_1,\ C^t\pi_2,\ C^t\pi_3
\]

formed a canonical atom for every \(t\). Equality of their ordered
suffixes would give

\[
 (C^t\pi_i)|_J=(C^t\pi_j)|_J
\]

for every \(t\) and every pair \(i,j\). By (4.2), the two base states
agree at every position. Hence all three are equal, contradicting the
three distinct endpoints of a star atom. Replacing \(\pi_i\) by fixed
translates \(C^{a_i}\pi_i\) proves the same assertion with arbitrary
fixed phase offsets.

For completeness, assume now \(m\ge5\). The intersections
\(J\cap C_0,J\cap C_1\) are directed intervals of respective lengths
\(\lfloor(m-1)/2\rfloor\) and \(\lceil(m-1)/2\rceil\), both at least
two. For a state \(\pi\), the multiset

\[
 {\cal D}(\pi)=\{(C^t\pi)|_J:t\in\mathbb Z_L\}
\tag{4.3}
\]

is the Cartesian product of all directed length-\(r\) windows in the
two cyclic label orders on \(C_0,C_1\). A directed window deck of length
at least two reconstructs its cyclic order: the unique window beginning
with a label records that label's successor. Hence equality of suffix
decks forces equality of both cyclic orders up to independent rotations.
The Chinese remainder theorem realizes those rotations by one power of
\(C\).

If three distinct full \(C\)-orbits could be repartitioned into canonical
atoms with one state from each orbit, equality of the three suffixes in
every atom would give pairwise equal suffix decks. The preceding
reconstruction would force the three \(C\)-orbits to coincide. This
contradiction proves Theorem C.

This does not exclude a growing orbit-level factor in which each orbit
is distributed among many different orbit triples. It excludes the
smallest synchronized or arbitrarily phase-rematched three-orbit packet.

## 5. Consequence for fractional-to-integral rounding

The canonical atom system has an exact uniform fractional solution to
its owner and signed-flow rows. Theorem A shows that on every even-\(m\)
instance the corresponding Boolean feasible set is empty. Therefore no
orbit-level fractional-to-integral theorem preserving those rows can
hold uniformly in \(m\).

On odd \(m\), a Boolean owner/flow solution is not excluded by owner
parity alone. It would have to:

1. activate full \(C\)-orbits;
2. pack their \(2L\)-owner blocks disjointly;
3. partition all source phases into canonical star triples involving a
   growing network of orbits.

Theorem C rules out the diagonal three-orbit packet, but not the growing
network. Nevertheless Theorem B says that even a successful solution of
these three tasks has a linear depth-one lower-shadow defect. Hence it
cannot imply the required Gaussian-annulus theorem.

The strictly alternating nested-star lane is therefore exhausted. A
surviving atom construction must alter the chronology—for example by
allowing nonuniform \(B\)-runs between cancelling switches—so that its
flow closure is not \(S=BA(S)\). Once that equality is abandoned, the
six-owner local atom and its exact nested divergence cancellation may
remain useful, but the orbit-rounding problem is a different theorem.

## 6. Adversarial audit

1. **State versus arc conventions.** An injective de Bruijn arc has a
   unique missing label and hence a unique associated permutation state.
   The maps \(A,C\) and the owner \(\kappa\) are therefore unambiguous.
2. **Composition order.** The displayed formula for \(C=BA\) fixes the
   pullback permutation \(c\). Equation (2.2) is checked directly, so no
   inverse-phase sign is hidden.
3. **Multiorbit cancellation.** Owner incidence vectors are nonnegative.
   Coordinatewise even vectors cannot sum to the all-ones vector.
4. **Approximate versus exact ownership.** For even \(m\), permitting a
   leave does not help under capacity one: every nonempty full orbit
   already repeats each owner it uses. Without capacity, (0.7) gives a
   linear mismatch.
5. **Odd-\(m\) divisibility.** If \(2L\nmid W\), exact owner partition is
   already impossible. Theorem B is conditional on a capacity-one union
   and remains valid whether or not the divisibility happens to hold.
6. **Owner simplicity versus shadow simplicity.** Odd \(m\) gives
   \(2L\) distinct middle owners, but the two rank-\((m-1)\) prefix
   orbits coincide. These are different ledgers.
7. **Scope.** The no-go concerns the strict atom chronology
   \(e\to Ae\to BAe\), equivalently \(S=BA(S)\). It says nothing against
   general clustered de Bruijn circulations with longer or variable
   \(B\)-runs.
