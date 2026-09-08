# Audit of the paired-window zipper: the phase/release inverse is not injective

Date: 2026-07-27

Method: adversarial hand mathematics only.  No computation, finite
search, solver, probabilistic black box, or web input is used.

Audited claims:

* Lemma 2.1 and Theorem 0.1 of
  MATH_THEOREM_DOMINO_TWIN_INVERSE_STABILITY_C_ONE_THIRD_20260727.md;
* the sharpened conflict-degree estimate (0.1') of
  MATH_THEOREM_MACRO_OVERLAP_QUARANTINE_BY_CONFLICT_THINNING_20260727.md.

## 0. Verdict

The asserted inverse

\[
 \{\text{cell intersections }J_i\}
 +\{\text{star/top phases}\}
 +\{\text{at most one released label per weak cell}\}
 \longmapsto
 \{\text{the second domino word}\}
\tag{0.1}
\]

is not valid.

At a two-target anchor realized in the top phase, the common edge fixes
the \((r+1)\)-domino carrier

\[
                         U=W_j\cup C_{j+r},
\tag{0.2}
\]

but it does not fix the endpoint domino \(C_{j+r}\).  There are
\(\Theta(n^2)\) possible endpoint two-sets.  The recurrence

\[
 W_{j+1}=(W_j\setminus C_j)\cup C_{j+r}
\tag{0.3}
\]

cannot be evaluated until that two-set is known.  Encountering
\(C_{j+r}\) at its paired front does not split it into two forced
labels: the same unknown unordered pair is encountered again.

There is a literal completed example already for

\[
                         m=6,\qquad r=2,\qquad R=5,
\tag{0.4}
\]

in which two different endpoint pairings have the same common edge,
the same carrier, the same top phase, the same orientation, and the
same finite endpoint state.  Thus the row

\[
 k=2\quad\Longrightarrow\quad 0\text{ released labels}
\tag{0.5}
\]

in the claimed decoding table is false.

More decisively, the globally aligned two-segment family gives a
counting contradiction to every inverse of the form (0.1).  For
\(h=m-2r=\Theta(\sqrt m)\) and
\(\ell=m/\sqrt{\log m}\), it has

\[
 \exp\bigl((4+o(1))m\sqrt{\log m}\bigr)
\tag{0.6}
\]

members at defect

\[
 s=(8+o(1))\frac{m}{\sqrt{\log m}}.
\tag{0.7}
\]

All records allowed by (0.1) number at most

\[
 \exp(O(m))n^{s/3}
 =\exp\bigl((8/3+o(1))m\sqrt{\log m}\bigr).
\tag{0.8}
\]

Hence two distinct packet supports have the same complete proposed
record.  This proves that the load-bearing uniqueness assertion fails,
not merely that its written local proof is incomplete.

Consequently the claimed uniform bound

\[
 \bigl|\{G:|F\setminus G|\le s\}\bigr|
 \le \exp(Cm)n^{s/3},\qquad s=o(m),
\tag{0.9}
\]

is false and must be retracted.  The crude
\(\exp(O(m))n^{3s}\) bound is unaffected.  A corrected static inverse
theorem based only on missing-target mass cannot have any fixed power
coefficient below \(1/2\).

## 1. What a top-phase edge actually determines

Let the second domino word be

\[
                         C_0,C_1,\ldots,C_{m-1},
 \qquad |C_j|=2,
\tag{1.1}
\]

and put

\[
                         W_j=C_j\cup\cdots\cup C_{j+r-1}.
\tag{1.2}
\]

The canonical top cell at position \(j\) is

\[
 {\cal T}_j
 =\left\{
 U_j\setminus\{z\}:z\in C_j\cup C_{j+r}
 \right\},
 \qquad
 U_j=W_j\cup C_{j+r}.
\tag{1.3}
\]

Suppose two of its targets are

\[
                         X=U_j\setminus\{v\},
 \qquad
                         Y=U_j\setminus\{u\}.
\tag{1.4}
\]

Then the observed common edge gives exactly

\[
                         U_j=X\cup Y,
 \qquad
                         \{u,v\}=U_j\setminus(X\cap Y).
\tag{1.5}
\]

It says only that \(u,v\) belong to the endpoint four-set

\[
                         C_j\cup C_{j+r}.
\tag{1.6}
\]

It does not say which endpoint domino contains them, nor does it
determine the other two endpoint labels.  Even when the endpoint state
records that \(\{u,v\}=C_j\), the other endpoint has the form

\[
                         C_{j+r}=\Lambda,
 \qquad
 \Lambda\in\binom{U_j\setminus\{u,v\}}2.
\tag{1.7}
\]

Thus (1.5), the top-phase bit, the orientation, and the shore state
leave

\[
                         \binom{2r}{2}=\Theta(n^2)
\tag{1.8}
\]

possible endpoint dominoes in the annular range \(r=\Theta(n)\).

This ambiguity is not removed by writing the two window recurrences

\[
 W_{j+1}=(W_j\setminus C_j)\cup C_{j+r},
\tag{1.9a}
\]

\[
 W_{j-r+1}=(W_{j-r}\setminus C_{j-r})\cup C_j.
\tag{1.9b}
\]

Equation (1.9a) contains the unknown two-set \(C_{j+r}\) itself.
At the paired occurrence that same two-set leaves another window.
No set difference in (1.9) selects one of its two members.  A domino
is the atom of both recurrences.

This is the exact algebraic error in the sentence that the other member
of a released domino is first encountered at the paired front.  The
paired front encounters both members together.  Unless an additional
target equation singles out one member, either the whole two-set must
be recorded, at cost \(\Theta(n^2)\), or two element releases must be
charged.

## 2. A completed six-domino counterexample

Take the fixed domino word

\[
\begin{aligned}
 B_0&=\{5,6\},&
 B_1&=\{1,2\},&
 B_2&=\{3,4\},\\
 B_3&=\{7,8\},&
 B_4&=\{9,10\},&
 B_5&=\{11,12\}.
\end{aligned}
\tag{2.1}
\]

Let

\[
 A=B_1\cup B_2=\{1,2,3,4\},
 \qquad
 E=\{5,7\},
\tag{2.2}
\]

and define the two fixed targets

\[
 X=A\cup\{5\},
 \qquad
 Y=A\cup\{7\}.
\tag{2.3}
\]

They are an edge in the fixed star cell with core \(A\).

Put

\[
 H_-=\{6,8\},\qquad H_+=\{9,10\},\qquad L=\{11,12\}.
\tag{2.4}
\]

For any \(\Lambda\in\binom A2\), let
\(D_\Lambda=A\setminus\Lambda\), which is also a two-set, and form the
completed second word

\[
 G_\Lambda=
 (H_-,E,D_\Lambda,\Lambda,H_+,L).
\tag{2.5}
\]

The three consecutive dominoes

\[
                         E,D_\Lambda,\Lambda
\tag{2.6}
\]

have the common union

\[
                         U=A\cup E.
\tag{2.7}
\]

Their top cell has endpoint dominoes \(E,\Lambda\), so it contains

\[
 U\setminus\{5\}=Y,
 \qquad
 U\setminus\{7\}=X.
\tag{2.8}
\]

Therefore every one of the six choices of \(\Lambda\) realizes the
same prescribed edge \(\{X,Y\}\), in the same carrier \(U\), in the
same top phase and the same oriented slot.

For example,

\[
\begin{aligned}
 G_{\{1,2\}}
 &=(\{6,8\},\{5,7\},\{3,4\},\{1,2\},\{9,10\},\{11,12\}),\\
 G_{\{1,3\}}
 &=(\{6,8\},\{5,7\},\{2,4\},\{1,3\},\{9,10\},\{11,12\}).
\end{aligned}
\tag{2.9}
\]

They have different top cells because the endpoint four-sets

\[
                         E\cup\{1,2\},
 \qquad
                         E\cup\{1,3\}
\tag{2.10}
\]

are different.  More intrinsically, a simple domino-twin support
recovers its unordered domino partition and its cyclic domino order up
to the one global dihedral symmetry.  The partitions in (2.9) contain
\(\{1,2\},\{3,4\}\) and \(\{1,3\},\{2,4\}\), respectively, while the
four fixed dominoes \(H_-,E,H_+,L\) fix the displayed alignment.
Hence the two simple packet supports are different.

The claimed decoder assigns no release to the common edge in (2.8):
it records only the top bit and a finite endpoint state.  Those data
are identical in (2.9), yet they do not select \(\Lambda\).
This is a literal finite counterexample to the asserted \(k=2\) row.

The example is local, as it should be: it refutes the claimed
“exhaustive” transition table.  It can be embedded in a longer domino
cycle with an unchanged run containing a complete common cell, so the
failure is compatible with a fixed global dihedral alignment.  The
global record collision in Section 4 removes any possible concern that
other cells might always repair this local ambiguity for free.

## 3. Why the release-to-weak-cell injection fails

The proposed proof makes three assertions:

1. a front containing a common edge receives no release;
2. the two members of a domino are assigned at its two distinct front
   occurrences; and
3. no weak front receives two releases.

The three statements are incompatible at the top anchor above.  The
unknown endpoint domino \(\Lambda=C_{j+r}\) has only two front
occurrences.  One is the strong top-phase anchor, which assertion (1)
forbids from receiving a release.  The other is its paired occurrence.
If no separate equation determines a member of \(\Lambda\), both
element choices remain at that paired occurrence.  Assertion (3) then
fails.

Equivalently, if one records the first member \(a\in\Lambda\) at the
paired weak front, the family

\[
                         \Lambda=\{a,b\},
 \qquad b\in A\setminus\{a\},
\tag{3.1}
\]

still has \(\Theta(n)\) possible partners.  The closing recurrence
does not determine \(b\) until the remaining internal pairing has
already been determined; using that pairing to force \(b\) is circular,
because determining all internal pairings is the conclusion of the
inverse lemma.

There are two honest ways to repair the record locally:

* record \(\Lambda\) as one pair-valued release, with
  \(\Theta(n^2)\) possibilities; or
* record both of its element labels and charge two releases.

Neither repair gives the asserted injection of element releases into
weak cells.  To recover an \(n^{s/3}\) estimate one would additionally
need a disjoint or bounded-overlap theorem charging the two releases to
at least six missing targets in neighbouring collars.  Such a theorem
is not contained in the zipper recurrence.

## 4. A full-record counting contradiction

The local example proves that the written inverse algorithm is invalid.
We now show that no alternative interpretation of the same record size
can restore its claimed uniqueness.

Work in the annular parametrization

\[
                         h=m-2r=\Theta(\sqrt m).
\tag{4.1}
\]

Fix a packet \(F\).  Choose two length-\(\ell\) intervals of its domino
cycle whose initial positions differ by \(r\).  Independently repartition
the \(2\ell\) labels of each interval into an ordered list of
\(\ell\) unordered dominoes, leaving all other dominoes fixed.  There
are at least

\[
                         \frac1{2m}
 \left(\frac{(2\ell)!}{2^\ell}\right)^2
\tag{4.2}
\]

distinct simple supports.

Only cores whose boundary cuts one of the two intervals can change.
The three bad-front bands have total size

\[
 2(\ell-1)+\min\{\ell-1,h\},
\tag{4.3}
\]

and there are at most four boundary-only exceptional cells.  Since
each cell has four targets, every member of (4.2) has defect at most

\[
                         s_\ell
 =8\ell+4\min\{\ell,h\}+O(1).
\tag{4.4}
\]

Stirling's formula gives

\[
 \log |\mathcal F_\ell|
 =4\ell\log\ell+O(\ell+\log m).
\tag{4.5}
\]

Choose

\[
                         \ell=\frac{m}{\sqrt{\log m}}.
\tag{4.6}
\]

Then \(h=o(\ell)=o(m)\), and hence

\[
 s_\ell=(8+o(1))\frac{m}{\sqrt{\log m}},
\tag{4.7}
\]

\[
 \log |\mathcal F_\ell|
 =(4+o(1))m\sqrt{\log m}.
\tag{4.8}
\]

Now count the records used in the zipper proof.  The global alignment,
all \(J_i\), all phase bits, and all finite endpoint states have only
\(\exp(O(m))\) possibilities.  If releases inject into weak cells,
then \(w\le s_\ell/3\) and the released label identities have at most
\(n^w\) possibilities.  Thus the complete record space has logarithm
at most

\[
 O(m)+\frac{s_\ell}{3}\log n
 =\left(\frac83+o(1)\right)m\sqrt{\log m}.
\tag{4.9}
\]

Comparison with (4.8) shows that, for every fixed constant hidden in
the \(O(m)\), the packet family is eventually larger than the record
space by

\[
 \exp\left(
 \left(\frac43-o(1)\right)m\sqrt{\log m}
 \right).
\tag{4.10}
\]

By the pigeonhole principle, distinct packets have exactly the same
complete proposed record.  Therefore “phase record plus ordered
releases uniquely reconstructs all dominoes, their order, and their
pairing” is false as a global statement.

The same comparison directly contradicts (0.9).

## 5. Exact surviving boundary

### Proved false

1. A two-point top-phase anchor is a zero-release anchor.
2. The paired recurrence splits an unknown endpoint domino into two
   independently forced labels.
3. Element releases inject into weak cells.
4. The recorded releases and phase bits uniquely reconstruct every
   internal pairing and cyclic order.
5. The uniform inverse bound \(\exp(Cm)n^{s/3}\) for all \(s=o(m)\).
6. The sharpened conflict-thinning conclusion based on that inverse
   bound.

### Still valid

1. Complete common cells determine their star cores and permit one
   global dihedral alignment.
2. A three- or four-target intersection fixes a star anchor.
3. A two-target intersection has only the star/top phase ambiguity at
   the level of its common Johnson edge.
4. The crude trace enumeration
   \[
       |\{G:|F\setminus G|\le s\}|
       \le \exp(O(m))n^{3s}.
   \]
5. Collar-disjoint non-domino reconnections admit local defect charges.

### Required for any replacement

A corrected inverse theorem must record every unresolved endpoint
domino and prove a nonoverlapping defect charge for those pair-valued
records.  Even that cannot give a uniform static coefficient below
\(1/2\), because the two \(r\)-separated bad fronts in Section 4 nearly
coincide.  Any surviving annulus route must instead use an explicit
terminal-scale constant, a clustered-front quotient, or information
from the stopped trajectory that excludes simultaneous survival of the
two segment repartitions.
