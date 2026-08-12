# Independent audit of the claimed common-phase \(Q_4\) block transposition

Date: 2026-07-26

Method: direct hand verification of every vertex, edge, phase, direction
word, and physical-strip condition.  No conclusion of the source note is
assumed.

Source audited:
`MATH_THEOREM_Q4_COMMON_PHASE_BLOCK_TRANSPOSITION_20260726.md`.

## 0. Verdict

The sixteen-vertex table contains a genuine and useful local braid, but the
main theorem in the source note is false as stated.

1. The displayed vertices are all distinct and exhaust \(Q_4\).
2. \(\mathcal F^0\) is a factor into two physical isometric \(C_8\)'s.
3. \(\mathcal F^1\) is a factor into two simple graph-theoretic \(8\)-cycles,
   and every listed rerouted edge is correct.
4. The common \(\mathbb Z_8\) colouring is correct for those graph cycles.
5. The two packet words are exactly

   \[
   AABBAABB\quad\hbox{and}\quad ABBAAABB.
   \]

6. However, the cycles of \(\mathcal F^1\) are **not isometric**.  Their
   direction word is

   \[
                         1432\,1234,                 \tag{0.1}
   \]

   not \(\sigma\sigma\).  Thus they are not physical \(C_8\)-strips under
   the exact interface used in this project.
7. No suspension obtained by inserting fresh split directions while
   preserving the displayed base-edge order can turn (0.1) into an
   isometric \(C_{2h}\).  Deleting the fresh symbols from a word
   \(\pi\pi\) always leaves a doubled word \(\tau\tau\), whereas (0.1) is
   not doubled.
8. A common phase colouring is only a coarse phase statement.  It does not
   identify the full entrance and exit collars.  The source note never
   writes the protected-depth ports and therefore does not prove their
   equality.
9. The quotient change is not a consecutive-phase adjacent transposition:
   on phases \(1,2,3\) it is

   \[
                         ABB\longmapsto BBA,          \tag{0.2}
   \]

   with the changed phases \(1\) and \(3\).  There is no common consecutive
   phase pair at which \(AB\) becomes \(BA\).

Consequently Theorem 1.1 is correct only after replacing “physical” by
“simple graph-theoretic”, Theorem 2.1 is correct as a coarse phase theorem,
and Corollary 3.1 and Theorem 4.1 do not follow.

There is a nearby repair.  Repeating the braid antipodally gives a second
factor with direction word

\[
                         1432\,1432.                  \tag{0.3}
\]

It is common-support, common-phase, and genuinely isometric, and it has a
standard physical suspension.  It proves a weaker nonzero block-holonomy
primitive.  It still does not literally prove the quoted adjacent-phase
transposition lemma or its full \(H\)-collar condition.

## 1. Exhaustion of \(Q_4\)

In hexadecimal notation, the first row of the source table is

\[
                         0,8,12,14,15,7,3,1,          \tag{1.1}
\]

and the second is

\[
                         5,13,9,11,10,2,6,4.          \tag{1.2}
\]

Their union is \(\{0,1,\ldots,15\}\).  Equivalently,

\[
                         b_j=a_j\mathbin\oplus0101   \tag{1.3}
\]

for every \(j\), and the two displayed lists are disjoint.  Hence the
owner-support claim at dimension four is exact.

## 2. Every displayed edge

For both original rows the successive differences, including the cyclic
seam, are

\[
                         1,2,3,4,1,2,3,4.             \tag{2.1}
\]

Explicitly, for the \(a\)-row,

\[
\begin{array}{c|cccccccc}
\text{edge}&a_0a_1&a_1a_2&a_2a_3&a_3a_4&
             a_4a_5&a_5a_6&a_6a_7&a_7a_0\\ \hline
\text{direction}&1&2&3&4&1&2&3&4,
\end{array}                                           \tag{2.2}
\]

and the \(b\)-row has the same table.

The four new joins in \(\mathcal F^1\) are

\[
\begin{array}{c|c|c}
\text{join}&\text{bit strings}&\text{direction}\\ \hline
a_1b_2&1000\leftrightarrow1001&4\\
b_1a_2&1101\leftrightarrow1100&4\\
b_3a_4&1011\leftrightarrow1111&2\\
a_3b_4&1110\leftrightarrow1010&2.
\end{array}                                           \tag{2.3}
\]

All other edges are inherited.  Therefore both new cycles have direction
word

\[
                         1,4,3,2,1,2,3,4.             \tag{2.4}
\]

Each uses eight distinct vertices, the two cycles are disjoint, and together
they exhaust the table.  Thus the graph-factor assertion is correct.

## 3. Common phase and packet words

Every displayed cycle, on both shores, takes one owner from columns
\(0,1,\ldots,7\) in that order.  Hence

\[
                         c(a_j)=c(b_j)=j\pmod8        \tag{3.1}
\]

increases by one along every successor, including the seam.  The common
\(\mathbb Z_8\) colouring is exact.

Colour directions \(1,2\) by \(A\) and \(3,4\) by \(B\).  Equations
(2.1) and (2.4) give

\[
\begin{array}{c|cccccccc}
\text{phase}&0&1&2&3&4&5&6&7\\ \hline
\mathcal F^0&A&A&B&B&A&A&B&B\\
\mathcal F^1&A&B&B&A&A&A&B&B.
\end{array}                                           \tag{3.2}
\]

Thus only phases \(1\) and \(3\) change packet colour.  The source note's
two words and its balanced colour census are correct.

But (3.2) is not the displayed adjacent-phase operation from Section 7 of
the zero-block-holonomy theorem.  Checking all eight cyclic adjacent pairs
shows that none changes from \(AB\) to \(BA\) while the other phases are
fixed.  The local quotient operation is the three-letter move (0.2), or,
equivalently, a swap of the entries at two nonconsecutive phases.

## 4. Failure of the physical-strip criterion

An isometric \(C_{2h}\) in \(Q_h\) has transition word

\[
                         \sigma\sigma                 \tag{4.1}
\]

for a permutation \(\sigma\) of the \(h\) directions.  Equivalently, the
two occurrences of every cube direction are antipodal.  In the physical
split-pair model this is the deletion/insertion identity

\[
                         b_t=a_{t+h}.                 \tag{4.2}
\]

For (2.4), the occurrence positions are

\[
\begin{array}{c|cccc}
\text{direction}&1&2&3&4\\ \hline
\text{positions}&0,4&3,5&2,6&1,7.
\end{array}                                           \tag{4.3}
\]

Directions \(2\) and \(4\) are not antipodal.  Thus (4.1)--(4.2) fail.

There is also a literal chord certificate.  In the first new cycle,

\[
 a_7=0001\to a_0=0000\to a_1=1000\to b_2=1001       \tag{4.4}
\]

is a three-edge cycle arc, but its endpoints \(a_7,b_2\) differ only in
coordinate \(1\).  They are adjacent in \(Q_4\).  The cycle distance is
therefore three while the ambient cube distance is one.  The second new
cycle has the analogous chord \(b_7a_2\).

Hence \(\mathcal F^1\) is not an isometric factor.  This is not a semantic
qualification: isometry is the condition which makes every protected
window a literal consecutive-deletion strip.

## 5. The claimed suspension cannot repair this word

Put \(s=h-4\).  The natural colour-fibre suspension, with all new split
directions inserted between the two four-edge passages, gives the old-shore
word

\[
 1234,e_1,\ldots,e_s,1234,e_1,\ldots,e_s,             \tag{5.1}
\]

which is isometric.  On the new shore it gives

\[
 1432,e_1,\ldots,e_s,1234,e_1,\ldots,e_s.             \tag{5.2}
\]

The two halves of (5.2) disagree.

More generally, suppose a suspended isometric cycle retains the eight base
edges in their displayed cyclic order.  Its direction word is \(\pi\pi\).
Delete every fresh direction from the first copy of \(\pi\), obtaining
\(\tau\); deleting the fresh directions from the second copy gives the
same \(\tau\).  The projected old-direction word must therefore be
\(\tau\tau\).  But (2.4) is not of this form: at antipodal positions
\(1,5\) it has \(4,2\).

Thus no insertion-only, projection-preserving suspension of the displayed
\(\mathcal F^1\) can be a physical isometric \(C_{2h}\).  A common colour
can make the two lifted *owner unions* agree and can produce simple lifted
graph cycles; it cannot change this direction-order invariant.

The source note does not give a different exterior-moving suspension, and
so Theorem 4.1 is unproved and, for the stated standard suspension, false.

## 6. Common phase is not a full port collar

The project interface for a forward protected-depth \(H\)-germ with
deletion word \(d_t\) is

\[
\begin{aligned}
 L_t&=(d_t,d_{t+1},\ldots,d_{t+H-2};d_{t-1}),\\
 R_t&=(d_{t+1},d_{t+2},\ldots,d_{t+H-1};d_t).
\end{aligned}                                         \tag{6.1}
\]

At depth two the full local port also retains the owner pairs

\[
 (X_t,X_{t+1})\quad\hbox{and}\quad(X_{t+1},X_{t+2}). \tag{6.2}
\]

The common colouring (3.1) records only \(c(X_t)=t\).  For example, at the
common owner \(a_1\),

\[
\begin{array}{c|cc}
&\text{first successor}&\text{second successor}\\ \hline
\mathcal F^0&a_2&a_3\\
\mathcal F^1&b_2&b_3.
\end{array}                                           \tag{6.3}
\]

So both the outgoing physical direction and the full depth-two port differ.
That difference is the intended braid payload, but it proves that a common
phase is not itself a collar identity.

To use a bounded braid as a context substitute, one must specify cut ports,
show that the entrance and exit \(H\)-germs at those cuts agree with the
exterior carrier, include every window crossing either cut, and give the
lifted owner fibre at every collar state.  None of these data appears in the
source note.  The sentence “there is no phase collar” proves only equality
of coarse phase classes.

## 7. The antipodally doubled repair

There is a simple corrected second shore:

\[
\begin{aligned}
 \mathcal F^{1,*}={}&
 (a_0,a_1,b_2,b_3,a_4,a_5,b_6,b_7)\\
 &\mathbin{\dot\cup}
 (b_0,b_1,a_2,a_3,b_4,b_5,a_6,a_7).                  \tag{7.1}
\end{aligned}

The last four edge directions are now \(1,4,3,2\), just like the first
four.  For example,

\[
 a_4a_5:1,qquad a_5b_6:4,qquad b_6b_7:3,qquad
 b_7a_0:2,                                            \tag{7.2}
\]

and the other cycle has the same word.  Hence every cycle in (7.1) has

\[
                         1432\,1432,                  \tag{7.3}
\]

so it is isometric.  The cycles remain disjoint and exhaustive.  They still
take one owner from column \(j\) at phase \(j\), so (3.1) remains a common
phase colouring.

The packet word of (7.1) is

\[
                         ABBAABBA.                    \tag{7.4}
\]

Thus the changes at phases \(1,3\) are necessarily repeated at their
antipodes \(5,7\).  This is the exact correction forced by physical
isometry.

The standard suspension is now legitimate: use direction words

\[
\begin{aligned}
 &1234,e_1,\ldots,e_s,1234,e_1,\ldots,e_s,\\
 &1432,e_1,\ldots,e_s,1432,e_1,\ldots,e_s.
\end{aligned}                                         \tag{7.5}
\]

Both are \(\pi\pi\).  The common base colouring makes the colour-dependent
tail fibres agree, exactly as in the audited coloured-square suspension.
Thus (7.1)--(7.5) give a genuine common-support, common-phase physical
all-length braid.

What this repaired braid proves is

\[
 \boxed{\text{nonzero packet-order holonomy is compatible with physical
 isometry.}}                                          \tag{7.6}
\]

It does not yet prove the quoted ported adjacent-block lemma:

* its quotient move is \(ABB\mapsto BBA\), not a consecutive
  \(AB\mapsto BA\);
* the move occurs in antipodal pairs, as every physical move must;
* no designated entrance/exit cuts or full \(H\)-crossing collars have been
  supplied.

If the intended lemma only asks for any nonconstant block-order projection
of two closed common-support physical factors, then the repaired shore
(7.1), not the source shore (1.4), proves that weaker statement.

## 8. Exact remaining lemma

To obtain the literal primitive quoted in the zero-block-holonomy theorem,
one still needs a **ported antipodal transposition gadget** with all of the
following data:

1. two common-support factors into isometric \(C_{2h}\)'s;
2. one common lifted phase map;
3. a consecutive quotient swap \(AB\leftrightarrow BA\) in one half and
   its forced antipodal copy in the other half;
4. designated entrance and exit cuts whose complete \(H\)-owner/deletion
   collars agree with the exterior carrier;
5. an exact ownership ledger for every state and every window crossing the
   two cuts.

The source file proves items 1--2 only after replacing its new shore by
(7.1), proves a weaker nonconsecutive version of item 3, and does not address
items 4--5.  Therefore it does not close the ported adjacent-block
transposition gate as stated.
