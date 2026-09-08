# Aligned clean lag-two losses admit a linear paired backup rail

**Date:** 2026-08-07  
**Method:** exact interval-deck algebra; no computation or search  
**Status:** unconditional local/bank theorem for \(d\ge3\).  It determines
the complete ordinary-to-fragmented loss deck of the fixed-core clean
lag-two collar and shows that a bank of \(p\) such collars can be aligned so
that every lost value has a literal backup occurrence in one ordinary
fixed-core rail of length

\[
 d+1+2p+(p\bmod2).
\]

The construction costs no additional word positions if that rail is
embedded in the ambient chronology.  What is not proved here is a single
Hamilton or protected-factor extension containing both the clean packet
bank and the backup rail.

## 1. One collar: the complete lost deck

Use the fixed-core data

\[
 G=Q\mathbin{\dot\cup}C_0\mathbin{\dot\cup}\{a_0\},
 \qquad |C_0|=d-1,
\]

and let the ordinary toggle substring be

\[
 b^-,u,a_1,\ldots,a_{d-1},z,b,v.                 \tag{1.1}
\]

Before fragmentation the source letter at toggle \(x\) is \(G+x\).  The
clean fragmented collar replaces (1.1) by

\[
 C_0+b^-,\ \{u\},\ Q+a_0+a_1,\ldots,Q+a_0+a_{d-1},
 \ C_0+z,\ \{b\},\ \{v\}.                       \tag{1.2}
\]

All toggles are distinct and outside \(G\).  For a toggle interval \(I\),
write \(G+I\) for \(G\) union its toggle set.

### Theorem 1.1 (exact loss classification)

For \(d\ge3\), the ordinary interval values absent after fragmentation are
exactly

\[
 \begin{aligned}
 \mathcal D(G)= {}&
 \{G+I:\varnothing\ne I\text{ is an interval of }
                  (u,a_1,\ldots,a_{d-1})\}\\
 &\mathbin{\dot\cup}\{G+b^-,\ G+b^-+u\}\\
 &\mathbin{\dot\cup}
 \{G+I:\varnothing\ne I\text{ is an interval of }(z,b,v)\}.
                                                               \tag{1.3}
 \end{aligned}
\]

In particular,

\[
 |\mathcal D(G)|=\binom{d+1}{2}+8.               \tag{1.4}
\]

#### Proof

An interval meeting an ordinary position contains all of \(G\), but also
contains the distinct toggle at that position.  It therefore cannot equal
an old value whose toggle set is wholly contained in (1.1).  Thus only
wholly exceptional intervals need be compared.

Inside (1.2), the \(Q+a_0\) part of \(G\) is supplied exactly at positions
\(a_1,\ldots,a_{d-1}\), while the \(C_0\) part is supplied exactly at
positions \(b^-\) and \(z\).  Hence a wholly exceptional interval retains
its old value if and only if it meets both sets of positions.  It is lost
if and only if it misses all \(a_i\)-positions or misses both
\(C_0\)-positions.

The intervals missing the \(a_i\)-bank lie in one of the two blocks

\[
 (b^-,u),\qquad (z,b,v).
\]

The intervals missing both \(C_0\)-positions lie in

\[
 (u,a_1,\ldots,a_{d-1}),\qquad (b,v).
\]

The second block is already contained in the interval family of
\((z,b,v)\), and the singleton \(u\) is already contained in the first
long block.  Removing these duplications gives (1.3).  All remaining
values are distinct because their noncore toggle sets are distinct.
The three summands have sizes

\[
 \binom{d+1}{2},\qquad 2,\qquad 6,
\]

which proves (1.4). \(\square\)

### Remark 1.2

The earlier disappearing values \(G+a_i\) are only \(d-1\) members of
the much larger first family in (1.3).  Thus a backup argument that repairs
only the one-letter cells is insufficient.

## 2. A resource-disjoint aligned packet bank

Put

\[
 A_1=\{a_1,\ldots,a_{d-1}\},\qquad H=G\cup A_1.
\]

Fix common labels \(b^-,u\), and choose pairwise disjoint labels

\[
 z_1,\ldots,z_p
\]

and, for \(1\le t\le\lceil p/2\rceil\), endpoint pairs

\[
 \{b_t,v_t\}.
\]

All these labels are outside \(G\cup A_1\) and are mutually distinct.
For packet \(2t-1\), use tail orientation

\[
 (z_{2t-1},b_t,v_t),                              \tag{2.1}
\]

and, when packet \(2t\) exists, use the relabelled reverse orientation

\[
 (z_{2t},v_t,b_t).                                \tag{2.2}
\]

For each packet choose a distinct \((d-1)\)-subset
\(C_{0,j}\subset G\), choose \(a_{0,j}\in G\setminus C_{0,j}\), and put

\[
 Q_j=G\setminus(C_{0,j}\cup\{a_{0,j}\}).
\]

This changes the saturated flag bottom

\[
 M_j=(G\setminus C_{0,j})\cup A_1                 \tag{2.3}
\]

without changing the owner core \(H\).

### Lemma 2.1 (packet-resource separation)

If

\[
 \binom{|G|}{d-1}\ge p,                           \tag{2.4}
\]

then the \(p\) flag bottoms in (2.3) are distinct, and all owner,
immediate-lower, and immediate-upper vertices of the \(p\) three-owner
packet paths are pairwise distinct.

#### Proof

Distinct \(C_{0,j}\)'s give distinct complements \(G\setminus C_{0,j}\)
and hence distinct \(M_j\)'s.  The three owners of packet \(j\) are

\[
 H+z_j+u+b^-,\qquad H+z_j+u+y_j,\qquad
 H+z_j+y_j+w_j,                                   \tag{2.5}
\]

where \((y_j,w_j)=(b_t,v_t)\) in (2.1) and
\((y_j,w_j)=(v_t,b_t)\) in (2.2).  Its lower colours are

\[
 H+z_j+u,\qquad H+z_j+y_j,                        \tag{2.6}
\]

and its upper colours are

\[
 H+z_j+u+b^-+y_j,\qquad H+z_j+u+y_j+w_j.          \tag{2.7}
\]

Every set in (2.5)--(2.7) contains the private label \(z_j\).  Since no
\(z_j\) is an endpoint label of another packet, equality across packets
would force the same \(z_j\).  Within one packet, the displayed fresh
labels distinguish all vertices of the same rank. \(\square\)

## 3. Paired-tail backup compression

Form the toggle word

\[
 \mathcal R_0=(b^-,u,a_1,\ldots,a_{d-1})\ \cdot\
 \prod_{t=1}^{\lfloor p/2\rfloor}
 (z_{2t-1},b_t,v_t,z_{2t})                        \tag{3.1}
\]

and, if \(p\) is odd, append

\[
 (z_p,b_{(p+1)/2},v_{(p+1)/2}).                   \tag{3.2}
\]

At every position of this word use the ordinary source letter \(G+x\).

### Theorem 3.1 (one rail backs up the complete aligned loss bank)

Every old value deleted by any of the \(p\) fragmented packets has a
literal interval occurrence in the ordinary rail (3.1)--(3.2).  The rail
length is

\[
 R_0=d+1+2p+(p\bmod2).                            \tag{3.3}
\]

#### Proof

The common prefix of (3.1) contains the whole interval deck of
\((u,a_1,\ldots,a_{d-1})\), as well as the intervals \((b^-)\) and
\((b^-,u)\).  It therefore backs up the first two lines of (1.3) for
every packet.

For a complete pair, the first three entries of

\[
 (z_{2t-1},b_t,v_t,z_{2t})
\]

carry the tail deck of packet \(2t-1\).  The last three entries have
order \((b_t,v_t,z_{2t})\), whose set-valued interval family equals that
of the reversed word \((z_{2t},v_t,b_t)\); they therefore carry the tail
deck of packet \(2t\).  The final three-entry block handles an unpaired
packet.  This proves coverage.  The length calculation is immediate:

\[
 (d+1)+4\lfloor p/2\rfloor+3(p\bmod2)
 =d+1+2p+(p\bmod2). \quad\square
\]

### Corollary 3.2 (ordinary resident backup cycle)

Let \(L=d+2\).  If

\[
 \max\{R_0,2L\}\le m+d+3=|[2m+1]\setminus G|,    \tag{3.4}
\]

extend \(\mathcal R_0\) with fresh toggles to a cyclic word of some length
\(R\) satisfying

\[
 \max\{R_0,2L\}\le R\le m+d+3.
\]

The ordinary letters \(G+x\) then have a simple rank-\(m\) Johnson owner
cycle, native simple immediate palettes, and two-sided owner residence
\(L\).  The cycle contains every backup occurrence from Theorem 3.1.

#### Proof

Every length-\(L\) owner value is \(G\) plus its \(L\) consecutive
distinct toggles.  Sliding changes one toggle, distinct proper cyclic
intervals give distinct sets, and each toggle has one owner run of length
\(L\) and a gap of length \(R-L\ge L\). \(\square\)

## 4. Asymptotic size and the exact remaining embedding gate

In the positive Ferrers-residue range,

\[
 p\le\binom{d+1}{2},\qquad \frac{d^2}{m}\longrightarrow\frac\pi4.
\]

Hence

\[
 \frac{R_0}{m}\le\frac{d+1+d(d+1)+1}{m}
 =\frac\pi4+o(1)<1.                               \tag{4.1}
\]

So the C4--spectral protected-factor theorem embeds the backup owner
cycle by itself for all sufficiently large \(m\).  The clean packet bank
also embeds by itself: it has protected parameter \(2p\), again at most
\((\pi/4+o(1))m\).

The theorem does **not** permit adding these two protected systems.  Their
combined sufficient parameter is

\[
 R+2p\le4p+o(m),                                  \tag{4.2}
\]

which can approach

\[
 \left(\frac\pi2+o(1)\right)m>m.
\]

Thus the present spectral extension theorem is quantitatively too weak
for the union, even though both pieces separately lie below its sharp
linear threshold.  Closing the B+2 backup route requires one of:

1. a joint host theorem exploiting the correlation between the packet
   paths and the backup rail;
2. a Hamilton-first theorem that finds all clean packet turns while
   retaining a prescribed \(O(m)\) backup rail; or
3. a smaller backup architecture whose additional protected parameter is
   \(o(m)\).

This is a topology/host obstruction, not a Ferrers-capacity obstruction.

## 5. Comparison with the monotone-pivot B+1 route

The monotone-pivot insertion is exactly compiler-functorial: every old
interval OR survives, the disappearing maximal-band cells have middle
rank and carry no strict-lower compiler assignments, and the new singleton
plus two rays compile locally with zero residual deficiency.  It therefore
needs no analogue of the backup rail above.

Its remaining global hypothesis is stronger at the owner layer: one must
construct an upper-exact, resident, rank-saturated Catalan Hamilton host
containing the protected pivot collar (and preserve deeper upper witnesses).

The clean B+2 route has the easier proved local owner factor, but the
fragmentation is not compiler-functorial and now needs the joint host in
Section 4.  Consequently neither route presently implies the other.
After arbitrary Ferrers deletion was proved, the B+1 route has fewer
remaining lower/compiler gates, while the B+2 route has the more developed
immediate-owner factor theorem.

The shortest honest frontier is therefore:

\[
 \boxed{\text{B+1: protected Catalan--pivot host}}
\]

versus

\[
 \boxed{\text{B+2: joint clean-packet + backup-rail host}}.
\]

