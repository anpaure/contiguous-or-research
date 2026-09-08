# Periodic zero-winding Dyck words: exact defect-one packing and a sector-mass no-go

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, or web search is
used.

## 0. Verdict

Put

\[
 N=2m+1,
 \qquad B_m=\operatorname{Cat}_m,
 \qquad \tau=\phi^2,
\]

where, for the canonical first-maximum factorization

\[
 D=P1R0S,
\]

the step-two PBBS quotient map and its positive sector deficit are

\[
 \tau D=S1P0R,
 \qquad d_0(D)=|S|+1.
\]

This note tests two literal periodic/iterated candidates for violating the
quotient form of \(\mathrm{RP}_A\).

1. The whole peak-defect-one sector can be solved exactly.  After the change
   of variables

   \[
   E(a,b,c)=(10)^a1(10)^b0(10)^c,
   \qquad x=b-1,
   \]

   \(\tau\) is cyclic rotation of the weak composition \((a,x,c)\) of
   \(m-2\).  A zero-winding return exists **only** at step-two time \(s=2\),
   and, in the displayed phase, exists exactly when \(c=0\).  For \(m\ge3\),
   the exact maximum number of pairwise quotient-edge-disjoint zero-winding
   intervals in the entire defect-one sector is

   \[
   \boxed{m-2.}
   \]

   Thus the genuine period-three family with constant physical return density
   has only linear quotient packing.  It is not a counterexample to
   \(\mathrm{RP}_A\).

2. There is a period-free no-go for iterated first-return packets with small
   terminal sectors.  Let \(\mathcal Z_m(H,T)\) be the set of pairs \((D,s)\)
   with \(1\le s\le H\) satisfying the zero-winding equality

   \[
   \sum_{j=0}^{s-1}d_0(\tau^jD)=\delta(\tau^sD)\le T.
   \]

   There are absolute constants \(c,C>0\) such that, for
   \(1\le T\le m\),

   \[
   \boxed{
   |\mathcal Z_m(H,T)|
   \le CHTm^2 4^m
        \exp\!\left(-c\sqrt{m/T}\right).}
   \]

   Consequently, if \(H\le m\) and

   \[
   T=o\!\left(\frac{m}{\log^2m}\right),
   \]

   then

   \[
   \boxed{|\mathcal Z_m(H,T)|=o(B_m/N).}
   \]

   In particular, for \(H=\lceil A\sqrt m\rceil\), all zero-winding
   intervals whose mean sector deficit is

   \[
   o\!\left(\frac{\sqrt m}{\log^2m}\right)
   \]

   have total quotient packing \(o(B_m/N)\), independently of their orbit
   periods.  This includes every fixed periodic sector gadget and every
   growing bounded-sector gadget below that threshold.

   The same conclusion holds at the opposite endpoint and for the
   half-shifted dual sectors.  Up to \(o(B_m/N)\) intervals, both exact
   ledgers

   \[
   \sum_{j<s}d_0(\tau^jD)=\delta(\tau^sD),
   \qquad
   \sum_{j<s}d_0(\phi\tau^jD)=\delta(D)
   \]

   must stay a distance not \(o(m/\log^2m)\) from both \(0\) and \(2m\).

Together with voltage-itinerary rigidity, this gives a sharp qualitative
double escape condition.  For arbitrary cutoffs

\[
 P_m=o(m/\log m),
 \qquad T_m=o(m/\log^2m),
\]

all zero-winding intervals either lying on quotient cycles of period at most
\(P_m\), or having cumulative sector deficit at most \(T_m\), have packing
\(o(B_m/N)\).  Hence a genuine periodic counterexample must simultaneously
use long, nonrepeating quotient orbits and macroscopic accumulated sector
transport.  The present note does not bound that remaining high-period,
high-sector class and therefore neither proves nor disproves \(\mathrm{RP}_A\).

## 1. Exact solution of the period-three defect-one sector

Every semilength-\(m\) Dyck word with \(m-1\) peaks has a unique form

\[
 E(a,b,c)=(10)^a1(10)^b0(10)^c,
 \qquad a,c\ge0,
 \quad b\ge1,
 \quad a+b+c=m-1.
 \tag{1.1}
\]

Put

\[
 x=b-1,
 \qquad a+x+c=m-2.
 \tag{1.2}
\]

Direct substitution in the first-maximum map gives

\[
 \phi E(a,b,c)=E(b-1,c+1,a),
 \qquad
 \tau E(a,b,c)=E(c,a+1,b-1).
 \tag{1.3}
\]

Thus in the coordinates (1.2),

\[
 \boxed{\tau(a,x,c)=(c,a,x).}
 \tag{1.4}
\]

The first maximum of \(E(a,b,c)\) is reached at the first up-step in the
middle block which raises the height from one to two.  The suffix after the
maximum-bearing primitive component is \((10)^c\).  Therefore

\[
 \boxed{
 \delta(E(a,b,c))=2a+2,
 \qquad d_0(E(a,b,c))=2c+1.}
 \tag{1.5}
\]

### Theorem 1.1 (complete zero-winding classification at defect one)

Let \(m\ge2\), and start at the phase \((a,x,c)\).  There is a
zero-winding return after \(2s+1\) PBBS steps if and only if

\[
 \boxed{s=2\quad\text{and}\quad c=0.}
 \tag{1.6}
\]

It is automatically the consecutive return.

#### Proof

Along the three successive \(\tau\)-phases, (1.4)--(1.5) give sector
deficits

\[
 2c+1,
 \qquad 2x+1,
 \qquad 2a+1,
 \tag{1.7}
\]

and endpoint first-maximum positions

\[
 2a+2,
 \qquad 2c+2,
 \qquad 2x+2.
 \tag{1.8}
\]

A zero-winding return at step-two time \(s\) is exactly

\[
 \sum_{j=0}^{s-1}d_0(\tau^jD)=\delta(\tau^sD).
 \tag{1.9}
\]

Every sector deficit in (1.7) is odd and every endpoint in (1.8) is even.
Thus \(s=1\) and \(s=3\) are impossible.  At \(s=2\), (1.9) is

\[
 (2c+1)+(2x+1)=2x+2,
\]

which holds exactly when \(c=0\).

One full three-phase sector sum is

\[
 (2c+1)+(2x+1)+(2a+1)
 =2(m-2)+3
 =N-2.
 \tag{1.10}
\]

For \(s\ge4\), the left side of (1.9) is at least

\[
 (N-2)+1=N-1=2m,
\]

whereas every endpoint in (1.8) is at most

\[
 2(m-2)+2=2m-2=N-3.
\]

Hence no \(s\ge4\) is possible.  At \(s=2\), the sole earlier candidate is
\(s=1\), already excluded by parity, so the return is consecutive. \(\square\)

The theorem recovers the exact gap-five classification, but the orbit form
(1.4) also permits an exact packing count.

### Theorem 1.2 (exact defect-one quotient packing)

For \(m\ge3\), the maximum number of pairwise quotient-edge-disjoint
zero-winding intervals whose start roots have peak defect one is exactly

\[
 \boxed{m-2.}
 \tag{1.11}
\]

For \(m=2\), the corresponding maximum is one.

#### Proof

Put \(n=m-2\).  By (1.4), defect-one \(\tau\)-cycles are the cyclic-rotation
orbits of weak three-compositions

\[
 (a,x,c),
 \qquad a+x+c=n.
\]

By Theorem 1.1, an orbit supports a zero-winding interval if and only if at
least one of its three coordinates is zero.  For \(n\ge1\), the number of
weak three-compositions with at least one zero is exactly

\[
 \binom{n+2}{2}-\binom{n-1}{2}=3n,
 \tag{1.12}
\]

where the same value is checked directly for \(n=1,2\).  A composition
fixed by three-cycle rotation has all three coordinates equal.  Such a
composition is interior whenever \(n>0\), so the cyclic action is free on
the boundary set counted in (1.12).  Hence there are exactly

\[
 \frac{3n}{3}=n=m-2
 \tag{1.13}
\]

relevant quotient cycles.

Every zero-winding interval in this sector uses the two consecutive
step-two edges which carry the two summands in (1.9).  Any two such
two-edge intervals on the same three-cycle intersect.  The literal
residence trace contains those two edges, so it also intersects.  Thus at
most one interval may be selected from each relevant orbit.  Conversely,
selecting one from every relevant orbit gives pairwise disjoint quotient
traces because distinct \(\tau\)-cycles are disjoint.  Equation (1.13)
proves (1.11).

When \(n=0\), the sole composition \((0,0,0)\) is fixed and supplies one
interval, proving the exceptional statement. \(\square\)

This theorem is quotient-level.  A defect-one physical component can have
constant-density short returns because its spatial lift has length
\(\Theta(N)\).  The quotient collapses that repetition to one period-three
orbit, which is precisely why the physical example does not have Catalan
mass.  Since these quotient cycles have length at most three, they belong
to the short-cycle term \(Z_H\), not to the nonwrapping long-cycle packing
\(\overline\nu_H\).  Theorem 1.2 counts pairwise disjoint quotient-edge
supports of their projected physical intervals; it is not silently treating
a wrapping projection as a nonwrapping quotient interval.

## 2. General short-period amplification is negligible

The preceding exact period-three calculation is a special case of a useful
entropy bound.  We include it to keep the quantifiers explicit.

### Lemma 2.1 (voltage-itinerary rigidity)

Let \(D_0,\ldots,D_{q-1}\) be a quotient \(\phi\)-cycle, and put

\[
 a_j=\delta(D_j)\in\{1,\ldots,N-1\}.
\]

The ordered cyclic voltage word \((a_0,\ldots,a_{q-1})\) determines the
quotient cycle up to its starting phase.  Consequently the number of
quotient states on \(\phi\)-cycles of period at most \(Q\) is at most

\[
 \boxed{QN^Q.}
 \tag{2.1}
\]

#### Proof

Normalize the first omitted coordinate to zero.  The voltage word gives the
whole periodic omitted-coordinate word by

\[
 \lambda_0=0,
 \qquad
 \lambda_{t+1}=\lambda_t+a_{t\bmod q}\pmod N.
\]

In a PBBS component every coordinate occurs as an omitted coordinate.
Between two consecutive omissions of a fixed coordinate, its membership in
the alternating factor states changes at every transition.  Consecutive
gaps are odd, so the prescriptions from their two ends agree.  Applying
this to every coordinate reconstructs every state, and hence the quotient
cycle.  There are fewer than \(N^q\) ordered voltage words of length \(q\);
summing over \(q\le Q\) proves (2.1). \(\square\)

### Corollary 2.2 (periodic constructions below linear-over-log period)

If

\[
 Q_m=o(m/\log m),
\]

then the total number of quotient states on \(\tau\)-cycles of period at
most \(Q_m\) is \(o(B_m/N)\).  Hence every collection of zero-winding
intervals confined to those cycles has quotient packing \(o(B_m/N)\).

#### Proof

A \(\tau=\phi^2\) cycle of period at most \(Q_m\) is contained in a
\(\phi\)-cycle of period at most \(2Q_m\).  Lemma 2.1 bounds its total state
mass by

\[
 2Q_mN^{2Q_m}=\exp(o(m)).
\]

On the other hand

\[
 B_m/N=\exp(m\log4-O(\log m)).
\]

The ratio tends to zero.  A packing cannot contain more intervals than
there are start states. \(\square\)

Thus repeating a fixed return word, or any return word with
\(o(m/\log m)\) quotient phases, cannot be amplified to the required scale.

## 3. Accumulated sector mass forces an early final maximum

Short period is not needed for the second no-go.  The key is that a
zero-winding equality identifies the accumulated sector mass with the
first-maximum time of the endpoint.

For \(1\le t\le m\), let \(M_{m,t}\) be the number of semilength-\(m\)
Dyck paths whose first visit to their global maximum ends at step \(t\).

### Lemma 3.1 (early-first-maximum bound)

There are absolute constants \(c,C>0\) such that, uniformly for
\(1\le t\le m\),

\[
 \boxed{
 M_{m,t}
 \le Cm^2 4^m
      \exp\!\left(-c\sqrt{m/t}\right).}
 \tag{3.1}
\]

#### Proof

Fix the attained maximum height \(h\), where \(1\le h\le t\).  Forgetting
the Dyck restriction and the first-visit condition in the prefix only
enlarges the class.  The number of length-\(t\) binary walks from zero to
\(h\) is at most

\[
 \binom{t}{(t+h)/2}
 \le 2^t\exp\!\left(-\frac{h^2}{2t}\right),
 \tag{3.2}
\]

with value zero when parity fails.

After the marked visit, the remaining walk has length \(2m-t\), starts at
height \(h\), ends at zero, and stays in
\(\{0,1,\ldots,h\}\).  The adjacency matrix of that path graph has spectral
radius

\[
 2\cos\frac{\pi}{h+2}.
\]

Bounding one matrix entry by the operator norm and using
\(\cos x\le e^{-x^2/3}\) on the required compact interval gives

\[
 2^{2m-t}\exp\!\left(-c_0\frac{m}{(h+2)^2}\right)
 \tag{3.3}
\]

possibilities, after decreasing the absolute \(c_0\) to cover \(h=1\).
The product of (3.2) and (3.3) is at most

\[
 4^m\exp\!\left(
  -\frac{h^2}{2t}-c_0\frac{m}{(h+2)^2}
 \right).
\]

For \(h\ge2\), arithmetic--geometric mean gives

\[
 \frac{h^2}{2t}+c_0\frac{m}{(h+2)^2}
 \ge c_1\sqrt{m/t};
\]

the case \(h=1\) is stronger after reducing \(c_1\).  Summing over at most
\(m\) heights and enlarging the harmless polynomial prefactor proves
(3.1). \(\square\)

For integers \(H,T\ge1\), define \(\mathcal Z_m(H,T)\) to be the set of
pairs \((D,s)\) such that

\[
 1\le s\le H,
 \qquad
 \sum_{j=0}^{s-1}d_0(\tau^jD)
 =\delta(\tau^sD)\le T.
 \tag{3.4}
\]

The equality in (3.4) is precisely zero winding.  Positivity of the dual
first-passage increments implies that such an equality, when it occurs, is
the consecutive return; that fact is not needed for the upper bound.

### Theorem 3.2 (low accumulated sector mass is superpolynomially sparse)

For \(1\le T\le m\),

\[
 \boxed{
 |\mathcal Z_m(H,T)|
 \le CHTm^2 4^m
      \exp\!\left(-c\sqrt{m/T}\right),}
 \tag{3.5}
\]

with the absolute constants from Lemma 3.1.

Consequently, if \(H\le m\) and

\[
 T=T_m=o(m/\log^2m),
 \tag{3.6}
\]

then

\[
 \boxed{|\mathcal Z_m(H,T_m)|=o(B_m/N).}
 \tag{3.7}
\]

#### Proof

Fix \(s\) and \(t\).  Since \(\tau^s\) is a bijection, the map

\[
 D\longmapsto \tau^sD
\]

injects the pairs in (3.4) with this \((s,t)\) into the endpoint class
counted by \(M_{m,t}\).  Therefore

\[
 |\mathcal Z_m(H,T)|
 \le \sum_{s=1}^H\sum_{t=1}^T M_{m,t}.
\]

The right side of (3.1) is increasing in \(t\), so (3.5) follows.

Under (3.6),

\[
 \frac{\sqrt{m/T_m}}{\log m}\longrightarrow\infty.
\]

Thus the exponential factor in (3.5) is smaller than every fixed negative
power of \(m\).  Since \(H,T_m\le m\), while

\[
 B_m/N\asymp \frac{4^m}{m^{5/2}},
\]

all polynomial prefactors are absorbed, proving (3.7). \(\square\)

### Corollary 3.3 (bounded-sector periodic and iterated packets)

Fix \(A>0\) and put \(H=\lceil A\sqrt m\rceil\).  Let
\(D_m=o(\sqrt m/\log^2m)\).  The total quotient packing of all
zero-winding intervals satisfying

\[
 d_0(\tau^jD)\le D_m
 \qquad(0\le j<s\le H)
 \tag{3.8}
\]

is \(o(B_m/N)\).

The same conclusion holds under the weaker average condition

\[
 \frac1s\sum_{j=0}^{s-1}d_0(\tau^jD)
 =o\!\left(\frac{\sqrt m}{\log^2m}\right)
 \tag{3.9}
\]

uniformly on the family.

#### Proof

Under (3.8), the common value in (3.4) is at most

\[
 HD_m=o(m/\log^2m).
\]

The same estimate is exactly (3.9) multiplied by \(s\le H\).  Theorem 3.2
bounds the number of candidate intervals by \(o(B_m/N)\), and an
edge-disjoint family cannot be larger. \(\square\)

In the plane-tree sector notation,

\[
 d_0(\tau^jD)=2b_0(T_j)+1,
\]

where \(b_0(T_j)\) is the number of edges in the root forest after the
first maximum-bearing root branch.  Thus Corollary 3.3 says that a periodic
or iterated construction built from bounded terminal root sectors cannot be
dangerous merely by increasing its orbit period.  Its terminal-sector mass
must grow to at least the displayed square-root-over-log-squared scale on
the selected intervals.

There is a symmetric endpoint refinement.  For a word
\(D=d_1\cdots d_{2m}\), put

\[
 D^\dagger=(1-d_{2m})(1-d_{2m-1})\cdots(1-d_1).
 \tag{3.10}
\]

If \(H_D(j)\) is the height after \(j\) steps, then

\[
 H_{D^\dagger}(j)=H_D(2m-j).
 \tag{3.11}
\]

Thus \(D^\dagger\) is Dyck.  If the first global maximum of \(D\) occurs
at time at least \(2m-U\), then the first global maximum of
\(D^\dagger\) occurs at time at most \(U\): reversal sends the last
maximum time of \(D\) to the first maximum time of \(D^\dagger\).

The zero-winding equation has a second exact positive ledger.  Write

\[
 D_j=\tau^jD,\quad
 a_j=\delta(D_j),\quad
 b_j=\delta(\phi D_j),\quad
 c_j=d_0(D_j),\quad
 \widehat c_j=d_0(\phi D_j).
\]

The two block identities are

\[
 c_j=N-a_j-b_j,
 \qquad
 \widehat c_j=N-b_j-a_{j+1}.
 \tag{3.12}
\]

Hence

\[
 a_{j+1}-a_j-c_j=-\widehat c_j.
 \tag{3.13}
\]

If \(\sum_{j<s}c_j=a_s\), telescoping (3.13) gives

\[
 \boxed{\sum_{j=0}^{s-1}\widehat c_j=a_0.}
 \tag{3.14}
\]

### Theorem 3.4 (two-sided primal/dual sector boundary is negligible)

For a zero-winding pair \((D,s)\), put

\[
 T^+(D,s)=\sum_{j=0}^{s-1}d_0(\tau^jD)=\delta(\tau^sD),
\]

\[
 T^-(D,s)=\sum_{j=0}^{s-1}d_0(\phi\tau^jD)=\delta(D).
 \tag{3.15}
\]

Let \(\mathcal Z_m^\partial(H,U)\) be the set of such pairs with
\(1\le s\le H\) for which at least one of the four quantities

\[
 T^+,\quad 2m-T^+,\quad T^-,\quad 2m-T^-
 \tag{3.16}
\]

is at most \(U\), where \(1\le U\le m\).  Then

\[
 \boxed{
 |\mathcal Z_m^\partial(H,U)|
 \le C'HUm^2 4^m
       \exp\!\left(-c\sqrt{m/U}\right)}
 \tag{3.17}
\]

for an absolute \(C'\).  In particular, if \(H\le m\) and

\[
 U=o(m/\log^2m),
 \tag{3.18}
\]

then

\[
 \boxed{|\mathcal Z_m^\partial(H,U)|=o(B_m/N).}
 \tag{3.19}
\]

#### Proof

The number of words with \(\delta(D)\le U\) is
\(\sum_{t\le U}M_{m,t}\).  By the involution (3.10)--(3.11), the same
quantity upper-bounds the number with \(\delta(D)\ge2m-U\).

For \(T^+\), fix \(s\) and use the endpoint bijection
\(D\mapsto\tau^sD\).  For \(T^-\), use (3.14) and the start word \(D\)
itself.  A union bound over the two ledgers, two boundary ends, and
\(s\le H\) gives

\[
 |\mathcal Z_m^\partial(H,U)|
 \le 4H\sum_{t=1}^U M_{m,t}.
\]

Lemma 3.1 proves (3.17), and the same polynomial-absorption argument as in
Theorem 3.2 proves (3.19). \(\square\)

## 4. Combined periodic obstruction and exact remaining boundary

Let

\[
 H=\lceil A\sqrt m\rceil,
 \qquad
 P_m=o(m/\log m),
 \qquad
 T_m=o(m/\log^2m).
\]

Let \(\mathcal P_m\) be any pairwise quotient-edge-disjoint family of
zero-winding intervals with step-two length at most \(H\).  Split it into

* intervals on \(\tau\)-cycles of period at most \(P_m\);
* intervals on longer cycles but with accumulated sector mass at most
  \(T_m\);
* the remaining intervals.

Corollary 2.2 makes the first class \(o(B_m/N)\), and Theorem 3.2 makes the
second class \(o(B_m/N)\).  Therefore every possible failure of the
quotient residence gate must be carried by the third class.  Such an
interval simultaneously obeys

\[
 \operatorname{per}_\tau(D)>P_m,
 \qquad
 \sum_{j=0}^{s-1}(2b_0(T_j)+1)>T_m.
 \tag{4.1}
\]

Theorem 3.4 strengthens the second inequality symmetrically: after another
\(o(B_m/N)\) deletion, both the primal and half-shifted dual sector totals
lie in

\[
 (T_m,\,2m-T_m).
 \tag{4.2}
\]

For example, taking any \(\omega(m)\to\infty\) and

\[
 P_m=\frac{m}{\omega(m)\log m},
 \qquad
 T_m=\frac{m}{\omega(m)\log^2m}
\]

(with integer parts understood) shows that bounded-period repetition and
low-sector iteration can both be discarded at the exact quotient scale.

This is a genuine no-go, not a proof of \(\mathrm{RP}_A\).  It leaves open
long trajectories in which the first-deepest-sector transport repeatedly
moves root suffix forests of average size at least roughly
\(\sqrt m/\log^2m\).  Neither the period count nor endpoint early-maximum
rarity controls that high-sector class.

## 5. Audit of the decisive points

1. **Phase convention.**  With \(x=b-1\), (1.3) gives
   \((a,x,c)\mapsto(c,a,x)\), not \((x,c,a)\).  The three deficits are
   therefore \(2c+1,2x+1,2a+1\) in that order.

2. **Floor versus congruence.**  Theorem 1.1 uses the integer
   zero-winding equation, not merely congruence modulo \(N\).  The bound
   for \(s\ge4\) compares the left side with the literal endpoint
   \(\delta<N\).

3. **Boundary orbit count.**  For \(n>0\), a rotation-fixed weak
   three-composition is \((n/3,n/3,n/3)\) and has no zero coordinate.
   Hence division of the \(3n\) boundary compositions by three is exact.

4. **Packing trace.**  The two sector-carrying quotient edges are contained
   in the literal residence interval.  Intersection of these two-edge
   subtraces is sufficient to forbid simultaneous selection; no assertion
   that they exhaust the residence trace is used.  These period-three
   projections are part of the short-cycle term, so Theorem 1.2 is not a
   statement about the separately defined nonwrapping \(\overline\nu_H\).

5. **Endpoint injection.**  In Theorem 3.2, \(\tau^s\) is bijective only
   after \(s\) is fixed.  This is why the safe factor \(H\) remains in
   (3.5).

6. **Asymptotic scope.**  The little-oh hypothesis
   \(T_m=o(m/\log^2m)\) is essential.  At a fixed positive multiple of
   \(m/\log^2m\), Lemma 3.1 yields only a fixed polynomial saving whose
   exponent depends on that multiple; no uniform \(o(B_m/N)\) is claimed
   there.

7. **Late-endpoint involution.**  Reversal alone does not preserve Dyck
   words.  The operation in (3.10) reverses and complements.  It sends the
   last maximum of \(D\), rather than its first maximum, to the first
   maximum of \(D^\dagger\); this is sufficient for the one-sided
   implication used in Theorem 3.4.
