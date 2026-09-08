# Odd-\(m\) BA growing blocks: pair-run saturation, owner rounding, and the annular cut

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad L=m(m+1),\qquad
 W=\binom{2m+1}{m},
\tag{0.1}
\]

and assume throughout that \(m\) is odd.  Let \(C=BA\), let \(H\) be the
protected height, and put

\[
                         h=\left\lceil {H\over2}\right\rceil.
\tag{0.2}
\]

The even-\(m\) source/successor owner collision is absent.  Nevertheless,
the surviving odd-\(m\) growing-block programme has two sharply different
answers.

1. **Component geometry is near-extremal.**  If a connected protected
   atom component contains \(M=kn\) full \(BA\)-orbits, the exact pair-run
   bound gives \(k\ge h+1\).  At the first possible scale
   \(k=h+1\), every orbit uses all but a relative
   \(O(1/h)\) of its relaxed pair-run capacity:

   \[
    {1\over2L}\sum_{\mathcal O'\ne\mathcal O}
    \left({2(m-j_{\mathcal O\mathcal O'})\over h}
              -\lambda_{\mathcal O\mathcal O'}\right)
    ={m-h-1\over h(m+1)}.
   \tag{0.3}
   \]

   Thus a minimal growing molecule cannot be obtained from diffuse random
   partners; almost every available protected run must be scheduled.

2. **Owner marginals do not obstruct a block.**  An owner-simple block at
   that scale would contain

   \[
                         R=2LM=2Lkn=\Theta(m^3H)
   \tag{0.4}
   \]

   distinct owners.  Its complete \(S_n\)-conjugate orbit has an exact
   uniform fractional owner matching.  Before conditioning on protected
   atom factorhood, a random \(M\)-tuple of odd-\(m\) \(BA\)-orbits has
   expected owner collision \(O(M^2L^2/W)=e^{-\Omega(m)}\).  Hence neither
   owner capacity nor the exact uniform fractional point supplies a
   statewise no-go for one polynomial-size block.

3. **Independent block rounding is quantitatively useless.**  Choosing
   \(W/R\) independent uniform conjugates gives expected owner-pair
   collision excess

   \[
                         {W-R\over2}=(1/2-o(1))W
   \tag{0.5}
   \]

   and expected owner leave \((e^{-1}+o(1))W\).  Moreover the conjugate
   block hypergraph has

   \[
                 {\Delta_2\over D}\ge {1\over m(m+1)},
   \qquad
                 R{\Delta_2\over D}\ge2kn=\Omega(mH),
   \tag{0.6}
   \]

   because every selected source owner is Johnson-adjacent to its
   \(A\)-successor owner.  Thus a generic growing-rank nibble does not
   round the uniform point.

4. **The protected annulus gives a decisive obstruction.**  At every odd
   depth \(q\), \(1\le q\le m-2\), the source and successor lower-prefix
   decks of one full \(BA\)-orbit coincide exactly.  Its \(2L\) prefix
   occurrences therefore have support exactly \(L\).  A union of
   owner-disjoint \(BA\) blocks using \(A_{\rm BA}\) owner occurrences,
   supplemented by arbitrary chronology on the other \(W-A_{\rm BA}\)
   occurrences, has

   \[
    \boxed{
    M_q^-\ge
       \left({A_{\rm BA}\over2}-(W-N_q)\right)_+,
    \qquad
    N_q=\binom{2m+1}{m-q},
    \quad q\ {\rm odd}.}
   \tag{0.7}
   \]

   In particular a full BA owner factor satisfies

   \[
                         M_q^-\ge N_q-{W\over2}.
   \tag{0.8}
   \]

   If \(q=a\sqrt m+O(1)\), then \(N_q/W=e^{-a^2+o(1)}\).  Hence every
   odd Gaussian depth with \(a<\sqrt{\log2}\) has

   \[
                         M_q^-\ge
             (e^{-a^2}-1/2-o(1))W=\Omega_a(W).
   \tag{0.9}
   \]

   Over any annulus
   \(a\sqrt m\le q\le b\sqrt m\), with
   \(0<a<b<\sqrt{\log2}\), the aggregate hole count is

   \[
    \sum_{\substack{a\sqrt m\le q\le b\sqrt m\\q\ {\rm odd}}}
       M_q^-
    \ge
    \left({b-a\over2}+o(1)\right)
       (e^{-b^2}-1/2)W\sqrt m.
   \tag{0.10}
   \]

This closes the **coefficient-one all-BA growing-block route**, even if the
owner-disjoint protected atom blocks themselves exist and even if their
owner hypergraph admits a perfect matching.  The atom partition cannot
change the physical BA prefix decks.

The purely component-theoretic existence of one owner-simple
\((h+1)n\)-orbit protected atom block is not disproved here.  Its exact
remaining conditions are (0.3), zero internal owner collision, and the
marked triangle factors in every protected suffix fibre.  Such blocks can
only be a vanishing reserve in a coefficient-one construction whose
protected system includes depth one: there (0.7) gives
\[
 M_1^-\ge
 \left({A_{\rm BA}\over2}-{2W\over m+2}\right)_+,
\]
so \(M_1^-=o(W)\) forces \(A_{\rm BA}=o(W)\).  If only a Gaussian annulus
starting at \(a\sqrt m\) is demanded, the corresponding sharp statement is
\[
 {A_{\rm BA}\over W}\le2(1-e^{-a^2})+o(1);
\]
the annular cut still excludes full or sufficiently dense BA deployment,
but not every small fixed density.

## 1. The growing component and its exact run deficit

For two active \(BA\)-orbits \(\mathcal O,\mathcal O'\), write

\[
 j_{\mathcal O\mathcal O'}
 =|A_{\mathcal O}\setminus A_{\mathcal O'}|,
\tag{1.1}
\]

and let \(\lambda_{\mathcal O\mathcal O'}\) be the number of selected
protected atoms containing states from both orbits.  The exact component
ledgers are

\[
 \sum_{\mathcal O'\ne\mathcal O}
   \lambda_{\mathcal O\mathcal O'}=2L,
\tag{1.2}
\]

\[
 \sum_{\mathcal O'\ne\mathcal O}
   j_{\mathcal O\mathcal O'}=kL,
\tag{1.3}
\]

and, for odd \(m\), the protected pair-run bound is

\[
 \lambda_{\mathcal O\mathcal O'}
 \le
 2\min\left\{
       j_{\mathcal O\mathcal O'},
       \left\lfloor{m-j_{\mathcal O\mathcal O'}\over h}\right\rfloor
       \right\}.
\tag{1.4}
\]

The \(1\)-design equation for a \(kn\)-orbit component also gives

\[
 \sum_{\mathcal O'\ne\mathcal O}
       (m-j_{\mathcal O\mathcal O'})
 =m(km-1).
\tag{1.5}
\]

Summing the relaxed form

\[
 \lambda_{\mathcal O\mathcal O'}
 \le {2(m-j_{\mathcal O\mathcal O'})\over h}
\tag{1.6}
\]

and using (1.2), (1.5), gives

\[
 2m(m+1)\le {2m(km-1)\over h}.
\tag{1.7}
\]

Its integral consequence is \(k\ge h+1\).

At equality scale \(k=h+1\), define the nonnegative relaxed run deficit

\[
 \Delta_{\rm run}(\mathcal O)
 =\sum_{\mathcal O'\ne\mathcal O}
 \left[
 {2(m-j_{\mathcal O\mathcal O'})\over h}
 -\lambda_{\mathcal O\mathcal O'}
 \right].
\tag{1.8}
\]

Equations (1.2), (1.5) give the exact value

\[
 \begin{aligned}
 \Delta_{\rm run}(\mathcal O)
 &= {2m((h+1)m-1)\over h}-2m(m+1)\\
 &= {2m(m-h-1)\over h}.
 \end{aligned}
\tag{1.9}
\]

Division by \(2L\) proves (0.3).  When
\(h\to\infty\) and \(h=o(m)\), the relative deficit is
\((1+o(1))/h\).

The losses hidden in (1.8) include all of the following:

* unused compatible phase pairs;
* the floor in (1.4);
* partners with \(j<(m-j)/h\), where the first term in the minimum is
  active; and
* common protected runs which overlap instead of packing disjointly.

Their total is only an \(O(1/h)\) fraction of the required pair
incidences.  This is the precise rigidity a construction at
\(k\asymp H\) must meet.

## 2. Owner size and absence of a local collision obstruction

For odd \(m\), one full \(BA\)-orbit has \(L\) distinct source owners and
\(L\) distinct \(A\)-successor owners, and the two decks are disjoint.
Thus one orbit has \(2L\) internally distinct owner occurrences.

Let \(\mathscr C\) be a protected atom component with \(M=kn\) orbits.
Its owner multiset has size

\[
                         2LM=R.
\tag{2.1}
\]

Write \(\Omega(\mathscr C)\) for its distinct owner set and

\[
 \operatorname {col}(\mathscr C)
 =R-|\Omega(\mathscr C)|.
\tag{2.2}
\]

Then the block is owner-simple exactly when
\(\operatorname {col}(\mathscr C)=0\).  All possible collisions in
(2.2) are cross-orbit collisions.

There is no unconditioned probabilistic collision obstruction at
polynomial \(M\).  Fix one odd-\(m\) orbit \(\mathcal O\), and conjugate a
second orbit uniformly by \(S_n\).  Every one of its \(2L\) distinct
owners is uniform on the middle layer.  Therefore

\[
 \mathbb E\,
 |\Omega(\mathcal O)\cap\Omega(\sigma\mathcal O')|
 ={(2L)^2\over W}.
\tag{2.3}
\]

For \(M\) independently conjugated orbits, the union bound gives

\[
 \Pr(\text{some cross-orbit owner collision})
 \le \binom M2{(2L)^2\over W}.
\tag{2.4}
\]

At \(M=kn=O(mH)\), with any subexponential \(H\), the right side is
\(e^{-\Omega(m)}\).  Thus almost every unconditioned orbit tuple is
owner-simple.  Such a tuple almost surely has no protected flag triples,
so (2.4) is not an atom construction.  It proves that a block obstruction
must come from the strong protected-run conditioning, not owner density.

## 3. Exact uniform block point and owner pair codegrees

The microscopic port/owner system already has the exact symmetric
fractional point

\[
 D_0=m!(m+1)!,\qquad
 p={1\over2D_0},\qquad
 y_{\mathcal O}=p,\qquad
 z_\alpha={p\over d_H},
\tag{3.0}
\]

where \(d_H\) is the exact state degree in the protected-atom
hypergraph.  It satisfies every orbit-port equation and every middle-owner
equation.  Its total activated orbit mass is \(W/(2L)\), exactly the mass
required by an owner factor.  Hence the obstruction below cannot be a
linear owner or port marginal missing from the established fractional
system.

Assume provisionally that one owner-simple protected component
\(\mathscr C\) exists, with owner set

\[
                         E=\Omega(\mathscr C),\qquad |E|=R.
\tag{3.1}
\]

Take all distinct label conjugates \(\sigma E\),
\(\sigma\in S_n\), and regard them as the edges of a block hypergraph
\(\mathcal G_E\) on the middle layer.  It is regular by transitivity.  If
its vertex degree is \(D\), assigning weight \(1/D\) to every conjugate
gives

\[
                         \sum_{B\ni X}{1\over D}=1
                         \qquad(X\in\tbinom{[n]}m).
\tag{3.2}
\]

Thus every seed block automatically has an exact uniform fractional owner
matching.  Its total fractional number of blocks is \(W/R\), as follows
by summing (3.2).

For \(0\le d\le m\), let

\[
 N_d=\binom md\binom{m+1}d
\tag{3.3}
\]

be the number of owners at Johnson distance \(d\) from a fixed owner, and
put

\[
 a_d(E)={1\over R}
 |\{(X,Y)\in E^2:d_J(X,Y)=d\}|.
\tag{3.4}
\]

### Proposition 3.1 (exact conjugate pair-codegree formula)

If \(D_d\) is the codegree in \(\mathcal G_E\) of two owners at Johnson
distance \(d\), then

\[
                         \boxed{{D_d\over D}={a_d(E)\over N_d}.}
\tag{3.5}
\]

#### Proof

Double-count triples consisting of a conjugate block and an ordered
distance-\(d\) owner pair inside it.  Counting by blocks gives
\(|\mathcal G_E|Ra_d(E)\).  Counting by the first owner, the second owner,
and their common blocks gives \(WN_dD_d\).  The vertex-incidence identity
\(|\mathcal G_E|R=WD\) proves (3.5). \(\square\)

Every state in an active orbit supplies the Johnson edge joining its
source owner to its \(A\)-successor owner.  In an owner-simple block these
\(LM\) edges are vertex-disjoint.  Consequently \(E\) contains at least
\(R\) ordered distance-one pairs, and

\[
                         a_1(E)\ge1.
\tag{3.6}
\]

Equations (3.3), (3.5) give

\[
 {D_1\over D}\ge{1\over m(m+1)},\qquad
 R{D_1\over D}\ge {2Lkn\over m(m+1)}=2kn.
\tag{3.7}
\]

Thus even the best possible seed block lies outside a black-box regime
requiring \(R\Delta_2/D=o(1)\); a criterion involving \(R^2\) fails more
strongly.  This is not a matching obstruction—the exact fractional point
(3.2) still exists—but it explains why ordinary growing-uniformity
codegree rounding does not solve the block problem.

The pair-run estimate (1.4) controls how often two **orbit ports** may lie
in common protected atoms.  It does not bound the full owner spectrum
\(a_d(E)\).  The exact additional moment condition required by an owner
matching theorem is therefore

\[
 \boxed{
 \max_{1\le d\le m}{a_d(E)\over N_d}
 \quad\text{together with higher block-intersection cuts}.}
\tag{3.8}
\]

Replacing (3.8) by the orbit-port codegree is an invalid projection.

## 4. Why independent rounding leaves linear owner error

Let

\[
                         B={W\over R}
\tag{4.1}
\]

and, for clarity, suppose this is integral.  Choose \(B\) independent
uniform conjugates of \(E\).  For an owner \(X\), its load \(Z_X\) has
binomial distribution

\[
                         Z_X\sim\operatorname {Bin}
                         \left(B,{R\over W}\right),
\qquad \mathbb EZ_X=1.
\tag{4.2}
\]

The expected number of colliding block pairs, counted at their common
owners, is

\[
 \begin{aligned}
 \mathbb E\sum_X\binom{Z_X}{2}
 &=W\binom B2\left({R\over W}\right)^2\\
 &={W-R\over2}.
 \end{aligned}
\tag{4.3}
\]

The expected owner leave is

\[
 \mathbb E|\{X:Z_X=0\}|
 =W\left(1-{R\over W}\right)^{W/R}
 =(e^{-1}+o(1))W,
\tag{4.4}
\]

because \(R\) is polynomial while \(W\) is exponential.  Equations
(4.3)--(4.4) quantify the negative dependence missing from the uniform
fractional point.

## 5. Exact odd-depth prefix pairing

Write \(m=2r+1\).  Let \(\sigma\) be the position permutation induced by
\(C=BA\); its two cycles have lengths \(m\) and \(m+1\).

At lower depth \(q\), put \(s=m-q\).  The source and successor prefix
footprints are

\[
                         P_s=\{1,\ldots,s\},\qquad
                         Q_s=\{2,\ldots,s+1\}.
\tag{5.1}
\]

### Lemma 5.1 (parity classification of prefix decks)

For \(1\le q\le m-2\):

\[
 \begin{cases}
 Q_{m-q}=\sigma^{m+1}P_{m-q}
     \text{ up to the fixed orientation convention},&q\text{ odd},\\
 P_{m-q},Q_{m-q}\text{ lie in disjoint }\sigma\text{-orbits},
     &q\text{ even}.
 \end{cases}
\tag{5.2}
\]

For odd \(q\), both footprint orbits have length \(L\).

#### Proof

If \(q\) is odd, then \(s=m-q=2a\) is even.  Both \(P_s\) and \(Q_s\)
meet each position cycle in \(a\) consecutive positions.  On the
length-\(m\) cycle, \(Q_s\) is the one-step translate of \(P_s\); on the
length-\((m+1)\) cycle they have the same phase.  The simultaneous shift
is the CRT solution

\[
                         t\equiv1\pmod m,\qquad
                         t\equiv0\pmod{m+1},
\tag{5.3}
\]

namely \(t=m+1\), up to reversing the convention for \(\sigma\).  This
proves the first line.  The two nonempty proper cyclic intervals have
trivial stabilizers, so their common orbit length is \(L\).

If \(q\) is even, then \(s\) is odd.  The footprint \(P_s\) has one more
position on the length-\(m\) cycle than on the length-\((m+1)\) cycle,
whereas \(Q_s\) has the reverse counts.  Powers of \(\sigma\) preserve
the two cycles, so the footprints cannot be translates. \(\square\)

### Corollary 5.2 (exact factor-two packet collision)

At every odd \(q\), the \(2L\) lower-prefix occurrences from one full
odd-\(m\) \(BA\)-orbit have support exactly \(L\), every supported target
occurring twice.

#### Proof

For a permutation representative \(\pi\), the two decks are

\[
 \{\pi(\sigma^tP_s):t\in\mathbb Z_L\},\qquad
 \{\pi(\sigma^tQ_s):t\in\mathbb Z_L\}.
\]

Lemma 5.1 identifies the decks by a phase shift and proves injectivity
within either deck. \(\square\)

Regrouping the source states into protected atoms changes neither deck.
The conclusion therefore holds inside every component, independent of
its partner graph, its size \(kn\), and its marked suffix triangle
factor.

## 6. Hybrid and annular hole bounds

Let \(A_{\rm BA}\) owner occurrences of an owner-transversal chronology
belong to full odd-\(m\) \(BA\)-orbits.  At an odd depth \(q\), Corollary
5.2 gives at most \(A_{\rm BA}/2\) distinct targets from those
occurrences.  The other \(W-A_{\rm BA}\) occurrences give at most one
new target each.  Hence total support is at most

\[
                         W-{A_{\rm BA}\over2}.
\tag{6.1}
\]

Subtracting from \(N_q\) proves (0.7).

For a full BA owner factor, \(A_{\rm BA}=W\), giving (0.8).  Uniformly
for \(q=a\sqrt m+O(1)\),

\[
 {N_q\over W}
 =\prod_{i=1}^q{m-q+i\over m+1+i}
 =e^{-a^2+o(1)}.
\tag{6.2}
\]

This proves (0.9).  In the interval
\([a\sqrt m,b\sqrt m]\), half the integer depths are odd.  Monotonicity of
\(N_q\) gives (0.10).

For a hybrid deployment with
\(A_{\rm BA}=\alpha W\), (0.7) at
\(q=a\sqrt m+O(1)\) reads

\[
 M_q^-\ge
 \left(\frac{\alpha}{2}-1+e^{-a^2}-o(1)\right)_+W.
\tag{6.2a}
\]

Thus \(o(W)\) holes at that depth require
\(\alpha\le2(1-e^{-a^2})+o(1)\).  At \(q=1\), the stronger shallow
consequence is

\[
 M_1^-\ge
 \left({A_{\rm BA}\over2}-{2W\over m+2}\right)_+,
\tag{6.2b}
\]

which forces \(A_{\rm BA}=o(W)\) whenever depth one belongs to the
protected target system.

There is also a fractional version which directly audits the exact
uniform block point.  Let \(\mathfrak B\) be any conjugacy-stable
catalogue of owner-simple BA blocks, and give its blocks nonnegative
weights \(x_B\) satisfying exact owner marginals:

\[
                         \sum_{B\ni X}x_B=1
                         \qquad(X\in\tbinom{[n]}m).
\tag{6.3}
\]

Summing gives

\[
                         \sum_B |B|x_B=W,
\tag{6.4}
\]

where \(|B|\) denotes its owner count.  At odd \(q\), every block has at
most \(|B|/2\) distinct lower targets.  Thus

\[
 \sum_T\sum_{B:T\in\operatorname {supp}_q(B)}x_B
 \le {W\over2}.
\tag{6.5}
\]

If \(N_q>W/2\), the average fractional target load is below one.  In
particular the all-ones target dual separates every exact-owner
fractional BA block mixture:

\[
 \boxed{
 \sum_T\left(1-
   \sum_{B:T\in\operatorname {supp}_q(B)}x_B\right)
 \ge N_q-{W\over2}>0.}
\tag{6.6}
\]

Thus the exact uniform fractional point survives the owner and port rows
but fails the augmented annular cover rows.  This is not an integral
rounding gap; it is already a fractional support-capacity cut.

## 7. Exact boundary

The following statements are proved.

* Pair-run packing forces \(kn\) orbits with \(k\ge h+1\), and a minimal
  block has the exact near-saturation deficit (0.3).
* Odd parity removes all within-orbit owner collisions.  Unconditioned
  polynomial orbit tuples are owner-simple with probability
  \(1-e^{-\Omega(m)}\).
* Every hypothetical owner-simple block orbit has an exact uniform
  fractional owner point, but independent rounding has the linear errors
  (0.5).
* Its conjugate owner hypergraph has the exact pair-codegree formula
  (3.5), and the forced source/successor Johnson pairs give the growing-rank
  obstruction (0.6).
* Every odd protected depth has exact factor-two BA prefix collision,
  yielding the hybrid and Gaussian-annulus cuts (0.7)--(0.10).

Accordingly there are two distinct remaining questions.

1. **Pure component question.**  Does there exist one owner-simple
   protected suffix-fibre triangle factor on \(kn\) orbits with
   \(k=h+1+o(h)\)?  Any such factor must satisfy (0.3), the cut
   \(1\)-design, the ordered-pair mod-three congruences, and zero collision
   (2.2).  The current equations neither construct nor refute it.

2. **Coefficient-one question.**  Can such blocks occupy positive owner
   density while covering the protected annulus?  The answer is no:
   (6.6) is a fractional obstruction whenever an odd protected depth has
   \(N_q>W/2\), and (0.10) gives a much larger aggregate Gaussian defect.

Therefore a successful coefficient-one construction may use
componentwise BA atoms only on \(o(W)\) owner occurrences, or must break
the strict \(e,Ae,Ce,ACe,\ldots\) BA chronology inside a positive fraction
of the blocks.  Growing the partner component alone cannot repair the
annular support loss.
