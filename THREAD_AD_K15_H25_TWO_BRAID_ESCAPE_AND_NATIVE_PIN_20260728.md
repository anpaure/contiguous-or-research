# Lane AD: exact H25 two-braid escape, seven-block contraction, and native-pin lifting

Date: 2026-07-28

Status: exact theorem and independently audited finite construction.  The
canonical route preserves every lower and upper support layer through depth
seven and improves the one-pin compiler Hall deficiency from 25 to 24.  A
separate branch reaches Hall 23 but loses two depth-three lower colours.  The
critical DM shores of the canonical H25 and H24 carriers admit simultaneous
native-pin realizations in one literal word.  None of these statements gives
Hall zero or a universal length-6438 word.

## 0. Main result and precise boundary

Let (T_0) be the authoritative carrier in
`scratch/k15_segment_braid_hall25.json`.  There is an exact two-step route

\[
T_0
 \xrightarrow{\operatorname{FR}(1512,2458,4103)}T_1
 \xrightarrow{\operatorname{FR}(2664,3491,6201)}T_2
\tag{0.1}
\]

with compiler deficiencies

\[
                         25\longrightarrow25\longrightarrow24.
\tag{0.2}
\]

Every state in (0.1) is a depth-three-resident Hamilton path through the
(W={15\choose8}=6435) middle owners.  Every expected-rank lower support
through depth seven is preserved, with hole vector

\[
                         (4,19,4,1,0,0,0),
\tag{0.3}
\]

and every upper support through depth seven remains complete.  The seven
zero-degree compiler targets remain

\[
2575,5801,13616,13620,17738,21641,29776.
\tag{0.4}
\]

The first move is a nonidentity Hall-neutral portal.  The second move is not
legal on (T_0): it becomes legal only after the first transport.  Therefore
the construction genuinely escapes the exhaustive one-move local minimum;
it is not a disguised commuting pair.

The canonical H24 critical shore has

\[
                         |S|=1168,\qquad |N(S)|=1144.
\tag{0.5}
\]

All 1144 cells in (N(S)) have distinct native traces in (S), and the
single maximal erosion word realizes all 1144 pins simultaneously.  Thus
common-pin coupling adds no defect on this critical shore: its literal
native-pin defect is exactly (1168-1144=24).  This is a shore theorem, not
a common-word lifting of an arbitrary global maximum matching.

The exact conclusions are consequently:

1. the braid distance from H25 to a lower deficiency inside the certified
   resident, upper-safe three-cut move graph is exactly two;
2. a seven-block, six-seam macro can pay one Hall unit while preserving every
   lower and upper support set;
3. the critical H24 DM shore itself has no additional common-pin penalty;
4. Hall zero, the remaining seven zero-degree targets, exterior owner
   compatibility, and a universal length-6438 word remain open.

The phrase “H25 local minimum” must mean **no strictly improving one-move
neighbour**.  It is not a strict local minimum: nonidentity flat portal moves
exist, including the first move in (0.1).

## 1. Exact notation

Identify masks with subsets of ([15]).  Put

\[
r=8,qquad d=3,qquad W={15\choose8}=6435.
\tag{1.1}
\]

A middle carrier is a word

\[
T=(T_0,\ldots,T_{W-1}),\qquad T_i\in{[15]\choose8},
\tag{1.2}
\]

which lists every rank-eight owner once.  It is a Johnson path when
(|T_i\mathbin\triangle T_{i+1}|=2) for every (i).  Its maximal
depth-three erosion is the length-(W+3) word

\[
P_p=\bigcap_{\max(0,p-3)\le i\le\min(p,W-1)}T_i,
\qquad 0\le p<W+3.
\tag{1.3}
\]

Depth-three residence is precisely the condition needed here to keep every
(P_p) nonempty and to have

\[
                         \bigcup_{p=i}^{i+3}P_p=T_i
\qquad(0\le i<W).
\tag{1.4}
\]

For (1\le q\le7), define the consecutive trace multisets

\[
L_q(T)=\left\{\bigcap_{h=0}^{q}T_{i+h}:0\le i<W-q\right\},
\tag{1.5}
\]

\[
U_q(T)=\left\{\bigcup_{h=0}^{q}T_{i+h}:0\le i<W-q\right\}.
\tag{1.6}
\]

Only traces of their expected ranks (8-q) and (8+q), respectively, are
counted in the support ledgers below.

The depth-three lower compiler graph has all nonempty targets of ranks at
most seven on the left and all physical cells

\[
c=(s,e),\qquad e\in\{0,1,2\},\qquad I_c=[s,s+e],
\tag{1.7}
\]

on the right.  An edge means that the target can be imposed on that cell
without violating the exact central row, the nonempty-letter condition, or
the forced controller positions.  The authoritative construction and
auditor use this full edge predicate, not envelope containment alone.

## 2. Oriented block transport theorem

### Theorem 2.1 (exact block transport)

Let (T) be any finite word, cut it at (s) positions into (s+1)
contiguous blocks, and form (T') by permuting the blocks and independently
reversing any of them.  Then:

1. (T') has exactly the same letter multiset as (T).
2. If consecutive letters of (T) are adjacent in an undirected graph,
   then (T') is a path exactly when every new block seam is an edge.
3. For either intersection or union and every (q\ge1), all length-(q+1)
   windows internal to a block transport bijectively.  The signed trace
   change is exactly

   \[
   \{
   \text{new windows crossing new seams}
   \}
   -
   \{
   \text{old windows crossing old cuts}
   \}.
   \tag{2.1}
   \]

   There are at most (sq) windows on each side and hence multiplicity
   (L^1)-change at most (2sq).
4. At depth (d), a depth-(e) compiler cell starting at (a) is determined
   by the middle motif

   \[
                         T[a-2d,\,a+e+d],
   \tag{2.2}
   \]

   with the evident endpoint truncation.  One seam can therefore affect at
   most (e+3d) depth-(e) cells.  Summed over (0\le e<d), this is

   \[
   \sum_{e=0}^{d-1}(e+3d)=\frac{7d^2-d}{2}
   \tag{2.3}
   \]

   cells per seam on either side.

In particular, at (d=3), one seam affects at most

\[
                         9+10+11=30
\tag{2.4}
\]

compiler cells on either side.  A composition of two three-cut braids is an
oriented permutation of at most seven original blocks, hence has at most six
old cuts and six new seams and at most 180 old and 180 new compiler cells
before identical signatures are cancelled.

#### Proof

Statements 1 and 2 are immediate: reversal preserves internal edges because
the ambient graph is undirected, and only the new seams are not transported
old edges.

For statement 3, a window contained in one old block appears in the
corresponding oriented new block.  Reversal changes the order of its letters
but not their intersection or union.  A length-(q+1) window crosses a fixed
seam at only the (q) possible starts immediately preceding it.  This proves
(2.1) and the (sq) bounds.

For statement 4, the maximal controller values used by the cell depend on
middle letters extending (d) positions to the left.  The mandatory-hit
predicate for a cell of length (e+1) also inspects central windows extending
(d) controller positions to the right.  Thus the exact dependency interval
is (2.2).  If a seam lies between (T_{c-1}) and (T_c), it can affect only
starts

\[
                         c-e-d\le a\le c+2d-1,
\tag{2.5}
\]

of which there are (e+3d).  Summing gives (2.3).  Finally, each of the
second braid's three cuts refines at most one of the first braid's four
blocks, so at most seven original atoms and six seams remain.  (square)

### Audit note on the constant

The bound 30 is proof-safe for the **full** compiler signature, including the
mandatory-mask lookback.  A shorter formula based only on the visible cell
interval omits that lookback and is not used.

## 3. Exact Hall-current and contraction theorems

Let (G_j=(L,R_j;E_j)) be successive compiler graphs on the same target set
(L), and let

\[
\delta(G)=\max_{A\subseteq L}(|A|-|N_G(A)|)
\tag{3.1}
\]

be Hall deficiency.  Assume (delta(G_0)=25).  Define

\[
\sigma_0(A)=25-|A|+|N_{G_0}(A)|\ge0,
\tag{3.2}
\]

\[
I_j(A)=|N_{G_j}(A)|-|N_{G_{j-1}}(A)|.
\tag{3.3}
\]

### Theorem 3.1 (telescoping blocker handoff)

For every (t\ge1),

\[
\boxed{
\delta(G_t)=25-
\min_{A\subseteq L}
\left(\sigma_0(A)+\sum_{j=1}^{t}I_j(A)\right).
}
\tag{3.4}
\]

Consequently (delta(G_t)\le24) exactly when

\[
                         \sigma_0(A)+\sum_{j=1}^{t}I_j(A)\ge1
\tag{3.5}
\]

for every target shore (A\subseteq L).

#### Proof

For each (A), telescope (3.3) and rearrange:

\[
|A|-|N_{G_t}(A)|
=25-\sigma_0(A)-\sum_{j=1}^{t}I_j(A).
\tag{3.6}
\]

Taking the maximum over (A) gives (3.4).  Since every term is integral,
(3.5) is equivalent to a one-unit deficiency descent.  (square)

This identity is the exact reason that a neutral first move can be necessary:
it may repair the old critical shore while making a different shore tight,
and the second move can then discharge that replacement blocker.

### Theorem 3.2 (common-signature contraction)

Represent every right cell by its complete target-neighbourhood signature,
retaining multiplicity.  Let two compiler graphs have common signature
multiset (mathscr H) and residual old/new banks (O,N).  In the transversal
matroid (mathcal M) on these cell tokens,

\[
\nu(\mathscr H\sqcup O)
=r_{\mathcal M}(\mathscr H)
 +r_{\mathcal M/\mathscr H}(O),
\tag{3.7}
\]

\[
\nu(\mathscr H\sqcup N)
=r_{\mathcal M}(\mathscr H)
 +r_{\mathcal M/\mathscr H}(N).
\tag{3.8}
\]

Thus the matching gain is exactly

\[
r_{\mathcal M/\mathscr H}(N)
-r_{\mathcal M/\mathscr H}(O).
\tag{3.9}
\]

#### Proof

A set of cell tokens is independent in (mathcal M) exactly when it can be
matched injectively to targets.  Its rank is therefore the maximum matching
size in the induced compiler graph.  The defining contraction identity

\[
r_{\mathcal M/\mathscr H}(X)
=r_{\mathcal M}(X\cup\mathscr H)-r_{\mathcal M}(\mathscr H)
\tag{3.10}
\]

gives (3.7)--(3.9).  Multiplicity causes no issue because equal signatures
remain distinct matroid elements.  (square)

Pure addition of independent packets is governed by submodularity and cannot
explain the present synergy.  Here old packets are removed, new packets are
inserted, and the second legal endpoint pattern exists only after the first
global transport.

## 4. The canonical support-preserving H24 construction

### 4.1 The two moves

The stored carriers are

* (T_0): `scratch/k15_segment_braid_hall25.json`;
* (T_1): `scratch/k15_segment_braid_hall25_portal.json`;
* (T_2): `scratch/k15_segment_braid_hall24.json`.

Their file SHA-256 values are, respectively,

```text
67a84c71f570dbdb8cdad5912b9bed333c4122e9237fed38d56690ad5bd0c473
83678f3fb928402b3e01f3de0553be0f1a60b30a50ee51d7979b8517abd99701
49eb1060ccbe86f056295f0b96fe409f275737b8b759f5b7ca0ee2fa7ca0416e
```

The SHA-256 values of the comma-separated middle sequences are

```text
0ddee21c54e6034e91f3e5b06d6ea2cef3c3a52a55539787d91d3fe2c9287df3
be4674ab73f013d6ad7db2e424d670e291b3382e8aefa7f3b2ab2fc743a620b3
96e7640ebcf8e4c3e372e0e4654b7a7c3934ed5d38be2d13c1371a04eabc49f5
```

The moves in (0.1) materialize these sequences exactly.

### 4.2 Direct seven-block form

Cut (T_0) at

\[
1512,2125,2458,3610,4104,6202
\tag{4.1}
\]

into consecutive blocks (A,B,C,D,E,F,G), of lengths

\[
                         1512,613,333,1152,494,2098,233.
\tag{4.2}
\]

Then the intermediate and final paths are

\[
T_1=A\,D\,E\,\overleftarrow C\,\overleftarrow B\,F\,G,
\tag{4.3}
\]

\[
\boxed{
T_2=A\,D\,\overleftarrow B\,F\,C\,\overleftarrow E\,G.
}
\tag{4.4}
\]

Equivalently, the final oriented original intervals are

\[
\begin{array}{c|c}
\text{interval}&\text{orientation}\\ \hline
[0,1512)&+\\
[2458,3610)&+\\
[1512,2125)&-\\
[4104,6202)&+\\
[2125,2458)&+\\
[3610,4104)&-\\
[6202,6435)&+
\end{array}
\tag{4.5}
\]

and its six seam positions are

\[
                         1512,2664,3277,5375,5708,6202.
\tag{4.6}
\]

The minimum separation among old cuts and among new seams is 333.  Every new
seam has symmetric-difference size two.  Direct materialization of (4.4)
equals (T_2) entry for entry, and the exact residence audit has no short
run.

### 4.3 Exact noncommutativity

If the second move (operatorname{FR}(2664,3491,6201)) is applied directly
to (T_0), its three proposed seam pairs have Hamming distances

\[
                              6,8,6,
\tag{4.7}
\]

so none is a Johnson edge; the resulting order also has seven forbidden
short runs.  The first move transports the needed endpoint states into the
correct order.  Therefore this is a state-dependent portal, not two
independent local collars whose effects can be added in advance.

### 4.4 Complete support and multiplicity ledger

For every state (T_j), (j=0,1,2), the lower hole vector is (0.3), and all
seven upper hole counts are zero.  Moreover the direct old-to-final change
has no lost or gained support at any lower or upper depth.

The trace **multiplicities** are not fixed.  The exact direct multiplicity
(L^1)-changes, by depth (q=1,\ldots,7), are

\[
\|L_q(T_2)-L_q(T_0)\|_1
                         =(0,4,8,14,17,16,8),
\tag{4.8}
\]

\[
\|U_q(T_2)-U_q(T_0)\|_1
                         =(6,9,15,14,16,4,4).
\tag{4.9}
\]

Thus the correct assertion is **all-depth support preservation**, not
all-depth shadow-multiset preservation.

### 4.5 Hall and DM audit

The matching sizes and deficiencies are

\[
\begin{array}{c|ccc}
&T_0&T_1&T_2\\ \hline
\nu&16358&16358&16359\\
\delta&25&25&24.
\end{array}
\tag{4.10}
\]

Let (S_0,S_1,S_2) be the canonical alternating DM left shores of the three
states.  The following matrix has **rows indexed by graphs**
(G_0,G_1,G_2) and **columns indexed by shores** (S_0,S_1,S_2):

\[
\begin{array}{c|ccc}
&S_0&S_1&S_2\\ \hline
G_0&25&24&23\\
G_1&22&25&24\\
G_2&21&24&24.
\end{array}
\tag{4.11}
\]

This orientation matters.  In particular, the old H25 shore improves
(25\to22\to21); it does not remain the active blocker.  The first move
creates the replacement shore (S_1) with gap 25.  The second lowers that
gap to 24, while (S_2) also has final gap 24.

In the notation of Theorem 3.1, the three displayed shore ledgers are

\[
\begin{array}{c|ccc|c}
&\sigma_0&I_1&I_2&\sigma_0+I_1+I_2\\ \hline
S_0&0&3&1&4\\
S_1&1&-1&1&1\\
S_2&2&-1&0&1.
\end{array}
\tag{4.12}
\]

This is the exact blocker handoff.

For the single common-signature core shared by all three states,

\[
|\mathscr H|=19253,qquad r(\mathscr H)=16323,
\tag{4.13}
\]

and every state has a residual bank of 58 cells.  The contracted ranks are

\[
                         35\longrightarrow35\longrightarrow36.
\tag{4.14}
\]

Hence the direct old/final comparison gains exactly one matching unit.  The
two pairwise comparisons use different cores:

\[
\begin{array}{c|ccc}
\text{transition}&|\mathscr H|&r(\mathscr H)&
  \text{contracted ranks}\\ \hline
T_0\to T_1&19293&16343&15\to15\\
T_1\to T_2&19271&16338&20\to21.
\end{array}
\tag{4.15}
\]

The figures (15\to15) and (20\to21) must not be treated as two terms in
one additive contraction ledger; (4.14) is the valid common-core statement.

Target 6308 has degree 14 in all three compiler graphs and plays no role in
this descent.

## 5. Exact common-word and native-shore theorem

The Hall graph alone does not guarantee that selected pins can be installed
in one physical word.  The exact compatibility criterion is nevertheless
simple once the middle skeleton is fixed.

Let (P) be the maximal erosion word of a resident carrier (T).  Select
pins ((X_c,I_c)), where (X_c) is the target assigned to cell interval
(I_c).  Define the coordinatewise maximal permitted word

\[
\boxed{
K_p=P_p\cap\bigcap_{c:\,p\in I_c}X_c.
}
\tag{5.1}

An empty intersection of pin labels in (5.1) means no additional
restriction.

### Theorem 5.1 (fixed-skeleton common-word criterion)

There is a nonzero word (A) such that

\[
\bigcup_{p=i}^{i+3}A_p=T_i
\qquad(0\le i<W)
\tag{5.2}
\]

and

\[
\bigcup_{p\in I_c}A_p=X_c
\qquad\text{for every selected pin }c
\tag{5.3}
\]

if and only if all three conditions hold:

1. (K_p\ne\varnothing) for every position (p);
2. for every (i) and every (x\in T_i), some
   (p\in[i,i+3]) has (x\in K_p);
3. for every selected (c) and every (x\in X_c), some
   (p\in I_c) has (x\in K_p).

When they hold, (A=K) is the coordinatewise maximal common word.

#### Proof

Any word satisfying (5.2) is pointwise contained in the maximal erosion:
(A_p\subseteq P_p).  Equation (5.3) also forces
(A_p\subseteq X_c) whenever (p\in I_c).  Hence every feasible word obeys
(A_p\subseteq K_p).  Nonemptiness and the two positive-hit conditions are
therefore necessary.

Conversely take (A=K).  Since (K_p\subseteq P_p), each central union in
(5.2) is contained in (T_i); condition 2 supplies every element of (T_i).
Similarly, (K_p\subseteq X_c) on (I_c), and condition 3 supplies every
element of (X_c).  Condition 1 makes the word nonzero.  (square)

For a cell (c), define its native trace

\[
                         E_c=\bigcup_{p\in I_c}P_p.
\tag{5.4}
\]

### Corollary 5.2 (native-shore lifting)

Let (S) be a target shore in the compiler graph and put (C=N(S)).  If

1. (E_c\in S) for every (c\in C), and
2. the map (c\mapsto E_c) is injective on (C),

then

\[
                         \{(E_c,c):c\in C\}
\tag{5.5}
\]

is a matching realized simultaneously by the single word (A=P).  The
maximum number of distinct targets of (S) assignable to distinct cells in
one common word is exactly (|C|), and the common-pin defect on this shore is
exactly

\[
                         |S|-|C|.
\tag{5.6}
\]

#### Proof

Each pair in (5.5) is a native compiler edge.  Injectivity makes the pairs a
matching.  A native pin imposes no deletion, because
(P_p\subseteq E_c) for every (p\in I_c); this remains true when native
intervals overlap.  Thus (5.1) gives (K=P), and Theorem 5.1 realizes every
pin simultaneously.  No matching from (S) can use more than its complete
neighbourhood (C=N(S)), proving optimality.  (square)

### 5.3 Exact H25 and canonical H24 instantiations

Independent reconstruction gives

\[
\begin{array}{c|rrrr|rrr}
\text{carrier}&|S|&|C|&|S|-|C|&\text{native pins}&
\#r5&\#r6&\#r7\\ \hline
H25&1320&1295&25&1295&72&344&879\\
H24&1168&1144&24&1144&63&302&779.
\end{array}
\tag{5.7}
\]

For H25 the 25 unmatched native-shore targets are

\[
\begin{aligned}
\{&89,449,960,1103,1920,2420,2575,2676,4213,4877,5801,7504,\\
&8217,8218,9524,13616,13620,17683,17738,18970,19568,20516,\\
&21641,24610,29776\}.
\end{aligned}
\tag{5.8}

Their rank profile is (4^8,6^{15},7^2).  For canonical H24 the same list
with 89 removed is the 24-element complement, with profile
(4^7,6^{15},7^2).

This proves an exact common-owner statement at the active obstruction: the
critical shore defect really falls from 25 to 24 with no hidden native-pin
penalty.  It does not show that an arbitrary 16359-edge maximum matching of
the entire H24 graph has a common word.  Indeed, across all 19311 short cells,
the H24 maximal word has only 14416 distinct lower traces and misses 1967
lower targets, with missing-rank census

\[
15,105,455,1365,4,19,4
\quad\text{in ranks }1,2,3,4,5,6,7.
\tag{5.9}
\]

Thus Corollary 5.2 is deliberately shore-local.

## 6. Separate zero-degree escape and a literal exceptional pin

There is a second nonmonotone two-braid route

\[
H25
\xrightarrow{\operatorname{FR}(2396,4635,5353)}H26_z
\xrightarrow{\operatorname{FF}(2125,4140,6201)}H25_z,
\tag{6.1}
\]

with score sequence

\[
                         (25,7)\to(26,6)\to(25,6),
\tag{6.2}
\]

where the second coordinate counts degree-zero targets.  It removes 2575
from the zero-degree set, leaving the other six targets in (0.4).  Every
upper support remains complete and the immediate-lower hole count remains
four.  This branch is not all-lower-support preserving: it loses target 8905
at depth two and targets 713 and 8777 at depth three, so its final lower hole
vector is

\[
                         (4,20,6,1,0,0,0).
\tag{6.3}

The appearance of target 2575 is nevertheless physically real, not merely
an abstract Hall edge.

### Proposition 6.1 (literal target-2575 shore replacement)

For the final carrier (H25_z), its canonical DM shore has

\[
                         |S|=1169,\qquad |C|=1144.
\tag{6.4}
\]

The native traces on (C) are distinct.  Cell

\[
c_*=18054,qquad I_{c_*}=[5179,5181]
\tag{6.5}
\]

has native trace 2607, and 2575 has this cell as its unique candidate.
Replacing the native pair ((2607,c_*)) by ((2575,c_*)) keeps a
1144-edge matching saturating (C) and is realized simultaneously with all
other selected native pins by one nonzero length-6438 word.

#### Proof

In the maximal erosion word,

\[
(P_{5179},P_{5180},P_{5181})=(2601,2602,2604).
\tag{6.6}
\]

The only deletion needed is bit value (2^5=32).  Put

\[
(A_{5179},A_{5180},A_{5181})=(2569,2570,2572)
\tag{6.7}
\]

and leave every other (A_p=P_p).  The union in (6.7) is 2575.  The six
central windows meeting the changed collar retain bit 32, respectively, at

\[
                         5178,5178,5178,5182,5182,5182.
\tag{6.8}
\]

Every other coordinate is unchanged, so all central equalities survive.
All letters in (6.7) are nonempty.  No other selected DM-right native cell
meets the modified collar, so all its native pins remain literal.  Finally,
2575 is not another selected native trace; the replacement is target
injective and simply swaps the unmatched shore target 2575 for 2607.
(square)

This proposition does not reduce deficiency 25, realize a global maximum
matching, or preserve exterior frozen pins.  “Six zero targets” refers to
zero degree in the maximal-controller compiler graph, not to the number of
masks absent from this partial compiled word.

## 7. Authoritative Hall-23 and Hall-22 continuation

The canonical H24 carrier continues by

\[
H24\xrightarrow{\operatorname{FF}(212,3732,4717)}H24'
\xrightarrow{\operatorname{FF}(210,1501,4867)}H23.
\tag{7.1}
\]

The second braid discharges the complete \(161/160\) DM component rooted at
20516.  It preserves residence, every upper support, and four immediate-lower
holes, but loses lower-depth-three targets 17445 and 28677.  The resulting
H23 lower hole vector is

\[
                         (4,19,6,1,0,0,0).
\tag{7.2}
\]

Its canonical shore is \(1007/984\), and all 984 right-shore cells have
distinct native traces in one common maximal erosion word.

The frontier then continues

\[
H23\xrightarrow{\operatorname{RF}(3799,4497,6039)}H23'
\xrightarrow{\operatorname{FR}(740,4051,6137)}H22.
\tag{7.3}
\]

Here the neutral router acts in the unrelated component rooted at 24610,
while the second braid remotely splits the sole shore \(\{4877,4909\}\)
into native singleton shores.  H22 has lower hole vector
\((4,18,6,1,0,0,0)\), all upper supports, and a \(1005/983\) critical shore
with 983 simultaneous native pins.  The exact router/splitter theorem and
the remaining groupoid-transitivity gate are in
THREAD_AD_K15_H22_NEUTRAL_ROUTER_CIRCUIT_SPLITTER_20260728.md.

## 8. Independent audit and artifacts

The decisive construction was checked in three logically separate ways.

1. `scratch/audit_k15_segment_braid_descent.py` reconstructs each stored
   move, Johnson legality, residence, every lower/upper support layer, the
   full compiler graph, exact maximum matching, canonical DM shore, and each
   pairwise contraction.
2. `scratch/audit_k15_h25_portal_escape_direct.py` independently materializes
   the seven-block macro, checks all six direct seams, verifies the full
   boundary-only trace ledger, computes the three-way common core, and proves
   the direct (35\to36) contracted-rank gain.  It also checks the illegal
   (6,8,6) seam distances of the second move on the unmodified H25 path.
3. `scratch/audit_k15_h25_native_dm_pins.py` and
   `scratch/audit_k15_h25_zero6_exceptional_pin.py` reconstruct the native
   shore matchings and audit every central and selected pin equality in the
   literal words.

Short reproduction commands are:

```sh
python3 scratch/audit_k15_segment_braid_descent.py \
  --base scratch/k15_segment_braid_hall25.json \
  --step scratch/k15_segment_braid_hall25_portal.json \
  --step scratch/k15_segment_braid_hall24.json

python3 scratch/audit_k15_h25_portal_escape_direct.py

python3 scratch/audit_k15_h25_native_dm_pins.py \
  scratch/k15_segment_braid_hall25.json
python3 scratch/audit_k15_h25_native_dm_pins.py \
  scratch/k15_segment_braid_hall24.json

python3 scratch/audit_k15_h25_zero6_exceptional_pin.py
```

The principal compact certificates are:

* `scratch/k15_segment_braid_hall24_portal_audit.json`, SHA-256
  `0c381981f90e7c7e251228d75593165534bc60a9b8f0bbae83fef247e1bbcdf1`;
* `scratch/k15_h24_portal_native_dm_pin_certificate.json`, SHA-256
  `73b556822577315caf70d06a6cc7b34cf41f5287fe03fcd47ad03f32ad06fda5`;
* `scratch/k15_h25_zero6_exceptional_pin_certificate.json`, SHA-256
  `89c6d006f1f5abc92f234ecd095fae8460412bd206b458b769cf1e8d29c634ae`;
* `scratch/k15_segment_braid_h23_lookahead_audit.json`, SHA-256
  `07b330095040bbf7d4a573ec8c43cb7dbfe8fa877010e0ec59486e4e5af65fba`;
* `scratch/k15_h23_lookahead_native_dm_pin_certificate.json`, SHA-256
  `b2509e2ca2a4bb47c3b8bf8350ed8d70bda3f1fab962b997755d79b012e7f378`.

No theorem here depends on target 6308, on ordinary reachability in place of
matching, or on separate pin realizations in place of one common literal
word.  The remaining finite gate is to combine Hall descent, reduction of the
degree-zero floor, preservation or deliberate repair of every required lower
support, and a common-word matching outside the native critical shore.
