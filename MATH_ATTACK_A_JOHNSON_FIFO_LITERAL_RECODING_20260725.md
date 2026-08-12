# Exact FIFO criterion and repair cost for Johnson-block recoding

Date: 2026-07-25

Method: pure mathematics only.

## 1. Exact tight-block criterion

Put (n=2m+1).  Let

\[
 C=(X_0,X_1,\ldots ,X_{n-1},X_n=X_0)
 \tag{1.1}
\]

be a directed closed walk in (J(n,m)), with every consecutive pair
distinct.  Define its departure and arrival labels by

\[
 X_i\setminus X_{i+1}=\{a_i\},\qquad
 X_{i+1}\setminus X_i=\{b_i\},
 \qquad i\in\mathbb Z_n .                         \tag{1.2}
\]

For a coordinate (x), put

\[
 d_C(x)=|\{i:x\in X_i\}|.                        \tag{1.3}
\]

### Theorem 1.1 -- FIFO/point-regularity equivalence

The following are equivalent.

1. There is a cyclic order (z_0,z_1,\ldots ,z_{n-1}) of ([n]) such
   that

   \[
   X_i=\{z_i,z_{i+1},\ldots ,z_{i+m-1}\}
   \qquad(i\in\mathbb Z_n).                      \tag{1.4}
   \]

2. The block is point-regular:

   \[
   d_C(x)=m\qquad(x\in[n]).                      \tag{1.5}
   \]

3. The departure word (a_0,a_1,\ldots ,a_{n-1}) is a permutation of
   ([n]), and the exact FIFO recurrence

   \[
   \boxed{b_i=a_{i+m}\qquad(i\in\mathbb Z_n)}    \tag{1.6}
   \]

   holds.

When these conditions hold, the cyclic order is uniquely reconstructed,
up to rotation, by

\[
 z_i=a_i.                                        \tag{1.7}
\]

#### Proof

Condition 1 immediately gives (a_i=z_i), (b_i=z_{i+m}), and every
coordinate belongs to exactly (m) of the windows.  Thus it implies both
2 and 3.

Assume 2.  In the cyclic membership word

\[
 (\mathbf1_{x\in X_i})_{i\in\mathbb Z_n}
\]

each coordinate has (m) ones and (m+1) zeroes.  It is therefore
nonconstant and has at least one (1\to0) transition.  Every Johnson edge
has exactly one departing coordinate, so the (n) edges supply exactly
(n) such transitions in total.  There are (n) coordinates.  Hence each
coordinate departs exactly once and, cyclically, enters exactly once.  Its
membership word is one run; by (1.5), that run has length (m).  If it
departs at edge (i), it entered at edge (i-m).  Therefore the departure
labels are a permutation and (b_{i-m}=a_i), which is (1.6).

Finally assume 3.  A coordinate (a_j) has its unique arrival at edge
(j-m) and its unique departure at edge (j).  Hence it belongs exactly
to the states

\[
 X_{j-m+1},X_{j-m+2},\ldots ,X_j.
\]

Consequently

\[
 X_i=\{a_i,a_{i+1},\ldots ,a_{i+m-1}\},
\]

which is (1.4) with (z_i=a_i).  This also proves uniqueness.  \(\square\)

Thus the first literal cut on an (n)-edge Johnson block is already the
singleton point condition (1.5).  Balanced first-shadow colours do not
imply it.

## 2. The quotient zero-voltage condition

Identify the coordinates with \(\mathbb Z_n\).  If only translation-orbit
representatives are retained, normalize every (m)-set to coordinate sum
zero.  A normalized odd-graph step has the form

\[
 A_{i+1}=T_{y_i}(A_i)
 =\bigl(\mathbb Z_n\setminus(A_i\cup\{y_i\})\bigr)-2y_i.
 \tag{2.1}
\]

Choose (s_0=0) and lift by

\[
 s_{i+1}=s_i+2y_i.                                \tag{2.2}
\]

### Proposition 2.1 -- exact voltage closure

Assume that the normalized quotient trajectory is closed, (A_n=A_0).
Then its lift closes if and only if

\[
 \boxed{\sum_{i=0}^{n-1}y_i=0\pmod n.}           \tag{2.3}
\]

After closure, every nonbacktracking length-(n) odd-graph cycle is a
wreath; after reindexing its middle vertices by every second position
(and, if necessary, reversing orientation),
its directed Johnson block obeys Theorem 1.1.  Hence (2.3) is the exact
additional condition when a packet is specified only in the translation
quotient.  For an already closed unquotiented block it is automatic.

#### Proof

Equation (2.2) gives

\[
 s_n-s_0=2\sum_i y_i.
\]

Because \(\gcd(m,n)=1\), no nonzero translation of \(\mathbb Z_n\) can
stabilize an (m)-set: every orbit of such a translation has a nontrivial
length dividing (n), whereas a union of those orbits would have cardinality
sharing that divisor with (n).  Thus, under (A_n=A_0), the lift closes
exactly when (s_n=s_0).  Since (2) is invertible modulo the odd integer
(n), this vanishes
exactly under (2.3).  The final assertion is the standard shortest-odd-cycle
description of (KG(2m+1,m)), followed by Theorem 1.1.  \(\square\)

## 3. Fixed-index edit lower bound

For a directed block (C), define

\[
 \Phi(C)=|\{i:b_i\ne a_{i+m}\}|,\qquad
 R(C)=n-|\{a_i:i\in\mathbb Z_n\}|,               \tag{3.1}
\]

and its point discrepancy

\[
 \Delta(C)=(d_C(x)-m)_{x\in[n]}.                 \tag{3.2}
\]

### Theorem 3.1 -- necessary number of vertex substitutions

Suppose (C) is changed into a tight (n)-vertex block by substituting
(r) vertex positions, while retaining the cyclic indexing of all
unsubstituted positions.  Then

\[
 \boxed{
 r\ge
 \max\left\{
  \|\Delta(C)\|_\infty,
  \left\lceil\frac{\|\Delta(C)\|_1}{2m}\right\rceil,
  \left\lceil\frac{R(C)}2\right\rceil,
  \left\lceil\frac{\Phi(C)}4\right\rceil
 \right\}.}                                      \tag{3.3}
\]

#### Proof

One vertex substitution changes the degree of any fixed coordinate by at
most one and changes the whole point-degree vector in \(\ell^1\) by at
most (2m).  The first two terms follow from the point-regularity required
by Theorem 1.1.

Changing (r) vertices changes at most (2r) directed Johnson edges.  To
make the departure word a permutation, at least

\[
 n-|\{a_i\}|=R(C)
\]

old departure occurrences must be changed, giving (2r\ge R(C)).
Finally, changing edge (j) can affect only the two FIFO equations indexed
by (j) and (j-m): it changes (b_j) in the first and (a_j) in the
second.  Thus (2r) changed edges can repair at most (4r) old FIFO
violations.  This proves the last term.  \(\square\)

For (B=W/n) independently prescribed blocks, repaired only by distinct
omitted owners, (3.3) must be summed over the blocks.  The saturating-cycle
reservoir has

\[
 d=W-N_1=\frac{2W}{m+2},\qquad
 \frac dB=\frac{2(2m+1)}{m+2}
 =4-\frac6{m+2}<4.                                \tag{3.4}
\]

Thus direct fixed-index recoding has fewer than four omitted-owner
substitutions per packet on average.  In particular, any block family whose
right side in (3.3) has average at least four cannot be repaired by this
reservoir.

## 4. Insertion-only completion of shortened core blocks

The natural use of the omitted owners may instead leave a shortened core
block (P) of (n-h) fixed middle vertices and add (h) omitted vertices
without removing or moving a core vertex.  Put

\[
 d_P(x)=|\{X\in P:x\in X\}|.
\]

### Proposition 4.1 -- exact first point cut

If (P) is contained in the vertex set of a wreath packet after adding
(h) middle vertices, then

\[
 \boxed{m-h\le d_P(x)\le m\qquad(x\in[n]).}       \tag{4.1}
\]

Consequently, if the (N_1=W-d) saturating-cycle vertices are divided into
(B=W/n) prescribed core blocks (P_j), and (h_j) omitted owners are
assigned to block (j), then necessarily

\[
 \max_x d_{P_j}(x)\le m,\qquad
 h_j\ge m-\min_x d_{P_j}(x),                     \tag{4.2}
\]

and hence

\[
 \boxed{
 \sum_{j=1}^{B}\bigl(m-\min_x d_{P_j}(x)\bigr)
 \le d.}                                         \tag{4.3}
\]

In particular, one core block with (d_P(x)>m) has an immediate singleton
point failure which insertions cannot repair.  If every block has
\(\min_x d_{P_j}(x)\le m-4\), then (4.3) fails because (4B>d).

#### Proof

Every completed wreath has point degree exactly (m).  The added (h)
sets can increase the degree of a coordinate by an integer between zero and
(h), and cannot decrease it.  This is exactly (4.1).  Equations
(4.2)--(4.3) follow by summing and using \(\sum_jh_j=d\).  \(\square\)

The inequalities are only the first point cuts.  Even when they hold, the
added vertices must belong to the actual omitted family, must provide
Johnson adjacencies, and must satisfy the FIFO recurrence (1.6).

## 5. Sharp scope and an explicit bad block

The point cut can fail by order (m), not merely by a floor unit.  For
(m\ge3), fix (x) and cyclically order the other (2m) coordinates as
(z_0,\ldots,z_{2m-1}).  Put

\[
 Y_i=\{x\}\cup\{z_i,z_{i+1},\ldots,z_{i+m-2}\}
 \qquad(i\in\mathbb Z_{2m}).                     \tag{5.1}
\]

The (Y_i)'s form a simple (2m)-cycle in (J(n,m)).  If

\[
 S=Y_0\cap Y_1,qquad Z=S\cup\{z_m\},             \tag{5.2}
\]

then (Z) is distinct from every (Y_i) and is adjacent to both (Y_0)
and (Y_1).  Subdividing (Y_0Y_1) through (Z) gives a simple directed
(n)-cycle all of whose vertices contain (x).  Its point discrepancy at
(x) is

\[
 d_C(x)-m=n-m=m+1.                                \tag{5.3}
\]

By Theorem 3.1, at least (m+1) vertex substitutions are needed before it
can be a wreath.  This proves that (O(1)) omitted owners per packet cannot
repair arbitrary Johnson-block defects.

This is not a no-go theorem for a specially chosen saturating cycle.  The
saturating-cycle theorem supplies no control of the blockwise quantities in
(3.1)--(3.2) or (4.2), but it also does not force them to be bad.  The exact
positive condition for direct recoding is therefore: choose the cuts and
omitted-owner allocation so that (4.1) holds, then satisfy the actual
adjacency completion and the FIFO/zero-voltage laws (1.6), (2.3).  Arbitrary
global rebundling of the middle vertices lies outside the edit and insertion
models proved here.
