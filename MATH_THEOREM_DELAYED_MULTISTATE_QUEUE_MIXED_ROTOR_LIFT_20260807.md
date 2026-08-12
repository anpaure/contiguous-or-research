# Delayed multistate queues give an owner-simple lift of every mixed rotor

**Date:** 2026-08-07  
**Method:** run a reduced variable-weight queue and read a longer owner
window; the old toggle occurrences form the terminal singleton rail  
**Status:** unconditional local theorem.  It repairs the exact mixed-rotor
gap left by the binary-toggle queue audit.  Every mixed monotone-rotor
vertex now has a literal simple Johnson owner cycle, simple local immediate
palettes, exact age profile, and two-sided owner residence.  Global
owner/target-once rounding, component fusion, upper coverage, and the
common compiler remain open.

## 1. Parameters

Fix full trace depth \(d\), owner rank \(R\), and a mixed-rotor split

\[
 1\le a<d,
 \qquad D=d-a,
 \qquad p=D+1=d-a+1.
\tag{1.1}
\]

Let

\[
 \mathbf h=(h_0,\ldots,h_{p-1}),\qquad h_i\ge1,
 \qquad H=\sum_i h_i\le R-a.
\tag{1.2}
\]

Choose an integer clock length \(L\) satisfying

\[
 \boxed{Lp\ge2(d+2).}
\tag{1.3}

Assume that the ambient ground set has at least

\[
 R-a+p(L-1)
\tag{1.4}

coordinates.  Choose disjoint sets

\[
 K,\quad P_i,\quad
 X_i=\{x_{i,0},\ldots,x_{i,L-1}\}\quad(0\le i<p)
\tag{1.5}

with

\[
 |K|=R-a-H,qquad |P_i|=h_i-1.
\tag{1.6}

The number of coordinates used is exactly

\[
 |K|+\sum_i(|P_i|+L)=R-a+p(L-1).
\]

Define a cyclic source word of period \(Lp\) by

\[
 \boxed{
 A_{up+i}=K\cup P_i\cup\{x_{i,u}\},
 \qquad u\in\mathbb Z_L,\quad 0\le i<p.}
\tag{1.7}

For an endpoint \(t\), write

\[
 Z_{t,j}=A_{t-j+1}\cup\cdots\cup A_t.
\tag{1.8}

## 2. Interval decoding

An interval of source positions meets phase \(i\) in consecutive clock
values.  The following elementary decoding fact will be used repeatedly.

### Lemma 2.1 (labelled interval decoding)

For every \(1\le j\le d+2\), the set \(Z_{t,j}\) determines both \(j\)
and \(t\pmod{Lp}\).  Consequently all displayed interval values are
pairwise distinct over all pairs \((t,j)\) with \(1\le j\le d+2\).

#### Proof

Condition (1.3) gives \(j<Lp\), so no toggle label can occur twice in the
same interval.

If \(j<p\), the active phase supports form a proper cyclic interval of
length \(j\), which recovers \(j\) and the endpoint phase.  The selected
toggle label in each active phase then recovers the clock value.

If \(j\ge p\), every \(P_i\) occurs and the intersections

\[
 Z_{t,j}\cap X_i
\]

are nonempty proper cyclic intervals in the fixed labelled cycle \(X_i\).
Their total cardinality is \(j\), so \(j\) is recovered.  The last label
of each oriented interval is the most recent clock value of that phase.
These last labels have the form \(u\) on the phases at or before the
endpoint cut and \(u-1\) on the phases after it.  If all phases have the
same last label, the endpoint is the final phase; otherwise the unique cut
between the two values recovers the endpoint phase.  In either case \(u\)
is recovered.  Hence \(t\pmod{Lp}\) is determined. \(\square\)

The orientation of each labelled toggle cycle is part of the component
data.  Thus a proper cyclic interval has a well-defined first and last
label; no reflection ambiguity is present.

## 3. Full owner and palette theorem

### Theorem 3.1 (delayed multistate queue)

The source word (1.7), read at full depth \(d\), has the following
properties.

1. Every \((d+1)\)-letter owner has rank exactly \(R\).
2. The \(Lp\) owners are distinct and form a simple Johnson cycle.
3. The lower and upper immediate owner palettes are the interval rows

   \[
   Q^-_t=Z_{t,d},\qquad Q^+_t=Z_{t+1,d+2},
   \tag{3.1}
   \]

   and are both simple.
4. Every toggle coordinate has an owner run of exactly \(d+1\) and an
   owner gap of exactly \(Lp-(d+1)\ge d+3\).  The coordinates in \(K\)
   and the \(P_i\)'s are permanent in the full owner row.  Hence the owner
   row is two-sided resident at depth \(d\).
5. At endpoint \(t=up+i\), the full age composition is

   \[
   \boxed{
   c(t)=
   (R-a-H+h_i,h_{i-1},\ldots,h_{i-D},
      \underbrace{1,\ldots,1}_{a\text{ times}}).}
   \tag{3.2}

6. The complete literal state regenerates after \(Lp\) positions.

#### Proof

A window of length \(d+1=p+a\) contains every phase at least once.  It
therefore contains \(K\), every \(P_i\), and exactly \(d+1\) distinct
toggle coordinates.  Its rank is

\[
 (R-a-H)+(H-p)+(d+1)=R.
\tag{3.3}

When the window advances, its outgoing and incoming source positions may
have different phases, but their \(K\) and \(P_i\) coordinates remain:
every phase still occurs in both windows.  Exactly one old toggle leaves
and one new toggle enters.  They are distinct by (1.3).  Consecutive
owners are therefore Johnson neighbours.  Lemma 2.1 at \(j=d+1\) proves
owner simplicity.

The overlap and union of two consecutive owner windows are respectively
the length-\(d\) and length-\((d+2)\) interval unions in (3.1).  Lemma 2.1
proves both palette rows simple.  It also gives their ranks \(R-1\) and
\(R+1\), either directly from the one-coordinate owner swap or from
(3.3).

A toggle label occurs in one source position per period.  It belongs to
exactly the next \(d+1\) full windows and then to none of the remaining
windows.  This proves Item 4.  Every \(P_i\) occurs at least once in every
window of length \(d+1\ge p\), and \(K\) occurs everywhere.

The most recent \(p\) source letters contain one occurrence of every
phase.  Their new coordinates have age classes

\[
 (R-a-H+h_i,h_{i-1},\ldots,h_{i-D}).
\]

The preceding \(a\) source letters repeat phase cores already seen in the
recent \(p\)-window, but each contributes its distinct old toggle label.
Those labels have ages \(D+1,\ldots,D+a=d\), one at every age.  This is
(3.2).  Periodicity of (1.7) proves regeneration. \(\square\)

## 4. Exact mixed-rotor lift

Fix a mixed vertex of the monotone rank polytope with

\[
 1\le a<d<b\le R-1.
\tag{4.1}

As in the monotone-rotor theorem, put

\[
 D=d-a,qquad B=b-a,qquad R'=R-a,
\tag{4.2}

and take a positive composition

\[
 h_0+\cdots+h_D=B+1=b-a+1.
\tag{4.3}

Then \(H=B+1\) and

\[
 R-a-H=R-b-1,
\]

which is exactly the permanent core in the reduced long rotor.

### Corollary 4.1 (owner-simple mixed rotor)

With the weights (4.3), equation (3.2) is exactly the mixed-rotor age type

\[
 (R-b-1+h_i,h_{i-1},\ldots,h_{i-D},1^a).
\tag{4.4}

As the endpoint phase advances, only the reduced positive composition is
rotated; the terminal \(1^a\) rail remains fixed.  Therefore uniform
averaging over positive compositions and endpoints gives the marked vector

\[
 \boxed{
 \frac{b-d}{b-a}v_a+
 \frac{d-a}{b-a}v_b,}
\tag{4.5}

exactly as in the monotone-rotor theorem, now on literal simple resident
Johnson owner cycles.

#### Proof

The age identity is Theorem 3.1.  A positive composition of \(B+1\) into
\(D+1\) parts is equivalent to choosing \(D\) of the \(B\) cut positions.
Thus every reduced rank is offered with probability
\(D/B=(d-a)/(b-a)\), while the final \(a\) ranks supplied by the terminal
singleton rail occur at every endpoint.  This is precisely (4.5).
\(\square\)

## 5. Combined consequence

The binary-toggle queue handles the zero, short, and ordinary long rotor
vertices.  Corollary 4.1 handles every mixed vertex.  Convexity therefore
gives the corrected strengthening:

### Theorem 5.1 (owner-simple monotone rotor theorem)

For every \(q\in\mathcal M_{R,d}\), and all sufficiently large ambient
dimensions with \(k-R\gg d\), choose for each delayed component the
minimal

\[
 L=\left\lceil\frac{2(d+2)}p\right\rceil.
\tag{5.1A}
\]

Then \(p(L-1)<2(d+2)\), so the component uses only \(R+O(d)\)
coordinates.  There is a convex combination of literal components having:

\[
 \boxed{
 \text{flat simple Johnson owners, simple local }q1\text{ palettes,
 two-sided owner residence, regeneration, and marked rank marginal }q.}
\tag{5.1}

For the optimal Ferrers residual vector, averaging the components over all
coordinate embeddings with total endpoint mass \(W=\binom kR\) gives the
same owner-correlated fractional loads stated in Corollary 3.3 of
`MATH_THEOREM_BINARY_TOGGLE_VARIABLE_WEIGHT_QUEUE_AND_ROTOR_LIFT_20260807.md`:
every owner has load one, and every rank-\(s\) lower target has load

\[
 1-\frac{b_s}{\binom ks}.
\tag{5.2}

The Ferrers boundary supplies the complement.

This is an exact fractional correlation theorem.  It does not perform the
integral owner/named-target rounding or component fusion.
