# Audit of the proposed \(\mathbb Z_4^r\) phase factor

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Consider

\[
 X=\mathbb Z_4^r,
 \qquad
 F(x)=x+e_{1+s(x)},
 \qquad
 s(x):=\sum_{i=1}^r\widetilde x_i\pmod r,
 \tag{0.1}
\]

where \(\widetilde x_i\in\{0,1,2,3\}\), and indices are read modulo
\(r\).  The intended claim was that the updated coordinate runs through

\[
                 1,2,\ldots,r,1,2,\ldots,r,\ldots
\tag{0.2}
\]

and that the orbits give a \(C_{4r}\)-factor of \(X\).

The claim is true exactly in the three cases

\[
                         \boxed{r\in\{1,2,4\}.}
\tag{0.3}
\]

For every other \(r\), the map in (0.1) is not even a permutation.  In
particular it cannot be used for the intended power-of-two regime
\(r\ge8\).

For a fixed tensor cell and a fixed pair-frame resolution, the lower and
upper \(q\)-shadow maps can also be classified exactly in the three valid
cases.  Put \(h=2r\).  They are injective for

\[
                         1\le q\le r.
\tag{0.4}
\]

For \(q=r+k\), \(1\le k<r\), precisely \(k\) local squares are traversed
halfway and lose their phase.  The only surviving constraint on those
phases is their sum modulo \(r\).  Consequently:

* for \(r=2\), the first collision is at \(q=3\);
* for \(r=4\), \(q=5\) is still injective and the first collision is at
  \(q=6\);
* at \(q=2r\), every phase in a fixed tensor cell has the same half-cycle
  shadow.

The smallest explicit collisions are

\[
 (0,0)\sim(2,0)\quad(r=2,q=3),
 \qquad
 (0,0,0,0)\sim(1,3,0,0)\quad(r=4,q=6).
\tag{0.5}
\]

There is an even earlier comparison collision between the two local
associator resolutions: their four large squares have the same complete
depth-one lower and upper shadow supports.  Thus a resolution bit is an
unavoidable part of any cross-packet guard.

The exact repair target is a checksum which separates the collision
fibres, not merely a different tie-breaking rule.  Section 7 formulates
this as an erasure-checksum condition and gives explicit finite
checksums for the valid cases.  Realizing that checksum by physical guard
coordinates while preserving exact middle ownership is a separate gate;
the algebra below does not claim that realization for free.

## 1. The carry obstruction

Incrementing a coordinate in \(\mathbb Z_4\), while representing it by
\(0,1,2,3\), changes the integer sum by

\[
 \widetilde{x_i+1}-\widetilde x_i=
 \begin{cases}
 1,&x_i\ne3,\\
 -3,&x_i=3.
 \end{cases}
\tag{1.1}
\]

Thus the schedule parameter always advances by one modulo \(r\) exactly
when

\[
                         -3\equiv1\pmod r,
\tag{1.2}
\]

or equivalently \(r\mid4\).

### Theorem 1.1 (exact validity range)

The map \(F\) in (0.1) has schedule (0.2) and is a factor into
\(C_{4r}\)'s if and only if \(r\in\{1,2,4\}\).

#### Proof

Suppose first that \(r\mid4\).  Equation (1.1) gives

\[
                         s(Fx)=s(x)+1\pmod r.
\tag{1.3}
\]

Hence the updated coordinates occur in the cyclic order (0.2).  In
\(4r\) steps every coordinate is incremented four times, so
\(F^{4r}x=x\).  If \(F^t x=x\), the schedule position must first return,
so \(r\mid t\).  Each coordinate has then been incremented \(t/r\)
times; returning in \(\mathbb Z_4\) forces \(4\mid t/r\).  Therefore the
orbit length is exactly \(4r\).  The orbits partition \(X\), proving the
factor assertion.

Now suppose \(r\nmid4\).  The residues

\[
                         a=1,
 \qquad b=1+4\pmod r
\tag{1.4}
\]

are distinct.  Let \(y\in\mathbb Z_4^r\) have \(y_a=1\), \(y_b=0\),
and all other coordinates zero.  Then \(s(y)=1=a\).  There are two
preimages of \(y\):

* decrement coordinate \(a\) from \(1\) to \(0\); its sum is
  \(s(y)-1=0\), so (0.1) selects coordinate \(a=1\);
* decrement coordinate \(b\) from \(0\) to \(3\); its sum is
  \(s(y)+3=4\), so (0.1) selects coordinate \(b=1+4\pmod r\).

The preimages are distinct.  Hence \(F\) is not injective and therefore
not a permutation. \(\square\)

### Remark 1.2

The formula \(\sum x_i\pmod r\) behaves as a homomorphism out of
\(\mathbb Z_4^r\) precisely when \(r\mid4\).  The failed construction is
therefore a genuine carry error, not a defect in a later orbit count.

## 2. Local square notation

Fix one of the six local \(C_4\)-cells in one resolution of the
8-coordinate associator frame, and orient it as

\[
 A_K(0),A_K(1),A_K(2),A_K(3),A_K(0).
\tag{2.1}
\]

It is an isometric \(Q_2\).  Define its one-step and half-square traces

\[
 \begin{aligned}
 \ell_K(z)&=A_K(z)\cap A_K(z+1),
 &u_K(z)&=A_K(z)\cup A_K(z+1),\\
 \ell_K^{(2)}(z)&=A_K(z)\cap A_K(z+2),
 &u_K^{(2)}(z)&=A_K(z)\cup A_K(z+2).
 \end{aligned}
\tag{2.2}
\]

For the resolution \(\mathcal F_0\) of the local associator, there are
four large cells \(Q_0\cup Y\), \(Y\in\mathcal Y\), and two reservoir
cells \(ab\cup Q_R,cd\cup Q_R\).

### Lemma 2.1 (local trace signatures)

Within either fixed resolution:

1. the maps \((K,z)\mapsto\ell_K(z)\) and
   \((K,z)\mapsto u_K(z)\) are injective over all six cells and all four
   phases;
2. \(\ell_K^{(2)}(z)\) and \(u_K^{(2)}(z)\) are independent of \(z\),
   but each of them determines the cell \(K\).

#### Proof

For a large cell \(Q_0\cup Y\), the four lower one-step traces are

\[
                         cY,bY,dY,aY,
\tag{2.3}
\]

and the four upper traces are the four special 3-subsets adjoined to
\(Y\).  The half-square traces are respectively

\[
                         Y,
 \qquad \{a,b,c,d\}\cup Y.
\tag{2.4}
\]

Thus they determine \(Y\).  For a reservoir cell with fixed special
pair \(X\in\{ab,cd\}\), the corresponding traces have two special and
one reservoir point below, two special and three reservoir points above,
and the half-square signatures are

\[
                         X,
 \qquad X\cup\{u,v,w,x\}.
\tag{2.5}
\]

They determine \(X\).  The different special/reservoir cardinality
profiles separate the large cells from the reservoir cells.  This proves
both assertions. \(\square\)

## 3. Tensor shadows

Fix a product cell

\[
                         K=K_1\square\cdots\square K_r
\tag{3.1}
\]

and identify its vertices with phase vectors
\(x=(x_1,\ldots,x_r)\in\mathbb Z_4^r\).  For a valid \(r\), let

\[
 L_q(x)=A(x)\cap A(F^qx),
 \qquad
 U_q(x)=A(x)\cup A(F^qx).
\tag{3.2}

These are the lower and upper decorations of the length-\(q\) arc.
Because the coordinate schedule has period \(r\), write

\[
                         q=r+k,
 \qquad 0\le k\le r.
\tag{3.3}

For \(0\le q\le r\), every touched local cell is traversed once.  For
\(q=r+k\), the first \(k\) cells in the cyclic schedule are traversed
twice and the remaining \(r-k\) cells once.

The local cardinalities themselves distinguish the three statuses:

\[
\begin{array}{c|ccc}
&\text{untouched}&\text{once}&\text{twice}\\ \hline
\text{lower local size}&4&3&2\\
\text{upper local size}&4&5&6.
\end{array}
\tag{3.4}
\]

Hence a tensor shadow reveals which cells were untouched, singly
touched, and doubly touched.  Lemma 2.1 then recovers both cell and phase
on every untouched or singly touched factor; it recovers the cell but
erases the phase on a doubly touched factor.

### Theorem 3.1 (exact collision fibres)

Fix one resolution and one product-cell partition.

1. For \(1\le q\le r\), both maps \(x\mapsto L_q(x)\) and
   \(x\mapsto U_q(x)\) are injective, even when all \(6^r\) product
   cells are considered together.
2. Let \(q=r+k\), \(1\le k<r\).  Equality of two lower shadows, or of
   two upper shadows, is equivalent to:
   * the product cell is the same;
   * all singly touched phases are equal;
   * the two hidden \(k\)-tuples have the same coordinate sum modulo
     \(r\).
3. At \(q=2r\), the shadow determines the product cell but is independent
   of every phase.

#### Proof

For \(q<r\), the nonempty cyclic interval of singly touched factor
indices determines the starting schedule position.  Lemma 2.1 then
recovers every local cell and every phase.  At \(q=r\), all factors are
singly touched, so Lemma 2.1 directly recovers the entire phase vector;
the recovered vector itself supplies \(s(x)\).

Now let \(q=r+k\), \(1\le k<r\).  The proper nonempty cyclic interval of
doubly touched indices determines the schedule start and hence
\(s(x)\).  Lemma 2.1 recovers all singly touched phases.  The only
condition left on the erased phases is therefore

\[
 \sum_{i\in D}x_i
 \equiv
 s(x)-\sum_{i\notin D}x_i
 \pmod r,
\tag{3.5}
\]

where \(D\) is the doubly touched interval.  Conversely, changing the
hidden phases while preserving (3.5) changes none of the local traces,
so it preserves both tensor shadows.  This proves assertion 2.

For \(q=2r\), every factor contributes its phase-independent half-square
signature, proving assertion 3.  The fact that the signatures determine
the cells also proves that no collision between distinct product cells
was omitted. \(\square\)

### Corollary 3.2 (first collisions)

For \(r=2\), a collision fibre at \(q=3\) has size two.  For \(r=4\),
the fibres at \(q=5,6,7\) have sizes respectively

\[
                         1,4,16.
\tag{3.6}
\]

The examples in (0.5) realize the first nontrivial fibres.

#### Proof

For \(r=2\), a prescribed parity sum on one hidden \(\mathbb Z_4\)
coordinate has two solutions.  For \(r=4\), a prescribed sum modulo four
on \(k\) hidden coordinates has \(4^{k-1}\) solutions. \(\square\)

## 4. The collision is genuinely cross-cycle

For \(r=2\), the orbit of \((0,0)\) is

\[
 00,10,11,21,22,32,33,03,00,
\tag{4.1}
\]

so \((2,0)\) lies in the other \(C_8\).  Thus the first collision in
(0.5) is between different cycles of the factor, not two descriptions of
one arc.

For \(r=4\), every orbit has the property that, after choosing a lift of
the four phases to integers over any interval shorter than a full orbit,
the four increment counts differ by at most one.  The phase difference
between \((0,0,0,0)\) and \((1,3,0,0)\) cannot occur along such a
balanced schedule.  Hence the \(q=6\) example is likewise a cross-cycle
collision.

## 5. Cross-resolution collisions occur already at depth one

Compare the two local resolutions \(\mathcal F_0,\mathcal F_1\).  For a
fixed reservoir orientation \(Y\), the large squares are

\[
 Q_0\cup Y=(ac,bc,bd,ad)+Y,
 \qquad
 Q_1\cup Y=(ab,bc,cd,ad)+Y.
\tag{5.1}
\]

Their lower one-step supports are both

\[
                         \{aY,bY,cY,dY\},
\tag{5.2}
\]

and their upper one-step supports are both

\[
 \{abcY,abdY,acdY,bcdY\}.
\tag{5.3}
\]

There are therefore sixteen common lower and sixteen common upper
depth-one targets among the four large cells.  The reservoir cells do
not add common targets because their fixed special pairs are
\(ab,cd\) on one side and \(ac,bd\) on the other.

This is not a defect of either individual resolution: Lemma 2.1 says
each resolution is internally injective at depth one.  It says that a
global construction which chooses resolutions independently in different
canonical packets cannot regard the resolution bit as invisible.

## 6. What this does and does not refute

The carry obstruction refutes only the proposed \(\mathbb Z_4^r\)
formula.  It does not affect the syndrome construction of the resolvable
Hamming \(C_{2h}\)-factor, whose proof is independent and valid for every
power of two \(h\).

The shadow collisions also do not invalidate exact middle ownership.
They show that exact middle ownership and shadow injectivity are
different properties: the former holds orbitwise, while the latter loses
phase information as soon as two local directions of more than one
factor have been erased.

## 7. A precise checksum repair target

Let \(\Phi_q^-(x)=L_q(x)\) and \(\Phi_q^+(x)=U_q(x)\).  A map

\[
                         \Gamma:X\longrightarrow\mathcal A
\tag{7.1}
\]

is called an \(H\)-shadow checksum if

\[
 x\longmapsto\bigl(\Phi_q^\pm(x),\Gamma(x)\bigr)
\quad\text{is injective for every }1\le q\le H.
\tag{7.2}
\]

This is exactly the missing information; it is neither probabilistic nor
asymptotic.

### Proposition 7.1 (explicit algebraic checksums)

For \(r=2\), the single bit

\[
                         \Gamma_2(x)=\lfloor x_1/2\rfloor
\tag{7.3}
\]

separates the first collision fibre \(q=3\) after cyclically moving the
doubly touched coordinate into position one.

For \(r=4\), at \(q=6\) the checksum

\[
                         \Gamma_{4,1}(x)=\sum_{i=1}^4 i x_i\pmod4
\tag{7.4}
\]

separates every collision fibre.  Indeed, the two hidden indices are
consecutive, so the unweighted sum (3.5) and the weighted sum (7.4) form
a \(2\times2\) system with determinant one in \(\mathbb Z_4\).

For all \(q<2r\), the universal finite checksum

\[
                         \Gamma_{\rm full}(x)=(x_1,\ldots,x_r)
\tag{7.5}
\]

is shadow-separating.  More economically, it is enough to record cyclic
phase differences

\[
 (x_1-x_2,x_2-x_3,\ldots,x_{r-1}-x_r)\pmod4,
\tag{7.6}
\]

together with one phase which is visible on every proper shadow.  The
visible singly touched factor supplies that phase automatically when
\(r<q<2r\).

Cross-resolution use additionally requires the resolution bit
\(\varepsilon\), by (5.2)--(5.3).

### Guard-realization criterion

A physical guard gadget solves the collision problem through height
\(H\) if its lower and upper traces supply labels
\(G_q^\pm(x)\) such that

\[
 \Phi_q^\pm(x)=\Phi_q^\pm(y)
 \quad\Longrightarrow\quad
 G_q^\pm(x)\ne G_q^\pm(y)
\tag{7.7}
\]

for distinct states, and if its augmented middle supports still partition
the ambient middle layer exactly.  Across associator resolutions the
label must also distinguish \(\varepsilon\).

Equivalently, form the finite collision graph whose vertices are
cycle-phase-resolution states and whose edges join two states sharing a
lower or upper \(q\)-shadow for some \(q\le H\).  A checksum is precisely
a proper coloring of this graph; a physical guard is an exact
middle-support realization of that coloring whose own \(q\)-traces retain
the color.

The algebraic colorings (7.3)--(7.6) prove that the information demand is
small in the valid cases.  They do **not** prove the exact physical guard
realization.  That realization, or use of the already valid syndrome
factor in place of (0.1), is the honest remaining repair gate.

## 8. Bottom line

\[
\boxed{
\begin{gathered}
F(x)=x+e_{1+\sum x_i\bmod r}
\text{ works exactly for }r=1,2,4;\\
r\notin\{1,2,4\}\Longrightarrow F\text{ has two-to-one fibres};\\
\text{first internal shadow collisions: }(r,q)=(2,3),(4,6);\\
\text{first cross-resolution collision: }q=1;\\
\text{repair requires an exact-factor-compatible phase and resolution
checksum.}
\end{gathered}}
\]
