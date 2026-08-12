# PBBS short returns: deck amplification and the necessary rare-root estimate

Date: 2026-07-25

No finite search, computation, or external input is used.

## 1. Setup

Put

\[
 N=2r+1,
 \qquad
 B=\operatorname{Cat}_r=\frac1N\binom Nr,
\]

and let \(P_r\) be the canonical PBBS factor.  Quotient the
complement-projected step-two cycles by cyclic coordinate rotation.  The
directed quotient-edge set has cardinality \(B\), and its edges are indexed
by the normalized Dyck roots of semilength \(r\).

If consecutive occurrences of one omitted label have odd gap \(2s+1\),
the associated positive projected residence interval has \(s+2\) transition
edges.  Thus residence at most \(H\) is equivalent to

\[
 2s+1\le 2H-1,
 \qquad
 |I|=s+2\le H+1.
\tag{1.1}
\]

Let \(R_H\) be the number of quotient edges which start such a return.
There is at most one relevant interval starting at any quotient edge,
because the next occurrence of the currently omitted label is unique.

Let \(Z_H\) be the number of quotient edges on quotient step-two cycles of
length at most \(H+1\).  The voltage-itinerary bound gives

\[
 Z_H\le (2H+2)N^{2H+2}.
\tag{1.2}
\]

Write \(\nu_H(P_r)\) for the maximum number of pairwise physical
step-two-edge-disjoint residence intervals of residence at most \(H\).

## 2. Circular packing with one start per edge

### Lemma 2.1

Let \(C\) be a directed cycle of length greater than \(K\), and let
\(\mathcal A\) be a family of directed circular intervals on \(C\), each
using at most \(K\) consecutive edges.  Suppose at most one member of
\(\mathcal A\) starts at each edge.  Then \(\mathcal A\) contains a
pairwise edge-disjoint subfamily of size at least

\[
 \frac{|\mathcal A|}{2K-1}.
\tag{2.1}
\]

#### Proof

Fix \(I\in\mathcal A\), of length \(k\le K\), and index its edges by
\(0,1,\ldots ,k-1\).  If an interval of length at most \(K\) meets \(I\),
its initial edge lies among the cyclic residues represented by

\[
 -(K-1),-(K-2),\ldots ,k-1.
\]

There are at most \(K+k-1\le2K-1\) such residues.  Since starts are
unique, the intersection graph of \(\mathcal A\) has maximum degree at
most \(2K-2\).  Greedy independent-set selection gives (2.1). \(\square\)

This proof includes intervals crossing an arbitrarily chosen drawing seam;
no linearization loss is present.

## 3. Every nonwrapping quotient interval has all \(N\) disjoint lifts

### Lemma 3.1

Let \(\overline C\) be a quotient step-two cycle of length \(d\), and let
\(I\) be an interval of \(k<d\) consecutive quotient edges.  Then the
\(N\) spatial rotations of any physical lift of \(I\) are pairwise
physical-edge-disjoint.

#### Proof

Let \(C\) be the physical step-two cycle containing one lift, and let
\(S\le C_N\) be its rotation stabilizer, of order \(h\).  Rotations outside
\(S\) put the lift on distinct physical cycles.  On \(C\), the \(h\)
rotations belonging to \(S\) start at positions spaced by exactly \(d\)
edges, because \(C/S=\overline C\).  Since \(k<d\), those \(h\) circular
arcs are pairwise disjoint.  Hence all \(N\) rotations are disjoint.
\(\square\)

If two quotient intervals have disjoint quotient-edge traces, no physical
lift of one can meet a physical lift of the other: a common physical edge
would project to a common quotient edge.

## 4. Deck-amplification theorem

### Theorem 4.1

For every \(H\) with \(2(H+1)<N\),

\[
 \boxed{
 \nu_H(P_r)
 \ge
 \frac{N}{2H+1}\bigl(R_H-Z_H\bigr).
 }
\tag{4.1}
\]

The right side may of course be replaced by its floor.

#### Proof

Discard the at most \(Z_H\) return starts lying on quotient cycles of
length at most \(H+1\).  Every remaining residence interval has at most
\(K=H+1\) quotient edges and lies on a quotient cycle of length greater
than \(K\).  Apply Lemma 2.1 separately on all those cycles.  Their union
contains an edge-disjoint quotient family of size at least

\[
 \frac{R_H-Z_H}{2K-1}
 =\frac{R_H-Z_H}{2H+1}.
\]

Every chosen quotient interval has length strictly smaller than its
quotient cycle.  Lemma 3.1 supplies all \(N\) pairwise disjoint spatial
lifts of each one, and disjoint quotient traces make the lift families for
different chosen intervals mutually disjoint.  Multiplication by \(N\)
proves (4.1). \(\square\)

The estimate handles both cyclic seams exactly: Lemma 2.1 is circular,
and the only quotient intervals which can traverse a quotient edge twice
were removed in the explicit \(Z_H\) term.

## 5. Consequence for the proposed Gaussian residence theorem

Fix \(A>0\) and put \(H_A=\lceil A\sqrt r\rceil\).  Since

\[
 \log Z_{H_A}=O_A(\sqrt r\log r)=o(r)
\]

whereas \(B\asymp4^r/r^{3/2}\), one has

\[
 Z_{H_A}=o_A(B/\sqrt r).
\tag{5.1}
\]

### Corollary 5.1 (necessary rare-root theorem)

If

\[
 \nu_{H_A}(P_r)=o_A(B),
\tag{5.2}
\]

then necessarily

\[
 \boxed{
 R_{H_A}=o_A(B/\sqrt r).
 }
\tag{5.3}
\]

#### Proof

Rearranging (4.1) gives

\[
 R_{H_A}-Z_{H_A}
 \le \frac{2H_A+1}{N}\nu_{H_A}(P_r)
 =o_A(B/\sqrt r).
\]

Use (5.1). \(\square\)

Thus RP\(_A\) requires much more than saying that a vanishing proportion
of Dyck roots starts a Gaussian-short return.  The required proportion is
\(o_A(r^{-1/2})\).  Equivalently, any proof by direct enumeration must
recover an additional square-root factor before packing or transversality
can enter.

## 6. Adversarial audit and precise boundary

1. **No hidden two-parity factor.**  A return start at PBBS time \(i\)
   is assigned to the projected transition with tail time \(i-1\).  This
   is a bijective reindexing of the directed step-two edge set, so at most
   one return interval starts at each quotient edge.
2. **Repeated quotient edges.**  They can occur only when the interval
   length reaches the quotient-cycle length.  All cycles of length at most
   \(H+1\) were put into \(Z_H\); hence Lemma 3.1 is applied only with
   \(k<d\).
3. **Physical seams.**  Rotations in one stabilizer are separated by
   exactly one quotient-cycle length \(d\), so a \(k<d\) arc cannot meet
   its rotated copy across the physical cyclic seam.
4. **Scope.**  Theorem 4.1 is a lower bound and therefore an obstruction,
   not a proof of RP\(_A\).  It shows that proving only
   \(R_{H_A}=o(B)\) is quantitatively insufficient.  The still-unproved
   minimal enumerative necessity is (5.3); even (5.3) alone is not asserted
   sufficient for RP\(_A\), because many sparse quotient returns may still
   have disjoint traces.

## 7. Exact Pascal form of the necessary estimate

Let \(E\in\mathcal D_d\) be a one-step peak-deletion core, let
\(k(E)=\operatorname{pk}(E)\), and suppose odd \(g<N\) is a reduced
predecessor-passage time prescribing final-slot occupancy \(z_E(g)\).  The
exact number of rank-\(r\) inverse roots starting that return is

\[
 K_r(E,g)=
 \binom{r+d-k(E)-z_E(g)-1}{2d-1}.
\tag{7.1}
\]

Consequently

\[
 R_H=
 \sum_{\substack{g\le2H-1\\g\ {m odd}}}
 \ \sum_{d=1}^{r-1}
 \ \sum_{\substack{E\in\mathcal D_d\\
                    g\ {m a\ passage\ for}\ E}}
 K_r(E,g).
\tag{7.2}
\]

Combining (7.2) with Corollary 5.1 shows that RP\(_A\) necessarily implies
the Pascal-weighted estimate

\[
 \boxed{
 \sum_{\substack{g\le2H_A-1\\g\ {m odd}}}
 \sum_{d,E:\,g\ {m passage}}
 \binom{r+d-k(E)-z_E(g)-1}{2d-1}
 =o_A\!\left(\frac{BH_A}{N}\right)
 =o_A(B/\sqrt r).
 }
\tag{7.3}
\]

This is necessary, not sufficient: an upper bound for the number of starts
does not by itself exploit possible overlap of their quotient traces.

The known mountain-tower family does not violate (7.3).  Its optimized
number of quotient starts is

\[
 B\exp[-\Theta(r^{1/3})],
\]

and its quotient intervals have length \(\Theta(r^{1/3})\).  Even after
the full factor-\(N\) deck amplification, its certified physical packing is

\[
 B\,r^{2/3}\exp[-\Theta(r^{1/3})]=o(B).
\]

At the Pascal saddle, by contrast, each of \(\Theta(\sqrt r)\) lattice
cells has outer mass \(\Theta(B/r)\).  Hence a positive bounded-slot
passage density throughout one Gaussian saddle tube would make the left
side of (7.3) \(\Theta(B/\sqrt r)\), and Theorem 4.1 would give a physical
packing \(\Omega_A(B)\).  This is a valid conditional refutation of
RP\(_A\), but no positive-density passage theorem is presently proved.
