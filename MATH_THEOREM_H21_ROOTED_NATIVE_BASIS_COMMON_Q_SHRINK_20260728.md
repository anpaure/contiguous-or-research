# Rooted native bases at Hall 21 and the exact duplicate-child common-`Q` shrink

Date: 2026-07-28

Status: proved general literal lemma and independently replayable finite
certificates.  No braid, SAT, or carrier search is used here.  The Hall-21
certificate has exactly 21 rooted native-basis DM components.  The frozen
Hall-22-to-Hall-21 splitter has an exact 849-pin common-`Q` realization, and
the new Hall-21-to-Hall-20 splitter has an exact 682-pin common-`Q`
realization.  In both cases a duplicated native child is shrunk to the missing
root while every selected central and lower window survives.  These are
shore-local compiler theorems, not common-word realizations of the full
global maximum matchings.

## 1. Native pins and the maximal common-`Q` word

Let

\[
                 P=(P_0,\ldots,P_{n-1})                         \tag{1.1}
\]

be a controller word with (P_p\ne\varnothing) at every position.  For a physical interval (I\), define its
native trace

\[
                 \tau_P(I)=\bigcup_{p\in I}P_p.                 \tag{1.2}
\]

A pin ((I,\tau_P(I))) is **native**.  It is negative-inert relative to
(P): if (x\notin\tau_P(I)), then (x\notin P_p) for every (p\in I).
Consequently any family of native pins is simultaneously realized by the
single word (P).

In the depth-(d) middle architecture, take (P=E_d(T)).  If every internal
coordinate run of (T) has length at least (d+1), then coordinatewise
erosion followed by dilation gives

\[
                 \bigcup_{p=i}^{i+d}P_p=T_i.                    \tag{1.3}
\]

Thus the central windows themselves are native pins of (P).

## 2. Exact duplicate-child root-shrink theorem

Assume (P) is the maximal pointwise word allowed by the protected central
windows; equivalently in the application,

\[
 P_p=\bigcap_{i:\,p\in[i,i+d]}T_i.                              \tag{2.0}
\]

Let ({\cal W}) be any family of protected native pins

\[
                  (J,S_J),\qquad S_J=\tau_P(J),                 \tag{2.1}
\]

including all central windows that must remain fixed.  Let (I) be another
physical cell with

\[
                  \tau_P(I)=s,\qquad \varnothing\ne r\subset s,\qquad
                  D=s\setminus r.                               \tag{2.2}
\]

We discard the native assignment (I\mapsto s) and instead pin (I\mapsto r).
Define

\[
 A_p=
 \begin{cases}
   P_p\cap r,&p\in I,\\
   P_p,&p\notin I.
 \end{cases}                                                     \tag{2.3}
\]

### Theorem 2.1 (duplicate-native-child root shrink)

The word (A) is nonzero and realizes the exceptional root pin
((I,r)) together with every protected pin in ({\cal W}) if and only if

\[
             P_p\cap r\ne\varnothing\qquad(p\in I),             \tag{2.4}
\]

and

\[
 \boxed{
 \forall(J,S_J)\in{\cal W}\ \forall x\in D\cap S_J,
 \quad
 \exists p\in J\setminus I\text{ with }x\in P_p.}              \tag{2.5}
\]

Moreover, (A) is exactly the maximal common-`Q` word for the central
controller constraints, the native pins ({\cal W}), and the root pin
((I,r)).  Hence (2.4)--(2.5) are necessary and sufficient for this
one-shrink common-`Q` operation, not merely sufficient local checks.

#### Proof

Every native pin in ({\cal W}) imposes no new negative deletion on (P).
The exceptional pin (I\mapsto r) deletes from (P) precisely the coordinates
of (D=s\setminus r) at positions of (I).  Therefore the maximal
common-`Q` candidate is exactly (2.3).

Since union distributes over intersection,

\[
       \bigcup_{p\in I}A_p
       =\left(\bigcup_{p\in I}P_p\right)\cap r
       =s\cap r=r.                                               \tag{2.6}
\]

Thus the exceptional root pin is exact.  Positions outside (I) remain
nonempty, and positions in (I) are nonempty exactly when (2.4) holds.

Fix a protected pin ((J,S_J)).  Shrinking can remove only coordinates in
(D), and it removes every occurrence of such a coordinate lying in (I).
For (x\in D\cap S_J), the coordinate survives the union over (J) exactly
when it has an old occurrence in (J\setminus I).  This is (2.5).  All
coordinates outside (D) are unchanged.  Hence (2.4)--(2.5) are sufficient.

Conversely, failure of (2.4) creates an empty physical letter.  If (2.5)
fails for ((J,S_J,x)), all old occurrences of (x) in (J) lie inside
(I) and are deleted, so the final union is not (S_J).  Both conditions
are therefore necessary.  The maximal-common-`Q` assertion follows from the
first paragraph.  \(\square\)

The formulation permits (I) to overlap other selected cells.  Those
overlaps are exactly what (2.5) audits; disjointness is not assumed.
Every noncentral protected interval in this theorem is native relative to
the baseline controller.  A pre-existing exceptional or point pin must first
be incorporated into the baseline common-`Q` word and then carried as an
additional protected obligation; it is not covered merely by calling it
native.

### Corollary 2.2 (rooted native-basis circuit completion)

Let a target/cell component have left side (X), right side (Y), and a
nonempty root (r\in X) satisfying

\[
                         r=\bigcap_{x\in X}x.                    \tag{2.7}
\]

Suppose the native trace map is a bijection

\[
                         \tau_P:Y\longrightarrow X\setminus\{r\}. \tag{2.8}
\]

Let (s\in X\setminus\{r\}), and suppose there is an additional cell
(I\notin Y) with native trace (s).  Keep the old native cell of trace
(s), and repin the duplicate (I) to (r).  If (2.4)--(2.5) hold for the
central windows and every retained pin, then one word realizes all
(|X|) component targets on distinct cells.  In particular, the component
is literally saturated.

#### Proof

The old native cells still serve every target in (X\setminus\{r\}), while
Theorem 2.1 makes the extra cell serve (r).  Target and cell endpoints are
both distinct, and all pins use the one word (A).  \(\square\)

For a global Hall descent one must additionally retain or reroute a disjoint
exterior matching.  Corollary 2.2 pays the complete local matching and
common-`Q` gate, but does not silently supply those exterior pins.

## 3. The exact Hall-21 rooted-native census

Consider the frozen carrier

```text
scratch/k15_segment_braid_hall21_zero6.json
```

of SHA-256

```text
8a294110b530ba016b790f08f59c9d5bca3471af732867e27b0cb4a0b628b447.
```

Its lower compiler graph has

\[
 |L|=16383,\qquad |R|=19311,\qquad \nu=16362,
 \qquad h=21.                                                    \tag{3.1}
\]

The canonical alternating DM shore is (846/825).

### Theorem 3.1 (all 21 components are rooted native bases)

The induced DM graph has exactly 21 connected components.  Every component
((X_i,Y_i)) satisfies

\[
                         |X_i|=|Y_i|+1,                          \tag{3.2}
\]

and, with (r_i=\bigcap_{x\in X_i}x),

\[
             \boxed{\{\tau_P(c):c\in Y_i\}=X_i\setminus\{r_i\},} \tag{3.3}
\]

with no repeated trace.  The component and root census is

\[
\begin{array}{c|c|l}
|X_i|/|Y_i|&\#&r_i\\ \hline
169/168&1&1920\\
161/160&3&960,8217,24610\\
160/159&1&8218\\
5/4&2&4213,7504\\
3/2&2&1103,18970\\
2/1&6&2420,2575,2676,9524,17683,19568\\
1/0&6&5801,13616,13620,17738,21641,29776.
\end{array}                                                       \tag{3.4}
\]

The root-rank histogram is

\[
                         (|r|=4,6,7)=(5,14,2).                  \tag{3.5}
\]

The 825 native component cells and their 825 distinct traces give one
simultaneous common-`Q` matching under the final controller (P).

#### Proof

The verifier reconstructs the graph from the frozen middle chronology,
computes an exact maximum matching, takes alternating reachability, and then
takes ordinary connected components of the induced DM graph.  For every
right cell it recomputes the union of its controller interval, verifies that
this target is adjacent to the cell and belongs to the same component, and
checks the bijection (3.3).  The component side sums are

\[
                         \sum_i|X_i|=846,
                         \qquad \sum_i|Y_i|=825.                 \tag{3.6}
\]

Thus no component or right cell is omitted.  Native negative-inertness from
Section 1 gives the simultaneous common-`Q` assertion.  \(\square\)

This proves more than 825 unrelated candidate edges: each component already
has a literal native basis missing exactly its Boolean root.

## 4. The certified duplicate-(462) shrink

The neutral H22 router creates a (24/23) component rooted at (458), and
the final H21 carrier contains 24 relevant cells whose native-trace multiset
is

\[
              (X\setminus\{458\})\uplus\{462\}.                 \tag{4.1}
\]

Thus (462) is duplicated and (458) is the sole missing native root.  The
two copies are

\[
\begin{array}{c|c|c|c}
\text{cell}&\text{depth/start}&\text{controller values}&\tau_P\\ \hline
7216&1/778&(398,206)&462\\
8268&1/1830&(206,398)&462.
\end{array}                                                       \tag{4.2}
\]

Keep cell 8268 pinned to (462), and repin cell 7216 to (458).  Here

\[
             D=462\setminus458=4,                               \tag{4.3}
\]

and the maximal common-`Q` shrink is

\[
                 (398,206)\longmapsto(394,202)                  \tag{4.4}
\]

at positions (778,779), with every other controller letter unchanged.
Both new letters are nonzero.  The verifier checks (2.5) for every central
window and every other selected native pin, then directly recomputes every
final union.

### Theorem 4.1 (849 simultaneous literal pins)

The word obtained by (4.4) realizes simultaneously:

1. all 6,435 prescribed middle windows;
2. all 825 native pins of the final Hall-21 DM shore;
3. 23 native pins for the nonroot targets of the discharged component; and
4. the exceptional pin (7216\mapsto458).

The 849 target labels and 849 physical cells are pairwise distinct.  On the
former 870-target portal shore, the exact remaining literal gap is 21, with
uncovered targets

\[
\begin{split}
\{&960,1103,1920,2420,2575,2676,4213,5801,7504,8217,8218,9524,\\
  &13616,13620,17683,17738,18970,19568,21641,24610,29776\}.
\end{split}                                                       \tag{4.5}
\]

The full word digest is

```text
30fc23fd013386b84faf9bbcbb038dd2ced98df4cb084c0f0181ff41c671feb0.
```

#### Proof

Equations (4.1)--(4.4) put the instance under Corollary 2.2.  The permanent
verifier checks 3,666 positive survival obligations for the deleted mask,
all point nonemptiness conditions, all central equalities, and all 849 pin
equalities.  It also checks the carrier hashes, the exact component roots,
the duplicate-cell identities, and (4.5).  \(\square\)

## 5. Exact Hall-21 to Hall-20 literal rank unit

The frozen route is

\[
\begin{split}
H21&\xrightarrow{\operatorname{RF}(1510,5017,6136)}
      H21^{(1801)}\\
   &\xrightarrow{\operatorname{RF}(885,1393,3668)}H20.
\end{split}                                                       \tag{5.1}
\]

The carriers are

```text
scratch/k15_segment_braid_hall21_zero6.json
scratch/k15_segment_braid_hall21_compressed_dm702.json
scratch/k15_segment_braid_hall20_zero6.json
```

with DM shores and matching ranks

\[
 846/825\longrightarrow702/681\longrightarrow677/657,
 \qquad
 16362\longrightarrow16362\longrightarrow16363.                 \tag{5.2}
\]

The Hall deficiencies are (21,21,20).  The zero set remains

\[
 \{5801,13616,13620,17738,21641,29776\}.                         \tag{5.3}
\]

All three paths are deck-exact, Johnson, depth-three resident, have four
immediate-lower holes, and retain every upper support layer.  Their complete
lower-hole vectors are

\[
 (4,18,9,1,0,0,0)\longrightarrow
 (4,18,11,1,0,0,0)\longrightarrow
 (4,18,11,1,0,0,0).                                             \tag{5.4}
\]

The first braid replaces the (169/168) component rooted at (1920) by a
(25/24) component rooted at (1801).  Its targets are

\[
\begin{split}
X=\{&1801,1803,1805,1807,1833,1835,1837,1865,1867,1869,1897,
1933,1993,\\
&5897,5899,5961,9993,9997,10025,14089,18185,18187,18249,22281,
26377\}.
\end{split}                                                       \tag{5.5}
\]

Its rank histogram is one rank-five, seven rank-six, and seventeen
rank-seven targets.  Its 24 native traces are pairwise distinct and equal
to (X\setminus\{1801\}).  Thus the neutral endpoint is itself a rooted
native-basis circuit.

The improving braid changes the restricted profile bank exactly by

\[
 \{1801,1803,1833,1835\}
 \longmapsto
 \{1801,1833\}\sqcup\{1803,1835\}.                              \tag{5.6}
\]

One ({1801,1833}) cell already survives, so the final component bank has
25 cells.  Their native-trace multiset is

\[
                    (X\setminus\{1801\})\uplus\{1833\}.          \tag{5.7}
\]

The two copies of the duplicated child (1833) are

\[
\begin{array}{c|c|c|c|c}
\text{cell}&\text{depth/start}&\text{controller pair}&
 \text{mandatory}&\text{restricted shore}\\ \hline
9334&1/2896&(1577,809)&1792&\{1801,1833\}\\
9599&1/3161&(1577,809)&1792&\{1801,1833\}.
\end{array}                                                       \tag{5.8}
\]

For either cell, keep the other copy pinned to (1833), repin the chosen
copy to (1801), and delete

\[
                         1833\setminus1801=32.                   \tag{5.9}
\]

The corresponding controller shrink is

\[
                         (1577,809)\longmapsto(1545,777).         \tag{5.10}
\]

Both choices satisfy Theorem 2.1.

### Theorem 5.1 (the H20 rank unit is literal common-`Q`)

For either root cell in (5.8), the word obtained by (5.10) realizes
simultaneously:

1. all 6,435 middle windows;
2. all 657 native pins of the final H20 DM shore;
3. one native pin for each of the 24 nonroot targets of (X); and
4. the exceptional root pin to (1801).

Thus there are exactly

\[
                         657+24+1=682                            \tag{5.11}
\]

distinct target/cell pins on the former 702-target compressed-H21 shore.
The literal gap is exactly 20.  The two valid word digests, according as the
root cell is 9334 or 9599, are

```text
f3c491b298548a7eb650f023086a9c2c0a5d3f9b3844425f780a84cad2f7d1e8
01087907e01a34c0716d9b7e46c2d6e1dc50739c09a017874865033de53b2a11.
```

In particular, the one-unit boundary-rank gain (17\to18) is accompanied
by one genuine literal common-`Q` unit on the active former critical shore.

#### Proof

The native pins impose no negative deletion.  For either choice of root
cell, the only deletion is mask 32 on its two positions.  The verifier checks
all 3,720 instances of the survival condition (2.5), all point nonemptiness,
every central equality, and every one of the 682 selected pin equalities.
Theorem 2.1 therefore gives one literal word.  Distinctness of targets and
cells gives the injection.  The exact graph audit independently gives Hall
rank 16,363 and the cross-shore gap matrix

\[
 \begin{pmatrix}21&20&20\\20&21&20\\20&20&20\end{pmatrix},       \tag{5.12}
\]

so the final deficiency is exactly 20.  \(\square\)

The final (677/657) DM shore itself decomposes into exactly 20 rooted
native-basis components: the Hall-21 root list (3.4) with (1920) removed.
Their 657 native pins are precisely the first family in Theorem 5.1.

The scope remains local to the former compressed critical shore.  A single
word realizing the remaining 15,681 exterior pins of a full 16,363-edge
matching is not proved.

## 6. Permanent verifiers and exact scope

Run

```text
python3 scratch/audit_k15_h21_rooted_native_basis_common_q.py
python3 scratch/audit_k15_h21_h20_rooted_native_common_q.py
```

The verifiers are deterministic and complete only the following finite
operations: graph reconstruction for the frozen carriers, maximum matching,
alternating reachability, connected components, interval unions, and direct
common-`Q` witness checks.  It performs no braid enumeration or optimization
search.  It cross-checks the earlier frozen certificate

```text
scratch/k15_h21_remote_component_common_q_certificate.json
scratch/k15_h21_h20_rooted_native_common_q_certificate.json
```

The H20 verifier and certificate SHA-256 values are

```text
a0d2db6ee712ac309f2f9c94bf07ca2be467e9cd729658ac8ad8ac1413b027e9  scratch/audit_k15_h21_h20_rooted_native_common_q.py
b8adf3d749c72d8ad57e8d7b1756f1ad8316b0a4110023bf61b43e53499affb6  scratch/k15_h21_h20_rooted_native_common_q_certificate.json
```

The proved boundary is exact:

* all 21 current H21 components are rooted native bases;
* duplicating a native child and shrinking one copy to the root is literal if
  and only if (2.4)--(2.5) hold;
* the (462\to458) instance passes and gives 849 simultaneous pins;
* the H21 compression creates a rooted (25/24) basis at root 1801;
* the H20 splitter duplicates child 1833, and either duplicate redirects
  literally to root 1801, giving 682 simultaneous pins and exact Hall 20;
* the same theorem applies to a remaining component once a neutral router
  creates a duplicate child satisfying the survival criterion;
* no full 16,363-pin common compiler or length-6438 universal word is proved
  here.
