# Period-\(2q\) context paths have simple owner reserves, but force an upper cap at every junction

**Date:** 2026-08-13  
**Method:** refine every exact-distance context edge into an ordinary
Johnson geodesic and use the antipodal half of a period-\(2q\) toggle
cycle.  No computation or search is used.

**Status:** unconditional single-commodity positive owner theorem and an
exact obstruction to composing these elementary rail squares with a
simple immediate-upper palette.  The obstruction does not rule out a
compound cap-coalescing actuator.

## 1. Setup

Put

\[
 q=d+1,\qquad c=R-q,\qquad r=R-1=c+d.
\tag{1.1}
\]

Fix distinct coordinates \(x,p\), and for every
\(A\in\binom{[k]\setminus\{x,p\}}r\) write

\[
 \delta_{xp}(A)=e_{A\cup\{x\}}-e_{A\cup\{p\}}.
\tag{1.2}
\]

Assume

\[
 q\ge2,qquad c\ge d,qquad k-R\ge q.
\tag{1.3}
\]

These inequalities hold for the central parameters for all sufficiently
large \(k\).

## 2. One exact-distance edge

Let \(A,B\) be contexts with

\[
 |A\cap B|=c.
\]

Write

\[
 D=A\cap B,qquad L=A\setminus D,qquad S=B\setminus D,
 \qquad |L|=|S|=d.
\]

Choose orders

\[
 L=(\ell_1,\ldots,\ell_d),qquad
 S=(s_1,\ldots,s_d),
\]

and the period-\(2q\) cyclic toggle orders

\[
 \sigma=(L,x,p,S),qquad \sigma'=(L,p,x,S).
\tag{2.1}
\]

With core \(D\), these are legal unprotected pure rails: their toggle
traces are \(1^q0^q\), every proper cyclic interval row is simple, and
the complete state regenerates after \(2q\) positions.

### Lemma 2.1 (exact square and common deck)

The two owner columns obey

\[
 f(D,\sigma)-f(D,\sigma')
 =\delta_{xp}(A)-\delta_{xp}(B).
\tag{2.2}
\]

Their common owner deck consists of the following \(2d=2q-2\) values:

\[
 F_j=D\cup\{\ell_{j+1},\ldots,\ell_d\}
       \cup\{s_1,\ldots,s_{j-1}\}\cup\{x,p\},
\tag{2.3}
\]

\[
 K_j=D\cup\{\ell_1,\ldots,\ell_j\}
       \cup\{s_j,\ldots,s_d\},
 \qquad 1\le j\le d.
\tag{2.4}
\]

#### Proof

An adjacent transposition in a proper cyclic window deck changes exactly
the two \(q\)-windows containing one of \(x,p\) but not the other.  They
are

\[
 A+x,\quad B+p
 \qquad\hbox{versus}\qquad
 A+p,quad B+x,
\]

which proves (2.2).  The other common windows split into the \(d\)
windows containing both special labels, namely (2.3), and their antipodal
\(q\)-window complements inside the \(2q\)-toggle cycle, namely (2.4).
The \(F_j\)'s contain both \(x,p\), the \(K_j\)'s contain neither, and
proper-window simplicity makes each displayed family simple. \(\square\)

Equivalently, if

\[
 A=G_0,G_1,\ldots,G_d=B,
 \qquad
 G_j=D\cup\{\ell_{j+1},\ldots,\ell_d\}
        \cup\{s_1,\ldots,s_j\},
\]

is the associated ordinary Johnson geodesic, then

\[
 F_j=(G_{j-1}\cap G_j)\cup\{x,p\}.
\tag{2.5}
\]

Thus choosing the two local orders is exactly choosing an ordinary
geodesic refinement of the exact-distance edge.

## 3. A squarefree reserve for any one context pair

### Theorem 3.1 (single-pair conformal period-\(2q\) lift)

For any distinct contexts \(A,B\), there is a context path

\[
 A=A_0,A_1,\ldots,A_\ell=B,qquad
 |A_{i-1}\cap A_i|=c,
\]

and period-\(2q\) rail pairs on its edges such that

\[
 \mathcal R\mathbin{\dot\cup}
 \{A\cup\{x\},B\cup\{p\}\}
 =\mathop{\dot\bigcup}_{i=1}^{\ell}\operatorname{supp}Q_i^+,
\tag{3.1}
\]

\[
 \mathcal R\mathbin{\dot\cup}
 \{A\cup\{p\},B\cup\{x\}\}
 =\mathop{\dot\bigcup}_{i=1}^{\ell}\operatorname{supp}Q_i^-.
\tag{3.2}
\]

Every union displayed here is genuinely owner-disjoint, every rail is
depth-\(d\) positive- and zero-resident, and

\[
 \ell\le
 \left\lfloor\frac{\operatorname{dist}(A,B)}d\right\rfloor+2,
 \qquad
 |\mathcal R|=2q\ell-2.
\tag{3.3}
\]

#### Proof

Put \(t=\operatorname{dist}(A,B)\).  While at least \(d\) differences
remain, exchange one fresh \(d\)-block of \(A\setminus B\) for one fresh
\(d\)-block of \(B\setminus A\).  This gives a block-monotone prefix of
\(m=\lfloor t/d\rfloor\) exact-distance edges and leaves residual
distance \(s=t-md<d\).

First suppose \(s=0\).  Let

\[
 Y=B\setminus A
\]

and let \(E_i\) be the \(i\)-th block edge.  For the common values (2.3)
on \(E_i\), the statistic \(|F_j\cap Y|\) runs through

\[
 (i-1)d,(i-1)d+1,\ldots,id-1.
\tag{3.4}
\]

For the antipodal values (2.4), \(|K_j\cap Y|\) runs through

\[
 (i-1)d+1,(i-1)d+2,\ldots,id.
\tag{3.5}
\]

The intervals in (3.4) are disjoint for different \(i\), as are those in
(3.5); and an \(F\)-value contains both \(x,p\), whereas a \(K\)-value
contains neither.  Hence all common decks in the monotone prefix are
mutually disjoint.

Now suppose \(0<s<d\), and denote the last prefix context by \(A'\).
Write

\[
 I=A'\cap B,\quad X=A'\setminus B,\quad Y_0=B\setminus A',
 \qquad |X|=|Y_0|=s.
\]

Choose \(O\subseteq I\), \(|O|=d\), and choose

\[
 Z\subseteq[k]\setminus(A'\cup B\cup\{x,p\}),
 \qquad |Z|=d-s.
\]

The choices exist by (1.3).  Put

\[
 J=I\setminus O,qquad
 T=J\cup X\cup Y_0\cup Z.
\tag{3.6}
\]

Then \(|A'\cap T|=|T\cap B|=c\), so append the two exact-distance
edges \(A'-T-B\).

For the first edge use removal block \(O\) and addition block
\(Y_0\cup Z\); for the second use removal block \(X\cup Z\) and addition
block \(O\).  Choose

\[
 y_0\in Y_0,qquad x_0\in X,qquad z_0\in Z,
\]

put \(y_0\) first and \(z_0\) last in the order of \(Y_0\cup Z\), put
\(x_0\) first in the order of \(X\cup Z\), and use the same order of
\(O\) as removal order on the first edge and addition order on the second.

Every \(F\)-value of the first terminal edge contains \(x_0\), while
every \(F\)-value of the second omits \(x_0\).  Thus the two \(F\)-decks
are disjoint.  If a first-edge \(K_j\) equalled a second-edge \(K_h\),
comparison of their \(O\)-parts would force

\[
 h=d-j+1,
 \qquad
 \{o_1,\ldots,o_j\}
   =\{o_h,\ldots,o_d\}.
\]

With the same order on \(O\), this is impossible for \(j<d\), since the
left set contains \(o_1\) and omits \(o_d\), while the right set does the
opposite.  For \(j=d\), equality would require the last point of the
first addition block to belong to \(Y_0\); it is \(z_0\notin Y_0\).
Hence the two \(K\)-decks are also disjoint.

They are also disjoint from the monotone prefix.  All first-edge
\(K\)-values contain the fresh label \(z_0\); all second-edge common
values contain \(Y_0\), which the prefix never uses.  A first-edge
\(F_j\) contains exactly \(md+j-1\) points of the original difference
set \(B\setminus A\), whereas every prefix \(F\)-value contains at most
\(md-1\).  Thus the first-edge \(F\)-deck is disjoint from the prefix as
well.

Finally, the changed endpoint owners on consecutive edges telescope.
At every internal context \(A_i\), the two owners

\[
 A_i\cup\{x\},\qquad A_i\cup\{p\}
\]

occur once on each aggregate shore and are placed in the common reserve.
They are distinct because the context path is simple, and they cannot
collide with (2.3)--(2.4), which contain respectively both or neither of
the special labels.  This proves the disjoint identities (3.1)--(3.2).
Each edge contributes \(2q-2\) common deck owners and each of the
\(\ell-1\) internal contexts contributes two lifted owners, giving

\[
 |\mathcal R|=\ell(2q-2)+2(\ell-1)=2q\ell-2.
\]

Period \(2q\) gives one-runs and zero-runs both exactly \(q=d+1\), so
the residence and regeneration assertions follow. \(\square\)

Theorem 3.1 is an actual positive-semigroup statement, not signed-lattice
membership.  It also shows why the old two-extra-label period hypothesis
was not intrinsic to the owner absorber.

## 4. The immediate-upper cap barrier

The preceding theorem is deliberately only an owner theorem.  The next
fact shows why it does not automatically lift to the compulsory immediate
upper row.

### Theorem 4.1 (every serial junction duplicates one upper cap)

For any adjacent-transposition rail realizing

\[
 \delta_{xp}(A)-\delta_{xp}(B),
\]

both rail states contain, in their width-\((q+1)\) source-interval decks,
the two common targets

\[
 A\cup\{x,p\},qquad B\cup\{x,p\}.
\tag{4.1}
\]

Consequently, if \(\ell\ge2\) such rail currents are composed serially
along a simple context path

\[
 A_0,A_1,\ldots,A_\ell,
\]

then for every internal \(i\), the immediate-upper target

\[
 A_i\cup\{x,p\}
\tag{4.2}

occurs in both the incoming and outgoing component.  The aggregate
immediate-upper deck therefore has multiplicity at least two at each of
the \(\ell-1\) internal caps, independently of every cyclic-order choice.

#### Proof

In the local order \(L,x,p,S\), the \((q+1)\)-window \(L,x,p\) has union
\(A\cup\{x,p\}\), and the \((q+1)\)-window \(x,p,S\) has union
\(B\cup\{x,p\}\).  Swapping the adjacent labels \(x,p\) changes neither
set.  This proves (4.1).  Apply it to the right endpoint of edge \(i\)
and the left endpoint of edge \(i+1\) to obtain the same target (4.2)
twice. \(\square\)

This is not a defect of period \(2q\).  It holds for every
adjacent-transposition rail realization of the context current, at every
larger period as well.

## 5. Consequence for the special star residual

In the balanced context decomposition of the special residual, for every
\(p\in P\setminus\{x\}\), exactly one source context must be routed to
the distinguished insertion sink \(A_p^\Delta\).  The proved source/sink
geometry gives ordinary Johnson distance at least \(c-q\).  Since one
exact-distance context edge changes only \(d=q-1\) points, every such
route has length at least

\[
 L_0=\left\lceil\frac{c-q}{q-1}\right\rceil.
\tag{5.1}
\]

Therefore any realization obtained by composing independent elementary
rail currents has, inside the collection of forced path-cap occurrences,
immediate-upper multiplicity excess at least

\[
 \boxed{
 (q-1)(L_0-1)
 \ge c-2q+1.}
\tag{5.2}
\]

For the central parameters this is \(\Theta(k)\), not \(O(1)\).

The inequality counts multiplicity excess, so collisions between caps
belonging to different paths cannot improve it: taking a union can only
decrease the number of distinct targets relative to the total number of
occurrences.

## 6. Exact remaining gate

The owner-level reserve-first problem is solved for every individual
context commodity by Theorem 3.1.  The naive serial strategy nevertheless
cannot satisfy a squarefree immediate-upper ticket bank because of
Theorem 4.1.  This is not, by itself, an obstruction to mere upper-target
coverage: a global construction can have deliberately repeated upper
targets.  It is an obstruction whenever these local occurrences are
required to be distinct or are already charged to a fixed protected
upper-ticket capacity.

The remaining local theorem must be a **cap-coalescing compound lift**:
it must replace a whole context path at once, so that each internal target

\[
 A_i\cup\{x,p\}
\]

is represented by one physical upper occurrence shared across the two
neighbouring transfer stages, rather than by two occurrences belonging to
two independent closed rails.  Equivalently, it must fuse the elementary
cycles at their common upper caps while preserving the owner reserve,
residence, all lower tickets, and closed trace.

Thus the first unresolved cut is no longer squarefree owner packing.  It
is literal occurrence coalescence at the immediate-upper caps; without
such coalescence, the special long routes have a forced linear defect.
