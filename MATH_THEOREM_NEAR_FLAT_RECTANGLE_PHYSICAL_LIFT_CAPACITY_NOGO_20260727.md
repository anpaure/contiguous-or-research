# Near-flat rectangle lifting: exact formal generation, physical orbit obstruction, and sharp bank capacity

Date: 2026-07-27

Method: pure mathematics only.  No computation, search, solver, web
input, or probabilistic construction is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
\]

\[
 N=\binom{2m}{M},\qquad W=\binom{2m}{m},\qquad
 T=dN=W-o(W),
\tag{0.1}
\]

and assume \(H\ge3\), \(m\ge6H+4\), and the calibrated common-core
regime.  Let \(A\) be the singleton-incidence matrix on
\(\Omega=\binom{[2m]}m\), and let

\[
 \rho(R;a,b,z,z')=
 e_{R\cup\{a,z\}}+e_{R\cup\{b,z'\}}
 -e_{R\cup\{a,z'\}}-e_{R\cup\{b,z\}},
\tag{0.2}
\]

where \(|R|=m-2\) and \(a,b,z,z'\) are distinct outside \(R\).

The exact conclusions are as follows.

1. The vectors (0.2), each of which is realized by the proved literal
   two-top collar-neutral macro, generate \(\ker_{\mathbb Z}A\).  Thus
   every same-singleton-marginal displacement has a formal signed lift
   with zero derivative at every protected depth other than the middle.

2. Every nonzero pair of *first-boundary* swaps whose other protected
   decks cancel is necessarily of the form (0.2).  On each participating
   top the transition lies in one fixed two-state orbit

   \[
       (a,b,\tau)\longleftrightarrow(b,a,\tau).
   \tag{0.3}
   \]

   Re-pairing companions and renaming the declared core do not change
   this orbit.

3. Hence a chronology made only of these rectangle macros has endpoint
   middle variation at most \(N\), irrespective of how many times its
   tops are reused.  The physical master-order coefficient has a
   same-marginal low-collision target at variation \((1-o(1))W\), so
   the requested physical lifting theorem is false for this move
   library, even with exactly zero boundary loss.

4. More generally, every successful augmented bank must have nearly
   maximal middle-deck mobility \(d\) on all but \(o(N)\) tops.  A fixed
   universal bank needs \((1-o(1))W\) independent rectangle directions.

5. There are explicit abstract loads in the legal near-flat marginal
   regime, both having \(o(W)\) collisions, whose difference needs

   \[
                         \Omega(W\sqrt m)
   \tag{0.4}
   \]

   elementary rectangle occurrences.  Thus even a target-dependent
   atomic bank can require average top-toggle multiplicity
   \(\Omega(m^{3/2})\).  These last endpoints are abstract fibre loads,
   not asserted to be physical common-core coefficients.

The smallest surviving positive statement is therefore not another
rectangle decomposition.  It is an orbit-recharge theorem supplying,
on almost every top, connectors between enough distinct orbits (0.3) to
give local middle-deck diameter \((1-o(1))d\), while retaining the common
protected-row and owner-capacity ledgers.

## 1. Formal rectangle generation

For an integral zero-total vector \(z\), define its rectangle word norm

\[
 \|z\|_\square=\min\left\{
   \sum_j|\lambda_j|:
   z=\sum_j\lambda_j\rho_j,
   \quad \lambda_j\in\mathbb Z
 \right\}.
\tag{1.1}
\]

### Lemma 1.0 (bipartite swap distance)

Let \(G,G'\) be two finite simple bipartite graphs on the same labelled
bipartition and with the same degree at every vertex.  Then \(G\) can be
changed into \(G'\) by at most

\[
                         |E(G)\setminus E(G')|
\tag{1.1a}
\]

legal two-row, two-column switches.

#### Proof

Colour \(E(G)\setminus E(G')\) red and
\(E(G')\setminus E(G)\) blue.  At every vertex the red and blue degrees
are equal, so the coloured symmetric difference decomposes into
alternating circuits.  Process one circuit at a time.

For completeness, the usual circuit induction is as follows.  A
four-edge circuit is one legal switch.  On a longer circuit, label the
successive red row--column edges
\(x_i y_i\) and the blue edges \(x_{i+1}y_i\), cyclically.  If the
fan chord needed to switch \(x_1y_1,x_2y_2\) is absent, that switch
installs the blue edge \(x_2y_1\) and leaves an alternating circuit two
edges shorter.  If the fan chord is already occupied, take the first
occupied fan chord; it splits the circuit into two shorter alternating
circuits, and apply the induction to those two circuits before removing
the chord.  In either case a circuit with \(k\) red edges is processed
in at most \(k-1\) switches.  No edge outside the circuit and its fan
chords is changed at the end.  Summing over the disjoint circuit
decomposition uses at most the total number of red edges, which is
(1.1a). \(\square\)

### Theorem 1.1 (exact lattice and a quantitative upper bound)

One has

\[
 \boxed{\operatorname{span}_{\mathbb Z}\{\rho\}=\ker_{\mathbb Z}A.}
\tag{1.2}
\]

Moreover, for every \(z\in\ker_{\mathbb Z}A\),

\[
 \boxed{\|z\|_\square
 \le {m(m-1)\over2}\|z\|_1.}
\tag{1.3}
\]

#### Proof

Every rectangle has zero singleton incidence, so the left side of
(1.2) is contained in the right side.

Write \(z=z^+-z^-\), and expand its positive and negative parts as two
multisets of

\[
                        t={1\over2}\|z\|_1
\tag{1.4}
\]

middle sets.  Their row-coordinate bipartite incidence graphs have row
degree \(m\).  The equation \(Az=0\) says that their coordinate degrees
are equal.  Lemma 1.0 transforms the first graph into the second using
at most \(mt\) two-row switches, because the first graph has \(mt\)
incidences.

One switch replaces rows \(P,Q\) by

\[
 P'=P-\{a\}+\{b\},\qquad
 Q'=Q-\{b\}+\{a\},
\tag{1.5}
\]

where \(a\in P\setminus Q\), \(b\in Q\setminus P\).  On the ground set
with \(a,b\) removed, join \(P-\{a\}\) to \(Q-\{b\}\) by a Johnson
geodesic \(K_0,\ldots,K_s\), where \(s\le m-1\).  Put

\[
                         g(K)=e_{K\cup\{b\}}-e_{K\cup\{a\}}.
\]

For adjacent \(K_i=C\cup\{z\}\),
\(K_{i+1}=C\cup\{z'\}\), the difference
\(g(K_i)-g(K_{i+1})\) is one rectangle (0.2), up to sign.  The path
telescopes to

\[
                         e_{P'}+e_{Q'}-e_P-e_Q.
\]

Thus every switch is a sum of at most \(m-1\) rectangles.  This proves
(1.2), and the bounds \(mt\) and \(m-1\), together with (1.4), prove
(1.3). \(\square\)

Theorem 1.1 is an equality of signed lattices.  It supplies neither a
nonnegative route nor one current path option at each top.

## 2. Classification of every collar-neutral first-boundary pair

For a top \(U\) and a rooted injective word

\[
                         p=(a,b,c_1,c_2,\ldots,c_{M-2}),
\tag{2.1}
\]

put

\[
 \mathcal D_h(U,p)=
 \sum_{i=1}^{d}e_{U\setminus\{p_i,\ldots,p_{i+h-1}\}}
 \qquad(0\le h\le2H).
\tag{2.2}
\]

Let \(sp=(b,a,c_1,c_2,\ldots)\).  The decks at \(h=0,1\) are equal.
For \(h\ge2\), only phase two changes, and, on writing

\[
 K_h=U\setminus\{a,b,c_1,\ldots,c_{h-1}\},
\]

one has the exact identity

\[
 \mathcal D_h(U,sp)-\mathcal D_h(U,p)
 =e_{K_h\cup\{b\}}-e_{K_h\cup\{a\}}.
\tag{2.3}
\]

### Theorem 2.1 (uniqueness of the two-top rectangle)

Suppose two nondegenerate first-boundary swaps on distinct tops have
aggregate derivative zero for every \(0\le h\le2H\), \(h\ne H\).
If their middle derivative is nonzero, then, after relabelling and
reversing the common orientation, the following all hold.

1. Both swaps use the same unordered pair \(\{a,b\}\), with opposite
   orientations.
2. Their sets \(K_h,K'_h\) are equal for
   \(2\le h\le2H\), \(h\ne H\).
3. The two tops are adjacent in \(J(2m,M)\).
4. Their first tail letters \(c_1,c'_1\) are the distinct auxiliary
   labels which distinguish the two tops.  After those letters, and up
   through the visible \(2H\)-collar, the ordered tails agree except that
   the letters in positions \(H-1,H\) are transposed.
5. With \(R=K_{H+1}\), their middle derivative is exactly (0.2).

#### Proof

At \(h=2\), each nondegenerate derivative (2.3) is one oriented edge of
the Johnson graph.  Equality of one signed basis difference with the
negative of another uniquely determines its two endpoints, hence its
common intersection and ordered exchanged pair.  This proves Item 1 and
\(K_2=K'_2\).  Applying the same uniqueness at every \(h\ne H\) proves
Item 2.

Write the second tail as \((c'_1,c'_2,\ldots)\).  From

\[
 K_{j+1}=K_j\setminus\{c_j\},\qquad
 K'_{j+1}=K'_j\setminus\{c'_j\},
\tag{2.4}
\]

the consecutive equalities on either side of \(H\) give

\[
 c_j=c'_j\quad(2\le j\le H-2),
 \qquad
 c_j=c'_j\quad(H+1\le j\le2H-1).
\tag{2.5}
\]

At the missing equality, \(K_{H-1}=K'_{H-1}\) and
\(K_{H+1}=K'_{H+1}\) imply

\[
 \{c_{H-1},c_H\}=\{c'_{H-1},c'_H\}.
\tag{2.6}
\]

If the two ordered pairs agree, then \(K_H=K'_H\) and the middle
derivative is zero.  Therefore the nonzero case transposes them.  Put

\[
 c_{H-1}=z,qquad c_H=z',qquad R=K_{H+1}.
\]

Then

\[
 K_H=R\cup\{z'\},\qquad K'_H=R\cup\{z\},
\]

and substitution in (2.3) gives (0.2).

Finally \(K_2=K'_2\) says that the tops have the form

\[
 U=K_2\cup\{a,b,c_1\},\qquad
 U'=K_2\cup\{a,b,c'_1\}.
\]

They are distinct, so \(c_1\ne c'_1\), and hence they share exactly
\(M-1\) labels.  This proves Items 3--4. \(\square\)

For a fixed rectangle, let

\[
 S=R\cup\{a,b,z,z'\},\qquad |S|=m+2.
\]

Its eligible tops are \(S\cup E\), where
\(E\in\binom{[2m]\setminus S}{H-2}\).  Its eligible top pairs form
\(J(m-2,H-2)\).  Consequently there are exactly

\[
 V_S=\binom{m-2}{H-2}
\tag{2.7}
\]

eligible tops and

\[
 E_S={1\over2}\binom{m-2}{H-2}(H-2)(m-H)
\tag{2.8}
\]

eligible unordered top pairs.  Every capacity vector \((c_U)\) must
therefore obey the fixed-support cut

\[
 2\,r_S\le\sum_{U\supset S}c_U
\tag{2.9}
\]

if it is to install \(r_S\) occurrences of that rectangle.

## 3. The intrinsic two-state orbit and failure of recycling

For a rooted top word define

\[
 \mathcal O(a,b,\tau)=\{(a,b,\tau),(b,a,\tau)\}.
\tag{3.1}
\]

Every local endpoint of a rectangle from Theorem 2.1 toggles one such
orbit and leaves the whole ordered suffix \(\tau\) fixed.

### Theorem 3.1 (parity normal form)

In every chronology consisting only of the collar-neutral first-boundary
rectangles, the endpoint deck difference is

\[
 \Delta_h^{\rm end}=
 \sum_{\mathcal O:\,t_{\mathcal O}\ {\rm odd}}
       \epsilon_{\mathcal O}\,
       \bigl(\mathcal D_h(p^1_{\mathcal O})
             -\mathcal D_h(p^0_{\mathcal O})\bigr),
\tag{3.2}
\]

where \(t_{\mathcal O}\) is the number of toggles and
\(\epsilon_{\mathcal O}\in\{-1,1\}\) records the initial shore.
In particular,

\[
 \boxed{{1\over2}\|\Delta_H^{\rm end}\|_1\le N.}
\tag{3.3}
\]

If every top is restored, every deck derivative is zero.

#### Proof

On one orbit, successive derivatives alternate \(\delta,-\delta,
\delta,-\delta,\ldots\).  Their sum is zero after an even number of
uses and \(\pm\delta\) after an odd number.  Summing over orbits gives
(3.2).  At the middle, \(\delta\) is one unit transfer and has
\(\ell_1\)-norm two.  A one-path-per-top table can end in at most one
odd orbit on each of its \(N\) tops, proving (3.3). \(\square\)

Changing the declared protected core, filler names, landmarks, or
companion pairing cannot alter (3.1), because every permitted physical
transition still changes only the first two letters.  A re-rooting or a
suffix-changing neutral connector is a new move, not recycling of the
existing rectangle.

This specializes the option-flow criterion in
`MATH_THEOREM_COLLAR_NEUTRAL_RECTANGLE_BANK_LITERAL_SPLICE_AND_INSTALLABILITY_20260727.md`:
without a separate connector, every local option component is just
\(K_2\).  Therefore a long single-source/single-sink trail in that
option graph does not exist.

## 4. A genuine physical source that cannot be lifted

Let \(K^\sigma\) be the master-order common-core coefficient.  Its
middle support is contained in a family \(\mathcal A_\sigma\) with

\[
 |\mathcal A_\sigma|
 \le2m\binom{2m-H}{m}
 \le2m\,2^{-H}W=o(W).
\tag{4.1}
\]

Its singleton marginals lie in the exact legal interval.  Hence
`MATH_THEOREM_NEAR_FLAT_MARGINAL_FIBRE_ROUNDING_20260727.md` supplies a
nonnegative integral load \(L\) with the same total and singleton
marginals and

\[
                             \Psi(L)=o(W).
\tag{4.2}
\]

### Theorem 4.1 (physical-source counterexample)

One has

\[
 \boxed{{1\over2}\|K^\sigma-L\|_1=(1-o(1))W.}
\tag{4.3}
\]

Therefore no chronology of the rectangles in Theorem 2.1 connects the
physical coefficient \(K^\sigma\) to \(L\).

#### Proof

For every integer \(x\ge0\),

\[
                             x\le1+\binom x2.
\]

Thus the mass of \(L\) on \(\mathcal A_\sigma\) is at most

\[
 \sum_{D\in\mathcal A_\sigma}L_D
 \le|\mathcal A_\sigma|+\Psi(L)=o(W).
\tag{4.4}
\]

The load \(K^\sigma\) vanishes off \(\mathcal A_\sigma\), while both
loads have total \(T=(1-o(1))W\).  Hence the mass of \(L\) outside
\(\mathcal A_\sigma\), which is \((1-o(1))W\), is a lower bound for
their total variation.  The reverse bound is their common total \(T\),
proving (4.3).  But (3.3) is only

\[
                         N={T\over d}=(1+o(1)){W\over m}=o(W).
\]

This contradiction proves the final assertion. \(\square\)

Although \(A(L-K^\sigma)=0\), so Theorem 1.1 gives a formal rectangle
sum, no nonnegative rectangle chronology realizes it.

There is also a step-count lower bound independent of the orbit
obstruction.  Put

\[
                         E(X)=\sum_D(X_D-1)_+.
\]

Then

\[
 E(K^\sigma)=T-|\operatorname{supp}K^\sigma|=(1-o(1))W,
 \qquad E(L)\le\Psi(L)=o(W).
\]

One rectangle has two negative cells and can lower \(E\) by at most two.
Consequently every hypothetical legal atomic route would need at least

\[
                         \left({1\over2}-o(1)\right)W
\tag{4.5}
\]

rectangle occurrences.  The constant \(1/2\) is sharp for this ledger.
A top-disjoint bank has at most \(N/2=o(W)\) rectangles and is therefore
too small.  Even before the stronger orbit-parity obstruction is used,
(4.5) forces total top incidence \((1-o(1))W\), or average incidence
\((1-o(1))m\) over the \(N\) tops.

## 5. Sharp mobility requirement for any augmented physical bank

Let \(\mathcal C_U\) be the set of path states accessible at top \(U\)
under an augmented bank, and define its middle-deck diameter

\[
 c_U=\max_{p,q\in\mathcal C_U}
 {1\over2}\|\mathcal D_H(U,p)-\mathcal D_H(U,q)\|_1.
\tag{5.1}
\]

### Theorem 5.1 (local-diameter capacity)

Every physical endpoint displacement \(Z\) obtainable by the bank
satisfies

\[
 \boxed{{1\over2}\|Z\|_1\le\sum_Uc_U,\qquad c_U\le d.}
\tag{5.2}
\]

If the bank connects its local states using \(B_U\) distinct
first-boundary unit-transfer edges at top \(U\), then

\[
                             c_U\le B_U.
\tag{5.3}
\]

For the displacement in Theorem 4.1 this forces

\[
 \sum_Uc_U\ge(1-o(1))dN.
\tag{5.4}
\]

For every fixed \(\varepsilon>0\),

\[
 \boxed{
 |\{U:c_U<(1-\varepsilon)d\}|=o(N).}
\tag{5.5}
\]

#### Proof

Write the endpoint coefficient difference as the sum of its one-top
deck differences and apply the triangle inequality.  Two decks of mass
\(d\) have total variation at most \(d\), proving (5.2).  A shortest
simple path in a finite local option graph uses no edge twice; every
first-boundary edge has middle variation one, proving (5.3).

Equations (4.3) and (5.2) give (5.4).  Since each summand is at most
\(d\), a positive proportion of summands deficient by at least
\(\varepsilon d\) would contradict (5.4).  This proves (5.5). \(\square\)

The bare rectangle library has \(c_U=1\).  Thus its failure is not
merely that it averages fewer than \(m\) chronological uses per top:
repeated use of its one edge is algebraically null.  A successful
recharge must expose \((1-o(1))d\) genuinely different middle transfers
on almost every top.

## 6. A fixed universal bank needs almost full rank

The rows of \(A\) are linearly independent.  Indeed, if
\(\sum_{i\in D}\alpha_i=0\) for every middle set \(D\), comparison of
two sets differing by \(i\leftrightarrow j\) gives
\(\alpha_i=\alpha_j\); then \(m\alpha_i=0\).  Hence

\[
                         \operatorname{rank}A=2m,
 \qquad \dim\ker A=W-2m.
\tag{6.1}
\]

### Theorem 6.1 (universal direction-bank lower bound)

Let \(L^0\) be a nonnegative integral load of total \(W-K_0\), where
\(K_0\ge0\), and put \(\Psi_0=\Psi(L^0)\).  A fixed bank capable of realizing every
same-marginal low-collision correction from \(L^0\) must contain at
least

\[
 \boxed{W-2m-4K_0-8\Psi_0}
\tag{6.2}
\]

linearly independent rectangle directions.  In particular this is
\((1-o(1))W\) when \(K_0+\Psi_0=o(W)\).

#### Proof

Choose \(W-2m\) linearly independent elementary rectangles, possible by
Theorem 1.1 and (6.1).  Let

\[
                         S=\{D:L^0_D\ne1\}.
\]

If \(E_0=\sum_D(L^0_D-1)_+\), then the number of zero cells is
\(K_0+E_0\), the number of overloaded cells is at most \(E_0\), and
\(E_0\le\Psi_0\).  Hence

\[
                         |S|\le K_0+2\Psi_0.
\tag{6.3}
\]

Conjugate the chosen rectangle basis by all ground-coordinate
permutations.  Each of the four cells of a fixed conjugated rectangle is
uniform on \(\Omega\), so the fraction of conjugates meeting \(S\) is at
most \(4|S|/W\).  By double counting, one conjugate basis has at least

\[
 W-2m-4|S|\ge W-2m-4K_0-8\Psi_0
\]

members supported wholly on load-one cells.  These members remain
linearly independent.  For each such oriented rectangle \(r\),

\[
 L^0+r\ge0,\qquad A(L^0+r)=AL^0,
 \qquad \Psi(L^0+r)=\Psi_0+2.
\]

The endpoint directions of a fixed bank which realizes all these
targets must span all these independent vectors.  This proves (6.2).
\(\square\)

If every direction is installed by a literal two-top macro and
\(W-K_0=dN\), then some top has bank incidence at least

\[
 {2(W-2m-4K_0-8\Psi_0)\over N}=(2-o(1))m.
\tag{6.4}
\]

This is a fixed-universal-bank bound.  A target-dependent adaptive bank
is addressed by the next section.

## 7. Quadratic rectangle distance and an amplified near-flat pair

### Theorem 7.1 (an exact \(s(m-s)\) rectangle metric)

Partition

\[
 [2m]=A_0\sqcup B_0\sqcup C_0\sqcup D_0,
 \qquad |A_0|=|B_0|=s,\quad |C_0|=|D_0|=m-s,
\]

and put

\[
 P=A_0\cup C_0,\quad Q=B_0\cup D_0,\quad
 P'=B_0\cup C_0,\quad Q'=A_0\cup D_0.
\]

Then

\[
 z_s=e_{P'}+e_{Q'}-e_P-e_Q
\]

satisfies

\[
 \boxed{\|z_s\|_\square=s(m-s).}
\tag{7.1}
\]

#### Proof

Order the four blocks.  Let \(A_i\) be obtained from \(A_0\) by
replacing its first \(i\) labels with the first \(i\) labels of \(B_0\),
and define \(C_j\) analogously using \(D_0\).  Put
\(S_{ij}=A_i\cup C_j\).  Every cell boundary

\[
 e_{S_{i,j-1}}+e_{S_{i-1,j}}
 -e_{S_{i-1,j-1}}-e_{S_{ij}}
\tag{7.2}
\]

is one elementary rectangle.  Summing over
\(1\le i\le s\), \(1\le j\le m-s\) telescopes to \(z_s\), proving the
upper bound.

For the lower bound define

\[
                         F(X)=\binom{|X\cap Q|}{2}.
\tag{7.3}
\]

If \(x_u=\mathbf1_{\{u\in Q\}}\), the mixed difference of \(F\) on an
elementary rectangle is

\[
                         (x_a-x_b)(x_z-x_{z'})\in\{-1,0,1\}.
\tag{7.4}
\]

But

\[
 \langle F,z_s\rangle
 =\binom s2+\binom{m-s}2-\binom m2
 =-s(m-s).
\tag{7.5}
\]

Every rectangle expression therefore has at least \(s(m-s)\) atoms.
Together with (7.2), this proves (7.1). \(\square\)

At \(s=\lfloor m/2\rfloor\), two collision-free loads

\[
 \mathbf1_\Omega-e_{P'}-e_{Q'},\qquad
 \mathbf1_\Omega-e_P-e_Q
\]

have total \(W-2\), identical singleton marginals \(W/2-1\), and exact
rectangle distance \(\lfloor m^2/4\rfloor\).

### Theorem 7.2 (Gaussian-stratum amplification)

For every \(T\le W\) with \(W-T=o(W)\), there are nonnegative integral
loads \(K,L\) of total \(T\), with identical aggregate-near-flat
singleton marginals and

\[
                         \Psi(K)+\Psi(L)=o(W),
\tag{7.6}
\]

such that

\[
 \boxed{\|L-K\|_\square=\Omega(W\sqrt m).}
\tag{7.7}
\]

#### Proof

Fix \(Q_0\in\Omega\).  For \(j<m/2\), the number of complementary
pairs \(\{D,D^c\}\) with \(|D\cap Q_0|=j\) is
\(\binom mj^2\).  At the central stratum there is only the harmless
factor \(1/2\).

Put

\[
 j_0=\lfloor m/2\rfloor,\qquad
 r=\left\lfloor{1\over2}\sqrt m\right\rfloor,
 \qquad t=\left\lfloor{W\over100\sqrt m}\right\rfloor.
\tag{7.8}
\]

The product formula for neighbouring coefficients gives, uniformly for
the two parities of \(m\),

\[
 \log{\binom m{j_0-r}\over\binom m{j_0}}
 =-{2r^2\over m}+o(1)=-{1\over2}+o(1).
\]

Also Stirling's formula gives
\(\binom m{j_0}^2=\Theta(W/\sqrt m)\), with a positive absolute
leading constant.  Hence

\[
 \binom m{j_0-r}^2
 =(e^{-1}+o(1))\binom m{j_0}^2
 =\Theta(W/\sqrt m)>t
\tag{7.9}
\]

for all sufficiently large \(m\); the same is true after the central
stratum's possible factor \(1/2\).  (The Stirling leading constants are
larger than \(1/100\).)

Hence choose \(t\) complementary pairs in the central stratum and
\(t\) in the displaced stratum; call their unions of sets
\(\mathcal B\) and \(\mathcal A\), respectively.  Define

\[
 K=\mathbf1_\Omega+\mathbf1_{\mathcal A}-\mathbf1_{\mathcal B},
 \qquad
 L=\mathbf1_\Omega-\mathbf1_{\mathcal A}+\mathbf1_{\mathcal B}.
\tag{7.10}
\]

Each complementary pair has singleton incidence \(\mathbf1\).  Thus
both loads have total \(W\) and singleton marginals exactly
\((W/2)\mathbf1\).  They take only the values \(0,1,2\), and each has
exactly \(2t\) cells of load two, so

\[
                         \Psi(K)=\Psi(L)=2t=o(W).
\tag{7.11}
\]

Use \(F(X)=\binom{|X\cap Q_0|}{2}\).  The sum of \(F\) on a
complementary pair with smaller intersection \(j\) is

\[
                         \binom m2-j(m-j).
\tag{7.12}
\]

Relative to the central stratum, the displaced pair increases (7.12)
by \(r^2\) if \(m\) is even and by \(r(r+1)\) if \(m\) is odd.
Since \(L-K=2(\mathbf1_{\mathcal B}-\mathbf1_{\mathcal A})\),

\[
                         |\langle F,L-K\rangle|\ge2tr^2.
\tag{7.13}
\]

Equation (7.4) holds for this \(F\) as well, so

\[
 \|L-K\|_\square\ge2tr^2=\Omega(W\sqrt m).
\]

For general \(T\), delete the same
\(\lfloor(W-T)/2\rfloor\) complementary pairs, chosen outside
\(\mathcal A\cup\mathcal B\), from both loads.  If \(W-T\) is odd,
delete one additional common set.  The difference and (7.13) are
unchanged; collisions do not increase.  The marginals are exactly
\(T/2\) when the deficit is even and differ from \(T/2\) by at most
\(1/2\) coordinatewise when it is odd.  Their normalized squared
deviation is then \(O(m/T^2)=o(1)\), proving the required near-flatness.
\(\square\)

Every atomic rectangle occurrence consumes two top-toggle slots.  Since
\(N=(1+o(1))W/m\), Theorem 7.2 forces average occurrence multiplicity
\(\Omega(m^{3/2})\) for any atomic bank servicing this pair.  This is an
atomic-catalogue statement: a genuinely larger physical macro which
realizes many rectangles at once is outside its hypothesis.

## 8. Exact boundary

Proved:

1. exact integral generation of every same-marginal displacement by the
   literal collar-neutral rectangle directions;
2. classification of every nonzero two-swap first-boundary cancellation;
3. the intrinsic \(K_2\)-orbit and parity normal form;
4. failure of physical rectangle-only lifting for a genuine master-order
   common-core source and its rounded low-collision target;
5. the nearly-maximal local-deck-diameter requirement for every augmented
   bank which could repair that source;
6. a \((1-o(1))W\) fixed-universal direction lower bound;
7. the exact metric \(s(m-s)\); and
8. an \(\Omega(W\sqrt m)\) atomic-occurrence lower bound inside the
   near-flat low-collision fibre.

Not proved:

1. a physical low-collision common-core coefficient;
2. an orbit-changing neutral recharge circuit;
3. an acyclic synchronized option flow with prefix owner capacity;
4. a larger macro which amortizes many elementary rectangles; or
5. coefficient one.

The smallest replacement lemma is therefore:

> **Near-full orbit-recharge lemma (unproved).**  On all but \(o(N)\)
> rank-\(M\) tops, connect first-boundary orbits by middle-neutral literal
> transitions so that the accessible middle-deck diameter is
> \((1-o(1))d\); synchronize these transitions across tops so that every
> nonmiddle protected-row derivative cancels and every prefix retains
> one physical option per top with aggregate owner excess \(o(W)\).

Theorems 3.1 and 5.1 show that both the orbit change and the near-full
diameter are necessary.  The present two-top rectangle relations supply
neither.
