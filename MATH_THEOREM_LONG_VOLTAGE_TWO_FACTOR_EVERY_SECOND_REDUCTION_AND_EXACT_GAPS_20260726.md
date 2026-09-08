# Long voltage two-factors: the every-second Johnson reduction and its exact gaps

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let

\[
                         p=2m+1
\]

be prime, let \(O_m=KG(p,m)\), and quotient by the coordinate translation
\(\rho:x\mapsto x+1\).  Write

\[
                         W=\binom pm,\qquad T=W/p.
\]

Relaxing quotient components from the special objects that lift to
shortest \(p\)-wreaths to arbitrary voltage cycles is mathematically
legitimate and does bypass the Catalan/two-loop obstruction.  It does not
by itself prove the band theorem.

The exact answers to the four proposed questions are:

1. **Every-second traversal: conditionally yes.**  A *simple-support*
   quotient two-factor lifts to a translation-invariant simple physical
   two-factor of \(O_m\).  Taking every second vertex on every lifted
   cycle gives a spanning Johnson two-factor.  A quotient two-factor of
   the projected **multigraph** need not have simple support: it may use
   two parallel copies of one edge orbit.  Those copies lift to the same
   physical edges twice, and every-second traversal backtracks.  Thus the
   bare \(2p\)-regular factorization argument is insufficient.
2. **Local omitted-label condition: yes for literal flags, no for band
   coverage.**  The every-second successor is \(H\)-safe exactly when
   every cyclic block of \(2H\) consecutive omitted labels is distinct.
   This gives literal lower and upper targets of the correct ranks.  It
   gives no global injectivity or covering estimate.  The canonical MSW
   factor is a decisive counterexample to the stronger implication: each
   wreath has a globally distinct omission permutation, yet its
   first-shadow hole count is at least
   \((1/16-o(1))W\).
3. **Few components: reduced but open under the safety and coverage
   constraints.**  There is an exact component formula.  Nonzero-voltage
   quotient cycles contribute only \(O(T)=o(W/H)\) Johnson components
   whenever \(H=o(p)\).  The precise remaining condition is that the
   number of zero-voltage quotient cycles, counted with a parity weight,
   is \(o(T/H)\).  \(H\)-safety alone forces their lengths to be at least
   \(2H\), yielding only \(O(W/H)\), not the required little-\(o\).
   Ordinary two-factorization controls neither voltage, omission
   distinctness, nor target holes.
4. **Catalan/two-loop obstruction: genuinely bypassed.**  A
   nonzero-voltage quotient cycle of any length \(\ell\) lifts to one
   translation-fixed physical cycle of length \(p\ell\).  Fixed physical
   components are therefore no longer restricted to the \(m\) AP loops,
   and their total number is no longer the Catalan number.  The congruence
   forcing two AP loops (or impossibility for odd \(m\)) has no analogue.
   In fact, when \(m\) is odd, the quotient graph has even degree
   \(m+1\) and hence already has spanning quotient two-factors.  Their
   safety and shadow profiles remain uncontrolled.

The relaxation therefore produces a useful exact reduction, not a proof:
find a simple-support quotient two-factor with local omission girth
beyond \(2H\), zero-voltage cycle count \(o(T/H)\), and aggregate
\(o(T)\) empty target necklaces over all protected depths and both signs.

## 1. Projecting an exact physical factor

Let \(F\) be any spanning simple two-factor of \(O_m\); the MSW wreath
factor is one example.  Let \(Q=O_m/\langle\rho\rangle\) be the voltage
quotient.  For an undirected quotient edge orbit \(e\), put

\[
             w_e=\bigl|E(F)\cap\pi^{-1}(e)\bigr|.
 \tag{1.1}
\]

Every physical edge orbit has \(p\) members, so

\[
                              0\le w_e\le p.
 \tag{1.2}
\]

Each quotient vertex represents \(p\) physical vertices, all of degree
two in \(F\).  Therefore, with loops counted twice,

\[
 \boxed{
                 \sum_{e\ni v}\operatorname{inc}_v(e)w_e=2p
                 \qquad(v\in V(Q)).}
 \tag{1.3}
\]

Thus the weighted projection \(Q_w\) is a \(2p\)-regular multigraph and
has a multigraph two-factorization.

### Proposition 1.1 (the parallel-copy gap)

A two-factor \(J\) selected from \(Q_w\) lifts to a spanning *simple*
physical two-factor if it uses at most one copy of every quotient voltage
edge orbit.  A factor which uses two parallel copies of one orbit does
not.

#### Proof

One quotient voltage edge represents its complete translation orbit of
\(p\) physical edges.  Selecting it once gives one incident physical
edge at the appropriate endpoint of every fibre.  Degree two at every
quotient vertex therefore lifts to degree two at every physical vertex.

Two parallel copies in \(Q_w\) came from two physical members of the same
translation orbit, but translating either selected copy regenerates the
same full orbit.  Hence their lifts coincide edge by edge and produce a
doubled physical edge.  This is not a simple subgraph of \(O_m\); its
two-step traversal returns immediately to the same owner.  \(\square\)

Consequently

\[
 \text{“\(Q_w\) is \(2p\)-regular”}
 \quad\not\Longrightarrow\quad
 \text{“one displayed factor has a usable lift”}
 \tag{1.4}
\]

without an additional simple-support factor theorem.  This is a gap in
the proposed proof, not a claim that such a factor never exists.

Away from the AP loop vertices, the prime quotient has at most one
voltage edge between two distinct necklace classes.  Thus a genuine
subgraph two-factor of the underlying quotient \(Q\), with a loop used at
most once, automatically passes Proposition 1.1.

### Corollary 1.2 (unconditional arbitrary-cycle factors for odd \(m\))

If \(m\) is odd, \(Q\) is \((m+1)\)-regular of even degree.  Hence \(Q\)
has a two-factorization, and every one of its two-factors lifts to a
translation-invariant spanning simple physical two-factor of \(O_m\).

#### Proof

Every finite even-regular multigraph decomposes into two-factors.
Nonloop quotient edges are unique-voltage edges; quotient loops are
single AP voltage loops and may themselves be components of a
two-factor.  Proposition 1.1 then applies.  \(\square\)

This already shows concretely that the odd-\(m\) Catalan obstruction was
an obstruction to a **wreath** factor, not to an invariant odd-graph
two-factor.

## 2. Every second odd edge is a Johnson edge

Let

\[
             C=(A_0,A_1,\ldots,A_{L-1})
 \tag{2.1}
\]

be a simple physical cycle of \(O_m\), with indices modulo \(L\).

### Lemma 2.1 (no triangles or quadrilaterals)

For \(m\ge2\), every simple cycle of \(O_m\) has length at least five.

#### Proof

Three pairwise disjoint \(m\)-sets would use \(3m>2m+1\) points, so there
is no triangle.  In a putative four-cycle \(A-B-C-D-A\), the distinct
sets \(B,D\) are both \(m\)-subsets of the complement of \(A\cup C\).
This forces
\[
 |A\cup C|\le m+1.
\]
Since \(A\ne C\), equality holds, and the complement has size exactly
\(m\).  It contains only one \(m\)-set, forcing \(B=D\), a
contradiction.  \(\square\)

### Theorem 2.2 (every-second Johnson factor)

For every \(i\), \(A_i\) and \(A_{i+2}\) are adjacent in \(J(p,m)\).
The graph

\[
                 E^{(2)}(C)=\{A_iA_{i+2}:i\in\mathbb Z_L\}
 \tag{2.2}
\]

is one Johnson cycle of length \(L\) when \(L\) is odd and two Johnson
cycles of length \(L/2\) when \(L\) is even.  Therefore every spanning
simple two-factor of \(O_m\) gives a spanning Johnson two-factor by
every-second traversal.

#### Proof

Both \(A_i\) and \(A_{i+2}\) are \(m\)-subsets of the
\((m+1)\)-element complement of \(A_{i+1}\).  Lemma 2.1 makes them
distinct, so their intersection has size \(m-1\), exactly Johnson
adjacency.  The permutation \(i\mapsto i+2\) has
\(\gcd(2,L)\) cycles, proving the rest.  \(\square\)

## 3. Voltage and the exact component formula

Let \(D\) be a quotient cycle of length \(\ell\) and total voltage
\(a\in\mathbb F_p\).  The standard voltage-lift calculation gives

* \(p\) physical cycles of length \(\ell\) if \(a=0\);
* one physical cycle of length \(p\ell\) if \(a\ne0\).

Because \(p\) is odd, Theorem 2.2 gives the following exact count.

### Theorem 3.1 (lifted Johnson component count)

If \(J\) is a simple-support quotient two-factor, the number of components
of its every-second Johnson lift is

\[
 \boxed{
 c_{\rm J}(J)=
 \sum_{D\in{\cal C}(J)}
 \gcd(2,\ell_D)
 \left(1+(p-1)\mathbf1_{\{a_D=0\}}\right).}
 \tag{3.1}
\]

In particular, for \(H=o(p)\),

\[
 c_{\rm J}(J)=o(W/H)
 \quad\Longleftrightarrow\quad
 \sum_{\substack{D\in{\cal C}(J)\\a_D=0}}
       \gcd(2,\ell_D)=o(T/H).
 \tag{3.2}
\]

#### Proof

Apply Theorem 2.2 to the lifted cycles listed above.  The contribution of
all nonzero-voltage quotient cycles is at most \(2T\), since the quotient
cycles are vertex-disjoint.  As
\[
 {2T\over W/H}={2H\over p}=o(1),
\]
only the zero-voltage term remains at the target scale.  \(\square\)

Thus long nonzero-voltage cycles are ideal for the component ledger.
Regularity alone, however, says nothing about which selected quotient
cycles have voltage zero.

## 4. Omitted labels and \(H\)-safety

For the physical odd edge \(A_iA_{i+1}\), let

\[
                         z_i
  =\mathbb F_p\setminus(A_i\cup A_{i+1})
 \tag{4.1}
\]

be its unique omitted coordinate.  (We identify the singleton with its
element.)

### Lemma 4.1 (two-step exchange)

\[
 \boxed{
                 A_{i+2}=A_i-\{z_{i+1}\}+\{z_i\}.}
 \tag{4.2}
\]

#### Proof

The complement of \(A_{i+1}\) is both
\(A_i\dot\cup\{z_i\}\) and
\(A_{i+2}\dot\cup\{z_{i+1}\}\).  The two-step walk does not backtrack, so
\(z_i\ne z_{i+1}\).  Rearranging gives (4.2).  \(\square\)

### Theorem 4.2 (exact omission-window criterion)

The every-second Johnson factor is safe through depth \(H\) from every
start if and only if every cyclic block

\[
                         z_i,z_{i+1},\ldots,z_{i+2H-1}
 \tag{4.3}
\]

has \(2H\) distinct entries.

Under this condition, for every \(q\le H\),

\[
\begin{aligned}
 A_{i+2q}
  &=A_i\setminus\{z_{i+1},z_{i+3},\ldots,z_{i+2q-1}\}\\
  &\qquad\cup\{z_i,z_{i+2},\ldots,z_{i+2q-2}\},
\end{aligned}
 \tag{4.4}
\]

and the lower meet and upper join of the \(q\)-step window are

\[
 L_{i,q}
   =A_i\setminus\{z_{i+1},z_{i+3},\ldots,z_{i+2q-1}\},
 \tag{4.5}
\]

\[
 U_{i,q}
   =A_i\cup\{z_i,z_{i+2},\ldots,z_{i+2q-2}\}.
 \tag{4.6}
\]

Hence \(|L_{i,q}|=m-q\) and \(|U_{i,q}|=m+q\).

#### Proof

Iterate (4.2).  If the displayed \(2q\) labels are distinct, every step
deletes a previously present original label and inserts a new label which
is never removed in the window.  This proves (4.4)--(4.6) and geodesicity.

Conversely a \(q\)-step Johnson geodesic changes \(q\) distinct old
coordinates into \(q\) distinct new coordinates, with the two sets
disjoint.  Lemma 4.1 identifies these coordinates with the odd- and
even-indexed labels in (4.3), proving their pairwise distinctness.
\(\square\)

Thus omitted-label distinctness supplies exactly the local literal
compiler condition.

### Proposition 4.3 (local safety does not imply band coverage)

Condition (4.3), even through the maximum possible scale in every
component, does not imply \(o(W)\) missing targets.

#### Proof

In every shortest \(p\)-cycle of \(O_m\), the omitted labels are a
permutation of all \(p\) coordinates.  Hence every wreath factor,
including the canonical MSW factor, satisfies (4.3) through
\(H=m\).

The proved canonical-MSW first-shadow theorem gives

\[
                 M_1(F_m^{\rm MSW})
                    \ge(1/16-o(1))W.
 \tag{4.7}
\]

Therefore even global omission distinctness along every component is
compatible with a linear target-hole set.  \(\square\)

The point is visible directly in (4.5): local distinctness controls the
rank of each \(L_{i,q}\), but it never compares
\(L_{i,q}\) and \(L_{j,q}\) at distant starts or on different cycles.

For a translation-invariant factor, target loads are constant on
translation necklaces.  Consequently physical holes at depth \(q\) are
\(p\) times the number of empty quotient target necklaces.  An eventual
positive theorem must impose

\[
 \sum_{q\le H}\left(h_q^-+h_q^+\right)=o(T),
 \tag{4.8}
\]

where \(h_q^\pm\) are the quotient hole counts.  A separate
\(o(T)\)-statement at every depth is not enough when \(H\) grows, and
neither form follows from (4.3).

## 5. What \(H\)-safety gives for zero-voltage cycles

### Proposition 5.1 (critical, but not little-\(o\), component bound)

If a zero-voltage quotient cycle \(D\) has an \(H\)-safe lift, then

\[
                             \ell_D\ge2H.
 \tag{5.1}
\]

Consequently an \(H\)-safe quotient two-factor has at most \(T/(2H)\)
zero-voltage cycles and its zero-voltage contribution to (3.1) is at most

\[
                             {W\over H}.
 \tag{5.2}
\]

#### Proof

A zero-voltage quotient cycle lifts to physical cycles with the same
cyclic omission word of length \(\ell_D\).  If \(\ell_D<2H\), a block of
\(2H\) consecutive positions repeats an omitted label, contradicting
Theorem 4.2.  Vertex-disjoint quotient cycles have total length at most
\(T\), proving the count.  Finally
\(\gcd(2,\ell_D)\le2\), so their Johnson component contribution is at
most
\[
                       2p\,{T\over2H}=W/H.
\]
\(\square\)

The bound is exactly at the forbidden boundary.  To obtain
\(o(W/H)\), one needs, for example,

* \(o(T/H)\) zero-voltage cycles;
* average zero-voltage cycle length \(\omega(H)\); or
* safety at a larger scale \(H'\) with \(H'/H\to\infty\).

No ordinary two-factorization theorem supplies any of these.

## 6. The Catalan/two-loop obstruction disappears

For a translation-invariant factor into shortest odd cycles, every
physical component has length \(p\).  Its quotient is therefore either

* a nonzero-voltage loop (an AP wreath), or
* one of \(p\) lifts of a zero-voltage quotient \(p\)-cycle.

Counting physical rows then fixes their number at \(T=C_m\), and the
congruence

\[
                         T\equiv2(-1)^m\pmod p
 \tag{6.1}
\]

forces exactly two AP loops for even \(m\) and gives impossibility for
odd \(m\).

For an arbitrary quotient two-factor, a nonzero-voltage cycle of length
\(\ell\) lifts to one translation-fixed physical cycle of length
\(p\ell\).  Such fixed cycles exist in as many quotient components and
lengths as the selected two-factor permits; they are not AP loops unless
\(\ell=1\).  Moreover the total number of physical cycles is

\[
 \sum_{D:a_D=0}p+
 \sum_{D:a_D\ne0}1,
 \tag{6.2}
\]

not the fixed Catalan number \(T\).  Therefore the congruence argument
has no input and the two-loop law vanishes.

This answers part (d) positively and exactly.  It does not control the
three statistics in Sections 3--5.

## 7. The corrected long-cycle target

The proposed route is valid after replacing “take any quotient
two-factorization” by the following theorem.

> **Long-cycle necklace successor theorem (open).**  For
> \(H/\sqrt m\to\infty\), \(H=o(p)\), choose a simple-support spanning
> two-factor \(J\) of the prime voltage quotient such that:
>
> 1. every lifted omission word is \(2H\)-locally distinct;
> 2. \(\sum_{D:a_D=0}\gcd(2,\ell_D)=o(T/H)\);
> 3. the aggregate number of empty target necklaces for the two
>    every-second maps (4.5)--(4.6) satisfies
>    \[
>       \sum_{q\le H}(h_q^-+h_q^+)=o(T).
>    \]

Its voltage lift and Theorems 2.2, 3.1, and 4.2 give an exact
translation-invariant \(H\)-safe Johnson factor with \(o(W/H)\)
components and \(o(W)\) signed target holes.  The already proved
factor-blind compilation and tail theorem would then apply.

What has been gained is real: no wreath-length constraint and no
Catalan/two-loop obstruction remain.  What has not been gained is the
essential balancing theorem.  The local omission condition solves
chronology, while Item 3 is still a global simultaneous necklace-cover
condition.
