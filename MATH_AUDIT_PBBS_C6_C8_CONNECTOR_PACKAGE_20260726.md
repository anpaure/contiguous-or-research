# Audit of the PBBS hexagon atlas, the (C_8) obstruction, and the long parity bridge

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, or web lookup is
used.

Audited sources:

* `MATH_THEOREM_PBBS_PAIRED_C6_COMPLETE_CLASSIFICATION_20260726.md`;
* `MATH_THEOREM_PBBS_NO_C8_AND_LONG_PARITY_BRIDGE_20260726.md`.

## 0. Verdict

The two notes are mutually consistent and their substantive claims pass.
In particular, the following statements are correct.

1. The natural fixed-(M_0) PBBS exchange digraph has exactly
   
   \[
   \binom{2r+1}{r-1}-(2r+1)
   \]
   directed triangles.  They are precisely the legal star triangles, and
   the exceptional cores are the rotations of
   (000(10)^{r-1}).
2. The support (3)-graph is linear, has maximum degree at most (r), and
   has a vertex-disjoint packing of size
   
   \[
   \frac{\binom{2r+1}{r-1}-(2r+1)}{3r-2}
   =\left(\frac23+o(1)\right)\operatorname {Cat}_r.
   \]
3. There is no (M_1)-alternating (C_8), even before forbidding new
   (M_0)-edges.
4. The displayed (A_b,T_b) states form a legal directed (C_{2n}),
   (n=2r+1).  Its alternating incidence circuit has length (4n).
5. Its exact monodromy change is
   
   \[
   c'-c=\gcd(n,3)-2
   \]
   for (r\ge3), and (c'-c=-1) for (r=2).  Hence it reverses component
   parity at (O(r)) edit cost.
6. Removing the physical support of the bridge destroys at most (2nr)
   members of the natural hexagon atlas.  The surviving atlas still has a
   physically disjoint packing of asymptotic size
   ((2/3)\operatorname {Cat}_r).
7. A circuit with (k) switched (M_1)-slots changes at most (k)
   lower-centred triple-union occurrences.  Consequently the bridge plus
   (O(\operatorname {Cat}_r)) hexagon switches preserves
   
   \[
   \beta_r=O(\operatorname {Cat}_r).
   \]

Neither note proves an (O(\operatorname {Cat}_r))-edit Hamiltonization.
The remaining assertion is exactly a component-quotient assertion: after the
parity bridge when needed, one must choose physically compatible legal
hexagons which meet three current components and form a spanning loose tree.
The local census, profile connectivity, portal property, and packing bound do
not imply that assertion.

There are two small proof-completeness repairs, recorded in Sections 1 and 5
below.  They do not change any theorem statement.

## 1. Forward clean labels in the triangle classification

The converse part of the C6 note's Lemma 3.1 invokes a clean-label
contraction without stating it.  The needed statement is the following exact
mirror of the reverse clean-label lemma in the C8 note.

### Lemma 1.1 (forward survivors only disappear)

Let a cyclic word (C) have (2t+1) more zeros than ones, and let
(U_+(C)) be its forward-unmatched zeros.  After changing at most (t)
zeros to ones, every forward-unmatched zero of the resulting word lies in
(U_+(C)).

#### Proof

It is enough to change one zero.  Cut the original word at its unmatched
zeros.  Between consecutive displayed zeros lie forward-Dyck words.  If a
displayed zero is changed to a one, cancellation of all unchanged Dyck blocks
leaves that new one to consume one other displayed zero.  If an internal zero
of a Dyck block is changed, retain every old matching edge except the edge
incident with that zero.  The new one and the formerly paired one become two
unmatched openings and, after contraction of the retained pairs, consume two
displayed zeros.  No new unmatched zero is created.  Iteration proves the
claim. \(square\)

Now suppose (C+x_0,C+x_1,C+x_2) is a directed star triangle.  Each
successor label is the forward survivor of one of these three states, hence
Lemma 1.1 puts it in the three-element set (U_+(C)).  The three distinct
successor labels exhaust (U_+(C)), and contraction gives the orientation

\[
C+z_0\longrightarrow C+z_2\longrightarrow C+z_1
\longrightarrow C+z_0.
\]

This supplies the only omitted local justification in the triangle census.

## 2. Audit of the exceptional-core criterion

Write the forward-unmatched-zero decomposition of a core as

\[
0_{z_0}D_0\,0_{z_1}D_1\,0_{z_2}D_2.
\]

For (Z_i=C+z_i), direct contraction gives

\[
p_+(Z_i)=z_{i+2}.
\]

The side (Z_i\to Z_{i+2}) collides with (M_0) precisely when

\[
p_-(C+z_{i+2})=z_i.
\]

For (j=i+2), rotate (C+z_j) to

\[
1D_j,0_{z_{j+1}}D_{j+1},0_{z_{j+2}}D_{j+2}.
\]

With (1) contributing (+1), its three regional prefix maxima are

\[
1+\operatorname {ht}(D_j),\qquad
\operatorname {ht}(D_{j+1}),\qquad
\operatorname {ht}(D_{j+2})-1.
\]

The reverse survivor is the zero after the rightmost global maximum.  It is
(z_{j+1}) if and only if

\[
D_j=D_{j+1}=\varnothing,qquad
\operatorname {ht}(D_{j+2})\le1.
\]

The strict rightmost tie condition is essential and is handled correctly in
the source.  Since the total semilength of the three blocks is (r-1>0), the
only illegal cyclic core is

\[
000(10)^{r-1}.
\]

It has full period (2r+1): equivalently, its unique maximal cyclic zero-run
has length four.  Thus there are exactly (2r+1) exceptional labelled cores.
The (r=2) endpoint also checks: all five cores are exceptional and no
directed triangle exists.

The profile separation theorem is also correct.  Cutting (Z_i) after its
forward survivor gives

\[
E_i=D_{i+2},1D_i0,D_{i+1},
\]

and peak-pruning additivity gives

\[
\mathbf a(E_i)=sum_{j=0}^2\mathbf a(D_j)
 +\mathbf e_{\operatorname {ht}(D_i)+1}.
\]

Thus pairwise distinct block heights do separate the three states into three
different (f)-orbits.  The subsequent profile-connectivity argument is a
descent only in the quotient by this invariant; the source correctly does not
promote it to component connectivity.

The inactive-centre census in Corollary 7.5 is correct as well.  The only
inactive normalized root is

\[
1(10)^{r-1}0.
\]

There are exactly (2r+1) labelled rotations.  A concise period check, not
spelled out in the source, is that any period dividing (2r+1) would make the
number (r) of ones divisible in the same ratio, whereas

\[
\gcd(r,2r+1)=1.
\]

The PBBS two-step image has normalized word

\[
1100(10)^{r-2},
\]

which is active for (r\ge3).  Hence every (f^{-2})-component has a legal
hexagon portal.  This is an incidence statement, not an expansion statement.

## 3. Audit of the (C_8) obstruction

Let (A_0,A_1,A_2,A_3) be the four old lower endpoints of a hypothetical
(M_1)-alternating (C_8).  Its old upper endpoint at (A_i) is

\[
U_i=A_i\cup\{p_-(A_i)\}=A_{i-1}\cup A_i,
\]

so

\[
p_-(A_i)=A_{i-1}\setminus A_i.
\]

The simple Johnson (4)-cycle has only the star and rectangle shapes listed
in the source.  In the star case four required reverse survivors would all
have to lie among the three reverse-unmatched zeros of the common core.

In the rectangle case the core has five reverse-unmatched zeros.  Contracting
its reverse-matched pairs reduces the four survivor equations to

\[
s(ac)=d,quad s(bc)=a,quad s(bd)=c,quad s(ad)=b.
\]

For five cyclic zeros, changing a selected pair to ones leaves the first zero
in the longer complementary gap.  Rotating (a) to zero, the equation
(s(bc)=0) leaves only ({b,c}={3,4}) or ({2,4}); the four ordered
possibilities fail one of the other displayed equations exactly as tabulated.
No fixed-(M_0) exclusion enters the proof.  Theorem A is therefore exact.

The consequence should be read with one harmless precision: a (C_8) which
appears only after earlier switches must intersect the **vertex support** of
an earlier switch.  Edge overlap is not asserted or needed.

## 4. Audit of the long directed cycle

For

\[
A_b=\{b-2,b-4,\ldots,b-2r\},qquad
T_b=A_b-\{b-2\}+\{b\},
\]

rotation covariance reduces every matching calculation to (b=0).  The
identities

\[
p_+(A_b)=b,qquad f(A_b)=A_{b+1},
\]

\[
p_+(T_b)=b-1,qquad f^3(T_b)=T_{b+1},
\]

and

\[
f^2(A_b)=A_b-\{b+1\}+\{b\},qquad
f^2(T_b)=T_b-\{b+1\}+\{b-1\}
\]

are correct.  Hence

\[
A_b\longrightarrow T_b\longrightarrow A_{b-2}
\]

uses neither forbidden (f^2)-successor.  Since (2) is invertible modulo
odd (n), these arrows form one directed (C_{2n}).  The (A)- and
(T)-families are disjoint: equality would force (A_b=T_{b+1}) by the
forward-survivor labels, but (b-2) belongs only to the former.

## 5. Audit of the monodromy calculation

Let (b_j=b_0-2j), (a_j=U_{A_{b_j}}), and (t_j=U_{T_{b_j}}).  Switching
the directed cycle left-multiplies the old monodromy (sigma=f^{-2}) by

\[
\tau=(a_0,t_0,a_1,t_1\cdots a_{n-1},t_{n-1}).
\]

The (a_j)'s form one complete old component and satisfy

\[
\sigma(a_j)=a_{j+1}.
\]

For (r\ge3), the three rotation families

\[
\{T_b\},\qquad\{f(T_b)\},\qquad\{f^2(T_b)\}
\]

are pairwise disjoint.  Thus the (T_b)'s lie in one (f)-cycle of length
(3n), hence in one (sigma)-cycle, and

\[
\sigma^3(t_j)=t_{j+1}.
\]

After cutting incoming (sigma)-arcs at the marked vertices, a trace from
(t_j) traverses the old (T)-segment, then (a_{j+2}), and enters
(t_{j+3}).  The return permutation is therefore

\[
j\longmapsto j+3\pmod n.
\]

It has (gcd(n,3)) cycles, replacing the two old touched components.  This
proves

\[
c(\tau\sigma)-c(\sigma)=\gcd(n,3)-2.
\]

The source's (r=2) sentence is correct but terse.  Here
(f(T_b)=T_{b+2}), so, in the (j)-index,

\[
\sigma(t_j)=t_{j+2}.
\]

Consequently (	au\sigma) returns (t_j) to (t_{j+4}).  This is a
nonzero shift on five points, hence one cycle; the two old components merge
and (c'-c=-1).

Since the multiplier is a (2n)-cycle, it is odd, independently confirming
the parity reversal.

## 6. Physical survival and the edit ledger

The bridge support contains exactly the (2n) upper centres (U_Z),
(Z\in\mathcal S={A_b,T_b}), and their (2n) old lower (M_1)-endpoints
(f(Z)).  A natural star hexagon whose centre triple avoids (mathcal S)
is disjoint from both sets because (f) is bijective.  Such a hexagon remains
alternating and legal after the bridge.  Since a centre lies in at most (r)
atlas triples, at most (2nr) triples are lost.  Linearity and greedy packing
then give exactly the post-bridge lower bound in the source.

The (k)-occurrence edit bound also passes, but it is worth making its reason
explicit.  The triple target centred at a lower owner (Y) is the union of
the two rank-((r+1)) upper vertices adjacent to (Y).  Under an
(M_1)-switch, only the (k) old (M_1)-lower endpoints have one of those
two upper neighbours changed.  The (M_0)-lower endpoint at a switched upper
keeps that upper neighbour, even though the other lower endpoint across the
same upper has changed.  Therefore at most (k), not (2k), centred triple
occurrences change.

For the bridge (k=2n); a hexagon has (k=3).  Starting from

\[
\beta_r^{\rm PBBS}=rac{2}{r+2}\binom{2r+1}{r},
\]

the exact one-sided ledger is

\[
\beta_r\le
\frac{2}{r+2}\binom{2r+1}{r}+2n+3s.
\]

Thus (s=O(\operatorname {Cat}_r)) would retain
(eta_r=O(\operatorname {Cat}_r)).

## 7. Exact proved/conditional boundary

The package proves a complete local (C_6) classification, an exact natural
(C_8) obstruction, and an explicit parity-changing longer circuit.  It also
proves that the parity bridge leaves Catalan-scale local hexagon supply and
the Catalan triple-defect budget intact.

It does **not** prove that the quotient multihypergraph of legal star triples
on the current (f^{-2})-components contains a physically representable
spanning loose tree.  Component portals, a single three-component connector,
profile-quotient connectivity, and a matching of more than
(rac12\operatorname {Cat}_r) physical hexagons do not imply this Hall/
connectivity statement.  Consequently the PBBS Hamiltonization and the
constant-one theorem remain conditional on that one component-quotient gate.

