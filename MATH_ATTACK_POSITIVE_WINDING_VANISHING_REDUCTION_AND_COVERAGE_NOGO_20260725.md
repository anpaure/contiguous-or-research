# Positive winding at the corrected coefficient-one scale

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Result and exact boundary

Put

\[
 N=2m+1,\qquad B_m=\operatorname {Cat}_m,
 \qquad H_A=\lceil A\sqrt m\rceil ,
\]

where \(A>0\) is fixed.  Let \(\mathcal P_+\) be a pairwise
quotient-edge-disjoint family of nonwrapping positive-winding PBBS return
intervals of positive residence at most \(H_A\).  If \(w(I)\) is the
two-step winding, \(h(I)\) the invariant Dyck height, and \(s(I)\) the
step-two duration, then its positive residence is \(s(I)+1\), its full
quotient support has \(s(I)+2\) edges, and \(s(I)\le H_A-1\).  This note
proves the following corrected-scale reductions.

For every function \(K_m\to\infty\),

\[
 \boxed{
 \#\{I\in\mathcal P_+:w(I)\ge K_m\}
 =O\!\left({B_m\over K_m\sqrt m}\right)
 =o\!\left({B_m\over\sqrt m}\right).}
 \tag{0.1}
\]

For every function \(L_m\to\infty\),

\[
 \boxed{
 \#\{I\in\mathcal P_+:s(I)+2\ge L_m(h(I)+2)\}
 =O\!\left({B_m\over L_m\sqrt m}\right)
 =o\!\left({B_m\over\sqrt m}\right).}
 \tag{0.2}
\]

The subfamily of height at most \(\sqrt m/\log m\) is also

\[
 \boxed{o(B_m/\sqrt m).}                            \tag{0.3}
\]

Thus, after taking for example \(K_m=L_m=\log\log m\), the entire
positive-winding problem at the corrected coefficient-one scale reduces to

\[
 \boxed{
 \begin{gathered}
  1\le w(I)<\log\log m,\qquad
  {\sqrt m\over\log m}<h(I)\le A\sqrt m,\\
  h(I)+2\le s(I)+2<(\log\log m)(h(I)+2),
 \end{gathered}}
 \tag{0.4}
\]

on the long quotient cycles.  This is an unconditional vanishing theorem
for every complementary positive-winding sector, but it does not yet give
the required little-oh bound for the residual class (0.4).

Two further exact results sharpen the obstruction.

1.  The entire peak-defect-one PBBS sector can be solved for positive as
    well as zero winding.  In its natural weak-composition coordinates
    \((a,x,c)\), every sub-circumference positive return has

    \[
       \boxed{s=3c+2,\qquad w=c\ge1.}               \tag{0.5}
    \]

    It is the first return.  These genuine fixed-winding examples all lie
    on quotient cycles of period at most three and hence contribute only
    polynomially many short-cycle roots.

2.  The old constant pseudoprofile failed full omitted-coordinate
    coverage.  Sections 3--4 repair that failure.  There are arbitrarily large
    formal long quotient cycles with all of the following properties:

    * exact two endpoint ledgers and their potential telescope;
    * exact first-return chronology, winding one, and both-parity support
      disjointness;
    * the floor-correct Gaussian height--gap relation;
    * full coverage of all \(N\) physical coordinates;
    * exact cycle-voltage closure and exact area-coboundary closure;
    * distinct aperiodic itineraries of least quotient period
      \(\Omega(N^2)>H_A\);
    * packing density \(\Theta(N^{-1/2})\); and
    * at every phase, the displayed height and both parity deficits are
      simultaneously realized by a literal first-dominant Dyck word.

    What is not asserted is the interphase identity

    \[
       D_{j+1}=\tau D_j.                            \tag{0.6}
    \]

    Theorem 4.2 also repairs the Gaussian-height mismatch in the stronger
    exact-moment complete-colour obstruction.  Consequently the surviving
    axiom is precisely simultaneous orbit realizability: the exact
    remaining positive theorem must use the literal block-rotation word
    recursion (0.6), or an equivalent transported-word correlation.

No zero-winding height converse is used or reinstated anywhere in this
note.

## 1. Vanishing sectors at the corrected scale

For a Dyck root \(D\), put

\[
 d(D)=|S(D)|+1,
 \qquad
 \mathscr D_m=\sum_{D\in\mathcal D_m}d(D).
 \tag{1.1}
\]

The audited first-deficit moment is

\[
 \mathscr D_m\le C\sqrt m\,B_m                    \tag{1.2}
\]

for an absolute constant \(C\).  A positive-winding return
\(I=(D_0,\ldots,D_{s-1})\) has the exact equation

\[
 \sum_{j=0}^{s-1}d(D_j)=\delta(D_s)+Nw(I).         \tag{1.3}
\]

### Theorem 1.1 (large winding is negligible)

For every \(K\ge1\),

\[
 \boxed{
 \#\{I\in\mathcal P_+:w(I)\ge K\}
 \le {\mathscr D_m\over KN}
 \le {CB_m\over K\sqrt m}.}                      \tag{1.4}
\]

#### Proof

The selected quotient edge supports are disjoint.  Sum (1.3) over the
subfamily with \(w(I)\ge K\), discard the positive terminal terms, and use
each Dyck root at most once:

\[
 KN\,\#\{I:w(I)\ge K\}
 \le\sum_I\sum_{j<s(I)}d(D_j)
 \le\mathscr D_m.
\]

Now use (1.2) and \(N\ge2m\).  Taking \(K=K_m\to\infty\) proves
(0.1). \(\square\)

Let \(b_{m,h}\) count semilength-\(m\) Dyck roots of exact height \(h\).
The normalized PBBS map preserves height.  Moreover, the projected trace
of a return of height \(h\) uses at least \(h+2\) quotient edges.  Hence

\[
 \sum_h{b_{m,h}\over h+2}\le C{B_m\over\sqrt m}. \tag{1.5}
\]

### Theorem 1.2 (large support-to-height ratio is negligible)

For every \(L\ge1\),

\[
 \boxed{
 \#\{I\in\mathcal P_+:s(I)+2\ge L(h(I)+2)\}
 \le {C B_m\over L\sqrt m}.}                     \tag{1.6}
\]

#### Proof

Fix a height \(h\).  Every selected full support in the displayed subfamily
uses at least \(L(h+2)\) distinct height-\(h\) quotient edges.  There are
exactly \(b_{m,h}\) such edges.  Thus its height-\(h\) part has size at
most \(b_{m,h}/(L(h+2))\).  Sum over \(h\) and use (1.5). \(\square\)

Finally, if \(F_m(t)\) counts Dyck roots of height at most \(t\), the
audited path-spectrum estimate gives, for \(t\le\sqrt m\),

\[
 F_m(t)
 \le C B_m\left({\sqrt m\over t}\right)^3
             \exp\!\left(-c{m\over t^2}\right).  \tag{1.7}
\]

Taking \(t=\lfloor\sqrt m/\log m\rfloor\), the right side is

\[
 C B_m(\log m)^3e^{-c(\log m)^2}
 =o(B_m/\sqrt m).                                  \tag{1.8}
\]

The number of selected intervals of those heights is at most the number
of available roots, so (1.8) proves (0.3).  The lower height--gap theorem
gives \(s(I)+2\ge h(I)+2\), completing (0.4).

## 2. Complete positive-return chronology at peak defect one

Every semilength-\(m\) Dyck root with \(m-1\) peaks has the unique form

\[
 E(a,b,c)=(10)^a1(10)^b0(10)^c,
 \qquad a,c\ge0,\quad b\ge1,\quad a+b+c=m-1.
 \tag{2.1}
\]

Put \(x=b-1\).  Then

\[
 a+x+c=m-2,
 \qquad
 \tau(a,x,c)=(c,a,x).                              \tag{2.2}
\]

At the three successive phases the suffix deficits and first-maximum
positions are respectively

\[
 (2c+1,,2x+1,,2a+1),                             \tag{2.3}
\]

and

\[
 (2a+2,,2c+2,,2x+2).                             \tag{2.4}
\]

### Theorem 2.1 (all sub-Gaussian positive returns in this sector)

Assume \(0\le s<m\), and write

\[
 s=3q+t,\qquad t\in\{0,1,2\}.
\]

The omitted coordinate returns at step-two time \(s\) if and only if

\[
 t=2\quad\hbox{and}\quad q=c.                     \tag{2.5}
\]

When \(c=0\), this is the zero-winding return \(s=2\).  When \(c\ge1\),
it is a positive-winding first return with

\[
 \boxed{s=3c+2,\qquad w=c.}                       \tag{2.6}
\]

#### Proof

For \(t=0\), the deficit sum minus the endpoint position is

\[
 q(N-2)-(2a+2)=qN-2(q+a+1).                       \tag{2.7}
\]

For a return, \(N\) must divide \(2(q+a+1)\), hence, since \(N\) is
odd, it must divide \(q+a+1\).  From \(s<m\), one has \(q<m/3\), and

\[
 0<q+a+1<m/3+m-1<N.
\]

Thus (2.7) is never a multiple of \(N\).

For \(t=1\), subtraction of the phase-one endpoint gives

\[
 q(N-2)+(2c+1)-(2c+2)=qN-(2q+1).                  \tag{2.8}
\]

Here \(0<2q+1<N\), so again there is no return.

For \(t=2\), subtraction of the phase-two endpoint gives

\[
 \begin{aligned}
 &q(N-2)+(2c+1)+(2x+1)-(2x+2)\\
 &\hspace{35mm}=qN+2(c-q).                         \tag{2.9}
 \end{aligned}
\]

Since \(|c-q|<N\) and \(N\) is odd, (2.9) is a multiple of \(N\) if
and only if \(c=q\).  In that case (2.9)=qN, proving \(w=q=c\).
Every earlier time has either \(t=0,1\), already excluded, or has
\(t=2\) with a smaller quotient \(q'<c\), which is excluded by the same
criterion.  Hence the return is consecutive. \(\square\)

For fixed \(A\), all returns from (2.6) with \(s+1\le H_A\) have
\(c=O_A(\sqrt m)\).  Their number of starting roots is

\[
 \sum_{1\le c\le(H_A-3)/3}(m-1-c)=O_A(m^{3/2}).   \tag{2.10}
\]

More importantly, (2.2) puts every such root on a quotient cycle of
period at most three.  They are therefore already contained in the
short-cycle error \(Z_{H_A}=\exp(o(m))=o(B_m/\sqrt m)\).  The theorem
shows that fixed positive winding is genuinely compatible with exact PBBS
chronology; it does not produce a long-cycle obstruction.

## 3. Why the scalar residual cannot be removed by coverage alone

The complete-colour cocycle in
MATH_ATTACK_Z14_PBBS_POSITIVE_WINDING_CYCLE_CHARGE_OBSTRUCTION_20260725.md
already repairs coordinate coverage, aperiodicity, and voltage-itinerary
rigidity.  Its selected literal local word has height

\[
 h_{\rm Z14}=a-c+1=k(s-4)+1=\Theta_A(N),           \tag{3.0}
\]

whereas its formal return has step-two duration \(s=\Theta_A(\sqrt N)\).
Thus that local realization is deliberately not a height-compatible
realization of the formal short return; the height--gap theorem would
forbid such an actual return.  This is not an error in that report, which
claims only local quadruple feasibility.

The construction below closes this different loophole.  It gives every
formal phase a literal first-dominant realization of the same critical
Gaussian height \(h=s-1\), while retaining full coordinate coverage and
long period.  It is useful to separate three levels of structure.

1.  The phase data obey every exact scalar identity forced by PBBS.
2.  Every individual phase datum is realized by an actual
    first-dominant Dyck root, including both parity deficits.
3.  The ordered list of those roots is not proved to obey the word
    recursion \(D_{j+1}=\tau D_j\).

Thus a contradiction to the model must use level 3.  Coordinate coverage,
which was missing from the old pseudoprofile, will hold exactly.

Choose odd integers \(s\ge7\) and \(e\ge3\) such that

\[
 s\not\equiv1\pmod3,
 \qquad
 N=e(2s+1),
 \qquad
 h=s-1,
 \qquad
 a=e(s-1).                                         \tag{3.1}
\]

Then \(N\) is odd, so \(N=2m+1\) for an integer \(m\).  By taking
\(e/s\) in a fixed compact interval bounded away from zero, one has

\[
 s=\Theta(\sqrt N)=\Theta(\sqrt m),                \tag{3.2}
\]

and one can arrange \(s+1\le H_A\) for any prescribed fixed Gaussian
cutoff by choosing the lower bound on \(e/s\) appropriately.

Put

\[
 L=2s+1,
 \qquad
 T=2(e-1)L.                                        \tag{3.3}
\]

Index a formal quotient cycle by \(j\in\mathbb Z_T\), and set
\(a_j=a\) at every phase.  Split the cycle into \(2(e-1)\) consecutive
blocks of \(L\) phases.  At ordinary phases put \(b_j=a\).  At the last
phase of each of the first \(e-1\) blocks put

\[
 b_j=a+2,                                          \tag{3.4}
\]

and at the last phase of each of the last \(e-1\) blocks put

\[
 b_j=a-2.                                          \tag{3.5}
\]

Define the two deficit ledgers by the exact block formulas

\[
 c_j=N-a_j-b_j,
 \qquad
 \widehat c_j=N-b_j-a_{j+1}.                      \tag{3.6}
\]

Since \(a_{j+1}=a_j=a\), one has \(c_j=\widehat c_j\), with values

\[
 3e,\qquad3e-2,\qquad3e+2                       \tag{3.7}
\]

at ordinary, positive-seam, and negative-seam phases respectively.  All
are positive odd integers.

### Theorem 3.1 (coverage-complete critical saturation model)

The cycle (3.3)--(3.7) has all of the following properties.

1.  It obeys both exact block identities and the potential telescope

    \[
       a_{j+1}-a_j-c_j=-\widehat c_j.              \tag{3.8}
    \]

2.  The area increments \(a_j-b_j\) sum to zero around the cycle.

3.  Its total ordinary voltage is a multiple of \(N\).

4.  Its voltage itinerary has least quotient period \(T=\Theta(N)\).

5.  The ordinary omitted-coordinate itinerary visits every one of the
    \(N\) coordinates.

6.  Every block contains a nonwrapping first return of step-two duration
    \(s\), positive residence \(s+1\), winding one, and height \(h=s-1\).
    Choosing one per block gives
    \(2(e-1)=\Theta(T/s)=\Theta(\sqrt N)\) pairwise
    quotient-edge-disjoint returns.  Their half-shifted supports are also
    pairwise disjoint.

#### Proof

Statement 1 is (3.6).  There are equally many seams of the two signs, and

\[
 a_j-b_j=0,-2,+2
\]

at the three phase types.  This proves statement 2.

The ordinary two-step voltage at phase \(j\) is \(a_j+b_j\).  The seam
corrections cancel, so the full voltage is

\[
 \sum_{j<T}(a_j+b_j)=2aT.
\]

Using (3.1) and (3.3),

\[
 2aT
 =4e(s-1)(e-1)(2s+1)
 =4(s-1)(e-1)N,                                    \tag{3.9}
\]

which proves statement 3.

Any period of the \(b\)-word must preserve its seam set, whose consecutive
gaps all equal \(L\); it is therefore a multiple of \(L\).  On the block
quotient, the seam-sign word is

\[
 +^{,e-1}-^{,e-1},
\]

whose least cyclic period is \(2(e-1)\).  Hence the least phase period is
\(T\), proving statement 4.

Now follow the ordinary omitted coordinate.  Away from a seam, every
ordinary increment is \(a\).  Since

\[
 \gcd(a,N)
 =e\gcd(s-1,2s+1)=e,                              \tag{3.10}
\]

where the last equality uses \(s\not\equiv1\pmod3\), repeated increments
by \(a\) visit every point of one residue class modulo \(e\), with exact
period \(L\).  Before the last increment of each block there are more than
\(L\) consecutive ordinary increments equal to \(a\), so that whole
residue class is visited.  A positive seam changes the next residue class
by \(+2\) modulo \(e\).  Since \(e\) is odd, the first \(e\) block
residues

\[
 0,2,4,\ldots,2(e-1)\pmod e
\]

are all distinct.  Thus every physical coordinate is visited.  The
negative seams return through the same residue classes, proving statement
5 together with the voltage closure.

The first \(2s\) phases of every block are ordinary.  Choose, for example,
the first \(s\) of them.  On the corresponding return interval,

\[
 c_j=\widehat c_j=3e
\]

and therefore

\[
 \sum_{j<s}c_j=3es=N+a_s,
 \qquad
 \sum_{j<s}\widehat c_j=3es=N+a_0.                \tag{3.11}
\]

Both ledgers have winding one.  On the ordinary one-step itinerary, the
\(2s+1=L\) consecutive increments, including the terminal endpoint step,
all equal \(a\).  Their sum is

\[
 La=(2s+1)e(s-1)=(s-1)N.                          \tag{3.12}
\]

Equation (3.10) says that no positive proper prefix is zero modulo \(N\).
Thus this is exactly the first return, not merely a return congruence.

Intervals chosen from different blocks have disjoint full supports:
each has \(s+2<2s+1=L\) edges and is contained in its own block.
Applying the parity permutation \(\phi\) sends disjoint even supports to
disjoint odd supports.  Finally \(h=s-1\), so the exact inequalities
\(h+1\le s+1\) and \(h+2\le s+2\) hold, and all three quantities are at
the same Gaussian order.  Since

\[
 {2(e-1)\over T}={1\over2s+1}=\Theta(N^{-1/2}),
\]

statement 6 follows. \(\square\)

### Theorem 3.2 (aperiodic amplification at total mass \(B_m\))

The construction can be amplified to a family of distinct aperiodic
voltage itineraries using \((1-o(1))B_m\) formal phases and carrying

\[
 \boxed{\Theta_A(B_m/\sqrt m)}
 \tag{3.13}
\]

pairwise support-disjoint winding-one returns.  Every amplified cycle
still has full coordinate coverage, exact voltage and area closure, and
least quotient period \(\Omega(N^2)\).

#### Proof

Regard the \(T=2(e-1)L\) phases of Theorem 3.1 as one motif of
\(2(e-1)\) blocks.  Write

\[
 \rho_q=b_j-a
\]

at the last phase of block \(q\).  In the first \(e-1\) blocks retain
\(\rho_q=2\).  In the last \(e-1\) blocks use one of the two sign words

\[
 (-4,0,-2,\ldots,-2),
 \qquad
 (0,-4,-2,\ldots,-2),                              \tag{3.14}
\]

where the tail contains \(e-3\) copies of \(-2\).  Call these motifs
\(\mathcal M_0,\mathcal M_1\).  In either case

\[
 \sum_{q<2(e-1)}\rho_q
 =2(e-1)-4-2(e-3)=0.                               \tag{3.15}
\]

Thus the area increments, which equal \(-\rho_q\) at the seams, sum to
zero.  The motif voltage remains

\[
 2aT+\sum_q\rho_q=2aT,
\]

which is the multiple of \(N\) in (3.9).  The first \(e-1\) seams are
unchanged, so the forward tour through the residue classes
\(0,2,\ldots,2(e-1)\pmod e\) still proves complete coordinate coverage
inside every motif.

At every phase one still has \(a_{j+1}=a_j=a\) and

\[
 c_j=\widehat c_j=3e-\rho_q
 \in\{3e-2,3e,3e+2,3e+4\}                         \tag{3.16}
\]

at a seam, with value \(3e\) elsewhere.  These are positive odd
integers.  The first \(2s\) phases of every block remain ordinary, so the
same return selected in Theorem 3.1 is unaffected.

Put \(M=N+1\).  Given a cyclic binary word
\(\boldsymbol\epsilon=(\epsilon_0,\ldots,\epsilon_{M-1})\), concatenate
the motifs

\[
 \mathcal M_{\epsilon_0}\cdots\mathcal M_{\epsilon_{M-1}}.
 \tag{3.17}
\]

The runs of \(e-1\) consecutive \(+2\) seams identify the motif
boundaries.  Inside each motif the ordered pair \((-4,0)\) or
\((0,-4)\) recovers its bit.  Hence an aperiodic binary necklace gives a
voltage itinerary of least phase period exactly \(MT\), and distinct
necklaces give distinct cyclic voltage itineraries.

The number of periodic ordered binary words of length \(M\) is at most
\(M2^{M/2}\).  Therefore, for all large \(M\), there are at least
\(2^{M-1}/M\) aperiodic binary necklaces.  Since

\[
 B_m\le4^m=2^{N-1}=2^{M-2},                        \tag{3.18}
\]

there are enough distinct necklaces to choose

\[
 Q=\left\lfloor {B_m\over MT}\right\rfloor         \tag{3.19}
\]

formal cycles.  Their total number of phases is

\[
 QMT=B_m-O_A(N^2)=(1-o(1))B_m.                    \tag{3.20}
\]

Each motif supplies \(2(e-1)\) selected intervals, one per block.
Consequently the family contains

\[
 QM\,2(e-1)
 ={(1-o(1))B_m\over L}
 =\Theta_A(B_m/\sqrt m)                            \tag{3.21}
\]

pairwise support-disjoint winding-one returns.  Every quotient cycle has
length

\[
 MT=(N+1)2(e-1)(2s+1)=\Omega_A(N^2)\gg H_A.
\]

All assertions follow. \(\square\)

## 4. Every phase of the obstruction is literally Dyck-realizable

It remains to verify that the scalar values in Theorem 3.1 are not ruled
out by the local first-dominant word geometry.

Fix one of its phase quadruples

\[
 (a,b,c,\widehat c),
 \qquad
 a+b+c=N,
 \qquad
 \widehat c=c\in\{3e-2,3e,3e+2,3e+4\}.           \tag{4.1}
\]

Put

\[
 t={a-h-\widehat c+1\over2},
 \qquad
 u={b-h\over2},
 \qquad
 v={c-1\over2}.                                   \tag{4.2}
\]

All three are nonnegative integers for \(s\ge7,e\ge3\).  Choose Dyck
words \(A,B,T_0,S\) of semilengths \(t,u,v,v\), respectively, all of
height at most two, and define

\[
 D=
 1A1^{h-2}\,\overline{T_0}\,1\,0^{h-1}B\,0S.     \tag{4.3}
\]

Here the bar interchanges zero and one.

### Lemma 4.1 (literal two-fringe realization)

The word (4.3) is a first-dominant Dyck word of semilength \(m\) and
height \(h\).  In its canonical first-maximum factorization

\[
 D=P1R0S
\]

one has exactly

\[
 \boxed{
 \delta(D)=a,\quad
 \delta(\phi D)=b,\quad
 d(D)=c,\quad
 d(\phi D)=\widehat c.}                            \tag{4.4}
\]

#### Proof

Starting with the first symbol, the word \(A\) is read at height one.
The following \(h-2\) up-steps reach height \(h-1\) for the first time.
Since \(T_0\) has height at most two and \(h\ge6\), the complemented word
\(\overline{T_0}\), read from height \(h-1\), stays strictly positive
and returns to height \(h-1\).  The displayed following up-step is
therefore the first step reaching height \(h\).

The block \(0^{h-1}B\) ends at height one and never reaches height \(h\);
the displayed zero closes the first primitive component.  The suffix
\(S\) has height at most two.  Hence the first primitive component is
uniquely tallest and \(D\) is first-dominant of height \(h\).

Its canonical pieces are

\[
 P=1A1^{h-2}\overline{T_0},
 \qquad R=0^{h-1}B,
 \qquad S=S.
\]

By (4.2),

\[
 |P|+1=2t+h+\widehat c-1=a,
\]

\[
 |R|+1=2u+h=b,
 \qquad
 |S|+1=2v+1=c.                                    \tag{4.5}
\]

The general two-step block theorem gives \(\delta(\phi D)=|R|+1=b\).
For a first-dominant word, the exact two-fringe theorem says that
\(d(\phi D)=|P^+|+1\), where \(P^+\) is the suffix of \(P\) after its
first hit of height \(h-1\).  Here

\[
 P^+=\overline{T_0},
\]

so \(d(\phi D)=|T_0|+1=2v+1=\widehat c\).  This proves (4.4).

Finally, the length of (4.3) is

\[
 (a-1)+1+(b-1)+1+(c-1)=N-1=2m,
\]

so its semilength is exactly \(m\). \(\square\)

There are enough choices to assign distinct literal roots to every phase
of one amplified cycle.  Indeed, for a fixed phase type,
\(t,u=\Theta(N)\) and \(v=\Theta(\sqrt N)\).  For every
\(0\le q\le t-2\),

\[
 A_q=(10)^q1100(10)^{t-q-2}
\]

is a distinct height-two choice for \(A\).  The analogous constructions
supply \(u-1\) choices for \(B\) and \(v-1\) choices for \(S\).  Thus
there are

\[
 (t-1)(u-1)(v-1)=\Theta(N^{5/2})>MT                \tag{4.6}
\]

distinct roots of every required phase type for all sufficiently large
\(s\).  Lemma 4.1 therefore verifies statewise literal Dyck geometry,
not just parity and positivity, throughout each amplified formal cycle.

### Theorem 4.2 (Gaussian-height repair of the Z14 witness)

Use the complete-colour cocycle parameters

\[
 s\equiv6\pmod {12},\quad k\ {\rm odd},\quad
 N=k(2s+1),\quad a=k(s-1),\quad c=3k.              \tag{4.6a}
\]

Thus \(2a+c=N\), and every selected formal return has local quadruple
\((a,a,c,c)\).  Put

\[
 h=s-1,\qquad
 t={a-h-c+1\over2},\qquad
 u={a-h\over2},\qquad
 v={c-1\over2}.                                    \tag{4.6b}
\]

For all sufficiently large admissible \(s\), there is a literal
first-dominant semilength-\(m\) Dyck word of height exactly \(h=s-1\)
such that

\[
 \boxed{\delta(D)=\delta(\phi D)=a,\qquad
 d(D)=d(\phi D)=c.}                                \tag{4.6c}
\]

#### Proof

All three quantities in (4.6b) are nonnegative integers; in particular

\[
 2t=k(s-4)-s+2\ge0.
\]

Choose height-at-most-two Dyck words \(A,B,T_0,S\) of semilengths
\(t,u,v,v\), and set

\[
 D=1A1^{h-2}\overline{T_0}\,1\,0^{h-1}B\,0S.
\]

Lemma 4.1 applies verbatim, giving first-dominance, height \(h\), and the
four identities in (4.6c).  Its length is exact because

\[
 |D|=a+a+c-1=N-1=2m.
\]

\(\square\)

The original Z14 local witness had height
\(a-c+1=k(s-4)+1=\Theta(N)\).  Theorem 4.2 replaces it by a witness of
the floor-correct Gaussian height \(s-1\).  Hence the Z14 formal system
now simultaneously has the audited first- and second-deficit moment
orders, distinct aperiodic voltage itineraries, complete colour, exact
area and both parity ledgers, critical support-separated winding-one
packing, and height-compatible literal first-dominant feasibility at every
selected start.  Its sole remaining failure is simultaneous orbit
realizability.

The construction deliberately stops one statement short of a PBBS
counterexample: it does not prove that the literal root assigned to phase
\(j+1\) equals \(\tau\) of the root assigned to phase \(j\).  The exact
meaning of Theorem 3.1 and Lemma 4.1 is consequently the no-go

\[
 \boxed{
 \begin{gathered}
 \text{two ledgers + first-return chronology + both-parity disjointness}\\
 {}+\text{ height and area + long period + full coordinate coverage}\\
 +\text{ statewise literal first-dominant Dyck realizability}
 \end{gathered}
 \not\Longrightarrow o(B_m/\sqrt m)}              \tag{4.7}
\]

Theorem 3.2 already amplifies the model to \((1-o(1))B_m\) formal phases
with distinct aperiodic itineraries.  Theorem 4.2 independently repairs
the same height issue in the exact-moment Z14 model.  Neither construction
injects its pointwise witnesses into one simultaneous PBBS orbit.
Accordingly, a successful PBBS argument must
compare the literal words at two or more successive phases.  Equivalently,
it must use
the exact recursion

\[
 P_{j+1}1R_{j+1}0S_{j+1}=S_j1P_j0R_j             \tag{4.8}
\]

or a theorem which genuinely implies a restriction of the same strength.

## 5. Final proved/conditional boundary

The positive-winding contribution to the corrected coefficient-one gate
is proved negligible in each of the following sectors:

\[
 w\to\infty,\qquad {s+2\over h+2}\to\infty,\qquad
 h\le {\sqrt m\over\log m},                       \tag{5.1}
\]

with the quantified estimates (0.1)--(0.3).  Fixed winding is not empty:
Theorem 2.1 gives genuine exact PBBS returns, although only on negligible
short quotient cycles.

The unresolved long-cycle sector can be taken to have bounded or
arbitrarily slowly growing winding, Gaussian height, and duration within
an arbitrarily slowly growing factor of height.  The coverage-complete
model proves that every disjoint-replication-stable scalar chronology,
both endpoint ledgers, and even statewise literal two-fringe geometry are
insufficient there.  Theorem 4.2 repairs the Gaussian-height mismatch in
the stronger exact-moment, distinct-itinerary Z14 obstruction.  Thus the
exact unproved statement is now solely a simultaneous cross-phase
consequence of (4.8), strong enough to show

\[
 \boxed{|\mathcal P_+|=o_A(B_m/\sqrt m).}          \tag{5.2}
\]

No claim of (5.2), of the full corrected packing gate, or of coefficient
one is made.
