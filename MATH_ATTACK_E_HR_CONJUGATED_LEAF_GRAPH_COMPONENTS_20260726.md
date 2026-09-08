# Lane E: components of the \(H_r\)-conjugated leaf-rotation graph

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let

\[
 H_r=\langle(2\ 3),(4\ 5),\ldots,(2r-2\ 2r-1)\rangle
 \cong(C_2)^{r-1},
 \tag{0.1}
\]

and let \(\mathcal G_r\) be the graph on the Dyck roots
\(\mathcal D_r\) whose edges are all \(H_r\)-translates of all contextual
leaf rotations

\[
                         1100R\longleftrightarrow1010R.
 \tag{0.2}
\]

The graph is connected for \(r\le3\) and disconnected for every \(r\ge4\).
There is a complete component invariant.

Pair the nonterminal coordinates of a Dyck word as

\[
 (2,3),(4,5),\ldots,(2r-2,2r-1).
\]

The pair sums form a Motzkin excursion \(M\) of length \(r-1\).  A level
step remembers whether its pair is \(10\) or \(01\).  Replace every
occurrence \(UD\) in \(M\) by two level steps.  The occurrences are
disjoint, so this gives a canonical \(UD\)-free excursion
\(\operatorname{nf}(M)\).

In that normal excursion, call a level position **rigid** when

1. it is isolated, i.e. neither neighbour is level; and
2. its previous step is \(D\), or its next step is \(U\).

Boundary sentinels are neither \(D\) nor \(U\).  Then two Dyck roots lie in
the same component of \(\mathcal G_r\) if and only if

1. their Motzkin excursions have the same \(UD\)-free normal form; and
2. the \(10/01\) orientations agree at every rigid level position of that
   normal form.

Consequently, if \(g_r\) is the number of components, then

\[
\boxed{
 g_r=
 \sum_{\substack{M\text{ Motzkin excursion}\\
                 |M|=r-1,\ UD\not\subset M}}
 2^{\rho(M)},}                                          \tag{0.3}
\]

where \(\rho(M)\) is the number of rigid level positions.  In particular

\[
                         g_1,g_2,g_3,g_4,g_5
                         =1,1,1,2,6.                    \tag{0.4}
\]

Thus root-scale \(H_r\) conjugation merges the two leaf components at
\(r=3\), exactly as witnessed by the five-row pentagon, but it does not
produce a Catalan conveyor in all dimensions.

## 1. Dyck roots as decorated Motzkin excursions

Write a Dyck word \(w\in\mathcal D_r\) in the form

\[
 w=1\,(b_1c_1)(b_2c_2)\cdots(b_{r-1}c_{r-1})\,0.
 \tag{1.1}
\]

For \(1\le i\le r-1\), put

\[
 s_i=b_i+c_i-1\in\{-1,0,1\}.
 \tag{1.2}
\]

Interpret \(1,0,-1\) as Motzkin steps \(U,L,D\), respectively.

### Lemma 1.1 (orbit quotient)

The word \(s_1\cdots s_{r-1}\) is a Motzkin excursion.  Two Dyck words lie
in the same \(H_r\)-orbit if and only if they give the same Motzkin
excursion.  Over a level step, the two points of the orbit are the
orientations

\[
                         10,\qquad01.                    \tag{1.3}
\]

Thus an orbit with \(\ell\) level steps has \(2^\ell\) elements.

#### Proof

After the first bit and the first \(i\) pairs, the Dyck height is

\[
 1+2\sum_{j=1}^is_j.
 \tag{1.4}
\]

It is a positive odd integer, so every partial sum in (1.4) is
nonnegative.  The total sum is zero because \(w\) has \(r\) ones.
Therefore the pair-sum word is a Motzkin excursion.

The generators in (0.1) independently reverse the two bits of every pair.
They fix pairs \(11,00\) and interchange the two orientations in (1.3).
This proves the orbit statement. \(\square\)

## 2. The two induced local moves

The starting position of a contextual leaf rotation has either parity.

### Lemma 2.1 (even-start move)

At an even starting position, the induced decorated-Motzkin move is

\[
 \boxed{
 UD\longleftrightarrow L_\varepsilon L_\eta
 \qquad(\varepsilon,\eta\in\{10,01\}).}
 \tag{2.1}
\]

All decorations outside the displayed positions are arbitrary and
unchanged.

#### Proof

The four bits of \(1100\) occupy two complete pairs and have pair sums
\((2,0)\), hence steps \(UD\).  The four bits of \(1010\) have pair sums
\((1,1)\).  Conjugating by the two corresponding generators of \(H_r\)
gives all four choices of their level orientations.  Generators on other
level pairs give arbitrary common outside decorations. \(\square\)

Every \(UD\) occurrence is a literal primitive \(1100\) subexcursion, so
it is node-aligned and (2.1) is available at every such position.

### Lemma 2.2 (odd-start move)

Let position \(i\) be a level step.  Its orientation can be flipped while
the Motzkin excursion and all other level orientations are fixed if and
only if

\[
                 s_{i-1}\ne D,\qquad s_{i+1}\ne U,       \tag{2.2}
\]

where the two boundary sentinels satisfy both inequalities.

#### Proof

At an odd start the middle two bits of the leaf relation are one complete
pair.  The relation is

\[
                         1(10)0\longleftrightarrow1(01)0.
 \tag{2.3}
\]

The preceding outer bit can be made \(1\) precisely when the preceding
pair is \(U\) or level, or when it is the initial sentinel; it cannot when
the preceding step is \(D\).  Likewise the following outer bit can be made
\(0\) precisely when the following pair is \(D\) or level, or when it is
the terminal sentinel; it cannot when the following step is \(U\).
The relevant \(H_r\) generators choose the needed orientations of
neighbouring level pairs, while all other generators prescribe arbitrary
common decorations.  This proves necessity and sufficiency. \(\square\)

Lemmas 2.1--2.2 give every edge of \(\mathcal G_r\): parity exhausts the
possible starts of (0.2).

## 3. The Motzkin normal form

Orient (2.1) by

\[
                         UD\longrightarrow LL.           \tag{3.1}
\]

### Lemma 3.1 (confluence)

Repeated application of (3.1) terminates and has a unique undecorated
normal form, obtained by replacing every \(UD\) occurrence of the original
Motzkin excursion by \(LL\).

#### Proof

Each move reduces the number of nonlevel steps by two.  Two occurrences
of \(UD\) cannot overlap, because the common letter would have to be both
\(D\) and \(U\).  Replacing one occurrence by \(LL\) creates no new
\(UD\).  Hence all reductions commute and the result is unique.
\(\square\)

Write \(\operatorname{nf}(M)\) for this \(UD\)-free normal form.

### Lemma 3.2 (the normal form is invariant)

Every move in Lemmas 2.1--2.2 preserves
\(\operatorname{nf}(M)\).

#### Proof

The odd-start move leaves \(M\) unchanged.  The two sides of (2.1)
reduce to the same \(LL\) word. \(\square\)

## 4. Rigid level orientations

Let \(N=\operatorname{nf}(M)\).  A level step of \(N\) is **rigid** if it
is isolated and its previous step is \(D\) or its next step is \(U\).

### Lemma 4.1 (rigid decorations are invariant)

The \(10/01\) decoration at every rigid position of \(N\) is constant on a
component of \(\mathcal G_r\).

#### Proof

An even-start move affects two adjacent level positions in \(N\), so it
cannot alter a rigid position.  An odd-start flip is forbidden at a rigid
position by (2.2).

More explicitly, before normalization an adjacent \(UD\) may be replaced
by \(LL\).  The two new level positions are adjacent and hence nonrigid.
If one is adjacent to a pre-existing level position, that position is also
nonisolated.  Thus normalization never hides an allowed change at a rigid
position. \(\square\)

### Lemma 4.2 (all nonrigid decorations are flexible)

For a fixed normal form \(N\), any two decorations agreeing at the rigid
positions are joined in \(\mathcal G_r\).

#### Proof

First reduce both roots to the common normal form using (3.1); Lemma 2.1
allows arbitrary decorations on each newly created \(LL\) pair.

Inside a run of at least two level steps, use

\[
 L_\varepsilon L_\eta\longrightarrow UD
 \longrightarrow L_{\varepsilon'}L_{\eta'}
\]

to prescribe the two decorations arbitrarily.  Overlapping adjacent pairs
therefore prescribe an entire level run.

Any remaining nonrigid level is isolated.  Since it is not rigid, its
previous step is not \(D\) and its next step is not \(U\).  Lemma 2.2
flips it.  Hence every nonrigid decoration is independently adjustable.
\(\square\)

## 5. Complete component theorem

### Theorem 5.1

Two roots \(w,w'\in\mathcal D_r\) are connected in \(\mathcal G_r\) if and
only if

1. \(\operatorname{nf}(M(w))=\operatorname{nf}(M(w'))\); and
2. their decorations agree at every rigid position of that normal form.

#### Proof

Necessity is Lemmas 3.2 and 4.1.  For sufficiency, reduce both roots to
their common normal skeleton and apply Lemma 4.2. \(\square\)

For \(r=3\), the two Motzkin excursions are \(LL\) and \(UD\), both with
normal form \(LL\), and there are no rigid positions.  Hence
\(\mathcal G_3\) is connected.  For \(r=4\), the normal forms \(LLL\) and
\(ULD\) are distinct, so \(\mathcal G_4\) is disconnected.  Appending
level steps gives distinct normal forms in every larger dimension, proving
the connectivity claims in Section 0.

## 6. Component generating function

For a \(UD\)-free Motzkin excursion \(M=s_1\cdots s_n\), put

\[
\rho(M)=\#\{i:s_i=L,\ s_{i-1},s_{i+1}\ne L,\ 
                    (s_{i-1}=D\text{ or }s_{i+1}=U)\},    \tag{6.1}
\]

with boundary sentinels which are neither \(D\) nor \(U\).

Theorem 5.1 gives the exact ordinary generating function

\[
\boxed{
 C(z)=\sum_{r\ge1}g_rz^{r-1}
 =\sum_{\substack{M\text{ Motzkin excursion}\\UD\not\subset M}}
      2^{\rho(M)}z^{|M|}.}                              \tag{6.2}
\]

This is a finite-memory weighted Motzkin generating function.  Equivalently
its coefficients are obtained by the following exact transfer rule:

1. take nonnegative walks with steps \(U,L,D\), beginning and ending at
   height zero;
2. forbid the adjacent transition \(UD\);
3. give a maximal level run weight one when its length is at least two;
4. give an isolated level step weight two except when its neighbours are
   \(U,D\) or both are boundary sentinels, in which cases give weight one.

Multiplying the run weights and summing gives \(g_{n+1}\).

The first cases are

\[
\begin{array}{c|l|c}
n&UD\text{-free normal excursions and weights}&g_{n+1}\\ \hline
0&\varnothing&1\\
1&L&1\\
2&LL&1\\
3&LLL,\ ULD&2\\
4&LLLL,\ ULLD,\ ULDL,\ LULD&1+1+2+2=6.
\end{array}                                              \tag{6.3}
\]

This proves (0.3)--(0.4).

## 7. Consequence for exact switches

Edge transpositions of a graph generate the full symmetric group on each
connected component.  Therefore the exact leaf-rectangle switches and all
their \(H_r\)-conjugates generate precisely

\[
 \boxed{
 \prod_{K\in\pi_0(\mathcal G_r)}\operatorname{Sym}(K),}
 \tag{7.1}
\]

with the components classified by Theorem 5.1.  They generate
\(\operatorname{Sym}(\mathcal D_r)\) only for \(r\le3\).

The five-row \(D_3\) pentagon is therefore the last dimension in which
root-scale \(H_r\) conjugation alone gives a full Catalan conveyor.  Any
all-\(r\) construction must add a move which changes the normal Motzkin
skeleton in a way not generated by \(UD\leftrightarrow LL\), or changes a
rigid level orientation.
