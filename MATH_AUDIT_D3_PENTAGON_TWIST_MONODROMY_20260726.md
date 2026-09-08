# D3 pentagon conveyor: exact switches and the failed order-three twist

## 1. Input path partitions

Write every row as an oriented alternating path

\[
X_0-Y_0-X_1-Y_1-X_2-Y_2-X_3.
\]

The old factor is

\[
\begin{array}{ll}
1:&123-136-146-456,\\
2:&124-126-156-356,\\
3:&125-145-345-346,\\
4:&135-235-245-246,\\
5:&134-234-236-256,
\end{array}
\]

and the new factor is

\[
\begin{array}{ll}
1:&123-126-156-456,\\
2:&124-234-345-356,\\
3:&125-235-236-346,\\
4:&135-136-146-246,\\
5:&134-145-245-256.
\end{array}
\]

For a row define its left incidences by \((X_t,Y_t)\) and its right
incidences by \((Y_t,X_{t+1})\).  Denote the two matching ledgers by
\(L\) and \(R\).

## 2. The phasewise matching differences are not C6/C8-only

Direct cancellation gives the following canonical alternating-cycle
decompositions:

\[
\begin{aligned}
L^-\triangle L^+
={}&(235,2345,234,2346,236,2356)\\
&\dot\cup
(124,1246,146,1456,156,1356,135,1235,125,1245,145,1345,134,1234),
\end{aligned}
\]

so the left difference is one \(C_6\) and one \(C_{14}\).  Similarly,

\[
\begin{aligned}
R^-\triangle R^+
={}&(145,1245,245,2345,345,1345)\\
&\dot\cup
(136,1236,126,1246,246,2456,256,2356,236,2346,346,3456,356,1356),
\end{aligned}
\]

so the right difference is again one \(C_6\) and one \(C_{14}\).

Because the symmetric difference of two matchings has a unique
decomposition into alternating connected components, these \(C_{14}\)
components cannot be refined into phasewise \(C_6\) and \(C_8\) switches.

## 3. The genuine C8 atom and its two exact contexts

In the full incidence graph there is an alternating eight-cycle

\[
Z_8=
126-1246-146-1456-156-1356-136-1236-126.
\]

Toggling \(Z_8\) in the old factor gives the exact equal-length path
partition

\[
\begin{array}{ll}
1:&123-126-156-456,\\
2:&124-146-136-356,
\end{array}
\]

with rows 3,4,5 unchanged.  Call this factor \(F^\circ\).  Both the
\(X\)- and \(Y\)-ledgers remain exact, the same five start and end ports
are used, and the intrinsic targets of the two affected rows are both
still 6.  Thus this C8 atom is target-neutral.

The same cycle can be toggled backwards from the new factor.  This gives
the second exact equal-length intermediate

\[
\begin{array}{ll}
1:&123-136-146-456,\\
2:&124-234-345-356,\\
3:&125-235-236-346,\\
4:&135-156-126-246,\\
5:&134-145-245-256.
\end{array}
\]

Call it \(F^\bullet\).  It has the same complete ledgers and the same
start-to-complement endpoint pairing.  Thus \(Z_8\) has two legal
contexts, \(F^-\leftrightarrow F^\circ\) and
\(F^\bullet\leftrightarrow F^+\), but produces no endpoint twist in
either context.

## 4. The residual correction is a coupled pair of C12 trails

After the C8 toggle, the residual difference \(F^\circ\triangle F^+\)
can be separated, at the four-valent color vertex 2345, into the two
edge-disjoint alternating closed trails

\[
\begin{aligned}
Z_{12}^{(1)}={}&
124-1246-246-2456-256-2356-235-2345\\
&-345-1345-134-1234-124,
\end{aligned}
\]

and

\[
\begin{aligned}
Z_{12}^{(2)}={}&
356-1356-135-1235-125-1245-245-2345\\
&-234-2346-346-3456-356.
\end{aligned}
\]

Toggling both trails gives the new factor.  Toggling either one alone
preserves the underlying incidence b-factor but destroys the
equal-length anchored path partition.  For example, toggling only
\(Z_{12}^{(1)}\) produces components

\[
124-1234-234-2346-236-2356-235-1235-135
\]

and

\[
134-1345-145-1245-125,
\]

with respectively four and two \(X\)-transitions.  Hence the two C12
corrections form one indivisible port-preserving atom in the anchored
category.

There is a complete eight-state check.  Let \(a,b,c\in\{0,1\}\) record
whether \(Z_8,Z_{12}^{(1)},Z_{12}^{(2)}\) are toggled from the old
factor.  All eight choices preserve the incidence degrees.  Their
multisets of numbers of \(X\)-transitions in the five path components
are

\[
\begin{array}{c|c}
(a,b,c)&\text{path lengths}\\ \hline
000&3,3,3,3,3\\
100&3,3,3,3,3\\
010&4,2,3,3,3\\
110&4,2,3,3,3\\
001&4,2,3,3,3\\
101&4,2,3,3,3\\
011&3,3,3,3,3\\
111&3,3,3,3,3.
\end{array}
\]

The four equal-length states are exactly
\(F^-,F^\circ,F^\bullet,F^+\), and each has the identity
start-to-complement endpoint pairing.  Therefore the complete
old/new symmetric-difference cube contains no legal twisted
intermediate.

## 5. The complete layer-splice cube

Let \(A,B,C\) denote respectively the three matchings from the start
stratum to the first interior \(X\)-stratum, between the two interior
strata, and from the second interior stratum to the end stratum.  Index
both interior strata by their old rows.  The new matchings induce the
permutations

\[
a=(1\ 2\ 5\ 3\ 4),\qquad
b=(3\ 4\ 5),\qquad
c=(1\ 4\ 5\ 3\ 2),
\]

and direct composition gives

\[
cba=1.
\]

The changes in the three phase-color ledgers are

\[
\begin{aligned}
d_0={}&e_{1356}+e_{1345}-e_{1246}-e_{1245},\\
d_1={}&e_{2356}+e_{1245}-e_{1345}-e_{2346},\\
d_2={}&e_{2346}+e_{1246}-e_{1356}-e_{2356},
\end{aligned}
\]

with \(d_0+d_1+d_2=0\).  Choosing old or new independently in the
three phases gives the following complete table.  Products act from
right to left.

\[
\begin{array}{c|c|c}
(A,B,C)&\text{endpoint permutation}&\text{color defect}\\ \hline
000&1&0\\
100&a&d_0\\
010&b&d_1\\
001&c&d_2\\
110&ba&-d_2\\
101&ca&-d_1\\
011&cb&-d_0\\
111&1&0.
\end{array}
\]

All eight entries are equal-length path collections, but only 000 and
111 have complete color ledgers.  Thus none of the six mixed layer
splices is itself a legal local factor.

The most useful formal splice is 101, namely new outer attachments and
the old middle matching.  Its endpoint monodromy is

\[
\tau=ca=(2\ 3\ 5)
\]

and its paths are

\[
\begin{array}{ll}
1:&123-126-156-456,\\
2:&124-234-236-346,\\
3:&125-235-245-256,\\
4:&135-136-146-246,\\
5:&134-145-345-356.
\end{array}
\]

The second and fifth paths repeat 2346 and 1345 respectively.  Its
ledger is

\[
\mathcal Y+e_{1345}+e_{2346}-e_{1245}-e_{2356}
=\mathcal Y-d_1.
\]

The complementary 010 splice has the opposite defect \(d_1\) and
endpoint permutation \(b=(3\ 4\ 5)\).  Under fixed port labels this
permutation is not the inverse of \(ca\); the color-defect cancellation
and port-monodromy cancellation are separate conditions.

The coupled C12 repair removes the 101 color defect, but at the same
time restores trivial endpoint monodromy.  Hence the pentagon trade
repairs the ledger and kills the twist simultaneously.

## 6. Serial twist with a defect cocycle

Let \(A\) be an equal-length port packet whose outgoing ports are
obtained from its incoming ports by a permutation \(\tau\) of finite
order \(h\).  Let \(\varepsilon\) be its signed internal ledger defect
and \(\delta\) its carrier direction.  Assume aligned serial gluing is
functorial for the induced actions \(\tau_*\) on ledger and carrier
coordinates.  Then \(h\) serial copies have trivial port monodromy,
ledger defect

\[
N_\tau\varepsilon
:=\varepsilon+\tau_*\varepsilon+\cdots+
\tau_*^{h-1}\varepsilon,
\]

and carrier direction

\[
N_\tau\delta
:=\delta+\tau_*\delta+\cdots+
\tau_*^{h-1}\delta.
\]

Consequently, a bounded-order twist atom closes to an exact serial
packet precisely when

\[
N_\tau\varepsilon=0,
\]

and it is productive precisely when additionally

\[
N_\tau\delta\ne0.
\]

The complete-ledger case is \(\varepsilon=0\).  If moreover
\(\tau_*\delta=\delta\), then \(N_\tau\delta=h\delta\).

This is the smallest useful bounded-order twist principle: the ledger
defect must lie in the augmentation part killed by the norm, while the
carrier must have a nonzero invariant component.  The D3 splice 101
supplies a formal order-three candidate, but the present five-row
construction does not provide a functorial gluing action for which its
explicit defect has zero \(\tau\)-norm.  Local exact repair instead
trivializes the monodromy.

There is also a literal three-copy obstruction.  If three copies use the
same six coordinate labels, the port permutation acts only on strands,
not on the color ledger.  Hence \(\tau_*\) is the identity on the four-set
coordinates and

\[
N_\tau(-d_1)=-3d_1\ne0.
\]

Nor is the row cycle \((2\ 3\ 5)\) induced by a coordinate permutation
of \([6]\) preserving the five Dyck roots.  Indeed, coordinate 2 belongs
to roots \(\{1,2,3\}\); that row set would be sent to
\(\{1,3,5\}\), but no coordinate has that membership pattern among

\[
\{123,124,125,135,134\}.
\]

Thus three literal or coordinate-equivariant copies of the existing D3
splice do not cancel its defect.  Any successful norm-zero realization
must add a genuinely new context action or a different local atom.

## 7. Verdict and exact successor target

The old/new D3 pentagon conversion has the exact factorization

\[
F^-\xrightarrow{\ Z_8\ }F^\circ
\xrightarrow{\ Z_{12}^{(1)}+Z_{12}^{(2)}\ }F^+.
\]

There is no phasewise C6/C8-only decomposition, and the complete
eight-state switch cube has no legal nontrivially twisted intermediate
among these five rows.  The smallest
remaining construction target is therefore:

> Find a bounded-row, equal-length path packet with nontrivial
> finite-order endpoint permutation \(\tau\), ledger defect
> \(\varepsilon\), and carrier direction \(\delta\), such that
> \(N_\tau\varepsilon=0\) but \(N_\tau\delta\ne0\).  The special case
> \(\varepsilon=0\), \(\tau_*\delta=\delta\), is the cleanest target.

For order three, one may either add a local ledger repair that preserves
the monodromy, or exhibit a serial gluing action under which the D3
defect
\(e_{1345}+e_{2346}-e_{1245}-e_{2356}\) has zero norm.  The repair
already present in the pentagon does neither: it restores the ledger by
trivializing the monodromy.

## 8. Interface with genuine C6/C8 monodromy routers

The clean star C8

\[
136-1236-236-2346-346-3456-356-1356-136
\]

is alternating in the old pentagon factor and gives a genuine odd
four-strand endpoint router.  It does not, however, preserve equal path
lengths.  Direct tracing after the toggle gives five paths with numbers
of \(X\)-transitions

\[
2,2,3,5,3.
\]

Thus the general C6/C8 strand-splicing theorem corrects monodromy in the
root-to-sink b-factor category, but does not by itself produce a wreath
factor or an equal-length twist atom.  A successful bounded-order atom
must combine monodromy routing with a length-balancing ledger, rather
than treating these as the same condition.
