# Lane K: the H25 interlaced-`C6` plateau pivot and its literal common-`Q` current

**Date:** 2026-07-28  
**Status:** exact finite theorem, independently reconstructed.  The outer
Hall obstruction descends from \(25\) to \(24\) by a genuinely non-one-braid
macro.  On the original critical DM shore the same macro has an explicit
one-word, \(1297\)-pin common-\(Q\) realization and reduces the literal shore
gap from \(25\) to \(23\).  No full \(16383\)-target compiler is claimed.

## 1. Main result

Let \(G(T)\) be the depth-three target--cell compiler graph of a resident
rank-eight Johnson chronology \(T\).  Starting from the audited H25 carrier,
put

\[
\begin{aligned}
T_0&=H25,\\
T_1&=\operatorname{RF}(2612,3222,3766)T_0,\\
T_2&=\operatorname{FF}(2125,2769,6201)T_1.
\end{aligned}                                                    \tag{1.1}
\]

Then

\[
\delta_H(T_0)=25,qquad \delta_H(T_1)=25,qquad \delta_H(T_2)=24. \tag{1.2}
\]

The matching sizes are \(16358,16358,16359\).  Every state in (1.1):

1. is a permutation of all \(6435\) rank-eight sets;
2. is a Johnson path and is depth-three resident;
3. has every protected upper target at each depth \(q=1,\ldots,7\);
4. has exactly four missing rank-seven lower edge colours.

The lower fixed-depth hole vectors are

\[
(4,19,4,1,0,0,0),quad
(4,19,6,1,0,0,0),quad
(4,19,6,1,0,0,0).                                   \tag{1.3}
\]

Thus the macro preserves the required middle, residence, upper-support and
immediate-lower conditions.  It is not a claim of exact deeper-lower
multiset preservation.

The independently reconstructed transition data are

| transition | changed cell shores | common-core rank | old/new boundary rank |
|---|---:|---:|---:|
| \(T_0\to T_1\) | 29 | 16334 | \(24\to24\) |
| \(T_1\to T_2\) | 40 | 16338 | \(20\to21\) |

Directly comparing \(T_0\) with \(T_2\), \(19242\) of the \(19311\) cell
shore signatures cancel, the two boundary banks have \(69\) cells each,
the common rank is \(16314\), and the contracted boundary rank is

\[
44\longrightarrow45.                                  \tag{1.4}
\]

This is the exact one-unit outer Hall gain.

## 2. Plateau-pivot descent theorem

For a bipartite graph \(G\) on the fixed target set, write

\[
d_G(X)=|X|-|N_G(X)|,\qquad \delta(G)=\max_X d_G(X).
\]

Suppose \(\delta(G_0)=h\), and for \(G_0,G_1,G_2\) put

\[
\sigma_0(X)=h-d_{G_0}(X),qquad
I_j(X)=|N_{G_j}(X)|-|N_{G_{j-1}}(X)|.                \tag{2.1}
\]

### Theorem 2.1 (two-step plateau criterion)

Exactly

\[
\delta(G_2)=h-min_X\bigl(\sigma_0(X)+I_1(X)+I_2(X)\bigr).       \tag{2.2}
\]

Consequently (delta(G_2)\le h-1) if and only if

\[
\sigma_0(X)+I_1(X)+I_2(X)\ge1qquad\text{for every }X.           \tag{2.3}
\]

If (G_1) remains on the plateau (delta(G_1)=h), its active shores are

\[
\mathcal F_1={X:\sigma_0(X)+I_1(X)=0}.                         \tag{2.4}
\]

The second move must in particular satisfy (I_2(X)\ge1) on every
(X\in\mathcal F_1).  This is why a one-move local minimum does not imply a
two-move local minimum: the first move may repair the old maximizer while
spending one unit of slack on a different shore, and the second move may
repair the newly tight family.

#### Proof

For every (X),

\[
d_{G_2}(X)
=d_{G_0}(X)-I_1(X)-I_2(X)
=h-\sigma_0(X)-I_1(X)-I_2(X).
\]

Taking the maximum over (X) proves (2.2), and (2.3)--(2.4) follow.  No
uniqueness assumption on a DM shore is used.  ∎

For the three canonical alternating shores (S_0,S_1,S_2), rows indexed by
the graphs (G(T_0),G(T_1),G(T_2)) and columns by the shores, the exact gap
matrix is

\[
\begin{pmatrix}
25&24&23\\
24&25&24\\
23&24&24
\end{pmatrix}.                                                   \tag{2.5}
\]

Hence the old shore improves (25\to24\to23); the pivot shore moves
(24\to25\to24); and the final active shore has gap (24).  This is a
literal realization of Theorem 2.1, not a heuristic lookahead effect.

## 3. Exact seven-block commutator form

Cut (T_0) at

\[
0<2125<2612<3222<3610<3767<6202<6435
\]

and call the seven consecutive blocks (X_0,\ldots,X_6).  Pulling the
second braid back through the first gives the reduced signed word

\[
\boxed{
X_0,\overleftarrow{X_3},X_2,X_5,X_1,\overleftarrow{X_4},X_6.}    \tag{3.1}
\]

It has seven monotone runs in the old index line, so it cannot coarsen to
the four-run normal form (A,C^{\epsilon}B^{\eta}D) of one
`FF/RF/FR/RR` braid.  Thus (1.1) genuinely escapes the exhausted H25
one-braid catalogue.

On the twelve exposed endpoint ports, the old and final seam matchings split
into two alternating (C_6)'s.  Their cut triples are

\[
\{2125,3610,6202\},qquad \{2612,3222,3767\}.          \tag{3.2}
\]

The triples interlace in the linear order.  They are port-disjoint but not
separated physical actions; this is precisely the nonlocal coupling which
allows the first `C6` current to move the active Hall shore and the second to
repay it.

More generally, two three-cut braids pull back to a signed permutation of at
most seven old intervals: the first map has at most three breakpoints, and
the three cuts of the second contribute at most three additional preimages.
For a final (s)-seam signed block word, at shadow depth (q) at most (sq)
old and (sq) new windows occur in the exact terminal-shadow ledger.  All
other windows cancel under block transport, including reversal.  Residence
can fail only at final seams.  This gives a complete local structural audit
of such macros.

The qualification “terminal shadow” is essential.  Reversal changes a
left-rooted owner tower to a right-rooted tower.  Nested occurrence pins do
not transport merely because their terminal unions/intersections agree.

## 4. Outer DM current on the old critical shore

The old H25 canonical shore (S_0) has

\[
|S_0|=1320,qquad |N_{G(T_0)}(S_0)|=1295.             \tag{4.1}
\]

In the final graph,

\[
|N_{G(T_2)}(S_0)|=1297.                              \tag{4.2}
\]

Thus the composite supplies net two physical neighbours outside the old
DM neighbourhood.  This is stronger than merely changing the identity of a
maximum matching.  It also explains why testing only the old shore is not
sufficient: its gap falls to (23), while a relocated shore keeps the
global deficiency at (24).

## 5. Literal common-`Q` realization of all 1297 final neighbours

Let (P=E_3(T_2)) be the maximal depth-three erosion controller.  For a
cell (c=(s,e)), (e=0,1,2), put

\[
\tau(c)=\bigcup_{p=s}^{s+e}P_p.                       \tag{5.1}
\]

Every native pin (c\mapsto\tau(c)) is realized simultaneously by the one
word (P).  On the (1297) cells in (N_{G(T_2)}(S_0)), every trace lies in
(S_0), but there are only (1295) distinct trace values.  The complete
collision list is

\[
\begin{aligned}
1928 &: c=3856,6045,\\
4189 &: c=10179,12640.
\end{aligned}                                                    \tag{5.2}
\]

Resolve these two collisions as follows:

\[
\begin{array}{c|c|c|c}
c&\text{physical interval}&\text{native trace}&\text{selected target}\\ \hline
3856 &[3856,3856]&1928&1920\\
6045 &[6045,6045]&1928&1928\\
10179&[3741,3742]&4189&89\\
12640&[6202,6203]&4189&4189.
\end{array}                                                       \tag{5.3}
\]

Use every other native trace on its unique cell.  The resulting (1297)
targets are distinct members of (S_0), and every displayed target--cell
pair is an exact singleton compiler edge.

Now modify (P) only by

\[
\begin{aligned}
(P_{3741},P_{3742})&=(4181,4125)\longmapsto(81,25),\\
P_{3856}&=1928\longmapsto1920,
\end{aligned}                                                     \tag{5.4}
\]

and call the resulting word (A).  Equivalently, the first exceptional pin
deletes coordinate (4) from one letter, while the second intersects two
letters with target (89).

### Theorem 5.1 (fixed-shore literal descent)

The word (A) is nonzero, satisfies

\[
D^3A=T_2,                                                        \tag{5.5}
\]

and realizes all (1297) selected lower pins simultaneously.  Consequently
the common-(Q) gap on the fixed old shore (S_0) is at most

\[
1320-1297=23.                                                    \tag{5.6}
\]

In fact the selected cells exhaust (N_{G(T_2)}(S_0)), so (23) is exact
for this shore.

#### Proof

Only nine central windows meet a changed position.  Their targets, before
and after (5.4), are respectively unchanged:

\[
\begin{array}{c|ccccc}
i&3738&3739&3740&3741&3742\\ \hline
T_{2,i}&5077&4573&12509&12383&14367
\end{array}
\]

and

\[
\begin{array}{c|cccc}
i&3853&3854&3855&3856\\ \hline
T_{2,i}&10200&4056&8136&8076.
\end{array}
\]

Every other central window is disjoint from the changed positions.  Thus
(5.5) holds.

Only eight selected pin intervals meet a changed position.  Their old and
new unions are

\[
\begin{array}{c|c|c|c}
c&\text{selected target}&\text{old union}&\text{new union}\\ \hline
3856&1920&1928&1920\\
10179&89&4189&89\\
10180&12317&12317&12317\\
10293&1992&1992&1992\\
16614&4565&4565&4565\\
16616&12381&12381&12381\\
16617&12319&12319&12319\\
16729&2008&2008&2008.
\end{array}
\]

All other selected pins remain native and disjoint from (5.4).  The three
new letters (81,25,1920) are nonempty.  This proves simultaneous pin
realization and nonzeroness.  Since the targets are distinct, these pins are
an injection.  ∎

The (23) unresolved targets of (S_0) are

\[
\begin{gathered}
449,960,1103,2420,2575,2676,4213,4877,5801,7504,8217,8218,9524,\\
13616,13620,17683,17738,18970,19568,20516,21641,24610,29776.
\end{gathered}                                                    \tag{5.7}
\]

Finally, (5.5) transfers every audited upper target literally: if
(U=\bigcup_{j=i}^{i+q}T_{2,j}), then

\[
U=\bigcup_{p=i}^{i+q+3}A_p.                                    \tag{5.8}
\]

Thus Theorem 5.1 audits a common physical word, not only Hall edges.

## 6. What remains globally

Theorem 5.1 is a literal two-unit improvement on the **fixed old critical
shore**.  It is not a common-(Q) injection for all (16383) lower targets.
The final carrier has a new canonical shore of size (1024) and neighbourhood
size (1000), hence global outer deficiency (24).  Its (1000) native
trace pins are distinct and simultaneously realized by (E_3(T_2)), so
that active core itself has no hidden pin collision; its (24)-target
complement is the next literal obstruction.

This gives the correct descent architecture:

1. a neutral first braid moves the active shore while preserving all frozen
   structural conditions;
2. a second, interlaced `C6` repays the new tight shore and gains one outer
   matching unit;
3. the old shore current is realizable in one common word after two explicit
   exceptional pin replacements;
4. a global compiler still requires coupling this current to every target
   outside the active shore.

An independently audited ordinary move continues from (T_2):

\[
T_2\xrightarrow{\operatorname{FR}(1045,3380,6137)}H23.          \tag{6.1}
\]

It has Hall deficiency (23), remains resident and all-upper-complete, and
keeps four immediate-lower holes.  Its canonical DM right shore likewise has
(999) distinct native pins simultaneously realized by maximal erosion.
This confirms that the plateau pivot crosses a genuine one-step barrier and
then re-enters a descending direction.  It still does not supply the global
common-(Q) compiler.

## 7. The separate zero-target portal

A second interlaced two-braid macro

\[
H25\to H26_{\rm zero6}\to H25_{\rm zero6}
\]

creates the unique target-(2575) cell

\[
(e,s)=(2,5179),qquad
(P_s,P_{s+1},P_{s+2})=(2601,2602,2604).              \tag{7.1}
\]

Its native trace is (2607).  Replacing the native pin (2607) by (2575)
changes the three letters to

\[
(2569,2570,2572),                                    \tag{7.2}
\]

deleting only coordinate (6).  The exact common-(Q) audit retains all
(1144) selected pins, reconstructs every central row, and has no empty
letter.  This is a literal Robin--Hood swap: (2575) leaves the unresolved
set and (2607) enters, so its size stays (25).  It proves that opening a
degree-zero target can be common-(Q)-legal while still failing to create
net capacity.

## 8. Frozen artifacts

The principal files and SHA-256 values are:

| file | SHA-256 |
|---|---|
| `scratch/k15_segment_braid_hall25.json` | `67a84c71f570dbdb8cdad5912b9bed333c4122e9237fed38d56690ad5bd0c473` |
| `scratch/k15_segment_braid_hall25_flat_pivot.json` | `9b76deb397b5a01a78b1196bdec2913fe0640be3cb7c58e0887408199ba8fc4b` |
| `scratch/k15_segment_braid_hall24_twobraid.json` | `aca78d0aa9d10bb468474de0eed21cf2edb54ff6ce6a68570c99ed0ab50c8a37` |
| `scratch/k15_segment_braid_h24_twobraid_audit.json` | `081e0cbae3c1fc37f00aa569a2c7f5b3a6378117a3f4c0a778b94f916e24f563` |
| `scratch/audit_k15_h24_old_dm_common_q_descent.py` | `349b953ed542f135a520c8a3b4797560703c61403616aea039189ac71d06d27a` |
| `scratch/k15_h24_old_dm_common_q_descent_certificate.json` | `6d7522a90ab724dda3c1a6edfec6c5470002f82caee4973a8617419ced3417c0` |
| `scratch/k15_segment_braid_hall23_after_lookahead.json` | `dc4d3ba2f8c8d3ef647f2c46856fb11c2f1aaa436b4f75db5d923f925ccfc563` |
| `scratch/k15_segment_braid_h23_lookahead_audit.json` | `07b330095040bbf7d4a573ec8c43cb7dbfe8fa877010e0ec59486e4e5af65fba` |
| `scratch/k15_h23_lookahead_native_dm_pin_certificate.json` | `b2509e2ca2a4bb47c3b8bf8350ed8d70bda3f1fab962b997755d79b012e7f378` |
| `scratch/k15_h25_zero6_exceptional_pin_certificate.json` | `89c6d006f1f5abc92f234ecd095fae8460412bd206b458b769cf1e8d29c634ae` |

## 9. Precise proved boundary

Proved:

* one-braid local minimality at H25 is defeated by an explicit interlaced
  two-`C6` plateau pivot;
* the outer Hall deficiency drops (25\to24), then (24\to23);
* the first composite supplies two net cells to the old H25 DM shore;
* all (1297) of those cells admit distinct pins realized simultaneously in
  one nonzero word with exact middle reconstruction and all upper coverage;
* the degree-zero (2575) portal is separately literal and common-(Q)-safe,
  but only as a one-for-one swap.

Not proved:

* a single common-(Q) injection covering all (16383) lower targets;
* transport of a globally maximal pin current across the macro;
* coefficient one or the exact (k=15) formula.

The next exact target is therefore not another scalar Hall score.  It is a
plateau-pivot step on the current active shore together with a simultaneous
exceptional-pin chain that extends the native common-(Q) current without
creating a new (24)-defect shore.
