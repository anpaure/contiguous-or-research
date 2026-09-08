# Iterating the lexicographic lower factor

## 1. Outcome

Put

\[
 P_m=[0,m]^4,\qquad L_j=\{x\in P_m:|x|=j\},\qquad
 M_m=|L_{2m}|.
\]

The regular line-fibre algebra inside the edge-minimum construction in
`LEX_THREE_LAYER_FACTOR.md` really does iterate.  Repeated coordinatewise
intersection is an exact sliding erosion on those lines.  The literal
erosion has a precisely computable boundary deficit.  Completing and
reordering the eroded fibres, and using lower-dimensional slice fans for
the remaining upper witnesses, gives the following theorem.  Thus the
global word below is a surface-completed deformation of the lex trail word,
not literally its unchanged global trail order.

### Theorem 1 (growing lower-central band)

Let \(0\le q\le m-2\), and put

\[
                         R=2m-q-2.                 \tag{1.1}
\]

There is an explicit nonzero word whose contiguous coordinatewise maxima
contain every point of

\[
                         L_R\cup L_{R+1}\cup\cdots\cup L_{2m}             \tag{1.2}
\]

and whose length is at most

\[
 |L_R|+2(q+2)(m+1)(2m+1)
 \le M_m+2(q+2)(m+1)(2m+1).                       \tag{1.3}
\]

Consequently, for every integer function \(q=q(m)=o(m)\), a growing band
of \(q+3\) lower-central layers has a word of length

\[
                              M_m+o(m^3).           \tag{1.4}
\]

All witnesses in the main spine are given by an exact formula.  The only
auxiliary blocks are explicit three-box slice words.  Thus this is a
one-dimensional factor construction, not merely a statement that the
required shadows exist.

The same calculation is not intrinsically one-sided.  A useful stronger
corollary is recorded after the proof: one word of length
\(M_m+O(qm^2)\) covers the symmetric band
\(L_{2m-q},\ldots,L_{2m+q}\).  Thus both sides of every sublinear central
band fit on one spine; there is no factor-two concatenation loss.

The theorem does not cover a linear-depth band with a lower-order error:
the displayed construction pays \(\Theta(qm^2)\) for its slice fan.  That
is a limitation of this architecture, not a lower bound for arbitrary
words.

## 2. The regular lexicographic core

For \(z\in L_{2m}\), the lexicographic selected-cover edge uses the first
two positive coordinates \(p<q\), and its minimum is

\[
                         b_z=z-e_p-e_q.             \tag{2.1}
\]

Call \(z\) regular when \(z_1,z_2>0\).  Then \(p=1,q=2\), so

\[
 b_z=z-e_1-e_2.
\]

For fixed \((c,d)=(z_3,z_4)\), the regular minima, ordered by increasing
first coordinate, form a consecutive coordinate line

\[
 \beta_t=(t,K-t,c,d),                              \tag{2.2}
\]

with both varying coordinates in \([0,m-1]\).  Conversely every point of

\[
 C_0=\{x\in L_{2m-2}:x_1<m,\ x_2<m\}              \tag{2.3}
\]

is the regular minimum of the unique colour \(x+e_1+e_2\).  Thus the
bulk of the lex edge-minimum word is exactly a family of complete truncated
lines.  The nonregular colours and line ends form only a surface-order
set.

## 3. Exact repeated erosion

On one regular line define its \(q\)-fold sliding erosion by

\[
 \gamma_t^{(q)}=\bigwedge_{h=0}^{q}\beta_{t+h},    \tag{3.1}
\]

whenever all the displayed terms exist.  Since one varying coordinate
increases and the other decreases,

\[
 \gamma_t^{(q)}=(t,K-t-q,c,d).                     \tag{3.2}
\]

In particular every eroded letter has rank \(2m-q-2\).  More generally,
for every valid \(s\ge0\),

\[
 \bigvee_{h=0}^{s}\gamma_{t+h}^{(q)}
       =(t+s,K-t-q,c,d).                           \tag{3.3}
\]

Equation (3.3) is the desired exact factor equation.  In particular, away
from the line ends,

\[
 \beta_t=\bigvee_{h=0}^{q}\gamma_{t-q+h}^{(q)},   \tag{3.4}
\]

and windows of another one or two letters recover the next two upper
layers.

### Lemma 2 (exact erosion image)

The singleton image of the regular \(q\)-fold erosion is

\[
 C_q=\{x\in L_{2m-q-2}:x_1\le m-q-1,\ x_2\le m-q-1\}.                 \tag{3.5}
\]

Hence the number of missing points in its bottom layer is exactly

\[
 D_q=
 2\sum_{j=0}^{q}\binom{m-q+j}{2}
 -\sum_{i=0}^{q}\sum_{j=0}^{q}(i+j-q-1)_+,         \tag{3.6}
\]

where \((a)_+=\max(a,0)\).  In fact this simplifies exactly to

\[
 D_q=(q+1)m^2-(q+1)^2m+\frac{q(q+1)(q+5)}6.         \tag{3.7}
\]

Consequently, uniformly for \(q=o(m)\),

\[
 D_q=(q+1)m^2+O\bigl((q+1)^2m+(q+1)^3\bigr).       \tag{3.8}
\]

### Proof

If (3.1) exists, both \(\beta_t\) and \(\beta_{t+q}\) have their first
two coordinates at most \(m-1\).  Formula (3.2) therefore has its first
two coordinates at most \(m-q-1\).

Conversely, given \(x\) on the right of (3.5), the points

\[
 (x_1+h,x_2+q-h,x_3,x_4),\qquad 0\le h\le q,
\]

form a legal regular line segment, and their coordinatewise minimum is
\(x\).  This proves (3.5).

A missing point has \(x_1\in\{m-q,\ldots,m\}\) or the analogous condition
on \(x_2\).  If \(x_1=m-q+j\), the other three coordinates sum to
\(m-2-j\), and the number of choices is \(\binom{m-j}{2}\).  Reversing
the index gives the first sum in (3.6).  If
\(x_1=m-i,x_2=m-j\), the last two coordinates sum to
\(i+j-q-2\), giving \((i+j-q-1)_+\) choices.  Inclusion-exclusion proves
(3.6).  The overlap sum equals \(\binom{q+1}{3}\); expanding the first
sum then gives (3.7)--(3.8).  \(\square\)

The deficit (3.6) is a genuine obstruction to the *pure* erosion word.
All its letters have the same rank \(2m-q-2\).  A maximum of such letters
can have that same rank only if every letter in the interval is the target
itself.  Therefore none of the \(D_q\) missing bottom points can occur as
an interval maximum in a word using only the letters of \(C_q\).

This is the sharp scoped no-go: literal repeated erosion must be completed
at the boundary.  It is not a no-go for variable-band or fan constructions.

## 4. Surface completion to a full line spine

The clean repair is not to append the \(D_q\) points in arbitrary order.
Complete the eroded fibres to the entire layer \(L_R\), and order that
layer by complete coordinate-\(\{1,2\}\) lines.

For every \((c,d)\in[0,m]^2\), put

\[
 S=R-c-d,
 \quad A=\max(0,S-m),
 \quad B=\min(m,S).                                \tag{4.1}
\]

When \(A\le B\), make the block

\[
 (A,S-A,c,d),(A+1,S-A-1,c,d),\ldots,(B,S-B,c,d).  \tag{4.2}
\]

Concatenate the nonempty blocks in lexicographic order of \((c,d)\).  Call
the resulting word \(W_R\).  It contains every point of \(L_R\) exactly
once, so

\[
                              |W_R|=|L_R|\le M_m.   \tag{4.3}
\]

The inequality is unimodality of the rank numbers of \([0,m]^4\), whose
maximum is attained at rank \(2m\).  Thus completing all eroded fibres
does not cost anything above the central width.

### Lemma 3 (line witness equation)

Let \(y\in L_{R+s}\), \(s\ge0\).  If \(y_1,y_2\ge s\), then \(y\) is the
maximum of a contiguous interval in one block of \(W_R\).

### Proof

The two points

\[
                         u=y-se_1,\qquad v=y-se_2   \tag{4.4}
\]

belong to \(L_R\), have the same last two coordinates, and are the two
ends of a segment in (4.2).  That segment is

\[
 (y_1-s+h,y_2-h,y_3,y_4),\qquad 0\le h\le s.
\]

Its coordinatewise maximum is exactly \(y\).  \(\square\)

This is the surface-completed form of (3.3).  The erosion identities are
retained, while the bottom layer is now complete.

## 5. Slice-fan completion and proof of Theorem 1

We use the standard three-chain hook word: every copy of \([0,m]^3\) has
a nonzero coordinatewise-maximum universal word for its nonzero points of
length at most

\[
                         (m+1)(2m+1)-1.             \tag{5.1}
\]

After fixing one additional positive coordinate, retaining the local zero
target costs at most one extra position.  Thus every positive
fixed-coordinate slice of \(P_m\) has a word of length at most

\[
                         G_m=(m+1)(2m+1).           \tag{5.2}
\]

For the zero fixed-coordinate slice, the omitted local origin is the global
zero and is not required; all embedded letters remain nonzero.  Hence the
same upper bound \(G_m\) applies uniformly to every slice below.

Start with \(W_R\).  For every \(a=0,1,\ldots,q+1\), append a slice word
for \(x_1=a\) and another for \(x_2=a\).

Let \(y\in L_{R+s}\), where \(0\le s\le q+2\).  If
\(y_1,y_2\ge s\), Lemma 3 supplies a witness in \(W_R\).  Otherwise one
of these two coordinates, say \(y_i=a\), satisfies

\[
                         0\le a<s\le q+2,
\]

so the appended slice word for \(x_i=a\) supplies a witness.  This proves
coverage of (1.2).  The length is bounded by

\[
 |L_R|+2(q+2)G_m,
\]

which is (1.3).  Since \(M_m=\Theta(m^3)\), equation (1.4) follows for
\(q=o(m)\).  \(\square\)

### Corollary 4 (one-spine symmetric band)

Let \(0\le 2q\le m\).  There is an explicit word of length

\[
 |L_{2m-q}|+4q(m+1)(2m+1)
 \le M_m+4q(m+1)(2m+1)                            \tag{5.3}
\]

covering every layer

\[
                         L_{2m-q},L_{2m-q+1},\ldots,L_{2m+q}.            \tag{5.4}
\]

In particular, if \(q=o(m)\), the length in (5.3) is
\(M_m+o(m^3)\).

### Proof

Run exactly the construction above with base rank \(R=2m-q\) and maximum
excess \(2q\): list the complete rank-\(R\) coordinate-line spine and
append the slices \(x_1=a,x_2=a\) for \(0\le a<2q\).  Lemma 3 and the
same low-coordinate dichotomy cover (5.4).  There are \(4q\) slice blocks.
The base layer is no larger than the central layer.  \(\square\)

## 6. What this does and does not iterate

There are three distinct statements which should not be conflated.

1. **Algebraic iteration is exact.**  Equations (3.2)--(3.4) give an
   arbitrary-depth sliding factor on every regular lex line.

2. **The fixed lex core has a real boundary loss.**  Its bottom deficit is
   exactly (3.6), already \(\Theta(qm^2)\) for \(q=o(m)\).  Repeated
   erosion without fibre completion cannot cover the bottom layer.

3. **A surface-completed fan reaches every sublinear depth.**  The full
   line spine plus slice fan has overhead \(O(qm^2)\), and hence gives
   width plus lower order for every \(q=o(m)\).

The \(\Theta(qm^2)\) term becomes width-scale when \(q=\Theta(m)\).  The
source is structural: the construction treats \(\Theta(q)\) boundary
slices as independent three-dimensional words.  Merely changing the order
inside those slice blocks cannot remove that term.

The next plausible escape is a **multiscale fan fusion**.  Instead of
appending one complete three-box word for each value of a low coordinate,
one should interleave a whole slab

\[
 \{x:x_1< s\}\quad\text{or}\quad\{x:x_2<s\}
\]

with the central line spine, assigning its central antichain endpoints to
the positions lost when lower-rank fibres shorten.  Equivalently, one needs
cross-fibre transitions which carry valid erosion windows through most
line seams.  If a depth-\(q\) construction had only \(o(m^2/q)\) genuinely
broken seams, its erosion loss would be lower order even for much larger
\(q\).  The proved lex excursion obstruction shows that one fixed local
pairing cannot do every upper job, so such a fusion must use virtual seams,
several transition systems, or a hierarchical choice of coordinate pair.

This identifies the remaining big-picture problem precisely: the local
factor equations already iterate; what is missing is a global seam/fan
fusion which shares the boundary work instead of paying for every slice
separately.

## 7. Exact complementary-seam portal

There is a concrete reason to expect such a fusion.  Mixed-direction seams
carry two-dimensional, rather than one-dimensional, families of maxima.

Let a coordinate-\(\{1,2\}\) line be oriented as

\[
 A_t=(t,K_A-t,c,d),\qquad P\le t\le H,             \tag{7.1}
\]

and immediately follow it by a coordinate-\(\{3,4\}\) line

\[
 B_u=(a,b,u,K_B-u),\qquad L\le u\le Q.             \tag{7.2}
\]

For \(P\le p\le H\) and \(L\le r\le Q\), take the interval consisting of
the suffix \(A_p,\ldots,A_H\) and the prefix \(B_L,\ldots,B_r\).  Its
maximum is exactly

\[
 \bigl(\max(H,a),\ \max(K_A-p,b),\
              \max(c,r),\ \max(d,K_B-L)\bigr).    \tag{7.3}
\]

Consequently, throughout any subranges on which

\[
 a\le H,\quad b\le K_A-p,\quad c\le r,\quad d\le K_B-L,                \tag{7.4}
\]

the seam supplies the full Cartesian rectangle

\[
                         (H,K_A-p,r,K_B-L),         \tag{7.5}
\]

with \(p\) and \(r\) varying independently.

### Proof

The suffix maximum in (7.1) is

\[
                         (H,K_A-p,c,d),
\]

and the prefix maximum in (7.2) is

\[
                         (a,b,r,K_B-L).
\]

Their join is (7.3), and (7.4) removes the four maxima signs to give
(7.5).  Every such join is the maximum of the displayed physical interval
crossing the seam.  \(\square\)

A seam with \(q\) usable letters on each side can therefore expose
\(\Theta(q^2)\) distinct portal values.  There are \(\Theta(m^2)\)
transverse line fibres.  Thus a surface-scale alternating braid has raw
portal capacity \(\Theta(q^2m^2)\), the same order as the total number of
fixed-pair boundary exceptions across a depth-\(q\) band.  This does not
prove that the rectangles can be made disjoint or assigned all required
values, but it removes the counting objection.

The precise next conjecture is therefore a **complementary seam-rectangle
tiling**: split the rank spine into alternating \(\{1,2\}\)- and
\(\{3,4\}\)-segments so that their rectangles (7.5) cover the line-missed
boundary family, while the segment interiors retain the sliding factor
equations (3.3).  Proving this with bounded overlap would replace the
independent slice fan and is the most direct route from sublinear depth to
linear depth.
