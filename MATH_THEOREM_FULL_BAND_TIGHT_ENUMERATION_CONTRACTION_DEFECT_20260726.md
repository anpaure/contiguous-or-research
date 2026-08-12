# Full-band tight enumerations: exact parity contraction and the irreducible chronology defect

Date: 2026-07-26

Method: pure mathematics.  The only external input is the existence of a
tight enumeration for every interval of consecutive cube levels, as in
Gregor--Mička--Mütze, Corollary 2 (equivalently Gregor--Mütze for the
non-central cases).  Everything below holds for **every** such tight
enumeration.

## 0. Verdict

Let

\[
 n=2m+1,
 \qquad
 \mathcal B_H=\bigcup_{q=0}^{H}\binom{[n]}{m-q},
 \qquad
 W=\binom n m .
\]

Write

\[
 A_H=\sum_{\substack{0\le q\le H\\q\ {m even}}}
             \binom n{m-q},
 \qquad
 B_H=\sum_{\substack{0\le q\le H\\q\ {m odd}}}
             \binom n{m-q}.
\]

Every tight enumeration of \(\mathcal B_H\) has a canonical first
contraction to a Hamilton cycle on the \(A_H\) even-depth vertices of the
band, every edge of that cycle changing exactly two coordinates.  Contract
again to the \(W\) rank-\(m\) vertices, listed in their inherited cyclic
order.  If \(t_i\) is the number of two-flip edges in the \(i\)-th gap and
\(d_i\) is the Johnson distance between its two rank-\(m\) endpoints, then

\[
 \boxed{
 \sum_{i=0}^{W-1}(d_i-1)
 +\sum_{i=0}^{W-1}(t_i-d_i)
 = A_H-W
 =\sum_{\substack{2\le q\le H\\q\ {m even}}}
      \binom n{m-q}.}
 \tag{0.1}
\]

Both sums on the left are nonnegative.  They have exact meanings:

* \(\sum(d_i-1)\) is the number of extra Johnson edges required to replace
  the inherited rank-\(m\) order by geodesics while retaining all its
  rank-\(m\) visits;
* \(2\sum(t_i-d_i)\) is exactly the number of physical coordinate-flip
  occurrences cancelled by parity inside the rank-\(m\) gaps.

Consequently a full-band tight enumeration cannot simultaneously give

1. adjacent consecutive rank-\(m\) owners, and
2. return-free physical chronology between those owners,

unless \(H\le1\).  If the inherited owner order is a Johnson cycle, then
all of the right side of (0.1) is forced into physical cancellations.  If
the physical excursions are return-free, all of it is forced into
nonadjacent owner gaps.

For growing \(H\),

\[
 A_H-W=\Theta\!\left(W\min\{H,\sqrt m\}\right).
 \tag{0.2}
\]

In particular, when \(H\to\infty\) and \(H=o(\sqrt m)\),

\[
 A_H=(\lfloor H/2\rfloor+1+o(H))W,
 \qquad
 A_H-W=(\lfloor H/2\rfloor+o(H))W.
 \tag{0.3}
\]

Thus the full-band theorem is not a source of a coefficient-one literal
OR word.  It contains \(A_H\) two-flip chronology slots, whereas a spanning
rank-\(m\) owner cycle has only \(W\).  In the Johnson-adjacent branch the
fraction of the physical chronology cancelled on contraction is

\[
 {A_H-W\over A_H}=1-{W\over A_H}=1-o(1)
 \tag{0.4}
\]

whenever \(H\to\infty\).  Tightness pays local metric optimality in the
band; it does not pay the global chronology compression needed by the
coefficient-one compiler.

## 1. The larger parity class

Put

\[
 N_q=\binom{2m+1}{m-q}.
\]

The even-depth class is always the larger bipartition class.  Indeed,
the alternating partial-sum identity

\[
 \sum_{j=0}^{r}(-1)^j\binom Nj=(-1)^r\binom{N-1}r
\]

gives

\[
 \begin{aligned}
 A_H-B_H
 &=\sum_{q=0}^{H}(-1)^q\binom{2m+1}{m-q}\\
 &=\binom{2m}{m}+(-1)^H\binom{2m}{m-H-1}.
 \end{aligned}
 \tag{1.1}
\]

For odd \(H\), the second binomial coefficient is strictly smaller than
the first; for even \(H\) it is added.  Hence

\[
                         A_H>B_H.                 \tag{1.2}
\]

The exact imbalance is the quantity in (1.1).

## 2. Tightness forces a Hamilton cycle in the even halved band

Let a cyclic enumeration of all \(A_H+B_H\) vertices have

* \(a\) consecutive pairs of opposite parity;
* \(b\) consecutive pairs both in the odd-depth class;
* \(c\) consecutive pairs both in the even-depth class.

Counting the two cyclic incidences at every vertex yields

\[
                         2B_H=a+2b,
 \qquad
                         2A_H=a+2c.                \tag{2.1}
\]

An opposite-parity pair has odd Hamming distance at least one.  A pair of
distinct vertices in the same parity class has even Hamming distance at
least two.  Therefore the total number of flipped coordinates is at least

\[
                         a+2b+2c=2A_H+2b.          \tag{2.2}
\]

By definition, a tight enumeration has total flip length

\[
 (A_H+B_H)+(A_H-B_H)=2A_H.                         \tag{2.3}
\]

Equality in (2.2) is therefore forced.

### Theorem 2.1 (exact first contraction)

Every tight enumeration of \(\mathcal B_H\) satisfies:

1. \(b=0\);
2. every opposite-parity step has Hamming distance one;
3. every even--even step has Hamming distance two;
4. \(a=2B_H\) and \(c=A_H-B_H\).

Deleting all odd-depth vertices gives a Hamilton cycle

\[
                         Y_0,Y_1,\ldots,Y_{A_H-1},Y_0
 \tag{2.4}
\]

on the even-depth band

\[
 \mathcal E_H=\bigcup_{\substack{0\le q\le H\\q\ {m even}}}
                    \binom{[n]}{m-q},
 \tag{2.5}
\]

and every edge of (2.4) has Hamming distance exactly two.

#### Proof

Equations (2.2)--(2.3) force \(b=0\) and equality in every local distance
lower bound.  An odd-depth vertex is therefore flanked by two distinct
even-depth vertices at cube distance one from it.  Those two vertices
differ in exactly two coordinates.  A direct even--even pair also differs
in exactly two coordinates.  Suppressing each odd vertex consequently
turns the original enumeration into (2.4), which visits every even-depth
vertex once. \(\square\)

An edge of (2.4) either deletes two elements, inserts two elements, or
exchanges one element for another.  We call its unordered two-coordinate
support its **physical pair label**.  Choosing either order of these two
toggles expands the edge into two physical flip tokens; the counting below
is independent of that choice.

## 3. The exact top-gap conservation law

The cycle (2.4) contains every rank-\(m\) set exactly once.  Retain these
vertices in inherited cyclic order:

\[
                         X_0,X_1,\ldots,X_{W-1},X_0.           \tag{3.1}
\]

Let the \(i\)-th **top gap** be the segment of (2.4) from \(X_i\) to
\(X_{i+1}\), with no internal rank-\(m\) vertex.  Put

\[
 t_i=\text{number of edges in that segment},
 \qquad
 d_i=d_J(X_i,X_{i+1})={|X_i\triangle X_{i+1}|\over2}.         \tag{3.2}
\]

The top sets in (3.1) are distinct, so \(d_i\ge1\).  Every edge of (2.4)
has Hamming length two, hence the triangle inequality gives

\[
                         1\le d_i\le t_i.                     \tag{3.3}
\]

All \(A_H\) edges of (2.4) belong to exactly one top gap, so

\[
                         \sum_i t_i=A_H.                      \tag{3.4}
\]

Define

\[
 D=\sum_i(d_i-1),
 \qquad
 R=\sum_i(t_i-d_i).                                           \tag{3.5}
\]

### Theorem 3.1 (distance--return conservation)

For every full-band tight enumeration,

\[
 \boxed{D+R=A_H-W.}                                          \tag{3.6}
\]

Moreover, after expanding the physical pair labels in the \(i\)-th gap,
let \(k_{i,x}\) be the number of occurrences of coordinate \(x\).  Then

\[
 2(t_i-d_i)
   =\sum_{x\in[n]}\bigl(k_{i,x}-(k_{i,x}\bmod2)\bigr).       \tag{3.7}
\]

Thus \(2R\) is exactly the total number of flip tokens removed when every
even-parity cancellation is erased.  In particular,

\[
 R=0
 \quad\Longleftrightarrow\quad
 \text{every top gap has pairwise distinct physical coordinates}.
 \tag{3.8}
\]

#### Proof

By (3.4),

\[
 D+R=\sum_i[(d_i-1)+(t_i-d_i)]
     =\sum_i(t_i-1)=A_H-W,
\]

which proves (3.6).

The coordinates occurring an odd number of times on a path are exactly
the coordinates on which its endpoints differ.  Hence exactly \(2d_i\)
coordinates have odd \(k_{i,x}\), while \(\sum_xk_{i,x}=2t_i\).  This
gives (3.7).  The right side of (3.7) vanishes exactly when every nonzero
\(k_{i,x}\) equals one, proving (3.8). \(\square\)

### Corollary 3.2 (the two extreme branches)

1. The inherited top order (3.1) is a Johnson cycle if and only if
   \(D=0\).  In that case
   \[
                             R=A_H-W.                          \tag{3.9}
   \]
2. If all physical top gaps are return-free, then \(R=0\), and
   \[
       \sum_i d_i=A_H,
       \qquad
       {1\over W}\sum_i d_i={A_H\over W}.                     \tag{3.10}
   \]
   Thus the inherited consecutive top owners have average Johnson distance
   \(A_H/W\), rather than one.
3. A literal geodesic subdivision of the inherited top gaps requires
   exactly
   \[
                             D=\sum_i(d_i-1)                   \tag{3.11}
   \]
   additional internal rank-\(m\) owner slots.  But (3.1) already uses all
   \(W\) rank-\(m\) sets as endpoints.  Therefore no such subdivision can
   retain every inherited top visit unless \(D=0\).

The first assertion follows from \(d_i=1\) for every \(i\); the second and
third are the definitions of Johnson distance and a Johnson geodesic.

### Corollary 3.3 (short-gap form of the chronology obstruction)

Suppose the inherited top order is a Johnson cycle and the expanded
physical word has no repeated coordinate in any window of \(2h\) flip
tokens.  Then every top gap satisfies

\[
                         t_i=1\quad\text{or}\quad t_i>h.       \tag{3.12}
\]

Indeed, if \(2\le t_i\le h\), then (3.9) forces a cancelled coordinate
inside its \(2t_i\le2h\) tokens, contradicting label separation.

This does not by itself forbid all long-gap concentrations.  It shows
exactly what additional theorem would be necessary: nearly all lower-band
vertices would have to be packed into expiration gaps longer than the
protected chronology window.  Tightness supplies no such assertion.

## 4. Size of the forced defect

The central binomial ratios satisfy, uniformly for \(q=o(m^{2/3})\),

\[
 {N_q\over W}
 =\prod_{j=0}^{q-1}{m-j\over m+2+j}
 =\exp\!\left(-{q(q+1)\over m}
       +O\!\left({q+q^3\over m^2}\right)\right).             \tag{4.1}
\]

Consequently, if \(H=o(\sqrt m)\), then \(N_q=(1-o(1))W\)
uniformly for \(q\le H\), and

\[
 A_H-W
 =\sum_{1\le s\le\lfloor H/2\rfloor}N_{2s}
 =(\lfloor H/2\rfloor+o(H))W.                                \tag{4.2}
\]

For \(H\ge c\sqrt m\), summing (4.1) over
\(1\le2s\le c\sqrt m\) gives \(A_H-W=\Omega(\sqrt mW)\).
The standard Gaussian upper estimate for binomial coefficients gives
\(A_H=O(\sqrt mW)\) for every \(H\le m\).  Together with the trivial
upper bound \(A_H-W\le(H/2)W\), this proves

\[
                         A_H-W
 =\Theta\!\left(W\min\{H,\sqrt m\}\right)                    \tag{4.3}
\]

for growing \(H\) (and with the evident constant-scale interpretation for
fixed \(H\ge2\)).

In the Johnson-adjacent branch, (3.9) and (4.2) show that the fraction of
cancelled physical tokens is

\[
 {2R\over2A_H}=1-{W\over A_H}
 =1-{1+o(1)\over\lfloor H/2\rfloor+1}.                        \tag{4.4}
\]

It tends to one whenever \(H\to\infty\) with \(H=o(\sqrt m)\), and the
same conclusion follows from (4.3) once \(H\gtrsim\sqrt m\).

## 5. Consequence for the coefficient-one OR interface

A coefficient-one middle-owner word has \(W+o(W)\) slots.  The canonical
parity contraction of a full-band tight enumeration has \(A_H\) physical
two-flip slots.  Equation (3.6) is the exact cost of reducing those slots
to the \(W\) inherited rank-\(m\) gaps:

\[
 \underbrace{A_H-W}_{\text{all lower even-rank vertices}}
 =
 \underbrace{D}_{\text{nonadjacent-owner/geodesic-subdivision cost}}
 +
 \underbrace{R}_{\text{cancelled-return chronology}}.         \tag{5.1}
\]

Thus tightness cannot force either of the two properties needed to obtain
the compiler for free:

* if \(D\) is small, then \(R\) is large and the physical band chronology
  is mostly erased on contraction;
* if \(R\) is small, then \(D\) is large and the inherited rank-\(m\)
  order is far from a Johnson owner cycle.

This is a statewise identity, not an entropy heuristic and not a defect of
the published construction.  It applies to every full-band tight
enumeration.  A positive use of the central-levels literature must
therefore add a genuinely new synchronization theorem which reassigns
lower-band vertices across top gaps, rather than merely contracting the
published tight tour.

The two-level case \(H=1\) is exceptional: \(A_1=W\), so (5.1) vanishes.
This is exactly why the tight two-level enumeration contracts perfectly to
the one-sided depth-one Hamilton Johnson cycle, while the wider-band
analogue does not.
