# K16 gap one: chart-intersection elimination and anchor pruning

Date: 2026-07-30  
Lane: AD  
Status: proved exact reduction and source-relative pruning; no profile SAT or
UNSAT verdict and no length-12,873 word are claimed

## 1. Frozen scope

The input is the authenticated universal word

~~~text
answers/k16_upper12874.word
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e
~~~

and its fixed-gap architecture

\[
             A_5\mid G_1\mid B_9\mid G_2\mid C_4.
\]

The two fixed gaps have ORs 0x7fff and 0xffff. Let \(F\) be the 65,478
targets already witnessed wholly in one of these gaps and let

\[
 R=\{1,\ldots,65535\}\setminus F,\qquad |R|=57.
\]

For any one of the three shortened profiles

\[
              (4,9,4),\qquad(5,8,4),\qquad(5,9,3),       \tag{1.1}
\]

an \(R\)-witness meets exactly one variable collar. Its variable part is a
nonempty interval \(I\) in that collar. If \(I\) reaches a collar boundary,
it may be extended by a suffix or prefix of the adjacent fixed gap.

For \(T\in R\) and such a local variable interval \(I\), let \(b_T(I)\) be
the union of the largest left suffix OR contained in \(T\) and the largest
right prefix OR contained in \(T\), using zero on a side that \(I\) does not
reach. The suffix and prefix OR families are chains, so both maxima are
unique.

## 2. Audit of maximal-context and closure normalization

### Lemma 2.1 (literal maximal-context equivalence)

For a fixed collar assignment \(z\), target \(T\), and variable interval
\(I\), some allowed literal interval whose variable part is exactly \(I\)
has OR \(T\) if and only if

\[
                     b_T(I)\vee\bigvee_{p\in I}z_p=T.    \tag{2.1}
\]

#### Proof

Write \(V=\bigvee_{p\in I}z_p\). Every physical context compatible with an
exact \(T\)-witness is \(c=\ell\vee r\subseteq T\), where the two chain
elements obey
\(\ell\subseteq\ell_T\) and \(r\subseteq r_T\). Hence
\(c\subseteq b_T(I)\subseteq T\). If \(c\vee V=T\), then \(V\subseteq T\)
and

\[
 T=c\vee V\subseteq b_T(I)\vee V\subseteq T.
\]

Conversely the two maximal chain elements are simultaneously realized by a
literal suffix, the variable interval, and a literal prefix. Thus (2.1)
is sufficient as well. \(\square\)

This lemma preserves literal chronology and target occurrence. It need not
preserve the endpoints of a particular smaller-context witness. Therefore
it is exact for the present unpinned universality problem, but it cannot be
imported without modification into a model that pins witness endpoints.

For a nonzero mask \(v\), put

\[
 \mathcal S(v)=\{T\in R:v\subseteq T\},\qquad
 \operatorname{cl}(v)=\bigcap_{T\in\mathcal S(v)}T
\]

when the first set is nonempty, and let

\[
 D=\{v\ne0:\mathcal S(v)\ne\varnothing,\ 
                    \operatorname{cl}(v)=v\}.
\]

The frozen audit gives \(|D|=245\).

### Lemma 2.2 (every nonempty active intersection is closed)

If \(\varnothing\ne\mathcal Q\subseteq R\) and

\[
                         v=\bigcap_{T\in\mathcal Q}T\ne0,
\]

then \(v\in D\).

#### Proof

Every member of \(\mathcal Q\) contains \(v\), so
\(\mathcal Q\subseteq\mathcal S(v)\). On the one hand, every member of
\(\mathcal S(v)\) contains \(v\), giving
\(v\subseteq\bigcap\mathcal S(v)\). On the other hand,

\[
 \bigcap\mathcal S(v)\subseteq\bigcap\mathcal Q=v.
\]

Thus \(\operatorname{cl}(v)=v\). \(\square\)

The cellwise closure argument is consequently sound: enlarging a live value
to its closure cannot add a bit outside any \(R\)-target whose witness uses
that cell, and removes no bit. A value contained in no member of \(R\) lies
in no exact \(R\)-witness at all. Targets in \(F\) keep their fixed-gap
witnesses. This preserves every old \(R\)-witness, but it is not a claim
that the complete interval-label multiset or Hamming distance is preserved.

## 3. Exact elimination of all collar values

A chart selection chooses, for each \(T\in R\), one local interval \(I_T\)
in one of the three collars. Its fixed context is \(b_T(I_T)\). For an
editable cell \(p\), define

\[
 \mathcal A_p=\{T\in R:p\in I_T\},\qquad
 K_p=\bigcap_{T\in\mathcal A_p}T                         \tag{3.1}
\]

when \(\mathcal A_p\ne\varnothing\).

### Theorem 3.1 (chart-intersection elimination)

For any profile in (1.1), the exact 17-cell collar CSP is feasible if and
only if there is a chart selection satisfying

\[
 \mathcal A_p\ne\varnothing\quad\Longrightarrow\quad K_p\ne0           \tag{3.2}
\]

at every editable cell, and

\[
       T\setminus b_T(I_T)\subseteq\bigcup_{p\in I_T}K_p
                         \qquad(T\in R).                 \tag{3.3}
\]

Whenever (3.2)--(3.3) hold, the canonical assignment

\[
                           z_p=K_p                       \tag{3.4}
\]

on used cells, with an arbitrary member of \(D\) on unused cells, is a
literal universal word in that profile. In particular all used values in
(3.4) automatically lie in the 245-value closure domain.

#### Proof: necessity

Start from a feasible collar word and choose one literal witness for every
\(T\in R\). Replace its fixed context by the maximal one using Lemma 2.1,
without changing its variable interval \(I_T\). If \(p\in I_T\), exactness
of this witness gives \(z_p\subseteq T\). Thus for every used cell

\[
                         0\ne z_p\subseteq K_p,
\]

which proves (3.2). Every bit of \(T\setminus b_T(I_T)\) must occur in at
least one \(z_p\), \(p\in I_T\); that value is contained in \(K_p\). This
proves (3.3).

#### Proof: sufficiency

Assign (3.4). It is nonzero by (3.2), and Lemma 2.2 puts it in \(D\). If
\(p\in I_T\), then \(T\in\mathcal A_p\), so \(K_p\subseteq T\). Therefore
the maximal context and all variable values in the selected interval are
subsets of \(T\). Condition (3.3) supplies every bit not already in the
context, whence

\[
             b_T(I_T)\vee\bigvee_{p\in I_T}K_p=T.
\]

Lemma 2.1 turns this equality into an actual literal interval. Every target
in \(F\) retains a fixed-gap witness. Hence the whole word is universal.
\(\square\)

The theorem is an exact projection, not a necessary-only intersection
relaxation. It removes the 245-valued cell variables entirely: only one
local interval chart per repair target remains.

### Corollary 3.2 (private-bit form)

Condition (3.3) is equivalent to

\[
 I_T\setminus
 \bigcup_{\substack{U\in R\\q\notin U}} I_U\ne\varnothing
 \quad\text{for every }q\in T\setminus b_T(I_T).        \tag{3.5}
\]

Here intervals in different collars are disjoint by definition.
This formula uses the one-chart-per-target selection of Theorem 3.1. If an
ALO-only encoding sets several chart selectors for one target to true, the
union is instead taken over every true \(q\)-omitting chart occurrence.

#### Proof

For \(p\in I_T\), the bit \(q\) belongs to \(K_p\) exactly when every active
target at \(p\) contains \(q\), equivalently when no selected interval of a
\(q\)-omitting target covers \(p\). \(\square\)

Thus every bit not supplied by the fixed context needs a durable point of
its selected interval. The following cuts are immediate and exact:

1. if target intervals all cover one cell and their target intersection is
   empty, those chart choices are incompatible;
2. an empty-intersection conflict has a subconflict of size at most 16,
   by choosing one target omitting each coordinate;
3. for every selected \((T,I)\) and every \(q\in T\setminus b_T(I)\), at
   least one point of \(I\) must avoid all selected \(q\)-omitting charts.

Because cells in different collars never interact in (3.1), fixing the
partition of \(R\) among the three collars decomposes the remaining chart
test into three independent interval systems. The only global operation is
choosing that target partition.

## 4. The forced 0x8000 anchor

Let \(H=\mathtt{0x8000}\). It is one of the 57 repair targets. At the four
relevant fixed-gap boundaries, the adjacent endpoint letters are

~~~text
G1 first  0x1009        G1 last  0x0600
G2 first  0x9620        G2 last  0x8c44.
~~~

Every nonempty compatible boundary context therefore has a low bit and is
not contained in \(H\). Consequently

\[
                             b_H(I)=0.                  \tag{4.1}
\]

### Corollary 4.1 (pure anchor and low-target separation)

Every feasible profile has a collar cell equal to 0x8000. One may choose
the \(H\)-chart to be the singleton consisting of that cell. No selected
chart for any target omitting bit 0x8000 can contain the anchor cell.

#### Proof

An \(H\)-witness has context zero by (4.1). Every nonzero cell in it is a
subset of the singleton-bit mask \(H\), hence equals \(H\). Any one of
those cells is itself a singleton witness. A target omitting the high bit
cannot have an exact witness containing that cell. Equivalently, the two
targets would have empty intersection at the anchor, violating (3.2).
\(\square\)

All 18 low repair targets omit the anchor bit. Thus an exact chart model may
branch on only 17 possible anchor locations, and all their chosen intervals
must avoid that location. This is a chronology constraint, not merely the
statement that some selected mask contains the high bit.

## 5. Exact blocker CNF without closure-domain clauses

For a fixed profile, introduce a selector \(x_{T,I}\) for each target and
local interval and impose one at-least-one row per target. No at-most-one row
is needed: selecting extra charts only adds constraints, while every
feasible word can select exactly one.

For each editable cell \(p\) and coordinate \(q\), introduce a blocker bit
\(B_{p,q}\). For every selector whose interval contains \(p\) and whose
target omits \(q\), impose

\[
                         x_{T,I}\Longrightarrow B_{p,q}.             \tag{5.1}
\]

The blocker is allowed to overstate the true obstruction; this cannot create
a false positive because it is used only negatively. Impose

\[
 \bigvee_{q=0}^{15}\neg B_{p,q}                                      \tag{5.2}
\]

at every cell, and, for every selector and every required bit,

\[
 x_{T,I}\Longrightarrow
       \bigvee_{p\in I}\neg B_{p,q}
       \qquad(q\in T\setminus b_T(I)).                               \tag{5.3}
\]

### Proposition 5.1 (blocker-CNF equivalence)

Equations (5.1)--(5.3) plus the 57 target rows are satisfiable if and only if
the corresponding profile contains a universal word.

#### Proof

Given a chart selection satisfying Theorem 3.1, set \(B_{p,q}=1\) exactly
when some selected \(q\)-omitting target interval contains \(p\). Then (5.2)
is (3.2), and (5.3) is (3.5).

Conversely, take all charts whose selectors are true. At a point with
\(B_{p,q}=0\), implication (5.1) guarantees that every selected target using
that point contains \(q\). Thus (5.2) gives a nonempty active intersection
at every used cell, while (5.3) gives every required durable point. Use all
true charts in the active intersections. Their canonical intersections give
a literal word by the proof of Theorem 3.1. The decoder must reconstruct
these intersections from the selected target charts; the possibly
overstated \(B\)-bits are not cell values and are not used in decoding.
\(\square\)

The exact dimensions, using the maximal-context ledgers already audited in
the three-profile compression, are:

| profile | selectors | blocker bits | variables | clauses |
|---|---:|---:|---:|---:|
| (4,9,4) | 3,705 | 272 | 3,977 | 120,206 |
| (5,8,4) | 3,477 | 272 | 3,749 | 104,916 |
| (5,9,3) | 3,762 | 272 | 4,034 | 122,849 |

The clause totals are respectively

\[
 91840+28292+57+17,\quad
 78400+26442+57+17,\quad
 94080+28695+57+17.
\]

This replaces the cell-bit/nonzero semantics by blocker semantics and needs
none of the 4,369 copied closure-domain clauses. The counts happen to equal
the earlier unrestricted-bit base CNFs; the gain is against the
closure-constrained versions and in the chart-only decoding/cut structure,
not a claim of fewer variables than every prior direct encoding.

## 6. Exact arbitrary adjacent-collapse criterion

The same elimination gives a closed-form test for replacing two adjacent
letters by one arbitrary nonzero letter. At boundary \(p\), let
\(\mathcal C_p\) be the targets not witnessed wholly to the left of the pair
or wholly to its right. Let

\[
 \mathcal B_p=\{a\vee b:a\text{ is a left suffix OR or }0,\ 
                         b\text{ is a right prefix OR or }0\},
\]

and put \(K_p=\bigcap_{T\in\mathcal C_p}T\), with the full mask as the
intersection of an empty family.

### Theorem 6.1 (canonical one-cell fusion test)

There is a nonzero replacement \(y\) making the collapsed word universal if
and only if \(K_p\ne0\) and, for every \(T\in\mathcal C_p\), there is an
\(s_T\in\mathcal B_p\) such that

\[
                         T\setminus K_p\subseteq s_T\subseteq T.       \tag{6.1}
\]

Given such choices, put

\[
                         y_0=\bigvee_{T\in\mathcal C_p}(T\setminus s_T).
                                                                        \tag{6.2}
\]

If \(y_0\ne0\), then \(y=y_0\) works. If \(y_0=0\), any one-bit nonzero
submask of \(K_p\) works.

#### Proof

If \(s\vee y=T\), then \(s\subseteq T\), \(y\subseteq T\), and hence
\(y\subseteq K_p\). Every bit of \(T\setminus K_p\) must therefore occur
in \(s\), proving necessity.

Conversely, (6.1) implies \(T\setminus s_T\subseteq K_p\), so (6.2) is a
submask of \(K_p\). It contains every bit missing from every chosen side
base. Therefore \(s_T\vee y_0=T\) for every target. If \(y_0=0\), then all
\(s_T=T\), and adding any common bit from nonzero \(K_p\) changes none of
them. Each side base is a literal suffix-prefix choice around the collapsed
cell, so these are literal interval witnesses. \(\square\)

Thus a complete arbitrary-collapse census of the 12,873 boundaries of the
frozen upper word needs no enumeration of 65,535 replacement values. For
each boundary it only forms the critical intersection and checks the at
most \(17^2=289\) side bases against each critical target. This remains a
source-relative finite census; no result of that census is asserted here.

## 7. Symmetry and scope boundary

Reversal exchanges the first and third collars but also exchanges the two
fixed gaps. Their OR ranks are 15 and 16. Every Boolean-lattice alphabet
automorphism is a coordinate permutation and preserves rank, so no
reversal-plus-coordinate relabelling maps this frozen ordered architecture
to itself. In particular (5,8,4) is not identified with a missing (4,8,5)
branch, and (5,8,4) and (5,9,3) cannot be quotiented by this obvious
symmetry. The three profiles in (1.1) remain genuinely separate finite
gates.

Theorems 3.1 and 6.1 preserve integrality and literal contiguous-OR
chronology. They prove neither feasibility nor infeasibility of a shortened
profile, and they say nothing about changing a fixed-gap letter, moving a
separator, or an unrelated length-12,873 word.

## 8. Independent complete arbitrary-collapse replay

Theorem 6.1 has now been applied independently at all 12,873 adjacent
boundaries of the authenticated word.

### Theorem 8.1 (frozen-word arbitrary adjacent-collapse no-go)

No word obtained from the authenticated length-12,874 word by replacing one
adjacent pair by one arbitrary nonzero 16-bit mask is universal.

Two independent implementations agree exactly on:

* 12,873 tested boundaries and zero feasible boundaries;
* 39 failures with zero critical-target intersection;
* 12,834 failures of the side-base condition (6.1);
* maximum critical-family size 25;
* maximum distinct side-base count 54; and
* the full critical-family-size histogram.

The first implementation is

~~~text
scratch/audit_ad_k16_upper12874_arbitrary_adjacent_collapse_20260730.py
SHA-256 3e301c901df6112578c879f5af86dfb62eb6fb6b7619588382c1b750c7f72da8

scratch/k16_upper12874_arbitrary_adjacent_collapse_20260730.audit.json
SHA-256 f38f4a7ce7ad1dd0f518850b0d241a60e5cb5606826c01b2a51b72ed1c94d180
payload SHA-256 8b5c1acb8f84a822a1f88b549fe78c777bf38527eb9e5e9c11ea412cdfed1e47
~~~

The independent C++ occurrence-span sweep is

~~~text
scratch/audit_ad_k16_arbitrary_adjacent_collapse_canonical_20260730.cpp
SHA-256 c758061f80ec74b066726aa870ea9d91d7fe2191eae20b2add1e5284fb53fb0f

scratch/ad_k16_arbitrary_adjacent_collapse_canonical_20260730.audit.json
SHA-256 ee8d65faffeee1891bcf32ac1db1edc7f4a931d243eb4649a4023ec0b00f0402

scratch/ad_k16_arbitrary_adjacent_collapse_canonical_20260730.log
SHA-256 677c99793e3161ff71de61547bcd87173319d427d33b278db61e40ac726b8dc6
~~~

It was compiled and run on one H100 CPU core after pinning the input SHA,
used 6,144 KiB maximum RSS, and finished in 0.06 seconds. Its critical
boundary interval identity is

\[
 \mathcal C_p=\{T:\ \sigma_T-1\le p\le\epsilon_T\},
\]

where \(\epsilon_T\) is the minimum end of a \(T\)-interval and
\(\sigma_T\) is the maximum start of a \(T\)-interval. This identity follows
because an interval avoiding the pair \(\{p,p+1\}\) must lie wholly before
it or wholly after it. The implementation then applies (6.1) literally.

Theorem 8.1 is strictly source-relative. It closes every arbitrary adjacent
two-to-one collapse of this frozen upper certificate, not nonadjacent
delete-plus-edit moves, larger collars, fixed-gap rethreading, or arbitrary
length-12,873 words.
